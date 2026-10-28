# NOTION PAYLOAD: RAYMONDREL Q2 FY27 (NOT WRITTEN; awaits operator approval)

Batch instruction 28-Oct-2026: no Notion write in this run. This file is the payload for the operator to approve and for claude.ai to execute. Decision Status is never written.

Target page: COMPANIES MASTER / "Raymond Realty"
Page ID: 394bb2b9-d3ab-81ab-a206-e4fbc8b538a5
URL: https://app.notion.com/p/394bb2b9d3ab81aba206e4fbc8b538a5
Data source: collection://345bb2b9-d3ab-8032-9b46-000ba16ab827
Page state at fetch (28-Oct-2026, read-only): Decision Status WATCHLIST / AVOID; Current Market Price 571; Analysis Date 2026-10-26; newest Key Notes entry dated 26-Oct-2026 (ICICI Pru AIF Rs 210 Cr).
Run folder: runs/raymondrel-q2fy27/ on branch claude/qr-raymondrel-q2fy27-f76d61 (commit hash in the session report).

## 1. update_properties (fetch the page first; preserve every prior Key Notes entry)

- Key Notes: PREPEND this entry, then " \| " (escaped pipe), then the existing Key Notes text unchanged:

```
28-Oct-2026 \| Q2 FY27 full review /run-quarterly (Reg 33 results with PR + deck + ICICI Pru filing + ASR call of 28-Oct; A5 COMPLETE after 1 correction loop) [FILED res/PR; deck MGMT; ASR call MGMT unverified]: consol rev ops Rs 748.52 Cr +7.4% YoY; op EBITDA Rs 106.27 Cr +15.0%, margin 14.20% (+94 bps); authority-adjusted +8.3% / +10 bps; finance cost +70% to Rs 43.53 Cr; PAT Rs 53.06 Cr -11.8% (H1 -13.3%). Pre-sales Rs 902 Cr +98% (about +81% at economic interest); collections Rs 682 Cr +67%. H1 CFO -Rs 147 Cr (vs -319). Net debt Rs 916 Cr computed / 912 PR (Mar-26 658; +Rs 129 Cr/qtr); gross D/E 0.752: Risk #2 first signals LIT; Rs 1,000 Cr line not fired. MARGIN STOP BASIS-DEPENDENT (ruling pending): PR basis Q1 13.11% / Q2 15.21% (15% stop not fired); operating basis 11.61% / 14.20% (15% stop FIRED); authority-adjusted below 14% both quarters. If ruled fired, review proposes AVOID. Deck JDA revenue recognised Rs 1,930 Cr (p5) vs Rs 2,549 Cr (project slides): Rs 619 Cr gap unreconciled; BKC and Sion revenue above bookings. ICICI Pru AIF up to Rs 210 Cr into Ten X Realty West: instrument, coupon, put, tranches, TXRWL shareholding NOT DISCLOSED; call says OCPRS, 60% of project capital, near-zero coupon; RRL is a party. No warrant or AIF money in H1 equity (call "has infused" contradicted). Revenue guide dropped; 17-19% EBITDA guide kept vs H1 14.3%; 20% pre-sales guide implies H2 about -10.5%. Mahim-1 slipped to Q4 FY27; Thane owned parcel Q2 FY28. Verdict PROCEED WITH FLAGS; cash INDETERMINATE-WITH-DIRECTION. CMP Rs 548 (screener 28-Oct 08:48 IST), Rs 2 below MoS Rs 550; Promoter CONCERN caps. Rulings asked: margin stop threshold AND basis; net-debt test before/after warrant and AIF money. Decision Status unchanged (operator-only).
```

- Current Market Price: 548 (screener.in, 28-Oct-2026 08:48 IST). Operator to approve; the page's last value is 571 (26-Oct).
- Analysis Date: 2026-10-28.
- Decision Status: NOT WRITTEN. The review proposes AVOID only if the operator rules a margin stop fired.
- Management grade: NOT WRITTEN. A4 scores credibility 50% (grade C) on one scored quarter, archetype OVERPROMISER (provisional). The operator decides whether to adopt it.

## 2. insert_content (position: end; split across sequential inserts; escape | inside table cells as \|)

Insert, in this order, complete tables, never summaries:
1. Heading: "Q2 FY27 quarterly review (28-Oct-2026, /run-quarterly, results + PR + deck + ICICI Pru filing + ASR call)".
2. The full merged review: runs/raymondrel-q2fy27/work/review_raymondrel_q2fy27.md (Section A Role 4, Section B Role 5, Section C combined verdict, monitorables, FORWARD ESTIMATE INPUTS, PLAIN-LANGUAGE BRIEF with all five parts, Loop 1 change log). Omit only the trailing YAML block.
3. The A3 forensics tables, one per document (checklist table and findings table of each): runs/raymondrel-q2fy27/work/forensics_results_raymondrel_q2fy27.md, forensics_presentation_raymondrel_q2fy27.md, forensics_concall_raymondrel_q2fy27.md. The ICICI filing has no A3 by design; its terms sit in the review, Step 0C.
4. The A5 audit verdict and its re-audit section: runs/raymondrel-q2fy27/work/audit_raymondrel_q2fy27.md (verdict blocks, coverage counts, surviving bear counters, findings by type).
5. The operator brief: runs/raymondrel-q2fy27/operator-brief.md.

## 3. DOWNSTREAM SIGNAL TRACKER (proposed rows only; operator approval required)

Tracker rows were not supplied to this run (titles only). Candidates from review Step 5.5C:

| # | Signal | Case | Cadence | Reason (anchored) |
|---|---|---|---|---|
| 1 | TXRWL OCPRS terms and classification (securities-issue intimation; Q3 BS NCI vs borrowing) | B (create) | Event, then quarterly | The instrument decides the net-debt reading (CA R063 NOT DISCLOSED; call L486, L584-587, ASR) |
| 2 | BKC aviation height approval and RERA for upper floors | B (create) | Event | H2 Invictus BKC pre-sales depend on it (call L517-522, ASR; FND-16) |
| 3 | JDA revenue recognised vs JDA collections (deck p5/p7/p26) | B (create) | Quarterly | Tests I-2 and revenue quality; deck p5 Rs 1,930 Cr vs project rows Rs 2,549 Cr (R039, R478; PRE-A3-27) |
| 4 | Interest to government authorities (quarterly) and principal outstanding | A (attach to the net-debt row) | Quarterly | A debt-like leg outside gross debt; Rs 17 Cr in Q2 (deck l365; RES L717-719) |

Existing rows to update (values from this quarter's filings; each row's own update rules apply):
- "Q2 FY27 EBITDA margin vs two-quarter stop-loss (Q1 13%)": Q2 15.21% reported / 14.20% operating (RES L475-479). Basis-dependent; ruling pending.
- "Net debt vs Rs 1,000 Cr line (Rs 914 Cr at Q2, +Rs 90 Cr/qtr)": Rs 916 Cr computed / Rs 912 Cr PR; H1 pace +Rs 129 Cr per quarter.
- "H1 FY27 CFO vs model FY27 -Rs 600 Cr": H1 CFO -Rs 147.02 Cr (RES L574).
- "Warrant money received (Rs 102 Cr upfront)": not received in H1 (equity roll, RES-A3-13).
- "Thane Jekegram launch (RERA) in FY27 vs warrant objects Rs 247 Cr": deck dates the Thane owned parcel launch Q2 FY28 (deck l464).

Role 5.5 flag: all five existing rows are company-derived. Fewer than three external signals exist (OR-17 floor). Reopen for external signals: MMR registrations, housing-loan rates, cement and steel prices.

## 4. Not in this payload

- No Decision Status write.
- No companies/RAYMONDREL.md file (none exists; /finalize writes it).
- No X post; not flagged as a publish candidate.
