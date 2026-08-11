# A3 FORENSIC NOTES — DIVGI TORQTRANSFER SYSTEMS LIMITED — Q1 FY27 (doctype: RESULTS)

Source doc: `results_divgi_q1fy27.pdf` (6 pages). A1 extract: `extract_results_divgi_q1fy27.txt`.
A2 ledger: `ledger_results_divgi_q1fy27.md`. Standalone-only filing (P&L + notes, no BS/CF,
no consolidated column). Units: ₹ million (x0.1 to Cr). Ledger reconciliation: 100% (all 8
ledger categories / every enumerated row read at its cited line before judging).

---

## 0. OCR RE-VERIFICATION OF THE 5 A2-FLAGGED GARBLED LOCATIONS (against source PDF pages 4-5)

Re-verified by reading source-PDF pages 4 (auditor report) and 5 (financial table) directly.

| # | Item | Ledger line | A2 extract text (garbled) | CONFIRMED true value | Page | Note |
|---|---|---|---|---|---|---|
| 1 | UDIN | 229 | `2 6 1 'L 50 s-, (,l...8 N PQO S' 0-1 ~` | **26125657RBNPQO8078** | p4 | Embeds membership no. 125657; year-prefix 26 (2026). Legible in handwriting-style font. |
| 2 | Deferred Tax (4 cols) | 274 | `(0.65'` / `(17.43'` / `4.11` / `(1 21)` | **(0.65) / (17.43) / 4.11 / (1.21)** | p5 | Signs confirmed: credit / credit / charge / credit. |
| 3 | Changes in inventories, FY26 col | 262 | `(8076)` — A2 *guessed* (807.60) | **(80.76)** — A2 GUESS WAS WRONG | p5 | Correction. Footing check confirms: FY26 total expenses 3,124.22 reconciles ONLY with (80.76), never (807.60). See §Arithmetic. |
| 4 | Total expenses formula label | 268 | `Totalexpenses(a+b+c+d+e+ij` | **Total expenses (a+b+c+d+e+f)** | p5 | Clean label; the `ij` was OCR of `f)`. |
| 5 | Basic/Diluted EPS, 31-Mar-26 col | 303-304 | `506` / `5 06` | **5.06 / 5.06** | p5 | Basic = Diluted = 5.06. Decimal confirmed. |

**Material correction:** ledger row 2(b) FY26 comparative is **(80.76)**, not the A2-guessed
(807.60). This does not touch any Q1 FY27 (30-Jun-26) figure; it corrects the FY26 audited
comparative only. All downstream arithmetic below uses the confirmed values.

### Arithmetic re-foot (using confirmed values), Q1 FY27 (30-Jun-26 column)
- Total Income: 1,371.42 + 46.22 = **1,417.64** ✓
- Total expenses: 536.26 + (4.59) + 134.77 + 0.69 + 78.20 + 334.80 = **1,080.13** ✓
- PBT: 1,417.64 − 1,080.13 = **337.51** ✓
- Total tax: 85.76 + (0.65) = **85.11** ✓  → Net profit 337.51 − 85.11 = **252.40** ✓
- TCI: 252.40 + (0.72) = **251.68** ✓
- FY26 total expenses foot (confirms (80.76)): 1,448.73 − 80.76 + 415.41 + 3.10 + 292.37 + 1,045.37 = **3,124.22** ✓ (with (807.60) it would be 2,397.38 ≠ printed 3,124.22).
- EPS cross-check: shares = 152.91/5 = 30.582m; 252.40/30.582 = 8.25 ✓ (matches printed Basic 8.25).

All statement math internally consistent after correction.

---

## FINDINGS TABLE

| id | check | ledger row ref | line | verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-F2 | F2 | §6 entities; A1 hdr 13-17 | 356-357, 381-383 | "the Foreign Entity has not been considered for consolidation for the period ended June 30, 2026" | FORWARD-SIGNAL | Standalone-vs-consolidated gap is non-computable this quarter; a consolidated statement is triggered once the equity-subscription completes. Non-consolidation is appropriate and disclosed (no shares held yet), but a consolidation obligation is forthcoming — first consolidated Divgi accounts likely next quarter or the one after. |
| A3-F6a | F6 | §7 Note 7 | 382 | "the equity shares subscription agreement with the Foreign Entity had not been completed" | FORWARD-SIGNAL | Dateable commitment: subscription to be completed post 30-Jun-26. Milestone to track quarter-over-quarter (initiated → completed). |
| A3-F6b | F6 | §5 Note 3 | 361-365 | capex object "1,507.07 ... 915.27 ... 591.80" unutilised | AMBIGUOUS | ₹591.80m (~₹59.2 Cr) of IPO capex funds still undeployed vs ₹1,507.07m earmarked = 60.7% utilised (915.27/1,507.07). GCP tranche fully spent. Slow capex deployment (IPO listed Mar-2023) → either a pending capacity build or a stalled one. Management question. |
| A3-F13a | F13 | §1 agenda item 5; §2 Annexure | 96-106, 103-105 | "Board approved appointment of M/s. Kirtane & Pandit LLP ... Due to arise in conflict of interest as a internal auditor the said firm has not continued its tenure ... as an internal auditor" | AMBIGUOUS | Statutory auditor CHANGE: incoming Kirtane & Pandit LLP (this quarter's review is signed by outgoing B. K. Khare & Co.). Incoming firm was the company's prior INTERNAL auditor, who exited that role citing conflict of interest and is now proposed as STATUTORY auditor. Familiarity/independence question; also no stated reason for B. K. Khare's exit. Management question. |
| A3-F13b | F13 | §1 agenda items 2 & 4 | 65-67, 87-94 | "61st Annual General Meeting ... will be held on Friday, September 18, 2026"; "final dividend of ₹ 3.27/- ... per equity share for FY 2025-26" | FORWARD-SIGNAL | AGM 18-Sep-2026 + record/cut-off 10-Sep-2026 + final dividend ₹3.27/sh (cash outflow ≈ 30.582m sh × ₹3.27 = ₹100.0m / ₹10.0 Cr). AGM within weeks ⇒ full Annual Report drops shortly ⇒ schedule Role 6 AR Deep Dive. Auditor-appointment resolution goes to members at this AGM. |
| A3-F15 | F15 | §6 entities (ENTITY_CHANGE) | 381-383 | "On June 4, 2026, Divgi Transmission Technologies and Systems Ltd. (the 'Foreign Entity') was incorporated" | FORWARD-SIGNAL | Entity ADDITION: first appearance of a foreign subsidiary-to-be. Signals cross-border/expansion step. No prior ledger to diff, but the incorporation date (04-Jun-2026) confirms genuine novelty this quarter. Watch relationship (subsidiary vs JV) at completion. |

---

## CHECKLIST SCORECARD (all 17; one status each — GATE A3)

| Check | Status | Basis (one line) |
|---|---|---|
| F1 Zero-value standing lines | **PASS** | Sole ZERO_STANDING row is Sr.9 "Other equity" (line 297), blank in quarter cols, populated only at FY-end (6,201.65) — a reporting-period convention, not a dormant transaction-class line. No exceptional-items / discontinued-ops / sale-of-subsidiary lines exist in the template to anticipate. |
| F2 Standalone vs consolidated | **FINDING** | No consolidated statement anywhere; S-vs-C gap non-computable. Foreign Entity excluded per Note 7 (subscription incomplete) — appropriate & disclosed, but a consolidation obligation is forthcoming. (A3-F2, FORWARD-SIGNAL, lines 356-357/381-383.) |
| F3 Shell-entity detection | **N.A.** | No consolidated cost lines to compare; the one non-reporting entity is newly incorporated with no operations/financials. Nothing to test. |
| F4 Unaudited contribution ratio | **N.A.** | Clean standalone limited review; no Other Matters paragraph, no JV/associate/component-auditor numbers exist (lines 191-217). |
| F5 Going concern / EoM scope | **PASS** | Auditor review is 4 paras (lines 191-217); NO Emphasis of Matter, NO Other Matters, NO Going Concern paragraph present — verified verbatim. Clean conclusion "nothing has come to our attention ... material misstatement" (212-217). Stated explicitly per instruction. |
| F6 Forward-commitment mining | **FINDING** | Multiple dated management commitments extracted (AGM, dividend record date, auditor term, Foreign Entity subscription, IPO capex deployment). See Commitment Register. Key forward items A3-F6a (subscription) & A3-F6b (IPO capex underspend). |
| F7 Hedge-phrase mining | **PASS** | Only lexicon hits are "subject to the approval of the shareholders/Members" (lines 76, 130) — standard governance conditionality on the auditor appointment. No newly-added hedge on revenue lumpiness or customer concentration. |
| F8 Tax forensics | **PASS** | ETR: Q1FY27 25.22% (85.11/337.51), Q4FY26 23.42%, Q1FY26 26.08%, FY26 25.22% — all near statutory 25.17%. Current-quarter deferred tax credit only (0.65)m = ~19 bps shield (immaterial). No "earlier years" tax-adjustment line. Q4FY26 large deferred credit (17.43)m sits in a balancing-figure quarter (Note 6) and self-explains. |
| F9 OCI forensics | **PASS** | Actuarial (defined-benefit remeasurement) only: Q1FY27 (0.72), Q4FY26 3.16, Q1FY25 (0.03), FY26 (2.89). Single-quarter swing |0.72| does NOT exceed full prior year |2.89|; no assumption-change signal. |
| F10 Share count & dilution | **PASS** | Paid-up capital 152.91m flat across all 4 periods — no corporate action. Basic EPS = Diluted EPS in every period (8.25/8.25, 5.06/5.06, 2.92/2.92, 15.34/15.34) — zero spread, no dilutive instruments. |
| F11 Reserves / net worth tie-out | **PASS** | FY26 net worth = Other equity 6,201.65 + Paid-up 152.91 = 6,354.56m (₹635.46 Cr). No third-party comparator (no rating rationale / slide) in the doc; no gap detectable. |
| F12 Segment forensics | **N.A.** | Single reportable segment "Auto Components and Parts" (Note 4, line 372); P&L-only filing carries no segment asset/liability data to trend. |
| F13 Board outcome beyond results | **FINDING** | Statutory auditor change + incoming firm was prior internal auditor (A3-F13a, AMBIGUOUS); AGM/record-date/dividend + AR-imminent (A3-F13b, FORWARD-SIGNAL). Lines 65-106. |
| F14 Note-drafting inconsistencies | **PASS** | Note 1 "reviewed by Statutory Auditors" (346) consistent with the limited-review letter — no audit/review mislabel. Entity name consistent ("Formerly known as ... Private Limited"). IPO sub-table foots. Only defect is a grammatically broken auditor-rationale sentence (103-105) — a drafting-quality nit, immaterial, no numeric/naming conflict. |
| F15 Entity-list diffs | **FINDING** | Addition of "Divgi Transmission Technologies and Systems Ltd." (Foreign Entity), incorporated 04-Jun-2026, first appearance (A3-F15, FORWARD-SIGNAL, lines 381-383). |
| F16 Presentation-specific | **N.A.** | Doctype is a results filing, not an investor presentation. |
| F17 Concall silence audit | **N.A.** | Doctype is a results filing, not a concall transcript; no Notion monitoring checklist exists (fresh company). |

Status tally: **PASS 8** (F1, F5, F7, F8, F9, F10, F11, F14) · **FINDING 4** (F2, F6, F13, F15) ·
**N.A. 5** (F3, F4, F12, F16, F17) = 17. No blanks. GATE A3: PASS.

---

## COMMITMENT REGISTER (from F6 / F13)

| commitment | implied date | note/agenda ref | status word |
|---|---|---|---|
| 61st AGM to be held | Fri 18-Sep-2026 | line 66 (agenda 2) | scheduled ("will be held") |
| Record/cut-off date for FY25-26 final dividend ₹3.27/sh (≈₹100m outflow) | Thu 10-Sep-2026 | lines 90-93 (agenda 4) | fixed |
| Kirtane & Pandit LLP statutory-auditor term begins (subject to member approval) | conclusion of 61st AGM (18-Sep-2026), 5 yrs to 66th AGM | lines 100-102 / 147-156 (agenda 5 / Annexure 2) | board-approved, pending AGM |
| Foreign Entity equity-subscription agreement completion → then consolidation | post 30-Jun-2026 (undated) | lines 382-383 (Note 7) | in process ("had not been completed") |
| Deploy remaining IPO capex ₹591.80m | undated | lines 361-365 (Note 3) | underway / unutilised (60.7% spent) |

---

## ROUTING FOR A4
- **Mandatory management questions (AMBIGUOUS + FORWARD-SIGNAL):** A3-F2, A3-F6a, A3-F6b, A3-F13a, A3-F13b, A3-F15.
- **AR Deep-Dive trigger (Role 6):** 61st AGM on 18-Sep-2026 ⇒ full FY26 Annual Report expected within weeks.
- **Promise-vs-delivery tracker seeds (Role 5):** Foreign Entity subscription completion; IPO capex deployment of remaining ₹591.80m; auditor-transition close-out at AGM.
- **Ledger correction to propagate:** row 2(b) FY26 = (80.76), superseding the A2-guessed (807.60).

```yaml
stage: A3-forensics
company: "divgi"
quarter: "q1fy27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/divgi-q1fy27/work/forensics_results_divgi_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: PASS
  F2: FINDING
  F3: N.A.
  F4: N.A.
  F5: PASS
  F6: FINDING
  F7: PASS
  F8: PASS
  F9: PASS
  F10: PASS
  F11: PASS
  F12: N.A.
  F13: FINDING
  F14: PASS
  F15: FINDING
  F16: N.A.
  F17: N.A.
findings:
  - {id: "A3-F2",   check: "F2",  line: "356-357,381-383", classification: "FORWARD-SIGNAL", implication: "Standalone-only; consolidation obligation forthcoming once foreign-entity subscription completes"}
  - {id: "A3-F6a",  check: "F6",  line: "382",             classification: "FORWARD-SIGNAL", implication: "Foreign Entity equity subscription to complete post 30-Jun-26; milestone to track"}
  - {id: "A3-F6b",  check: "F6",  line: "361-365",         classification: "AMBIGUOUS",      implication: "IPO capex only 60.7% deployed; ~Rs 591.8m undeployed since 2023 IPO"}
  - {id: "A3-F13a", check: "F13", line: "96-106,103-105",  classification: "AMBIGUOUS",      implication: "Statutory auditor change; incoming Kirtane & Pandit was prior internal auditor (independence question)"}
  - {id: "A3-F13b", check: "F13", line: "65-67,87-94",     classification: "FORWARD-SIGNAL", implication: "AGM 18-Sep-26, dividend Rs 3.27/sh, AR imminent -> schedule Role 6 deep dive"}
  - {id: "A3-F15",  check: "F15", line: "381-383",         classification: "FORWARD-SIGNAL", implication: "New foreign entity incorporated 04-Jun-26; cross-border expansion step"}
forward_signals: ["A3-F2", "A3-F6a", "A3-F13b", "A3-F15"]
ambiguous: ["A3-F6b", "A3-F13a"]
commitments:
  - {commitment: "61st AGM to be held", implied_date: "2026-09-18", ref: "line 66 (agenda 2)", status_word: "scheduled"}
  - {commitment: "Record/cut-off date for FY25-26 final dividend Rs 3.27/sh", implied_date: "2026-09-10", ref: "lines 90-93 (agenda 4)", status_word: "fixed"}
  - {commitment: "Kirtane & Pandit LLP statutory-auditor term begins, subject to member approval", implied_date: "2026-09-18", ref: "lines 100-102 (agenda 5)", status_word: "board-approved"}
  - {commitment: "Foreign Entity equity-subscription completion then consolidation", implied_date: "post-2026-06-30", ref: "lines 382-383 (Note 7)", status_word: "in-process"}
  - {commitment: "Deploy remaining IPO capex Rs 591.80m", implied_date: "undated", ref: "lines 361-365 (Note 3)", status_word: "underway"}
gate_a3: pass
blank_checks: []
```
