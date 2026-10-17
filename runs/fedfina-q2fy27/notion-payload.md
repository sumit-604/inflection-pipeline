# Notion payload: FEDFINA Q2 FY27 (NOT WRITTEN; awaiting operator batch approval)

Write gate (operator ruling 2026-10-03): nothing below has been written to Notion. Per the operator's 2026-10-17 instruction, this run did not wait at the gate; the operator approves all writes later in one batch. Decision Status is NEVER written by this pipeline.

## Target page
- COMPANIES MASTER page: Fedbank Financial Services Ltd (FEDFINA)
- Page ID: 39fbb2b9-d3ab-81d9-b09d-dd45266d56c2
- URL: https://app.notion.com/p/39fbb2b9d3ab81d9b09ddd45266d56c2
- Page last edited (at fetch): 2026-09-30T02:06:31Z. Re-fetch before writing; if edited since, re-check the Key Notes prefix.

## 1. update_properties
- Key Notes: PREPEND the line below, then the separator ` \| `, then the existing Key Notes text unchanged. Pipes inside the line are already escaped as `\|`.

```
2026-10-17 Q2 FY27 (results + deck + release, /run-quarterly A1-A5; A5 INCOMPLETE after 2 loops on one wording item F5, carried open; no third loop per operator ruling): PROCEED WITH FLAGS. PAT Rs 130.75 Cr (+63.1% YoY), ROE 17.0%, ROA 2.8%, C/I 52.5%; AUM Rs 22,035 Cr (+36.6%). No tripwire fired: credit cost 0.6%, ROE > 14%, PCR 35.37% > 32%. FLAG: PCR 38.36% -> 35.37% and GNPA 1.55% -> 1.82% while impairment fell 20.5% QoQ; stressed (Stage 2+3) coverage 24.5% -> 20.2%; Stage 2 +34.6% QoQ. Pillar 2L self-withdraw condition ("PCR thins further") MET on the QoQ baseline, NOT on the FY26 baseline (32.29%): operator to rule. Growth off-book-led (AUF +Rs 27 Cr vs AUM +Rs 899 Cr; gold AUF -Rs 52 Cr) and gold-price-led (tonnage +1.6% QoQ vs gold AUM +6.5%); gold guide +25-30% AT RISK, needs ~14.0 t FY27 tonnage vs +2.4% in H1. Deck sell-down Rs 1,085 Cr vs filed DA Rs 876.89 Cr unreconciled. D/E 4.61x vs 6x NCD cap; leverage 5.0x -> 6.0x drives ~half the ROE gain. Q2 basic EPS 3.56 printed vs 3.49 derived. Entry zone max Rs 77 now below BVPS Rs 84.4 (Role 1). 31 management questions logged. Decision Status unchanged (operator-only).
```

- Analysis Date 1: 2026-10-17
- Decision Status: NOT WRITTEN (proposed: no change, WATCHLIST / AVOID; the Pillar 2L condition is flagged for the operator, not decided).
- Entry Price Max / Margin of Safety Price: NOT CHANGED (Role 1 recompute deferred under OR-30).
- Properties flagged stale for the operator to refresh: Current Market Price (164); gold mix in page text (~46.5%; Q2 54.1%, Deck R315); secured share (98.9%; Q2 99.4%, Deck R064).

## 2. insert_content (position: end), as a new section headed
"## Q2 FY27 — Quarterly Review (extraction-first pipeline, results + presentation + press release) — 17-Oct-2026"

Insert in sequential calls, verbatim, complete tables (never summaries), pipes in cells escaped as `\|`:
1. runs/fedfina-q2fy27/work/review_fedfina_q2fy27.md, in full (824 lines; includes the PLAIN-LANGUAGE BRIEF and the OPEN ITEMS AT CLOSE section). Split at its `## STEP` headings.
2. A3 forensics tables (completeness proof):
   - runs/fedfina-q2fy27/work/forensics_results_fedfina_q2fy27.md (checklist scorecard and findings table)
   - runs/fedfina-q2fy27/work/forensics_presentation_fedfina_q2fy27.md (checklist scorecard and findings table)
   - runs/fedfina-q2fy27/work/forensics_pressrelease_fedfina_q2fy27.md (checklist scorecard and findings table)
3. A5 audit verdict block:

```
A5 verdict: INCOMPLETE after loop 2 of 2 (operator approved one second loop 17-Oct-2026; no third loop; close with open items flagged).
Run 1 INCOMPLETE: 3 FACTUAL, 6 MISSING, 2 CONTRADICTION; all closed in loop 1.
Loop 1 INCOMPLETE: 1 FACTUAL (trigger count), 1 CONTRADICTION (gold guide wording); both closed in loop 2.
Loop 2 INCOMPLETE: 1 FACTUAL, F5: A4 YAML note says ECL/AUF rose "only" because of Stage 1; correct wording "mainly ... (55%)". Body figures correct. Carried open.
Coverage: 752 / 1,102 / 247 rows referenced (results incl. 4 loop-1 rows), no orphans. Arithmetic: no other mismatch.
Open STYLE notes (no loop): S7-S10, S12-S14.
No finding in any round changed the protocol verdict (PROCEED WITH FLAGS) or the proposed Decision Status (no change).
```

## 3. DOWNSTREAM SIGNAL TRACKER candidates (payload only; operator-approval gate)
Tracker rows were not supplied to this run (Step 5.5). The three new signal candidates A4 lists in review section "STEP 5.5 DOWNSTREAM SIGNAL RECONCILIATION" are payload only. Create them via Role 5.5 in claude.ai if the operator approves.

## Operator items carried
1. Pillar 2L baseline ruling: "PCR thins further" is met QoQ (38.36% -> 35.37%) but not against FY26 (32.29%). The clause names no baseline.
2. Credit-cost basis in Notion: FY26 ~0.64% is on average AUM; the tripwire is on average assets (company FY26 figure on that basis 0.8%).
3. Prior question unit error: Q1 question 8 cites "~585cr" FVOCI loss; the filing shows Rs 58.51 Cr.
4. Notion monitoring item 3 ("gold branch count 140-150") matches nothing in the deck (706 gold branches); restate the checklist item.
5. Open A5 item F5 (wording only), above.
6. Concall held mid-October; transcript not in this run. Grade the 31 questions against it when filed.
