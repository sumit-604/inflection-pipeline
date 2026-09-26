# STAGE 2 PASS 1: NOTES TO FINANCIAL STATEMENTS, FULL EXTRACTION
Company: Fabtech Technologies Ltd (FABTECH). Run: fabtech-2026-09-26.
Basis: CONSOLIDATED (primary), standalone noted where materially different.
Units: as stated on the face of each source. AR is INR lakh (OCR text, cite as "AR p.N (txt)"); FY26 audited results filing is INR lakh (text layer, cite as "Results p.N").
Source: runs/fabtech-2026-09-26/inputs/annual-report/Annual_Report_2026.txt (standalone notes 1-56, txt p.101-138; consolidated notes 1-62, txt p.155-200); cross-checked against inputs/results/20260427-Results_FY26_audited.txt.

---

## 0. KNOWN ITEM SETTLED: consolidated trade receivables face-vs-note discrepancy (LBF2)

The KNOWN ITEM is a **drafting/printing error on the AR consolidated balance sheet face**, not an OCR misread and not a reclassification.

Evidence:
- AR consolidated balance sheet face (AR p.150, txt line 7088): "Trade receivables 13 24,151.90 15,073.61" (FY26 / FY25).
- AR consolidated Note 13 total (AR p.173 (txt), txt line 8291): "Total 20,433.51 15,073.61".
- AR consolidated MD&A (AR p.44 (txt), txt line 1538): "Trade receivables increased from Rs. 15,265.94 lakhs in FY2024-25 to Rs. 20,433.51 lakhs in FY2025-26".
- AR consolidated financial-instruments note (AR p.192 (txt), txt line 9329): trade receivables carrying value 20,433.51.
- FY26 audited results filing (Results p. line 316, text layer, exchange-filed, authoritative): "(i) Trade receivables 20,433.51 15,073.61" and "Total assets 65,370.29 42,655.80" (line 325).
- AR consolidated balance sheet face Total Assets = 69,088.68 (txt line 7097). 69,088.68 minus 65,370.29 = 3,718.39, which equals 24,151.90 minus 20,433.51 exactly.
- Internal arithmetic check: summing every other AR face current-asset line (inventories, investments, cash, bank balances, loans, other financial assets, current tax assets, other current assets = 31,208.37) and subtracting from the AR's own stated Total Current Assets (55,360.26) yields 24,151.89 — i.e. the AR face's own total ties to 24,151.90, not to 20,433.51. This rules out a simple single-cell OCR misread: the wrong number was carried consistently through the face's own subtotals and grand total.

Conclusion: 🔴 The FY26 AR **consolidated balance sheet face** (trade receivables 24,151.90 lakh, Total Assets 69,088.68 lakh) is the outlier and is wrong. Every other source in the same filing set (Note 13, the MD&A, the financial-instruments note, and the exchange-filed audited results) agrees on trade receivables Rs 20,433.51 lakh and Total Assets Rs 65,370.29 lakh for FY26 consolidated. **Anchor all downstream cash-conversion and balance-sheet work to Rs 20,433.51 lakh / Rs 65,370.29 lakh.** This is itself a disclosure-quality red flag: a signed, audited annual report contains an internally-consistent-but-wrong balance sheet face that was not caught before filing (Reg 34 filed 31-Jul-2026, three months after the audited results were filed 27-Apr-2026 with the correct number). Flag for stage 3/8: what does this say about the company's financial-close controls at listing-year scale-up.

---

## 1. ACCOUNTING POLICIES & CHANGES

- 🟢 No policy changes with quantified P&L impact disclosed. MCA amendments to Ind AS 1/12/21/107/7 effective 1-Apr-2025 assessed as "no significant impact" (standalone Note 4, AR p.114 txt; consolidated Note 4, AR p.168 txt).
- 🟡 Depreciation useful lives: standard Schedule II lives used for most classes, except Leasehold Improvement depreciated over 9 years (lease term) vs Schedule II's 10 years (standalone Note 3(H), AR p.105-106 txt). Minor, disclosed, not a red flag on its own.
- 🟢 Capitalisation threshold: assets costing ≤ INR 5,000 fully depreciated in year of acquisition (standalone Note 3(F), AR p.107 txt).
- 🟡 Revenue recognition: turnkey contracts are a "single performance obligation… recognised based on actual shipments as of the reporting date" (standalone Note 3(D), AR p.104-105 txt). This is a shipment/milestone basis, not percentage-of-completion on cost incurred — worth checking against LBF1 order-book delivery math; revenue recognition timing on long-cycle turnkey projects is a judgment area investors should watch (no red flag evidenced yet, but the basis itself creates lumpiness risk).
- 🟢 Ind AS 116 (leases): ROU assets and lease liabilities both disclosed with movement schedules (standalone Note 49; consolidated Note 51). FY26 consolidated: ROU asset closing Rs 2,597.70 lakh (FY25: 3,015.43); lease liability closing Rs 2,690.20 lakh (FY25: 2,920.43). Discount/incremental borrowing rate not separately stated as a single number in the lease note (uses "interest rate implicit in the lease" or IBR per policy, actual rate not disclosed as a %).
- 🟡 ECL matrix: NOT static — expected loss rates rose sharply YoY across every ageing bucket (consolidated): 1-2yr bucket 10.10% (FY26) vs 3.39% (FY25); 2-3yr bucket 10.10% (FY26) vs 3.81% (FY25); blended rate 3.37% (FY26) vs 1.26% (FY25) (consolidated Note 13(b), AR p.174 txt). This is a genuine deterioration in the credit-quality of the receivables book, not just growth in the base. See section 4.
- 🟢 Critical estimates and judgements named: defined benefit obligation (Note 43/45), impairment of trade receivables (Note 13) — standard, no unusual items flagged.
- No first-time standard adoptions beyond the routine MCA package noted above.

## 2. RELATED PARTY TRANSACTIONS (consolidated Note 49, AR p.192-195 txt; standalone Note 47, AR p.133-135 txt)

Full related-party universe named: promoters/directors (Aasif Khan, Aarif Khan, Hemant Anavkar, Manisha Anavkar — combined 68.94% holding, unchanged YoY per shareholding table), KMP (CEO Ashwani Singh, CS Neetu Buchasia/Tibrewal, CFO Kalpesh Chauhan), associates (Mark Maker Engineering Pvt Ltd, FABL International Technologies LLP), and 15 promoter-group entities/LLPs including **Fabtech Technologies Cleanrooms Limited**, **Fabtech Turnkey Projects LLP**, **Fabtech Technologies International Private Limited (FTIPL)**, **F Plus Healthcare Technologies Pvt Ltd**, **FTS Cleanrooms Systems LLC (UAE, step-down subsidiary)**, **Fabtech Technologies KSA / Fabtech Lifecare Company (Saudi, step-down subsidiary)**, Fabsafe Technologies, Altair Partition Systems LLP, Advantek Air Systems, G7 Universal LLC, SA Universal LLC, Pacifab Technologies LLP, Fillpac Solutions, FVE Lifecare General Trading LLC, Alanar One Health Equity Fund.

Key consolidated RPT lines, FY26 vs FY25 (Rs lakh):
| Nature | Party | FY26 | FY25 | YoY |
|---|---|---|---|---|
| Purchases | Fabtech Technologies Cleanrooms Ltd | 2,358.58 | 2,985.00 | -21% |
| Purchases | Fabsafe Technologies Pvt Ltd | 381.81 | 366.27 | +4% |
| Purchases | F Plus Healthcare Technologies | 434.62 | 98.17 | +343% |
| Purchases | FVE Lifecare General Trading LLC | 468.76 | 598.33 | -22% |
| Sales | Fabtech Technologies International Pvt Ltd (FTIPL) | 1,261.56 | 697.06 | +81% |
| Sales | FVE Lifecare General Trading LLC | 626.29 | 6.15 | +10082% |
| Sales | Fabtech Technologies KSA | 43.73 | 12.12 | +261% |
| Sales commission | G7 Universal LLC | 359.84 | — | new |
| Corporate guarantee expense | FTIPL + Fabtech Turnkey Projects LLP | 21.38 each | — | new |
| Rent paid | Fabtech Turnkey Projects LLP | 9.05 | 97.30 | -91% |

Note: standalone-only line "Sales — FTS Cleanrooms Systems LLC 4,367.49 (FY26) / 6,373.20 (FY25)" (standalone Note 47, AR p.133 txt) does **not appear** in the consolidated RPT table for FY26 (FTS Cleanrooms LLC is consolidated as a step-down subsidiary, so its transactions with the parent are eliminated on consolidation — expected and correct, not a red flag, but confirms FTS Cleanrooms LLC is the single largest intra-group trading relationship in the standalone books, at ~16% of standalone FY26 revenue).

🟡 Non-arm's-length signal to test: standalone-to-FTS-Cleanrooms sales fell 31% YoY (6,373.20 → 4,367.49) even as FTS Cleanrooms LLC itself contributed Rs 16,048.75 lakh revenue and Rs 700.15 lakh profit to the group (Note 52(a), AR p.198 txt) — down from Rs 1,161.83 lakh profit in FY25 despite higher revenue (13,888.46 → 16,048.75). Margin compression at the UAE subsidiary is worth a question for management (Q5 below).

🟡 Corporate guarantees given by the Holding Company for promoter-group entities: Rs 1,000.00 lakh for Fabtech Technologies Cleanrooms Ltd and Rs 600.00 lakh for Fabsafe Technologies Pvt Ltd, both unchanged FY25→FY26 (Note 43/41, both standalone and consolidated). These are off-balance-sheet exposures to related, non-consolidated entities.

🟢 Loans to related parties: FT Institutions Pvt Ltd, FABL International Technologies LLP, Fabtech Technologies LLC UAE, Mark Maker Engineering — all disclosed at cost/interest income, no impairment beyond the standard doubtful-loan allowance (standalone Rs 12.02 lakh, consolidated Rs 12.02 lakh, both flat/small).

🟢 The AGM notice (AR p.202-203 txt) discloses a **prospective material RPT approval sought** with FTS Cleanrooms Systems LLC for FY27: sales up to Rs 6,000 lakh + purchase/installation/reimbursement up to Rs 2,800 lakh = Rs 8,800 lakh aggregate ceiling, "notwithstanding... expected to exceed the prescribed thresholds." This is a forward-looking related-party ceiling, not an FY26 transaction, but material for FY27 modelling (~2x the FY26 standalone-to-FTS-Cleanrooms sales run rate).

Directors state transactions are "at arm's length and in the ordinary courses of business" (standard boilerplate, both standalone and consolidated notes) — no independent verification possible from the notes alone.

## 3. CONTINGENT LIABILITIES (standalone Note 41, AR p.125 txt; consolidated Note 43, AR p.183-184 txt — identical figures standalone and consolidated)

| Item | FY26 (Rs lakh) | FY25 (Rs lakh) |
|---|---|---|
| Claims not acknowledged as debt (Clean Coats Pvt Ltd MSME dispute) | 85.53 | 85.53 |
| Corporate guarantee — Fabtech Technologies Cleanrooms Ltd (Axis Bank WC) | 1,000.00 | 1,000.00 |
| Corporate guarantee — Fabsafe Technologies Pvt Ltd (Axis Bank WC) | 600.00 | 600.00 |
| Performance guarantees for turnkey project contracts | 2,829.57 | 1,570.67 |
| **Total** | **4,515.10** | **3,256.20** |

Total equity FY26 (consolidated) Rs 41,976.93 lakh → contingent liabilities ~10.8% of net worth. No single item exceeds 10% of net worth individually. 🟡 Performance guarantees nearly doubled YoY (+80%), consistent with a growing order book (LBF1) — expected direction, but the pace should be checked against actual order inflow.

The Clean Coats MSME dispute (Rs 85.53 lakh deposited with the Bombay High Court, later withdrawn by the vendor, now under Supreme Court-directed arbitration via FTIPL, the demerged entity) is unresolved since 2017 — a long-running, small, non-material litigation. 🟢 Not a red flag at this size.

No tax disputes disclosed as contingent liabilities in either standalone or consolidated notes — 🟢 clean on tax litigation, or NOT FOUND IN DOCUMENT if any exists outside Note 41/43.

## 4. TRADE RECEIVABLES (standalone Note 13, AR p.117-118 txt; consolidated Note 13, AR p.173-174 txt)

Consolidated (correct figures per Section 0 above):
- Considered good (gross, incl. retention money): Rs 21,145.59 lakh (FY26) vs Rs 15,265.94 lakh (FY25), +38.5% YoY, against revenue growth of +25.7% (41,077.18 vs 32,666.85) — receivables growing faster than revenue. 🟡
- Allowance for doubtful debts: Rs 712.08 lakh (FY26) vs Rs 192.33 lakh (FY25), +270%.
- Net trade receivables: Rs 20,433.51 lakh (FY26) vs Rs 15,073.61 lakh (FY25).
- Receivable from related parties: Rs 2,393.55 lakh (FY26) vs Rs 2,037.38 lakh (FY25) (11.3% of gross receivables, FY26).

Ageing (consolidated, gross, FY26): <6mo Rs 11,922.69 lakh (56.4%); 6mo-1yr Rs 3,335.36 lakh (15.8%); 1-2yr Rs 4,250.00 lakh (20.1%); 2-3yr Rs 246.53 lakh (1.2%); >3yr Rs 1,391.01 lakh (6.6%). **>6 months as % of total = 43.6%** (FY25 comparable: >6mo = 35.3%) — ageing is worsening, not improving. 🔴

ECL loss rates by bucket, consolidated:
| Bucket | FY26 rate | FY25 rate |
|---|---|---|
| <6mo | 0.20% | 0.20% |
| 6mo-1yr | 2.79% | 2.50% |
| 1-2yr | 10.10% | 3.39% |
| 2-3yr | 10.10% | 3.81% |
| >3yr | 10.16% | 3.54% |
| Blended | 3.37% | 1.26% |

🔴 The loss-rate jump in the 1-3yr buckets (roughly 3x) is a genuine credit-quality signal, not a mechanical consequence of receivables growth. Combined with debtor days of 182 (screener, per B00 LBF2) and consolidated CFO of ~Rs 0 on PAT Rs 38 Cr, this is evidence toward **GROWTH-INDUCED-AND-STRUCTURAL** cash conversion strain, not purely growth-induced — the provisioning increase shows management itself sees rising non-recovery risk on ageing balances, which a pure "growth dilutes the ratio" story would not produce.

No customer >10% of gross trade receivables is separately disclosed by name in the receivables note (customer concentration is disclosed for revenue, not receivables — see Section 11). Receivables by geography (Note 44(b)): Saudi Arabia Rs 6,336.63 lakh (30%, up from Rs 2,587.75 lakh, +145%) and UAE Rs 3,954.13 lakh (19%, up from Rs 2,457.69 lakh, +61%) — the two largest export markets show the fastest receivables growth. 🟡

Auditor's Key Audit Matter (consolidated auditor's report, AR p.139-140 txt) is precisely this item: "old outstanding trade receivables before ECL provisions of Rs 5,887.55 Lakhs (more than 365 days overdue)" — the auditor flagged recoverability of overdue receivables as a key audit matter. 🔴 This is an external, independent confirmation (not just management's own numbers) that receivable ageing is a live audit risk area.

## 5. INVENTORY (standalone Note 11, AR p.116 txt; consolidated Note 11, AR p.172 txt)

Standalone: Stock in Trade Rs 447.08 lakh + Goods in Transit Rs 1,462.20 lakh = Rs 1,909.28 lakh (FY26) vs Rs 1,599.17 lakh (FY25). No write-downs disclosed either year ("There is no amount written down from the inventory during the year").

Consolidated: Raw material Rs 1,109.40 lakh (new line, FY26 only) + Stock in Trade Rs 671.94 lakh + Goods in Transit Rs 1,462.20 lakh = Rs 2,134.14 lakh (FY26) vs Rs 5,941.58 lakh (FY25, which included Rs 3,736.85 lakh Stock in Trade + Rs 1,019.20 lakh Goods in Transit + an implicit WIP of Rs 76.13 lakh per the Changes-in-inventory note). Consolidated inventory **fell** 64% YoY despite revenue growth of 26% — driven by the FABL International Technologies LLP deconsolidation (51% stake sold 1-Apr-2025, reclassified from subsidiary to associate), which removed FABL's inventory from the consolidated balance sheet. 🟢 Explained by the deconsolidation, not organic — but flag for stage 3 that the consolidated inventory turnover ratio (Note 50: 6.01x FY26 vs 4.10x FY25, "+46.48%... due to sale of stake in one subsidiary") is itself distorted by this deconsolidation and should not be read as an operating efficiency gain.

No obsolete-inventory disclosure in either standalone or consolidated notes — NOT FOUND IN DOCUMENT (may be immaterial for a turnkey-project business with pass-through equipment).

## 6. INVESTMENTS (standalone Note 7, AR p.116-117 txt; consolidated Note 7 + Note 52-54, AR p.170, 198-199 txt)

Subsidiaries and associates, consolidated (Note 52, AR p.198 txt):
| Entity | Country | Ownership FY26 | Ownership FY25 |
|---|---|---|---|
| FT Institutions Pvt Ltd | India | 99.99% | 99.99% |
| Fabtech Technologies LLC | UAE | 100.00% | 100.00% |
| FTS Cleanrooms Systems LLC (step-down) | UAE | 100.00% | 100.00% |
| Fabtech Lifecare Company (step-down, new 26-Aug-2025) | Saudi Arabia | 100.00% | — |
| FABL International Technologies LLP (subsidiary→associate 1-Apr-2025) | India | — (49% associate) | 99.99% (subsidiary) |
| Mark Maker Engineering Pvt Ltd (associate) | India | 33.33% | 33.33% |

🔴 **LBF3 Saudi entity naming discrepancy**: B00/companies/FABTECH.md names the Saudi 51% structure as "Specialized Contracting Activities LLC." The AR's actual disclosed Saudi step-down subsidiary is **"Fabtech Lifecare Company, KSA"**, incorporated 26-Aug-2025, **100% owned** by Fabtech Technologies LLC (UAE) — not 51%, and a different name. FY26 contribution: Revenue Rs 1,370.91 lakh, **Loss** Rs 455.52 lakh (Note 52(a)). This needs reconciliation at stage 3/8: either the Spear-line fact is wrong, or a separate 51% Saudi entity exists that is not in these AR notes (e.g., a JV/associate not required to be listed under Note 52/54, or an entity incorporated after the FY26 AR date — the B00 corpus_manifest lists "acquisition filings (02-Jun-2026, 25-Jun-2026)" which post-date the 31-Mar-2026 balance sheet date and would not appear in these notes). Flag for verification: is "Specialized Contracting Activities LLC" a post-year-end acquisition?

Goodwill (consolidated, Note 52(a), AR p.198 txt): Rs 3,699.81 lakh (1-Apr-2025 opening: FT Institutions Rs 2.00 lakh + FTS Cleanrooms LLC Rs 2,089.39 lakh + FABL Rs 1,608.42 lakh) → **Rs 2,296.83/2,294.83 lakh closing** (FT Institutions Rs 2.00 lakh + FTS Cleanrooms LLC Rs 2,089.39 lakh + exchange fluctuation reserve Rs 205.45 lakh, with FABL's Rs 1,608.42 lakh goodwill removed on deconsolidation). Matches B00 LBF3 figure. 🟢 Explained movement, no impairment charge — the goodwill decline is a deconsolidation effect, not an impairment.

Sale of 51% of FABL International Technologies LLP (1-Apr-2025, day 1 of FY26) generated an exceptional gain of Rs 177.49 lakh (consolidated Note 40) / Rs 90.52 lakh (standalone Note 38, "Profit on stake sale of Associate LLP") — the two figures differ because standalone and consolidated compute the gain on different bases (standalone at entity level pre-consolidation elimination). 🟡 Both are small relative to FY26 PBT (Rs 4,827.41 lakh consolidated / Rs 3,243.46 lakh standalone) but both years show an exceptional gain from a stake sale (FY25: Rs 1,784.86 lakh consolidated / Rs 2,197.80 lakh standalone, from the TSA Process Equipment stake sale to Thermax). **Two consecutive years of exceptional gains from disposing of stakes in group entities** is a pattern (see Section 12, LBF4 earnings quality).

TSA Process Equipment Pvt Ltd: residual 33.33%-of-51%-tranche stake (2,23,440 equity shares) held as "Non-current Assets classified as held for sale," Rs 563.35 lakh consolidated / Rs 166.60 lakh standalone, unchanged FY25→FY26 (i.e., not yet sold/settled two years after the Feb-2024 SPA with Thermax). 🟡 Stuck in held-for-sale status for over two years — worth a management question.

## 7. BORROWINGS (standalone Note 22/25, AR p.121-122 txt; consolidated Note 23/26, AR p.177-178 txt)

Consolidated total borrowings: Rs 4,273.26 lakh (FY26) vs Rs 5,462.08 lakh (FY25) — down 22% despite revenue growth, consistent with the Rs 20,752 lakh IPO net proceeds funding working capital instead of bank debt.

🟡 **Unexplained line, consolidated only**: Note 26 (Borrowings — Current) shows "Loan from related party (Unsecured): Loan from Others 2,350.83 (FY26) / 1,987.99 (FY25)" under a sub-heading literally labelled "Loan from related party" but the line itself says "Loan from Others." This label is either a drafting error or genuinely represents an unsecured related-party loan of Rs 2,350.83 lakh embedded in current borrowings that is NOT itemised by counterparty name anywhere in Note 49 (the related-party note's "Balances as on year end" table shows no related-party loan payable of this size). This is a disclosure gap: a Rs 2,350.83 lakh unsecured current borrowing labelled "related party" cannot be traced to a named counterparty in the RPT note. Flag for stage 3/8 verification.

Security package (both standalone and consolidated, Facility I): common collateral across Fabtech Technologies Ltd, Fabtech Technologies Cleanrooms Ltd, and Fabsafe Technologies Pvt Ltd — cross-company charge on Umbergaon (Gujarat) and Mumbai properties held in the name of Fabtech Turnkey Projects LLP, plus personal guarantees of Aasif Khan, Hemant Anavkar, Aarif Khan, plus corporate guarantees of FTIPL and Fabtech Turnkey Projects LLP. 🟡 This is a **cross-collateralised group structure**: the listed entity's working-capital facility is secured partly by assets/guarantees of non-consolidated promoter-group entities (Cleanrooms Ltd, Fabsafe, FTIPL, Fabtech Turnkey Projects LLP), and vice versa (the listed entity gives corporate guarantees back to Cleanrooms Ltd and Fabsafe). This is disclosed, not hidden, but it means the listed entity's balance sheet is financially entangled with non-consolidated group entities.

No covenant breaches or waivers disclosed. Facility III (secured against mutual fund lien) was closed during FY26. Fixed vs floating: term loans at 8.00%-10.95%; cash credit/packing credit rates not separately disclosed as a %.

5-year repayment schedule: only maturity buckets to "Above 5 years" given in the financial-risk-management liquidity note (Note 46 standalone / Note 48 consolidated), not a full 5-year amortisation table — NOT FOUND IN DOCUMENT as a distinct 5-year schedule.

## 8. TRADE PAYABLES (standalone Note 26, AR p.123 txt; consolidated Note 27, AR p.178-179 txt)

Consolidated: Rs 10,537.44 lakh (FY26) vs Rs 9,880.29 lakh (FY25), +6.7%, i.e. payables grew far slower than revenue (+26%) or receivables (+38.5%) — a working-capital mismatch (customers taking longer to pay, suppliers not being stretched further to compensate). 🟡

MSME dues >45 days: 🔴 Interest accrued and remaining unpaid to MSME suppliers: **Rs 53.59 lakh (FY26) vs Rs 21.52 lakh (FY25), +149%** (identical figure standalone and consolidated — the MSME exposure is a standalone-entity matter). "The amount of further interest due and payable even in the succeeding year… Rs 53.59 lakh" — i.e., this interest has not been paid and is expected to roll forward again. This is a genuine, worsening MSME payment-delay pattern, not disclosure noise: principal unpaid to MSME suppliers beyond the appointed day was Rs 1,700.85 lakh (standalone) / Rs 1,870.84 lakh (consolidated) at FY26 year-end, both up YoY.

Payable days trend: not separately given as "days" but payables turnover ratio (Note 48/50): standalone 2.19x FY26 vs 1.97x FY25 (+11%); consolidated 2.12x FY26 vs 2.59x FY25 (-18%, "Not Applicable" reason given despite exceeding the 25% variance-disclosure threshold on the standalone side but not flagged as a >25% variance on the consolidated side — the consolidated payables turnover fell 18%, under the 25% disclosure trigger, so no explanation is required or given).

## 9. PROVISIONS (standalone Note 24/43; consolidated Note 25/45)

Warranty: no separate warranty provision — back-to-back vendor warranty arrangement, "no separate provision for warranty costs has been established" (both standalone Note 51/58 and consolidated). 🟢 Standard for a turnkey equipment reseller/integrator model; means the company does not bear inventory/product warranty risk directly.

Employee benefits (gratuity): consolidated funded status — present value of obligation Rs 247.59 lakh (FY26) vs Rs 215.91 lakh (FY25); plan assets Rs 201.22 lakh vs Rs 147.02 lakh; net liability Rs 105.20 lakh (FY26, including a consolidation adjustment of Rs 58.83 lakh) vs Rs 68.89 lakh (FY25). Partially funded, LIC-managed. Actuarial assumptions: discount rate 7.27% (FY26) vs 6.78% (FY25); salary escalation 6.00% both years. 🟢 Standard, no unusual assumptions.

No decommissioning provisions, no onerous-contract provisions, no litigation provisions beyond the contingent-liability disclosures in Section 3 (the Clean Coats MSME matter is disclosed as a contingent liability, not booked as a provision, since management assesses the outcome as favourable).

## 10. DEFERRED TAX (standalone Note 10; consolidated Note 10)

Effective tax rate reconciliation:
| | FY26 | FY25 |
|---|---|---|
| Standalone statutory rate | 25.17% | 25.17% |
| Standalone effective rate | 27.56% | 26.39% |
| Consolidated statutory-equivalent shown | 19.63% | 21.71% |
| Consolidated effective rate | 20.54% | 23.13% |

🟡 The standalone effective rate (27.56%) runs **above** the domestic statutory rate, while the consolidated effective rate (20.54%) runs **below** both the standalone rate and the domestic statutory rate — the gap is explained by the UAE/Saudi subsidiaries' lower/nil tax jurisdictions pulling the blended consolidated rate down. This is a normal multinational-mix effect, not aggressive tax planning per se, but it means standalone PAT margin is not representative of the group's true tax burden and downstream models should use the consolidated effective rate.

No MAT credit disclosed. DTA composition dominated by lease-liability timing differences (Rs 673.61-677.07 lakh) and impairment-of-financial-assets timing differences (Rs 179.08-182.27 lakh, up from Rs 46.86-54.82 lakh — tracks the ECL provisioning increase in Section 4). No unrecognised DTA disclosed. 🟢 DTA realism appears standard; no valuation-allowance concerns flagged.

## 11. REVENUE DETAILS (standalone Note 30; consolidated Note 31 + Note 44)

Consolidated revenue disaggregation: Sale of products Rs 37,227.82 lakh + Installation/commissioning services Rs 3,672.15 lakh + Export incentives Rs 177.21 lakh = Rs 41,077.18 lakh (FY26) vs Rs 32,666.85 lakh (FY25), +25.7%. Single segment disclosed: "Trading of pharmaceutical and surgical products" — CODM reviews revenue only; "In view of the interwoven/intermix nature of business, Other segmental information is not ascertainable" (Note 44). 🟡 This means no segment-level profitability is disclosed even though the group spans India/UAE/Saudi and multiple entity types — an investor cannot see which geography or entity drives margin.

Customer concentration (consolidated, Note 44(c), customers ≥10% of revenue in either year):
| Customer | FY26 revenue | FY26 % | FY25 revenue | FY25 % |
|---|---|---|---|---|
| Al-Afiya | 5,155.04 | 12.55% | 515.46 | 1.58% |
| Himalaya | 3,321.13 | 8.09% | 4,566.83 | 13.98% |
| Qomel Company Arabia | 1,419.49 | 3.46% | 4,411.69 | 13.51% |
| Massoun Darou | 1,388.67 | 3.38% | 3,682.61 | 11.27% |

🔴 Customer churn is severe: three of FY25's top-4 customers (Himalaya, Qomel, Massoun Darou) each fell from >10% of revenue to single digits in FY26, while a new customer (Al-Afiya) appeared from near-zero to 12.55%. Combined, these four named customers went from 40.34% of FY25 revenue to 27.48% of FY26 revenue. This is a **lumpy, project-driven customer base with no visible repeat-customer durability** in the disclosed data — directly relevant to the "order-book business" archetype's book-to-bill and stickiness questions, and to the R2/R3 quality-ladder pricing-power test (a business with pricing power/stickiness would show the same large customers recurring, not rotating).

No contract-asset/contract-liability (unbilled revenue) balance is separately disclosed as a line item in either standalone or consolidated notes — advances from customers (a contract liability, Rs 4,651.62 lakh consolidated FY26 vs Rs 6,108.06 lakh FY25) are shown, but no "unbilled revenue" or "contract assets" line appears anywhere in the notes (ageing tables show blank "Unbilled dues" rows in both years). NOT FOUND IN DOCUMENT — relevant to LBF2: the company's revenue-recognition-on-shipment policy plus zero disclosed contract assets is consistent with receivables (not contract assets) being the primary WC-heavy line, which matches the LBF2 hypothesis but rules out "contract assets" as a hidden second WC drag.

## 12. OTHER CRITICAL NOTES

**Exceptional items, two-year pattern** (🔴 flag, ties to LBF4): FY26 consolidated Rs 177.49 lakh gain (FABL stake sale) on PBT of Rs 4,827.41 lakh (3.7% of PBT); FY25 consolidated Rs 1,784.86 lakh gain (TSA/Thermax stake sale) on PBT of Rs 6,043.36 lakh (29.5% of PBT — nearly a third of FY25's pre-tax profit came from a one-time stake disposal gain). Two consecutive years of gains from disposing of stakes in group/associate entities is a recurring "exceptional" pattern, which is definitionally inconsistent with "exceptional" — worth naming as a quality-of-earnings concern for stage 3/8, though the FY26 amount is now much smaller (3.7% vs 29.5% of PBT).

**IPO proceeds utilisation** (both standalone Note 53 and consolidated Note 60, identical figures): of Rs 23,029.65 lakh total (fresh issue Rs 20,752.02 lakh net + estimated issue expenses), only Rs 5,107.70 lakh utilised by FY26 year-end (22%), leaving **Rs 17,921.95 lakh (78%) unutilised**, parked as fixed deposits per Note 48/50's current-ratio commentary. Breakdown: Working capital Rs 2,747.24 lakh utilised of Rs 12,700.00 lakh budgeted (22%); **Inorganic growth/acquisitions: Rs 0 utilised of Rs 3,000.00 lakh budgeted (0%)**; General corporate purposes Rs 125.00 lakh utilised of Rs 5,052.02 lakh budgeted (2.5%); Issue expenses Rs 2,235.46 lakh of Rs 2,277.63 lakh (98%, essentially complete). 🟡 Zero inorganic-growth utilisation by 31-Mar-2026 is notable given B00 records acquisition-related filings dated 02-Jun-2026 and 25-Jun-2026 (post-year-end) — implying the acquisition activity only began after FY26 closed, roughly 8 months after listing. Ties to LBF4 (IPO proceeds deployment vs RHP objects) — the monitoring agency reports and deviation statements referenced in B00 should be read alongside this note.

**Other income composition** (standalone Note 31; consolidated Note 32), ties to LBF4: consolidated Other Income Rs 2,055.77 lakh (FY26) vs Rs 927.36 lakh (FY25). Largest single sub-lines FY26: Net foreign exchange gain Rs 1,188.73 lakh (58% of other income!), Interest on bank deposits Rs 677.05 lakh, Doubtful-debt reversal / MSME-interest reversal / gain on FVTPL / write-back items totalling under Rs 300 lakh combined. 🔴 **Rs 1,188.73 lakh of Rs 2,055.77 lakh other income (58%) is unrealised/realised FX gain** — a volatile, non-repeatable item for a company with heavy export exposure (Saudi, UAE, Kenya, etc.) and outstanding monetary foreign-currency assets of Rs 22,129.51 lakh (mostly USD receivables) against liabilities of Rs 1,711.72 lakh (Note 48, consolidated). This FX gain is disclosed as flowing through "Other Income," not through operating revenue or a separate FX line in operating profit — meaning EBITDA/OPM as conventionally screened likely already excludes this Rs 1,188.73 lakh, but PBT (and the LBF4 "other income ~Rs 23 Cr of PBT ~Rs 48 Cr" observation) is materially inflated by an FX swing that could reverse. This is the single largest earnings-quality item found in the notes.

**EPS**: Basic and diluted EPS are identical in both years (standalone Rs 6.33 FY26/Rs 11.85 FY25; consolidated Rs 10.00 FY26/Rs 14.34 FY25) — no dilutive instruments (ESOP, warrants, convertibles) disclosed. 🟢 No dilution sources found; EPS decline YoY is a share-count effect (IPO issuance) combined with PAT change, not a dilution/anti-dilution artifact.

**CSR**: Required Rs 59.22 lakh (FY26) vs Rs 59.32 lakh (FY25); spent in full both years, with a small carried-forward excess of Rs 0.68 lakh. 🟢 Fully compliant, no shortfall.

**Capital commitments**: NOT FOUND IN DOCUMENT as a distinct disclosed line in either standalone or consolidated notes (only contingent liabilities and IPO-proceeds tables were found under adjacent note numbers).

**Foreign currency exposure**: heavily USD/SAR/AED-denominated; a 10% currency move would swing consolidated PBT by ~Rs 2,350.64 lakh (FY26) vs Rs 811.49 lakh (FY25) (Note 48 sensitivity, consolidated) — the sensitivity itself nearly tripled YoY, meaning FX risk to earnings has grown materially, consistent with the export-revenue mix shift toward UAE/Kenya. Only one USD forward contract (USD 20.00 lakh notional) is disclosed as hedged — an immaterial hedge ratio against the stated exposure. 🔴 Under-hedged given the scale of the sensitivity.

**Events after balance sheet date** (standalone Note 54; consolidated Note 60/second-numbered-60, duplicate note number in the AR — a drafting error: consolidated notes 60 and 61 both appear to be numbered around IPO/events, see note numbering anomaly below): Final dividend of Rs 0.60/share recommended, Rs 266.70 lakh total cash outflow, both standalone and consolidated. No other post-balance-sheet events disclosed in the notes (the acquisition filings of Jun-2026 referenced in B00 are NOT mentioned in this note — they postdate the AR's April 27, 2026 signing date but predate the AR's actual filing date of 31-Jul-2026, and are absent from the "events after reporting period" note, which should arguably have captured them if material and known before the report was finalised. Flag for stage 3/8.)

**Note-numbering anomaly** (🟡 disclosure-quality flag): the consolidated notes contain **two notes numbered "60"** — "60 Initial Public Offering" (AR p.199-200 txt) followed immediately by "60 Events after the Reporting period" (AR p.200 txt). This is a genuine numbering error in the filed AR (both standalone and consolidated close with Note 53-56 / 59-62 respectively, and the consolidated sequence skips from 59 to 60-duplicate to 61 to 62). Minor, but another data point on financial-statement drafting quality at listing-year scale, consistent with the balance-sheet-face error in Section 0.

**Auditor's Order (CARO) qualifications** (Independent Auditor's Report, AR p.144 txt): Clause (vii)(a) of the CARO Order (statutory dues) reported as unfavourable/qualified for the **Holding Company itself**, for **FT Institutions Private Limited** (subsidiary), and for **Mark Maker Engineering Private Limited** (associate). 🔴 Clause (vii)(a) concerns regularity in depositing statutory dues (PF, ESI, GST, income tax, etc.) — a CARO qualification here across the holding company AND a subsidiary AND an associate is a compliance red flag that should be read from the full CARO report text (not fully reproduced in the notes; the AR's CARO annexure itself should be pulled for the exact statutory dues in arrears — NOT FOUND IN DOCUMENT within the notes themselves, follow up in stage 3 with the standalone/consolidated CARO annexure text).

**Going concern language**: NONE found in the notes. Audit opinion is unmodified/unqualified on going concern in both standalone and consolidated reports (standard boilerplate risk-assessment language only, no material uncertainty disclosed).

**Direct debits/credits to reserves bypassing P&L**: Bonus share issue (Rs 2,944.75 lakh, FY25, capitalised from reserves) and IPO issue-expense utilisation against Securities Premium (Rs 2,232.66 lakh, FY26, net of taxes) are both direct equity-reserve movements, correctly routed through the Statement of Changes in Equity rather than P&L. 🟢 Standard, not a bypass concern.

---

# PASS 1 SUMMARY — TOP 10 FINDINGS RANKED BY INVESTOR IMPORTANCE

1. 🔴 **Consolidated balance sheet face overstates trade receivables and total assets** by Rs 3,718.39 lakh (24,151.90 vs correct 20,433.51 lakh trade receivables; 69,088.68 vs correct 65,370.29 lakh total assets). Confirmed a genuine AR drafting error, not OCR, by triangulating Note 13, MD&A, the financial-instruments note, and the exchange-filed audited results (all agree on 20,433.51 / 65,370.29). (Note 13 / balance sheet face, AR p.150 & p.173 txt.)
2. 🔴 **Trade receivable ageing is deteriorating, confirmed by the auditor as a Key Audit Matter**: >6-month receivables rose from 35.3% to 43.6% of gross receivables; ECL loss rates roughly tripled in the 1-3yr buckets (3.4-3.8% → 10.1%); the auditor separately flagged Rs 5,887.55 lakh of receivables overdue >365 days as a Key Audit Matter. Directly evidences the LBF2 cash-conversion concern is structural, not purely growth-induced. (Note 13, consolidated; Independent Auditor's Report, AR p.139-140 txt.)
3. 🔴 **58% of FY26 other income (Rs 1,188.73 lakh of Rs 2,055.77 lakh) is a net foreign-exchange gain**, against an under-hedged FX exposure (only one USD 20 lakh forward contract vs monetary FX assets of ~Rs 22,130 lakh) and an FX sensitivity that nearly tripled YoY. This is the largest single earnings-quality item found and directly informs LBF4 (other income composition). (Note 32, consolidated; Note 48 sensitivity.)
4. 🔴 **Customer concentration shows severe rotation, not durability**: three of FY25's top-4 customers each fell from >10% to single-digit % of revenue in FY26; a new customer appeared from near-zero to 12.55%. No segment profitability disclosed to assess whether this rotation is margin-neutral. Central to the quality-ladder pricing-power/stickiness question. (Note 44, consolidated.)
5. 🔴 **CARO qualification (Clause vii(a), statutory dues) across the Holding Company, a subsidiary, and an associate**, plus a duplicate note-49/49-numbering... [note-60 duplication] and the balance-sheet-face error (#1) together form a pattern of drafting/compliance quality issues in the first full-year AR post-listing. (Independent Auditor's Report, AR p.144 txt.)
6. 🟡 **Two consecutive years of "exceptional" gains from stake disposals** in group/associate entities (FY25: Rs 1,784.86 lakh, 29.5% of consolidated PBT, TSA/Thermax; FY26: Rs 177.49 lakh, 3.7% of PBT, FABL stake sale) — a recurring pattern under an "exceptional" label, relevant to earnings-quality assessment (LBF4). (Note 40, consolidated.)
7. 🟡 **MSME payment delays are worsening**: interest accrued and unpaid to MSME suppliers rose 149% YoY (Rs 21.52 lakh → Rs 53.59 lakh), with a statement that the same interest is expected to remain unpaid into the next year. Working-capital stress signal alongside the receivables deterioration. (Note 26/27.)
8. 🟡 **Rs 2,350.83 lakh current borrowing labelled "Loan from related party" but itemised as "Loan from Others,"** untraceable to a named counterparty in the related-party note. Disclosure gap requiring stage 3/8 follow-up. (Consolidated Note 26.)
9. 🟡 **Zero utilisation (0%) of the Rs 3,000 lakh IPO proceeds earmarked for inorganic growth/acquisitions** by FY26 year-end, with only 22% of total IPO proceeds deployed overall — directly relevant to LBF4 (IPO deployment vs RHP objects) and to the timing of the Jun-2026 acquisition filings (post-year-end). (Note 53/60.)
10. 🟡 **Saudi entity name/ownership mismatch against B00's Spear-line load-bearing fact**: the AR discloses "Fabtech Lifecare Company, KSA," 100%-owned via the UAE subsidiary, incorporated 26-Aug-2025, loss-making (Rs 455.52 lakh loss on Rs 1,370.91 lakh revenue in its first partial year) — not the "51% Specialized Contracting Activities LLC" named in company memory. Needs reconciliation: is the 51% entity a separate, later (post-FY26) acquisition? (Note 52/53, consolidated.)

**Carried-forward input gaps (from B00-inputs.yaml, unresolved by this pass):**
- Shareholding pattern beyond the NSE XBRL filings already held (promoter pledge trend still to be read from those XML tags, not a notes-to-accounts item).
- Screener export sheets empty for FABTECH and all three peers (does not affect notes reading).
- No results PDFs / rating PDF gaps already resolved at intake per B00.
- CARO annexure full text (statutory-dues qualification detail) not itself part of the Notes to Financial Statements and should be pulled separately in stage 3 if not already in scope.
- The Jun-2026 acquisition filings (post-FY26 balance sheet date) are not addressable from the FY26 AR notes; carry to stage 3/8 for announcements-based verification.
