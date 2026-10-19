# Notion payload: TATVA Q2 FY27 (NOT WRITTEN; awaiting operator approval)

Write gate (operator ruling 2026-10-03): nothing below has been written to Notion. The operator was asleep (19-Oct instruction: no questions), so the run saved the payload and did not wait at the gate. Decision Status is NEVER written by this pipeline.

## Target page
- COMPANIES MASTER page: Tatva Chintan Pharma Chem (TATVA)
- Page URL: https://www.notion.so/39bbb2b9d3ab81379187e5a370ea087f
- Page last edited (at fetch 2026-10-19): 2026-10-14T02:15:52Z. Re-fetch before writing; if edited since, re-check the Key Notes prefix.

## 1. update_properties
- Key Notes: PREPEND the line below, then the existing separator ` \|\| `, then the existing Key Notes text unchanged.

```
20-Oct-2026 \| Q2 FY27 RESULTS REVIEW (results + updated deck + call-cancellation notice; /run-quarterly A1-A5, A5 COMPLETE after 1 loop; NO CALL: company cancelled the 19-Oct call 56 min before start, "unforeseen circumstances", no new date). Revenue Rs 217.32 Cr +75.9% YoY; PAT Rs 21.45 Cr +116.3%; op EBITDA margin 18.72% (below 20-22% guide for a 2nd quarter, above 18% red line); mgmt cites solvent +60-100% and freight +100%. CASH: H1 cons CFO Rs -3.68 Cr on revenue +59.9%; working capital took 99% of pre-WC operating profit; net debt 1.22x (band 0.65x), 97.4% short-term. Receivable days 84.9 (H1) / 100.2 (TTM), below the 185 line: trigger (a) 2 of 3 legs met, which line governs is pending operator ruling 50. Profit shifting to overseas trading subs (no plant, staff or debt) = 28.3% of Q2 PAT while the parent margin fell to 15.05%. Same-evening deck restatement changed RoE (2.6% -> 6.3%) and Debt/EBITDA (4.30 -> 1.16), both favourable, called typographical. Q1 Rs 1.32 Cr exceptional still unexplained. Standalone DTA nearly used (cash tax up from Q3). SDA ~45% of Q2 revenue (one quarter). Verdict PROCEED WITH FLAGS; cash INDETERMINATE-WITH-DIRECTION (structural lean). Decision Status unchanged WATCHLIST / AVOID (operator-only). 20 IR questions.
```

- Analysis Date 1: 2026-10-20
- Decision Status: NOT WRITTEN (WATCHLIST / AVOID; no change proposed).
- Entry Price Max / MoS / CMP: not written (stale verdict-block entry zone vs properties is an open operator item on the page).

## 2. insert_content (position: end), as a new section headed
"## Q2 FY27 — Results Review (extraction-first pipeline; results + updated deck + call-cancellation notice; no call held) — 20-Oct-2026"

Insert in sequential calls, verbatim, complete tables (never summaries), pipes in cells escaped as `\|`:
1. runs/tatva-q2fy27/work/review_tatva_q2fy27.md, in full (ends with the PLAIN-LANGUAGE BRIEF, the YAML and the loop 1 change log). Split at its `## STEP` headings.
2. A3 forensics tables (completeness proof):
   - runs/tatva-q2fy27/work/forensics_results_tatva_q2fy27.md
   - runs/tatva-q2fy27/work/forensics_presentation_tatva_q2fy27.md
   - runs/tatva-q2fy27/work/forensics_notice_tatva_q2fy27.md
3. A5 audit verdict block:

```
A5 verdict: COMPLETE (loop 1 re-audit, runs/tatva-q2fy27/work/audit_tatva_q2fy27_loop1.md). Run 1 INCOMPLETE: F1 (CWIP +Rs 19.48 Cr wrongly tied to Dahej-III), C1 (guidance tally), M1-M3 (bear counters: FX gain line placement; parent margin -317 bps; SDA trigger on one quarter). All closed in loop 1. STYLE L1-L4 logged. Note: 12 of 14 results pages were scans transcribed from page images by the extraction agent (tesseract not installed); all statements foot. Re-verify standalone EPS 6.57 / 6.01 (page 10) on the image.
```

## 3. Tracker rows (not written; candidates for Claude web)
- Operator ruling 50 (receivable-days line for trigger (a)).
- Rescheduled earnings call or written Q&A (none announced).
- Q3 FY27 SDA revenue (monitorable M25), by 14-Feb-2027.
- Solvent and freight cost normalisation claimed "within Q3".
