# Stage 2 / Pass 1 — Notes to Financial Statements, Full Extraction
Company: Trident Lifeline Ltd (TLL) | Run: tll-2026-09-26 | Source: Annual_Report_2026.pdf (FY2025-26 AR, 150 PDF pages)
Unit: all figures quoted as printed, "Amount in Lakhs" per the AR face. 100 lakh = ₹1 Cr; I convert to ₹Cr in parentheses on first use of a figure for readability, source unit is lakh throughout.
Basis note: the AR is prepared under Indian GAAP / Accounting Standards (AS-18 related party, AS-3 cash flow), NOT Ind AS. No Ind AS 116 lease, no ECL matrix, no fair-value hierarchy note exist because the framework does not require them at this entity's size — their absence is a basis fact, not a disclosure gap.

Both a Standalone note set (Notes 1-32, pp.57-80) and a Consolidated note set (same numbering, Notes 1-33, pp.97-124) exist. I extracted both and flag where the two diverge materially.

## 1. ACCOUNTING POLICIES & CHANGES
- Basis of preparation: Indian GAAP, historical cost, AS-18/AS-3 (p.82, Consolidated Significant Accounting Policies; identical text standalone p.94/8600 area). 🟢
- Depreciation: Straight Line; Company's useful life for Vehicles is 3 years vs Schedule II norm of 8 years (more conservative/accelerated than the statutory norm) (p.83, policy D). All other classes (Computer, Furniture, Office Equipment, Electrical Installation, Intangibles) match Schedule II exactly. 🟢 no aggressive extension found.
- Capitalisation threshold: NOT FOUND IN DOCUMENT (no rupee threshold disclosed).
- Impairment: standard CGU/value-in-use language, no company-specific growth/discount-rate assumptions disclosed (NOT FOUND — assumptions not quantified). 🟡
- ECL matrix: NOT FOUND IN DOCUMENT — consistent with AS (not Ind AS) framework; no provision for doubtful debts is carried on any trade receivable in either standalone or consolidated ageing schedule (Note 17.1/17.2, pp.67, 108-109) despite receivables tripling. 🟡 WATCH — zero doubtful-debt provisioning against a fast-growing, largely export book (Ghana, Kenya, Peru, Venezuela) is not itself wrong under AS, but it removes a normal early-warning signal.
- Revenue recognition: recognised at dispatch/handover to transporter (p.83, policy I); both standalone and consolidated auditors named revenue recognition (discounts/rebates estimation) as Key Audit Matter #1 (p.43-44 standalone, p.86-87 consolidated). 🟡 judgmental area, not a red flag on its own — no restatement or reversal found.
- Ind AS 116 ROU/lease liability: NOT FOUND — AS-framework entity, no lease liability line on either balance sheet.
- First-time standard adoption: NOT FOUND — no new standard adoption disclosed this year.
- KAM #2 (both standalone and consolidated auditor reports, p.44/p.87): "The system needs to be further strengthened for its efficacy to control deficiencies of input/output data from the system" — auditors describe a "DOS based accounting system." 🟡 WATCH — dated, non-cloud accounting infrastructure named directly by the auditor as a control-strengthening item, for a company that has grown revenue 3x and added 5 subsidiaries in three years.

## 2. RELATED PARTY TRANSACTIONS (Note 30, AS-18; standalone pp.75-78, consolidated pp.118-122)
Two entities dominate the RPT picture and are NOT subsidiaries — they are "Director's Interest" LLPs:

| Party | Relationship | Consol. Sales FY26 | Consol. Sales FY25 | YoY % |
|---|---|---|---|---|
| Tench Life Sciences LLP | Director's Interest | ₹931.99L (9.32 Cr) | ₹666.24L (6.66 Cr) | +40% |
| Talon Healthcare LLP | Director's Interest | ₹854.73L (8.55 Cr) | ₹579.09L (5.79 Cr) | +48% |
| **Combined** | | **₹1,786.72L (17.87 Cr)** | **₹1,245.33L (12.45 Cr)** | **+43%** |

Combined RPT sales to these two LLPs = 13.9% of consolidated revenue from operations (₹12,902.13L) in FY26, up from 14.3% in FY25 — a stable but material dependency on two director-linked counterparties that are outside the consolidation perimeter. (Note 30B, p.118-119) 🟡 WATCH, borders 🔴.

Outstanding trade receivables from the same two LLPs at 31-Mar-26: ₹716.01L (Tench) + ₹408.03L (Talon) = ₹1,124.04L (11.24 Cr), 15.3% of total consolidated trade receivables of ₹7,365.39L. (Note 30C, p.121) 🟡

Unsecured loan taken FROM Chairman Hardik Desai during FY26 (consolidated): ₹1,353.37L (13.53 Cr) vs ₹491.00L (4.91 Cr) FY25 — promoter funding the company at an accelerating rate; year-end balance ₹295.69L (up from ₹35.99L) (Note 30B/C, p.120-121). 🟡 WATCH — direction (promoter lending TO company) is not itself adverse, but the pace of increase and the "repayable on demand" characterisation of these loans (Note 3.2, standalone p.60/consolidated p.100) means a material liquidity item sits outside normal covenant/maturity discipline.

Loans and advances GIVEN by the company to related parties (mix of subsidiaries and director-interest entities) — standalone outstanding ₹2,590.51L (25.91 Cr) is 100% of "loans in nature of loans" reported under CARO 3(iii)(f) (p.49) — all repayable on demand, no fixed term. Consolidated outstanding to non-subsidiary related parties (after eliminating subsidiary loans) = ₹919.91L (9.20 Cr), still material, spread across Talon (₹149.12L), Tench (₹217.38L), Trident Texofab (₹326.70L, a promoter-linked listed entity), T-Med Biovations (₹55.51L), VN Capital Services LLP (₹136.46L) (Note 30D, p.121-122). 🟡 WATCH.

New related party disclosed this year: T-Med Biovations Pvt. Ltd., Han Enterprise (consolidated only, subsidiary-level director interests) (Note 30A, p.118). 🟢 disclosed, not concealed.

Director remuneration: Rs 88.20L consolidated employment-benefit-expense line for FY26 vs Rs 140.68L FY25 (Note 25, p.112) — but see Section 12 below for the Section 197 excess-remuneration finding, which is the more material RPT-adjacent item.

## 3. CONTINGENT LIABILITIES (Note 32; standalone p.80, consolidated p.124)
| | Standalone FY26 | Standalone FY25 | Consol. FY26 | Consol. FY25 |
|---|---|---|---|---|
| Guarantees | ₹2,855.00L (28.55 Cr) | ₹2,900.00L (29.00 Cr) | ₹500.00L (5.00 Cr) | ₹500.00L (5.00 Cr) |

Standalone guarantees cover TNS Pharma, TLL Parenterals (both subsidiaries, eliminated on consolidation), PLUS Talon Healthcare LLP and Tench Life Sciences LLP (non-subsidiary, director-interest LLPs) (p.80). The consolidated figure of ₹500L is entirely the Talon + Tench guarantees, i.e., corporate guarantees the holding company has extended for entities it does NOT consolidate and does not own equity in beyond a token capital contribution (₹0.09L each, Note 11). 🔴 RED FLAG — the company is putting its balance sheet behind two LLPs it neither owns nor controls, whose only disclosed link is "Director's Interest." Total consolidated net worth at 31-Mar-26 = ₹9,667.56L (Reserves ₹8,474.26L + Share Capital ₹1,193.30L); ₹500L guarantee = 5.2% of net worth — not itself huge, but the qualitative fact (guaranteeing non-group entities) is the flag, not the quantum.
Contingent liabilities for "claims against the company not acknowledged as debt": NIL both years, both bases. 🟢
Capital commitments: NIL disclosed both years, both bases (Note 32) — though Capital WIP grew from ₹156.22L to ₹1,749.91L consolidated (Balance Sheet, p.107), meaning committed-not-executed capex should logically exist; NOT FOUND as a quantified commitment. 🟡 WATCH — disclosure gap given the scale of CWIP.

## 4. TRADE RECEIVABLES (Note 17; standalone p.67, consolidated p.108-109)
| | Standalone FY26 | Standalone FY25 | Consol. FY26 | Consol. FY25 |
|---|---|---|---|---|
| Total | ₹4,934.11L (49.34 Cr) | ₹2,040.16L (20.40 Cr) | ₹7,365.39L (73.65 Cr) | ₹2,768.25L (27.68 Cr) |
| >6 months | ₹385.26L (7.8%) | ₹234.35L (11.5%) | ₹449.73L (6.1%) | ₹363.97L (13.1%) |

This confirms LBF1 exactly at the consolidated level (₹27.7 Cr → ₹73.7 Cr). Revenue (consolidated) grew 48.4% (₹86.96 Cr → ₹129.02 Cr, Note 21) while trade receivables grew 166% — receivables grew 3.4x faster than revenue. However the AGEING COMPOSITION improved: the >6-months share of the book fell from 13.1% to 6.1%, and the >3-years bucket, while newly appearing at ₹141.78L in FY26 (nil equivalent bucket in FY25's disclosure structure, which showed a 2-3yr bucket of ₹87.57L instead), is small relative to the total. No provision for doubtful debts is carried in either year (Note 17.1/17.2). No single-customer concentration is disclosed by customer name; the only receivable-quality cut given is by geography (Note 31, Segment Reporting) and by related party (Note 30C). 🟡 WATCH, nuanced — this is GROWTH-INDUCED in composition (fresh money, not aged), but the disproportionate scale versus revenue growth, combined with a debtor-days jump from 116 to 208 (per LBF1/screener, consistent with the quantum here), means the growth-vs-structural question cannot be closed on ageing alone; it needs the customer-concentration and payment-terms evidence claude.ai verification is tasked with.
Segment note (Note 31) discloses "Analysis of Segment Assets By Geography (Only Trade Receivable)" totalling ₹4,947.50L consolidated at 31-Mar-26 (p.123) — this does NOT reconcile to the Note 17 Balance Sheet trade receivables total of ₹7,365.39L, a gap of ₹2,417.89L (24.18 Cr). The standalone equivalent DOES reconcile exactly (₹4,934.11L segment total = ₹4,934.11L Note 17 total, p.66/67). 🔴 RED FLAG — internal inconsistency between two notes in the same consolidated financial statements; the segment note appears to carry only the holding company's own receivables, not the consolidated Group figure, despite being presented as a consolidated note.

## 5. INVENTORY (Note 16; standalone p.66, consolidated p.107)
| | Standalone FY26 | Standalone FY25 | Consol. FY26 | Consol. FY25 |
|---|---|---|---|---|
| Raw Materials | 1,520.10 | 1,142.30 | 2,104.13 | 1,713.41 |
| Packing Material | 294.30 | 202.53 | 294.30 | 204.56 |
| Finished Goods | 507.47 | 312.41 | 1,245.48 | 906.32 |
| Total | 2,321.87 | 1,657.23 | 3,643.91 | 2,824.29 |
(all ₹ Lakhs)
No write-downs or obsolete-inventory disclosures found (NOT FOUND — inventory valued at "cost or NRV, whichever is lower," no impairment charge line visible in Note 28 Other Expenses). Consolidated finished goods grew 37.4% (₹906.32L→₹1,245.48L) against revenue growth of 48.4% — finished goods growing slower than revenue, no red flag. 🟢
No inventory-days trend computed in the AR (Analytical Ratio table, standalone Note 29(q), shows Inventory Turnover Ratio improving marginally, 4.91x→5.12x, "No Major Variance" per management's own note, p.74). 🟢

## 6. INVESTMENTS (Note 11; standalone pp.64-65, consolidated pp.105-106) + AOC-1 (p.41, Annexure to Directors' Report)
Standalone non-current investments in subsidiaries at cost:
| Subsidiary | Holding % | FY26 Carrying Value | FY25 Carrying Value |
|---|---|---|---|
| TNS Pharma Pvt. Ltd. | 51% | ₹255.00L | ₹153.00L |
| TLL Wellness Ltd. | 51% | ₹5.10L | ₹5.10L |
| TLL Parenterals Ltd. | 51% | ₹112.71L | ₹112.71L |
| TLL Elements Pvt. Ltd. | 100% | ₹1.00L | ₹1.00L |
| Trident Mediquip Ltd. | 59.77% (up from 51%) | ₹1,141.83L | ₹449.15L |

AOC-1 Part A (salient features of subsidiaries, p.41) — this is the critical LBF3 cross-check:
| Subsidiary | FY26 Turnover | FY26 PAT | Other Equity | % Holding |
|---|---|---|---|---|
| TNS Pharma Pvt. Ltd. | ₹576.52L (5.77 Cr) | (₹298.98L) loss | (₹676.55L) — negative net worth | 51.00% |
| Trident Mediquip Ltd. | ₹2,731.75L (27.32 Cr) | ₹430.39L profit | ₹821.03L | 59.77% |
| TLL Parenterals Ltd. | ₹0 — "yet to commence operations" | ₹1.86L PBT (₹1.35L PAT) | ₹1.39L | 51.00% |
| TLL Wellness Ltd. | ₹11.78L | ₹0.87L | (₹7.25L) | 51.00% |
| TLL Elements Pvt. Ltd. | ₹2.46L | (₹11.03L) loss | (₹10.95L) | 100.00% |

This DIRECTLY confirms the LBF3 gap: TNS Pharma (deck peak Rs 40 Cr) delivered ₹5.77 Cr and is LOSS-MAKING with negative net worth; Trident Mediquip (deck peak Rs 70 Cr) delivered ₹27.32 Cr; TLL Parenterals (deck peak Rs 200 Cr) has NOT COMMENCED OPERATIONS and shows zero turnover. 🔴 RED FLAG (deck-vs-delivery gap, evidenced from the audited AOC-1 itself, not inferred).
No impairment has been booked against the TNS Pharma investment (carrying value INCREASED from ₹153.00L to ₹255.00L during the year despite the subsidiary's accumulated losses exceeding its share capital) (Note 11 vs AOC-1). 🔴 RED FLAG — a subsidiary with negative net worth is being carried at cost with no stated impairment testing basis (impairment policy note E, p.83, gives generic CGU language with no company-specific test disclosed for this investment).
ICDs/loans given: see Section 2 (RPT) — no arm's-length interest-rate benchmark disclosed for related-party loans/ICDs; rates received range ~7-10% per the Note 30 "Interest Received" lines, broadly consistent with the company's own borrowing cost range (7.6-9.75% per Note 3.4). 🟢 not obviously non-arm's-length on rate.
Goodwill: consolidated Balance Sheet carries Goodwill of ₹555.15L (5.55 Cr) at 31-Mar-26 vs ₹52.37L at 31-Mar-25 — a 10.6x increase with ZERO explanatory note anywhere in the AR (no goodwill note, no acquisition-accounting breakdown, no impairment test disclosed) (Balance Sheet line only, p.107). 🔴 RED FLAG — a material, fast-growing intangible asset with no supporting note is a disclosure gap the operator should press on; it plausibly arises from the Trident Mediquip stake increase to 59.77% (Note 33.1, p.124), but the AR does not say so.
Quoted investment: Trident Texofab Ltd. (promoter-linked listed entity) carried at cost ₹22.38L; market value at 31-Mar-26 disclosed as ₹16.04L (i.e., an unrealised loss of ₹6.34L against cost, not written down since AS treats long-term investments at cost less permanent diminution only) (Note 11, p.65/106). 🟡 WATCH, immaterial in size.

## 7. BORROWINGS (Note 3, 6; standalone pp.58-60, consolidated pp.99-101)
Standalone secured borrowings: ICICI vehicle loans, Axis Bank term loan (hypothecation of P&M), Surat People's Bank solar loan; personal guarantees of Hardik Desai, Anjanaben Desai, Nathabhai Gajera, Vilasben Gajera pledged for term loan & CC facility (Note 3.5, p.60); two shop properties + FDR of ₹2.11 Cr pledged as collateral (Note 3.6-3.7). 🟢 disclosed, standard SME practice.
Consolidated borrowings add subsidiary-level facilities: SIDBI, Yes Bank, Zoroastrian Co-op Bank, Surat People's Co-op Bank term loans (Trident Mediquip), Yes Bank term loan (TLL Parenterals — despite the subsidiary having "not commenced operations," it carries a term loan of ₹1,067.47L non-current + ₹186.44L current, Note 3, p.100), Axis Bank term loan (TNS Pharma). 🟡 WATCH — debt-funding a pre-revenue subsidiary is a funding-structure point worth flagging (ties to LBF3 funding-plan question).
No covenant breach or waiver disclosed (Note 3.3/6.2, both bases: "the company has not defaulted in repayment of Loans and Interest"). 🟢
Rate range: 7.60%-10.25% across secured facilities (Note 3.4, consolidated p.100-101). Unsecured loans from Directors & Promoter Group: ₹1,408.64L non-current + nil current FY26 vs ₹1,070.59L FY25 (Note 3, consolidated p.100) — growing promoter-funding line, consistent with Section 2 above.

## 8. TRADE PAYABLES (Note 7; standalone pp.61-62)
Standalone: Total ₹2,602.92L FY26 vs ₹964.97L FY25 — 100% "Less than 1 Year" bucket in the ageing schedule both years (Note 7.1/7.2, p.61); MSME dues within the total: ₹309.61L FY26 vs ₹123.46L FY25, both fully "less than 1 year," NO disputed dues, NO interest accrued or paid under Section 16 MSMED Act (Note 7.3, p.62). 🟢 clean, though the payable book has also grown ~170%, roughly matching the receivables growth on the other side of working capital — consistent with a genuinely scaling business rather than pure stretching of one side of the book.
Consolidated trade payables: ₹3,843.48L FY26 vs ₹1,478.83L FY25 (Balance Sheet, p.107) — detailed ageing/MSME breakdown for the consolidated book was NOT located as a separately reconciled consolidated note (the standalone Note 7 ageing table is the only one directly read); consolidated-level MSME/ageing split: NOT FOUND IN DOCUMENT within the pages reviewed.

## 9. PROVISIONS (Note 4, 9; standalone pp.58, 62-63)
Long-term provision: Gratuity ₹7.02L, unchanged both years, "as certified by management" — i.e., NOT an independent actuarial valuation for this figure specifically (though policy note J states an independent actuary is used for the defined benefit plan, p.83/95). 🟡 WATCH — the static ₹7.02L figure for two consecutive years despite headcount and salary growth (Salary & Wages up 12.6% standalone, employee costs up generally) is unusual for an actuarially-revalued liability; no actuarial assumptions (discount rate, salary growth, attrition) are disclosed anywhere (NOT FOUND).
Short-term provisions: Income Tax provision ₹589.50L FY26 vs ₹425.00L FY25 (Note 9, p.63) — no litigation provision, no warranty provision, no onerous-contract provision disclosed (all NOT FOUND / not applicable to this business model).

## 10. DEFERRED TAX (Note 5, 12; standalone pp.60, 66)
Standalone: Deferred Tax LIABILITY ₹94.37L FY26 vs ₹45.78L FY25, entirely "Related to Fixed Assets" (accelerated tax depreciation vs book) — standalone carries NO deferred tax asset (Note 12 all-zero, p.66). 🟢 straightforward, no unusual reconciliation items.
Consolidated: Deferred Tax ASSET (net) ₹297.00L FY26 vs ₹240.10L FY25 — ₹234.02L of this is "Related to Carried Forward loss and Unabsorbed Depreciation" (consolidated Note 12, p.107) — i.e., the Group nets a subsidiary-level DTA against the holding company's own DTL. Given TNS Pharma's accumulated losses (Section 6 above), this DTA recognition implicitly assumes TNS Pharma (or another loss-making subsidiary) will generate future taxable profit to utilise carried-forward losses. No virtual-certainty evidence (per the company's own policy L, p.83) is disclosed to support this. 🟡 WATCH — DTA realism is unverified from the note itself.
No effective-vs-statutory tax rate reconciliation table found in either note set (NOT FOUND IN DOCUMENT — AS framework does not mandate the Ind AS 12-style rate reconciliation).
MAT credit entitlement: ₹5.31L FY25 fell to NIL FY26 (Note 20 Other Current Assets, both standalone and consolidated) — fully utilised, no timeline commentary needed since it is now zero. 🟢

## 11. REVENUE DETAILS (Note 21, 31; standalone pp.66, 79; consolidated pp.110, 123)
Consolidated revenue disaggregation (Note 21, p.110): Domestic Products ₹7,537.81L, Export Products ₹5,271.48L, Sale-MEIS ₹11.55L, Sales of Services (Domestic) ₹81.29L. Total ₹12,902.13L.
Geographic segments (Note 31, p.123): India ₹7,630.65L, Ghana ₹1,589.76L, Kenya ₹858.68L, Peru ₹1,293.71L, Venezuela ₹469.49L (down sharply from ₹2,212.89L FY25 — a 78.8% drop in the single largest FY25 export market), Rest of World ₹1,059.85L (up from ₹121.86L). 🟡 WATCH — Venezuela concentration collapsed and was replaced by a "Rest of World" bucket that grew almost 8.7x with no country-level breakdown — this masks which new markets replaced Venezuela.
No customer-level revenue concentration disclosed (product/segment only by geography; NOT FOUND at customer level, beyond the related-party customer concentration already covered in Section 2 — Tench + Talon alone = 13.9% of consolidated revenue).
No contract assets/liabilities, no unsatisfied performance obligations note (NOT FOUND — AS framework, dispatch-based recognition, no Ind AS 115-style disclosure required).

## 12. OTHER CRITICAL NOTES
- **Section 197 excess director remuneration** (Directors' Report item 20, p.25; Consolidated Auditor's Report Other Matters (g) p.89 and (vii) p.91): Hardik Desai's FY26 remuneration exceeded the Section 197 statutory limit by ₹22.62L — within limits previously approved by members (21-Sep-2023 AGM), so procedurally covered. Ashish Bafna's remuneration exceeded the limit by ₹6.37L WITHOUT prior member approval; the Board on 26-Aug-2026 has RATIFIED it subject to member approval, with a special resolution placed before the FY26 AGM. The statutory auditor separately and explicitly qualifies this in the Section 143 "Other Matters" of BOTH the standalone-referencing and consolidated audit reports. 🔴 RED FLAG (governance) — the auditor is on record naming a Companies Act breach requiring retrospective shareholder ratification; the outcome of that AGM resolution is a live, checkable fact.
- **IT audit trail (edit log) not maintained in one subsidiary company**, both at database level (payroll, consolidation, general ledger) and application level (revenue, trade receivables, general ledger, PP&E) for the full year (Consolidated Auditor's Report, Rule 11(g), p.90). 🔴 RED FLAG — a named, unremediated internal-control gap under the Companies (Audit and Auditors) Rules audit-trail mandate, at one (unnamed) subsidiary.
- **Statement of Deviation, Preferential Warrant Issue** (Directors' Report item 5, p.24): estimated utilisation ₹2,657.34L; ACTUAL utilisation as of 31-Mar-26 only ₹1,526.57L (57.5%), disclosed in a single vague line "as mentioned in the offer documents," unlike the IPO utilisation table immediately above it which breaks spend into four named categories. 🔴 RED FLAG — a genuine SEBI LODR Regulation 32 deviation disclosure exists (partially answers LBF3/LBF4's funding-plan question), but the categorical breakdown investors need to assess WHERE the ₹1,130.77L shortfall sits (working capital vs subsidiary investment vs debt repayment vs business expansion) is not given.
- **IPO proceeds deviation**: "Product registration in international markets" category was budgeted ₹513.66L but only ₹75.81L (14.8%) had been utilised by 31-Mar-26, three-plus years after listing (Directors' Report item 5, p.24). 🟡 WATCH — slow international registration spend is consistent with the export-market concentration risk already flagged (Venezuela collapse, Section 11).
- **Exceptional/one-time items**: none labelled "exceptional" or "extraordinary" in either P&L (P&L structure shows "Profit before Exceptional and Extraordinary items" = "Profit before Tax" in both years/both bases, i.e., zero such items, Directors' Report financial highlights table p.19-20). 🟢
- **EPS**: Basic = Diluted in all cases (no separate diluted figure disclosed, Note 29(r) standalone p.74; consolidated EPS 16.32 vs standalone 15.37 per Directors' Report table, p.20) — the gap between standalone (₹15.37) and consolidated (₹16.32) EPS is explained by Minority Interest absorbing a smaller loss/larger share of profit allocation; no dilution instruments (ESOP, warrants outstanding at year-end) remained after full warrant conversion during the year (Note 1.7, all warrants converted to equity by year-end). 🟢
- **CSR**: standalone required ₹22.85L, spent ₹22.85L including reversing a prior-year ₹4.04L shortfall — fully compliant (Note 28.3, p.72-73). 🟢
- **Share capital / warrants** (Note 1, both bases; Directors' Report items 3-9, pp.35-36): 9,94,200 warrants allotted 09-Jun-2025 at ₹266/warrant (₹256 premium); converted in five tranches (93,000 on 01-Jul-25; 49,800 on 21-Nov-25; 55,800 on 05-Dec-25; 1,00,200 on 16-Dec-25; 1,35,000 on 27-Dec-25) = 4,33,800 shares converted, matching the Note 1.7 reconciliation exactly. Outstanding warrants not yet converted at year-end: 9,94,200 − 4,33,800 = 5,60,400, consistent with the Balance Sheet "Share Application Money Pending Allotment" of ₹372.67L (consolidated, p.107) representing warrant money received but not yet converted. 🟢 arithmetic reconciles cleanly.
- **Bonus shares issued by Trident Mediquip** debited against consolidated P&L Surplus (₹155.60L, Note 2, p.108) rather than routed through Securities Premium — a direct adjustment to Reserves bypassing the current-year P&L, described only as "adjusted on account of changes in shareholding during the year 2025-26" with no further breakdown. 🟡 WATCH — a direct-to-reserves adjustment tied to the subsidiary stake/bonus restructuring (Note 33.1) that is not separately reconciled.
- **Going concern**: no going-concern language anywhere in either audit report; both explicitly conclude no material uncertainty exists (Standalone CARO xix, p.51; auditor's responsibilities section, both reports). 🟢 NONE.
- **Auditor's remuneration**: ₹3.10L FY26 vs ₹2.35L FY25, split Statutory Audit/Tax Audit/GST Fees (Note 28.1, p.72) — modest increase, no non-audit-fee concentration concern. 🟢

---

# PASS 1 SUMMARY — TOP 10 FINDINGS RANKED BY INVESTOR IMPORTANCE

1. **Corporate guarantees given for non-subsidiary, director-interest LLPs** (Talon Healthcare LLP, Tench Life Sciences LLP) — ₹500L consolidated / ₹2,855L standalone total guarantees, Note 32, pp.80/124. 🔴
2. **Segment note (Note 31) trade-receivable total does not reconcile to the Balance Sheet/Note 17 consolidated trade receivables** — ₹4,947.50L vs ₹7,365.39L, a ₹2,417.89L gap; standalone reconciles exactly. Notes 17 & 31, pp.108/123. 🔴
3. **Goodwill jumped 10.6x (₹52.37L → ₹555.15L) with zero explanatory note** on the consolidated balance sheet, p.107. 🔴
4. **AOC-1 confirms the LBF3 deck-vs-delivery gap directly from audited data**: TNS Pharma loss-making with negative net worth on turnover of ₹5.77 Cr (deck peak ₹40 Cr); TLL Parenterals "yet to commence operations" (deck peak ₹200 Cr); Trident Mediquip ₹27.32 Cr (deck peak ₹70 Cr). p.41. 🔴
5. **TNS Pharma investment carried at INCREASED cost (₹153L→₹255L) despite negative net worth and a widening loss**, with no impairment disclosed. Note 11 vs AOC-1, pp.65/41. 🔴
6. **Section 197 excess director remuneration**, separately and explicitly qualified by the statutory auditor in "Other Matters" — Ashish Bafna's excess (₹6.37L) still pending shareholder ratification at the FY26 AGM. Consolidated Auditor's Report pp.89/91; Directors' Report p.25. 🔴
7. **IT audit trail (edit log) not maintained in one subsidiary company**, both database and application level, all year. Consolidated Auditor's Report Rule 11(g), p.90. 🔴
8. **Unexplained "Claim Income" of ₹541.05L is 58% of consolidated Other Income** (₹927.15L) with no note anywhere describing its nature. Note 22, p.110-111. 🔴
9. **Preferential warrant proceeds utilisation deviation**: only 57.5% (₹1,526.57L of ₹2,657.34L) utilised by year-end, disclosed in one vague line with no category breakdown, unlike the IPO utilisation table. Directors' Report item 5, p.24. 🔴
10. **Consolidated trade receivables grew 3.4x faster than revenue** (166% vs 48.4%) confirming LBF1's cash-conversion concern quantitatively; CFO of only ₹469.07L against PAT of ₹1,931.88L, with the ₹4,597.13L increase in trade receivables as the single largest working-capital drag. Consolidated Cash Flow Statement p.97-98; Note 17 p.108-109. However ageing composition IMPROVED (>6-months share fell 13.1%→6.1%), so this is not yet a pure deterioration story — it needs the customer-concentration/terms evidence from claude.ai to classify GROWTH-INDUCED vs STRUCTURAL. 🟡/🔴 boundary.

---
This is Pass 1 of 3. Pass 2 (what was missed) and Pass 3 (pattern pass + consolidation) follow in separate calls per the pipeline instruction; this file carries only the Pass 1 extraction and its top-10 summary as specified.
