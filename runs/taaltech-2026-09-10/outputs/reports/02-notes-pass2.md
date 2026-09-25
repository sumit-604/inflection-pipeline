# STAGE 2 — NOTES TO FINANCIAL STATEMENTS, PASS 2 OF 3 (WHAT WAS MISSED)
Company: TAAL Tech Limited (TAALTECH) | Run: taaltech-2026-09-10
Source: Annual_Report_2026 (FY2025-26 AR, filed to BSE 7-Aug-2026, scrip 539956), 164 pages.
Cross-checked against: Results_Q4FY26_Mar_2026, Results_Q1FY27_Jun_2026,
Results_Q3FY26_Dec_2025.

This pass does not repeat Pass 1 findings. It (i) resolves the five items
Pass 1 left open, (ii) confirms or refutes the six leads named in the task
brief, and (iii) reports genuinely new findings surfaced on the note-by-note
re-read. All amounts in ₹ lakh unless converted to ₹Cr (1 lakh = 0.01 Cr).

═══════════════════════════════════════════════════════════════
PART A — THE FIVE ITEMS PASS 1 LEFT OPEN, NOW RESOLVED
═══════════════════════════════════════════════════════════════

## A1. Note 41 PBT reconciliation — resolved. The note is right neither
figure, and it is not what its own heading claims to be.

Traced line by line against the audited primary statements:

**Note 41(b) Consolidated, "Summarised Statement of Consolidated Profit
and Loss of TTL" (p.155):**
| Line | Note 41(b) | Standalone P&L (p.66) | Match? |
|---|---|---|---|
| Revenue | 19,010.10 | 19,010.10 (Note 24) | Identical |
| Other income | 1,851.18 | 1,851.18 (Note 25) | Identical |
| Employee benefits | 6,816.03 | 6,816.03 | Identical |
| Finance costs | 44.33 | 44.33 | Identical |
| Depreciation | 404.21 | 404.21 | Identical |
| Other expenses | 1,923.77 | 1,923.77 | Identical |
| Total Expenses | 9,188.34 | 13,922.82 | **Differs by exactly 4,734.48** |
| PBT | 11,672.94 | 6,976.49 (audited) | Differs |

4,734.48 is the standalone "Cost of technical services" line (Note 27,
p.66) — the intercompany subcontract charge paid to TAAL Technologies
Inc, USA. Note 41(b) is the **Standalone P&L with only that one expense
line deleted**, nothing else adjusted: no subsidiary revenue added, no
subsidiary expense added, no subsidiary tax added, no elimination of the
matching intercompany income on the other side. Deleting an expense with
no offsetting revenue mechanically inflates PBT. This is confirmed
identically in Note 41(c) "Summarised Consolidated Balance Sheet" (Total
Assets 25,499.46 = Standalone Total Assets 25,499.45 exactly, Note 41(c)
p.155, standalone BS p.65) and Note 41(d) "Summarised Consolidated Cash
Flow Statement" (CFO 2,886.29 = Standalone CFO 2,886.27 exactly,
Standalone Cash Flow Statement p.67).

**Neither audited primary statement is wrong.** Standalone PBT ₹6,976.49
lakh (p.66) and audited Consolidated PBT ₹7,436.21 lakh (p.115) are both
internally consistent and reconcile to their own cash flow and balance
sheet statements. The error sits entirely inside Note 41(b)-(d), which
mislabels the **Standalone** financials (with one line item struck) as
"Consolidated." 🔴 Red Flag — quantified downstream-reader risk: a
reader who takes Note 41 at its word, rather than the audited primary
Consolidated statements, would compute PBT 57% higher (11,672.94 vs
7,436.21), CFO 54% higher (2,886.29 vs the true Consolidated 1,874.29,
Statement of Cash Flows p.116), and Total Assets 5.9% lower (25,499.46 vs
the true Consolidated 27,092.63, Consolidated Balance Sheet p.114) than
the real Group position — and would read a CFO/PAT ratio of roughly 51%
(2,886.29/5,671.50) instead of the true 33.0% that is this run's active
FLAG-CASH. This is the single most consequential note-quality defect in
the filing: it sits inside the AUDITED consolidated financial statements,
not a voluntary MD&A table, and directly contradicts LBF-1 and LBF-2 if
read uncritically.

## A2. Unbilled revenue — tied to policy, to the quarterly run-rate, and
decomposed into volume effect vs billing-lag effect.

Revenue recognition policy (Note 2.7, both sets, p.6 of the policy
section / consolidated equivalent p.12 of the policy section): "Revenue
recognized in excess of billings is classified as contract assets
(Unbilled revenue) included in other current financial assets."
Consistent with the 95.5% T&M revenue mix (Note 24) — unbilled revenue
here is overwhelmingly billing-cycle lag on time-and-material delivery,
not percentage-of-completion milestone timing on the small 4.5%
fixed-price book.

Quarterly consolidated revenue run (Results filings, all consolidated):
Q3FY26 (Dec-25) ₹45.79cr → Q4FY26 (Mar-26) ₹57.04cr → Q1FY27 (Jun-26)
₹64.81cr — a real, accelerating top line (Results_Q3FY26 p.1;
Results_Q4FY26 p.14; Results_Q1FY27 p.1, second/consolidated line).

Decomposing the unbilled build: unbilled revenue as a % of exit-quarter
revenue (a proxy for "days of work outstanding," controlling for the
revenue run-rate change) —
- Mar-25: unbilled ₹4.64cr / Q4FY25 revenue ₹44.69cr (Results_Q4FY26 p.14,
  prior-year column) = **10.4%**.
- Mar-26: unbilled ₹13.75cr / Q4FY26 revenue ₹57.04cr = **24.1%**.

The ratio more than doubled even after netting out the revenue
acceleration itself. If unbilled had simply tracked the higher exit
run-rate at the SAME 10.4% ratio, it would sit near ₹5.94cr at Mar-26, not
₹13.75cr — **roughly ₹7.8cr of the build is not explained by revenue
growth alone**; it reflects a genuine lengthening of the billing cycle
(more work delivered per rupee billed at period end). 🔴 Red Flag,
sharper than Pass 1's framing: the unbilled build is CONSISTENT WITH, but
not FULLY EXPLAINED BY, the Q4 FY26/Q1 FY27 revenue acceleration — a
material share is billing-cadence deterioration, independent of volume,
and this is the mechanical driver of the CFO shortfall in LBF-2. No
contract-asset rollforward/reconciliation note exists in either note set
(searched; absent) to show opening/closing/reclassified-to-billed
movements directly — this decomposition is derived from the disclosed
period-end balances and results-filing revenue, not from a company-
provided rollforward. NOT FOUND IN DOCUMENT: an explicit contract-asset
movement schedule.

Asymmetry worth naming: the same policy paragraph defines "Billings in
excess of revenue recognized" as a contract liability (Deferred revenue),
but no such line appears anywhere in Other current liabilities (Note 21
Standalone/Consolidated) in either year — contract liabilities are Nil
both years. 🟡 Watch — the company's working-capital build in this note
set runs one-directionally (only contract assets grow); there is no
offsetting deferred-revenue cushion.

## A3. Vishkul Enterprises Pvt Ltd loan — full trace.

- **Board approval:** NOT FOUND IN DOCUMENT. No board-meeting date is
  disclosed anywhere in the AR as the specific approval for this ₹1,000
  lakh loan. The only Section 186-linked board date disclosed is 10-Feb-
  2026 (Directors' Report Item 5, p.20/34), and that meeting's business
  was to seek shareholder approval to RAISE the aggregate Section 186
  ceiling from ₹250cr to ₹350cr for FUTURE use — it is prospective and
  distinct from this loan (see A3/lead-f below). Given the ~9.85%
  effective, near-full-year interest income (₹98.55 lakh on ₹1,000 lakh),
  the loan was almost certainly disbursed early in FY26 (around Apr-May
  2025), before the Feb-2026 meeting — confirming the two events are
  unrelated. No earlier board-meeting date is named for the loan itself.
- **Section 186 disclosure:** Directors' Report (p.34) states "Particulars
  of Loans, Guarantees & Investments covered under Section 186 of the
  Act has been given in Notes to Financial Statements" — but no note in
  either set carries a distinct "Section 186" heading, and none states
  the loan's purpose or contractual interest rate as Section 186(4)
  requires (searched for "purpose for which"/"rate of interest"/"utilised
  by the recipient" — no matches anywhere in the document). The 9.85%
  figure used throughout this run is DERIVED (interest income ÷ opening-
  ish balance), never disclosed as a stated contractual rate.
- **Audit committee:** the Audit Committee's general mandate includes
  "approval of related party transactions" (Corporate Governance Report,
  p.~46) and met four times in FY26 (28-May-2025, 04-Aug-2025,
  11-Nov-2025, 10-Feb-2026) — but no minute, meeting date, or agenda item
  is disclosed anywhere in the AR as the specific approval for the
  Vishkul loan. NOT FOUND IN DOCUMENT.
- **AOC-2 (Form for Section 188 disclosures, Annexure 'E', p.56):** both
  Part 1 (non-arm's-length) and Part 2 (material arm's-length) tables are
  filled "NA" across every field — name, nature, duration, value,
  approval date, all "NA." The company's own governance framework
  therefore treats the ₹10cr Vishkul ICD as NOT a "material" related
  party transaction requiring Section 188/AOC-2 disclosure. This is
  consistent with (and helps explain) the absence of a named approval
  date elsewhere — the company's materiality threshold routed this
  transaction below the level that triggers formal AOC-2 particulars,
  even though it is disclosed at Ind AS 24 level (Note 36/37) and in
  CARO. 🟡 Watch — a ₹10cr unsecured loan to the 50.74% holding company
  sitting below the company's own "material RPT" bar is itself a finding
  about where that bar is set.
- **Repayment terms:** CARO Annexure A, clause 3(iii)(c) (p.60): "the
  schedule of repayment of principal and payment of interest has been
  stipulated and repayments of principal amounts and receipt of interest
  are regular as per stipulation" — confirms a repayment schedule
  EXISTS and is being followed, per the auditor, but the schedule's actual
  terms (tenure, rate, moratorium, security) are not disclosed anywhere in
  the AR itself, standalone or consolidated notes.
- **Cash flow statement:** **YES, it appears distinctly.** "Loans to
  related Party (1,000.00)" is a separate line under Cash flow from
  Investing activities in BOTH the Standalone Statement of Cash Flows
  (p.67) and the Consolidated Statement of Cash Flows (p.116) — Pass 1
  did not check this explicitly; it is clean, traceable disclosure on
  this specific point. 🟢 Clean (cash-flow-statement visibility) even as
  the surrounding approval-trail disclosure remains thin.

## A4. Retained earnings Rs91.78 lakh — resolved as unexplained, and the
mislabeling goes deeper than a missing footnote.

Found identically in Standalone Note 16(c) "Retained earnings" (p.83, "Other
adjsutment [sic] 91.78," Mar26 only, Nil Mar25) and Consolidated Note 17(d)
"Retained earnings" (p.139, same caption, same amount, same year-only
pattern). Because the value is IDENTICAL in both standalone and
consolidated books, it cannot be a consolidation-mechanics item (foreign
subsidiary translation, elimination adjustment, minority interest) — those
would differ between the two sets or route through the Foreign Currency
Translation Reserve, which is already a separate, fully reconciling line
(₹365.51 lakh FY26, Note 17(c) Consolidated, p.139). This is a
**parent-company-level, non-P&L, non-OCI credit of ₹91.78 lakh**, present
in the standalone books and carried through unchanged on consolidation.

New finding beyond Pass 1: **the face of both primary Statements of
Changes in Equity mislabels this item.** The Standalone SOCE (p.68) and
Consolidated SOCE (p.117) each show a single row "Add: Other comprehensive
income" in the Retained Earnings column of **98.56** (Consolidated) /
**98.56** (Standalone) — but the audited Statement of P&L's actual Total
Other Comprehensive Income for the year is only **₹6.78 lakh** (both
Standalone p.66 and Consolidated p.115). 6.78 + 91.78 = 98.56 exactly: the
primary Statement of Changes in Equity folds the unexplained ₹91.78 lakh
into a row captioned "Other comprehensive income," overstating what a
reader would take as OCI by more than 14x (₹98.56 lakh shown vs ₹6.78 lakh
actual). Only the notes (16(c) Standalone / 17(d) Consolidated) break the
two components apart — and even there, the ₹91.78 lakh sub-line carries no
narrative at all.

Ruled out as explanations, checked directly in this pass: not the Labour
Code exceptional item (₹333.02 lakh, runs through P&L as Exceptional
Items, Note 31/30) or the customer-claims reversal (₹371.05 lakh, same
route); not explained by the NCLT merger/restatement note (Note 47
Standalone, p.104), which addresses the appointed-date mechanics and name
change only; FY25 comparatives were NOT restated to include any prior
amount (the column reads Nil), which also rules out a retrospective Ind
AS 8 error correction (that would restate the FY25 opening balance, not
insert a current-year-only credit). 🔴 Red Flag, elevated from Pass 1's
rating: this is not merely an unexplained note-level credit; it is a
primary-statement captioning error that misstates the composition of
Other Comprehensive Income on the face of the audited Statement of
Changes in Equity, standalone and consolidated alike.

## A5. The "summarised consolidated P&L" note — what it actually
summarises, and who it would mislead.

Resolved together with A1 above: Note 41(b)-(d) Consolidated is not a
summary of the consolidated Group at all. It is the **Standalone**
Statement of Profit and Loss, Balance Sheet, and Cash Flow Statement,
with exactly one line (the intercompany "Cost of technical services"
expense) stripped out of the P&L sub-table and nothing else touched. The
heading text itself is internally contradictory: part (a) lists "TAAL
Tech Limited and its subsidiaries (TTL)" as if TTL were itself a
subsidiary being disclosed under Ind AS 112's "material partly-owned
subsidiary" summarised-financials requirement (100% ownership, 0% NCI
shown) — but TTL is the LISTED PARENT, not a subsidiary of itself, and
the Group has zero NCI anywhere (Note 41(a) itself states 0.00% NCI). Ind
AS 112 paragraph 12/B10-B16 requires this summarised-financials
disclosure only for subsidiaries with MATERIAL non-controlling interests;
since the Group has no NCI at all, this entire Note 41(b)-(d) sub-table
does not appear to correspond to any disclosure Ind AS 112 actually
requires for this Group — it reads as a carried-over or misapplied
template structure populated with the wrong (standalone, adjusted) data.
🔴 Red Flag — a downstream reader (screener tool, analyst skimming notes
for "the group P&L," or an automated extraction pipeline) who pulls PBT,
Total Assets, or CFO from Note 41 rather than from the primary
Consolidated Financial Statements gets a materially rosier picture on
every one of the three financial statements it purports to summarise
(see A1 for the exact deltas). This is worse than a routine drafting
error because it sits inside the set of notes an investor is directed to
by the Directors' Report itself (see A3, "particulars...given in Notes to
Financial Statements").

═══════════════════════════════════════════════════════════════
PART B — SIX LEADS FROM THE PRIOR PARTIAL ATTEMPT, CONFIRMED AT SOURCE
═══════════════════════════════════════════════════════════════

**(a) CONFIRMED — CARO Annexure A, clause 3(iii)(a) vs 3(iii)(d) directly
contradict each other.** Clause 3(iii)(a) (p.60): "The Company has made
investments and granted unsecured loans to companies and other parties in
respect of which the requisite information is as below," followed by a
table showing "Vishkul Enterprises Pvt. Ltd — Aggregate amount granted/
provided during the year: 1,000.00." Clause 3(iii)(d), same page: "There
is no overdue amount for more than ninety days in respect of loans given.
**Further, the Company has not given any advances in the nature of loans
to any party during the year.**" These two clauses, four lines apart in
the same Annexure, cannot both be literally true: (a) discloses a ₹10cr
loan granted during FY26; (d) states no loan of any kind was given during
the year. Most likely a boilerplate/template carry-over error in clause
(d) that was not updated to reflect the new disclosure added in clause
(a) — but as filed, it is a direct textual contradiction inside the
signed Independent Auditor's Report. 🔴 Red Flag.

**(b) CONFIRMED.** Note 13 Standalone, "Current financial assets — Loans"
(p.85): "Unsecured, considered good / Loans recoverable in cash 1,000.00
/ Total Current financial assets – Loans 1,000.00." No counterparty name,
no rate, no tenure anywhere in the note itself — the Vishkul identity is
only recoverable by cross-reading Note 37(B)'s RPT transaction table.
Classified entirely Current (no non-current portion), consistent with
Note 37's "regular repayment per stipulation" (CARO 3(iii)(c)) implying a
short tenor, though the actual maturity date is not disclosed.

**(c) CONFIRMED.** Note 39 Standalone (p.99) / Note 38 Consolidated
(p.152), Fair value hierarchy: "Loans 1,000.00" is listed under "Level 3
— Financial assets measured at amortized cost," alongside Trade
receivables and Other financial assets — with NO specific
counterparty-credit-risk commentary. Immediately below, the note gives an
explicit sentence for a DIFFERENT line: "The fair values of security
deposits were calculated based on cash flows discounted using a current
lending rate. They are classified as level 3 fair values...due to the
inclusion of unobservable inputs including own and counterparty credit
risk" — naming security deposits specifically, silent on the new,
materially larger Loans balance. Additional new observation this pass:
the note's closing boilerplate paragraph ("The fair values of borrowings,
liability component of convertible preference shares and security
deposits were calculated...") references **borrowings** and
**convertible preference shares** — instruments the company does not
have in either year (Note 40/41 Capital Management confirms nil debt,
and no preference shares exist anywhere in the share capital notes). This
reads as an un-updated template paragraph, never revised to mention the
new ₹10cr Loans line that first appeared this year. 🟡 Watch — disclosure
maintenance quality.

**(d) CONFIRMED, and extended with the full quantified KMP table.** Note
37 Standalone (B) (p.98) groups the Vishkul transaction under sub-heading
"(i) Entities under common control:" even though Note 37(A) on the
immediately preceding page separately and correctly lists "Holding
company: Vishkul Enterprises Private Limited, India" as its own category
distinct from "Entities under common control." The identical structure
recurs in Note 36 Consolidated (p.150-151) — so the mislabeling is not a
standalone-vs-consolidated cross-note issue but occurs **within each note
set internally**, in both sets. New this pass: the FY25 KMP remuneration
comparatives differ between the Standalone (Note 37, p.98) and
Consolidated (Note 36, p.151) notes on **four separate lines**, not just
the previously-flagged Laurus Tradecon cut-off date:
| KMP | Standalone FY25 | Consolidated FY25 | Difference |
|---|---|---|---|
| Salil Baldevraj Taneja (Director Remuneration) | 368.80 | 344.60 | ₹24.20 lakh |
| Sudishkumar Kuttappan Nair | 31.75 | 17.58 | ₹14.17 lakh |
| Priya Chouksey (up to 30-09-2024) | 2.63 | 4.14 | ₹1.51 lakh (consolidated HIGHER) |
| Aditya Oza | 1.88 | – (nil shown) | ₹1.88 lakh |
The FY26 (current year) figures for all four match exactly between the
two note sets; only the FY25 comparative differs, and the direction is
inconsistent (sometimes standalone higher, sometimes consolidated
higher) — inconsistent with a simple "subsidiary paid additional
remuneration" explanation, which would push consolidated figures
uniformly higher, never lower. This looks like a genuine comparative-
figure error in at least one of the two notes, present in the audited
AR as filed. 🔴 Red Flag, upgraded from Pass 1's 🟡 — four discrepant
lines, not one, and no consistent direction to explain them.

**(e) CONFIRMED.** Directors' Report (p.34, printed page number "20" in
the source PDF pagination but page 34 by this extraction's file-page
count — anchor as p.34 per the file's own page markers): "PARTICULARS OF
LOANS, GUARANTEES AND INVESTMENTS — Particulars of Loans, Guarantees &
Investments covered under Section 186 of the Act has been given in Notes
to Financial Statements forming part of this Annual Report." No note in
either set carries a heading naming "Section 186." Searched exhaustively
for the Section 186(4) mandated language ("purpose for which," "rate of
interest," "utilised by the recipient") — zero matches anywhere in the
164-page document. The nearest disclosures (Note 13/37 Standalone,
Note 36 Consolidated, CARO Annexure A clause 3(iii)) collectively give
amount, counterparty (via cross-reference only), and interest income, but
never a stated rate, tenure, or purpose. 🟡 Watch — the Directors' Report
points to a disclosure that does not exist under any distinct heading.

**(f) CONFIRMED.** AGM Notice Item 5 (p.4-5) and Directors' Report Item
No. 5 narrative (p.20): the special resolution seeks to raise the
Section 186 aggregate ceiling from the "existing limit of Rs. 250 crores"
to "Rs. 350 crores," approved for placing before shareholders by the
Board at its meeting of **10-Feb-2026**. This is explicitly headroom for
FUTURE loans/investments/guarantees, framed as "to achieve optimum
utilisation of funds...and to achieve long term strategic business
objectives" — forward-looking language, not a ratification of a past
transaction. The Vishkul loan (₹10cr) is immaterial relative to even the
PRE-EXISTING ₹250cr ceiling and needed no special resolution to be legal
under Section 186 in the first place. The two items are confirmed
unrelated: the AGM Item 5 resolution has no bearing on the Vishkul loan's
approval basis, and citing it as approval cover for that loan would be
incorrect. 🟢 Clean (on this specific point) — no contradiction between
the AGM item and the loan, just confirmation they are separate matters.

═══════════════════════════════════════════════════════════════
PART C — ADDITIONAL NEW FINDINGS FROM THE COMPLETE RE-READ
(not among the five open items or six leads; surfaced independently)
═══════════════════════════════════════════════════════════════

## C1. The ₹51.71 lakh "Receivable from related parties" cannot be
reconciled under EITHER the standalone or the consolidated definition of
"related party" — and its identical appearance in both note sets is
itself evidence of a probable consolidation-elimination gap.

Confirmed at source: Note 10 Standalone (p.83) and Note 10 Consolidated
(p.135) both show "Receivable from related parties 51.71" (Mar26) / Nil
(Mar25) — the exact same figure in both books.

Under Ind AS 24 as applied in the Standalone accounts, "related parties"
includes the wholly-owned subsidiaries (TAAL Technologies Inc USA, TAAL
Tech GmbH), which have disclosed "Service Rendered" transactions in
FY26 (₹127.89 lakh and ₹29.92 lakh respectively, Note 37(B) Standalone,
p.98) — the only revenue-type RPT categories disclosed anywhere in either
note set, and therefore the only plausible source of a trade
receivable. Under the CONSOLIDATED definition, however, subsidiaries are
not "related parties" to the Group (they are the reporting entity) — the
Consolidated related-party universe is only Vishkul, Laurus Tradecon,
Taneja Aerospace, Katra Auto, Asscher, and KMP (Note 36(A) Consolidated,
p.150) — **none of which has any disclosed revenue/services transaction
in FY26** (Note 36(B) shows only the Vishkul loan/interest and the
Taneja Aerospace car sale, neither a revenue transaction that would
create a trade receivable).

Two explanations are consistent with the evidence, and the document does
not allow choosing between them:
1. The ₹51.71 lakh is the (partial) unpaid balance of the subsidiary
   "Service Rendered" transactions, and this intercompany trade
   receivable was **not eliminated** on consolidation — an intercompany
   balance that should net to zero in the Group's books but was carried
   through unchanged, a control weakness in the consolidation process
   (though immaterial in quantum, ~0.2% of Consolidated Total Assets).
2. The ₹51.71 lakh arises from a related-party revenue transaction that
   Note 36/37 simply does not disclose at all — meaning the RPT note is
   incomplete, not merely under-narrated.
🔴 Red Flag either way — Pass 1 flagged the balance as unreconciled;
this pass establishes that reconciliation is not merely undisclosed but
structurally impossible given what IS disclosed, under either accounting
scope.

## C2. Neither Independent Auditor's Report carries a Key Audit Matter.

Both the Standalone auditor's report (p.57, "We have determined that
there are no key audit matters to communicate in our report") and the
Consolidated auditor's report (p.~148, identical sentence) report zero
KAMs. 🟡 Watch — this is the auditor's professional judgment, not a
company disclosure failure, and is noted here as context rather than a
company-side red flag: the profit-quality concentration in MTM gains
(LBF-1), the cash-conversion deterioration (LBF-2), the new related-party
loan (LBF-4), and the Note 41 numerical error (A1/A5, an error inside the
audited financial statements themselves) all sit within the same audit
period without being surfaced as a KAM. Worth a question for management/
auditor, not a finding against the company's own disclosures.

## C3. AOC-1 and AOC-2 cross-check: no contradiction found beyond what is
already noted in A3/lead (e).

Checked AOC-1 (Part A, subsidiary financials, p.162) against AOC-2
(Section 188 particulars, p.56) for internal consistency — no further
discrepancy found; AOC-1's subsidiary figures were already fully
extracted in Pass 1 and are unaffected by this pass's findings.

═══════════════════════════════════════════════════════════════
PASS 2 NEW FINDINGS SUMMARY
═══════════════════════════════════════════════════════════════

| # | New finding this pass | Anchor | Rating |
|---|---|---|---|
| 1 | Note 41(b)-(d) Consolidated is the Standalone P&L/BS/CF with only the intercompany service-cost expense stripped out — not a consolidated summary at all; overstates PBT 57%, CFO 54%, understates Total Assets 5.9% vs audited Consolidated figures | Note 41, Consolidated, p.155-156; cross-checked p.66-67, p.114-116 | 🔴 |
| 2 | Unbilled revenue growth (+196%) is only partly explained by the Q3→Q4→Q1FY27 revenue acceleration; unbilled-to-exit-quarter-revenue ratio more than doubled (10.4%→24.1%), implying ~₹7.8cr of the build is billing-cadence lengthening, not volume | Note 14, Consolidated, p.137; Results_Q3/Q4FY26, Q1FY27 | 🔴 |
| 3 | CARO Annexure A clause 3(iii)(a) discloses a ₹10cr loan given during the year; clause 3(iii)(d), same page, states no loan was given during the year — direct contradiction in the signed audit report | Annexure A to Independent Auditor's Report, p.60 | 🔴 |
| 4 | Vishkul loan: no board-approval date, no audit-committee minute, and no Section 186(4) purpose/rate disclosure found anywhere in the AR; AOC-2 (Section 188 form) shows the transaction as "NA" i.e. below the company's own material-RPT threshold | Directors' Report p.34; AOC-2, Annexure E, p.56; Note 13, p.85 | 🟡 |
| 5 | The ₹91.78 lakh direct credit to Retained Earnings is folded into a line captioned "Other comprehensive income" on the face of BOTH primary Statements of Changes in Equity (standalone and consolidated), overstating apparent OCI by >14x (98.56 shown vs 6.78 actual); the credit is identical in both books, ruling out a consolidation-mechanics explanation | Standalone SOCE p.68 / Note 16(c) p.83; Consolidated SOCE p.117 / Note 17(d) p.139 | 🔴 |
| 6 | KMP remuneration FY25 comparatives differ standalone vs consolidated on four lines (not one), in inconsistent directions, ruling out a simple subsidiary-remuneration explanation | Note 37 Standalone p.98 vs Note 36 Consolidated p.151 | 🔴 |
| 7 | ₹51.71 lakh "receivable from related parties" cannot reconcile under either the standalone or the consolidated definition of related party; identical value in both note sets suggests an un-eliminated intercompany balance or an undisclosed RPT | Note 10, both sets, p.83/p.135 | 🔴 |
| 8 | Fair value hierarchy note's boilerplate paragraph still references "borrowings" and "convertible preference shares" the company does not have, and gives no counterparty-credit-risk commentary for the new, material Loans line, unlike security deposits | Note 39 Standalone p.99-100 / Note 38 Consolidated p.152 | 🟡 |
| 9 | Neither Independent Auditor's Report (standalone or consolidated) communicates any Key Audit Matter | p.57, p.~148 | 🟡 |
| 10 | AGM Item 5's Section 186 limit increase (₹250cr→₹350cr, board date 10-Feb-2026) is confirmed prospective and unrelated to the Vishkul loan's approval basis | AGM Notice p.4-5; Directors' Report p.20 | 🟢 |
| 11 | Contract liabilities (Deferred revenue) are Nil both years despite a policy that defines them — working capital build is one-directional (contract assets only) | Note 21, both sets | 🟡 |

END OF PASS 2.
