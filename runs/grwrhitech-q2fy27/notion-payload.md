# Notion payload: GRWRHITECH Q2 FY27 (NOT WRITTEN)

Status: NOT WRITTEN. Two gates block the write.
1. A5 verdict is INCOMPLETE after the one permitted correction loop (one FACTUAL item, F3, wording only). The orchestrator rule says STOP and ask the operator before a second iteration. The save runs only after A5 COMPLETE.
2. The write gate (operator ruling 2026-10-03) needs the operator's explicit approval in the run. The operator was away; no approval exists.

Operator choices:
- (a) Approve loop 2: A4 removes the transfer-price lean (review l.183, l.524, l.588, l.692, l.694), A5 re-audits, then this payload is written.
- (b) Accept the review with F3 as a logged open item, and approve the write of this payload as it stands.

## Target
- Page: Garware Hi-Tech Films Limited, COMPANIES MASTER
- URL: https://app.notion.com/p/35fbb2b9d3ab811ab613eb3cc3456141
- Page ID: 35fbb2b9-d3ab-811a-b613-eb3cc3456141

## update_properties
- Key Notes: PREPEND the line below, then " | ", then the existing Key Notes text unchanged.
- Decision Status: DO NOT WRITE (operator-only; stays WATCHLIST).
- No other property changes.

Key Notes line:
```
23-Oct-2026 | Q2 FY27 /run-quarterly (results + embedded deck; Role 5 not run, call 23-Oct 11:30): rev 695.53 Cr (+22.09% YoY, +9.86% QoQ); op EBITDA ex-OI 169.47 / 24.37% (+340 bps YoY, -280 bps QoQ); reported EBITDA incl OI 27.17%; PAT 129.44; EPS 55.71 (Q1 57.10); H1 CFO/PAT 0.75x group, 0.36x parent; no thesis-broken trigger fired; TPU not commissioned (on track Q3 FY27); MPCB Rs 25 lakh BG forfeiture absent from results; guidance 27% +/-2% incl OI implies H2 ~25.1%; next test Q3 ex-OI margin bull >=22.3% / bear <=19.5%; protocol verdict PROCEED WITH FLAGS; A5 INCOMPLETE (F3 wording, loop 2 pending operator). Decision Status unchanged (operator-only).
```

## insert_content (position: end), in this order, split across sequential inserts
1. Heading: "Quarterly Review: Q2 FY27 (A4, 23-Oct-2026)". Body: runs/grwrhitech-q2fy27/work/review_grwrhitech_q2fy27.md in full (complete tables, the Questions-for-Management table and the PLAIN-LANGUAGE BRIEF; drop only the trailing YAML block). Escape `|` inside table cells as `\|`.
2. Heading: "A3 Forensics: Q2 FY27". Body: the F1-F17 scorecard and findings table from runs/grwrhitech-q2fy27/work/forensics_grwrhitech_q2fy27.md.
3. Heading: "A5 Audit Verdict: Q2 FY27". Body: verdict lines and finding tables from runs/grwrhitech-q2fy27/work/audit_grwrhitech_q2fy27.md (iteration 0: INCOMPLETE, C1/M1/M2/M3/F1/F2, all fixed) and runs/grwrhitech-q2fy27/work/audit_grwrhitech_q2fy27_loop1.md (iteration 1: INCOMPLETE, F3 open).

## Flags for the Key Notes reader (no trigger fired)
- MPCB bank-guarantee forfeiture (Reg 30, 22-Oct-2026) not mentioned in results, notes or deck.
- Record conflict still open: price-zone table says AVOID above Rs 5,000; Decision Status says WATCHLIST.
