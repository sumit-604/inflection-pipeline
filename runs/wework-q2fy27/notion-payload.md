# Notion payload: WEWORK Q2 FY27 quarterly review (NOT WRITTEN; awaiting operator approval)

Status: not sent. Batch standing instruction 6 (28-Oct-2026) says no Notion write in this session. The orchestrator write gate (operator ruling 2026-10-03) needs explicit operator approval in the run. This file is the payload for that approval. Execute it from claude.ai or an approved session.

Pre-write check done 28-Oct-2026 (read only): COMPANIES MASTER (data source `collection://345bb2b9-d3ab-8032-9b46-000ba16ab827`) holds NO WeWork page. Searches "WeWork India" and "WEWORK Wework India Management" returned none. So this payload CREATES a new row. Re-search before writing, in case a page was added since.

## Step 1. Create the page (one row in COMPANIES MASTER)

Parent: data source `collection://345bb2b9-d3ab-8032-9b46-000ba16ab827`

Properties (exact names from the live schema):

| Property | Type | Value |
|---|---|---|
| Name | title | WeWork India Management Ltd (WEWORK) |
| Ticker | text | WEWORK |
| Sector | text | Flexible workspace (office lessee and operator) |
| SECTOR | select | Other |
| Current Market Price | number | 641 |
| Analysis Date | text | 28-Oct-2026 |
| date:Analysis Date 1:start | date | 2026-10-28 |
| Key Notes | text | (line below) |
| Decision Status | select | DO NOT WRITE. Leave empty. The operator sets it. |

Key Notes line (first entry; no prior audit trail exists):

```
28-Oct-2026 Q2 FY27 quarterly review (pre-thesis read, /run-quarterly): PROCEED WITH FLAGS; A5 COMPLETE after 1 loop. Rev from ops +33.6% YoY to Rs 767.8 Cr [FILED]; desks 145.3k, members 121.7k, occupancy 83.7% (-114 bps QoQ) [MGMT]. Headline IGAAP-eq PAT Rs 65.8 Cr is untaxed; audited Ind AS PAT Rs 20.4 Cr, of which OI+FI Rs 18.6 Cr; core PBT ex OI/FI about Rs 1.0 Cr. Net cash 23.1 Cr, ROCE 34.5% and order-book cover do not rebuild from filings; FCFF 16.0 Cr excludes Rs 20.0 Cr lease cash. Lease liabilities Rs 5,233 Cr (15.3x equity); DTA 90% of equity. Call (ASR): ~7-year large customer exits to own campus FY28; Q1 pledge release not delivered. Next: Q3 occupancy by 14-Feb-2027 (bull >=85.0%, bear <=82.5%). No thesis on record; no trigger fired. Run: runs/wework-q2fy27 (commit in hand-over note).
```

No pre-committed trigger fired: there is no thesis, tripwire or trigger on record for this name.

## Step 2. Page content (insert_content, position: end, sequential inserts)

Insert these repo files verbatim, in this order. Complete tables, never summaries. Escape `|` inside table cells as `\|` where Notion needs it. Split large files across sequential inserts.

1. `runs/wework-q2fy27/work/review_wework_q2fy27.md`: the full A4 merged review (loop 1), Sections A, B, C, the Questions-for-Management table, monitorables, and the PLAIN-LANGUAGE BRIEF (summary narrative, sector, business model, competition, forward map). The brief is part of the review and is saved with it. The "Loop 1 change log" annex may be included or left out.
2. A3 forensics tables, one per document, verbatim:
   - `runs/wework-q2fy27/work/forensics_results_wework_q2fy27.md`
   - `runs/wework-q2fy27/work/forensics_deck_wework_q2fy27.md`
   - `runs/wework-q2fy27/work/forensics_letter_wework_q2fy27.md`
   - `runs/wework-q2fy27/work/forensics_press_wework_q2fy27.md`
   - `runs/wework-q2fy27/work/forensics_concall_wework_q2fy27.md`
3. A5 audit verdict: `runs/wework-q2fy27/work/audit_wework_q2fy27.md` (re-audit, COMPLETE; loop-0 audit at `audit_wework_q2fy27_loop0.md` for the record).
4. Optional: `runs/wework-q2fy27/operator-brief.md` (indicative FY27E / FY28E and forward PE; not a Role 1 valuation).

Header block to put above item 1:

```
Q2 FY27 MERGED QUARTERLY REVIEW (RESULTS + DECK + SHAREHOLDERS' LETTER + PRESS RELEASE + CONCALL ASR), WeWork India Management Ltd (WEWORK)
Run: /run-quarterly, 28-Oct-2026, runs/wework-q2fy27. Pre-thesis read: no prior Notion page, no Spear line.
Verdict: PROCEED WITH FLAGS. A5: COMPLETE after 1 correction loop.
Concall source is a machine transcript (faster-whisper small.en); every call number is management tier and unverified.
```

## What this payload does not do

- It does not set Decision Status, Entry Price Max, Margin of Safety Price or Position Size.
- It does not link Downstream Signals rows. Tracker rows were not supplied this run.
- It does not run any valuation. Steps 6.5, 7 and 8D are deferred to /fttcp and Role 1 (OR-30).
