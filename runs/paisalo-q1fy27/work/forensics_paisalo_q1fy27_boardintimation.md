# A3 FORENSIC NOTES — Paisalo Digital Ltd | Q1 FY27 | doctype: results (Board Outcome intimation subtype, SEBI Reg 30 — NOT the Reg 33 results statement)

Source extract: `runs/paisalo-q1fy27/work/extract_results_paisalo_q1fy27_boardintimation.txt` (122 lines, 2 pages)
Ledger: `runs/paisalo-q1fy27/work/ledger_results_paisalo_q1fy27_boardintimation.md` (22 rows)
Ledger reconciliation: 22/22 rows read at their cited line numbers = 100%.

## DOCTYPE PREAMBLE
This is a Regulation 30 Board Outcome / governance intimation. It carries no P&L,
no balance sheet, no auditor report, no notes, no segment table, no consolidation
list, and no financial figures of any kind (A1 header `unit_convention: N/A`; A2
confirms `line_items / notes / auditor_paras / entities` all N/A). Consequently the
financial-statement forensics checks (F1-F5, F8-F12, F15) have no substrate in this
document and are marked N.A. with reason. The monitoring checklist asks that F4/F5/F12
be run "in full" for this NBFC; there is simply no auditor Other-Matters paragraph,
no going-concern/EoM paragraph, and no segment table in a Board intimation to run them
against — where a check depends on Reg-33 statement content absent here, it is marked
N.A. with the reason, per the task instruction. The document's forensic weight sits
entirely in F6 (dated commitments), F13 (board outcome beyond results / director term
dates / succession) and F14 (drafting hygiene).

## FINDINGS TABLE

| id | check | ledger row ref | line | verbatim quote | classification | forward implication |
|----|-------|----------------|------|----------------|----------------|---------------------|
| F6-a | F6 | §1 items 1-3; §2 2a/3b; §5 rows 1-2 | 39-40, 44-46, 53-54, 87-88 | "to be held on September 21, 2026" (39-40); "final Dividend payment for FY 2025-26, subject to approval" (45-46); "for a further term commencing from May 06, 2027, till May 05, 2032" (54); "the Board has approved the re-appointment" (87-88) | FORWARD-SIGNAL | Four dateable governance/cash milestones set: AGM 21-Sep-2026, book closure 15-21 Sep 2026, FY25-26 final dividend payable post-AGM, and DMD term running to May-2032. Feed the FTTCP catalyst timeline and the Role 5 promise-vs-delivery tracker. |
| F13-a | F13 | §1 items 1-2; §2 2a | 38-46 | "Fixed the date of the 34th Annual General Meeting (AGM) of the Company to be held on September 21, 2026" (39-40) | FORWARD-SIGNAL | AGM notice + book-closure record-date = special resolutions (director re-appointment) and FY25-26 final dividend incoming within ~7 weeks. Schedule Role 6 AR Deep Dive: the full Annual Report typically drops with/ahead of the AGM notice. Note: this intimation contains NO AR/Board's-Report/results-approval agenda item (Reg 30, not Reg 33) — the financial-results board meeting is a separate event still pending. |
| F13-b | F13 | §2 row 3b; §5 rows 2 & 4 | 53-54, 96-97, 104-105 | "as Whole Time Director designated as Deputy Managing Director for a further term" (53-54); "son of Mr. Sunil Purushottanm Agarwal, Managing Director of the Company" (104-105) | AMBIGUOUS | Executive DMD re-appointment is a promoter-family succession (son of the MD) locked in through 05-May-2032, with the term forward-dated to commence 06-May-2027 (~9 months after this board meeting, ~8 months after the AGM). Direction uncertain: continuity/governance-positive vs family-entrenchment/RPT-remuneration question. Flag to A4 for a management question — (i) why the new term is forward-dated to May-2027 rather than continuous, and (ii) NRC process / remuneration terms for a related-party executive re-appointment. |
| F14-a | F14 | §5 row 4 | 104 | "son of Mr. Sunil Purushottanm Agarwal, Managing Director" | NEUTRAL-FACT | The MD's name is misspelt "Purushottanm" (stray 'n') inside a related-party disclosure row; A2 renders it correctly as "Purushottam". Individually immaterial drafting error; logged as a cumulative governance-hygiene data point, no thesis impact. |

## CHECKLIST SCORECARD (all 17)

| Check | Status | Basis (one line) |
|-------|--------|------------------|
| F1 ZERO-VALUE STANDING ITEMS | N.A. | No financial table / line items in a Reg-30 Board intimation (A2 `line_items` N/A). |
| F2 STANDALONE vs CONSOLIDATED | N.A. | No standalone/consolidated statements present. |
| F3 SHELL-ENTITY DETECTION | N.A. | No cost lines, no consolidation to compare. |
| F4 UNAUDITED CONTRIBUTION RATIO | N.A. | No auditor Other-Matters paragraph exists in this document (checklist asks F4 in full; no Reg-33 substrate present). |
| F5 GOING CONCERN / EoM | N.A. | No auditor report / EoM paragraph; no prior-quarter extract supplied for verbatim-diff. |
| F6 FORWARD-COMMITMENT MINING | FINDING | Lexicon hits: "commenc" (54), "board has approved" (87-88), "proposes" (88), "subject to approval" (45-46, 95); dated AGM/dividend/DMD-term commitments — see F6-a and Commitment Register. |
| F7 HEDGE PHRASE MINING | PASS | Only hedge-lexicon hit is procedural "subject to approval of the Shareholders" (45-46, 95-97) — a shareholder-approval condition, not a business-risk hedge on revenue lumpiness or concentration; no pre-emptive legal cover added. |
| F8 TAX FORENSICS | N.A. | No tax line / ETR in document. |
| F9 OCI FORENSICS | N.A. | No OCI / actuarial figures. |
| F10 SHARE COUNT & DILUTION | N.A. | No paid-up capital / EPS. (NCD ×15 and CP ×5 series codes listed at 24-26 are debt identifiers, not equity dilution.) |
| F11 RESERVES / NET WORTH | N.A. | No equity or reserves figures. |
| F12 SEGMENT FORENSICS | N.A. | No segment assets/liabilities table (checklist asks F12 in full for NBFC; no segment substrate in a Board intimation). |
| F13 BOARD OUTCOME BEYOND RESULTS | FINDING | AGM 21-Sep-2026 + book closure + FY25-26 dividend + forward-dated DMD term to 2032 + promoter-family succession; no AR/results-approval item present — see F13-a, F13-b. |
| F14 NOTE-DRAFTING INCONSISTENCIES | FINDING | MD's name misspelt "Purushottanm" in RPT row (104); Annexure signature block (119-123) omits the "Company Secretary" designation restated on p.1 — minor, cumulative hygiene — see F14-a. |
| F15 ENTITY LIST DIFFS | N.A. | No consolidation entity list; no prior-quarter list to diff. |
| F16 PRESENTATION DROPPED/REFRAMED | N.A. | Not a presentation/deck. |
| F17 CONCALL SILENCE AUDIT | N.A. | Not a concall transcript. Signature-timestamp-vs-meeting-conclusion check (task's "F17 area") performed separately: sign-offs 12:28:27 and 12:28:37 IST vs meeting conclusion 12:25 P.M. (line 60) — 3 min after, correct sequencing, NO backdating. Monitoring-checklist items (pledge/GNPA/co-lending fees/rating/SAST-Reg31 overhang) are absent here as expected for a governance intimation — not a confirmatory-negative silence in this doctype. |

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/line ref | status word |
|------------|--------------|---------------|-------------|
| 34th AGM to be held | 21-Sep-2026 | item 1, lines 39-40 | fixed / scheduled |
| Book Closure window | 15-Sep to 21-Sep-2026 (inclusive) | item 2, lines 44-45 | fixed |
| FY 2025-26 final dividend payment | on/after AGM (post 21-Sep-2026) | 2a, lines 45-46 | proposed, subject to shareholder approval |
| Santanu Agarwal re-appointed as retire-by-rotation Director | effective AGM 21-Sep-2026 | 3a / row 2, lines 51-52, 94-95 | board-recommended, subject to shareholder approval |
| Santanu Agarwal WTD/Deputy Managing Director further term | commences 06-May-2027, runs to 05-May-2032 | 3b / row 2, lines 53-54, 96-97 | board-approved (NRC-recommended), subject to shareholder approval |

## LEDGER RECONCILIATION LOG
All 22 A2 rows read verbatim at cited lines: §1 agenda items (38-40, 43-46, 48-54);
§2 sub-disclosures 2a/3a/3b (44-46, 51-52, 53-54); §3 meeting times (60 ×2); §4
signatures (63-68, 119-123); §5 Annexure rows 1-5 (82-91, 94-97, 99-103, 104-107,
108-118); §6 recipients (17-21, 17-20, 72, 72); §7 identifiers (23, 24-25, 26).
No row unread; no row disputed on line placement. Reconciled 100%.

```yaml
stage: A3-forensics
company: "paisalo"
quarter: "q1fy27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "runs/paisalo-q1fy27/work/forensics_paisalo_q1fy27_boardintimation.md"
ledger_reconciled_pct: 100
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
  - {id: "F6-a", check: "F6", line: "39-40,44-46,53-54,87-88", classification: "FORWARD-SIGNAL", implication: "Four dated governance/cash milestones: AGM 21-Sep-2026, book closure 15-21 Sep 2026, FY25-26 final dividend post-AGM, DMD term to May-2032; feed FTTCP catalyst timeline."}
  - {id: "F13-a", check: "F13", line: "38-46", classification: "FORWARD-SIGNAL", implication: "AGM + record date = dividend/special resolutions incoming ~7 weeks; schedule Role 6 AR Deep Dive; NO AR/results-approval item in this Reg-30 intimation, results board meeting still pending."}
  - {id: "F13-b", check: "F13", line: "53-54,96-97,104-105", classification: "AMBIGUOUS", implication: "Promoter-family succession: MD's son re-appointed DMD through 2032, term forward-dated to commence May-2027; A4 to ask why forward-dated and NRC/remuneration terms for a related-party executive."}
  - {id: "F14-a", check: "F14", line: "104", classification: "NEUTRAL-FACT", implication: "MD's name misspelt 'Purushottanm' in RPT row; immaterial drafting hygiene data point."}
forward_signals: ["F6-a", "F13-a"]
ambiguous: ["F13-b"]
commitments:
  - {commitment: "34th AGM held", implied_date: "2026-09-21", ref: "line 39-40 (item 1)", status_word: "fixed"}
  - {commitment: "Book closure window", implied_date: "2026-09-15..2026-09-21", ref: "line 44-45 (item 2)", status_word: "fixed"}
  - {commitment: "FY25-26 final dividend payment", implied_date: "post 2026-09-21", ref: "line 45-46 (2a)", status_word: "proposed-subject-to-approval"}
  - {commitment: "Santanu Agarwal re-appointed rotational Director", implied_date: "2026-09-21", ref: "line 51-52,94-95 (3a)", status_word: "board-recommended"}
  - {commitment: "Santanu Agarwal WTD/Deputy MD further term", implied_date: "2027-05-06..2032-05-05", ref: "line 53-54,96-97 (3b)", status_word: "board-approved-subject-to-approval"}
gate_a3: pass
blank_checks: []
```
