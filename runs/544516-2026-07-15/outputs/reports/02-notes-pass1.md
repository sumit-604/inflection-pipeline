# STAGE 2 — NOTES TO FINANCIAL STATEMENTS — PASS 1: FULL EXTRACTION
**Company:** Airfloa Rail Technology Ltd | **Ticker:** 544516 (AIRFLOA) | **Run date:** 2026-07-15
**Source document:** `inputs/annual-report/1758608206692.pdf`

## DOCUMENT IDENTIFICATION FLAG (read before using this extraction)
The file supplied as {{ANNUAL_REPORT}} is **not a conventional annual report**. It is the company's **IPO Prospectus dated September 16, 2025** (386 pages), filed for the BSE SME platform listing. It contains no "Notes to Accounts 1, 2, 3…" in the traditional annual-report sense. Instead, the financial statements are furnished as **Restated Financial Statements** per SEBI ICDR / ICAI Guidance Note, structured as **Annexures I through XLVI (Consolidated)** and **Annexures I through XLVII (Standalone)**, audited by M/s. Varadarajan & Co (current auditor, appointed for the FY25 audit; FY24 and FY23 audits were originally done by G. Sekar Associates — auditor change ahead of IPO).
- Consolidated restated financials: **FY25 only** (one year), because the subsidiary (Sree Dakssnaa Aerospace and Defence India Pvt Ltd) was incorporated 11-June-2024 and this is the first consolidation.
- Standalone restated financials: **FY23, FY24, FY25** (three years) — this is the only source with a genuine trend.
- There is no separate Annual Report and no DRHP in the file set; all extraction below is anchored to this Prospectus's Annexures (cited as "Annexure [no.], CFS p.[x]" for consolidated or "Annexure [no.], SFS p.[x]" for standalone, using the document's own internal page stamps CFS1–CFS39 and SFS1–SFS45).
- All figures below are converted from the source's ₹ Lakhs to **₹ Crores** (÷100, exact conversion, not an estimate) per pipeline convention. Original ₹ Lakhs figure is not separately restated in each line, but conversion is precise to 2 decimals.
- This gap (no traditional annual report, no DRHP, single-year consolidated base) is itself a Section-2 finding, flagged in the Top 10 below.

---

## 1. ACCOUNTING POLICIES & CHANGES
(Annexure IV, Significant Accounting Policies, CFS p.8–11 / SFS p.8–12)

- **Accounting framework: Indian GAAP (IGAAP), not Ind AS.** Financial statements prepared under Schedule III, Companies Act 2013, historical cost convention (Note 2.01). No Ind AS 115 five-step revenue model, no Ind AS 116 lease accounting (no ROU asset / lease liability anywhere in the annexures — **NOT FOUND IN DOCUMENT**), no Ind AS fair value hierarchy note. 🟡 Watch — normal for an SME filer but means IND AS-style disclosures (ECL matrix, lease right-of-use, fair value levels) simply do not exist; investors should not expect Ind AS comparability with larger peers.
- **Depreciation policy:** WDV method, "rates arrived at based on the useful lives estimated by the management, **or** those prescribed under Schedule II" (Note 2.06, Annexure IV). No asset-class useful-life table disclosed — cannot verify whether management's estimated lives are more or less conservative than Schedule II. **NOT FOUND IN DOCUMENT** (specific useful lives by asset class). 🟡
- **Intangibles:** amortised SLM over 5 years (Note 2.06). Immaterial balances (₹0.0086 Cr net block, planning software + CREO elements, Annexure XV/XIV PP&E schedule, SFS p.22–24) — 🟢.
- **Revenue recognition:** "Revenue is recognized to the extent it is probable that economic benefits will flow… Sales are recognized on transfer of significant risk and ownership which generally coincide with the despatch of goods" (Note 2.13). Single-point, dispatch-based recognition — not aggressive for a manufacturing/fabrication business. 🟢
- **Impairment policy** (Note 2.08): standard boilerplate (higher of net selling price / value in use); **no quantified growth-rate or discount-rate assumptions disclosed anywhere** — **NOT FOUND IN DOCUMENT**.
- **ECL / doubtful debts:** Policy is silent on a formal ECL matrix (pre-Ind-AS). Provision for Bad & Doubtful Debts is **₹0.00 Cr in all three years (FY23, FY24, FY25)** despite receivables aged 1–3 years and beyond 3 years appearing in the ageing schedule (Annexure XIX/XXXIV) — see Section 4. 🔴 Watch/Red Flag — provisioning adequacy is questionable.
- **Major prior-period restatement / material errors corrected:** The Annexure IV reconciliation notes (Note 3 and Note 4, both standalone SFS p.13–14 and consolidated CFS p.12–13) disclose that historically the company **did not book**: gratuity provision, CSR expenditure liability, correct interest on borrowings, interest on late statutory dues (TDS), interest on delayed MSME payments, and had **incorrectly computed income tax and deferred tax** in prior years. All of these are now retrospectively restated across FY23–FY25. 🔴 Red Flag — breadth and repetition of "inadvertently missed" items (recurring language across gratuity, CSR, MSME interest, TDS interest, rates & taxes) points to a weak financial-control environment pre-IPO, now being cleaned up specifically for listing.
- **Section 185 (Companies Act) violation:** Auditor's report states explicitly: "The Company has violated provisions of Section 185 in the financial years ended March 31, 2024 and March 31, 2023 as the company has given loans to related parties which has been repaid till date and hence, such non-compliance does not exist as on August 21, 2025" (CFS p.2 item 8(iv); SFS p.3 item 8(iv)). 🔴 Red Flag — statutory violation, remediated only by repayment, not contemporaneous compliance.
- **Section 115BAA tax election:** "The Company has opted for income tax rates specified under section 115BAA of Income Tax Act, 1961 from financial year 2024-25 onwards" (Annexure XXXVIII footnote, SFS p.37). Explains FY25 tax rate drop to 25.17% from 29.12% (FY24) / 27.82% (FY23), and MAT rate going to 0% from FY25. 🟢 routine.

## 2. RELATED PARTY TRANSACTIONS
(Annexure XXXV, CFS p.30 / SFS p.34)

Full three-year (FY23–FY25, standalone) RPT table extracted. Key relationships and amounts (₹ Cr, FY25 transaction / FY25 outstanding):
| Party | Relationship | Nature | FY25 txn (₹Cr) | FY25 O/S (₹Cr, Payable/(Receivable)) |
|---|---|---|---|---|
| Dakshinamoorthy Venkatesan | Promoter/MD | Rent 0.11, Remuneration 0.66, Advance repaid 4.57, Advance given 2.64 | — | Nil |
| Dakshinamoorthy Manikandan | Promoter/MD | Rent 0.11, Remuneration 0.66, Advance repaid 6.64, Advance given 5.97 | — | (1.39) receivable |
| Raghavendra Industries | Controlled by relative of director | Sales of goods 2.01, Purchase of goods 0.68 | — | 7.46 receivable — large and growing (FY23: 4.91, FY24: 4.83, FY25: 7.46) |
| Starkeon Engineering Pvt Ltd | Controlled by relative of director | Capital Advance Given 0.73; R&D expense nil | — | 1.98 (capital advance, ties to machinery purchase — see Section 3) |
| Bharani Engineering Industries Pvt Ltd | Controlled by relative of director | Sales/Purchase of goods | — | (1.72) payable |
| Sree Dakssnaa Aerospace & Defence India Pvt Ltd | Subsidiary (new, w.e.f. 11-June-2024) | Customer Advance Received 1.83 | — | (1.81) payable |
| Papa Sanjeevi Karunakaran | CFO w.e.f. 01-07-2024 | Salary expense 0.07 | — | (0.01) |
| Apex Material Sciences | Controlled by relative of director | Advance repaid/given | — | 1.21 receivable |
| Airtrec Equipments, Airflow Energy Solutions, Nautone Pvt Ltd | Controlled by relative/director | Advances | — | small balances 0.06–0.38 |

- **RPT as % of revenue:** related-party sales (Raghavendra Industries ₹2.01 Cr) ≈ 1.05% of FY25 revenue (₹192.39 Cr) — small. But **RPT loans/advances to Promoters and related parties were material historically**: per Annexure XLV (loans and advances in the nature of loans, SFS p.39), Promoters' loans outstanding were **₹2.44 Cr (50.41% of total such loans) in FY23** and **₹2.80 Cr (55.49%) in FY24**, falling to **₹0 (0.00%) in FY25** — consistent with the Section 185 remediation noted above. Related-party loans (non-promoter) stayed material: FY23 ₹2.06 Cr (42.56%), FY24 ₹2.16 Cr (42.86%), FY25 ₹1.65 Cr (76.42% of a much smaller base). 🟡 Watch.
- **New related parties this year:** subsidiary Sree Dakssnaa Aerospace (11-June-2024); CFO Papa Sanjeevi Karunakaran (01-07-2024); Venkatesan Sathishkumar and Manikandan Nanthini added as relative/director w.e.f. 24-07-2024.
- **Non-arm's-length signal:** capital advance of ₹0.73 Cr (FY25) to Starkeon Engineering Pvt Ltd (relative-controlled) for purchase of machinery — cross-references directly to the capital commitment note (Section 3 below). Paying a related party in advance for capex, rather than an independent vendor, is a related-party-fairness question worth raising with management. 🟡

## 3. CONTINGENT LIABILITIES
(Annexure XXXIX, CFS p.35 / SFS p.38)

- Claims against the company not acknowledged as debt: **FY25 ₹0.40 Cr, FY24 ₹0.20 Cr, FY23 nil.** Both are GST demand-appeal matters: Order No. 527/2024-SUPDT dated 20-Aug-2024, demand ₹20,01,526 (₹0.20 Cr), appealed 26-Nov-2024; and Order No. 17/2024-SUPD dated 27-Feb-2024, demand ₹19,87,584 (₹0.20 Cr), appealed 21-Jun-2024.
- **Total contingent liabilities as % of net worth:** ₹0.40 Cr / ₹108.44 Cr net worth (FY25) = **0.37%** — immaterial. 🟢
- No item exceeds 10% of net worth. No guarantees for subsidiaries recorded as a contingent line (financial guarantees "nil" in this table), though see Section 7 for personal/corporate guarantees backing borrowings — those are not treated as company contingent liabilities in this note but are a real promoter-risk item.
- **Commitments:** ₹0.12 Cr (₹11.66 Lakh) capital commitment "not provided for" (FY25 only; nil FY23/FY24). Footnote explains: Starkeon Engineering Pvt Ltd acquired a Heavy Duty Horizontal Turnmill Center, CNC Vertical Machining Center, Rotary Table and Hydraulic Press Brake under a purchase order dated 25-Oct-2024 valued at **₹2.10 Cr**, against which Airfloa had paid **₹1.98 Cr** as of 31-Mar-2025 — the ₹0.12 Cr balance is the unpaid commitment. This ties out exactly with the related-party capital advance in Section 2. 🟢 (numbers reconcile — a positive consistency signal even though the RPT nature is a fairness question).

## 4. TRADE RECEIVABLES
(Annexure XIX/XXXIV, CFS p.18,29 / SFS p.20,33)

Standalone, ₹ Cr:
| | FY23 | FY24 | FY25 |
|---|---|---|---|
| Total trade receivables | 48.77 | 101.71 | 127.60 |
| >6 months (unsecured, good) | 7.78 | 18.15 | 29.83 |
| >6 months as % of total | 15.95% | 17.85% | 23.38% |
| Doubtful / ECL provision | 0.00 | 0.00 | 0.00 |

- **Ageing (Annexure XXXIV):** FY25 buckets (₹Cr): <6mo 97.77, 6mo–1yr 13.57, 1–2yr 9.56, 2–3yr 6.66, >3yr 0.04. FY24: <6mo 83.56, 6mo–1yr 4.26, 1–2yr 13.79, 2–3yr 0.10, >3yr nil. FY23: <6mo 40.99, 6mo–1yr 1.19, 1–2yr 5.31, 2–3yr 0.74, >3yr 0.53.
- **Trend: >6-months share of receivables is deteriorating each year (15.95% → 17.85% → 23.38%)**, and the 1–2yr bucket jumped materially in FY24 (₹13.79 Cr) before falling back in FY25 (₹9.56 Cr) — inconsistent/volatile ageing. 🟡 Watch → feeds FLAG-CASH.
- **Zero doubtful-debt provisioning across all 3 years** despite ₹6.66 Cr sitting in the 2–3 year bucket and receivables generally aged out to >1 year totalling ₹16.26 Cr (FY25) — provisioning adequacy is a real concern given the ECL policy gap noted in Section 1. 🔴
- **No single-customer concentration disclosed** — **NOT FOUND IN DOCUMENT** (no top-customer % anywhere in the annexures).
- **Related-party receivables:** Raghavendra Industries ₹7.46 Cr (FY25, up from ₹4.83 Cr FY24, ₹4.91 Cr FY23) — a related party is one of the larger receivable counterparties and its balance keeps growing even as overall ageing deteriorates. 🟡
- **Company-disclosed Trade Receivables Turnover Ratio** (Annexure — Significant Accounting Ratios, SFS p.44): FY23 1.69, FY24 1.59, FY25 1.68 — broadly flat per the company's own ratio, which does not fully capture the ageing-bucket deterioration seen above; the two data points (ratio vs. ageing mix) should be read together, not the ratio alone.

## 5. INVENTORY
(Annexure XVIII, CFS p.18 / SFS p.20)

Standalone, ₹ Cr:
| | FY23 | FY24 | FY25 |
|---|---|---|---|
| Raw Material | 12.84 | 11.20 | 7.35 |
| Work-in-Progress | 27.28 | 29.39 | 38.87 |
| Finished Goods | 10.21 | 5.21 | 16.21 |
| **Total** | **50.32** | **45.80** | **62.44** |

- **Finished goods growth vs revenue growth:** FG fell 49% FY23→FY24 (₹10.21→5.21 Cr) then surged 211% FY24→FY25 (₹5.21→16.21 Cr), while revenue grew 61.3% in FY25 (₹119.30→192.39 Cr). FG growth materially outpaced revenue growth in FY25 — possible unsold-stock buildup at year-end, or simply order-book timing (large WIP also grew). 🟡 Watch — worth a management question.
- Total inventory grew 36.3% FY25 vs 61.3% revenue growth — overall inventory efficiency improved even as the FG mix point above needs explanation.
- **No write-downs, no obsolete-inventory disclosure anywhere** — **NOT FOUND IN DOCUMENT**.
- Company-disclosed Inventory Turnover Ratio (SFS p.44): FY23 1.38, FY24 1.54, FY25 2.30 — company's own metric shows clear improvement, which is the more encouraging read. 🟢

## 6. INVESTMENTS
(Annexure XV/XVI, SFS p.19; Annexure XVII/XLV)

- **Subsidiary:** Sree Dakssnaa Aerospace and Defence India Pvt Ltd, incorporated 11-June-2024, **79.20% owned**, carrying value **₹0.0099 Cr (₹0.99 Lakh)** — 9,999 equity shares of ₹10 each, first appearing FY25 (nil FY23/FY24). Described in the prospectus body (not the notes) as "a recent Aerospace and Defence startup" — pre-revenue at consolidation (consolidated FY25 revenue = ₹192.39 Cr, identical to standalone FY25 revenue, implying the subsidiary contributed no revenue in the period). Minority interest carries a loss of ₹0.0027 Cr for the year. No impairment disclosed (too new to test). 🟢/informational.
- No JVs, no other quoted/unquoted non-current investments beyond the subsidiary stake, no unrealised gains/losses table — nothing else to extract.
- ICDs / loans given: covered under RPT (Section 2) and short-term loans & advances (Annexure XXI) — "Advances to related parties" ₹1.65 Cr FY25 (Annexure XXI, SFS p.21), consistent with the RPT table.

## 7. BORROWINGS
(Annexure VII/X/XXXII, CFS p.15–16,25–27 / SFS p.17–18,29–31)

Standalone, ₹ Cr:
| | FY23 | FY24 | FY25 |
|---|---|---|---|
| Long-term borrowings | 0.23 | 0.04 | 1.20 |
| Short-term borrowings | 60.00 | 63.77 | 58.78 |
| **Total debt** | **60.22** | **63.80** | **59.98** |

- Instrument-level detail (Annexure XXXII, terms of borrowings):
  - **Axis Bank Ltd**: working capital/cash credit, hypothecation of current assets + multiple immovable-property collateral + personal guarantees of 4 promoters/relatives (Venkatesan D, Manikandan D, Mrs. Nanthini, Mrs. Revathy) — 3-Month MCLR+2.50%, outstanding ₹31.98 Cr FY25.
  - **Union Bank of India**: EBLR+0.75%, secured by industrial property, outstanding ₹17.97 Cr FY25.
  - **Share India Fincap Pvt Ltd** (NBFC): unsecured-nature bullet loan **at 16.00% p.a.**, sanction ₹6.00 Cr, secured by 34.94 acres of land + personal guarantees of all 4 promoter/relatives + **corporate guarantees of Airflow Energy Solutions Pvt Ltd and Airflow Dafeng Rail Equipments Pvt Ltd** (both promoter-group entities) — outstanding ₹6.00 Cr FY25. 🟡 High-cost debt, cross-guaranteed by group companies.
  - **Rauhat Financial & Financial Consultancy Services Pvt Ltd**: unsecured inter-corporate loan **at 24.00% p.a.** — extremely high cost — guaranteed against 8 separate parcels of land pledged by directors and relatives. Outstanding ₹2.73 Cr (FY23), ₹2.75 Cr (FY24), **₹0 (FY25 — repaid)**. 🔴 Red Flag (historical) — a company borrowing at 24% p.a. against promoters' personal land is a strong liquidity-stress signal for FY23/FY24, even though it was repaid before the IPO.
  - **Aditya Birla Finance** (16.00% p.a.) and **RBL Bank** (16.50% p.a.) unsecured business loans, both repaid to nil by FY25.
  - Vehicle loans (Axis, Yes Bank, BMW India Financial) at 8.5%–10.99% p.a. — routine.
  - **Related-party borrowings**: "Loan from Related parties" — unsecured, and explicitly noted as **interest-free** ("*Loan from Directors are interest-free," Annexure X footnote, SFS p.18) — ₹0.50 Cr (FY23), ₹0.52 Cr (FY24), nil (FY25).
- **Debt-Equity ratio** (company-disclosed, SFS p.44): FY23 1.44, FY24 1.14, FY25 0.55 — clear deleveraging trend, driven by the FY25 equity raise (fresh shares + bonus) rather than debt paydown from operations. 🟢 trend, but context matters (equity-funded, not FCF-funded).
- **Debt Service Coverage Ratio** (company-disclosed, SFS p.44): **FY23 0.21x, FY24 0.42x, FY25 0.68x — below 1.0x in every single year disclosed.** 🔴 Red Flag — the company has not generated sufficient operating cash flow to cover its debt service (interest + principal) from operations in any of the three years shown, despite the improving trend. This corroborates the reliance on high-cost NBFC/ICD borrowing noted above.
- **Unregistered charges beyond statutory period** (Additional Regulatory Information, Annexure XLV item x, SFS p.43): Axis Bank Ltd sanction of ₹51.17 Cr — charge status "Not Modified," reason for delay "Inadvertently missed to file the same," to be registered with ROC Chennai; and BMW India Financial Services vehicle loan (₹1.43 Cr) — same "inadvertently missed" reason, to be registered by 02-03-2025. 🔴 Red Flag — statutory charge-registration non-compliance, again using the recurring "inadvertently missed" language seen elsewhere in the restatement notes (Section 1).
- **Stock statement / book-debt discrepancies vs. banks** (unnumbered Additional Regulatory Information table, SFS p.40–42 / CFS p.38): for **every quarter of FY23, FY24 and FY25**, and for **both** working-capital lenders (Axis Bank and Union Bank of India), the amount of stock/book debts reported to the bank for drawing-power purposes **differs materially from the amount per the company's own books** — differences ranging from a few lakh to **₹70.97 Cr (Q1 FY25, Axis Bank book debts: books ₹118.73 Cr vs. reported ₹47.76 Cr)** and **₹65.40 Cr (Q4 FY24, Axis Bank book debts)**. Reasons given are generic: "inadvertently netting-off advance from customer," "due to non-completion of bank entries," "no stock statement copy available with management." 🔴🔴 Major Red Flag — this is a recurring, multi-year, multi-bank, multi-quarter control failure in reporting to secured lenders, not a one-off. See Top 10.

## 8. TRADE PAYABLES
(Annexure XI/XXXIII/XLIV, CFS p.16,28 / SFS p.18,32,39)

Standalone, ₹ Cr:
| | FY23 | FY24 | FY25 |
|---|---|---|---|
| MSME payable | 0.35 | 0.35 | 0.35 |
| Other payable | 51.72 | 59.42 | 63.58 |
| **Total** | **52.07** | **59.77** | **63.93** |

- **MSME principal payable is frozen at exactly ₹0.35 Cr in all three years** — the ageing schedule (Annexure XXXIII) confirms this is the *same* disputed balance rolling forward: "Disputed Dues – MSME" shows ₹0.32 Cr in the 2–3yr bucket for FY23 and FY24, and ₹0.35 Cr in the >3yr bucket for FY25 — i.e., **the identical MSME dues have now aged past 3 years unpaid.** 🔴🔴 Red Flag.
- **Interest on late MSME payments** (Annexure XLIV, "Dues of Small and Micro Enterprises"): cumulative interest due and payable under Section 16 of the MSME Act — **₹0.15 Cr (FY23) → ₹0.26 Cr (FY24) → ₹0.39 Cr (FY25)**, i.e., **accrued interest now exceeds the ₹0.35 Cr principal it relates to**, and the note explicitly states "the Company does not have a system in place to determine the bifurcation of the creditors as Micro, Small or Medium Enterprises" and that MSME creditor status was "determined to the extent such parties have been identified on the basis of information available with the Company" — i.e., the disclosure itself is admittedly incomplete. 🔴🔴 — top-tier red flag, statutory violation compounding annually with an admitted disclosure gap.
- **Trade payables turnover ratio** (company-disclosed, SFS p.44): FY23 1.40, FY24 1.30, FY25 2.38 — company attributes the FY25 jump to "increase in average payable, and turnover... payable, ratio has improved."
- Payable ageing (non-MSME) shows a growing "more than 3 years" bucket: FY23 ₹2.94 Cr, FY24 ₹5.46 Cr, FY25 ₹8.19 Cr — aged trade payables (beyond MSME) are also rising in absolute terms, worth monitoring alongside the receivables ageing above.

## 9. PROVISIONS
(Annexure IX/XXXVI/XLVI, CFS p.16,31–32 / SFS p.18,35,45)

- **Gratuity (unfunded defined benefit plan)** — Present Value of Obligation: FY23 ₹1.50 Cr, FY24 ₹1.81 Cr, FY25 ₹1.88 Cr. Assumptions: discount rate declining 7.20% (FY23) → 7.15% (FY24) → 6.55% (FY25); salary escalation flat 5.00% all years; **attrition rate flat at 54.00% in all three years** — an unusually high assumed attrition rate for a manufacturing workforce, which mechanically reduces the discounted gratuity liability (shorter expected service tenures = lower PVO). 🟡 Watch — worth a management question on why 54% attrition is assumed and whether it is actuarially supportable or liability-minimising.
- No warranty provision, no decommissioning provision, no onerous-contract provision anywhere in the annexures — **NOT FOUND IN DOCUMENT**.
- No litigation provisions beyond the two GST matters already disclosed as contingent liabilities (Section 3) — no case provided for as a liability.
- **CSR (Annexure XLVI, "Details of Corporate Social Responsibility"):** Required FY23 ₹0.20 Cr, actual incurred FY23 nil (per table, N.A. shown for FY24 required amount is a drafting gap in the table itself); Balance CSR liability carried forward: **₹0.90 Cr at both FY23 and FY24 year-ends (unpaid, unchanged for two years)**, then a large **₹1.08 Cr payment made in FY25** ("Payment during the year" row) that clears the backlog to near-nil (₹(0.0004) Cr shortfall). Explanatory note: "During the previous financial years, the Company inadvertently missed booking the required Corporate Social Responsibility (CSR) expenditure. To rectify this and ensure compliance, the Company has taken corrective steps in FY 2024-25 by contributing funds to the Prime Minister's National Relief Fund." 🔴 Red Flag — multi-year CSR non-compliance, remediated via a lump catch-up payment timed with the IPO process, echoing the same "inadvertently missed" pattern seen in gratuity, MSME interest, statutory-dues interest, and charge registration (Sections 1, 7, 8). This is a recurring theme, not an isolated item — see Top 10.
- **Interest on late payment of statutory dues** (Finance Cost, Annexure XXVIII): ₹0.11 Cr (FY23) → ₹0.69 Cr (FY24) → **₹1.76 Cr (FY25)** — a 155% jump in FY25, consistent with catch-up interest accruing on historically unpaid statutory dues (TDS etc.) as flagged in the restatement notes. 🔴

## 10. DEFERRED TAX
(Annexure VIII, SFS p.18; Statement of Tax Shelters, Annexure XXXVIII, SFS p.37)

- **Deferred tax liability (net):** FY23 ₹0.20 Cr, FY24 ₹0.0079 Cr, FY25 ₹0.0072 Cr — arising from WDV differences (Companies Act vs. Income Tax Act) and expenses disallowed under the Income Tax Act; small and declining. 🟢
- **Effective vs. statutory tax rate:** statutory/notional rate applied: FY23 27.82%, FY24 29.12%, FY25 25.17% (post-115BAA election). Actual current tax provision vs. PBT: FY23 ₹1.31 Cr / ₹2.34 Cr PBT = **55.9% effective rate** (distorted upward by disallowed permanent differences — donation, CSR, late-payment interest — being large relative to a small PBT base); FY24 ₹6.56 Cr / ₹20.60 Cr = 31.8%; FY25 ₹9.42 Cr / ₹34.98 Cr = 26.9%. The FY23 55.9% effective rate is a notable data point reflecting how disallowed compliance-related costs (late fees, CSR shortfall, MSME interest) materially eroded reported earnings that year. 🟡
- **MAT credit / utilisation timeline:** MAT rate disclosed (17.47% FY24, 16.69% FY23, 0.00% FY25) but **no MAT credit entitlement asset or utilisation schedule disclosed** — **NOT FOUND IN DOCUMENT**.
- **Unrecognised DTA:** not discussed — **NOT FOUND IN DOCUMENT**.

## 11. REVENUE DETAILS
(Annexure XXII, CFS p.21 / SFS p.25; Annexure XLIII earnings in forex)

- Single revenue line only: "Revenue from Sale of Products" — FY23 ₹95.17 Cr, FY24 ₹119.30 Cr, FY25 ₹192.39 Cr (+61.3% YoY FY25, +25.4% YoY FY24).
- **No disaggregation by product, segment, or geography anywhere in the annexures.** Segment reporting accounting policy is stated (Note 2.19) but **no actual segment note or table is presented** — implies a single reportable segment, but this is inferred, not explicitly confirmed. **NOT FOUND IN DOCUMENT** (explicit single-segment statement).
- No contract asset/liability note, no unsatisfied performance obligations — expected under IGAAP (pre-Ind AS 115), not itself a red flag given the accounting framework.
- **No top-customer revenue concentration disclosed** — **NOT FOUND IN DOCUMENT**.
- **Export revenue:** Annexure XLIII (Earnings in Foreign Exchange) shows export of goods (FOB basis) of **₹0.078 Cr in FY23 only; nil in FY24 and FY25** — the company is almost entirely a domestic-revenue business despite the "Rail Technology" branding suggesting possible export ambition.
- **Import dependency rising:** raw material imported as % of total consumption (Annexure XLI): FY23 1.71%, FY24 1.52%, **FY25 5.51%** — import share more than tripled in FY25, increasing unhedged foreign-currency exposure (no hedging policy disclosed — see Section 12). 🟡

## 12. OTHER CRITICAL NOTES
(Various annexures, CFS/SFS throughout)

- **Exceptional / extraordinary items:** none. Both auditor's reports (CFS p.2, SFS p.2, item 7c) state "have no extra-ordinary items that need to be disclosed separately." 🟢
- **Goodwill:** none — subsidiary investment carried at cost (₹0.0099 Cr), no goodwill arises on consolidation given the tiny investment size relative to the subsidiary's own share capital.
- **Capital commitments:** ₹0.12 Cr (see Section 3), tied to a related-party machinery purchase.
- **Foreign currency exposure / hedging:** no hedging policy disclosed anywhere; small unrealised/realised forex loss of ₹0.037 Cr in Other Expenses (FY25) and correspondingly small forex gains/losses in Other Income in other years. Import dependency rising (Section 11) with **no hedging mechanism in place** — **NOT FOUND IN DOCUMENT** (no forward contracts, no hedge accounting note).
- **Segment reporting:** policy exists (Note 2.19) but no segment table presented (see Section 11).
- **Basic vs. diluted EPS:** identical in all periods (no dilutive instruments) — standalone FY25 basic/diluted EPS ₹15.64 (post-bonus), FY24 ₹9.50, FY23 ₹1.00. No ESOP scheme disclosed anywhere — **NOT FOUND IN DOCUMENT**.
- **Share capital changes (FY25, Annexure V):** (i) 4,99,318 fresh equity shares issued via private placement at ₹10 face + **₹290 premium** (₹300/share) on 01-Aug-2024; (ii) 44,000 fresh shares at the same ₹290 premium on 09-Aug-2024; (iii) **bonus issue of 2 shares for every 1 held**, 1,10,76,636 bonus shares, on 31-Aug-2024; (iv) 8,48,000 fresh shares via private placement at ₹10 face + **₹115 premium** (₹125/share) on 04-Dec-2024. The pre-bonus placement price (₹300/share, Aug) is materially higher than the post-bonus December placement (₹125/share), though the bonus issue (2:1) mechanically dilutes the earlier price to a bonus-adjusted ~₹100/share — so the December placement at ₹125 is not strictly a "down round" once bonus-adjusted, but the sequencing (raise high, bonus, raise lower, then IPO at ₹136–140 cap price per prospectus cover) is a pattern worth a management question on pricing rationale for pre-IPO placements. 🟡
- **Direct debits/credits to reserves bypassing P&L:** the restatement adjustments (gratuity, CSR, interest reversal, MSME interest, statutory-dues interest, rates & taxes, income tax, deferred tax — Section 1) were routed as "Opening Restatement adjustment" directly against opening retained earnings (Annexure VI, Reserves & Surplus) rather than through the current year's P&L. This is the standard IPO-restatement mechanic under the ICAI Guidance Note (not itself an ongoing earnings-management practice), but is flagged here for completeness per the Section 2 instruction to check reserve-bypass entries.
- **Events after balance sheet date:** no discrete "subsequent events" note found in the annexures — **NOT FOUND IN DOCUMENT** as a formal note (the conversion to public limited company, name changes, and IPO itself are covered elsewhere in the prospectus body, not in a dedicated financial-statement subsequent-events note).
- **Promoter personal guarantees:** aggregate loan amount guaranteed by directors and others: **₹37.98 Cr (FY25)**, ₹42.24 Cr (FY24), ₹38.53 Cr (FY23) (Annexure XXXII footer) — substantial personal-guarantee exposure carried by the promoter group across the secured lending relationships (Axis Bank, Share India Fincap, Rauhat Financial). Not a company contingent liability per se, but a material promoter-alignment/key-man-risk data point.
- **Going concern:** no going-concern qualification, emphasis-of-matter, or explicit management going-concern discussion found anywhere in either audit report or the annexures. Both auditor opinions are clean/unqualified on the restated statements. **NONE.**

---

# PASS 1 SUMMARY — TOP 10 MOST SIGNIFICANT FINDINGS

| Rank | Finding | Note anchor | Rating |
|---|---|---|---|
| 1 | Multi-year, multi-bank, multi-quarter discrepancies between books and stock/book-debt statements filed with lenders for working-capital drawing power (differences up to ₹70.97 Cr in a single quarter), across FY23–FY25, with only generic explanations offered | Additional Regulatory Info table, SFS p.40–42 / CFS p.38 | 🔴 |
| 2 | MSME dues: same ₹0.35 Cr principal unpaid for 3+ years, accrued interest (₹0.39 Cr) now exceeds the principal, and the company admits its MSME-creditor identification process is incomplete | Annexure XI/XXXIII/XLIV, SFS p.18,32,39 | 🔴 |
| 3 | Debt Service Coverage Ratio below 1.0x in all three disclosed years (0.21x FY23, 0.42x FY24, 0.68x FY25) — operating cash flow has not covered debt service in any year shown | Significant Accounting Ratios, SFS p.44 | 🔴 |
| 4 | Extensive prior-period restatement: gratuity, CSR, interest on borrowings, statutory-dues interest, MSME interest, and income/deferred tax were all "inadvertently" mis-booked in prior years and are now retrospectively corrected across FY23–FY25 | Annexure IV Notes 3 & 4, SFS p.13–14 / CFS p.12–13 | 🔴 |
| 5 | Section 185 Companies Act violation (loans to related parties) in FY23 and FY24, remediated only by repayment before the audit date, not contemporaneous compliance | Auditor's Report item 8(iv), CFS p.2 / SFS p.3 | 🔴 |
| 6 | Historical reliance on very high-cost debt (24% p.a. ICL from Rauhat Financial secured by promoters' personal land; 16–16.5% p.a. from Share India Fincap, Aditya Birla Finance, RBL Bank), all repaid to nil by FY25 but indicating liquidity stress in FY23/FY24 | Annexure XXXII, SFS p.29–31 | 🔴 |
| 7 | CSR non-compliance for multiple years (₹0.90 Cr shortfall carried unpaid FY23–FY24) cleared via a lump ₹1.08 Cr catch-up payment in FY25, timed with the IPO process | Annexure XLVI, SFS p.45 | 🔴 |
| 8 | Trade receivables aged >6 months rising steadily as a share of total (15.95% FY23 → 17.85% FY24 → 23.38% FY25) with zero doubtful-debt provisioning in any of the three years | Annexure XIX/XXXIV, SFS p.20,33 | 🟡 → feeds FLAG-CASH |
| 9 | Unregistered charges with ROC beyond the statutory period on ₹51.17 Cr (Axis Bank) and ₹1.43 Cr (BMW India Financial) borrowings, both attributed to "inadvertently missed to file" | Annexure XLV item x, SFS p.43 | 🔴 |
| 10 | Document-level: the {{ANNUAL_REPORT}} input is actually the IPO Prospectus; consolidated financials cover FY25 only (one year) and standalone covers FY23–FY25 (three years) — no separate Annual Report or DRHP exists in the file set, materially limiting historical trend depth versus a normal listed-company notes review | Document identification flag (this report) | 🟡 |

**Additional watch items not in Top 10 but noted for Pass 2/3 follow-up:** 54% flat actuarial attrition assumption on gratuity (Annexure XXXVI); finished-goods inventory growth (211% FY25) outpacing revenue growth (61.3%); rising import dependency (1.71%→5.51% of raw material) with no disclosed hedging policy; related-party receivable (Raghavendra Industries) growing to ₹7.46 Cr; pre-IPO share placement pricing sequence (₹300/share Aug placement → 2:1 bonus → ₹125/share Dec placement).
