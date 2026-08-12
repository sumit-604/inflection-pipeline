# A3 FORENSIC NOTES — 526717 (HCP Plastene Bulkpack Ltd), Q1FY27
Doctype: results (Regulation 30 event disclosure — CFO resignation, 3 pages)
Source extract: runs/526717-q1fy27/work/extract_reg30cfo_526717_q1fy27.txt
Ledger reconciled: 37/37 unique field rows read verbatim at cited lines (Tables 1-3);
Table 4 (3 signature cross-refs) also read. Reconciliation 100%.

## DOCTYPE NOTE
This is a single-topic Reg 30 KMP-cessation letter with no P&L, balance sheet,
auditor report, notes, segments, consolidation list, or concall transcript. The
balance-sheet/audit/financial checks (F2-F5, F8-F12, F15) and the
presentation/concall checks (F16, F17) have no applicable rows and are marked
N.A. with a one-line basis each. The governance / KMP / disclosure checks that DO
apply (F1, F6, F7, F13, F14) are run in full.

## THE ASSESSMENT ASKED (event facts, anchored)
- Stated reason (verbatim): "for further career opportunity" (BSE letter l.58;
  Annexure A reason row l.99-100; CFO letter l.131). CFO adds "there is no
  material reason other than mentioned above for my resignation" (l.134-135).
- Effective date: w.e.f. 12 August 2026 (Annexure A l.99; cessation-date row
  l.101; CFO letter "from 12/08/2026" l.131). OCR renders "12t"/"12%" = 12th.
- Immediate or with notice: IMMEDIATE. Effective date equals the letter date
  equals the filing date; no notice period, no handover/relief date, no interim
  continuation. (l.55-58 filing date 12 Aug 2026 = l.99 w.e.f. date.)
- Successor named: NO. Annexure A carries no appointment/successor field
  populated; Brief Profile "NA" (l.103), relationships "NA" (l.104-106). No
  acting/interim CFO disclosed.
- Timing vs results: filed 12 Aug 2026, per injected context the same day as the
  Q1 FY27 results.
- Timing vs prior governance exits: Company Secretary resigned Jan-2026; internal
  auditor (S.A. Gadhia & Co) withdrew consent 17-Jul-2026, ~7 weeks after
  appointment; CFO resigns 12-Aug-2026 (this filing) — third governance/KMP exit
  in ~7 months.

## FINDINGS TABLE
| id | check | ledger row ref | line | verbatim quote | classification | forward implication |
|----|-------|----------------|------|----------------|----------------|---------------------|
| A3-F07-01 | F7 | T3 row 7 (l.134-135) | 134-135 | "there is no material reason other than mentioned above for my resignation" | AMBIGUOUS | Pre-emptive SEBI-boilerplate denial paired with the most generic possible reason ("further career opportunity"); against a 3-exit governance cluster its assurance value is low. A4 question: is the disclosed reason complete, and did the audit committee independently record the reason? |
| A3-F13-01 | F13 | T2 rows 3-5 (l.101-107) | 101-107 | "Brief Profile (in case of appointment) NA" (l.103); "Resignation letter Attached" (l.107) | FORWARD-SIGNAL | No successor or interim CFO named. Sec 203 Companies Act / LODR require a CFO KMP; vacancy must be filled within 3 months (by ~12-Nov-2026). Watch for a successor-appointment Reg 30 filing; interim financial-signing-authority gap. |
| A3-F13-02 | F13 | T2 row 2 (l.99-100); T3 row 6 (l.131) | 99-100, 131 | "has resigned from the post of Chief Financial Officer w.e.f. 12t August 2026"; "I hereby tender my resignation ... from 12/08/2026" | FORWARD-SIGNAL | Effective immediately, zero notice/handover, on the results-filing day. Continuity-of-controls risk over financial reporting exactly at the reporting boundary. |
| A3-F13-03 | F13 | T1 row 8 (l.55-58) | 55-58 | "Mr. Dhrumil PranavKumar Shah, Chief Financial Officer ... has tendered his resignation" | FORWARD-SIGNAL | Third governance/KMP exit in ~7 months (CS Jan-2026; internal-auditor consent withdrawal 17-Jul-2026; CFO 12-Aug-2026). Directly trips Notion monitoring item 6 ("No further KMP/CS resignation within 12 months of the Jan-2026 CS exit"). Escalate FLAG-GOVERNANCE; consistent with FLAG-PROMOTER (CONCERN). |
| A3-F13-04 | F13 | T1 row 1 (l.34); body l.55-58 | 34, 55-58 | "12t August 2026" (letter date) | AMBIGUOUS | CFO departs on the same day the Q1 FY27 results are filed. A4 question: did the resigning CFO certify/sign off the Q1 FY27 financials before cessation, and is that certification on record? |
| A3-F14-01 | F14 | T2 row 6, NUMBERING_ANOMALY (l.107) | 104, 107 | two rows both printed "5." — "5. ... relationships ..." (l.104) and "5. Resignation letter Attached" (l.107) | NEUTRAL-FACT | Sr.No. sequencing error (second "5." should be "6."). Individually immaterial; cumulatively consistent with FLAG-DISCLOSURE drafting sloppiness. |
| A3-F14-02 | F14 | T4 row 3, SIGNATORY_UNIDENTIFIED (l.144-151) | 151 | "DIRECTO!" [OCR-truncated; no director name] | AMBIGUOUS | The director who countersigned/accepted the resignation "FOR HCP PLASTENE BULKPACK LIMITED" is not named in the extract (NOT FOUND). A4/monitoring: identify the accepting authority; relevant given active governance flags. |
| A3-F14-03 | F14 | T4 rows 1-3, NO_TIMESTAMP (l.143-145) | 34, 74, 117 | letter dates only: "12t August 2026" (l.34), "Date: 12/08/2026" (l.117); no signing timestamp | NEUTRAL-FACT | No signature/filing timestamp anywhere in the filing, so the Reg 30 disclosure-timeliness window (KMP-resignation disclosure duty) cannot be verified from this extract (NOT FOUND). Monitoring item 6's "no repeat SEBI/BSE disclosure lapse" cannot be cleared from this document alone; A4 to confirm the actual BSE filing timestamp. |

## CHECKLIST SCORECARD
| Check | Status | Basis (one line) |
|-------|--------|------------------|
| F1 ZERO-VALUE STANDING ITEMS | PASS | Both ZERO_STANDING Annexure rows read (l.103-106); "NA" because they are appointment-only template fields on a resignation; no concealed transaction class. Financial exceptional-item lines: none in this doctype. |
| F2 STANDALONE vs CONSOLIDATED | N.A. | No standalone/consolidated financials in an event letter. |
| F3 SHELL-ENTITY DETECTION | N.A. | No cost lines / no subsidiary entities disclosed. |
| F4 UNAUDITED CONTRIBUTION RATIO | N.A. | No auditor Other Matters / no PAT. |
| F5 GOING CONCERN / EoM SCOPE | N.A. | No auditor report or EoM paragraph. |
| F6 FORWARD-COMMITMENT MINING | PASS | Full prose scan (l.55-62, 130-140): zero lexicon hits; no successor/transition/board-approval commitment language (that absence carried under F13-01). |
| F7 HEDGE PHRASE MINING | FINDING | Pre-emptive "no material reason other than mentioned above" denial, l.134-135 (A3-F07-01). |
| F8 TAX FORENSICS | N.A. | No tax figures. |
| F9 OCI FORENSICS | N.A. | No OCI / actuarial data. |
| F10 SHARE COUNT & DILUTION | N.A. | No share capital / EPS. |
| F11 RESERVES & NET WORTH | N.A. | No equity / reserves data. |
| F12 SEGMENT FORENSICS | N.A. | No segment tables. |
| F13 BOARD OUTCOME / KMP | FINDING | KMP cessation: no successor (A3-F13-01), immediate/no-notice (A3-F13-02), third exit in 7 months tripping monitoring item 6 (A3-F13-03), results-day timing (A3-F13-04). |
| F14 DRAFTING INCONSISTENCIES | FINDING | Numbering anomaly (A3-F14-01), unidentified countersignatory (A3-F14-02), no timestamp / timeliness unverifiable (A3-F14-03). |
| F15 ENTITY LIST DIFFS | N.A. | No consolidation entity list. |
| F16 PRESENTATION DROPPED/REFRAMED | N.A. | Not a presentation. |
| F17 CONCALL SILENCE AUDIT | N.A. | No concall transcript; the Notion monitoring item-6 linkage is handled under F13-03. |

## COMMITMENT REGISTER (from F6)
None. The filing contains no forward-commitment language and — notably for a KMP
cessation — no transition-plan, successor-appointment, or interim-arrangement
commitment. The absence is itself a forward signal, carried as A3-F13-01.

## RECONCILIATION
All 37 unique ledger field rows (Table 1: 17, Table 2: 6, Table 3: 14) read
verbatim at their cited lines; Table 4's 3 signature cross-refs also read. A2
flags NUMBERING_ANOMALY, SIGNATORY_UNIDENTIFIED, NO_TIMESTAMP each escalated to a
finding (A3-F14-01/02/03). ZERO_STANDING rows resolved at F1. Reconciled 100%.

```yaml
stage: A3-forensics
company: "526717"
quarter: "q1fy27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/526717-q1fy27/work/forensics_reg30cfo_526717_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: PASS
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: PASS
  F7: FINDING
  F8: N.A.
  F9: N.A.
  F10: N.A.
  F11: N.A.
  F12: N.A.
  F13: FINDING
  F14: FINDING
  F15: N.A.
  F16: N.A.
  F17: N.A.
findings:
  - {id: "A3-F07-01", check: "F7", line: "134-135", classification: "AMBIGUOUS", implication: "Pre-emptive no-material-reason denial + generic reason against a 3-exit cluster; A4 to test completeness of the stated reason."}
  - {id: "A3-F13-01", check: "F13", line: "101-107", classification: "FORWARD-SIGNAL", implication: "No successor/interim CFO; Sec 203 3-month fill clock (~12-Nov-2026); watch successor Reg 30 filing."}
  - {id: "A3-F13-02", check: "F13", line: "99-100,131", classification: "FORWARD-SIGNAL", implication: "Immediate, zero-notice cessation on results-filing day; continuity-of-controls risk at the reporting boundary."}
  - {id: "A3-F13-03", check: "F13", line: "55-58", classification: "FORWARD-SIGNAL", implication: "Third governance/KMP exit in ~7 months; trips Notion monitoring item 6; escalate FLAG-GOVERNANCE."}
  - {id: "A3-F13-04", check: "F13", line: "34,55-58", classification: "AMBIGUOUS", implication: "CFO departs on Q1 FY27 results-filing day; A4 to confirm CFO signed off the Q1 numbers pre-cessation."}
  - {id: "A3-F14-01", check: "F14", line: "104,107", classification: "NEUTRAL-FACT", implication: "Duplicate Sr.No. '5.' numbering error; minor, consistent with FLAG-DISCLOSURE sloppiness."}
  - {id: "A3-F14-02", check: "F14", line: "151", classification: "AMBIGUOUS", implication: "Accepting/countersigning director not named (NOT FOUND); A4/monitoring to identify."}
  - {id: "A3-F14-03", check: "F14", line: "34,74,117", classification: "NEUTRAL-FACT", implication: "No signing/filing timestamp; Reg 30 timeliness window unverifiable from extract; monitoring item 6 disclosure-lapse cannot be cleared here."}
forward_signals: ["A3-F13-01", "A3-F13-02", "A3-F13-03"]
ambiguous: ["A3-F07-01", "A3-F13-04", "A3-F14-02"]
commitments: []
gate_a3: pass
blank_checks: []
```
