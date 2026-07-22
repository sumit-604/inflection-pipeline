# STAGE 2 — NOTES TO FINANCIAL STATEMENTS, PASS 3 (PATTERN PASS + CONSOLIDATION)
Company: Laxmi India Finance Ltd (LAXMIINDIA), NBFC-ML (MSME/mortgage/vehicle lender)
Run date: 2026-07-22

SOURCES:
- **[PROSPECTUS]** = inputs/annual-report/drhp.pdf (Prospectus dated 2025-07-31), Restated Financial
  Statements, Notes 1-105, printed pp.289-386. Figures converted to ₹ Cr from ₹ Millions (÷10).
- **[FY26RESULTS]** = inputs/results/Annual_Report_2024.pdf (misnamed; actually the FY26 Audited Results
  filing under Reg 33/52 SEBI LODR, board meeting 13-May-2026), 29 pp, Notes 1-13. Figures converted to
  ₹ Cr from ₹ Lakhs (÷100).

Spot-verification performed in Pass 3 against source PDF pages for Note 79/80 (ECL-vs-IRACP table, BSE
penalty table) and Note C.3 (ECL staging/definition-of-default policy language) confirms Pass 1/2 figures
and quotations are faithful to source; no transcription errors found in the sampled anchors.

---

## PASS 3: PATTERN PASS

Re-reviewed the notes package specifically for: (i) notes that contradict each other, (ii) notes-vs-main-
statement mismatches, (iii) deliberately thin disclosure relative to other notes, (iv) prior-year
restatements/reclassifications, (v) post-balance-sheet events, (vi) going-concern language.

Categories (iv), (i)/(ii), and (vi) were already substantively surfaced in Pass 2 (the accrual-to-cash
policy change and four Note 104 restatement items; the ~180x Note 98(c)-vs-Note 75/5.7 reconciliation gap;
the Note 59 going-concern paragraph in tension with the Company's own rising-Stage-3 disclosure). A
further contradiction-focused read did not surface additional unreconciled note-pairs beyond what Pass 2
already found. One additional pattern observation, not previously stated as such:

- **The Company's own disclosure register shows a consistent pattern of "correction only under external
  scrutiny"**: the four Note 104 GAAP errors were caught during IPO due-diligence (external, by a new
  auditor engaged for the listing), not the ordinary audit cycle; the BSE listing-compliance penalties
  (Note 80) were externally imposed, not self-reported remediation; and the audit-trail deficiency was
  narrowed only after auditor change, not self-initiated. Individually each item was already flagged in
  Pass 1/2; taken together as a *pattern* they support treating "no further undetected issues" as an
  unverified assumption rather than a reasonable default, since the Company's own track record shows
  internal detection has repeatedly lagged external review across three separate control domains
  (GAAP application, IT audit-trail, listing compliance).

No further material new findings emerged. **PASS 3: material new findings limited to the one synthesis
observation above; no new anchored facts beyond Pass 1/2.**

---

## CONSOLIDATED NOTES ANALYSIS, ALL THREE PASSES COMBINED

### A. TOP 15 MOST SIGNIFICANT FINDINGS

| Rank | Finding | Note # | Rating | Why it matters |
|---|---|---|---|---|
| 1 | DA/ARC upfront gain-on-sale is a large, judgment-dependent, non-cash driver of reported PAT: ₹9.63cr (FY25, 26.8% of PAT ₹36.01cr), ₹15.19cr (FY24, 67.6% of PAT ₹22.47cr), ₹12.15cr (FY23, 76.1% of PAT ₹15.97cr). | [PROSPECTUS] Note 52.2/98(a), pp.355,379 | 🔴 Red Flag | Core lending profitability ex-gain is materially thinner than headline PAT in FY23/FY24; the single biggest earnings-quality question for the Company. |
| 2 | Four material GAAP errors in the original FY23/FY24 audited financials (business-correspondence treatment, missing ECL on DA receivable, ARC upfront-gain non-recognition, wrong software capitalisation) were corrected only via restatement during IPO prep by a new auditor; the previous statutory auditor did not catch them across two audit cycles. | [PROSPECTUS] Note 104(a)-(d), p.383 | 🔴 Red Flag | Raises a direct question about pre-IPO financial-control rigor and whether smaller uncorrected misstatements remain in periods outside the restatement's scope. |
| 3 | Stressed-loan (NPA+SMA) transfers to ARC jumped >36x FY24→FY25 (₹7.27cr combined principal to ₹264.8cr), and for the first time included SMA (pre-NPA, 1-89 DPD) accounts, not just NPA. | [PROSPECTUS] Note 98(c), p.379 | 🔴 Red Flag | Selling not-yet-NPA accounts to an ARC is atypical; raises the question of whether asset-quality stress was pre-emptively transferred off-book in FY25, ahead of the FY26 Up Money DA-pool stress event. |
| 4 | Note 98(c)'s FY25 NPA-transferred-to-ARC figure (₹109.54cr) is ~9x the Company's entire Stage-3 book at FY25-end (₹12.18cr) and ~180x the "Sold to ARC" line (₹0.61cr) in the Stage-3 roll-forward for the same year, with no narrative cross-reference reconciling the two views. | [PROSPECTUS] Note 98(c) p.379 vs Note 75 p.368 / Note 5.7 p.318 | 🔴 Red Flag | A numbers-in-notes-do-not-match pattern that needs direct management clarification before either figure can be relied on as a complete description of NPA disposition. |
| 5 | FY26 Investments (dominated by ARC Security Receipts) grew 5.4x in one year (₹29.27cr→₹158.91cr) vs loan book growth of ~31.3%; Investments/Total Assets rose from ~2.1% to ~8.7%. | [FY26RESULTS] Balance Sheet | 🔴 Red Flag | A fast-rising share of the balance sheet sits in illiquid, NAV-marked ARC-trust paper rather than realised cash, in the very year of the Up Money stress event; materially worsens the FY23-FY25 trend already flagged. |
| 6 | Previous auditor's qualified opinion on audit-trail (edit-log) non-implementation for FY23 and FY24; current auditor flags a narrower but still-unresolved gap for FY25 (one disable/re-enable instance; SOC-2 unavailable for loan-collection software). | [PROSPECTUS] p.290-291 | 🔴 Red Flag | A recurring IT-governance control weakness across two audit firms and three years is a data-integrity concern for a lender whose staging/ECL disclosures depend entirely on system-generated records. |
| 7 | Gross Stage-3/Total Loans ratio rose from 0.58% (FY23) to 0.73% (FY24) to 1.07% (FY25); gross NPA more than tripled (₹3.33cr→₹5.97cr→₹12.18cr); MSME/LAP segment shows the clearest deterioration. | [PROSPECTUS] Note 75/93(d), pp.368,377 | 🟡 Watch | The FY26 Up Money-related GNPA spike sits atop an already-rising organic pre-IPO NPA trend, softening the "one-off DA-partner problem" framing. |
| 8 | Customer complaints rose from 18 (FY23) to 123 (FY24) to 341 (FY25), +283% YoY in FY25 vs ~38% loan-book growth; CIC-related complaints rose 11→64→245. Partially offset: 100% Company-favourable resolution rate before the RBI Ombudsman in all three years (32/32 cumulative). | [PROSPECTUS] Note 96/96(a), pp.377-378 | 🟡 Watch | Disproportionate complaint growth (esp. credit-bureau-related) warrants a direct collections-conduct question, though the clean independent-adjudication record is a genuine mitigant. |
| 9 | Three non-reconciling write-off figures across two filings for overlapping scope (Note 29.1 core book write-offs; Note 98(c) footnote ARC-sale write-offs ₹4.614cr FY25; FY26RESULTS Note 9.4 footnote ₹2.77cr labelled "year ended March 31, 2025" inside an FY26-dated table). | [PROSPECTUS] Notes 29.1, 98(c); [FY26RESULTS] Note 9.4 | 🟡 Watch / Question | Needs management confirmation of which year each figure describes before any single write-off number can be anchored with confidence for FY26. |
| 10 | Going-concern paragraph asserts "lower gross NPA and net NPA," templated/carried-forward language, in tension with the Company's own Note 75/93(d) showing Gross Stage-3 nearly doubling FY23-FY25 and Note 98(c)'s >36x FY25 stressed-transfer jump. | [PROSPECTUS] Note 59, p.364 | 🟡 Watch | This is the pattern-pass "going concern language" item; the assertion does not hold up against the Company's own concurrent disclosures. |
| 11 | Fee & commission income grew ~201% YoY in FY25 (₹4.47cr→₹13.46cr), ~5x faster than loan-book growth (~38%), driven by pre-closure (+330%) and instrument-return (+516%) charges. | [PROSPECTUS] Note 25, p.337 | 🟡 Watch | Disproportionate fee growth coincides with the same period's accrual-to-cash accounting-policy change for these fee categories; worth a direct management question on genuine pricing power vs recognition-timing effect. |
| 12 | CFO (Feb-2024) and Company Secretary (Oct-2023) both turned over during the exact FY23-FY24 window in which the four Note 104 GAAP errors originated and went undetected by the then-statutory auditor. | [PROSPECTUS] Note 47(A)(b), p.350 | 🟡 Watch | Relevant control-environment context for the error period; not proof of cause but a coincidence of timing worth naming. |
| 13 | Promoter and promoter-group entities give personal/corporate guarantees securing essentially all secured Company debt across all three years; title to one PPE property (₹0.28cr) remains in the MD's personal name 14+ years post incorporation-conversion. | [PROSPECTUS] Notes 15.1, 16.2, 47(E), 99, 9.4 | 🟡 Watch | Structural funding-cost/covenant dependency on continued promoter credit support, and an unresolved governance-hygiene formality, both worth monitoring as promoter shareholding dilutes post-IPO. |
| 14 | Contingent liabilities disclosure is unusually thin for an NBFC of this scale: a single ₹0.09cr income-tax demand is the only item shown in any of three years; no guarantee, litigation, or securitisation-recourse contingent items disclosed despite active DA/ARC volumes. | [PROSPECTUS] Note 46, p.349 | 🟡 Watch | Plausible under Ind AS derecognition mechanics but the note gives no narrative cross-reference to Note 52/98 to make this explicit; a disclosure-transparency gap worth direct management confirmation. |
| 15 | CRAR declined steadily pre-IPO (23.09%→21.81%→20.80% FY23-FY25) while Debt/Equity rose (4.04x→3.80x→4.42x); both reversed post-IPO (FY26 CRAR 26.12%, D/E ~2.87-2.88x). | [PROSPECTUS] Note 74/100, pp.374,381; [FY26RESULTS] Reg 52(4) Annexure | 🟢 Clean (resolved) | Confirms IPO proceeds were structurally necessary to correct a genuinely tightening pre-IPO capital trajectory, not purely growth optionality; post-IPO metrics are healthy. |

### B. ACCOUNTING QUALITY SCORE (1-10)

| Dimension | Score | Basis |
|---|---|---|
| Revenue recognition conservatism | 4/10 | DA/ARC upfront gain-on-sale is judgment-heavy and was entirely mis-recognised (not booked) in the original FY23/FY24 audited financials; now the dominant PAT driver in two of three restated years. SMA-inclusion in FY25 ARC sales adds a further judgment layer to what counts as "derecognition." |
| Expense capitalisation honesty | 6/10 | One software-licence capitalisation error corrected via restatement (Note 104(d)); otherwise depreciation policy (WDV, Schedule II lives, 5% residual) is standard and consistently applied; no other capitalisation aggressiveness found. |
| Provisioning adequacy | 8/10 | ECL provisions exceed the RBI IRACP regulatory minimum in every year shown (FY25 ₹13.33cr vs ₹6.51cr required); Stage-3 coverage improving (45.6%→54.4%→55.2% FY23-FY25); no impairment-reserve transfer required. Conventional staging/default definition, no stretching. |
| RPT fairness | 7/10 | RPTs small relative to revenue (~2.6% FY25); no related-party ICDs/loans outstanding; but promoter/promoter-group guarantees underpin nearly all secured debt (a structural, non-P&L dependency) and a small CSR routing through a KMP-controlled trust is a minor self-dealing-adjacent item. |
| Disclosure transparency | 4/10 | Contingent-liability note is strikingly thin with no cross-reference to the much larger DA/ARC activity elsewhere; the Note 98(c)/Note 75 NPA-to-ARC figures do not reconcile with no narrative bridge; going-concern language is stale/templated and contradicts concurrent disclosures; three write-off figures across two filings do not reconcile. |
| Consistency with prior years | 3/10 | Three-plus material GAAP errors restated, auditor changed mid-restatement, CFO/CS turnover in the error-origination window, and an audit-trail qualification persisting (narrower) across the auditor change — a weak multi-year consistency record. |
| **OVERALL** | **5/10** | Provisioning discipline and RPT scale are genuine strengths; revenue-recognition judgment on DA/ARC transactions, disclosure-reconciliation gaps, and the restatement/audit-trail history are the dominant drags. A capable but not yet fully trustworthy reporting apparatus, materially improved by IPO-driven scrutiny but with unresolved cross-note reconciliation questions that a management response could either resolve cleanly or turn into a bigger issue. |

### C. KEY RISKS FROM NOTES

| Risk | Severity | What to monitor | When it could hit |
|---|---|---|---|
| DA/ARC gain-on-sale earnings-quality dependency | High | Core NII + fee income ex-DA/ARC-gain run-rate each quarter; DA-pool performance (esp. post-Up Money) | Already partly realised (FY26 Up Money stress); further hits possible each results cycle as pools season |
| Off-book asset-quality masking via rising ARC SR balance | High | SR carrying value vs loan book growth; cash recovery vs NAV marks; Infomerics recovery-rating changes | FY27 as SR trusts mature and NAV marks are tested against actual recoveries |
| Unreconciled NPA-to-ARC and write-off figures across notes | Medium-High | Management clarification/restated note in next annual filing; consistency of population definitions | Next annual report or direct management response |
| Control-environment history (restatement, audit-trail qualification, CFO/CS turnover) | Medium | Next statutory audit report's audit-trail language; any further restatements or auditor changes | Each annual audit cycle (FY26 audit due) |
| Customer complaint growth / collections conduct | Medium | CIC-related complaint trend vs RBI Ombudsman outcomes; regulatory correspondence | Ongoing; escalates if Ombudsman record deteriorates |
| Promoter guarantee dependency on secured funding | Medium-Low | Promoter shareholding/net worth trend; any guarantee release or replacement schedule | If promoter dilution accelerates or promoter financial stress emerges |
| New off-book exposure: co-lending 5% Default Loss Guarantee, ₹400cr NCD authorisation | Low (currently) | CLA utilisation/DLG drawdown; pace of NCD private-placement drawdown vs authorisation | FY27 as both channels scale from near-zero base |

### D. FIVE QUESTIONS FOR MANAGEMENT

1. Please reconcile Note 98(c)'s FY25 NPA-transferred-to-ARC principal (₹109.54cr) against the Stage-3
   "Sold to ARC" line in Note 75/Note 5.7 (₹0.61cr) for the same fiscal year — what population or
   definitional difference (gross original principal vs Ind AS 109 carrying amount; cumulative multi-year
   pool vs single-year Stage-3 flow) explains the ~180x gap?
2. What is core lending profitability (net interest income plus fee income, excluding DA/ARC upfront
   gain-on-sale) for FY23 through FY26, and what is management's view on whether DA/ARC gain
   recognition will normalise or continue to be a first-order driver of reported PAT?
3. Please confirm which fiscal year the FY26 results filing Note 9.4 write-off footnote (₹2.77cr,
   labelled "year ended March 31, 2025" inside a table dated as at 31-Mar-2026) actually describes, and
   reconcile it against the DRHP's Note 98(c) FY25 ARC-sale write-off figure of ₹4.614cr.
4. Why did the Company begin selling SMA (pre-NPA, 1-89 DPD) accounts to ARCs for the first time in
   FY25 (₹155.27cr principal, 470 accounts) — is this a change in credit-risk management philosophy, or
   pre-emptive transfer of stress ahead of the book seasoning into reported GNPA?
5. What is the remediation timeline for the persisting audit-trail deficiency (one instance of the
   feature being disabled/re-enabled in FY25; SOC-2 report unavailable for the loan-collection software),
   and what root-cause analysis has been done on why the four Note 104 GAAP errors went undetected by the
   previous statutory auditor across two audit cycles?

### E. NOTES-BASED RED FLAGS

- DA/ARC upfront gain-on-sale represented 76.1% of PAT (FY23) and 67.6% of PAT (FY24), moderating to
  26.8% (FY25); a judgment-dependent, largely non-cash gain recognised on derecognition, not cash-realised
  core lending income (Note 52.2/98(a)).
- The original (pre-restatement) audited FY23/FY24 financials had not recognised this DA/ARC gain at all,
  along with three other material errors (BC transaction treatment, missing ECL on a DA receivable, wrong
  software capitalisation), all corrected only via restatement during IPO preparation by a new auditor,
  undetected by the previous statutory auditor across two audit cycles (Note 104).
- Two consecutive years of CARO/audit-trail non-implementation qualification by the previous auditor; a
  narrower but unresolved audit-trail gap persists under the new auditor in FY25 (p.290-291).
- Stressed-loan transfers to ARC jumped >36x FY24→FY25 (₹7.27cr→₹264.8cr combined NPA+SMA principal) and
  for the first time included SMA (pre-NPA) accounts — an atypical population for ARC disposal (Note
  98(c)).
- An unreconciled ~180x gap exists between Note 98(c)'s NPA-transferred-to-ARC figure and Note 75/5.7's
  Stage-3 "Sold to ARC" roll-forward line for the same fiscal year, with no narrative bridge in the notes.
- FY26 Investments (ARC Security Receipts) grew 5.4x in one year versus ~31% loan-book growth, a
  fast-rising share of the balance sheet in illiquid, NAV-marked paper rather than realised cash
  ([FY26RESULTS] balance sheet).
- The going-concern paragraph's assertion of "lower gross NPA and net NPA" (Note 59) is templated language
  in direct tension with the Company's own concurrent Note 75/93(d) disclosure of Gross Stage-3 nearly
  doubling FY23-FY25.

### F. ONE-LINE NOTES VERDICT

The notes reveal moderate-to-concerning accounting practices, with strong ECL provisioning discipline
offset by a restated GAAP-error history and an unreconciled ARC/NPA disclosure trail. Key concern: DA/ARC
gain-on-sale accounting and off-book stressed-loan transfers dominate reported earnings and asset quality
in ways the notes package does not fully reconcile against itself. Key strength: Ind AS 109 ECL
provisioning consistently exceeds the RBI regulatory floor with improving Stage-3 coverage, and RPTs are
small in scale with no related-party loans outstanding. Overall accounting quality: 5/10.

---

```yaml
stage: B02-notes
company: "LAXMIINDIA"
run_date: "2026-07-22"
model: claude-sonnet-5
status: complete
input_gaps: [announcements, shareholding, research, laxmiindia_screening]
flags:
  - type: FLAG-CASH
    reason: "DA/ARC upfront gain-on-sale drove 76.1% of PAT (FY23) and 67.6% of PAT (FY24), moderating to 26.8% (FY25) (Note 52.2/98(a), pp.355,379); ARC Security Receipt investments grew 5.4x in FY26 alone vs ~31% loan-book growth (FY26RESULTS balance sheet), meaning a rapidly rising share of the balance sheet is illiquid NAV-marked ARC paper rather than cash from stressed-asset disposals; the Note 98(c) NPA-transferred-to-ARC figure (Rs109.54cr FY25) and the Note 75/5.7 Stage-3 roll-forward Sold-to-ARC line (Rs0.61cr FY25) are unreconciled (~180x gap), and three separate write-off figures across two filings also do not reconcile. Cash conversion quality is INDETERMINATE pending management reconciliation of these figures; caps at PROCEED WITH CAVEATS per Master v3.3, missing evidence named above."
accounting_quality: 5   # /10
pass_2_empty: false
pass_3_empty: false
top_findings:
  - {rank: 1, finding: "DA/ARC upfront gain-on-sale is a large, judgment-dependent driver of PAT: 26.8% (FY25), 67.6% (FY24), 76.1% (FY23) of PAT", note_ref: "Note 52.2/98(a), pp.355,379", rating: "RED", why: "Core lending profitability ex-gain is materially thinner than headline PAT in FY23/FY24"}
  - {rank: 2, finding: "Four material GAAP errors in original FY23/FY24 audited financials corrected only via restatement during IPO prep; previous auditor did not catch them across two audit cycles", note_ref: "Note 104(a)-(d), p.383", rating: "RED", why: "Raises question about pre-IPO financial-control rigor and whether smaller uncorrected misstatements remain elsewhere"}
  - {rank: 3, finding: "Stressed-loan (NPA+SMA) transfers to ARC jumped >36x FY24-FY25 (Rs7.27cr to Rs264.8cr combined principal), first year including SMA (pre-NPA) accounts", note_ref: "Note 98(c), p.379", rating: "RED", why: "Atypical population for ARC sale; raises question of pre-emptive off-book transfer of stress ahead of FY26 Up Money event"}
  - {rank: 4, finding: "Note 98(c) FY25 NPA-transferred-to-ARC figure (Rs109.54cr) is ~180x the Note 75/5.7 Stage-3 roll-forward Sold-to-ARC line (Rs0.61cr) for the same year, unreconciled", note_ref: "Note 98(c) p.379 vs Note 75 p.368/Note 5.7 p.318", rating: "RED", why: "Numbers-in-notes-do-not-match pattern requiring direct management clarification"}
  - {rank: 5, finding: "FY26 Investments (ARC Security Receipts) grew 5.4x in one year vs ~31% loan-book growth; Investments/Total Assets rose ~2.1% to ~8.7%", note_ref: "FY26RESULTS Balance Sheet", rating: "RED", why: "Fast-rising share of balance sheet in illiquid NAV-marked paper rather than realised cash, in the year of the Up Money stress event"}
  - {rank: 6, finding: "Previous auditor qualified audit-trail non-implementation for FY23/FY24; narrower but unresolved gap persists under new auditor in FY25", note_ref: "p.290-291", rating: "RED", why: "Recurring IT-governance control weakness across two audit firms and three years; data-integrity concern for staging/ECL disclosures"}
  - {rank: 7, finding: "Gross Stage-3/Total Loans rose 0.58% (FY23) to 0.73% (FY24) to 1.07% (FY25); gross NPA more than tripled", note_ref: "Note 75/93(d), pp.368,377", rating: "YELLOW", why: "FY26 Up Money GNPA spike sits atop an already-rising organic pre-IPO NPA trend"}
  - {rank: 8, finding: "Customer complaints rose 18/123/341 FY23-FY25 (+283% YoY FY25) vs ~38% loan growth; but 100% Company-favourable RBI Ombudsman resolution rate all three years (32/32)", note_ref: "Note 96/96(a), pp.377-378", rating: "YELLOW", why: "Disproportionate complaint growth warrants a collections-conduct question, though independent-adjudication record is a genuine mitigant"}
  - {rank: 9, finding: "Three non-reconciling write-off figures across two filings for overlapping scope (Note 29.1, Note 98(c) footnote Rs4.614cr FY25, FY26RESULTS Note 9.4 Rs2.77cr mislabelled)", note_ref: "Note 29.1, 98(c); FY26RESULTS Note 9.4", rating: "YELLOW", why: "Needs management confirmation of which year each figure describes before anchoring any FY26 write-off number"}
  - {rank: 10, finding: "Going-concern paragraph asserts 'lower gross NPA and net NPA', templated language in tension with Company's own rising Stage-3 disclosure", note_ref: "Note 59, p.364", rating: "YELLOW", why: "Assertion does not hold up against the Company's own concurrent disclosures"}
  - {rank: 11, finding: "Fee & commission income grew ~201% YoY FY25 vs ~38% loan-book growth, ~5x faster", note_ref: "Note 25, p.337", rating: "YELLOW", why: "Coincides with the accrual-to-cash policy change for these fee categories; worth a pricing-power vs recognition-timing question"}
  - {rank: 12, finding: "CFO (Feb-2024) and Company Secretary (Oct-2023) both turned over during the exact window the four restated GAAP errors originated", note_ref: "Note 47(A)(b), p.350", rating: "YELLOW", why: "Relevant control-environment context for the error period; coincidence of timing, not proof of cause"}
  - {rank: 13, finding: "Promoter/promoter-group guarantees secure essentially all secured Company debt; one PPE property title remains in MD's personal name 14+ years post incorporation-conversion", note_ref: "Notes 15.1, 16.2, 47(E), 99, 9.4", rating: "YELLOW", why: "Structural funding dependency on promoter credit support and an unresolved governance-hygiene item"}
  - {rank: 14, finding: "Contingent liabilities disclosure unusually thin for NBFC scale: only a Rs0.09cr tax demand shown in any year, no cross-reference to DA/ARC activity", note_ref: "Note 46, p.349", rating: "YELLOW", why: "Plausible under Ind AS mechanics but a disclosure-transparency gap worth direct management confirmation"}
  - {rank: 15, finding: "CRAR declined pre-IPO (23.09% to 20.80% FY23-FY25) and D/E rose (4.04x to 4.42x), both reversed post-IPO (FY26 CRAR 26.12%, D/E ~2.87x)", note_ref: "Note 74/100, pp.374,381; FY26RESULTS Reg 52(4) Annexure", rating: "GREEN", why: "Confirms IPO proceeds were structurally necessary; post-IPO capital metrics are healthy"}
red_flags:
  - "DA/ARC upfront gain-on-sale drove 76.1% of PAT (FY23), 67.6% (FY24), 26.8% (FY25) (Note 52.2/98(a))"
  - "Original FY23/FY24 audited financials contained four material GAAP errors undetected by previous statutory auditor, corrected only via IPO-time restatement (Note 104)"
  - "Two consecutive years of CARO audit-trail qualification by previous auditor; narrower gap persists under new auditor FY25 (p.290-291)"
  - "Stressed-loan (NPA+SMA) transfers to ARC jumped >36x FY24-FY25, first year including SMA/pre-NPA accounts (Note 98(c))"
  - "Unreconciled ~180x gap between Note 98(c) and Note 75/5.7 NPA-sold-to-ARC figures for the same fiscal year"
  - "FY26 ARC-dominated Investments grew 5.4x vs ~31% loan-book growth (FY26RESULTS balance sheet)"
  - "Going-concern paragraph's 'lower gross NPA and net NPA' language contradicts the Company's own concurrent rising-Stage-3 disclosure (Note 59 vs Note 75/93(d))"
questions_for_mgmt:
  - "Reconcile Note 98(c) FY25 NPA-transferred-to-ARC principal (Rs109.54cr) against Note 75/5.7 Stage-3 Sold-to-ARC line (Rs0.61cr) for the same year"
  - "What is core lending profitability (NII + fees, ex-DA/ARC gain) for FY23-FY26, and will DA/ARC gain recognition normalise?"
  - "Confirm which fiscal year FY26RESULTS Note 9.4's Rs2.77cr write-off footnote describes and reconcile against DRHP Note 98(c)'s Rs4.614cr FY25 figure"
  - "Why did the Company begin selling SMA (pre-NPA) accounts to ARCs for the first time in FY25 (Rs155.27cr principal)?"
  - "What is the remediation timeline for the persisting audit-trail deficiency, and what root-cause analysis exists for the four undetected Note 104 GAAP errors?"
receivables_trend: "not applicable in the trade-receivables sense (Note 4, immaterial, <6 months ageing, NBFC lender has no meaningful trade-receivable book); the relevant asset-quality trend is Gross Stage-3/NPA ratio, which is DETERIORATING: 0.58% FY23 -> 0.73% FY24 -> 1.07% FY25 (Note 75/93(d), pp.368,377), with a further unreconciled >36x jump in FY25 stressed-loan transfers to ARC (Note 98(c))"
restatements_found:
  - "Accounting policy change, accrual to cash basis for certain fee income categories, applied retrospectively (Note 1.1.A.4/1.2, p.297-298; Note 104(e), p.383)"
  - "Business-correspondence transaction accounting treatment corrected (Note 104(a), p.383)"
  - "ECL not created on DA/EIS receivable in earlier years, now created (Note 104(b), p.383)"
  - "ARC upfront gain not recognised in earlier years due to interpretation gap in RBI ToLE guidelines/Ind AS 109, now recognised (Note 104(c)(1), p.383)"
  - "ARC Security Receipts re-measured/reclassified to FVTPL per Ind AS 109/107 (Note 104(c)(2), p.383)"
  - "Software licence payments (Synoriq) incorrectly capitalised as Intangible Asset, corrected to expense per Ind AS 8 (Note 104(d), p.383)"
  - "Face value sub-division Rs10 to Rs5 per share and bonus-like rights issue during FY25 (Note 22(a))"
going_concern_language: "Note 59, p.364: 'The Company, at this juncture, is focused on capital preservation, balance sheet protection and operating expenses management. Given its healthy capital adequacy, strong liquidity position, lower gross NPA and net NPA, diversified portfolio mix, geographical distribution and strong risk metrics.' -- templated/carried-forward language assessed in tension with the Company's own Note 75/93(d) disclosure of Gross Stage-3 nearly doubling FY23-FY25 and Note 98(c)'s >36x FY25 stressed-transfer jump; not a going-concern qualification, but a disclosure-consistency flag."
```
