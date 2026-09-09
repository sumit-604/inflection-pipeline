# STAGE 2 — NOTES TO FINANCIAL STATEMENTS — PASS 2 (WHAT WAS MISSED)
Company: Forbes Precision Tools and Machine Parts Ltd (TOTEM) | Run: totem-2026-09-09
Source re-read: work/text/annual-report__Annual_Report_2026.txt, Notes 1 to 44 in full (PDF p.74-128),
against the Pass 1 output at outputs/reports/02-notes-pass1.md. Figures stated in ₹ Lakhs as filed,
converted to ₹ Crore in-line (÷100). Rated 🟢 Clean | 🟡 Watch | 🔴 Red Flag.

Method: read every note again start to finish; for each, checked whether Pass 1 covered it fully. Notes
1, 2A-2C, 4, 6, 9, 10, 13, 16, 17, 18, 20, 22, 23, 25, 26, 29, 32(i)-(iii), 34(a), 40, 42, 43, 44 are
covered fully by Pass 1 (or immaterial) and are not repeated here. New findings below sit in Notes 3, 5,
15B/31, 24, 27, 30, 31, 33.1, 33.2, 33.6, 33.8, 33.9, 35, 36, 37 — either a sub-note Pass 1 skipped, a
cross-note reconciliation Pass 1 did not run, or an arithmetic check on Pass 1's own reasoning.

═══════════════════════════════════════════════════════════════
PASS 2 NEW FINDINGS
═══════════════════════════════════════════════════════════════

## NF1. Note 36 (Offsetting financial assets and liabilities) — an entire note Pass 1 did not cover 🟡

Pass 1's note-by-note walk goes from Note 34 (Contingencies) to Note 37 (Assets pledged) and never
mentions Note 36, "Offsetting financial assets and financial liabilities" (PDF p.125).

Note 36 shows the trade-receivables figure carried into Note 5 (₹32.33cr FY26 / ₹35.04cr FY25, i.e.
"gross trade receivables" as Pass 1 called it) is itself already NET of an offsetting arrangement:

| | Gross-gross receivables | Rebates/discounts offset | Net (= Note 5's "gross") |
|---|---|---|---|
| Mar-2026 | ₹37.04cr | ₹4.71cr | ₹32.33cr |
| Mar-2025 | ₹38.36cr | ₹3.32cr | ₹35.04cr |

"The Company gives rebates/discounts for Engineering segment. Under the terms of contract, the amounts
payable by the Company are offset against receivables from customers and only the net amount is settled
… presented net in the Balance Sheet." (Note 36, PDF p.125)

The rebate/discount liability netted off customers grew 41.6% YoY (₹3.32cr to ₹4.71cr) while true
gross-gross receivables actually FELL 3.4% (₹38.36cr to ₹37.04cr). This is a genuinely new fact: trade
terms toward customers appear to be getting more generous (larger rebate/discount accrual) even as the
headline receivables figure Pass 1 examined was improving. It does not overturn Pass 1's "receivables
improving" read (the net, settled figure is what matters for cash), but it is a disclosure Pass 1 missed
entirely and it qualifies the improvement: part of the better receivables optics is a bigger rebate
accrual sitting on the liability side, not purely faster collection. 🟡 Watch — worth a management
question on what is driving the rebate/discount growth.

## NF2. Note 37 (Assets pledged as security) — collateral released fell 74.9%, far larger than Pass 1's debt-equity framing conveyed 🟢/🟡

Pass 1 discussed the improving debt-equity ratio (0.14 to 0.10) but did not quantify the collateral
release itself. Note 37 (PDF p.125):

| Asset class pledged | Mar-2026 | Mar-2025 |
|---|---|---|
| Leasehold land | ₹0 | ₹7.57cr |
| Freehold buildings | ₹0 | ₹32.78cr |
| Plant & Machinery | ₹28.91cr | ₹66.04cr |
| Furniture & fixtures | ₹0 | ₹0.37cr |
| Office equipment | ₹0 | ₹0.16cr |
| Capital WIP | ₹0 | ₹8.20cr |
| **Total** | **₹28.91cr** | **₹115.12cr** |

Total pledged assets fell 74.9% (₹115.12cr to ₹28.91cr); only Plant & Machinery remains charged, and even
that fell 56.2%. This is a substantially bigger balance-sheet-quality signal than the ratio table alone
shows — nearly all real-estate and non-machinery assets have been released from lender charge. It also
sharpens the materiality of the compliance point Pass 1 already flagged (Note 41(i)): the company has NOT
yet filed the modification-of-charge / satisfaction-of-charge paperwork with the Registrar of Companies
for these released/repaid assets. Pass 1 called this "small in monetary terms" — with the collateral scale
now visible at ₹115cr+ of formerly-pledged assets, the RoC filing lapse is a bigger process gap than the
₹0 quantified penalty exposure suggested. 🟡 Watch (upgraded emphasis on the RoC point; the release itself
is 🟢).

## NF3. Employee Benefits Expense — Pass 1's "8.6% underlying growth" does not check out; correct figure is ~1.2%, and a workforce-mix disclosure explains why 🟡

Pass 1 (Rank 3 finding) wrote: "Employee benefits expense rose 14.6% YoY (₹44.03cr to ₹50.44cr) partly on
this one item [the ₹5.90cr Labour Codes charge]; without it, the underlying increase is closer to 8.6%,
roughly tracking revenue growth." Re-computing directly from Note 24 (PDF p.101-102):

Total increase FY25→FY26 = ₹50.44cr − ₹44.03cr = ₹6.41cr.
Labour Codes one-time charge (Note 39, entirely incremental to FY26) = ₹5.90cr.
Underlying (ex-Labour-Codes) increase = ₹6.41cr − ₹5.90cr = **₹0.51cr = 1.16% on the ₹44.03cr FY25 base**,
not 8.6%. Pass 1's arithmetic appears to have been mis-stated; the corrected read is that underlying
employee cost barely moved while revenue grew 7.9% — a materially more positive operating-leverage signal
than Pass 1 conveyed, not a neutral "roughly tracking revenue" one.

Note 31, Section I ("Other Details," PDF p.113) — NOT covered by Pass 1 — gives a plausible explanation:

| | Mar-2026 | Mar-2025 | Change |
|---|---|---|---|
| Number of Active Members (gratuity scheme) | 410 | 481 | −14.8% |
| Per Month Salary for Active Members (₹ Lakh, aggregate) | 149.19 | 82.46 | +80.9% |

Read together (both figures as disclosed, division is this analyst's own): average monthly salary per
active member rises from roughly ₹17,100 to roughly ₹36,400, near-doubling, while headcount on the
gratuity roll falls almost 15%. **NOT FOUND IN DOCUMENT: any explanation for either the headcount fall or
the near-doubling of average pay**, and no standalone total-headcount figure is disclosed anywhere else in
the Notes to cross-check the "481/410" reading. Two readings are consistent with the data: (a) a genuine
workforce mix shift toward fewer, higher-skilled, higher-paid employees, which would bear directly on the
transition thesis; or (b) a scope/definitional change in what "active members" means for the actuarial
valuation, possibly triggered by the Labour Codes recompute itself (Note 39), which would make the
comparison not like-for-like. The notes give no way to choose between them. 🟡 Watch — a genuine question
for management, and the combined finding (flat underlying labour cost + falling headcount + rising average
pay) is more consequential to the transition narrative than Pass 1's employee-cost line implied.

## NF4. AUD-denominated unhedged vendor-advance exposure — a specific, sizeable currency concentration Pass 1's general FX comment did not name 🟡

Pass 1 flagged the general point that FX policy claims hedging but zero derivatives are outstanding, and
the FX transaction loss rose ~6x. It did not break out currency composition. Note 33.8(a) (PDF p.121-122),
"Advances to vendors":

| | Mar-2026 | Mar-2025 |
|---|---|---|
| AUD advances to vendors | 4.94 lakh AUD = ₹3.19cr | 24.28 lakh AUD = ₹12.99cr |

At Mar-2025, unhedged AUD vendor advances alone were ₹12.99cr, 5.6% of that year's revenue — larger than
any single item in Pass 1's FX discussion — falling to ₹3.19cr at Mar-2026. This points to Australia as a
sourcing or capital-equipment geography (advances to vendors, not trade receivables, so likely
capex/import-related) and is a materially more concentrated single-currency exposure than the general
"USD/GBP/EUR/CHF/AUD, unhedged" framing in Pass 1 conveyed. The Note 33.8(b) sensitivity table confirms
a 5% AUD move would have swung FY25 PBT by ₹0.65cr (64.83 lakh), versus only ₹0.16cr (15.96 lakh) in
FY26 — the AUD exposure genuinely shrank, but was a real, sizeable risk in the prior year. 🟡 Watch.

## NF5. Interest capitalised under Ind AS 23 rose 4.1x — a small item Pass 1 did not surface at all 🟢

Note 35 (Net debt reconciliation, PDF p.123-124) footnote: "The interest paid during the year includes
₹18.57 Lakhs (Previous year ₹4.53 Lakhs) in respect of interest costs capitalised for the property, plant
and equipment in accordance with Ind AS 23." This means ₹0.19cr of FY26 borrowing cost sits inside PP&E
additions (Note 3) rather than in Note 25 Finance Costs (₹1.66cr as reported) — legitimate under Ind AS 23
for qualifying assets under construction, and immaterial in size (≈11% of total finance costs), but it is
a genuine new fact: reported finance costs slightly understate total borrowing cost incurred, and reported
capex is slightly inflated by the capitalised interest. 🟢 Clean — sized correctly, just not previously
named.

## NF6. Total equity/book value barely grew despite a strong profit year — quantifies Pass 1's payout-ratio point from the balance-sheet side 🟡

Note 33.1 (Capital Management, PDF p.117): Total Equity ₹168.58cr (Mar-2026) vs ₹166.24cr (Mar-2025), an
increase of just ₹2.34cr (+1.4%) despite FY26 PAT of ₹28.77cr. Pass 1 computed the 89.7% payout ratio from
the income-statement side; this is the balance-sheet confirmation — nearly the entire year's profit left
the company as dividend, book value per share effectively stood still. Consistent with, and reinforces,
Pass 1's dividend/payout finding; not a new number, but a new angle worth carrying forward, especially
alongside NF10 below (this is the FIRST dividend the company has ever paid). 🟡 Watch (capital-allocation
context, not a red flag on its own).

## NF7. Company's own ratio table refines, and partly explains, Pass 1's receivable/inventory-days narrative 🟡

Note 33.2's own ratio table (PDF p.117-118), not examined in this depth by Pass 1:
- **Trade Receivables turnover**: 7.94x (Mar-26) vs 7.45x (Mar-25), i.e. ≈46 days vs ≈49 days on an
  average-receivables basis — still improving, as Pass 1 found, but a smaller improvement than Pass 1's
  simplified revenue/closing-balance calculation (52 to 44 days) suggested. The direction is unchanged;
  the magnitude is more modest on the company's own (average-balance) method.
- **Net capital turnover ratio** (credit sales / working capital): rose 3.99x to 4.49x (+12.6%) in the SAME
  year inventory ballooned 76.7%. This only makes sense if net working capital itself did not grow much —
  confirmed by the **Current Ratio falling** 1.95 to 1.84 (−5.6%) in Note 33.2. Read together with Pass
  1's Rank 8 finding (MSME trade payables nearly doubling), this closes the loop quantitatively: the
  inventory build was funded largely through the current-liabilities side (MSME and other trade payables),
  not primarily through cash/mutual-fund drawdown, which is why working-capital-based ratios did not
  deteriorate as sharply as the raw inventory or CFO numbers alone would imply.
- **Debt Service Coverage Ratio** fell 7.67x to 5.83x (−24.0%), company's stated reason "attributable to
  repayment of loan during the year" — the Zoroastrian machinery loan's amortisation began Jan-2026
  (Note 13), raising the current-year debt-service denominator even as total debt outstanding fell.
🟡 Watch — none of this changes Pass 1's directional conclusions, but it adds the quantitative mechanism
Pass 1 asserted without fully showing.

## NF8. A possible cross-note inconsistency on the FY25 doubtful-receivables provision — flagged, not asserted 🟡

Note 5's ECL movement table shows FY25 "Impairment losses recognised on receivables" = ₹15.79 lakh
(₹0.158cr). Note 27 (Other Expenses, P&L line items) shows a separate "Provision for doubtful trade
receivables" line with a value only in the FY26 column (₹18.57 lakh) and no value shown for FY25 — i.e.
the P&L expense breakdown does not carry a matching FY25 provision line for the amount Note 5 says was
recognised that year. Separately, the Cash Flow Statement's own "Provision for doubtful Trade Receivable"
add-back for FY26 is ₹13.98 lakh — different from both Note 5's ₹18.58 lakh and Note 27's ₹18.57 lakh for
the same year. The within-FY26 Note 5/Note 27 gap (18.58 vs 18.57) is immaterial rounding; the FY26
cash-flow figure (13.98, a ₹4.6 lakh gap from the other two) and the FY25 Note 27 omission are the two
points worth a management question. A plausible explanation for both: the cash-flow line nets the gross
impairment recognised against amounts already captured in the separately-listed "Trade receivables written
off" add-back line, and FY25's provision may simply have sat inside "Miscellaneous expenses" in Note 27
rather than being broken out as its own line that year. **NOT FOUND IN DOCUMENT: a reconciliation between
these three figures.** 🟡 Watch — a disclosure-consistency question, not confirmed as an error.

## NF9. Gratuity current-provision footnote — minor granularity, does not change the rating 🟢

Of the ₹28.79 lakh current gratuity provision (Note 15B), a footnote to Note 31C states ₹28.52 lakh
relates to already-exited ("left") staff awaiting payment, and only ₹0.27 lakh is the live actuarial net
liability for continuing employees — matching the ₹0.27 lakh "Net Liability/(Asset) recognised in the
Balance Sheet" figure in Note 31C exactly. This confirms Pass 1's "near fully funded" read at a finer
level of detail; no rating change. 🟢

## NF10. FY26 is the company's first-ever dividend — not stated as such by Pass 1 🟡

The Statement of Changes in Equity (PDF p.71) shows "Payment of dividends on equity shares" only in the
FY26 column; the FY25 column carries no dividend line at all (opening retained earnings ₹124.80cr at
1-Apr-2024, i.e. FY24's closing balance, rolls forward with no distribution until FY26). Given the company
was incorporated 30-Aug-2022 and listed 11-Jun-2024, the ₹25.80cr interim dividend (89.7% payout, Note 11)
declared for FY26 is its FIRST dividend ever. Pass 1 discussed the payout ratio and the promoter cash flow
but did not flag the "maiden dividend" framing. Worth naming: the company chose to inaugurate dividend
payments, at a near-90% payout ratio, in the same year inventory built ₹24.5cr and CFO nearly halved — a
capital-allocation choice made in a year of rising working-capital stress, funded in part by drawing down
the mutual-fund book (Note 4B, down 47.2%, as Pass 1 already noted) rather than operating cash flow alone.
🟡 Watch — capital-allocation context for the operator, not an accounting-quality flag.

═══════════════════════════════════════════════════════════════
PASS 2 NEW FINDINGS SUMMARY
═══════════════════════════════════════════════════════════════

| # | New finding | Note # | Rating | Why it matters beyond Pass 1 |
|---|---|---|---|---|
| NF1 | Note 36 (Offsetting) not covered by Pass 1: true gross receivables fell 3.4% but the rebate/discount liability netted against them grew 41.6% | Note 36 (PDF p.125) | 🟡 | Qualifies the "receivables improving" read; part of the optics is a bigger customer-rebate accrual |
| NF2 | Pledged-asset collateral fell 74.9% (₹115.12cr to ₹28.91cr), far larger than the debt-equity ratio alone conveyed; sharpens materiality of the unfiled RoC charge-satisfaction gap Pass 1 already flagged | Note 37 (PDF p.125) | 🟡 | Balance-sheet quality point Pass 1 under-quantified |
| NF3 | Pass 1's "8.6% underlying employee-cost growth ex-Labour-Codes" does not check out; correct figure is ~1.2%; Note 31 shows active members fell 14.8% while average pay roughly doubled, unexplained | Note 24; Note 31 Section I (PDF p.113) | 🟡 | Arithmetic correction to Pass 1 Rank 3, plus a new workforce-mix disclosure directly relevant to the transition thesis |
| NF4 | AUD unhedged vendor-advance exposure was ₹12.99cr (5.6% of revenue) at Mar-2025, falling to ₹3.19cr at Mar-2026 — a specific, sizeable single-currency concentration | Note 33.8(a)-(b) (PDF p.121-122) | 🟡 | More concrete than Pass 1's general "unhedged FX" comment; points to an Australia sourcing/capex link |
| NF5 | ₹18.57 lakh of FY26 borrowing cost was capitalised into PP&E under Ind AS 23 (4.1x the FY25 figure), not expensed through Finance Costs | Note 35 footnote (PDF p.123-124) | 🟢 | Small, legitimate, but not previously named; finance costs and capex are each slightly affected |
| NF6 | Total equity grew only ₹2.34cr (+1.4%) despite ₹28.77cr PAT — the balance-sheet mirror of Pass 1's 89.7% payout finding | Note 33.1 (PDF p.117) | 🟡 | Quantifies capital retention (or lack of it) directly |
| NF7 | Company's own ratio table: receivable-day improvement is smaller on an average-balance basis (49→46 days) than Pass 1's point-in-time calc (52→44); net capital turnover rose because current liabilities absorbed the inventory build, confirmed by the current ratio falling 1.95→1.84 | Note 33.2 (PDF p.117-118) | 🟡 | Shows the mechanism behind Pass 1's inventory/payables findings quantitatively |
| NF8 | FY25 doubtful-receivables provision shows inconsistent figures across Note 5 (₹15.79 lakh), Note 27 (nil shown), and no clean tie to the FY26 cash-flow add-back (₹13.98 lakh vs Note 5/27's ₹18.57-18.58 lakh) | Note 5; Note 27; Cash Flow Statement | 🟡 | Cross-note reconciliation gap Pass 1 did not test; flagged as a question, not an error |
| NF9 | Of the ₹28.79 lakh current gratuity provision, ₹28.52 lakh is for already-exited staff; only ₹0.27 lakh is the live net liability | Note 31C footnote (PDF p.112) | 🟢 | Minor granularity, confirms Pass 1's "near fully funded" read, no rating change |
| NF10 | FY26's ₹25.80cr interim dividend is the company's first-ever dividend (no FY25 distribution in the Statement of Changes in Equity) | Statement of Changes in Equity (PDF p.71); Note 11 | 🟡 | Frames the 89.7% payout as a maiden capital-allocation decision made in a year of rising working-capital stress |

No going-concern language was found on this second read either (Note 33.1's "ensure it will be able to
continue as going concern" is standard capital-management boilerplate, not an emphasis of matter or
qualification) — Pass 1's "NONE" finding stands confirmed, not contradicted.

═══════════════════════════════════════════════════════════════
END OF PASS 2
═══════════════════════════════════════════════════════════════
