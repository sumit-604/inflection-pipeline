# A3 FORENSIC NOTES — UFBL Q1 FY27 (doctype: RESULTS, Reg-33 filing)

Source: `extract_results_ufbl_q1fy27.txt` (12 pages, 715 lines, unit Rs Millions, x0.1 to Cr)
Ledger: `ledger_results_ufbl_q1fy27.md` — 100% of ledger rows read at cited lines before judging.
Units below in Rs Millions unless converted to Cr. Statutory tax rate reference: 25.17%.

Reconciliation note: A2 ledger enumerated 27 notes, 53 value-bearing P&L line items,
12 auditor paragraphs, 14 consolidation entities, 5 signature blocks, 2+1 zero-standing
rows, 1 agenda item. Every one was read at its line number. No unread rows. GATE A3 met.

---

## FINDINGS TABLE

| id | check | ledger row ref | line | verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| F1-a | F1 | Sec3 rows 15,17 (ZERO_STANDING) | 166, 169 | "(a) Current tax expense … -" / "(c) Deferred tax … -" | NEUTRAL-FACT | Standalone books a Rs 61.32mn PBT with nil current AND nil deferred tax. The template line exists to carry a charge that management has chosen not to book — carryforward-loss shelter that will lapse. See F8. |
| F2-a | F2 | Sec9 STANDALONE_CONSOLIDATED_PAT_GAP | 171 vs 501/503/504 | standalone PAT "61.32" vs consol PAT "23.08"; owners "30.93"; NCI "(7.85)" | FORWARD-SIGNAL | S-vs-C gap = -38.24mn = 62% of standalone PAT. Subsidiaries as a bloc were loss-making in Q1FY27. Gap swung from +2.81mn (Q1FY26) to -37.16 (Q4FY26) to -38.24 (Q1FY27) — a >40mn deterioration far exceeding the 5pp trigger. The profitable headline is standalone-only; the group is barely above breakeven. |
| F2-b | F2 | Sec3 line 152 vs Sec6 line 478 | 152, 478 | rev std "3,283.85" vs consol "4,258.99" | FORWARD-SIGNAL | Subsidiary revenue = 975.14mn (Q1FY27) vs 680.45mn (Q1FY26), +43% YoY, yet the same subsidiary bloc is net loss-making. Revenue scaling into losses = cash burn at the edge. |
| F3-a | F3 | Sec5b entities h, j | 368, 370, 385 | "United Foodbrands Thai Holding Co., Ltd.*" / "Barbeque Nation Restaurant W.L.L.*" / "*Operations not yet commenced." | FORWARD-SIGNAL | At least 2 step-down entities are pre-operating shells (Thai holdco, Qatar LLC). No going-concern EoM attaches — consistent with pre-commissioning builds, not distress. Future revenue + capex + funding events sit here. Subsidiary-level cost lines not disclosed, so shell/operating split cannot be fully reconciled from this filing. |
| F4-a | F4 | Sec5a para 6 OTHER_AUDITOR_RELIANCE | 397-405 | "in respect of 8 subsidiaries … total revenues of Rs. 968.86 million, total net loss after tax of Rs. 25.50 million … reviewed by their respective independent auditors" | CONFIRMATORY-NEGATIVE | 968.86mn = 22.7% of consolidated revenue rests on OTHER auditors (principal auditor relies solely on furnished reports). This is the Southwest failure mode: the group number the market sees is 23% not independently reviewed by the signing firm. |
| F4-b | F4 | Sec5a para 7 UNAUDITED_SUBSIDIARY_RELIANCE | 418-435 | "3 subsidiaries … total net loss after tax of Rs. 11.43 million … have not been audited/ reviewed by their auditors … not material to the Group" | CONFIRMATORY-NEGATIVE | Unaudited management-furnished net loss 11.43mn = 49.5% of consolidated PAT (23.08mn) in absolute terms — "not material" is management's word, not the auditor's independent finding. Combined para 6+7 net loss = 36.93mn, which alone explains nearly the entire S-vs-C drag. |
| F4-c | F4 | Sec5 reliance reconciliation | 397, 418, 355-383 | "8 subsidiaries" + "3 subsidiaries" of 13 | AMBIGUOUS | Arithmetic gap: 8 (other-auditor) + 3 (unaudited) = 11 of 13 subsidiaries; only 2 are directly reviewed by the principal auditor, and those 2 are not itemised. Which 2, and how much revenue/PAT do they carry, is undisclosed. |
| F6-a | F6 | Sec4 note 9 / Sec7 note 11 | 259-261, 691 | "continues to monitor the finalisation of Central / State Rules … would provide appropriate accounting effect on the basis of such developments as needed" | FORWARD-SIGNAL | Open-ended commitment to book further Labour-Code true-ups once rules finalise. Q1FY27 P&L does NOT yet carry the recurring in-quarter charge (the 46.68+14.20mn was a FY26 catch-up). Future quarterly employee-cost step-up is signalled. |
| F6-b | F6 | Sec4 note 11 | 269-277 | "Rs 100 million … had disbursed Rs 14 million … Total tenor of such loan is four years … moratorium period of 12 months" | FORWARD-SIGNAL | Rs 86mn of the sanctioned Red Apple loan remains undisbursed = a committed future cash outflow to a domestic subsidiary; related-party funding pipeline. |
| F7-a | F7 | Sec4 note 9 | 251-261 | "based on the best information available" / "would provide appropriate accounting effect … as needed" | AMBIGUOUS | Pre-emptive hedge language on Labour-Code exposure inside a note = legal cover that next-year employee costs may be revised. New hedge on a cost line = tells you the direction of the next surprise (up). |
| F8-a | F8 | Sec3 rows 15-18 | 164-171 | PBT "61.32"; tax "-"; PAT "61.32" | FORWARD-SIGNAL | Standalone ETR = 0.0% vs 25.17% statutory. Full shield = ~2,517 bps / ~15.4mn tax deferred, funded by carried-forward losses (FY26 PBT -647.06). As losses exhaust and/or a DTA is recognised, reported PAT takes a full statutory-rate haircut. Consolidated ETR = 1.26/24.34 = 5.2% (reconciles to the deck's ~4.2% ballpark; the deck's Rs 59.6 Cr DTA is a balance-sheet item absent from this filing — see F11). |
| F8-b | F8 | Sec3 row 16 / Sec6 row 18, note 10/12 | 167, 264-267, 497, 695 | "Adjustment of tax relating to earlier years … (61.42)" / "reversed Rs 61.42 million relating to Income-tax provisions created in earlier years" | NEUTRAL-FACT | Non-zero earlier-year tax adjustment (F8 trigger). One-off FY26 credit from favourable appellate orders — a non-recurring item that flattered FY26 and does not repeat. |
| F9-a | F9 | Sec6 row 27 | 508-509 | remeasurement DBP consol Q4FY26 "8.63" vs FY26 "2.49" | AMBIGUOUS | The single Q4FY26 remeasurement GAIN (+8.63) exceeds the full-year figure (+2.49), implying earlier FY26 quarters were ~-6mn and a year-end actuarial assumption revision (discount rate / plan assets) reversed them. Verify assumptions at the Annual Report. |
| F9-b | F9 | Sec6 row 30 | 513-514 | FX translation "1.78 / (5.72) / 7.25 / (16.24)" | FORWARD-SIGNAL | Foreign-operations translation reserve swings sign every period (FY26 -16.24). Overseas exposure introduces non-operating equity volatility that will grow as international subs scale. |
| F10-a | F10 | Sec3 row 25 / Sec6 row 35 | 179-180, 520-521 | paid-up "195.43 / 195.43 / 195.41 / 195.43" | NEUTRAL-FACT | Paid-up rose 195.41 -> 195.43 (Q1FY26 to Q4FY26), ~4,000 shares at Rs 5 FV = ESOP allotment during FY26. Traces to a corporate action, not a break. |
| F10-b | F10 | Sec3 rows 28-29 / Sec6 rows 38-39 | 185-186, 526-527 | basic "1.57" vs diluted "1.55"; consol "0.79" vs "0.78" | FORWARD-SIGNAL | Basic-diluted spread appears only in the profit quarter (loss quarters show none, anti-dilutive). Confirms live dilutive instruments (options/ESOP) outstanding; A4 to size against the Notion warrant/ESOP register. |
| F11-a | F11 | Sec3 row 26 / Sec6 row 36 | 181, 522 | other equity FY26 std "3,220.92" / consol "2,907.64" | AMBIGUOUS | Net worth computable only for FY26 audited (std 341.6 Cr; consol 310.3 Cr; 31.3 Cr gap = subsidiary accumulated losses + NCI). NO balance sheet, NO cash-flow statement, NO investments schedule, NO DTA note in this filing. The deck's Rs 12.1 Cr "vanished" investments and Rs 59.6 Cr DTA CANNOT be reconciled here, and the deck's INDETERMINATE cash-conversion cap is NOT resolved — no CFO is disclosed. Flag remains open. |
| F12-a | F12 | Sec7b geographical segment | 573-574 | "Others (Overseas) … 385.42 / 336.38 / 262.91 / 1,247.12" | FORWARD-SIGNAL | Overseas revenue +46.6% YoY (262.91 -> 385.42) while the overseas/subsidiary bloc is net loss-making (F2/F4). Single reported segment means no segment asset/liability disclosure — the equity-funded international build is invisible on this statement except through the widening S-vs-C loss. |
| F14-a | F14 | Sec8 SIGNATURE_TIMING | 298-304, 449-457, 705-712 vs 34 | CEO std results signed "12:09:04", consol "12:10:59"; auditor consol "12:26:20", std "12:27:17"; meeting concluded "12:30 PM" | AMBIGUOUS | All 4 substantive financial-document signatures (both CEO, both auditor) are timestamped 3-21 minutes BEFORE the board meeting concluded. Only the CS cover letter (12:42) post-dates the meeting. Could be routine pre-signing of approved drafts, or a governance-sequence weakness. A4 question. |
| F14-b | F14 | Sec3 header | 150-151 | "Unudited" (misspelled) in standalone results header | NEUTRAL-FACT | Typo "Unudited" x2 in the standalone statement header (consolidated spells it correctly). Individually immaterial; a cumulative drafting-control data point. |
| F15-a | F15 | Sec4/7 notes 5-8, Sec5b | 211-243, 355-385, 542-560 | "WGPL has become a subsidiary … w.e.f. June 30, 2025"; 2 Thai + 1 Qatar step-downs; "Blue Planet … Amalgamated with Red Apple … w.e.f. May 29, 2026" | FORWARD-SIGNAL | Four entity-structure changes since prior FY: WGPL associate->subsidiary; +2 Thai step-downs (Dec 2025); +1 Qatar step-down (Feb 2026); Blue Planet amalgamated into Red Apple (NCLT May 29 2026, appointed date retroactive to Apr 1 2024). Scope now 14 entities. Retroactive amalgamation forces a 3-period NCI/owner restatement (18 rows, Sec7c) — every previously-reported attribution figure is superseded. No prior-quarter ledger supplied, so a mechanical cross-quarter diff could not be run; changes are evidenced from the notes. |

---

## CHECKLIST SCORECARD (all 17)

| Check | Status | One-line basis |
|---|---|---|
| F1 | FINDING | Nil current AND nil deferred tax standing on a positive Rs 61.32mn standalone PBT (lines 166, 169). |
| F2 | FINDING | S-vs-C PAT gap -38.24mn = 62% of standalone PAT; swung >40mn from +2.81 (Q1FY26) to -38.24 (Q1FY27); subs loss-making (line 171 vs 501). |
| F3 | FINDING | 2 step-down entities "Operations not yet commenced" (lines 368,370,385); pre-commissioning builds, no GC EoM. |
| F4 | FINDING | Other-auditor revenue 968.86mn = 22.7% of consol rev; unaudited net loss 11.43mn = ~50% of consol PAT; 11 of 13 subs not principal-reviewed (lines 397,418). |
| F5 | PASS | No Emphasis-of-Matter / Going-Concern paragraph in either review report; no prior-quarter extract to verbatim-diff (lines 48, 441). |
| F6 | FINDING | Forward commitments: Labour-Code true-ups "as needed", Rs 86mn undisbursed Red Apple loan (lines 259-261, 269-277). |
| F7 | FINDING | Pre-emptive hedge language on Labour-Code cost exposure inside note 9 (lines 251-261). |
| F8 | FINDING | Standalone ETR 0.0% vs 25.17%; carryforward shield ~2,517 bps; non-zero earlier-year tax adjustment -61.42mn (lines 164-171, 264-267). |
| F9 | FINDING | Consol Q4FY26 remeasurement +8.63 exceeds full FY26 +2.49 = year-end actuarial assumption change; FX reserve sign-swings (lines 508, 513). |
| F10 | FINDING | Paid-up 195.41->195.43 (ESOP); basic-diluted spread only in profit quarter = live dilutive instruments (lines 179, 185-186). |
| F11 | FINDING | No balance sheet / cash-flow / investments / DTA schedule; deck's Rs 12.1 Cr investments, Rs 59.6 Cr DTA and cash-conversion cap UNRESOLVED (lines 181, 522). |
| F12 | FINDING | Overseas revenue +46.6% YoY while overseas bloc loss-making; single segment hides asset/liability build (lines 573-574). |
| F13 | PASS | Single agenda item — results approval only; no AR/AGM/record-date/dividend/director/capital-raise item to schedule (lines 34-36). |
| F14 | FINDING | 4 of 5 substantive signatures pre-date meeting conclusion by 3-21 min; "Unudited" header typo (lines 298-304, 449-457, 150). |
| F15 | FINDING | Four entity-structure changes + 14-entity scope + retroactive amalgamation restatement (lines 211-243, 355-385, 613-662). |
| F16 | N.A. | Presentation-specific; this is a results filing. |
| F17 | N.A. | Concall-specific; no transcript in scope. |

Blanks: none. GATE A3: PASS.

---

## COMMITMENT REGISTER (from F6/F7)

| commitment | implied date | note/ref | status word |
|---|---|---|---|
| Book further Labour-Code accounting effect on finalisation of Central/State Rules | open (on rule finalisation) | note 9 std (259-261) / note 11 consol (691) | underway (monitoring) |
| Disburse remaining Rs 86mn of Rs 100mn sanctioned Red Apple loan | over 4-yr tenor incl. 12-mo moratorium | note 11 std (269-277) | initiated (14mn of 100mn disbursed) |
| Commence operations at Thai holdco and Qatar LLC step-downs | unspecified | notes 7,8 std / 9,10 consol (232-243, 385, 560) | initiated (incorporated, pre-ops) |
| Employee-compensation restructuring effective April 01, 2026 | effective 01-Apr-2026 (recurring impact ongoing) | note 9 std (253) / note 11 consol (685) | completed (effective, impact recurring) |

---

## A4 HAND-OFF — FLAGGED FINDINGS

FORWARD-SIGNAL (management questions): F2-a, F2-b, F3-a, F6-a, F6-b, F8-a, F9-b, F10-b, F12-a, F15-a.
AMBIGUOUS (lean-bear questions): F4-c, F7-a, F9-a, F11-a, F14-a.
CONFIRMATORY-NEGATIVE (Southwest-mode monitor): F4-a, F4-b.
NEUTRAL-FACT (record only): F1-a, F8-b, F10-a, F14-b.

Monitoring-checklist reconciliation: S-vs-C PAT gap = F2 (subs drag confirmed, standalone flatters). Other-auditor / unaudited reliance = F4 (23% of consol revenue, ~50% of consol PAT not principal-reviewed). Entity change (14) + signature timing = F15 + F14-a. Tax nil + note 10 + deck DTA/ETR = F8 + F11-a. Rs 12.1 Cr investments + cash-flow statement = F11-a: NEITHER present in this filing; cash-conversion INDETERMINATE cap NOT resolved — carry forward.

```yaml
stage: A3-forensics
company: "UFBL"
quarter: "Q1FY27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/ufbl-q1fy27/work/forensics_results_ufbl_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: FINDING
  F3: FINDING
  F4: FINDING
  F5: PASS
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: FINDING
  F10: FINDING
  F11: FINDING
  F12: FINDING
  F13: PASS
  F14: FINDING
  F15: FINDING
  F16: N.A.
  F17: N.A.
findings:
  - {id: "F1-a", check: "F1", line: "166,169", classification: "NEUTRAL-FACT", implication: "Nil current+deferred tax on Rs 61.32mn PBT; carryforward shelter that will lapse."}
  - {id: "F2-a", check: "F2", line: "171,501", classification: "FORWARD-SIGNAL", implication: "S-vs-C gap -38.24mn (62% of standalone PAT); subsidiaries loss-making; group barely breakeven."}
  - {id: "F2-b", check: "F2", line: "152,478", classification: "FORWARD-SIGNAL", implication: "Subsidiary revenue +43% YoY into net losses = cash burn scaling."}
  - {id: "F3-a", check: "F3", line: "368,370,385", classification: "FORWARD-SIGNAL", implication: "Two pre-operating step-down shells; future revenue/capex/funding events sit here."}
  - {id: "F4-a", check: "F4", line: "397", classification: "CONFIRMATORY-NEGATIVE", implication: "22.7% of consolidated revenue rests on other auditors; Southwest failure mode."}
  - {id: "F4-b", check: "F4", line: "418", classification: "CONFIRMATORY-NEGATIVE", implication: "Unaudited net loss 11.43mn = ~50% of consol PAT; materiality is management's word only."}
  - {id: "F4-c", check: "F4", line: "397,418,355", classification: "AMBIGUOUS", implication: "Only 2 of 13 subs directly principal-reviewed and not itemised; coverage gap."}
  - {id: "F6-a", check: "F6", line: "259", classification: "FORWARD-SIGNAL", implication: "Open Labour-Code true-up commitment; recurring quarterly employee-cost step-up not yet in P&L."}
  - {id: "F6-b", check: "F6", line: "269", classification: "FORWARD-SIGNAL", implication: "Rs 86mn undisbursed related-party loan = committed future cash outflow."}
  - {id: "F7-a", check: "F7", line: "251", classification: "AMBIGUOUS", implication: "Pre-emptive hedge on Labour-Code cost = next surprise likely upward on employee cost."}
  - {id: "F8-a", check: "F8", line: "164", classification: "FORWARD-SIGNAL", implication: "0% standalone ETR (~2517 bps shield); PAT faces full statutory haircut when losses exhaust/DTA booked."}
  - {id: "F8-b", check: "F8", line: "167,264", classification: "NEUTRAL-FACT", implication: "Non-recurring Rs 61.42mn earlier-year tax credit flattered FY26; does not repeat."}
  - {id: "F9-a", check: "F9", line: "508", classification: "AMBIGUOUS", implication: "Q4FY26 remeasurement gain exceeds full year = year-end actuarial assumption change; verify at AR."}
  - {id: "F9-b", check: "F9", line: "513", classification: "FORWARD-SIGNAL", implication: "FX translation reserve sign-swings; growing overseas exposure adds equity volatility."}
  - {id: "F10-a", check: "F10", line: "179", classification: "NEUTRAL-FACT", implication: "Paid-up change traces to FY26 ESOP allotment."}
  - {id: "F10-b", check: "F10", line: "185", classification: "FORWARD-SIGNAL", implication: "Basic-diluted spread confirms live dilutive instruments; size vs Notion register."}
  - {id: "F11-a", check: "F11", line: "181,522", classification: "AMBIGUOUS", implication: "No balance sheet/cash-flow/investments/DTA; deck's Rs 12.1 Cr investments, Rs 59.6 Cr DTA and cash-conversion cap UNRESOLVED."}
  - {id: "F12-a", check: "F12", line: "573", classification: "FORWARD-SIGNAL", implication: "Overseas revenue +46.6% YoY while loss-making; equity-funded international build hidden by single-segment reporting."}
  - {id: "F14-a", check: "F14", line: "298,449,705", classification: "AMBIGUOUS", implication: "4 substantive signatures pre-date meeting conclusion by 3-21 min; governance-sequence question."}
  - {id: "F14-b", check: "F14", line: "150", classification: "NEUTRAL-FACT", implication: "'Unudited' header typo; cumulative drafting-control data point."}
  - {id: "F15-a", check: "F15", line: "211,355,613", classification: "FORWARD-SIGNAL", implication: "Four entity-structure changes; retroactive amalgamation supersedes all prior attribution figures."}
forward_signals: ["F2-a","F2-b","F3-a","F6-a","F6-b","F8-a","F9-b","F10-b","F12-a","F15-a"]
ambiguous: ["F4-c","F7-a","F9-a","F11-a","F14-a"]
commitments:
  - {commitment: "Book further Labour-Code accounting effect on rule finalisation", implied_date: "open", ref: "note 9 std L259 / note 11 consol L691", status_word: "underway"}
  - {commitment: "Disburse remaining Rs 86mn of Red Apple loan", implied_date: "4-yr tenor incl 12-mo moratorium", ref: "note 11 std L269", status_word: "initiated"}
  - {commitment: "Commence operations at Thai holdco and Qatar LLC step-downs", implied_date: "unspecified", ref: "notes 7-8 std / 9-10 consol L385,L560", status_word: "initiated"}
  - {commitment: "Employee-compensation restructuring effective Apr 01 2026", implied_date: "2026-04-01", ref: "note 9 std L253 / note 11 consol L685", status_word: "completed"}
gate_a3: pass
blank_checks: []
```
