# A3 FORENSIC NOTES — E2E Networks Limited (E2E), Q1 FY27 — doctype: RESULTS

Source extract: `/home/user/inflection-pipeline/runs/e2e-q1fy27/work/extract_results_e2e_q1fy27.txt` (398 lines, 7 pages)
Ledger contract: `/home/user/inflection-pipeline/runs/e2e-q1fy27/work/ledger_results_e2e_q1fy27.md`
Unit convention: Rs Lakhs; x0.01 -> Rs Crores. (PBT Q1 FY27 = 5,862.64 lakhs = Rs58.63 Cr; Revenue = 15,675.99 lakhs = Rs156.76 Cr; net worth = 1,68,505.18 lakhs = Rs1,685.05 Cr.)
Ledger reconciliation: 100% — all 60 line-item rows, 18 notes, 10 auditor paragraphs, 5 signature blocks, 1 entity and both financial tables read verbatim at their cited lines before judging.

Note on comparatives: per Note 9 (L141-142) all prior-period "consolidated" columns are standalone-only figures (subsidiary incorporated 17-Jun-2026), so QoQ/YoY here is effectively standalone continuity, not a consolidation trend.

---

## FINDINGS TABLE

| id | check | ledger row ref | line | verbatim quote | classification | forward implication |
|----|-------|----------------|------|----------------|----------------|---------------------|
| A3-F1 | F1 | T3 r15 / T4 r15 (Current tax ZERO_STANDING) | 99 (consol), 183 (standalone) | "(a) Current tax   -   -   -   -" | FORWARD-SIGNAL | Zero current tax across all four periods despite a positive Q1 PBT of 5,862.64 lakhs. The anticipated transaction class for this template line (a cash-tax charge) is absent — profit is fully shielded by unabsorbed depreciation / carried-forward losses. Cash tax steps up once the depreciation shield stops outrunning book profit. |
| A3-F6 | F6 | T5 note 9 / T6 note 9 | 141-142 (consol), 227-228 (standalone) | "had not commenced its business operations as at June 30, 2026" | FORWARD-SIGNAL | Lexicon hit "commenc". Sovcloud Technologies Limited incorporated 17-Jun-2026, pre-operational at quarter-end. Commencement of subsidiary operations is a dateable Q2 FY27 milestone for the promise-vs-delivery tracker. |
| A3-F8 | F8 | T3 r15-18 / T4 r15-18 | 99-102 (consol), 183-186 (standalone) | "(c) Deferred Tax   1,474.43" ; "(b) Tax Expenses pertains to earlier years ... (40.96)" | FORWARD-SIGNAL | Entire Q1 tax charge (1,474.43) is deferred, current tax nil; deferred tax flipped from a credit in loss quarters (Q1 FY26 (91.21)) to a large charge now = DTA/carryforward being consumed. Book ETR 25.15% (1,474.43/5,862.64) sits at statutory 25.17% but cash-tax shield is ~2,515 bps of PBT. Also earlier-years tax adjustment (40.96) is non-zero in FY26 column (per-rule FINDING; CONFIRMATORY-NEGATIVE, prior period). |
| A3-F9 | F9 | T3 r21/r23 / T4 r21/r23 (OCI) | 107 & 110 (consol), 191 & 194 (standalone) | "(i) Items that will not be reclassified to profit or loss   (505.01)" | AMBIGUOUS | Q1 FY27 OCI (items not reclassified, i.e. actuarial remeasurement) is (505.01) gross / (377.91) net — a single-quarter swing exceeding the FULL prior year FY26 (125.47 gross / 93.89 net). Per rule = likely defined-benefit assumption change (discount rate / plan assets). Verify assumptions at Annual Report; direction uncertain -> A4 question. |
| A3-F10 | F10 | T3 r29-30 / T4 r29-30 (EPS) | 120-121 (consol), 203-204 (standalone) | "Basic 2.14 ... Diluted 2.10" | FORWARD-SIGNAL | Basic-vs-diluted spread opens to 0.04 (~1.9%) in Q1 FY27 vs zero spread in all prior periods. Dilutive potential shares surface now that the company is profitable (anti-dilutive/hidden in loss years). ~1.9% dilution overhang implied (ESOP/warrant) on ~20.56 Cr shares. A4 to identify the instrument. |
| A3-F14 | F14 | T6 note 2 vs T5 note 2; T5 note 9 vs T6 note 9 | 211 vs 128; 141 vs 227 | "the above unaudited standalone financial results for the year ended June 30, 2026" | NEUTRAL-FACT | Standalone Note 2 says "year ended June 30, 2026" where "quarter ended" is meant (consolidated Note 2 is correct); consolidated Note 9 describes the subsidiary without naming it while standalone Note 9 names "Sovcloud Technologies Limited". Individually immaterial drafting inconsistencies; cumulatively a governance/controls data point. |
| A3-F15 | F15 | T9 r1 (ENTITY_CHANGE) | 141-142, 227-228, 370-372 | "The Company incorporated Sovcloud Technologies Limited as its wholly owned subsidiary in India on June 17, 2026" | FORWARD-SIGNAL | New consolidation entity added this quarter. Name "Sovcloud" points to a sovereign/government-cloud vehicle; entity already carries a separate unmodified limited-review conclusion (dated 20-Jul, auditor para 4, L370-372) despite zero operations — suggests it may already hold capital/assets. Probe purpose, capex allocation and revenue plan with A4. |

---

## CHECKLIST SCORECARD (all 17, exactly one status each)

| # | Status | One-line basis |
|---|--------|----------------|
| F1 | FINDING | 4 ZERO_STANDING rows read (L94-95/99/179/183). Exceptional items = pure template/nil (NEUTRAL). Current tax = nil despite Rs58.6 Cr PBT -> forward finding above. |
| F2 | PASS | Standalone and consolidated P&L are line-for-line identical every period (subsidiary pre-operational, Note 9); S-vs-C gap = 0 on Revenue/EBITDA/PAT, no >5pp move. Gap will emerge from Q2 FY27. |
| F3 | PASS | Identical Cost/Employee/Depreciation lines confirm Sovcloud has zero operations (pre-operational, not a cleanup shell); no Going Concern / EoM paragraph in either report to reconcile against. |
| F4 | PASS | Consolidated auditor Other Matters (para 4, L370-372) states the subsidiary was reviewed by the same auditor with an unmodified conclusion; 0% of consolidated PAT rests on unaudited/management-furnished numbers. |
| F5 | PASS | No Emphasis of Matter, Other Matters-adverse, or Going Concern paragraph in either review report (clean conclusions L291-297, L374-380); nothing to verbatim-diff, no scope expansion. |
| F6 | FINDING | Notes lexicon sweep: hit "commenc" at Note 9 (subsidiary not yet commenced) -> forward milestone; sub-division and BSE listing are completed dated actions (register below). |
| F7 | PASS | Notes lexicon sweep ("subject to", "no assurance", "evaluating", "exploring", "in discussions", "endeavour", etc.) returns zero hits in either notes block (L124-142, L207-228). No newly-added revenue-lumpiness or concentration hedge. |
| F8 | FINDING | Tax forensics: nil current tax, deferred-only charge 1,474.43, book ETR 25.15% vs statutory 25.17%, deferred tax flipped credit->charge, earlier-years adj (40.96) non-zero. |
| F9 | FINDING | OCI (items not reclassified) single-quarter swing (505.01) gross exceeds full prior year 125.47 -> assumption-change flag, verify at AR. |
| F10 | FINDING | Basic/diluted EPS spread widens 0 -> 0.04 (~1.9%) in Q1 FY27; dilutive instruments surfaced. |
| F11 | PASS | Net worth tie-out: Other Equity 1,66,449.53 + Paid-up 2,055.65 = 1,68,505.18 lakhs (Rs1,685.05 Cr). No third-party number (rating/slide) in filing to reconcile; internal tie is clean, no reconciling gap. |
| F12 | N.A. | Note 6 (L138/224): single business segment, Ind AS 108 not applicable — filing carries no segment asset/liability tables to trend. |
| F13 | PASS | SINGLE_AGENDA_ITEM confirmed (L38-41): only results approval. No AR/AGM/record-date/dividend/appointment/auditor-change/ESOP/capital-raising resolution — normal for a March-FY-end Q1 board meeting; no forward resolution to schedule. |
| F14 | FINDING | Standalone Note 2 "year ended" mis-statement (L211) and consolidated Note 9 leaving the subsidiary unnamed while standalone names it — drafting inconsistencies. |
| F15 | FINDING | Entity list diff: Sovcloud Technologies Limited added to consolidation perimeter this quarter (incorporated 17-Jun-2026). |
| F16 | N.A. | Doctype is a results filing, not a presentation deck — no dropped/reframed slide disclosures to test. |
| F17 | N.A. | Doctype is a results filing, not a concall transcript — silence audit deferred to the concall pass. |

Counts: FINDING x7 (F1, F6, F8, F9, F10, F14, F15); PASS x7 (F2, F3, F4, F5, F7, F11, F13); N.A. x3 (F12, F16, F17). No blanks — GATE A3 satisfied.

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/turn ref | status word |
|------------|--------------|---------------|-------------|
| Sovcloud Technologies Limited to commence business operations | post 30-Jun-2026 (watch Q2 FY27) | Note 9 (L141-142 / L227-228) | initiated |
| 1:10 equity share sub-division (Rs10 -> Re1) | effective / record date 05-Jun-2026 | Note 4 (L131-135 / L216-220) | completed |
| BSE Main Board direct listing (in addition to NSE) | effective 12-Jun-2026 | Note 5 (L136-137 / L221-223) | completed |

---

## FORWARD NARRATIVE (context weighed, not anchored — Notion checklist targeting)

The three completed corporate actions plus the new subsidiary sit on top of an aggressive GPU capex build that shows up across the P&L: depreciation 6,064.44 lakhs (+18% QoQ, +121% YoY) and finance costs 1,005.15 lakhs (+173% QoQ, from 368.04) both rising fast, while current tax stays nil (F1/F8). Revenue 15,675.99 lakhs is +63.9% QoQ and +334% YoY (Notion item 7 green, though comparatives are standalone per Note 9). Operating EBITDA margin computes to ~75% on operating revenue (15,675.99 - 2,287.55 - 1,099.70 - 498.52), above the 64% guide (Notion item 9). The forward tension the document quietly carries: zero cash tax and a widening dilution spread today, against a subsidiary ("Sovcloud") and a leverage/depreciation ramp that will define Q2 FY27. These feed A4 as management questions, not conclusions.

Findings flagged to A4 (FORWARD-SIGNAL + AMBIGUOUS): A3-F1, A3-F6, A3-F8, A3-F9, A3-F10, A3-F15.

---

```yaml
stage: A3-forensics
company: "E2E"
quarter: "q1fy27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/e2e-q1fy27/work/forensics_e2e_q1fy27_results.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: PASS
  F3: PASS
  F4: PASS
  F5: PASS
  F6: FINDING
  F7: PASS
  F8: FINDING
  F9: FINDING
  F10: FINDING
  F11: PASS
  F12: N.A.
  F13: PASS
  F14: FINDING
  F15: FINDING
  F16: N.A.
  F17: N.A.
findings:
  - {id: "A3-F1", check: "F1", line: "99,183", classification: "FORWARD-SIGNAL", implication: "Nil current tax across all periods despite Rs58.6 Cr Q1 PBT; cash-tax step-up when depreciation shield exhausts"}
  - {id: "A3-F6", check: "F6", line: "141,227", classification: "FORWARD-SIGNAL", implication: "Sovcloud not yet commenced ops; commencement is a Q2 FY27 milestone to track"}
  - {id: "A3-F8", check: "F8", line: "99,101,102,183,185,186", classification: "FORWARD-SIGNAL", implication: "Deferred-only tax charge, DTA/carryforward being consumed, ~2515 bps cash-tax shield; ETR normalisation risk"}
  - {id: "A3-F9", check: "F9", line: "107,191", classification: "AMBIGUOUS", implication: "Single-quarter OCI swing (505.01) exceeds full prior year; likely actuarial assumption change, verify at AR"}
  - {id: "A3-F10", check: "F10", line: "120,203", classification: "FORWARD-SIGNAL", implication: "Basic/diluted EPS spread opens ~1.9%; dilutive instrument (ESOP/warrant) overhang surfaced"}
  - {id: "A3-F14", check: "F14", line: "211,141", classification: "NEUTRAL-FACT", implication: "Note 2 'year ended' misstatement and unnamed subsidiary in consol Note 9; governance/controls data point"}
  - {id: "A3-F15", check: "F15", line: "141,227,370", classification: "FORWARD-SIGNAL", implication: "New entity Sovcloud (sovereign-cloud) added; already separately reviewed despite zero ops; probe purpose/capex/revenue"}
forward_signals: ["A3-F1", "A3-F6", "A3-F8", "A3-F10", "A3-F15"]
ambiguous: ["A3-F9"]
commitments:
  - {commitment: "Sovcloud Technologies Limited to commence business operations", implied_date: "post 30-Jun-2026 (Q2 FY27)", ref: "Note 9 L141-142/L227-228", status_word: "initiated"}
  - {commitment: "1:10 equity share sub-division (Rs10->Re1)", implied_date: "2026-06-05", ref: "Note 4 L131-135/L216-220", status_word: "completed"}
  - {commitment: "BSE Main Board direct listing", implied_date: "2026-06-12", ref: "Note 5 L136-137/L221-223", status_word: "completed"}
gate_a3: pass
blank_checks: []
```
