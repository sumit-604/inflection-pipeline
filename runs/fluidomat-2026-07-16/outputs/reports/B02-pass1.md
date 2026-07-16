# FLUIDOMAT LIMITED — STAGE 2, PASS 1: FULL NOTES EXTRACTION

## ⚠️ CRITICAL DATA-CURRENCY ALERT — READ FIRST

The injected task stated the source file is the **FY2017 Annual Report (~9 years old)**. This is
**INCORRECT**. The file at `runs/fluidomat-2026-07-16/inputs/annual-report/Annual_Report_2017.pdf`
is in fact the **49th Annual Report, FY2024-25** (year ended 31st March 2025), filed with BSE on
31st August 2025, covering Board's Report, MD&A, Corporate Governance Report, Auditor's Report,
and Notes to the Financial Statements for FY 2024-25 (with FY2023-24 comparatives). There is no
FY2017 content anywhere in this file.

This is **good news for data currency** (the AR is current, filed weeks before the 2026-07-16 run
date, not 9 years stale) but it is a **material mismatch** against the orchestrator's injected
framing, which the downstream stages (valuation, synthesis) must be made aware of. All findings
below are extracted faithfully from the FY2024-25 Notes to the Financial Statements (Notes 1–48,
p.86–p.106 of the printed Annual Report). RPT balances, contingent liabilities, receivables ageing
and borrowings below reflect the **31 March 2025** position, not FY2017. This should be flagged to
the orchestrator/operator immediately — the entire premise of "stale 9-year-old AR" driving the
pipeline's caution level for this run does not apply; instead the correct caveat is "single AR on
file, most recent FY only, no multi-year trend data available beyond the two years shown."

---

## 1. ACCOUNTING POLICIES & CHANGES

- Depreciation: Written Down Value (WDV) method, Schedule II useful lives — Building 5 & 30 yrs,
  Plant & Machinery 10-15 yrs, Office Equipment 5 yrs, Furniture 10 yrs, Computer 3 & 6 yrs,
  Software 6 yrs, Vehicle 8/10 yrs (Note 3E, p.87). Standard Schedule II lives, no aggressive
  extension. 🟢
- No accounting policy changes with quantified P&L impact disclosed this year; Board's Report
  confirms "no revisions in the Financial Statement and Board's Report" (Board's Report General
  item g, p.38, cross-ref only). 🟢
- Capitalisation threshold: NOT FOUND IN DOCUMENT.
- Impairment testing (Note 3J, p.88): policy described qualitatively only ("assesses at each
  reporting date whether there is an indication..."); no quantified growth/discount rate
  assumptions disclosed anywhere (immaterial risk — no goodwill on the books, intangibles are
  Rs 1.15 lakh of software, Note 6 p.92). 🟢 (not material given asset base)
- ECL / expected credit loss (Note 3I(iii), p.88): "measures the expected credit loss... based on
  historical trend, industry practices and business environment... or any other appropriate
  basis" — no quantified ECL matrix or rate disclosed, and **zero ECL/doubtful provision is
  recognised against trade receivables in either year** despite Rs 97.57 lakh (FY25) in the 2-3
  year ageing bucket and Rs 45.76 lakh (FY25) / Rs 25.49 lakh (FY24) outstanding for more than 3
  years (Note 11, p.94). 🔴 Red Flag — provisioning adequacy concern.
- Ind AS 116 leases (Note 3P, p.89): company applies the low-value-asset recognition exemption
  (Para 5(b)) for all its leases; no ROU asset or lease liability recognised anywhere on the
  balance sheet. Lease rent expense Rs 0.92 lakh (FY25) vs Rs 0.94 lakh (FY24) (Note 33, p.100).
  One of these leases is office premises rented from Executive Director Kunal Jain (Board's Report
  p.24: "He has also rented out office premises to the Company on terms approved by the Board");
  Note 45c (p.103) shows Rs 2.48 lakh (FY25) / Rs 2.42 lakh (FY24) lease rent paid to Kunal Jain —
  this appears to be treated as a separate lease outside the Note 33 lease-rent line, or the two
  figures overlap; the document does not reconcile them. 🟡 Watch.
- No first-time standard adoption disclosed this year.

## 2. RELATED PARTY TRANSACTIONS (Note 45, p.102-103)

Full remuneration/compensation table (Note 45b, p.103), this year vs prior year (Rs lakh):

| Party | Relationship | FY25 | FY24 | YoY % |
|---|---|---|---|---|
| Ashok Jain | Chairman & MD | 91.10 | 83.69 | +8.86% |
| Kunal Jain | Executive Director | 78.16 | 71.30 | +9.61% |
| Radhica Sharma | Dy. Managing Director | 80.16 | 66.75 | +20.09% |
| Monica Jain | CFO (relative of promoters) | 17.60 | 16.85 | +4.46% |
| Devendra Kumar Sahu | Company Secretary | 14.00 | 9.83 | +42.46% |
| Pramila Jain | Relative of Director | 21.04 | 19.88 | +5.84% |
| Sundeep Sharma | Relative of Director | 23.70 | 22.35 | +6.04% |
| Sunaina Jain | Relative of Director | 12.89 | 12.16 | +6.00% |
| Independent Directors (3) | Sitting fee | ~0.63 each | ~0.25-0.50 each | up |

Total managerial + KMP + relatives remuneration ≈ Rs 340.83 lakh (FY25) = **4.72% of revenue**
(7218.29) and **11.4% of PBT** (2980.52). 🟡 Watch — three of six board seats and the CFO/CS/
several "relative of director" roles are all Jain/Sharma family; this is a small promoter-family-
run company, consistent with its size, but the concentration is total.

Non-remuneration RPTs (Note 45c, p.103):
- Focus Eye Technocraft Pvt Ltd (relative of director Sandeep Sharma): Purchase of Goods Rs 2.69
  lakh (FY25) vs Rs 4.30 lakh (FY24). No arm's-length benchmarking disclosed. 🟡
- Kunal Jain (Executive Director): Lease Rent Rs 2.48 lakh (FY25) vs Rs 2.42 lakh (FY24) — company
  rents office premises from its own Executive Director. 🟡 Watch — non-arm's-length signal
  (self-dealing in real estate), no independent valuation cited.
- Fluidomat UK Private Limited (listed as "Wholly Owned Subsidiary" in the related-party roster,
  Note 45a, p.102): Disinvestment in Subsidiary Company Rs 0.00 (FY25) vs Rs 13.70 lakh (FY24) —
  yet the Board's Report (p.30) states unambiguously "Your Company does not have any Subsidiary/
  Associate/Joint venture for the financial year 2024-25." The subsidiary was wound up during/
  before FY24 (Annexure 3, p.45: "Proceed from closure of Foreign Wholly Owned Subsidiary" Rs 13.70
  lakh in FY24, Rs 0.00 in FY25). Retaining it on the FY25 related-party list is not technically a
  contradiction but is loose disclosure practice. 🟡 Watch.
- No loans/ICDs to related parties: explicitly confirmed NIL (Note 46.5, p.103): "There is no
  loans or advances in the nature of loans are granted to promoters, directors, KMPs and the
  related parties." 🟢
- No new related parties added this year (roster is the standing family/board list).
- Board's Report (p.30) self-assesses all RPTs as "in the ordinary course of business and on
  arm's length basis" and states "there are no significant transactions with related parties" —
  this is management's own assertion, not independently verified in the notes.

## 3. CONTINGENT LIABILITIES (Note 36.2, p.101)

| Item | FY25 (Rs lakh) | FY24 (Rs lakh) |
|---|---|---|
| Counter-guarantees given to banks for guarantees issued on Company's behalf | 387.65 | 374.03 |
| Demands disputed, not acknowledged as debt — labour payment | 5.32 | 3.04 |
| **Total** | **392.97** | **377.07** |

Net worth (Equity Share Capital Rs 492.70 lakh, Note 17 p.95 + Other Equity Rs 7552.24 lakh, Note
18 p.96-97) = Rs 8,044.94 lakh.

Total contingent liabilities as % of net worth = **4.88%** (FY25); single largest item (bank
guarantees) = 4.82% of net worth. **No single item exceeds 10% of net worth.** 🟢 Clean —
immaterial contingent liability quantum for this data year.

No tax dispute composition disclosed (no income tax/GST litigation items in the contingent
liability table) — NOT FOUND IN DOCUMENT (implies none, or none material enough to disclose).
No guarantees for subsidiaries (none exist in FY25).

Capital commitments (Note 36.1, p.101): Rs 59.83 lakh (FY25) vs Rs 41.40 lakh (FY24) — modest
increase, consistent with the ongoing building-shed CWIP (Note 46.6, p.104). 🟢

## 4. TRADE RECEIVABLES (Note 11, p.94)

Ageing schedule, FY25 vs FY24 (Rs lakh):

| Bucket | FY25 | FY24 |
|---|---|---|
| < 6 months | 1960.27 | 1130.92 |
| 6 months – 1 year | 73.96 | 54.40 |
| 1-2 years | 68.02 | 93.85 |
| 2-3 years | 97.57 | 42.80 |
| > 3 years | 45.76 | 25.49 |
| **Total** | **2245.58** | **1347.46** |

- >6 months as % of total: FY25 = 12.7% ((73.96+68.02+97.57+45.76)/2245.58); FY24 = 16.07%. The
  *percentage* improved, but the *absolute* aged balances worsened materially: 2-3yr bucket more
  than doubled (Rs 42.80 → Rs 97.57 lakh, +128%) and >3yr bucket rose 79.5% (Rs 25.49 → Rs 45.76
  lakh).
- Receivable days (computed from closing balance ÷ revenue from operations × 365, since no
  formal DSO note is given): FY25 = 2245.58/7218.29×365 = **113.6 days**; FY24 =
  1347.46/5549.18×365 = **88.6 days**. **Receivable days deteriorated by ~25 days YoY** even
  though total receivables grew (66.7%) faster than revenue (30.1%). This contradicts the
  "improving" signal from the % >6-months metric and from the Trade Receivables Turnover Ratio in
  Note 46.13 (p.105), which shows only a mild decline (4.02x vs 4.09x, -1.8%) because that ratio
  is computed on *average*, not closing, receivables and is therefore less sensitive to the
  year-end balance sheet spike. 🔴 Red Flag — cash conversion deterioration, feeds FLAG-CASH.
- Zero ECL/doubtful/credit-impaired provisioning in either year, despite the aged buckets above
  (Note 11: "Considered doubtful: 0.00", "Credit impaired: 0.00" both years). 🔴 Red Flag
  (repeated from Section 1 — provisioning adequacy).
- No related-party receivables: "There are no dues against related parties and directors" (Note
  11(ii), p.94). 🟢
- No single-customer concentration disclosure — NOT FOUND IN DOCUMENT.
- All receivables are "unsecured" (Note 11(i), p.94) — standard for this industry, not itself a
  flag.

## 5. INVENTORY (Note 9, p.93 and Note 30, p.99-100)

| Category | FY25 | FY24 |
|---|---|---|
| Raw materials & components | 276.87 | 373.70 |
| Stock-in-process | 97.19 | 106.10 |
| Finished goods | 95.41 | 124.00 |
| Stores & spares | 42.98 | 40.13 |
| Tools | 0.41 | 0.21 |
| Scrap | 3.82 | 1.02 |
| **Total** | **516.68** | **645.16** |

- Finished goods **decreased** 23% (124.00 → 95.41) while revenue **grew** 30.1% — inventory
  efficiency improved, consistent with Note 46.13's Inventory Turnover Ratio jump from 8.62x to
  12.43x (+44.1%), attributed by management to "Higher Turnover and reduction in Inventory." 🟢
- No write-downs, no obsolete-inventory disclosure — NOT FOUND IN DOCUMENT (may simply mean none
  occurred; company physically verifies inventory at "reasonable intervals" per Auditor's Annexure
  A (ii)(a), p.76, with "no discrepancies of 10% or more in aggregate for each class of inventory").
- Valuation policy (Note 3H, p.87): raw materials/stores at weighted-average cost; finished
  goods/WIP at lower of cost or NRV; scrap at NRV — standard, conservative. 🟢

## 6. INVESTMENTS (Note 10, p.93-94; Note 45, p.102-103)

- **No subsidiaries, associates, or JVs during FY25** (Board's Report, p.30). The prior wholly
  owned subsidiary, Fluidomat UK Private Limited, was wound up; the Company received Rs 13.70
  lakh in FY24 as "Proceeds from closure of Foreign Wholly Owned Subsidiary" (Annexure 3, p.45)
  and Rs 0.00 in FY25 (Note 45c). No impairment charge was needed since the exit apparently
  realised value rather than losing it — but no gain/loss on disposal is separately quantified in
  the notes. NOT FOUND IN DOCUMENT (P&L impact of the disinvestment, if any).
- Current investments — extensive mutual fund portfolio (Note 10, p.93-94), ~26 individual
  schemes across large-, multi-, small-cap and hybrid/arbitrage categories. Total carrying value
  (quoted market value) Rs 831.63 lakh (FY25) vs Rs 511.21 lakh (FY24); original cost Rs 763.45
  lakh vs Rs 426.00 lakh. Implied unrealised gain: Rs 68.18 lakh (FY25) vs Rs 85.21 lakh (FY24).
  Portfolio was substantially churned — several FY24 holdings (Edelweiss Arbitrage, HDFC Arbitrage
  WP) exited entirely and ~15 new schemes added in FY25.
- Return on Investment ratio (Note 46.13, p.105) collapsed from **38.78% (FY24) to 3.72% (FY25),
  a -90.4% swing**, explained by management as "NAV of Mutual funds decreased sharply in Current
  Period." 🟡 Watch — treasury income is volatile and mark-to-market dependent; investors should
  not extrapolate FY24's investment income run-rate.
- No loans/ICDs given to any party (Note 46.5, p.103, confirmed NIL). 🟢
- No loss-making subsidiaries (none exist).

## 7. BORROWINGS (Note 21, p.97; Note 46.9-46.12, p.104-105; Note 48D, p.106)

- **Short-term borrowings: Rs 0.00 in both FY25 and FY24** — the Company is entirely debt-free.
  🟢
- Finance cost (Note 32, p.100): Rs 0.00 (FY25) vs Rs 0.09 lakh (FY24) — negligible, consistent
  with zero borrowings.
- Debt-Equity Ratio and Debt Service Coverage Ratio: both "NA — not applicable as there is no
  debts in the company" (Note 46.13, p.105). 🟢
- Company holds large fixed deposits instead: Rs 2,517.60 lakh (non-current FD, Note 7, p.93) +
  Rs 731.10 lakh (current FD, Note 14, p.95) + Rs 526.64 lakh (current FD held as 100% margin
  against bank guarantees, Note 14, p.95) ≈ **Rs 3,775 lakh in fixed deposits alone**, funded from
  internal accruals, not borrowings. 🟢 Strong balance sheet.
- **Unresolved MCA charge registry issue** (Note 46.12, p.104-105): "There are 2 (two) charges for
  charge id no. 90205616 and 90204976 reflecting in the index of charges at the portal of MCA.
  however, the loan amount was repaid and satisfied long back the company is trying to get the
  charge satisfied, however the company could not find whereabout the charge holders, therefore
  the filing of form CHG-4... could not be uploaded." 🟡 Watch / borderline 🔴 — this is an
  unresolved statutory compliance gap: charges from historical (fully repaid) borrowings remain
  open on the public MCA registry because the company cannot locate the original charge-holder to
  co-sign the satisfaction filing. Not a going-concern issue (loans are confirmed repaid) but a
  governance/administrative loose end that could confuse counterparties checking the charge
  registry.
- No covenants, no fixed-vs-floating disclosure (moot given zero borrowings), no related-party
  borrowings, no 5-year repayment schedule (none needed).

## 8. TRADE PAYABLES (Note 22, p.97-98)

| Item | FY25 | FY24 |
|---|---|---|
| MSME dues (principal, not overdue) | 16.73 | 17.26 |
| Other creditors | 308.71 | 384.86 |
| **Total** | **325.44** | **402.12** |

- MSME interest due: Rs 0.00 in both years; no interest paid/payable for delayed MSME payments
  under Section 16 of the MSMED Act; no interest accrued and remaining unpaid. 🟢 Clean.
- Ageing schedule (both years): **100% of both MSME and non-MSME payables fall in the "Less than
  1 Year" bucket** — no payables aged beyond 1 year in either year. 🟢
- Trade Payables Turnover Ratio (Note 46.13, p.105): improved from 5.60x (FY24) to 6.46x (FY25),
  +15.48% — i.e., **payment to suppliers is happening faster**, while (per Section 4) collection
  from customers is happening slower. 🟡 Watch — combined, this lengthens the cash conversion
  cycle and increases working-capital funding needs; the Company currently absorbs this
  comfortably given its debt-free, cash/FD-rich balance sheet, but the trend direction (faster
  payables, slower receivables) is the kind of combination worth monitoring in future periods.

## 9. PROVISIONS (Note 19, p.97; Note 25, p.98; Note 3R(ii)(a), p.89-90)

| Provision | FY25 | FY24 |
|---|---|---|
| Leave encashment (non-current) | 120.63 | 110.18 |
| Bonus (current) | 67.73 | 54.26 |

- **Gratuity / employee defined benefit plan**: Note 3R(ii)(a) (p.89-90) discloses only that the
  "Employee's Gratuity Fund Scheme...is managed by Trust maintained with Life Insurance
  Corporation of India (LIC)" and that "the difference, if any, between the actuarial valuation
  of the gratuity... and the balance of funds with LIC is provided for as assets/(liability) in
  the books." **No actuarial assumption table (discount rate, salary escalation rate, mortality
  table), no funded-status reconciliation (plan assets vs. defined benefit obligation), and no
  sensitivity analysis is presented anywhere in the notes I could locate.** This is normally a
  mandatory Ind AS 19 disclosure block (typically its own dedicated note). 🔴 Red Flag —
  disclosure transparency gap on employee benefits.
- No warranty provision disclosed — NOT FOUND IN DOCUMENT (may be immaterial/absent for this
  product line).
- No onerous-contract or decommissioning provisions — not applicable to this business.
- No standalone litigation provision; the one disputed item (labour payment, Rs 5.32 lakh) is
  carried as a contingent liability (Note 36.2(ii)(a), p.101), not a provision, implying
  management assesses the outflow as not probable. 🟢 (consistent treatment)

## 10. DEFERRED TAX (Note 20, p.97)

| Item | FY25 | FY24 |
|---|---|---|
| DTL — related to property, plant & equipment | 49.22 | 44.23 |
| DTA — disallowables u/s 43B of Income Tax Act | (25.47) | (25.00) |
| **Net DTL** | **23.75** | **19.23** |

- No effective-tax-rate-vs-statutory-rate reconciliation table is presented — NOT FOUND IN
  DOCUMENT. Computed implied effective rate for cross-check: Current tax 758.09 + tax adjustment
  for prior years (4.44) + deferred tax 4.52 = Rs 758.17 lakh total tax on PBT of Rs 2,980.52 lakh
  = **25.44% effective rate**, broadly in line with the ~25.17-25.4% domestic corporate tax
  regime slabs — no anomaly evident from the raw numbers, but the absence of the formal
  reconciliation note itself is a disclosure gap. 🟡 Watch.
- No MAT credit entitlement/utilisation disclosed — NOT FOUND IN DOCUMENT (consistent with a
  profitable company likely paying tax above MAT floor, so probably not applicable, but not
  confirmed in text).
- No unrecognised DTA disclosed or implied — company is consistently profitable (PBT up from
  Rs 1757.10 lakh to Rs 2980.52 lakh).

## 11. REVENUE DETAILS (Note 27, p.98; Note 39, p.101; Note 3K, p.88)

| Component | FY25 | FY24 |
|---|---|---|
| Sale of products (incl. spares & components) | 7153.05 | 5519.98 |
| Income from services | 59.45 | 18.67 |
| Scrap sales | 5.79 | 10.53 |
| **Total revenue from operations** | **7218.29** | **5549.18** |

- Total revenue growth: +30.1%. Income from services grew +218% off a small base — worth noting
  but immaterial to total (0.8% of revenue).
- **Single reportable segment**: "the Company operates in one segment only" (Note 3K, p.88),
  confirmed in MD&A ("the company has only one segment i.e., manufacturing of fluid couplings").
  No geographic or product-line disaggregation beyond the single Sale-of-products/Services/Scrap
  split. 🟢 consistent, but limited granularity for investor analysis.
- No contract-asset/contract-liability note under Ind AS 115 terminology; "Advance from
  customers" (Note 24, p.98) of Rs 106.60 lakh (FY25) vs Rs 54.90 lakh (FY24) functions as a
  contract liability but is not labelled or reconciled as such. NOT FOUND IN DOCUMENT (formal Ind
  AS 115 disclosures).
- No top-customer revenue % disclosed — NOT FOUND IN DOCUMENT.
- Export sales & services (Note 39, p.101): Rs 219.05 lakh (FY25) vs Rs 279.23 lakh (FY24), a
  **21.5% decline**, even as total revenue grew 30.1% — i.e., growth this year was entirely
  domestic-market-driven. 🟡 Watch (a mild diversification-reversal signal).
- Cross-reference note (from Board's Report, not the Notes themselves, flagged here because it
  directly informs how to read Note 27): the Board's Report (p.26) states order booking for
  FY25 was Rs 5,815.76 lakh vs Rs 6,003.22 lakh in FY24, a **3.12% decline**, even as revenue
  (executed/billed) grew ~30%. This implies FY25 revenue was substantially fulfilled from a prior
  backlog, and forward order intake did not keep pace with delivery — a potential deceleration
  signal for FY26 revenue that is not evident from the Notes' revenue table alone. 🟡 Watch.

## 12. OTHER CRITICAL NOTES

- **Exceptional items**: none disclosed; no separate exceptional-item line in the P&L. NOT FOUND
  IN DOCUMENT (implies none this year).
- **Goodwill**: none on the balance sheet. Not applicable.
- **Intangibles** (Note 6, p.92): Software Rs 1.15 lakh (FY25) vs Rs 1.22 lakh (FY24); Intangible
  assets under development (software) Rs 9.00 lakh (FY25) vs Rs 5.00 lakh (FY24) — immaterial.
- **Capital commitments**: Rs 59.83 lakh (FY25) vs Rs 41.40 lakh (FY24) (Note 36.1, p.101).
- **Foreign currency exposure / hedging**: Note 48A (p.106) describes market risk generically; no
  FX derivative contracts held; Auditor's Report confirms "the Company did not have any long-term
  contracts, including derivative contracts, for which there were any material foreseeable
  losses" (Auditor's Report B(b), p.74). No quantified FX sensitivity table. NOT FOUND IN
  DOCUMENT.
- **Segment reporting**: single segment confirmed (see Section 11). 🟢
- **Basic vs. diluted EPS gap**: Basic = Diluted = Rs 45.15 in both the P&L statement (p.83) and
  Note 35 (p.101, combined comprehensive-income EPS); no ESOP, no convertible instruments, no
  dilution sources. 🟢 Clean.
- **Events after balance sheet date**: proposed final dividend Rs 7.50/share for FY25 (vs Rs
  5.50/share FY24), subject to shareholder approval, correctly **not recognised as a liability**
  as at 31 March 2025 (Note 18(iv), p.96) — standard, compliant Ind AS 10 treatment. 🟢
- **CSR required vs. actual** (Note 41, p.102; Annexure 2 to Board's Report, p.43-44): Required
  Rs 25.13 lakh (FY25) vs Rs 17.01 lakh (FY24, per Note 41 — note this figure differs from the
  Annexure 2 CSR report's Rs 25,12,793 FY25 figure, which is consistent; the FY24 comparative in
  Note 41 appears to reference a different average-profit base year, not fully reconciled in the
  notes). Actual spent Rs 19.95 lakh (FY25) vs Rs 24.01 lakh (FY24). FY25 shortfall Rs 5.18 lakh,
  transferred to the PM National Relief Fund on 06.08.2025 (per Annexure 2, p.43) — i.e., **after**
  the 31 March 2025 year-end but within the permitted 6-month statutory window (confirmed by
  Auditor's CARO Annexure A, clause (xx)(a), p.79). Prior year's Rs 7.00 lakh shortfall (FY23
  carryforward, per Note 41(iv)) was fully cleared this cycle. 🟢 Compliant, though the pattern of
  recurring shortfalls against direct-project CSR spend (met instead via national relief fund
  transfers) is worth noting as a mild governance observation, not a red flag. 🟡 Watch (pattern,
  not a violation).
- **ESOP dilution**: none — Board's Report confirms "the Company has not issued shares (including
  sweat equity shares) to employees... under any scheme" (p.38). 🟢
- **Share capital changes**: none — Rs 492.70 lakh, 49.27 lakh equity shares of Rs 10 each,
  unchanged both years (Note 17, p.95). 🟢
- **Direct debits/credits to reserves bypassing P&L**: Statement of Changes in Equity (p.85)
  shows dividends (Rs 270.99 lakh FY25) debited directly against Retained Earnings, and Rs 100
  lakh transferred to General Reserve in both years — both are standard, non-aggressive equity
  movements, not disguised expense avoidance. OCI (fair-value gain on mutual funds, Rs 2.28 lakh
  FY25 vs Rs 85.46 lakh FY24) flows through the "Other Items of OCI" reserve column per standard
  Ind AS treatment. 🟢
- **Minor statutory compliance lapse** (Auditor's Annexure A, clause (vii)(a), p.77): "Professional
  Tax Employee (Kolkata Branch) amounting to Rs. 15,780" outstanding for more than six months from
  the date it became payable — immaterial in quantum but worth noting as a data point on
  compliance discipline. 🟡 Watch (minor).
- **No Key Audit Matters** are actually described in the Auditor's Report despite the report
  containing a full boilerplate "Key Audit Matters" section header (p.72) — the section states the
  general definition of KAM but lists no actual matters. This is unusual/thin audit reporting
  practice for a listed company but is not itself a Notes-based finding; flagged for context on
  audit rigor.
- **Going concern**: No going-concern qualification anywhere. Directors' Responsibility Statement
  (Board's Report, p.28) states financial statements "have been prepared on a going concern
  basis"; CARO clause (xix) (Auditor's Annexure A, p.79) states nothing came to the auditor's
  attention causing belief the Company cannot meet its liabilities as they fall due — both are
  standard boilerplate, no material uncertainty language anywhere. **going_concern_language:
  NONE.**
- **Restatements**: Note 47 (p.105) states only "Previous year figures have been regrouped and/or
  rearranged wherever considered necessary" — a generic reclassification statement, not a
  substantive restatement; no restated prior-year figures presented anywhere. No "restated" P&L
  or balance sheet line found.

---

# PASS 1 SUMMARY — TOP 10 MOST SIGNIFICANT FINDINGS

| Rank | Finding | Note Ref | Rating | Why it matters |
|---|---|---|---|---|
| 1 | **Source-file mismatch**: document is FY2024-25 (49th) AR, not FY2017 as briefed | N/A (whole document) | 🔴 | Changes the entire data-currency framing for this pipeline run; must be corrected upstream before valuation/synthesis proceed |
| 2 | Zero ECL/doubtful provision on trade receivables despite Rs 97.57 lakh in 2-3yr bucket and Rs 45.76 lakh >3yr (FY25) | Note 11, p.94 | 🔴 | Provisioning adequacy concern; receivables considered "good" in full across all ageing buckets in both years |
| 3 | Receivable days rose from ~88.6 to ~113.6 days YoY (closing-balance basis) even as % >6-months improved | Note 11, p.94; Note 27, p.98 | 🔴 | Cash conversion deterioration masked by average-based turnover ratio; feeds FLAG-CASH |
| 4 | No Ind AS 19 actuarial disclosure for gratuity (no discount rate, salary growth, funded status, sensitivity) | Note 3R(ii)(a), p.89-90 | 🔴 | Disclosure transparency gap on a mandatory employee-benefit note |
| 5 | Two unsatisfied MCA charges from long-repaid loans; charge-holders untraceable, CHG-4 not filed | Note 46.12, p.104-105 | 🟡 | Unresolved governance/compliance loose end on public registry, though not a going-concern issue |
| 6 | Order booking down 3.12% YoY (Rs 5815.76 lakh vs Rs 6003.22 lakh) even as revenue up ~30% | Board's Report p.26, cross-ref to Note 27 p.98 | 🟡 | Possible forward revenue deceleration signal not visible from the Notes' revenue table alone |
| 7 | Company rents office premises from its own Executive Director (Kunal Jain) | Note 45c, p.103 | 🟡 | Related-party self-dealing on real estate; no independent arm's-length benchmarking disclosed |
| 8 | Return on Investment ratio collapsed 38.78% → 3.72% (-90.4%) on mutual fund portfolio | Note 46.13, p.105 | 🟡 | Treasury income is volatile/mark-to-market dependent; do not extrapolate prior-year investment income |
| 9 | Trade payables turnover improved (faster payment) while receivables turnover slowed (closing-balance basis) | Note 22, p.97-98; Note 11, p.94 | 🟡 | Lengthening cash conversion cycle, currently absorbed by large debt-free cash/FD position |
| 10 | Company fully debt-free (Nil borrowings both years) with ~Rs 3,775 lakh in fixed deposits; contingent liabilities only 4.88% of net worth | Note 21, p.97; Notes 7 & 14, p.93/95; Note 36.2, p.101 | 🟢 | Strong balance sheet position — a genuine positive that should not be lost among the flags above |

---

*This is Pass 1 of 3. Pass 2 (what was missed) and Pass 3 (pattern pass + consolidation) follow in
subsequent calls per the stage 2 pipeline instructions.*
