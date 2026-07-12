# STAGE 2 — NOTES TO FINANCIAL STATEMENTS — PASS 2 (WHAT WAS MISSED)
Company: Prizor Viztech Limited (PRIZOR) | FY 2024-25 Annual Report (8th AR)
Run date: 2026-07-12 | Source: runs/prizor-2026-07-12/inputs/_textcache/Annual_Report_2025.txt,
cross-checked against runs/prizor-2026-07-12/inputs/annual-report/Annual_Report_2025.pdf (p.89 visual,
Note 32 Ratio Analysis, for table-parsing accuracy)

Re-read Notes 1 through 54 (both note sets) against the Pass 1 extraction. Pass 1 was thorough;
this pass surfaces items that were skipped, under-extracted, or that only emerge from cross-checking
Note 3/4 (share capital/reserves) against Note 31 (RPT) and the Cash Flow Statement. One correction
to a Pass 1 figure is also made below (Note 4 bonus-issue debit unit error).

═══════════════════════════════════════════════════════════════
NEW FINDING 1 — UNIT/DECIMAL ERROR IN PASS 1, NOTE 4 (Reserves & Surplus, p.79)
═══════════════════════════════════════════════════════════════
Pass 1 stated the bonus-issue debit against Reserve & Surplus was "₹0.40 Cr / 40,000.03 thousand."
This is incorrect by a factor of 10. Applying the stage's own conversion rule (÷10,000 on the
thousands figure): 40,000.03 / 10,000 = ₹4.000003 Cr, not ₹0.40 Cr.

Verification via full reconciliation (Note 4, p.79):
- R&S: Opening 58,682.01 + P&L transfer 1,01,526.31 − Bonus Issue 40,000.03 = Closing 1,20,208.29
  (all in thousands) — the arithmetic only closes if the bonus debit is 40,000.03 thousand
  (₹4.00 Cr), confirming the Pass 1 figure was a mis-transcription.
- Cross-check against Note 3(i) bonus share count: 66,00,003 bonus shares × Rs 10 face value =
  Rs 6,60,00,030 = ₹6.600003 Cr required capitalisation.
- Sources: R&S debit ₹4.000003 Cr + Security Premium debit ₹2.60 Cr (26,000.00 thousand, Note 4)
  = ₹6.600003 Cr — matches the bonus share face-value requirement exactly.
🟢 Clean (corrected) — the bonus issue was fully funded from free reserves and securities premium,
with zero revaluation reserve involved (Note 38, p.91 confirms no PPE revaluation), which is Section
63 Companies Act 2013 compliant. The accounting entries themselves remain correctly classified as
Pass 1 concluded; only the ₹0.40 Cr figure needs correcting to ₹4.00 Cr in any downstream synthesis
that cites this line.

═══════════════════════════════════════════════════════════════
NEW FINDING 2 — ₹3.00 CR LOAN-TO-EQUITY CONVERSION DOES NOT RECONCILE TO ANY NAMED LENDER
═══════════════════════════════════════════════════════════════
Note 3(i) Share Capital reconciliation (p.79): 4,00,000 equity shares issued at Rs 75/share
(Rs 10 face + Rs 65 premium) = ₹3.00 Cr, "by way of Conversion of Loans into equity," per
shareholder resolution dated 07-May-2024. Corroborated by the Cash Flow Statement, "Proceeds from
conversion of loan to Share Capital ₹30,000.00 thousand" (p.73), and by the Directors' Report
Capital Structure section (p.29-30), which repeats the same mechanics but does not name the lender.

Cross-check against Note 31 (RPT, p.87-88): the ONLY loans disclosed anywhere in the notes are the
two director unsecured loans. Their balance moved from a combined FY24 close of ₹3.9026 Cr
(Dasharathbharthi ₹2.7576 Cr + Mitali ₹1.1450 Cr) to a combined FY25 close of ₹1.6720 Cr
(₹1.2065 Cr + ₹0.4655 Cr) — a reduction of ₹2.2306 Cr. This reduction is fully and exactly
explained by the disclosed cash transactions in Note 31(ii): Loan Repaid to Directors
(₹2.5751 Cr + ₹0.9157 Cr = ₹3.4908 Cr) minus Loan Received from Directors (₹1.0240 Cr +
₹0.2362 Cr = ₹1.2602 Cr) = ₹2.2306 Cr net cash repayment — leaving zero unexplained residual and
therefore zero room for any equity-conversion component within the director loan account. No other
borrowing note (Note 5, Note 8) shows a corresponding ₹3.00 Cr reduction attributable to a
conversion either. Note 31(i) lists "Prizor Snacks Private Limited" as a related party (Group
Company) but this entity appears in NO transaction or balance line in either year's table, in
either the standalone or consolidated note set.
🔴 Red Flag — the identity of the party whose ₹3.00 Cr loan was converted into equity nine days
before a 5.5:1 bonus issue and roughly ten weeks before the SME IPO cannot be established from the
notes. This is a direct question for management: whose loan, on what original terms (rate,
tenure, arm's-length basis), and why does the conversion not appear as a movement in the only loan
account the notes do disclose (director loans)?

═══════════════════════════════════════════════════════════════
NEW FINDING 3 — SECURITIES PREMIUM APPEARS ENGINEERED TO FUND THE BONUS ISSUE
═══════════════════════════════════════════════════════════════
The Security Premium account (Note 4, p.79) opened the year at NIL. It was credited ₹2.60 Cr from
the loan-to-equity conversion ("Add: Security Premium From Conversion of Loan to Share Capital,"
26,000.00 thousand) and then debited the identical ₹2.60 Cr nine days later for the bonus issue
("Less: Bonus Issue," 26,000.00 thousand) — before any IPO premium existed. The two amounts are
numerically identical.
🟡 Watch — not improper (securities premium is a permitted funding source for a bonus issue under
Section 52), but the sequencing (create premium via loan conversion on 07-May-2024, immediately
consume the same amount for the bonus issue on 09-May-2024) is not narrated anywhere in the notes
and is only visible by reading Note 3 and Note 4 together. Combined with Finding 2 (unidentified
lender), this is worth a single consolidated management question on the full mechanics and
counterparties of the pre-IPO capital restructuring.

═══════════════════════════════════════════════════════════════
NEW FINDING 4 — NOTE 32 RATIO ANALYSIS: SIX RATIOS NOT EXTRACTED IN PASS 1
═══════════════════════════════════════════════════════════════
Pass 1 extracted only Trade Receivables Turnover, Inventory Turnover, Trade Payables Turnover, and
Net Profit Ratio from Note 32 (p.89). Visual reconciliation of the full table (the note is
garbled in the plain-text extraction) yields six further ratios, all company-computed
(Numerator/Denominator basis stated in the note):

| Ratio | FY25 | FY24 | Change | Company's stated reason (Note 32, p.89) |
|---|---|---|---|---|
| Current Ratio | 5.08x | 1.75x | +190% | Increase in Inventory and Trade Receivable in current assets, current liabilities change lower |
| Debt-Equity Ratio | 0.18x | 1.45x | -88% | Significant increase in shareholders' fund vs prior year |
| Debt Service Coverage Ratio | 3.77x | 1.55x | +143% | Increase in EBITDA, change in debt lower |
| Return on Equity Ratio | 0.41x (41%) | 1.41x (141%) | -71% | Significant increase in shareholders' fund, net profit change slightly lower |
| Return on Capital Employed | 0.31x (31%) | 0.70x (70%) | -55% | Significant increase in shareholders' fund vs prior year |
| Net Capital Turnover Ratio | 3.02x | 5.21x | -42% | Increase in Revenue from Operations, working-capital change slightly lower |

Analysis:
- Current Ratio 5.08x is a striking new data point: the balance sheet is now heavily overcapitalised
  (>5x current assets to current liabilities) even as operating cash flow is deeply negative (Pass 1
  Finding 1) — i.e. the surplus is IPO cash sitting on the balance sheet net of the working-capital
  build, not organically generated liquidity headroom.
- FY24's Return on Equity of 141% and Return on Capital Employed of 70% are mechanical artefacts of
  a near-nil pre-IPO equity base (opening paid-up capital ₹0.08 Cr plus thin reserves), not evidence
  of extraordinary FY24 operating economics. FY25's 41% ROE, while still high, reflects the ~6.4x
  increase in the equity base (IPO + bonus + loan conversion) diluting an underlying PAT that itself
  grew 84% (₹5.52 Cr → ₹10.15 Cr). Verified independently: FY25 average shareholders' equity
  ≈ ₹24.75 Cr (computed from Note 3/4 closing balances), giving PAT/avg equity = 10.1526/24.75 =
  41.0%, consistent with the printed 0.41. 🟡 Watch — any investor extrapolating a "141% → 41% ROE
  decline" as a deteriorating-returns signal would be mis-reading a capital-base effect; flag this
  explicitly for the synthesis/valuation stages so ROE is not used as a like-for-like input without
  this adjustment.
- Net Capital Turnover Ratio (-42%) is the company's own quantified confirmation of the double
  working-capital squeeze already flagged in Pass 1 Finding 6.
🟡 Watch, collective — deepens rather than changes the existing red flags; no new standalone risk.

═══════════════════════════════════════════════════════════════
NEW FINDING 5 — NOTE 28 OTHER EXPENSES: FULL LINE-ITEM BREAKDOWN NOT EXTRACTED IN PASS 1
═══════════════════════════════════════════════════════════════
Pass 1 mentioned only the Miscellaneous Expense footnote list. The full table (Note 28, p.86, ₹ Cr):

| Line | FY25 | FY24 | YoY |
|---|---|---|---|
| Advertisement & Publicity | 0.0638 | 0.0160 | +298% |
| Asset Written Off | NIL | 0.0067 | -100% |
| Audit Fees | 0.0200 | 0.0200 | 0% |
| CSR Expense | 0.0550 | NIL | new |
| Exhibition Expenses | 0.2264 | 0.0348 | +551% |
| GST Interest and Late Fees Expense | 0.1142 | NIL | new |
| Interest on Income Tax | 0.1806 | NIL | new |
| Laboratory Testing Fee | NIL | 0.0287 | -100% |
| Miscellaneous Expense | 0.6252 | 0.0855 | +631% |
| Mca Fees Expense | 0.1234 | NIL | new |
| Rent Expense | 0.1960 | 0.2111 | -7% |
| Power and Fuel Expense | 0.0475 | 0.0267 | +78% |
| Professional and Legal Fees | 0.3614 | 0.1415 | +155% |
| Rates and Taxes | 0.0429 | 0.0591 | -27% |
| Repairs and Maintenance | 0.0583 | 0.0457 | +27% |
| Telephone & Internet | 0.0121 | 0.0082 | +47% |
| Travelling and Conveyance | 0.0994 | 0.0459 | +116% |
| **Total** | **2.2262** | **0.7300** | **+205%** |

- Total Other Expenses grew +205% YoY, more than double the revenue growth rate (+99.4%). Not
  flagged as an aggregate in Pass 1.
- Two entirely new expense lines with NIL FY24: "GST Interest and Late Fees Expense" (₹0.1142 Cr)
  and "Interest on Income Tax" (₹0.1806 Cr), combined ₹0.2948 Cr. 🟡 Watch — compliance-friction
  cost (interest for late/short payment of statutory dues) appearing for the first time in the IPO
  year; worth a direct question, particularly given the deeply negative operating cash flow already
  flagged (a plausible, non-alarming explanation is cash-timing pressure ahead of IPO proceeds
  landing on 22-Jul-2024).
- "Mca Fees Expense" ₹0.1234 Cr (new) is more plausibly a one-time ROC fee tied to the Authorised
  Share Capital increase from ₹0.80 Cr to ₹12.50 Cr (Directors' Report Capital Structure section,
  p.29-30) than a penalty — distinguishing it from the two items above narrows the genuine
  compliance-friction estimate to ~₹0.29 Cr rather than ~₹0.42 Cr.
- Miscellaneous Expense (+631%, now the single largest Other Expense line) bundles 15+ disparate
  items per its footnote including "Vivo V-Shield Warranty" with no separately quantified amount —
  this sharpens Pass 1's Section 9 warranty-provisioning observation: whatever warranty cost exists
  is being expensed through a catch-all line that itself grew 7x, with zero standalone visibility.
- Exhibition Expenses +551% is consistent with post-IPO/scale-up marketing spend, not itself
  concerning.

═══════════════════════════════════════════════════════════════
NEW FINDING 6 — NOTE 26 EMPLOYEE BENEFIT EXPENSE: FULL BREAKDOWN AND A SECOND/THIRD DISAPPEARING BENEFIT LINE
═══════════════════════════════════════════════════════════════
Note 26 (p.86, ₹ Cr): Bonus & Incentive 0.0073 (FY24) → NIL (FY25); Director's Insurance 0.10
(FY24) → NIL (FY25); Director's Remuneration 0.24 → 0.24 (flat); Contributions to PF 0.0152 →
0.0317 (+108%); Salary Expense 1.0247 → 1.4380 (+40%); Staff Welfare 0.0045 → 0.0161 (+256%).
Total 1.3917 → 1.7258 Cr, +24% — well below the +99.4% revenue growth, a materially positive
operating-leverage data point that reinforces Pass 1 Finding 5 (manufacturing-to-trading shift)
with a specific figure not previously cited.

🟡 Watch — Pass 1's Red Flag 4 (gratuity provision disappearing) is not an isolated item: two
further benefit-related lines also fell to NIL in the same year — "Director's Insurance" (₹0.10 Cr)
and "Bonus & Incentive" (₹0.0073 Cr). Individually immaterial, but the pattern of three
simultaneous benefit-line derecognitions (Gratuity Provision, Director's Insurance, Bonus &
Incentive) is worth naming as a cluster rather than treating the gratuity movement in isolation.

═══════════════════════════════════════════════════════════════
NEW FINDING 7 — CASH FLOW STATEMENT REFINES (SOFTENS) THE GRATUITY RED FLAG
═══════════════════════════════════════════════════════════════
Cross-referencing the Cash Flow Statement (p.73) against Note 7: the ₹0.0978 Cr Gratuity Provision
movement is captured within "Changes in Working Capital" as "Increase/(Decrease) in Long Term
Provision" — shown as +978.18 (thousand) in FY24 (provision created, added back as an accrual) and
(978.18) in FY25 (provision reduced, treated as a use of cash) — rather than within the "Adjustments
for" non-cash items section immediately above it (which separately captures Depreciation and
Finance Costs). This placement is more consistent with a cash settlement (gratuity actually paid
out, e.g. on an employee's exit) than with a non-cash actuarial reversal, though the notes still
name no triggering event and still disclose zero actuarial assumptions in either year (Note 2(m)).
🟡 Watch (refined from Pass 1's 🔴) — the balance-sheet mechanics are consistent with a mundane cash
payout rather than an accounting anomaly, which should modestly lower investor concern versus Pass
1's framing, but the disclosure gap itself (no note explaining the payout, no actuarial assumptions
disclosed in either year) remains open and unresolved.

═══════════════════════════════════════════════════════════════
NEW FINDING 8 — CONTINUING CAPEX PIPELINE NOT CAPTURED IN PASS 1; NO CAPITAL COMMITMENTS NOTE EXISTS
═══════════════════════════════════════════════════════════════
Note 19, Short-Term Loans and Advances (p.84): "Advance paid to Supplier for Plant and Machinery"
₹1.1567 Cr, new in FY25 (NIL FY24), the primary driver of the line's total rising from ₹0.0936 Cr
to ₹1.4220 Cr (+1,420%). Combined with Note 12's ₹8.2755 Cr FY25 PPE additions and Note 39's
₹1.8634 Cr Capital Work-in-Progress (both already flagged in Pass 1 as clean), this advance signals
an open capex pipeline extending beyond what is already capitalised on the balance sheet.
Searched the full text for a "Capital Commitments" or equivalent Schedule III disclosure
("estimated amount of contracts remaining to be executed on capital account and not provided for")
— NOT FOUND IN DOCUMENT anywhere in either note set. 🟡 Watch — a disclosure gap not previously
flagged, notable given the clear evidence of ongoing capex commitment.

═══════════════════════════════════════════════════════════════
NEW FINDING 9 — NOTE 27 FINANCE COSTS: FULL BREAKDOWN
═══════════════════════════════════════════════════════════════
Note 27 (p.86, ₹ Cr): Interest on Borrowings 0.4421 → 0.8546 (+93.3%); Bank and Loan Processing
Charges 0.1857 → 0.3856 (+107.7%); Rate Fluctuations 0.0187 → NIL. Total Finance Costs 0.6465 →
1.2402 Cr, +91.9%. Finance costs nearly doubled even though period-end borrowings actually fell
(Note 5 long-term borrowings -4.3%, Note 8 short-term borrowings -40.9%) — consistent with the
company carrying/rolling higher average debt through the first ~4 months of FY25 (before the
22-Jul-2024 IPO proceeds arrived) to fund the working-capital build, then repaying from IPO
proceeds later in the year. 🟡 Watch — adds a P&L-side data point corroborating the pre-IPO cash
squeeze already established via the Cash Flow Statement in Pass 1.

═══════════════════════════════════════════════════════════════
NEW FINDING 10 — MINOR/CLEAN ITEMS NOT PREVIOUSLY NAMED
═══════════════════════════════════════════════════════════════
- Note 15, Other Non-Current Assets (p.83): a new ₹0.10 Cr fixed deposit with Bajaj Finance Limited
  (an NBFC) appears in FY25 (NIL FY24), alongside routine NSDL/CDSL depository deposits tied to
  listing. 🟢 Clean, immaterial (₹0.10 Cr), but a new non-bank counterparty for company funds worth
  naming.
- Note 3(iii), Promoter shareholding (p.79-80): combined promoter holding fell to 68.28%
  (Mitali 45.18% + Dasharathbharthi 23.10%) from a pre-IPO base of effectively 100% (90.00% +
  9.99%, with a ~5-share rounding gap in the pre-IPO total that is immaterial). Background context
  not stated in Pass 1; promoters retain comfortable majority control post-IPO.
- Note 2(b), "Significant accounting judgements, accounting estimates and assumptions" (p.75), is a
  distinct sub-note not individually anchored in Pass 1. Content is generic boilerplate with no
  specific judgment areas named (no impairment, gratuity, revenue, or inventory judgment called
  out). Reinforces the general disclosure-thinness pattern already flagged (Notes 2(f), 2(m)) rather
  than adding a new substantive gap. 🟡 Watch, minor.
- Note 39 PPE cash-flow cross-check: FY24 cash paid for PPE/CWIP per the Cash Flow Statement
  (₹1.8620 Cr) is ₹0.0763 Cr lower than FY24's Note 12 "Previous Year" additions column
  (₹1.9383 Cr) — a small, immaterial timing/accrual difference (e.g. capital creditor unpaid at
  year-end), not worth a red flag but noted for completeness of the cross-check.

═══════════════════════════════════════════════════════════════
SUPPLEMENTARY CONTEXT (outside Notes scope, flagged only because it conditions Note 31's reading)
═══════════════════════════════════════════════════════════════
The AGM Notice section of this same annual report (p.7-8, p.30-31, ordinary/special resolutions) —
NOT a numbered financial-statement note, included here only because it materially affects how
Note 31's KMP remuneration figures should be read forward — proposes raising the ceiling on monthly
remuneration for both the Chairman & Managing Director and the Whole-time Director from Rs 1,00,000
to up to Rs 2,50,000 (a 150% ceiling increase), even though FY25 actual remuneration paid was flat
at ₹0.12 Cr each (Note 31, p.88). If the increased ceiling is utilised in FY26, combined KMP
remuneration could rise from ₹0.24 Cr to as much as ₹0.60 Cr. This is forward-looking, sourced
outside the Notes, and is flagged as supplementary context only — not counted as a Notes-based
finding for the accounting-quality scoring in Pass 3.

═══════════════════════════════════════════════════════════════
PASS 2 NEW FINDINGS SUMMARY
═══════════════════════════════════════════════════════════════
1. 🟢 Correction: Note 4 bonus-issue debit from Reserve & Surplus is ₹4.00 Cr, not ₹0.40 Cr as
   stated in Pass 1 (10x unit error); fully reconciles to the bonus share face value, confirming
   the bonus issue was cleanly funded from free reserves/premium.
2. 🔴 The ₹3.00 Cr loan-to-equity conversion (Note 3, 4,00,000 shares at Rs 75) does not reconcile
   to any named lender; the disclosed director-loan movement is fully explained by cash alone.
3. 🟡 Securities premium created by the loan conversion (₹2.60 Cr) was consumed for the bonus issue
   nine days later in an identical amount — engineered pre-IPO capital-structure sequencing not
   narrated in the notes.
4. 🟡 Six additional Note 32 ratios extracted (Current Ratio, Debt-Equity, DSCR, ROE, ROCE, Net
   Capital Turnover); FY24's 141% ROE/70% ROCE are base-effect artefacts of a near-nil pre-IPO
   equity base, not operating-economics signals — a caution for downstream ROE use.
5. 🟡 Note 28 Other Expenses full breakdown: total +205% YoY (vs +99.4% revenue growth); two new
   compliance-friction lines (GST interest/late fees + income-tax interest, ₹0.2948 Cr combined)
   appear for the first time in the IPO year.
6. 🟡 Note 26 Employee Benefit Expense breakdown: costs grew only +24% vs +99.4% revenue (positive
   leverage); two further benefit lines (Director's Insurance, Bonus & Incentive) joined the
   Gratuity Provision in falling to NIL this year — a three-item cluster, not an isolated event.
7. 🟡 Cash Flow Statement placement of the Gratuity Provision movement (within working-capital
   changes, not non-cash adjustments) is more consistent with a cash payout than a non-cash
   reversal — softens Pass 1's 🔴 to 🟡, though the disclosure gap remains open.
8. 🟡 New ₹1.1567 Cr advance to supplier for plant and machinery (Note 19) signals an open capex
   pipeline; no Capital Commitments note exists anywhere in the document — a disclosure gap not
   previously flagged.
9. 🟡 Note 27 Finance Costs breakdown: costs nearly doubled (+91.9%) despite falling period-end
   borrowings, consistent with higher average pre-IPO debt carrying costs.
10. 🟢/🟡 Minor items: new NBFC deposit (Bajaj Finance, ₹0.10 Cr, immaterial); promoter post-IPO
    holding 68.28%; Note 2(b) judgments sub-note is boilerplate with no specifics; small immaterial
    PPE cash-flow timing difference.

END OF PASS 2.
