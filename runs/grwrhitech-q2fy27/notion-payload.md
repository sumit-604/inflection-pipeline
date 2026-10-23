# Notion payload: GRWRHITECH Q2 FY27 (NOT WRITTEN)

Status: NOT WRITTEN. Two gates block the write.
1. The merged A5 verdict is INCOMPLETE after the last allowed loop. One FACTUAL label fix is open: NF2. The spoken "26.30%" (call L0049) is the filed H1 PBT margin, not an ASR error. Review 7A should read CONFIRMED; align review l.24, l.600, l.630, l.903, l.921, l.996, l.1039. No number or verdict changes. The save runs only after A5 COMPLETE, or when the operator accepts NF2 as an open item.
2. The write gate (operator ruling 2026-10-03) needs the operator's explicit approval in the run. No write approval exists.

## Target
- Page: Garware Hi-Tech Films Limited, COMPANIES MASTER
- URL: https://app.notion.com/p/35fbb2b9d3ab811ab613eb3cc3456141
- Page ID: 35fbb2b9-d3ab-811a-b613-eb3cc3456141

## update_properties
- Key Notes: PREPEND the line below, then " | ", then the existing Key Notes text unchanged.
- Decision Status: DO NOT WRITE (operator-only; stays WATCHLIST).
- No other property changes (Promoter Verdict and Management Grade unchanged; no promoter on the call; Role 5 credibility ratio ND).

Key Notes line:
```
23-Oct-2026 | Q2 FY27 /run-quarterly MERGED (results + embedded deck + ASR call, no company transcript): rev 695.53 Cr (+22.09% YoY; two-year 5.8% a year); op EBITDA ex-OI 24.37% (+340 bps YoY, -280 bps QoQ; up to 11 Cr one-off US tariff refund inside H1 per call, 16 Cr more due Q3); PAT 129.44; EPS 55.71; H1 CFO/PAT 0.75x (SA 0.36x); finance cost not lease alone; TPU "yet to start commissioning" 23-Oct; ADD not imposed; FY28 3,000+ / 28-28.5% verbal only; MPCB Rs 25 lakh BG forfeiture (old boiler run during trials, per call) absent from results; only the sales director spoke; no thesis-broken trigger fired; next test Q3 margin incl OI before refund vs Q3 FY26 18.95% (bull >=22.7% / bear <=18.95%); verdicts Role 4 and Role 5 PROCEED WITH FLAGS; net impact WEAKENED (mild); A5 INCOMPLETE on NF2 (label only). Decision Status unchanged (operator-only).
```

## insert_content (position: end), in this order, split across sequential inserts
1. Heading: "Quarterly Review: Q2 FY27 (merged results + concall, 23-Oct-2026)". Body: runs/grwrhitech-q2fy27/work/review_grwrhitech_q2fy27.md in full: Section A (Role 4), Section B (Role 5), Section C (combined verdict), flags, monitorables, Questions-for-Management with call status, and the PLAIN-LANGUAGE BRIEF; drop only the trailing YAML block. Escape `|` inside table cells as `\|`.
2. Heading: "A3 Forensics: Q2 FY27". Body: the F1-F17 scorecards and findings tables from runs/grwrhitech-q2fy27/work/forensics_grwrhitech_q2fy27.md (results) and runs/grwrhitech-q2fy27/work/forensics_concall_grwrhitech_q2fy27.md (concall).
3. Heading: "A5 Audit Verdicts: Q2 FY27". Body: verdict lines and finding tables from, in order:
   - results pass: audit_grwrhitech_q2fy27.md (iter 0), audit_grwrhitech_q2fy27_loop1.md (iter 1), audit_grwrhitech_q2fy27_loop2.md (iter 2), all INCOMPLETE, every item fixed in the merged review;
   - merged pass: audit_grwrhitech_q2fy27_merged.md (iter 0), audit_grwrhitech_q2fy27_merged_loop1.md (iter 1), audit_grwrhitech_q2fy27_merged_loop2.md (iter 2: INCOMPLETE, NF2 open).
   All under runs/grwrhitech-q2fy27/work/.
4. Heading: "Operator Brief: Q2 FY27". Body: runs/grwrhitech-q2fy27/operator_brief_grwrhitech_q2fy27.md in full.

## Flags for the Key Notes reader (no trigger fired)
- Concall source is a machine transcript; re-check every [ASR] number against the company transcript when filed.
- MPCB bank-guarantee forfeiture (Reg 30, 22-Oct-2026) not mentioned in results, notes or deck.
- Record conflict still open: price-zone table says AVOID above Rs 5,000; Decision Status says WATCHLIST.
