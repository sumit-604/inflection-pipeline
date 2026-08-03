# A3 FORENSIC NOTES — Unimech Aerospace and Manufacturing Limited (UNIMECH)
Quarter: Q1 FY27 | Doctype: results (Reg 30 QIP fund-raising intimation, 2 pages)
Source: pr_qip_unimech_q1fy27.pdf | A1 extract: runs/unimech-q1fy27/work/extract_pr-qip_unimech_q1fy27.txt
A2 ledger: runs/unimech-q1fy27/work/ledger_pr-qip_unimech_q1fy27.md
Unit convention: Crores (x1) | Monitoring checklist: NONE (fresh company, no prior thesis)
Ledger reconciliation: 29/29 disclosure units read at cited lines = 100%

## DOCTYPE POSTURE
This is a Reg 30 / Schedule III intimation of a single Board-approved matter: an
enabling resolution to raise up to Rs 750 Cr via QIP, subject to AGM approval.
There is NO financial-statement table, NO auditor report, NO consolidation list,
NO segment/tax/OCI/EPS/net-worth data, NO concall, NO presentation. Consequently
the balance-sheet, statement, auditor and consolidation checks (F1-F5, F8, F9,
F11, F12, F15) and the presentation/concall checks (F16, F17) are mechanically
N.A. The live forensic lens is forward-commitment (F6), hedge latitude (F7),
dilution signalling (F10), Board-outcome forward items (F13), and drafting/
disclosure completeness (F14). The A2 flags CONDITIONAL_ON_SHAREHOLDER_APPROVAL,
SCHEDULE_III_INCOMPLETE and MISSING_MEETING_TIMES are all carried into the
findings below.

---

## FINDINGS TABLE

| id | check | ledger row ref | line | verbatim quote | classification | forward implication |
|----|-------|----------------|------|----------------|----------------|---------------------|
| FND-01 | F6 | Cat.3 rows 1-6, Cat.4 S.No.1-3 | 39-46 | "the Board has approved to raise further capital ... for an aggregate consideration not exceeding 750,00,00,000 (Rupees Seven Hundred and Fifty Crore Only) ... in one or more tranches" | FORWARD-SIGNAL | Dated management commitment to raise up to Rs 750 Cr. This QIP sits ON TOP of still-being-deployed IPO proceeds (A4 context) — a second capital ask before the first is fully absorbed. Feeds Role 5 promise-vs-delivery tracker and FTTCP catalyst timeline. No completion date disclosed; commitment is dateable only to "ensuing AGM". |
| FND-02 | F7 | Cat.3 rows 3-4, 6; Cat.4 S.No.1-2 | 42, 44, 89-90 | "convertible securities or any combination of the Securities thereof" ... "in one or more tranches" ... "as may be considered appropriate under the applicable laws" | AMBIGUOUS | Maximum-latitude drafting: instrument (equity vs convertible), tranche count, and structure all left open. "Not exceeding" caps size but nothing else. Standard for an enabling resolution, but the equity/convertible optionality means the dilution mechanism is undetermined. A4 question: pure-equity QIP or convertible structure? |
| FND-03 | F10 | Cat.5 row 1 (SCHEDULE_III_INCOMPLETE) | 96; 79, 92 | "[end of document - Annexure-I table ends at S.No. 3 as extracted; no further rows present in source PDF]" | AMBIGUOUS | Dilution magnitude is UNQUANTIFIABLE from this filing: Annexure-I discloses only type/mode/size and omits floor-price/pricing formula, discount, relevant date, current promoter shareholding, indicative share count, and use of proceeds. A1 confirms this is not an extraction gap. Only face value (Rs 5) is given. At Rs 750 Cr the dilution % turns entirely on the undisclosed price. A4 questions: floor price basis, expected discount, promoter/promoter-group participation, use of proceeds vs. residual IPO proceeds. |
| FND-04 | F13 | Cat.3 row 1 (CONDITIONAL_ON_SHAREHOLDER_APPROVAL) | 39 | "Subject to the approval of the Shareholders at the ensuing Annual General Meeting of the Company" | FORWARD-SIGNAL | Capital-raising enabling resolution foreshadows a funding round. Two forward catalyst events implied: (1) the ENSUING AGM will carry a QIP special resolution (AGM notice + record date incoming; no AGM date disclosed) and (2) subsequent QIP launch/pricing in one or more tranches. Schedule both. Reg 30 lineage noted: this follows a prior intimation dated July 29, 2026 (line 30). |
| FND-05 | F14 | Cat.1 row 6 (MISSING_MEETING_TIMES); Cat.6 row 2 | 33, 62-63, 45, 68 | "meeting held today, i.e., August 03, 2026" (no start/end time); CS digital-sign "Date: 2026.08.03 18:18:45"; stray "law by way of a qualified institutions placement" | NEUTRAL-FACT | Governance data point, individually immaterial: no board-meeting start/end time disclosed, so the standard "signature-before-meeting-concluded" timing check cannot be performed (signature 18:18:45 unverifiable against meeting close). One dangling drafting word ("law", line 45) and ligature-drop OCR artifacts ("Quali ied", "Of icer") noted but not substantive. Body resolution (lines 40-46) and Annexure S.No.1-3 reconcile cleanly — no substantive inconsistency. |

Note: extraction-side artifacts ("Quali ied", "Of icer", "Of icer") are ligature
drops from the PDF text layer, not source drafting errors, and are excluded from
the F14 substantive-inconsistency judgement.

---

## CHECKLIST SCORECARD (all 17, exactly one status each)

| # | Check | Status | Basis |
|---|-------|--------|-------|
| F1 | Zero-value standing line items | N.A. | No financial-statement table; A2 zero_standing count = 0 (Cat. "Zero-Standing" note). Single-event intimation. |
| F2 | Standalone vs consolidated decomposition | N.A. | No standalone or consolidated figures in the document. |
| F3 | Shell-entity detection | N.A. | No cost lines, no entity/consolidation list. |
| F4 | Unaudited contribution ratio | N.A. | No auditor report / Other Matters paragraph. |
| F5 | Going concern / EoM scope tracking | N.A. | No auditor report / EoM; fresh company, no prior quarter to diff. |
| F6 | Forward-commitment phrase mining | FINDING | FND-01: "board has approved", "proposed to be issued", "not exceeding ... in one or more tranches" — dated commitment to raise Rs 750 Cr. |
| F7 | Hedge phrase mining | FINDING | FND-02: "subject to", "and/or ... any combination", "as may be considered appropriate" — pre-emptive latitude on instrument, tranche and structure. |
| F8 | Tax forensics | N.A. | No tax charge, ETR or deferred-tax data. |
| F9 | OCI forensics | N.A. | No OCI / actuarial data. |
| F10 | Share count and dilution | FINDING | FND-03: forward dilution event; magnitude unquantifiable — no pricing/floor-price/discount/share-count disclosed (SCHEDULE_III_INCOMPLETE). |
| F11 | Reserves and net worth tie-out | N.A. | No equity / reserves table; no third-party net-worth figure. |
| F12 | Segment forensics | N.A. | No segment disclosure. |
| F13 | Board outcome beyond the results | FINDING | FND-04: capital-raising enabling resolution → ensuing AGM special resolution + QIP launch; catalyst events to schedule. |
| F14 | Note drafting inconsistencies | FINDING | FND-05: MISSING_MEETING_TIMES blocks signature-timing check; stray "law"; NEUTRAL-FACT, body/Annexure otherwise reconcile. |
| F15 | Entity list diffs | N.A. | No consolidation entity list; fresh company, no prior quarter. |
| F16 | Presentation dropped/reframed disclosures | N.A. | Not a presentation (per doctype rule, F16 N.A. on a results filing). |
| F17 | Concall silence audit | N.A. | Not a concall; monitoring checklist NONE (fresh company). |

Statuses: N.A. x11 (F1-F5, F8, F9, F11, F12, F15, F16, F17) | FINDING x4 (F6, F7, F10, F13, F14 → actually 5) — see YAML for authoritative map. No PASS, no blanks. GATE A3 satisfied.

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/turn ref | status word |
|------------|--------------|---------------|-------------|
| Raise up to Rs 750 Cr via QIP of equity shares and/or convertible securities, in one or more tranches | Subject to "ensuing AGM" approval (no AGM date disclosed); launch/pricing thereafter | lines 39-46; Annexure-I S.No.1-3 (lines 79-95) | board-approved (enabling / initiated) |
| Convene ensuing AGM carrying the QIP special resolution (AGM notice + record date to follow) | Not dated in filing | line 39 | intends-to (foreshadowed) |
| Prior Reg 30 intimation of the same fund-raising matter | Dated July 29, 2026 (already occurred) | line 30 | completed (precedent event) |

---

## HANDOFF TO A4 (questions to convert)
1. (FND-03) Floor-price basis, expected discount, and current promoter/promoter-group shareholding — dilution % is undeterminable without them.
2. (FND-03) Use of proceeds: what does Rs 750 Cr fund, and how does it relate to the still-being-deployed IPO proceeds? Sequencing/absorption question.
3. (FND-02) Instrument mix — pure equity QIP or convertible structure, and why the open-ended optionality?
4. (FND-04) Ensuing AGM date / record date and expected QIP launch window — for the catalyst timeline.
5. (FND-01) Why a second capital ask before the first (IPO) is fully deployed — capital-allocation cadence.
