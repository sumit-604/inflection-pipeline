# STAGE 2 — NOTES TO FINANCIAL STATEMENTS, PASS 1 OF 3
Company: TruAlt Bioenergy Ltd (TRUALT) | Run: trualt-2026-09-18 | Model: claude-sonnet-5
Source: Annual_Report_2026.pdf (FY2025-26, 359 pp, ₹ lakh), text route
runs/trualt-2026-09-18/inputs/annual-report/Annual_Report_2026.txt
Supplementary (comparison only): TRUALT-Prospectus-01OCT2025.txt (restated FY23-25)

Structure of the AR: CONSOLIDATED financial statements and notes (Notes 1-62,
pp.251-296) precede STANDALONE financial statements and notes (Notes 1-62,
pp.297-359). Both note sets read in full for this pass. All amounts ₹ lakh
unless stated; ₹ Cr equivalents given in parentheses for load-bearing figures
(1 Cr = 100 lakh).

Company memory check before extraction (per task instructions):
- Fact 2 (inventory build, CFO, IPO proceeds use): CONFIRMED and deepened below.
- Fact 3 (Nirani-group feedstock RPT, Unit 5 sale, pledge): CONFIRMED and
  deepened below. Unit 5 (Badami) slump sale to Onkar Agro Sugars & Energy
  (04-Aug-2026) is NOT in this AR (FY26 AR signed 22-May-2026, board report
  dated before the sale); NOT FOUND IN DOCUMENT, expected — post balance-sheet
  and post-signing event, outside this AR's subsequent-events window.

---

## 1. ACCOUNTING POLICIES & CHANGES

- Ind AS 21 (forex), Ind AS 1 (current/non-current with covenants), Ind AS 7
  and Ind AS 107 (supplier finance disclosure) amendments applicable FY26:
  company states "no significant impact" for all three (Note 4, consolidated
  p.262 / standalone p.326). 🟢 Clean, standard boilerplate.
- Depreciation useful lives: Plant & machinery 10-25 years (wide band),
  Building-Factory 30-40 years, Building-Others 30-50 (consol.) /40-50
  (standalone, note the consolidated and standalone tables disagree on
  Building-Others: 30-50 in consolidated Note 2.2 table vs 40-50 in
  standalone Note 2.2 table — Note 2.2, consolidated p.256 vs standalone
  p.320) 🟡 Watch: minor internal inconsistency between the two useful-life
  tables for the same asset class, immaterial in isolation but a disclosure
  hygiene miss. Company states useful lives differ from Schedule II based on
  "technical expert assessment," standard disclosure, no further support
  given (Note 2.2(g), both sets).
- Capitalisation of borrowing cost: three grain-conversion units capitalised
  specific borrowing costs at 11.67% capitalisation rate — Unit 1 (550 KLPD,
  commissioned 01-Nov-2025) ₹849.03 lakh, Unit 2 (450 KLPD, commissioned
  28-Feb-2026) ₹883.80 lakh, Unit 4 (300 KLPD, commissioned 26-Jan-2026,
  funded from IPO) (Note 5, consolidated p.264 / standalone p.327). 🟢 Clean,
  disclosed and quantified — directly verifies the multi-feed conversion
  capex is real and dated.
- Goodwill impairment test: goodwill ₹5,159.38 lakh (consol.) / ₹4,786.18
  lakh (standalone, excludes TruAlt Gas goodwill) tested annually, value in
  use, discount rate 10.46%, terminal growth 3%, 5-year budget. No
  impairment (Note 5/6, consol. p.264-265 / standalone p.328). 🟡 Watch: a
  single discount rate and terminal growth figure disclosed with no
  sensitivity table — an investor cannot stress-test the headroom.
- Customer relationship intangible: ₹11,540.40 lakh gross (consol.),
  amortised over 10-25 years (consol. policy table) vs 10 years flat
  (standalone policy table) (Note 2.2(h)) — 🟡 Watch: same
  consolidated-vs-standalone useful-life inconsistency pattern as buildings
  above.
- Gratuity: unfunded defined benefit plan (Note 38(B) consol. / 37(B)
  standalone). 🟡 Watch: unfunded means the liability sits wholly on
  balance sheet with no plan assets; standard for many Indian mid-caps but
  worth noting as a governance/cash-planning item. Magnitude small
  (₹310.70 lakh consol. / ₹233.01 lakh standalone obligation at FY26-end),
  not material to the thesis.
- ECL / impairment on trade receivables: "no loss allowance computed for
  the year" because customers are public-sector OMCs (Note 42(C) consol. /
  41(C) standalone). 🟢 Clean given the customer base, but the ECL matrix
  itself is not shown (no ageing-bucket-wise provisioning table) —
  NOT FOUND IN DOCUMENT: quantified ECL rate assumptions.
- Revenue recognition — Performance Linked Incentive (PLI): company
  recognises 1.75% of eligible turnover as PLI revenue under "other
  operating revenue" for FY25 and FY26 even though "for FY 2024-25 and FY
  2025-26, the Company will submit the claim application within the due
  date" — i.e., revenue is booked before the claim is filed, on management's
  assessment of "reasonable assurance" based on approvals received in
  earlier years (Note 27 consol. p.277 / Note 26 standalone p.341). 🟡
  Watch: this is a judgement-based accrual of government-incentive income
  ahead of the formal claim — not improper under Ind AS 20 if recovery is
  reasonably assured, but it is a discretionary revenue recognition
  practice worth a management question, especially since PLI receivable
  jumped from ₹6,617.66 lakh to ₹9,189.39 lakh in FY26 (Note 15
  consol./Note 16 standalone) while FY26 PLI revenue booked (₹2,571.73
  lakh) fell sharply from FY25's ₹6,617.66 lakh — i.e., the receivable grew
  even as the current-year income recognised shrank, implying older claims
  remain unrealised in cash.
- First-time standard adoption: none material; company is newly listed
  (03-Oct-2025) with no history of standard transition disclosures beyond
  the routine MCA notifications above.
- Capitalisation threshold: NOT FOUND IN DOCUMENT (no rupee threshold
  disclosed for PPE capitalisation).

## 2. RELATED PARTY TRANSACTIONS

Full table, consolidated (Note 39) and standalone (Note 38) — figures
below are STANDALONE unless marked [C] for consolidated-only variance.

| Party | Relationship | Nature | FY26 ₹ lakh | FY25 ₹ lakh | YoY % |
|---|---|---|---|---|---|
| Nirani Sugars Ltd (erstwhile MRN Chamundi) | Affiliate, KMP significant influence | Sale of steam/diesel/chemicals | 10,195.11 | 7,730.35 | +31.9% |
| Nirani Sugars Ltd | same | Purchase of raw material | 87,317.92 | 1,07,323.69 | -18.6% |
| Accutrade Global LLP | Affiliate | Purchase of raw material | 969.21 | 0 | new |
| Nirani Sugars Ltd | same | Rent expense | 37.23 | 13.50 | +175.8% |
| Vijaykumar Murugesh Nirani + Vishal Nirani | KMP (MD + Director) | Remuneration | 514.88 | 522.06 | -1.4% |
| Anand Kishore (CFO) | KMP | Remuneration | 62.55 | 16.28 | +284% |
| Nirani Holdings Pvt Ltd | Affiliate | Loan received | 440.00 | 241.00 | +82.6% |
| TruAlt Gas Pvt Ltd | Subsidiary | Sale of land | 69.20 | 0 | new |

RPT purchase of raw material as % of total purchases (Note 28 standalone):
FY26 ₹88,287.13 lakh / ₹1,21,624.88 lakh total = **72.6%**. FY25
₹1,07,323.69 lakh / ₹1,03,698.51 lakh total = **103.5%** — RPT purchase
EXCEEDS the disclosed total purchases figure. 🔴 RED FLAG: same pattern in
the consolidated notes (RPT purchase ₹1,08,130.02 lakh vs Note 29 total
purchases ₹1,04,267.14 lakh, consolidated, FY25) and in the prospectus
restated financial information (RPT purchase ₹1,08,130.02 lakh, FY25,
"consolidated basis," identical figure to the AR). This is not a one-off
extraction artefact: it recurs across two independently filed documents
(prospectus Sep-2025, AR May-2026) with the same FY25 figures. Possible
explanations (classification difference between "raw material" and
"stock-in-trade" purchase lines, or a note-level reconciliation gap) are
not addressed anywhere in either document. Flagged for management question.

RPT purchase of raw material as % of revenue from operations (standalone):
FY26 88,287.13/1,70,465.34 = **51.8%**. FY25 1,07,323.69/1,88,011.66 =
**57.1%**. The company sources the majority of its feedstock cost from a
single promoter-family entity group.

Historical trend (prospectus, restated, ₹ lakh, all Nirani-group entities
combined): FY23 ₹58,302.51, FY24 ₹84,660.22, FY25 ₹1,08,130.02 — RPT
feedstock purchases have risen every year and have consistently represented
essentially the entire raw-material purchase base pre-FY26 (prospectus
p.432).

RPTs as % of revenue (sale-side, steam/diesel/chemicals to Nirani Sugars):
FY26 6.07%, FY25 4.11% — smaller but rising.

Trade payables to related parties as % of total trade payables (standalone
Note 24/38(C)): FY26 ₹17,247.45 lakh / ₹26,975.25 lakh total = **63.9%**.
FY25 ₹34,422.53 lakh / ₹46,826.90 lakh total = **73.5%**. 🔴 RED FLAG /
structural finding: a single related-party group has funded a majority
share of the company's trade payables (working-capital financing) in both
years. Cross-referenced against the mandatory Schedule III ratio note
(Note 52 standalone, "Net Capital Turnover Ratio"): FY25 closing working
capital was **negative ₹18,309.03 lakh** (current liabilities exceeded
current assets) and FY26 closing working capital is **positive ₹18,769.55
lakh**. Read together, this indicates the company effectively financed
working capital pre-IPO through extended trade credit from the
promoter-family sugar mills, and used IPO proceeds in FY26 to pay this
down (RPT payable nearly halved YoY even as gross purchases from the same
counterparty stayed large). This is a load-bearing structural fact for
fact 3 not previously stated this precisely.

Loans to promoter entities: none disclosed (loans flow the other direction
— Nirani Holdings lent ₹440.00 lakh TO the company, standalone Note 38(C)).
No loans to promoter entities found. 🟢 on this specific point.

Corporate guarantee for subsidiary: the Company "has also given corporate
guarantee in favour of NABARD in respect of the said borrowing availed by
TruAlt Gas Private Limited" (standalone Note 8, Investments, p.330).
Management states "no liability is expected to arise." 🔴 RED FLAG /
disclosure inconsistency: standalone Note 57 (Contingent liabilities) states
"The Company does not have any contingent liabilities and contingent assets
as at the end of 31 March 2026 (31 March 2025: Nil)" — a corporate
guarantee given on behalf of a subsidiary is a contingent liability under
Ind AS 37 by definition, even where the probability of outflow is assessed
as remote; standard practice is to disclose it under the contingent
liabilities note with an amount and a "no outflow expected" comment, not to
omit it from that note entirely. Note 39(D)(4) (standalone RPT terms)
reinforces the omission by stating flatly "There have been no guarantees
provided or received for any related party receivables or payables" —
directly contradicting Note 8's own guarantee disclosure two ways.
Amount of the guarantee itself: NOT FOUND IN DOCUMENT (Note 8 names the
guarantee but does not state its ₹ amount; the NABARD loan to TGPL is
disclosed elsewhere at ₹18,000 lakh sanctioned, ₹4,666 lakh disbursed at
FY26-end, consolidated Note 20(vii), so the guarantee ceiling is inferable
but not stated).

Related-party equity dealings in TruAlt Gas Pvt Ltd (TGPL): the Company
bought 51% of TGPL at ~₹24/share (Oct-2025, standalone Note 35 / Note 36
consol.), briefly increased to 77.84% via capital infusion, then TGPL
issued a rights allotment of 80,06,536 shares to Nirani Holdings Private
Limited (promoter entity) diluting the Company back to 51%. Subsequent
event (Note 59 consolidated only, p.294): on 16-Apr-2026 Sumitomo
Corporation bought 1,13,77,743 TGPL shares FROM Nirani Holdings at
₹30.90/share, taking Sumitomo to 49% of TGPL. 🟡 Watch: Nirani Holdings
(promoter entity) picked up TGPL shares via a rights issue and sold a
tranche to a third party (Sumitomo) at ₹30.90/share, a ~29% premium to the
Company's own ₹24/share acquisition price eight months earlier, with no
disclosed pricing rationale for either the rights issue price to Nirani
Holdings or the Sumitomo sale price. This falls outside the FY26 balance
sheet but is disclosed as a subsequent event in the consolidated notes
only, not the standalone notes (standalone Note 61 states "no significant
adjusting events" — reasonable, since it is a subsidiary-level equity
transaction, but the asymmetry between the two note sets on this point is
worth flagging).

New related parties this year: TruAlt Gas Private Limited (subsidiary from
27-Oct-2025), Accutrade Global LLP (raw-material purchase and advances
counterparty, new in FY26; advance of ₹4,030.79 lakh outstanding to this
entity at FY26-end, standalone Note 38(C) — a NEW, not previously
disclosed related-party advance of meaningful size, ~₹40 cr, with no
narrative on its purpose).

## 3. CONTINGENT LIABILITIES

Both note sets (consolidated Note 57, standalone Note 57): "**NIL**"
contingent liabilities and contingent assets for FY26 and FY25. Consistent
with the prospectus restated disclosure ("As of March 31, 2025, there were
no contingent liabilities... that have not been provided for," prospectus
p.27) — so the NIL position itself is not new. However, see Section 2 above:
the NIL position is contradicted within the same AR by the standalone Note
8 corporate-guarantee disclosure. 🔴 RED FLAG (disclosure consistency, not
a going-concern issue — the amounts involved are modest relative to
balance sheet size).
No tax dispute litigation appears in either note set. NOT FOUND IN
DOCUMENT: the GST demand order dated 20-Aug-2026 (per company memory) —
correctly absent, as it postdates the AR's board-approval date (22-May-2026)
and is not an adjusting subsequent event as of the signing date.
Total contingent liabilities as % of net worth: 0% (nil base).
Guarantees for subsidiaries: one identified (NABARD/TGPL, see above),
amount not quantified in the note itself.

## 4. TRADE RECEIVABLES

Standalone ageing (Note 12, p.331), ₹ lakh:

| Bucket | FY26 | % of total | FY25 | % of total |
|---|---|---|---|---|
| Not due | 14,071.82 | 34.7% | 23,321.70 | 69.1% |
| <6 months (overdue) | 23,367.56 | 57.6% | 6,835.60 | 20.2% |
| 6m-1yr | 853.75 | 2.1% | 3,414.27 | 10.1% |
| 1-2yr | 2,256.51 | 5.6% | 194.03 | 0.6% |
| 2-3yr | 37.31 | 0.1% | 14.80 | 0.0% |
| >3yr | 0 | 0% | 0 | 0% |
| **Total** | **40,586.96** | | **33,780.40** | |

🟡 Watch / receivables trend: the "not due" share collapsed from 69.1% to
34.7% of the book while the "less than 6 months overdue" share jumped from
20.2% to 57.6%. Receivables aged **more than 6 months** as % of total
actually *improved* slightly (7.7% FY26 vs 10.6% FY25, sum of the 6m-1yr /
1-2yr / 2-3yr / >3yr buckets), so the long tail did not worsen — but the
short-term payment cycle from customers (predominantly public-sector OMCs)
visibly lengthened within the year. Combined with the Schedule III "Trade
Receivables Turnover Ratio" falling from 5.68 to 4.51 (-21%, standalone
Note 52), this is a genuine, if moderate, receivables-quality deterioration
worth monitoring, not yet a red flag given the OMC counterparty quality.
Single customer >10%: 4 customers represent >10% of revenue each,
combined ₹1,30,921.30 lakh (FY26) vs ₹1,60,050.79 lakh (FY25) — names not
disclosed (Note 26 standalone / 27 consolidated). NOT FOUND IN DOCUMENT:
individual customer names/amounts.
ECL provision: NIL loss allowance computed both years — see Section 1.
Retention money within trade receivables: ₹6,187.10 lakh (FY26) vs
₹2,945.30 lakh (FY25), more than doubled — customers (OMCs) retain 3% of
invoice value, settled at season-end (Note 42(C) consol. / 41(C)
standalone). This retention component is itself a slow-pay structural
feature of the OMC relationship, not new.
Receivables from related parties: "Receivable from related parties" ₹1,686.19
lakh (non-current, current split, Note 15.2 standalone), essentially flat
YoY (₹1,507.69 lakh FY25) — modest.

## 5. INVENTORY

Standalone (Note 11, p.330), ₹ lakh:

| Category | FY26 | FY25 | Change |
|---|---|---|---|
| Raw materials | 19,091.80 | 5,498.31 | +247.2% |
| Finished goods | 28,221.96 | 11,946.34 | +136.2% |
| Finished goods in transit | 2,726.88 | 1,913.21 | +42.5% |
| Stores & spares | 2,142.07 | 1,062.37 | +101.6% |
| **Total** | **52,182.71** | **20,420.23** | **+155.6%** |

This directly CONFIRMS company memory fact 2's inventory build (₹210 cr
→ ₹528 cr, standalone total here is ₹521.8 cr, essentially the same
figure the screener/company-memory figure references, small variance from
consolidated ₹528.4 cr). Finished goods growth (+136.2%) far outpaces
revenue growth (standalone revenue FY26 ₹1,704.65 cr vs FY25 ₹1,880.12
cr — revenue actually FELL 9.3% while finished goods inventory more than
doubled). 🔴 RED FLAG: inventory built sharply while revenue declined,
consistent with the known Q2FY26 multi-feed shutdown story but the notes
give no narrative explaining WHY finished goods specifically (not just raw
material for the new grain lines) grew 136%. No write-down disclosed
(inventory carried at lower of cost and NRV per policy, no NRV write-down
amount stated in either note set) — NOT FOUND IN DOCUMENT: any inventory
write-down/obsolescence figure.
Inventory turnover ratio (Schedule III Note 52 standalone): 3.06x FY26 vs
7.05x FY25, -57% — the ratio note itself attributes the variance "mainly
due to increase in the inventory as compared to previous Financial year,"
confirming management's own framing of this as the dominant driver, without
further explanation of the composition.
Inventory pledged as security for borrowings in full (Note 54, both sets).

## 6. INVESTMENTS

Standalone Note 8 (Investments), non-current:

| Investment | FY26 ₹ lakh | FY25 ₹ lakh |
|---|---|---|
| Investment in subsidiary — Leafiniti Bioenergy Pvt Ltd | 1,691.52 | 1,691.52 |
| Investment in subsidiary — TruAlt Gas Pvt Ltd (1,18,42,140 shares) | 2,842.11 | 0 |
| SBI Innovative Opportunities Fund (current) | 406.53 | 436.08 |
| **Total unquoted** | **4,940.16** | **2,127.60** |

Ownership %: Leafiniti Bioenergy 51% (FY26 and FY25, unchanged per Note 42
standalone "Disclosure of significant interest in subsidiary"); TruAlt Gas
51% at FY26-end (down from a peak 77.84% intra-year, per business
combination Note 35/36). No impairment on either subsidiary investment
disclosed. No loss-making subsidiary explicitly flagged in these notes
(subsidiary-level P&L not separately stated in standalone notes; segment
note (consolidated Note 40) shows Compressed Biogas segment result was
POSITIVE ₹1,842.20 lakh FY26 on a consolidated basis, so no obvious
loss-maker at segment level, though Note 52 (Group information) shows
TruAlt Gas Pvt Ltd's own share of total comprehensive income was
**negative ₹104.59 lakh** for FY26 — a modest but real subsidiary-level
loss in its first part-year as a subsidiary). ICDs/loans given: intercompany
loan to subsidiary (Leafiniti, per Note 38(C)/9 standalone) — opening
₹266.33 lakh, interest ₹16.60 lakh, repayment ₹16.33 lakh, closing ₹266.60
lakh; unsecured, considered good, rate/tenure NOT FOUND IN DOCUMENT beyond
the interest income figure implying roughly 6.2% effective yield.
Corporate guarantee for TGPL's NABARD facility and 15.11% TGPL shareholding
pledge to NABARD: see Section 2 (RPT/contingent liability inconsistency).
No other investments with unrealised gains/losses of note — mutual fund
FVTPL loss of ₹29.55 lakh FY26 (immaterial, Note 33 standalone).

## 7. BORROWINGS

Instrument table (standalone Note 20, non-current, p.335-336):

| Lender | FY26 ₹ lakh | FY25 ₹ lakh | Rate | Security |
|---|---|---|---|---|
| State Bank of India (Term loan 1, via consortium) | 16,296.27 | 19,768.07 | 6M SBI MCLR + 1.55% | First charge stock/receivables + equitable mortgage |
| IREDA (Term loans 1-3) | 98,420.13 | 1,05,452.40 | 10.52-10.95% (blended) | Same |
| HDFC (vehicle) | 53.89 | 65.94 | 8.60-8.95% | Vehicle hypothecation |
| Bank of India (vehicle) | 8.03 | 16.36 | 8.85% | Vehicle hypothecation |

Plus current borrowings (Note 22 standalone): current maturities of LT
debt ₹21,747.51 lakh + working capital loan ₹43,267.91 lakh = ₹65,015.42
lakh (FY26) vs ₹42,958.31 lakh (FY25), **+51.4%** — working capital
borrowing grew sharply despite the IPO equity infusion, consistent with
the inventory-funded-by-debt-and-equity story.
Covenant breaches: NONE disclosed; "the Company has satisfied all other
debt covenants... has not defaulted on any loans payable" (Note 20A,
both sets). The "limitation on indebtedness" covenant is stated as
"suspended" as of the authorisation date, its trigger condition not
detailed — NOT FOUND IN DOCUMENT: the specific criteria for suspension.
🟡 Watch given Section 52's Schedule III DSCR figure below.
Fixed vs floating: predominantly floating (MCLR-linked or IREDA
grade-linked), one fixed-rate exception (Term loan 3, IREDA, 10.95% fixed
as at FY26-end per the rate schedule).
5-year repayment schedule (Note 20B standalone): within 1 year ₹21,747-ish
lakh (aggregate across lenders), 1-5 years the bulk (₹89,255 lakh
aggregate across SBI+IREDA), more than 5 years ₹4,553 lakh (IREDA only).
Related-party borrowings: none identified as borrowings from related
parties (the ₹440 lakh from Nirani Holdings is classified as a loan/advance
received, not a borrowing instrument, Note 38(C) standalone).
TReDS / reverse factoring: Company settles MSME vendor dues partly through
the TReDS platform (RXIL); ₹7,508.80 lakh payable to RXIL at FY26-end,
settled within 54-59 days (Note 22 standalone, footnote). 🟡 Watch:
supply-chain financing of this scale (~₹75 cr) effectively extends
payables via a financial intermediary; while disclosed per the new Ind AS 7
supplier-finance amendment, it is a structure that can flatter reported
payable-days if not read alongside the RXIL balance.
Term loan use-of-proceeds is specific and traceable to the multi-feed
conversion units (see Section 1), a positive on capital-allocation
discipline.

## 8. TRADE PAYABLES

Standalone Note 24 (p.339), ageing:

| Bucket | FY26 ₹ lakh | FY25 ₹ lakh |
|---|---|---|
| MSME | 2,717.76 | 1,338.86 |
| Others | 24,257.49 | 45,488.04 |
| **Total** | **26,975.25** | **46,826.90** |

MSME dues >45 days: the ageing table shows MSME entirely in the
"less than 1 year" bucket with none in "not due," implying all MSME
payables are technically overdue by the reporting date, though no bucket
splits 45 days specifically — NOT FOUND IN DOCUMENT: an explicit >45-day
MSME breakout. Interest on delayed MSME payments: **NIL** disclosed, all
four MSMED Act interest disclosure lines (paid, due, accrued, further due)
show zero (Note 24 standalone / 25 consolidated). 🟢 Clean on interest, but
🟡 Watch: MSME dues more than doubled YoY (+103%) while total payables fell
42%, so MSME suppliers now form 10.1% of payables (up from 2.9%), a
mix-shift toward smaller suppliers worth watching for payment-practice
pressure even absent formal interest penalties.
Payable days trend: Trade Payables Turnover Ratio (Schedule III Note 52)
3.84x FY26 vs 4.36x FY25, -12% (implying payable days lengthened modestly).

## 9. PROVISIONS

Only employee-benefit provisions found: gratuity (unfunded) and leave
encashment (Note 21 standalone / consolidated). No warranty, decommissioning,
onerous-contract, or litigation provisions disclosed in either note set —
NOT FOUND IN DOCUMENT (consistent with a distillery/manufacturing business
with no product-warranty exposure and the NIL contingent-liability
position noted above).
Actuarial assumptions (Note 37 standalone / 38 consolidated): discount
rate 7.15% (FY26) vs 6.75% (FY25); salary growth 7.50% flat; attrition
7.50% flat. Sensitivity table provided (±1% discount/salary, ±50%
attrition, ±10% mortality) — 🟢 Clean, full IND AS 19 disclosure.
Funded status: 0% funded (unfunded plan) — see Section 1.

## 10. DEFERRED TAX

Standalone Note 34 (p.343): effective tax rate (income tax
expense/PBT) FY26 = 2,944.48/10,947.48 = **26.9%** vs statutory 25.17%
(under Section 115BAA). FY25 = 1,153.58/15,215.11 = **7.6%** vs statutory
25.17% — the FY25 effective rate was far BELOW statutory, explained in the
reconciliation by a large negative adjustment "Impact of depreciation on
customer relationship not considered in tax WDV in earlier years"
(-₹2,785.48 lakh, a one-off correcting item). FY26's reconciliation carries
no equivalent large one-off, so FY26's effective rate is closer to a clean
read of ongoing tax burden. No MAT credit: "no liability for Current Tax
as the Company has tax losses and MAT provisions are not applicable... as
it has opted for section 115BAA" (Note 34 standalone). Unrecognised DTA:
NOT FOUND IN DOCUMENT (no explicit unrecognised-DTA disclosure; deferred
tax asset on unabsorbed depreciation/carry-forward losses of ₹676.11 lakh
(FY26, standalone) is recognised in full, implying management judges
future taxable profit probable). DTA realism: 🟡 Watch — no forward
taxable-income projection disclosed to support recognition, standard
industry practice but a bare assertion.

## 11. REVENUE DETAILS

Disaggregation (standalone Note 26, p.341): Sale of goods ₹1,46,791.77
lakh, Sale of traded goods ₹20,894.70 lakh, PLI ₹2,571.73 lakh, provision
write-back ₹207.14 lakh = total ₹1,70,465.34 lakh (FY26). Single segment
(biofuels manufacture, Note 39 standalone — CODM confirmation of one
segment). Consolidated has two segments: Ethanol and other products
(₹1,70,502.73 lakh) and Compressed Biogas (₹2,247.93 lakh) (Note 40
consolidated). No geographic disaggregation beyond "India only." No
contract assets/liabilities: "no unsatisfied performance obligations or
contractual liabilities" both years (Note 26 standalone / 27 consolidated).
Top customer revenue: 4 customers >10% each, aggregate disclosed, names
not disclosed (see Section 4).

## 12. OTHER CRITICAL NOTES

- Exceptional items: NOT FOUND IN DOCUMENT — no exceptional-items note or
  line exists in either P&L; no one-off/non-recurring items called out
  anywhere in the notes (consistent with the NIL contingent liability and
  NIL impairment picture — either a genuinely clean year or a thin
  disclosure appetite for one-offs).
- Capital commitments: standalone Note 56 — ₹789.49 lakh (FY26) vs
  ₹22,240.69 lakh (FY25), a **-96.4%** collapse, consistent with the
  multi-feed conversion capex programme substantially completing during
  FY26 (three units commissioned Nov-2025 to Feb-2026).
- Foreign currency exposure: "not exposed to significant foreign currency
  risk... no material transactions, monetary assets, or monetary
  liabilities denominated in foreign currencies" (Note 41(A)(ii)
  standalone / 42(A)(ii) consolidated). 🟢 Clean, and notable for a
  business with SAF/export optionality in its narrative — confirms that
  optionality has not yet touched the financials.
- Basic vs diluted EPS: no gap either year (FY26 10.23=10.23 standalone;
  FY25 20.08=20.08, "potential equity shares are anti-dilutive" — the CCPS
  fully converted in FY25 before the IPO, so FY26 has a completely clean
  capital structure with no dilution overhang). No ESOP scheme identified
  anywhere in the share capital or other-equity notes — NOT FOUND IN
  DOCUMENT, i.e., no ESOP dilution risk currently exists.
- Share capital changes: CCPS (₹46,919.00 lakh, 4,69,19,000 shares)
  converted to 95,55,804 equity shares in FY25 at ₹491/share (1:4.91 ratio,
  IBBI valuer report); IPO issued 1,51,20,967 fresh equity shares
  (₹10 FV + ₹486 premium) on 30-Sep-2025, listed 03-Oct-2025. IPO total:
  1,69,20,967 shares at ₹495/share = 1,51,20,967 fresh + 18,00,000 OFS
  (Note 60 standalone) — OFS value ₹89.1 cr, close to the ~₹88 cr figure in
  company memory.
- Direct debits/credits to reserves bypassing P&L: deferred tax liability
  on the CCPS liability component, ₹3,730.13 lakh, credited directly to
  retained earnings on conversion (FY25) rather than through P&L (Note 18
  standalone/17 consolidated) — disclosed and Ind-AS-compliant treatment,
  not a red flag, but a reader must know to look in the statement of
  changes in equity, not the P&L, to see it.
- IPO proceeds utilisation (Note 60/61, both sets, identical table):
  Capex ₹15,068 lakh proposed / ₹14,014 lakh utilised (₹1,054 lakh
  unutilised); **Working Capital ₹42,500 lakh proposed / ₹42,500 lakh
  utilised in FULL**; General Corporate Purpose ₹8,136 lakh proposed/
  utilised in full; Issue Expenses ₹9,296 lakh proposed / ₹7,371 lakh
  utilised (₹1,925 lakh unutilised). Total unutilised ₹2,979 lakh held in
  IPO Public Issue Account (₹1,925 lakh) and IPO Monitoring Account
  (₹1,054 lakh). This CONFIRMS and resolves part of load-bearing fact 2:
  the ₹425 cr working-capital tranche was fully deployed to working
  capital per the company's own utilisation statement, and — read against
  FY26 standalone CFO of exactly **₹(29,615.04) lakh = ₹(296.15) cr**
  (Note: standalone cash flow statement, matching company memory's "FY26
  CFO Rs -296 cr" precisely) and the ₹318 cr inventory build — the ₹425 cr
  injection was consumed by the operating cash burn and inventory build,
  not retained as a liquidity cushion. Net cash proceeds actually received
  from the fresh issue were ₹665.71 cr (₹66,570.56 lakh, net of ₹84.29 cr
  issue expenses deducted from securities premium), not the full ₹750 cr
  headline "objects of the issue" figure — a reconciling detail not stated
  plainly anywhere in the notes as a single number (has to be triangulated
  across Notes 18, 19, and the cash flow statement).
- Events after balance sheet date: consolidated Note 59 — Sumitomo
  Corporation's 16-Apr-2026 purchase of 49% of TruAlt Gas from Nirani
  Holdings (see Section 2). Standalone Note 61 states no significant
  adjusting events. No mention of the GST demand order (20-Aug-2026,
  post-signing) or the Unit 5 Badami slump sale to Onkar Agro Sugars &
  Energy (04-Aug-2026, post-signing) in either note set — expected, both
  postdate the 22-May-2026 board approval date.
- CSR: required ₹164.50 lakh FY26 (₹65.45 lakh FY25), spent in full both
  years, no shortfall (Note 33 standalone footnote). 🟢 Clean.
- Componentisation of PPE in progress: standalone/consolidated Note 59/60
  — company is still carrying out Ind AS 16 componentisation for the three
  converted distillery units, expected complete by 30-Jun-2026 (i.e., AFTER
  the FY26 signing date). 🟡 Watch: depreciation on these units for FY26
  was computed before this exercise completes, meaning the FY26
  depreciation charge on the newly converted units may be revised
  (typically prospectively) once componentisation finishes — a live
  estimate, not yet settled.
- Schedule III mandatory ratios (standalone Note 52, p.354-356) — the
  single richest disclosure block in the AR for cross-checking the
  narrative, full table:

| Ratio | FY26 | FY25 | Change | Mgmt explanation |
|---|---|---|---|---|
| Current ratio | 1.33 | 1.03 | +29% | Trade receivables, GST inputs, govt grants up |
| Debt-Equity | 1.04 | 2.00 | -48% | IPO fresh issue |
| **DSCR** | **0.99** | **1.28** | **-23%** | NA (unexplained) |
| Return on Equity | 0.07 | 0.27 | -74% | Lower sales/depreciation + IPO dilution |
| Inventory turnover | 3.06x | 7.05x | -57% | Inventory increase |
| Receivables turnover | 4.51x | 5.68x | -21% | NA |
| Payables turnover | 3.84x | 4.36x | -12% | NA |
| Net capital turnover | 9.08x | -10.27x | -188% | WC swung positive (see Section 2) |
| Net profit margin | 0.05 | 0.07 | -29% | Lower sales/depreciation |
| Return on Capital Employed | 0.10 | 0.13 | -23% | NA |
| Return on Investment | 0.05 | 0.18 | -72% | Lower sales, IPO capital increase |
| Fixed asset coverage | 1.74 | 1.30 | +34% | Grain project capitalisation |

🔴 RED FLAG: **Debt Service Coverage Ratio fell to 0.99x in FY26** (from
1.28x in FY25) — net operating income did not fully cover debt service
(interest + lease payments + principal repayments) in the year, a genuine
coverage shortfall, disclosed by the company itself in its mandatory
ratio note with NO explanation given ("NA" in the reason-for-variance
column despite the -23% move exceeding the report's own 25%-variance
disclosure threshold on other lines — a disclosure gap, since DSCR moved
almost exactly to the trigger line and the company chose not to explain
it). This sits alongside the capital-management note's statement that DSCR
is itself one of the lender covenant metrics (Note 53 standalone) — the
covenant threshold level is not stated, so whether 0.99x breaches,
approaches, or sits comfortably inside the covenant cannot be determined
from this document. NOT FOUND IN DOCUMENT: the covenant DSCR threshold.

## PASS 1 SUMMARY — TOP 10 MOST SIGNIFICANT FINDINGS

1. **DSCR fell to 0.99x (FY26) from 1.28x (FY25)**, per the company's own
   mandatory Schedule III ratio note, with no explanation given despite the
   move exceeding the report's stated 25% variance-disclosure trigger.
   (Note 52 standalone, p.355) 🔴
2. **Related-party feedstock purchases from Nirani-group entities
   (principally Nirani Sugars Ltd) are 72.6% of total raw-material
   purchases in FY26 and EXCEED 100% of disclosed total purchases in FY25**
   (₹1,073.24 cr RPT vs ₹1,036.99 cr total purchases, standalone; same
   pattern in consolidated and in the prospectus restated financials for
   the identical FY25 figures). (Notes 28 & 38, standalone; Notes 29 & 39,
   consolidated) 🔴
3. **Corporate guarantee given for a subsidiary's NABARD borrowing is
   disclosed in the Investments note (Note 8) but the Contingent
   Liabilities note (Note 57) says NIL, and the RPT terms note (38(D))
   states flatly that no guarantees were given** — a three-way internal
   inconsistency within the same standalone financial statements. 🔴
4. **Inventory (standalone) more than doubled, ₹204.2 cr → ₹521.8 cr
   (+155.6%), while standalone revenue FELL 9.3%** in the same year;
   finished goods alone grew 136.2%. No write-down or composition
   narrative given. (Note 11) 🔴
5. **FY26 CFO was ₹(296.15) cr standalone**, confirmed to the rupee against
   company memory; the ₹425 cr IPO working-capital tranche was fully
   utilised per the IPO utilisation table (Note 60/61) but was absorbed by
   the operating cash burn and inventory build, not retained as liquidity.
   Net IPO cash actually received was ₹665.71 cr net of issue costs, below
   the ₹750 cr headline "objects of the issue" figure. (Notes 18, 19, 60/61,
   cash flow statement) 🟡
6. **Related-party trade payables funded 63.9% (FY26) / 73.5% (FY25) of
   total trade payables**, and the Schedule III working-capital ratio shows
   the company's working capital was structurally NEGATIVE (-₹183.1 cr) at
   FY25-end, turning positive (+₹187.7 cr) only after the IPO — implying
   pre-IPO working capital was substantially financed by promoter-family
   trade credit. (Notes 24, 38, 52) 🔴
7. **Trade receivables ageing shifted sharply from "not due" (69.1% →
   34.7% of book) to "overdue but under 6 months" (20.2% → 57.6%)**, even
   as the long-tail (>6 months) share improved slightly; receivables
   turnover fell 21%. (Note 12, Note 52) 🟡
8. **A related-party entity (Nirani Holdings) bought TruAlt Gas shares via
   a rights issue and sold a tranche to Sumitomo Corporation at ₹30.90/
   share, a ~29% premium to the Company's own ₹24/share acquisition price**
   eight months earlier, with no pricing rationale disclosed for either
   leg; this transaction is a subsequent event disclosed only in the
   consolidated notes. (Note 36 standalone / Note 59 consolidated) 🟡
9. **Performance Linked Incentive (government scheme) revenue is booked
   ahead of the formal claim filing** for FY25 and FY26, based on
   management's judgement of "reasonable assurance"; the PLI receivable
   grew to ₹91.9 cr even as current-year PLI revenue recognised fell to
   ₹25.7 cr from ₹66.2 cr, implying older claims remain uncollected in
   cash. (Notes 15/16, 26/27) 🟡
10. **Capital commitments collapsed 96.4%** (₹222.4 cr → ₹7.9 cr),
    consistent with the multi-feed conversion capex programme completing
    during the year (three units commissioned Nov-2025 to Feb-2026,
    specific borrowing costs disclosed and traceable). This is the one
    clean confirmatory finding among the top 10: the capex story in the
    notes matches the narrative. (Note 56 standalone) 🟢
