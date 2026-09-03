# STAGE 2 / PASS 2: NOTES TO FINANCIAL STATEMENTS, WHAT WAS MISSED
Company: Venus Remedies Ltd (VENUSREM) | Run date: 2026-09-02 | Mode: NO-CONCALL
Source: FY2025-26 Annual Report, page-marked .txt extract (Annual_Report.txt, 137-page extraction)
Page citations use the extraction's own "===== PAGE n of 137 =====" markers, written as p.n.
This pass re-read every standalone note (1-48) and consolidated note (1-51) against the Pass 1
output, verified the Top-10 findings against the primary financial statements (Balance Sheet, P&L)
and cross-checked the specific moderate-confidence / NOT FOUND items the orchestrator named.
Only NEW findings, resolutions, or escalations not already stated in Pass 1 are reported below.

Rating key: Green = clean/positive. Yellow = Watch. Red = Red Flag.

═══════════════════════════════════════════════════════════════════
## NEW FINDING 1: UNDISCLOSED EXCEPTIONAL ITEM (FY25, Rs 9.91 Cr) CONTRADICTS BOARD'S REPORT
═══════════════════════════════════════════════════════════════════
🔴 Red Flag -- missed entirely in Pass 1.

The Standalone Statement of Profit & Loss (p.99, line item VI, between "Profit before Taxes"
and "Profit after exceptional items and Taxes") carries an **Exceptional Items line of
Rs 991.32 Lakhs (Rs 9.91 Cr) in FY25, and NIL in FY26.** This lifts FY25 standalone PBT from
Rs 69.16 Cr (before exceptional items, row V) to Rs 79.08 Cr (after, row VII) -- a positive
addition to profit. The IDENTICAL Rs 9.91 Cr exceptional item appears in the CONSOLIDATED P&L
too (p.~124, Note VI/VII: Profit before exceptional items FY25 Rs 61.91 Cr -> after, Rs 71.83 Cr).
No note anywhere in the standalone (1-48) or consolidated (1-51) note set narrates what this
exceptional item was. NOT FOUND IN DOCUMENT: nature of the FY25 exceptional item.

This was not surfaced in Pass 1's Note 17 (Deferred Tax / tax reconciliation) extraction even
though Note 17's own tax-reconciliation table uses "Profit before tax: Rs 7,907.50 Lakhs" for
FY25 (p.108-109) -- i.e., Pass 1 used the POST-exceptional PBT figure without noticing the P&L
face itself splits out an exceptional-items row immediately above it.

**Direct contradiction with the Board's Report / MD&A (p.~65, Financial Highlights narrative):**
"Profit Before Tax rose 117% to Rs134.15 Crore from Rs61.91 Crore. Profit After Tax rose 127% to
Rs102.79 Crore from Rs45.31 Crore, **with no exceptional items in either direction distorting the
comparison**." (consolidated basis; standalone commentary a few lines later repeats the same
"no exceptional items" framing implicitly by not mentioning any).

This is factually incorrect on the company's own numbers:
- The Rs 61.91 Cr FY25 base used for the "117%" PBT-growth claim is the PRE-exceptional-items
  figure (consolidated Note V, "Profit before exceptional items and Taxes" = Rs 6,191.32 Lakhs),
  not the actual audited, as-reported FY25 PBT of Rs 71.83 Cr (Note VII, "after Exceptional
  Items"). The company silently strips the FY25 exceptional gain from its own growth-rate base
  while asserting in the same sentence that no exceptional items distorted the comparison.
- The PAT growth figure ("127%... Rs45.31 Crore") is NOT similarly adjusted -- it uses the
  as-reported FY25 PAT of Rs 45.31 Cr, which DOES include the flow-through of the Rs 9.91 Cr
  exceptional gain (P&L Statement: PBT after exceptional Rs 71.83 Cr -> tax -> PAT Rs 45.31 Cr,
  ties out exactly, p.~124). So within the same paragraph, PBT growth is computed on an
  ex-exceptional base and PAT growth is computed on an as-reported (inclusive) base -- an
  inconsistent methodology, and the "no exceptional items... distorting the comparison" sentence
  is not accurate for either computation.

Why it matters: this is a quotable, source-anchored discrepancy between the Board's Report
narrative and the company's own audited financial statements, on a headline growth metric (PBT
growth) that investors are likely to quote directly from the MD&A. It also means FY26's PBT
growth on a truly clean, like-for-like basis (Rs 130.67 Cr standalone vs. a clean FY25 base of
Rs 69.16 Cr, i.e. stripping the FY25 one-off) is actually 88.9%, HIGHER than the reported 117%
(cons.)/ the narrative implies once framed correctly -- so the distortion, ironically, understates
rather than overstates FY26's underlying momentum, but the current wording is inaccurate and
should be corrected or explained. This is a five-questions-for-management item.
Source: Standalone P&L p.99 (line 14290-14302 of extraction); Consolidated P&L p.~124
(line 19427-19439); Board's Report / MD&A p.~65 (line 8366-8370, 9216-9230).

═══════════════════════════════════════════════════════════════════
## NEW FINDING 2: NOTE 36 "REIMBURSEMENT OF EXPENSE" COLUMN ATTRIBUTION -- RESOLVED (downgrade)
═══════════════════════════════════════════════════════════════════
🟢 Resolves Pass 1's moderate-confidence flag definitively.

Pass 1 flagged uncertainty over which related-party category the Rs 24.84 Cr (FY26) /
Rs 17.09 Cr (FY25) "Reimbursement of Expense" line in Note 36 belonged to, due to the linear
text extraction of the table. Cross-checking against the CONSOLIDATED Note 34 related-party
table (p.132) resolves this with certainty: the consolidated table (where the "Subsidiaries"
relationship category does not exist, because subsidiaries are line-by-line consolidated, not
related parties at group level) **omits the "Reimbursement of Expense" row entirely**, along
with every other row that was Subsidiaries-only in the standalone table (Revenue from operation,
Sale of Assets, Rent Paid, Purchases and Others). Every row that DID carry a value in the
"Entities with Significant Influence" / KMP / Relatives columns in the standalone table (Recovery
of Expense, Rent Received, Brand Promotion, IT Services, Remuneration lines, the two IP/licensing
lines, CSR, Fund Transfer for Gratuity) reappears in the consolidated table with identical
figures. This confirms "Reimbursement of Expense" is a 100%-Subsidiaries-column item (i.e.,
ordinary intercompany cost recharge to/from the wholly-owned German subsidiary and its step-down
Hungarian entity), eliminated on consolidation, and has NO connection to the promoter-linked
"significant influence" entity category (Sunev Pharma, Spine Software, Tark AI, the two trusts).
Downgrade from 🟡 Watch (moderate confidence) to 🟢 Clean/routine. This does NOT reduce the
severity of the separate Rs 30 Cr IP purchase / Rs 21.55 Cr licensing-advance flags (Finding 3
below and Pass 1 Rank 1), which remain fully in the Entities-with-Significant-Influence column
in both standalone and consolidated tables.
Source: Std Note 36 (p.112, line 17864-17869); Cons Note 34 (p.132, line 23037-23099).

═══════════════════════════════════════════════════════════════════
## NEW FINDING 3: Rs 21.55 CR LICENSING ADVANCE -- EXHAUSTIVE SEARCH CONFIRMS NO TRACE (escalation)
═══════════════════════════════════════════════════════════════════
🔴 Escalates Pass 1's Watch item toward Red Flag.

Pass 1 could not trace the FY25 "Advance for in Licensing for Technology" (Rs 21.55 Cr,
Note 36) to a specific balance-sheet line and flagged it as NOT FOUND IN DOCUMENT. This pass
re-read every single non-current and current asset note line by line specifically hunting for
it: Note 4 (Other Financial Assets, non-current: Share Application Money, Security Deposit,
Fixed Deposits >1yr -- no match), Note 5 (Other Non-Current Assets: Advances for Capital Goods
Rs 3.98 Cr only -- too small and wrong category), Note 11 (Other Financial Assets, current:
Advance to Staff Rs 0.36 Cr only), Note 12 (Current Tax Assets), Note 13 (Other Current Assets:
Balance with Govt Authorities, Income Tax Demand Paid, Advance to Suppliers Rs 2.45 Cr, Prepaid
Expenses, Export Incentive Recoverable -- none match), and there is no "Intangible Assets Under
Development" note anywhere in the AR (a note IND AS 38 / Schedule III would normally carry
alongside Note 2C if the advance were sitting there as a work-in-progress intangible). The
Rs 21.55 Cr genuinely does not appear, as an asset, anywhere in the FY25 or FY26 balance sheet
notes in this extraction. Also confirmed via the AR's own narrative (p.~52-55, R&D section) that
there IS a real, separately identified in-licensing deal in FY26 -- MET-X, a metallo-beta-
lactamase inhibitor in-licensed from **Infex Therapeutics, UK** -- but that counterparty is an
unrelated third party, explicitly NOT one of the five "significant influence" entities named in
Note 36. The Rs 21.55 Cr related-party advance and the Infex/MET-X in-licensing deal are two
different things; conflating them would be a misread. The related-party advance's counterparty
and resting place remain genuinely undisclosed. Given the Rs 30 Cr Patent IPR purchase in the
SAME prior year (FY25) landed cleanly and traceably in Note 2C's intangible gross block, the
absence of ANY balance-sheet trace for the Rs 21.55 Cr advance is a sharper disclosure gap than
a merely "not itemised" one -- an advance of this size should sit on the balance sheet as a
prepayment/receivable until the underlying licence is delivered, capitalised, or expensed, and
none of those outcomes is visible.
Source: Notes 4, 5, 11, 12, 13 (p.106-107, full re-read); Note 2C (p.105, no separate
"Intangibles Under Development" note exists in this AR); MD&A Infex/MET-X references (p.~52-55,
line 3942, 5145, 5219, 10693, 10803).

═══════════════════════════════════════════════════════════════════
## NEW FINDING 4: STANDALONE P&L HAS NO SEPARATE "FINANCE COSTS" LINE DESPITE NEW LEASE INTEREST
═══════════════════════════════════════════════════════════════════
🟡 Watch -- new presentation-quality observation.

Note 2D (p.105-106) discloses a new lease liability in FY26 (first year) with "Finance Cost
accrued during the year" of Rs 54.85 Lakhs (Rs 0.55 Cr). The Standalone Statement of Profit &
Loss (p.99), however, has NO separate "Finance Costs" line item at all -- its expense lines run
Cost of Materials, Purchase of Stock-in-Trade, Changes in Inventories, Employee Benefit, Depn &
Amortisation, Selling/Manufacturing/Admin (Note 29), R&D (Note 30), with no finance-cost row.
Total Expenses tie out arithmetically to the reported Rs 64,951.10 Lakhs, so the Rs 0.55 Cr must
be embedded, unidentified, inside one of the Note 29 sub-categories. By contrast, the
CONSOLIDATED P&L (p.~124) DOES carry a separate "Finance Costs" line (Rs 3.67 Lakhs FY26 /
Rs 6.54 Lakhs FY25) -- but that figure is unrelated to the new lease (it is interest on the
now-repaid subsidiary working capital loan, per Cons Note 17/p.127) and is far too small to
contain the Rs 54.85 Lakh standalone lease interest either. Ind AS 1 / Schedule III generally
expects finance costs (including Ind AS 116 lease interest) to be presented as a distinct line
on the face of the P&L; its absence here, in the first year the company has any lease liability
at all, is a minor disclosure-quality gap worth naming, not a reconciliation error.
Source: Note 2D (p.106, line 16047-16049); Standalone P&L (p.99, line 14256-14286); Cons P&L
(p.~124, line 19408-19411); Cons Note 17 (p.127).

═══════════════════════════════════════════════════════════════════
## NEW FINDING 5: PPE DELETIONS (Note 2A) -- GRANULAR CHECK CONFIRMS ROUTINE SCRAPPING, NOT VALUE LOSS
═══════════════════════════════════════════════════════════════════
🟢 Confirmatory detail, strengthens Pass 1's "no anomalies" read on PPE.

Pass 1 reported PPE gross deletions of Rs 20.11 Cr for FY26 without asset-class detail. The
category-level Note 2A table (p.104-105) shows these deletions are concentrated in three asset
classes: R&D Equipment (gross deletion Rs 9.08 Cr, accumulated-depreciation deletion Rs 8.70 Cr
-- net book value written off only Rs 0.38 Cr), Computer/IT & Communication Equipment (gross
deletion Rs 5.20 Cr, accumulated-depreciation deletion Rs 5.20 Cr exactly -- NBV write-off nil,
i.e. fully depreciated assets scrapped), and Plant & Machinery (gross deletion Rs 5.76 Cr,
accumulated-depreciation deletion Rs 5.35 Cr -- NBV write-off Rs 0.41 Cr). Together these three
lines account for Rs 20.04 Cr of the Rs 20.11 Cr total deletions (99.6%). This confirms the large
gross deletions are routine retirement/scrapping of largely-to-fully depreciated older equipment
(consistent with the company's stated capex ramp replacing older R&D/IT/production assets), not
disposal of active, undepreciated assets at a loss. No P&L "loss on sale/disposal of assets" line
is disclosed separately in Note 29, consistent with an immaterial net NBV write-off (~Rs 0.8 Cr
combined). Reassuring detail, no action needed.
Source: Note 2A (p.104-105, line 15497-15736).

═══════════════════════════════════════════════════════════════════
## NEW FINDING 6: PATTERN OF UNDISCLOSED "OTHER X EXPENSES" CATCH-ALL LINES EXTENDS BEYOND SELLING
═══════════════════════════════════════════════════════════════════
🟡 Watch -- minor extension of a Pass 1 flag, not a new severity.

Pass 1 flagged "Other Selling Expenses" (+92.5%, Rs 34.68 Cr FY26) as an undisclosed catch-all.
Re-reading Note 29 in full (p.110, Administration Expenses sub-table) shows the same disclosure
pattern recurs, at smaller scale, in two further lines with zero sub-breakdown anywhere in the
notes: "Other Administrative Expenses" Rs 7.19 Cr (FY26) vs Rs 6.09 Cr (FY25), +18.1%, and
"Other Corporate Expenses" Rs 1.94 Cr vs Rs 1.45 Cr, +34.0%. Neither is individually alarming in
growth rate (the first roughly tracks core sales growth of 13.0%; the second is a small absolute
increase of Rs 0.49 Cr), but together with "Other Selling Expenses" they show the Note 29
disclosure structure carries an undifferentiated "Other" bucket in all three of its
sub-categories (Manufacturing/Admin/Selling), not just the one Pass 1 named. Worth noting once
as a structural disclosure-granularity observation rather than three separate flags.
Source: Note 29(B) (p.110, line 17576-17582).

═══════════════════════════════════════════════════════════════════
## NEW FINDING 7: PROMOTER SHARE PLEDGE -- RESOLVED CLEAN (found outside the Notes)
═══════════════════════════════════════════════════════════════════
🟢 Positive resolution of a Pass 1-noted scope gap.

Pass 1 correctly noted that Note 14 (Equity Share Capital) does not carry a pledge/encumbrance
schedule and that such disclosure typically sits outside the Notes to Financial Statements. This
pass located it: the Corporate Governance section of the AR (p.~46) states explicitly,
"PLEDGE OF PROMOTER'S SHAREHOLDING: No promoter holding is under pledge." This closes the
question cleanly -- no promoter shares are pledged. Included here for completeness since it
strengthens the balance-sheet-quality picture (debt-free, no pledged promoter stock, clean
receivables) alongside Pass 1's Rank 10 finding.
Source: Corporate Governance Report, p.~46 (line 9738-9739). Outside the Notes to Financial
Statements proper; flagged as context, not a Notes-sourced finding.

═══════════════════════════════════════════════════════════════════
## NEW FINDING 8: CWIP MD&A CONTEXT -- NEW CAPEX NARRATIVE DOES NOT ADDRESS THE AGED >3YR TRANCHE
═══════════════════════════════════════════════════════════════════
🟡 Watch -- sharpens Pass 1's Rank 2 finding, does not resolve it.

The Board's Report / Risk Management section (p.~57-58) explains the FY26 CWIP build as funding
"lyophilisation and other high-value manufacturing lines" -- useful context Pass 1 did not have,
since Pass 1 was scoped to the Notes only. However, this narrative describes the NEW additions
during the year (Rs 31.55 Cr per Note 2B) and does not mention or address the pre-existing >3-year
aged CWIP bucket (Rs 20.84 Cr at FY26 year-end, essentially unchanged in absolute terms from
Rs 20.48 Cr at FY25 year-end -- i.e., this tranche predates the FY26 expansion story and was
already aged >3 years as of the FY25 balance sheet too). The lyophilisation narrative explains
the new capex; it does not explain, or even acknowledge, the legacy aged balance. Pass 1's
question about whether the aged tranche represents active or stalled/abandoned projects remains
open. Source: Board's Report, p.~57-58 (line 8393-8402, 8582-8585); Note 2B (p.105).

═══════════════════════════════════════════════════════════════════
## VERIFICATION OF PASS 1 TOP-10 FIGURES AGAINST PRIMARY STATEMENTS -- ALL CONFIRMED
═══════════════════════════════════════════════════════════════════
Cross-checked every Pass 1 Top-10 figure directly against the Standalone Balance Sheet (p.98) and
Standalone Statement of Profit & Loss (p.99), not just against the individual notes:
- Total Equity Rs 689.63 Cr, Trade Receivables Rs 116.39 Cr, Trade Payables Rs 110.77 Cr
  (Rs 12.41 Cr MSME + Rs 98.36 Cr Others), Inventory Rs 129.37 Cr, Cash Rs 23.54 Cr, Investments
  (non-current Rs 163.95 Cr + current Rs 73.80 Cr) -- all tie exactly to the Balance Sheet face.
- Revenue Rs 768.73 Cr, PAT Rs 99.31 Cr, EPS Rs 74.29, GST contingent liability Rs 19.26 Cr, new
  Gratuity provision Rs 1.03 Cr / Past Service Cost Rs 2.88 Cr -- all tie exactly to the P&L face
  and Note 44.
No discrepancies found between any Pass-1-cited note figure and the primary statements, other
than the newly surfaced Exceptional Items line (Finding 1), which sits on the P&L face itself
and was not a Pass-1 Top-10 item at all -- it was simply missed.

Confirmed unresolved (re-checked, genuinely NOT FOUND, no new information located):
- Nature/underlying issue of the GST disputed demand (Note 44) -- amount only, no narrative
  anywhere in the AR.
- Nature of the gratuity plan amendment behind the Rs 2.88 Cr Past Service Cost (Note 27.3) --
  no narrative anywhere in the AR.
- Composition of "Other Payable" (Note 19, Rs 15.82 Cr) -- no sub-breakdown anywhere.
- Identity of the specific related-party counterparty (among the five named "significant
  influence" entities) behind the Rs 30 Cr Patent IPR purchase and the Rs 21.55 Cr licensing
  advance (Note 36) -- neither director-profile disclosures nor any other AR section names it.

═══════════════════════════════════════════════════════════════════
## PASS 2 NEW FINDINGS SUMMARY
═══════════════════════════════════════════════════════════════════
1. 🔴 NEW: Undisclosed Rs 9.91 Cr exceptional item in FY25 P&L (standalone and consolidated),
   nil in FY26 -- and the Board's Report/MD&A statement "no exceptional items in either direction
   distorting the comparison" is factually incorrect against the company's own P&L Statement and
   its own Financial Highlights table. Nature of the item is NOT FOUND IN DOCUMENT. (P&L Statement
   p.99/p.~124; Board's Report p.~65)
2. 🟢 RESOLVED: Note 36 "Reimbursement of Expense" (Rs 24.84 Cr FY26) confirmed via consolidated
   Note 34 cross-check to be a 100% Subsidiaries-column (intercompany) item, unrelated to the
   promoter-linked "significant influence" entity category. Downgraded from Watch to Clean.
3. 🔴 ESCALATED: Rs 21.55 Cr related-party licensing advance (FY25) confirmed, after exhaustive
   note-by-note search of every asset note, to have NO traceable resting place anywhere on the
   FY25 or FY26 balance sheet. Distinct from the unrelated, third-party Infex Therapeutics
   (UK) MET-X in-licensing deal referenced in the MD&A.
4. 🟡 NEW: Standalone P&L carries no separate Finance Costs line despite a new Rs 0.55 Cr
   lease-liability interest cost in FY26 (first year of any lease) -- embedded, unidentified,
   inside Note 29.
5. 🟢 NEW (confirmatory): PPE deletions (Rs 20.11 Cr) are 99.6% concentrated in largely/fully
   depreciated R&D Equipment, Computer/IT Equipment and Plant & Machinery -- routine scrapping,
   combined NBV write-off only ~Rs 0.8 Cr. No value-destructive disposal signal.
6. 🟡 NEW (minor): the undisclosed "Other X Expenses" catch-all pattern (Pass 1 named Other
   Selling Expenses) extends to Other Administrative Expenses (+18.1%) and Other Corporate
   Expenses (+34.0%), both smaller and less alarming, but structurally the same gap.
7. 🟢 NEW (positive, outside Notes): "No promoter holding is under pledge" -- found in the
   Corporate Governance section, resolving Pass 1's noted scope gap cleanly.
8. 🟡 NEW (context, outside Notes): MD&A explains the new FY26 CWIP additions as funding
   lyophilisation capacity, but this narrative does not address or explain the pre-existing,
   unchanged >3-year aged CWIP tranche (Rs 20.84 Cr) -- Pass 1's open question stands.
9. Verification pass: every Pass 1 Top-10 figure ties out exactly to the primary Balance Sheet
   and P&L Statement; no numeric discrepancies found. Four Pass-1 NOT FOUND items (GST dispute
   nature, gratuity amendment nature, Other Payable composition, RPT counterparty identity)
   re-confirmed as genuinely absent from the document after a further targeted search.

**PASS 2 STATUS: Complete.** Both standalone and consolidated note sets re-read in full against
the Pass 1 output; primary financial statements (Balance Sheet, P&L Statement, both standalone
and consolidated) cross-checked line by line for the first time in this pass; targeted searches
run for RPT counterparty names, pledge disclosure, ICD/loan-given disclosures, and exceptional/
one-time-item language across the full document. Ready for Pass 3 (pattern pass + consolidation).
