# STAGE 2 — NOTES TO FINANCIAL STATEMENTS, PASS 3 (PATTERN PASS + CONSOLIDATION)
KROSS | run date 2026-09-27 | source: Annual_Report_2026 (FY2025-26 standalone),
backward check Annual_Report_2025 (FY2024-25). AR reports in INR Mn; this report
states the source Mn figure and the Rs Cr conversion (divide by 10) alongside
every number. Page anchors below use the form AR PDF p.N (printed p.X), per
the page map in the AR .txt (each half of the landscape spread carries a
"[page N | left half | printed p.X]" marker); prior passes' anchors are
restated in this form here.

---

## PASS 3: PATTERN RE-READ

Targeted re-read for contradictions, numbers that do not tie to the main
statements, deliberately thin disclosure, restatements, subsequent events,
and going-concern language.

- **Restatement check**: Note 62 (AR PDF p.84 (printed p.163)) states
  explicitly: "Previous year figures have been regrouped/ rearranged/
  reclassified wherever necessary. Further, there are no material
  regrouping/ reclassifications during the year." Confirmed by a full-text
  search of the AR for "restat"/"reclassif": the only reclassification
  language found is this boilerplate policy statement and Note 62 itself.
  No restatement of a prior-year number was found anywhere in the note set.
- **Contradiction found and confirmed on re-read**: Note 36's Fair Value
  Measurement table (AR PDF p.78 (printed p.150)) is headed "As at March 31,
  2025" and "As at March 31, 2024," but the two figures under those headers
  (Rs 2,323.04 Mn and Rs 2,786.97 Mn) are the actual FY26 and FY25 totals —
  confirmed by matching them to Note 39(a) credit risk (AR PDF p.79 (printed
  p.153)), which labels the identical numbers "Financial Year 2025-26" and
  "Financial Year 2024-25." This is a genuine internal contradiction between
  two notes describing the same balances, not a rounding or presentation
  choice.
- **Second contradiction, same class**: Note 52's own stated ROE formula
  ("Net Profit after tax - preference dividend / Average total equity") does
  not reconcile to the disclosed ROE percentages (171.18% FY26, 161.98% FY25,
  221.26% FY24, AR PDF p.82-83 (printed p.159-160)); the disclosed figures
  instead reconcile exactly to PAT / average paid-up share capital. The
  Debt-Equity ratio in the SAME table correctly uses total equity. This is a
  documented, three-year-recurring internal inconsistency (formula stated vs
  formula applied) within a single statutory note, distinct in kind from the
  Note 36 date-header contradiction but of the same species: the notes do
  not always say what they compute.
- **Vague-versus-detailed disclosure asymmetry**: Note 53's bank-return
  reconciliation (AR PDF p.83-84 (printed p.161-162)) gives a specific,
  mechanical explanation for the Stock line ("net figure exclusive of GST")
  but a generic, repeated explanation for the Sundry Debtors line
  ("period-end/year-end adjustments accounted for post submission") across
  5 of 8 quarters shown, with a third explanation pattern ("provisional
  books... elimination of gross margin on stock done on finalization")
  appearing only in the two quarters nearest each year-end. Three different
  explanation registers in one note, with the least specific one applied to
  the largest and most persistent variance (Sundry Debtors), is the kind of
  disclosure asymmetry the pattern pass is built to catch. It does not by
  itself evidence receivables manipulation.
- **Document-quality pattern**: two independent, unrelated year/date defects
  found across the note set (Note 16(B) term-loan maturities printed
  "1930"/"1931" instead of "2030"/"2031", AR PDF p.72-73 (printed
  p.138-139); Note 36's mislabelled fair-value-table headers above). Neither
  changes a number used in this pipeline, but two separate date-labelling
  errors in one 62-note set, on top of the ROE-formula error and the Note 53
  explanation asymmetry, together read as a broader disclosure-quality
  pattern rather than four unrelated one-offs.
- **Subsequent events**: financial statements approved May 12, 2026 (Note
  61, AR PDF p.84 (printed p.163)); no separate subsequent-events note
  disclosing anything after that date. NOT FOUND IN DOCUMENT.
- **Going concern**: NONE found anywhere in the notes, including Note 3
  basis of preparation, the auditor's report cross-reference, and Note 61.

No further material new findings emerged from the pattern re-read beyond
what is folded into the consolidated table below; Pass 3 is not empty
because it produced the four items above (two contradictions confirmed and
sharpened, one disclosure-asymmetry characterisation, one document-quality
synthesis), but no new numeric finding outside the consolidated table.

---

## CONSOLIDATED NOTES ANALYSIS, ALL THREE PASSES COMBINED

### A. TOP 15 MOST SIGNIFICANT FINDINGS

| Rank | Finding | Note # | Rating | Why it matters |
|---|---|---|---|---|
| 1 | Note 52's Return on Equity Ratio (171.18% FY26, 161.98% FY25, 221.26% FY24) is computed on average paid-up SHARE CAPITAL only (Rs 322.55 Mn unchanged), not average total equity as the note's own stated formula requires; true ROE on total equity is ~11.95% FY26. The error repeats across all three disclosed years; the Debt-Equity ratio in the same table correctly uses total equity, so this is an internal inconsistency, not a policy choice. | Note 52, AR PDF p.82-83 (printed p.159-160) | 🔴 Red Flag | A ~14x overstatement of a headline profitability ratio, repeated three years running in a statutory disclosure, is a disclosure-competence flag. Any downstream valuation or FTTCP work must use the recomputed ~11.95% ROE, never the printed 171.18%. |
| 2 | Bills discounted with recourse (ICICI Bank, DBS Bank) rose 7.6% YoY to Rs 349.00 Mn (Rs 34.90 Cr), now 88% of total contingent liabilities and 7.13% of net worth; this receivables financing sits off the Note 11 trade receivables balance while credit risk is retained by the company. | Note 34, AR PDF p.76-77 (printed p.146-147) | 🟡 Watch | Understates the true credit extended to customers within the Note 11 balance; directly relevant to LBF2 cash-conversion analysis: part of apparent "cash collected" is borrowed against uncollected bills, with recourse risk retained. |
| 3 | Related-party sale to Bull Auto Parts, the proprietorship of Kunal Rai (Whole Time Director-Finance & CFO): Rs 93.54 Mn (Rs 9.354 Cr) FY26, 1.39% of revenue, outstanding receivable Rs 49.38 Mn (Rs 4.938 Cr) at year end. No arm's-length pricing comparison disclosed anywhere in the notes. | Note 51, AR PDF p.82 (printed p.158) | 🟡 Watch | A sitting CFO's proprietorship as a recurring sale-side counterparty is a governance structure Role 2 Section 3G and LBF4 must weigh; the note evidences the relationship and the balance, not the pricing terms. |
| 4 | Trade receivables ageing: the 6-month-to-1-year bucket grew 45.5% (Rs 137.63 Mn to Rs 200.28 Mn) against 8.5% revenue growth; the >6-month share of gross receivables rose from 8.9% to 11.0%. ECL allowance held flat at Rs 14.35 Mn (Rs 1.435 Cr) for two years running. Receivables turnover fell 7.67x (FY24) to 4.25x (FY25) to 3.55x (FY26), a company-disclosed three-year deterioration. | Note 11, AR PDF p.69 (printed p.132-133); Note 52, AR PDF p.82-83 (printed p.159-160) | 🟡 Watch | Feeds FLAG-CASH. A rising aged-receivables share with an unchanged provision, corroborated by the company's own turnover-ratio trend and its own remarks column (Net Capital Turnover Ratio commentary, finding 11 below), is a consistent, multi-source cash-conversion deterioration signal. |
| 5 | Note 53's bank-return reconciliation of Sundry Debtors versus books shows a one-directional gap (bank return understates book) of Rs 150-406 Mn (Rs 15-41 Cr) in 5 of 8 disclosed quarters, uniformly explained as "period-end/year-end adjustments accounted for post submission," reversing sign in the two quarters nearest FY26 year-end. The Stock line in the same note carries a distinct, mechanical explanation ("net figure exclusive of GST"). | Note 53, AR PDF p.83-84 (printed p.161-162) | 🟡 Watch | An independent, bank-facing cross-check on the receivables balance that management itself files. The generic explanation attached to the largest, most persistent variance (Debtors) versus the specific explanation attached to Stock is a disclosure-quality asymmetry worth a direct management question; it does not on its own evidence manipulation. |
| 6 | Cash and cash equivalents fell from Rs 828.43 Mn to Rs 44.40 Mn (Rs 82.84 Cr to Rs 4.44 Cr); "other bank balances" (locked/collateral deposits) rose from Rs 14.35 Mn to Rs 192.95 Mn (Rs 1.44 Cr to Rs 19.30 Cr), reflecting the capex ramp and full IPO-proceeds deployment. | Note 12-13, AR PDF p.70 (printed p.134) | 🟡 Watch | Liquid, freely available cash is now thin, raising the importance of the operating cash-flow/working-capital trend for near-term funding headroom, alongside the FY27 finance-cost step-up flagged in finding 12. |
| 7 | Gratuity plan funded only 24.1% (plan assets Rs 18.32 Mn / Rs 1.832 Cr vs obligation Rs 75.87 Mn / Rs 7.587 Cr); the company states explicitly it pays gratuity from its own funds as amounts fall due rather than fully funding the plan. Net liability Rs 57.55 Mn (Rs 5.755 Cr). | Note 35, AR PDF p.76-78 (printed p.147-150) | 🟡 Watch | A disclosed, recurring, modest-size cash-timing risk; small in absolute terms but a governance-of-employee-obligations data point, and a template a verifier can re-check against peers. |
| 8 | Warranty provisioning nearly doubled YoY (Rs 24.24 Mn to Rs 29.89 Mn / Rs 2.424 Cr to Rs 2.989 Cr) against 8.5% revenue growth; warranty cost as % of revenue rose from 0.39% to 0.44%. | Note 33/35, AR PDF p.76-78 (printed p.147-150) | 🟡 Watch | Could indicate product-quality drift on newer product lines (Tipping Jacks, V-Rod, Torsion Assemblies) or a growing installed base; a direct management question, not yet resolved by the notes alone. |
| 9 | Trade payable days extended across three years: payables turnover 12.85x (FY24) -> 8.88x (FY25) -> 8.58x (FY26), implying payable days stretching from ~28 to ~43 days, even as MSME overdue-interest fell (Rs 1.92 Mn to Rs 0.71 Mn). The DTA line "Disallowance under 43(B)(h)" rose 51.6% (Rs 3.84 Mn to Rs 5.82 Mn), an independent tax-note corroboration of growing unpaid-beyond-window MSME dues. | Note 20/40/52, AR PDF p.74/81/82-83 (printed p.142/156/159-160); Note 19, AR PDF p.73 (printed p.141) | 🟡 Watch | A working-capital-funding-via-suppliers signal running opposite to a "getting better with suppliers" narrative; corroborated from an independent statutory tax disclosure (43B(h) DTA), not just the payables note itself. Read alongside finding 4 as a combined WC-days story. |
| 10 | The FY24 opening debt position, disclosed for the first time in Note 38's reconciliation, was Rs 1,171.04 Mn (Rs 117.104 Cr) total borrowings, against Rs 326.62 Mn (Rs 32.662 Cr) at FY25 close, a 72.1% one-year deleveraging funded by the Rs 900 Mn (Rs 90 Cr) IPO debt-repayment tranche. Note 52's own remarks column independently states the Debt-Equity improvement (0.95 to 0.12) and Current Ratio improvement (1.37 to 3.21) were "due to repayment of borrowings from IPO Proceeds." | Note 38, AR PDF p.79 (printed p.152); Note 52, AR PDF p.82-83 (printed p.159-160) | 🟡 Watch | The current low-leverage picture (debt-equity 0.12) is IPO-proceeds-driven, not the product of structural organic deleveraging; relevant context before crediting the low-leverage level as a durable quality improvement. |
| 11 | Note 52's own remarks column: Net Capital Turnover Ratio declined 12.02x (FY24) to 3.78x (FY25) to 2.59x (FY26), with the company's own stated reason "Increase in revenue along with increase in working capital following lower current liabilities" — a management-authored acknowledgement of rising working-capital intensity. | Note 52, AR PDF p.82-83 (printed p.159-160) | 🟡 Watch | Independently corroborates the FLAG-CASH receivables/payables findings (4 and 9) from the company's own analytical-ratio commentary, not from an outside recomputation. |
| 12 | Finance costs fell 34.3% (Rs 122.86 Mn to Rs 80.70 Mn) in a year when period-end borrowings rose 60.3% (Rs 326.62 Mn to Rs 523.65 Mn), because the FY26 borrowing increase (HDFC Repo+3.25% facility) was drawn progressively through the year rather than outstanding for a full 12 months, on top of an already-low FY25 opening base. | Note 29, AR PDF p.75 (printed p.144); Note 16/38, AR PDF p.71/79 (printed p.136/152) | 🟡 Watch | FY27 finance costs are likely to step up materially on a full-year basis of debt only partly outstanding during FY26, independent of any rate move; a modelling input for Role 1/FTTCP margin bridges. |
| 13 | GST receivables rose 124.6% (Rs 30.16 Mn to Rs 67.75 Mn) and advances to suppliers rose 50.3% (Rs 139.10 Mn to Rs 209.11 Mn), both inside Note 9's "Total other current assets" line (+59.2% overall), both well ahead of 8.5% revenue growth. | Note 9, AR PDF p.69-70 (printed p.132) | 🟡 Watch | A working-capital-adjacent build on the capex ramp (input-tax credit timing is the plausible explanation for the GST line, but the notes give no further breakdown to confirm it); a data point for the WC/cash-conversion read, not a standalone concern on the evidence given. |
| 14 | Two independent, unrelated date/year-labelling defects found in the statutory notes: Note 16(B) term-loan maturities printed "1930"/"1931" instead of "2030"/"2031"; Note 36's Financial Instruments and Fair Value tables headed "As at March 31, 2025/2024" over figures that are actually the FY26/FY25 numbers (confirmed by cross-reference to Note 39(a), which correctly labels the identical figures). Neither changes a number used in this pipeline. | Note 16, AR PDF p.72-73 (printed p.138-139); Note 36, AR PDF p.78 (printed p.150) | 🟡 Watch | Two separate document-quality defects, on top of the three-year-recurring ROE formula error (finding 1) and the Note 53 explanation asymmetry (finding 5), together read as a broader disclosure-quality pattern worth naming to the auditor/company, though none individually is a valuation input error. |
| 15 | IPO net proceeds (Rs 2,369.19 Mn / Rs 236.919 Cr) fully and specifically utilised: capex Rs 700.00 Mn (Rs 70.00 Cr), debt repayment Rs 900.00 Mn (Rs 90.00 Cr), working capital Rs 300.00 Mn (Rs 30.00 Cr), general corporate purposes Rs 469.19 Mn (Rs 46.919 Cr); nil balance remaining. | Note 54, AR PDF p.84 (printed p.163) | 🟢 Clean | Confirms LBF3 with a specific, auditable utilisation table (net of Rs 13.08 Cr offer expenses against the Rs 250 Cr gross COMPANY MEMORY figure); no diversion from the prospectus-stated use of proceeds is evidenced. |

### B. ACCOUNTING QUALITY SCORE

| Dimension | Score (1-10) | Basis |
|---|---|---|
| Revenue recognition conservatism | 8 | Single operating segment, no contract-asset gymnastics, no top-line aggressiveness found; only issue is an internal wording inconsistency in the segment-note label ("logistics and allied services" vs the manufacturing business description in Note 1), a template artefact, not a recognition issue. |
| Expense capitalisation honesty | 7 | Capex/CWIP additions tie to the disclosed capex programme; CWIP ageing shows no stalled projects; no capitalisation-threshold changes; the qualitative-only override of Schedule II depreciation lives (Note 3.7) is unsized and caps this below a clean 8-9. |
| Provisioning adequacy | 5 | ECL held flat against a rising aged-receivables share (finding 4); warranty provisioning nearly doubled against flat revenue growth (finding 8); gratuity plan only 24.1% funded (finding 7). None individually severe, but three separate under-provisioning-adjacent signals in one AR pulls this down. |
| RPT fairness | 5 | CFO's proprietorship as a recurring sale-side counterparty with no disclosed arm's-length comparison (finding 3); promoter unsecured loans interest-free; no evidence of overtly unfair terms, but no evidence of fair terms either. |
| Disclosure transparency | 4 | Note 52's ROE formula error (repeated 3 years), Note 36's mislabelled year headers, Note 16's date typos, and Note 53's asymmetric explanation registers are four separate disclosure-quality defects found across the note set, none individually large but cumulatively a below-average transparency read for a 62-note statutory set. |
| Consistency with prior years | 6 | The ROE-formula error itself is "consistent" (repeats identically for three years, i.e. never caught or corrected), which is a competence signal rather than a volatility signal; otherwise no restatements, no policy changes, no first-time-adoption surprises. |
| **OVERALL** | **6** | Moderate. No fraud indicator, no going-concern language, no goodwill games, clean tax reconciliation, and a fully-accounted IPO utilisation on the positive side; a repeated statutory-ratio computation error, a CFO-linked RPT with no pricing evidence, flat ECL against deteriorating ageing, and a cluster of smaller disclosure-quality defects on the negative side. |

### C. KEY RISKS FROM NOTES

| Risk | Severity | What to monitor | When it could hit |
|---|---|---|---|
| Receivables/cash-conversion deterioration (aged bucket growth, flat ECL, falling turnover ratio, company's own WC-intensity remark) | Medium | Note 11 ageing buckets and Note 52 turnover ratios each subsequent AR/quarter; any further ECL non-adjustment against a widening aged book | Visible at FY27 AR; earlier if quarterly disclosures surface it |
| Bills discounted with recourse rising toward net worth materiality (currently 7.13% of net worth) | Medium | Note 34 contingent liability balance and its % of net worth trend | Crystallises only if customers default on discounted bills; monitor growth rate meanwhile |
| CFO-linked related-party sale relationship (Bull Auto Parts) with no disclosed arm's-length pricing evidence | Medium (governance) | Any pricing-comparison disclosure in future filings; the receivable balance trend; any change in the volume/receivable trajectory | Ongoing; a governance overhang rather than a dated trigger |
| FY27 finance-cost step-up on a full-year basis of FY26's partly-drawn borrowing increase | Low-Medium | Note 29 finance costs and Note 16 borrowings in the FY27 AR/quarterlies against the FY26 base | FY27 results |
| Statutory-note computation/disclosure defects (ROE formula, Note 36 year headers, Note 16 date typos, Note 53 explanation asymmetry) recurring or expanding | Low (disclosure quality, not a cash/solvency risk) | Whether FY27's Note 52 corrects the ROE formula; whether new defects appear | FY27 AR |
| Underfunded gratuity plan (24.1% funded) | Low | Note 35 funded ratio trend; any acceleration of the cash-out pace | Ongoing, small absolute cash call |

### D. FIVE QUESTIONS FOR MANAGEMENT

1. Note 52's Return on Equity Ratio uses average paid-up share capital, not average total equity, across all three disclosed years (FY24-FY26), overstating ROE by roughly 14x versus the note's own stated formula. Will this be corrected in the FY27 AR, and was the discrepancy flagged to the statutory auditor?
2. What are the pricing terms for sales to Bull Auto Parts, the proprietorship of CFO Kunal Rai, and how do they compare with pricing to unrelated third-party customers of comparable size and credit profile?
3. Why has the ECL allowance on trade receivables been held flat at Rs 14.35 Mn (Rs 1.435 Cr) for two consecutive years while the greater-than-6-months aged bucket grew from 8.9% to 11.0% of gross receivables and the 6-month-to-1-year bucket grew 45.5%?
4. What is driving the near-doubling of warranty provisioning (Rs 24.24 Mn to Rs 29.89 Mn) against only 8.5% revenue growth: product-quality issues on the newer product lines (Tipping Jacks, V-Rod, Torsion Assemblies), or simply a growing installed base?
5. Bills discounted with recourse now stand at Rs 349.00 Mn (Rs 34.90 Cr), 88% of total contingent liabilities. What is the expected FY27 trajectory of this off-balance-sheet receivables financing, and is it related to the recurring bank-return-versus-book discrepancy on Sundry Debtors disclosed in Note 53?

### E. NOTES-BASED RED FLAGS

- **Earnings management**: no evidence found. No exceptional items smoothed, no goodwill impairment games, no revenue recognition aggression, no reserve-bypass entries, no undisclosed related-party loans beyond the interest-free promoter demand loans.
- **Aggressive accounting**: none found. Depreciation, DTA/DTL, gratuity actuarial assumptions, and inventory valuation policy all read as standard and unremarkable.
- **Undisclosed risk indicators**: the closest candidate is the Note 53 bank-return-versus-book Sundry Debtors gap, which is disclosed (not undisclosed) but explained in generic, repeated language across most of the quarters shown; this is a disclosure-quality concern, not an undisclosed risk, since the company itself files the reconciling table.
- **The one confirmed hard-number error**: Note 52's Return on Equity Ratio computation, wrong for three consecutive disclosed years, on a formula the note itself states correctly. This is the single finding in this analysis that crosses from "judgment call" or "watch item" into a demonstrable arithmetic/disclosure error.

### F. ONE-LINE NOTES VERDICT

The notes reveal moderate accounting practices with one confirmed disclosure error and several working-capital caution signals. Key concern: Note 52's Return on Equity Ratio is computed on the wrong denominator for three straight years (true ROE ~11.95% FY26, not the disclosed 171.18%), alongside a CFO-linked related-party sale with no arm's-length pricing evidence and a flat ECL allowance against deteriorating receivables ageing. Key strength: fully and specifically accounted IPO-proceeds utilisation, clean tax reconciliation, genuinely low period-end leverage (though IPO-driven, not organic), and no going-concern language or goodwill/impairment manipulation anywhere in the 62-note set. Overall accounting quality: 6/10.

END OF STAGE 2 (PASS 3 / CONSOLIDATED).
