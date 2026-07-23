# STAGE 2 — NOTES TO FINANCIAL STATEMENTS — PASS 1 (FULL EXTRACTION)
Company: DDev Plastiks Industries Ltd (DDEVPLSTIK) | Run date: 2026-07-23

## PROVENANCE CORRECTION — READ FIRST

The task briefing described the source file as "Annual_Report_2020.pdf ... FY2020 ...
~6 years stale." This is **incorrect for the actual file content**. The PDF and its
text cache (`inputs/annual-report/Annual_Report_2020.pdf`, 190 pages) are the
**FY2024-25 Annual Report** of Ddev Plastiks Industries Limited — financial
statements for the year ended 31st March 2025, comparatives 31st March 2024,
auditor's report dated 15 May 2025, board sign-off 15 May 2025 (p.147, p.188 —
cover page explicitly reads "Annual Report 2024-25"; Independent Auditor's Report
opinion paragraph: "state of affairs of the Company as at March 31, 2025").
Only the file name is stale/mislabeled; the content is the **most recent annual
report available**, roughly 14 months old relative to the 2026-07-23 run date, not
six years. This is standalone (not consolidated) — CARO Annexure A clause XXI
confirms "the company is not required to prepare consolidated financial statements
as the company is not a holding company of any other company."

All findings below are anchored to FY2024-25 (current year) vs FY2023-24 (prior
year) as printed in the document. Note numbering: Note 1 (Company Info) through
Note 57 (regrouping statement). Page references are the PDF's own printed page
numbers (as shown in the running footer), not text-cache line numbers.

---

## SECTION-BY-SECTION EXTRACTION

### 1. Accounting policies and changes (Notes 1-3, p.159-168)
- 🟢 Standard Ind AS compliance framework, historical cost basis except
  derivatives/FVTOCI equity/defined benefit plan assets (Note 2.2, p.159).
- 🟡 Depreciation: Plant & Machinery useful life taken as **25 years vs 15 years
  prescribed under Schedule II**, justified by management as "based on the
  prevailing practices of the comparable industries and our past experience for
  last 30 years" (Note 3.2, p.160). This is a materially longer life than the
  statutory default and directly lowers annual depreciation charge — no
  independent technical justification (e.g. third-party assessment) disclosed.
  Worth monitoring; not new this year (recurring policy, "previous year"
  comparatives use the same rate — no P&L impact from a change this year, but the
  underlying choice itself is an aggressive-side judgment).
- 🟢 Revenue recognition: point-in-time on dispatch/delivery, standard Ind AS 115
  language; variable consideration (returns/rebates) constrained; no unusual
  contract asset/percentage-of-completion exposure (Note 3.1, p.160-161).
- 🟢 ECL: simplified approach, provision matrix based on historical loss
  experience "adjusted as appropriate," explicit forward-looking overlay of **5%
  for worsening future economic conditions** (Note 12, p.163). Reasonably
  conservative and quantified.
- 🟢 Ind AS 116 leases: ROU/lease liability recognized for all leases except
  short-term/low-value; discount rate used is described as "the Company's
  actuarial discounting rate" (unusual phrasing — normally incremental borrowing
  rate — but no separate rate % disclosed) (Note 52, p.185). NOT FOUND: explicit
  lease discount rate %.
- 🟢 No new Ind AS standards adopted/notified for the year (Note 56, p.188): "For
  the year ended March 31, 2025, MCA has not notified any new standards."
- 🟢 Impairment testing: standard Ind AS 36 language; no goodwill on balance
  sheet, no CGU-level impairment testing disclosed (single reportable segment, no
  subsidiaries) — not applicable this year.
- 🟢 Capitalisation threshold: NOT FOUND IN DOCUMENT (no explicit Rs threshold
  disclosed).

### 2. Related party transactions (Note 41, p.188-189)
Full transaction table, FY25 vs FY24 (₹ Lacs):
| Party | Nature | FY25 | FY24 | YoY % |
|---|---|---|---|---|
| KMPs (5 individuals) | Remuneration | 270.71 | 249.51 | +8.5% |
| Bbigplas Poly Pvt Ltd (promoter/holding co) | Final dividend | 767.51 | 766.05 | +0.2% |
| Bbigplas Poly Pvt Ltd | Interim dividend | 0 | 383.03 | n/a |
| Bbigplas Poly Pvt Ltd | Rent paid | 98.16 | 98.16 | 0% |
| Bbigplas Poly Pvt Ltd | Security deposit given (against rent) | 98.16 | 98.16 | 0% |
| Kkalpana Industries (India) Ltd (fellow subsidiary) | Purchase of goods | 1,268.21 | 671.33 | **+88.9%** |
| Kkalpana Industries (India) Ltd | Purchase of capital goods | 179.50 | 0 | new |
| Kkalpana Industries (India) Ltd | Sale of goods | 317.51 | 457.87 | -30.7% |
| Kkalpana Industries (India) Ltd | Sale of capital goods | 0 | 72.24 | n/a |
| Kkalpana Industries (India) Ltd | Royalty expense paid | 458.39 | 1,664.55 | **-72.5%** |
| Kkalpana Industries (India) Ltd | Rental income received | 0 | 3.80 | n/a |

🟡 **Watch**: Royalty paid to fellow subsidiary Kkalpana Industries fell 72.5%
YoY (₹16.65 Cr to ₹4.58 Cr) with no explanation in the notes of why the royalty
rate/base changed. No agreement terms, % of sales, or renegotiation disclosed.
Simultaneously purchases from the same fellow subsidiary nearly doubled. The
notes give no mechanism linking these two; a reader cannot verify arm's-length
pricing from disclosure alone (Note 41, p.188-189).

Total identifiable RPT flow (remuneration + dividends + purchases + sales +
royalty + rent), FY25 ≈ ₹33.4 Cr against FY25 revenue of ₹2,603.32 Cr (Note 26,
p.169) = **1.3% of revenue** — not material in aggregate.

🟢 (C) "Balances at the year ended 31.03.2025" heading is printed with **no
outstanding related-party balance table beneath it** (p.189) — implies no
related-party receivables/payables/loans outstanding at year end. No loans/ICDs
to promoter entities anywhere in the document (Note 37, p.183-184: "There are no
loans given by the company").

No new related parties added this year; related party list (KMPs, promoters,
Bbigplas Poly, and three fellow subsidiaries — Kkalpana Industries, Plastic
Processor and Exporters Pvt Ltd, Kkalpana Plastick Limited) unchanged from prior
year list shown (Note 41(A), p.188).

### 3. Contingent liabilities (Note 36, p.183-184)
| Nature | FY25 (₹ Lacs) | FY24 (₹ Lacs) |
|---|---|---|
| Income tax matters (demand disputed) | 221.20 | 0 |
| Bank guarantees | 765.59 | 1,639.52 |
| Capital commitments (net of advances) | 1,167.37 | 227.31 |
| Letters of credit outstanding | 3,192.43 | 2,425.53 |

Tax dispute composition (Annexure A to Auditor's Report, p.139): Income Tax Act
1961, u/s 154, AY2022-23, ₹219.27 Lacs, pending at CIT(A); u/s 156, AY2023-24,
₹1.93 Lacs, pending at CIT(A). Total ₹221.30 Lacs (rounding vs the ₹221.20 shown
in Note 36 — trivial reconciliation gap, likely rounding only).

Net worth (Total Equity, Note 44, p.182) = ₹83,470.59 Lacs (₹834.71 Cr) at
31-Mar-2025. Largest single contingent item (LC outstanding ₹31.92 Cr) = 3.8% of
net worth; income tax demand = 0.26% of net worth. **No single item exceeds 10%
of net worth.** 🟢 No guarantees given for subsidiaries (company has none).
Capital commitments roughly quintupled YoY (₹2.27 Cr to ₹11.67 Cr), consistent
with the disclosed land/capex additions in PPE (see Section 6 below) — 🟡 watch as
a forward funding signal, not a red flag per se.

### 4. Trade receivables (Note 12, p.163-164)
Ageing (₹ Lacs), gross of allowance:
| Bucket | FY25 | FY24 |
|---|---|---|
| Not due | 38,831.66 | 31,107.50 |
| <6 months overdue | 8,174.99 | 8,902.33 |
| 6m-1yr overdue | 7.60 | 482.17 |
| 1-2yr overdue | 89.89 | 60.96 |
| 2-3yr overdue | 11.52 | 8.89 |
| >3yr overdue | 4.95 | 31.68 |
| **Total (gross)** | **47,120.61** | **40,593.54** |
| Less: allowance | (479.50) | (774.96) |
| **Net** | **46,641.11** | **39,818.58** |

- 🟢 100% "undisputed, considered good" — no credit-impaired or disputed
  receivable line has any balance in either year.
- 🟢 Overdue >6 months as % of total (gross): FY25 = (7.60+89.89+11.52+4.95) /
  47,120.61 = **0.24%**; FY24 = (482.17+60.96+8.89+31.68) / 40,593.54 = **1.44%**.
  Improved YoY.
- 🟡 Receivable days trend (net receivables / revenue from operations × 365,
  using Note 26 revenue): FY25 = 46,641.11 lacs / 2,60,332.37 lacs × 365 ≈
  **65.4 days**; FY24 = 39,818.58 / 2,43,124.37 × 365 ≈ **59.8 days**. This is
  corroborated by the company's own Note 53 Accounting Ratio: **Trade receivables
  turnover ratio fell from 6.39x to 6.02x (-5.8%)** (p.187, no ">25% variance"
  explanation required/given at that threshold). Direction is a mild
  deterioration, not yet material.
- 🟢 ECL allowance actually fell (₹7.75 Cr to ₹4.80 Cr) even as gross receivables
  grew, consistent with the improved ageing mix above — not evidence of
  under-provisioning on its face, though see Pass 3 pattern check re: bad debts
  written off alongside the allowance release.
- No customer >10% of revenue (Note 40(f), p.176: "No customer individually
  accounted for more than 10% of the revenue in the years ended 31st March, 2025
  and 31st March, 2024").
- No receivables from related parties (see Section 2).
- 3-year trend: NOT FOUND — the document discloses only FY25 and FY24 ageing;
  no FY23 comparative ageing table is present.

### 5. Inventory (Note 10, p.161-162)
| Category | FY25 (₹ Lacs) | FY24 (₹ Lacs) | YoY % |
|---|---|---|---|
| Raw materials | 19,465.83 | 17,523.00 | +11.1% |
| Finished goods | 3,741.93 | 2,334.27 | **+60.3%** |
| Stores & spares | 1,020.09 | 671.77 | +51.9% |
| **Total** | **24,227.85** | **20,529.04** | **+18.0%** |

- 🟡 **Watch**: Finished goods grew +60.3% vs revenue growth of +7.08%
  (₹2,431.24 Cr to ₹2,603.32 Cr, Note 26) — a significant build-up of finished
  stock well ahead of sales growth. No write-down/obsolescence disclosure
  accompanies this (Note 10, p.161-162: "no amount was recognised as an expense
  for the inventories carried at net realisable value" in either year, and no
  obsolete-inventory note). The company's own Inventory Turnover Ratio (Note 53)
  is essentially flat (11.63x FY25 vs 11.49x FY24, +1.25%), which smooths the
  optic because it is computed on average total inventory including raw material
  and stores, not finished goods alone — the finished-goods-specific build is not
  visible in that aggregate ratio.
- 🟢 Inventory pledged as security for working capital loans (Note 47, p.184,
  cross-ref Note 10) — standard for the fund-based facility structure; no
  incremental risk beyond normal WC financing.
- No obsolete inventory disclosures, no write-downs with amounts (both years
  nil per the express statement above).
- 3-year inventory-days trend: NOT FOUND (only two years' data in this report).

### 6. Investments (Notes 11, 37, PPE Note 4)
- 🟢 No subsidiaries or JVs (standalone company; CARO Annexure A clause XXI
  confirms not a holding company).
- 🟢 No loans given, no ICDs: Note 37 (p.183): "There are no loans given by the
  company... There are no investments made by the company except as disclosed in
  Note no. 11... There is no security given during the year."
- New this year: Current investments in mutual funds (debt/liquid/arbitrage) of
  ₹6,139.23 Lacs (₹61.39 Cr), **zero in FY24** (Note 11, p.162). Fully unquoted,
  FVTPL, no impairment. This is simply surplus cash being parked in liquid/debt
  funds — consistent with the operator context's "net-debt-free since Q4 FY24"
  narrative — 🟢 clean, sensible treasury management, not a red flag.
- Free-hold land jumped from ₹1,476.31 Lacs to ₹3,283.35 Lacs (+122.4%) within
  PPE (Note 4, p.158) — consistent with the Bhiwadi (Rajasthan) greenfield land
  acquisition referenced in operator context, though the notes themselves give
  no location/purpose narrative for the addition — 🟢 anchored to a hard number,
  flagged for cross-reference only.

### 7. Borrowings (Notes 17, 20, 44-45, 47-48)
- Short-term borrowings (Note 20, p.164-165): Cash credit from banks ₹0 (FY25)
  vs ₹1,579.80 Lacs (FY24); Working Capital Demand Loan ₹4,200.00 Lacs (FY25) vs
  ₹5,025.54 Lacs (FY24). Total secured short-term borrowings **₹4,200.00 Lacs
  FY25 vs ₹6,605.34 Lacs FY24, down 36.4%**.
- 🟢 No long-term/term borrowings in either year (Note 44, p.182: "Non-current
  Borrowings — Nil" both years).
- Security: first pari passu charge over all current assets/stock/receivables +
  lien on fixed deposit of ₹1.35 Cr; second pari passu equitable mortgage over
  Dhulagarh, Daman, Dadra, Surangi unit properties (Note 20/47, p.165, 184).
- No covenant breaches or waivers disclosed; CARO clause IX(a) (p.140): "the
  Company has not defaulted in the repayment of loans or other borrowings or in
  the payment of interest thereon to any lender during the year." Not declared a
  willful defaulter (IX(b)).
- Fixed vs floating: NOT FOUND explicitly by instrument, but the interest-rate
  sensitivity note (Note 43, p.179) implies floating-rate exposure on
  unhedged borrowings (₹26.78 Lacs PBT impact per 50bp move, FY25).
- Net debt: **negative** — Note 44 Capital Management (p.182) shows Net Debt =
  (₹5,808.72 Lacs) FY25 and (₹1,050.38 Lacs) FY24, i.e. the company is net cash in
  both years, gearing (Net Debt/Equity) at -0.07x (FY25) and -0.02x (FY24).
- 5-year repayment schedule: NOT FOUND (no term debt to schedule).
- No related-party borrowings.

### 8. Trade payables (Note 21, p.165-166)
Ageing (₹ Lacs):
| Bucket | FY25 | FY24 |
|---|---|---|
| MSME, not due | 2,249.80 | 1,656.56 |
| MSME, <1yr overdue | 14.83 | 10.35 |
| MSME, 1-2yr overdue | 0.07 | 0.09 |
| **MSME total** | **2,264.70** | **1,667.00** |
| Others, not due | 5,160.55 | 8,547.54 |
| Others, <1yr overdue | 500.18 | 464.85 |
| **Others total** | **5,660.73** | **9,012.39** |
| **Grand total** | **7,925.43** | **10,679.39** |

(Separately, Note 21's own summary table shows total trade payables including
acceptances of ₹20,237.21 Lacs FY25 vs ₹18,123.54 Lacs FY24 — the ageing table
above appears to exclude "Acceptances secured" of ₹12,311.78 Lacs FY25 /
₹7,444.15 Lacs FY24, i.e. supply-chain-finance/bill-acceptance liabilities are
tracked separately from the ageing schedule. NOT FOUND: explicit reconciliation
of the two totals in the notes themselves — a disclosure gap, see Pass 3.)

- 🟡 **MSME dues outstanding grew +35.9%** (₹16.67 Cr to ₹22.65 Cr), and
  **interest on delayed MSME payments recurs both years**: ₹0.66 Lacs FY25 (P.Y.
  ₹0.86 Lacs) under Section 16 of the MSMED Act (Note 21, p.166). Amount is
  immaterial in absolute terms but the recurrence (two years running) indicates
  the company does not consistently pay all MSME vendors within the statutory 45
  days.
- Payable days: total payables (incl. acceptances) ₹202.37 Cr / purchases
  ₹2,160.61 Cr (Note 28, p.169) × 365 ≈ 34.2 days FY25 vs ₹181.24 Cr /
  ₹1,944.08 Cr × 365 ≈ 34.0 days FY24 — broadly flat. However the company's own
  Note 53 Trade Payables Turnover Ratio shows **+36.7% YoY (8.24x to 11.26x)**,
  attributed by management to "change in credit cycle" (p.187) — this appears to
  measure something narrower than the payables total used above (likely excludes
  acceptances), so the two views diverge; flagged for reconciliation in Pass 3.

### 9. Provisions (Notes 18, 24, 39)
- Long-term provisions (Note 18, p.164): Gratuity ₹503.23 Lacs FY25 vs ₹356.53
  Lacs FY24, +41.1%.
- Short-term provisions (Note 24, p.168): Leave encashment (unfunded) ₹260.05
  Lacs FY25 vs ₹230.38 Lacs FY24; Gratuity current portion ₹0 FY25 vs ₹152.02
  Lacs FY24.
- Gratuity (defined benefit plan) full actuarial roll-forward at Note 39(b),
  p.172-175:
  - Obligation at year end: ₹762.08 Lacs FY25 vs ₹636.52 Lacs FY24.
  - Plan assets at year end: ₹122.85 Lacs FY25 vs ₹127.97 Lacs FY24.
  - **Funded status: deficit of (₹639.23) Lacs FY25 vs (₹508.55) Lacs FY24** —
    plan is only ~16% funded (122.85/762.08); deficit is fully recognized on
    balance sheet (net liability), so not a hidden risk, but worth noting the
    funding gap is widening in absolute terms.
  - Discount rate 6.61% FY25 (down from 7.20% FY24); salary escalation 6% p.a.
    both years; mortality IALM (2012-14) Ultimate both years; attrition-based
    withdrawal rates disclosed by age band.
  - Sensitivity: 1% discount rate decrease raises DBO from ₹762.08 to ₹823.04
    Lacs (+8.0%); 1% salary escalation increase raises DBO to ₹813.90 Lacs
    (+6.8%) — reasonable, disclosed sensitivities.
- 🟢 No warranty provisions, no decommissioning provisions, no onerous contract
  provisions, no litigation provisions disclosed beyond the tax dispute in
  Note 36 — consistent with a manufacturing business without warranty
  obligations on compounds sold.
- CSR: gross amount required ₹301.16 Lacs FY25 (P.Y. ₹139.83 Lacs); amount
  spent ₹309.51 Lacs FY25 (P.Y. ₹150.00 Lacs) — **spent exceeds required in both
  years**; unspent amount NIL both years (Note 38, p.171). 🟢 Clean, no CSR
  shortfall carried forward.

### 10. Deferred tax (Note 19, p.164-165, and Note 33, p.170-171)
- DTL (net): ₹2,526.52 Lacs FY25 vs ₹2,269.53 Lacs FY24, driven almost entirely
  by depreciation timing differences (₹2,744.68 Lacs FY25 vs ₹2,636.79 Lacs FY24
  gross liability from depreciation/amortisation).
- Effective tax rate reconciliation (Note 33 II, p.171): accounting profit
  before tax ₹25,064.30 Lacs FY25; statutory rate 25.168%; tax at statutory rate
  ₹6,308.18 Lacs; non-deductible items +₹89.32 Lacs; earlier-year tax +₹98.77
  Lacs; effective tax expense ₹6,504.11 Lacs → **effective rate = 25.95%** vs
  statutory 25.168% (FY25); FY24 effective rate = 6,280.79/24,465.62 = **25.68%**
  vs same statutory rate. Small, explained gap both years — 🟢 clean, no MAT
  credit mechanics disclosed (company appears to be on the lower corporate tax
  regime given the 25.168% rate, consistent with Section 115BAA).
- No unrecognised DTA disclosed; no MAT credit note found — NOT FOUND IN
  DOCUMENT (not applicable under 115BAA regime, most likely, though the notes
  do not state this explicitly).

### 11. Revenue details (Note 26, p.169; Note 40, p.176)
- Disaggregation by product (Note 26): Polyethylene ₹2,22,931.97 Lacs FY25
  (₹2,229.32 Cr) vs ₹2,05,292.08 Lacs FY24 (+8.6%); Poly Vinyl Chloride
  ₹30,617.86 Lacs FY25 vs ₹29,832.16 Lacs FY24 (+2.6%); Others ₹6,782.54 Lacs
  FY25 vs ₹8,000.13 Lacs FY24 (-15.2%). **Total ₹2,60,332.37 Lacs FY25
  (₹2,603.32 Cr) vs ₹2,43,124.37 Lacs FY24 (₹2,431.24 Cr), +7.08%.**
- Geography (Note 39-continuation table mislabeled under gratuity section in
  the text extraction but is segment revenue by customer location, p.174):
  India ₹2,05,242.24 Lacs FY25 (78.8% of revenue) vs ₹1,82,288.41 Lacs FY24
  (75.0%); Overseas ₹55,090.13 Lacs FY25 (21.2%) vs ₹60,835.96 Lacs FY24
  (25.0%) — export mix **declined** ~4 points YoY in this document's figures.
  (Note: this is directionally different from the operator context's "Exports
  FY26 +30% revenue" claim — that is a later, FY26 data point not covered by
  this FY25 report; no contradiction, just different periods.)
- Single reportable operating segment (Note 40(a), p.176): "manufacturing and
  sale of Poly Vinyl Chloride, Polyethylene, Antifab and EP Compound" — company
  discloses no segment-level assets/liabilities/results as a consequence.
- No customer >10% of revenue either year (Note 40(f)).
- Contract assets/liabilities, unsatisfied performance obligations: NOT FOUND
  IN DOCUMENT as a distinct disclosure (only "advance from customers" of
  ₹100.10 Lacs FY25 / ₹296.78 Lacs FY24 appears under Other Current Liabilities,
  Note 23, p.166-167, which functions as the contract liability).

### 12. Other critical notes
- **Exceptional items**: NOT FOUND — no exceptional/one-time items disclosed or
  presented in the P&L for either year.
- **EPS**: Basic = Diluted = ₹17.93 FY25 vs ₹17.56 FY24 (Note 35, p.171) — 🟢 no
  dilution gap, no ESOP/convertible instruments disclosed anywhere in the
  document.
- **Bonus shares**: 94,03,734 bonus shares issued during FY24 (prior year); none
  in FY25 (Note 15, p.164). Equity share capital unchanged FY25 at ₹1,034.77
  Lacs (10,34,76,664 shares of ₹1 each).
- **Shareholding change — watch item**: Almond PolyTraders Pvt Ltd held 8.24% (a
  ">5% shareholder" line) at 31-Mar-2024 and **does not appear at all** in the
  31-Mar-2025 shareholder table (Note 15(c), p.164); simultaneously Bbigplas Poly
  Pvt Ltd (promoter/holding company) rose from 74.03% to 74.17%. The notes do not
  explain Almond PolyTraders' exit or where those shares went — outside the scope
  of related-party notes proper but adjacent to Note 15's shareholding
  disclosure; flagged here as a data point for the ownership-structure workstream
  (not independently anchored beyond the two snapshot tables).
- **Foreign currency exposure/hedging** (Note 43, p.180-181): Hedged forward
  contracts — Exports USD 1,45,00,000 (₹12,393.15 Lacs) FY25 vs USD 1,20,00,000
  (₹10,004.87 Lacs) + EUR 9,00,000 (₹811.96 Lacs) FY24; new Import hedge USD
  15,00,000 (₹1,282.05 Lacs) FY25, none FY24. Unhedged net trade receivables USD
  1,24,67,288 (₹10,655.75 Lacs) + EUR 7,47,215 (₹666.74 Lacs) FY25. Sensitivity:
  50bp currency move affects PBT by ₹566.05 Lacs FY25 vs ₹346.00 Lacs FY24 — the
  unhedged FX exposure to earnings has grown materially (+63.6%) YoY.
- **Capital commitments**: see Section 3 above (contingent liabilities table),
  ₹1,167.37 Lacs FY25 vs ₹227.31 Lacs FY24.
- **Segment reporting**: single segment, see Section 11.
- **Basic vs diluted EPS gap**: none, see above.
- **Events after balance sheet date**: Final dividend of ₹1.75 per share
  proposed on 15-May-2025 (Board meeting date), cash outflow ≈ ₹1,810.84 Lacs,
  subject to shareholder approval (Note 44 B, p.182-183) — this is the standard
  proposed-dividend disclosure, not an unusual subsequent event. No other
  post-balance-sheet event disclosed (no note under a separate "Subsequent
  Events" heading beyond the dividend).
- **CSR required vs actual**: see Section 9 — spent exceeded required both
  years.
- **ESOP dilution**: none present/disclosed.
- **Share capital changes**: bonus issue in FY24 only (see above); no
  fresh issuance, buyback, or rights issue in FY25.
- **Direct debits/credits to reserves bypassing P&L**: Other Comprehensive
  Income (actuarial remeasurement on gratuity) of (₹31.20) Lacs FY25 and
  (₹53.18) Lacs FY24 routed through OCI into "Other Comprehensive Income"
  reserve, per Ind AS 19 requirement — this is required treatment, not
  aggressive; correctly disclosed in Note 16 (Other Equity roll-forward,
  p.165).
- **Accounting ratios with company's own variance commentary** (Note 53, p.186,
  full table extracted): Current Ratio 3.01x FY25 vs 2.42x FY24 (+24.07%, just
  under the 25% disclosure trigger, "NA" reason given); Debt-Equity 0.06x vs
  0.10x (-44.64%, "decrease in Total Debt and increase in Equity because of
  Profit earned during the year"); Debt Service Coverage 12.80x vs 12.11x
  (+5.68%); **Return on Equity 24.82% vs 31.48% (-21.15%)**; Inventory Turnover
  11.63x vs 11.49x (+1.25%); Trade Receivables Turnover 6.02x vs 6.39x (-5.76%);
  **Trade Payables Turnover 11.26x vs 8.24x (+36.71%, "change in credit
  cycle")**; Net Capital Turnover 5.14x vs 6.75x (-23.91%); Net Profit Ratio
  0.07 vs 0.07 (-4.64%); **Return on Capital Employed 0.30 vs 0.36 (-16.06%)**.
  🟡 RoE and RoCE both declined meaningfully even though absolute profit grew
  (PAT ₹18,549.70 Lacs FY25 vs ₹18,166.94 Lacs FY24, +2.1%) — driven by equity
  base growth outpacing profit growth (retained earnings compounding, large cash
  build now sitting in low-yield treasury investments rather than being deployed
  or returned). This is a capital-efficiency signal an investor should weigh
  alongside the growth capex narrative in the operator context.

---

## PASS 1 SUMMARY — TOP 10 FINDINGS RANKED BY INVESTOR IMPORTANCE

1. 🟡 **Provenance correction**: this is the FY2024-25 annual report (year ended
   31-Mar-2025), not FY2020 as briefed — the most recent AR available, not stale.
   (Cover page/Auditor's Report, p.145-147.) [Not a company-quality flag; a
   pipeline-input-correctness flag.]
2. 🟡 **RoE fell from 31.48% to 24.82% and RoCE from 0.36 to 0.30** (Note 53
   Accounting Ratios, p.186) despite profit growth, because equity base grew
   faster (retained earnings/cash accumulation) than profit — capital efficiency
   is diluting even as the balance sheet strengthens.
3. 🟡 **Finished goods inventory grew 60.3% vs revenue growth of 7.08%** (Note
   10, p.161-162 vs Note 26, p.169) with no obsolescence/write-down disclosure to
   explain the build.
4. 🟡 **Royalty paid to fellow-subsidiary Kkalpana Industries fell 72.5%** while
   purchases from the same entity nearly doubled (+88.9%) — no explanation given
   in notes; arm's-length basis not independently verifiable from disclosure
   (Note 41, p.188-189).
5. 🟢 Company is **net cash** (negative net debt) in both years, gearing -0.07x
   FY25 / -0.02x FY24; ₹61.39 Cr newly parked in mutual funds this year (Note 44,
   p.182; Note 11, p.162) — clean balance sheet.
6. 🟡 **MSME payable dues up 35.9% and interest on delayed MSME payments
   recurs both years** (₹0.66 Lacs FY25, ₹0.86 Lacs FY24) — small in absolute
   terms but a recurring statutory-payment-timing issue (Note 21, p.166).
7. 🟢 Clean, unqualified auditor's opinion; no going-concern qualification; no
   fraud reported; no willful defaulter status; no promoter share pledge (Note
   Auditor's Report + CARO Annexure A, p.145-153; Board's Report §7.1, p.99).
8. 🟢 No related-party loans/ICDs to promoter entities, no outstanding
   related-party balances at year end, RPT total ≈1.3% of revenue — clean RPT
   profile in aggregate despite item 4 above (Note 41, p.188-189; Note 37,
   p.183-184).
9. 🟡 **Gratuity plan funded status deficit widened** from (₹508.55) Lacs to
   (₹639.23) Lacs, plan only ~16% funded by LIC-managed trust assets — fully
   recognized on balance sheet, not a hidden liability, but the funding gap
   is growing in absolute terms (Note 39(b), p.172-174).
10. 🟢 Receivables ageing quality **improved** YoY (overdue >6 months fell from
    1.44% to 0.24% of gross receivables) even as net receivable days rose
    modestly (~60 to ~65 days) — a mixed but net-neutral-to-positive
    receivables picture; no single customer concentration, no related-party
    receivables (Note 12, p.163-164; Note 40(f), p.176).

This concludes Pass 1. Pass 2 (what was missed) and Pass 3 (pattern pass +
consolidated analysis, including the final YAML block) follow as separate
pipeline calls per the Stage 2 instructions.
