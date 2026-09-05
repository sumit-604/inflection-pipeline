# STAGE 2 — NOTES TO FINANCIAL STATEMENTS — PASS 3 (PATTERN PASS + CONSOLIDATION)
Company: DIFFNKG (Diffusion Engineers Limited) | Run date: 2026-09-05
Source: Annual_Report_2026.txt (FY2026, primary; FY2025 comparatives from the same document).
Standalone notes: AR2026 pp.144-181 (Notes 1-46). Consolidated notes: AR2026 pp.194-232 (Notes 1-46).
All amounts as printed in the AR are in Rupees Million; Crore conversions given only where useful
(1 Cr = 10 Mn). This report consolidates three passes: Pass 1 (full extraction, note by note),
Pass 2 (what was missed, second full re-read), Pass 3 (pattern pass across both statements).

---

## PASS 3: PATTERN-LEVEL RE-READ

Read the notes a third time, not sequentially, looking specifically for: notes that contradict each
other; numbers in the notes that do not match the main statements; deliberately thin disclosure next
to detailed disclosure elsewhere; restated prior-year figures; post-balance-sheet events; going
concern language anywhere.

Pass 1 and Pass 2 already surfaced three notes carrying RECURRING internal numeric inconsistencies
(Note 36, Note 34, Note 39). The pattern-pass task is to confirm these are clusters, not one-offs, and
to look for any further cross-note pattern neither pass caught.

**Cluster 1 — Note 36 (Employee Benefit Obligations), consolidated set: THREE separate numeric
mismatches, all inside the same note, across three different sub-tables/columns:**
1. Leave Encashment DBO, FY25 comparative: ₹4.23 Mn ("recognised in Balance Sheet" sub-table, p.216)
   vs ₹6.31 Mn ("changes in DBO" reconciliation sub-table, p.217). (Note 36, consolidated) 🔴
2. Gratuity plan assets, FY25 closing balance: ₹31.36 Mn ("recognised in Balance Sheet" sub-table,
   p.216) vs ₹31.53 Mn ("changes in plan assets" reconciliation, p.218). (Note 36, consolidated) 🔴
3. Leave Encashment current-liability bifurcation, FY25: ₹0.97 Mn (standalone, p.170) vs ₹1.62 Mn
   (consolidated, p.219) for what should be the same underlying obligation figure at the standalone
   entity level plus consolidation. (Note 36, both) 🟡
Pattern read: all three sit in the SAME note, all involve the SAME mechanism (a figure quoted twice in
different sub-tables of one note disagreeing), and all three understate rather than overstate the
FY25 comparative in the "recognised in Balance Sheet" table relative to the reconciliation tables. A
single-direction pattern across three instances is more consistent with a carry-forward/rollover
template error in the AR's Note 36 drafting (e.g., a prior-year column not fully refreshed when the
note was rebuilt for FY26) than with three independent typos. This does not by itself imply the
balance sheet or P&L numbers outside Note 36 are wrong — the ₹4.23 Mn and ₹31.36 Mn figures tie to the
standalone note and to the face-of-balance-sheet provisions line — but it means Note 36's internal
numeric set, taken as a whole, cannot be treated as self-consistent, and the company/auditor should be
asked to reconcile all three at once rather than item by item. 🔴 Red Flag (escalated from 🟡 given
the recurrence across three sub-tables).

**Cluster 2 — Note 34 (Tax Expense reconciliation): TWO reconciliation lines that fail to tie between
standalone and consolidated for the identical FY25 comparative year:**
1. "Others" catch-all reconciling item: -₹22.15 Mn (standalone, FY26) / -₹24.69 Mn (standalone, FY25)
   vs +₹23.21 Mn (consolidated, FY26) — sign flips between the two statements despite similar
   magnitude. (Note 34, both, p.164-165/213-214) 🟡
2. "Effect of Deferred Tax" reconciling line, FY25 comparative: ₹3.55 Mn (standalone, p.164) vs
   ₹0.50 Mn (consolidated, p.214) for the same label, same year. (Note 34, both) 🟡
Pattern read: unlike Cluster 1 (which is internal to one statement's own note), Cluster 2 is a
standalone-vs-consolidated tie-out failure. Some of this is explainable by ordinary consolidation
mechanics (foreign subsidiary losses with no Indian tax offset flowing through "Others"; a subsidiary
level deferred-tax adjustment changing the "Effect of Deferred Tax" line) but the notes provide no
narrative bridge to confirm that reading for either line. The effective tax rate itself (22.20%
standalone / 22.48% consolidated vs 25.17% statutory) is not disputed by this finding; what is
undermined is the VERIFIABILITY of the two- to three-line reconciliation that is supposed to explain
the effective-vs-statutory gap. 🟡 Watch, confirmed as a genuine two-item cluster rather than a single
flagged line.

**Cluster 3 — Note 39 (Fair Value Hierarchy, consolidated only): a structurally wrong table repeated
unchanged across both comparative years.** Cash and Bank Balances and Trade Receivables — neither a
fair-valued instrument under Ind AS 107 — are classified as "Level 3" fair-value inputs at carrying
value in BOTH FY26 and FY25 columns; Investments carry a Level 2 figure of ₹313.97 Mn (FY26) /
₹262.14 Mn (FY25) against an unexplained NEGATIVE "Level 3" line of ₹(30.91) Mn (FY26) / ₹(36.71) Mn
(FY25). (Note 39, consolidated, pp.222-224) 🔴 The standalone version of the same note (p.174) has no
Level 3 column at all for the equivalent disclosure — a further internal inconsistency, this time
between the standalone and consolidated presentations of the identically-named note. Pattern read: the
fact that the SAME mechanically-wrong pattern (non-fair-valued items in Level 3; a negative
unexplained plug) repeats identically across two annual reports (FY25 and FY26 columns both show it)
means this is very unlikely to be a fresh transcription error made this year — it looks like a
templated note that has never been corrected. This is a disclosure-quality finding about the AR's
drafting process, not evidence of a misstated fair value or a hidden liability; the underlying
Investments carrying value (₹270.30 Mn consolidated) and cash/receivables balances are independently
corroborated elsewhere (Notes 5, 8, 9) and are not themselves in question. 🔴 Red Flag on disclosure
mechanics, not on the underlying numbers.

**Other pattern-pass checks, no new findings beyond Pass 1/2:**
- Numbers in notes vs main statements: cross-checked total receivables (Note 8) to balance sheet,
  total borrowings (Note 16/19) to balance sheet, PBT/tax (Note 34) to statement of profit and loss —
  all tie out at the headline level in both standalone and consolidated sets; the mismatches found are
  confined to the three clusters above, all sub-note-level, none at the primary-statement level. 🟢
- Deliberately vague vs detailed disclosure: segment reporting (Note 41, flagged Pass 1) remains the
  clearest case of a promised disclosure ("see consolidated financial statements") that is not actually
  delivered anywhere; no further instance of this pattern found on the third read.
- Restatements: only the generic boilerplate "previous year figures regrouped/rearranged wherever
  necessary" (Note 46, both sets); no specific line item identified as restated, consistent with Pass 1.
- Events after balance sheet date: only the routine Note 44 proposed final dividend (15%); no other
  subsequent event note found on this read either.
- Going concern language: NONE found anywhere in the notes or (to the extent visible from the notes
  extraction) the auditor's report references within the notes section, in any of the three passes.

PASS 3 yields no NEW findings beyond escalating Cluster 1 to Red Flag status and formally confirming
the three clusters named by Pass 2 as genuine multi-instance patterns rather than one-off items. The
consolidation below proceeds with these clusters folded in.

---

# CONSOLIDATED NOTES ANALYSIS, ALL THREE PASSES COMBINED

## A. TOP 15 MOST SIGNIFICANT FINDINGS

| Rank | Finding | Note # | Rating | Why it matters |
|---|---|---|---|---|
| 1 | Outgoing CEO's remuneration jumped 552% (₹2.40 Mn → ₹15.66 Mn) in the same year he resigned (effective 6-Feb-2026), with no note explaining the nature of the payment | Note 38.2 (p.171/219-220) | 🔴 | Large, unexplained related-party payment to a departing executive; needs explanation (severance/bonus/accelerated vesting) before it can be read as clean |
| 2 | Note 36 (Employee Benefit Obligations) carries THREE separate internal numeric mismatches across its own sub-tables and between standalone/consolidated (Leave Encashment DBO ₹4.23 Mn vs ₹6.31 Mn; Gratuity plan assets ₹31.36 Mn vs ₹31.53 Mn; Leave Encashment current-liability ₹0.97 Mn vs ₹1.62 Mn) | Note 36 (p.216-219, consol; p.170, standalone) | 🔴 | Numbers within the notes disagree with each other in a recurring, single-note pattern; needs company/auditor confirmation before the employee-benefit disclosure can be relied upon as a set |
| 3 | Note 39 Fair Value Hierarchy (consolidated) misclassifies non-fair-valued cash and receivables as "Level 3," and carries an unexplained negative Level 3 plug against Investments, identically in both FY25 and FY26 columns; absent entirely from the standalone version of the same note | Note 39 (p.222-224 consol; p.174 standalone) | 🔴 | Mechanically wrong Ind AS 107 disclosure repeated across two years; a drafting-process failure the auditor should be asked to fix, though the underlying carrying values are independently corroborated elsewhere |
| 4 | Consolidated trade receivables grew 51.2% YoY (₹848.01 Mn → ₹1,281.79 Mn) against 21.3% revenue growth; Receivables Turnover Ratio fell 4.55x → 3.82x; standalone ratio also fell 4.19x → 3.61x | Note 8/42 (p.153-156/176; p.202-205/226) | 🟡 | Working capital deteriorating faster than revenue at both parent and group level; feeds FLAG-CASH |
| 5 | New unrelated investment of ₹21.49 Mn in Tejorup Sunmay Systems Private Limited (equity + CCPS), first appearance this year, zero narrative on the investee's business or rationale | Note 5 (p.153/201) | 🟡 | Surplus IPO cash deployed into an unrelated private company with no disclosed rationale; capital-allocation question |
| 6 | Segment reporting effectively absent in BOTH statements: standalone Note 41 defers to consolidated set, but consolidated Note 41 is retitled "Additional Information Regarding Subsidiaries," not segment data | Note 41 (both) | 🟡 | Investors cannot see manufacturing vs trading vs job-work vs export profitability split, only revenue splits |
| 7 | Note 34 tax reconciliation carries TWO lines that fail to tie between standalone and consolidated for the identical FY25 comparative ("Others" sign-flip -22.15 vs +23.21; "Effect of Deferred Tax" 3.55 vs 0.50) | Note 34 (both) | 🟡 | Largest driver of the effective-vs-statutory tax gap is an unnamed, non-reconciling catch-all; limits verifiability of the tax story |
| 8 | Gratuity funded status deteriorated sharply (net liability ₹2.31 Mn FY25 → ₹10.65 Mn FY26), driven by a ₹5.97 Mn past-service-cost exceptional item with no explanation of the underlying scheme change | Note 33/36 (p.164-168) | 🟡 | First-ever exceptional item in the comparative set, unexplained scheme change; worth a direct management question |
| 9 | No capital commitment note found despite Capital Work-in-Progress growing ~7x YoY (₹31.44 Mn → ₹221.70 Mn) | Note 3A (p.152); absence checked Notes 1-46 | 🟡 | Disclosure gap for a company mid-capex; forward capital commitments would normally be disclosed |
| 10 | Advance received from customers jumped ~+514% in one year (₹14.06 Mn → ₹86.33 Mn standalone; similar consolidated), no order-level detail given | Note 23 (p.160-161/210-211) | 🟡 | Unusual year-end spike vs 12-21% revenue growth; could be genuine order intake or a balance-sheet optic |
| 11 | Diffusion Super-Conditioning Services' related-party sales to the parent collapsed 95% YoY (₹98.21 Mn → ₹4.71 Mn), no explanation | Note 38.2 (p.169) | 🟡 | Large unexplained swing in intercompany billing; ask management |
| 12 | New related-party "Advance For Purchase" of ₹47.14 Mn to Diffusion Engineers Singapore Pte Ltd, nil in FY25, no stated purpose, repayment terms, or interest | Note 38.3 (p.174) | 🟡 | Functions like related-party financing dressed as a trade advance; needs arm's-length confirmation |
| 13 | ROE fell at standalone level (12.66% → 12.07%) despite higher absolute profit, with Net Capital Turnover falling 22-27%, company's own note attributing this to unutilised IPO proceeds ~18 months after listing | Note 42 (both) | 🟡 | Capital deployment timeline for balance IPO proceeds is an open question, dilutes return ratios |
| 14 | CSR spend routed through promoter-family-linked foundations (N.K. Garg Foundation ₹2.06 Mn FY26; BTSG Awareness Foundation ₹0.50 Mn FY25), no CSR-required-vs-actual figure disclosed in the notes | Note 38.2/Note 32 | 🟡 | Arm's-length/adequacy of this channel cannot be assessed from the notes alone |
| 15 | ESOP Trust structure: 300,000 shares purchased from the market for ₹90 Mn, funded by a company loan to the Trust, presented as Treasury Shares; the loan itself is not separately sized as an RPT | Note 43 (p.177-180/227-230) | 🟡 | Loan-funded secondary-market ESOP purchase warrants confirmation of arm's-length terms and full RPT disclosure |

## B. ACCOUNTING QUALITY SCORE

| Dimension | Score /10 | Basis |
|---|---|---|
| Revenue recognition conservatism | 8 | Point-in-time model, disaggregated by product/geography/customer type, no aggressive milestone or bill-and-hold pattern found; trading-mix shift toward lower-quality revenue is a mix concern, not a recognition-conservatism concern |
| Expense capitalisation honesty | 6 | PPE useful-life carve-out (Note 2.4) undisclosed by asset class; no capital-commitment note despite 7x CWIP growth; IPO expenses correctly taken to securities premium, not P&L |
| Provisioning adequacy | 5 | ECL matrix rate structure undisclosed (only the resulting number given); gratuity funded-status deterioration unexplained; no warranty provision despite a repair/reconditioning services line |
| RPT fairness | 5 | Outgoing CEO's 552% remuneration jump unexplained; unsized ESOP Trust loan; unexplained 95% collapse in intercompany sales; CSR via family foundations; otherwise RPT total is immaterial (1.8% of revenue) and arm's-length security/trade terms disclosed for the rest |
| Disclosure transparency | 4 | Segment reporting effectively absent in both statements; Note 39 fair-value-hierarchy table mechanically wrong across two years; Note 36 internally inconsistent across three sub-tables; new unrelated investment with zero rationale |
| Consistency with prior years | 5 | Note 34 and Note 36 both show standalone-vs-consolidated or within-note figures that fail to tie to the prior year; borrowings note has a header-vs-footnote secured/unsecured contradiction (standalone) |
| **OVERALL** | **5** | Clean revenue and tax-rate substance, negligible leverage and contingent liabilities, but the notes' own internal numeric consistency (Notes 34, 36, 39) and several unexplained related-party and disclosure gaps pull the score down from what the headline financials alone would suggest |

## C. KEY RISKS FROM NOTES

| Risk | Severity | What to monitor | When it could hit |
|---|---|---|---|
| Working capital deterioration (receivables outpacing revenue, both standalone and consolidated) | Medium | Receivables Turnover Ratio, ageing mix, DSO trend next 2-3 quarters | Next 1-2 quarters if trend continues |
| Note 36 internal inconsistency across employee-benefit sub-tables | Medium | Company/auditor confirmation of the correct FY25 comparative figures | Immediate (needs a direct management question before relying on the note) |
| Note 39 fair-value-hierarchy table structurally wrong (consolidated) | Low-Medium | Whether the FY27 AR corrects the classification and removes the negative plug | Next annual report cycle |
| Unexplained CEO remuneration spike and Note 38.2/38.3 related-party items (Singapore advance, Super-Conditioning sales collapse) | Medium | Whether these recur or reverse in FY27; whether disclosed with fuller narrative next year | Next annual report / quarterly RPT disclosures |
| Undeployed IPO proceeds dragging ROE, alongside an unexplained diversification investment (Tejorup Sunmay) | Medium | Capital deployment announcements, use-of-proceeds disclosure | Ongoing, watch next 2-4 quarters |
| No capital-commitment disclosure despite active capex (CWIP 7x) | Low | Whether FY27 AR adds a capital-commitment note as capex crystallises | Next annual report |
| Absent segment reporting | Low | Whether investor presentations/quarterly disclosures fill this gap outside the notes | Ongoing |

## D. FIVE QUESTIONS FOR MANAGEMENT

1. What was the nature of the ₹15.66 Mn remuneration paid to the outgoing CEO in the year of his
   resignation (severance, bonus, accelerated vesting), and why was it not separately disclosed as an
   exceptional or one-time item? (Note 38.2)
2. Can the company/auditor reconcile the three internal numeric mismatches inside Note 36 (Leave
   Encashment DBO, Gratuity plan assets, Leave Encashment current-liability split) and confirm which
   figures are correct? (Note 36)
3. What is the business rationale for the ₹21.49 Mn investment in Tejorup Sunmay Systems Private
   Limited, and how does it fit the stated use of IPO proceeds? (Note 5)
4. What drove the 95% collapse in Diffusion Super-Conditioning Services' related-party sales to the
   parent (₹98.21 Mn → ₹4.71 Mn), and what is the purpose and repayment term of the new ₹47.14 Mn
   advance to Diffusion Engineers Singapore? (Note 38.2/38.3)
5. Given trade receivables growing 51.2% (consolidated) against 21.3% revenue growth, what specific
   customers or segments are driving the buildup, and is the ECL matrix being revisited given the pace
   of growth? (Note 8)

## E. NOTES-BASED RED FLAGS

- Earnings management: no direct evidence of revenue-recognition manipulation; the ₹7 Mn exceptional
  gratuity/leave past-service cost is a one-off scheme-change charge, not a smoothing device, but its
  underlying cause is undisclosed. 🟡
- Aggressive accounting: none identified at the level of accounting POLICY (revenue, leases,
  capitalisation are all conservative or non-aggressive); the concerns found are DISCLOSURE-QUALITY and
  INTERNAL-CONSISTENCY issues (Notes 34, 36, 39), not choice-of-policy issues.
- Undisclosed risk indicators: unexplained CEO remuneration spike in the resignation year (🔴); three
  loss-making foreign/domestic subsidiaries carried at cost with no impairment test rationale, including
  one (Middle East) with negative net worth (🟡); a loan-funded ESOP Trust share purchase not separately
  sized as an RPT (🟡).

## F. ONE-LINE NOTES VERDICT

The notes reveal moderate accounting practices with several drafting-consistency lapses. Key concern:
Note 36's three-way internal numeric contradiction and the unexplained 552% CEO remuneration spike in
his resignation year. Key strength: conservative revenue recognition, near-zero leverage, and no
goodwill or hidden impairment exposure. Overall accounting quality: 5/10.

```yaml
stage: B02-notes
company: "DIFFNKG"
run_date: "2026-09-05"
model: claude-sonnet-5
status: complete
input_gaps:
  - {item: "prospectus", severity: HIGH, note: "ABSENT; company listed 4-Oct-2024"}
  - {item: "results/rating/announcements/shareholding/research", severity: MEDIUM, note: "ABSENT from corpus"}
flags:
  - {type: FLAG-CASH, reason: "Consolidated trade receivables +51.2% YoY vs +21.3% revenue growth; receivables turnover fell 4.55x to 3.82x consolidated and 4.19x to 3.61x standalone (Note 8/42)"}
accounting_quality: 5
pass_2_empty: false
pass_3_empty: false
top_findings:
  - {rank: 1, finding: "Outgoing CEO remuneration jumped 552% (Rs2.40Mn to Rs15.66Mn) in year of resignation, unexplained", note_ref: "Note 38.2, p.171/219-220", rating: "RED FLAG"}
  - {rank: 2, finding: "Note 36 carries three internal numeric mismatches across employee-benefit sub-tables (Leave Encashment DBO, Gratuity plan assets, current-liability split)", note_ref: "Note 36, p.216-219 consol / p.170 standalone", rating: "RED FLAG"}
  - {rank: 3, finding: "Note 39 fair value hierarchy misclassifies cash/receivables as Level 3 and carries unexplained negative Level 3 plug, identically in both years, consolidated only", note_ref: "Note 39, p.222-224 consol / p.174 standalone", rating: "RED FLAG"}
  - {rank: 4, finding: "Consolidated trade receivables +51.2% YoY vs +21.3% revenue growth; turnover ratio fell 4.55x to 3.82x (also standalone 4.19x to 3.61x)", note_ref: "Note 8/42", rating: "WATCH"}
  - {rank: 5, finding: "New unrelated investment of Rs21.49Mn in Tejorup Sunmay Systems Pvt Ltd, no rationale disclosed", note_ref: "Note 5, p.153/201", rating: "WATCH"}
  - {rank: 6, finding: "Segment reporting effectively absent in both standalone and consolidated statements despite standalone note promising it in the consolidated set", note_ref: "Note 41, both", rating: "WATCH"}
  - {rank: 7, finding: "Note 34 tax reconciliation has two lines that fail to tie between standalone and consolidated for the same FY25 comparative (Others sign-flip; Effect of Deferred Tax)", note_ref: "Note 34, both", rating: "WATCH"}
  - {rank: 8, finding: "Gratuity funded status deteriorated sharply (net liability Rs2.31Mn to Rs10.65Mn), driven by unexplained Rs5.97Mn past-service-cost exceptional item", note_ref: "Note 33/36, p.164-168", rating: "WATCH"}
  - {rank: 9, finding: "No capital commitment note found despite CWIP growing ~7x YoY (Rs31.44Mn to Rs221.70Mn)", note_ref: "Note 3A, p.152", rating: "WATCH"}
  - {rank: 10, finding: "Advance received from customers jumped ~514% in one year (Rs14.06Mn to Rs86.33Mn), no order-level detail", note_ref: "Note 23, p.160-161/210-211", rating: "WATCH"}
  - {rank: 11, finding: "Diffusion Super-Conditioning Services related-party sales to parent collapsed 95% YoY (Rs98.21Mn to Rs4.71Mn), unexplained", note_ref: "Note 38.2, p.169", rating: "WATCH"}
  - {rank: 12, finding: "New related-party advance for purchase of Rs47.14Mn to Diffusion Engineers Singapore, nil prior year, no stated purpose/terms", note_ref: "Note 38.3, p.174", rating: "WATCH"}
  - {rank: 13, finding: "Standalone ROE fell (12.66% to 12.07%) with Net Capital Turnover down 22-27%, company attributes to undeployed IPO proceeds ~18 months post-listing", note_ref: "Note 42, both", rating: "WATCH"}
  - {rank: 14, finding: "CSR spend routed through promoter-family-linked foundations, no CSR-required-vs-actual figure disclosed", note_ref: "Note 38.2/Note 32", rating: "WATCH"}
  - {rank: 15, finding: "ESOP Trust: Rs90Mn market share purchase funded by company loan to Trust, loan not separately sized as RPT", note_ref: "Note 43, p.177-180/227-230", rating: "WATCH"}
red_flags:
  - "Outgoing CEO remuneration jumped 552% in resignation year with no explanation (Note 38.2)"
  - "Note 36 (Employee Benefit Obligations) shows three separate internal numeric mismatches across its own sub-tables and standalone/consolidated boundary (Note 36)"
  - "Note 39 (consolidated Fair Value Hierarchy) mechanically misclassifies non-fair-valued items as Level 3 and carries an unexplained negative plug, unchanged across two years (Note 39)"
questions_for_mgmt:
  - "Nature of the Rs15.66Mn payment to the outgoing CEO in his resignation year, and why not disclosed as exceptional (Note 38.2)"
  - "Reconciliation of the three internal numeric mismatches inside Note 36 (Note 36)"
  - "Business rationale for the Rs21.49Mn Tejorup Sunmay Systems investment and fit with IPO-proceeds use (Note 5)"
  - "Cause of the 95% collapse in Diffusion Super-Conditioning related-party sales, and purpose/terms of the new Rs47.14Mn advance to Diffusion Engineers Singapore (Note 38.2/38.3)"
  - "Customer/segment drivers of the 51.2% receivables growth and whether the ECL matrix is being revisited (Note 8)"
receivables_trend: "deteriorating - consolidated receivables +51.2% YoY (Rs848.01Mn to Rs1,281.79Mn) vs +21.3% revenue growth, turnover ratio 4.55x to 3.82x; standalone +27.1% YoY vs +12.1% revenue growth, turnover 4.19x to 3.61x (Note 8/42); ageing mix itself modestly improved (>6m bucket 13.9% to 11.8% of gross, consolidated), so quantum is deteriorating while ageing quality is not worsening"
restatements_found: []
going_concern_language: "NONE"
analyst_note: "The three internal-consistency clusters (Notes 34, 36, 39) are drafting/template failures, not evidence of misstated primary financials; all headline balance sheet and P&L figures tie out cleanly. They matter because they mean the notes, taken as a documentary record, cannot be trusted line-by-line without cross-checking sub-tables against each other, which raises the bar for any downstream stage relying on granular note figures (especially Note 36 employee-benefit numbers and Note 34 tax reconciliation detail). Separately, the RPT cluster (CEO remuneration spike, Singapore advance, Super-Conditioning sales collapse) and the undisclosed-rationale Tejorup Sunmay investment sit in the same period as ~18 months of still-undeployed IPO proceeds; read together they warrant closer capital-allocation scrutiny at Halt 1, independent of the notes' technical accounting quality."
```
