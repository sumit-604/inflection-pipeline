# STAGE 2 — NOTES TO FINANCIAL STATEMENTS — PASS 2 (WHAT WAS MISSED)
Company: Barbeque-Nation Hospitality Limited (BNHL), now United Foodbrands Ltd (UFBL)
Source: Annual Report FY2024-25 (FY2025), file on disk mislabeled "Annual_Report_2023" but content
confirmed FY2025. Run date: 2026-08-05.

**UNIT FLAG (carried from Pass 1):** Source document is in ₹ Millions, not ₹ Crores. All figures
below are as disclosed, in ₹ Millions, with ₹ Crore equivalent in parentheses (÷10) for headline
numbers. Do not silently re-scale.

**METHOD:** Re-read Standalone Notes 1-47 (p.116-186) and Consolidated Notes 1-48 (p.196-262) note
by note against the Pass 1 output, with particular attention to sub-notes/footnotes, the auditor's
report language (read alongside the notes it cross-references), fair value/financial risk
management notes, the Schedule III consolidated-entity table, and the two items the orchestrator
flagged for deepening: the Barbeque Nation MENA "fully impaired" narrative vs carrying value, and
the Consolidated Note 25(b) FY24 revenue reconciliation gap. Also traced the goodwill/CGU
discount-rate reductions and the DTA/unabsorbed-depreciation issue into adjacent notes not read in
depth in Pass 1. Findings below are NEW ONLY — items Pass 1 already covered are not repeated.

---

## PASS 2 NEW FINDINGS

### 1. 🔴 [NEW, HIGHEST PRIORITY] The statutory auditor states it CANNOT confirm audit-trail
integrity for part of the accounting records — a control-environment gap Pass 1 missed entirely
(Notes 46/47 in the standalone set and 47/48 in the consolidated set were not read in Pass 1).

Standalone Note 47 "Maintenance of Books of Account" (p.172-173) and its Consolidated equivalent
Note 48 (p.249-250) disclose that BNHL/the Group uses an accounting software **operated by a
third-party software service provider**, and that:
- (a) *Physical server location*: "Management is not in possession of Service Organisation Controls
  report to determine whether the back-up of books of account maintained in electronic mode in
  respect of said accounting software was kept in server physically located in India on a daily
  basis" (Standalone Note 47(a), p.172; Consolidated Note 48(a), p.249).
- (b) *Audit trail*: "In the absence of Service Organisation Controls report, we are unable to
  comment on whether the audit trail feature of the aforesaid software was enabled and operated
  throughout the year... or whether there were any instances of the audit trail feature being
  tampered with... [or] whether the audit trail has been preserved... as per the statutory
  requirements for record retention" (Standalone Note 47(b), p.173; Consolidated Note 48(b),
  p.250).

Critically, this is not just company self-disclosure — **the statutory auditor S.R. Batliboi &
Associates LLP repeats this verbatim as its own limitation in the Independent Auditor's Report**
(standalone report, p.104-105; consolidated report, p.178-179), under the Rule 11(g) audit-trail
reporting requirement: "In the absence of Service Organisation Controls report, we are unable to
comment on whether the audit trail feature of the aforesaid software was enabled and operated
throughout the year for all relevant transactions... or whether there were any instances of the
audit trail feature being tampered with... Additionally... we are unable to comment whether the
audit trail has been preserved by the Company as per the statutory requirements for record
retention."

No "Qualified Opinion" or "Emphasis of Matter" heading was found anywhere in either the standalone
or consolidated Independent Auditor's Report (checked both reports in full) — the overall opinion
on true-and-fair-view remains unmodified, and the separate Internal Financial Controls report
(Annexure 2 to the consolidated auditor's report, p.181-182) gives a clean "operating effectively"
opinion. So this is a specific compliance-reporting limitation, not a qualification of the
financial statements. It is nonetheless a genuine, auditor-confirmed gap: for at least the
third-party-hosted portion of its books, **neither the Company nor its auditor can independently
verify that the audit trail was tamper-free, complete, or retained as required by law**, for the
second year running an entity in genuine financial stress (widening losses, tightening liquidity,
first working-capital draw). This directly bears on the reliability of every other number in this
report and should weigh on the overall accounting-quality score.

### 2. 🟡 [NEW] Provisioning/impairment build-up is broader than trade receivables alone — it spans
three separate asset categories simultaneously in FY25, roughly 3x the prior year in aggregate.

Pass 1 (Section 4) flagged only the trade receivables ECL swing (₹0 → ₹10.26mn). Two further,
separate provisioning build-ups were not read in Pass 1:
- **Security deposits / other financial-asset impairment** (Standalone Note 11(a), p.137-138):
  allowance opening ₹4.01mn → closing ₹25.71mn, i.e. a **₹21.70mn FY25 addition** vs ₹4.01mn in
  FY24. A new "Others — Credit impaired" current receivable of ₹24.05mn appeared in FY25 (nil
  FY24), fully provided. Consolidated equivalent (Note 10(a), p.210-211): allowance opening
  ₹24.26mn → closing ₹44.74mn, a **₹20.48mn FY25 addition** vs ₹4.01mn FY24; the "Others — Credit
  impaired" current line grew from ₹9.29mn (FY24) to **₹43.08mn (FY25)**, a ~4.6x increase.
- **Doubtful advances to suppliers** (Standalone Note 12, p.138-139): allowance opening ₹16.57mn →
  closing ₹25.87mn, a **₹9.30mn FY25 addition** (vs ₹11.15mn FY24, roughly flat YoY).
  Consolidated equivalent (Note 11, p.211-212): opening ₹17.05mn → closing ₹26.35mn, addition
  ₹9.30mn (vs ₹10.73mn FY24).

Standalone total new provisioning charges across all three categories: FY25 ₹21.70mn (deposits) +
₹9.30mn (advances) + ₹10.26mn (trade receivables, per Pass 1) = **₹41.26mn**, vs FY24 ₹4.01mn +
₹11.15mn + (₹1.78mn reversal) = **₹13.38mn** — roughly a 3x increase in balance-sheet credit-quality
provisioning, concentrated in the same year revenue fell and the working-capital loan was first
drawn. This is a broader and more material working-capital-quality signal than Pass 1's Section 4
implied.

### 3. 🟡 [NEW] FY25 is the first year BNHL carries a "net investment in lease" receivable from its
own loss-making subsidiaries — a new, growing 15-year intercompany exposure layered on top of the
loan/equity exposure to the same corporate family.

Standalone Note 38 (p.163) discloses: "The Company has entered into agreements for sub-lease of
premises, with Red Apple Kitchen Consultancy Private Limited and Blue Planet Foods Private Limited
to use the premises as outlet for 15 years." This generated a new balance-sheet asset in FY25 —
"Net investment in lease" of ₹117.33mn (non-current, Note 11, p.137) + ₹13.00mn (current, p.138) =
**₹130.33mn total** (nil FY24; confirmed in the RPT balances table, Note 43, p.168: "Net investment
in lease — Subsidiaries ₹130.33mn"). It generated ₹13.08mn "Profit on sub-lease" and ₹6.43mn
notional interest income in FY25 (both nil FY24) (Note 26, p.149; Note 38, p.163). **Future minimum
sub-lease rentals receivable total ₹228.18mn** over the 15-year term: ₹12.70mn within 1 year,
₹53.65mn 1-5 years, ₹161.83mn beyond 5 years (Note 38, p.163). This is a new and growing
intercompany financial-asset channel to Red Apple and Blue Planet — the two subsidiaries whose
combined FY25 results swung sharply negative (Red Apple -₹22.90mn from +₹77.22mn profit; Blue
Planet -₹2.21mn loss, narrowing but still negative) — on top of the existing loan and equity
exposure already flagged in Pass 1. Not inherently a red flag (sub-leasing owned leasehold space to
a subsidiary outlet is a normal group structure), but it is new FY25 balance-sheet exposure to
the same stressed corporate family that Pass 1 did not capture.

### 4. 🟡 [NEW — sharpens Pass 1 Rank-1 finding] The MENA loan "reduction" was 99.86% a non-cash
loan-to-equity reclassification, not a real repayment.

The Regulation 34(3) loan disclosure (Standalone Note 45, p.172) shows the Barbeque Nation MENA
Holding loan falling by exactly ₹250.00mn (₹921.49mn → ₹671.49mn) under a single combined
"Repayment/(Conversion)" column. Cross-referencing Note 9(c) (p.135), the loan-to-equity
conversion itself was **₹249.65mn** (109,457 new AED-100 shares allotted). That means **only
₹0.35mn (0.14%) of the ₹250.00mn reduction was an actual repayment** — essentially the entire
reduction was a non-cash reclassification of the exposure from "loan" to "investment," into an
entity whose equity investment the same note narrative separately describes as "fully impaired."
BNHL received effectively zero net cash recovery on its MENA exposure in FY25. This sharpens (does
not contradict) Pass 1's Rank-1 finding: the year's headline "loan reduction" is optics, not
substance.

### 5. 🟡 [NEW] The premium paid to increase BNHL's stake in Red Apple is charged directly to
retained earnings, bypassing the P&L and any impairment test, in the same year Red Apple's own
result swung to a loss — and this is now a two-year, ₹260.90mn pattern.

Standalone Note 9(a) / Consolidated Note 42(b) (p.135, p.242-243) confirm BNHL bought an
incremental 6.62% stake in Red Apple in FY25 for ₹160.29mn via **secondary purchase from existing
(non-group) shareholders**, raising its holding from 82.43% to 89.05% — the same year Red Apple's
standalone-equivalent result swung from +₹77.22mn profit (FY24) to -₹22.90mn loss (FY25, per
Consolidated Note 45, already flagged in Pass 1). At consolidated level, this purchase of
non-controlling interest is (correctly, per Ind AS 110) routed entirely through equity, not P&L:
the Consolidated Statement of Changes in Equity (p.198) shows "Further acquisition of NCI in Red
Apple Kitchen Consultancy Private Limited" of **₹(160.29)mn** charged to retained earnings, offset
by ₹33.34mn transferred out of non-controlling interest (Note 18, p.218) — a **net ₹126.95mn charge
to owners' equity that never passes through the P&L or a goodwill impairment test**. The prior year
carried an equivalent ₹100.61mn charge for the same reason (4.21% stake increase, FY24). Cumulative
two-year cost of buying out Red Apple's minority shareholders, charged direct to retained earnings:
**₹260.90mn**, while Red Apple's own annual result has gone from profit to loss over the same
period. This is standard Ind AS accounting, but the economics are investor-relevant: the parent
paid up for a growing stake in a subsidiary whose profitability just collapsed, and the premium
paid is invisible below the P&L line.

### 6. 🟡 [NEW] Willow Gourmet: 99.9% of the new associate investment is implicit goodwill — an
even more extreme version of the Blue Planet goodwill pattern Pass 1 already flagged.

Consolidated Note 9 (p.209-210) discloses the equity-method accounting for Willow Gourmet Private
Limited (42.36% stake, acquired March 11, 2025, ₹120.00mn consideration): the Group's 42.36% share
of WGPL's total equity (₹121.79mn) is just **₹0.76mn**; the remaining **₹119.83mn of the ₹120.59mn
carrying value (99.3%) is goodwill** embedded within the equity-accounted investment. This extends,
with an even higher ratio, the pattern Pass 1 flagged for Blue Planet (76% of deal value to
goodwill, Rank finding in Pass 1's Section 12): BNHL's two most recent bolt-on acquisitions (Blue
Planet FY24, Willow Gourmet FY25) have both been priced almost entirely for brand/growth
optionality rather than tangible net assets, and neither is co-located inside the goodwill
impairment-test note (Note 7) that carries the sensitivity disclosure gap Pass 1 already flagged —
Willow Gourmet's goodwill sits inside the equity-method investment line, outside the CGU/goodwill
impairment framework altogether, and is not separately tested for impairment under the same
Note 7/10A methodology.

### 7. 🟡 [NEW] Barbeque Nation Restaurant LLC (Dubai) — the Group's largest single profit
contributor among subsidiaries — carries a deeply negative net-asset position, unexplained in the
notes.

Per the Consolidated Schedule III additional information (Note 45, p.244-246), Barbeque Nation
Restaurant LLC shows: net assets **₹(641.23)mn** FY25 [-17.29% of consolidated net assets] and
**₹(690.00)mn** FY24 [-17.09%], even as it generated **+₹48.77mn** profit FY25 and **+₹50.68mn**
FY24 — the single largest positive profit contributor in the entire subsidiary table both years.
In other words, the Group's most consistently profitable individual subsidiary is technically
insolvent on a book-equity basis, and has been for at least two years running, with no narrative
explanation anywhere in the notes read (no note on historical accumulated losses, intercompany
payable structuring, or parent support specific to this entity — distinct from the MENA support
commitment in Note 36, which is expressed at the Barbeque MENA Holding level, not this step-down
entity specifically). Worth a direct management question on how this entity is capitalised/funded
given persistent negative net worth.

### 8. 🟡 [NEW] The "Adjustments arising out of consolidation" residual line in the Schedule III
table more than tripled YoY on a net-assets basis and now absorbs an outsized share of the
consolidated loss and OCI, with no decomposition given anywhere in the notes.

Consolidated Note 45 (p.244-246): "Adjustments arising out of consolidation" shows net-assets
impact of **₹(650.55)mn** FY25 [-17.54% of consolidated net assets] vs **₹(185.01)mn** FY24
[-4.58%] — a **3.5x increase**; share of consolidated loss **₹(20.15)mn** FY25 [7.45% of
consolidated loss] vs **₹(3.26)mn** FY24 [2.92%] — a **6.2x increase**; and **95.79%** of
consolidated OCI (₹(12.74)mn of ₹(13.30)mn total, almost entirely the foreign currency translation
reserve). This residual consolidation/elimination plug (goodwill, intercompany eliminations —
including, plausibly, elimination of the new intercompany sub-lease profit flagged in Finding 3
above — fair-value and other adjustments) is not broken out or explained anywhere in the notes,
which limits an investor's ability to independently verify what is now driving close to a fifth of
consolidated net assets. This is a disclosure-transparency gap, not evidence of misstatement on its
own, but the magnitude of the YoY jump warrants a management question.

### 9. 🟡 [NEW, minor but pattern-relevant] A second/third drafting-quality lapse in the same note
set as the FY24 revenue-reconciliation gap Pass 1 already flagged.

Consolidated Note 46 (Related Party Disclosures, p.248) states: "For the year ended March 31, 2025,
the Group **has recorded** any impairment of assets relating to amounts owed by related parties."
This almost certainly should read "has **not** recorded any impairment," consistent with the
parallel sentence in the Standalone Note 43 (p.169): "the Company has **not** recorded any
impairment of assets relating to amounts owed by related parties." Read literally, the consolidated
sentence as drafted says the opposite of what is almost certainly intended. On its own this is a
minor typo, but combined with the FY24 Note 25(b) revenue-reconciliation gap and the MENA "fully
impaired" narrative-vs-table mismatch (both Pass 1 Rank-1/2 findings), this is now the **third**
internal drafting inconsistency identified across the note set in a single year, suggesting a
broader note-drafting quality-control gap this reporting cycle rather than three unrelated,
isolated incidents. Worth folding into the accounting-quality "disclosure transparency" dimension
score.

### 10. 🟡 [NEW] Gearing ratio, disclosed but not extracted in Pass 1, quantifies the leverage
deterioration Pass 1 flagged only qualitatively.

Standalone Note 42 (p.166): gearing ratio (net debt ÷ (capital + net debt)) rose to **61.98%**
(FY25) from **58.74%** (FY24). Consolidated Note 41 (p.241-242): gearing ratio rose to **67.13%**
(FY25) from **62.31%** (FY24). These formal figures corroborate, with a quantified metric, Pass 1's
Rank-6 finding (standalone liquidity tightening / first working-capital draw / rising near-term
maturity share) — leverage is rising at both standalone and consolidated levels, with the
consolidated ratio running ~5 points higher than standalone and widening faster YoY (+4.8pp
consolidated vs +3.2pp standalone).

### 11. [NEW, completeness correction to Pass 1's RPT table] KMP total compensation is ₹81.47mn,
not the ₹35.16mn cash figure Pass 1's RPT table implied — share-based payments are the larger
component.

Standalone/Consolidated Note 43/46 (p.169-170, p.248): "Compensation of Key Managerial Personnel"
shows Short-term employee benefits ₹35.16mn (FY25) / ₹28.25mn (FY24) — the figure Pass 1's RPT
table captured as "Remuneration to KMP" — **plus Share based payments ₹46.31mn (FY25) / ₹44.58mn
(FY24)**, for a **Total compensation of ₹81.47mn (FY25) vs ₹72.83mn (FY24), +11.9% YoY**. SBP is
the larger of the two components in both years. This does not change Pass 1's directional finding
but corrects the magnitude: total KMP pay is more than double what the RPT transaction table alone
suggested, and is growing steadily even as the Company's losses widen and headline EPS
deteriorates.

### 12. [NEW, minor disclosure gap] Blue Planet's consolidated economic ownership moved in a
direction and magnitude not explained in the notes read.

Consolidated Note 42 "Group Information" (p.242-243) discloses Blue Planet Foods Private Limited
ownership (combining BNHL's direct 11.77% stake, held flat both years per Note 9, plus Red Apple's
indirect stake) at **48.76% (FY25) vs 46.01% (FY24)**. At the November 2023 acquisition date, the
combined stake was disclosed (Consolidated Note 44, business combination note, already read by
Pass 1) as **53.26%** (11.77% direct + 41.49% via Red Apple). No note explains the mechanism by
which combined group ownership fell from 53.26% at acquisition to 46.01% (FY24) and then partially
recovered to 48.76% (FY25) — most likely dilution from a Blue Planet-level funding/ESOP event
followed by partial anti-dilutive reinvestment, but this is inference, not disclosed fact. NOT FOUND
IN DOCUMENT: explanation for the Blue Planet ownership percentage movement across the two years.

---

## PASS 2 NEW FINDINGS SUMMARY

Twelve new items were identified on the second read-through, none overlapping Pass 1's Top 10. The
single highest-priority new finding is **Finding 1** — the statutory auditor's own stated inability
to confirm audit-trail integrity for part of the Company's books, disclosed in both the standalone
and consolidated Notes 47/48 and repeated verbatim in the Independent Auditor's Report itself. This
was missed in Pass 1 because Notes 46-47 (standalone) and 47-48 (consolidated) — "Other Statutory
Information" and "Maintenance of Books of Account" — were not read in Pass 1's note-by-note pass;
they are late-numbered, routine-looking notes that in this AR happen to carry a genuine,
auditor-confirmed control gap. Findings 2-3 extend Pass 1's working-capital and related-party
exposure themes with material new quantum (broader provisioning build; new 15-year intercompany
lease exposure to the same stressed subsidiaries). Findings 4-5 sharpen and add nuance to Pass 1's
already-flagged MENA and Red Apple items rather than contradicting them. Findings 6-8 are new,
stand-alone items from the consolidated Schedule III and equity-method notes that Pass 1's Section
6/12 treatment of subsidiaries did not reach. Findings 9-12 are smaller completeness/consistency
corrections.

---

```yaml
stage: B02-notes
company: "UFBL"
run_date: "2026-08-05"
model: claude-sonnet-5
pass: 2
status: complete
pass_2_empty: false
notes_read_this_pass: "Full re-read of Standalone Notes 1-47 (p.116-186) and Consolidated Notes 1-48 (p.196-262), plus the Independent Auditor's Reports (standalone p.100-115, consolidated p.175-182) cross-referenced against Note 47/48"
new_findings_count: 12
new_findings:
  - {rank: 1, finding: "Statutory auditor states it is unable to confirm audit-trail integrity/tampering/retention for books maintained on third-party-hosted accounting software, absent a Service Organisation Controls report; repeated in the Independent Auditor's Report itself (Rule 11(g)); overall audit opinion remains unmodified", note_ref: "Standalone Note 47(a)-(b) p.172-173; Consolidated Note 48(a)-(b) p.249-250; Auditor's Report standalone p.104-105, consolidated p.178-179", rating: "red_flag", why: "Control-environment gap confirmed by the external auditor, not just management; bears on reliability of the underlying books behind every other number in this report; missed entirely in Pass 1 because these late notes were not read"}
  - {rank: 2, finding: "Provisioning build-up spans three separate asset categories (security deposits/other receivables, doubtful advances to suppliers, trade receivables), roughly 3x FY24's combined addition, not just trade receivables as Pass 1 Section 4 implied", note_ref: "Standalone Note 11(a) p.137-138, Note 12 p.138-139; Consolidated Note 10(a) p.210-211, Note 11 p.211-212", rating: "watch", why: "Broader and more material working-capital-quality signal than Pass 1 captured"}
  - {rank: 3, finding: "New FY25 'net investment in lease' of Rs130.33mn from sub-leasing premises to Red Apple and Blue Planet (both stressed subsidiaries), with Rs228.18mn of future minimum rentals receivable over 15 years", note_ref: "Standalone Note 11 p.137-138, Note 38 p.163, Note 43 p.168", rating: "watch", why: "New and growing intercompany financial exposure to the same subsidiaries already flagged for loss/impairment issues in Pass 1"}
  - {rank: 4, finding: "MENA loan 'reduction' of Rs250.00mn was 99.86% (Rs249.65mn) a non-cash loan-to-equity reclassification, not a real repayment; BNHL received near-zero net cash recovery on this exposure in FY25", note_ref: "Standalone Note 45 p.172; Note 9(c) p.135", rating: "red_flag", why: "Sharpens Pass 1's Rank-1 MENA finding: the year's loan reduction is optics into a nominally 'fully impaired' entity, not substance"}
  - {rank: 5, finding: "Rs160.29mn paid to increase Red Apple stake via secondary purchase, charged directly to retained earnings bypassing P&L/impairment testing, same year Red Apple swung to loss; cumulative two-year cost Rs260.90mn", note_ref: "Standalone Note 9(a) p.135; Consolidated Note 42(b) p.242-243, Statement of Changes in Equity p.198, Note 18 p.218", rating: "watch", why: "Economically relevant premium paid for a deteriorating subsidiary that is invisible below the P&L line under correct NCI accounting"}
  - {rank: 6, finding: "Willow Gourmet associate investment: 99.3% (Rs119.83mn of Rs120.59mn) is implicit goodwill embedded in the equity-method carrying value, sitting outside the Note 7/10A goodwill impairment-test framework", note_ref: "Consolidated Note 9 p.209-210", rating: "watch", why: "Extends Pass 1's Blue Planet 76%-goodwill finding to an even more extreme second case, and this goodwill is not covered by the CGU impairment-sensitivity note"}
  - {rank: 7, finding: "Barbeque Nation Restaurant LLC (Dubai), the Group's largest single profit contributor among subsidiaries, carries deeply negative net assets (Rs(641.23)mn FY25, Rs(690.00)mn FY24) with no explanation in the notes", note_ref: "Consolidated Note 45 p.244-246", rating: "watch", why: "Technically insolvent on a book-equity basis despite being the most profitable individual subsidiary two years running; unexplained capital structure"}
  - {rank: 8, finding: "'Adjustments arising out of consolidation' residual line grew 3.5x on net assets and 6.2x on share of loss YoY, absorbing 95.79% of consolidated OCI, with no decomposition given", note_ref: "Consolidated Note 45 p.244-246", rating: "watch", why: "Unexplained consolidation plug now material to net assets and loss attribution; limits independent verification"}
  - {rank: 9, finding: "Consolidated RPT note (Note 46) contains an apparent missing 'not': states Group 'has recorded' rather than 'has not recorded' impairment on related-party receivables, contradicting the parallel standalone note", note_ref: "Consolidated Note 46 p.248; cf. Standalone Note 43 p.169", rating: "watch", why: "Third internal drafting inconsistency identified across the two passes, suggesting a note-drafting quality-control gap this year rather than isolated incidents"}
  - {rank: 10, finding: "Gearing ratio rose to 61.98% standalone (from 58.74%) and 67.13% consolidated (from 62.31%)", note_ref: "Standalone Note 42 p.166; Consolidated Note 41 p.241-242", rating: "watch", why: "Quantifies Pass 1's qualitative liquidity-tightening flag with a formal leverage metric"}
  - {rank: 11, finding: "Total KMP compensation is Rs81.47mn (FY25) vs Rs72.83mn (FY24), more than double the Rs35.16mn cash figure in Pass 1's RPT table, because share-based payments (Rs46.31mn) are the larger component", note_ref: "Standalone/Consolidated Note 43/46 p.169-170/248", rating: "clean", why: "Completeness correction to Pass 1's RPT table; KMP pay growing steadily despite widening losses"}
  - {rank: 12, finding: "Blue Planet consolidated ownership moved from 53.26% at acquisition to 46.01% (FY24) to 48.76% (FY25) with no explanatory note found", note_ref: "Consolidated Note 42 p.242-243; cf. Note 44 business combination note", rating: "watch", why: "Unexplained ownership-percentage movement; NOT FOUND IN DOCUMENT for the mechanism"}
input_gaps_added_this_pass:
  - "Mechanism for Blue Planet consolidated ownership percentage movement (53.26% to 46.01% to 48.76%) not disclosed"
  - "No explanation for Barbeque Nation Restaurant LLC's persistent deeply negative net-asset position despite consistent profitability"
  - "Composition/decomposition of the 'Adjustments arising out of consolidation' Schedule III residual line not disclosed"
```
