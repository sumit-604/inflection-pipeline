# Notion payload — SYNGENE Q2 FY27 review (NOT WRITTEN; for operator approval)

Batch standing instruction 6: this session does not write to Notion. The write gate (operator ruling 2026-10-03) needs the operator's explicit approval of this payload. Decision Status is never written.

## Target
- Database: COMPANIES MASTER (collection://345bb2b9-d3ab-8032-9b46-000ba16ab827)
- Page: Syngene International Ltd, id 3e9bb2b9-d3ab-8168-afd5-ca86954e8113 (https://app.notion.com/p/3e9bb2b9d3ab8168afd5ca86954e8113)
- Page state at fetch (28-Oct-2026): Decision Status blank; Analysis Date 2026-10-20; Current Market Price 386. Snapshot: runs/syngene-q2fy27/work/notion_snapshot_2026-10-28.md.

## 1. update_properties (PREPEND to Key Notes; keep every prior entry after a " | " separator)

Key Notes prefix, exact text (A4 Step 9 line with the two qualifiers A5 asked for at L1-S5, taken from the review body Step 2 and Step 6B; no number changed):

```
28-Oct-2026 | Q2 FY27 [FILED, no transcript]: rev Rs 832.7 Cr (-8.6% YoY; above Rs 790 Cr base path on reported revenue, cash not confirming: H1 other current liabilities -Rs 313.4 Cr); op margin 17.7% (ex-FX 25.1%; H1 ex-FX ~18.1% if Bayview pre-op Rs 66.1 Cr were expensed); H1 CFO -Rs 143.2 Cr, T3 FIRED; Bayview first contract (unnamed), DS manufacturing FY28, T4 FIRED (conservative, contested); CFO + Head Strategy + both discovery heads leaving; research split not filed (R2/T1 untestable). No re-engage trigger. A5 COMPLETE after 1 loop. Decision Status unchanged (operator-only).
```

Other properties: none. Do not write Decision Status. Promoter Verdict unchanged (CONCERN, structure). Analysis Date and Current Market Price: operator's call (CMP Rs 411, screener.in 28-Oct-2026 08:48 IST).

## 2. insert_content (position: end), in this order, split across sequential calls as needed

Heading: `## Q2 FY27 Results Review (filed documents only), 28-Oct-2026`

1. The full A4 review, complete tables, never summarised: runs/syngene-q2fy27/work/review_syngene_q2fy27.md, from the title line through the end of the CORRECTION LOOP 1 table (leave out the closing YAML block). It ends with the PLAIN-LANGUAGE BRIEF and the forward map; both are part of the save. Escape `|` inside table cells as `\|`.
2. A3 forensics tables (completeness proof): the F1-F17 status table and findings table from each of
   - runs/syngene-q2fy27/work/forensics_syngene_q2fy27_results.md (A3-01 to A3-16)
   - runs/syngene-q2fy27/work/forensics_syngene_q2fy27_presentation.md (A3P-01 to A3P-17)
   - runs/syngene-q2fy27/work/forensics_syngene_q2fy27_pressrelease.md (A3R-01 to A3R-26)
3. A5 audit verdict block, exact text:

```
A5 ADVERSARY (Opus 5.5), loop 1 of 1: COMPLETE (style notes only).
Loop 0: INCOMPLETE, 3 FACTUAL (F1 Q1 tax pair, F2 Note 4 impact, F3 CTS lab commissioned), 4 MISSING (M1 resignation-letter date, M2 ex-FX margin flattered by Bayview pre-op, M3 revenue GREEN needs cash qualifier, M4 Bayview acquisition probe), 2 CONTRADICTION (C1 CDMO share status, C2 TTM PAT 184.2 vs 186.1). All nine fixed by A4; no drift outside the patches.
Coverage: structured IDs results 828, deck 350, press release 879, disclosure 71; orphans none. Arithmetic: 62 metric groups recomputed.
Open STYLE notes: loop-0 S1-S6; loop-1 L1-S1 to L1-S7 (audit file runs/syngene-q2fy27/work/audit_syngene_q2fy27.md).
```

## 3. Proposed DOWNSTREAM SIGNAL TRACKER rows
A4 Step 5.5C proposes two new tracker-signal payload rows (review Step 5.5C). They are not written. Tracker rows for SYNGENE exist in Notion (for example "SYNGENE R2/T1: Quarterly research revenue run-rate", "SYNGENE T7: Biocon stake sale") but were not supplied to this run, so Step 5.5A reads "tracker rows not supplied".

## Flags for the operator (Decision Status untouched)
- T3 FIRED: H1 FY27 CFO -Rs 143.2 Cr against a threshold of 70% x Rs 238.2 Cr operating EBITDA = Rs 166.7 Cr (res l.226). H1 FY26 was also negative (-Rs 45.1 Cr).
- T4 FIRED on the conservative reading, contested: "drug substance manufacturing at Bayview expected to begin in the next financial year" = FY28 (PR L159-161). Separating observation: the call transcript (~6-Nov-2026) and whether Bayview CWIP Rs 487.6 Cr moves to PPE by 31-Mar-2027.
- No re-engage trigger fired (R1 not fired: customer unnamed and scale unstated; R2 untestable; R3 not fired).
