# Stage 2 — Notes to Financial Statements, Triple Pass: PASS 3 (Pattern Pass + Consolidation)

Company: Steel Strips Wheels Ltd (SSWL) | Run date: 2026-09-19
Source: inputs/annual-report/SSWL-AR-FY26-Reg34-2026-09-03.txt (page-marked text of the 245-page PDF; "AR p.N" cites the PDF page)
Unit as printed on the face of every note: Rs in Lakhs. This report states every figure as "Rs X lakh (Rs Y.YY Cr)".

Scope: pattern re-read of standalone notes 1-54 (AR p.144-183) and consolidated notes 1-56 (AR p.196-239), the auditor's reports (standalone AR p.130-138, consolidated AR p.183-189), the accounting-policy notes (Note 2, both statements) and AOC-1 (AR p.239-240), searching specifically for contradictions, figures that do not tie across notes or against the main statements, deliberately thin disclosure next to detailed disclosure elsewhere, restatements, subsequent events and going-concern language. Cross-checked against Pass 1 (outputs/reports/02-notes-pass1.md) and Pass 2 (outputs/reports/02-notes-pass2.md).

---

## PASS 3 PATTERN FINDINGS (new)

### Pattern Finding 1: The AR's own business-combination accounting policy names the exact mechanism that would produce Findings 1-2's unexplained reserve transfers — but never confirms it was used for AMW

Consolidated Note 2.04(C) "Business Combinations" (AR p.197-198) states the Group's default policy is the **acquisition method** (fair-value purchase accounting, goodwill/bargain-purchase recognition). Immediately after, the same note sets out a **separate pooling-of-interests method for common-control business combinations** (AR p.198), with two clauses that are a near-exact mechanical match to the pattern Pass 1 and Pass 2 found unexplained in Note 19:
- Clause (d): "The balance of the retained earnings appearing in the financial statements of the transferor is aggregated with the corresponding balance appearing in the financial statements of the transferee **or is adjusted against revenue reserve**."
- Clause (f): "The difference... between the amounts recorded as share capital issued... and the amount of share capital of the transferor **is transferred to revenue reserves/capital reserves**."

This is the only place anywhere in the AR that names "capital reserves" as a destination for a business-combination-driven equity adjustment — which is exactly the label of the unexplained Rs 364.52 Cr FY26 line Pass 1/2 flagged as the single largest disclosure gap in the filing. No note states whether AMW's acquisition (NCLT resolution plan under IBC, per CWIP Note 4(II), standalone AR p.213) was accounted for as a common-control combination or under the stated default acquisition method, and **no Ind AS 103 purchase-price-allocation note (consideration transferred, fair value of identifiable net assets, goodwill or bargain-purchase gain) for AMW appears anywhere in this AR**, in either the current year or the two-year comparative window. Given no goodwill balance exists anywhere in the consolidated notes (confirmed by Pass 1), a bargain-purchase or common-control treatment is the more consistent read of the numbers than a standard acquisition-method purchase — but the AR itself never says so.

This is the strongest documentary lead yet connecting the mechanism to the two unexplained reserve transfers (Rs 674.68 Cr FY25 General Reserve, Rs 364.52 Cr FY26 Capital Reserve). It remains inferential: the policy note is boilerplate that could equally apply to a hypothetical future combination and not to AMW at all. (Note 2.04(C), consol AR p.197-198; cross-refs Note 19 consol AR p.219-220, Note 4(II) standalone AR p.213)

Rating: 🔴 Red Flag — elevates Findings 1 and 2 from "unexplained" to "unexplained despite the AR itself carrying an accounting policy that would explain them."

### Pattern Finding 2: AACL's land, received via a demerger scheme, is not yet registered in the subsidiary's own name

Consolidated Note 3 (Property, Plant and Equipment), title-deeds note (AR p.212): *"land lying in the books of the subsidiary company ('AACL') that was transferred by virtue of the demerger scheme of Asia Motor Works Limited ('AMWL') is not yet registered in the name of the subsidiary company."* This is the first appearance across all three passes of the term "demerger" or "Asia Motor Works Limited" — it identifies a second corporate-action layer behind AMW's asset base (a demerger from AMWL, the original promoter group entity, separate from and presumably prior to the NCLT resolution-plan acquisition by SSWL) and a live title-registration gap on the land AACL uses. No note states the land's carrying value, how long the registration has been outstanding, or whether it affects any charge/security. Small in isolation; material because it is a third unexplained AMW-linked disclosure gap (alongside Findings 1-2 and the AOC-1/Note 53 net-asset gap already found in Pass 2). (Note 3, consol AR p.212)

Rating: 🟡 Watch — new.

### Pattern Finding 3: A Rs 100 Cr HDFC Bank term loan was raised specifically to fund the AMW acquisition — quantifying part of LBF4 for the first time in this corpus

Standalone auditor's CARO Annexure, end-use-of-borrowed-funds table (AR p.136): a **Rs 10,000.00 lakh (Rs 100.00 Cr) term loan from HDFC Bank Limited** is listed with fund utilisation "Acquisition of AMW Autocomponent Ltd," remark "Related to FY 2023-24." This is disclosed as a standard CARO compliance item (funds used for stated purpose), not as a business-combination note, but it is the first hard number in this corpus for how the AMW acquisition (company memory LBF4, consideration ~Rs 138 Cr) was financed: at least Rs 100 Cr of it was debt-funded. (CARO Annexure, standalone AR p.136)

Rating: 🟢 informational — corroborates and partially quantifies LBF4; not itself a flag.

### Pattern Finding 4: Both auditor's reports state there are NO Key Audit Matters, despite the notes carrying several judgment-heavy, weakly substantiated areas

Both the standalone (AR p.130) and consolidated (AR p.183) Independent Auditor's Reports state verbatim: *"We have determined that there are no key audit matters to be communicated in our report."* Under SA 701, a listed company's KAM determination is expected to surface areas of significant audit judgment. Pass 1-3 together identified several such areas inside the notes themselves: a Rs 364.52 Cr unexplained reserve transfer (Finding 1), a Rs 34.84 Cr unreconciled consolidation-only reserve, a Rs 59.31 Cr DTA recognised and grown against a three-years-loss-making subsidiary with no disclosed forecast support, and an impairment-assessment cross-reference (Note 6(II) to Note 52(C)) that leads to no actual methodology. None of these became a KAM. This does not itself indicate an audit-quality problem — the auditor may have concluded none met the "most significant" bar, or resolved concerns through work not visible in the notes — but the gap between what the notes leave unexplained and what the audit report treats as routine is itself a pattern worth naming, and is not something later stages should assume the audit has separately closed. (Auditor's Reports, standalone AR p.130, consolidated AR p.183)

Rating: 🟡 Watch — new, process observation.

### Pattern re-checks that found nothing new
- **Numbers vs main statements**: Note 19's consolidated Other Equity closing total, Note 40's contingent-liability figures, and Note 11/10/20/25's balance-sheet-line totals were checked against the face of the Balance Sheet references embedded in the notes' own comparative columns; no unreconciled mismatch beyond the AOC-1-vs-Note-53 AMW net-asset gap Pass 2 already found.
- **Restatements**: full-text search for "restat" (AR-wide) returns only accounting-policy boilerplate (Ind AS 8 policy language, the Ind AS 109 reclassification policy explicitly stating "does not restate," and the common-control policy's own restatement clause covered in Pattern Finding 1). No note discloses an actual prior-period restatement having occurred. `restatements_found: []` stands from Pass 2.
- **Going concern**: full-text search confirms, again, no material-uncertainty-related-to-going-concern paragraph in either auditor's report and no subsequent-events note format anywhere (Pass 1/2 findings stand, unchanged).
- **Deliberately thin vs detailed disclosure**: the pattern is consistent across all three passes — AMW-linked items (reserves, DTA, net assets, land title, turnover) are uniformly the thinnest disclosures in an otherwise detailed AR; nothing outside the AMW cluster showed the same pattern on a fresh read.

---

## CONSOLIDATED NOTES ANALYSIS, ALL THREE PASSES COMBINED

### A. TOP 15 MOST SIGNIFICANT FINDINGS

| Rank | Finding | Note # | Rating | Why it matters |
|---|---|---|---|---|
| 1 | Two consecutive years of large, unexplained equity-to-equity reserve transfers in consolidated Other Equity: Rs 674.68 Cr to General Reserve (FY25, 3.5x that year's own profit) and Rs 364.52 Cr to Capital Reserve (FY26). Consolidated retained earnings swung from +Rs 57.64 Cr (FY24 close) to -Rs 826.70 Cr (FY26 close) despite positive profit both years. Note 19's own reserve-purpose list explains every reserve except Capital Reserve. | Note 19, consol AR p.219-220 | 🔴 Red Flag | The single largest transparency gap in the filing; an investor reading only the balance sheet would misread accumulated losses where none exist. Ties directly to LBF4. |
| 2 | The AR's own Note 2.04(C) accounting policy describes a pooling-of-interest/common-control method whose clauses on retained-earnings aggregation and "revenue reserves/capital reserves" differences mechanically match Finding 1's pattern, but no note confirms this method (vs. the stated default acquisition method) was applied to AMW, and no Ind AS 103 purchase-price-allocation note for AMW exists anywhere in this AR. | Note 2.04(C), consol AR p.197-198 | 🔴 Red Flag | The strongest documentary lead yet on Finding 1's mechanism; still unconfirmed, but this is exactly the kind of note a direct management question or the FY24/FY25 AR should close. |
| 3 | Consolidation-only Capital Revaluation Reserve of Rs 87.65 Cr (vs Rs 52.81 Cr standalone, a Rs 34.84 Cr gap), static both years, sits against the AR's own explicit "no revaluation of PPE/intangibles" declaration (standalone and consolidated). | Note 19 vs Note 53(X)/55(X), AR p.164/182/219-220/237 | 🔴 Red Flag | A reserve whose defined purpose is PPE revaluation gains coexists with a flat no-revaluation statement; most likely traces to AMW's pre-acquisition reserve surviving consolidation, never stated. Compounds Finding 1. |
| 4 | Supplier Finance Arrangement (reverse factoring): Rs 676.50 Cr, 67.6% of standalone trade payables (Rs 1,001.77 Cr), sits with a third-party financial institution; Rs 494.84 Cr already paid to suppliers by the institution at year-end. First-year Ind AS 7/107 disclosure, no FY25 comparative (transitional relief). | Note 25, standalone AR p.166-167, consol AR p.221-222 | 🔴 Red Flag | The mechanism behind LBF3: debt-like financing classified as an operating trade payable, flattering the current ratio and Net Debt/EBITDA, and routed through operating (not financing) cash flow. |
| 5 | Mark-to-market loss of Rs 32.42 Cr on FX forwards/options at FY26 close, including a USD 25mn notional Put & Call Options position (not a plain forward hedge). No FY25 comparative; P&L/OCI recognition point not traceable from the notes. | Note 48(c), standalone AR p.178-179, consol AR p.233-234 | 🔴 Red Flag | ~16% of standalone FY26 PAT (Rs 202.09 Cr). Options structure implies more than a natural hedge; opacity limits verifiability. |
| 6 | AMW Autocomponent Ltd (100% subsidiary): third consecutive year of losses (FY26 standalone loss Rs 16.82 Cr per AOC-1), Turnover disclosed as "0," net assets falling, and a growing Rs 59.31 Cr deferred tax asset on its carried-forward tax losses recognised with no disclosed forecast support. | Note 51/52/53 consol AR p.236-238; AOC-1 AR p.239 | 🔴 Red Flag | DTA realism risk plus a wholly-owned operating subsidiary reporting zero turnover; directly extends LBF4. |
| 7 | AACL's land, transferred via the demerger scheme of Asia Motor Works Limited (AMWL), is not yet registered in AACL's own name. No carrying value, duration, or security implication stated. | Note 3, consol AR p.212 | 🟡 Watch | New corporate-action layer (an AMWL demerger, distinct from the NCLT acquisition) and a live title/registration gap on a subsidiary's fixed asset. |
| 8 | Unsecured, interest-bearing Rs 133.15 Cr loan from SSWL to loss-making AMW, unchanged for two years; interest accrued Rs 8.27 Cr FY26. Eliminated on consolidation, so invisible in consolidated statements. | Note 41, standalone AR p.171-172 | 🟡 Watch | A related-party support commitment to a loss-making subsidiary that position-sizing and downside work should treat as a contingent capital commitment, not a risk-free asset. |
| 9 | Working capital deterioration across every line simultaneously: receivables +25.2% YoY vs revenue +11-17%, inventory +28.2%, payable days 69.29->75.64 (a two-year accelerating trend, Note 48(e): +25.4% then +33.2%). FY26's Net Debt/EBITDA improvement is an EBITDA-growth effect, not continued deleveraging (borrowings flat FY25-FY26 after a 21% FY24-25 fall). | Notes 11, 25, 10, 48(e), 52 standalone | 🟡 Watch | Coherent, multi-note, multi-year cash-conversion-quality signal alongside compressing ROE/ROCE/net margin; resolves LBF3's core question. |
| 10 | "Interest Others" of Rs 69.85 Cr within finance costs (1.4x disclosed bank-loan interest), a stable two-year unexplained structural gap (Rs 65.02 Cr FY25 -> Rs 69.85 Cr FY26, +7.4%), no breakdown sub-note in either year. | Note 35, standalone AR p.169, consol AR p.224 | 🟡 Watch | Likely embeds SCF/bill-discounting and/or derivative costs; opacity on a large finance-cost line limits verifiability of true borrowing cost. |
| 11 | MSME payables overdue-and-unpaid principal nearly doubled (Rs 1.97 Cr -> Rs 3.73 Cr); unpaid interest on delayed MSME payments also nearly doubled. | Note 25, standalone AR p.166-167 | 🟡 Watch | Vendor-payment-stress signal corroborating the broader working-capital read. |
| 12 | Note 6(II)'s impairment-assessment cross-reference for the associate ("Refer Note 52(C)") leads only to the associate's summarised balance sheet/P&L — no discount rate, methodology, or headroom is disclosed anywhere. | Note 6(II)/52(C), consol AR p.215-216/236-237 | 🟡 Watch | The promised substantiation for a stated management judgment does not exist in the document; Ind AS 36 para 134-type disclosure is absent. |
| 13 | Both auditor's reports (standalone and consolidated) determine there are NO Key Audit Matters, despite the notes carrying multiple judgment-heavy, weakly substantiated areas (Findings 1, 3, 6, 12). | Auditor's Reports, standalone AR p.130, consol AR p.183 | 🟡 Watch | Process observation: the gap between what the notes leave unexplained and what the audit treats as routine should not be assumed closed by the audit. |
| 14 | No product-level segment disclosure anywhere in the notes; single business segment under Ind AS 108, geography-only split. | Note 44, standalone AR p.173-174, consol AR p.228-229 | 🟡 Watch | LBF2 (mix-shift margin, alloy % of revenue) cannot be verified or cross-checked from the AR notes at all; evidence gap for downstream stages. |
| 15 | AMW's net-asset figure differs by Rs 5.37 Cr between its own AOC-1 (Rs 75.98 Cr) and the consolidated Note 53 Schedule III schedule (Rs 70.61 Cr), unreconciled. A Rs 100 Cr HDFC Bank term loan raised specifically for "Acquisition of AMW Autocomponent Ltd" (FY23-24) is disclosed in the CARO Annexure, quantifying part of LBF4's financing for the first time in this corpus. | AOC-1 AR p.239 vs Note 53 consol AR p.237; CARO standalone AR p.136 | 🟡 Watch / 🟢 informational | Small unreconciled gap sits inside the same AMW cluster carrying the AR's largest disclosure gaps; the HDFC loan figure is a useful new LBF4 anchor. |

### B. ACCOUNTING QUALITY SCORE

| Dimension | Score /10 | Basis |
|---|---|---|
| Revenue recognition conservatism | 8 | Point-in-time on delivery, standard Ind AS 115 language, no acceleration signals, no contract-asset/liability aggressiveness (Section 11 all passes). |
| Expense capitalisation honesty | 7 | R&D capex/opex split fully traceable across 3 years with no threshold changes; interest capitalisation declines consistently with the Mehsana capex ramp coming out of construction (Section 1/7). |
| Provisioning adequacy | 5 | ECL provision flat at Rs 20.26 lakh despite 25% receivables growth; leave-encashment non-current provision jumped 12.4x unexplained; no warranty provision roll-forward despite an explicit warranty policy for an auto-OEM supplier (Section 9, Pass 2 confirmed gap). |
| RPT fairness | 6 | Quantum small (1.06% of standalone revenue) and arm's-length asserted, but an unsecured Rs 133.15 Cr loan to a loss-making subsidiary and a CSR spend routed through a related-party trust are watch items, not clean passes. |
| Disclosure transparency | 3 | The weakest dimension by a wide margin: two years of unexplained reserve transfers (Rs 1,039.20 Cr combined), an unreconciled consolidation-only reserve, a dead-end impairment cross-reference, an opaque Rs 69.85 Cr finance-cost line, an AOC-1 "Turnover: 0" line never explained, no subsequent-events note format at all, and zero Key Audit Matters despite all of the above. |
| Consistency with prior years | 5 | No restatements found; policies stable across the two-year comparative window. But the reserve-transfer pattern and the payables/receivables growth are both confirmed two-year, accelerating trends, not one-year anomalies — consistency of a deteriorating and an unexplained pattern, not of clean mechanics. |
| **OVERALL** | **4** | Weighted down by disclosure transparency, which carries the most investor-relevant unresolved items and the largest rupee amounts of any dimension. |

### C. KEY RISKS FROM NOTES

| Risk | Severity | What to monitor | When it could hit |
|---|---|---|---|
| Unexplained two-year, Rs 1,039 Cr reserve-transfer pattern tied to AMW's acquisition accounting, with the AR's own policy note as an unconfirmed explanation | High | FY25 AR (not in this corpus), Board's Report, a direct management question on Note 19 and Note 2.04(C) | First verification priority for Stage 3/5/8; feeds any equity-based valuation or ROE/ROCE work now |
| Reverse-factoring debt-like financing (Rs 676.50 Cr, 67.6% of payables) off the borrowings note | High | Note 25 disclosure each quarter; factoring-limit utilisation vs the Rs 400-500 Cr limit named in LBF3 | Immediate, for any cash-conversion or liquidity analysis |
| FX options position (not a plain hedge) with a Rs 32.42 Cr MTM loss | Medium-High | Quarterly FX/derivatives note; INR volatility | Next 1-2 quarters if rupee moves against the position |
| AMW deferred tax asset realism (Rs 59.31 Cr against 3 years of losses) | Medium | AMW's quarterly performance; any DTA write-off disclosure | Could hit P&L in a future impairment/recoverability review |
| Working-capital and vendor-payment stress (MSME overdue doubling, payables stretching 2 years accelerating, receivables outpacing revenue) | Medium | Payable/receivable days each quarter; MSME note annually | Ongoing; a supplier-relationship or covenant risk if it continues |
| AACL land title unregistered (AMWL demerger) | Low-Medium | Registration completion status in future ARs | Legal/collateral risk only if the land is pledged or disputed |
| Zero Key Audit Matters against multiple weakly substantiated judgment areas | Medium | Next year's audit report; any auditor communication | Governance signal, ongoing rather than event-driven |

### D. FIVE QUESTIONS FOR MANAGEMENT

1. What is the accounting basis and full journal-level explanation for the Rs 674.68 Cr FY25 transfer to General Reserve and the Rs 364.52 Cr FY26 transfer to Capital Reserve in consolidated Other Equity (Note 19), and is either connected to the AMW/NCLT transaction accounting?
2. Was AMW's acquisition accounted for as a common-control combination (pooling of interest, per Note 2.04(C)) or under the stated default acquisition method — and if pooling, why does no note explain the resulting Capital Revaluation Reserve (Rs 34.84 Cr, consolidation-only) or connect it to the reserve transfers above?
3. What is the basis for recognising and growing a Rs 59.31 Cr deferred tax asset against AMW's carried-forward tax losses when AMW has posted losses every year since acquisition, and what is the expected utilisation timeline?
4. What does the Rs 69.85 Cr "Interest Others" line within finance costs comprise (supplier-finance/reverse-factoring charges, FX derivative costs, or other), and can a breakdown be provided?
5. What is the status of registering AACL's land (transferred via the AMWL demerger scheme) in AACL's own name, and does the unregistered status affect any charge or security currently in place?

### E. NOTES-BASED RED FLAGS

- Two consecutive years of large, unexplained equity-to-equity reserve reclassifications (Rs 674.68 Cr FY25, Rs 364.52 Cr FY26) that make consolidated retained earnings look like accumulated losses (-Rs 826.70 Cr) when the company was profitable both years — a presentation effect the notes never explain, and one the AR's own accounting policy (Note 2.04(C)) could explain but never is stated to apply.
- Consolidation-only Capital Revaluation Reserve (Rs 34.84 Cr) coexisting with an explicit "no revaluation" declaration elsewhere in the same AR.
- Debt-like financing (reverse factoring, Rs 676.50 Cr, 67.6% of payables) kept off the borrowings note and routed through operating cash flow, flattering liquidity and leverage ratios.
- A deferred tax asset (Rs 59.31 Cr) recognised and grown against a subsidiary that has never turned a profit under SSWL ownership, with no disclosed forecast support.
- A Put & Call Options FX position (not a plain forward hedge) generating a Rs 32.42 Cr mark-to-market loss with no prior-year comparative and no clear P&L trail.
- Zero Key Audit Matters in either auditor's report despite the above.

### F. ONE-LINE NOTES VERDICT

The notes reveal moderate to concerning accounting practices. Key concern: two years of large, unexplained equity reserve transfers tied to an unreconciled AMW acquisition, compounded by debt-like financing kept off the borrowings note. Key strength: clean, conservative mechanics on revenue recognition, gratuity, standalone deferred tax reconciliation, and EPS dilution. Overall accounting quality: 4/10.

---

## COMPANY MEMORY LOAD-BEARING FACTS: WHAT THE NOTES SETTLE AND WHAT STAYS OPEN

**LBF3 (cash conversion / factoring / CFO)** — SETTLED on the mechanism, OPEN on the multi-quarter cash-conversion trend. The notes confirm the ~Rs 6.5 Cr year-end cash figure almost exactly (Rs 6.52 Cr, Note 12+13) and identify the factoring mechanism precisely: a payables-side Supplier Finance Arrangement (Note 25) covering Rs 676.50 Cr, 67.6% of trade payables, first-year Ind AS 7/107 disclosure with no FY25 comparative. What stays open: whether this arrangement's utilisation is stable or growing relative to the Rs 400-500 Cr limit named in LBF3 (no trend visible from one year's disclosure), and how the coherent multi-note working-capital deterioration (Finding 9) plays out into FY27 cash flow — both are Stage 3/5 items, not resolvable from the AR notes alone.

**LBF4 (AMW NCLT gain, subsidiary status, carrying value)** — PARTIALLY SETTLED and MORE OPEN QUESTIONS SURFACED than closed. Settled: AMW is 100% wholly owned (AOC-1, Note 52C), acquired via NCLT resolution plan under IBC (Note 4(II) CWIP), acquisition date 09-01-2024 via Companies Act Section 2(87)(ii) (Pass 2), and at least Rs 100 Cr of the ~Rs 138 Cr consideration was HDFC-Bank debt-funded (Pattern Finding 3). Still open, and now better characterised than before this pass: the FY24 exceptional gain itself falls outside this AR's two-year comparative window and cannot be directly re-verified here; the two-year, Rs 1,039 Cr reserve-transfer pattern (Findings 1-2) and the Rs 34.84 Cr consolidation-only Capital Revaluation Reserve (Finding 3) both trace most plausibly to AMW's acquisition accounting, and the AR's own Note 2.04(C) policy on common-control combinations is the closest the document comes to an explanation — but no note confirms it applies. The AMW AOC-1 "Turnover: 0" line and the Rs 5.37 Cr AOC-1-vs-Note-53 net-asset gap also remain unexplained. The FY25 AR, not in this corpus, is the most direct way to close the remaining gap; failing that, a direct management question (Section D, Q1-Q2) is the next-best route.

---

PASS 3 rating tally (all three passes combined, final): 🔴 Red Flag = 6 (Findings 1-6 in Section A); 🟡 Watch = 9 (Findings 7-15); 🟢 Clean/informational = revenue recognition, gratuity mechanics, standalone deferred-tax reconciliation, EPS dilution, R&D capex/opex tracking, the HDFC acquisition-loan disclosure, AMW acquisition-date/legal-basis detail, and the resolved Note 8 security-deposit gap.
