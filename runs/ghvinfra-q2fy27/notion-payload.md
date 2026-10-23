# Notion payload: GHVINFRA Q2 FY27 (NOT WRITTEN; operator approval required)

Write gate (operator ruling 2026-10-03): this payload is printed and saved only. No Notion call has been made.
Decision Status is never written by this pipeline.

## Target page
- Page: GHV Infra Projects Limited, COMPANIES MASTER
- Page ID: 387bb2b9-d3ab-81de-8c50-d96623d49e02
- URL: https://app.notion.com/p/387bb2b9d3ab81de8c50d96623d49e02
- Fetched live 2026-10-23 (read only). Decision Status on page: AVOID.

## 1. update_properties: PREPEND to Key Notes (keep every prior entry after it)

```
2026-10-23 | Q2 FY27 results review (/run-quarterly, A5 INCOMPLETE on one text item F-D after 2 loops): revenue +63.30% YoY, core PBT +37.88%, H1 CFO -244.37 Cr, net debt 388.24 Cr; Erisha UAE contract ended with legal proceedings, no provision; parent funded exposure to the two subsidiaries up to 25.39 Cr (booked-balance ceiling 37.61 Cr if guaranteed; claim amounts and performance guarantees NOT FOUND, outside it), group up to 40.52 Cr gross; promoter converted warrants at Rs 80 a share, 21,83,333 pending warrants convert or lapse by 31-Mar-2027 at the latest [INFERENCE]; AVOID reinforced, no re-entry condition met. \|\|
```

Properties NOT touched: Decision Status, Promoter Verdict, Entry Price Max, Margin of Safety Price, Position Size.

## 2. insert_content, position: end (split across sequential inserts if large)

Heading: `# Q2 FY27 QUARTERLY REVIEW (/run-quarterly, added 2026-10-23)`

Content, in order:
1. The full A4 review: runs/ghvinfra-q2fy27/work/review_ghvinfra_q2fy27.md (all tables, Questions for Management Q1-Q34, monitorables M1-M14, flags 1-12, and the PLAIN-LANGUAGE BRIEF with its forward map). Escape `|` inside table cells as `\|`.
2. The A3 forensics table: runs/ghvinfra-q2fy27/work/forensics_ghvinfra_q2fy27.md (F1-F17 scorecard, FN01-FN31, commitment register).
3. The A5 audit verdict: runs/ghvinfra-q2fy27/work/audit_ghvinfra_q2fy27.md (iteration 3: INCOMPLETE on F-D only).

OPEN ITEM to carry with the append (A5 F-D, FACTUAL, not fixed because the loop cap was reached):
- Review line 72 says "Paid-up capital did not move in that window (l353), so the 38.50 Cr was not a share issue." Line 353 prints closing capital only, so it cannot show this.
- A5 replacement text: "Line 353 prints closing capital only (no 31-Mar-2025 opening), so it cannot show whether capital moved in H1 FY26. Corroboration: Q2 FY26 diluted EPS Rs 1.52 sits below basic Rs 1.56 (l356-357), so a dilutive instrument was outstanding in Jul-Sep 2025; the warrants are the only one the filing names (l475) [INFERENCE]."
- Operator choice: approve the swap before the append, or append as is with this note.

## 3. Tracker rows proposed (DOWNSTREAM SIGNAL TRACKER; operator gate)
- GHV Infra: Erisha legal proceedings and subsidiary exposure (tests EM catalyst list and parent dependence).
- GHV Infra: conversion or lapse of 21,83,333 pending warrants by 31-Mar-2027 [INFERENCE].

## Pending operator rulings carried forward
1. Is the UAE Rs 2,645 Cr catalyst on file the RAKEZ Erisha contract now ended? The filing gives no contract value.
2. Log H1 FY27 CFO (-244.37 Cr S, -246.77 Cr C) as the cash re-entry baseline. FY26 full-year CFO needs the FY26 Annual Report (Role 6).
3. Notion record conflict: "three CFO changes in 13 months" vs the resignation letter's "first CFO, about 2 years".
4. Proposed re-entry conditions (d) Erisha resolved and FZ-LLC audited, (e) consolidated PAT at or above standalone for two quarters.
