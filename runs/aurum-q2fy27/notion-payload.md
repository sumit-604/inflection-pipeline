# Notion payload: AURUM Q2 FY27 (NOT WRITTEN; awaiting operator batch approval)

Write gate (operator ruling 2026-10-03): nothing below has been written to Notion. Per the operator's 2026-10-17 instruction, this run did not wait at the gate; the operator approves all writes later in one batch. Decision Status is NEVER written by this pipeline.

## Target page
- COMPANIES MASTER page: AURUM (Aurum Proptech Ltd)
- Page ID: 39ebb2b9-d3ab-817e-8d09-d887dc5b6a93
- URL: https://app.notion.com/p/39ebb2b9d3ab817e8d09d887dc5b6a93
- Page last edited (at fetch): 2026-10-14T02:10:33Z. Re-fetch before writing; if edited since, re-check the Key Notes prefix.

## 1. update_properties
- Key Notes: PREPEND the line below, then a separator, then the existing Key Notes text unchanged. Escape `|` inside the line as `\|`.

```
17-Oct-2026 \| Q2 FY27 (results + deck + release, /run-quarterly A1-A5, A5 COMPLETE after 2 loops): core PBT ex-OI Rs(0.52) Cr after Q1 Rs(4.86) Cr (Rs(4.26) Cr with Rs3.74 Cr capitalised team cost expensed). TRIGGER 1 FIRED on the 03-Oct named test (Reading A); Reading B (ex one-time OI only) unresolved, Q2 split ND. Continuing PAT Rs4.29 Cr rests on OI Rs7.12 Cr. Revenue +63.9% YoY to Rs130.19 Cr, Distribution 83.8% of the rise, organic split ND. Housing.com consolidated 29-Sep: Rs458.06 Cr in stock, goodwill Rs549.45 Cr + intangibles Rs410.05 Cr provisional (94.7% of owners' equity), swap multiple NOT COMPUTABLE. Cash INDETERMINATE-WITH-DIRECTION: lease-adj CFO H1 Rs13.06 Cr (Rs9.38 Cr ex tax refund). AREDL loan test NOT DETERMINABLE: Rs9.52 Cr loan at ~42% annualised, borrower unnamed. Goodwill baseline mismatch: Notion Rs174.25 Cr vs audited Mar-26 Rs207.17 Cr. Protocol verdict PROCEED WITH FLAGS. Proposed status AVOID (no change). Decision Status unchanged (operator-only). 22 IR questions logged.
```

- Analysis Date 1: 2026-10-17
- Decision Status: NOT WRITTEN (proposed AVOID, no change; trigger 1 fired, flagged for the operator).
- Entry Price Max / Margin of Safety Price: NOT CHANGED (Role 1 recompute deferred; ruling 17 pending).

## 2. insert_content (position: end), as a new section headed
"## Q2 FY27 — Quarterly Review (extraction-first pipeline, results + presentation + press release) — 17-Oct-2026"

Insert in sequential calls, verbatim, complete tables (never summaries), pipes in cells escaped as `\|`:
1. runs/aurum-q2fy27/work/review_aurum_q2fy27.md, in full (770 lines; includes the PLAIN-LANGUAGE BRIEF as its last narrative section). Split at its `## STEP` headings.
2. A3 forensics tables (completeness proof):
   - runs/aurum-q2fy27/work/forensics_results_aurum_q2fy27.md (checklist table and findings table)
   - runs/aurum-q2fy27/work/forensics_presentation_aurum_q2fy27.md (checklist table and findings table)
   - runs/aurum-q2fy27/work/forensics_pressrelease_aurum_q2fy27.md (checklist table and findings table)
3. A5 audit verdict block:

```
A5 verdict: COMPLETE (loop 2 of 2; operator approved the second loop 17-Oct-2026).
Run 1 INCOMPLETE: 3 FACTUAL, 2 CONTRADICTION, 3 MISSING, all closed in loop 1.
Loop 1 INCOMPLETE: 1 FACTUAL, 2 MISSING, all closed in loop 2.
Coverage: 1,728 / 367 / 96 structured IDs referenced, no orphans. Arithmetic: no mismatch above rounding.
Open STYLE notes (no loop): REA "held both" inference not grafted; Rental loaded result Rs(2.08) Cr not stated; A1/A2 anchor and keying notes.
No finding in any round affected the proposed Decision Status (AVOID).
```

## 3. DOWNSTREAM SIGNAL TRACKER candidates (payload only; operator-approval gate)
See review section STEP 5.5C for the three new signal candidates. Not written.

## Operator items carried
- Rulings pending: 16 (warrant tracker falsifier), 17 (house-case re-base to 10.32 Cr diluted shares), 40 (item 9 scope).
- New: reconcile goodwill baseline (Rs174.25 Cr vs audited Rs207.17 Cr) before item 7 is scored.
- Verify both auditor UDINs on the ICAI portal from the exchange copy (OCR-illegible).
- Obtain the H1 Reg 23(9) RPT disclosure (filed with results, 16-Oct) to close the AREDL loan test.

---

## ROLE 5 ADDENDUM (2026-10-18): NOT WRITTEN; awaiting operator batch approval

Prepend this Key Notes line too (pipes escaped), after the 17-Oct line:

```
18-Oct-2026 \| Q2 FY27 CONCALL (16-Oct call, the company's "22nd earnings call"; machine transcript of company recording; Role 5 A1-A5, 2 loops, final A5 INCOMPLETE on 1 minor open item L2-F1, flagged). Verdict PROCEED WITH FLAGS unchanged; AVOID case MAINTAINED, BUY-break path WEAKENED. SM-REIT not mentioned: TRIGGER 3 NOT DETERMINABLE (about 14 calls since the Jun-2023 registration on Reading A = FIRED [INFERENCE]; 1 evidenced since the trigger was set on Reading B = NOT FIRED); operator to rule the count start date. Housing.com: management declined its base numbers (first evasion on record); break-even internal 4-6 qtrs (~Q2-Q4 FY28), after the earliest re-entry pair; Rs120 Cr cost cut, Rs150 Cr revenue add. Call vs filing: other income "mainly treasury" vs H1 >=51.9% one-time; "fourth consecutive profitable quarter" true only on PBT (Q1 FY27 continuing PAT Rs(0.34) Cr); "effectively debt-free" holds ex-leases only (net debt incl. leases Rs26.10 Cr). Notion goodwill baseline (Rs174.25 Cr = 61% of NW) is stale: equity is Rs1,019.64 Cr. Of 22 filing questions: 0 answered, 7 partial, 1 evaded part, 15 not addressed. Decision Status AVOID unchanged (operator-only).
```

insert_content additions: the merged review runs/aurum-q2fy27/work/review_aurum_q2fy27.md now carries "## ROLE 5: CONCALL ANALYSIS (Q2 FY27 call, 16-Oct-2026; machine transcript)" and "(Role 5 addendum)" passages; insert the Role 5 section and the updated Step 8.5 table (ANSWER STATUS column, rows 23-35). A3 concall forensics: work/forensics_concall_aurum_q2fy27.md.

Role 5 audit verdict block:
```
Role 5 A5 verdict: INCOMPLETE on 1 minor open item after loop 2 of 2 (operator rule: no third loop, close with open items flagged).
OPEN ITEM L2-F1 (FACTUAL, minor, owner A4): review brief 1A (REV L1342) and the Step 8.5 rule line (REV L569) say four NOT ADDRESSED rows (4, 8, 17, 22) got only a restated filed figure; row 7 also qualifies (the call gave only the filed warrant amounts). Correct text: "Five of the 15 (rows 4, 7, 8, 17, 22)". No tally, grade, flag or verdict moves.
Run 1: 3 MISSING, 2 FACTUAL (+ hedge count) -> closed in loop 1. Loop 1: 1 CONTRADICTION, 1 MISSING -> closed in loop 2. Coverage 341/341 concall rows, A3C-01 to A3C-31 cited.
```
New operator rulings needed: (a) trigger 3 count start date; (b) re-base the goodwill baseline for watchlist item 7 and trigger 4 (audited Mar-26 Rs207.17 Cr; Sep-26 Rs549.45 Cr provisional).
Source caveat: machine transcript of the company's own recording, speakers inferred; on any number conflict the filing wins.
