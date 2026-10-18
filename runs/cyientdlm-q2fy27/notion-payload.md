# Notion payload: CYIENTDLM Q2 FY27 (NOT WRITTEN; awaiting operator batch approval)

Write gate (operator ruling 2026-10-03): nothing below has been written to Notion. Per the operator's 2026-10-17 instruction, this run did not wait at the gate; the operator approves all writes later in one batch. Decision Status is NEVER written by this pipeline.

## Target page
- COMPANIES MASTER page: Cyient DLM Ltd
- Page ID: 3d8bb2b9-d3ab-81fc-b72e-faa77c718141
- URL: https://app.notion.com/p/3d8bb2b9d3ab81fcb72efaa77c718141
- Page last edited (at fetch): 2026-10-13T02:54:06Z. Re-fetch before writing; if edited since, re-check the Key Notes prefix.

## 1. update_properties
- Key Notes: PREPEND the line below, then the existing separator ` \|\| `, then the existing Key Notes text unchanged.

```
17-Oct-2026 \| Q2 FY27 PRE-THESIS READ (results + deck + release, /run-quarterly A1-A5; A5 closed after 2 loops with 1 open item OI-1, flagged): revenue Rs393.09 Cr +26.5% YoY; op EBITDA margin 8.69% (-135 bps); gross margin 37.41% (-381 bps YoY, third compression on the Notion count; mgmt cause mix + product development, no component-cost answer). Reported PAT Rs34.01 Cr, of which Rs18.20 Cr (53.5%) is an earnout write-back, second Q2 in a row; ex-earnout PAT Rs15.82 Cr +25.85%, but ~89% of that gain is FX and ex-earnout ex-FX PBT +1.9%. US arm EBITDA Rs1.15 Cr (1.17%), loss ex-earnout; carrying value 5.4x falling TTM EBITDA. India revenue +25.1%. H1 CFO Rs14.75 Cr vs PAT Rs50.30 Cr; India took Rs28.79 Cr new short-term debt. Order book Rs2,813.7 Cr record, stated intake growth does not tie to the book walk. Cash falsifier: needs NWC basis ruling (filing 189.0 days, deck 153, Notion 169 not reproducible). Tests: 2 RED (prov), 4 margin leg RED, 6 US leg RED, 3 GREEN, 1 AMBER, 5 UNKNOWN. Verdict PROCEED WITH FLAGS. Decision Status not set (operator-only). 30 IR questions; Role 5 on the 15-Oct call pending.
```

- Analysis Date 1: 2026-10-17
- Decision Status: NOT WRITTEN (NOT SET; Halt 1 pending; no change proposed).
- Entry Price Max / Margin of Safety Price: none exist; not written.

## 2. insert_content (position: end), as a new section headed
"## Q2 FY27 — Results Review, pre-thesis read (extraction-first pipeline, results + presentation + press release) — 17-Oct-2026"

Insert in sequential calls, verbatim, complete tables (never summaries), pipes in cells escaped as `\|`:
1. runs/cyientdlm-q2fy27/work/review_cyientdlm_q2fy27.md, in full (776 lines; ends with the PLAIN-LANGUAGE BRIEF). Split at its `## STEP` headings.
2. OPEN-ITEM NOTE, inserted directly after Step 8.5 Question 10:

```
OPEN ITEM OI-1 (A5 final re-audit, CONTRADICTION, not looped under the no-third-loop rule): the Q10 "Bull Answer" cell reads "Internal cash; borrowings are US refinancing only". The filing rules this out: consolidated borrowings rose Rs25.84 Cr in H1, all of it the India entity's Rs28.79 Cr of new short-term debt; subsidiary borrowings fell Rs2.96 Cr (results L170, L177, L243, L245, L565). A5's proposed wording: "Operating cash and the India short-term line fund the build, repaid from collections by Q4; US borrowings refinanced, not grown." The cell is a hypothetical answer; no number, flag or verdict changes.
```

3. A3 forensics tables (completeness proof):
   - runs/cyientdlm-q2fy27/work/forensics_results_cyientdlm_q2fy27.md
   - runs/cyientdlm-q2fy27/work/forensics_presentation_cyientdlm_q2fy27.md
   - runs/cyientdlm-q2fy27/work/forensics_pressrelease_cyientdlm_q2fy27.md
4. A5 audit verdict block:

```
A5 verdict: INCOMPLETE on 1 open item (OI-1), closed out under the operator rule "no third loop: close with open items flagged" (17-Oct-2026).
Run 1 (fresh re-run after the restart): 2 CONTRADICTION, 4 MISSING; all closed in loop 1.
Loop 1: 1 CONTRADICTION, 1 FACTUAL, 3 MISSING; all closed in loop 2.
Loop 2: OI-1 open (one-cell bull-answer text). Coverage: 993 / 372 / 60 structured IDs referenced, no orphans. Arithmetic: no mismatch above rounding.
Open STYLE: LS3 (a reading-(b) cite in Step 4 points at the employee-cost note).
```

## 3. DOWNSTREAM SIGNAL TRACKER candidates (payload only)
Four candidate signals in review section 5.5C. Not written.

## Operator items carried
- Halt 1 decision and Mental Model signature: still pending.
- Ruling: NWC basis for the cash falsifier, and whether the H1 print counts (two readings in 6B test 1).
- Rulings still open from 11-Sep: Gate 0 window, sector cap row (no EMS row), archetype rung, Rule G for a parent promoter, stage 5/6/7 rework.
- Run Role 5 on the 15-Oct-2026 earnings call transcript (not in this run).
- Filing data defects to note: consolidated Q2 FY26 employee cost misprint (329.42 vs 529.42 Mn by footing); standalone H1 basic EPS read 4.35 (4.55 by arithmetic); UDINs illegible.

---

## ROLE 5 ADDENDUM (2026-10-18): NOT WRITTEN; awaiting operator batch approval

Supersedes the Key Notes line above if the operator approves both: prepend this line instead (pipes escaped).

```
18-Oct-2026 \| Q2 FY27 CONCALL (15-Oct call, machine transcript of company recording; Role 5 A1-A5, A5 COMPLETE after 2 loops). Verdict PROCEED WITH FLAGS unchanged; concall impact WEAKENED. Call vs filing: chairman says gross/contribution margin rose and "not the revenue mix" vs filed gross margin -381 bps; earnout reversal called "one-time" though the deck shows one in both Q2s (80.5% of Q2 other income); US unit "as per plans" at 1.17% EBITDA. Guidance: FY27 EBITDA "close to 9%" / "9-10%" (at 9%, H2 ~8.5%, below Q2); FY28 "double digits"; FY27 revenue 30-35%, H2 >30% (Q3 bar 394.29 Cr is +0.3% QoQ; test H2 >= 874.15 Cr). B2S revenue now FY29-FY30; FY27 double-digit B2S target unanswered. 600 Cr quarterly intake guide "probably" (met 1 of 5 walk quarters). Of 30 filing questions: 1 answered, 4 partial, 4 evaded, 21 not addressed; Q31-Q42 added. OI-1 (Q10 bull answer) corrected. Decision Status not set (operator-only).
```

insert_content additions (position end, after the Q2 FY27 review section):
1. The merged review runs/cyientdlm-q2fy27/work/review_cyientdlm_q2fy27.md now carries "## ROLE 5: CONCALL ANALYSIS (Q2 FY27 call, 15-Oct-2026; machine transcript)" and "(Role 5 addendum)" passages; insert the Role 5 section in full and the updated Step 8.5 table (ANSWER STATUS column, Q31-Q42) in place of the earlier copy.
2. A3 concall forensics table: runs/cyientdlm-q2fy27/work/forensics_concall_cyientdlm_q2fy27.md.
3. Role 5 audit verdict block:
```
Role 5 A5 verdict: COMPLETE (loop 2 of 2, operator standing rule). Run 1: 4 FACTUAL, 3 CONTRADICTION, 4 MISSING (both directions: 4 too bearish, 3 too lenient) -> closed in loop 1. Loop 1: 2 CONTRADICTION, 3 MISSING -> closed in loop 2. Coverage 303/303 concall rows, CF01-CF25 cited; M001 (cc L238) added to the ledger. STYLE open: 25-line summary narrative vs 10-20 spec; L2-S1 (chairman's "revenue mix is always going to be there" clause unquoted).
```
Source caveat for every Role 5 line: machine transcript of the company's own recording, speakers inferred; on any number conflict the filing wins.
