# Notion payload: HFCL Q2 FY27 (NOT WRITTEN; awaiting operator approval)

Write gate (operator ruling 2026-10-03): nothing below has been written to Notion. The operator was asleep (19-Oct instruction: no questions), so the run saved the payload and did not wait at the gate. Decision Status is NEVER written by this pipeline.

## Target page
- COMPANIES MASTER page: HFCL Limited
- Page URL: https://www.notion.so/375bb2b9d3ab81c284d1dd6feead52d0
- Page last edited (at fetch 2026-10-19): 2026-10-14T02:13:51Z. Re-fetch before writing; if edited since, re-check the Key Notes prefix. Note: the Key Notes export was cut off mid-sentence at a 30-Jul entry ("two orders in"); check the live property before prepending.

## 1. update_properties
- Key Notes: PREPEND the line below, then the existing separator ` \|\| `, then the existing Key Notes text unchanged.

```
20-Oct-2026 \| Q2 FY27 RESULTS + CONCALL REVIEW (results/press release, deck, CARE monitoring agency reports, 19-Oct call recording as machine transcript; /run-quarterly A1-A5; Role 4 A5 COMPLETE after 2 loops; Role 5 addendum A5 after 2 loops, see audit). TRIPWIRE #4 FIRED on the silence limb (receivable ageing, DSO and unbilled revenue undisclosed in Q1 and in all three Q2 channels); under 8A-W the protocol PROPOSES AVOID. FLAG ONLY: Decision Status unchanged (operator decides). Counter: computed receivable days improved; no analyst asked; reverses if ageing and unbilled are given in writing. Trigger #6 NOT FIRED: E&Y-advised restructuring committee near recommendation; board ~10 days after the call; decision ~early-mid Nov; scope unstated. Revenue Rs 2,541.79 Cr +143.6% YoY; op EBITDA margin 24.81%; PAT Rs 394.22 Cr. H1 CFO Rs 455.27 Cr = 0.71x PAT reported, 0.52x counting Rs 123.40 Cr tax charged not paid. Cons PAT exceeds standalone by 47.1%. "At least 80%" FY27 guide = H1 run-rate (implies H2 +46.7% vs H1 +132.8%), basis unstated. Defence book ~Rs 1,850 Cr, ~86.5% in an aerospace target not yet bought; price and financials undisclosed; multiple NOT COMPUTABLE; no accretion credited; close "within November". Defence Rs 5,000 Cr is an aspiration on the call. Hyperscalers at most ~39.90% of the book on the export-orders reading. MA report: Rs 416.25 Cr of preferential objects unfunded until warrant conversion; Rs 90 Cr HASPL object missed 30-Sep, extended by board circular to 31-Dec. Customer contracts reset yearly (no price floor). Provisional credibility grade C (40%), archetype EVASIVE (provisional), specificity 0.40. Verdict PROCEED WITH FLAGS; cash INDETERMINATE-WITH-DIRECTION. Notion corrections: warrant balance Rs 416.25 Cr (not ~412.5); FII+DII 27.62%. 61 IR questions.
```

- Analysis Date 1: 2026-10-20
- Decision Status: NOT WRITTEN (WATCHLIST "DO NOT INITIATE"; protocol proposes AVOID on tripwire #4; operator decides).
- CMP / entry fields: not written.

## 2. insert_content (position: end), as a new section headed
"## Q2 FY27 — Results + Concall Review (extraction-first pipeline; results, deck, monitoring agency reports, machine transcript of 19-Oct call) — 20-Oct-2026"

Insert in sequential calls, verbatim, complete tables (never summaries), pipes in cells escaped as `\|`:
1. runs/hfcl-q2fy27/work/review_hfcl_q2fy27.md, in full: the Role 4 review (with loop change logs), then the ROLE 5 ADDENDUM whose PLAIN-LANGUAGE BRIEF (UPDATED) supersedes the Role 4 brief. Split at `## STEP` headings.
2. A3 forensics tables (completeness proof):
   - runs/hfcl-q2fy27/work/forensics_results_hfcl_q2fy27.md
   - runs/hfcl-q2fy27/work/forensics_presentation_hfcl_q2fy27.md
   - runs/hfcl-q2fy27/work/forensics_mareport_hfcl_q2fy27.md
   - runs/hfcl-q2fy27/work/forensics_concall_hfcl_q2fy27.md
3. A5 audit verdict block: see runs/hfcl-q2fy27/work/audit_hfcl_q2fy27_role5_loop2.md (final) and the Role 4 audits audit_hfcl_q2fy27*.md. Role 4: run 1 INCOMPLETE (OCI cell, guidance wording, tax-accrual CFO, acquisition probe, 10 ledger units, pointers), loop 1 closed them and raised one (para-7 cash), loop 2 closed it. Role 5: run 1 INCOMPLETE (contract price floor, Reading B band, 14 ledger units, hyperscaler basis, defence aspiration, margin readings), loop 1 closed them and raised two (hyperscaler maximum, MD quote), loop 2 fixed them. Concall source: machine transcript, medium.en and small.en mixed by chunk.

## 3. Tracker rows (not written; candidates for Claude web)
- Receivable ageing and unbilled revenue in writing (reverses the tripwire #4 FIRED reading).
- Restructuring board decision, ~early-mid Nov 2026 (trigger #6 test).
- Aerospace acquisition close, "within November": price and target financials.
- Promoter warrant conversion (Rs 416.25 Cr) and HASPL Rs 90 Cr object by 31-Dec-2026.
- Q3 FY27 consolidated Telecom Products revenue (bull >= Rs 2,321.98 Cr; bear < Rs 2,006.15 Cr).
