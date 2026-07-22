# A3 FORENSIC NOTES — Atlanta Electricals Ltd, Q1FY27, doctype: presentation (Reg 30 press release / earnings release)

Source extract: `runs/atlantaelec-q1fy27/work/extract_pressrelease_atlantaelec_q1fy27.txt` (156 lines, 3 pages, 100% coverage)
Ledger reconciled: 91/91 discrete disclosure units read verbatim at cited lines = 100%.
Model: claude-opus-4-8.

CROSS-DOC POSTURE: This is the THIRD document for an already-reviewed quarter (Reg 33 filing + investor deck already extracted/enumerated/forensically reviewed; merged A4 exists). Verified consolidated spine (forced-OCR-clean filing): Revenue 466.33, Other Income 2.32, CON operating EBITDA ex-OI 77.10 / 16.53%, PAT 46.84 / 10.04%, Q4FY26 CON Revenue 747.62 / PAT 102.19 / margin 20.00%. On this doctype the load-bearing checks are F16 (dropped/reframed/added disclosures) plus F6 forward-commitment mining; F1-F5, F8-F13, F15 are structurally N.A. (no auditor report, no balance sheet, no segment data, no entity list, single-agenda transmittal); F17 is N.A. (no concall transcript — silence audit folded into F16).

---

## RECONCILIATION AGAINST VERIFIED SPINE (every highlights-table figure)

| Row | Press release (line) | Verified spine | Tie? |
|---|---|---|---|
| Revenue Q1FY27 | 466.33 (73) | 466.33 | EXACT |
| EBITDA* Q1FY27 | 77.10 / 16.5% (74,75) | 77.10 / 16.53% | EXACT (rounds) |
| PAT Q1FY27 | 46.84 / 10.0% (76,77) | 46.84 / 10.04% | EXACT (rounds) |
| Col-4 Revenue (labelled "Q4FY25") | 747.62 (73) | Q4FY26 = 747.62 | value = Q4FY26, LABEL WRONG |
| Col-4 EBITDA | 149.56 / 20.0% (74,75) | Q4FY26 margin 20.00% | value = Q4FY26, LABEL WRONG |
| Col-4 PAT | 102.19 / 13.7% (76,77) | Q4FY26 PAT 102.19 | value = Q4FY26, LABEL WRONG |
| Q1FY26 comps | 315.11 / 48.78 / 15.5% / 31.14 / 9.9% (73-77) | internally consistent | YoY math ties |

Conclusion: every Q1FY27 figure ties EXACTLY to the verified filing. The 4th column carries the verified Q4 **FY26** numbers under a "Q4FY25" header — a period-label error, not a data error (assessed F14/F16 below). Other Income 2.32 is dropped from the release, but EBITDA is defined ex-OI so the omission is internally consistent.

---

## FINDINGS TABLE

| id | check | ledger row | line/slide | verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-F6-1 | F6 | 5.13,5.14,5.16-5.18, 6.7-6.14 | 111, 116-117, 134-140 | "development of the 400 kV transformer at Vadod and 765 kV transformer at Atlanta Trafo remains on track"; "commissioning its Inverter Duty Transformer facility, progressing with Tank & Radiator backward integration" | FORWARD-SIGNAL | 8 undated commitments feed the Role 5 promise-vs-delivery tracker; none carry a date/capex/target so next quarter must show status transitions (on track -> commissioned). IDT + Tank/Radiator backward-integration are Section-8 items 6 & 7. |
| A3-F14-1 | F14 | 2.1-2.5 | 72 | header reads "Q4FY25" over values 747.62 / 149.56 / 20.0% / 102.19 / 13.7% | NEUTRAL-FACT | Drafting error: column header is one fiscal year stale; the numbers are the verified Q4 **FY26** consolidated figures. Cosmetic in isolation; material via F16-1. |
| A3-F14-2 | F14 | 4.7, 5.8 | 91-92, 105 | "Order of Rs. 291.68 crore order from Rajashthan Rajya Vidhyut Prasaran Nigam Ltd." | NEUTRAL-FACT | Entity name misspelled ("Rajashthan Rajya Vidhyut Prasaran" vs Rajasthan Rajya Vidyut Prasaran) and duplicated word "Order ... order"; verbatim twice (4.7-4.10 and 5.8-5.11). Cumulative drafting-quality data point. |
| A3-F16-1 | F16 | 2.1-2.5 | 72-77 | table shows only Q1FY27 / Q1FY26 / YoY% / "Q4FY25"; "+105 Bps" YoY, no QoQ | FORWARD-SIGNAL / lean-bear | No QoQ P&L column, and the sequential quarter is mislabelled/stale. This obscures a **-350 bps sequential EBITDA-margin compression** (Q4FY26 20.0% -> Q1FY27 16.5%) and a -35% sequential PAT drop (102.19 -> 46.84). The +105 bps YoY headline is real but a reader cannot see the QoQ step-down. Direct read-through to the Voltamp Q4FY26 sector margin shock (Notion tripwire) and Section-8 item 3 (margin below 18-20% green band; 16.5% is also below the 17% two-quarter red line — quarter 1 of 2). |
| A3-F16-2 | F16 | 5.3, 5.6, 5.7 | 97-104 | "Q1 FY27 order inflows of ₹972.42 crore"; "Over 55% of the order book comprises 220 kV transformers, while 400 kV transformers and reactors contribute nearly ₹275 crore" | FORWARD-SIGNAL | NEW disclosures the investor deck did not break out: (a) quarterly order INFLOW Rs 972.42 cr — vs Section-8 item 1 green band of only Rs 600-700 cr/qtr, i.e. inflow ran ~40% above the green threshold; (b) EHV/voltage-class split of the order book (400 kV+reactors ~Rs 275 cr; 220 kV >55%) that the deck left unquantified. Both are additive positives feeding Section-8 items 1 & 2. |
| A3-F16-3 | F16 | (absence) | whole doc | SBPDCL / debarment: no mention anywhere in the 156-line extract | CONFIRMATORY-NEGATIVE | Silence on the SBPDCL 2-year debarment (Notion active tripwire, Section-8 item 8). No re-testing outcome, no Bihar in-field inspection update, no acknowledgement. Sustained silence on a watch-item = confirmatory negative; carries the queued concall questions forward to the Aug 2026 call. |
| A3-F16-4 | F16 | 2.6 | 78 | "*EBITDA excluding other income" | NEUTRAL-FACT | EBITDA is cleanly defined ex-OI here and ties to the verified 77.10 / 16.53%. This CONTRADICTS the same-day investor deck slide-27 EBITDA mislabel (deck F16-1). Same issuer, same day, two different EBITDA presentations — a definitional-consistency governance data point; the press-release version is the correct one. |
| A3-F16-5 | F16 | 4.7-4.10, 5.8-5.11 | 91-94, 105-108 | "₹291.68 crore order from Rajashthan Rajya Vidhyut Prasaran Nigam Ltd. (RRVPNL)" | FORWARD-SIGNAL | RVPN/RRVPNL is a named state utility on the thesis SBPDCL-cascade watch-list. Here it appears as a **CUSTOMER placing a large order**, not a debarring authority. Signal direction is POSITIVE: a cascade-risk counterparty is in a commercial-buy relationship, materially lowering the modelled probability of a second-utility debarment. A4 should downweight cascade risk accordingly. |
| A3-F16-6 | F16 | 5.1-5.3 | 97-98 | "Order book stood at ₹3,116.63 crore ... 25.0% QoQ growth, with Q1 FY27 order inflows of ₹972.42 crore" | AMBIGUOUS | Roll-forward does not close: implied opening OB = 3,116.63/1.25 = 2,493.30; opening + inflow - revenue executed = 2,493.30 + 972.42 - 466.33 = 2,999.39, vs stated closing 3,116.63 (~Rs 117 cr unreconciled). Either the 25.0% QoQ is rounded, revenue is not fully drawn from the book, or the OB is measured gross of something (GST/escalation). Order-book definition basis is undisclosed — feed A5 arithmetic and an A4 clarification question. |

---

## CHECKLIST SCORECARD (all 17)

| Check | Status | Basis |
|---|---|---|
| F1 ZERO-VALUE STANDING LINE ITEMS | N.A. | Ledger `zero_standing = 0`; the sole financial table (20 cells) has no zero/nil/dash cells and no P&L detail lines to carry template zeros. |
| F2 STANDALONE vs CONSOLIDATED | N.A. | Consolidated figures only; no standalone column disclosed. |
| F3 SHELL-ENTITY DETECTION | N.A. | No cost lines, no standalone/consolidated split, no entity list to compare. |
| F4 UNAUDITED CONTRIBUTION RATIO | N.A. | No auditor Other Matters; results labelled unaudited, `NO_AUDITOR_REPORT_REFERENCED`. |
| F5 GOING CONCERN / EoM | N.A. | No auditor report, no EoM / going-concern paragraph in a press release. |
| F6 FORWARD-COMMITMENT MINING | FINDING | A3-F6-1: 8 undated forward commitments (400/765 kV "remains on track" L111; IDT commissioning + Tank/Radiator backward integration L116-117; "will further strengthen" L139). Commitment register below. |
| F7 HEDGE PHRASE MINING | PASS | No F7 hedge-lexicon hits (no "no assurance/subject to/evaluating/exploring/in discussions/endeavour"). Note: release carries NO safe-harbor/forward-looking disclaimer despite 8 FLS — absence of a disclaimer, not a hedge; recorded, not a finding. |
| F8 TAX FORENSICS | N.A. | No tax line, no ETR, no deferred-tax disclosure in a highlights press release. |
| F9 OCI FORENSICS | N.A. | No OCI / actuarial disclosure. |
| F10 SHARE COUNT / DILUTION | N.A. | No paid-up capital, no basic/diluted EPS disclosed. |
| F11 RESERVES / NET WORTH | N.A. | No balance sheet, no other-equity figure. |
| F12 SEGMENT FORENSICS | N.A. | No segment assets/liabilities/revenue table. |
| F13 BOARD OUTCOME BEYOND RESULTS | N.A. | Single Reg 30 transmittal (`SINGLE_AGENDA_ITEM`); no AR/AGM/record date/dividend/director/auditor/ESOP/capital-raise resolution. |
| F14 NOTE DRAFTING INCONSISTENCIES | FINDING | A3-F14-1 (period-label header "Q4FY25" over Q4FY26 values, L72) + A3-F14-2 (entity-name misspelling & duplicated "Order...order", L91-92/105). |
| F15 ENTITY LIST DIFFS | N.A. | `NO_ENTITY_LIST` — "consolidated" results with zero subsidiary names to diff against prior quarter. |
| F16 PRESENTATION-SPECIFIC: DROPPED/REFRAMED | FINDING | A3-F16-1 (no QoQ column + mislabelled sequential period obscures -350 bps QoQ margin / -35% QoQ PAT); F16-2 (NEW inflow 972.42 & EHV split disclosures vs deck); F16-3 (SBPDCL silence); F16-4 (EBITDA ex-OI clean here vs deck slide-27 mislabel); F16-5 (RVPN cascade-watch utility appears as customer); F16-6 (order-book roll-forward ~Rs 117 cr unreconciled). |
| F17 CONCALL SILENCE AUDIT | N.A. | No concall transcript in this document (press release only); the SBPDCL/monitoring silence audit is folded into A3-F16-3. Concall F17 to run on the Aug 2026 transcript when available. |

Checks marked: 4 FINDING (F6, F14, F16 group; F7 PASS), 1 PASS, 12 N.A. No blanks -> GATE A3 pass.

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | ref (line) | status word |
|---|---|---|---|
| "commenced FY27 on a strong note" | Q1FY27 (past) | 123 | completed |
| 400 kV transformer development at Vadod | none given | 110-111 | "remains on track" (underway) |
| 765 kV transformer at Atlanta Trafo | none given | 111 | "remains on track" (underway) |
| Commissioning Inverter Duty Transformer (IDT) facility | none given | 116, 137 | "commissioning" (in progress) |
| Tank & Radiator backward integration | none given | 116-117, 137-138 | "progressing" (underway) |
| Increasing capacity utilisation across facilities | none given | 116, 136-137 | "remains focused on" (ongoing) |
| Expanding export footprint | none given | 137 | "expanding" (ongoing) |
| "These strategic initiatives will further strengthen ... sustained long-term growth" | none given | 139-140 | intent (undated) |

Every commitment is UNDATED. Cross-map to Notion Section-8: IDT/capex-util (items 6), Tank/Radiator backward integration (item 7, thesis-expected commence Q2FY27 / commission Q3FY28 — release says only "progressing", no date), 765 kV (item 5, thesis-expected PGCIL audit by FY27 — release says only "remains on track", no PGCIL re-approval status). A4 should convert each into a dated concall question.

---

## FORWARD-SIGNAL SUMMARY FOR A4

- POSITIVE / green-band beats: order inflow Rs 972.42 cr (>green 600-700), order book Rs 3,116.63 cr +25% QoQ (>green 2,500), EHV order-book share now quantified (400 kV+reactors ~Rs 275 cr; 220 kV >55%), RVPN as customer not debarrer.
- BEAR / watch: -350 bps sequential EBITDA-margin compression (20.0% -> 16.5%) hidden by the missing/mislabelled QoQ column — direct Voltamp-shock read-through, and quarter 1 of 2 below the 17% red line; SBPDCL silence; all growth commitments undated; order-book roll-forward gap ~Rs 117 cr.
