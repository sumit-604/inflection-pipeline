# STAGE 2 — NOTES TO FINANCIAL STATEMENTS — PASS 3: PATTERN PASS + CONSOLIDATION
**Company:** Airfloa Rail Technology Ltd | **Ticker:** 544516 (AIRFLOA) | **Run date:** 2026-07-15
**Source document:** `inputs/annual-report/1758608206692.pdf` (IPO Prospectus, 16-Sep-2025, 386 pages)

## DOCUMENT IDENTIFICATION (carried from Pass 1/2)
The source is the IPO Prospectus, not a conventional annual report. Restated financials: consolidated
Annexures I–XLVI (FY25 only, CFS1–CFS39); standalone Annexures I–XLVII (FY23–FY25, SFS1–SFS45). No
separate Annual Report or DRHP exists in the file set. This gap is carried into `input_gaps` below.

---

## PASS 3 — PATTERN RE-READ (contradictions, mismatches, deliberate vagueness, restatements, subsequent events, going concern)

A targeted, non-sequential re-read of both passes' extraction plus cross-checks against the auditor's
reports surfaces the following NEW pattern-level findings not previously isolated as such in Pass 1 or
Pass 2 (both passes already captured most raw data; Pass 3's job is to name the patterns that connect it):

1. **CONTRADICTION — company's own ratios say "improving," the cash flow statement says the opposite.**
   The company's Significant Accounting Ratios note (SFS p.44) shows DSCR rising 0.21x → 0.42x → 0.68x
   and Current Ratio rising 0.95x (FY22) → 0.99x → 1.12x → 1.44x — a narrative of steady deleveraging and
   liquidity improvement. The Restated Statement of Cash Flows (Annexure III, SFS p.7 / CFS p.7) shows the
   opposite underlying reality: net operating cash flow went **negative in FY25 (₹(4.43) Cr)** and the
   FY25 current-ratio improvement is substantially an artifact of the FY25 equity raise inflating cash, not
   of operating cash generation. Two notes in the same filing, read together, tell contradictory stories
   about the trajectory of the business's cash health; an investor reading only the ratios note (the more
   prominent, summary-style disclosure) would reach the wrong conclusion. 🔴🔴

2. **META-PATTERN — "inadvertently missed" recurs across at least six independent, unrelated notes.**
   Gratuity provision (Annexure IV Note 3/4), CSR expenditure (Annexure XLVI), interest on late statutory
   dues/TDS (Annexure IV, Finance Cost XXVIII), interest on delayed MSME payments (Annexure XLIV), ROC
   charge registration for ₹51.17 Cr Axis Bank and ₹1.43 Cr BMW India Financial borrowings (Annexure XLV),
   and the quarterly stock/book-debt discrepancies reported to Axis Bank and Union Bank (Additional
   Regulatory Information, SFS p.40–42) all use near-identical exculpatory language ("inadvertently
   missed," "inadvertently netting-off"). Six separate control failures across six separate statutory/
   compliance domains, all surfacing and all being remediated in the same pre-IPO window, is a pattern of
   its own: either a genuinely weak controls environment across the whole company, or standardised
   boilerplate explanatory language applied uniformly regardless of the actual root cause in each case.
   Either reading is a going-in caution on management's self-reporting of control gaps. 🔴

3. **Related-party receivable disproportionate to transaction volume — Raghavendra Industries.**
   FY25 sales to this related party were ₹2.01 Cr (Section 2, Pass 1), yet the outstanding receivable from
   the same party is ₹7.46 Cr — **3.7x the year's sales volume** — and has grown every year (₹4.91 Cr FY23
   → ₹4.83 Cr FY24 → ₹7.46 Cr FY25). This is not explainable by normal credit terms on current-year sales
   alone; it implies multi-year uncollected balances sitting with a related party, with zero doubtful-debt
   provisioning anywhere in the filing (Section 1/4, Pass 1). A collectability and arm's-length-terms
   question follows directly from reading the RPT table against the receivables ageing note together. 🔴

4. **Vagueness gradient — detailed disclosure where scrutiny is low, terse disclosure where scrutiny would matter more.**
   Borrowings (Annexure XXXII) and RPT (Annexure XXXV) are disclosed at instrument/counterparty level with
   full detail. By contrast, the nature of the >5x, two-year rise in Advertisement & Business Promotion
   spend (Annexure XXX, Pass 2 Finding 8) and the rising but unhedged import exposure (Annexure XLI,
   Pass 1 Section 11) receive no explanatory detail at all, despite both being directionally unusual and
   coinciding with the pre-IPO period. The asymmetry in disclosure depth is itself a signal worth naming
   even though each underlying fact was already captured individually. 🟡

5. **Subsequent events / going concern — confirmed clean on this final read.** No dedicated subsequent-
   events note exists in the annexures (the IPO process, corporate conversion, and name changes are
   covered in the prospectus body, not a financial-statement note — NOT FOUND IN DOCUMENT as a formal
   note). Both auditor's reports (CFS p.2, SFS p.2) are unqualified with no emphasis-of-matter or
   going-concern paragraph. This is unchanged from Pass 1 and is reconfirmed, not a new finding, but is
   restated here per the Pass 3 checklist requirement. 🟢

No further material new findings beyond the five patterns above emerged from the contradiction/mismatch/
vagueness sweep; Pass 1 and Pass 2 already captured the underlying raw disclosures comprehensively.

---

# CONSOLIDATED NOTES ANALYSIS, ALL THREE PASSES COMBINED

## A. TOP 15 MOST SIGNIFICANT FINDINGS (ranked by investor importance)

| Rank | Finding | Note # | Rating | Why it matters |
|---|---|---|---|---|
| 1 | Standalone operating cash flow turned **negative in FY25 (₹(4.43) Cr)** despite PBT nearly tripling to ₹34.98 Cr since FY23; FY24 OCF of only +₹3.46 Cr already masked a ₹52.94 Cr swing into receivables. FY25 growth funded by the equity raise (+₹26.90 Cr gross), not operations. Directly contradicts the "improving" DSCR/current-ratio narrative in the ratios note (see Pass 3 Pattern 1). | Annexure III (Cash Flow), SFS p.7 / CFS p.7 | 🔴🔴 | Core cash-quality test; profit growth is not converting to cash — the single most important finding for FLAG-CASH |
| 2 | Multi-year, multi-bank, multi-quarter discrepancies between company books and stock/book-debt statements filed with lenders for working-capital drawing power, up to **₹70.97 Cr in a single quarter** (Q1 FY25, Axis Bank), across FY23–FY25, with only generic explanations offered | Additional Regulatory Info table, SFS p.40–42 / CFS p.38 | 🔴🔴 | Systemic, recurring misreporting to secured lenders; raises questions about the reliability of internal MIS/controls |
| 3 | ₹8.73 Cr of company-book land ("Land-Nehru Nagar") has unregistered title still in the personal names of the two promoter-MDs (sale agreement dated FY2021-22, unregistered 4+ years later), and this same land is pledged as bank collateral for company debt | Annexure XLV(i), SFS p.39; cross-ref XIV/XV (PP&E), XXXII (Borrowings) | 🔴🔴 | Governance and asset-recoverability risk; ~3.4% of consolidated assets with unclear legal title, entangled with promoter personal holdings |
| 4 | MSME dues: the same ₹0.35 Cr principal has been unpaid for 3+ years; accrued interest (₹0.39 Cr) now **exceeds the principal**; company admits its MSME-creditor identification process is incomplete | Annexure XI/XXXIII/XLIV, SFS p.18,32,39 | 🔴🔴 | Statutory violation, compounding, with an admitted disclosure gap on top |
| 5 | Debt Service Coverage Ratio below 1.0x in **all three** disclosed years (0.21x FY23, 0.42x FY24, 0.68x FY25); current ratio below 1.0x in FY22 and FY23 too, with negative Net Capital Turnover Ratio in FY23 | Significant Accounting Ratios, SFS p.44 | 🔴 | Operating cash flow has never covered debt service in the disclosed history; liquidity stress predates the restated window |
| 6 | Extensive prior-period restatement: gratuity, CSR, interest on borrowings, statutory-dues interest, MSME interest, and income/deferred tax were all "inadvertently" mis-booked in prior years, retrospectively corrected across FY23–FY25 via opening-reserves adjustment | Annexure IV Notes 3 & 4, SFS p.13–14 / CFS p.12–13 | 🔴 | Breadth and repetition point to a weak pre-IPO financial-control environment now being cleaned up specifically for listing |
| 7 | FY23 restated profit was **226% higher** than originally audited (₹0.46 Cr → ₹1.49 Cr), driven by a single ₹2.26 Cr interest-expense reversal by the prior auditor; FY23 restated net worth is simultaneously **₹0.81 Cr lower** than originally audited, implying larger negative adjustments to pre-FY23 opening reserves | Annexure IV Note 3 & 4, SFS p.13–14 | 🔴 | FY23 is the base/anchor year for every growth-rate calc in this analysis; its own profit figure required a near-tripling correction, and control weaknesses extend before the restated window even starts |
| 8 | Section 185 Companies Act violation (loans to related parties) in FY23 and FY24, remediated only by repayment before the audit date, not contemporaneous compliance | Auditor's Report item 8(iv), CFS p.2 / SFS p.3 | 🔴 | Statutory violation; remediation timing (repaid "till date," i.e., pre-IPO) suggests IPO-driven cleanup rather than ongoing compliance discipline |
| 9 | Historical reliance on very high-cost debt: 24% p.a. ICL from Rauhat Financial secured by promoters' personal land; 16–16.5% p.a. from Share India Fincap, Aditya Birla Finance, RBL Bank; all repaid to nil by FY25 | Annexure XXXII, SFS p.29–31 | 🔴 | Strong liquidity-stress signal for FY23/FY24; cost of capital that severe implies constrained access to conventional bank credit at the time |
| 10 | CSR non-compliance for multiple years, predating even the restated window (opening FY23 CSR liability already ₹0.70 Cr), cleared via a lump ₹1.08 Cr catch-up payment in FY25 timed with the IPO process | Annexure XLVI, SFS p.45 (+ Note 2) | 🔴 | Multi-year statutory non-compliance, remediated only under IPO scrutiny, part of the recurring "inadvertently missed" pattern (Pass 3 Pattern 2) |
| 11 | Trade receivables aged >6 months rising steadily as a share of total (15.95% FY23 → 17.85% FY24 → 23.38% FY25) with **zero doubtful-debt provisioning** in any of the three years despite ₹6.66 Cr sitting in the 2–3yr bucket | Annexure XIX/XXXIV, SFS p.20,33 | 🔴 | Provisioning adequacy is a genuine concern given the ECL-policy gap under IGAAP; feeds FLAG-CASH directly |
| 12 | Unregistered charges with ROC beyond the statutory period on ₹51.17 Cr (Axis Bank) and ₹1.43 Cr (BMW India Financial) borrowings, both attributed to "inadvertently missed to file" | Annexure XLV item x, SFS p.43 | 🔴 | Statutory charge-registration non-compliance on the company's two largest secured facilities |
| 13 | Recurring "inadvertently missed" / "inadvertently netting-off" language spans at least six independent statutory and lender-reporting domains (gratuity, CSR, TDS interest, MSME interest, ROC charges, bank stock-statement reporting) | Pass 3 meta-pattern; cross-refs Annexures IV, XLIV, XLV, XLVI, Additional Regulatory Info | 🔴 | A cross-note pattern, not isolated incidents; suggests either systemic control weakness or uniform boilerplate explanatory language regardless of root cause |
| 14 | Related-party receivable from Raghavendra Industries (₹7.46 Cr FY25) is **3.7x** that party's annual sales volume from the company (₹2.01 Cr) and has grown every year since FY23 (₹4.91 Cr) | Annexure XXXV (RPT); cross-ref Annexure XIX/XXXIV (Receivables ageing) | 🔴 | Collectability/arm's-length-terms question on a related party, not just a general receivables-ageing concern |
| 15 | Standalone net cash used in operating activities corroborated at consolidated level (FY25 consol. OCF ₹(4.45) Cr); growth funded by fresh equity (₹26.91 Cr) and short-term borrowing, not the business | Annexure III, CFS p.7 | 🔴 | Confirms Finding 1 is not a standalone-only artifact; group-level cash generation is equally weak |

## B. ACCOUNTING QUALITY SCORE (1–10)

| Dimension | Score /10 | Basis |
|---|---|---|
| Revenue recognition conservatism | 6 | Single-point, dispatch-based recognition, not aggressive (Note 2.13); but no segment/customer-concentration disclosure limits verifiability |
| Expense capitalisation honesty | 7 | No material capitalisation controversy found; intangibles/PP&E balances are small and unremarkable |
| Provisioning adequacy | 3 | Zero doubtful-debt provision across 3 years despite deteriorating ageing (Finding 11); 54% flat gratuity attrition assumption is liability-minimising; no warranty/onerous-contract provisions to assess |
| RPT fairness | 3 | Related-party capital advance for machinery ahead of an independent vendor; disproportionate related-party receivable (Finding 14); historical promoter loans requiring Section 185 remediation; promoter personal land pledged as collateral and sitting unregistered on company books (Finding 3) |
| Disclosure transparency | 4 | Detailed instrument-level RPT/borrowings tables coexist with several NOT FOUND items (useful lives, customer concentration, segment table, hedging policy) and one direct note-to-note numeric mismatch (imports CIF vs. forex expenditure note, Pass 2 Finding 9) |
| Consistency with prior years | 2 | Extensive multi-item restatement, FY23 profit revised +226%, FY23 net worth revised down, control weaknesses traced to before the restated window begins (Finding 7) |
| **OVERALL** | **3** | Weighted toward the severity and multiplicity of statutory violations (Section 185, MSME, ROC charge registration, CSR) and the cash-flow/ratio contradiction (Pattern 1), not a simple arithmetic average of the above |

## C. KEY RISKS FROM NOTES

| Risk | Severity | What to monitor | When it could hit |
|---|---|---|---|
| Operating cash flow not covering earnings growth (FY25 OCF negative despite PBT growth) | High | FY26 OCF vs. PBT trend; receivables/inventory as % of revenue | Next reported quarter/FY26 results |
| Lender reporting discrepancies (stock/book-debt statements vs. books) | High | Any bank covenant review, facility renewal terms, or RBI/lender action | Next facility renewal cycle |
| Unregistered land title used as collateral, held personally by promoter-MDs | High | Registration completion status; any dispute or promoter-related transaction involving this asset | Registration deadline (none disclosed) or any promoter-entity transaction |
| MSME/statutory non-compliance pattern (MSME interest > principal, ROC charges, CSR, TDS) | Medium-High | Whether new occurrences arise post-listing (would break the "pre-IPO cleanup" narrative) | Each subsequent quarterly/annual filing post-listing |
| Related-party receivable concentration and collectability (Raghavendra Industries) | Medium | Balance trend and any write-off/provision taken | Next annual note disclosure |
| Deteriorating receivables ageing with zero doubtful-debt provisioning | Medium | >6-month ageing % trend; any provision finally taken | Next annual note disclosure |
| Rising unhedged import exposure (1.71% → 5.51% of raw material) with no hedging policy | Low-Medium | INR/import-currency movements; any forex loss volatility in P&L | Ongoing, currency-dependent |

## D. FIVE QUESTIONS FOR MANAGEMENT

1. What specific remediation and controls have been implemented to prevent recurrence of the stock/book-debt reporting discrepancies to Axis Bank and Union Bank of India, given these occurred in every quarter across three consecutive years with differences up to ₹70.97 Cr?
2. What is the current status and expected timeline for registering the title transfer of the ₹8.73 Cr Nehru Nagar land from the promoter-MDs' personal names into the company's name, and what is the contingency if registration is not completed while the asset remains pledged as bank collateral?
3. Given standalone operating cash flow turned negative in FY25 (₹(4.43) Cr) despite PBT growth, what specific working-capital actions are planned to convert profit growth into operating cash generation, and was FY25 growth structurally dependent on the equity raise rather than the business?
4. Why is the actuarial attrition assumption for gratuity held flat at 54% for three consecutive years, and can this be supported against the company's actual historical attrition experience?
5. What is the collectability assessment and credit-term basis for the ₹7.46 Cr receivable from related party Raghavendra Industries, which is 3.7x that party's FY25 purchase volume and has grown every year since FY23?

## E. NOTES-BASED RED FLAGS

- Multi-year, multi-bank, multi-quarter discrepancies between books and stock/book-debt statements filed with lenders for drawing power (up to ₹70.97 Cr in a single quarter).
- ₹8.73 Cr of company-book land with unregistered title held personally by promoter-MDs, simultaneously pledged as company debt collateral.
- MSME dues unpaid 3+ years with accrued interest now exceeding principal, and an admitted incomplete MSME-creditor identification process.
- Standalone and consolidated operating cash flow negative in FY25 despite PBT nearly tripling; growth funded by equity raise and borrowing, not operations — directly contradicts the "improving" DSCR/current-ratio narrative in the company's own ratios note.
- Debt Service Coverage Ratio below 1.0x in every disclosed year (FY23–FY25).
- Section 185 Companies Act violation (loans to related parties, FY23–FY24), remediated only by pre-audit repayment.
- Extensive prior-period restatement (gratuity, CSR, interest, tax) with FY23 profit revised up 226% via a single ₹2.26 Cr interest reversal, and FY23 net worth simultaneously revised down.
- Unregistered ROC charges on ₹51.17 Cr and ₹1.43 Cr borrowings, past the statutory filing period.
- CSR non-compliance spanning multiple years pre-dating the restated window, cleared via a lump catch-up payment timed with the IPO.
- Recurring "inadvertently missed" language across at least six independent statutory/compliance and lender-reporting notes — a cross-note systemic-control-weakness pattern, not isolated incidents.
- Related-party receivable (Raghavendra Industries) disproportionate to transaction volume (3.7x annual sales), with zero doubtful-debt provisioning anywhere in the filing.

## F. ONE-LINE NOTES VERDICT

The notes reveal concerning accounting practices. Key concern: operating cash flow turned negative in FY25 despite profit growth, against a backdrop of six independent, recurring "inadvertently missed" statutory and lender-reporting failures (MSME, CSR, ROC charges, bank stock statements) and an unregistered land title pledged as collateral. Key strength: revenue recognition itself is conservative and unremarkable, and the restated financials, however extensive the corrections, appear to have been fully reconciled and disclosed rather than concealed. Overall accounting quality: 3/10.

---

```yaml
stage: B02-notes
company: "544516"
run_date: "2026-07-15"
model: claude-sonnet-5
status: complete
input_gaps:
  - "Source document is the IPO Prospectus (16-Sep-2025), not a conventional Annual Report; no separate Annual Report or DRHP exists in the file set"
  - "Consolidated restated financials cover FY25 only (subsidiary incorporated 11-June-2024); standalone covers FY23-FY25"
  - "Credit rating ABSENT"
  - "External research coverage ABSENT"
flags:
  - {type: FLAG-CASH, reason: "Standalone and consolidated operating cash flow turned negative in FY25 (₹(4.43) Cr standalone, ₹(4.45) Cr consolidated) despite PBT nearly tripling since FY23; trade receivables >6-months share deteriorated 15.95% to 23.38% over FY23-FY25 with zero doubtful-debt provisioning in any year; FY25 growth was funded by the equity raise and borrowing, not operating cash generation"}
accounting_quality: 3        # /10
pass_2_empty: false
pass_3_empty: false
top_findings:                # max 15
  - {rank: 1, finding: "Standalone operating cash flow turned negative in FY25 (₹(4.43) Cr) despite PBT nearly tripling to ₹34.98 Cr since FY23; contradicts the improving DSCR/current-ratio narrative in the company's own ratios note", note_ref: "Annexure III (Cash Flow), SFS p.7 / CFS p.7", rating: "🔴🔴", why: "Profit growth is not converting to cash; core FLAG-CASH evidence"}
  - {rank: 2, finding: "Multi-year, multi-bank, multi-quarter discrepancies between company books and stock/book-debt statements filed with lenders for drawing power, up to ₹70.97 Cr in a single quarter", note_ref: "Additional Regulatory Info table, SFS p.40-42 / CFS p.38", rating: "🔴🔴", why: "Systemic, recurring misreporting to secured lenders; raises internal-controls reliability questions"}
  - {rank: 3, finding: "₹8.73 Cr of company-book land has unregistered title held personally by promoter-MDs (sale agreement FY2021-22, unregistered 4+ years later), pledged as bank collateral for company debt", note_ref: "Annexure XLV(i), SFS p.39; cross-ref XIV/XV, XXXII", rating: "🔴🔴", why: "Governance and asset-recoverability risk on a material asset entangled with promoter personal holdings"}
  - {rank: 4, finding: "MSME dues: same ₹0.35 Cr principal unpaid 3+ years, accrued interest (₹0.39 Cr) now exceeds principal, company admits incomplete MSME-creditor identification process", note_ref: "Annexure XI/XXXIII/XLIV, SFS p.18,32,39", rating: "🔴🔴", why: "Statutory violation compounding, with admitted disclosure gap"}
  - {rank: 5, finding: "Debt Service Coverage Ratio below 1.0x in all three disclosed years (0.21x/0.42x/0.68x); current ratio below 1.0x in FY22-FY23 too", note_ref: "Significant Accounting Ratios, SFS p.44", rating: "🔴", why: "Operating cash flow has never covered debt service; liquidity stress predates restated window"}
  - {rank: 6, finding: "Extensive prior-period restatement across gratuity, CSR, interest, and tax, retrospectively corrected FY23-FY25 via opening-reserves adjustment", note_ref: "Annexure IV Notes 3 & 4, SFS p.13-14 / CFS p.12-13", rating: "🔴", why: "Breadth and repetition point to a weak pre-IPO financial-control environment"}
  - {rank: 7, finding: "FY23 restated profit revised up 226% (₹0.46 Cr to ₹1.49 Cr) via a single ₹2.26 Cr interest reversal; FY23 restated net worth simultaneously revised down ₹0.81 Cr", note_ref: "Annexure IV Note 3 & 4, SFS p.13-14", rating: "🔴", why: "FY23 is the base year for all growth-rate calcs and its own figures required near-tripling correction"}
  - {rank: 8, finding: "Section 185 Companies Act violation (loans to related parties) in FY23 and FY24, remediated only by repayment before audit date", note_ref: "Auditor's Report item 8(iv), CFS p.2 / SFS p.3", rating: "🔴", why: "Statutory violation remediated on an IPO-driven timeline, not through ongoing compliance"}
  - {rank: 9, finding: "Historical reliance on very high-cost debt (24% p.a. ICL secured by promoters' personal land; 16-16.5% p.a. unsecured loans), all repaid to nil by FY25", note_ref: "Annexure XXXII, SFS p.29-31", rating: "🔴", why: "Strong liquidity-stress signal for FY23/FY24"}
  - {rank: 10, finding: "CSR non-compliance predates the restated window (opening FY23 liability already ₹0.70 Cr), cleared via a lump ₹1.08 Cr catch-up payment in FY25 timed with the IPO", note_ref: "Annexure XLVI, SFS p.45", rating: "🔴", why: "Multi-year statutory non-compliance remediated only under IPO scrutiny"}
  - {rank: 11, finding: "Trade receivables >6 months rising steadily (15.95% to 23.38%, FY23-FY25) with zero doubtful-debt provisioning across all three years", note_ref: "Annexure XIX/XXXIV, SFS p.20,33", rating: "🔴", why: "Provisioning adequacy concern under an IGAAP framework with no formal ECL policy; feeds FLAG-CASH"}
  - {rank: 12, finding: "Unregistered ROC charges on ₹51.17 Cr (Axis Bank) and ₹1.43 Cr (BMW India Financial) borrowings, past statutory filing period", note_ref: "Annexure XLV item x, SFS p.43", rating: "🔴", why: "Statutory charge-registration non-compliance on the company's two largest secured facilities"}
  - {rank: 13, finding: "Recurring inadvertently-missed language spans at least six independent statutory/lender-reporting notes (gratuity, CSR, TDS interest, MSME interest, ROC charges, bank stock statements)", note_ref: "Cross-refs Annexures IV, XLIV, XLV, XLVI, Additional Regulatory Info", rating: "🔴", why: "A cross-note pattern suggesting systemic control weakness, not isolated incidents"}
  - {rank: 14, finding: "Related-party receivable from Raghavendra Industries (₹7.46 Cr FY25) is 3.7x that party's annual purchase volume (₹2.01 Cr) and has grown every year since FY23", note_ref: "Annexure XXXV; cross-ref XIX/XXXIV", rating: "🔴", why: "Collectability and arm's-length-terms question on a related party"}
  - {rank: 15, finding: "Consolidated FY25 operating cash flow also negative (₹(4.45) Cr), confirming the standalone cash-flow weakness is not an isolated-entity artifact", note_ref: "Annexure III, CFS p.7", rating: "🔴", why: "Group-level cash generation is equally weak; growth funded by fresh equity and short-term borrowing"}
red_flags:
  - "Multi-year, multi-bank, multi-quarter stock/book-debt reporting discrepancies with lenders, up to ₹70.97 Cr in one quarter"
  - "Unregistered land title (₹8.73 Cr) held personally by promoter-MDs, pledged as company debt collateral"
  - "MSME dues unpaid 3+ years; accrued interest exceeds principal; admittedly incomplete MSME identification"
  - "Standalone and consolidated operating cash flow negative in FY25 despite PBT growth; contradicts the company's own improving-ratios narrative"
  - "DSCR below 1.0x in every disclosed year (FY23-FY25)"
  - "Section 185 Companies Act violation (related-party loans, FY23-FY24)"
  - "Extensive prior-period restatement; FY23 profit revised up 226%, FY23 net worth revised down"
  - "Unregistered ROC charges on ₹51.17 Cr and ₹1.43 Cr borrowings"
  - "Multi-year CSR non-compliance cleared via a lump catch-up payment timed with the IPO"
  - "Recurring inadvertently-missed language across six independent statutory/lender-reporting notes"
  - "Related-party receivable disproportionate to transaction volume (3.7x annual sales), zero doubtful-debt provisioning throughout"
questions_for_mgmt:
  - "What remediation and controls prevent recurrence of the stock/book-debt reporting discrepancies to Axis Bank and Union Bank, given these occurred every quarter across three years with differences up to ₹70.97 Cr?"
  - "What is the status and timeline for registering the ₹8.73 Cr Nehru Nagar land transfer from the promoter-MDs' personal names to the company, and what is the contingency if registration is not completed while it remains pledged collateral?"
  - "Given standalone OCF turned negative in FY25 despite PBT growth, what working-capital actions are planned to convert profit growth into cash, and was FY25 growth structurally dependent on the equity raise?"
  - "Why is the gratuity actuarial attrition assumption held flat at 54% for three consecutive years, and is this supportable against actual attrition experience?"
  - "What is the collectability assessment and credit-term basis for the ₹7.46 Cr receivable from related party Raghavendra Industries, 3.7x that party's FY25 purchase volume?"
receivables_trend: "deteriorating - >6 months share of standalone trade receivables rose from 15.95% (FY23) to 17.85% (FY24) to 23.38% (FY25), with the 1-2yr ageing bucket volatile (₹5.31 Cr FY23, ₹13.79 Cr FY24, ₹9.56 Cr FY25) and zero doubtful-debt provisioning throughout; cash flow statement shows ₹52.94 Cr (FY24) and ₹26.05 Cr (FY25) absorbed into receivables, driving FY25 operating cash flow negative"
restatements_found:
  - "Gratuity provision not previously booked, retrospectively corrected FY23-FY25 (Annexure IV Note 3/4)"
  - "CSR expenditure liability not previously booked, retrospectively corrected (Annexure IV Note 3/4, Annexure XLVI)"
  - "Interest on borrowings incorrectly computed/reversed, most material in FY23 (₹2.26 Cr reversal driving 226% profit restatement)"
  - "Interest on late statutory dues (TDS) not previously booked, retrospectively corrected"
  - "Interest on delayed MSME payments not previously booked, retrospectively corrected"
  - "Income tax and deferred tax incorrectly computed in prior years, retrospectively corrected"
  - "FY23 net worth restated ₹0.81 Cr lower than originally audited, implying negative adjustments to pre-FY23 opening reserves beyond the FY23-specific corrections"
going_concern_language: "NONE - both auditor's reports (CFS p.2, SFS p.2) are clean/unqualified with no going-concern qualification or emphasis-of-matter paragraph found anywhere in the annexures reviewed"
```
