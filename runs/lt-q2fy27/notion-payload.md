# Notion payload: LT Q2 FY27 quarterly review (NOT WRITTEN; awaiting operator approval)

Status: not sent. Batch standing instruction 6 (28-Oct-2026) says no Notion write in this session. The orchestrator write gate (operator ruling 2026-10-03) needs explicit operator approval in the run. This file is the payload for that approval. Execute it from claude.ai or an approved session.

Pre-write check done 28-Oct-2026 (read only): COMPANIES MASTER (data source `collection://345bb2b9-d3ab-8032-9b46-000ba16ab827`) holds NO Larsen & Toubro page. Searches "Larsen & Toubro" (workspace) and "Larsen Toubro LT" (inside the data source) returned none. So this payload CREATES a new row. Re-search before writing, in case a page was added since. Property names below follow the schema used by the batch's WeWork payload; confirm them against the live schema at write time.

## Step 1. Create the page (one row in COMPANIES MASTER)

Parent: data source `collection://345bb2b9-d3ab-8032-9b46-000ba16ab827`

| Property | Type | Value |
|---|---|---|
| Name | title | Larsen & Toubro Ltd (LT) |
| Ticker | text | LT |
| Sector | text | EPC and order-book capital goods (infrastructure, energy, hi-tech manufacturing), with listed IT and financial services subsidiaries |
| SECTOR | select | Other |
| Current Market Price | number | 3801 |
| Analysis Date | text | 29-Oct-2026 |
| date:Analysis Date 1:start | date | 2026-10-29 |
| Key Notes | text | (line below) |
| Decision Status | select | DO NOT WRITE. Leave empty. The operator sets it. |

Key Notes line (first entry; no prior audit trail exists):

```
29-Oct-2026 Q2 FY27 quarterly review (pre-thesis read, /run-quarterly): PROCEED WITH FLAGS; cash conversion INDETERMINATE-WITH-DIRECTION; A5 INCOMPLETE on 1 text item (N1) after 1 loop, no verdict-card number moved. Orders Rs 1,47,665 Cr (+28%, record) [FILED], all growth in Energy-Conventional (rest -10.6% together); Middle East 51% of Q2 orders, 40% of the Rs 8,53,514 Cr book [MGMT]. Revenue +15.8% to Rs 78,750 Cr; operating EBITDA +0.6%, margin 8.7% vs 10.0% [FILED]. Owners PAT +32.5% to Rs 5,202 Cr: other income 71% of the PBT gain, deferred tax credit Rs 337 Cr, lower finance cost 22% (Hyderabad Metro perimeter up to ~17%). Segment EBITDA includes allocated other income (call, ASR). NWC 1.7% of sales rests on customer advances (balance ND); ex-FS cash before WC -3.6% H1. FY27 guide held: inflow and revenue +10-12%, PPM margin 7.8% (ASR). Hyderabad Metro sale slipped to 31-Dec-2026. Dhaka Metro order 27-Oct (Q3 inflow, Major band Rs 5,000-10,000 Cr, basis ND). Indicative FY27E/FY28E owners PAT Rs 20,009 / 21,748 Cr (Reading A), PE 26.1x / 24.0x at Rs 3,801; not a Role 1 valuation. Next: Q3 operating margin YoY (bull >= -30 bps, bear <= -100 bps). No thesis on record; no trigger fired. Run: runs/lt-q2fy27 (commit in hand-over note).
```

No pre-committed trigger fired: there is no thesis, tripwire or trigger on record for this name.

## Step 2. Page content (insert_content, position: end, sequential inserts)

Insert these repo files verbatim, in this order. Complete tables, never summaries. Escape `|` inside table cells as `\|` where Notion needs it. Split large files across sequential inserts (the review is 1,287 lines).

1. `runs/lt-q2fy27/work/review_lt_q2fy27.md`: the full A4 merged review after correction loop 1. It holds Section A (Role 4), Section B (Role 5, ASR call), Section C (combined verdict), Section D (monitorables and the Dhaka Metro order item), Section E (indicative FY27E / FY28E), the Questions-for-Management table, and the PLAIN-LANGUAGE BRIEF (summary narrative, sector, business model, competition, forward map). The brief is part of the review and is saved with it. The "CORRECTION LOOP 1" log at the top may be included or left out.
2. A3 forensics tables, one per document, verbatim:
   - `runs/lt-q2fy27/work/forensics_results_lt_q2fy27.md`
   - `runs/lt-q2fy27/work/forensics_presentation_lt_q2fy27.md`
   - `runs/lt-q2fy27/work/forensics_concall_lt_q2fy27.md`
3. A5 audit verdict: `runs/lt-q2fy27/work/audit_lt_q2fy27.md` (loop-0 audit plus the "RE-AUDIT LOOP 1" section; verdict INCOMPLETE on N1 only).
4. Optional: `runs/lt-q2fy27/operator-brief.md` (indicative FY27E / FY28E and forward PE; not a Role 1 valuation).

Header block to put above item 1:

```
Q2 FY27 MERGED QUARTERLY REVIEW (RESULTS + ANALYST PRESENTATION + CONCALL ASR + DHAKA METRO ORDER RELEASE), Larsen & Toubro Ltd (LT)
Run: /run-quarterly, 28-29 Oct 2026, runs/lt-q2fy27. Pre-thesis read: no prior Notion page, no Spear line.
Verdict: PROCEED WITH FLAGS. Cash conversion INDETERMINATE-WITH-DIRECTION. A5: INCOMPLETE on one text item (N1) after 1 correction loop; no verdict-card number moved.
Open item N1: review line 876 says standalone debt is not lower at Sep-26; filed standalone D/E 0.26 / 0.23 / 0.19 (Sep-25 / Jun-26 / Sep-26) shows it is lower YoY and QoQ, higher only vs Mar-26.
Concall source is a machine transcript (faster-whisper small.en); every call number is management tier and unverified.
```

## What this payload does not do

- It does not set Decision Status, Entry Price Max, Margin of Safety Price or Position Size.
- It does not link Downstream Signals rows. Tracker rows were not supplied this run. The review's Step 5.5C lists new signal candidates as payload only; they need Role 5.5 live verification in claude.ai.
- It does not run any valuation. Role 4 Steps 6.5 and 7 and Role 5 Step 8D are deferred to /fttcp and Role 1 (OR-30).
