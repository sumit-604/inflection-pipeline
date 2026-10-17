# Notion payload: KARNIKA H1 FY27 (NOT WRITTEN; awaiting operator batch approval)

Write gate (operator ruling 2026-10-03): nothing below has been written to Notion. Per the operator's 2026-10-17 instruction, this run did not wait at the gate; the operator approves all writes later in one batch. Decision Status is NEVER written by this pipeline.

## Target page
- No COMPANIES MASTER page exists for Karnika (live notion-search 2026-10-17 for "Karnika Industries" and "KARNIKA": no result). No companies/KARNIKA.md. No spear on record.
- Proposed action: create a new page in COMPANIES MASTER (data source collection://345bb2b9-d3ab-8032-9b46-000ba16ab827), titled "Karnika Industries Ltd (KARNIKA)". OPERATOR DECIDES whether to open a page for a pre-thesis read or hold the payload. Re-search before writing in case a page was created since.

## 1. Properties (new page)
- Title: Karnika Industries Ltd (KARNIKA)
- Key Notes (first entry; escape `|` as `\|`):

```
17-Oct-2026 \| H1/Q2 FY27 PRE-THESIS READ (results + concall + deck, /run-quarterly A1-A5, 2 loops, final A5 INCOMPLETE with 3 open A4 items, none verdict-moving). Standalone Q2 rev +17.4% to Rs81.83 Cr (ex sales to Kidcity ~+5.8%, INFERENCE); core PBT ex-OI +7.4%; mgmt 52.3% is consolidated vs standalone base. Standalone H1 CFO Rs(4.88) Cr on PAT Rs18.17 Cr; receivable days 109.7 -> 141.7. Loans to corporates Rs15.48 -> Rs31.41 Cr, borrowers unnamed; Elementa Lifespaces 40% (Rs2.00 Cr) + RDB Elementa 26% pending, non-textile. Kidcity 75% derived price ~Rs3.67 Cr (~0.70x TTM PAT), H1 CFO Rs0.47 Cr on PAT Rs5.30 Cr. Filing errors: Q1 NCI on tax base, Mar-26 consolidated FVOCI omission, EPS not bonus-restated. Concall: 3 statements contradicted by filing; specificity 0.41, lean EVASIVE. Cash INDETERMINATE-WITH-DIRECTION. Protocol verdict PROCEED WITH FLAGS. Branch 8A-W, no status proposed. 37 IR questions; top: related-party status of the Rs31.41 Cr loans.
```

- Analysis Date 1: 2026-10-17
- Decision Status: NOT WRITTEN (no status proposed; pre-thesis read).
- Entry Price Max / Margin of Safety Price: NOT SET (Role 1 not run).

## 2. insert_content (position: end), as a new section headed
"## H1 / Q2 FY27 — Quarterly Review (extraction-first pipeline, results + concall + presentation) — 17-Oct-2026"

Insert in sequential calls, verbatim, complete tables (never summaries), pipes in cells escaped as `\|`:
1. runs/karnika-h1fy27/work/review_karnika_h1fy27.md, in full (about 1,390 lines; starts with OPEN ITEMS AT CLOSE; ends with the PLAIN-LANGUAGE BRIEF and the forward map). Split at its `## STEP` and `# SECTION` headings.
2. A3 forensics tables (completeness proof):
   - runs/karnika-h1fy27/work/forensics_results_karnika_h1fy27.md (checklist and findings tables)
   - runs/karnika-h1fy27/work/forensics_concall_karnika_h1fy27.md (checklist, findings and commitment register, incl. Loop 1 delta)
   - runs/karnika-h1fy27/work/forensics_presentation_karnika_h1fy27.md (checklist and findings tables)
3. A5 audit verdict block:

```
A5 verdict: INCOMPLETE at close (loop 2 of 2; operator batch rule 17-Oct-2026: no third loop, close with open items flagged).
Run 1 INCOMPLETE: 3 FACTUAL, 7 MISSING; closed in loop 1.
Loop 1 INCOMPLETE: 3 FACTUAL, 4 MISSING, 1 CONTRADICTION; closed in loop 2.
Loop 2 INCOMPLETE: 1 FACTUAL, 2 MISSING, all A4-local, carried as OPEN ITEMS OI-1 to OI-3 at the top of the review:
  OI-1 H2 FY26 base already holds a full post-deal half of Kidcity supply (Rs27.25 Cr purchases).
  OI-2 deck FY26 balance sheet already carries the FVOCI-corrected figures; error likely confined to this filing's comparative column (narrows Q8 bear fork).
  OI-3 Kidcity H1 CFO +Rs0.47 Cr rests on +Rs5.74 Cr payables and +Rs3.43 Cr inventory release (about -Rs8.70 Cr without); Kidcity payables >= Rs23.51 Cr may sit in Karnika receivables.
Coverage at close: 780 / 246 / 553 structured IDs referenced, no orphans; 167 turns, 67 questions, 106 mgmt numbers, 61 forward rows, 32 slides. Arithmetic: all derived metrics tie to the lakh.
No finding in any round moved PROCEED WITH FLAGS or the cash class.
```

## 3. DOWNSTREAM SIGNAL TRACKER candidates (payload only; operator-approval gate)
See review STEP 5.5C for the four new signal candidates (Case B). Not written. Tracker floor 0 of 3 (OR-17).

## Operator items carried
- Decide: open a COMPANIES MASTER page and/or a /step1 intake (no spear on record).
- Send the 37 IR questions (review STEP 8.5); Q1, Q2, Q8 are the top three.
- Apply or rule on open items OI-1 to OI-3 (exact replacement text: work/audit_karnika_h1fy27_loop2.md section 4).
