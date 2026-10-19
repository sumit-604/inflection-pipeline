# Notion payload: GOCL Q2 FY27 (NOT WRITTEN; awaiting operator approval)

Write gate (operator ruling 2026-10-03): nothing below has been written to Notion. The operator was asleep (19-Oct instruction: no questions), so the run saved the payload and did not wait at the gate. Decision Status is NEVER written by this pipeline.

## Target page
- COMPANIES MASTER page: GOCL Corporation Limited (HELD)
- Page URL: https://www.notion.so/36ebb2b9d3ab81dbb91ff63d8459a4cb
- Page last edited (at fetch 2026-10-19): 2026-10-14T02:10:30Z. Re-fetch before writing; if edited since, re-check the Key Notes prefix.

## 1. update_properties
- Key Notes: PREPEND the line below, then the existing separator ` \|\| `, then the existing Key Notes text unchanged.

```
20-Oct-2026 \| Q2 FY27 RESULTS REVIEW (results filing only, no call or deck; /run-quarterly A1-A5, A5 COMPLETE after 1 loop). HELD momentum: HOLD per 8A momentum clause, conditional on the Chandelier; no trigger fired; CHANDELIER LEVEL STILL NOT ON FILE (ruling 20 overdue). PAT Rs 40.50 Cr (Q1 40.40, Q2 FY26 14.03), all treasury: other income Rs 62.65 Cr vs revenue Rs 4.11 Cr; core loss ex other income widened to Rs (15.35) Cr from (6.12). The four logged questions: (1) H1 CFO Rs 28.87 Cr, all from a one-off working-capital release, Rs (4.27) Cr before it; (2) standalone loans +Rs 68 Cr to Rs 2,349.90 Cr, borrower printed as an unnamed "Other Company"; 70-80% of interest received re-lent to the same book (tripwire 4 adverse move, no fire threshold on file); (3) auditor EoM on Rs 1,316.10 Cr guarantees REPEATS, regularisation "in process"; (4) unallocable liabilities are dividend payable and tax, not debt. Tax liabilities Rs 282.75 Cr vs ~Rs 68.73 Cr liquid cash after the Rs 148.72 Cr dividend. UK sub HGHL (not reviewed by main auditor) 17.1% of Q2 PAT. Squarespace Rs 111.68 Cr advance (next Kukatpally tranche). HNPCL scheme meeting 24-Nov-2026 11:00 IST; merger multiple NOT DETERMINABLE from the filing (Explanatory Statement needed). Verdict PROCEED WITH FLAGS; cash INDETERMINATE-WITH-DIRECTION. Rulings due: 20 (Chandelier) now; 42 (exit on scheme pass?) before 24-Nov. Decision Status unchanged HELD (operator-only). 25 IR questions.
```

- Analysis Date 1: 2026-10-20
- Decision Status: NOT WRITTEN (HELD; no change proposed).
- Current Market Price / stop fields: not written (no price refresh in this run).

## 2. insert_content (position: end), as a new section headed
"## Q2 FY27 — Results Review (extraction-first pipeline, results filing) — 20-Oct-2026"

Insert in sequential calls, verbatim, complete tables (never summaries), pipes in cells escaped as `\|`:
1. runs/gocl-q2fy27/work/review_gocl_q2fy27.md, in full (ends with the PLAIN-LANGUAGE BRIEF, the YAML block and the loop 1 change log). Split at its `## STEP` headings.
2. A3 forensics table (completeness proof): runs/gocl-q2fy27/work/forensics_results_gocl_q2fy27.md
3. A5 audit verdict block:

```
A5 verdict: COMPLETE (loop 1 re-audit, runs/gocl-q2fy27/work/audit_gocl_q2fy27_loop1.md). Run 1 INCOMPLETE: F1 (EMS capacity commissioning not filed; only Rs 0.76 Cr CWIP capitalised), M1 (gross vs net interest cash), M2 (HNPCL multiple not determinable). All closed in loop 1. STYLE logged, not looped, incl. L1-S1: the review's "HNPCL borrowings at least Rs 1,096.10 Cr" rests on a guarantee-never-exceeds-loan premise that need not hold (tagged INFERENCE; operator may overrule to FACTUAL). OCR-layer note mismatches to check on page images: guarantee 109,640 vs 109,610 lakhs; notes dated 18 vs 19-Oct; AGM 28 vs 29-Sep; advance 11,166.42 vs 11,168.42.
```

## 3. Tracker rows (not written; candidates for Claude web)
- HNPCL scheme meeting result, 24-Nov-2026.
- Kukatpally sale deed for the Rs 111.68 Cr advance (date not stated).
- Ecopolis sale deed, about Rs 815 Cr (date not stated).
- Tax liability settlement, Rs 282.75 Cr (date not stated).
