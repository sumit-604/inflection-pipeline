# STAGE 2 — NOTES TO FINANCIAL STATEMENTS — PASS 3: PATTERN PASS + CONSOLIDATION
**Company:** Smruthi Organics Ltd (SMRUTHI) | **Run date:** 2026-07-09
**Source:** Annual Report FY2024-25 (36th AGM), full pattern re-read across Notes 1–48, Balance Sheet, Statement of P&L, Cash Flow Statement, Segment Note, Statement of Changes in Equity, Auditors' Report and CARO Annexures. Printed page = document page − 4 throughout the Financial Statements section (Notes, primary statements, Auditors' Report/CARO all carry this same offset per the printed page numbers visible on each page).
**Input gaps carried forward:** concalls absent (NO-CONCALL MODE), peer-concalls absent, investor presentation absent.

---

## PASS 3: PATTERN RE-READ

This pass did **not** re-walk the notes sequentially. It specifically hunted for: (a) notes that contradict each other, (b) numbers in the notes that do not match the main financial statements, (c) notes disclosed with deliberately thin detail relative to others, (d) prior-year restatements/reclassifications, (e) events after the balance sheet date that change the picture, (f) going-concern language anywhere in the document. Pass 1 and Pass 2 were both exceptionally thorough (48/48 notes, all CARO/Section 197(16) paragraphs, corporate governance report, Annexures I–III), so this pass concentrated on cross-statement arithmetic checks that a sequential note-by-note read does not naturally surface.

**Two material new findings emerged. The no-manufacturing guard is not invoked.**

### PATTERN FINDING 1 — 🟡 "Profit before tax" figure is inconsistent across three parts of the same annual report

- The **Statement of Profit and Loss** (p.47) reports Profit Before Tax (line V/VII, no exceptional items either year) = **₹490.00L** for FY25.
- The **Cash Flow Statement** (p.48) begins its indirect-method reconciliation with "**Profit before income tax**" = **₹511.02L** for FY25 — a figure ₹21.02L higher than the P&L's own PBT line.
- **Note 45, Segment Reporting** (p.89–90), section 3 "Profit Before Tax," sums API (₹912.04L) + Formulation (₹(73.00)L) + Unallocable (₹(328.03)L) = **₹511.02L** — the same non-P&L figure as the Cash Flow Statement, not the ₹490.00L actually reported as PBT in the Statement of Profit and Loss.
- The ₹21.02L gap is traceable: it equals exactly the pre-tax Other Comprehensive Income for the year (Note 27.1, p.78): Fair Value Change on Equity Investment ₹2.97L + Remeasurement Gain on Gratuity Plan Asset/Obligation ₹18.05L = ₹21.02L. Both OCI items are, by Ind AS 19/109 design, correctly routed **outside** the P&L's PBT line and into Other Comprehensive Income — the Statement of Profit and Loss's ₹490.00L PBT is the Ind-AS-correct figure.
- The Cash Flow Statement's non-cash adjustment line, labelled **"Fair Valuation (Gain) / Loss on Investments (21.02)"**, is itself mislabeled: the actual fair-value gain on the equity investment (Note 27.1) is only ₹2.97L. The ₹21.02L used in the cash flow reconciliation is the **combined** OCI pre-tax total (investment FV gain + gratuity remeasurement gain), netted through a single line that carries the wrong name. The final operating cash flow figure ties out correctly because the addition (in the "profit before income tax" starting point) and the subtraction (in the mislabeled line) offset each other — but a reader trying to trace "profit before tax" from the P&L into the Cash Flow Statement or the Segment Note cannot do so without independently reconstructing this ₹21.02L bridge, which is not explained or footnoted anywhere.
- This is a genuine, quantifiable inconsistency between three primary disclosures in the same annual report (P&L vs Cash Flow Statement vs Segment Note), not a rounding difference. It does not change reported PAT or cash flow, but it is a disclosure-integrity/quality-control gap: the same underlying "PBT" figure is presented three different ways with no reconciliation note, and the segment note in particular is not tied to the audited P&L's PBT line as it normally should be. (Note 27, 27.1 p.78; Statement of Profit and Loss p.47; Cash Flow Statement p.48; Note 45 p.89–90)

🟡 — disclosure transparency / financial-statement-preparation quality control.

### PATTERN FINDING 2 — 🟡 Bank stock-statement reconciliation gap is largest, and concentrated, in Trade Payables at fiscal year-end

Pass 1 flagged the CARO Annexure A(ii)(b) bank-stock-statement reconciliation only for **Inventory** (differences ≤ ₹9.07L across all four quarters, immaterial). A pattern re-read of the same Annexure A(ii)(b) table (p.40–41) shows the company also discloses quarterly reconciliations for **Trade Receivables** and **Trade Payables** submitted to SBI/Axis Bank against the working-capital facilities, and these show materially larger, and differently-timed, gaps:

| Quarter | Receivables gap (SBI/Axis, ₹L) | Payables gap (SBI/Axis, ₹L) |
|---|---|---|
| Jun-24 | (28.09) / (28.09) | +21.78 / +21.79 |
| Sep-24 | (34.20) / (33.67) | (43.39) / (43.16) |
| Dec-24 | +3.54 / +3.82 | (9.08) / (8.87) |
| **Mar-25** | (20.74) / (20.56) | **(135.31) / (134.82)** |

The Mar-25 (fiscal year-end) Trade Payables gap of **₹135.31L (SBI) / ₹134.82L (Axis)** is by far the single largest discrepancy in either table across all four quarters and both metrics — roughly **8.5% of the year-end reported Trade Payables balance of ₹1,599.18L** (Note 22, p.75), versus a maximum inventory-reconciliation gap of only ₹9.07L (0.3% of the ₹2,830.67L inventory balance) noted in Pass 1. The company attributes all such differences uniformly to "gross vs net presentation of receivables/payables" (Note 46(j), p.91), but does not explain why this specific gap widens roughly 3x at year-end and is concentrated in payables rather than receivables or inventory. This coincides with the already-flagged 44% YoY collapse in Trade Payables (₹2,864.14L → ₹1,599.18L, Pass 1 finding #10) and the large negative working-capital swing in the Cash Flow Statement (₹1,264.95L). Since these very bank stock-statements determine the company's secured drawing power on its CC facilities, a discrepancy of this magnitude at the reporting date — even if benign — is a legitimate follow-up item, not something the "gross vs net" explanation alone fully addresses given the quarter-to-quarter volatility in the gap's sign and size. (CARO Annexure A(ii)(b), p.40–41; Note 22, p.75; Note 46(j), p.91)

🟡 — disclosure transparency / working-capital-quality follow-up, additive detail to the already-flagged payables collapse.

No further material new findings emerged from the pattern re-read. No prior-year restatements were found — the Statement of Changes in Equity explicitly shows "Changes in Equity Share Capital due to prior period errors" = Nil for both FY24 and FY25 (p.50), and no reclassification note appears anywhere else. No going-concern qualification exists anywhere in the report (Auditors' Report CARO para 3(xix), p.43, and Directors' Responsibility Statement, p.16, both affirm going concern with no material uncertainty language).

---

═══════════════════════════════════════════════════════════
## CONSOLIDATED NOTES ANALYSIS, ALL THREE PASSES COMBINED
═══════════════════════════════════════════════════════════

## A. TOP 15 MOST SIGNIFICANT FINDINGS

| Rank | Finding | Note # | Rating | Why it matters |
|---|---|---|---|---|
| 1 | Audit trail (edit log) not verifiable throughout the year and confirmed **not enabled at database level** for EasyERP, one of two accounting systems; Directors' Report nonetheless calls the auditor's report "clean...no qualifications" | Note 48, p.97–98; Auditors' Report para 2(h)(vi), p.38–39 | 🔴 Red Flag | Statutory (Companies Act Rule 11(g)) compliance gap explicitly raised by the auditor; undermines confidence in the traceability of all financial records, and MD&A framing understates it |
| 2 | Managerial remuneration paid **in excess of the 11%-of-net-profit statutory cap** under Section 197/Schedule V, sustained only via special resolutions from the 33rd and 34th AGMs; combined family remuneration (₹413.29L) exceeds FY25 PAT (₹356.29L) | Auditors' Report Section 197(16) para, p.39; Note 39, p.81 | 🔴 Red Flag | A recurring, structural governance/RPT-fairness issue formally reported by the statutory auditor, not disclosed as such anywhere in the notes narrative or Directors' Report |
| 3 | Four mortgaged factory-collateral land parcels registered in the **Managing Director's personal name**, not the company's, for ~24 years; SBI released its charge on these very parcels in Feb-2025 | Note 46(m), p.91; Note 17, p.71; CARO Annexure A(i)(c), p.40 | 🔴 Red Flag | Long-standing related-party title/governance defect on operating collateral, directly connected to a real reduction in bank security cover this year |
| 4 | ECL provisioning on the >3-year, litigated receivable bucket (₹219.67L, incl. ₹216.15L legal-recovery case, unchanged 2 years) is only ~0.11% vs the company's stated 2.5%–7.5% policy band | Note 10, p.67; Note 3.3/3.19, p.52/60 | 🔴 Red Flag | Material internal inconsistency between stated ECL policy and actual provisioning on the single highest-risk receivable bucket; feeds FLAG-CASH |
| 5 | Gratuity plan only 45.6% funded (DBO ₹559.94L vs plan assets ₹255.44L); LIC contribution jumped from ₹0.79L to ₹53.43L this year, with FY26 contribution projected at ₹357.09L | Note 41, p.84–86 | 🔴 Red Flag | Materially underfunded defined-benefit plan with a large, unexplained prospective cash-flow call for FY26 |
| 6 | Top-2 customer concentration roughly doubled to 27.5% of net revenue (vs top-1 at 11.4% last year), alongside fully unhedged export receivables | Note 26/45, p.77/90; Note 47, p.94 | 🟡 Watch | Growing concentration risk compounded by unhedged FX exposure on the same export book |
| 7 | Debt-financed capex weakened credit metrics: total borrowings +43.5% YoY; Debt-Equity worsened 38.4%; DSCR nearly halved (-58.3%, 3.01x vs 7.21x) | Note 17/21/44/47, p.71/74/88/94 | 🟡 Watch | Magnitude of DSCR deterioration warrants monitoring even though company-explained by term-loan drawdown |
| 8 | Forged/altered cheque litigation ongoing since 2020 (₹1.42L altered to ₹4.42L), fully provided but unresolved 5+ years | Note 46(o), p.92; Note 8, p.66 | 🔴 Red Flag | Indicative of a historical payment/cheque-issuance control weakness that remains legally unresolved |
| 9 | Significant, growing related-party job-work/remuneration flows to the promoter family (₹443.96L, ≈3.5% of revenue); receivable from MD's wife's proprietorship up 161% YoY; Axis facilities personally guaranteed by the MD | Note 39, p.81–82; Note 17/21, p.71/74 | 🟡 Watch | Concentration of financial flows and personal guarantees within one family, not flagged as "material RPT" by the company |
| 10 | Stated FX hedging policy is not executed: both export receivables (₹1,315.88L) and import payables (₹635.86L) remain fully unhedged in both years | Note 3.4/47, p.53/94 | 🟡 Watch | Disclosed policy-vs-practice inconsistency on currency risk management |
| 11 | Trade payables collapsed 44% YoY (₹2,864.14L → ₹1,599.18L), a large negative working-capital swing, alongside a first-time appearance of delayed-MSME-payment interest | Note 22, p.75; Cash Flow Statement, p.48 | 🟡 Watch | Significant cash-flow drag from working capital; first MSME-delay interest disclosure signals a payment-timing shift |
| 12 | "Profit before tax" is presented as three different figures across the P&L (₹490.00L), Cash Flow Statement (₹511.02L) and Segment Note (₹511.02L), with the ₹21.02L gap (= pre-tax OCI items) unreconciled and a mislabeled cash-flow line | P&L p.47; Cash Flow Statement p.48; Note 45, p.89–90; Note 27.1, p.78 | 🟡 Watch | Cross-statement numerical inconsistency; disclosure/preparation quality-control gap (Pass 3 pattern finding) |
| 13 | Bank stock-statement reconciliation gap for Trade Payables peaks at fiscal year-end (₹135.31L/₹134.82L, ~8.5% of the reported balance) — far larger than the equivalent Inventory or Receivables gaps in any quarter | CARO Annexure A(ii)(b), p.40–41; Note 46(j), p.91 | 🟡 Watch | Coincides with, and adds quantitative texture to, the already-flagged payables collapse; affects secured drawing-power calculations (Pass 3 pattern finding) |
| 14 | Mrs. Eaga Vaishnavi (MD's wife) is the company's **second-largest individual shareholder at 15.27%**, while simultaneously the proprietor of the RPT job-work vendor (fees +15.4% YoY, receivable +161% YoY) | Note 15(d), p.69; Note 39, p.81–82 | 🟡 Watch | Sharpens the RPT-fairness picture: the same family member is both a top-2 equity holder and a growing RPT counterparty |
| 15 | MD's remuneration is **63.55x** median employee remuneration; JMD's is 42.37x | Directors' Report Annexure III, p.23 | 🟡 Watch | Concrete quantification of internal pay disparity underlying the broader family-remuneration theme |

---

## B. ACCOUNTING QUALITY SCORE (1–10)

| Dimension | Score /10 | Basis |
|---|---|---|
| Revenue recognition conservatism | 8 | Standard point-in-time recognition on dispatch, 60–90 day credit terms, no aggressive judgment; formulation-segment returns fell sharply (-79%), a genuine improvement, not manufactured |
| Expense capitalisation honesty | 6 | Borrowing cost (₹13.15L), gratuity (₹3.16L) and leave encashment (₹2.04L) capitalised to PPE — disclosed, but payroll-cost capitalisation to capital projects is a practice worth monitoring for consistency |
| Provisioning adequacy | 3 | ECL on the highest-risk receivable bucket is ~0.11% vs the company's own 2.5–7.5% policy band (Finding 4); gratuity plan only 45.6% funded (Finding 5); both are direct, quantifiable inconsistencies between policy and practice |
| RPT fairness | 3 | Managerial remuneration structurally exceeds the statutory 11% cap (Finding 2); family remuneration ≈3.5% of revenue and growing; MD's wife is both top-2 shareholder and RPT vendor (Finding 14); company states "no material RPT" despite this concentration |
| Disclosure transparency | 5 | Strong disclosure in most areas (full ageing schedules, actuarial sensitivity tables, fair value hierarchy) offset by: audit trail exception understated in Directors' Report, PBT presented three different ways with no reconciliation (Finding 12), title deed and personal guarantee disclosed only in fine print of Note 46(m) and CARO |
| Consistency with prior years | 6 | No restatements or reclassifications; consistent accounting policies year-on-year; but credit metrics (DSCR, gearing) deteriorated meaningfully and working capital swung sharply |
| **OVERALL** | **5** | A mix of genuinely clean, conservative revenue recognition and good actuarial/fair-value disclosure quality, set against multiple statutory-auditor-flagged compliance gaps (audit trail, remuneration cap), a real ECL policy breach on the highest-risk receivable bucket, and a governance-adjacent title/personal-guarantee entanglement. Weighted toward the more severe findings rather than a simple average of the six dimensions. |

---

## C. KEY RISKS FROM NOTES

| Risk | Severity | What to monitor | When it could hit |
|---|---|---|---|
| Audit trail / database-level control gap in EasyERP | High | Whether database-level audit trail gets enabled in FY26; any subsequent auditor comment on tampering | Next annual audit (FY26) or if a specific tampering issue surfaces |
| Managerial remuneration structurally above the 11% statutory cap | Medium-High | Whether fresh special resolutions are needed under the new FY25–28/31 appointment terms; any RoC/SEBI query | At future AGMs, or if profitability declines further, tightening the compliance math |
| Title deed defect on mortgaged land held in MD's personal name | Medium | Progress on rectification of the purchase-deed drafting error; any dispute on MD succession/estate | On MD succession, any change in the MD-company relationship, or renewed bank scrutiny |
| ECL under-provisioning on the >3-year litigated receivable bucket | Medium-High (cash) | Progress of the 4-party legal recovery case (₹216.15L, unchanged 2 years) | If courts rule against the company, forcing a full write-off not currently provisioned |
| Gratuity underfunding and FY26 contribution step-up (₹357.09L projected) | Medium | Actual FY26 cash contribution vs. plan; any further catch-up requirement | Within FY26, as the projected contribution materially exceeds recent-year funding levels |
| Customer concentration (27.5% top-2) with unhedged FX exposure | Medium | Retention of top customers; INR/USD and China-trade-policy moves | Any time, given no hedging is in place |
| DSCR deterioration (7.21x → 3.01x) amid rising debt | Medium | DSCR trend as term-loan amortization ramps through FY26–29 | Over FY26–27 as repayment obligations increase |
| Bank stock-statement reconciliation gap concentrated in Trade Payables at year-end | Low-Medium | Recurrence in FY26 quarterly submissions; any drawing-power impact | If the pattern recurs or widens in subsequent quarters |

---

## D. FIVE QUESTIONS FOR MANAGEMENT

1. Why does the ECL provision on the >3-year overdue, litigated receivable bucket (₹219.67L) sit at just ~0.11% versus the company's own stated 2.5%–7.5% policy band, and what is the realistic recovery timeline on the ₹216.15L legal case that has been unchanged for two consecutive years?
2. Given managerial remuneration has structurally exceeded the 11% Section 197 cap for multiple years (per the auditor's Section 197(16) paragraph) and combined family remuneration is near or above FY25 PAT, what is the Board's plan to bring remuneration within ordinary statutory limits, and will fresh shareholder waivers be required given the FY25–28/31 reappointment terms just approved?
3. What is the timeline and cost to rectify the title-deed defect on the four mortgaged land parcels held in the Managing Director's personal name for ~24 years, and what protections exist for the company and its lenders in the event of any change in the MD's personal circumstances?
4. What specifically triggered the gratuity funding catch-up (LIC contribution jumping from ₹0.79L in FY24 to ₹53.43L in FY25, with ₹357.09L projected for FY26) — was the plan under-provisioned historically, or has the actuarial/funding policy changed?
5. Can management reconcile the "Profit before income tax" figures used in the Cash Flow Statement and Segment Note (₹511.02L) against the ₹490.00L Profit Before Tax reported in the Statement of Profit and Loss, and clarify why the reconciling cash-flow line item is labelled "Fair Valuation (Gain)/Loss on Investments" when the ₹21.02L amount appears to represent total pre-tax OCI (investment fair value gain of ₹2.97L plus gratuity remeasurement gain of ₹18.05L) rather than just the investment fair value change?

---

## E. NOTES-BASED RED FLAGS

- **Earnings management / aggressive accounting indicator:** ECL provisioning on the highest-risk (>3-year, litigated) receivable bucket at ~0.11% against a stated 2.5–7.5% policy band is a quantifiable divergence between policy and practice that flatters both the balance sheet (net receivables) and the P&L (no incremental ECL charge) — the single most direct accounting-quality red flag in the notes.
- **Undisclosed risk indicator:** the title-deed defect (Note 46(m)) and the personal guarantee backing Axis Bank facilities (Note 17/21) are disclosed only within fine-print regulatory notes and CARO annexures, not surfaced in the Directors' Report or MD&A, despite directly affecting bank security cover on operating assets.
- **Aggressive accounting/disclosure-integrity indicator (new, Pass 3):** three different "profit before tax" figures appear across the P&L, Cash Flow Statement and Segment Note with no reconciliation footnote, and a cash-flow line is mislabeled relative to its actual composition.
- **Governance/quality-of-earnings indicator:** managerial remuneration structurally above the statutory 11% cap, sustained via recurring special resolutions, with combined family remuneration close to or exceeding reported PAT — while technically compliant, this materially affects the distributable-earnings picture available to minority shareholders.
- Not flagged as earnings management: revenue recognition, inventory valuation, and the gratuity actuarial assumptions/sensitivity disclosures are all conservative and well-documented; no evidence of channel stuffing, premature revenue recognition, or hidden liabilities beyond the items above.

---

## F. ONE-LINE NOTES VERDICT

The notes reveal moderate accounting practices with two concerning pockets. Key concern: ECL under-provisioning on the highest-risk litigated receivables combined with statutory-auditor-flagged gaps in managerial remuneration compliance and audit-trail integrity. Key strength: conservative, consistent revenue recognition and genuinely thorough actuarial/fair-value disclosure with no restatements. Overall accounting quality: 5/10.

```yaml
stage: B02-notes
company: "SMRUTHI"
run_date: "2026-07-09"
model: claude-sonnet-5
status: complete
input_gaps: [concalls absent (NO-CONCALL MODE), peer-concalls absent, presentation absent]
flags:
  - {type: FLAG-CASH, reason: "ECL provision on >3-year, litigated trade receivable bucket (Rs 219.67L, incl. Rs 216.15L unresolved legal-recovery case unchanged for 2 years) is only ~0.11% vs the company's own stated 2.5-7.5% policy band; top-2 customer concentration doubled to 27.5% of revenue with fully unhedged export FX exposure (Note 10, Note 26/45, Note 47)."}
accounting_quality: 5        # /10
pass_2_empty: false
pass_3_empty: false
top_findings:                # max 15
  - {rank: 1, finding: "Audit trail (edit log) not verifiable throughout the year and not enabled at database level for EasyERP software, a statutory Rule 11(g) compliance gap", note_ref: "Note 48, p.97-98; Auditors' Report para 2(h)(vi), p.38-39", rating: "Red Flag", why: "Undermines confidence in traceability of all financial records; understated by Directors' Report's 'clean, no qualifications' framing"}
  - {rank: 2, finding: "Managerial remuneration paid in excess of the 11% statutory cap under Section 197/Schedule V, sustained via special resolutions; family remuneration exceeds FY25 PAT", note_ref: "Auditors' Report Section 197(16) para, p.39; Note 39, p.81", rating: "Red Flag", why: "Structural governance/RPT-fairness issue formally reported by the auditor, not flagged as such in the notes narrative"}
  - {rank: 3, finding: "Four mortgaged factory-collateral land parcels registered in the Managing Director's personal name for ~24 years; SBI released its charge on them in Feb-2025", note_ref: "Note 46(m), p.91; Note 17, p.71; CARO Annexure A(i)(c), p.40", rating: "Red Flag", why: "Long-standing related-party title/governance defect on operating collateral, connected to reduced bank security cover this year"}
  - {rank: 4, finding: "ECL provisioning on the >3-year, litigated receivable bucket is ~0.11% vs the company's own stated 2.5-7.5% policy band", note_ref: "Note 10, p.67; Note 3.3/3.19, p.52/60", rating: "Red Flag", why: "Material internal inconsistency between stated ECL policy and actual provisioning on the single highest-risk receivable bucket"}
  - {rank: 5, finding: "Gratuity plan only 45.6% funded with a sudden funding catch-up and a large FY26 contribution projected", note_ref: "Note 41, p.84-86", rating: "Red Flag", why: "Materially underfunded defined-benefit plan with an unexplained, large prospective cash-flow call"}
  - {rank: 6, finding: "Top-2 customer concentration roughly doubled to 27.5% of net revenue, alongside fully unhedged export receivables", note_ref: "Note 26/45, p.77/90; Note 47, p.94", rating: "Watch", why: "Growing concentration risk compounded by unhedged FX exposure on the same export book"}
  - {rank: 7, finding: "Debt-financed capex weakened credit metrics: borrowings +43.5% YoY, Debt-Equity +38.4%, DSCR down 58.3%", note_ref: "Note 17/21/44/47, p.71/74/88/94", rating: "Watch", why: "Magnitude of DSCR deterioration warrants monitoring despite company's term-loan-drawdown explanation"}
  - {rank: 8, finding: "Forged/altered cheque litigation ongoing since 2020, fully provided but unresolved 5+ years", note_ref: "Note 46(o), p.92; Note 8, p.66", rating: "Red Flag", why: "Indicative of a historical payment-control weakness that remains legally unresolved"}
  - {rank: 9, finding: "Significant, growing related-party job-work/remuneration flows to the promoter family; personal guarantee backs Axis facilities", note_ref: "Note 39, p.81-82; Note 17/21, p.71/74", rating: "Watch", why: "Concentration of financial flows and personal guarantees within one family, not flagged as material RPT by the company"}
  - {rank: 10, finding: "Stated FX hedging policy is not executed; both receivables and payables remain fully unhedged", note_ref: "Note 3.4/47, p.53/94", rating: "Watch", why: "Disclosed policy-vs-practice inconsistency on currency risk management"}
  - {rank: 11, finding: "Trade payables collapsed 44% YoY, a large negative working-capital swing, alongside first-time delayed-MSME-payment interest", note_ref: "Note 22, p.75; Cash Flow Statement, p.48", rating: "Watch", why: "Significant cash-flow drag from working capital; first MSME-delay interest disclosure signals a payment-timing shift"}
  - {rank: 12, finding: "Profit before tax presented as three different figures across the P&L, Cash Flow Statement and Segment Note, unreconciled, with a mislabeled cash-flow line", note_ref: "P&L p.47; Cash Flow Statement p.48; Note 45, p.89-90; Note 27.1, p.78", rating: "Watch", why: "Cross-statement numerical inconsistency; disclosure/preparation quality-control gap identified in pattern pass"}
  - {rank: 13, finding: "Bank stock-statement reconciliation gap for Trade Payables peaks at fiscal year-end at ~8.5% of the reported balance", note_ref: "CARO Annexure A(ii)(b), p.40-41; Note 46(j), p.91", rating: "Watch", why: "Far larger than equivalent Inventory/Receivables gaps; coincides with the flagged payables collapse and affects secured drawing power"}
  - {rank: 14, finding: "MD's wife is the second-largest shareholder (15.27%) while also proprietor of the growing RPT job-work vendor", note_ref: "Note 15(d), p.69; Note 39, p.81-82", rating: "Watch", why: "Sharpens the RPT-fairness picture: same family member is both a top-2 equity holder and a growing RPT counterparty"}
  - {rank: 15, finding: "MD's remuneration is 63.55x median employee remuneration; JMD's is 42.37x", note_ref: "Directors' Report Annexure III, p.23", rating: "Watch", why: "Concrete quantification of internal pay disparity underlying the broader family-remuneration theme"}
red_flags:
  - "ECL under-provisioning (~0.11% vs 2.5-7.5% policy) on the highest-risk, litigated receivable bucket flatters both balance sheet and P&L"
  - "Title deed defect and MD personal guarantee on core operating/collateral assets disclosed only in fine-print regulatory notes, not in Directors' Report or MD&A"
  - "Three inconsistent 'profit before tax' figures across P&L, Cash Flow Statement and Segment Note with no reconciliation footnote and a mislabeled cash-flow line"
  - "Managerial remuneration structurally above the statutory 11% cap, sustained via recurring special resolutions, with family remuneration near or above reported PAT"
questions_for_mgmt:
  - "Why is the ECL provision on the >3-year, litigated receivable bucket (Rs 219.67L) only ~0.11% against the company's own 2.5-7.5% policy band, and what is the realistic recovery timeline on the unchanged Rs 216.15L legal case?"
  - "What is the Board's plan to bring managerial remuneration within the ordinary 11% statutory cap, and will fresh shareholder waivers be needed under the newly approved FY25-28/31 reappointment terms?"
  - "What is the timeline and cost to rectify the 24-year-old title-deed defect on land mortgaged as collateral but held in the MD's personal name, and what lender/company protections exist if his personal circumstances change?"
  - "What specifically triggered the gratuity funding catch-up (LIC contribution from Rs 0.79L to Rs 53.43L, with Rs 357.09L projected for FY26) - historic under-provisioning or a policy change?"
  - "Can management reconcile the Rs 511.02L 'profit before tax' used in the Cash Flow Statement and Segment Note against the Rs 490.00L PBT in the Statement of Profit and Loss, and clarify the mislabeled Rs 21.02L cash-flow adjustment line?"
receivables_trend: "mixed: aggregate turnover improving (3.83x FY25 vs 3.61x FY24; >6-months share 7.5% vs 7.8%) but quality deteriorating at the tail - the >3-year litigated bucket (Rs 219.67L, incl. Rs 216.15L legal-recovery case) is unchanged for 2 years and provisioned at only ~0.11% vs the stated 2.5-7.5% ECL policy band (Note 10, p.67; Note 44, p.88)"
restatements_found: []
going_concern_language: "NONE - Auditors' Report CARO para 3(xix), p.43, and Directors' Responsibility Statement, p.16, both affirm going concern with no material uncertainty language"
```
