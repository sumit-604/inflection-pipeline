# STAGE 2 - NOTES TO FINANCIAL STATEMENTS, PASS 2 (WHAT WAS MISSED)
Company: Rappid Valves (India) Ltd (RAPPID) | Run date: 2026-09-19
Source: AR FY26 (Annual_Report_2026.txt), amounts "in INR Lakhs" (Notes, p.58-71).
Cross-check source: AR FY25 (Annual_Report_2025.txt), amounts "in INR Thousands."
This pass re-read Note 1 through Note 37 end to end against the Pass 1 output.
Most notes were covered fully in Pass 1 (which was unusually thorough). The
items below are genuinely new: not repeats, not elaborations of a Pass 1
finding under a different name.

═══════════════════════════════════════════════════════════════════
NEW FINDING 1 - Note 32's IPO paragraph is internally impossible on its
own dates, independent of the Note 3.5 error Pass 1 already found
═══════════════════════════════════════════════════════════════════

Note 32 (Utilisation Summary, p.68), verbatim two consecutive sentences:
"...IPO was open for subscription from September 23, 2025, to September 25,
2025. The Company has allotted 13,69,800 Equity shares... aggregating to
₹3041 Lakhs on September 26, 2024."

The subscription window is dated 2025; the allotment for that same
subscription, one day later in the same paragraph, is dated 2024. The two
events cannot be one year apart when the text describes them as
consecutive days of one offering. The very next sentence in the same note
correctly states "listed with Emerge platform of NSE... on September 30,
2024" - so the note contains the CORRECT year (2024) once and the WRONG
year (2025) once, for what must be the same week.

Cross-checked: AR FY25's own text (two locations) gives "IPO was open for
public subscription from September 23, 2024, to September 25, 2024...
allotment... finalized on 26th September 2024" (AR FY25, p. corresponding
to lines ~1567 and ~2901 of that file). Note 3.3's share reconciliation
(this AR, p.60) shows the entire 16,71,984-share increase (including the
13,69,800 IPO allotment) landing in the FY25 column with zero equity
allotment in FY26.

This is the SAME rolled-forward-boilerplate defect Pass 1 found at Note
3.5 (which misdated the CCPS event as "10th July, 2025"), but it is a
SEPARATE instance, inside a DIFFERENT note (Note 32, the IPO-utilisation
note that is a company-memory priority item), and it is worse than the
Note 3.5 instance because the contradiction sits inside one note's own
two sentences, not only across notes/years. Two notes now carry the same
uncorrected-date defect (Note 3.5 and Note 32), plus the previously-found
third instance at Note 35 (CSR) - three separate load points for the same
control weakness: rolled-forward narrative text not re-dated on reuse.

Rating: 🔴 Red Flag (disclosure-quality / drafting-control, not a
quantification error - the underlying share count, cash amount, and
listing date all tie out correctly).
Anchor: Note 32 (AR FY26, p.68); cross-ref Note 3.5, Note 3.3 (p.60); AR
FY25 (two locations, ~p. corresponding to lines 1567 and 2901).

═══════════════════════════════════════════════════════════════════
NEW FINDING 2 - Note 29's own FY25 comparative deferred-tax figure does
not tie to the Balance Sheet / Note 7 FY25 figure in the SAME filing
═══════════════════════════════════════════════════════════════════

Note 29 (Deferred Tax, p.67) computes and displays "Net deferred tax
liabilities: 14.8 (FY26) / 0.1 (FY25)."
The Balance Sheet (p.55) and Note 7 (p.61-62) both show "Deferred tax
assets: 14.8 (FY26) / 13.4 (FY25)."
FY26 ties (14.8 = 14.8, only the asset/liability label differs - already
flagged by Pass 1). FY25 does NOT tie: Note 29 says 0.1, the Balance Sheet
and Note 7 say 13.4. That is a ₹13.3 Lakh unreconciled gap between two
places in the same audited document, not merely a labelling swap.

Cross-checked against AR FY25's own filed Note 29 (that AR's own Note 29,
p. corresponding to line ~7652 of that file), which independently computes
FY25 year-end "Net deferred tax liabilities" as 1,342.4 (in INR Thousands)
= ₹13.424 Lakh = ₹13.4 Lakh. This confirms 13.4 is the figure the company
itself computed and filed for FY25 at the time; the "0.1" shown as the FY25
comparative inside the FY26 AR's Note 29 is the erroneous figure, most
likely a transcription/decimal slip when the FY25 column was re-keyed for
the FY26 filing (the underlying build-up rows in Note 29 also show a
"Difference" of "0.5" against the correct 13.4 answer, so the error sits in
the FY25 column of Note 29's own arithmetic, not merely in the final line).

Rating: 🔴 Red Flag - compounds Pass 1 Finding #10-adjacent labelling issue
into an actual number mismatch, cross-year, cross-note, in a filed and
audited statement.
Anchor: Note 29 (AR FY26, p.67); Note 7, Balance Sheet (AR FY26, p.55,
p.61-62); AR FY25 Note 29 (own filing, FY25 column).

═══════════════════════════════════════════════════════════════════
NEW FINDING 3 - Unexplained capex reversal: machinery bought in FY25,
returned in FY26
═══════════════════════════════════════════════════════════════════

Note 13 (PPE schedule, p.64), Plant & Machinery, "Sale during the year"
column: ₹10.5 Lakh, with the footnote "Machinery amounted 10,47,358
returned during the year which is purchased on Mar'25."
No narrative anywhere in the notes on why a machine bought in March 2025
was returned within the following year (defect, wrong specification,
cancelled order, vendor dispute). Immaterial in size (0.7% of gross
block), but it is the only capex REVERSAL disclosed in either year, and it
coincides with the same year the company carried out the useful-life/
residual-value technical reassessment (Note 2.6) - two separate PPE
estimate/composition changes in one year with no cross-referenced
explanation for either.
Rating: 🟡 Watch.
Anchor: Note 13 (AR FY26, p.64).

═══════════════════════════════════════════════════════════════════
NEW FINDING 4 - "Rates & taxes" line falls 99.7% YoY with zero narrative,
inside a filing that discloses Nil exceptional items in both years
═══════════════════════════════════════════════════════════════════

Note 27 (Other Expenses, p.67): Rates & taxes ₹0.1 Lakh (FY26) vs ₹35.9
Lakh (FY25). This is the single largest percentage swing in the entire
Other Expenses note and is not mentioned in Note 36's ratio-change table
(because it sits below the ratio-table's own line items) nor anywhere
else in the notes. A ₹35.8 Lakh one-off cost of this kind (timing and
scale are consistent with one-time stamp duty, listing fees, or similar
IPO-adjacent statutory cost in the year of listing, September 2024,
which falls in FY25) sitting inside a routine "Rates & taxes" line - never
isolated as an exceptional item - is the same pattern Pass 1 noted
generally (P&L shows Nil exceptional/extraordinary items both years):
a lumpy one-off is being absorbed into an ordinary line rather than
called out, which understates the "clean" run-rate comparability of
FY25 Other Expenses against FY26.
Rating: 🟡 Watch.
Anchor: Note 27 (AR FY26, p.67).

═══════════════════════════════════════════════════════════════════
NEW FINDING 5 - GST input tax credit balance up 68% YoY, a third
unquantified cash-conversion drag alongside receivables and inventory
═══════════════════════════════════════════════════════════════════

Note 20 (Other Current Assets, p.65-66): "Goods and Services Tax (Input
Tax Credit)" ₹329.5 Lakh (FY26) vs ₹195.8 Lakh (FY25), +68.3% YoY, a
₹133.7 Lakh increase. This sits inside Other Current Assets (total ₹601.7
Lakh FY26 vs ₹535.4 Lakh FY25) and was not itemised or discussed in Pass 1.
Export revenue more than doubled in the same year (Note 21, ₹1,020.3 Lakh
vs ₹439.2 Lakh) - exports are typically zero-rated for GST, and a rising
unutilised input credit balance is a plausible direct consequence of the
export mix shift, meaning cash is increasingly parked in a GST refund
receivable rather than converted. This is a THIRD, previously unquantified
component of the working-capital build (after receivables +29% and
inventory +65%, both already flagged 🔴 in Pass 1) and belongs in the same
cash-conversion narrative feeding FLAG-CASH; no GST refund status, ageing,
or claim-pending disclosure exists anywhere in the notes to say whether
this ₹329.5 Lakh is a live claim or a stuck one.
Rating: 🟡 Watch (feeds and extends the existing 🔴 FLAG-CASH finding; not
independently red-flag-rated because no adverse fact about recoverability
is disclosed, only the growth itself).
Anchor: Note 20 (AR FY26, p.65-66); cross-ref Note 21 (p.66).

═══════════════════════════════════════════════════════════════════
NEW FINDING 6 - Export incentive accounting policy exists (Note 2.19) but
no export incentive is ever disclosed, despite export revenue more than
doubling
═══════════════════════════════════════════════════════════════════

Note 2.19 (Significant Accounting Policies, p.59-60): "Export Incentive if
any is accounted on accrual basis except Interest Subsidy which has been
accounted for on receipt basis." This policy exists specifically because
the company expects export-incentive income (RoDTEP, duty drawback, or
similar) to arise. Note 22 (Other Income, p.65-66) itemises only Interest
Income (₹26.8 Lakh), Foreign Exchange Gain (₹5.5 Lakh) and a small "Other
Income" residual (₹(0.4) Lakh) - no export incentive line appears in
either year, despite export revenue rising from ₹439.2 Lakh to ₹1,020.3
Lakh (+132.3%, Note 21). NOT FOUND IN DOCUMENT: any export incentive
income, in a year the company's own accounting policy specifically
anticipates it and export revenue surged. Either the company earns none
(unusual for an Indian exporter of this profile, and worth a management
question) or it is earned and buried inside a line that does not name it.
Rating: 🟡 Watch.
Anchor: Note 2.19 (AR FY26, p.59-60); Note 22, Note 21 (p.65-66).

═══════════════════════════════════════════════════════════════════
NEW FINDING 7 - Minor cross-note reconciliation gap: RPT-disclosed
director/KMP compensation does not fully trace into the functional
expense notes
═══════════════════════════════════════════════════════════════════

Note 28 (RPT, p.66-67) discloses non-loan compensation-type items totalling
₹107.4 Lakh (Mansi Dalal Directors' Remuneration ₹28.0 Lakh + Gaurav Dalal
Salary ₹62.0 Lakh + Vijay Dalal Salary ₹12.0 Lakh + three independent
directors ₹1.8 Lakh each = ₹5.4 Lakh). Note 25 (Employee Benefit Expense,
p.66) shows "Salary to Directors" of only ₹74.0 Lakh, which reconciles
exactly to Gaurav (₹62.0 Lakh) + Vijay (₹12.0 Lakh) and no one else. The
remaining ₹33.4 Lakh (Mansi Dalal's ₹28.0 Lakh remuneration plus the three
independent directors' ₹5.4 Lakh) is NOT FOUND IN DOCUMENT anywhere in
Note 25's or Note 27's functional expense line items under a traceable
label (no "sitting fees," "commission to directors," or similar caption
exists). Either this amount is folded into a generic line (e.g. Legal &
Professional Fees, or Salaries & Wages, both of which grew YoY) without
being named, or the RPT note and the functional-expense notes are drawing
on different underlying figures. Immaterial in absolute size relative to
total revenue, but a genuine, unexplained cross-note gap.
Rating: 🟡 Watch.
Anchor: Note 28 (p.66-67); Note 25, Note 27 (p.66-67).

═══════════════════════════════════════════════════════════════════
Items checked and found to already be fully covered by Pass 1 (no new
finding written up): Note 21 unbilled-revenue roll-forward decimal error
(Pass 1 Finding #6 - this pass located the mathematically correct
replacement figures, 119.4 opening / 161.3 closing rather than Pass 1's
approximate 52.7/119.4 guess, but this is a refinement of an existing
finding, not a new one, so it is not written up separately); Note 36
"Principal repayments" typo (Pass 1 Finding #9); Note 3.5 CCPS misdating
and Note 35 CSR year mislabel (Pass 1 Finding #5); Note 34/37 contingent
liability self-contradiction (Pass 1 Finding #4); Note 10 MSME ageing
(Pass 1 Finding #7); depreciation useful-life change (Pass 1 Finding #8);
P&L face vs Note 30 EPS mismatch (Pass 1 Finding #10). Going concern
language (Note 2.16, p.59) is standard, unqualified, boilerplate,
consistent with the auditor's own positive going-concern statement Pass 1
already cited - no new going-concern signal found on re-read.

═══════════════════════════════════════════════════════════════════
PASS 2 NEW FINDINGS SUMMARY
═══════════════════════════════════════════════════════════════════

| # | Finding | Note anchor | Rating |
|---|---|---|---|
| 1 | Note 32's IPO paragraph self-contradicts on year (subscription dated 2025, allotment one day later dated 2024, listing correctly dated 2024) - a second, worse instance of the rolled-forward-date defect Pass 1 found at Note 3.5 | Note 32 (p.68); cross-ref Note 3.5, 3.3 (p.60); AR FY25 | 🔴 Red Flag |
| 2 | Note 29's FY25 comparative "Net deferred tax liabilities" of ₹0.1 Lakh does not tie to the Balance Sheet/Note 7 FY25 figure of ₹13.4 Lakh in the same filing; AR FY25's own Note 29 confirms 13.4 is correct | Note 29 (p.67); Note 7, Balance Sheet (p.55, p.61-62); AR FY25 | 🔴 Red Flag |
| 3 | ₹10.5 Lakh of Plant & Machinery bought Mar-2025 returned during FY26, no narrative given | Note 13 (p.64) | 🟡 Watch |
| 4 | "Rates & taxes" fell 99.7% YoY (₹35.9 Lakh to ₹0.1 Lakh) with no narrative, inside a filing with Nil exceptional items both years | Note 27 (p.67) | 🟡 Watch |
| 5 | GST input tax credit balance up 68.3% YoY (+₹133.7 Lakh), a third, previously unquantified cash-conversion drag alongside receivables and inventory, plausibly linked to the export surge | Note 20 (p.65-66); cross-ref Note 21 | 🟡 Watch |
| 6 | Export incentive accounting policy exists (Note 2.19) but no export incentive income is disclosed anywhere despite export revenue up 132% | Note 2.19 (p.59-60); Note 22, 21 (p.65-66) | 🟡 Watch |
| 7 | ₹33.4 Lakh of RPT-disclosed director/KMP compensation (Mansi Dalal + 3 independent directors) does not trace to any line in the functional expense notes | Note 28 (p.66-67); Note 25, 27 (p.66-67) | 🟡 Watch |
