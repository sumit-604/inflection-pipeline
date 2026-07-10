# STAGE 2 — NOTES TO FINANCIAL STATEMENTS — CONSOLIDATED (PASSES 1–3)
Company: APEXECO (Apex Ecotech Limited) | Run date: 2026-07-10
Source: Annual_Report_2025.pdf (FY 2024-25, year ended 31 March 2025), Notes 1–31 (p.49–65),
cross-referenced against Boards' Report, Annexures, CARO Annexure A and MDA throughout.
Basis of accounting: IGAAP, SME-Emerge listed entity, exempt from Ind AS (Boards' Report, p.24).

This document combines: Pass 1 (full sequential extraction, Note 1–31), Pass 2 (second sequential
re-read for missed items), and Pass 3 (pattern-based re-read: contradictions, note-to-note mismatches,
vague-vs-detailed disparities, restatements, subsequent events, going concern) into one consolidated
analysis. Full Pass 1 and Pass 2 outputs are preserved verbatim at
runs/apexeco-2026-07-10/outputs/reports/02-pass1.md and 02-pass2.md; this file synthesizes them and
adds the Pass 3 pattern layer plus the required consolidated sections A–F.

---

## PASS 3 — PATTERN RE-READ

Method: rather than a third sequential Note-1-to-31 walk, this pass applied a pattern lens —
contradictions between notes, numbers not tying to the main statements, disparities in disclosure
depth, restated/reclassified language, subsequent events, and going-concern language — across the
complete Note 1–31 dataset already extracted verbatim in Passes 1 and 2 (both of which quote exact
rupee figures, page references, and cross-references for every note). Note: direct PDF re-rendering was
not available to this call (tool dependency unavailable in this environment), so this pass worked from
the complete, quote-level Pass 1/2 extraction rather than a fresh independent read of the source file;
this is disclosed for transparency rather than presented as a substitute for source access.

**Contradictions already surfaced (Pass 2) that constitute the core "pattern" findings and are not
repeated as new here, only re-confirmed under the pattern lens:**
- Note 20(b) rupee-implied pay increases (169.3% / 26.9%) vs Annexure III's stated percentages
  (37.02% / 37.02% / 53.35%) for the same three individuals — direct numeric contradiction.
- Note 1(i) narrative (₹12.20 lakh FY25 DTA) vs Note 23's table (₹12.63 lakh) — note-to-note mismatch.
- Note 25's ₹11.88 lakh DLF principal vs Note 30's ₹11.89 lakh ageing-table figure, and the
  unexplained ₹15.51→₹11.89 lakh FY24-to-FY25 movement in an unresolved litigation.
- MDA (p.32) claim that FY25 growth was "driven by international and domestic contracts" vs Note 22
  showing export revenue fell 59% with 100% geographic/customer churn.
- MDA Risk Factors (p.33) describing "material litigations ... financial liabilities, reputational damage"
  vs Note 25's actual portfolio, which is modest (<1% of net worth) and where the company is
  predominantly the plaintiff.

**Additional pattern-level observations from this pass:**

1. **Vague-vs-detailed disparity pattern.** The notes are highly granular on low-risk items (PPE
   roll-forward by asset class down to the rupee, Note 8; payment-to-auditors split by fee type, Note
   21; solvency ratios with an explanatory sentence per ratio, Note 29) but conspicuously thin on the
   highest-stakes items: revenue recognition methodology for an EPC contractor (Note 1e, generic
   language only), the three related enterprises with directors' significant influence (Note 20a, named
   with zero further detail), and the ₹10.81 lakh disputed "Others" trade payable (Note 30, no
   counterparty ever named). The pattern — precision on routine disclosures, silence on judgment-heavy
   or related-party items — is itself a transparency signal worth weighting in the accounting quality
   score (Note 1e p.49, Note 20a p.58, Note 30 p.64).

2. **Restatement / reclassification language.** Only one instance found: Note 26 (p.60), "Previous
   year figures have been regrouped and reclassified wherever required," with no itemized schedule of
   what moved or by how much. No quantified prior-period restatement was identified anywhere else in
   Notes 1–31 (confirmed against Pass 1 and Pass 2's line-by-line coverage of every note).

3. **Events after balance sheet date.** No dedicated "Subsequent Events" or "Events after the
   Reporting Period" note exists within Notes 1–31 (the notes run from share capital through balance
   confirmations with no such heading). The only identified post-year-end item, the Company Secretary
   change (Kirti Jain resigned effective 30 June 2025, replaced by Vishakha Rani w.e.f. 25 August 2025),
   surfaces only in the Corporate Information section outside the audited notes (Pass 2, Note 20a
   cross-ref, p.58), not in a subsequent-events disclosure. This is a completeness gap in the notes
   themselves rather than a new financial finding, and is noted here as a pattern rather than escalated
   to a numbered top finding given its governance (not financial-statement) nature.

4. **Going concern language.** NOT FOUND IN DOCUMENT anywhere in Notes 1–31, the Auditor's Report
   extract available via Pass 1/2 (CARO Annexure A references), or the Boards' Report cross-references
   used throughout Passes 1–2. No material uncertainty, no qualification, no going-concern paragraph.
   This is consistent with, and corroborated by, the company's own disclosed solvency ratios (Note 29):
   current ratio 4.50x, Debt-Equity 0.00, Debt Service Coverage 34.15x — a balance sheet with no
   plausible going-concern question. Recorded as "NONE" rather than a gap.

No wholly new note-anchored numeric finding beyond the above pattern synthesis emerged from this pass.

**PASS 3: NO MATERIAL NEW FINDINGS** (beyond the pattern-level synthesis above, which re-frames but
does not add to the underlying numbers already captured in Passes 1–2).

---

═══════════════════════════════════════════════
CONSOLIDATED NOTES ANALYSIS, ALL THREE PASSES COMBINED
═══════════════════════════════════════════════

## A. TOP 15 MOST SIGNIFICANT FINDINGS (ranked by investor importance)

| Rank | Finding | Note # | Rating | Why it matters |
|---|---|---|---|---|
| 1 | Trade receivables up 155.3% (₹866.67→₹2,212.83 lakh) vs revenue up only 33.67%; **zero** doubtful-debt provision in the ageing table both years; debtors turnover fell 6.77x→4.61x (implied days ~54→~79), self-flagged by the company as a "Significant Change" | Note 10 (p.55), Note 30 (p.64), Note 29 (p.63) | 🔴 Red Flag | Core cash-conversion/earnings-quality signal; growth is being funded by working capital, not cash, with no provisioning discipline against the risk |
| 2 | Note 20(b) rupee figures imply a 169.3% FY25 pay increase for MD Anuj Dosajh and ED Ramakrishnan Balasundaram Aiyer, versus 37.02% stated for both in Annexure III; the third director's Annexure III figure (53.35%) is likewise inconsistent with his Note 20(b)-implied 26.9% increase | Note 20(b) p.58 vs Annexure III p.31 | 🔴 Red Flag | Direct numeric contradiction between two statutory disclosures on management compensation in the IPO year; a governance/integrity question, not a rounding issue |
| 3 | Director's Remuneration +90.9% YoY; average managerial pay growth 38.79% vs average employee (non-managerial) growth of only 7.19% in the listing year | Note 17 (p.57); Annexure III (p.31) | 🔴 Red Flag | Disproportionate insider enrichment concurrent with the IPO, ahead of the receivables/turnover deterioration reaching investors |
| 4 | Three "enterprises over which Directors have significant Influence" (Oakens Engineering Services, Flagmo Ea Technologies, Flagmo Marketing) are named with **zero** disclosed transactions anywhere in the notes | Note 20(a) (p.58) | 🔴 Red Flag | Either genuinely dormant relationships disclosed with unusual formality, or transactions exist outside Note 20(b)'s table; a specific, answerable completeness question |
| 5 | Undisclosed Bank of India CC account debit balance of ₹665.43 lakh (FY25 only, ~11% of total assets) within Cash and Cash Equivalents, with no corresponding facility in Note 4 (Borrowings), which shows Debt-Equity of 0.00 | Note 11 (p.55); no cross-ref in Note 4 (p.52) | 🟡 Watch | A material-sized banking facility with no limit, security, or terms disclosed is a completeness gap in a "debt-free" balance sheet narrative |
| 6 | Unexplained, stale (>3-year), disputed non-MSME trade payable of ₹10.81 lakh, unchanged to the rupee across both years, with no counterparty or nature ever identified | Note 30 (p.64); no cross-ref in Note 25 | 🔴 Red Flag | An unexplained liability sitting static for 3+ years signals either a disclosure gap or an unresolved dispute investors cannot assess |
| 7 | 9:1 bonus share issue (87,17,400 shares, ₹871.74 lakh capitalised from P&L surplus) immediately pre-IPO; combined promoter holding diluted 25.03 percentage points (94.32%→69.29%) in one year | Note 2 (p.51), Note 3 (p.52) | 🟡 Watch | Classic pre-listing cosmetic action on per-share metrics; dilution magnitude worth tracking against promoter commitment post-listing |
| 8 | Export revenue fell 59% (₹407.71→₹167.10 lakh) with 100% customer/geography churn (Vietnam FY24 → Egypt/Nigeria FY25), directly contradicting the MDA's claim that growth was "driven by international and domestic contracts" | Note 22 (p.59) vs MDA (p.32) | 🟡 Watch | Narrative-vs-notes contradiction on a growth driver; international mix is shrinking and fully non-repeating, not expanding |
| 9 | MDA Risk Factors describe "material litigations ... financial liabilities, reputational damage" while Note 25's actual litigation portfolio is modest (well under 1% of net worth) and the company is predominantly a plaintiff (net claimant) | Note 25 (p.60) vs MDA (p.33) | 🟡 Watch | Boilerplate risk language overstating actual exposure, or an indication undisclosed litigation may exist beyond Note 25 |
| 10 | Trade Retentions now 47.7% of total trade receivables (₹1,056.03 of ₹2,212.83 lakh), up 61.7% YoY | Note 10 (p.55) | 🟡 Watch | Large, growing, contractually-locked share of "current" assets tied to project milestone/defect-liability release, a slower-cash-conversion component |
| 11 | Disputed DLF receivable fell unexplained from ₹15.51 lakh (FY24) to ₹11.89 lakh (FY25) in active, unresolved litigation; Note 25 states ₹11.88 lakh for the same balance Note 30 shows as ₹11.89 lakh | Note 30 (p.64); Note 25 item 2 (p.60) | 🟡 Watch | Movement in a litigated asset with no settlement/write-off disclosed, plus an inter-note tie-out failure |
| 12 | Return on Equity fell from 60% to 28%; ROCE fell from 59.61% to 24.70% — equity-base (IPO) driven, not operational | Note 29 (p.63) | 🟡 Watch | Resets the forward profitability baseline materially lower for valuation purposes; not a quality flag per se but valuation-critical |
| 13 | No warranty provision and no gratuity actuarial assumptions (discount rate, salary escalation, mortality, funded status) disclosed anywhere; depreciation useful lives admitted to deviate from Schedule II with no independent justification | Note 1 (p.49–50), Note 5 (p.52) | 🟡 Watch | Provisioning-adequacy and disclosure gaps for a plant manufacturer/EPC contractor where such items are standard practice |
| 14 | Note 1(i)'s DTA narrative states a ₹12.20 lakh FY25 closing balance; Note 23's detailed table shows ₹12.63 lakh for the same Fixed Assets DTA component | Note 1(i) p.50 vs Note 23 p.59 | 🟡 Watch | Small in size but a genuine cross-note tie-out failure, a drafting/proofing quality signal |
| 15 | Three Company Secretaries within roughly 17 months spanning the IPO window (Nidhi Sharma one month, then Kirti Jain, then Vishakha Rani post year-end), with no reason disclosed | Note 20(a) (p.58) | 🟡 Watch | Compliance-continuity/governance observation during the most disclosure-sensitive period of the company's life |

*(Not separately tabled but noted: "Factory Building" carried at nil in both years' PPE schedule against a self-described manufacturing model — Note 8, p.54; gratuity expense embedded in "Salaries, wages and bonus" with no separate P&L quantification — Note 17, p.57. Both are extensions of Findings 5/13 respectively and are folded into the accounting-quality scoring below.)*

---

## B. ACCOUNTING QUALITY SCORE (1–10)

| Dimension | Score /10 | Basis |
|---|---|---|
| Revenue recognition conservatism | 6 | Policy language is generic/vague for an EPC contractor with large project retentions (Note 1e), but Note 14's revenue reconciles cleanly to the P&L and Note 16's COGS reconciles exactly; no evidence of premature recognition found, only a disclosure-quality gap |
| Expense capitalisation honesty | 8 | No CWIP, no capitalisation of routine opex identified; capex is small and straightforward (Note 8); IPO expenses correctly and transparently charged against Securities Premium (Note 3) rather than deferred or capitalised |
| Provisioning adequacy | 2 | Zero doubtful-debt/ECL provision against ₹2,212.83 lakh of receivables growing 155% (Note 10, Note 30); no warranty provision for a plant manufacturer (Note 5); no gratuity actuarial assumptions disclosed (Note 1l, Note 5); weakest dimension by a wide margin |
| RPT fairness | 3 | Three related enterprises with zero disclosed transactions (Note 20a); identical, unexplained spousal salaries (Note 20); a direct numeric contradiction between Note 20(b) and Annexure III on director pay increases |
| Disclosure transparency | 3 | Multiple note-to-note mismatches (Note 1i vs 23, Note 25 vs 30), an undisclosed ₹665.43 lakh CC facility (Note 11 vs Note 4), an unexplained static disputed payable (Note 30), no subsequent-events note despite post-year-end KMP changes |
| Consistency with prior years | 5 | Policies stated as consistent (Note 1a); boilerplate, non-itemised prior-year regrouping language (Note 26); a newly recognised gratuity DTA component with no explanatory note (Note 23) |
| **OVERALL** | **4** | Core mechanical reconciliations (revenue, COGS, PPE roll-forward, reserves) are clean, but provisioning, related-party transparency, and cross-note consistency are materially weak for a company in its IPO year, when disclosure discipline should be at its highest |

---

## C. KEY RISKS FROM NOTES

| Risk | Severity | What to monitor | When it could hit |
|---|---|---|---|
| Receivables/working-capital deterioration, zero doubtful provisioning | High | Receivable days trend, any provisioning policy introduced, collections vs revenue growth in FY26 quarterly filings | Next 1–2 quarters if the growth-outpacing-collections pattern persists |
| Management remuneration disclosure inconsistency (Note 20b vs Annexure III) | High | FY26 AGM/Annexure III disclosures, any exchange or SEBI clarification sought, restated remuneration figures | Any time; reputational and potential regulatory query |
| Opaque related-party enterprises with zero transaction disclosure | Medium-High | FY26 Note 20(b) for any transactions with the three named enterprises; auditor commentary | Next annual report (FY26) |
| Undisclosed/unclear Bank of India CC facility | Medium | FY26 Note 4 and cash flow financing activities for a CC/OD line item and its terms | FY26 annual report |
| Unexplained static disputed trade payable (₹10.81 lakh) | Low (size) / Medium (disclosure discipline) | Whether the FY26 notes name the counterparty or resolve the balance | FY26 annual report |
| Post-IPO ROE/ROCE step-down (60%→28%, 59.6%→24.7%) | Medium (valuation, not solvency) | Deployment of IPO proceeds, capital allocation, whether growth reinvestment restores return ratios | Over the 2–3 year holding horizon |
| Unquantified Section 270A tax penalty exposure | Low-Medium | CIT(A) appeal outcome (filed 22.04.2024) | FY26–FY27, upon appeal resolution |

---

## D. FIVE QUESTIONS FOR MANAGEMENT

1. Which FY25 remuneration increase figure is correct for Mr. Anuj Dosajh and Mr. Ramakrishnan Balasundaram Aiyer — the 169.3% implied by Note 20(b)'s rupee figures, or the 37.02% stated in Annexure III — and what explains the discrepancy (e.g., different remuneration bases, perquisites, employer PF contributions)?
2. What is the nature, counterparty, and current transaction status (if any) with Oakens Engineering Services Private Limited, Flagmo Ea Technologies Private Limited, and Flagmo Marketing Private Limited, the three related enterprises named in Note 20(a) with zero disclosed transaction value?
3. What is the sanctioned limit, security, interest rate, and banking relationship terms for the Bank of India CC account showing a ₹665.43 lakh debit balance in Note 11, and why does no corresponding facility appear in Note 4 (Borrowings)?
4. What is the company's formal provisioning policy for doubtful trade receivables, and why has zero doubtful/ECL-equivalent provision been recognised despite receivables growing 155% and debtors' turnover falling from 6.77x to 4.61x?
5. Who is the counterparty and what is the nature of the ₹10.81 lakh disputed non-MSME trade payable that has sat unchanged in the greater-than-3-year ageing bucket in both FY24 and FY25?

---

## E. NOTES-BASED RED FLAGS

- **Zero doubtful-debt provisioning** against fast-growing receivables (₹2,212.83 lakh, +155.3% YoY) — a provisioning-adequacy red flag that directly affects reported asset quality and, prospectively, earnings if a catch-up provision is ever taken.
- **Cross-document remuneration inconsistency**: Note 20(b)'s rupee-implied percentage changes do not reconcile with Annexure III's stated percentages for the same three individuals — a potential misstatement in one of two statutory disclosures.
- **Opaque related-party enterprises**: three named entities with directors' significant influence and zero disclosed transactions — an undisclosed-risk-indicator pattern rather than a confirmed abuse, but unusual disclosure practice.
- **Undisclosed banking facility**: ₹665.43 lakh CC account debit balance with no matching Note 4 entry — a completeness gap in a balance sheet otherwise presented as debt-free.
- **Mild earnings-quality softening**: recurring "Balance Written Off" credits to Other Income (₹1.64 lakh FY25, ₹1.47 lakh FY24) and a one-off ₹20.63 lakh FY24 settlement receipt run through ordinary Other Income rather than classified as exceptional, both of which modestly flatter comparability without being individually material.

---

## F. ONE-LINE NOTES VERDICT

The notes reveal moderate to concerning accounting practices. Key concern: zero receivables
provisioning against 155% growth in trade receivables, compounded by an unreconciled 169% vs 37%
management remuneration discrepancy between Note 20(b) and Annexure III. Key strength: clean core
mechanical reconciliations across revenue, cost of materials, PPE and reserves, and a genuinely
debt-free operating balance sheet outside the undisclosed CC account. Overall accounting quality: 4/10.

---

```yaml
stage: B02-notes
company: "APEXECO"
run_date: "2026-07-10"
model: claude-sonnet-5
status: complete
input_gaps:
  - {type: rating, detail: "no credit rating PDF provided"}
flags:
  - {type: FLAG-CASH, reason: "Trade receivables up 155.3% (Note 10, p.55: Rs.866.67 lakh FY24 to Rs.2,212.83 lakh FY25) against revenue growth of only 33.67% (Note 14, p.56); debtors turnover deteriorated from 6.77x to 4.61x (Note 29, p.63, implied days ~54 to ~79); zero doubtful-debt provision in the ageing table across both years (Note 30, p.64) despite the scale of the increase and an actively litigated receivable classified 'considered good' rather than doubtful"}
accounting_quality: 4        # /10
pass_2_empty: false
pass_3_empty: true
top_findings:                # max 15
  - {rank: 1, finding: "Trade receivables up 155.3% (Rs.866.67 to Rs.2,212.83 lakh) vs revenue up 33.67%; zero doubtful-debt provision both years; debtors turnover fell 6.77x to 4.61x", note_ref: "Note 10 p.55, Note 30 p.64, Note 29 p.63", rating: "Red Flag", why: "Core cash-conversion/earnings-quality signal; growth funded by working capital with no provisioning discipline"}
  - {rank: 2, finding: "Note 20(b) rupee figures imply a 169.3% FY25 pay rise for MD Dosajh and ED Aiyer vs 37.02% stated in Annexure III for the same individuals; third director's 53.35% vs implied 26.9% also inconsistent", note_ref: "Note 20(b) p.58 vs Annexure III p.31", rating: "Red Flag", why: "Direct numeric contradiction between two statutory disclosures on management compensation in the IPO year"}
  - {rank: 3, finding: "Director's Remuneration +90.9% YoY; average managerial pay growth 38.79% vs average employee growth 7.19% in the listing year", note_ref: "Note 17 p.57; Annexure III p.31", rating: "Red Flag", why: "Disproportionate insider enrichment concurrent with the IPO"}
  - {rank: 4, finding: "Three enterprises with directors' significant influence (Oakens Engineering, Flagmo Ea Technologies, Flagmo Marketing) named with zero disclosed transactions", note_ref: "Note 20(a) p.58", rating: "Red Flag", why: "Either dormant relationships disclosed unusually, or undisclosed transactions exist; answerable completeness question"}
  - {rank: 5, finding: "Undisclosed Bank of India CC account debit balance of Rs.665.43 lakh (~11% of total assets) with no corresponding facility in Note 4 Borrowings, which shows Debt-Equity of 0.00", note_ref: "Note 11 p.55; no cross-ref Note 4 p.52", rating: "Watch", why: "Material banking facility with no limit, security, or terms disclosed; completeness gap in a 'debt-free' narrative"}
  - {rank: 6, finding: "Unexplained, stale (>3 year) disputed non-MSME trade payable of Rs.10.81 lakh, unchanged across both years, no counterparty or nature disclosed", note_ref: "Note 30 p.64; no cross-ref Note 25", rating: "Red Flag", why: "Static unexplained liability signals a disclosure gap or unresolved dispute investors cannot assess"}
  - {rank: 7, finding: "9:1 bonus issue (Rs.871.74 lakh capitalised from P&L surplus) immediately pre-IPO; promoter holding diluted 25.03pp (94.32% to 69.29%) in one year", note_ref: "Note 2 p.51, Note 3 p.52", rating: "Watch", why: "Pre-listing cosmetic action on per-share metrics; dilution magnitude worth tracking"}
  - {rank: 8, finding: "Export revenue fell 59% (Rs.407.71 to Rs.167.10 lakh) with 100% customer/geography churn (Vietnam to Egypt/Nigeria), contradicting MDA's claim growth was driven by international and domestic contracts", note_ref: "Note 22 p.59 vs MDA p.32", rating: "Watch", why: "Narrative-vs-notes contradiction on a stated growth driver"}
  - {rank: 9, finding: "MDA Risk Factors describe material litigations with financial/reputational exposure while Note 25's actual portfolio is modest (<1% of net worth) and company is predominantly a plaintiff", note_ref: "Note 25 p.60 vs MDA p.33", rating: "Watch", why: "Boilerplate risk language overstates actual exposure, or undisclosed litigation may exist"}
  - {rank: 10, finding: "Trade Retentions now 47.7% of total trade receivables (Rs.1,056.03 of Rs.2,212.83 lakh), up 61.7% YoY", note_ref: "Note 10 p.55", rating: "Watch", why: "Large, growing, contractually-locked share of current assets slows cash conversion"}
  - {rank: 11, finding: "Disputed DLF receivable fell unexplained Rs.15.51 to Rs.11.89 lakh in active litigation; Note 25's Rs.11.88 lakh does not match Note 30's Rs.11.89 lakh for the same balance", note_ref: "Note 30 p.64; Note 25 item 2 p.60", rating: "Watch", why: "Movement in a litigated asset with no settlement disclosed, plus an inter-note tie-out failure"}
  - {rank: 12, finding: "Return on Equity fell from 60% to 28%; ROCE fell from 59.61% to 24.70%, equity-base (IPO) driven not operational", note_ref: "Note 29 p.63", rating: "Watch", why: "Resets forward profitability baseline materially lower for valuation purposes"}
  - {rank: 13, finding: "No warranty provision and no gratuity actuarial assumptions disclosed; depreciation useful lives admitted to deviate from Schedule II with no independent justification", note_ref: "Note 1 p.49-50, Note 5 p.52", rating: "Watch", why: "Provisioning-adequacy and disclosure gaps standard for this business type but absent here"}
  - {rank: 14, finding: "Note 1(i)'s DTA narrative states Rs.12.20 lakh FY25 closing balance; Note 23's table shows Rs.12.63 lakh for the same Fixed Assets DTA component", note_ref: "Note 1(i) p.50 vs Note 23 p.59", rating: "Watch", why: "Small but genuine cross-note tie-out failure; drafting/proofing quality signal"}
  - {rank: 15, finding: "Three Company Secretaries within ~17 months spanning the IPO window, no reason disclosed", note_ref: "Note 20(a) p.58", rating: "Watch", why: "Compliance-continuity/governance observation during the most disclosure-sensitive period"}
red_flags:
  - "Zero doubtful-debt provisioning against receivables up 155.3% YoY (Note 10, Note 30)"
  - "Cross-document remuneration inconsistency: Note 20(b) implies 169.3% pay rise vs Annexure III's 37.02% for same individuals (Note 20b p.58 vs Annexure III p.31)"
  - "Disproportionate managerial remuneration growth (38.79% avg) vs employee growth (7.19% avg) in the IPO year (Note 17 p.57, Annexure III p.31)"
  - "Three related enterprises named with zero disclosed transactions (Note 20a p.58)"
  - "Unexplained, stale, disputed non-MSME trade payable of Rs.10.81 lakh (Note 30 p.64)"
questions_for_mgmt:
  - "Which FY25 remuneration increase figure is correct for Mr. Dosajh and Mr. Aiyer, the 169.3% implied by Note 20(b) or the 37.02% in Annexure III, and what explains the discrepancy?"
  - "What is the nature and current transaction status with Oakens Engineering Services, Flagmo Ea Technologies, and Flagmo Marketing, the three related enterprises in Note 20(a) with zero disclosed transactions?"
  - "What is the sanctioned limit, security, interest rate and terms for the Bank of India CC account showing a Rs.665.43 lakh debit balance in Note 11, and why is it absent from Note 4 Borrowings?"
  - "What is the formal doubtful-receivables provisioning policy, and why is zero provision recognised despite 155% receivables growth and debtors turnover falling from 6.77x to 4.61x?"
  - "Who is the counterparty and what is the nature of the Rs.10.81 lakh disputed non-MSME trade payable unchanged in the >3-year ageing bucket in both FY24 and FY25?"
receivables_trend: "deteriorating - trade receivables up 155.3% (Note 10 p.55: Rs.866.67 lakh FY24 to Rs.2,212.83 lakh FY25) vs revenue up 33.67% (Note 14 p.56); debtors turnover ratio fell 6.77x to 4.61x, implied days ~54 to ~79 (Note 29 p.63); trade retentions now 47.7% of receivables, up 61.7% YoY (Note 10 p.55); zero doubtful-debt provision in ageing table both years (Note 30 p.64)"
restatements_found:
  - "Note 26 (p.60): 'Previous year figures have been regrouped and reclassified wherever required' - boilerplate, no itemized schedule of what moved or by how much; no quantified prior-period restatement identified elsewhere in Notes 1-31"
going_concern_language: "NONE - no going concern qualification, material uncertainty, or discussion found anywhere in Notes 1-31 or cross-referenced Auditor's Report/CARO extracts; consistent with strong solvency ratios per Note 29 (current ratio 4.50x, Debt-Equity 0.00, Debt Service Coverage 34.15x)"
```
