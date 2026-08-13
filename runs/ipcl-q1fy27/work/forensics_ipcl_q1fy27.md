# A3 FORENSIC NOTES — IPCL (INVPRECQ / BSE 504786) — Q1 FY27 — DOCTYPE: results

Source A1 extract: `extract_results_ipcl_q1fy27.txt` (7 pages, 377 lines, Lakh units).
A2 ledger: `ledger_results_ipcl_q1fy27.md` (gate_a2: pass).
Units: Rs. Lakhs; x0.01 -> Cr. Filing carries BOTH standalone and consolidated
statements. Prior-quarter extract NOT provided (PRIOR_LEDGER_NOT_PROVIDED) —
verbatim QoQ diffs (F5/F15) noted as limited where applicable.

## LEDGER RECONCILIATION — 100%

Every A2 ledger row was read at its cited line in the A1 extract before judging:
- Financial-results line items (42): Table 4 lines 146-184 (main table, 35 rows)
  and Format C lines 99-108 (7 rows). All read.
- Notes (6): lines 206, 208, 210, 212, 214, 216. All read.
- Auditor paras (10): standalone lines 238-266 + signatory 270-288 (4);
  consolidated lines 300-350 + signatory 353-370 (6). All read.
- Zero-standing (8): lines 153, 163, 167 (main table) + 103, 104, 105, 106,
  107-108 (Format C). All read.
- Entities (2): lines 301, 332 (Parent + I&PCL Vacuum Cast Limited). All read.
- Board outcome / covering letter: lines 41-71. All read.
Rows read / rows in ledger = 100%.

## BINDING-TRIGGER RECONCILIATION (operator's pre-committed Q1 FY27 test)

The operator pre-committed THREE thresholds this quarter as the binding test of
the AVOID thesis. Reconciled against the filing:

| # | Threshold | Filing evidence (line) | Result |
|---|-----------|------------------------|--------|
| 1 | EBITDA >= ₹9.5 Cr | PBET 710.48 (l.162) + Finance 171.82 (l.156) + Deprn 238.64 (l.157) = 1,120.94 L = **₹11.21 Cr** (₹11.06 Cr ex-other-income); Q1FY26 was ₹6.63 Cr | **MET** (+69% YoY) |
| 2 | A&D order book >= ₹100 Cr | No order-book line anywhere in filing | **NOT FOUND** — un-testable; management question |
| 3 | Power & Fuel < 9.5% of revenue | P&F 435.80 (l.158) / net sales 5,333.58 (l.147) = **8.17%**; Q1FY26 was 9.62% | **MET** (improved) |

Two of three pre-committed thresholds are affirmatively MET on disclosed
numbers; the third (A&D order book) is NOT DISCLOSED in this bare Reg 33 filing
and, per Note 2 (segment collapse, see F12), the segment line that would have
carried A&D visibility has just been removed. Net read: material FORWARD-SIGNAL
with a transparency caveat — routed to A4 (finding F13).

## FINDINGS TABLE

| id | check | ledger row ref | line | verbatim quote | classification | forward implication |
|----|-------|----------------|------|----------------|----------------|---------------------|
| F1 | F1 | Format C row 1A / row 3 (Table 6) | 102, 107-108 | "Total amount outstanding as on date 30.06.2026 \| 77.60"; row 3 "Total financial indebtedness ... \| --" | FORWARD-SIGNAL | Bank/revolving debt ₹77.60 Cr as at 30.06.2026 is UP vs the ~₹70 Cr FY26 watch (monitoring item 9), NOT drifting toward ₹50 Cr; finance cost 171.82 vs 159.08 Q1FY26 (+8% YoY, l.156) corroborates. Row 3 total-indebtedness prints a dash despite row 1A = 77.60 — internal inconsistency. Rising debt collides with the MD's 1% Guarantee-Commission-on-sanctioned-credit conflict. A4 question. |
| F2 | F2 | Net Profit row 9 (l.170); Other exp 4i (l.160) | 170, 160 | S "499.12 / 376.51 / 217.51 / 1,176.62" vs C "498.89 / 376.97 / 217.27 / 1,176.15" | AMBIGUOUS | S-vs-C PAT gap is trivially small (<0.5 L, <0.12% of standalone PAT — below the 5pp threshold) BUT the sign flips: consolidated EXCEEDS standalone only in Q4FY26 (+0.46 L) while the sole subsidiary is loss-making every period. Traces entirely to Other expenditure (l.160). Q4 is a note-4 balancing figure; low-priority A4 question. |
| F3 | F3 | Consol other-matter para 5 (l.332-335); Other exp 4i (l.160) | 332-335 | "wholly-owned subsidiary company, I&PCL Vacuum Cast Limited, whose interim financial results reflect total revenues of Nil ... net loss of 0.23 lacs" | FORWARD-SIGNAL | All cost lines identical S vs C except Other expenditure (l.160, +0.23 L) = subsidiary is a non-operating SHELL: Nil revenue, only ₹0.23 L expense. Name "Vacuum Cast" points to a pre-commissioning vacuum-casting (precision/A&D-adjacent) vehicle. No Going Concern EoM. Watch asset accretion as a capex proxy at AR. A4 question: purpose/capex plan of Vacuum Cast. |
| F8 | F8 | Earlier Years' Tax 8-EYT (l.167); Deferred tax 8-DT (l.168) | 167, 168 | "- Earlier Years' Tax \| 0.00 \| 0.00 \| 0.00 \| 7.61"; deferred tax "73.77 / (47.13) / 33.78 / 78.75" | NEUTRAL-FACT | Earlier-Years' Tax non-zero in FY26 (₹7.61 L) = F8 trigger. ETR Q1FY27 = 211.36/710.48 = 29.75%, ~4.6pp above statutory 25.17% (not on 22% concessional regime). Deferred tax swings +73.77 L (Q1FY27 charge) from (47.13) credit in Q4FY26 = 120.90 L swing lifting current-quarter ETR. Immaterial but note for AR. |
| F12 | F12 | Note 2 (l.208) | 208 | "the Company has from this year, identified Investment Casting Activities as its only reportable segment ... separate segment information is not required to be provided" | FORWARD-SIGNAL | Segment reporting COLLAPSED to a single segment starting this year — removes the disclosure line where Aerospace & Defence would appear, exactly the metric the pre-committed trigger (#2 A&D order book) needs. Transparency reduction on the watched axis. A4 question: A&D revenue/order-book split now that segment reporting is gone. |
| F13 | F13 | Covering letter (l.41-57); Notes; Format C | 41-57 | "the Board has considered and approved the Un-audited standalone and consolidated financial results" (l.42-43); no other agenda item | FORWARD-SIGNAL | Board Outcome carries ONLY results approval + audit-committee review (NO_AGENDA_BEYOND_STANDARD): no AGM notice, no dividend, no AR approval, and critically NO managerial-remuneration / MD-pay-cap (₹3.50->₹6.00 Cr) special resolution or related-party disclosure despite the governance tripwire. Monitoring reconciliation: trigger-1 EBITDA MET (₹11.21 Cr), trigger-3 P&F MET (8.17%), trigger-2 A&D order book NOT FOUND; external-processing (item 3) rising 30.4%->33.2% of total expenses (l.159 1,539.65 / l.161 4,641.98) = confirmatory-negative. Mixed signal, all NOT-FOUND items -> A4 questions. |
| F14 | F14 | Covering letter l.54 vs review reports / Note 1 | 54, 52, 206, 259, 301 | l.54 "The statutory auditors have issued an unmodified audit report on the financial results" vs l.259 "we do not express an audit opinion"; l.301 "and and its wholly-owned subsidiary" | NEUTRAL-FACT | Covering letter mischaracterises a Reg 33 LIMITED REVIEW (SRE 2410, review conclusion) as an "unmodified audit report"; contradicted by l.52 "Limited Review Report", Note 1 (l.206) and para 3 (l.259). Double-"and" typo l.301. Individually immaterial; cumulatively a filing-care governance data point. |

## CHECKLIST SCORECARD (all 17)

| Check | Status | Basis (one line) |
|-------|--------|------------------|
| F1 ZERO-VALUE STANDING | FINDING | 8 zero-standing rows read; Format C row 3 total-indebtedness dash despite row 1A ₹77.60 Cr; borrowings UP vs deleveraging watch (l.102, 107-108). Benign zeros: 4b stock-in-trade (l.153, pure manufacturer), 6 Exceptional (l.163, FY26-only 52.51), Format C default lines. |
| F2 STANDALONE vs CONSOLIDATED | FINDING | Gap <0.12% of standalone PAT (below 5pp) but sign flips positive->negative in Q4FY26 only (l.170); traces to Other exp (l.160); AMBIGUOUS. |
| F3 SHELL-ENTITY DETECTION | FINDING | I&PCL Vacuum Cast Ltd = shell: Nil revenue, ₹0.23 L loss, identical cost lines except Other exp (l.332-335, l.160); no GC EoM. |
| F4 UNAUDITED CONTRIBUTION | PASS | Unaudited subsidiary = net loss 0.23 L = 0.05% of consol PAT 498.89 (l.170, 334), far below 10% threshold; OTHER_MATTER_PARA noted. |
| F5 GOING CONCERN / EoM | PASS | No going-concern or EoM language in either review report (l.176 summary, l.190); nothing to track. Prior-quarter not provided; no scope change detectable. |
| F6 FORWARD-COMMITMENT MINING | PASS | 6 notes (l.206-216) read; no lexicon hit ("expected to","will be","underway","proposes to","board has approved" beyond results, etc.). Commitment register empty. |
| F7 HEDGE PHRASE MINING | PASS | No hedge lexicon ("no assurance","evaluating","exploring","subject to","in discussions") in the notes; only mild "wherever necessary" (l.216, Note 6). |
| F8 TAX FORENSICS | FINDING | Earlier-Years' Tax ₹7.61 L non-zero in FY26 (l.167) = trigger; ETR ~29.75% vs 25.17% statutory; deferred-tax 120.90 L QoQ swing (l.168). |
| F9 OCI FORENSICS | PASS | Actuarial OCI steady small positive (2.08/1.56/1.21/8.31, l.176); single-quarter (2.08) does not exceed prior year (8.31); no assumption-change swing. |
| F10 SHARE COUNT / DILUTION | PASS | Paid-up ₹1,000.00 L unchanged all periods (l.179); Basic = Diluted EPS every period (l.183-184), no spread, no dilutive instrument, no corporate action. |
| F11 RESERVES / NET WORTH | PASS | FY26 net worth ties: other equity 9,278.09 + paid-up 1,000 = ₹102.78 Cr standalone / ₹102.61 Cr consol (l.181, 179); quarter-end other equity blank per source (standard Reg 33); no third-party figure to reconcile; C<S by 17.11 L = subsidiary accumulated deficit. |
| F12 SEGMENT FORENSICS | FINDING | Note 2 (l.208) collapses reporting to a single "Investment Casting Activities" segment from this year, removing A&D visibility. |
| F13 BOARD OUTCOME BEYOND RESULTS | FINDING | Only results approval (l.42-43); NO_AGENDA_BEYOND_STANDARD; MD-pay-cap resolution / AGM / related-party absent; binding triggers 1&3 MET, trigger 2 NOT FOUND; external-processing rising (l.159). |
| F14 NOTE DRAFTING INCONSISTENCIES | FINDING | Covering letter "unmodified audit report" (l.54) vs limited-review conclusion (l.259); "and and" typo (l.301). |
| F15 ENTITY LIST DIFFS | PASS | Single WOS I&PCL Vacuum Cast Ltd (l.301); intra-filing consistent; prior-quarter ledger NOT provided so QoQ add/delete/rename diff not performable (PRIOR_LEDGER_NOT_PROVIDED) — no line evidences a change. |
| F16 PRESENTATION-SPECIFIC | N.A. | Doctype is a results filing, not an investor presentation. |
| F17 CONCALL SILENCE AUDIT | N.A. | Doctype is a results filing, not a concall transcript. (Monitoring-checklist reconciliation captured under F13.) |

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/turn ref | status word |
|------------|--------------|---------------|-------------|
| (none) | — | — | — |

No dated or dateable management commitments in the 6 notes (l.206-216). Register empty.

## FLAGGED FOR A4 (management questions)

FORWARD-SIGNAL: F1 (borrowings ₹77.60 Cr up vs deleveraging watch + guarantee-
commission conflict), F3 (Vacuum Cast shell — purpose/capex), F12 (segment
collapse hides A&D), F13 (A&D order book NOT FOUND; MD-pay-cap resolution not in
filing; external processing still rising).
AMBIGUOUS: F2 (S-vs-C PAT sign flip in Q4FY26).

```yaml
stage: A3-forensics
company: "IPCL"
quarter: "Q1FY27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/ipcl-q1fy27/work/forensics_ipcl_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: FINDING
  F3: FINDING
  F4: PASS
  F5: PASS
  F6: PASS
  F7: PASS
  F8: FINDING
  F9: PASS
  F10: PASS
  F11: PASS
  F12: FINDING
  F13: FINDING
  F14: FINDING
  F15: PASS
  F16: N.A.
  F17: N.A.
findings:
  - {id: "F1", check: "F1", line: "102,107-108", classification: "FORWARD-SIGNAL", implication: "Bank/revolving debt Rs77.60 Cr at 30.06.2026 UP vs ~70 Cr watch, not toward 50 Cr; row 3 total-indebtedness dash inconsistency; finance cost +8% YoY; collides with MD 1% guarantee-commission conflict"}
  - {id: "F2", check: "F2", line: "170,160", classification: "AMBIGUOUS", implication: "S-vs-C PAT gap immaterial (<0.12%) but sign flips (consol>standalone) only in Q4FY26 balancing-figure period; low-priority question"}
  - {id: "F3", check: "F3", line: "332-335", classification: "FORWARD-SIGNAL", implication: "I&PCL Vacuum Cast Ltd is a non-operating shell (Nil revenue, 0.23 L loss); name suggests pre-commissioning vacuum-casting/A&D vehicle; watch capex accretion"}
  - {id: "F8", check: "F8", line: "167,168", classification: "NEUTRAL-FACT", implication: "Earlier-Years Tax 7.61 L non-zero FY26; ETR ~29.75% vs 25.17%; deferred-tax 120.90 L QoQ swing; immaterial, note for AR"}
  - {id: "F12", check: "F12", line: "208", classification: "FORWARD-SIGNAL", implication: "Segment reporting collapsed to single segment this year, removing the A&D disclosure line the pre-committed trigger needs"}
  - {id: "F13", check: "F13", line: "41-57", classification: "FORWARD-SIGNAL", implication: "Bare board outcome; triggers 1&3 MET (EBITDA 11.21 Cr, P&F 8.17%), trigger 2 A&D order book NOT FOUND, MD-pay-cap resolution absent, external processing rising 30.4->33.2%"}
  - {id: "F14", check: "F14", line: "54", classification: "NEUTRAL-FACT", implication: "Covering letter calls limited review an 'unmodified audit report'; and-and typo l.301; filing-care governance data point"}
forward_signals: ["F1", "F3", "F12", "F13"]
ambiguous: ["F2"]
commitments: []
gate_a3: pass
blank_checks: []
```
