# Notion payload: GMBREW Q2 FY27 (NOT WRITTEN; awaiting operator batch approval)

Write gate (operator ruling 2026-10-03): nothing below has been written to Notion. Per the operator's 2026-10-17 instruction, this run did not wait at the gate; the operator approves all writes later in one batch. Decision Status is NEVER written by this pipeline.

## Target page
- COMPANIES MASTER (collection://345bb2b9-d3ab-8032-9b46-000ba16ab827): NO PAGE EXISTS for G M Breweries Ltd.
- Live search 2026-10-17 ("G M Breweries", "GM Breweries GMBREW", "Breweries country liquor Virar", "Breweries" in COMPANIES MASTER): no match. See work/notion-thesis.md.
- No companies/GMBREW.md; no spear on record. This review is a PRE-THESIS READ.
- Operator decision needed first: create a COMPANIES MASTER row for GMBREW, or keep the review in the repo only. The spear gate (CLAUDE.md) applies before any /run-pipeline or /fttcp on this name.

## 1. create page (only if the operator approves a new row)
- Title: G M Breweries Ltd (GMBREW)
- Decision Status: NOT WRITTEN (operator-only; no status proposed by this pipeline).
- Analysis Date 1: 2026-10-17
- Key Notes (first entry; escape `|` as `\|`):

```
17-Oct-2026 \| Q2 FY27 PRE-THESIS READ (results only, /run-quarterly A1-A5, A5 COMPLETE after 2 loops) \| Net revenue (ex excise ~75% of gross) Rs213.52 Cr, +18.3% YoY; op EBITDA Rs49.91 Cr, +11.4%; op margin on net revenue 23.37%, -145 bps YoY on other expenditure +63.0% (line not split); PAT Rs39.29 Cr, +12.6%; std = consol PAT \| H1 CFO Rs95.53 Cr = 1.24x PAT (readings 1.02x-1.29x; 1.06x ex payables stretch); cash INDETERMINATE-WITH-DIRECTION; debt nil \| Investments Rs659.64 Cr + investment property Rs216.72 Cr = 68.3% of assets; 93% of H1 CFO invested; ~Rs951 Cr average non-operating book at a recognised 3.3% pre-tax \| Buildfort Infradev (shell WOS) funded Rs1.01 Cr, purpose undisclosed; consol gross-up 1.01 Cr \| CMD lease rent Rs1.49 Cr H1 with no ROU asset or lease liability \| LRR signed 10:27-10:28 IST, before the 11:30 board; LRR names quarter only \| Protocol verdict PROCEED WITH FLAGS \| Decision Status not set (operator-only) \| 14 IR questions logged.
```

## 2. insert_content (position: end), as a new section headed
"## Q2 FY27 — Quarterly Review (extraction-first pipeline, results only, PRE-THESIS READ) — 17-Oct-2026"

Insert in sequential calls, verbatim, complete tables (never summaries), pipes in cells escaped as `\|`:
1. runs/gmbrew-q2fy27/work/review_gmbrew_q2fy27.md, in full (includes the PLAIN-LANGUAGE BRIEF as its last narrative section). Split at its `## STEP` headings.
2. A3 forensics tables (completeness proof): runs/gmbrew-q2fy27/work/forensics_results_gmbrew_q2fy27.md (checklist table, findings table, LOOP 1 ADDENDUM).
3. A5 audit verdict block:

```
A5 verdict: COMPLETE (loop 2 of 2; second loop under the operator standing ruling of 17-Oct-2026).
Run 1 INCOMPLETE: 1 FACTUAL, 8 MISSING (3 orphan ledger groups, 2 rows missing from the ledger, 3 bear counters), all closed in loop 1.
Loop 1 INCOMPLETE: 1 CONTRADICTION (CFO/PAT range stated one-sided), closed in loop 2.
Coverage: 757 structured IDs referenced, no orphans; ledger rows M1-M4 added. Arithmetic: no mismatch above rounding.
Open STYLE notes (no loop): S16 capital-advance double-count reading fits the same tax/capex tie at CFO 1.24x (Q8 separates); S17 "deposits" label on 119.67 Cr of undisclosed other financial assets; S18 name the 68.3% base; S15 A2 grep label; S8 A1 RPT approval cells.
```

## 3. DOWNSTREAM SIGNAL TRACKER candidates (payload only; operator-approval gate)
See review section STEP 5.5C: two candidate signals (Maharashtra excise regime; spirit input price). Tracker rows were not supplied; Role 5.5 has never run for this name. Not written.

## Operator items carried
- Decide whether GMBREW gets a COMPANIES MASTER row and a spear pass (/step1) before any thesis work.
- IR email to the Company Secretary (14 questions, draft in review Step 8.5). The pipeline does not send it.
- FY26 Annual Report needed for: investment category, CWIP ageing, tax reconciliation, OCA/OCFL/other non-current asset notes, Ind AS 116 lease note, Buildfort AOC-1.
- A1 extraction defects EX-1 to EX-3 (consolidated Total Equities and Liabilities column shift R387/R388); no review number depends on them.
