# STAGE 2 — NOTES TO FINANCIAL STATEMENTS — PASS 2 OF 3 (WHAT WAS MISSED)
Company: KCPSUGIND (K.C.P. Sugar and Industries Corporation Ltd)
Run date: 2026-07-21
Source: Annual Report FY2024-25 (year ended 31.03.2025), text cache of Annual_Report.pdf
Cache path: runs/kcpsugind-2026-07-21/inputs/_textcache/Annual_Report.txt
Scope: Standalone Notes 1-76 (AR pp.90-129), re-read in full a second time against the Pass 1
output. Only items NOT already reported in Pass 1 are listed below. Coverage caveats
(pp.151-275 and p.2 scanned, NOT AVAILABLE) carry over unchanged from Pass 1.

---

## NOTE-BY-NOTE RE-CHECK LOG (abbreviated — full coverage confirmed, new items only extracted below)

Notes 1-2 (Corporate info, Accounting policies): re-read in full; no new quantified items beyond
Pass 1. Confirmed Note 2(c) critical-estimates list explicitly names "turnover and earnings
multiples, growth rates and net margins... risk-adjusted discount rate" as impairment inputs
used qualitatively — still no numeric rates disclosed (consistent with Pass 1's NOT FOUND).
Notes 3-5: new items below (PP&E deletions detail, CWIP ageing, Note 17.3/17.4 shareholding).
Notes 6-16: multiple new items below (Notes 6, 7, 14, 15, 16).
Notes 17-28: new items below (Notes 17.3-17.4, 20, 25, 26, 28).
Notes 29-36: new items below (Note 30 agricultural land gain, Note 33 remuneration
cross-check, Note 34 borrowing-cost split, Note 36 arithmetic anomaly + two new P&L lines).
Notes 37-44: new items below (Notes 37-38 confirmatory, Note 44 production volumes).
Notes 45-51: fully re-checked, no new items beyond Pass 1 (contingent liability table,
MSME, financial instruments, risk management, gratuity, leave encashment all previously
captured in full detail).
Notes 52-54: fully re-checked; new item below (Note 33/53(B)/54 remuneration reconciliation).
Notes 55-71: entirely NEW to this pass — Pass 1 did not extract this block at all. See below.
Notes 72-76: new items below (Note 72 bank-stock reconciliation entirely missed in Pass 1;
Note 73 four ratios not extracted in Pass 1 — DSCR, RoCE, ROI, Net Capital Turnover; Note 76
segment table — Chemicals/Power&Fuel segment results, capex, and PP&E-linked exceptional
gain quantification not extracted in Pass 1).

---

## NEW FINDINGS

### 1. Debt Service Coverage Ratio collapsed to 0.25x (Note 73, AR p.126) — 🔴 New Red Flag
Ratio table row 3: DSCR = 0.25 (FY25) vs 1.52 (FY24), a **-84% decline**. Numerator is
"Profit after tax + Interest + Depreciation + non-cash adjustments"; denominator is "Interest
on loans + principal repayment during the year for long-term loan." A DSCR below 1.0x means
FY25 cash-flow-proxy earnings did not cover the year's interest-plus-principal obligations —
consistent with the net loss year, but this is a harder, ratio-form confirmation of financing
stress that Pass 1's Debt/Equity-only lens (0.30x, deleveraging, rated 🟢) did not surface.
Investors should not read the Debt/Equity improvement in isolation; coverage deteriorated
sharply in the same year. Not previously reported in Pass 1.

### 2. Return on Capital Employed and Return on Investment both collapsed (Note 73, AR p.126-127) — 🟡 New Watch
- RoCE (EBIT / (Total Assets − Current Liabilities + Current Borrowings)): **0.03 (3%) FY25
  vs 0.18 (18%) FY24, -81%.**
- Return on Investment (income from investments / average investments): **0.05 (5%) FY25 vs
  0.27 (27%) FY24, -82%.**
- Net Capital Turnover Ratio (Net Sales / Working Capital): **1.58x FY25 vs 2.04x FY24, -22%.**
These three ratios were not extracted in Pass 1 (which covered only Current Ratio, D/E,
Inventory/Receivable/Payable turnover, and Net Profit Ratio from the same Note 73 table).
RoCE and ROI both quantify precisely how far capital efficiency fell this year — RoCE at 3%
is well below any reasonable cost of capital, and the ROI figure hard-numbers the investment
portfolio's return collapse that Pass 1 only described qualitatively via the P&L fair-value
gain line. Counterpoint: **Current Ratio improved to 2.80x (FY25) from 1.94x (FY24), +44%** —
liquidity position strengthened even as profitability/efficiency ratios weakened, worth
holding both facts together.

### 3. Note 36 "Other Expenses" — FY24 column contains an internal arithmetic inconsistency (AR p.113) — 🟡 New Watch (data-quality/OCR flag, not a company error)
Summing all sixteen FY24 line items as extracted from the source text (Power & Fuel 318.81,
Labour 176.04, Rental 2.00, Repairs-Buildings 50.58, Repairs-Machinery 807.75,
Repairs-Others 59.29, Insurance 39.95, Payment to auditors 8.11, Legal & Professional 54.11,
Selling expenses [as printed] 1,811.72, Provision for doubtful debt NIL, Assets written off
NIL, Director's sitting fees 9.80, CSR 21.38, Security charges 97.51, Miscellaneous 577.20)
gives ₹4,034.25 lakhs, which does not reconcile to the disclosed FY24 total of **₹2,437.24
lakhs** — a ₹1,597.01 lakhs gap. Reconciling to the stated total instead implies FY24
"Selling expenses" should be approximately **₹214.71 lakhs**, not the ₹1,811.72 lakhs as it
appears in the extracted text (all other fourteen line items sum cleanly with the total).
This is most likely a text-extraction/OCR artifact on the FY24 Selling Expenses cell rather
than a genuine reporting error — the FY25 column reconciles exactly (₹2,348.28 lakhs) — but
it is flagged because taking the raw OCR figure at face value would incorrectly suggest an
~88% YoY collapse in selling expenses, which is not supported once the total is used to
back-solve. **Recommend verifying this cell against the source PDF image (p.113) before using
it in any modelling.** Not previously reported in Pass 1.

### 4. Two new P&L expense lines in Note 36, both NIL in FY24, now non-zero in FY25 (AR p.113) — 🟡 New Watch
- **"Provision for Doubtful debt" (P&L charge): ₹36.00 lakhs FY25 vs NIL FY24.** This
  reconciles exactly to the increase in "Advances to Supplier (Considered Doubtful)" in
  Note 15 (₹4.27 lakhs FY24 → ₹40.27 lakhs FY25, a delta of ₹36.00 lakhs) — i.e. this is a
  **new doubtful-advance provision against a supplier, not against trade receivables** (the
  Note 10 trade receivable allowance stayed flat at ₹146.89 lakhs both years, per Pass 1).
  A supplier advance nearly 10x-ing in doubtful status (₹4.27L → ₹40.27L) with no narrative
  on the supplier or the underlying dispute is a fair management question.
- **"Assets Written off": ₹33.07 lakhs FY25 vs NIL FY24.** No further disclosure of which
  assets or the reason for write-off appears anywhere in Notes 1-76.
Neither line was reported in Pass 1's Provisions (section 9) or Inventory (section 5)
coverage.

### 5. Note 72 — Reconciliation between quarterly stock statements filed with banks and books of account (AR p.126) — entirely missed by Pass 1 — 🟢 New, Clean (explained)
All four quarters show the value of Finished Goods (Sugar & Molasses) **reported to the
consortium banks (SBI, ICICI, Axis, CTBC) exceeding the books-of-account value**: Q1
₹9,045.32L (bank) vs ₹8,799.38L (books), diff ₹245.94L; Q2 ₹4,926.17L vs ₹4,662.91L, diff
₹263.26L; Q3 ₹2,738.65L vs ₹2,454.49L, diff ₹284.16L; Q4 ₹9,562.38L vs ₹9,288.31L, diff
₹274.08L. Stated reason: banks value stock at 3-month moving average or market price
(whichever lower), while books use cost/NRV (whichever lower) per Ind AS. This is a
statutorily-required (CARO-linked) disclosure that Pass 1 did not extract at all. Rated
clean because the direction is conservative — books are lower than what is reported to
lenders in every quarter, i.e. no evidence of over-stating collateral value to books relative
to banks (the opposite direction would be the red flag). Still worth listing as new since it
directly answers a standard "notes contradict main statements" pattern-check question in
advance of Pass 3.

### 6. Note 44 — Actual production volumes fell sharply across every core product line (AR p.115) — new quantification not in Pass 1
Sugar production 214,236 Qtls (FY25) vs 368,680 Qtls (FY24), **-41.9%**; Molasses 14,951 MTs
vs 22,791 MTs, **-34.4%**; Industrial/Anhydrous Alcohol 1,160,610 BL vs 6,541,279 BL,
**-82.3%**; Electrical (incidental co-gen) power 14,352,500 Kwh vs 18,925,684 Kwh, **-24.2%**;
Bio Fertiliser 91,836 Qtls vs 81,052 Qtls, **+13.3%**; Urad Dal 45,985 Qtls vs 12,235 Qtls,
**+275.9%**. Licensed/installed cane-crushing capacity unchanged at 7,500 TCD both years — no
capacity change, purely a utilisation/output collapse in the core sugar and alcohol lines
(likely reflecting a shorter/lower-yield crushing season). This is the production-side mirror
of the revenue declines Pass 1 already flagged from Note 40 (sales value) — new because Pass 1
did not extract Note 44's physical output data, which confirms the decline is volume-driven,
not merely price/realisation-driven.

### 7. Note 76 Segment Reporting — additional segment-level detail not extracted in Pass 1 (AR p.128) — 🟡 New Watch
- **Chemicals segment also swung to a loss**: segment result (PBDIT basis) **-₹42.12 lakhs
  FY25 vs +₹59.20 lakhs FY24** — a second operating segment (beyond Sugar) turned
  loss-making this year.
- **Power & Fuel segment result fell 83% while staying positive**: **₹68.80 lakhs FY25 vs
  ₹408.33 lakhs FY24**, a material deterioration not previously quantified.
- **Total capital expenditure fell 36.1% YoY: ₹342.68 lakhs (FY25) vs ₹536.73 lakhs (FY24)**,
  and FY25 capex (₹342.68 lakhs) is now **below FY25 depreciation (₹514.01 lakhs, Note 35)**
  — a capex/depreciation ratio of ~0.67x, i.e. the company is investing below its rate of
  asset consumption this year. By segment, Chemicals capex fell hardest (₹264.01L → ₹84.26L,
  -68.1%) and Urad Dal received zero capex both years despite being the growth segment.
  This is a reinvestment-intensity signal relevant to the GARP/transition thesis that Pass 1
  did not surface (Pass 1 discussed segment revenue/result mix but not capital allocation).
- **PP&E note (Note 3, p.102) cross-check on the exceptional gain**: gross block deletions
  of ₹488.22 lakhs (Plant & Machinery) against accumulated-depreciation deletions of
  ₹454.34 lakhs implies a net book value of only **~₹33.88 lakhs** for assets disposed of
  during the year — consistent with, and quantifying, the ₹480.54 lakhs "Profit on sale of
  Lakshmipuram Plant and Machinery" exceptional gain that Pass 1 flagged qualitatively
  (finding #12/Other Critical Notes) but did not tie back to the PP&E movement schedule. The
  large gain-to-book-value ratio confirms the disposed asset was a near-fully-depreciated,
  low-carrying-value item — mechanically explains the gain size, not itself a red flag.
- Segment liabilities for Urad Dal are shown as **identical in both years (₹139.46 lakhs FY25
  and FY24)** — worth a source-verification flag given every other segment liability line
  moved YoY; could be a genuine coincidence or an extraction artifact.

### 8. Note 16 — Assets held for sale, ₹239.50 lakhs (FY25), no FY24 comparative shown (AR p.107-108) — 🟡 New Watch, forward-looking
Plant and Machinery of ₹239.50 lakhs is newly classified as held for sale at 31.03.2025 with
no prior-year comparative value presented (implying NIL at 31.03.2024, i.e. new this year).
Combined with the recurring "profit on sale of surplus plant" pattern Pass 1 already flagged
across two consecutive years (₹804.42L FY24, ₹480.54L FY25), this held-for-sale balance
signals a further exceptional gain is plausible in FY26 — useful forward context for
normalising future-year "core" earnings that Pass 1 did not have visibility into.

### 9. Note 7 — "Deposit made as per Court Order," ₹403.48 lakhs, unchanged both years (AR p.106) — 🟡 New Watch
Other Non-Current Assets (Note 7) includes a ₹403.48 lakhs deposit made as per Court Order,
static across FY24 and FY25, alongside a new ₹90.51 lakhs Capital Advance (NIL FY24). The
court-order deposit is not cross-referenced to any specific case in Note 45 (Contingent
Liabilities) or elsewhere in the notes — it sits as an unexplained ₹4.03 crore of cash tied
up in litigation-related escrow with no narrative on which dispute it relates to, its
expected resolution, or whether it is refundable. This is a legitimate management question
that Pass 1's Contingent Liabilities section (which covered only the disclosed/undisclosed
Note 45 items) did not raise, since Note 7's court deposit is a separate line not
cross-referenced there.

### 10. Working-capital liability lines show large, unexplained YoY swings beyond what Pass 1 captured (Notes 25, 26, 28, AR p.111) — 🟡 New Watch
- **Earnest Money and Other Deposits (Note 25): ₹90.57 lakhs FY25 vs ₹542.49 lakhs FY24, a
  -83.3% (₹451.92 lakhs) decline.**
- **Advance from customers (Note 26): ₹22.87 lakhs FY25 vs ₹431.11 lakhs FY24, a -94.7%
  decline** — a near-total disappearance of customer advances, consistent with the weaker
  order book implied by the revenue and production declines, but large enough in relative
  terms to be worth an explicit management question on order-booking practice changes versus
  demand weakness.
- **Statutory liabilities (Note 26): ₹125.72 lakhs vs ₹379.16 lakhs, -66.8%.**
- **Current Tax Liabilities (Note 28): NIL FY25 vs ₹251.58 lakhs FY24** — consistent with the
  much lower current tax charge in FY25 (₹37.80 lakhs per Note 22/P&L, already flagged by
  Pass 1) and full utilisation of the FY24 liability during FY25.
None of these four items appeared in Pass 1.

### 11. Note 30 — "Profit on sale of Agricultural land (Acquisition by Government)," ₹61.09 lakhs FY25, NIL FY24 (AR p.111) — 🟡 New Watch, adds to the "recurring one-off gains" pattern
This is a *third* source of one-off/non-recurring gain in FY25 (alongside the ₹480.54 lakhs
exceptional "profit on sale of Lakshmipuram Plant and Machinery" and the ₹437.57 lakhs
fair-value gain on investments, both already flagged by Pass 1) — government acquisition of
agricultural land generated a further ₹61.09 lakhs gain routed through Other Income rather
than Exceptional Items, meaning it is embedded in "core" other income rather than singled
out, which understates how much of FY25's Other Income (₹1,958.02 lakhs total, Note 30) is
non-recurring in nature. Also in the same note: "Claims Received" ₹16.75 lakhs in FY24 fell
to NIL in FY25 — a minor, non-recurring income item that disappeared.

### 12. Note 17.3/17.4 — Shareholding pattern detail not extracted in Pass 1 (AR p.108) — 🟢 New, informational
Durgamba Investment Pvt Ltd holds 38.58% (43,742,656 shares), unchanged both years — the sole
>5% shareholder disclosed. Total promoter/promoter-group holding (Durgamba + Irmgard
Velagapudi 1.59% + Kiran Velagapudi 0.26% + Vinod R. Sethi 0.16%) = **40.59%**, unchanged
both years, no change during the year for any promoter. No pledge of promoter shareholding is
disclosed within the notes (distinct from the company's own investment-book pledge to Kotak
Mahindra Bank, Note 5(b), already covered by Pass 1). Relevant background for governance/UA
assessment even though it carries no YoY change signal.

### 13. Remuneration cross-check across Notes 33, 53(B) and 54 — reconciles cleanly (AR p.112, 124-125) — 🟢 New, confirmatory (resolves what could otherwise look like a discrepancy)
Note 33's "Remuneration to wholetime directors" (₹101.24 lakhs FY25) reconciles exactly to
the sum of the three whole-time directors' individual remuneration in Note 53(B) — Vinod R.
Sethi ₹12.53L + Irmgard Velagapudi ₹48.00L + Kiran Velagapudi ₹40.71L = ₹101.24L. Note 54's
"minimum remuneration" figure of ₹60.53 lakhs (already flagged by Pass 1 as a governance red
flag) is in turn exactly the sum of only the two individuals named in Note 54 as being paid
under the Schedule V inadequate-profits exception — Vinod R. Sethi (₹12.53L) + Irmgard
Velagapudi (₹48.00L) = ₹60.53L — i.e. Kiran Velagapudi's remuneration (₹40.71L) is *not*
part of the minimum-remuneration exception mechanism and is presumably within normal limits.
This is a useful clarification (the three figures — 101.24, 60.53, and the individual KMP
lines — all internally reconcile with no gap) that sharpens, without altering, Pass 1's
governance flag: the Schedule V exception specifically covers the Executive Chairman and
Managing Director, not the Executive Director.

### 14. Notes 55-71 — Schedule III mandatory statutory disclosures, entirely un-extracted in Pass 1 (AR p.125-126) — 🟢 New, clean bundle
A full block of Companies Act Schedule III/CARO-linked disclosures, all answered "Nil" or
in the negative: no property revaluation during the year (Note 56); no intangible asset
revaluation (Note 57); no loans/advances in the nature of loans to Promoters, Directors, KMP
or related parties (Note 58 — independently corroborates Pass 1's Note 52 finding of NIL
loans to subsidiaries, from a different statutory angle); no Benami property proceedings
(Note 61); borrowings from banks/financial institutions confirmed used for intended purpose
(Note 62); **no wilful defaulter declaration by any bank or financial institution (Note
63)** — a standard but material governance clean-check not previously reported; no
transactions with struck-off companies (Note 64); no charge registration delays beyond the
statutory period (Note 65); compliance with the number-of-layers-of-companies rule (Note 66);
compliance with approved schemes of arrangement (Note 67); no funds advanced/loaned/invested
with an understanding that the intermediary would on-lend to or guarantee Ultimate
Beneficiaries (Note 68 — a "layering"/round-tripping check); no funds received from any
person with a reciprocal understanding to on-lend to Ultimate Beneficiaries (Note 69 — the
mirror-image round-tripping check); no crypto/virtual currency transactions (Note 70); no
undisclosed income surrendered/disclosed during tax proceedings (Note 71). All clean; none of
this bundle was reported by Pass 1 despite being routine "would an investor care" territory
(these are exactly the checks used to screen out shell-company/round-tripping/undisclosed-
income risk).

---

## PASS 2 NEW FINDINGS SUMMARY

1. 🔴 Debt Service Coverage Ratio collapsed to 0.25x (FY24: 1.52x, -84%) — Note 73, p.126 —
   a harder financing-stress signal than the Debt/Equity improvement alone conveys.
2. 🟡 RoCE fell to 3% (FY24: 18%, -81%) and Return on Investment fell to 5% (FY24: 27%,
   -82%) — Note 73, p.126-127.
3. 🟡 Note 36 Other Expenses FY24 column does not arithmetically reconcile to its stated
   total; the "Selling expenses" FY24 cell as extracted (₹1,811.72L) is very likely an
   OCR/extraction artifact — reconciled implied value ≈ ₹214.71L — verify against source PDF
   before use — p.113.
4. 🟡 Two new FY25-only P&L expense lines: Provision for Doubtful Debt ₹36.00L (ties exactly
   to a new doubtful supplier advance in Note 15) and Assets Written Off ₹33.07L, both NIL
   in FY24 — Note 36, p.113.
5. 🟢 Note 72 bank-vs-books stock statement reconciliation (all four quarters, banks report
   higher stock value than books; explained by valuation-method difference) — entirely
   missed in Pass 1 — p.126.
6. 🟡 Actual production volumes fell sharply in every core line (Sugar -41.9%, Alcohol
   -82.3%, Molasses -34.4%, Power -24.2%; Urad Dal +275.9%, Bio Fertiliser +13.3%) — Note
   44, p.115 — confirms revenue decline is volume-driven.
7. 🟡 Chemicals segment also swung to loss (-₹42.12L vs +₹59.20L) and Power & Fuel segment
   result fell 83% (₹68.80L vs ₹408.33L, staying positive) — Note 76, p.128.
8. 🟡 Capital expenditure fell 36.1% YoY (₹342.68L vs ₹536.73L) and is now below FY25
   depreciation (₹514.01L) — capex/depreciation ≈0.67x — Note 76/Note 35, p.128/112.
9. 🟡 New Assets Held for Sale, ₹239.50L (FY25), NIL FY24 — signals a further exceptional
   plant-sale gain is plausible in FY26 — Note 16, p.107-108.
10. 🟡 Unexplained "Deposit made as per Court Order," ₹403.48L, static both years, not
    cross-referenced to any Note 45 contingent liability — Note 7, p.106.
11. 🟡 Large, unexplained declines in Earnest Money/Other Deposits (-83.3%), Advance from
    Customers (-94.7%), and Statutory Liabilities (-66.8%) — Notes 25/26, p.111.
12. 🟡 A third source of one-off gain in FY25: Profit on Sale of Agricultural Land ₹61.09L
    (NIL FY24), embedded in Other Income rather than flagged as exceptional — Note 30, p.111.
13. 🟢 Shareholding detail: Durgamba Investment 38.58%, total promoter group 40.59%,
    unchanged both years — Note 17.3-17.4, p.108.
14. 🟢 Remuneration figures across Notes 33/53(B)/54 reconcile exactly; Schedule V minimum-
    remuneration exception applies only to the Executive Chairman and MD, not the Executive
    Director — clarifies, does not weaken, Pass 1's governance flag.
15. 🟢 Notes 55-71 (Schedule III mandatory disclosure bundle: no wilful defaulter
    declaration, no Benami property, no struck-off company dealings, no crypto transactions,
    no round-tripping/layering of funds, no undisclosed income) — entirely un-extracted in
    Pass 1, all clean — p.125-126.

*End of Pass 2. Notes 1 through 76 re-read in full against the Pass 1 output; the fifteen
items above are new findings not previously reported. No material new findings were
identified in Notes 45-51 (Contingent Liabilities, Foreign Currency, MSME, Financial
Instruments, Risk Management, Employee Benefits) — Pass 1's coverage of that block was
already thorough and is not repeated here.*
