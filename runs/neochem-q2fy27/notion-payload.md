# Notion payload — NEOCHEM H1 FY27 review (NOT WRITTEN; for operator approval)

Batch standing instruction 6: this session does not write to Notion. The write gate (operator ruling 2026-10-03) needs the operator's explicit approval of this payload. Decision Status is never written.

## Target
- Database: COMPANIES MASTER (collection://345bb2b9-d3ab-8032-9b46-000ba16ab827)
- Page: **NONE EXISTS.** Workspace search on 2026-10-29 for "Neochem Bio Solutions" and "NEOCHEM" returned no page. Creating a page is the operator's decision. companies/NEOCHEM.md does not exist; no spear is on record.
- If the operator creates the page, it starts as a PRE-THESIS record. Decision Status stays blank.

## 1. Page creation (operator decision; proposed values only)
- Title: `Neochem Bio Solutions Ltd`
- Company Name: Neochem Bio Solutions Limited (formerly Neochem Technologies Private Limited); NSE SME, symbol NEOCHEM, ISIN INE21UM01018, CIN L24304GJ2017PLC097754 (res l.10-14, 64-66)
- Current Market Price: 105 (screener.in, 28-Oct-2026 08:48 IST). Operator's call.
- Decision Status: **do not write.**

## 2. Key Notes (first entry; prepend on any later page)

Exact text (A4 Step 9 line after correction loop 1):

```
2026-10-29 | H1 FY27 PRE-THESIS READ (connector copy, pending NSE verification): revenue +50.4% YoY, operating EBIT +42.6% (core PBT +68.7% incl. a 0.71 Cr interest saving), EPS +1.3%; CFO negative 2nd period; fraud loss unquantified; CFO replaced at results meeting; PROCEED WITH FLAGS
```

## 3. insert_content (position: end), in this order, split across sequential calls as needed

Heading: `## H1 FY27 Results Review (filed documents only, connector-rebuilt copy), 29-Oct-2026`

1. The full A4 review, complete tables, never summarised: runs/neochem-q2fy27/work/review_neochem_q2fy27.md, from the title line through the end of the LOOP 1 CHANGE LOG table (leave out the closing YAML block). It ends with the PLAIN-LANGUAGE BRIEF and the forward map; both are part of the save. Escape `|` inside table cells as `\|`.
2. A3 forensics tables (completeness proof): sections 2 (findings table, A3-01 to A3-20), 3 (F1-F17 scorecard) and "Loop 1 dispositions (A5 F1)" of runs/neochem-q2fy27/work/forensics_neochem_q2fy27.md.
3. A5 audit verdict block, exact text:

```
A5 ADVERSARY (Opus 5.5), loop 1 of 1: COMPLETE (style notes only).
Loop 0: INCOMPLETE, 1 FACTUAL (F6 "CFO since 2018" unsupported), 4 MISSING (F1 three orphan row groups, F3 sequential opex test, F4 FY26 receivables build, F5 review-report qualifier dropped), 1 CONTRADICTION (F2 core growth vs operating EBIT +42.6%). All six fixed by A3/A4; drift check clean; protocol verdict PROCEED WITH FLAGS unchanged.
Coverage: structured IDs results 363, intimation 33; orphans none after loop. Arithmetic: PASS, no mismatch beyond rounding.
Source: connector-rebuilt copy of the NSE filing; every number pending verification against the exchange original.
Open STYLE notes: S1-S16 (audit file runs/neochem-q2fy27/work/audit_neochem_q2fy27.md).
```

## 4. Proposed DOWNSTREAM SIGNAL TRACKER rows
None. No tracker rows exist for NEOCHEM (review Step 5.5A: "tracker rows not supplied"; flag F-15). Role 5.5 has never run on this name.
