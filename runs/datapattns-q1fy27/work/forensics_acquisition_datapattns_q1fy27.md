# A3 FORENSIC NOTES — Data Patterns (India) Ltd (DATAPATTNS) — Q1 FY27 — DOCTYPE: ACQUISITION (SEBI Reg 30 / Annexure A)

Source: acquisition_datapattns_q1fy27.pdf (3 pages, 114 extract lines)
A1 extract: /home/user/inflection-pipeline/runs/datapattns-q1fy27/work/extract_acquisition_datapattns_q1fy27.txt
A2 ledger: /home/user/inflection-pipeline/runs/datapattns-q1fy27/work/ledger_acquisition_datapattns_q1fy27.md
Ledger reconciliation: 60/60 rows read verbatim at cited lines (Table 1: 10, Table 2: 24, Table 3: 18, Table 4: 8) = 100%.

## DOCTYPE MAPPING NOTE
This is a single Reg 30 material-event letter + Annexure A, not a results filing / concall / presentation. Per the standard doctype map, balance-sheet checks (F2, F3, F4, F5, F8, F9, F12) and the presentation check (F16) have no substrate and are marked N.A. with the reason stated. Per the A3 task instruction, every Annexure A disclosure field is treated as a ledger row and any field a diligent analyst would expect but that is absent or vague is a FINDING with the forward implication stated. Phrase-mining (F6, F7), board-outcome (F13), drafting (F14), entity-diff (F15) and the silence audit (F17, re-purposed against the Notion checklist) all apply.

## HEADLINE ARITHMETIC (used across findings)
- Total cash deployment = Rs 1.50 Cr (equity) + Rs 8.50 Cr (loan to settle target liabilities) = **Rs 10.00 Cr** (lines 112-115).
- Equity price/share = Rs 1.50 Cr / 5,00,000 shares = **Rs 30/share** vs Rs 10 face (3.0x face) (lines 66-67, 112-113).
- Target turnover: FY23-24 Rs 1.58 Cr (audited) -> FY24-25 Rs 4.42 Cr (audited) -> **FY25-26 Rs 4.17 Cr (PROVISIONAL, down ~5.7% YoY)** (lines 126-128).
- Loan to clear liabilities Rs 8.50 Cr ≈ **2.0x FY26 turnover**; total cash Rs 10.0 Cr ≈ **2.4x FY26 turnover**.

---

## FINDINGS TABLE

| id | check | ledger row ref | line | verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| F1 | F1 | T1 Field 5 (ZERO_STANDING); T1 Field 2 (ZERO_STANDING) | 103-105; 69 | "Not Applicable" (approvals); "No" (RPT) | AMBIGUOUS | A 100% control change of a defence-composites maker (radomes, "defence composite solutions", DRDO customers) is asserted to need no approval. If a defence/CCI/sectoral approval later surfaces, the "3 Months" timeline slips. A4 question. |
| F6 | F6 | T1 Field 6; T1 Field 4; T3 L9 | 106-107; 80-84; 34 | "Indicative time period for completion of the acquisition 3 Months"; "STAC shall become a wholly owned subsidiary" | FORWARD-SIGNAL | Dateable commitment: completion ~end Oct 2026 -> first-ever consolidated accounts land Q2/Q3 FY27. Feeds Role 5 promise-vs-delivery tracker; verify closing next quarter. |
| F7 | F7 | T3 L9; T2 4c | 34-35; 100-102 | "subject to other statutory / regulatory approval required, if any"; "estimated 1.3– 2.0x" | AMBIGUOUS | The letter hedges "approval... if any" while Field 5 says "Not Applicable" (see F14). The value-accretion claim is an unquantified 1.3-2.0x range with no basis. A4 question on the accretion math. |
| F11 | F11 | T2 8b; T2 1c/10f-h | 114-115; 126-128 | "Rs.8.50 Cr. as a loan to the Target Company to enable it to settle its liabilities" | FORWARD-SIGNAL | Implied target liabilities >= Rs 8.5 Cr (~2.0x its Rs 4.17 Cr turnover) against equity valued at only Rs 1.50 Cr => target net worth is thin or negative and turnover already declined YoY (FY26 provisional). True cash outlay is Rs 10 Cr, not the Rs 1.50 Cr "cost of acquisition." Goodwill/consolidation drag + Rs 10 Cr cash-deployment event vs the net-cash tripwire. |
| F13 | F13 | T3 L8-L10 | 33-35 | "the proposed acquisition, which was approved by the Board of Directors... at its Meeting held today i.e. Thursday, July 30, 2026" | FORWARD-SIGNAL | Board outcome beyond results (same board meeting as Q1 FY27 results). Schedule a monitoring event for (a) completion confirmation ~Oct 2026 and (b) first consolidated statements. First subsidiary in company history. |
| F14 | F14 | T3 L9 vs T1 Field 5; T4 sig block | 34-35 vs 103-105; 43-50 | letter: "subject to other statutory / regulatory approval required, if any" vs Field 5: "Not Applicable" | AMBIGUOUS | Internal contradiction on whether approvals exist. Secondary: SIGNATURE_TIMESTAMP_ABSENT (lines 43-50) — no signing timestamp captured, so signing-vs-board-conclusion timing cannot be verified. Cumulative governance-hygiene data point. |
| F15 | F15 | Notion baseline (standalone-only) vs T1 Field 4 | 80-84 | "STAC shall become a wholly owned subsidiary of the Data Patterns (India) Limited" | FORWARD-SIGNAL | Company was standalone-only (zero subs) at 30 Jun 2026 per Notion; this creates its FIRST subsidiary. Consolidation scope, component-audit scope and first-ever consolidated P&L/BS arrive next quarter. |
| F17 | F17 | Notion checklist vs T2 2b (IMPLICIT_NA); T2 10d/10e (DISCLOSURE_GAP) | 70-75; 120-121 | Field 2 arm's-length sub-q "Not explicitly answered"; incorporation date & country "NOT PROVIDED" | AMBIGUOUS | Silence audit against Notion watch-list: (1) arm's-length basis never affirmatively stated even though Rs 1.50 Cr is paid "to the Promoters" (line 112); (2) target net worth / valuation multiple never framed; (3) date of incorporation absent; (4) country of presence absent (only "Chennai-based" city). All four are analyst-expected fields the disclosure is silent on. A4 questions. |

---

## CHECKLIST SCORECARD (all 17)

| Check | Status | One-line basis |
|---|---|---|
| F1 ZERO-VALUE STANDING ITEMS | FINDING | 2 ZERO_STANDING fields; regulatory "Not Applicable" (line 103-105) not credible for a defence-sector 100% control change. |
| F2 STANDALONE vs CONSOLIDATED | N.A. | No financial statements / no S-vs-C tables in a Reg 30 letter. |
| F3 SHELL-ENTITY DETECTION | N.A. | No cost-line pairs to compare; single-entity disclosure. |
| F4 UNAUDITED CONTRIBUTION RATIO | N.A. | No auditor Other-Matters paragraph in this doctype. |
| F5 GOING CONCERN / EoM TRACKING | N.A. | No EoM/going-concern paragraph; no prior-quarter extract on file. |
| F6 FORWARD-COMMITMENT MINING | FINDING | "3 Months" completion (line 106-107); "shall become a wholly owned subsidiary" (line 84). |
| F7 HEDGE PHRASE MINING | FINDING | "subject to... approval... if any" (line 34-35); "estimated 1.3– 2.0x" (line 102). |
| F8 TAX FORENSICS | N.A. | No ETR / deferred-tax / tax figures disclosed. |
| F9 OCI FORENSICS | N.A. | No OCI / actuarial data disclosed. |
| F10 SHARE COUNT AND DILUTION | PASS | Consideration is "Cash Consideration" (line 108); no share swap, zero dilution to DATAPATTNS. |
| F11 RESERVES / NET-WORTH TIE-OUT | FINDING | Rs 8.50 Cr loan "to settle its liabilities" (line 114-115) implies distressed/negative target net worth; true outlay Rs 10 Cr. |
| F12 SEGMENT FORENSICS | N.A. | No segment tables in this doctype. |
| F13 BOARD OUTCOME BEYOND RESULTS | FINDING | Board approved acquisition 30 Jul 2026 (line 33-35); schedule completion + first-consolidation monitoring. |
| F14 NOTE DRAFTING INCONSISTENCIES | FINDING | Letter "approval... if any" vs Field 5 "Not Applicable"; plus signature timestamp absent. |
| F15 ENTITY LIST DIFFS | FINDING | Creates first-ever subsidiary vs standalone-only Notion baseline (line 80-84). |
| F16 DROPPED / REFRAMED DISCLOSURES | N.A. | Not a presentation; no prior deck to diff. |
| F17 SILENCE AUDIT (vs Notion) | FINDING | Silent on arm's-length basis, target net worth/multiple, incorporation date, country (lines 70-75, 120-121). |

Statuses: PASS 1 (F10) | FINDING 8 (F1, F6, F7, F11, F13, F14, F15, F17) | N.A. 8 (F2, F3, F4, F5, F8, F9, F12, F16). No blanks. GATE A3: pass.

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/ref | status word |
|---|---|---|---|
| Acquisition of 100% of STAC; "STAC shall become a wholly owned subsidiary" | on completion | Field 4, lines 80-84 | proposes to / board has approved |
| "Indicative time period for completion of the acquisition 3 Months" | ~end Oct 2026 | Field 6, lines 106-107 | initiated |
| Board approval of the proposed acquisition | 30 Jul 2026 (done) | Letter, lines 33-35 | board has approved |
| Post-acquisition addressable value per programme "estimated 1.3– 2.0x" | undated (post-close) | Field 4c, lines 100-102 | intends to (forward projection) |
| Completion "subject to other statutory / regulatory approval required, if any" | conditional | Letter, lines 34-35 | subject to approval |

---

## NOTES FOR A4
- FORWARD-SIGNAL findings to convert to management questions: F6 (closing/consolidation timing), F11 (true Rs 10 Cr outlay + target net worth + declining provisional turnover), F13 (first-consolidation event), F15 (entity-scope change).
- AMBIGUOUS findings to convert to management questions: F1 (defence/regulatory approval genuinely NA?), F7 (basis for 1.3-2.0x accretion), F14 (approval contradiction), F17 (arm's-length basis for the Rs 1.50 Cr paid to promoters; target net worth/multiple; incorporation date; country).
- Cross-check for A4/A5: consideration is paid "to the Promoters" (STAC's) yet the deal is declared not an RPT and arm's-length is left unanswered (IMPLICIT_NA). Confirm the counterparty identity and that no DATAPATTNS promoter/group interest exists in STAC.

```yaml
stage: A3-forensics
company: "DATAPATTNS"
quarter: "q1fy27"
doctype: "acquisition"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/datapattns-q1fy27/work/forensics_acquisition_datapattns_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: N.A.
  F9: N.A.
  F10: PASS
  F11: FINDING
  F12: N.A.
  F13: FINDING
  F14: FINDING
  F15: FINDING
  F16: N.A.
  F17: FINDING
findings:
  - {id: "F1", check: "F1", line: "103-105", classification: "AMBIGUOUS", implication: "Regulatory 'Not Applicable' on a defence-composites control change may be under-disclosure; approval surprise could slip the 3-month timeline."}
  - {id: "F6", check: "F6", line: "106-107", classification: "FORWARD-SIGNAL", implication: "Completion ~Oct 2026 -> first consolidated accounts Q2/Q3 FY27; track closing."}
  - {id: "F7", check: "F7", line: "34-35", classification: "AMBIGUOUS", implication: "Letter hedges 'approval if any' vs Field 5 'Not Applicable'; 1.3-2.0x accretion claim unquantified."}
  - {id: "F11", check: "F11", line: "114-115", classification: "FORWARD-SIGNAL", implication: "Rs 8.5 Cr to clear target liabilities (~2x its turnover) implies thin/negative net worth; true outlay Rs 10 Cr; goodwill/consolidation drag."}
  - {id: "F13", check: "F13", line: "33-35", classification: "FORWARD-SIGNAL", implication: "Board approved first-ever acquisition; schedule completion + first-consolidation monitoring events."}
  - {id: "F14", check: "F14", line: "34-35", classification: "AMBIGUOUS", implication: "Internal contradiction on approvals; signature timestamp absent — governance-hygiene data point."}
  - {id: "F15", check: "F15", line: "80-84", classification: "FORWARD-SIGNAL", implication: "First-ever subsidiary vs standalone-only baseline; new consolidation and component-audit scope next quarter."}
  - {id: "F17", check: "F17", line: "70-75", classification: "AMBIGUOUS", implication: "Silent on arm's-length basis (Rs 1.5 Cr paid to promoters), target net worth/multiple, incorporation date, country."}
forward_signals: [F6, F11, F13, F15]
ambiguous: [F1, F7, F14, F17]
commitments:
  - {commitment: "STAC becomes 100% wholly owned subsidiary", implied_date: "on completion", ref: "Field 4 / lines 80-84", status_word: "board has approved"}
  - {commitment: "Indicative completion within 3 Months", implied_date: "~end Oct 2026", ref: "Field 6 / lines 106-107", status_word: "initiated"}
  - {commitment: "Board approval of proposed acquisition", implied_date: "2026-07-30", ref: "letter / lines 33-35", status_word: "completed"}
  - {commitment: "Addressable value per programme estimated 1.3-2.0x", implied_date: "post-close (undated)", ref: "Field 4c / lines 100-102", status_word: "intends"}
  - {commitment: "Completion subject to statutory/regulatory approval if any", implied_date: "conditional", ref: "letter / lines 34-35", status_word: "subject to approval"}
gate_a3: pass
blank_checks: []
```
