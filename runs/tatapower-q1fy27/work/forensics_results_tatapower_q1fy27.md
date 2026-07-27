# A3 FORENSIC NOTES — Tata Power (TATAPOWER), Q1 FY27 — Doctype: RESULTS

Source spine: `extract_results_tatapower_q1fy27.txt` (19 pages, PDFium reconstruction,
100% coverage). All line refs below are the extract's internal `NNN|` line numbers
(the same convention the A2 ledger uses). Ledger reconciliation: 100% — every A2 row
(notes 74, line_items 213, zero_standing 1, agenda 4, auditor_paras 30, entities 96,
signature_blocks 14) was read at its cited line before judging.

Standalone AND consolidated both reconciled. Note the extraction's known digit-space
artifacts (e.g. "1 ,400.86" = 1,400.86; "(94.1 7)" = (94.17)); numbers below are
de-spaced.

---

## FINDINGS TABLE

| id | check | ledger row ref | line | verbatim quote | classification | forward implication |
|----|-------|----------------|------|----------------|----------------|---------------------|
| F1-A | F1 | C-27/C-28, CS-19 | 347-348, 426 | "Impairment of Investment … (94.17)" (Mar-26 & FY26 only; Jun-26 blank) | NEUTRAL-FACT | Q4FY26 carried a Rs 94.17cr exceptional impairment of investment that is absent in Q1FY27; the standing Exceptional Items template line anticipates further investment write-downs. QoQ PBT comparability is distorted by this one-off. |
| F1-B | F1 | S-22 (ZERO_STANDING) | 772 | "Current Tax   -   -   -   -" (standalone, all 4 periods dash) | FORWARD-SIGNAL | Standalone parent books ZERO current tax across every period shown while consolidated books Rs 225.14cr (C-31, line 351). Parent is running on carry-forward losses / MAT credit; when that shield exhausts, standalone cash tax steps up (~Rs 94cr/qtr at 25.17% on PBT 374.23). |
| F2-A | F2 | S-25 vs C-36 | 775 vs 356 | Standalone PAT "277.37 … 520.09" vs Consolidated PAT "1,400.86 … 1,262.32" | FORWARD-SIGNAL | Standalone PAT -47% YoY, consolidated PAT +11% YoY. S-vs-C PAT gap widened from Rs 742.23cr (143% of standalone PAT) to Rs 1,123.49cr (405% of standalone PAT) — a >250pp swing, far above the 5pp trigger. Parent earnings are deteriorating while the consolidated print is carried by subsidiaries/associates. |
| F4-A | F4 | CR-7a/7b, CR-9a/9b | 96-104, 122-127 | "43 subsidiaries … total net profit after tax of Rs 18.42 crore … not been reviewed by any auditor … furnished … by the Management" | AMBIGUOUS | Truly unaudited/management-furnished PAT = Rs 18.42cr = 1.3% of consolidated PAT (below 10%). BUT PAT reviewed only by OTHER (component) auditors, not the principal auditor SR BC = 127.79 + 168.44 + 18.42 = Rs 314.65cr = 22.5% of consolidated PAT — above the 10% threshold on the component-auditor basis. No prior-quarter disclosure supplied to trend the YoY jump (NOT FOUND). |
| F5-A | F5 | CR-6, SR-3, N-C4/N-S4 | 87-93, 646-653, 588-590, 1006-1008 | "no provision has been recorded … The hearings on the case are completed and the order is reserved in this matter" | FORWARD-SIGNAL | Emphasis of Matter in BOTH auditor reports over the SIAC/Kleros award USD 490.32m + 5.33% interest from 30-Nov-2020 + SGD 11.34m, with NO provision. Order is reserved at the SICC — an adverse ruling is a dateable, imminent (next 1-2 quarters) event that would crystallise a ~Rs 4,100cr+ liability with zero balance-sheet cushion. No prior-quarter extract supplied to verbatim-diff EoM scope (diff N/A). |
| F6-A | F6 | N-C3, N-S3 | 574-577, 992-995 | "extended up to 30th September, 2026, during which period management expects completion of the SPPA with the other procurers" | FORWARD-SIGNAL | Mundra Section 11 / SPPA with GUVNL is a dated management commitment: plant operation permission and SPPA completion with remaining procurers both hinge on 30-Sep-2026. If the other-procurer SPPAs are not signed and Section 11 not re-extended, Mundra dispatch is at risk in Q3FY27. |
| F7-A | F7 | N-C4/N-S4, N-C3/N-S3 | 588, 573, 1006, 992 | "does not foresee any affirmative payment obligation" / "approvals from the remaining procurers are in progress" | FORWARD-SIGNAL | Pre-emptive legal-cover hedges inside the Notes: the "no provision"/"does not foresee" language on a live USD 490m award, and "in progress" on the Mundra procurer approvals. Both tell you what management is bracing for; both are unresolved at quarter close. |
| F8-A | F8 | S-22, S-23 | 772-773 | standalone "Current Tax  -" with "Deferred Tax 96.86" | FORWARD-SIGNAL | Standalone ETR entirely deferred-tax driven (nil current tax), consolidated ETR ~23.2% (422.48/1,823.34) vs statutory 25.17%. Deferred-only pattern at parent = future cash-tax step-up risk (shield ~Rs 94cr/qtr). |
| F8-B | F8 | C-32, C-34 | 352, 354 | "Current Tax in respect of earlier period 1.34 … (18.50)"; "Deferred Tax In respect of earlier period (0.31) … 10.85" | NEUTRAL-FACT | Non-zero prior-year tax true-ups in Mar-26/Jun-25/FY26 (F8 flags any non-zero earlier-year tax adjustment). Immaterial in size but confirms recurring estimate revisions. |
| F8-C | F8 | C-22 / S-19 (reg deferral) | 341, 769 | consol "Total Movement in Regulatory Deferral Balances (Net) (153.09) 1,061.72 (570.76) 1,252.04" | AMBIGUOUS | Regulated-utility earnings-quality metric: consolidated regulatory deferral swung from +Rs 1,061.72cr (which lifted Q4FY26 PBT) to -Rs 153.09cr in Q1FY27; standalone -Rs 136.52cr. The Mar-26 comparator PBT was materially flattered by the deferral true-up. Trend and driver need a concall question. |
| F9-A | F9 | C-38 (i)/S-27 (i) OCI | 359, 778 | consol OCI "Income/(Expense) 219.41 (324.04) 67.06 (652.58)"; standalone "262.63 (440.25) 166.27 (471.81)" | AMBIGUOUS | Standalone single-quarter OCI (items not reclassified) swing of +Rs 703cr (from -440.25 in Mar-26 to +262.63 in Jun-26) EXCEEDS the full prior-year FY26 figure (-471.81) — F9 trigger for an assumption change (discount rate / FVOCI equity remeasurement). Verify driver (actuarial vs FVOCI equity) at the Annual Report. |
| F11-A | F11 | C-58/C-14, S-36/SR-14 | 380, 500, 786, 896 | consol Net Worth "42,153.39" vs Other Equity "39,147.65" + capital 319.56; standalone Net Worth "16,807.73" vs Other Equity "18,096.53" + 319.56 | AMBIGUOUS | Net-worth tie-out gap >5% BOTH statements and in OPPOSITE directions: consolidated net worth is Rs 2,686cr (+6.8%) ABOVE book owners' equity (likely NCI inclusion), standalone net worth is Rs 1,608cr (-8.7%) BELOW book equity (Section 2(57) excludes certain non-free reserves / FVOCI reserve). Reconciling items to confirm: NCI, revaluation/FVOCI reserves. |
| F12-A | F12 | CS-24 (assets) vs CS-31 (liab) | 435, 442 | Renewables Segment Assets "59,381.69 … 53,118.58"; Segment Liabilities "6,972.12 … 7,825.88 (Mar-26)" | FORWARD-SIGNAL | Renewables segment assets +Rs 6,263cr YoY (11.8% accretion, a capex proxy) while segment liabilities FELL QoQ (6,972 vs 7,825) — an equity/holdco-debt-funded build (debt sits in Unallocable liabilities Rs 85,809cr, line 445). Continued renewables capex at this rate implies a future external funding round. |
| F12-B | F12 | CS-30 / SS-23 (Thermal liab) | 441, 840 | consol Thermal & Hydro Segment Liabilities "4,198.48 … 8,426.02 (Jun-25)"; standalone "3,767.59 … 8,270.08" | AMBIGUOUS | Thermal & Hydro segment liabilities roughly halved YoY (down ~Rs 4,227cr consol, ~Rs 4,502cr standalone) — WC unwind on the Mundra suspension OR debt reduction. Direction uncertain; generate a concall question. |
| F14-A | F14 | N-C5 vs N-S5 | 591-593, 1009-1011 | consol: nine months "subjected to limited review"; standalone: "audited published figures of nine months" | NEUTRAL-FACT | Note 5 discloses the entire 31-Mar-26 (Q4) comparator column is a BALANCING figure (FY audited minus 9M), so every QoQ delta vs Mar-26 rests on a derived plug. The S vs C wording differs (standalone 9M audited, consolidated 9M only reviewed) — explained by differing audit provenance, but it means the consolidated Mar-26 plug is unaudited-derived. Treat all vs-Mar-26 deltas as soft. |

---

## CHECKLIST SCORECARD (all 17, one status each)

| Check | Status | Basis (one line) |
|-------|--------|------------------|
| F1 | FINDING | ZERO_STANDING S-22 standalone Current Tax nil all 4 periods (line 772); Exceptional Items standing line blank Jun-26 but (94.17) impairment Mar-26/FY26 (347-348). |
| F2 | FINDING | S-vs-C PAT gap widened from 143% to 405% of standalone PAT YoY (277.37 vs 1,400.86); >5pp trigger breached massively (775/356). |
| F3 | PASS | Consolidated cost lines materially exceed standalone (Employee Benefits 1,184.83 vs 223.52 line 330/760; D&A 1,259.86 vs 318.81) — subsidiaries have real operations; no going-concern EoM on any entity. |
| F4 | FINDING | Non-principal-auditor (component + management) PAT = Rs 314.65cr = 22.5% of consolidated PAT, above 10% (96-104, 122-127); truly unaudited alone = 1.3%; no prior period to trend jump. |
| F5 | FINDING | SIAC/Kleros EoM in BOTH auditor reports, USD 490.32m + interest + SGD 11.34m, no provision, SICC order reserved (87-93, 646-653, 588-590). Prior-quarter EoM diff not possible (no prior extract). |
| F6 | FINDING | Mundra SPPA/Section 11 dated commitment to 30-Sep-2026 with "management expects completion" (574-577, 992-995). |
| F7 | FINDING | Pre-emptive Note hedges: "does not foresee any affirmative payment obligation" (588/1006), "approvals … in progress" (573/992). |
| F8 | FINDING | Standalone nil current tax (deferred-only, future step-up); non-zero earlier-year tax true-ups (352/354); regulatory-deferral swing +1,061.72 to -153.09 (341). |
| F9 | FINDING | Standalone OCI (not reclassified) single-quarter swing +Rs 703cr exceeds full prior-year FY26 (-471.81) — assumption/FVOCI change (778); consolidated echoes (359). |
| F10 | PASS | Paid-up capital 319.56 unchanged all periods S and C (379/785); basic-vs-diluted EPS spread <=0.01 (383-387/789-793); no corporate action, no new dilutive instrument. |
| F11 | FINDING | Net-worth vs book-equity tie-out gap >5% both statements, opposite signs (consol +6.8%, standalone -8.7%) (380/500, 786/896). |
| F12 | FINDING | Renewables assets +11.8% YoY with QoQ-falling segment liabilities = equity-funded build (435/442); Thermal & Hydro liabilities ~halved YoY = ambiguous WC/debt (441/840). |
| F13 | PASS | Results-only Board agenda, 2h15m (line 17); dividend already approved at 7-Jul-2026 shareholder meeting (566); no AR approval, AGM notice, director appointment, or capital-raise resolution — nothing to schedule. |
| F14 | FINDING | Note 5 flags Mar-26 (Q4) column is a balancing plug; S vs C 9M audit provenance differs (591-593 vs 1009-1011). |
| F15 | N.A. | Applicable to doctype, but no prior-quarter Annexure 1 (96 entities) supplied to diff against — cannot perform (ledger confirms). Recommend A4 obtain Q4FY26 entity list. |
| F16 | N.A. | Doctype is results, not presentation. |
| F17 | N.A. | Doctype is results; no concall transcript in this run. |

Blank checks: none. GATE A3: PASS.

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/ref | status word |
|------------|--------------|----------|-------------|
| Complete SPPA with the other (non-GUVNL) procurers | 30-Sep-2026 | Note 3, line 576/994 ("management expects completion") | underway |
| Mundra Section 11 plant-operation permission (post-30-Jun-2026 window) | extended to 30-Sep-2026 | Note 3, line 575/993-994 | extended / underway |
| SICC ruling on setting-aside of SIAC/Kleros award | order reserved (date TBD) | Note 4, line 590/1008 ("hearings … completed and the order is reserved") | underway |
| FY2025-26 final dividend Rs 2.50/share (Rs 798.83cr) | paid 10-Jul-2026 | Note 2, line 566/985 | completed |

---

## FORWARD-SIGNAL / AMBIGUOUS ROUTING TO A4

- FORWARD-SIGNAL (management questions): F1-B (parent cash-tax step-up), F2-A (parent earnings deterioration masked by consol), F5-A (SIAC award, order reserved, no provision), F6-A (Mundra SPPA 30-Sep-2026 cliff), F7-A (no-provision / in-progress hedges), F8-A (deferred-only tax shield), F12-A (renewables equity-funded capex → funding round).
- AMBIGUOUS (lean-bear questions): F4-A (22.5% component-auditor reliance), F8-C (regulatory-deferral swing / Q4 flatter), F9-A (OCI assumption change), F11-A (net-worth tie-out gaps), F12-B (Thermal liabilities halved — WC vs debt).

```yaml
stage: A3-forensics
company: "TATAPOWER"
quarter: "Q1 FY27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "runs/tatapower-q1fy27/work/forensics_results_tatapower_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: FINDING
  F3: PASS
  F4: FINDING
  F5: FINDING
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: FINDING
  F10: PASS
  F11: FINDING
  F12: FINDING
  F13: PASS
  F14: FINDING
  F15: N.A.
  F16: N.A.
  F17: N.A.
findings:
  - {id: "F1-A", check: "F1", line: "347-348", classification: "NEUTRAL-FACT", implication: "Q4FY26 (94.17) exceptional impairment absent Q1FY27; distorts QoQ PBT comparability"}
  - {id: "F1-B", check: "F1", line: "772", classification: "FORWARD-SIGNAL", implication: "Standalone nil current tax all periods; future cash-tax step-up when shield exhausts"}
  - {id: "F2-A", check: "F2", line: "775", classification: "FORWARD-SIGNAL", implication: "Standalone PAT -47% vs consol +11%; S-vs-C gap widened 143%->405% of standalone PAT"}
  - {id: "F4-A", check: "F4", line: "122-127", classification: "AMBIGUOUS", implication: "22.5% of consol PAT reviewed only by component auditors, not principal auditor"}
  - {id: "F5-A", check: "F5", line: "588-590", classification: "FORWARD-SIGNAL", implication: "SIAC USD490.32m award, no provision, SICC order reserved = imminent crystallisation risk"}
  - {id: "F6-A", check: "F6", line: "574-577", classification: "FORWARD-SIGNAL", implication: "Mundra SPPA/Section 11 hard date 30-Sep-2026; dispatch at risk if procurer SPPAs unsigned"}
  - {id: "F7-A", check: "F7", line: "588", classification: "FORWARD-SIGNAL", implication: "Note hedges 'does not foresee'/'in progress' signal unresolved award and Mundra risk"}
  - {id: "F8-A", check: "F8", line: "772-773", classification: "FORWARD-SIGNAL", implication: "Deferred-only tax at parent; future ETR/cash-tax step-up"}
  - {id: "F8-B", check: "F8", line: "352", classification: "NEUTRAL-FACT", implication: "Non-zero earlier-year tax true-ups; recurring estimate revision"}
  - {id: "F8-C", check: "F8", line: "341", classification: "AMBIGUOUS", implication: "Reg-deferral swing +1,061.72 to -153.09 flattered Q4 comparator; earnings-quality question"}
  - {id: "F9-A", check: "F9", line: "778", classification: "AMBIGUOUS", implication: "Standalone OCI single-quarter swing exceeds full prior year; assumption/FVOCI change - verify at AR"}
  - {id: "F11-A", check: "F11", line: "500", classification: "AMBIGUOUS", implication: "Net-worth tie-out gap >5% both statements, opposite signs; NCI/reserve reconciliation needed"}
  - {id: "F12-A", check: "F12", line: "435", classification: "FORWARD-SIGNAL", implication: "Renewables +11.8% assets YoY, QoQ-falling seg liabilities = equity-funded build -> future funding round"}
  - {id: "F12-B", check: "F12", line: "441", classification: "AMBIGUOUS", implication: "Thermal & Hydro liabilities ~halved YoY; WC unwind or debt reduction - concall question"}
  - {id: "F14-A", check: "F14", line: "591-593", classification: "NEUTRAL-FACT", implication: "Mar-26 (Q4) column is a balancing plug; all vs-Mar-26 deltas are soft/unaudited-derived"}
forward_signals: ["F1-B", "F2-A", "F5-A", "F6-A", "F7-A", "F8-A", "F12-A"]
ambiguous: ["F4-A", "F8-C", "F9-A", "F11-A", "F12-B"]
commitments:
  - {commitment: "Complete SPPA with the other (non-GUVNL) procurers", implied_date: "2026-09-30", ref: "Note 3, line 576/994", status_word: "underway"}
  - {commitment: "Mundra Section 11 plant-operation permission window", implied_date: "2026-09-30", ref: "Note 3, line 575/993", status_word: "extended"}
  - {commitment: "SICC ruling on setting-aside of SIAC/Kleros award", implied_date: "TBD-order-reserved", ref: "Note 4, line 590/1008", status_word: "underway"}
  - {commitment: "FY2025-26 final dividend Rs2.50/share (Rs798.83cr)", implied_date: "2026-07-10", ref: "Note 2, line 566/985", status_word: "completed"}
gate_a3: pass
blank_checks: []
```
