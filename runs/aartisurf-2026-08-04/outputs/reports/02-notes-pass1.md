# STAGE 2 — NOTES TO FINANCIAL STATEMENTS, PASS 1 OF 3
## AARTISURF | Run date 2026-08-04

---

## ⚠️ DOCUMENT IDENTITY FLAG (read before anything else)

The file supplied at `inputs/annual-report/Annual_Report_2022.pdf` is titled on its cover
**"Annual Report 2020-21"** ("Adapting to Sustain Momentum") and its financial statements are
for the **year ended March 31, 2021 (FY2020-21)**, the Company's **3rd Annual Report** (AGM
notice for 3rd AGM, dated May 21, 2021 board approval). It is **not** a FY2022 annual report
despite the filename. This is confirmed by: cover page title, Directors' Report ("Third Annual
Report... year ended March 31, 2021"), all financial statement headers ("as at/for the year
ended March 31, 2021"), Notice of 3rd AGM (p.121), and MD/CFO/Auditor sign-off dated May 21,
2021 (all pages, e.g. p.56, p.85, p.120).

Relative to the 2026-08-04 run date, this is the **FY2020-21** annual report — roughly **5
years and 4 months stale**, not the "~4 years" characterized in the task brief. There is no
FY2022, FY2023, FY2024, or FY2025 annual report in this run's input folder as supplied. This
gap is material to every downstream valuation and trend stage and should be flagged upstream
(input_gaps).

All notes below are anchored to this FY2020-21 (year ended 31 March 2021) standalone and
consolidated financial statements, Notes 1–33. Currency: ₹ Lakhs unless stated. PDF page
numbers cited alongside the printed page numbers in the document footer (printed page = PDF
page − 3 in the front matter through note 33; Notice section onward printed page = PDF page − 3
also holds).

---

## SCOPE COVERED

Full read of Notes 1–33 to the Standalone Financial Statements (pp.60–85 printed / PDF pp.63–88)
and Notes 1–33 to the Consolidated Financial Statements (pp.96–120 printed / PDF pp.99–123),
plus the Standalone and Consolidated Independent Auditors' Reports and CARO Annexures (pp.48–55
printed / PDF pp.51–58), which carry disclosures (disputed statutory dues, title-deed status)
that cross-reference directly into Note 27 (Contingent Liabilities). Every note number 1 through
33 was read in both the standalone and consolidated sets; consolidated figures differ from
standalone only immaterially because the sole subsidiary, Aarti HPC Limited, is a dormant
shell (Share Capital ₹50,000; Reserves ₹(1,18,375); Total Assets ₹67,075; Turnover Nil — Annexure
A / Form AOC-1, p.19). Standalone figures are used as the primary anchor throughout unless
stated otherwise.

---

## 1. ACCOUNTING POLICIES & CHANGES

**Depreciation useful lives vs Schedule II** (Note B.3(h), Significant Accounting Policies, p.62
standalone / p.99 consolidated): Company departs from Schedule II defaults for six asset
classes — Leasehold Land (over remaining lease tenure), Buildings (19 years, vs Schedule II's
30/60-year defaults — **shorter, i.e. more conservative/faster depreciation**), Plant & Machinery
(19 years, "technically assessed," vs Schedule II's typical 15–25 years depending on process
type — roughly in line, not aggressive), Furniture & Fixtures (10 years), Vehicles (7 years),
Intangible Assets/Product Registration Rights (5 years). 🟢 Clean — faster-than-mandated
depreciation on buildings is conservative, not earnings-inflating.

**Borrowing cost capitalisation — first year of this practice**: Note 22 (Finance Cost, p.78/114)
shows "Less: Amount capitalised in the cost of PPE (101.84)" for FY21 against **Nil** in FY20.
Note 1(c) (PPE, p.67/103) confirms "Borrowing costs of ₹101.84 Lakhs has been capitalised during
the year (Previous year – Nil)." The Standalone and Consolidated Auditors' Reports both flag
this as a Key Audit Matter area ("we have verified the capitalisation of borrowing cost incurred
on qualifying assets in accordance with Ind AS 23," p.48/86). 🟡 Watch — new capitalisation
policy in year one of a large capex programme (₹6,148.73 Lakhs cash capex per Cash Flow
Statement, p.59) understates finance cost and overstates PPE/profit versus the prior
convention of full expensing; auditors reviewed it and it is disclosed, but it is a genuine
P&L-improving accounting choice made in the same year profit jumped >10x.

**Fire loss at Silvassa plant — asset write-off, not expensed as loss**: Note 1(b) (PPE, p.67/103):
"In the reporting period, plant and machinery was destroyed/lost in the fire, which occurred in
Silvassa Plant and accordingly Gross Block and Depreciation Block is reduced to the extent of
assets destroyed in the fire amounting to ₹158.18 Lakhs (Corresponding Depreciation ₹80.17
Lakhs for plant and machinery)." Net book value written off ≈ ₹78.01 Lakhs. No separate
"exceptional item" or "loss on fire" line appears in the P&L (Note 12, Profit before
Exceptional Items and Tax, shows Exceptional Items = Nil in both years). The write-off was
instead netted directly against Gross Block/Depreciation in the fixed asset schedule — an
unusual presentation for what should arguably be a P&L loss event. An Insurance Claim
Receivable of ₹360.89 Lakhs is separately recognised (Note 7, Other Financial Assets, p.71) —
i.e., the company has booked an insurance recovery asset larger than the net book value
destroyed, with no corresponding gain/loss recognised yet in the P&L this year (Other Income,
Note 18, shows no insurance claim income for FY21; PY had ₹14.07 Lakhs). 🟡 Watch — the netting
of an asset destruction event directly against Gross Block rather than through P&L, paired with
an insurance receivable not yet reconciled to the loss, is worth a management question.

**Revenue recognition**: Standard "control transfers on shipment/dispatch" policy (Note B.3(f),
p.62/98) — not bill-and-hold, not percentage-of-completion; unremarkable for a bulk-chemical
manufacturer. 🟢 Clean.

**ECL / impairment matrix**: Policy states "simplified approach" using "historical default
rates" for trade receivables (p.65/101) but **no quantitative ECL matrix or default-rate table
is disclosed anywhere in Notes 1–33**. Provision for doubtful debts is static at ₹69.97 Lakhs in
both FY20 and FY21 (Note 5, p.70) despite gross trade receivables more than tripling (see
Section 4 below). NOT FOUND IN DOCUMENT — ECL rate/matrix. 🟡 Watch.

**Ind AS 116 Leases**: A full lessee/lessor accounting policy is written out in detail (pp.63,
99–100) but **no Right-of-Use asset, lease liability, or lease discount rate appears anywhere in
the Balance Sheet, PPE note, or borrowings note.** The only rent-adjacent line is "Rent, Rates
and Taxes" ₹12.77 Lakhs inside Other Expenses (Note 23, Office Administrative Expenses, p.78).
This implies either (a) all leases qualify for the short-term/low-value exemption, or (b) a
disclosure gap. NOT FOUND IN DOCUMENT — ROU asset, lease liability, discount rate. 🟡 Watch.

**Capitalisation threshold**: NOT FOUND IN DOCUMENT — no monetary threshold disclosed for
capitalising PPE additions.

**Impairment test assumptions (growth/discount rates)**: NOT FOUND IN DOCUMENT — no goodwill on
the balance sheet (subsidiary investment carried at cost ₹0.50 Lakhs, Note 2.1, immaterial); no
impairment indicators or testing disclosed for PPE/intangibles despite the fire event.

**First-time standard adoptions**: None disclosed this year; Ind AS basis is continuing from
incorporation (Note A, Corporate Information, p.60).

---

## 2. RELATED PARTY TRANSACTIONS

**Full list of related parties** (Note 31.1/31.2, p.81/117): subsidiary Aarti HPC Limited
(100%, w.e.f. 26 Dec 2019); Non-Executive/Executive Directors (Chandrakant V. Gogri, Nikhil P.
Desai, Dattatray S. Galpalli, Santosh M. Kakade, Mulesh M. Savla, Misha B. Gala); Company
Secretary (Prashant Gaikwad); CFO (Nitesh Medh); Aarti Surfactants Limited Employees Group
Gratuity Scheme (Post Employment Benefit Trust).

**Transactions table** (Note 31.3, p.82, standalone; consolidated Note 31.2, p.117 — figures
identical because eliminations wash out the tiny subsidiary):

| Party/nature | FY2020-21 (₹ Cr) | FY2019-20 (₹ Cr) | YoY % |
|---|---|---|---|
| KMP remuneration paid | 1.170 | 0.748 | +56.4% |
| KMP sitting fees | 0.0125 | 0.0038 | +229% |
| Investment in Aarti HPC Ltd | Nil | 0.005 | n/a |
| Advance to Aarti HPC Ltd | Nil | 0.0075 | n/a |
| Post-employment trust contribution | 0.190 | Nil | new |

RPT as % of FY21 revenue (₹465.77 Cr): ≈ 0.29% (KMP remuneration + sitting fees + trust
contribution) — low. 🟢 Clean on quantum.

**KMP remuneration detail** (Corporate Governance Report, p.32): Nikhil P. Desai (MD) — Salary
& perquisites ₹60 Lakhs, Total ₹60 Lakhs; Santosh M. Kakade (ED) — ₹28 Lakhs, Total ₹28 Lakhs.
Director's Report / Notice Item 5 (p.121–122) discloses a **post-year-end** revision: from
April 1, 2021, MD Nikhil Desai's package moves to Salary ₹66 Lakhs p.a. + Commission 0.5% of Net
Profit; ED Santosh Kakade's to Salary ₹31 Lakhs p.a. + Commission 0.1% of Net Profit — i.e.
executive pay is being re-linked to net profit for the first time, in the same year profit grew
>10x off a low base. 🟡 Watch — profit-linked commission introduced right after a low-base
earnings jump; monitor whether reported profit growth sustains or was a one-off normalisation.

**Advance to Related Party**: Note 7 (Other Current Financial Assets, p.71) carries "Advance to
Related Party (Refer Note No.31)" of ₹0.75 Lakhs, flat both years — **no interest rate or
tenure disclosed** for this related-party advance (task requires rate/tenure for
loans/ICDs to related parties). NOT FOUND IN DOCUMENT — rate/tenure on this advance.

**Undisclosed counterparty for a new ₹820 Lakh Inter Corporate Deposit**: Note 11 (Non-Current
Borrowings, p.72/108) shows a new line "Inter Corporate Deposit ₹820.00 Lakhs" (PY: Nil), with
repayment terms given (Note 11.3: ₹824.48 Lakhs due 1–2 years — note this figure includes the
car loan too) but **no lender name or relationship disclosed anywhere**, and it does **not**
appear in the Related Party note (31). Whether this ICD is from a promoter entity, group
company, or an unrelated NBFC/institution is NOT FOUND IN DOCUMENT. 🟡 Watch — given the promoter
group runs multiple listed/private "Aarti" entities (Aarti Industries Ltd is the demerged
parent; Valiant Organics Ltd shares two common directors — Mulesh Savla and Dattatray Galpalli,
per Corporate Governance Report p.26), an undisclosed-counterparty ICD warrants a management
question.

**No RPTs with promoters beyond KMP pay**: Directors' Report (p.15) and Corporate Governance
Report (p.37) both state: "no materially significant related party transactions... which may
have potential conflict of interest," and "all related party transactions... were on arm's
length basis." 🟢 Clean on this specific representation, but see the ICD gap above.

---

## 3. CONTINGENT LIABILITIES

**Note 27 table** (Contingent Liabilities and Commitments, p.79/115, standalone = consolidated):

| Item | FY2020-21 (₹ Cr) | FY2019-20 (₹ Cr) |
|---|---|---|
| Claims against Co. not acknowledged as debt — Unpaid | 8.8401 | 10.0202 |
| Claims against Co. not acknowledged as debt — Paid (under dispute) | 2.6042 | 2.5054 |
| Letter of Credit, Bank Guarantees | 0.1174 | Nil |
| **Contingent liabilities subtotal** | **11.5617** | **12.5256** |
| Commitments (capital, net of advances) | 3.0824 | 0.7500 |
| **Total (Note 27)** | **14.6441** | **13.2756** |

As % of standalone net worth (₹132.66 Cr): contingent-liability-only portion (excl.
commitments) ≈ **8.72%** of net worth — below the 10% single-item threshold the task flags,
but close to it, and Note 27 itself gives **no breakdown by nature** (tax type, forum, dispute
stage). 🟡 Watch.

**Composition is disclosed elsewhere, not in Note 27 itself** — cross-reference from CARO
Annexure A to the Standalone Auditors' Report (p.52–53): disputed statutory dues are Customs
Duty ₹670.86 Lakhs (Commissioner of Customs, relates to FY2016-17), VAT ₹151.61 Lakhs
(Commissioner Appeals, FY2011-12 to FY2015-16), Entry Tax ₹53.33 Lakhs (Appellate Board –
Commercial Taxes, FY2010-11, FY2011-12, FY2015-16, FY2016-17). Sum = ₹875.80 Lakhs, closely
matching the "Unpaid" contingent liability line of ₹884.01 Lakhs in Note 27. No guarantees for
subsidiaries appear (the ₹0.1174 Cr LC/BG line is generic, not subsidiary-related). 🟡 Watch —
the fact that dispute composition lives only in the CARO annexure and not in Note 27 itself is
a disclosure-location gap, not a substance gap, but a downstream stage relying on Note 27 alone
would miss it.

---

## 4. TRADE RECEIVABLES

**Note 5** (Current Financial Assets – Trade Receivables, p.70/106):

| | FY2020-21 (₹ Cr) | FY2019-20 (₹ Cr) | YoY % |
|---|---|---|---|
| Less than six months (unsecured, considered good) | 54.3327 | 17.5121 | +210.2% |
| More than six months — unsecured, considered good | 0.0993 | 0.4078 | -75.6% |
| More than six months — unsecured, doubtful | 0.6997 | 0.6997 | 0% |
| Provision for doubtful debts | (0.6997) | (0.6997) | 0% |
| **Net Trade Receivables** | **54.4320** | **17.9199** | **+203.7%** |

Revenue grew only **+42.9%** (₹465.77 Cr vs ₹325.86 Cr) over the same period. Computed
receivable days: FY21 ≈ **42.6 days** (54.432/465.77×365); FY20 ≈ **20.1 days**
(17.9199/325.864×365) — **receivable days roughly doubled** year-on-year. 🔴 Red Flag —
receivables growing at ~4.8x the rate of revenue is a material deterioration in cash
conversion and the single largest quantitative finding in these notes.

No ageing schedule finer than the ">6 months" bucket is given (task asks for a full ageing
schedule — NOT FOUND IN DOCUMENT beyond the two buckets shown). No single-customer receivable
concentration is disclosed (only revenue concentration, see Section 11). No related-party
receivables. ECL provision is static despite the underlying base tripling (see Section 1) —
provisioning has not scaled with growth, worth flagging as adequacy concern. 🔴 Red Flag
(compounds with the receivable-days finding) — **feeds FLAG-CASH**.

---

## 5. INVENTORY

**Note 4** (Current Assets – Inventories, p.69/105):

| Category | FY2020-21 (₹ Cr) | FY2019-20 (₹ Cr) | YoY % |
|---|---|---|---|
| Raw Materials & Components (incl. transit) | 33.8295 | 23.3090 | +45.1% |
| Work-in-Progress | 1.9599 | 1.0317 | +90.0% |
| Finished Goods (incl. transit) | 34.6767 | 30.8329 | +12.5% |
| Stores and spares | 1.7447 | 0.8014 | +117.7% |
| Fuel (incl. transit) | 0.4325 | 0.1731 | +150.0% |
| Packing Materials | 0.5465 | 0.3403 | +60.6% |
| **Total** | **73.1898** | **56.4884** | **+29.6%** |

Total inventory growth (+29.6%) trails revenue growth (+42.9%) — inventory turns improved.
Finished Goods specifically grew only +12.5% against +42.9% revenue growth, which is a
favourable divergence (goods moving faster than they are being produced/stocked). 🟢 Clean —
no red flag on inventory efficiency, in contrast with receivables.

**Goods in Transit** (Note 4.1, p.69/105): Raw Materials ₹4.1038 Cr (PY ₹1.2153 Cr), Finished
Goods ₹2.3345 Cr (PY Nil) — Finished Goods in transit going from zero to ₹2.33 Cr is consistent
with the near-tripling of export sales (see Section 11) rather than a red flag on its own.

No write-downs to NRV, no obsolete-inventory disclosure, no inventory-days trend beyond the two
years shown (3-year trend NOT FOUND IN DOCUMENT — this is only a 2-year annual report).

---

## 6. INVESTMENTS

**Note 2** (Non-Current Financial Assets – Investments, p.69/105): Aarti HPC Limited (100%
subsidiary, unquoted equity, at cost) ₹0.50 Lakhs, unchanged; SVC Co-operative Bank Limited
(unquoted equity) ₹0.03 Lakhs, unchanged. No JVs. No impairment recognised on the subsidiary
investment despite the subsidiary carrying **negative net worth** (Reserves & Surplus
₹(1,18,375), i.e. accumulated loss exceeds the ₹50,000 paid-up capital — Annexure A/Form AOC-1,
p.19) — the ₹0.50 Lakh cost basis is de minimis so this is immaterial, but technically the
investment is carried above the subsidiary's book net worth with no stated impairment
assessment. 🟡 Watch (immaterial in ₹ terms, noted for completeness). No ICDs/loans to
subsidiaries beyond the flat ₹0.75 Lakh advance already noted in Section 2. No unrealised
gains/losses on other investments (SVC Bank shares are at cost, not FVTOCI).

---

## 7. BORROWINGS

**Note 11** (Non-Current Financial Liabilities – Borrowings, p.72/108):

| Instrument | FY2020-21 (₹ Cr) | FY2019-20 (₹ Cr) |
|---|---|---|
| Term Loans from Banks (secured) | 67.00 | 30.00 |
| Less: Current Maturity | (6.00) | Nil |
| Car Loan from Banks | 0.0713 | 0.0866 |
| 0% Non-Convertible Redeemable Preference Shares | 19.4188 | 18.6927 |
| Inter Corporate Deposit (counterparty undisclosed — see Sec. 2) | 8.20 | Nil |
| **Total Non-Current Borrowings** | **88.6901** | **48.7793** |

**Security**: Term loan secured by first charge on all movable/immovable assets, including
current assets (Note 11.1a). Same first-charge security backs the Current Borrowings (WC loan,
Note 13.1). **Entire movable/immovable PPE is charged to SVC Co-operative Bank Limited and
HSBC Bank** (PPE Note 1, footnote a, p.67/103) — same bank (SVC) the Company also holds a
minority equity stake in (Note 2) and banks with (Corporate Information, p.1) — a related-party-
adjacent banking relationship worth noting though not itself irregular.

**Repayment schedule** (Note 11.2, Term Loan, p.73/109): 1–2yr ₹12.00 Cr, 2–3yr ₹14.00 Cr,
3–4yr ₹14.00 Cr, Beyond 4yr ₹27.00 Cr. No covenant terms, covenant breaches, or waivers are
disclosed anywhere in Notes 1–33 — NOT FOUND IN DOCUMENT (task asks explicitly for covenant
breach/waiver disclosure).

**0% Redeemable Preference Shares — quasi-equity instrument**: Note 11.1(b) explains these are
0% Cumulative, Non-Convertible, Non-Participating Preference Shares issued to shareholders of
demerged entity Aarti Industries Limited at fair value of ₹167/share pursuant to the Scheme of
Arrangement; redeemable **at the Company's option**; holders get a 4% annualised return on the
₹167 fair value (i.e., accretion, not a coupon paid in cash — carrying value grows from ₹1,869.27
Lakhs to ₹1,941.88 Lakhs, a ~3.9% increase consistent with 4% accretion). Voting rights limited
to resolutions directly affecting preference shareholders' interest. 🟡 Watch — an accreting,
company-optional-redemption instrument sitting in Borrowings (debt) rather than equity, issued
to the promoter-linked demerged parent's shareholders, inflates reported leverage optics but its
economic substance (no fixed maturity forced by holders, no cash coupon) is closer to preferred
equity. Net Gearing Ratio (Note 32.1) of 1.09x includes this instrument as part of Gross Debt.

**Fixed vs floating**: NOT FOUND IN DOCUMENT — no explicit fixed/floating breakdown for the
term loan or WC facility.

**Related party borrowings**: None disclosed as such (the ICD counterparty gap in Section 2
means this cannot be fully ruled out).

---

## 8. TRADE PAYABLES

**Balance Sheet / Note 14 area** (standalone Balance Sheet, p.56; consolidated, p.92): Trade
Payables Due to "Other Than Micro and Small Enterprises" — ₹78.1067 Cr (FY21) vs ₹19.2441 Cr
(FY20), **+305.9%**, against COGS (Cost of Materials Consumed, Note 19) growth of only +43.4%
(₹356.1536 Cr vs ₹248.3793 Cr). Computed payable days: FY21 ≈ **80.1 days** (78.1067/356.1536×
365); FY20 ≈ **28.3 days** (19.2441/248.3793×365) — **payable days nearly tripled**. 🔴 Red Flag
— combined with the receivable-day doubling in Section 4, this is a second, larger working-
capital signal; the Company appears to be stretching suppliers materially while also letting
customers stretch it, which nets out favourably for near-term cash (Cash Flow Statement shows
Trade Payables & Other Current Liabilities contributing +₹62.389 Cr to Cash Generated from
Operations, p.59) but raises questions about sustainability and about whether purchase timing
(e.g., large raw-material buys near year-end) is inflating the payables balance.

**MSME disclosure** (Note 28, p.79/115): "There are no Micro, Small and Medium Enterprises...
to whom the Company owes dues... accordingly no additional disclosures have been made. The
above information... has been determined to the extent such parties have been identified on the
basis of information available with the Company." 🟡 Watch — this is a soft, "as far as we
know" disclosure with no evidence of active MSME-status verification of vendors, paired with a
trade payables balance that nearly tripled; no interest-on-delayed-MSME-payment disclosure
(consistent with claiming zero MSME dues, but the qualifier language keeps this a watch item
rather than clean).

---

## 9. PROVISIONS

**Note 15** (Current Provisions, p.74/109): Provision for Employee Benefits ₹2.3853 Cr (PY
₹1.5814 Cr); Other Provisions ₹0.97 Cr (PY ₹2.4376 Cr).

**Note 15.1** (Movement in Other Provisions, p.74/109): Opening (FY20) ₹0.0314 Cr →
Recognised ₹2.4828 Cr → Utilised ₹(0.0766) Cr → Balance FY20 ₹2.4376 Cr → Recognised (FY21)
₹1.5952 Cr → Utilised ₹(3.0629/3.0628) Cr → Balance FY21 ₹0.97 Cr. **The nature of "Other
Provisions" is never disclosed** — not warranty, not litigation, not decommissioning, not
onerous contracts by name; task-required categorisation is NOT FOUND IN DOCUMENT. 🟡 Watch — a
provision that saw ₹2.48 Cr recognised and ₹3.06 Cr utilised in two years without any
description of what it covers is a disclosure gap worth a management question, though the
absolute amounts are small.

**Employee benefit — Gratuity (funded)** (Note 21.1, p.76–77/112–113): Defined Benefit
Obligation ₹1.1566 Cr (PY ₹1.0163 Cr); Fair value of plan assets ₹0.9466 Cr (PY ₹0.7826 Cr);
net unfunded liability ₹0.2101 Cr (PY ₹0.2337 Cr) — funded status **improved slightly**.
Actuarial assumptions: Discount rate 6.80% (PY 6.84%); Expected return on plan assets 6.80% (PY
6.84%); Salary escalation 5.00% (PY **7.00%** — lowered materially); Employee turnover 5.00%
(unchanged). 🟡 Watch — lowering the salary-escalation assumption from 7% to 5% reduces the
projected obligation (all else equal); this contributed to a ₹(24.65) Lakh actuarial gain "due
to change in financial assumptions" that was partly offset by a +₹8.82 Lakh actuarial loss "due
to experience." 100% of plan assets invested with LIC (Group Gratuity Cash Accumulation
Policy). Leave encashment liability ₹78.95 Lakhs (PY ₹100.31 Lakhs), unfunded, provided
directly in the books (Note 21.1, footnote, p.77/113).

No litigation provisions disclosed by name/case.

---

## 10. DEFERRED TAX

**Note 12** (Deferred Tax Liability (Net), p.73/109):

| | FY2020-21 (₹ Cr) | FY2019-20 (₹ Cr) |
|---|---|---|
| At start of year | 8.1360 | 7.2769 |
| Charge/(credit) to P&L | 0.7795 | 0.8591 |
| MAT Credit Entitlement | Nil | (0.5154) |
| At end of year | 8.9155 | 7.6206 |

Components (Note 12.1): DTL on PPE ₹12.6088 Cr (PY ₹12.6517 Cr); DTA on Carried Forward Tax
Losses ₹(3.6933) Cr (PY ₹(4.5157) Cr) — **tax-loss DTA is shrinking**, consistent with the
Company now being profitable and utilising losses; MAT Credit Entitlement Nil (PY, a DTA of
₹(0.5154) Cr, fully utilised this year). Net DTL ₹8.9155 Cr.

**No effective-vs-statutory tax rate reconciliation is disclosed anywhere in Notes 1–33.** NOT
FOUND IN DOCUMENT — this is a standard Ind AS 12 disclosure item and its absence is a genuine
gap (task item 10 explicitly requires it). Current Tax charge for FY21 is only ₹0.50 Cr on Profit
Before Tax of ₹22.92 Cr — an effective current-tax rate of ~2.2%, almost certainly driven by
brought-forward tax losses being set off, but this cannot be confirmed/reconciled without the
missing rate reconciliation. 🟡 Watch. MAT credit utilisation timeline: NOT FOUND IN DOCUMENT
beyond the single-year "entitlement" line. Unrecognised DTA and reasons: NOT FOUND IN DOCUMENT.

---

## 11. REVENUE DETAILS

**Note 17** (Revenue from Operations, p.75/110):

| | FY2020-21 (₹ Cr) | FY2019-20 (₹ Cr) | YoY % |
|---|---|---|---|
| Local Sales | 332.1763 | 266.9814 | +24.4% |
| Export Sales | 131.0966 | 53.4406 | +145.3% |
| Sales of Products (Net of GST) | 463.2729 | 320.4220 | +44.6% |
| Other Operating Revenues (Note 17.1) | 2.4974 | 5.4420 | -54.1% |
| **Total Revenue from Operations** | **465.7703** | **325.8640** | **+43.0%** |

Export sales nearly tripling and outgrowing domestic sales by ~6x rate is the single largest
top-line driver and matches the near-tripling of Export Freight expenses (Section on Other
Expenses) and Goods-in-Transit Finished Goods appearing from zero. 🟢 Clean, well-corroborated
across multiple notes (a good internal-consistency signal).

**Note 17.1** (Other Operating Revenues, p.75/111): Export Benefits/Incentives ₹0.9564 Cr (PY
₹0.9008 Cr); Scrap Sales ₹0.3304 Cr (PY ₹0.3624 Cr); State Government Grant – Industry Promotion
Incentive ₹1.2106 Cr (PY ₹4.1788 Cr, **-71.0%**) — a large drop in a government subsidy line
worth noting given it flows through revenue rather than a below-the-line grant.

**Segment disclosure is minimal** (Note 30, p.80–81/116): Company self-declares a **single
reportable segment** ("Home and personal care ingredients") despite the MD&A (p.4–5) describing
a diverse product portfolio spanning Surfactants, Mild Surfactants, UV Blocker, Preservatives,
Pearlising Agent, and Blends across Home Care, Hair Care, Skin/Personal Care, Oral Care, Baby
Care, and Industrial Applications end-markets. Revenue is disaggregated only by geography
(Within India ₹332.18 Cr / Outside India ₹131.10 Cr) — **no product-line revenue breakdown**
despite the apparent internal diversity. 🟡 Watch — single-segment reporting for a genuinely
multi-product chemical manufacturer is a low-disclosure-granularity choice; it is permissible
under Ind AS 108 if that is genuinely how the CODM reviews the business, but it limits investor
visibility into which product lines are actually driving the 43% revenue growth.

**Customer concentration**: Note 30 (p.81/116): "Company's total Revenue of ₹46,327.29 Lakhs
(P.Y. ₹32,042.20 Lakhs) include sales of ₹16,235.00 Lakhs (P.Y. ₹19,385.00 Lakhs) to two large
customers with whom the company is having long standing Relationship." That is **35.0%** of
FY21 sales concentrated in two unnamed customers (down from 60.5% in FY20, so concentration is
*improving* even as the absolute customer-revenue dollar amount fell slightly). Customer names
NOT FOUND IN DOCUMENT (not required to be disclosed under Ind AS 108, but a task item). No
contract assets/liabilities or unsatisfied performance obligations disclosure — NOT FOUND IN
DOCUMENT (consistent with point-in-time revenue recognition on dispatch, so likely N/A, but
not explicitly stated as N/A either).

---

## 12. OTHER CRITICAL NOTES

**Other Expenses** (Note 23, p.76–78/112–114): Total ₹53.1623 Cr (PY ₹40.6590 Cr, +30.7%).
Notable line items: Export Freight Expenses/Outward Freights ₹13.5031 Cr (PY ₹4.8462 Cr,
**+178.6%**, consistent with the export sales surge); Effluent Treatment Cost ₹0.6233 Cr (PY
₹1.7265 Cr, **-63.9%**) — a large decline in an environmental-compliance cost line worth a
question given the Company's own MD&A emphasis on effluent treatment/GMP investment (p.12);
Donations and CSR Expenses (Non-Operating) ₹0.2023 Cr (PY ₹0.015 Cr) — see CSR note below.

**CSR — voluntary spend despite stated non-applicability**: Director's Report (p.13) states the
Company "did not fall in the criteria mentioned under Section 135... for applicability of the
provisions of Corporate Social Responsibility" and so was "not required to constitute a CSR
Committee." Yet Note 29 (Corporate Social Responsibility, p.79/115) discloses ₹19.65 Lakhs of
CSR-styled spend (Free Medical Equipment ₹12.10 Lakhs, COVID-19 Donation ₹5.00 Lakhs,
Preventive Healthcare ₹2.55 Lakhs), with "Amount required to be spent as section 135 of the
act" shown as **Nil**. 🟢 Clean/immaterial — this is voluntary philanthropic spend, correctly
labelled as not statutorily mandated; no discrepancy, just worth noting the Company still chose
to disclose it under a "CSR" heading.

**EPS / dilution**: Note 25 (p.76/114): Basic = Diluted EPS both years (₹28.53 standalone /
₹28.52 consolidated FY21; ₹2.76 / ₹2.75 PY) — **no dilutive instruments** (Total weighted
average potential equity shares = Nil both years), so no ESOP or convertible dilution to model.
🟢 Clean, simple capital structure for EPS purposes (though note the accreting preference shares
in Borrowings, Section 7, which are debt-classified and hence don't dilute EPS but do carry a
real economic cost via the 4% accretion).

**Standalone-vs-consolidated small gap**: Consolidated EPS (₹28.52) is one paisa below
Standalone EPS (₹28.53) — driven by the dormant subsidiary's own small loss (₹(68,375), i.e.
₹0.0068 Cr) flowing through consolidation; immaterial.

**Foreign currency exposure / hedging**: Note 33.B(a)(i) (Financial Risk Management, p.83/119):
"The Company's exposure to the risk of changes in foreign exchange rates relates primarily to
the Company's operating activities in exports and imports which is majorly in US dollars. In
case of Long term Contract with Large Customer, Currency Fluctuation is to Customer's
Account." 🟡 Watch — this is purely qualitative; **no quantified net FX exposure, no forward
contracts/hedge instruments, and no sensitivity analysis are disclosed**, despite Export Sales
of ₹131.10 Cr and Foreign Exchange Outgo of ₹28.20 Cr (Annexure C, p.24) — a meaningful USD
book with apparently no formal hedging programme beyond passing risk to one large customer
contractually. NOT FOUND IN DOCUMENT — quantified FX exposure, hedge positions, sensitivity.

**Events after balance sheet date**: Director's Report (p.16) states "There are no other
material changes and commitment affecting the financial position of the company... between the
end of the Financial Year... and the date of the report" — but the same Annual Report's Notice
(Item 5, p.121–122) discloses a **post-year-end executive remuneration revision effective April
1, 2021** (see Section 2) that is not flagged as a subsequent event in the financial statements
themselves. 🟡 Watch — minor internal inconsistency in what counts as a "material" post-year-end
change.

**Direct debits/credits to reserves bypassing P&L**: Note 10 (Other Equity, p.72/108) and the
Statement of Changes in Equity (p.58) show, in the **prior year (FY19-20)** only, large
non-P&L reserve movements from the 2019 demerger scheme (Reserves Pending Allocation
transferred to Retained Earnings ₹79.0711 Cr; Gain on Disposal of Investment in Equity Shares
through OCI transferred to Retained Earnings ₹22.1579 Cr). **No such non-P&L reserve movements
occur in the current FY2020-21 year** — Other Equity movements in FY21 are limited to Profit for
the year (₹21.6413 Cr) and Remeasurement of defined benefit plans, net of tax (₹0.0661 Cr),
both legitimate OCI/P&L items. 🟢 Clean for the year under review; the large one-off
reserve reclassifications are a prior-year (demerger-related) event, not a current-year
red flag, though they explain why FY19-20 is a poor comparison base for equity-based ratios.

**Title deeds not in Company's name — CARO qualification**: CARO Annexure A to the Standalone
Auditors' Report (p.52, item i.c): "In respect of immovable properties taken on lease and
disclosed as property, plant and equipment... the lease agreements are in the name of the
company, except Plot No 62,63,64,57,61, 62A and S-3/1 at Pithampur, Madhya Pradesh (Aggregate
book value ₹267.80 lakhs) are in the name of demerged Company (Aarti Industries Limited).
According to explanation obtained from management, in view of the demerger through court
scheme, leasehold rights are deemed to be transferred to the Company in the name of the Company
is yet to be completed." 🟡 Watch — a legal title-transfer formality still pending nearly two
years after the demerger became effective (2019), against PPE with book value ₹2.68 Cr. Low
dollar amount but a genuine legal-risk item an equity analyst should track to closure.

**Auditor opinion — clean, both standalone and consolidated**: Both Independent Auditors'
Reports (p.48–51 standalone; p.86–89 consolidated) are **unmodified/unqualified**, with a single
Key Audit Matter each (PPE/CWIP capitalisation and useful-life judgement, and — per the
standalone auditor — borrowing-cost capitalisation verification). No fraud reported by or on the
Company (CARO Annexure A item x, p.53). No qualifications per the Corporate Governance Report's
own disclosure table (p.38: "Audit Qualifications — The Company's financial statement for the
year 2020-21 is unmodified"). 🟢 Clean.

**Dividend — first-ever, proposed amid rising leverage and stretched working capital**: Note
32.2 (p.83/117): Final Dividend of ₹3/share (30% of face value) proposed for FY2020-21 (PY:
Nil) = ₹227.53 Lakhs cash outflow if approved (Director's Report, p.13). This is the Company's
**first dividend since listing** (14 July 2020), proposed in the same year that: Net Gearing
Ratio rose from 0.98x to 1.09x (Note 32.1, p.82/117, Gross Debt +39.1% YoY to ₹151.94 Cr);
receivable days doubled; and payable days nearly tripled. 🟡 Watch — not a red flag per se
(dividend is modest relative to ₹21.64 Cr net profit, a ~10.5% payout), but a capital-allocation
data point worth weighing against the working-capital deterioration above.

---

## PASS 1 SUMMARY — TOP 10 MOST SIGNIFICANT FINDINGS

| Rank | Finding | Note Anchor | Rating | Why it matters |
|---|---|---|---|---|
| 1 | Document is FY2020-21 (year ended 31 Mar 2021), not FY2022; ~5.3 years stale vs 2026-08-04 run date; no later AR supplied | Cover/Directors' Report p.13; all FS headers | 🔴 Red Flag | Every downstream valuation/trend stage built on this document is working with financials over five years old — a structural data-currency risk for the whole run, independent of company quality |
| 2 | Trade receivables +203.7% YoY vs revenue +43.0%; receivable days ~doubled (20.1→42.6 days); ECL provision static despite tripling of the base | Note 5, p.70/106 | 🔴 Red Flag | Largest quantitative deterioration signal in the notes; feeds FLAG-CASH |
| 3 | Trade payables +305.9% YoY vs COGS +43.4%; payable days nearly tripled (28.3→80.1 days) | Balance Sheet/Note 14 area, p.56/92 | 🔴 Red Flag | Second, larger working-capital swing; combined with #2, signals the Company is materially stretching both sides of the cash conversion cycle in the same year it declared its first dividend |
| 4 | First-year borrowing-cost capitalisation (₹101.84 Lakhs, PY Nil), flagged as Key Audit Matter by both standalone and consolidated auditors | Note 22, p.78/114; Note 1(c) p.67/103 | 🟡 Watch | New accounting choice that understates finance cost/overstates profit in the same year profit rose >10x off a low base |
| 5 | Fire loss at Silvassa plant (₹158.18 Lakhs gross, ₹78.01 Lakhs NBV) netted directly against Gross Block/Depreciation rather than run through P&L as a loss; ₹360.89 Lakhs insurance receivable booked with no matching P&L recognition yet | Note 1(b) p.67/103; Note 7 p.71/106 | 🟡 Watch | Unusual presentation of an asset-destruction event; insurance recovery accounting not yet reconciled |
| 6 | Undisclosed counterparty for new ₹820 Lakh Inter Corporate Deposit; not named in Related Party note despite promoter group running multiple affiliated entities | Note 11, p.72/108; Note 31, p.81/117 | 🟡 Watch | Related-party-adjacent lending gap; cannot confirm arm's length nature |
| 7 | Title deeds for PPE with book value ₹267.80 Lakhs (Pithampur plots) still registered in demerged parent Aarti Industries Limited's name, ~2 years post-demerger | CARO Annexure A, p.52 (cross-refs Note 1/27) | 🟡 Watch | Ongoing legal title-transfer risk on owned/leased manufacturing assets |
| 8 | No effective-vs-statutory tax rate reconciliation disclosed anywhere; ~2.2% effective current tax rate on ₹22.92 Cr PBT cannot be independently verified against brought-forward losses | Note 12, p.73/109 | 🟡 Watch | Standard Ind AS 12 disclosure missing; limits DTA/tax-sustainability analysis |
| 9 | Single-segment reporting despite a genuinely diverse product portfolio (surfactants, UV blockers, preservatives, pearlising agents, blends); no product-line revenue disaggregation | Note 30, p.80–81/116 | 🟡 Watch | Limits visibility into which products actually drove the 43% revenue growth |
| 10 | 0% Redeemable Preference Shares (₹1,941.88 Lakhs, accreting at 4% p.a., company-optional redemption, issued to demerged-parent shareholders) classified within Borrowings/Gross Debt | Note 11.1(b), p.72/108; Note 32.1, p.82/117 | 🟡 Watch | Quasi-equity instrument inflates reported leverage (Net Gearing 1.09x) versus its economic substance |

---

## HANDOFF TO PASS 2

Pass 1 covered Notes 1–33 (standalone and consolidated) sequentially, plus the Standalone and
Consolidated Independent Auditors' Reports and CARO Annexures. Areas flagged as thin and worth
a dedicated second look in Pass 2: sub-notes/footnotes within Notes 1, 11, and 21 (already
mined but worth a re-check for missed cross-references); any qualitative management-judgment
language embedded in the accounting policy notes (B.1–B.3, pp.60–66/96–102) not yet fully
mined; the Corporate Governance Report and CARO Annexure A/B for any further cross-references
into the numbered notes; and a check for internal contradictions between the Directors' Report
narrative (e.g., "no material post-year-end changes") and Notice/Annexure disclosures (e.g.,
the executive remuneration revision) already surfaced in Section 12 above.

```yaml
stage: B02-notes
company: "AARTISURF"
run_date: "2026-08-04"
model: claude-sonnet-5
pass: 1
status: complete
input_gaps:
  - "Annual report supplied is FY2020-21 (year ended 31 March 2021), not FY2022 as characterized in task brief; document is ~5.3 years stale vs 2026-08-04 run date, not ~4 years"
  - "No effective-vs-statutory tax rate reconciliation disclosed (Note 12)"
  - "No quantitative ECL matrix/default-rate table disclosed for trade receivables"
  - "No Ind AS 116 ROU asset, lease liability, or discount rate disclosed anywhere despite full lessee/lessor policy language"
  - "No covenant terms, breaches, or waivers disclosed for term loan/WC facility"
  - "No counterparty/relationship disclosed for new ₹820 Lakh Inter Corporate Deposit (Note 11)"
  - "No interest rate/tenure disclosed for ₹0.75 Lakh related-party advance (Note 7/31)"
  - "No quantified FX exposure, hedge positions, or sensitivity analysis (Note 33), despite meaningful export book"
  - "Nature of 'Other Provisions' (Note 15.1) never described (not warranty/litigation/decommissioning by name)"
  - "No product-line revenue disaggregation despite single-segment reporting for a multi-product portfolio (Note 30)"
preliminary_flags:
  - {type: FLAG-CASH, reason: "Trade receivables +203.7% YoY vs revenue +43.0% (receivable days ~doubled, 20.1 to 42.6 days) and trade payables +305.9% YoY vs COGS +43.4% (payable days nearly tripled, 28.3 to 80.1 days); both in Notes 5 and Balance Sheet, pp.70/56"}
top_findings_count: 10
notes_covered: "1-33 standalone and consolidated, full sequential read"
pass_2_next: true
```
