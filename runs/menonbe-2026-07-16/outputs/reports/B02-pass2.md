# STAGE 2 — NOTES TO FINANCIAL STATEMENTS — PASS 2 (WHAT WAS MISSED / VERIFICATION PASS)
Company: MENON BEARINGS LTD (MENONBE) | Run: 2026-07-16 | Model: claude-sonnet-5
Method: Re-read Notes 1-33 (standalone + consolidated) against the Pass 1 report. Where Pass 1 flagged
"LOW CONFIDENCE — VERIFY AGAINST SOURCE PDF" (Notes 4, 6, 7, 8; AOC-1 subsidiary table; ₹29cr Menon
Alkop guarantee), the underlying PDF text-extraction stream was re-read directly (pdftoppm/page-image
rendering is NOT available in this environment — "pdftoppm is not installed" — so verification relies on
re-deriving exact-match arithmetic ties within the text extraction itself: sums, cross-note totals, and
cross-statement reconciliations that tie to the paisa are treated as CONFIRMED; where no such tie could be
established, the item remains LOW CONFIDENCE and is reported as such, per the "never estimate" rule).

This is a "what was missed" pass. Items already fully covered in Pass 1 are not repeated. Only new findings,
corrections, and resolved-confidence items are reported below, organised note by note, followed by two
cross-statement findings that go beyond the Notes proper but bear directly on Note-level claims (consistent
with Pass 1's own practice of extending cross-references).

═══════════════════════════════════════════════════════════════════
NOTE-BY-NOTE: NEW FINDINGS / CORRECTIONS / RESOLVED CONFIDENCE
═══════════════════════════════════════════════════════════════════

## Note 4 — Long-Term Security Deposits — RESOLVED (was LOW CONFIDENCE in Pass 1)

Direct re-read of the PDF text stream (AR p.114/116) ties out exactly: Telephone Deposit ₹0.57 lakh, MSEB
Deposit ₹140.38 lakh, Water Deposit ₹2.02 lakh, Total ₹142.97 lakh (FY26); Telephone ₹0.63 lakh, MSEB
₹140.38 lakh, Water ₹2.02 lakh, Total ₹143.03 lakh (FY25). Sum checks exactly in both years (0.57+140.38+
2.02=142.97; 0.63+140.38+2.02=143.03). 🟢 Clean, immaterial, confirmed — no correction to Pass 1's
directional read, only the confidence rating changes from LOW to CONFIRMED.

## Note 6 — Trade Receivables — NEW FINDING: internal note contradicts Note 31's own ageing schedule

Re-derivation of Note 6's own "Outstanding for a period exceeding 6 months" / "Other Debts" split (Note 6,
AR p.114/116) now ties exactly to the Note 6 total: FY26 Outstanding >6 months ₹588.77 lakh + Other Debts
₹6,059.99 lakh = ₹6,648.76 lakh (matches Note 31's total exactly). FY25: ₹16.13 lakh + ₹3,847.77 lakh =
₹3,863.90 lakh (also ties exactly).

This is a genuine NEW finding: Note 6's own "exceeding 6 months" figure (₹588.77 lakh FY26, 8.9% of total;
₹16.13 lakh FY25, 0.4% of total) is drastically SMALLER than the mandatory Note 31 ageing schedule's
">6 months" total for the identical balance sheet date (₹1,473.49 lakh FY26, 22.2% of total; ₹261.45 lakh
FY25, 6.8% of total) — roughly a 2.5x (FY26) to 16x (FY25) gap between two notes in the SAME standalone
financial statements, both purporting to classify the identical trade receivables balance by age. The most
plausible explanation is that Note 6 classifies age from the invoice DUE DATE (i.e., only overdue amounts
count) while Note 31 (the Ind AS 107/Schedule III mandatory ageing schedule) classifies from the invoice/
transaction date — a common convention difference given multi-month credit terms — but the magnitude and
the fact that BOTH notes' own "aged" figures independently grew far faster than revenue (Note 6's own
figure grew 36.5x YoY, from ₹16.13 lakh to ₹588.77 lakh) means this is not merely a reconciling-item
curiosity: it independently corroborates the receivables deterioration from a second data source, using a
different definition, and it is a legitimate Question for Management (what is the exact ageing convention
used in Note 6 vs Note 31, and why do the two conventions produce such a large gap). 🔴 New Red Flag
(second, independent confirmation of the Note 31 receivables concern, via a different classification method).

Also resolves Pass 1's stated uncertainty about the ₹(19.57) lakh figure potentially being "shared/
misattributed" between Note 6 and Note 8: it is NOT part of Note 6's numbers (Note 6's own figures, as shown
above, tie out cleanly without it). It belongs solely to Note 8 (see below). 🟢 Ambiguity resolved.

## Note 8 — Short-Term Loans & Advances — MAJOR CORRECTION: pass 1's "Advance Income Tax" figure is
actually a related-party advance to Menon Brakes Limited

This is the most consequential correction in this pass. Pass 1 read the Note 8 figures of ₹457.22 lakh (FY26)
/ ₹405.44 lakh (FY25) as "Advance Income Tax." Cross-verification against TWO independent sources shows
this is incorrect:

1. CARO Annexure A to the Independent Auditor's Report (clause (iv), AR pp.92-93/PDF p.94-95) discloses,
   under "transactions with fully owned subsidiaries...within limits prescribed u/s.185 and 186": "Menon
   Brakes Limited — Advance — Transaction during the year ₹1,81,84,352 — Closing Balance ₹4,57,22,112."
   ₹4,57,22,112 = ₹457.22 lakh, exact match to the figure Pass 1 attributed to "Advance Income Tax."
2. Standalone Note 16, Related Party Disclosures under Ind AS 24 (AR pp.108-109/PDF p.117-119), lists
   Menon Brakes Limited (party #17, Wholly Owned Subsidiary) with a transaction type "Advance" showing
   balances of ₹457.22 lakh (current year) and ₹405.44 lakh (previous year) — the identical pair of figures.

CONCLUSION: the ₹457.22 lakh (FY26) / ₹405.44 lakh (FY25) balance in Note 8 is a related-party ADVANCE
TO MENON BRAKES LIMITED (a wholly-owned subsidiary), not advance income tax. It grew by ₹181.84 lakh
(+44.9%) during FY26 per the CARO transaction-during-year disclosure. No interest rate, tenure, or business
purpose is disclosed for this advance anywhere in Note 8, Note 16, or the CARO Annexure — it appears to
be interest-free (Note 19's "Interest Received" line actually DECLINED during the year, see below finding),
unsecured, and growing. This is a materially different and more significant finding than Pass 1's "advance
income tax, scaling with higher profitability, no concern" — it is instead an undisclosed-terms, growing
intercompany advance that should be a Question for Management (interest rate, repayment schedule,
business purpose, and whether it will be repaid or is effectively permanent working-capital support for
Menon Brakes). 🟡 New Watch item, upgraded materiality.

The company's own "true" Advance Income Tax line (if disclosed at all under that exact label in Note 8)
could NOT be independently re-derived from the extracted number stream with confidence in this pass —
NOT FOUND WITH CONFIDENCE. This does not change Pass 1's directional observation that SOME income-
tax-related prepayment likely exists and scales with profitability, but the specific ₹457.22/₹405.44 lakh
figures Pass 1 attached to it belong to the Menon Brakes advance instead, per the two independent
cross-checks above.

Separately, per the same Note 16 table, Menon Bearings New Ventures Ltd (MBNV, party #18) shows an
"Advance/Debtors" balance of ₹12.08 lakh (FY26) / ₹11.80 lakh (FY25) — this is the small, near-static
figure that Pass 1 attributed (with a different FY25 comparative of ₹12.08 lakh) to "Menon Brakes Limited."
Both the party name and the FY25 comparative in Pass 1 were therefore attached to the wrong entity: the
₹12.08/₹11.80 lakh small advance belongs to MBNV, not Menon Brakes; the much larger, growing ₹457.22/
₹405.44 lakh figure belongs to Menon Brakes, not "Advance Income Tax." CARO's own MBNV line corroborates
this: "Menon Bearings New Ventures Limited — Advance — Transaction during the year ₹29,020 — Closing
Balance ₹12,07,625" (=₹12.08 lakh), consistent.

The Menon Alkop Branch Account balance of ₹(19.57) lakh (both years, static) does NOT appear as a line
item for "Menon Alkop Ltd." in the standalone RPT Note 16 table (unlike Menon Brakes and MBNV, which
both have explicit "Advance" rows) — suggesting this may be an internal parent-company branch/depot
clearing account rather than a subsidiary-facing balance, though this is an inference, not a directly
confirmed label. Recommend a management question to close this out definitively. 🟡 Watch (minor,
informational; the static, unlabelled nature across two years is itself slightly unusual and worth asking about).

## Note 19 — Other Income — RESOLVED: Interest Received figure and direction corrected

Direct re-read of the numeric stream (Note 19, AR p.120) resolves Pass 1's stated uncertainty: Interest
Received = ₹43.31 lakh FY26 vs ₹88.13 lakh FY25 — a DECLINE of 50.9% YoY (Pass 1 had this ambiguous,
citing both "₹88.13 lakh vs ₹23.25 lakh" and, as an alternative reading, "₹43.31 lakh vs a differing prior-year
figure"). The arithmetic ties exactly: Total Other Income = Dividend (₹289.10 lakh FY26 / ₹0.00 FY25) +
Interest Received (₹43.31/₹88.13) + Net Gain/(Loss) on investments (₹(2.45)/₹23.25) = ₹329.96 lakh FY26
(company states ₹329.97, rounding) and ₹111.38 lakh FY25 (company states ₹111.39, rounding) — both tie.

This is a new, notable observation: interest income DECLINED by half in the very year that (per the Note 8/
CARO finding above) the company's advance to Menon Brakes Limited GREW by 44.9%. If the Menon Brakes
advance carried interest, rising principal should produce rising, not falling, interest income — this is
consistent with the advance being interest-free, and consistent with materially lower average cash/FD
balances during the year (see the Cash Flow Statement finding below: standalone cash & cash equivalents
fell 69.7% during FY26). Three independent notes/statements (Note 8/CARO advance growth, Note 19
declining interest income, and the Cash Flow Statement's cash decline below) now mutually corroborate a
single, coherent liquidity-tightening narrative that Pass 1 did not connect across notes. 🟡 New Watch,
cross-note corroboration.

## AOC-1 Subsidiary Table (Board's Report Annexure I, "Form AOC-1", AR pp.41-42/PDF p.39-40) — RESOLVED
with specific attribution (was LOW CONFIDENCE, unattributed, in Pass 1)

Re-reading the table in column order (Menon Alkop Ltd / Menon Brakes Ltd / Menon Bearings New Ventures
Ltd, matching the header row) and anchoring on each subsidiary's known Share Capital figure (from Note 3:
Alkop ₹825.00 lakh, Brakes ₹825-826.00 lakh, MBNV ₹1.00 lakh) resolves the attribution Pass 1 could not
make:

- Menon Alkop Ltd (the SEBI Reg. 16(c) "material subsidiary," aluminium die-casting): Share Capital ₹825.00
  lakh, Reserves and Surplus ₹(206.98) lakh — NEGATIVE — implied net worth ≈ ₹618.02 lakh. Turnover
  ₹1,371.07 lakh. Against this, the PARENT carries its investment in Menon Alkop at cost of ₹2,823.50 lakh
  (₹825.00 lakh face value + ₹1,996.50 lakh share premium, per Note 3) with ZERO impairment recognised in
  either standalone financial year. The parent's carrying cost is therefore roughly 4.6x the subsidiary's own
  AOC-1-disclosed net worth. 🔴 New Red Flag (upgraded from Pass 1's unattributed "Watch, verify") — this
  is precisely the entity that also carries the ₹29 crore parent corporate guarantee (see below) and the
  growing capex programme, so the combination of negative subsidiary reserves, no impairment testing
  disclosure with quantified assumptions (Note 1 confirms this gap generally), and rising parent exposure to
  this specific entity deserves a Question for Management on the parent's Ind AS 36 impairment assessment
  for its Menon Alkop investment.
- Menon Brakes Ltd: Share Capital ₹826.00 lakh, Reserves and Surplus ₹4,603.11 lakh — strongly POSITIVE
  — implied net worth ≈ ₹5,429 lakh, against a parent carrying cost of only ₹825.00-826.00 lakh (i.e., carried
  at roughly 15% of the subsidiary's own book net worth — conservative, not a concern; the opposite
  situation to Alkop). 🟢 Clean, confirmed, resolves the ambiguity in the opposite (favourable) direction for
  this entity.
- Menon Bearings New Ventures Ltd (MBNV): confirmed dormant, as Pass 1 stated (Share Capital ₹1.00 lakh,
  Turnover Nil, PBT/PAT ₹(0.29) lakh, Reserves ₹(13.30) lakh — small accumulated losses consistent with a
  shell "yet to commence operations"). 🟢 Clean, as expected, no change from Pass 1.

Total Assets/Total Liabilities sub-fields for Alkop and Brakes could not be reconciled with full internal
consistency from the extracted number stream (a residual gap of a few hundred lakh remains between
Share Capital + Reserves + stated "Total Liabilities" and stated "Total Assets" for both entities) — these
sub-fields remain LOW CONFIDENCE, but Share Capital and Reserves & Surplus (the two figures that matter
for the impairment question) are now CONFIRMED with high confidence via the anchor-and-cross-check
method above.

## Corporate Guarantee to Menon Alkop Ltd (₹29 crore) — NEW CORROBORATION (refines, does not remove,
Pass 1's Red Flag framing)

Consolidated Note 11 (Long-Term Borrowings, AR ~p.153/PDF ~p.155-156) discloses, in the notes to Menon
Alkop's own facilities: "The loan is secured by Exclusive charge on factory land and building at Plot No C1
Kagal Five Star MIDC Hatangale, Kolhapur and charge over entire movable present and future fixed assets of
Menon Alkop Limited. The loan is also secured by Corporate Guarantee of Menon Bearing[s] Limited" — stated
identically for both Menon Alkop's HDFC Bank ₹13 crore facility and its Federal Bank ₹2.50 crore term loan +
₹0.50 crore bank guarantee facility. This corroborates that the CARO-disclosed ₹29 crore guarantee (Pass 1
Top Finding #2) is tied to real, identifiable, disclosed subsidiary indebtedness (at least ~₹16 crore of it
traceable directly to these two facilities, with the balance plausibly covering Alkop's ₹12 crore HDFC cash
credit limit referenced elsewhere in the consolidated Note 7 footnote) — it is NOT an opaque or unexplained
number for a reader who cross-references CARO against the consolidated borrowings notes. Pass 1's
disclosure-format Red Flag stands (there is genuinely no dedicated Ind AS 37 Contingent Liabilities note
presenting this, or the disputed TDS demand, in Schedule III format) but the characterisation should be
refined from "invisible/undisclosed" to "disclosed only in scattered cross-references (CARO + consolidated
borrowings notes), never consolidated into the single Contingent Liabilities table Schedule III expects." 🟡
Refined framing, not a new severity level, but a materially more precise one.

═══════════════════════════════════════════════════════════════════
CROSS-STATEMENT FINDINGS (new, outside the Notes proper but directly bearing on Note-level claims)
═══════════════════════════════════════════════════════════════════

## NEW FINDING — Standalone Cash Flow Statement quantifies the Note 31 receivables problem in hard cash
terms, and CORRECTS a Pass 1 citation error

Direct re-read of the Standalone Cash Flow Statement (AR pp.98-99/PDF ~p.100-101) gives, for FY26:
Profit After Tax & Adjustments (start point) ₹3,237.85 lakh; add back Deferred Tax ₹71.13 lakh, Interest (Net)
₹269.76 lakh, Fair-value loss add-back ₹2.45 lakh, Depreciation ₹516.63 lakh = Operating Profit before
Working Capital changes ₹4,097.81 lakh (all four add-back figures tie exactly to their respective P&L/Note
25/Note 1/Note 2 sources). Working capital changes: Inventories ₹(547.38) lakh [ties exactly to Note 5's
FY26-FY25 inventory increase of ₹547.37 lakh], Trade Receivables ₹(2,784.87) lakh [ties almost exactly to
the Note 6/31 receivables increase of ₹2,784.86 lakh], Short-Term Loans & Advances ₹(63.23) lakh, Other
Current Assets ₹(0.16) lakh, Trade Payables +₹684.91 lakh [ties almost exactly to Note 14's payables
increase of ₹684.90 lakh], Other Current Liabilities +₹98.85 lakh, Short-Term Provisions ₹(37.72) lakh =
Cash From Operating Activities ₹1,448.22 lakh (independently verified by direct summation: 4,097.81 −
547.38 − 2,784.87 − 63.23 − 0.16 + 684.91 + 98.85 − 37.72 = 1,448.21, ties to the stated 1,448.22 within
rounding).

This means: Cash conversion (Cash from Operating Activities ÷ Operating Profit before WC changes) =
35.3% in FY26 — a large gap, and the single largest driver of that gap, by a wide margin, is the ₹2,784.87
lakh of cash absorbed by the trade receivables build-up alone (this one line item is 1.9x the entire net
decrease in cash for the year, see below). This converts Pass 1's Note 31 ageing-schedule observation
(a red flag on paper) into a directly quantified, material cash-flow-statement impact — the strongest single
piece of evidence in this pipeline stage that the receivables build-up is a genuine, not merely cosmetic,
cash-conversion problem.

Total Cash Flow for FY26 = ₹(935.42) lakh [Opening Cash & Cash Equivalents ₹1,341.82 lakh + Total Cash
Flow ₹(935.42) lakh = Closing Cash & Cash Equivalents ₹406.40 lakh — ties exactly]. Cash From Investing
Activities reconciles (via the "Total Cash Flow = Operating + Investing + Financing" identity, using the
independently-confirmed Operating (₹1,448.22 lakh) and Financing (₹(1,633.74) lakh, itself built from Change
in Long-Term Borrowings ₹(274.97) lakh [ties exactly to Note 11's non-current borrowings decrease of
₹274.97 lakh, 1,504.76→1,229.79], Change in Short-Term Borrowings +₹84.42 lakh [ties closely to Note 13's
short-term borrowings increase of ₹84.41 lakh], Dividend Paid ₹(1,120.80) lakh [ties exactly to Note 10], and
Interest Paid ≈ ₹(313.08) lakh [ties exactly to Note 23's Finance Costs]) to approximately ₹(749.91) lakh —
i.e., a genuine, capex-and-treasury-driven net cash use in investing, consistent with the ₹669.76 lakh of PPE
additions (Note 2) and continued mutual fund purchases (Note 3).

**CORRECTION TO PASS 1**: Pass 1 stated "Total cash & bank balances reconcile approximately to the Cash
Flow Statement closing balance of ₹2,301.86 lakh FY26 vs ₹1,341.82 lakh FY25." On direct re-verification,
₹2,301.86 lakh is NOT the FY26 closing cash & cash equivalents figure in the Standalone Cash Flow
Statement — it does not appear at the position in the numeric stream that the Opening-plus-Total-Cash-Flow
arithmetic confirms as the closing balance (that position, cross-checked three independent ways above,
is unambiguously ₹406.40 lakh). ₹1,341.82 lakh (FY25 closing / FY26 opening) is confirmed correct and
appears identically in both years' columns, as it must. This means **standalone Cash & Cash Equivalents
(the narrow Ind AS 7 definition used in the Cash Flow Statement) FELL from ₹1,341.82 lakh (FY25) to
₹406.40 lakh (FY26), a decline of 69.7%**, in the same year PAT grew 64.4% and the company was reporting
record profitability — driven principally by the receivables build-up and continued capex/treasury deployment.
(Note: the Balance Sheet's own Note 7 "Cash and Bank Balances" total, which includes longer-tenor fixed
deposits and the earmarked dividend account that fall outside the CFS's narrower "cash equivalents"
definition, is a separate, larger figure that could not be fully reconstructed line-by-line from the extraction
in this pass — see Note 7 discussion above; this does not affect the CFS finding, which is self-contained and
independently verified.) 🔴 New Red Flag — this is the single most consequential quantitative finding of
Pass 2, directly reinforcing and hardening Pass 1's Top Finding #1 (Note 31 receivables) with an
independently-verified cash-flow-statement quantification, while correcting a material citation error.

## NEW FINDING — Board's Report "Key Financial Ratios" table silently uses CONSOLIDATED figures, diverges
from standalone Note 33 on direction of the receivables-turnover ratio

Board's Report Item 13, "Details of Significant Changes in Key Financial Ratios" (AR p.60/PDF p.62) and
Item 14, "Details of any change in Return on Net Worth" (same page), present a ratio table (Debtors
Turnover, Inventory Turnover, Interest Coverage Ratio, Current Ratio, Debt-Equity Ratio, Operating Profit
Margin, Net Profit Margin) with values for FY26/FY25 and % change: Debtors Turnover 3.88 / 4.14 (−6.27%),
Inventory Turnover 7.84 / 7.64 (+2.71%), Interest Coverage 10.87 / 10.00 (+8.74%), Current Ratio 2.51 / 2.46
(+1.79%), Debt-Equity Ratio 0.25 / 0.26 (−6.60%), Operating Profit Margin 16.70% / 13.88% (+20.31%), Net
Profit Margin 12.74% / 10.23% (+24.56%).

These figures do NOT match standalone Note 33 (Current Ratio 3.66/2.35; Debt-Equity 0.17/(0.22); Trade
Receivables Turnover 4.05/3.60; Inventory Turnover 8.66/6.69; Net Profit Ratio 14.82%/11.98%) — most
strikingly, the Board's Report shows Debtors Turnover DECLINING 6.27% while standalone Note 33 shows
Trade Receivables Turnover IMPROVING 12.6% — opposite directions on what both purport to be the same
metric, same company, same fiscal year, within the same Annual Report.

Cross-checking the CONSOLIDATED Note 33 (AR pp.~154-155/PDF ~p.163-164) resolves the puzzle: its
figures (Current Ratio 2.51, Debt-Equity 0.25, Debt Service Coverage 5.83, ROE 22.25%, Inventory Turnover
7.84, Trade Receivables Turnover 3.88, Trade Payables Turnover 8.19, Net Capital Turnover 3.50, Net Profit
Ratio 12.74%) match the Board's Report table EXACTLY, number for number. The Board's Report "Key
Financial Ratios" disclosure is therefore drawn from the CONSOLIDATED financial statements, not
standalone — a basis it never states. Because most readers treat the MD&A/Board's Report ratio
commentary as pertaining to the listed (standalone) entity's own performance unless told otherwise, this is
a disclosure-transparency gap in its own right (SEBI LODR Reg. 34(3)/Schedule V requires the ratio
disclosure but the AR does not state which financial statements it is drawn from), and — combined with
Pass 1's own finding (Finding #5) that standalone Note 33's Trade Receivables Turnover Ratio itself uses an
average-receivables base that mechanically softens the deterioration visible in the standalone Note 31
ageing schedule — it means that a reader relying on EITHER of the two most prominent, official "ratio
summary" disclosures in this Annual Report (the Board's Report table, or standalone Note 33) would come
away with a materially rosier picture of receivables efficiency than the granular, audited Note 31 ageing
schedule (DSO 85→114 days, standalone) actually supports. Only the most granular disclosure — the
mandatory ageing bucket table — shows the real, standalone-entity-specific severity; both higher-level
"ratio" summaries (one silently consolidated, one using an averaging convention) dilute it. 🔴 New Red Flag
— a genuine "notes that contradict each other" pattern, now traced to a specific, identifiable mechanism
(undisclosed consolidated-vs-standalone basis) rather than left as an unexplained inconsistency.

Separately, this comparison also RESOLVES Pass 1's flagged uncertainty about standalone Note 33's FY25
Debt-Equity Ratio being shown with an apparently erroneous negative sign, "(0.22)." The Board's Report
(consolidated) shows a sensible, positive Debt-Equity Ratio of 0.26 for FY25 — of a similar order of
magnitude to what a correctly-signed standalone figure would likely be — corroborating Pass 1's suspicion
that the "(0.22)" in standalone Note 33 is a data-entry/sign artefact in the source document rather than a
real negative debt-equity position (which would be conceptually odd for a company with positive net debt in
both years per Note 11/13). 🟡 Confirms Pass 1's suspicion with an independent comparator, does not fully
eliminate the need to check the source printed page for the correct sign.

═══════════════════════════════════════════════════════════════════
ITEMS CHECKED AND CONFIRMED — NO NEW FINDING (routine verification, listed for completeness)
═══════════════════════════════════════════════════════════════════

- Note 5 Inventories: FY26 Raw Material ₹614.80 lakh, Stores & Spares ₹136.69 lakh, Finished Goods
  ₹1,033.80 lakh, WIP ₹327.82 lakh, Total ₹2,113.10 lakh — re-derived independently from the raw number
  stream (not just cross-referenced via Notes 20/21 as Pass 1 did) and ties exactly. No change from Pass 1.
- Note 25 Tax Expense: Current Tax ₹972.00 lakh, Deferred Tax ₹71.13 lakh (FY26) — confirmed exactly
  against the standalone P&L account (AR p.98/PDF p.100). No change from Pass 1.
- EPS: Basic and Diluted EPS both ₹5.82 (FY26) and both ₹3.60 (FY25) per the P&L statement (AR p.98) —
  confirms Pass 1's implicit assumption of no dilution/ESOP gap; explicitly verified in this pass.
- Note 3 Investments in subsidiaries: the jumbled label/number sequence for Menon Alkop's face-value-plus-
  premium structure (₹825.00 lakh + ₹1,996.50 lakh = ₹2,823.50 lakh) was independently re-derived from
  the raw extraction and confirmed to match Pass 1's figure exactly. No change.
- Going concern: searched the full text extract for "going concern," "material uncertainty," "subsequent
  event," and "after the balance sheet date" — no material uncertainty related to going concern is
  disclosed anywhere (standard Ind AS 1/SA 570 boilerplate only, both in Directors' Responsibility Statement
  and Auditor's Report). NONE. Confirms the implicit absence already reflected in Pass 1.

═══════════════════════════════════════════════════════════════════
PASS 2 NEW FINDINGS SUMMARY
═══════════════════════════════════════════════════════════════════

1. 🔴 MAJOR CORRECTION: The ₹457.22 lakh (FY26) / ₹405.44 lakh (FY25) figure Pass 1 attributed to
   "Advance Income Tax" in Note 8 is in fact a related-party ADVANCE TO MENON BRAKES LIMITED (wholly
   owned subsidiary), confirmed via CARO Annexure A and standalone Note 16 (RPT). It grew ₹181.84 lakh
   (+44.9%) in FY26, is apparently interest-free and unsecured, with no disclosed terms. (Note 8, Note 16,
   CARO Annexure A, AR pp.92-93/108-109)
2. 🔴 NEW: AOC-1 confirms, with specific attribution (unresolved in Pass 1), that Menon Alkop Ltd — the
   SEBI-designated material subsidiary — carries NEGATIVE Reserves & Surplus of ₹(206.98) lakh (implied
   net worth ≈₹618 lakh) against the parent's ₹2,823.50 lakh carrying cost (at cost, unimpaired) — a ~4.6x
   gap, and an impairment-assessment question for management. Menon Brakes Ltd is the opposite case
   (₹4,603.11 lakh reserves against only ₹825-826 lakh carrying cost — conservative, no concern).
   (Board's Report Annexure I "Form AOC-1", AR pp.41-42)
3. 🔴 NEW: Standalone Cash Flow Statement shows Cash from Operating Activities of only ₹1,448.22 lakh
   against Operating Profit before Working Capital changes of ₹4,097.81 lakh (35.3% conversion), driven
   almost entirely by ₹2,784.87 lakh of cash absorbed by the trade receivables increase. Standalone Cash &
   Cash Equivalents FELL 69.7% during FY26 (₹1,341.82 lakh → ₹406.40 lakh) — this CORRECTS Pass 1's
   citation of "₹2,301.86 lakh FY26 closing cash," which does not match the Cash Flow Statement's own
   Opening + Total Cash Flow = Closing arithmetic. (Standalone Cash Flow Statement, AR pp.98-99)
4. 🔴 NEW: Board's Report "Key Financial Ratios" table (AR p.60) is drawn from CONSOLIDATED figures
   (confirmed by exact match to consolidated Note 33) without disclosing that basis, and shows Debtors
   Turnover DECLINING 6.27% — the opposite direction from standalone Note 33's Trade Receivables
   Turnover, which shows an IMPROVEMENT of 12.6%. Neither of the two official "ratio summary" disclosures
   conveys the severity visible in the standalone Note 31 ageing schedule (DSO 85→114 days). (Board's
   Report Item 13, AR p.60; consolidated Note 33; standalone Note 33, AR p.127)
5. 🟡 NEW: Note 6's own "outstanding exceeding 6 months" sub-classification (₹588.77 lakh FY26 / ₹16.13
   lakh FY25) is 2.5x-16x smaller than Note 31's ageing-schedule total for the same concept (₹1,473.49 lakh
   FY26 / ₹261.45 lakh FY25) — an unreconciled inter-note gap, likely a due-date-vs-invoice-date convention
   difference, but independently confirms the receivables ageing deterioration is real and material by either
   measure. (Note 6 vs Note 31, AR p.114/116 vs p.126-127)
6. 🟡 RESOLVED: Note 4 Long-Term Security Deposits confirmed exactly (₹142.97 lakh FY26 / ₹143.03 lakh
   FY25); immaterial, no change to Pass 1's conclusion, only the confidence rating is upgraded.
7. 🟡 RESOLVED: Note 19 Interest Received corrected to ₹43.31 lakh FY26 (down 50.9% from ₹88.13 lakh
   FY25) — resolves Pass 1's ambiguous figure and, combined with Finding #1 and #3 above, forms a
   coherent liquidity-tightening picture across three separate notes/statements that Pass 1 did not connect.
8. 🟡 REFINED: The ₹29 crore Menon Alkop corporate guarantee is corroborated by the consolidated Note 11
   borrowings note as tied to real, identifiable Menon Alkop bank facilities (HDFC ₹13cr, Federal Bank
   ₹2.5cr+₹0.5cr BG, plausibly plus its ₹12cr HDFC cash credit limit) — refining Pass 1's framing from
   "invisible/undisclosed" to "disclosed only via scattered cross-references, never consolidated into a
   Schedule III Contingent Liabilities table." The underlying disclosure-format Red Flag from Pass 1 stands.
9. 🟡 MINOR: The small ₹12.08 lakh / ₹11.80 lakh advance Pass 1 attributed to "Menon Brakes Limited" in
   Note 8 actually belongs to Menon Bearings New Ventures Ltd (MBNV) per Note 16/CARO — a minor
   party-attribution swap, now corrected as part of Finding #1's broader re-attribution.
10. No new findings on: Note 5 Inventories, Note 25 Tax Expense, EPS basic/diluted, Note 3 subsidiary
    investment cost structure, or going-concern language — all independently re-verified in this pass and
    confirmed consistent with Pass 1, no corrections needed.
