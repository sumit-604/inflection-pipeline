# Notion payload: TEJASNET Q2 FY27 (NOT WRITTEN; operator approval not given in this run)

Target page: 📡 Tejas Networks, COMPANIES MASTER
URL: https://app.notion.com/p/345bb2b9d3ab819c8523e9d04213694a
Page state at fetch: 2026-10-23 02:05 UTC. Re-fetch before any write; the page may have changed.
Never write Decision Status (stays WATCHLIST; operator-only).

## 1. update_properties

Key Notes: PREPEND the line below, then " \| ", then the existing Key Notes text unchanged (10 entries at fetch).

```
24-Oct-2026 | /run-quarterly Q2 FY27 (A1-A5 pipeline; results + filed transcript + deck; A5 COMPLETE after 2 loops). Verdict PROCEED WITH FLAGS. Rev Rs 405.68 Cr (+55% YoY, +0.9% QoQ); PAT Rs -206.94 Cr; op EBITDA margin -26.3%. YoY PBT gain 196.11 fully explained by base charge 145.43 + warranty release + ECL swing (208.76). H1 CFO -311.93, FCF -709.11. Net debt ex-lease Rs 4,384.39 Cr (headroom 115.61 to the 4,500 break); incl. leases 4,518.90: operator to rule the binding definition. Q3 at Q2 pace 4,491.78, at H1 pace 4,811.25. BV/share Rs 139.33 (below Rs 140: #9 RED). Checklist #2 AMBER, #4 RED, #6 AMBER toward RED (intl 12% of revenue, 4% of book), #7 AMBER, #8 UNKNOWN, #9 RED, #10 AMBER (86.53). DTA and QIP silent a second call: RED per pre-registered rule. BSNL: deck says TCS LoI only; POs partial and spoken; value withheld; operator to reconfirm the 27-Aug ruling on PO evidence. EBITDA-positive date dropped. Credibility 55.0% Grade C, EVASIVE. No thesis-broken trigger fired. Re-weighting FIRES (Q1 pre-registered condition met). Entry Rs 247-309 not confirmed; Role 1 recompute. Gate: net debt at 31-Dec-2026. WATCHLIST, not held. Decision Status unchanged (operator-only).
```

(Escape each `|` inside the line as `\|` when writing; the line above shows one separator after the date.)

## 2. insert_content (position: end), in sequential inserts

Insert A, heading: "Q2 FY27 /run-quarterly review (24-Oct-2026, A1-A5 pipeline)". Body: the full text of
runs/tejasnet-q2fy27/work/review_tejasnet_q2fy27.md, lines 1-976 verbatim (everything above the YAML block), split across inserts at the section headings:
- A1: lines 1-319 (change log, preamble, Role 4 Steps 0-5.5)
- A2: lines 320-461 (Role 4 Steps 6-8.5, incl. the 22-row Questions for Management)
- A3: lines 462-890 (Role 5 Steps 0-8F)
- A4: lines 891-976 (Combined verdict and PLAIN-LANGUAGE BRIEF: summary, sector, business model, competition, forward map)
Complete tables, never summaries. Escape `|` inside cells as `\|`.

Insert B, heading: "Q2 FY27 forensic checklist (A3)". Body: the F1-F17 scorecard table and the findings table from each of
- runs/tejasnet-q2fy27/work/forensics_results_tejasnet_q2fy27.md (incl. ADDENDUM loop 1)
- runs/tejasnet-q2fy27/work/forensics_concall_tejasnet_q2fy27.md (incl. section 7 ADDENDUM loop 1)
- runs/tejasnet-q2fy27/work/forensics_presentation_tejasnet_q2fy27.md

Insert C, heading: "Q2 FY27 completeness audit (A5)". Body:
- Verdict: COMPLETE (loop 2). Run 1 INCOMPLETE (4 MISSING, 2 CONTRADICTION, 3 FACTUAL); loop 1 resolved all nine; loop 2 resolved M1b (ledger count-test header).
- Open STYLE notes: S4, S9, S10, S11 (logged, no re-run).
- Count reconciliation: results 864 ledger rows (851 structured + 13 MISSING_FROM_STRUCTURED), concall 52 turns (327 rows), presentation 13 pages (210 rows); 0 orphans.
- Source: runs/tejasnet-q2fy27/work/audit_tejasnet_q2fy27.md, sections "Re-audit (loop 1)" and "Re-audit (loop 2)" verbatim.

## 3. Tracker rows
None written. A4 Step 5.5C proposes 5 new dependency rows (review lines 307-313); they go through the operator gate in claude.ai.

## 4. Flags for the operator (decision stays human)
- Rule the binding net-debt definition (ex-lease 4,384.39 vs incl. lease 4,518.90 against the 4,500 break).
- Reconfirm the 27-Aug BSNL ruling on PO evidence (filed deck says LoI only, PL187).
- Book value per share Rs 139.33 is below the Rs 140 red line.
- Probability re-weighting fires; Role 1 to recompute the entry zone.
