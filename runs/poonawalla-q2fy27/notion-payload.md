# Notion payload: POONAWALLA Q2 FY27 (NOT WRITTEN; awaiting operator approval)

Write gate (operator ruling 2026-10-03): nothing below has been written to Notion. This run did not wait at the gate (parent-session brief, 2026-10-17); the operator approves all writes later. Decision Status is NEVER written by this pipeline.

## Target page
- COMPANIES MASTER: NO PAGE EXISTS for Poonawalla Fincorp Limited. Live search 2026-10-17: "Poonawalla" 0 hits; "Poonawalla Fincorp" 1 hit (Aye Finance Limited, matched on "Muthoot Fincorp" only).
- COMPANIES MASTER data source: collection://345bb2b9-d3ab-8032-9b46-000ba16ab827
- Action needed: the operator decides whether to CREATE a COMPANIES MASTER row for this name. This is a PRE-THESIS READ; there is no spear line and no companies/POONAWALLA.md. If the operator declines page creation, file this review under the run folder only.

## 1. create page (only if the operator approves page creation), properties
- Name: Poonawalla Fincorp Limited (POONAWALLA; NSE POONAWALLA, BSE 524000)
- Key Notes (first entry; escape `|` as `\|`):

```
17-Oct-2026 \| PRE-THESIS READ Q2 FY27 (results + concall + deck + release, /run-quarterly A1-A5; A5 INCOMPLETE after loop 1, 4 open items, closed without loop 2): PAT Rs374.85 Cr (+21.8% QoQ, +405.2% YoY), S = C on P&L, no DA gain in Q2 (Q1 Rs50.93 Cr). Core PBT +41.7% QoQ, about +31.0% at Q1 credit-cost ratio. Credit cost 2.19% vs 2.40% but rupees flat (373.33 to 375.70) while AUM +10.4% QoQ to Rs74,008 Cr: denominator-led. Stage 2 PCR 23.63% to 14.61% over 4 quarters. Write-offs undisclosed. GNPA 1.20% GREEN on ratio, AMBER-CONDITIONAL: Rs161.60 Cr stressed principal to ARCs in Q2, classification ND. D/E 3.82x to 4.30x one quarter after Rs2,500 Cr QIP; RoE ~11%. Joint-auditor change after 17-Jul-2026, reason ND. Rs83.92 Cr written-off pool sale: P&L line NOT FOUND. Cash conversion INDETERMINATE-WITH-DIRECTION. Protocol verdict PROCEED WITH FLAGS. Decision Status not set (operator-only). 27 IR questions logged.
```

- Analysis Date 1: 2026-10-17
- Decision Status: NOT WRITTEN (no status on record; operator decides whether to open /step1).
- Entry Price Max / Margin of Safety Price: NOT WRITTEN (no Role 1 run).

## 2. insert_content (position: end), as a new section headed
"## Q2 FY27 — Quarterly Review (extraction-first pipeline, results + concall + presentation + press release) — 17-Oct-2026 — PRE-THESIS READ"

Insert in sequential calls, verbatim, complete tables (never summaries), pipes in cells escaped as `\|`:
1. runs/poonawalla-q2fy27/work/review_poonawalla_q2fy27.md, in full (977 lines; ends with the PLAIN-LANGUAGE BRIEF and the A4 YAML block). Split at its `## STEP` and `# SECTION` headings.
2. A3 forensics tables (completeness proof), checklist table and findings table from each:
   - runs/poonawalla-q2fy27/work/forensics_results_poonawalla_q2fy27.md
   - runs/poonawalla-q2fy27/work/forensics_concall_poonawalla_q2fy27.md
   - runs/poonawalla-q2fy27/work/forensics_presentation_poonawalla_q2fy27.md
   - runs/poonawalla-q2fy27/work/forensics_pressrelease_poonawalla_q2fy27.md
3. A5 audit verdict block:

```
A5 verdict: INCOMPLETE after loop 1 of 1. No loop 2 (no operator approval given in this session). Closed with open items flagged.
Run 1 INCOMPLETE: 3 FACTUAL (F1-F3), 4 MISSING (M1-M4), 0 CONTRADICTION, 3 STYLE. All 7 closed in loop 1 (confirmed by re-audit).
Loop-1 re-audit INCOMPLETE: 2 MISSING, 2 FACTUAL, 0 CONTRADICTION, 4 STYLE. OPEN, not grafted:
- ML1-1 (MISSING): note 11(c) gives Q2 ARC transfers NBV 92.49 vs principal 161.60 = 42.8% cover at transfer (Q1 54.3%), near Stage 3 PCR 49.1% and ~3x Stage 2 PCR 14.6% (Res L904-906; Deck L709-718). Stage 3 reading better evidenced [INFERENCE]; pre-transfer GNPA +2.5% in rupees; like-for-like ratio 1.55% to 1.42%.
- ML1-2 (MISSING): ARC qualifier absent on NNPA (review L280, L303) and the Step 7 asset-quality pillar row (L384). If Stage 3: pre-transfer NNPA +5.9% (493.29 to 522.49); like-for-like 0.79% to 0.74%.
- FL1-1 (FACTUAL): "cross-sell income is the line exposed to the insurance-commission rule" is stated as fact; the extract does not define the line and management uses "cross-sell" for loan cross-sell (Call L244-245, L298-307). Read it as [INFERENCE]; the stated bear exposure may be lower.
- FL1-2 (FACTUAL): review L106 calls Annexure II note 3 a "column-reporting note"; the filed note says NCD book value = principal plus accrued interest (Res L1753).
Coverage: 2,386 structured IDs referenced (results 1,327, concall 287, deck 676, release 96), no orphans. Arithmetic: 0 mismatches in the re-audit.
PROCEED WITH FLAGS was not challenged in either audit round.
```

## 3. DOWNSTREAM SIGNAL TRACKER candidates (payload only; operator-approval gate)
Tracker rows were not supplied. See review STEP 5.5 for the three proposed signal candidates. Not written. Role 5.5 must open at initial workup.

## Operator items carried
- Decide: create a COMPANIES MASTER page, or keep this as a run-folder-only pre-thesis read.
- Decide: run /step1 intake for POONAWALLA, or not.
- Open A5 items ML1-1, ML1-2, FL1-1, FL1-2: read them as corrections to the review text at the cited lines. A graft pass needs your approval of a second loop.
- IR email: 27 questions in review STEP 8.5 (top 8 first).
