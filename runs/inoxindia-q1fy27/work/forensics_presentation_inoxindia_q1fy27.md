# A3 FORENSIC NOTES — INOX India (INOXINDIA / INOXCVA) — Q1 FY27 — doctype: presentation (Q1 FY27 Result Press Release)

Inputs read verbatim:
- A1 extract: `extract_presentation_inoxindia_q1fy27.txt` (182 lines, 4 pages)
- A2 ledger: `ledger_presentation_inoxindia_q1fy27.md` (64 rows across 11 sections)
- Unit convention: Crores (x1)
- Ledger reconciliation: 64 / 64 rows read at cited lines = 100%

Doctype applicability (per prompt lines 128-131): on a presentation/press release,
F16 applies plus any F6/F10/F11 numbers the document carries; most balance-sheet
and auditor-report checks (F3, F4, F5, F8, F9, F11, F15) are N.A. because a Reg 30
press release carries no auditor report, no balance sheet, and no consolidation
entity list. F17 (concall silence audit) is N.A. — this is a press release, not a
transcript; keg-volume silence is instead captured under F12.

---

## FINDINGS TABLE

| id | check | ledger row ref | line | verbatim quote | classification | forward implication |
|----|-------|----------------|------|----------------|----------------|----------------------|
| F2.1 | F2 | §1 row 5 / §8 note | 36-37 | "Unaudited Standalone and Consolidated Financial Results of the Company for the quarter ended on 30th June, 2026" | AMBIGUOUS | Cover letter promises standalone + consolidated; body shows only the Consolidated Highlights table (line 156). Parent-only performance is withheld, so any divergence between the India parent and the Brazil/Europe subsidiaries is invisible. A4: obtain standalone P&L to test parent-vs-subsidiary split. |
| F6.1 | F6 | §5 row 7-8 | 113 | "Installation activities commenced following the delivery of the first batch of large storage tanks to the mini-LNG terminal project site in The Bahamas" | FORWARD-SIGNAL | Sole clean status-transition ("commenc") in the document: Bahamas mini-LNG has moved from supply to installation phase → revenue-recognition milestone due next 1-2 quarters. Track "commenced" → "completed" transition and the "satellite LNG stations" follow-on (line 115). |
| F12.1 | F12 | §4 rows 1-4 | 100, 109, 117, 126 | "The Stainless-Steel Keg – During the quarter, the Company continued executing orders..." (no % given) | AMBIGUOUS | IG 53% + LNG 22% + CSD 20% = 95% of revenue; the keg segment paragraph carries NO revenue %, NO volume, NO run-rate. Keg is the thesis "weakening leg" (Notion checklist 4: red if flat at 10-12k vs 100k target). The one segment with a deteriorating watch-metric is the one segment left unquantified. A4: keg quarterly volume + revenue % + Q-o-Q trend. |
| F16.1 | F16 | §2 rows 1-3 / §8 rows 1-3 | 85-87, 161-165 | "Revenue... grew 8.3%... EBITDA... rose 1.4%... PAT... stood at ₹ 61 Cr" | FORWARD-SIGNAL | Operating deleverage masked by absolute-growth framing. Revenue +8.3% (352→382), EBITDA +1.4% (88→90), PAT 0% (61→61). EBITDA margin fell 25.0%→23.6% (−150bps); PAT margin fell 17.3%→15.9% (−140bps). 8.3% top-line growth converted to zero PAT growth; incremental EBITDA margin ≈ 2/30 = 6.7%. Each line framed "grew/rose/stood" with no mention of margin decline. |
| F16.2 | F16 | §2 row 5 / §3 row 7 / §7 rows 1-2 | 89, 96-98, 144-146 | "taking total order book to ₹ 1,686 Cr"; "Export orders now exceed ₹1,140 Cr" | AMBIGUOUS | Order book (1,686), inflow (532) and export order book (1,140) carry no definition (gross vs net of GST, executed vs pending) and no opening balance, so the roll-forward is unverifiable (implied opening ≈ 1,686 − 532 + revenue executed). Export order book is 67.6% of total book vs export at 58% of current revenue → future revenue mix skewing further to exports. A4: opening order book, execution during quarter, order-book definition. |
| F16.3 | F16 | §2 rows 1-2 / §8 rows 1-2 | 85-86, 161-163 | "grew 8.3% YoY"; "rose 1.4% YoY" | NEUTRAL-FACT | Integer-implied YoY differs from stated: revenue 382/352 = 8.52% (stated 8.3%); EBITDA 90/88 = 2.27% (stated 1.4%). Consistent with sub-crore rounding (underlying EBITDA ≈ 89.6/88.4), but the EBITDA 0.9pp gap sits at the edge of rounding tolerance — documented, no contradiction. |

---

## ARITHMETIC RECONCILIATION (all eight headline figures cross-checked)

Every headline number is internally consistent with the others within rounding;
NO arithmetic contradiction was found. The analytically material result is the
margin trend, not an arithmetic error.

| metric | stated | recomputed | verdict |
|--------|--------|-----------|---------|
| Revenue YoY | 8.3% | 30/352 = 8.52% | consistent within rounding (F16.3) |
| EBITDA YoY | 1.4% | 2/88 = 2.27% | edge of rounding tolerance (F16.3) |
| EBITDA margin | 23.5% | 90/382 = 23.56% | ✓ |
| PAT margin | 15.9% | 61/382 = 15.97% | ✓ (truncated; implies PAT ≈ 60.9) |
| Export % of revenue | 58% | 222/382 = 58.1% | ✓ |
| PAT YoY | 0% | 61 vs 61 | ✓ |
| EBITDA margin Q1FY26 (derived) | — | 88/352 = 25.0% | → −150bps YoY (F16.1) |
| PAT margin Q1FY26 (derived) | — | 61/352 = 17.3% | → −140bps YoY (F16.1) |
| Export order book share | — | 1,140/1,686 = 67.6% | future mix more export-weighted (F16.2) |
| Segment mix sum | — | 53+22+20 = 95% | 5pp gap = keg, unquantified (F12.1) |

FY26 column self-consistency: EBITDA 388/1,632 = 23.8%; PAT 258/1,632 = 15.8%. Consistent.

---

## CHECKLIST SCORECARD (all 17, one status each — GATE A3)

| # | status | basis |
|---|--------|-------|
| F1 | N.A. | No zero-standing line items (ledger §8: zero_standing count = 0). Press release carries no BS/CF/P&L template — only a 3-row Consolidated Highlights table, all nonzero. |
| F2 | FINDING | Standalone promised (line 36-37) but only consolidated table disclosed (line 156). Gap is uncomputable → the disclosure omission itself is the finding (F2.1). |
| F3 | N.A. | No standalone cost lines to compare against consolidated; shell-entity test not runnable in a press release. |
| F4 | N.A. | No auditor Other Matters / component-auditor split; results labelled "unaudited" (line 36, 91) with no review scope table. |
| F5 | N.A. | No going-concern / EoM paragraph in a press release; no prior-quarter extract supplied to diff. |
| F6 | FINDING | Lexicon hit "commenc" at line 113 (Bahamas installation commenced) = status transition (F6.1). "approved by the Board" (line 92) refers to results, not a project. See Commitment Register. |
| F7 | PASS | No hedge lexicon term present ("no assurance", "subject to", "evaluating", "exploring", "endeavour" — none). Observation: document carries NO safe-harbor / forward-looking-statement disclaimer while repeating the unhedged claim "providing strong revenue visibility for the coming quarters" twice (lines 97-98 and 145-146; A2 REPEAT_PHRASE). All-upside framing; no newly added hedge to flag. |
| F8 | N.A. | No PBT or tax line disclosed; ETR not computable (only EBITDA and PAT given). |
| F9 | N.A. | No OCI / actuarial disclosure in a press release. |
| F10 | N.A. | No share count, paid-up capital, or EPS disclosed in this deck. |
| F11 | N.A. | No balance sheet / other equity / net worth disclosed. |
| F12 | FINDING | Segment revenue mix incomplete: 53%+22%+20% = 95%, keg segment unquantified (F12.1). No segment assets/liabilities disclosed (that portion N.A.); the keg silence carries the F17 monitoring item. |
| F13 | N.A. | No AGM notice, record date, AR/Board's-Report approval, or director appointment/term dates beyond routine "approved by the Board of Directors" for the results (line 92). |
| F14 | PASS | Entity-name variants (INOXCVA / INOX CVA / INOX India Limited) are brand vs legal name, not a governance inconsistency; "INDX INDIA LIMITED" (line 71) and garbled scrip/CIN are OCR artifacts (A2 OCR_GARBLE), not document defects. No note-vs-auditor conflict (no auditor letter). Signature timestamp 18:08:33 (line 59) with no disclosed board start/end time (A2 TIMESTAMP_NO_BOARD_TIME_REF) — immaterial, no same-day sequencing to cross-check. The substantive standalone-vs-body mismatch is logged under F2. |
| F15 | N.A. | No consolidation entity list in a press release; no prior-quarter ledger to diff additions/deletions/renames. |
| F16 | FINDING | Presentation-specific: margin compression masked by absolute-growth framing (F16.1); order-book definition/roll-forward undefined (F16.2); integer-implied YoY vs stated (F16.3); standalone disclosure dropped (cross-ref F2.1). |
| F17 | N.A. | Press release, not a concall transcript — no turns to audit for silence. Keg-volume silence (Notion checklist 4) captured under F12.1; order backlog 1,686 satisfies Notion checklist 2 (green ≥1,500). |

GATE A3: pass — all 17 checks carry exactly one status, no blanks.

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | ref | status word |
|------------|-------------|-----|-------------|
| Bahamas mini-LNG terminal — installation of large storage tanks | H1 FY27 (post 30-Jun-2026) | line 113 | commenced / underway |
| Satellite LNG stations follow-on from Bahamas success | undated (opportunity, not committed) | line 115 | opportunity created |
| Semiconductor transportation tanks — Dholera facilities | initial orders booked in Q1 | line 105 | secured / initiated |
| CERN cryogenic modules order | in execution | line 118 | secured |
| ITER, France — repeat order | in execution | line 123-124 | secured (repeat) |
| Six additional space-exploration cryogenic tanks (same customer) | in execution | line 102 | secured |

Note: the register is dominated by past-tense "secured/received" wins, not dated
forward commitments. The single clean forward status transition to track is the
Bahamas installation ("commenced", line 113).

---

## FORWARD-SIGNAL SUMMARY FOR A4
- FORWARD-SIGNAL: F6.1 (Bahamas install commenced — milestone due), F16.1 (margin compression / operating deleverage).
- AMBIGUOUS → convert to management questions: F2.1 (standalone withheld), F12.1 (keg volume/% unquantified — the weakening leg), F16.2 (order-book definition & opening balance).
- NEUTRAL-FACT: F16.3 (rounding).

---

```yaml
stage: A3-forensics
company: "INOXINDIA"
quarter: "Q1 FY27"
doctype: "presentation"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/inoxindia-q1fy27/work/forensics_presentation_inoxindia_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: "N.A."
  F2: FINDING
  F3: "N.A."
  F4: "N.A."
  F5: "N.A."
  F6: FINDING
  F7: PASS
  F8: "N.A."
  F9: "N.A."
  F10: "N.A."
  F11: "N.A."
  F12: FINDING
  F13: "N.A."
  F14: PASS
  F15: "N.A."
  F16: FINDING
  F17: "N.A."
findings:
  - {id: "F2.1", check: "F2", line: "36-37", classification: "AMBIGUOUS", implication: "Standalone results promised in cover letter but only consolidated shown; parent-vs-subsidiary divergence invisible"}
  - {id: "F6.1", check: "F6", line: "113", classification: "FORWARD-SIGNAL", implication: "Bahamas mini-LNG installation commenced; revenue-recognition milestone due next 1-2 quarters"}
  - {id: "F12.1", check: "F12", line: "100,109,117,126", classification: "AMBIGUOUS", implication: "Segment mix 95% (53+22+20); keg segment unquantified for %, volume and run-rate — the thesis weakening leg is the unqquantified one"}
  - {id: "F16.1", check: "F16", line: "85-87,161-165", classification: "FORWARD-SIGNAL", implication: "Operating deleverage: +8.3% revenue -> 0% PAT; EBITDA margin -150bps, PAT margin -140bps YoY, masked by absolute-growth framing"}
  - {id: "F16.2", check: "F16", line: "89,96-98,144-146", classification: "AMBIGUOUS", implication: "Order book/inflow/export order book undefined and no opening balance; roll-forward unverifiable; export order book 67.6% of book vs 58% of revenue"}
  - {id: "F16.3", check: "F16", line: "85-86,161-163", classification: "NEUTRAL-FACT", implication: "Integer-implied YoY (8.5%/2.3%) differs from stated (8.3%/1.4%); consistent with sub-crore rounding, EBITDA gap at edge of tolerance"}
forward_signals: ["F6.1", "F16.1"]
ambiguous: ["F2.1", "F12.1", "F16.2"]
commitments:
  - {commitment: "Bahamas mini-LNG terminal installation of large storage tanks", implied_date: "H1 FY27 (post 30-Jun-2026)", ref: "line 113", status_word: "commenced"}
  - {commitment: "Satellite LNG stations follow-on from Bahamas", implied_date: "undated", ref: "line 115", status_word: "opportunity"}
  - {commitment: "Semiconductor transportation tanks for Dholera facilities", implied_date: "Q1 FY27 initial orders", ref: "line 105", status_word: "initiated"}
  - {commitment: "CERN cryogenic modules order", implied_date: "in execution", ref: "line 118", status_word: "secured"}
  - {commitment: "ITER France repeat order", implied_date: "in execution", ref: "line 123-124", status_word: "secured"}
gate_a3: pass
blank_checks: []
```
