# STAGE 2 - NOTES TO FINANCIAL STATEMENTS - PASS 2 (WHAT WAS MISSED)
Company: Balu Forge Industries Ltd (BALUFORGE) | Run date: 2026-09-06
Source: Annual Report FY2025 (primary, PDF 216pp) and Annual Report FY2024 (prior year, PDF 232pp)

SCOPE NOTE: Pass 1 read the Notes to the Standalone and Consolidated Financial Statements end to end and
found no material new items on a straight note-by-note re-read (confirmed below, note by note). Per the
orchestrator's task instruction for this pass, the second sweep was widened to the areas Pass 1 explicitly
excluded but that the notes cross-reference constantly: the Independent Auditor's Report (Key Audit Matters,
opinion, Emphasis of Matter check), the CARO 2020 Annexure A (both years, standalone and consolidated), the
Deferred Tax note (never opened in Pass 1), the Income Tax rate-reconciliation arithmetic (re-verified line by
line), the Compensated Absences policy against the Provisions note, and the BRSR/ESG Annexure. This is where
the material new findings sit. All figures in Rs Lakhs unless stated. Page anchors are PDF page numbers per
the [[PAGE n]] markers in the source text extraction.

NOTE ON CORPUS GAP (carried from Stage 0): FY2026 AR not yet filed; items needing it are marked [NEEDS FY26 AR].

---

## NOTE-BY-NOTE RE-READ CONFIRMATION (Notes 1-50 standalone, 1-48 consolidated)

Re-read confirms Pass 1's coverage was complete and accurate for the Notes proper: policies (Notes 1-5), PPE/
CWIP (6/8), ROU (7), intangibles/goodwill (9), investments in subsidiaries (10), other assets (11-13/20),
inventory (14), trade receivables (15), cash (16-17), loans (18-19), equity (21-22), borrowings (23/25),
provisions (24/29), trade payables (26), other liabilities (27-28), revenue (30), other income (31), changes
in inventories (32), employee benefits (33), D&A/finance costs/other expenses (34-36), income tax (37), EPS
(39), R&D (40), segment (41), CSR (43), financial instruments (44), gratuity (45), contingent liabilities (46),
related parties (47), additional regulatory info (48), closing notes (49-50). No new item on straight re-read
of these tables and narratives beyond what is below. The genuinely new findings come from (a) notes Pass 1
under-mined for sub-detail (Deferred Tax, the tax rate-reconciliation arithmetic, the Compensated Absences
policy cross-reference), and (b) the Auditor's Report / CARO Annexure / BRSR, which the parent task directed
this pass to open.

---

## 1. CARO 2020 ANNEXURE A - CLAUSE 3(ii)(b): STOCK STATEMENT VS BOOKS DISCREPANCIES (NEW)

Standalone Auditor's Report, Annexure A, p.107 (FY2025 AR); comparable table in FY2024 AR, Annexure A, p.122.

The auditor discloses a table of differences between amounts per books and amounts reported to Union Bank of
India in quarterly stock/book-debt statements (a CARO-mandated disclosure when working capital is secured
against current assets):

| Quarter | Item | Books (Lk) | Reported to bank (Lk) | Difference (Lk) |
|---|---|---|---|---|
| Jun-24 | Trade Receivables up to 90 days | 10,727.90 | 9,787.57 | (940.34) |
| Sep-24 | Trade Receivables up to 90 days | 9,797.18 | 8,817.46 | (979.72) |
| Dec-24 | Trade Receivables up to 90 days | 13,385.26 | 13,363.85 | (21.40) |
| Mar-25 | Trade Receivables up to 90 days | 8,503.65 | 8,581.24 | 77.60 |

Inventory differences the same four quarters are trivial (Rs 1.29 Lk, Rs 0.12 Lk, Rs 0.00 Lk, Rs (0.00) Lk) -
the discrepancy is confined to the receivables line. The FY2024 AR's equivalent table (p.122) shows the same
pattern one year earlier and smaller in absolute terms: Jun-23 N.A., Sep-23 (142.52), Dec-23 (315.22),
Mar-24 351.52. 🟡 This is a two-year recurring pattern, not a one-off: receivables reported to the company's
secured lender diverge from the books by amounts that are material in absolute terms (up to Rs 9.8 Cr in
Sep-24) and have grown YoY as the receivables book has grown.

Cross-reference: Note 25 (Borrowings, current, standalone p.135, and Note 24 consol p.183) contains the
boilerplate line "the quarterly returns or statements of current assets filed by the company with banks...
generally are in agreement with the books of accounts with minor difference on account of provisional
figures." 🟡 Watch: this characterization ("minor difference") sits uneasily next to the auditor's own
disclosed table, where the Sep-24 gap alone is roughly 10% of the reported receivables base for that return.
The note's own materiality language and the CARO table's own numbers are in tension. [Note 25 p.135 vs
Annexure A p.107, standalone FY2025 AR]

## 2. RECEIVABLES/BILLS DISCOUNTING WITH BANKS - NO RECOURSE DISCLOSURE, NOT IN BORROWINGS NOTE (NEW)

Note 15 (standalone, p.129) and Note 14 (consolidated, p.177):

| | FY25 (Lk) | FY24 (Lk) |
|---|---|---|
| Total Trade Receivables (before discounting) | 33,203.65 | 24,617.38 |
| Less: Bills discounted with banks | (6,478.20) | (5,559.16) |
| Net Trade Receivables carried | 26,725.45 | 19,058.22 |

Rs 64.78 Cr of receivables (FY25) are discounted with banks and netted straight off the Trade Receivables
line. 🔴 Three things do not add up around this:
- The word "recourse" (or "non-recourse", "without recourse", "with recourse") appears NOWHERE in either
  year's annual report. Whether the company retains credit risk on these discounted bills (in which case Ind
  AS 109 would generally require them to stay ON balance sheet as a secured borrowing, not be derecognized) is
  simply never addressed.
- This Rs 64.78 Cr facility is NOT listed anywhere in the Borrowings note (Note 23/25 standalone, Note 22/24
  consol). Total disclosed borrowings (long + short + current maturities) are only Rs 3,591.25 Lk - i.e. the
  receivables-discounting quantum alone (Rs 6,478.20 Lk) is roughly 1.8x the company's entire disclosed formal
  debt. The Debt-Equity ratio of 0.04 (Note 48(l)) and the "gearing ratio -" / net-cash positioning (Note
  44(b)(4)) do not reflect this financing channel at all, whichever way it should properly be classified.
  [Note 15 p.129 + Note 25 p.135 standalone; Note 14 p.177 + Note 24 p.183 consol]
- The associated cost line, "Discounting & LC Charges" (inside Finance Costs, Note 34 standalone p.137 / Note
  33 consol p.186), FELL from Rs 445.04 Lk (FY24) to Rs 377.83 Lk (FY25), a 15.1% decline, even as the
  discounted-bills balance GREW 16.5% (Rs 5,559.16 Lk -> Rs 6,478.20 Lk). Falling discount rates across the
  banking system could explain this, but the notes offer no explanation, and the divergence runs the opposite
  direction from what the growing balance would suggest.
This is a financial-instruments/risk-management disclosure gap the "pay special attention" instruction for
this pass specifically calls out, and it also plausibly bears on Finding 1 above (bank stock-statement
mismatches on the receivables line, not inventory) - a discounting arrangement whose treatment or timing
differs between the two records is a natural candidate explanation, though the notes never draw the
connection either. [NEEDS FY26 AR / claude.ai live verification: is this discounting facility with recourse,
and is it disclosed anywhere as a distinct credit line with its own limit?]

## 3. DEFERRED TAX NOTE - INDEPENDENT CORROBORATION OF THE ECL REVERSAL (NEW - note never opened in Pass 1)

Note 12 (standalone, p.128) and Note 11 (consolidated, p.177), deferred tax asset rollforward:

| Component | FY24 closing (Lk) | Recognised/(reversed) through P&L (Lk) | FY25 closing (Lk) |
|---|---|---|---|
| Property, plant and equipment | (56.51) | (77.90) | (134.41) |
| Provisions for employee benefits | 27.40 | 10.10 | 35.91 |
| Lease liabilities | 0.08 | 6.01 | 6.09 |
| Impairment of Financial Assets | 406.65 | (145.10) | 261.55 |
| Total | 377.62 | (206.89) | 169.14 |

Identical in both standalone and consolidated notes. 🔴 The "Impairment of Financial Assets" line is the
deferred tax asset the company carries against its ECL provision on trade receivables. It fell Rs 145.10 Lk
through the P&L in FY25 - the tax-effected mirror of the same gross ECL reversal Pass 1 flagged as its #1 red
flag (Rs 576.48 Lk standalone / Rs 479.88 Lk consol P&L credit, Note 36/35). This is not a new fact in
substance, but it is a second, independent note (Deferred Tax) corroborating the same underlying event from a
different angle, and it was not examined at all in Pass 1. It strengthens rather than adds to the existing
red flag; recorded here for completeness and cross-reference. [Note 12 p.128 standalone, Note 11 p.177 consol]

## 4. INCOME TAX RATE RECONCILIATION - DISCLOSURE REGRESSION VS FY2024 AR (NEW)

Note 37 (standalone, p.138) and Note 36 (consolidated, p.186-187), FY2025 AR:

Standalone: Total tax expense per the first table (Current Tax 4,348.56 + Deferred tax 210.07 + Prior-year
true-up 450.09) = Rs 5,008.72 Lk. But the rate-reconciliation table two lines below it reads:
"Profit before tax 18,431.69 x 25% = 4,639.26; less deductible/non-deductible adjustment (290.70); Income tax
expense for the year 4,348.56." 🔴 The reconciliation's bottom line (4,348.56) equals ONLY the Current Tax
component - it silently excludes the Rs 660.16 Lk of deferred tax and prior-year adjustment from the bridge.
Confirmed against the P&L: PBT 18,431.69 less TOTAL tax expense 5,008.72 = Net profit 13,422.97 (matches Note
22 Other Equity exactly) - i.e. the P&L actually bears Rs 5,008.72 Lk of tax, not the Rs 4,348.56 Lk the
reconciliation table implies. True standalone effective tax rate FY25 = 27.17% (5,008.72/18,431.69), not the
~23.6% a reader would compute from the reconciliation table alone.

The consolidated Note 36 (p.186-187) repeats the identical structure: "Profit before tax 25,394.26 x 25.17% =
6,391.74; less effect of different tax rate of subsidiaries (1,752.48); less deductible/non-deductible
adjustment (290.70); Income tax expense in the consolidated statement of profit and loss 4,348.56" - again
only the current-tax figure, again omitting the Rs 660.16 Lk deferred-tax/prior-year component (which, per
Finding 3 above and the standalone note, is a wholly domestic-entity item, not a subsidiary effect).

🔴 Cross-year comparison confirms this is a REGRESSION, not a stable format: the FY2024 AR's standalone Note
37 (p.155) bridges PBT-at-statutory-rate all the way through to the TOTAL tax expense (Rs 2,017.46 Lk, which
DOES match the FY24 P&L tax charge) and closes with an explicit line: "Effective income tax rate 23.10%." The
FY2025 AR drops this "Effective income tax rate" disclosure line entirely in both the standalone and
consolidated notes, and narrows the reconciliation's scope to current tax only, without any statement that the
presentation changed. An investor who reads only the widely-used rate-reconciliation table (rather than
cross-footing it against the total-tax rollforward two lines above) would materially understate the group's
true effective tax burden and would have no way to see that deferred tax and prior-year true-ups now sit
outside the bridge. This compounds Pass 1's #2 red flag (the low-tax offshore subsidiary mix) with a second,
independent transparency problem in the same note family. [Note 37 p.138 standalone FY25 AR vs Note 37 p.155
FY24 AR; Note 36 p.186-187 consol FY25 AR]

## 5. AUDITOR'S KEY AUDIT MATTERS, OPINION, AND CARO SUMMARY (NEW - report not read in Pass 1)

Standalone Independent Auditor's Report, p.101-103, names three Key Audit Matters:
- KAM 1: CWIP and capital expenditure funded through preferential capital (Note 5.3/8). Auditor's stated
  conclusion: "the Company's accounting for CWIP and utilization of preferential capital proceeds were
  reasonable and disclosures were appropriate." 🟢 This is an independent mitigant to Pass 1's Finding 7
  (CWIP capex-execution watch item) - the auditor specifically tested budget-vs-actual, impairment
  indicators, and use-of-proceeds reconciliation, and found no issue.
- KAM 2: Trade Receivables and Recoverability (Note 15), explicitly citing ECL judgment, ageing, probability
  of default and loss given default as the audit focus. 🟡 The auditor's own selection of this as a KAM
  independently corroborates that the ECL/ageing area (Pass 1's #1 red flag) was recognised by the audit team
  as high-judgment; the KAM disclosure does not resolve the concern (there is no stated quantitative
  conclusion, unlike KAM 1), it only confirms it was scrutinised.
- KAM 3: Revenue recognition (point-in-time, export delivery terms) - standard, no incremental finding.
No Emphasis of Matter paragraph, no qualified/adverse/disclaimer opinion, no material uncertainty related to
going concern anywhere in the standalone or consolidated auditor's reports (both p.100-167 range). 🟢
Consolidated auditor's report (p.157) states explicitly: "there are no qualifications or adverse remarks" in
the CARO reports issued for the company and its Indian subsidiaries. [Independent Auditor's Report, standalone
p.101-103, consolidated p.157]

## 6. CARO 3(vii)(a): PROFESSION TAX ARREARS ACROSS THREE CONSECUTIVE YEARS (NEW)

Annexure A, standalone, p.107: undisputed statutory dues outstanding more than 6 months, all marked "Not
Paid" as of the 14-May-2025 audit report date:

| Statute | Nature | Amount (Rs) | Due date | Status |
|---|---|---|---|---|
| Profession Tax | Employees | 38,750 | 30-Jun-2022 | Not Paid |
| Profession Tax | Employees | 47,300 | 30-Jun-2023 | Not Paid |
| Profession Tax | Employees | 43,500 | 30-Jun-2024 | Not Paid |

🟡 Trivial in Rupee terms (~Rs 1.3 Lk total) but a persistent, unremediated compliance lapse spanning three
consecutive statutory years, still open as of the audit sign-off date. Worth a direct question given it costs
nothing to fix and has not been fixed.

## 7. GOVERNANCE - INDEPENDENT DIRECTOR RESIGNATION TIED TO THE COMPANY'S OWN LENDER (NEW, outside Notes scope)

Directors' Report, p.30 (out of strict Notes-to-Accounts scope, flagged because it connects directly to
Finding 1 above): Mr. Sumer Singh was appointed an Additional Independent Director on 6-Sep-2024 and resigned
19 days later, on 25-Sep-2024, because he could not obtain a No-Objection Certificate from his employer, Union
Bank of India, where he serves as Deputy General Manager. Union Bank of India is the company's own secured
working-capital lender (packing credit facility, hypothecation of stock and book debts, Note 25 p.135) - the
same bank named in the CARO stock-statement discrepancy table (Finding 1). A bank-employee independent
director candidate withdrawing within three weeks for want of employer clearance, at the company's own lender,
is a governance data point worth carrying forward even though it sits in the Board Report rather than the
Notes. 🟡

## 8. COMPENSATED ABSENCES POLICY VS PROVISIONS NOTE - CROSS-REFERENCE GAP (NEW)

Accounting policy Note 5.12.3 (standalone p.122-123, consolidated p.167): "Liabilities recognised in respect
of other long-term employee benefits such as annual leave and sick leave are measured at present value...
using the projected unit credit method with actuarial valuation... Compensated absences which are not expected
to occur within twelve months... are recognised based on actuarial valuation." This is a firm policy
commitment to carry an actuarially-valued leave liability. Yet the Provisions note (Note 24 standalone p.134,
Note 23 consolidated p.183) discloses ONLY a gratuity provision in both years - no compensated-absences or
leave-encashment liability line appears anywhere in either year's balance sheet notes, and no actuarial
assumptions for compensated absences appear in the Employee Benefits note (Note 45/43), which covers gratuity
only. 🟡 Either the company's leave policy is genuinely non-accumulating (so no liability is due and the
policy paragraph is standard boilerplate not actually triggered), or a liability exists and is simply not
separately disclosed. "NOT FOUND IN DOCUMENT" which of the two is true - worth a direct management question,
raised here because Pass 1 read the policy note and the Provisions note separately without cross-checking them
against each other.

## 9. BRSR / ESG ANNEXURE (Annexure II, p.69-90) - UNASSURED, SCANNED FOR MATERIAL ITEMS (NEW)

- Assurance: "Name of assurance provider: Not Applicable; Type of assurance obtained: Not Applicable" (p.69).
  The entire BRSR is self-reported with zero external assurance. 🟡 (context for everything below)
- Safety (p.83): Lost Time Injury Frequency Rate, total recordable work-related injuries, and fatalities are
  all reported as "Nil" for BOTH employees and workers, in BOTH FY2024-25 and FY2023-24, at a heavy forging
  and machining operation. 🟡 A two-year clean safety record for this industry type is plausible but notably
  clean and entirely unverified by any external assurance provider; no corroborating detail (near-miss counts,
  audit frequency results) is quantified beyond the qualitative narrative.
- Employee/worker attrition (p.71) IMPROVED across three years: Permanent Employees 6% (FY23) -> 5% (FY24) ->
  3% (FY25); Permanent Workers 9% (FY23) -> 10% (FY24) -> 6% (FY25). 🟢 A genuinely constructive, internally
  consistent trend for a scaling manufacturer; no red flag, noted for completeness.
- POSH/sexual harassment complaints: Nil both years (p.89). No whistleblower complaints received (also
  confirmed in the standalone Directors' Report). 🟢 Clean, consistent with the CARO auditor statement (no
  fraud noticed, no whistleblower complaints).
No other BRSR item (water, emissions, energy) surfaced anything an equity investor would weight materially
for this thesis; not reproduced here to avoid manufacturing significance in routine ESG boilerplate.

## 10. MINOR: TRIVIAL FY24-COMPARATIVE MISMATCH BETWEEN STANDALONE AND CONSOLIDATED DEFERRED TAX (NEW)

The FY24 comparative figure for "Deferred tax liabilities (Net)" in the Income Tax note reads Rs (167.67) Lk in
the standalone Note 37 (p.138) but Rs (168.17) Lk in the consolidated Note 36 (p.186) for what should be the
identical FY2024 domestic-entity figure - a Rs 0.50 Lk difference. Immaterial in amount, but it is another
instance of the "same fact, different number across notes/documents" pattern Pass 1 already flagged at far
larger scale (the Safa Otomotiv trade receivable cross-AR mismatch, and the consolidated Finished Goods
opening/closing gap). Recorded here as a small additional data point for the pattern, not as a standalone
concern. [Note 37 p.138 standalone vs Note 36 p.186 consol, FY2025 AR]

## 11. SAFA OTOMOTIV LOAN-Dr BALANCE MOVEMENT NOT EXPLAINED BY DISCLOSED TRANSACTIONS (NEW)

Note 47, standalone, p.149: the Safa Otomotiv FZ-LLC "Loan-Dr" outstanding balance grew from Rs 665.00 Lk
(FY24) to Rs 738.92 Lk (FY25), a Rs 73.92 Lk increase. But the same table's transaction lines show "Loan
Given" and "Loan Repaid by parties" to Safa Otomotiv as blank/nil for FY25 (versus Rs 763.42 Lk given and Rs
202.35 Lk repaid in FY24) - i.e. no new loan was advanced and none was repaid in FY25 per the disclosed
transaction lines, yet the outstanding balance still rose by Rs 73.92 Lk. 🟡 Interest income of Rs 55.87 Lk
was separately shown as "Interest Received" (implying cash receipt, which should not add to the Dr balance),
so the increase is not obviously interest capitalisation; FX retranslation of an AED-denominated balance is
the most plausible explanation but is never stated. This sits alongside the two already-flagged static
balances in the same relationship (Trade Receivable-Dr and Machinery Advance, both unchanged Rs 1,301.27 Lk
and Rs 2,695.39 Lk for two straight years, Pass 1 Finding 3) as a further sign that the Safa Otomotiv
related-party balance reconciliation process may not be fully tight. [Note 47 p.149, standalone FY2025 AR]

---

# PASS 2 NEW FINDINGS SUMMARY

Eleven new items surfaced on the widened second sweep (Auditor's Report, CARO Annexure, Deferred Tax note,
tax-reconciliation arithmetic, policy-vs-provisions cross-check, BRSR). The straight note-by-note re-read of
Notes 1-50/1-48 themselves confirmed Pass 1's coverage was complete; no new items emerged there. Ranked by
investor importance:

1. (🔴) Receivables/bills discounting with banks (Rs 64.78 Cr FY25) netted off Trade Receivables, no
   recourse/non-recourse disclosure anywhere in the document, and not reflected in the Borrowings note despite
   exceeding total disclosed borrowings by ~1.8x - a real gap in leverage and receivables-quality visibility.
2. (🔴) Income tax rate-reconciliation tables (standalone and consolidated) bridge only to CURRENT tax, not
   total tax expense, silently dropping Rs 660.16 Lk of deferred tax/prior-year adjustment from the bridge and
   dropping the "Effective income tax rate" disclosure line that was present in the FY2024 AR - a genuine
   disclosure regression compounding Pass 1's existing tax-transparency red flag.
3. (🔴) CARO Annexure A: two-year recurring, growing pattern of Trade-Receivables-up-to-90-days discrepancies
   between books and quarterly returns filed with Union Bank of India (up to Rs 9.8 Cr in Sep-24), while the
   Borrowings note characterizes these as merely "minor... provisional" - a materiality-language mismatch.
4. (🟡) Auditor's Key Audit Matters independently corroborate the CWIP (mitigating - auditor found it
   reasonable) and Trade Receivables/ECL (reinforcing - auditor flagged it as high-judgment) areas; no
   qualified opinion, no Emphasis of Matter, no going-concern paragraph in either report.
5. (🟡) Deferred tax asset rollforward (never opened in Pass 1) independently corroborates the gross ECL
   reversal already flagged as Pass 1's #1 red flag.
6. (🟡) Independent Director candidate resigned 19 days after appointment for want of an NOC from his employer,
   Union Bank of India - the company's own working-capital lender (Board Report, connects to Finding 3).
7. (🟡) Compensated-absences accounting policy commits to an actuarially-valued leave liability that never
   appears in either year's Provisions note - unresolved whether leave is genuinely non-accumulating or simply
   undisclosed.
8. (🟡) CARO: Profession Tax arrears unremediated across three consecutive statutory years (trivial amount).
9. (🟡) BRSR is entirely unassured; reports a clean two-year safety record (Nil LTIFR/injuries/fatalities) at
   a heavy forging operation with no external verification.
10. (🟢/minor) Trivial Rs 0.50 Lk standalone-vs-consolidated mismatch in the FY24-comparative deferred tax
    figure - adds one more small data point to the "same fact, different number" pattern.
11. (🟡) Safa Otomotiv Loan-Dr balance rose Rs 73.92 Lk in FY25 with no corresponding "Loan Given"/"Loan
    Repaid" transaction disclosed - a further unreconciled movement in the same related-party relationship
    already flagged for its static Trade Receivable and Machinery Advance balances.

END OF PASS 2.
