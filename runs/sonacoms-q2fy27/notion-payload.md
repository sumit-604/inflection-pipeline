# NOTION PAYLOAD — SONACOMS Q2 FY27 (WRITTEN 2026-10-29 on operator approval; see work/run_log.md. Tracker rows in section 3 NOT written)

Batch instruction 28-Oct-2026: no Notion write in this run. This file is the payload for the operator to approve and for claude.ai to execute. Decision Status is never written.

Target page: COMPANIES MASTER / "Sona BLW Precision Forgings"
Page ID: 36dbb2b9-d3ab-81cf-879a-c0b005eaa4ae
URL: https://app.notion.com/p/36dbb2b9d3ab81cf879ac0b005eaa4ae
Data source: collection://345bb2b9-d3ab-8032-9b46-000ba16ab827
Page state at fetch (28-Oct-2026 10:02 IST): Decision Status WATCHLIST; Current Market Price 782; Analysis Date 2026-10-26; newest Key Notes entry dated 26-Oct-2026.
Run folder: runs/sonacoms-q2fy27/ on branch claude/qr-sonacoms-q2fy27-c7173c (commit hash in the session report).

## 1. update_properties (fetch the page first; preserve every prior Key Notes entry)

- Key Notes: PREPEND this entry, then " \| " (escaped pipe), then the existing Key Notes text unchanged:

```
28-Oct-2026 \| Q2 FY27 full review /run-quarterly (results + deck + PR + ASR call of 26-Oct; A5 COMPLETE after 1 correction loop) [FILED res; deck; PR; ASR call]: consol rev ops Rs 1,535.84 Cr +34.9% YoY; owners PAT Rs 223.40 Cr +29.3%; op EBITDA margin 23.20% rev ops / 22.51% ex-forex (-219 / -243 bps YoY); parent margin -343 bps, group held by subsidiary layer. CFO/PAT H1 1.48x printed, 0.78x ex-payables (1.00x a year ago); ST borrowings Rs 234 -> 462 Cr. C1 MISSED (conceded on call), C2 not evidenced (scored DROPPED), C3 DELAYED: provisional credibility 8.3% on 3 scored commitments, grade D, archetype EVASIVE (one quarter only; page shows grade A). DENSO JV1 close guided end-Dec/Jan [ASR]; accounting route unstated (Note 5 says JV and subsidiary); 49% at EV Rs 1,750 Cr = Rs 857.5 Cr pre-tax, about 2.2x proxy sales vs about 10.1x for Sona; carve-out earnings NOT FOUND. Auditor signed about 33 min before board (second quarter). Railway AMBER / UNVERIFIED. Indicative FY27E/FY28E owners PAT Rs 851 / 1,074 Cr (lower 808 / 994), 64.5x / 51.1x at Rs 879 (screener 28-Oct 08:48 IST); not Role 1. Rulings pending: margin basis (incl/ex forex), cash leg (printed/ex-payables). No thesis-broken trigger fired. Decision Status unchanged (operator-only).
```

- Current Market Price: 879 (screener.in, 28-Oct-2026 08:48 IST). Operator to approve; the page's last value is 782 (26-Oct, pre-results).
- Analysis Date: 2026-10-28.
- Decision Status: NOT WRITTEN.
- Management grade: NOT WRITTEN. A4 flags a provisional change from A to D on one scored quarter; the operator decides whether to adopt it.

## 2. insert_content (position: end; split across sequential inserts; escape | inside table cells as \|)

Insert, in this order, complete tables, never summaries:
1. Heading: "Q2 FY27 quarterly review (28-Oct-2026, /run-quarterly, results + deck + PR + ASR call)".
2. The full merged review: runs/sonacoms-q2fy27/work/review_sonacoms_q2fy27.md (Section A Role 4, Section B Role 5, Section C combined verdict, FORWARD ESTIMATE INPUTS, PLAIN-LANGUAGE BRIEF with all five parts). Omit only the trailing YAML block.
3. The A3 forensics tables, one per document: runs/sonacoms-q2fy27/work/forensics_results_sonacoms_q2fy27.md, forensics_presentation_sonacoms_q2fy27.md (with loop 1 addendum), forensics_pressrelease_sonacoms_q2fy27.md, forensics_concall_sonacoms_q2fy27.md (checklist table and findings table of each).
4. The A5 audit verdict and its re-audit section: runs/sonacoms-q2fy27/work/audit_sonacoms_q2fy27.md (verdict blocks, coverage counts, surviving bear counters, findings by type).
5. The operator brief: runs/sonacoms-q2fy27/operator-brief.md.

## 3. DOWNSTREAM SIGNAL TRACKER (proposed rows only; Case B create; operator approval required)

Tracker rows were not supplied to this run. Candidates from review Step 5.5C:
| # | Signal | Cadence | Reason (anchored) |
|---|---|---|---|
| 1 | India E2W/E3W registrations (Vahan) | monthly | 2W/3W traction motors "almost 50% quarter on quarter" [ASR, call L060]; E2W/E3W share 10% FY26 to 14% H1 FY27 (deck L297); Rs 16.3 bn of Q2 adds are 2W motors and controllers (deck L201-203) |
| 2 | Consolidated op EBITDA margin incl. and ex-forex | quarterly | gate variable needs a defined basis; already proposed 26-Oct [NOTION MEMORY] |
| 3 | Trade payables and ST borrowings vs CFO | half-yearly | cash leg passed on payables; already proposed 26-Oct [NOTION MEMORY] |
| 4 | DENSO JV1 close | event | guided end-Dec 2026, may slip to Jan 2027 [ASR, call L439-440]; breaks like-for-like |
| 5 | Steel, copper and freight indices | monthly | management names steel, copper, oil derivatives and freight "nearly doubled" [ASR, call L064-067] |

Role 5.5 gate (OR-17): fewer than three EXTERNAL tracker signals exist for this entity; reopen Role 5.5 in claude.ai.
