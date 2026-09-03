# STAGE 2 — NOTES TO FINANCIAL STATEMENTS — PASS 3 (PATTERN CHECK + CONSOLIDATION)
Company: MPS Ltd (MPSLTD) | Run date: 2026-09-03 | Model: claude-sonnet-5
Source: Annual Report 2025-26 (56th AR) — `Annual_Report_2022.pdf` (filename legacy/misleading;
content confirmed FY2025-26). Standalone notes printed pp.160-227; consolidated notes printed
pp.246-311; Auditor's Report pp.228-239. All figures INR lacs unless stated. Page numbers cited
are the AR's own printed page numbers (the source PDF stores two printed pages per PDF image
page, confirmed by direct spot-reads of PDF pages corresponding to printed pp.154-161, 218-227,
272-291 during this pass).

This pass re-reads the notes for PATTERNS rather than sequentially: cross-note contradictions,
numbers that do not match the primary statements, deliberately thin disclosure next to detailed
disclosure elsewhere, prior-year restatements/reclassifications, subsequent events, and
going-concern language. Several Pass 1/Pass 2 figures were re-verified directly against the
source pages during this pass (Note 51 standalone ratios, Note 28/19(b)/33(h) exceptional items,
Note 47/48/49/50, Note 2.1 basis of preparation) rather than taken on trust.

---

## PASS 3 PATTERN-CHECK FINDINGS

### P3-1. The Liberate Group write-back DOES reconcile arithmetically; Pass 2's "cannot be
reconciled" framing is corrected, but a real cross-note labeling defect remains
(Note 19(b), p.280; Note 28(d), p.283; Note 33(h)/fair-value roll-forward, p.292)
Direct re-read of Note 19(b)'s exact text: "the liability of INR 1,324.79 lacs was written back
under 'Exceptional Items (net)' for the year ended 31 March 2026. Amount of INR 1,572.68 lacs
shown as Exceptional Items (net)... This includes increase in fair value by AUD 0.44 million
(INR 247.89 lacs)... recorded as other income." **1,324.79 + 247.89 = 1,572.68 exactly** — the
two figures reconcile to the rupee. What does NOT reconcile is the LABEL: Note 28(d) calls the
full combined 1,572.68 "the liability... written back," when only 1,324.79 of it is actually the
liability write-back and 247.89 is a separately-driven fair-value gain folded into the same
Exceptional Items bucket. The Note 33(h) fair-value roll-forward's cross-reference to "note 28(c)"
(the Goodwill Impairment note) instead of the write-back note is also confirmed as a genuine
mis-reference on re-read. 🟡 Watch, downgraded from Pass 2's 🔴 characterization — the underlying
economics tie out; the notes are imprecisely drafted, not internally contradictory in substance.
This is the most important Pass 2 -> Pass 3 correction in this run.

### P3-2. Note 28(f)'s 591.07 write-back is the FY25 comparative footnote, not a FY26 sub-item —
Pass 2's implied FY26/FY25 mix-up resolved
(Note 28, p.283)
The FY26 "Liability written back" total of 2,967.64 is fully explained by items (d) 1,572.68 +
(e) 1,394.96 = 2,967.64 exactly. Footnote (f) (591.07, "remaining amount for purchase of 65%
stake of Liberate Group") explains the FY25 comparative column's write-back, consistent with the
FY25 net exceptional gain of 591.07 already reported in Pass 1. This is normal AR footnoting
practice (one footnote block serving both year columns of one table), not a contradiction. 🟢
Clean, correcting an ambiguity in how Pass 2 described the pattern.

### P3-3. Routine reclassification note confirms no undisclosed restatement beyond the AJE PPA
finalisation
(Note 50 standalone, p.225 [confirmed by direct read]; equivalent consolidated note)
"The figures for the corresponding previous year have been regrouped/reclassified, wherever
necessary to make them comparable. The impact of such reclassification/regrouping is not
material to the standalone financial statements." Standard boilerplate, but it is the only
general restatement disclosure in the filing beyond the AJE Group PPA measurement-period
adjustment (Pass 2 Finding #11, confirmed material: goodwill cut 10,165.50 -> 7,299.40, -28.2%).
🟢 Clean/routine for the general reclassification; the AJE PPA revision remains the one
substantive restatement of a prior-year reported figure.

### P3-4. No going-concern language anywhere in the filing; consistent with an unqualified,
unmodified audit opinion
Direct re-read of Note 1 (Corporate Information) and Note 2.1 (Basis of preparation, including
critical estimates and judgments, p.160-161) contains no going-concern emphasis-of-matter or
management going-concern assessment paragraph. The Auditor's Report (already reviewed in Pass 1/2
for its Key Audit Matters) carries no qualification, adverse opinion, disclaimer, or emphasis of
matter. 🟢 Clean. going_concern_language = NONE.

### P3-5. Auditor's Report elevation confirmed on direct re-read: goodwill quantified at 40% of
consolidated total assets is the auditor's own materiality framing, not an analyst inference
(Auditor's Report, consolidated KAM #3, pp.228-231, cross-checked against Note 5 goodwill total
of 37,632.09 and the Group balance sheet)
This corroborates Pass 2 Finding #9 and strengthens Pass 1 Finding #1 into the single
highest-priority item in this notes analysis. 🔴 Confirmed and retained at Rank 1.

### P3-6. No further contradictions surfaced between the segment Schedule III profit-share table
(Note 42 consolidated) and the standalone/consolidated P&L bridge; the 73.47%-profit /
66.80%-net-assets split is arithmetically consistent with the recharge-driven divergence already
flagged (Pass 1 #2, Pass 2 #15/#16). No new pattern beyond what Pass 2 already surfaced.

No other material new findings emerged from the pattern re-read (contingent liability table,
CSR compliance, ESOP trust mechanics, and the "Other Statutory Information" Nil-disclosures block
were all re-checked and remain 🟢 clean, consistent with Pass 1/2).

---

═══════════════════════════════════════════════════════
CONSOLIDATED NOTES ANALYSIS, ALL THREE PASSES COMBINED
═══════════════════════════════════════════════════════

## A. TOP 15 MOST SIGNIFICANT FINDINGS

| Rank | Finding | Note # | Rating | Why it matters |
|---|---|---|---|---|
| 1 | Corporate Learning segment goodwill impaired 1,292.54, exactly matching that CGU's goodwill fall (11,330.29→10,037.75); segment revenue -16.5%, segment profit -43.4%; a new external investor (Rodney Charles Beach) was installed as President of Corporate Learning the same year the CGU he now leads took an impairment. Auditor frames goodwill at 40% of consolidated total assets, its own top KAM. | Note 28(c)/(d), Note 5(a), Note 36; Auditor's Report | 🔴 Red Flag | Highest-priority cross-note pattern; goodwill quality and governance timing both in question in the segment carrying 40% of Group assets in this one intangible. |
| 2 | Standalone revenue grew 24.7% YoY vs only 5.7% consolidated, driven by a 761% surge in intercompany "rendering of services" billed to MPS North America LLC (434.24→3,737.81), eliminated on consolidation. Corroborated on the cost side: consolidated employee costs FELL 2.4% while standalone employee costs rose 25.4%, and the parent contributed 73.47% of consolidated profit vs only 66.80% of consolidated net assets. | Note 38(b), Note 22, Note 24, Note 42 | 🔴 Red Flag | Standalone revenue growth is materially a recharge/allocation artefact, not organic; a same-store view of true growth is closer to the 5.7% group figure. |
| 3 | Consolidated ECL allowance on receivables grew 35.4% (317.36→429.85) vs gross receivables +15.0%; the "significant increase in credit risk" ageing bucket, invisible at standalone level, grew 32.0% YoY (256.54→338.65, not merely a one-year balance as first reported); >180-day ECL coverage rose from 71.5% to 90.8%, coinciding with an AJE subsidiary policy change writing back customer advances. | Note 11, Note 34 consolidated; Note 28(e) | 🔴 Red Flag | Subsidiary-level (AJE) credit-risk deterioration is real, growing, and structurally hidden from the standalone accounts investors may default to reading. |
| 4 | Exceptional items were a net POSITIVE contributor to consolidated pre-tax profit in both FY25 (+591.07) and FY26 (+764.24), driven mainly by liability write-backs. The Liberate Group write-back reconciles arithmetically (1,324.79 liability write-back + 247.89 fair-value gain = 1,572.68) but Note 28(d) imprecisely labels the combined 1,572.68 as "the liability written back," and Note 33(h)'s cross-reference points to the wrong note (28(c) instead of the write-back note). | Note 28, Note 19(b), Note 33(h) | 🔴 Red Flag | A recurring positive "exceptional" bucket built on write-backs raises the question of whether prior-period provisioning was conservative and is now being released; the imprecise cross-note labeling makes the pattern harder, not easier, to verify from the filing. |
| 5 | Current Ratio collapsed: standalone 4.67x→2.53x (-45.82%), consolidated 1.97x→1.45x (-26.40%), both breaching the company's own 25% disclosure-materiality threshold; management attributes it to new external borrowings and the labour-code-driven jump in gratuity/leave liabilities. Verified directly against Note 51. | Note 51 standalone, p.226; Note 50 consolidated | 🔴 Red Flag / Escalate | The single largest ratio movement in the filing; a materially weaker post-acquisition-debt liquidity position that a receivables/turnover-only ratio read would miss entirely. |
| 6 | First-ever borrowing: secured ICICI Bank term loan (facility 4,200, drawn 4,025) funding the Unbound Medicine, Inc. acquisition. Company converts from a fully net-cash entity to net debt (Debt-Equity 0.11x) for the first time, with new financial covenants (DSCR, Debt/EBITDA, Debt/Net Worth) now in force; company reports full compliance. | Note 14 | 🟡 Watch | Structural balance-sheet first for the company; the covenant regime is new and untested through a downturn. |
| 7 | Two unexplained, order-of-magnitude cost-line spikes with no narrative anywhere in the notes: standalone Rent +1,478% (11.91→187.86), consolidated Royalty expense +1,977% (30.15→626.16), while standalone Royalty was flat-to-down over the same period. | Note 27 standalone/consolidated | 🔴 Red Flag | Two large, unexplained cost lines in the same filing warrant a direct management question; plausibly tied to newly acquired Unbound Medicine/AJE content-licensing arrangements but not disclosed as such. |
| 8 | Goodwill and intangibles grew 54.3%/54.8% at consolidated level on the Unbound Medicine and AJE acquisitions, but amortisation expense FELL slightly in FY26 (only a partial year, ~7 weeks, of Unbound Medicine amortisation hit the P&L). Separately, the AJE Group purchase price allocation was materially revised ~13 months post-acquisition: goodwill cut 10,165.50→7,299.40 (-28.2%), reallocated to a new DTA of 2,360.06 and reversal of a DTL of 688.91. | Note 5, Note 26, Note 40(b) | 🟡 Watch / restatement | A materially larger amortisation charge should be expected in FY27; the AJE PPA revision is a genuine, disclosed retrospective revision of a previously reported figure, sitting at the edge of Ind AS 103's 12-month measurement window. |
| 9 | Gratuity and compensated-absence obligations swelled sharply (gratuity PVO +58.0%, standalone compensated-absence net liability +578.9%) due to the newly notified Labour Codes (21-Nov-2025), transparently disclosed as a one-time Exceptional Item (611.30 standalone / 701.44 consolidated). | Note 32, Note 28(b) | 🟡 Watch | Well explained and one-time by disclosure, but a material balance-sheet swing (and a direct driver of Finding 5's current-ratio collapse) to confirm does not recur in FY27. |
| 10 | Standalone customer concentration is high and rising: top 3 customers = 39.0% of revenue (FY26) vs top 2 = 30.1% (FY25); top 15 = 78.8% of revenue. Consolidated concentration is milder and improving (top 1 customer 17.3% vs 18.6%). | Note 35(ii), Note 34(ii) | 🟡 Watch | Standalone-entity revenue is increasingly dependent on very few counterparties, a different risk profile than the group-level picture suggests. |
| 11 | Consolidated Auditor's Report carries THREE Key Audit Matters (revenue recognition; the Unbound Medicine business combination; goodwill impairment, with goodwill framed as 40% of Group total assets), versus the single KAM in the standalone report that a reader focused only on standalone filings would see. | Auditor's Report pp.228-231 | 🟡 Watch / Elevate | Reinforces Finding 1; the auditor's own risk assessment is broader at group level than at standalone level. |
| 12 | Title deeds for freehold land and buildings (PP&E + investment property, combined ~1,186.33 lacs, roughly 48% of the Company's total PP&E + investment property net book value) remain in the names of erstwhile partnership/merged entities (HASCO Associates structure, Brigade Marketing Company Pvt Ltd), unresolved since 1993/2000 across multiple court-approved schemes. | Note 3.1.1/3.2 standalone; Note 3.2 consolidated | 🟡 Watch | A three-decade-old administrative gap on title deeds; no current dispute disclosed, but relevant to the pending ADI BPO amalgamation and to any future financing or sale of these properties. |
| 13 | Forward currency book: USD forward-sell notional up 72.4% (FC 47.00 lacs→81.00 lacs); a first-ever net "Unrealised loss payable on forward covers" (358.56 vs Nil) appears alongside a new DTA "Unrealised MTM gain receivables" (90.22) in the same year — a gross, directionally mixed hedge book. Net USD balance-sheet exposure grew 27.2% (8,170.29→10,394.94). | Note 35(iii), Note 18, Note 16 standalone | 🟡 Watch | Rising USD concentration plus a swing to a net hedging loss position in the same year revenue growth quality is already in question (Finding 2). |
| 14 | Major pending related-party corporate action: Board-approved amalgamation of holding company ADI BPO Services Limited into MPS Limited, NCLT Chennai approval pending as of the 15-May-2026 report date. The Group's accounting policy for common-control mergers requires retrospective restatement of comparatives once effective. | Note 48/47, Note 2.4 | 🟡 Watch | A significant structural event with a built-in restatement mechanism that has not yet fired; a live item to track into FY27. |
| 15 | Audit-trail (edit-log) control gap at the database level of the accounting software during FY26, disclosed at both standalone and consolidated level (application-level logs were retained). Separately, four overseas subsidiaries (≈14.4% of consolidated revenue) were audited by other auditors, not the principal auditor, on a newly acquisitive group. | Note 47/46; Auditor's Report Other Matter paras 15-16 | 🟡 Watch | Governance/IT-control disclosure item, industry-wide in Indian filings, compounded here by meaningful reliance on other auditors for newly acquired entities in the same year. |

## B. ACCOUNTING QUALITY SCORE (1-10)

| Dimension | Score /10 | Rationale |
|---|---|---|
| Revenue recognition conservatism | 5 | POC method is the sole/lead KAM industry-wide; standalone revenue growth (24.7%) is materially inflated by a 761% intercompany recharge surge eliminated on consolidation (Finding 2). Group-level 5.7% growth is closer to organic reality. |
| Expense capitalisation honesty | 7 | No evidence of aggressive capitalisation; IAUD fully and cleanly capitalised on completion with no impairment; ROU step-change explained by disclosed lease additions, not opex-to-balance-sheet shifting. |
| Provisioning adequacy | 5 | Mixed: consolidated ECL coverage is rising (conservative direction) on aged receivables, but the PF Supreme Court provision is unquantified, and two consecutive years of net-positive "exceptional" items built on write-backs raise a legitimate question of whether prior-period provisions were set conservatively and are now being released into profit (Finding 4). |
| RPT fairness | 5 | Standard arm's-length boilerplate asserted; no non-arm's-length signal flagged by the company or auditor, but the scale and direction of the intercompany services recharge (Finding 2) materially shapes reported standalone performance and deserves scrutiny beyond the boilerplate assurance. |
| Disclosure transparency | 6 | Extensive, detailed notes overall (ageing tables, sensitivity analyses, segment detail, PPA disclosures), but undercut by two unexplained cost-line spikes with zero narrative (Finding 7), imprecise cross-note labeling on the Liberate write-back with a misdirected cross-reference (Finding 4), and a disclosure-placement gap on the App-eLearn Pty Ltd dissolution. |
| Consistency with prior years | 6 | One genuine, disclosed restatement (AJE Group PPA revision, -28.2% goodwill, Finding 8); routine immaterial reclassification is separately and properly disclosed (Note 50); no undisclosed restatements found on the pattern re-read. |
| **OVERALL** | **6** | Extensive, unqualified disclosure with no fraud indicators, clean audit opinion, and improving group-level credit provisioning discipline in places, set against real revenue-growth-quality and cross-note-consistency concerns that keep this at "moderate" rather than "clean." |

## C. KEY RISKS FROM NOTES

| Risk | Severity | What to monitor | When it could hit |
|---|---|---|---|
| Standalone revenue quality (intercompany recharge inflation) | High | FY27 intercompany "rendering of services" growth rate vs standalone revenue growth; standalone-vs-consolidated growth gap | Q1 FY27 results, FY27 AR Note 38/22 |
| Corporate Learning goodwill/segment | High | Further impairment testing on the Corporate Learning CGU; Beach/Liberate integration progress; segment revenue and profit trend | H1 FY27 impairment review, FY27 interim/annual results |
| Consolidated (AJE) receivable credit quality | Medium-High | "Significant increase in credit risk" ageing bucket trend; ECL coverage ratio on >180-day bucket; recurrence of customer-advance write-backs | Each quarter; FY27 AR Note 11/34 |
| Liquidity/leverage post-acquisition-debt | Medium | Current ratio trend; covenant compliance (DSCR, Debt/EBITDA, Debt/Net Worth); any further acquisition-linked borrowing | Each covenant testing date; FY27 AR |
| Unexplained cost-line spikes (Rent, Royalty) | Medium | Management clarification; whether the spikes recur or reverse in FY27 | Next quarterly filing or investor call |
| FY27 amortisation step-up on acquired intangibles | Medium | Full-year amortisation impact on consolidated EPS once Unbound Medicine/AJE intangibles amortise for a full year | FY27 annual results |
| Pending ADI BPO amalgamation / restatement mechanism | Medium | NCLT Chennai hearing outcome; scope and timing of any retrospective comparative restatement | NCLT ruling date; FY27 AR |

## D. FIVE QUESTIONS FOR MANAGEMENT

1. What specifically explains the 761% jump in intercompany "rendering of services" billed to MPS North America LLC, and is part of the Group's underlying delivery cost migrating from the US subsidiary's books to the Indian parent's (consistent with consolidated employee costs falling 2.4% while standalone employee costs rose 25.4%)? Is the recharge benchmarked and audited at arm's length under transfer-pricing rules?
2. What drove standalone Rent expense up roughly 16x (11.91 to 187.86 lacs) and consolidated Royalty expense up roughly 20x (30.15 to 626.16 lacs) in FY26, given no note anywhere explains either movement?
3. On the Liberate Group liability write-back: can management confirm the bridge of 1,324.79 lacs (liability write-back) + 247.89 lacs (fair-value gain) = 1,572.68 lacs (Exceptional Items), and correct the Note 33(h) cross-reference that currently points to Note 28(c) (Goodwill Impairment) instead of the write-back note?
4. Has any prior-period comparative already been restated in anticipation of the ADI BPO Services Limited amalgamation, and what is the expected accounting and P&L impact once NCLT Chennai approves the scheme?
5. What is the quantum of the provision recognised for the 2019 EPF Supreme Court judgment (Note 39(ii)), and why is this the one item in the filing where a recognised provision's rupee amount is not disclosed?

## E. NOTES-BASED RED FLAGS

- Intercompany revenue recharge (761% YoY surge) materially inflates standalone revenue growth relative to the consolidated, arguably-more-organic 5.7% figure — a revenue-growth-quality flag, not a fabrication, but material to interpreting standalone-level metrics.
- Recurring net-positive "exceptional items" in both FY25 and FY26, driven substantially by liability and provision write-backs rather than genuine one-off costs — a pattern consistent with (though not proof of) earlier conservative over-provisioning being released into current-period profit.
- Two unexplained, order-of-magnitude cost-line spikes (Rent, Royalty) with zero disclosed narrative.
- Cross-note labeling and cross-referencing defects on the Liberate Group write-back (figures reconcile; labels and one cross-reference do not) — a disclosure-quality flag, not a numerical discrepancy.
- Consolidated (AJE-subsidiary) credit-risk deterioration that is structurally invisible at the standalone level.
No evidence of undisclosed restatements, qualified audit opinion, benami/crypto/struck-off-company dealings, or going-concern uncertainty.

## F. ONE-LINE NOTES VERDICT

The notes reveal moderate accounting practices, with real disclosure depth undercut by
internal-consistency gaps. Key concern: an intercompany recharge inflates standalone revenue
growth quality while exceptional items lean on recurring write-backs. Key strength: extensive,
unqualified disclosure with no fraud indicators and improving group-level credit provisioning
discipline. Overall accounting quality: 6/10.

---

## WHERE PASS 2 AND PASS 3 CORRECTED PASS 1

- **Liberate write-back reconciliation break (Pass 2 Finding #13) → corrected in Pass 3 (P3-1,
  P3-2):** the two rupee figures (1,324.79 and 1,572.68) DO reconcile exactly once the 247.89
  fair-value-gain component is added back; the defect is imprecise labeling in Note 28(d) and a
  misdirected cross-reference in Note 33(h), not an unreconcilable numerical break. Severity
  downgraded accordingly in the consolidated Top 15 (Rank 4), while still carried forward as a
  disclosure-quality red flag.
- **Current-ratio collapse (Pass 2 Finding #6):** entirely absent from Pass 1's ratio coverage,
  which reported only the immaterial Trade Receivable Turnover Ratio move. Verified directly
  against Note 51 in Pass 3 (4.67x→2.53x standalone, -45.82%; 1.97x→1.45x consolidated, -26.40%,
  both breaching the company's own 25% materiality threshold). Retained at Rank 5, escalated.
- **ECL/credit-risk mis-anchor (Pass 2 Finding #8):** Pass 1 reported the "significant increase in
  credit risk" ageing bucket as "256.54 (FY26)... entirely zero at standalone level," when 256.54
  is actually the FY25 comparative and the FY26 figure is 338.65 (+32.0% YoY). Corrected in the
  consolidated Top 15 (Rank 3) to reflect the worse, more established deterioration trend.

## PASS 3 SUMMARY

Pattern re-read surfaced one significant correction to Pass 2 (the Liberate write-back reconciles
arithmetically; the defect is drafting precision, not a numerical break), confirmed the absence of
any going-concern language, confirmed no undisclosed restatements beyond the already-flagged AJE
Group PPA revision, and directly verified the current-ratio and ECL/credit-risk figures against
source pages. This is not "PASS 3: NO MATERIAL NEW FINDINGS" — the reconciliation correction
itself is a material refinement carried into the consolidated Top 15 and dimension scoring above.
