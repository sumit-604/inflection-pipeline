# A3 FORENSIC NOTES: INDORAMA, Q2 FY27, doctype results (file tag "capex": Reg 30 Board Outcome, capex approval, 16-Oct-2026)

Inputs read: A1 structured `runs/indorama-q2fy27/extracted/indorama-capex-q2fy27-structured.md` (R001-R047), A1 fulltext `runs/indorama-q2fy27/extracted/indorama-capex-q2fy27-fulltext.md` (62 lines, 1 page), A2 ledger `runs/indorama-q2fy27/work/ledger_capex_indorama_q2fy27.md`. Prior-quarter fulltext: ND. Notion checklist: NONE (no page, no spear on record). Source PDF and `inputs/` not opened.

Document scope: a one-page Regulation 30 letter. It carries one agenda item (capex approval). It carries no financial statements, no notes, no auditor report, no segment data, no entity list. Most balance-sheet checks (F1-F5, F8-F12, F15) therefore have nothing to test and are marked N.A. with that basis.

## LEDGER RECONCILIATION (47 of 47 rows read at cited line = 100%)

| Ledger group | Row IDs | Read at fulltext line | Result |
|---|---|---|---|
| A01 capex approval | R011, R022, R023, R027, R030, R031, R042, R044 | 37-41 | Verbatim match. R022 full name "Indo Rama Synthetics (India) Limited" is not on line 39; line 39 reads "in the Company"; the full name sits at lines 51 and 59. Meaning unchanged. R027 "Board of / Directors" spans lines 37-38. |
| A01a timeline | R012, R032, R040, R043 | 42-43 | Verbatim match. "12-18" on line 42, "months" on line 43. |
| A01b financing | R033, R034, R046 | 43-44 | Verbatim match. "internal accrual" closes on line 44. |
| Entities | R018-R029 | 21-62 | Match. R018 cites line 21; line 21 is "Corporate Listing Department", the NSE name is on line 22 and "NEAPS" on line 26. R024 "Butibori Plant," line 41, "Nagpur, Maharashtra" line 42. Cite drift only. |
| Signature | R013, R014, R028, R039, R047 | 52-56 | Verbatim match. |
| Reference / addressing | R001-R008, R020, R035 | 18-29 | Verbatim match. |
| Dates / LODR basis | R009, R010, R036, R037, R038, R041, R045 | 19, 36-38, 62 | Verbatim match. |
| Address / CIN | R015, R016, R017, R029 | 60-62 | Verbatim match. |

A2 flags carried and tested: SPLIT_NOT_STATED (confirmed, FN-04), FUNDING_UNQUANTIFIED (confirmed, FN-03), MEETING_TIMES_ABSENT (confirmed, FN-05). No row unread. No orphan ID.

## FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| FN-01 | F6 | A01: R011, R030, R031, R024-R026, R042 | 38-41 | "have considered and approved expansion plan of approx. INR 200 Crores ... towards capex for speciality filament and speciality Fibre production at Butibori Plant" | FORWARD-SIGNAL | A dated board-approved capex commitment of about Rs 200 Cr aimed at speciality (not commodity) filament and fibre at the existing Butibori site. Feeds the Role 5 promise-vs-delivery tracker. A4 asks: capacity added (tpa), product mix, incremental revenue at full use, and whether the spend is brownfield on existing land and utilities. |
| FN-02 | F6 | A01a: R012, R032, R040, R043 | 42-43 | "with an estimated commercial operation date in next 12-18 months" | FORWARD-SIGNAL | Commissioning window 16-Oct-2027 to 16-Apr-2028 (12-18 months from the 16-Oct-2026 meeting, line 38). Earliest revenue contribution falls in Q3 FY28; latest in Q1 FY29. Catalyst-timeline entry. The word "estimated" means the tracker holds a range, not a date. A4 asks for the milestone path (orders for machinery, civil start, trial run). |
| FN-03 | F6 | A01b: R033, R034, R046 | 43-44 | "The projects would be financed by taking term loan for the same with mix of internal accrual." | AMBIGUOUS | Debt is the named primary source; the debt-to-accrual split is not quantified. Conservative read: up to most of Rs 200 Cr is new term debt, with interest cost running ahead of revenue during the 12-18 month build. A term-loan sanction is a likely follow-on disclosure. A4 asks: loan quantum, lender, tenor, rate, which entity borrows, and whether the term loan is already sanctioned. |
| FN-04 | F13 | A01: R022, R023, R044 | 39-40 | "in the Company and its Wholly Owned Material Subsidiary, i.e., Indorama Ventures Yarns Private Limited (IVYPL)" | AMBIGUOUS | One outlay spans two entities with no split stated. The split decides where the assets, the term loan and the future revenue land, so it decides the standalone-vs-consolidated read in later results (F2/F3 next quarter). IVYPL is named a "Material Subsidiary". A4 asks: Rs split between the Company and IVYPL, which product line sits in which entity, and how IVYPL is funded (equity infusion, inter-corporate loan, or its own term loan). |
| FN-05 | F14 | A01, R037, R014, R039 | 38, 53 | "in their meeting held today, i.e., 16th October 2026" / "Date: 2026.10.16 14:51:58 +05'30'" | AMBIGUOUS | The letter states no meeting start or end time. With only the 14:51:58 signature time, the timeliness of the board-outcome disclosure against meeting close cannot be tested from the document. Individually minor; a governance data point. A4 or Claude web checks meeting times and the exchange dissemination time on NSE/BSE. |
| FN-06 | F14 | R001, R002, R035, R009 | 18, 31, 36 | "IRSL: STEXCH:2026-27:" / "Disclosure under Regulations 30" / "Pursuant to Regulation 30" | NEUTRAL-FACT | Reference number ends in a trailing colon with no serial. Subject line says "Regulations 30", body says "Regulation 30". Immaterial drafting slips; logged for the cumulative governance count only. Not routed to A4. |

## CHECKLIST SCORECARD

| Check | Status | Basis |
|---|---|---|
| F1 Zero-value standing line items | N.A. | No financial table; ledger line_items count 0, no ZERO_STANDING rows. |
| F2 Standalone vs consolidated decomposition | N.A. | No standalone or consolidated figures in the letter. |
| F3 Shell-entity detection | N.A. | No cost lines. IVYPL is described as an operating capex site entity (line 40-41), no cost data to test. |
| F4 Unaudited contribution ratio | N.A. | No auditor report; ledger auditor_paras count 0. |
| F5 Going concern / EoM scope tracking | N.A. | No EoM paragraph; prior-quarter fulltext ND. |
| F6 Forward-commitment phrase mining | FINDING | FN-01, FN-02, FN-03. "approved" (lines 38-39, equivalent of "board has approved"), "estimated commercial operation date" (line 42), "would be financed" (line 43). |
| F7 Hedge phrase mining | PASS | Zero lexicon hits (no "subject to", "no assurance", "evaluating", "exploring", "in discussions", "endeavour", "may sometimes", "could have an effect"). Non-lexicon qualifiers "approx." (line 39), "estimated" (line 42) and "would be" (line 43) are carried on the F6 commitment rows. |
| F8 Tax forensics | N.A. | No P&L or tax lines. |
| F9 OCI forensics | N.A. | No OCI lines. |
| F10 Share count and dilution | N.A. | No paid-up capital or EPS data; no equity-raise item in the board outcome. |
| F11 Reserves and net worth tie-out | N.A. | No balance-sheet data. |
| F12 Segment forensics | N.A. | No segment data. Capex will add segment assets in a later quarter; trend from next results. |
| F13 Board outcome beyond the results | FINDING | FN-04. Single agenda item: capex approval funded by term loan plus accruals. No AR, AGM, record date, director, auditor, ESOP or capital-raising enabling resolution (ledger line 20). |
| F14 Note drafting inconsistencies | FINDING | FN-05 (meeting times absent), FN-06 (reference serial missing; "Regulations"/"Regulation"). |
| F15 Entity list diffs | N.A. | No consolidation list; prior-quarter list ND (ledger line 23). |
| F16 Presentation: dropped and reframed disclosures | N.A. | Not a presentation (doctype results). |
| F17 Concall silence audit | N.A. | Not a concall; no Notion checklist exists (pre-thesis read). |

## COMMITMENT REGISTER (from F6)

| commitment | implied date | ref | status word |
|---|---|---|---|
| Capex of approx. Rs 200 Cr across the Company and IVYPL for speciality filament and speciality fibre at Butibori | approved 16-Oct-2026 | line 38-41 (R011, R030, R031) | approved (not yet initiated) |
| Commercial operation of the speciality filament and fibre capacity | 16-Oct-2027 to 16-Apr-2028 (estimated) | line 42-43 (R012, R032, R040) | approved (not yet initiated) |
| Financing by term loan with a mix of internal accrual, split not stated | not stated (before or during build) | line 43-44 (R033, R034, R046) | proposed ("would be") |

## A4 ROUTING
Forward signals: FN-01, FN-02. Ambiguous (convert to management questions): FN-03, FN-04, FN-05.

```yaml
stage: A3-forensics
company: "INDORAMA"
quarter: "Q2 FY27"
doctype: "results"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/indorama-q2fy27/work/forensics_capex_indorama_q2fy27.md"
ledger_reconciled_pct: 100        # 47 of 47 rows read at cited line
checklist:
  F1: N.A.
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: PASS
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
  - {id: "FN-01", check: "F6", line: "38-41", classification: "FORWARD-SIGNAL", implication: "Board-approved capex approx Rs 200 Cr for speciality filament and speciality fibre at Butibori; tracker entry; ask capacity, mix, revenue at full use, brownfield scope."}
  - {id: "FN-02", check: "F6", line: "42-43", classification: "FORWARD-SIGNAL", implication: "Estimated COD 16-Oct-2027 to 16-Apr-2028; earliest revenue Q3 FY28, latest Q1 FY29; catalyst timeline holds a range; ask milestone path."}
  - {id: "FN-03", check: "F6", line: "43-44", classification: "AMBIGUOUS", implication: "Term loan plus internal accrual, split unquantified; lean bear: most of Rs 200 Cr may be new debt with interest ahead of revenue; ask quantum, lender, tenor, rate, borrowing entity, sanction status."}
  - {id: "FN-04", check: "F13", line: "39-40", classification: "AMBIGUOUS", implication: "Outlay spans Company and IVYPL (wholly owned material subsidiary) with no split; decides where assets, debt and revenue land in standalone vs consolidated; ask split and IVYPL funding route."}
  - {id: "FN-05", check: "F14", line: "38, 53", classification: "AMBIGUOUS", implication: "No meeting start/end time; only signature 14:51:58; disclosure timeliness untestable; verify meeting times and exchange dissemination time."}
  - {id: "FN-06", check: "F14", line: "18, 31, 36", classification: "NEUTRAL-FACT", implication: "Reference number has no serial; 'Regulations 30' vs 'Regulation 30'; immaterial drafting slips, cumulative governance count only."}
forward_signals: ["FN-01", "FN-02"]
ambiguous: ["FN-03", "FN-04", "FN-05"]
commitments:
  - {commitment: "Capex approx Rs 200 Cr, Company plus IVYPL, speciality filament and speciality fibre, Butibori", implied_date: "approved 2026-10-16", ref: "line 38-41 (R011, R030, R031)", status_word: "approved (not yet initiated)"}
  - {commitment: "Commercial operation of new speciality capacity", implied_date: "2027-10-16 to 2028-04-16 (estimated)", ref: "line 42-43 (R012, R032, R040)", status_word: "approved (not yet initiated)"}
  - {commitment: "Financing by term loan with mix of internal accrual, split not stated", implied_date: "not stated", ref: "line 43-44 (R033, R034, R046)", status_word: "proposed"}
gate_a3: pass
blank_checks: []
analyst_note: "One-page Reg 30 letter tagged doctype results; it holds no financials, so F1-F5, F8-F12 and F15 are N.A. on content, not skipped. The forward content is three parameters, each softened: amount 'approx.', date 'estimated', funding 'would be'. The two missing splits matter more than the hedges. Company vs IVYPL decides which books carry the asset, the loan and the revenue, so next quarter's F2/F3 standalone-vs-consolidated read depends on it. Debt vs accrual decides leverage and interest drag during a 12-18 month build with no revenue. Lean bear on funding until the term-loan sanction is disclosed. 'Speciality' product language is a possible mix-shift signal; A3 does not judge it, A4 should ask for capacity and mix. Structured-file cite drift (R018 line 21 vs 22; R022 full name not on line 39) does not change any meaning. No prior-quarter text and no Notion checklist, so no diff or silence audit was possible."
```
