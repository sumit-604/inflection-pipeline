# A3 FORENSIC NOTES — Credo Brands Marketing Ltd (CREDO) — Q1 FY27 — DOCTYPE: results

Source: Un-audited **Standalone** Financial Results (quarter ended June 30, 2026) + Board
Outcome cover letter + Independent Auditor's Limited Review Report. Unit convention:
Millions (x0.1 to Rs Cr). First substantive coverage (no prior-quarter extract; Notion
checklist EMPTY). Standalone-only filer (Note 7, line 228) — no consolidated columns exist.

Ledger reconciliation: all A2 rows (8 notes, 34 line items incl. 4 zero_standing, 10 agenda,
9 auditor paras, 1 entity, plus C1-C6 context rows) READ at their cited lines and reconciled
100%. Every OCR_ARTIFACT number was arithmetically reconstructed from its components and
ties (see DATA-QUALITY note); no artifact corrupts a judgment below.

---

## FINDINGS TABLE

| id | check | ledger row ref | line | verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-F1-01 | F1 | Row 18 (Current tax, ZERO_STANDING) | 157 | "Current tax" [blank in Jun-30-2026 column; 78.64 / 23.73 / 211.80 in the other three periods] | AMBIGUOUS | Only period among four with ZERO current tax despite positive PBT (31.43); entire Q1FY27 tax is a deferred charge. Advance-tax/MAT-timing vs. genuine nil-current-tax is unresolved — A4 question. |
| A3-F6-01 | F6 | Note 5 | 216-221 | "requires gratuity to be calculated based on wages constituting at least 50% of total remuneration. This has resulted in an increase in gratuity benefits" | FORWARD-SIGNAL | New Labour Codes effective Nov 21, 2025 lift the gratuity/employee-cost run-rate structurally; Q1FY27 employee benefits 94.29 up +12.4% YoY (vs 83.87) while revenue up only +4.4% — margin drag persists into future quarters. |
| A3-F8-01 | F8 | Row 20 (Deferred Tax charge/(credit)) | 160 | "Deferred Tax charge/(credit) 8.58" [vs (24.87) / (4.41) / (47.73)] | FORWARD-SIGNAL | Sign FLIP: deferred tax is a CHARGE of 8.58 in Q1FY27 against persistent credits in all three comparatives. Prior credits = DTA build/utilisation; a charge signals DTA depletion and future ETR step-up. |
| A3-F8-02 | F8 | Row 19 (Excess provision earlier years, ZERO_STANDING) | 158-159 | "Excess provision of Income tax in relation to earlier years (0.31)" [FY26 column only] | NEUTRAL-FACT | Prior-year tax true-up present (immaterial, Rs 0.031 Cr) but per F8 any non-zero earlier-year adjustment is logged; watch for recurrence/enlargement. |

---

## CHECKLIST SCORECARD (all 17)

| Check | Status | One-line basis |
|---|---|---|
| F1 ZERO-VALUE STANDING LINES | **FINDING** | 4 zero_standing rows read. Exceptional Item (154), Excess-provision (158-159), Other Equity (174) are standard SEBI-template lines (Exceptional anticipates one-offs; FY26 carried 13.97 gratuity past-service cost). Anomaly = **Current tax blank in Q1FY27 only** (157) despite PBT 31.43 → A3-F1-01. |
| F2 STANDALONE vs CONSOLIDATED | **N.A.** | Standalone-only filer; no consolidated columns. Note 7 (228): "the company doesn't have any subsidiary, associate and joint venture company." No S-vs-C gap to compute. |
| F3 SHELL-ENTITY DETECTION | **N.A.** | No subsidiaries/JV/associates (Note 7, 228) → no consolidated cost lines to compare; no shells possible. |
| F4 UNAUDITED CONTRIBUTION RATIO | **N.A.** | Auditor's "Other Matters" paragraph ABSENT (grep 0 hits; report lines 73-99). No JV/associate/component-auditor numbers; 0% of PAT rests on unreviewed figures. |
| F5 GOING CONCERN / EoM SCOPE | **PASS** | No Emphasis-of-Matter and no Going-Concern paragraph present; clean unmodified conclusion (P4, 95-99). First coverage → no QoQ verbatim diff computable. Current EoM/GC scope recorded verbatim = NONE. |
| F6 FORWARD-COMMITMENT MINING | **FINDING** | Lexicon hits ("commenced" 40, "approved" 32/203) are trivial (meeting/results approval, completed). Substantive forward item = New Labour Codes ongoing gratuity impact (Note 5) → A3-F6-01. |
| F7 HEDGE PHRASE MINING | **PASS** | Lexicon ("subject to", "no assurance", "evaluating", "exploring", "in discussions", "endeavour", "may sometimes", "could have an effect") — zero hits in notes/auditor text. No newly-added hedge (no prior to diff anyway). |
| F8 TAX FORENSICS | **FINDING** | ETR: Q1FY27 27.30% / Q4FY26 26.09% / Q1FY26 23.46% / FY26 25.67% vs statutory 25.17%. Q1FY27 sits ~213bps ABOVE statutory (negative shield). Deferred-tax SIGN FLIP to a charge (160) → A3-F8-01; earlier-year adjustment (0.31) → A3-F8-02. |
| F9 OCI FORENSICS | **PASS** | Re-measurement gain/(loss) on defined benefit liability: 0.24 / 2.38 / (0.13) / 1.88. No single-quarter swing exceeds full prior year (FY26 = 1.88); no assumption-change signal. (Actuarial assumptions to verify at AR given Labour Codes — see A3-F6-01.) |
| F10 SHARE COUNT & DILUTION | **PASS** | Paid-up 130.79 (Q1FY27) vs 130.74 = +0.05M, traces cleanly to Note 4 (213): 24,000 ESOP shares x Rs 2 = Rs 0.048M. Basic vs diluted spread 0.00 quarterly, 0.01 FY26 — immaterial; Credo Stock Option Plan 2020 active (register). |
| F11 RESERVES & NET WORTH TIE-OUT | **PASS** | FY26 net worth = Other Equity 4,255.26 + Paid-up 130.74 = 4,386.00M (Rs 438.6 Cr). Other Equity blank in quarterly columns (standard SEBI convention). No third-party figure in filing to reconcile against → no gap detectable. |
| F12 SEGMENT FORENSICS | **N.A.** | Single business segment per Note 6 (225-226): "single business segment namely retailing of men's casual wear." No segment asset/liability table to trend. |
| F13 BOARD OUTCOME BEYOND RESULTS | **PASS** | Sole substantive agenda item = approval of Q1 results (A1, 28-38). A2-A10 (AR approval, AGM, record date, dividend, director action, auditor change, scrutinizer, new ESOP grant, capital-raise) all AGENDA_NOT_DISCLOSED — structurally expected for a results-only outcome letter; no Role 6 AR event or funding signal foreshadowed. A4 to confirm AGM/dividend timeline in a later intimation. |
| F14 NOTE DRAFTING INCONSISTENCIES | **PASS** | Note 1 (204) "Statutory Auditors have conducted limited review" is CONSISTENT with auditor P3 (86-93, SRE 2410 limited review) — no audit/limited-review mismatch. Entity name consistent ("Credo Brands Marketing Limited (fka ...Private Limited)"). All anomalies are OCR/scan-layer (see DATA-QUALITY), not the company's drafting. |
| F15 ENTITY LIST DIFFS | **N.A.** | Sole entity, standalone (Note 7, 228). First coverage → no prior consolidation list to diff. Current entity state recorded verbatim: no subsidiary/associate/JV. |
| F16 PRESENTATION DISCLOSURES | **N.A.** | No investor presentation in this filing set. |
| F17 CONCALL SILENCE AUDIT | **N.A.** | No concall transcript; Notion monitoring checklist EMPTY; results doctype. |

Blank checks: NONE. **GATE A3: PASS.**

---

## COMMITMENT REGISTER (from F6 + forward-relevant notes)

| commitment | implied date | note/turn ref | status word |
|---|---|---|---|
| New Labour Codes: gratuity computed on wages >=50% of total remuneration; elevated gratuity/employee-cost run-rate | effective Nov 21, 2025 | Note 5 (216-221) | completed (FY26 past-service cost 13.97 booked as Exceptional) / ongoing run-rate |
| Credo Stock Option Plan 2020 — further ESOP vesting/exercise and share allotment | rolling | Note 4 (213) | underway (24,000 shares allotted this quarter; plan active) |

---

## DATA-QUALITY NOTE (OCR_ARTIFACT investigation — each reconciled, no misstatement)

- Note 1 numbering: leading "1" dropped and "The"->"Toe" at lines 203/206/210 — scan artifact; Note 1 is present (anchor "were reviewed by the Audit Committee", 203). Confirmed 8 notes.
- Total Income "11273.64" (143) = Revenue 1,252.69 + Other Income 20.95 = 1,273.64 ✓ (leading-digit duplication). Q4 "11665.23"=1,665.23 ✓; FY26 "61029.53"=6,029.53 ✓.
- Total expenses "11242.21" (152) = sum of (a)-(g) = 1,242.21 ✓; Q4 1,459.16 ✓; Q1FY26 1,133.19 ✓; FY26 5,377.56 ✓ (Other expenses FY26 "1 558.85"=1,558.85 ✓).
- PBT-before-exceptional 31.43 = 1,273.64 - 1,242.21 ✓; FY26 "651,97"=651.97 ✓; Q1FY26 PBT "82,35"=82.35 ✓ (comma-for-period).
- Net profit "22,85" (162) = PBT 31.43 - tax 8.58 = 22.85 ✓.
- Other Equity "4 255.26" (174) = 4,255.26. Auditor firm-reg prefix garbled (104) but digits legible 001595S/S000168; UDIN 26109752XMVUNP9536 intact.
- Unlabeled subtotal (168, value 0.18) = remeasurement 0.24 + tax (0.06) = 0.18, equals "Total OCI net of tax" (169-170) because single OCI item — dropped caption, not a data error.

All artifacts reconstruct arithmetically; data integrity confirmed. Judgments above are not affected.

---

## NARRATIVE (forensic, non-thesis)

Clean unmodified limited review, standalone-only, single segment, no going-concern or
emphasis-of-matter language — governance surface is quiet. The forward-relevant tells are
in tax and cost structure, not disclosure:

1. **Tax is the loudest signal.** Q1FY27 carries zero current tax and an 8.58 deferred
   *charge* — a sign flip from persistent deferred *credits* in every comparative period.
   ETR (27.3%) runs above statutory, i.e. a negative shield. Read conservatively, this is
   DTA depletion with future ETR/cash-tax normalisation risk (A3-F8-01) and an open question
   on why current tax is nil in a profitable quarter (A3-F1-01).
2. **Labour-Code gratuity is a structural cost step, not a one-off.** FY26 took 13.97 as an
   exceptional past-service cost; the *ongoing* service-cost basis is now higher. Employee
   benefits +12.4% YoY against revenue +4.4% is consistent with that (A3-F6-01).
3. **Everything else reconciles.** Share count change ties to ESOP exercise; net worth ties;
   OCI is quiet; board outcome carries only results approval. No prior quarter and empty
   Notion mean F5/F15 diffs and F17 are not computable this run — recorded as N.A./PASS with
   current state captured verbatim for next-quarter baselining.

```yaml
stage: A3-forensics
company: "CREDO"
quarter: "Q1 FY27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/credo-q1fy27/work/forensics_results_credo_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: PASS
  F6: FINDING
  F7: PASS
  F8: FINDING
  F9: PASS
  F10: PASS
  F11: PASS
  F12: N.A.
  F13: PASS
  F14: PASS
  F15: N.A.
  F16: N.A.
  F17: N.A.
findings:
  - {id: "A3-F1-01", check: "F1", line: "157", classification: "AMBIGUOUS", implication: "Current tax blank in Q1FY27 only despite positive PBT 31.43; whole-quarter tax is a deferred charge — advance-tax/MAT timing vs genuine nil current tax unresolved."}
  - {id: "A3-F6-01", check: "F6", line: "216-221", classification: "FORWARD-SIGNAL", implication: "New Labour Codes lift gratuity/employee-cost run-rate structurally; employee benefits +12.4% YoY vs revenue +4.4% — margin drag persists forward."}
  - {id: "A3-F8-01", check: "F8", line: "160", classification: "FORWARD-SIGNAL", implication: "Deferred tax sign flip to an 8.58 charge from persistent credits signals DTA depletion and future ETR step-up."}
  - {id: "A3-F8-02", check: "F8", line: "158-159", classification: "NEUTRAL-FACT", implication: "Prior-year tax true-up (0.31) present (immaterial); logged per F8 non-zero rule, watch for recurrence."}
forward_signals: ["A3-F6-01", "A3-F8-01"]
ambiguous: ["A3-F1-01"]
commitments:
  - {commitment: "New Labour Codes gratuity basis (wages >=50% of remuneration); elevated gratuity/employee-cost run-rate", implied_date: "effective 2025-11-21", ref: "Note 5 (216-221)", status_word: "completed"}
  - {commitment: "Credo Stock Option Plan 2020 further ESOP vesting/exercise and allotment", implied_date: "rolling", ref: "Note 4 (213)", status_word: "underway"}
gate_a3: pass
blank_checks: []
```
