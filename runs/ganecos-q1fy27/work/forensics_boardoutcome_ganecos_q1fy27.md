# A3 FORENSIC NOTES — GANECOS (Ganesha Ecosphere Limited) — Q1 FY27 — doctype: results (SEBI Reg 30 Board Outcome / governance disclosure)

Source extract: `extract_boardoutcome_ganecos_q1fy27.txt` (75 lines, 2 pages, 100% coverage)
Ledger reconciled: `ledger_boardoutcome_ganecos_q1fy27.md` — 8 tables, all rows read at cited lines (100%)
Doctype note: This is a same-day (3 Aug 2026) single-agenda Board Outcome letter approving the re-appointment of a Senior Management Person. It carries NO financial statements, NO auditor's report, NO consolidation list, NO segment or capital tables. Content-driven checks (F1-F5, F8-F12) are therefore N.A. by content, each stated with a one-line reason per instruction. F16/F17 are N.A. by doctype (not a deck, not a transcript).

---

## LEDGER RECONCILIATION

| Ledger table | Rows | Lines read | Status |
|---|---|---|---|
| T1 Agenda item(s) | 1 | 19-23, 37-39 | read |
| T2 Meeting metadata | 3 | 21, 43 | read |
| T3 Annexure particulars | 4 | 53-75 | read |
| T4 Related-party facts | 2 | 62-65, 71-75 | read |
| T5 Regulatory references | 2 | 15-19, 26-28, 48-50 | read |
| T6 Signatory block | 4 | 33-42 | read |
| T7 Boilerplate | 4 | 13-14, 44-46 | read |
| T8 Explicit-absence record | 7 | n/a (absence) | read |

Reconciliation: 100%. A2 flags carried in: RELATED_PARTY (x2), CONTRADICTION (x1), DATA_QUALITY (x4), ENTITY (x1). Every flag is dispositioned in a finding or scorecard basis below.

---

## FINDINGS TABLE

| id | check | ledger row ref | line | verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-F6-01 | F6 | T1 / T3 row 2 | 21-23, 55-56 | "the Board of Directors ... has approved the re-appointment of Mr. Sandeep Khandelwal as Senior Vice President ... with effect from October 202G, for a period of 5 (Five) years" | FORWARD-SIGNAL | Dated/dateable board commitment: a promoter-family Senior Management Person is locked into plant administration and operations through ~Oct 2031. Term-end date is a governance catalyst to map against the monitoring window; a mid-term non-renewal would be the louder signal. |
| A3-F13-01 | F13 | T3 row 3+4 / T4 row 1 | 22-23, 71-75 | "Shri Sandeep Khandelwal is son of Shri Vishnu Dutt Khandelwal, Executive Vice-Chairman of the Company" | FORWARD-SIGNAL | Board Outcome beyond results: promoter-family (Khandelwal) KMP entrenchment. Re-appointment was on NRC + Audit Committee recommendation (T1) — a procedural positive — but the appointee is a promoter son in an executive operations role. Feeds the still-open promoter/governance verdict on the WATCHLIST thesis. |
| A3-F13-02 | F13 | T3 row 3 / T4 row 2 | 62-65 | "He is holding the position of Managing Director in M/s. Ganesha Ecoverse Limited, a Group Company listed at BSE-SME" | AMBIGUOUS | ENTITY interlock: the same individual is SVP (operations) at GANECOS and MD of a separately listed BSE-SME group company. Related-party-transaction and time-allocation/conflict questions arise (inter-company sales of textile yarns/fibre, resource sharing). Direction unresolved -> A4 management question. Lean bear pending RPT disclosure. |
| A3-F14-01 | F14 | T3 row 4 / T4 row 1 | 71-75 | "Disclosure of relationship between the Directors ... N.A. (Shri Sandeep Khandelwal is son of Shri Vishnu Dutt Khandelwal, Executive Vice-Chairman of the Company)" | AMBIGUOUS | Drafting/disclosure-adequacy contradiction: the particular is answered "N.A." while the same cell parenthetically discloses a father-son relationship that plainly exists. Either the "N.A." is a template-fill error or reflects a view that the SVP is not a "Director" (arguably true — he is Senior Management Personnel, not a board director), leaving the particular technically mis-answered. Cited, not resolved -> A4 question on disclosure control. Lean bear. |
| A3-F14-02 | F14 | T2 / T3 row 2 | 22-23, 55-56 | letter: "with effect from October 202G" (no day, year garbled); annexure: "Re-appointed with effect from oisrOctober,2026" | AMBIGUOUS | Internal effective-date inconsistency between cover letter and annexure. The letter body (line 22-23) states the effective month "October" with NO day and an OCR-garbled year "202G"; the annexure (line 55) renders the day as "oisr" (plausibly "01st") October 2026. The two renderings are not consistent on their face; the exact commencement day is not cleanly determinable from either. Stated as a discrepancy, unresolved beyond text -> A4 question / confirm against source PDF. |
| A3-F14-03 | F14 | T2 / T3 rows 1-3 | 43, 53, 57-58 | "l:Q .0. P.M." (meeting conclusion); row numeral "I" for "1"; "aged about ___ years" with "50" displaced to line 57 | NEUTRAL-FACT | Cluster of OCR/extraction data-quality artifacts (illegible meeting-close time; roman-vs-arabic row marker; age numeral displaced by column wrap). Individually immaterial and attributable to extraction rather than source drafting; logged for completeness so the A2 DATA_QUALITY flags are fully dispositioned. No forward signal on their own. |

---

## CHECKLIST SCORECARD (all 17)

| Check | Status | Basis (one line) |
|---|---|---|
| F1 Zero-value standing line items | N.A. | No financial table exists in this Reg 30 letter; ledger zero_standing count = 0, no standing item could be nil. |
| F2 Standalone vs consolidated decomposition | N.A. | No standalone or consolidated financials present; no Revenue/EBITDA/PAT to decompose. |
| F3 Shell-entity detection | N.A. | No cost lines (materials/employee/depreciation) and no entity financials to compare. |
| F4 Unaudited contribution ratio | N.A. | No auditor's report / Other Matters paragraph attached; ledger auditor_paras = 0. |
| F5 Going concern / EoM scope tracking | N.A. | No auditor's report or EoM paragraph in this doctype; nothing to verbatim-diff. |
| F6 Forward-commitment phrase mining | FINDING | "has approved the re-appointment ... with effect from October 202G, for a period of 5 (Five) years" (L21-23, 55-56) — dated board commitment. See A3-F6-01. |
| F7 Hedge phrase mining | PASS | Full lexicon scanned (may/could/no assurance/subject to/evaluating/exploring/in discussions/endeavour). The only "subject to" adjacency is regulatory citation boilerplate; no substantive hedge on operations or lumpiness present. |
| F8 Tax forensics | N.A. | No P&L, no tax lines, no ETR computable. |
| F9 OCI forensics | N.A. | No OCI / actuarial disclosure in a governance letter. |
| F10 Share count and dilution | N.A. | No paid-up capital or EPS figures present. |
| F11 Reserves and net worth tie-out | N.A. | No Other Equity / paid-up figures to reconcile. |
| F12 Segment forensics | N.A. | No segment assets/liabilities/revenue table present. |
| F13 Board outcome beyond the results | FINDING | Director/KMP term-date and promoter-family + group-company interlock signals. See A3-F13-01, A3-F13-02. |
| F14 Note drafting inconsistencies | FINDING | Relationship cell "N.A." contradicts disclosed father-son link; effective-date inconsistency letter vs annexure; OCR artifact cluster. See A3-F14-01/02/03. |
| F15 Entity list diffs | N.A. | No consolidation entity list in this doctype (ledger consolidation-list = 0). The one entity named (Ganesha Ecoverse Ltd) is a related-party interlock, dispositioned under F13-02, not a consolidation-scope diff. |
| F16 Presentation-specific (dropped/reframed disclosures) | N.A. | Not an investor presentation; no slides. |
| F17 Concall-specific (silence audit) | N.A. | Not a transcript; no turns/questions (ledger turns = 0). |

Gate A3: PASS — all 17 checks carry exactly one status; no blanks.

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/turn ref | status word |
|---|---|---|---|
| Re-appointment of Mr. Sandeep Khandelwal as Senior Vice President (plant administration & operations), 5-year term (runs to ~Oct 2031) | effective October 2026 — day unresolved ("oisr"/possibly 01st Oct 2026; letter body gives month+garbled year only, no day) | L21-23 (letter), L55-56 (annexure row 2) | board has approved |

Note for A4: the commitment's own start date is the subject of finding A3-F14-02 (internal inconsistency). Carry the commitment as approved but flag the unresolved effective day when the source PDF is available.

---

## FORWARD-LOOKING SUMMARY FOR A4

1. Promoter-family entrenchment through a 5-year window (A3-F6-01, A3-F13-01) — governance monitoring input, no promoter verdict yet on the WATCHLIST thesis.
2. Group-company interlock — same person is MD of listed peer Ganesha Ecoverse Ltd (A3-F13-02) — convert to an RPT / conflict-of-interest management question.
3. Disclosure-control softness — "N.A." relationship answer (A3-F14-01) and inconsistent effective dates (A3-F14-02) — convert to a disclosure-quality question; individually immaterial, cumulatively a governance data point.
