# A3 FORENSIC NOTES — Digitide Solutions Limited (DSSL) — Q1 FY27 — Investor Presentation

Source extract: `runs/dssl-q1fy27/work/extract_presentation_dssl_q1fy27.txt` (1495 lines, 34 pages)
Ledger reconciled: `runs/dssl-q1fy27/work/ledger_presentation_dssl_q1fy27.md` — 100% (all 34 SLIDES rows, all 554 NUMBERS tokens by slide, all 5 FOOTNOTES, all 28 LINE-ITEM rows read at cited lines and cross-checked against the extract; chart data labels re-verified against slide rasters slide_15/21/22/23/24.png).
Doctype rule applied: presentation. F1,F2,F3,F4,F5,F8,F9,F10,F11,F13,F14,F15,F17 = N.A. (no statements / notes / auditor report / board letter / balance sheet / share-count / transcript). F6, F7, F12, F16 = live. DROPPED_SLIDE and changed-baseline-vs-last-deck NOT COMPUTABLE (first quarterly run, no prior deck) — recorded, not fabricated.

## RECONCILIATION AGAINST REG 33 FILING / PRESS RELEASE
Every headline the task supplied ties to the deck exactly — no disagreement:
- Revenue Rs775.1cr = slide 22/33 L845-847/L1414 (775.1). OK
- EBITDA Rs76.9cr / 9.9% = slide 22 L852/L858, slide 33 L1428/L1434. OK
- Reported PAT Rs2.9cr = slide 22 L864, slide 33 L1466. OK
- Segment BPM Rs537.7cr = slide 23 L904 (537.7). OK
- T&D Rs237.4cr +20.3% YoY = slide 23 L914/L916. OK
- International Rs295.6cr +10.2% = slide 23 L993 (295.6, 38.1%), L998. OK
- TCV Rs205cr = slide 4/20 L143/L781. OK
- 26 logos = slide 4/20 L143/L782. OK
No deck figure contradicts the filing. The internal inconsistencies below are inside the deck, not deck-vs-filing.

---

## FINDINGS TABLE

| id | check | ledger ref | line / slide | verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| M1 | F16 (MECHANICAL_INCONSISTENCY) | T2 slide 23; T4 T&D row | L966-967 / slide 23 | "Tech & Digital share has risen to 32% and International business to 38% in Q4 FY26" | AMBIGUOUS | Header cites 32% / "Q4 FY26" while the slide's own data column is Q1 FY27 at 30.6% and its Q4 FY26 column is 31.1% — 32% matches neither. Adjudication: STALE COPY-PASTE header carried from the prior (Q4 FY26) deck, not a restatement (the data tables are internally consistent). Flatters T&D mix and reveals a drafting-control gap. A4 to confirm carryover, not restatement. |
| M2 | F16 (CHART_AXIS_SCALE) | T2 slide 24; axis ticks | L1106-1112 / slide 24 | axis ticks "700.0 … 820.0" (Revenue & YoY chart) | NEUTRAL-FACT | Revenue bar chart baseline truncated at 700.0 (not zero) on a 735.8→800.0 series, visually exaggerating a 5–9% band into a staircase and softening the 3.1% QoQ drop. Verified on raster: the other five charts on the slide (EBITDA, EBIT, PAT, Employees, DSO) are zero-based; only revenue is truncated. Presentation-framing that overstates growth momentum. |
| M3 | F16 (non-GAAP measure) | T3 #2/#5; T4 Adj PAT rows | L873-880 / L1474-1483 / slides 22,33 | "Adjusted PAT* … *Excludes exceptional items, including demerger-related expenses in Q1FY26, labour code impact in Q4FY26" | NEUTRAL-FACT | Non-GAAP add-back lifts prior comparatives (Q4FY26 -5.0 reported → 11.2 adjusted). Q1FY27 adjusted = reported = 2.9 (exceptional = 0.0), so this quarter is clean. Footnoted and consistent across both slides. Monitor exceptional-item recurrence. |
| M4 | F16 (UNIT_MISMATCH) | T2 slide 15 | L610 / slide 15 | "$2M-$6M+ savings per use case" | NEUTRAL-FACT | Only non-Rs figures in the deck; illustrative per-use-case Insurance saving, all sibling IMPACT bullets are % / x. Covered by the slide-3 currency caveat (L110). Immaterial to financials; no conversion needed for the Rs Cr series. |
| M5 | F16 (DECK_COLOR_INVERSE) | T2 slide 21 | L823-825 / slide 21 | "Client Concentration: Top 30 Clients … 57.7% … 59.5% … 176 bps" (amber DOWN-arrow) | CONFIRMATORY-NEGATIVE | Raster-confirmed: rising Top-30 concentration (+176 bps) shown with an amber down-arrow — the deck itself flags rising concentration as adverse. Revenue-at-risk concentration is increasing; a candid disclosure, not a data error. Monitor. |
| M6 | F16 (SOLE_SOURCE_DATA_POINT) | T2 slide 24 PAT chart | L1005, L1078 / slide 24 | PAT "3.0" (Q2'FY26), "-2.1" (Q3'FY26) | NEUTRAL-FACT | Raster-confirmed. These two interim-quarter PAT points appear only on this chart (slide 33 tabulates only Q1FY26/Q4FY26/Q1FY27). They corroborate the "two consecutive quarters of losses" claim (Q3FY26 -2.1, Q4FY26 -5.0). Captured for continuity; not independently cross-checkable in this doc. |
| H1 | F7 (hedge / attribution) | T4 EBITDA/margin rows | L835 / slide 22 | "EBITDA: Eased to ₹76.9 Cr (9.9% margin), driven by lower revenue and the impact of minimum wage revisions across states" | AMBIGUOUS | Margin compression to 9.9% (below the 11% FLAG-CASH tripwire; -131 bps YoY, -107 bps QoQ) is pre-emptively attributed to external wage revisions. This is the FIRST of the tripwire's two legs now printed. If Q2 FY27 also prints ~9%, the falsifier fires: Q4 FY26 compression is STRUCTURAL and the DaaS/CBaaS pivot dilutes unit economics. Direction unresolved by the deck. A4. |
| H2 | F7 (hedge / forward) | T2 slide 22 | L833-834 / slide 22 | "down 3.1% QoQ due to lower book-to-bill conversion and a disciplined approach to deal selection, including the renegotiation of low-margin contracts" | FORWARD-SIGNAL | "Lower book-to-bill conversion" = bookings not converting to revenue = near-term top-line softness. Deliberate exit/renegotiation of low-margin contracts will further pressure revenue but should aid margin — a self-declared revenue-for-margin trade. A4. |
| C1 | F6 (forward commitment) | T2 slide 27 | L1285-1287 / slide 27 | "Strengthen the Core … portfolio treatment underway" (with L1276 "fix, divest or exit") | FORWARD-SIGNAL | "Fix, divest or exit" of low-margin / non-profitable areas is status = UNDERWAY. Signals future portfolio/divestiture actions and further revenue attrition. Milestone to track quarter-over-quarter. |
| C2 | F6 (forward commitment) | T2 slide 27/31 | L1290-1291, L1392-1396 / slides 27,31 | "disciplined M&A in BPaaS, healthcare RCM, and Western access … must be margin as well as EPS accretive" | FORWARD-SIGNAL | Inorganic-growth intent (status SELECTIVE) = potential capital deployment / equity issuance risk against the ~Rs90cr PPE / capital-intensity monitorable. Watch funding route. |
| S1 | F12 (segment forensics) | T4 slide 23 EBITDA rows | L949-957 / slide 23 | Tech & Digital EBITDA "18.9  8.0%  -408 bps  -156 bps" | FORWARD-SIGNAL | The strategic growth segment (T&D, +20.3% YoY revenue) carries the thinnest and most volatile segment EBITDA margin — 8.0%, down 408 bps QoQ / 156 bps YoY, below BPM's 13.5%. The pivot the thesis rests on is currently margin-DILUTIVE, directly corroborating the FLAG-CASH tripwire (H1). A4. |
| S2 | F12 (working-capital proxy) | T2 slide 24 DSO chart | L1068-1072 / slide 24 | DSO "91  82  79  75  82" | CONFIRMATORY-NEGATIVE | Raster-confirmed. DSO (billed + unbilled) rose 75→82 days QoQ (+7) after four quarters of improvement — confirms monitorable (c) receivables tail worsening and feeds monitorable (d) cumulative CFO/PAT 0.529x near the 0.50 cash-conversion cap. Cash-conversion risk. |

Derived note (T1, tax): Slide 33 P&L implies an elevated effective tax rate of ~73% in Q1 FY27 (Tax 8.0 on PBT 10.9, L1456/L1462), vs ~51% in Q1 FY26 (10.3/20.0). No tax note / deferred-tax breakout exists in the deck, so the formal F8 forensic cannot run (marked N.A.), but the ETR consumes most of the thin PBT and is worth an A4 question (non-deductible exceptional/demerger items, DTA non-recognition, or prior-year adjustment?). Classification AMBIGUOUS.

---

## CHECKLIST SCORECARD (all 17 — no blanks; GATE A3)

| Check | Status | One-line basis |
|---|---|---|
| F1 ZERO-STANDING | N.A. | Investor presentation, no statements/notes/auditor report; ledger confirms 0 zero-standing line items across slides 22/23/33 (Exceptional Items 8.9/16.1/0.0 is a period change, not a standing zero). |
| F2 STANDALONE vs CONSOLIDATED | N.A. | Deck presents one consolidated set of figures; no standalone column to decompose. |
| F3 SHELL-ENTITY | N.A. | Investor presentation, no statements/notes/auditor report; no entity-level cost lines. |
| F4 UNAUDITED CONTRIBUTION | N.A. | No auditor "Other Matters" / component-auditor disclosure in a presentation. |
| F5 GOING CONCERN / EoM | N.A. | No auditor report / EoM paragraph; investor presentation. |
| F6 FORWARD-COMMITMENT MINING | FINDING | "portfolio treatment underway" (L1287), disciplined M&A intent (L1392-1396) — see C1, C2; commitment register below. |
| F7 HEDGE PHRASE MINING | FINDING | Margin compression attributed to "minimum wage revisions" (L835, H1) and "lower book-to-bill conversion" + low-margin renegotiation (L833-834, H2). |
| F8 TAX FORENSICS | N.A. | Investor presentation, no tax note / deferred-tax breakout. (Noted: single P&L tax line implies ~73% ETR Q1FY27 — carried to A4 as derived note T1, not a formal F8 finding.) |
| F9 OCI FORENSICS | N.A. | No OCI / actuarial disclosure in a presentation. |
| F10 SHARE COUNT / DILUTION | N.A. | Deck carries no share count, paid-up capital, or basic/diluted EPS (slide 8 shareholding % is ownership structure, not dilution). |
| F11 RESERVES / NET WORTH | N.A. | No balance sheet, reserves, or net-worth figure in the deck. |
| F12 SEGMENT FORENSICS | FINDING | T&D segment EBITDA collapsed to 8.0% (-408 bps QoQ, S1) and DSO rose 75→82 days (S2), slide 23/24. Segment assets/liabilities not disclosed (that sub-check N.A.). |
| F13 BOARD OUTCOME | N.A. | No board's report / AGM notice / AR-approval / director-term letter; investor presentation. |
| F14 NOTE-DRAFTING INCONSISTENCY | N.A. | No notes vs auditor-letter pairing to compare. (The stale slide-23 header is captured under F16 M1, not F14.) |
| F15 ENTITY LIST DIFFS | N.A. | No consolidation entity schedule and no prior-quarter deck to diff. |
| F16 PRESENTATION-SPECIFIC | FINDING | Stale header 32%/Q4FY26 (M1), truncated revenue axis (M2), non-GAAP Adjusted PAT (M3), USD unit mismatch (M4), colour-inverse concentration (M5), sole-source PAT points (M6). DROPPED_SLIDE / changed-baseline-vs-last-deck NOT COMPUTABLE (no prior deck) — explicitly skipped. |
| F17 CONCALL SILENCE AUDIT | N.A. | Investor presentation, no transcript. Monitoring-checklist coverage folded into the narrative below (not a scored silence audit). |

---

## COMMITMENT REGISTER (F6)

| commitment | implied date | note / slide ref | status word |
|---|---|---|---|
| Get unified — one enterprise operating model, leadership in place | now / current | slide 27 L1283-1284 | LIVE (completed) |
| Strengthen the Core — fix / divest / exit low-margin BPM areas | ongoing, near-term | slide 27 L1285-1287, L1276 | underway (IN MOTION) |
| Go West, Go Digital — compete as challenger, AI at core, deepen international/digital mix | ongoing | slide 27 L1288-1289 | ACCELERATING |
| Go all out — disciplined M&A in BPaaS, healthcare RCM, Western access; margin+EPS accretive | future / opportunistic | slide 27/31 L1290-1291, L1392-1396 | SELECTIVE (intends to) |
| Renegotiation of low-margin contracts / disciplined deal selection | ongoing | slide 22 L833-834 | underway |
| Added Adobe as new Global Silver Partnership | this quarter | slide 20 L791-793 | completed |

---

## MONITORING-CHECKLIST COVERAGE (phase-1 evidence-gate record; no Notion page)
- BINDING TRIPWIRE (FLAG-CASH): Q1 FY27 EBITDA margin = 9.9% (slide 22 L858), below the 11% line — LEG 1 of the "two consecutive quarters" falsifier is now printed. Q2 FY27 is the decisive read. Elevated via H1/S1. RAISED for A4 and phase-3 monitoring.
- (a) As-a-Service (DaaS/CBaaS) unit economics — NOT disclosed. Deck gives ACV totals (~2/~13/6 Cr, slide 14) and "~70% revenue annuity-based" (slide 7 L187-189), but no per-unit As-a-Service economics. Monitorable (a) NOT cleared.
- (b) ~Rs90cr PPE capital-intensity gap — NOT disclosed. No balance sheet / capex plan in the deck. Monitorable (b) NOT cleared.
- (c) receivables ageing tail — CORROBORATED WORSE. DSO 75→82 days QoQ (S2). ECL not disclosed.
- (d) cumulative CFO/PAT 0.529x near 0.50 cap — no cash-flow statement; DSO deterioration (S2) is directionally adverse for cash conversion.
- (e) governance (Cybercons, related-party advances, RMC zero meetings) — SILENT. Slide 18 board bios carry no DIN, no committee-meeting or related-party disclosure.

## QUESTIONS FLAGGED FOR A4 (FORWARD-SIGNAL / AMBIGUOUS)
1. (H1/S1) Is the 9.9% Q1 FY27 EBITDA margin genuinely wage-revision-driven and reversible, or structural to the T&D / As-a-Service pivot (T&D segment EBITDA only 8.0%)? — the FLAG-CASH falsifier.
2. (H2) Quantify "lower book-to-bill conversion": how much Q1 revenue softness is deliberate low-margin exit vs demand weakness, and what is the book-to-bill ratio?
3. (M1) Confirm the slide-23 "32% … Q4 FY26" header is a stale carryover, not a restatement of Q4 FY26 T&D mix (data table shows 31.1% / 30.6%).
4. (C1/C2) Portfolio "divest or exit" scope and the M&A funding route (cash vs equity) against the Rs90cr capital-intensity gap.
5. (T1) Why is the Q1 FY27 effective tax rate ~73% of PBT, and is it recurring?
