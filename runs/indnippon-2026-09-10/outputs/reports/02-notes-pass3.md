# STAGE 2 PASS 3: PATTERN PASS + CONSOLIDATION
Company: INDNIPPON (India Nippon Electricals Ltd) | Run date: 2026-09-10
Source: Pass 1 (runs/indnippon-2026-09-10/outputs/reports/02-notes-pass1.md), Pass 2
(runs/indnippon-2026-09-10/outputs/reports/02-notes-pass2.md), both re-checked against
runs/indnippon-2026-09-10/extracted/annual-report__Annual_Report_2026.txt (FY26 AR) and
...__Annual_Report_2025.txt (FY25 AR) for this pass's own verification.
All amounts in Rs Lakhs unless converted to Rs Crores (Cr); Lakhs source figure given first.

---

## PATTERN PASS (Note 1 to last note, contradiction/consistency lens)

Passes 1 and 2 already surfaced the note set's main cross-note contradictions (receivables
turnover ratio vs ageing table; three different credit-term statements; the two-line export
gap; the Note 13/cash-flow Rs 134 Lakh gap; the Note 48(i) new-text-in-the-deterioration-year
coincidence). This pass re-ran the four pattern-specific checks the instructions name that had
not yet been independently confirmed:

- **Going concern language.** Grep of the full FY26 AR text for "going concern" returns nine
  hits, all boilerplate: management's responsibility statement ("...using the going concern
  basis of accounting..."), the auditor's responsibility paragraph (both standalone, p.~172 PDF,
  and consolidated, p.~253 PDF, near-identical wording: "...We conclude that a material
  uncertainty exists... may cast significant doubt on the [Company's/Group's] ability to
  continue as a going concern"), and the CARO-adjacent risk-factor list. No paragraph states a
  material uncertainty EXISTS; the "may cast doubt" language is the standard SA 570 template
  sentence every auditor's report carries, not a triggered disclosure. NONE, confirmed.
- **Numbers vs primary statements, spot-check beyond what Pass 2 already reconciled.** Note 8
  investment total (Rs 53,153 Lakhs) ties to the Balance Sheet non-current + current investment
  lines (p.183 PDF); Note 13 receivables (Rs 20,646 Lakhs) ties to the Balance Sheet exactly
  (confirmed in Pass 2); Note 18 share capital (Rs 1,131 Lakhs) ties to the Balance Sheet.
  No new primary-statement mismatch found beyond the Rs 134 Lakh receivables/cash-flow gap
  Pass 2 already bounded.
- **Prior-year restatements/reclassifications.** No note anywhere uses the words "restated" or
  "regrouped" for a P&L or Balance Sheet line (searched both ARs). The only prior-year note
  renumbering is mechanical (FY25 AR's Note 27 becomes FY26 AR's Note 28, a one-note shift from
  the subsidiary-related notes moving position after PT Automotive's winding-up) — a structural
  renumbering, not a restatement of figures. NONE found.
- **Events after balance sheet date.** Confirmed again: no note titled "Subsequent Events" or
  equivalent exists in either note set; Note 52/equivalent is a Board-approval confirmation, not
  a subsequent-events disclosure. The Note 38 exceptional item was recognized and cash-realized
  WITHIN FY26 (Feb-2026), before the 31-Mar-2026 year end, so it is not a subsequent event either.
  NOT FOUND IN DOCUMENT as a distinct disclosure category.
- **Deliberately thin disclosure by comparison.** The one genuine asymmetry this pass adds to
  Pass 1/2's list: contingent liabilities (Note 45) gives only aggregate amounts by tax type with
  no case-by-case narrative (Pass 1 flagged this), while the Lucas TVS valuation (Note 47) gets a
  full technique-and-sensitivity paragraph and the exceptional item (Note 38) gets a full
  litigation-history narrative. The company clearly CAN write detailed narrative disclosure when
  it chooses to; the tax-dispute note is thin by choice or by immateriality (Rs 16.23 Cr, 1.98%
  of net worth), not by incapacity. 🟡 Watch, low materiality given the size.

PASS 3 pattern re-read confirms no new material finding beyond what Passes 1-2 already carry
forward into this consolidation. The remainder of this report is the required consolidation and
the explicit adjudication of the six items the run brief named.

---

## ADJUDICATION OF THE SIX FLAGGED ITEMS

### 1. The zero-ECL question (highest materiality)

**Both readings are legitimate; here is the one observation that separates them.**

Defensible-position reading: Note 48(i) (p.232-233 PDF) states the debtor base is "four to five
major OEMs," and BRSR Q19(c) (p.129 PDF) names three of them outright: TVS Motor, Hero MotoCorp,
Bajaj Auto — investment-grade, large-balance-sheet counterparties with, per the company,
"negligible defaults" and a "strong collection track record." Deloitte's sole standalone Key
Audit Matter is the Lucas TVS valuation, NOT receivables/ECL (Independent Auditor's Report,
p.172-173 PDF) — an external, independent signal the statutory auditor did not treat the
zero-ECL call as the year's top audit-risk item. OEM receivables move in bulk payment cycles, so
a jump concentrated in the near-term bucket is consistent with normal OEM payment-cycle timing,
not necessarily credit deterioration.

Red-flag reading: the near-term-overdue bucket rose 152.4% (Rs 1,699 to Rs 4,290 Lakhs, Note 13c,
p.208-209 PDF) against 26.5% revenue growth. Pulling the FY24 comparative from the FY25 AR, the
three-year overdue-share trend is 15.3% (FY24) -> 11.1% (FY25) -> 22.3% (FY26, Note 13c both ARs)
— FY26 is the worst year of three, not a rebound from an unusually clean FY25. And the specific
defensive paragraph now used to justify zero ECL ("negligible defaults," "strong collection track
record," "concentration is considered low") is confirmed, by direct text search, to be ENTIRELY
ABSENT from the FY25 AR's equivalent Note 46(i) (p.233 PDF, FY25 AR) — new text, added in the
exact year the ageing table deteriorated most.

**The one observation that separates the two readings, and where it would appear:** whether the
Rs 4,290 Lakh near-term-overdue bucket is concentrated in the two large-OEM accounts (consistent
with normal bulk payment-cycle timing, the benign reading) or is broad-based across the smaller
customer tail (consistent with a genuine credit-quality shift, the red-flag reading). Note 13c
gives no debtor-level or size-band split within the ageing table — only aggregate buckets by
time, not by counterparty. This single cut is not disclosed anywhere in the Notes and is the
one fact that would resolve the question. **Final read: this is a genuine accounting-quality
watch item, not yet a confirmed red flag.** The company's own default definition (90 days
past due, policy 2.16(d), p.199 PDF) means part of the "less than 6 months" bucket is not yet
"in default" under its own policy, which tempers the 152% headline without closing the question.
Rated 🟡 Watch, sharpened toward 🔴: the coincidence of new defensive disclosure text arriving in
the exact deterioration year is the fact that moves this from routine to worth a direct
management question (Question 1 below).

### 2. The Lucas TVS valuation (highest materiality)

**What IS disclosed:** the holding is 97,351 equity shares, face value Rs 100, unchanged both
years (Note 8A, p.204-205 PDF); FVTOCI, Level 3, valued by Comparable Companies Method,
EV/EBITDA multiple (Note 47(f)-(g), p.228-229 PDF, confirmed by direct read at line 15327-15334
of the extracted FY26 AR text); the multiple is 8x in FY26 (same as FY25), was 9x at FY24 and cut
to 8x for FY25 (FY25 AR's own Note 47-equivalent, p.232 PDF FY25 AR) — a genuine downward
revision, not a frozen input; sensitivity is explicit and precise: "A decrease in the multiple by
0.5x would result in a decrease in the fair value by Rs 1,651 Lakhs and an increase in the
multiple by 0.5x would result in an increase in the fair value by Rs 1,651 Lakhs" (Note 47(g),
verbatim). Extrapolating linearly, a full 1x change in the multiple moves fair value by
approximately Rs 3,302 Lakhs (Rs 33.02 Cr), which is 0.40% of FY26 net worth (Rs 821.33 Cr) per
1.0x of multiple change — material at the position level, small at the whole-balance-sheet level.
Fair value: Rs 19,037 Lakhs (FY24) -> Rs 22,468 Lakhs (FY25, +18.0%) -> Rs 26,412 Lakhs (FY26,
+17.6%); Deloitte's sole standalone and consolidated Key Audit Matter for FY26 is this valuation,
with disclosed audit response including "engaging our fair valuation expert" and a "look back
analysis" against past actuals (Independent Auditor's Report, p.172-173 PDF).

**What is NOT disclosed anywhere in this document:** India Nippon's percentage ownership of Lucas
TVS Limited's total issued share capital (only the absolute share count is given, with no
denominator); Lucas TVS's own EBITDA; Lucas TVS's own net debt or cash position; any named
comparable-company set used in the CCM; the identity of the external fair-valuation expert. Since
value rose in all three years shown, including the year the multiple was CUT (FY25: value +18.0%
while the multiple fell 9x to 8x), the entire three-year gain of +38.7% cumulative is
mathematically attributable to the undisclosed EBITDA/net-debt bridge input, never to multiple
expansion — and that bridge input is completely opaque in this document. 🔴 Red Flag on
disclosure gap specifically (not on misstatement; nothing here suggests the valuation is wrong,
only that it cannot be independently checked from this AR).

**Scale and earnings-quality consequence, stated plainly:** the Lucas TVS stake alone is Rs 264.12
Cr, 32.2% of FY26 net worth (Rs 821.33 Cr) and 49.70% of the total Rs 531.53 Cr investment book.
Per accounting policy 2.16(i)(b) (p.195 PDF) and confirmed in Note 19's Other Equity roll-forward,
FVTOCI equity gains "do not recycle to profit or loss, even on sale of investment" — the Rs 3,944
Lakh gross FY26 revaluation gain sits permanently in the OCI reserve (closing balance Rs 18,318
Lakhs, Note 19) and will NEVER appear in reported P&L or EPS, this year, in any future year, or
even on an eventual sale of the stake. The practical consequence: book value (and any
price-to-book-based read of this stock) is materially inflated by a third-party asset whose gains
are real economic value creation but structurally invisible to earnings-based valuation metrics
(P/E, ROE-on-reported-earnings). An investor relying on reported EPS or P&L-based ROE will
systematically understate the shareholder value this holding has created, while an investor
relying on book value / net worth will be carrying a third of that book in an asset whose
underlying economic drivers (EBITDA, net debt, ownership %) this AR does not let them verify.

### 3. The concentration-versus-related-party reconciliation

**Final reconciliation:** the Ind AS 24 perimeter in Note 42 (p.222-224 PDF) reads as CORRECTLY
DRAWN. BRSR Q19(c) (p.129 PDF) names the major customers directly: TVS Motor Company, Hero
MotoCorp, Bajaj Auto — a three-OEM group. Hero MotoCorp and Bajaj Auto have no ownership,
control, or significant-influence link to India Nippon's promoter chain (Lucas Indian Service
Ltd, 70.32%-70.37% holding shareholder / SB TVS Industrial Ventures Pvt Ltd, ultimate holding
company); they are correctly excluded from Note 42. TVS Motor Company is also correctly excluded:
though it shares the "TVS" name and general commercial ecosystem with Lucas TVS Limited (which
IS a Note 42 related party, "enterprise over which KMP exercise significant influence") and with
Lucas Indian Service Ltd (the direct 70%+ promoter), TVS Motor Company itself is not shown to be
under common control, joint control, or significant influence with India Nippon under Ind AS 24's
tests — it is a separate, independently listed group entity, and the AR gives no ownership chain
connecting TVS Motor Company to India Nippon's promoter structure. **Technically correct: yes.**

**Economically informative: only partially.** The Rs 754.91 Cr / 70.66% two-customer
concentration (Note 28e, p.217-218 PDF) is drawn from a pool of two OEMs out of the three BRSR
names, but Note 28e's Ind AS 108 anonymisation means the Notes alone cannot say which two of the
three cross 10% individually, or confirm whether one of the two is TVS Motor at all. That
identification only becomes possible by reading Note 28e alongside BRSR Q19(c) and the front-matter
"Our Journey" history and Founder's Day disclosures (p.15, p.41 PDF) — none of which are formally
cross-referenced to Note 28e or Note 42 within the financial statements themselves. A reader
relying on the Notes in isolation, without the BRSR, cannot reconstruct that the dominant revenue
counterparties are large, named, investment-grade 2W OEMs rather than an undisclosed related
entity. The technical correctness of the Ind AS 24 line is not in question; the CROSS-REFERENCING
between the concentration note and the customer-naming disclosure is the gap, and it is a
disclosure-navigation gap, not a perimeter-drawing error.

### 4. The residual Rs 134 Lakh receivables gap

Recorded as an OPEN QUESTION FOR MANAGEMENT, not resolved. Pass 2 anchored both source figures
precisely: Note 13's balance-sheet movement is Rs 3,681 Lakhs (Rs 20,646 - Rs 16,965 Lakhs,
tying exactly to the Balance Sheet, p.183 PDF); the Cash Flow Statement's working-capital line is
Rs 3,547 Lakhs ("Decrease/(increase) in trade receivables (3,547)," p.185-186 PDF standalone,
identical in the consolidated Cash Flow Statement p.247-248 PDF). The Rs 134 Lakh (Rs 1.34 Cr)
residual does not match any candidate line searched: no bad-debt write-off exists in Note 37
(Other Expenses); the Rs 118 Lakh unrealized-forex line in the cash flow statement is close in
magnitude but relates to all monetary items, not trade receivables specifically, and does not tie
exactly; no other-asset reclassification absorbs it. This is small (0.65% of the Note 13
receivables balance) and does not change the substance of the cash-conversion read, but this
report does not guess at the missing reconciling item. NOT FOUND IN DOCUMENT.

### 5. The technical-knowhow intangible

Rs 477 Lakhs (Rs 4.77 Cr) added in FY25 and the identical Rs 477 Lakhs appears as "Charge for the
year" in that same FY25 column of Note 6A's roll-forward (p.202-203 PDF) — a 100% first-year
write-off against a stated 5-year useful life (policy 2.5, p.191-192 PDF). This is a FY25 P&L
event (confirmed by the roll-forward dates), so it does not depress FY26 earnings directly, but it
is the primary driver of Note 36's FY25-to-FY26 amortization decline (Rs 531 Lakhs to Rs 42
Lakhs, a Rs 489 Lakh / 92% drop, of which Rs 477 Lakhs is this single item). Earnings effect,
quantified: the full Rs 477 Lakh charge landed in FY25's P&L in one year instead of being spread
over 5 years (which would have been roughly Rs 95 Lakhs/year); FY25 pre-tax profit therefore
absorbed an approximately Rs 382 Lakh (Rs 3.82 Cr) higher one-time charge than a straight-line
policy would have produced, and FY26 by the same token carries roughly Rs 95 Lakhs LESS
amortization expense than a straight-line spread would show — inflating the YoY "amortization
decline" as an apparent efficiency gain when it is a base-year policy anomaly unwinding. No note
anywhere explains why a stated 5-year-life asset got a 100% first-year charge. **Rating: 🔴 Red
Flag** — a direct, unexplained policy-versus-practice contradiction on a capitalized asset, the
kind of inconsistency that, unexplained, should make a reader question whether other
capitalization/amortization decisions in the accounts follow the stated policies as written.

### 6. The Rs 38 Lakh export inconsistency

Confirmed as an uncorrected carry-forward, not a one-off transcription slip: the FY25 AR's OWN
current-year note (its Note 27, p.218 PDF FY25 AR) already shows the identical Rs 38 Lakh gap for
FY25's own figures ("Export sales" Rs 3,363 Lakhs vs "Rest of the world" Rs 3,325 Lakhs), and this
carries unchanged into the FY26 AR's FY25 comparative column. The FY24 figures tie exactly both
ways (Rs 3,578 Lakhs = Rs 3,578 Lakhs, FY25 AR). **Rated for what it says about disclosure
control, separate from its size:** the amount itself (Rs 0.38 Cr, immaterial to both the revenue
base and the ~160% export-growth headline either way it is computed) is not the point. The point
is that the same internal inconsistency between two sub-disclosures of the identical note (28a
product-type vs 28d geography) survived TWO successive statutory audits and TWO board-approved
annual reports without correction or explanation. This is a 🟡 Watch on disclosure-control
process quality (does the company's note-preparation process cross-check its own sub-schedules
before filing), explicitly NOT a valuation or earnings-quality concern, and explicitly NOT
evidence of anything larger — it is presented here as a small, persistent process signal, nothing
more.

---

## CONSOLIDATED NOTES ANALYSIS, ALL THREE PASSES COMBINED

### A. TOP 15 MOST SIGNIFICANT FINDINGS RANKED BY INVESTOR IMPORTANCE

| Rank | Finding | Note # | Rating | Why it matters |
|---|---|---|---|---|
| 1 | Lucas TVS Ltd equity stake Rs 264.12 Cr = 32.2% of net worth, 49.70% of the investment book, Level-3/CCM-EV/EBITDA valued; INEL's % ownership of Lucas TVS, and Lucas TVS's own EBITDA/net debt, are disclosed NOWHERE in this document even though these are the sole drivers of 3 straight years of fair-value gains; gains permanently trapped in OCI, never touch EPS | Note 8A, 42.3, 47 (p.204-207, 223, 228-229 PDF) | 🔴 Red Flag (disclosure gap) | Nearly a third of book value is unverifiable from this AR; central to any SOTP/book-value work and to earnings-quality framing (see Item 2 above) |
| 2 | Trade receivables near-term-overdue bucket up 152.4% (Rs 16.99 Cr to Rs 42.90 Cr) against 26.5% revenue growth; FY26 is the worst of 3 years shown (15.3% -> 11.1% -> 22.3% overdue share); zero ECL recognised; the specific defensive zero-ECL narrative is NEW text added in this exact deterioration year, absent from the FY25 AR | Note 13, 48(i) (p.208-209, 232-233 PDF); FY25 AR Note 46(i) (p.233 PDF) | 🟡 Watch, sharpened toward 🔴 | Direct cash-conversion guard (LB1); the ageing table does not disclose the OEM-vs-tail split that would resolve whether this is benign payment-cycle timing or genuine credit deterioration (see Item 1 above) |
| 3 | Technical knowhow Rs 4.77 Cr added and 100% amortized within the same FY25 year, against a stated 5-year useful-life policy; no explanation given; ~Rs 3.82 Cr excess FY25 charge, ~Rs 0.95 Cr/yr understated FY26-forward amortization vs straight-line | Note 6A, 2.5, 36 (p.202-203, 191-192, 219-220 PDF) | 🔴 Red Flag | Unexplained policy-vs-practice contradiction on a capitalized asset; raises a direct question on whether other capitalization decisions follow stated policy |
| 4 | The two >10% customers (Rs 754.91 Cr, 70.66% of FY26 revenue) sit outside the Note 42 related-party perimeter; the perimeter itself reads as CORRECTLY drawn once BRSR Q19(c) names TVS Motor, Hero MotoCorp, and Bajaj Auto, but no cross-reference exists between Note 28e and the BRSR naming, so a Notes-only reader cannot make this connection | Note 28e, 42; BRSR Q19(c) (p.217-218, 222-224, 129 PDF) | 🟡 Watch | Concentration risk on a named-but-not-cross-referenced counterparty group; resolved as technically correct, navigation gap remains (see Item 3 above) |
| 5 | Cash and bank balances fell 64.8% (Rs 15.62 Cr to Rs 5.50 Cr) in a year of rising dividend (Rs 35.06 Cr vs Rs 28.28 Cr), rising capex commitments (Rs 26.35 Cr vs Rs 3.67 Cr), and Rs 55.01 Cr of investment purchases, against a zero-borrowing balance sheet | Note 14, 45, 48 (p.209-210, 227, 232 PDF) | 🟡 Watch | Liquidity-mix shift, not distress (no debt); cash cushion now thin relative to business scale, compounds LB1 |
| 6 | Inventory provisioning coverage thinned from 11.1% to 9.4% of gross inventory even as raw-material inventory surged 40.8% (vs 26.5% revenue growth); finished goods fell 9.2% (no channel-stuffing signal) | Note 12 (p.208 PDF) | 🟡 Watch | Part of the LB1 cash-conversion picture; raw-material build direction (pre-buy vs early obsolescence risk) not distinguishable from the Notes |
| 7 | Exceptional item Rs 15.21 Cr (10.4% of FY26 pre-tax profit) is a one-off 16-year-old Gurugram land-compensation settlement, cash-realized Feb-2026; company's own Note 51 footnote flags ROE/ROCE/Net Profit ratios as "includes exceptional item" | Note 38, 51 (p.221-222, 234 PDF) | 🟢 Clean | Verified exactly against the brief; strip for any run-rate profitability read |
| 8 | Rs 134 Lakh (Rs 1.34 Cr) gap between Note 13's receivables movement (Rs 36.81 Cr) and the Cash Flow Statement's working-capital line (Rs 35.47 Cr) is precisely bounded but the reconciling item is NOT FOUND anywhere in the document | Note 13 / Balance Sheet p.183 PDF vs Cash Flow Statement p.185-186 PDF | 🟡 Watch | Small (0.65% of the receivables balance), does not change LB1's substance, but genuinely unresolved — open question for management |
| 9 | Rs 38 Lakh export-figure gap (Export sales vs Rest-of-world geography, same note) carried uncorrected across two successive annual reports (FY25 AR and FY26 AR both show it for FY25's own figures); FY24 tied exactly | Note 28 (p.217-218 PDF); FY25 AR Note 27 (p.218 PDF) | 🟡 Watch | Immaterial in amount; a genuine disclosure-control-process signal, not a valuation concern |
| 10 | Deloitte's sole standalone/consolidated Key Audit Matter for FY26 is the Lucas TVS fair valuation; NO KAM raised on receivables/ECL — an independent external signal on where the auditor placed the year's top judgment risk | Independent Auditor's Report, KAM section (p.172-173 PDF) | 🟢 Clean (context) | Cuts against the strongest form of the zero-ECL red flag, without resolving the underlying disclosure gap on Lucas TVS |
| 11 | Same-population receivable credit terms stated three different ways: 60-90 days (policy 2.3), 45-60 days (Note 13a), 45-90 days (Note 48) | Note 2.3, 13, 48 (p.190, 208, 233 PDF) | 🟡 Watch | Internal disclosure inconsistency; small but genuine, worth a housekeeping question |
| 12 | Receivables turnover ratio (5.7, average-balance basis) improved even as the year-end ageing snapshot worsened; mechanically explained as a measurement-basis effect (average vs point-in-time), not a data error, but the point-in-time ageing is the more decision-relevant of the two for cash-conversion purposes | Note 13, 51 (p.208-209, 233-234 PDF) | 🟡 Watch (methodology resolved; substance remains) | Prevents a reader from being falsely reassured by the summary ratio alone |
| 13 | Foreign-currency receivable exposure (Rs 28.07 Cr, up from Rs 16.57 Cr) is fully unhedged; "the Company has not entered into any derivative contracts to hedge its foreign currency exposure" — explicit no-hedging statement, tracking the +162% export growth | Note 48(ii) (p.233 PDF) | 🟡 Watch | Small in absolute PBT-sensitivity terms today (0.65% of PBT for a 5% USD move) but growing with export mix; monitor as exports scale |
| 14 | Warranty provision closing balance nearly doubled YoY (Rs 78 Lakhs to Rs 141 Lakhs, +80.8%), additions outpacing utilizations for a second year, with no specific litigation-driven spike disclosed | Note 21, 25 (p.213, 216 PDF) | 🟡 Watch | Reads as routine scale-driven growth but the acceleration rate (well above 26.5% revenue growth) merits a management question |
| 15 | Management's MD&A/BRSR Risk Factors claim the Company has "progressively reduced its dependency on key customers over the years," in tension with Note 28e showing two-customer concentration still above 70% of revenue and growing 21.1% in absolute rupees YoY | MD&A Risk Factors (p.126 PDF) vs Note 28e (p.217-218 PDF) | 🟡 Watch | Narrative-versus-data tension; not proof of misstatement, but a direct question for management on what multi-year trend supports the "progressively reduced" claim |

### B. ACCOUNTING QUALITY SCORE (1-10)

| Dimension | Score | Basis |
|---|---|---|
| Revenue recognition conservatism | 7/10 | Standard Ind AS 115 point-in-time policy, no aggressive language, no policy change; one immaterial catch-up subsidy item (Rs 2.02 Cr, correctly disclosed as such); the uncorrected Rs 38 Lakh export-note gap is a process ding, not a recognition-policy concern |
| Expense capitalisation honesty | 5/10 | Technical-knowhow Rs 4.77 Cr fully written off in the year of addition against a stated 5-year life, unexplained (Finding 3); no capitalisation threshold disclosed anywhere; otherwise depreciation lives are standard/conservative (Schedule II ranges) |
| Provisioning adequacy | 4/10 | Zero ECL against a 3-year-worst ageing deterioration with no debtor-level split to independently test the benign reading (Finding 2); inventory provision coverage thinned from 11.1% to 9.4% against a 40.8% raw-material build; gratuity/warranty provisioning itself is routine and adequately disclosed |
| RPT fairness | 6/10 | Ind AS 24 perimeter reads as correctly drawn (Finding 4); no non-arm's-length pricing signal is flagged by the company or evidenced in the Notes; but the multi-directional Lucas TVS relationship (customer-adjacent, landlord, raw-material supplier, management-fee recipient, AND the Rs 264.12 Cr investee) concentrates a lot of related-party surface area in one counterparty group without an arm's-length pricing confirmation for any of it |
| Disclosure transparency | 6/10 | Strong on some fronts (explicit KAM disclosure, explicit sensitivity math on Lucas TVS, explicit MSME/warranty/CSR detail); weak on others (Lucas TVS ownership %/EBITDA/net debt not disclosed, NBFC deposit counterparty not named, capitalisation threshold not disclosed, three-way credit-term inconsistency, no cross-reference between Note 28e concentration and BRSR customer naming) |
| Consistency with prior years | 6/10 | Policies stable YoY, no restatements found; but the zero-ECL defensive paragraph is genuinely new text arriving in the deterioration year (Finding 1), and the export-note gap has now persisted, uncorrected, across two ARs |
| **OVERALL** | **6/10** | Moderate. The balance sheet mechanics (zero debt, clean MSME payables, clean CSR, no ESOP dilution, no restatements, no going-concern language) are genuinely clean. The two dimensions that matter most for a cash-conversion and valuation read — provisioning adequacy and the disclosure depth behind a third-of-net-worth related-party investment — are the dimensions dragging the score down, and both are HIGH-materiality, not peripheral, items |

### C. KEY RISKS FROM NOTES

| Risk | Severity | What to monitor | When it could hit |
|---|---|---|---|
| Zero-ECL position unwinds if OEM payment terms genuinely stretch | Medium-High | Next AR's ageing table (Note 13c) near-term-overdue bucket; whether it continues past 2 years of deterioration into a 3rd | FY27 AR (filed ~mid-2027) |
| Lucas TVS fair value driven by an undisclosed EBITDA/net-debt bridge that cannot be independently checked | Medium (disclosure risk), Low-Medium (valuation risk given auditor KAM testing) | Any Lucas TVS-specific disclosure (its own financials if ever obtained via other channels); the multiple's stability at 8x; whether the sensitivity band (±Rs 16.51 Cr per 0.5x) is ever breached by a bigger single-year move | Each AR's Note 47 refresh |
| Technical-knowhow-style capitalization-vs-amortization inconsistency recurs on a future intangible addition | Low-Medium | Note 6A roll-forward in future ARs for any new intangible addition fully charged in-year against a longer stated life | Whenever a new intangible is capitalized |
| Cash cushion (now Rs 5.50 Cr) thins further if dividend + capex + investment purchases continue to outpace CFO | Medium | Note 14 cash balance trend; capital commitments (Note 45b) vs actual CFO in the next AR | FY27 AR |
| Unhedged FX receivable exposure (Rs 28.07 Cr) grows with export mix (+162% FY26) with no hedging policy in place | Low today, rising | Note 48(ii) unhedged exposure and the export revenue share in future ARs | Scales with export growth, watch FY27-FY28 |
| Two-customer concentration (70.66% of revenue) sits outside the RPT perimeter with no independently verifiable arm's-length pricing confirmation | Medium | Note 28e concentration trend; any BRSR/MD&A commentary on pricing or contract renewal terms | Ongoing, structural to the business model |

### D. FIVE QUESTIONS FOR MANAGEMENT

1. What share of the Rs 42.90 Cr near-term-overdue receivables bucket sits with the two >10%
   OEM customers versus the smaller customer tail, and is the increase concentrated in a payment-
   cycle timing shift by one or two large accounts rather than broad-based credit deterioration?
   (Note 13c, 28e)
2. What is India Nippon's percentage ownership of Lucas TVS Limited's total issued share
   capital, and what were Lucas TVS's own EBITDA and net debt/cash position in each of the last
   three fiscal years, that the Comparable Companies Method valuation (Note 47) relies on?
   (Note 8A, 47)
3. Why was the Rs 4.77 Cr technical-knowhow intangible added and 100% amortized in the same
   financial year, against the stated 5-year useful-life policy, and does this treatment apply
   to any other capitalized intangible in the current or prior periods? (Note 6A, policy 2.5)
4. What is the reconciling item behind the Rs 1.34 Cr gap between Note 13's balance-sheet
   receivables movement and the Cash Flow Statement's trade-receivables working-capital line?
   (Note 13, Cash Flow Statement)
5. What multi-year data supports the MD&A/BRSR Risk Factors claim of having "progressively
   reduced dependency on key customers," given the two-customer concentration was 70.66% of FY26
   revenue and grew 21.1% in absolute rupees year over year? (MD&A Risk Factors p.126 PDF,
   Note 28e)

### E. NOTES-BASED RED FLAGS

- **Earnings management signal:** none found rising to the level of earnings management. The
  Rs 15.21 Cr exceptional item is transparently labelled non-recurring, and the company's own
  Note 51 footnote flags the ratios it inflates.
- **Aggressive accounting signal:** the technical-knowhow full write-off against a stated 5-year
  life (Finding 3) is the closest thing to an aggressive/inconsistent accounting choice found in
  the Notes, though its direction (accelerating an expense, not deferring one) is conservative
  for FY25 earnings and only becomes a flag through the unexplained policy-vs-practice gap and
  its effect on the FY26 YoY amortization comparison.
- **Undisclosed risk indicators:** the Lucas TVS EBITDA/net-debt/ownership-percentage opacity
  (Finding 1) is the clearest undisclosed-risk-indicator item: a valuation input worth 32.2% of
  net worth cannot be independently tested from this document. The zero-ECL position against a
  worsening ageing table, absent a debtor-level split, is the second.

### F. ONE-LINE NOTES VERDICT

The notes reveal moderate accounting practices, clean on debt, payables, and CSR mechanics but
carrying two genuine disclosure gaps at the highest-materiality items in the balance sheet. Key
concern: a third of net worth sits in a related-party, Level-3 investment (Lucas TVS, Rs 264.12
Cr) whose entire three-year value driver is an undisclosed EBITDA/net-debt bridge, alongside a
zero-ECL conclusion against the worst receivables ageing in three years with no debtor-level
split to test it. Key strength: zero borrowings, clean MSME payables with no delayed-interest
history, no restatements, no going-concern language, and a transparently labelled, correctly
excluded one-off exceptional item. Overall accounting quality: 6/10.

---

```yaml
stage: B02-notes
company: "INDNIPPON"
run_date: "2026-09-10"
model: claude-sonnet-5
status: complete
input_gaps:
  - "shareholding-pattern filing absent (promoter pledge trend UNRESOLVED; FY26 AR carries no pledge/encumbrance disclosure)"
  - "no concalls (company holds none)"
  - "no rating (debt free, no rated facilities)"
  - "screener Profit_Loss/Balance_Sheet/Cash_Flow/Quarters CSVs are header-only templates; only Data_Sheet.csv carries data"
flags:
  - {type: FLAG-CASH, reason: "Trade receivables near-term-overdue bucket up 152.4% (Rs 16.99 Cr to Rs 42.90 Cr, Note 13c) against 26.5% revenue growth; overdue share worst of 3 years (15.3% FY24 -> 11.1% FY25 -> 22.3% FY26); zero ECL recognised (Note 13, 48(i)); no debtor-level split disclosed to test benign-vs-adverse reading; cash balance fell 64.8% (Note 14) in the same year"}
accounting_quality: 6
pass_2_empty: false
pass_3_empty: true
top_findings:
  - {rank: 1, finding: "Lucas TVS Ltd stake Rs 264.12 Cr = 32.2% of net worth, 49.70% of investment book, Level-3/CCM-EV/EBITDA valued; INEL's % ownership of Lucas TVS and Lucas TVS's own EBITDA/net debt are disclosed nowhere despite driving all 3 years of fair-value gains; gains permanently trapped in OCI, never touch EPS", note_ref: "Note 8A, 42.3, 47 (p.204-207, 223, 228-229 PDF)", rating: "RED FLAG (disclosure gap)"}
  - {rank: 2, finding: "Trade receivables near-term-overdue bucket up 152.4% against 26.5% revenue growth; FY26 worst of 3 years (15.3%->11.1%->22.3% overdue share); zero ECL recognised; the specific zero-ECL defensive narrative is NEW text added in this exact deterioration year, absent from the FY25 AR", note_ref: "Note 13, 48(i) (p.208-209, 232-233 PDF); FY25 AR Note 46(i) (p.233 PDF)", rating: "WATCH, sharpened toward RED"}
  - {rank: 3, finding: "Technical knowhow Rs 4.77 Cr added and 100% amortized within the same FY25 year against a stated 5-year useful-life policy, unexplained; drives 92% of the FY25-to-FY26 amortization decline", note_ref: "Note 6A, 2.5, 36 (p.202-203, 191-192, 219-220 PDF)", rating: "RED FLAG"}
  - {rank: 4, finding: "Two >10% customers (Rs 754.91 Cr, 70.66% of FY26 revenue) sit outside the Note 42 related-party perimeter; perimeter reads as correctly drawn once BRSR Q19(c) names TVS Motor, Hero MotoCorp, Bajaj Auto, but no cross-reference exists between Note 28e and the BRSR naming", note_ref: "Note 28e, 42; BRSR Q19(c) (p.217-218, 222-224, 129 PDF)", rating: "WATCH"}
  - {rank: 5, finding: "Cash and bank balances fell 64.8% (Rs 15.62 Cr to Rs 5.50 Cr) in a year of rising dividend, rising capex commitments, and Rs 55.01 Cr of investment purchases, against a zero-borrowing balance sheet", note_ref: "Note 14, 45, 48 (p.209-210, 227, 232 PDF)", rating: "WATCH"}
  - {rank: 6, finding: "Inventory provisioning coverage thinned 11.1% to 9.4% of gross inventory even as raw-material inventory surged 40.8% vs 26.5% revenue growth; finished goods fell 9.2% (no channel-stuffing signal)", note_ref: "Note 12 (p.208 PDF)", rating: "WATCH"}
  - {rank: 7, finding: "Exceptional item Rs 15.21 Cr (10.4% of FY26 pre-tax profit), a one-off Gurugram land-compensation settlement, cash-realized Feb-2026; company's own Note 51 footnote flags ROE/ROCE/Net Profit as including it", note_ref: "Note 38, 51 (p.221-222, 234 PDF)", rating: "CLEAN"}
  - {rank: 8, finding: "Rs 1.34 Cr gap between Note 13's receivables movement and the Cash Flow Statement's working-capital line is precisely bounded but the reconciling item is NOT FOUND in the document", note_ref: "Note 13 / Balance Sheet p.183 PDF vs Cash Flow Statement p.185-186 PDF", rating: "WATCH"}
  - {rank: 9, finding: "Rs 38 Lakh export-figure gap (Export sales vs Rest-of-world geography) carried uncorrected across two successive annual reports for FY25's own figures; FY24 tied exactly", note_ref: "Note 28 (p.217-218 PDF); FY25 AR Note 27 (p.218 PDF)", rating: "WATCH"}
  - {rank: 10, finding: "Deloitte's sole standalone/consolidated Key Audit Matter for FY26 is the Lucas TVS fair valuation; no KAM raised on receivables/ECL, an independent external signal on the auditor's top judgment-risk placement", note_ref: "Independent Auditor's Report, KAM section (p.172-173 PDF)", rating: "CLEAN (context)"}
  - {rank: 11, finding: "Same-population receivable credit terms stated three different ways: 60-90 days (policy 2.3), 45-60 days (Note 13a), 45-90 days (Note 48)", note_ref: "Note 2.3, 13, 48 (p.190, 208, 233 PDF)", rating: "WATCH"}
  - {rank: 12, finding: "Receivables turnover ratio improved (average-balance basis) even as the year-end ageing snapshot worsened; a measurement-basis effect, not a data error, but the point-in-time ageing is the more decision-relevant read", note_ref: "Note 13, 51 (p.208-209, 233-234 PDF)", rating: "WATCH"}
  - {rank: 13, finding: "Foreign-currency receivable exposure (Rs 28.07 Cr, up from Rs 16.57 Cr) is fully unhedged, tracking +162% export growth; explicit no-hedging statement", note_ref: "Note 48(ii) (p.233 PDF)", rating: "WATCH"}
  - {rank: 14, finding: "Warranty provision closing balance nearly doubled YoY (Rs 78 to Rs 141 Lakhs, +80.8%), additions outpacing utilizations for a second year, no specific litigation-driven spike disclosed", note_ref: "Note 21, 25 (p.213, 216 PDF)", rating: "WATCH"}
  - {rank: 15, finding: "MD&A/BRSR claim of 'progressively reduced dependency on key customers' sits in tension with Note 28e showing two-customer concentration still above 70% of revenue and growing 21.1% in absolute rupees YoY", note_ref: "MD&A Risk Factors p.126 PDF vs Note 28e (p.217-218 PDF)", rating: "WATCH"}
red_flags:
  - "Zero-ECL conclusion (Note 13, 48(i)) against a receivables ageing table showing the worst overdue share in 3 years (22.3% FY26 vs 11.1% FY25 vs 15.3% FY24), with a newly-added defensive justification paragraph appearing in the exact deterioration year and absent from the FY25 AR; no debtor-level split disclosed to independently test whether the deterioration is benign OEM payment-cycle timing or genuine credit-quality change"
  - "Lucas TVS Limited valuation opacity: 32.2% of net worth (Rs 264.12 Cr) sits in a Level-3, related-party, CCM/EV-EBITDA-valued holding; India Nippon's % ownership of Lucas TVS, and Lucas TVS's own EBITDA and net debt, are disclosed nowhere in the document, even though these (not the multiple, which was cut 9x to 8x) are the sole drivers of 3 straight years of fair-value gains that are permanently trapped in OCI and never reach reported EPS"
  - "Technical knowhow Rs 4.77 Cr added and 100% amortized within the same FY25 year against a stated 5-year useful-life policy, with no explanation given anywhere in the notes"
questions_for_mgmt:
  - "What share of the Rs 42.90 Cr near-term-overdue receivables sits with the two >10% OEM customers versus the smaller customer tail, and is the increase a payment-cycle timing effect or broad-based credit deterioration? (Note 13c, 28e)"
  - "What is India Nippon's percentage ownership of Lucas TVS Limited, and what were Lucas TVS's own EBITDA and net debt/cash in each of the last 3 fiscal years underlying the Note 47 valuation? (Note 8A, 47)"
  - "Why was the Rs 4.77 Cr technical-knowhow intangible added and fully amortized in the same year against the stated 5-year policy, and does this treatment apply to any other capitalized intangible? (Note 6A, policy 2.5)"
  - "What is the reconciling item behind the Rs 1.34 Cr gap between Note 13's receivables movement and the Cash Flow Statement's trade-receivables line? (Note 13, Cash Flow Statement)"
  - "What multi-year data supports the MD&A/BRSR claim of 'progressively reduced dependency on key customers,' given two-customer concentration was 70.66% of FY26 revenue and grew 21.1% in absolute rupees YoY? (MD&A p.126 PDF, Note 28e)"
receivables_trend: "deteriorating. Overdue-of-any-age share: 15.3% FY24 -> 11.1% FY25 -> 22.3% FY26 (Note 13c, FY25 AR p.211 PDF and FY26 AR p.208-209 PDF). Near-term-overdue bucket (less than 6 months) up 152.4%, Rs 16.99 Cr to Rs 42.90 Cr, against 26.5% revenue growth. Zero ECL recognised in both years (Note 13, 48). Not-yet-due share fell from 88.9% to 77.7% of the book."
restatements_found: []
going_concern_language: "NONE. Standard SA 570 boilerplate only (management's and auditor's responsibility paragraphs, both standalone p.~172 PDF and consolidated p.~253 PDF); no material uncertainty is stated to exist."
analyst_note: "The two highest-materiality items both resolve to disclosure gaps, not confirmed misstatements: the zero-ECL call is plausible given the named OEM debtor base and the absent auditor KAM, but the ageing table's own worst-of-3-years trend and the newly-added defensive paragraph keep it a live watch item; the Lucas TVS valuation is Deloitte's sole KAM and has been externally tested, but this AR alone cannot verify the EBITDA/net-debt bridge driving 100% of 3 years of gains on 32.2% of net worth. Both require the BRSR/MD&A and, ideally, Lucas TVS's own filings to close. The technical-knowhow write-off is the one item that reads as a genuine unexplained policy-practice inconsistency rather than a disclosure-depth question, and is rated accordingly."
```
