# STAGE 2 — NOTES TO FINANCIAL STATEMENTS, PASS 1 (FULL EXTRACTION)
Company: Laxmi India Finance Ltd (LAXMIINDIA), NBFC-ML (MSME/mortgage/vehicle lender)
Run date: 2026-07-22

SOURCES READ (full notes sections, note-by-note):
- **[PROSPECTUS]** = inputs/annual-report/drhp.pdf (Prospectus dated 2025-07-31), Section V — Financial
  Information — Restated Financial Statements, printed pp. 289-386 (PDF pp. 294-391). Covers Restated
  Statement of Assets & Liabilities, P&L, Cash Flow, Changes in Equity, and Notes 1 to ~105 (Material
  Accounting Policies + explanatory notes) for FY23/FY24/FY25 (restated), plus "Other Financial
  Information" ratios page. All amounts in the Prospectus are ₹ in Millions; converted to ₹ Cr in this
  report (÷10) for consistency with pipeline convention.
- **[FY26RESULTS]** = inputs/results/Annual_Report_2024.pdf (misnamed; actually the FY26 Audited
  Results filing under Reg 33/52 SEBI LODR, board meeting 13-May-2026), all 29 pages. This is a limited
  stock-exchange results filing (Statement of P&L, Balance Sheet, Cash Flow for FY26 vs FY25) with only
  13 explanatory notes — not a full annual-report notes package. Amounts in this filing are ₹ in Lakhs;
  converted to ₹ Cr (÷100) below.

NOTE ON SCOPE: There is no glossy standalone AR for FY26 with a full notes package. The Prospectus
restated financials (FY23-FY25, ~105 notes) are the primary notes-quality source; the FY26 results
filing supplies the latest-year balance sheet/P&L and a thin set of 13 notes (co-lending, DA/ARC
transfers, labour code provision, DA revenue impact). Every note number in both documents was read.

---

## 1. ACCOUNTING POLICIES & CHANGES

- **Change in income recognition method, accrual → cash basis, applied retrospectively.**
  [PROSPECTUS] Note 1.1.A.4 and Note 1.2 (p.297/298): "the entity has changed the accounting method of
  certain incomes from accrual basis to cash basis. This change aligns the entity's accounting policy
  with the general industry practice." Restated retrospectively into FY24/FY23 comparatives per Note 104
  item (e) (p.383). 🟡 Watch — a shift from accrual to cash basis for "certain incomes" (largely File
  Cancellation/Collection/Pre-closure/late-payment/instrument-return/seizing charges per Note 25 exclusion
  language, Note H.3 p.306) is *less* accrual-based, which is generally the more conservative direction for
  a lender (recognising fee income only on realisation, not accrual), so this specific change reads as
  conservative, but it was made concurrently with a broader restatement exercise and the "aligns with
  industry practice" language is generic boilerplate that does not disclose the quantified pre-tax P&L
  swing per year in one place — investor must reconstruct it from Note 104(2)/(3) tables.

- **Material prior-period errors corrected via restatement — three separate GAAP errors, all caught only
  during IPO prospectus preparation, not by the original statutory audits.** [PROSPECTUS] Note 104,
  "Notes for Changes due to material errors" (p.383):
  (a) business correspondence transaction accounting treatment was wrong and has been corrected;
  (b) an ECL was **not** created on the receivable representing the Excess Interest Spread (EIS) on Direct
  Assignment (DA) — this has now been created (a conservative correction, i.e. more provisioning);
  (c)(1) the Company had **not recognised upfront gain on ARC (Asset Reconstruction Company)
  transactions in earlier years** due to "gap in interpretation of RBI Transfer-of-Loan-Exposure guidelines
  and Ind AS 109" — this is now rectified, i.e. **more gain is now recognised upfront** than the original
  audited financials showed;
  (c)(2) ARC Security Receipts had been measured with "disparity" vs Ind AS 109/107 and are now
  reclassified/re-measured at FVTPL;
  (d) software licence payments (Synoriq) had been **incorrectly capitalised as an Intangible Asset**
  when they should have been expensed (it was a service, not an owned asset) — corrected per Ind AS 8.
  🔴 Red Flag — four distinct, non-trivial GAAP errors in the original FY23/FY24 audited financials
  (wrong RPT-adjacent transaction treatment, missing ECL on a DA-related receivable, wrong revenue-timing
  treatment on ARC gains, wrong capitalisation of a software cost) were only caught and fixed during IPO
  prospectus preparation by the new auditor (S.C. Bapna & Associates), not flagged by the previous
  statutory auditor (A Bafna & Co.) at the time. Net P&L effect of all restatement + regrouping combined
  was small (Total Comprehensive Income FY24: ₹22.47cr as originally reported → ₹22.62cr restated; FY23:
  ₹15.45cr → ₹16.03cr restated — see Note 104(2), p.382), but the *individual line items* moved by much
  larger relative amounts (e.g., FY24 Net Gain on FV Changes moved from ₹0.59cr to ₹3.88cr, a >6x swing,
  driven by the ARC-gain-recognition correction, item c(1)/(2)).

- **Auditor changed mid-restatement.** [PROSPECTUS] p.290-291: current auditor S.C. Bapna & Associates
  (FRN 115649W) issued the FY25 audit report (19-May-2025) and re-examined FY24/FY23 for restatement
  purposes; the FY24 (04-May-2024) and FY23 (06-May-2023) statutory audits were done by the *previous*
  auditor, A Bafna & Co., whose reports carried **qualifications**: "Company has not implemented the
  feature of recording audit trail facility in its core business software (Jaguar) ... and same has not
  operated throughout the year for all transactions recorded in that software" (p.291). 🔴 Red Flag —
  a CARO Rule 11(g) audit-trail qualification for two consecutive years by the previous auditor.

- **Audit trail (edit-log) deficiency persists into FY25 under the new auditor too**, albeit narrower.
  [PROSPECTUS] p.290-291: the FY25 auditor's report states the accounting-software audit trail "operated
  throughout the year... except in one instance where the audit trail feature was disabled and then
  enabled. We are unable to assess whether there are any instances of audit trail feature being modified";
  and for the loan-collection software, "in absence of SOC 2 report from Service Provider's Auditor, we
  are unable to obtain sufficient appropriate audit evidence to comment whether the audit trail feature was
  enabled and remained operational." 🟡 Watch — narrowed from a blanket non-implementation (previous
  years) to a single instance + one system's SOC-2 gap, i.e., improving but not fully resolved.

- **ECL / staging methodology (NBFC-specific).** [PROSPECTUS] Notes C.3.1-C.3.6 (pp.302-305) and Note 53
  (p.358): three-stage Ind AS 109 model — Stage 1 (0-30 DPD, 12-month ECL), Stage 2 (30-90 DPD /
  qualitative SICR triggers, lifetime ECL), Stage 3 (90+ DPD, credit-impaired, lifetime ECL, 100% PD
  applied). Default definition is the standard 90-DPD test plus qualitative triggers (emergency funding
  request, material collateral value fall, unwaived covenant breach, borrower bankruptcy filing) —
  reasonably conventional, no aggressive stretching of the default definition. 🟢 Clean policy design.
  Provisioning coverage on Stage 3 (gross NPA): FY25 55.2% (₹6.72cr/₹12.18cr), FY24 54.4%
  (₹3.25cr/₹5.97cr), FY23 45.6% (₹1.52cr/₹3.33cr) [PROSPECTUS Note 5.6, p.318] — improving coverage,
  🟢 Clean trend. Ind AS 109 ECL provisions **exceed** the RBI IRACP regulatory minimum in every year
  shown (FY25: ₹13.33cr actual vs ₹6.51cr IRACP-required, a ₹6.82cr cushion; FY24: ₹5.09cr vs ₹3.94cr;
  FY23: ₹4.64cr vs ₹3.28cr) [PROSPECTUS Note 79, pp.371-373] — 🟢 Clean, conservative vs regulatory floor,
  no transfer to Impairment Reserve required (Note 79 footnote, p.373).

- **Depreciation / useful life.** [PROSPECTUS] Note 1.2.A(iii) and Note 9.1: Written Down Value method,
  Schedule II useful lives, 5% residual value across all PPE blocks; no revaluation in any year (Note
  9.1, p.321). 🟢 Clean, standard.

- **Impairment test assumptions / discount rates:** no goodwill or CGU impairment testing disclosed
  (Company has no goodwill/CGUs). Gratuity discount rate 6.64% (FY25), 6.94% (FY24), 7.27% (FY23) per
  government-bond yields [PROSPECTUS Note 50(B)(vii), p.354] — 🟢 Clean, in line with market yields.

- **Ind AS 116 leases.** [PROSPECTUS] Note 49 (p.353): incremental borrowing rate used as discount rate,
  11.15% (FY25), 12.40% (FY24), 13.31% (FY23); ROU asset ₹2.12cr, lease liability ₹2.21cr at FY25-end.
  🟢 Clean, immaterial in scale.

- **First-time adoption / new standards:** Note Q (p.310) — MCA notified no new Ind AS applicable to the
  Company for the year ended 31-Mar-2024; Labour Codes (effective Nov-2025) noted as a pending estimated
  impact in [FY26RESULTS] Note 10 — provision of ₹44.67 lakh (₹0.45cr) recognised as an estimate under
  "Employee Benefit Expenses" for FY26, pending final Central/State rules. 🟡 Watch — an estimate booked
  ahead of final rules; company states it will true up as clarity emerges.

## 2. RELATED PARTY TRANSACTIONS

[PROSPECTUS] Note 47 (pp.350-352), full table for FY25/FY24/FY23, ₹ in Cr (converted from Millions):

| Party | Nature | FY25 | FY24 | FY23 | YoY FY25 |
|---|---|---|---|---|---|
| Deepak Baid (MD, Promoter) | Director remuneration | 2.76 | 2.875 | 2.76 | -4.0% |
| Aneesha Baid (WTD, Promoter) | Director remuneration | 1.725 | 1.797 | 1.725 | -4.0% |
| Prem Devi Baid (Promoter) | Director remuneration | 1.380 | 1.438 | 1.246 | -4.0% |
| Various NEDs | Sitting fees | 0.31 | 0.192 | 0.092 | +61% |
| Deepak/Aneesha/Prem Devi Baid | Rent paid | 0.21 | 0.169 | 0.309 | +24% |
| Deepak Baid | Purchase of PPE (immovable property) | — | — | 3.00 | n/a |
| Aneesha/Deepak/Prem Devi Baid | Loan repaid (to promoters) | — | — | 5.56 | n/a |
| Aneesha/Deepak/Prem Devi Baid | Interest on such loan | — | — | 0.07 | n/a |
| Tejkaran Foundation (CSR Trust, KMP-controlled) | CSR expense | 0.10 | — | — | new |
| KMP (CFO/CS) | Short-term employee benefits (Note 47(D)) | 6.39 | 6.62 | 6.15 | -3.5% |

- RPTs as % of Total Revenue FY25: director remuneration + rent + sitting fees ≈ ₹6.4cr / ₹245.7cr ≈
  **2.6%** — small in scale. 🟢 Clean on magnitude.
- **Promoter/promoter-group personal and corporate guarantees securing Company borrowings and NCDs** —
  not a P&L RPT but a recurring credit-support dependency: [PROSPECTUS] Note 15.1 (NCDs), Note 16.2
  (secured term loans), Note 47(E), Note 99 (p.380) — Deepak Baid, Aneesha Baid, Prem Devi Baid give
  personal guarantees; Deepak Hitech Motors Pvt Ltd, Hirak Vinimay Pvt Ltd (holding company, 52.01%
  shareholder), Prem Dealers Pvt Ltd, and Dreamland Buildmart Pvt Ltd give corporate guarantees for bank
  term loans and NCDs across all three years. 🟡 Watch — the Company's borrowing cost/covenant profile is
  structurally dependent on continued promoter/promoter-group guarantee support; if this support were
  withdrawn or promoter shareholding/net worth were impaired, refinancing terms could tighten. This is
  disclosed but not quantified as a contingent liability (guarantees are given *by* related parties *for*
  the Company, not the reverse, so no contingent-liability recognition is required, but it is a
  structural dependency worth monitoring, especially as promoter shareholding has been diluting post-IPO
  per operator-context SHP data, 60.45%→60.17% Sep25→Mar26).
- **Title deed of a PPE property (carrying value ₹0.28cr) is registered in the personal name of Mr Deepak
  Baid (Managing Director), not the Company**, since the property was originally used by a proprietorship
  (Deepak Finance and Leasing Company) that converted into the present corporate entity in 2011; title
  has never been transferred to the Company; Company states it is "in process for transfer" [PROSPECTUS
  Note 9.4, p.322]. 🟡 Watch — a 14+ year unresolved formality; low financial materiality but a
  governance-hygiene flag typical of promoter-family NBFCs.
- No loans/advances to promoters, directors or KMPs outstanding in the nature of loans repayable on
  demand or without specified terms, in any of the three years [PROSPECTUS Note 48, p.352] — 🟢 Clean;
  Note 47(C) confirms max O/S to promoters was Nil at FY24-end and FY25-end (only FY23 had small O/S
  balances, since repaid).
- CSR routed partly through a KMP-controlled trust (Tejkaran Foundation) — ₹0.10cr FY25, new item.
  🟡 Watch — small in amount but a self-dealing-adjacent structure worth naming.

## 3. CONTINGENT LIABILITIES

[PROSPECTUS] Note 46 (p.349): contingent liabilities are **strikingly thin** for an NBFC of this scale —
only one line item in all three years: an income-tax demand of ₹0.09cr (FY25) under section 80JJA
(AY2020-21), appealed to CIT(A); Nil in FY24/FY23. No guarantees given by the Company for third parties,
no litigation provisions, no disputed indirect-tax matters disclosed. Capital commitments (partially
disbursed sanctioned loans) were ₹2.45cr (FY25), ₹15.05cr (FY24), ₹17.86cr (FY23) — routine, declining.
🟡 Watch — for a lender that runs DA/assignment and ARC-sale transactions with retained MRR (beneficial
economic interest), the near-total absence of contingent-liability disclosure (no FLDC, no recourse
guarantee lines) is *plausible* given Note 52.1 states the last securitisation-with-FLDC arrangement was
closed out in FY22-23 and DA transactions are structured to transfer substantially all risk/reward (hence
no residual guarantee recognition is required under Ind AS), but the absence of any narrative discussion
of this in the contingent-liability note itself (it is left to be inferred from Note 52) is a disclosure-
transparency gap rather than a substantive risk. No single item exceeds 10% of net worth. Total
contingent liabilities as % of net worth: FY25 ≈ 0.03% — immaterial in disclosed form.

## 4. TRADE RECEIVABLES

[PROSPECTUS] Note 4 (pp.314-315): "Other Receivables" (not trade receivables from lending customers —
the Company has no meaningful trade-receivable book since it is a lender, not a goods/services business).
FY25 ₹0.17cr, FY24 ₹0.31cr, FY23 ₹0.07cr — all "less than 6 months," no disputed or credit-impaired
receivables in the ageing schedule in any year. No ECL provision held against them (immaterial). 🟢 Clean,
not a meaningful analytical category for this NBFC — the "receivables" that matter are Loans (Note 5) and
Receivables on Assigned Loans (Note 7), both covered separately below.

## 5. INVENTORY

Not applicable — the Company is an NBFC lender with no inventory. 🟢 N/A.

## 6. INVESTMENTS

[PROSPECTUS] Note 6 (p.319): Investment portfolio is FVTPL, dominated by **Security Receipts (SR) of
Asset Reconstruction Companies (ARC)** received in exchange for stressed-loan sales:
FY25 ₹28.62cr, FY24 ₹14.20cr, FY23 ₹7.23cr — **roughly doubling year-on-year**, driven by the Company's
increasing use of ARC sales to manage stressed assets (Note 87, 93, 98(c)). SR are Level-2 fair-valued
using NAV (Note 56, p.361) — illiquid, thinly-traded instruments whose "fair value" is really the ARC
trust's own NAV computation, not a market price. 🟡 Watch — SR carrying value growing faster than the
loan book (loan book grew ~38% FY24→FY25; SR grew ~102% FY24→FY25), meaning a rising share of balance
sheet is parked in ARC-trust paper rather than cash from stressed-asset disposals; recovery ratings on
the underlying SR trusts (Note 98, p.380) show "more than 150%" and "100-150%" expected recovery per
Infomerics — a positive input, but self-reported by the ARC/rating agency, not yet realised in cash.
Small residual investments: Mutual Fund units ₹0.09cr, Equity-oriented Fund-ULIP ₹0.57cr FY25 (Note 6).
No subsidiaries, JVs, ICDs or loans given to related entities (Note 6, Note 55). 🟢 Clean on structure —
no consolidation complexity, no related-party ICDs.

## 7. BORROWINGS

[PROSPECTUS] Notes 15-17 (pp.326-330), full instrument tables:

- **Debt Securities (NCDs):** FY25 ₹27.39cr, FY24 ₹5.00cr, FY23 ₹23.17cr — all secured by first/exclusive
  hypothecation charge on receivables (min. 100% coverage) plus **personal guarantees of Deepak Baid,
  Aneesha Baid, Prem Devi Baid** (Note 15.1). Coupon range 11.49%-15.04% across outstanding series
  (Note 15.2); maturities laddered 2025-2027.
- **Borrowings (other than debt securities):** FY25 ₹1,101.73cr — Term loans from banks ₹676.24cr
  (7.70%-14.25%), Term loans from NBFC/FIs ₹418.62cr (8.02%-14.50%), unsecured term loan from
  "other than related parties" ₹6.56cr (11.90%), associated liabilities re co-lending ₹0.31cr. All
  secured term loans carry **personal guarantees of Directors + corporate guarantees of promoter-group
  companies** (Starpoint Constructions Pvt Ltd, Hirak Vinimay Pvt Ltd, Dreamland Buildmart Pvt Ltd, Prem
  Dealers Pvt Ltd) — Note 16.2 (p.328). No default in repayment of dues to lenders in any year (Note
  16.3). No breach of covenant in any year (Note 62, p.365). Company has not been declared a Wilful
  Defaulter (Note 16.6).
- **Subordinated Liabilities:** unsecured term loan "from others" at 16.00% coupon, FY25 ₹7.95cr,
  FY24 ₹7.94cr, FY23 Nil (Note 17) — high-cost sub-debt, small in scale, boosts Tier II capital.
- **Repayment schedule (5-yr ladder), FY25 (Note 16.1):** Within 1 yr ₹390.02cr (36% of secured bank+NBFC
  debt), 1-3 yrs ₹527.04cr, 3-5 yrs ₹177.71cr, >5 yrs ₹0.11cr — reasonably laddered, no cliff-maturity
  concentration.
- **Debt/Equity ratio** (Note 100, p.381): FY25 4.42x, FY24 3.80x, FY23 4.04x — 🟡 Watch, rising leverage
  into the IPO (pre-IPO net worth base); post-IPO the operator context shows this fell to 2.87x by
  FY26-end per the FY26 results filing (Reg 52(4) disclosure, Debt-Equity Ratio 2.88 as at 31-Mar-2026) —
  consistent deleveraging post-capital-raise.
- **CRAR declining across the restated years:** FY25 20.80%, FY24 21.81%, FY23 23.09% (Note 74/100) —
  still comfortably above the regulatory minimum (15%) but the trend is down as growth outpaces retained
  capital, pre-IPO. 🟡 Watch (resolved by IPO capital per FY26 results, CRAR 26.12%).
- **Top-20 funding counterparty concentration** (Note 73, p.367): 47 counterparties fund 98.48% of total
  liabilities FY25 (43 counterparties/97.90% FY24) — high concentration among *wholesale* lenders is
  normal for an NBFC of this size, but top-10 borrowings alone are 53.94% of total borrowings FY25 (down
  from 62.27% FY24) — 🟢 Clean, diversifying trend.

## 8. TRADE PAYABLES

[PROSPECTUS] Note 14/14.1/14.2 (pp.324-326): Trade payables FY25 ₹1.95cr, FY24 ₹1.23cr, FY23 ₹1.15cr.
MSME dues: FY25 ₹0.026cr, FY24 ₹0.144cr (of which ₹0.026cr is >45 days / disputed-MSME), FY23 ₹0.012cr —
all immaterial; **no interest paid or payable** under MSMED Act Section 16 in any year (Note 14.1(ii)-(v)).
🟢 Clean, no MSME payment-delay pattern.

## 9. PROVISIONS

[PROSPECTUS] Note 20 (pp.330-331), Note 50 (pp.353-355):
- Employee benefits (Gratuity): defined-benefit obligation ₹1.553cr FY25 (₹1.128cr FY24, ₹1.059cr FY23),
  unfunded (Company does not fund the plan — Note 50(B) "Unfunded Plan Risk" acknowledges this explicitly
  as a liability risk). Actuarial assumptions: discount rate 6.64% FY25 (declining from 7.27% FY23),
  salary escalation 12.00% FY25 (steady), attrition 30-40% FY25 (rising from 15-19% FY23) — 🟡 Watch, a
  rising attrition assumption is realistic for a branch-heavy MSME lender but flags high frontline
  employee churn, a business-quality signal worth cross-referencing against the business-model stage.
- No warranty, decommissioning, or onerous-contract provisions (not applicable to an NBFC).
- Litigation provisions: none disclosed beyond the ₹0.09cr income-tax demand (Note 46).
- CSR shortfall provisioning: FY24 had a ₹0.21cr under-spend not fully provided against (Note 45,
  p.349) — 🟡 Watch, minor compliance gap, resolved by FY25 (over-spent by ₹0.07cr FY25).

## 10. DEFERRED TAX

[PROSPECTUS] Note 8 (p.320), Note 44 (pp.347-348): Net Deferred Tax **Liability** (not asset) in all
three years: FY25 ₹1.30cr, FY24 ₹4.97cr, FY23 ₹3.88cr — driven primarily by DTL on "Interest receivable
on direct assignments" (₹5.24cr FY25, ₹5.97cr FY24, ₹4.98cr FY23), i.e., the EIS/excess-interest-spread
recognised for accounting purposes ahead of its taxability — directly linked to the DA/ARC upfront-gain
recognition issue flagged in Section 1 above. Effective tax rate: FY25 23.97%, FY24 24.19%, FY23 27.47%
vs statutory 25.17% (Note 44(iii)) — no material unexplained gap; Company has elected Section 115BAA
concessional regime. No MAT credit (elected 115BAA, so MAT is not applicable). 🟢 Clean reconciliation,
but the DTL composition reinforces that DA/ARC gain timing is a first-order driver of the tax and P&L
profile, not a rounding item.

## 11. REVENUE DETAILS

[PROSPECTUS] Notes 24-27 (pp.337-338), Note 57-58 (p.364):
- **Interest Income breakdown, FY25/FY24/FY23 (₹cr):** Interest on Loans 214.91/145.35/109.39; Interest
  from Margin Money/FDRs 8.32/5.56/2.25; Income from Securitisation 0.00/0.00/1.90; **Income on
  Derecognised (Assigned) Loans 8.09/13.87/11.30**. Total Interest Income 231.31/164.79/124.82.
- **Income on Derecognised (Assigned) Loans + the separate DA/ARC upfront-gain line (Note 52) together
  represent the single largest swing factor in reported profitability** — see Top Findings below for the
  consolidated calculation.
- Fees & Commission income up sharply: ₹13.46cr FY25 vs ₹4.47cr FY24 vs ₹4.44cr FY23 (+201% YoY FY25) —
  driven by Pre-closure charges (₹4.78cr FY25 vs ₹1.11cr FY24) and Instrument Return charges (₹2.71cr
  FY25 vs ₹0.44cr FY24) [Note 25 footnote, p.337]. 🟡 Watch — a >3x jump in one year in prepayment- and
  bounced-instrument-related fee income is worth cross-checking against loan-book growth (loan book grew
  ~38% FY24→FY25, fee income grew ~201%) — fee income is growing roughly 5x faster than the book,
  disproportionate and worth a management question.
- No single customer contributes ≥10% of revenue (Note 58(c)) — 🟢 Clean, no concentration.
- Single reportable segment (lending) per Ind AS 108; CODM = Managing Director (Note 58(a)) — 🟢 standard
  for an NBFC of this size, though it means no product-line (MSME vs vehicle vs mortgage) segment P&L is
  disclosed in the notes — investors must rely on the Selected Statistical Information section elsewhere
  in the Prospectus (outside notes scope) for product mix.

## 12. OTHER CRITICAL NOTES

- **DA/ARC transaction accounting is the dominant swing factor in reported earnings quality** — see Top
  Findings.
- **No exceptional items in any year** (Note 65, p.365) — 🟢 Clean, no exceptional-item recurrence pattern
  to assess (none used to flatter results).
- **No goodwill/intangibles impairment issue**; intangible assets are small and software-only (Note 12);
  one software-capitalisation error was corrected (Section 1 above).
- **No capital commitments beyond loan sanctions** already disclosed (Note 46(b)).
- **No foreign-currency exposure, no derivatives** in any year (Notes 83-85, 101-102) — 🟢 Clean, simple
  balance sheet on this dimension.
- **EPS gap (basic vs diluted):** FY25 8.78 vs 8.78 (no dilution — ESOPs not yet vested/exercisable);
  FY24 6.11 vs 5.66 (a real dilution gap, -7.4%, from partly-paid share conversion timing); FY23 5.02 vs
  5.02 (nil). 🟢 Clean, dilution source (partly-paid share conversion) is disclosed and explained
  (Note 22(b)).
- **ESOP dilution:** ESOP 2023 plan, grant date 01-Oct-2024, 3,93,283 options granted at exercise price
  ₹92 vs fair value of underlying ₹114.83 at grant (in-the-money grant), vesting 20%/20%/30%/30% over
  12/24/36/48 months; Black-Scholes fair value ₹40.18-₹56.37/option; expense recognised ₹0.41cr FY25
  (Nil prior years) [Note 51, p.355]. 🟡 Watch — modest dilution (7,50,556 options post-bonus-adjustment
  reserved vs 4.18cr shares outstanding, ~1.8% potential dilution), in-the-money grant price is a mild
  governance point worth noting but not a red flag at this scale.
- **Events after balance sheet date:** none disclosed within the notes themselves (Note 1.1.A.5/A.7
  confirms Restated FS do not reflect post-30-Jun-2025-board-meeting events) — the major post-period
  event (Up Money Ltd DA-pool stress, Q3 FY26) is **not and cannot be** in these FY23-FY25 restated notes;
  it surfaces instead in the FY26 results filing and rating-agency commentary (see cross-reference below).
- **Share capital changes:** sub-division of face value from ₹10 to ₹5 per share (Nov-2024 board/EGM),
  bonus-like right issue of 1,04,43,62 shares during FY25 (Note 22(a)) — routine pre-IPO capital
  structuring, adequately disclosed.
- **No direct debits/credits to reserves bypassing P&L** other than the routine Statutory Reserve
  (Section 45-IC RBI Act) transfer and Impairment Reserve movements, both standard NBFC mechanics
  (Note 23) — 🟢 Clean.
- **No CSR shortfall carried at FY25-end** (resolved, see Section 9). CSR spend fully compliant FY25/FY23,
  a small carry-forward gap in FY24 only.
- **Complaints from customers rose sharply** — see Top Findings.
- **RBI interest-on-interest (COVID moratorium) refund liability: Nil recorded in all years** (Note 78,
  p.379) — Company states methodology was circulated by IBA but it has not recorded any liability towards
  estimated interest relief. 🟡 Watch — an unquantified item; likely immaterial at this point (multiple
  years post-moratorium) but the note itself provides no quantification or rationale for treating it as
  Nil, which is a disclosure gap.
- **[FY26RESULTS cross-reference, outside restated-notes scope but read for completeness]**: FY26 audited
  results filing Note 12 shows Interest Income "inclusive of Unrealised Gain/(Loss) booked on DA
  Assignment" with an explicit P&L impact table: Increase in Revenue ₹7.53cr FY26 vs ₹8.09cr FY25 (Note
  12, p. per filing) — confirming the DA-gain-recognition issue is a continuing, not one-off, feature of
  the earnings build, consistent with the pattern already flagged from the restated Prospectus notes.
  FY26 filing Note 9.4 states Company sold stressed loan assets with write-offs of ₹2.77cr for FY26
  (**note: this figure is materially lower than the ~₹4.53cr FY26 write-off figure cited in the operator's
  non-anchored summary sourced from investor-presentation commentary** — flagged as a reconciliation gap
  between the audited note and the investor-deck figure; the audited note (₹2.77cr) is the anchored
  number). FY26 filing Note 9.1/9.2 confirm continuing DA assignment activity (972 accounts assigned,
  ₹41.18cr assigned part FY26) and DA acquisition (4,251 accounts acquired, ₹28.74cr acquired part FY26).
  FY26 filing Note 11 confirms a new Co-Lending Arrangement entered FY25-26 (90%/10% Laxmi India/partner
  split, one CLA partner, ₹15cr disbursement quantum, max 15% company interest share) — a new off-book
  structuring channel to watch going forward for disclosure completeness in FY27.

---

## PASS 1 SUMMARY — TOP 10 MOST SIGNIFICANT FINDINGS

| Rank | Finding | Note anchor | Rating | Why it matters |
|---|---|---|---|---|
| 1 | **DA/ARC upfront gain-on-sale is a very large and rising share of reported PAT**: gain from derecognition of assigned loans was ₹9.63cr (FY25, 26.8% of PAT ₹36.01cr), ₹15.19cr (FY24, 67.6% of PAT ₹22.47cr), ₹12.15cr (FY23, 76.1% of PAT ₹15.97cr). Core lending profitability excluding this gain is materially thinner than headline PAT in FY23/FY24, improving in FY25 as the book has scaled. | [PROSPECTUS] Note 52.2/98(a), pp.355,379 | 🔴 Red Flag | This is the single biggest earnings-quality question for the Company: a large, judgment-dependent, non-cash gain recognised at the point of sale drives the majority of two of the three restated years' profit. Investors must separate "core NII/fee-based earnings" from "DA-gain-boosted PAT" when assessing run-rate quality and when comparing to the Up Money DA-pool stress event in FY26. |
| 2 | **The original (pre-restatement) audited FY23/FY24 financials had NOT recognised this DA/ARC gain upfront at all** — it was added retrospectively via the restatement because the original treatment (per the Company's own note) reflected a "gap in interpretation of RBI Transfer-of-Loan-Exposure guidelines and Ind AS 109." Three other material errors (business-correspondence accounting, missing ECL on DA receivable, wrong software capitalisation) were corrected in the same restatement exercise, by a new auditor, only during IPO preparation. | [PROSPECTUS] Note 104(a)-(d), p.383 | 🔴 Red Flag | Reveals that the previous statutory auditor's signed-off financials materially misapplied Ind AS 109/8 on a revenue-recognition-adjacent item for two consecutive years, undetected until IPO diligence. This raises a question about the rigor of pre-IPO financial control and whether further, smaller misstatements remain uncorrected in periods not covered by the restatement. |
| 3 | **Rising NPA trend was already visible before the FY26 Up Money DA-pool stress event**: Gross Stage-3/Total Loans ratio rose from 0.58% (FY23) to 0.73% (FY24) to 1.07% (FY25); gross NPA balance more than tripled, ₹3.33cr→₹5.97cr→₹12.18cr over the same period. The largest loan segment (MSME/LAP, "Other personal loans," ~80% of book) shows the clearest deterioration: 0.48%→0.61%→1.12% gross-NPA-to-exposure FY23→FY24→FY25. | [PROSPECTUS] Note 75/93(d), pp.368,377 | 🟡 Watch | The Up Money-related GNPA spike to 2.13-2.40% in FY26 (per rating agency/operator context) is not an isolated shock; it sits atop an already-rising organic NPA trend in the pre-IPO years, which softens the "one-off DA-partner problem" framing management gives it. |
| 4 | **Customer complaints surged far faster than loan-book growth**: total complaints received rose from 18 (FY23) to 123 (FY24) to 341 (FY25), a 283% YoY jump in FY25 alone (loan book grew ~38% over the same period); "Credit Information Companies related" complaints (Ground 1) rose from 11→64→245 over the same years. | [PROSPECTUS] Note 96, pp.377-378 | 🟡 Watch | A disproportionate rise in CIBIL/credit-bureau-related complaints against a lender using cash-flow underwriting and whole-family co-borrower/guarantor structures (per operator-context collections practices) warrants a direct management question on collections conduct and CIBIL-reporting accuracy — reputational/regulatory risk if unaddressed. |
| 5 | **Previous auditor's qualified opinion on audit-trail (edit-log) non-implementation for two consecutive years (FY23, FY24); current auditor flags a narrower but still-unresolved audit-trail gap for FY25** (one instance of the feature being disabled/re-enabled; SOC-2 report unavailable for the loan-collection software). | [PROSPECTUS] p.290-291 | 🔴 Red Flag | A recurring IT-governance control weakness across two different audit firms and three years is a data-integrity concern for a lending business whose entire asset quality disclosure (staging, ECL) depends on system-generated transaction records. |
| 6 | **Fee & commission income grew ~201% YoY in FY25 (₹4.47cr→₹13.46cr) — roughly 5x faster than the loan book (~38% growth)** — driven by pre-closure charges (+330%) and instrument-return charges (+516%). | [PROSPECTUS] Note 25, p.337 | 🟡 Watch | Disproportionate fee growth relative to book growth deserves a direct question: is this a genuine shift in fee structure/pricing power, or a timing/recognition effect tied to the same period's accounting-policy change (accrual→cash basis for these very fee categories)? |
| 7 | **Investment in ARC Security Receipts (SR) roughly doubled YoY and is growing faster than the loan book**: ₹7.23cr (FY23) → ₹14.20cr (FY24) → ₹28.62cr (FY25), Level-2 fair-valued via ARC-trust NAV (not a market price). | [PROSPECTUS] Note 6, 56, 98, pp.319,361,380 | 🟡 Watch | A rising share of balance sheet sits in illiquid ARC-trust paper valued by the ARC's own NAV computation rather than realised cash from stressed-asset sales; recovery ratings ("100-150%+") are agency estimates, not cash-in-hand. |
| 8 | **Promoter and promoter-group entities give personal and corporate guarantees securing essentially all secured Company debt (bank loans, NBFC/FI loans, NCDs)** across all three restated years, and title to one PPE property remains registered in the MD's personal name 14+ years after incorporation-conversion. | [PROSPECTUS] Notes 15.1, 16.2, 47(E), 99, 9.4 | 🟡 Watch | Structural dependency of the Company's funding cost/covenant profile on continued promoter credit support and an unresolved title-transfer formality are governance-hygiene items to monitor, particularly as promoter shareholding dilutes post-IPO (60.45%→60.17%, Sep25-Mar26 per operator context). |
| 9 | **Contingent liabilities disclosure is unusually thin for an NBFC of this scale** — a single ₹0.09cr income-tax demand is the *only* contingent liability shown in any of the three years; no guarantee, litigation, or securitisation-recourse contingent items are disclosed despite active DA/ARC transaction volumes. | [PROSPECTUS] Note 46, p.349 | 🟡 Watch | Plausible given the DA structure transfers substantially all risk/reward and the last FLDC-bearing securitisation closed in FY22-23, but the note provides no narrative cross-reference to Note 52/98 to make this explicit — a disclosure-transparency gap rather than a substantive risk, worth a direct management confirmation. |
| 10 | **CRAR declined steadily pre-IPO (23.09% FY23 → 21.81% FY24 → 20.80% FY25) while Debt/Equity rose (4.04x → 3.80x → 4.42x)**, both trends reversed by the IPO capital raise (FY26 CRAR 26.12%, D/E 2.87-2.88x per FY26 results filing and operator context). | [PROSPECTUS] Note 74/100, pp.374,381; [FY26RESULTS] Reg 52(4) Annexure | 🟢 Clean (resolved) | Confirms the IPO capital was needed and used as intended to correct a genuinely tightening pre-IPO capital-adequacy trajectory; post-IPO metrics are healthy, but this underlines why the fresh-issue proceeds were structurally necessary rather than purely growth-optionality capital. |

**Pass 1 complete.** Every note number in the Prospectus Restated Financial Statements (Notes 1 through
105) and every note in the FY26 audited results filing (Notes 1 through 13) was read. Proceeding to
Pass 2 (what was missed) in the next call.
