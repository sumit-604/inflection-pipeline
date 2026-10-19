# Notion payload: FEDFINA Q2 FY27 (NOT WRITTEN; awaiting operator batch approval; updated 2026-10-19 with Role 5)

Write gate (operator ruling 2026-10-03): nothing below has been written to Notion. Per the operator's 2026-10-17 instruction, this run did not wait at the gate; the operator approves all writes later in one batch. Decision Status is NEVER written by this pipeline.

## Target page
- COMPANIES MASTER page: Fedbank Financial Services Ltd (FEDFINA)
- Page ID: 39fbb2b9-d3ab-81d9-b09d-dd45266d56c2
- URL: https://app.notion.com/p/39fbb2b9d3ab81d9b09ddd45266d56c2
- Page last edited (at fetch): 2026-09-30T02:06:31Z. Re-fetch before writing; if edited since, re-check the Key Notes prefix.

## 1. update_properties
- Key Notes: PREPEND the line below, then the separator ` \| `, then the existing Key Notes text unchanged. Pipes inside the line are already escaped as `\|`.

```
2026-10-19 Q2 FY27 results + call (results, deck, release and call ASR transcript; /run-quarterly A1-A5; Role 4 A5 INCOMPLETE after 2 loops on one wording item later fixed; Role 5 A5 COMPLETE after 2 loops): PROCEED WITH FLAGS. PAT Rs 130.75 Cr (+63.1% YoY), ROE 17.0%, ROA 2.8%, C/I 52.5%; AUM Rs 22,035 Cr (+36.6%). No tripwire fired: credit cost 0.6% of avg assets, ROE > 14%, PCR 35.37% > 32%. FLAG: PCR 38.36% -> 35.37% and GNPA 1.55% -> 1.82% while impairment fell 20.5% QoQ; stressed (Stage 2+3) coverage 24.5% -> 20.2%; Stage 2 +34.6% QoQ; call blames gold bullet-to-periodic interest change, gives no product split. Call kept credit cost 'way below 1%', GNPA below 2%, AUM +20-25% at flat gold, ROA 3% 'sooner'; declined numbers on Stage 2 peak, gold yield and ST LAP; signalled NIM pressure from rate hikes and an insurance-income headwind. Record Rs 1,085 Cr sell-down against a stated aim to 'reduce reliance on DA'; CFO ~Rs 700 Cr gold DA vs filed Rs 876.89 Cr. Gold guide +25-30% AT RISK (needs ~14.0 t FY27 tonnage vs +2.4% H1). D/E 4.61x vs 6x NCD cap; H1 net de-leverage nil. Q2 basic EPS 3.56 printed vs 3.49 derived. Credibility ratio ND. OPERATOR RULINGS OPEN: Pillar 2L 'PCR thins further' baseline (met QoQ, not vs FY26); credit-cost tripwire basis. Entry zone max Rs 77 below BVPS Rs 84.4 (Role 1). 47 management questions logged. Decision Status unchanged (operator-only).
```

- Analysis Date 1: 2026-10-19
- Decision Status: NOT WRITTEN (proposed: no change, WATCHLIST / AVOID; the Pillar 2L condition is flagged for the operator, not decided).
- Entry Price Max / Margin of Safety Price: NOT CHANGED (Role 1 recompute deferred under OR-30).
- Properties flagged stale for the operator to refresh: Current Market Price (164); gold mix in page text (~46.5%; Q2 54.1%, Deck R315); secured share (98.9%; Q2 99.4%, Deck R064).

## 2. insert_content (position: end), as a new section headed
"## Q2 FY27 — Quarterly Review (extraction-first pipeline, results + presentation + press release) — 17-Oct-2026"

Insert in sequential calls, verbatim, complete tables (never summaries), pipes in cells escaped as `\|`:
1. runs/fedfina-q2fy27/work/review_fedfina_q2fy27.md, in full (1,505 lines; Role 4 steps, then the ROLE 5 CONCALL ANALYSIS section saved under the sub-heading "Q2 FY27 Concall Analysis", then monitorables, verdict and the PLAIN-LANGUAGE BRIEF). Split at its `## STEP` and `### R5 STEP` headings. The change-log sections at the end may be omitted from Notion.
2. A3 forensics tables (completeness proof):
   - runs/fedfina-q2fy27/work/forensics_results_fedfina_q2fy27.md (checklist scorecard and findings table)
   - runs/fedfina-q2fy27/work/forensics_presentation_fedfina_q2fy27.md (checklist scorecard and findings table)
   - runs/fedfina-q2fy27/work/forensics_pressrelease_fedfina_q2fy27.md (checklist scorecard and findings table)
   - runs/fedfina-q2fy27/work/forensics_concall_fedfina_q2fy27.md (checklist scorecard, findings table, commitment register C01-C26)
3. A5 audit verdict block:

```
A5 verdict, Role 5 concall (audit work/audit_concall_fedfina_q2fy27.md): COMPLETE after loop 2 of 2 (operator standing rule 17-Oct-2026).
Run 1 INCOMPLETE: A2 1 FACTUAL + 3 MISSING (21 units added, mixed turns flagged, 26 question turns); A4 2 FACTUAL, 3 CONTRADICTION, 6 MISSING (incl. ex-DA spread narrowed 13-20 bps; breakeven price-assisted; one holder-analyst). All closed in loop 1.
Loop 1 INCOMPLETE: 1 CONTRADICTION (C7, slab-cap LTV sentence, from A5's own note). Closed in loop 2.
Source caveat: concall is a machine (ASR) transcript of company audio; 52 of 74 turns speaker-inferred; auction-loss negation (L420) garbled.
Open STYLE notes: S13, S23, S25, S28, S29, S7-S10, S12.

A5 verdict, Role 4 filings: INCOMPLETE after loop 2 of 2 (operator approved one second loop 17-Oct-2026; no third loop; close with open items flagged).
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
5. Role 4 open item F5 (wording only) was fixed in the Role 5 merge (2026-10-19).
6. The call was transcribed locally from company audio (ASR). When the company files its official transcript, check the figures the review takes from the call (the auction-loss sentence L420 and the ROE target L736 are garbled).
