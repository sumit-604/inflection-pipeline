# STAGE 2 — NOTES TO FINANCIAL STATEMENTS, PASS 2 OF 3 (WHAT WAS MISSED)
Company: TAAL Tech Limited (TAALTECH) | Run: taaltech-2026-09-10
Source: Annual_Report_2026 (FY2025-26 AR, filed to BSE 7-Aug-2026, scrip 539956), 164 pages.

## MECHANICAL FAILURE NOTICE — READ THIS FIRST

This pass did not complete. Partway through the note-by-note re-read, every
file under `runs/taaltech-2026-09-10/` (the extracted annual report, the
Pass 1 report I had already read once at the start of this session, the
supporting results filings, and `companies/TAALTECH.md`) became inaccessible
to this subagent's Read and Grep tools. Read calls returned "File does not
exist"; Grep calls against the run folder and against `runs/` as a whole
returned "No files found" / zero matches, including a repo-wide,
case-insensitive grep for "taaltech" and for the scrip code "539956", which
matched nothing anywhere in the repository. Other run folders
(`runs/indnippon-2026-09-10/`, `runs/totem-2026-09-09/`, `runs/iex-2026-09-08/`
etc.) remained fully intact and listable throughout, so this is not a
general tool outage — the taaltech-2026-09-10 corpus specifically disappeared
from the working tree mid-task.

This is a mechanical failure, not a finding about TAAL Tech's accounting. It
most likely reflects a concurrent process (branch switch, clean, or reset)
acting on the same shared repo checkout while this subagent was mid-read;
the session's git-status snapshot at conversation start showed a different
active branch (`run/totem-2026-09-09`) with no taaltech files listed as
untracked, consistent with the taaltech corpus having been created after
that snapshot and removed later by an operation outside this subagent's
control.

Per CLAUDE.md ("Never halt a run on company quality... only mechanical
failures halt"), this qualifies as the kind of failure that halts: I cannot
verify or extend further findings against a corpus that no longer exists on
disk. Everything reported below was read directly from the live document,
with page anchors captured at read time, in the interval before access was
lost. Nothing below is inferred from memory of a typical annual report or
estimated — items I had queued but had not yet reached are listed under
ESCALATION as NOT COMPLETED, not filled in.

**Action needed from the orchestrator:** re-provision
`runs/taaltech-2026-09-10/` (confirm Pass 1's output file is still present
and byte-identical, since Pass 3 depends on re-reading it) and re-run Pass 2
to complete the sweep the mechanical failure interrupted, before Pass 3
proceeds.

═══════════════════════════════════════════════════════════════
PASS 2 NEW FINDINGS (confirmed before file access was lost)
═══════════════════════════════════════════════════════════════

Pass 1 covered the Notes to Financial Statements (standalone and
consolidated) exhaustively. This pass's surviving work extended into two
areas Pass 1 did not reach — the Independent Auditor's Report / CARO
Annexure A, and the AGM Notice's Section 186 resolution — plus a deeper
re-read of the Standalone Related Party note (37) against the Consolidated
one (36), which is exactly the kind of cross-reference-between-notes check
Pass 2 is meant to run.

## NF-1. CARO Annexure A, clause 3(iii): the Vishkul loan, and an internal
contradiction inside the audit report itself — 🔴 new anchor, not in Pass 1

Pass 1 anchored the ₹1,000 lakh loan to Vishkul Enterprises Pvt Ltd via
Note 36 (Consolidated RPT). Pass 1 did not reach the Independent Auditor's
Report's CARO Annexure A, which carries independent, additional detail.

Verbatim, Annexure A to the Independent Auditor's Report, clause 3(iii)
(p.60-61 in the extracted text's page numbering):

> (a) "The Company has made investments and granted unsecured loans to
> companies and other parties in respect of which the requisite information
> is as below. The Company has not provided any guarantee or security or
> granted any advances in the nature of loans, secured or unsecured to
> companies, firms, limited liability partnership or any other parties
> during the year. The Company has not made any investments in firms and
> limited liability partnership." Table: "Vishkul Enterprises Pvt. Ltd —
> Aggregate amount granted/provided during the year: 1,000.00 [₹ lakh];
> Balance outstanding as at balance sheet date: 1,000.00."
> (b) "the investments made, guarantees provided, security given and the
> terms and conditions of the grant of all loans and advances in the nature
> of loans and guarantees provided are not prejudicial to the Company's
> interest."
> (c) "the schedule of repayment of principal and payment of interest has
> been stipulated and repayments of principal amounts and receipt of
> interest are regular as per stipulation."
> (d) "There is no overdue amount for more than ninety days in respect of
> loans given. Further, the Company has not given any advances in the
> nature of loans to any party during the year."

Clause (d)'s second sentence — "the Company has not given any advances in
the nature of loans to any party during the year" — directly contradicts
clause (a) of the same paragraph, which discloses the ₹1,000 lakh loan
granted to Vishkul during the year. 🔴 Red Flag: this is an internal
contradiction inside the statutory audit report, not merely a
notes-to-accounts inconsistency — most likely a stale boilerplate sentence
carried over from a prior year's CARO annexure and not updated for this
year's new loan. It does not change the substance of what was disclosed
(the loan itself is clearly and consistently reported in (a)-(c)), but it
is a document-quality flag on the auditor's own report.

This also partly answers the open item on repayment terms: clause (c)
confirms a repayment schedule for principal and interest WAS stipulated and
is being met, though the schedule's actual dates/tenure are not disclosed
anywhere in the AR (see ESCALATION).

Rating: 🔴 Red Flag (internal contradiction in the audit report) / 🟡 Watch
(confirms a stipulated repayment schedule exists, partially resolving the
"repayment terms" question without disclosing its specifics).

## NF-2. Note 13, Standalone, "Current financial assets - Loans" (p.85) —
new primary-statement anchor for the Vishkul loan

> "Current financial assets - Loans / Unsecured, considered good / Loans
> recoverable in cash: 1,000.00 [Mar-26] / – [Mar-25] / Total Current
> financial assets - Loans: 1,000.00 / –"

This is the balance-sheet note carrying the loan; Pass 1 anchored the loan
only via the RPT note and the fair-value hierarchy line, not this primary
note. Two points Pass 1 did not draw out:
- The balance is classified CURRENT, not non-current — management expects
  recovery within 12 months of the 31-Mar-2026 balance sheet date, i.e., by
  roughly March 2027. This is consistent with CARO's "repayment schedule...
  stipulated" language (NF-1) and is the closest the AR comes to disclosing
  a tenure.
- The note label is generic ("Loans recoverable in cash," no counterparty
  named) — the Vishkul name only appears in the RPT note (36/37) and the
  CARO annexure (NF-1), not in the primary financial-asset note itself.

Rating: 🟡 Watch — new anchor, partially resolves the "repayment terms"
open item (current classification implies ~12-month expected recovery);
the specific rate and maturity date remain undisclosed anywhere in the AR.

## NF-3. Note 39, Standalone, "Fair value hierarchy" (p.99-100) — the loan
sits in an undifferentiated Level 3 bucket

Verbatim: under "Level 3 / Financial assets measured at amortized cost,"
the table lists "Loans: 1,000.00 [Mar-26] / – [Mar-25]" alongside trade
receivables, other non-current/current financial assets, and cash/bank
balances — all lumped as Level 3 with no line-item-specific valuation
commentary. By contrast, the same note gives security deposits a specific
methodology note ("calculated based on cash flows discounted using a
current lending rate... classified as level 3... due to the inclusion of
unobservable inputs including own and counterparty credit risk"). No
equivalent counterparty-credit-risk commentary is given for the ₹1,000 lakh
related-party loan specifically. 🟡 Watch — a new-this-year, unsecured,
related-party Level 3 asset receives less risk-specific disclosure than a
routine security deposit in the same note.

## NF-4. Note 37 Standalone RPT (p.97-99) vs Note 36 Consolidated RPT
(p.150-151) — KMP remuneration cross-set mismatches wider than Pass 1
characterised, plus two new classification points

Re-reading Note 37 Standalone in full against Pass 1's Consolidated table
(reproduced in Pass 1 LBF-4) surfaces gaps Pass 1 did not size correctly:

| KMP | FY25 Standalone (Note 37, p.97-98) | FY25 Consolidated (Pass 1 table) | Gap |
|---|---|---|---|
| Mr. Salil Baldevraj Taneja, Director Remuneration | ₹368.80 lakh | ₹344.60 lakh | ₹24.20 lakh — new, Pass 1 did not flag this pair at all |
| Mr. Sudishkumar Kuttappan Nair, Remuneration | ₹31.75 lakh | ₹17.58 lakh | ₹14.17 lakh — Pass 1 called this "a few days/lakh"; it is materially larger |
| Ms. Priya Chouksey (up to 30-09-2024) | ₹2.63 lakh | ₹4.14 lakh | ₹1.51 lakh, opposite direction |
| Mr. Aditya Oza | ₹1.88 lakh | not shown / blank in Pass 1's Consolidated table | new gap Pass 1 missed entirely — standalone books show FY25 pay, the consolidated note shows none |

FY26 figures agree exactly across both note sets for every KMP line. Only
the FY25 comparatives diverge, and by more than Pass 1's language ("a few
lakh") conveyed for the items it did catch, plus one pair (Mr Oza) it
missed outright.

Two further new points from the same note:
- Mr. Salil Baldevraj Taneja's KMP designation in the Standalone note is
  given as "Chairman and Managing Director (w.e.f 05-08-2025)" (p.98) — a
  mid-year effective date for the Chairman & MD designation, not mentioned
  in Pass 1.
- Vishkul Enterprises Pvt Ltd is captioned as "Holding company" in part (A)
  of the note (naming related parties) but its transactions are listed
  under the sub-heading "Entities under common control" in part (B) (the
  transaction table) — an internal classification inconsistency within the
  same note (p.97, p.99). Minor disclosure-hygiene point, not previously
  flagged.

Rating: 🟡 Watch — this widens (does not create) an issue Pass 1 already
rated Watch; the standalone-vs-consolidated KMP remuneration gaps are
larger and more numerous than Pass 1's summary suggested.

## NF-5. Directors' Report, "Particulars of Loans, Guarantees and
Investments" (p.35) — a cross-reference that points nowhere specific

Verbatim: "Particulars of Loans, Guarantees & Investments covered under
Section 186 of the Act has been given in Notes to Financial Statements
forming part of this Annual Report." No note in either note set is
separately headed as a Section 186 particulars disclosure. The only places
the loan's Section 186 character is actually evidenced are the CARO
annexure (NF-1) and the generic Note 13/RPT entries (NF-2, and Pass 1's
LBF-4). 🟡 Watch — the cross-reference is satisfied in substance (the
amount is disclosed) but there is no note presenting the statutory
particulars (rate of interest, purpose) that a Section 186(4)-style
disclosure would normally carry as a distinct block.

## NF-6. AGM Notice, Item 5 (p.4-5, p.20) — the Section 186 limit increase
is prospective, not the approval basis for the Vishkul loan

Special resolution, Item 5: the Board (meeting held 10-Feb-2026) sought
shareholder approval to raise the aggregate Section 186 loan/investment/
guarantee limit from ₹250 crore to ₹350 crore, "over and above the
permissible limits under Section 186(2)." This is FORWARD-LOOKING headroom
for future transactions, not a retrospective or transaction-specific
approval of the Vishkul loan. Since the Vishkul ICD carries a near-full-year
interest balance (Pass 1's arithmetic implies an early-FY26 disbursement,
i.e., before this Feb-2026 board meeting), the loan was made under the
company's pre-existing, standing Section 186 shareholder mandate (the prior
₹250 crore omnibus limit), not under any new or loan-specific resolution.
🟢 Clean/procedural — this resolves the "board approval" question in the
open item: there is a standing omnibus authority, no evidence of a
transaction-specific board minute or Audit Committee RPT approval citation
for this loan by name anywhere in the AR (see ESCALATION).

═══════════════════════════════════════════════════════════════
ESCALATION — WHAT PASS 1 LEFT OPEN, STATUS AFTER THIS (INCOMPLETE) PASS
═══════════════════════════════════════════════════════════════

1. **Note 41 PBT reconciliation (which figure is right).** NOT ADDITIONALLY
   RESOLVED — the mechanical failure hit before I re-opened Note 41 in the
   source text to trace the arithmetic line by line. Pass 1 already quoted
   both figures in full (Note 41(b)-(d) Consolidated "summarised P&L of
   TTL" shows Revenue ₹19,010.10 lakh / Other Income ₹1,851.18 lakh / PBT
   ₹11,672.94 lakh / PAT ₹10,071.52 lakh, against the audited Consolidated
   PBT ₹7,436.21 lakh and audited Standalone PBT ₹6,976.49 lakh). Reasoned
   inference from what Pass 1 already quoted, NOT a freshly confirmed
   finding: the error most plausibly sits IN THE NOTE, not in either
   primary statement, because (a) both primary PBT figures independently
   tie to the audited Results_Q4FY26 filing per Pass 1's LBF-1 cross-check,
   and (b) the note's own construction is internally inconsistent — it
   takes Standalone Revenue and Standalone Other Income but strips the
   intercompany "Cost of technical services" out of Total Expenses as if
   consolidation elimination had already occurred, which double-counts the
   elimination against unconsolidated top-line figures. This is an
   inference from Pass 1's quotes, not a re-verified primary-source
   finding — flagged as ESCALATED, not closed.

2. **Unbilled revenue vs Q4FY26/Q1FY27 quarterly acceleration.** NOT
   COMPLETED. `results__Results_Q4FY26_Mar_2026.txt` and
   `results__Results_Q1FY27_Jun_2026.txt` were never opened before file
   access was lost. The cross-check the task brief asked for (whether the
   unbilled-revenue build from ₹4.64cr to ₹13.75cr is consistent with the
   ₹45.79cr → ₹57.04cr → ₹64.81cr quarterly revenue acceleration cited in
   the brief) is UNRESOLVED. NOT FOUND / NOT COMPLETED — not estimated.

3. **The Vishkul ICD — board approval, Section 186, Audit Committee,
   repayment terms, cash flow statement.** PARTIALLY RESOLVED this pass:
   - Board/shareholder approval basis: standing Section 186 omnibus
     mandate (pre-existing ₹250 crore limit), not a loan-specific
     resolution (NF-6).
   - Section 186 disclosure: present in substance via CARO (NF-1) and
     Note 13 (NF-2); the Directors' Report's specific cross-reference to a
     dedicated Section 186 note does not resolve to any such note (NF-5).
   - Repayment terms: a schedule is confirmed to exist and be current per
     CARO (NF-1); the CURRENT balance-sheet classification implies
     recovery within 12 months (NF-2); the specific rate (only the
     implied ~9.85% from Pass 1's income/balance arithmetic) and exact
     maturity date are NOT FOUND anywhere in the AR.
   - Audit Committee-specific RPT approval citation (SEBI LODR Regulation
     23): NOT COMPLETED — I had not reached a targeted search of the
     Corporate Governance Report's Audit Committee section for an
     RPT-specific approval statement naming this loan before the failure.
   - Cash flow statement tie-out (does the ₹1,000 lakh appear under
     investing activities as "loans given to related party," and does the
     ₹98.55 lakh interest appear under operating or investing activities):
     NOT COMPLETED — the Cash Flow Statement was never re-opened in this
     pass.

4. **The ₹91.78 lakh direct credit to Retained Earnings.** NOT
   ADDITIONALLY RESOLVED. I had queued a full read of the Statement of
   Changes in Equity (Consolidated, p.117) and Note 17(d), together with
   the NCLT-merger restatement notes (Note 1/48, both sets), to test
   whether the ₹91.78 lakh ties to a merger-accounting adjustment arising
   from the TAAL Tech India Pvt Ltd pooling-of-interests restatement
   (plausible given the appointed-date-1-Apr-2023 retrospective merger
   accounting Pass 1 already documented) — but this was not reached before
   the failure. This is a HYPOTHESIS carried over from reasoning about
   Pass 1's own findings, not a confirmed source-anchored finding. Cause
   remains NOT FOUND IN DOCUMENT as verified fact.

5. **The mislabeled "summarised consolidated P&L" note (Note 41).** Same
   underlying item as #1. Pass 1's characterisation — that it is in
   substance a hybrid of Standalone revenue/other-income figures with a
   consolidated-style expense adjustment, and that a downstream reader
   taking its PBT/PAT figures as the audited consolidated numbers would be
   misled — stands as the operative answer. This pass did not add further
   primary-source confirmation before the failure.

═══════════════════════════════════════════════════════════════
PASS 2 NEW FINDINGS SUMMARY
═══════════════════════════════════════════════════════════════

This is NOT "PASS 2: NO MATERIAL NEW FINDINGS" — six new, source-anchored
findings were confirmed (NF-1 through NF-6) before the source corpus became
inaccessible. The sweep is INCOMPLETE, not exhaustive: it did not reach a
second full pass over every note Pass 1 already covered, and five items the
task brief specifically asked Pass 2 to resolve remain partially or fully
open, listed above under ESCALATION with their exact status.

| # | Finding | Anchor | Rating |
|---|---|---|---|
| NF-1 | CARO Annexure A clause 3(iii)(d) contradicts clause 3(iii)(a) on whether any loan was given during the year; clause (c) confirms a stipulated repayment schedule for the Vishkul loan | Independent Auditor's Report, Annexure A, clause 3(iii), p.60-61 | 🔴 |
| NF-2 | Vishkul ICD sits in Note 13 Standalone as "Current financial assets – Loans," classified CURRENT (implies ~12-month recovery), generic label, no counterparty name in the note itself | Note 13, Standalone, p.85 | 🟡 |
| NF-3 | The ₹1,000 lakh loan is Level 3 fair value with no counterparty-credit-risk-specific commentary, unlike security deposits in the same note | Note 39, Standalone, p.99-100 | 🟡 |
| NF-4 | Standalone-vs-Consolidated FY25 KMP remuneration gaps are wider and more numerous than Pass 1 characterised (Taneja ₹24.20 lakh gap missed entirely; Oza pair missed entirely); Vishkul is "Holding company" in (A) but "Entities under common control" in (B) of the same note | Note 37 Standalone p.97-99 / Note 36 Consolidated p.150-151 | 🟡 |
| NF-5 | Directors' Report cites a Section 186 particulars note that does not exist under any distinct heading | Directors' Report, p.35 | 🟡 |
| NF-6 | AGM Item 5's Section 186 limit increase (₹250cr→₹350cr) is prospective and unrelated to the Vishkul loan, which used the pre-existing standing mandate | AGM Notice, Item 5, p.4-5, p.20 | 🟢 |

END OF PASS 2 (INCOMPLETE — mechanical failure; see notice above).
