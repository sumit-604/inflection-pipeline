# A3 FORENSIC NOTES — INDIQUBE (Indiqube Spaces Limited) — Q1FY27 — doctype: results (CRISIL Reg 32(6)/Schedule XI Monitoring Agency Report, IPO-proceeds utilisation)

Source extract: extract_results-monitoring_indiqube_q1fy27.txt (15 pages, 744 lines, unit = Rs million)
Ledger: ledger_results-monitoring_indiqube_q1fy27.md (155 enumerated units)
Ledger reconciled: 155 / 155 rows read at cited line = 100%
Prior extract: NONE (first pipeline run — no EoM / entity / dropped-slide verbatim diffs possible)

This document directly answers pre-committed Q1 monitoring question #3 ("IPO proceeds Rs 374 Cr unutilized — FY27 deployment plan and any promoter-linked recipient anticipated"). Doctype has no P&L / balance sheet / consolidation list / statutory-audit opinion / concall, so the standard financial checks F1-F5, F8-F12, F15-F17 are N.A. The load-bearing forensic work is the DEVIATION (postal-ballot reallocation into four new broad objects), the DELAY (underspend vs FY26 estimate), and the UTILISATION-STATE recompute.

---

## RECOMPUTE OF UTILISATION TOTALS (from raw rows)

Cross-checks performed against the raw Progress table (P1-P10) and Deployment summary:

- Unutilized Gross Proceeds = Rs 3,405.88M (Progress Total, line 458) = DS3 "Unutilized Gross Proceeds" (line 616). TIES. (= Rs 340.6 Cr.)
- Parked balance Rs 3,412.32M (DS1 line 610 / FD-Total line 606) minus earnings Rs 6.44M (DS2 line 613) = Rs 3,405.88M. TIES.
- Object-level utilised-to-date: new centres Rs 1,276.28M (P1 end, line 387) + GCP Rs 500.69M (P3 end, line 427) = Rs 1,776.97M = Note 3 utilised figure (line 651). TIES EXACTLY.
- Delay shortfall: FY26 estimate Rs 2,448.73M (Object1 Rs 1,944.03M + GCP Rs 504.70M, lines 639/644 & 649) minus utilised Rs 1,776.97M = Rs 671.76M shortfall. TIES.
- Progress sub-total columns (P8, line 450) each foot: proposed 6,044.59; beginning 2,306.38; during 383.99; end 2,690.37; unutilized 3,354.22 — all recomputed and correct.

INTERNAL INCONSISTENCY FOUND (immaterial, rounding): Progress "During quarter" Total = 389.02 (line 458), but sub-total 383.99 (line 450) + Issue expenses 5.04 (line 454) = 389.03 (0.01 drift). Issue-expenses "Total unutilized" = 51.66 (line 454) but proposed 455.41 − end 403.74 = 51.67 (0.01 drift). Both are single-paisa rounding artifacts; the headline unutilized Rs 3,405.88M and all object-level figures reconcile cleanly. No integrity concern — logged under F14 as NEUTRAL-FACT.

Utilisation state this quarter: only Rs 389.02M deployed during the quarter (P10 line 458); all four new objects (C4-C7 / P4-P7) at Nil; Rs 3,405.88M still unutilized, parked in 62 fixed deposits + Public Issue + Monitoring accounts.

---

## FINDINGS TABLE

| id | check | ledger row | line | verbatim quote | classification | forward implication |
|----|-------|-----------|------|----------------|----------------|---------------------|
| FND-1 | F6 | N3 / DL1-DL2 | 651-652 | "the Company has utilized Rs 1,776.97 million only as at quarter ended June 30, 2026. Hence, there is a delay... This delay is on account of lower operational requirements." | AMBIGUOUS | Rs 671.76M underspend vs FY26 estimate. "Lower operational requirements" may signal softer leasing/expansion demand rather than pure timing. Convert to management question: is slower new-centre capex demand-driven (fewer centres needed) or capex-efficiency? Ties pre-committed Q1. |
| FND-2 | F6 | N2 / C4-C7 / P4-P7 / OD1 | 357-362; 482-483 | "reallocation of proceeds from Object 1... to four additional objects as stated above (Objects 4 -7)" and "Rs 1,868.68 million during Fiscal 2027... from the Net Proceeds towards establishment of such new centers" | FORWARD-SIGNAL | Rs 1,870M reallocated/new-object firepower is entirely undeployed (all Nil this quarter); FY27 is the deployment year. Answers pre-committed Q1 FY27-deployment-plan question. Watch the recipient of the first draws next quarter. |
| FND-3 | F7 | C5/C7 / P5/P7 / N2 | 448; 438; 359-361 | "Capital deployment in strategic commercial real estate opportunities" (Rs 640M) and "fit-out and interior in non-Indiqube properties" (Rs 550M); "a portion of the funds... can also be efficiently deployed towards other synergic opportunities" | FORWARD-SIGNAL | The two broadest-mandate objects (Rs 1,190M combined) are the exact channels that could route IPO cash to promoter-linked entities (Innoprop / Grub RPT context; promoter+group 60.10%). Pre-committed checklist #3 RED trigger. A4 question: named counterparties/lessors for non-Indiqube fit-out and "strategic CRE." |
| FND-4 | F13 | N2 | 357-358 | "Shareholder's approval has been obtained vide special resolution dated June 24, 2026 through Postal Ballot Notice, for reallocation of proceeds from Object 1" | FORWARD-SIGNAL | Shareholder-approved latitude to redeploy IPO proceeds into discretionary objects, passed ~6 days before quarter-end. Governance-enabling event foreshadowing FY27 discretionary deployment. A4 to confirm no promoter-linked recipient anticipated. |
| FND-5 | F14 | OD table (Section 9) / DROPPED_DESCRIPTION | 471-517 | "Brief description of objects" (page-10 table describes only legacy Objects 1-3; Objects 4-7 have no narrative entry) | AMBIGUOUS | The four new discretionary objects (incl. Rs 640M strategic CRE, Rs 550M non-Indiqube fit-out) carry zero description of how/where/to-whom funds deploy — opacity precisely where promoter-routing risk is highest. A4 question: request object-level deployment narrative for Objects 4-7. |
| FND-6 | F14 | P8/P9/P10 | 450/454/458 | Total "during quarter" = "389.02" vs 383.99 + 5.04 = 389.03; issue-exp unutilized "51.66" vs 51.67 computed | NEUTRAL-FACT | 0.01M rounding drift only; headline Rs 3,405.88M unutilized and all object-level figures reconcile. No integrity concern; noted for completeness. |
| FND-7 | F7 | DC5 / MA declaration | 138-141; 697-700 | "The MA or its affiliates may have credit rating or other commercial transactions with the entity... we do not perceive any conflict of interest" | NEUTRAL-FACT | Standard MA boilerplate: CRISIL both rates and monitors the issuer, self-cleared. Disclosed, low weight; logged so the ledger CONFLICT_OF_INTEREST flag is reconciled. |

---

## CHECKLIST SCORECARD (all 17)

| Check | Status | Basis |
|-------|--------|-------|
| F1 Zero-value standing line items | N.A. | No P&L/template standing lines (no exceptional/sale-of-subsidiary/impairment structure). The nil-utilisation object rows (P4-P7) are the four new objects, addressed under F6 (FND-2), not as template anticipation. |
| F2 Standalone vs Consolidated | N.A. | No standalone/consolidated split in a monitoring report. |
| F3 Shell-entity detection | N.A. | No cost lines / subsidiary structure disclosed. |
| F4 Unaudited contribution ratio | N.A. | No statutory audit / component auditors. MA "does not perform an audit" (line 130); the S K Patodia CA certificate is not a statutory audit opinion. |
| F5 Going concern / EoM | N.A. | No auditor's report / EoM paragraph; no prior extract to diff. |
| F6 Forward-commitment mining | FINDING | FND-1 (delay/underspend), FND-2 (four new objects + FY27 deployment commitments). See Commitment Register. |
| F7 Hedge phrase mining | FINDING | FND-3 (discretionary "strategic opportunities" / non-Indiqube / "synergic opportunities" latitude); FND-7 (MA "may have... commercial transactions" conflict boilerplate). |
| F8 Tax forensics | N.A. | No tax lines / ETR in this doctype. |
| F9 OCI forensics | N.A. | No OCI / actuarial disclosure. |
| F10 Share count & dilution | N.A. | No paid-up capital / EPS disclosure. |
| F11 Reserves & net worth tie-out | N.A. | No equity / reserves disclosure. |
| F12 Segment forensics | N.A. | No segment tables. |
| F13 Board outcome beyond results | FINDING | FND-4: postal-ballot special resolution (24-Jun-2026) reallocating IPO proceeds and creating four new objects — a shareholder-approved enabling resolution foreshadowing FY27 discretionary deployment. |
| F14 Note-drafting inconsistencies | FINDING | FND-5 (object-description table not updated for new Objects 4-7 = disclosure gap); FND-6 (0.01M rounding drift in Progress totals). |
| F15 Entity list diffs | N.A. | No consolidation entity list; first run, no prior list to diff. |
| F16 Presentation dropped/reframed disclosures | N.A. | Not a presentation/deck. |
| F17 Concall silence audit | N.A. | Not a concall/transcript; no turns to audit. Monitoring-checklist #3 promoter-recipient watch is addressed via FND-2/FND-3/FND-4/FND-5 for A4. |

No check left blank. GATE A3: pass.

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/ref | status word |
|-----------|--------------|----------|-------------|
| Deploy Rs 1,868.68M on new centres (1.24 msf) | Fiscal 2027 | OD1, line 482-483 | proposes to (FY27 tranche not started; Nil this qtr) |
| Deploy Rs 813.78M on new centres (0.54 msf) | Fiscal 2028 | OD1, line 483-484 | proposes to |
| Deploy four new objects (security deposit Rs 520M, non-Indiqube fit-out Rs 550M, renewable power Rs 160M, strategic CRE Rs 640M) | FY27+ (post 24-Jun-2026 approval) | N2 / C4-C7 / P4-P7, line 357-362 | board proposed / shareholder-approved; deployment NOT initiated (all Nil) |
| Carry unutilised Net Proceeds forward to later Fiscals | subsequent Fiscals | N3, line 654-656 | intends to ("shall be utilized in subsequent Fiscals") |

---

## HANDOFF TO A4

FORWARD-SIGNAL findings (management questions to draft): FND-2, FND-3, FND-4.
AMBIGUOUS findings (lean-bear questions): FND-1, FND-5.
Core governance thread for A4: the Rs 640M "strategic commercial real estate opportunities" and Rs 550M "non-Indiqube properties fit-out" objects are broad, undescribed (FND-5), undeployed (FND-2), and shareholder-enabled (FND-4) — the precise deployment channels flagged in monitoring checklist #3 for promoter-linked recipients (Innoprop/Grub RPT; promoter+group 60.10%). Convert into direct management questions on counterparty identity and RPT screening before first FY27 draws.

```yaml
stage: A3-forensics
company: "INDIQUBE"
quarter: "Q1FY27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/indiqube-q1fy27/work/forensics_results-monitoring_indiqube_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: N.A.
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
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
  - {id: "FND-1", check: "F6", line: "651-652", classification: "AMBIGUOUS", implication: "Rs 671.76M underspend vs FY26 estimate; 'lower operational requirements' may signal softer expansion demand vs timing"}
  - {id: "FND-2", check: "F6", line: "357-362; 482-483", classification: "FORWARD-SIGNAL", implication: "Rs 1,870M new/reallocated objects entirely undeployed; FY27 is the deployment year; watch first-draw recipient"}
  - {id: "FND-3", check: "F7", line: "448; 438; 359-361", classification: "FORWARD-SIGNAL", implication: "Rs 1,190M broad discretionary objects are the exact channels for possible promoter-linked routing; checklist #3 RED trigger"}
  - {id: "FND-4", check: "F13", line: "357-358", classification: "FORWARD-SIGNAL", implication: "Postal-ballot special resolution enabling discretionary IPO-proceeds redeployment; confirm no promoter-linked recipient"}
  - {id: "FND-5", check: "F14", line: "471-517", classification: "AMBIGUOUS", implication: "New Objects 4-7 have no description narrative; opacity where promoter-routing risk is highest"}
  - {id: "FND-6", check: "F14", line: "450/454/458", classification: "NEUTRAL-FACT", implication: "0.01M rounding drift only; headline totals reconcile; no integrity concern"}
  - {id: "FND-7", check: "F7", line: "138-141; 697-700", classification: "NEUTRAL-FACT", implication: "MA rates and monitors same issuer, self-cleared conflict; standard boilerplate, low weight"}
forward_signals: ["FND-2", "FND-3", "FND-4"]
ambiguous: ["FND-1", "FND-5"]
commitments:
  - {commitment: "Deploy Rs 1,868.68M on new centres (1.24 msf)", implied_date: "FY2027", ref: "OD1 line 482-483", status_word: "proposes to"}
  - {commitment: "Deploy Rs 813.78M on new centres (0.54 msf)", implied_date: "FY2028", ref: "OD1 line 483-484", status_word: "proposes to"}
  - {commitment: "Deploy four new objects (Rs 520M/550M/160M/640M)", implied_date: "FY27+ post 24-Jun-2026", ref: "N2/C4-C7/P4-P7 line 357-362", status_word: "shareholder-approved, not initiated"}
  - {commitment: "Carry unutilised Net Proceeds forward to later Fiscals", implied_date: "subsequent Fiscals", ref: "N3 line 654-656", status_word: "intends to"}
gate_a3: pass
blank_checks: []
```
