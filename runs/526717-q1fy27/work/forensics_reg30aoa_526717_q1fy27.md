# A3 FORENSIC NOTES — Reg 30 AoA Adoption Disclosure
Company: HCP Plastene Bulkpack Ltd (526717) | Quarter tag: q1fy27 | Doctype: results (Regulation 30 event disclosure)
Source extract: extract_reg30aoa_526717_q1fy27.txt (1 page, 54 body lines / 68 extract lines incl. header)
Ledger: ledger_reg30aoa_526717_q1fy27.md (23 discrete disclosure units, gate_a2 pass)
Ledger reconciliation: 23/23 disclosure units read verbatim at cited lines = 100%.

## DOCUMENT NATURE (bearing on checklist scope)
Single-subject Regulation 30 event letter. The Board, at its meeting held
12 August 2026, approved adoption of a **new set** of Articles of Association,
subject to Members' approval at the ensuing AGM. No financial tables, numbered
notes, auditor report, consolidation list, tax/OCI/segment data, or annexures
exist (A2 confirms all such categories at 0/0, not merely unlisted). Consequently
the financial-statement checks (F1-F5, F8-F12, F15) are N.A. by content, and the
presentation/concall checks (F16, F17) are N.A. by doctype. The letter is a
governance / forward-commitment artifact, so F6, F7, F13, F14 carry the analysis.

Live-monitoring context (inline, not self-fetched; Decision Status AVOID;
FLAG-GOVERNANCE, FLAG-DISCLOSURE): CS resigned Jan-2026; internal auditor
withdrew 17-Jul-2026; CFO resigned 12-Aug-2026 (same-day, separate filing);
this full-AoA-replacement letter also filed 12-Aug-2026.

---

## FINDINGS TABLE
| id | check | ledger row ref | line | verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| F6-01 | F6 | Table 3 row 8 / Table 4 row 10 (AGM_APPROVAL_PENDING) | 44-46 | "has approved the adoption of a new set of Articles of Association of the Company, subject to the approval of the Members of the Company at the ensuing Annual General Meeting" | FORWARD-SIGNAL | A dateable management commitment: a special resolution to replace the entire AoA is bound for the ensuing (FY27) AGM. Schedule the AGM notice/record-date as a Role 6 event; the AGM notice will carry the explanatory statement and the actual new-AoA text that this letter withholds. |
| F13-01 | F13 | Table 4 row 10 (AGM_APPROVAL_PENDING) + rationale row 9 | 45-46, 48-50 | "approved the adoption of a new set of Articles of Association ... subject to the approval of the Members ... at the ensuing Annual General Meeting" / "to align the Articles ... with the applicable provisions of the Companies Act, 2013" | AMBIGUOUS | A **full replacement** (not a targeted amendment) of the constitutional document, filed the same calendar day as the CFO resignation (12-Aug-2026) and inside a 7-month governance-exit sequence (CS Jan-2026, internal auditor 17-Jul-2026, CFO 12-Aug-2026). The stated WHY is generic ("align with Companies Act 2013"). Lean bear: a wholesale AoA rewrite can quietly alter board-composition, related-party, borrowing, or share-transfer provisions. A4 question required — see below. |
| F14-01 | F14 | Table 4 row 10 (MEETING_TIMES_NOT_FOUND); no annexure row (annexures 0/0) | 45, 48-50; annexures absent | "the adoption of a new set of Articles of Association" (referenced, not reproduced); rationale limited to "align ... with the applicable provisions of the Companies Act, 2013, the rules made thereunder and other applicable regulatory requirements" | CONFIRMATORY-NEGATIVE | Disclosure-completeness deficit: (a) the new AoA text is **merely referenced, not attached** — no annexure exists; (b) the letter names **no specific article** being changed and gives no WHAT, only a boilerplate WHY; (c) board-meeting start/end times are not disclosed (MEETING_TIMES_NOT_FOUND, rule 3), so signature-timestamp-vs-meeting-conclusion cannot be verified. Consistent with the standing FLAG-DISCLOSURE and the AVOID posture; a materially thin disclosure on a constitutional-document rewrite. |

---

## CHECKLIST SCORECARD (all 17; one status each)
| Check | Status | Basis (one line) |
|---|---|---|
| F1 Zero-value standing line items | N.A. | No financial table; A2 line_items 0/0 and zero ZERO_STANDING rows. |
| F2 Standalone vs consolidated | N.A. | No standalone/consolidated financials in the document. |
| F3 Shell-entity detection | N.A. | No cost lines and no entity/consolidation list to compare. |
| F4 Unaudited contribution ratio | N.A. | No auditor report / Other Matters paragraph (auditor_paras 0/0). |
| F5 Going concern / EoM tracking | N.A. | No auditor report, no EoM/going-concern paragraph to diff. |
| F6 Forward-commitment phrase mining | FINDING | Lexicon hits "board has approved" / "subject to approval" / "proposes to (proposed adoption)" at lines 44-48; AoA-to-AGM commitment -> F6-01. |
| F7 Hedge phrase mining | PASS | Sole "subject to" (line 45) is a procedural AGM-approval condition precedent, not a pre-emptive business-risk hedge; no revenue/concentration hedge language present. |
| F8 Tax forensics | N.A. | No ETR, deferred-tax, or prior-year tax-adjustment figures. |
| F9 OCI forensics | N.A. | No OCI / actuarial data. |
| F10 Share count and dilution | N.A. | No paid-up capital or EPS figures; new AoA text not attached, so no rights change is assessable here. |
| F11 Reserves / net worth tie-out | N.A. | No Other Equity / paid-up capital figures. |
| F12 Segment forensics | N.A. | No segment tables. |
| F13 Board outcome beyond results | FINDING | Special-resolution (full AoA replacement) bound for ensuing AGM plus governance-timing overlay -> F13-01. |
| F14 Note drafting inconsistencies | FINDING | New AoA text not annexed, WHAT not itemized, board-meeting times not disclosed -> F14-01. (Name variants at lines 67 are OCR_GARBLED per A2, not source drafting defects.) |
| F15 Entity list diffs | N.A. | No consolidation/entity list in the document (entities 0/0). |
| F16 Presentation dropped/reframed | N.A. | Not a presentation deck. |
| F17 Concall silence audit | N.A. | Not a concall/transcript; no turns to audit. |

---

## COMMITMENT REGISTER (from F6)
| commitment | implied date | note/turn ref | status word |
|---|---|---|---|
| Adopt a new set of Articles of Association (full replacement), subject to Members' approval | Ensuing (FY27) AGM — date not yet disclosed | Lines 44-46 (Ledger Table 3 row 8 / Table 4 row 10) | initiated (board-approved 12-Aug-2026; AGM approval pending) |

---

## FORWARDED TO A4 (questions to raise)
1. (F13-01, AMBIGUOUS) What specific Articles are being changed by the full
   AoA replacement, and why a wholesale replacement rather than targeted
   amendment? Do any changed provisions touch board composition/quorum,
   borrowing powers, related-party approvals, or share-transfer/pre-emption
   rights? (A4 to obtain the AGM notice explanatory statement + new AoA text.)
2. (F13-01) Why is a constitutional-document rewrite being adopted on the same
   day as the CFO resignation and amid the CS / internal-auditor / CFO exit
   sequence — coincidence of AGM-cycle timing, or connected?
3. (F14-01, CONFIRMATORY-NEGATIVE feeding disclosure-quality tracker) Absent
   annexure and absent board-meeting times: confirm the actual new AoA is
   released with the AGM notice and that meeting timings are recorded.
