# A3 FORENSIC NOTES: QPOWER Q2 FY27 | doctype: presentation (one-off Reg 30 letter, Turkiye PCS manufacturing commencement, doctag turkiye)

Agent: A3 forensic notes | model: claude-opus-5-5 | run date: 2026-10-19 | loop iteration 1 update: 2026-10-20 (A2 rows M01, M02 added)
Inputs read: A1 structured (runs/qpower-q2fy27/extracted/qpower-turkiye-q2fy27-structured.md), A1 fulltext (runs/qpower-q2fy27/extracted/qpower-turkiye-q2fy27-fulltext.md), A2 ledger (runs/qpower-q2fy27/work/ledger_turkiye_qpower_q2fy27.md), Notion brief sections 4, 5, 7, 9 (runs/qpower-q2fy27/work/notion-brief.md; memory to weigh, not evidence). Prior-quarter fulltext: none supplied. Source PDF and inputs/ not opened.

## 1. LEDGER RECONCILIATION (30 of 30 units read at fulltext line; 100%: R001-R028 plus M01-M02)

| Row | A1 line | Verified at fulltext line | Verbatim (short) | Result |
|---|---|---|---|---|
| R001 | 27 | 27 | "BSE Scrip Code: 544367" | match |
| R002 | 23 | 23 | "Exchange Plaza, Plot No. C/1, G Block," | match |
| R003 | 24 | 25 | "Mumbai - 400051" | LINE OFFSET (A1 says 24; 24 carries 400001) |
| R004 | 24 | 24 | "Dalal Street, Fort, Mumbai - 400001" | match |
| R005 | 29 | 29 | "SEBI (LODR) Regulations, 2015" | match (RESTATED = R025) |
| R006 | 29 | 29, 53 | "Intimation under Regulation 30" | match |
| R007 | 71 | 71 | "Membership No. A27641" | match |
| R008 | 22 | 22 | "National Stock Exchange of India Limited," | match |
| R009 | 22 | 22 | "BSE Limited" | match |
| R010 | 27 | 27 | "NSE Symbol: QPOWER" | match |
| R011 | 34 | 35 | "of our subsidiary, Endoks Energy Systems" | LINE OFFSET (A1 says 34) |
| R012 | 30 | 30, 35 | "PCS Facility in Nide, T?rkiye" | match (extraction damage noted by A1 header line 16) |
| R013 | 34 | 34 | "new Power Conversion Systems (PCS) manufacturing facility" | match |
| R014 | 38 | 38 | "power electronic converters and inverters" | match |
| R015 | 39 | 38-39 | "utility-scale Battery Energy Storage Systems (BESS)" | match |
| R016 | 47 | 46 | "execution of its international BESS order book" | LINE OFFSET (A1 says 47); NO_FIGURES_DISCLOSED confirmed |
| R017 | 60 | 60 | "For Quality Power Electrical Equipments Limited" | match |
| R018 | 67 | 67, 69 | "Deepak Ramchandra Suryavanshi ... Company Secretary & Compliance Officer" | match |
| R019 | 21-24 | 22-25 | address block NSE / BSE | LINE OFFSET (block runs 22-25) |
| R020 | 50 | 50-51 | "will progressively ramp up production in accordance with its operational plans and customer delivery schedules" | match; FORWARD_NO_DATES_OR_VOLUMES confirmed |
| R021 | 45-47 | 45-48 | "supports the execution of its international BESS order book" | match; FORWARD_NO_DATES_OR_VOLUMES confirmed |
| R022 | 19 | 19 | "Date: 17 October 2026" | match |
| R023 | 36 | 36 | "operations on 16 October 2026." | match |
| R024 | 65 | 65 | "Date: 2026.10.17 15:30:33 +05'30'" | match |
| R025 | 29 | 29 | "2015" | match (RESTATED = R005) |
| R026 | 62 | 62 | "Digitally signed by DEEPAK" | match; A1_NONDATE_IN_DATE_TABLE confirmed (label, not a date) |
| R027 | 53 | 53 | "submitted for your records pursuant to Regulation 30" | match (RESTATED = R022) |
| R028 | 36 | 36 (no quarter text in document) | "operations on 16 October 2026." | A1_NONDATE_IN_DATE_TABLE confirmed; QUARTER TAG WRONG, see FN-04 |
| M01 | n/a (A2 cites fulltext 41-43) | 41-43 | "an important step in the Group's expansion into power electronics and energy storage technologies, complementing its established portfolio of high-voltage equipment and power quality solutions." | match, verbatim; MISSING_FROM_STRUCTURED confirmed; see FN-05 |
| M02 | n/a (A2 cites fulltext 45, first clause) | 45 | "The new facility strengthens the Group's manufacturing and system integration capabilities," | match, verbatim; MISSING_FROM_STRUCTURED confirmed; cited in FN-03 |

Line offsets (R003, R011, R016, R019) are one-line errors in A1's index. Every quote exists at the adjacent line. No row content is wrong. M01 and M02 are A2 additions for text A1 did not index; both quotes match the fulltext word for word. ZERO_STANDING rows: none. Qualifier rows: none (fulltext confirms; line 16 is an extraction-tool note, not document text).

## 2. FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| FN-01 | F6 | R011, R013, R023 | 34-36 | "commenced manufacturing operations on 16 October 2026" | FORWARD-SIGNAL | Status word "commenc" = completed. Notion memory carried "Endoks PCS Nigde Dec 2026 ON TRACK ($2M Phase 1)". Delivery lands about 2 months ahead of that date. This runs against the logged pattern "Capex slips 1-2 quarters from initial guidance" (Sangli). Promise-vs-delivery tracker: DELIVERED (early), PROVISIONAL. Bear reading: "manufacturing operations" may mean trial or first-article output, not commercial production. A4 question: is this commercial production with customer-accepted units, or trial runs? |
| FN-02 | F6 | R020, R014, R015 | 38-39, 50-51 | "will progressively ramp up production in accordance with its operational plans and customer delivery schedules" | AMBIGUOUS | Undated, unquantified ramp. No capacity (MW or units per year), no capex spent vs the $2M Phase 1 in memory, no utilisation path, no first-revenue quarter. The ramp is tied to "customer delivery schedules", so output pace is demand-paced and can be lumpy. Line 39 widens scope to "other grid-connected applications", beyond BESS. A4 questions: Phase 1 capacity and capex to date; first quarter of PCS revenue; share of output for in-group BESS vs third-party or non-BESS sales. |
| FN-03 | F16 | R016, R021, M02 | 45-46 | "supports the execution of its international BESS order book" | AMBIGUOUS | The order book is cited as the reason for the facility, with no size, no customer count, no delivery window. Memory carries a $30M BESS order book and a $60-80M FY27 BESS target; this letter neither restates nor updates either. [INFERENCE] M02 (line 45) "strengthens the Group's manufacturing and system integration capabilities" suggests PCS was earlier bought in; in-house PCS would raise content per BESS unit inside Endoks. [INFERENCE] Endoks is a 51%-owned subsidiary already at 51% of consol PAT (memory, 07-Sep); growth here feeds the Endoks-concentration tracker (falsifier >55%) and the 49% NCI leakage. A4 questions: current BESS order book size; share of order book that uses in-house PCS; PCS margin vs bought-in cost. |
| FN-04 | F6 | R023, R028 | 36 | "operations on 16 October 2026." | NEUTRAL-FACT | 16-Oct-2026 falls in Q3 FY27 (October-December), not Q2 FY27. A1 R028 tags the event Q2 FY27 "event falls in quarter"; the tag is wrong. Nothing from this facility can sit in Q2 FY27 numbers. Q2 results may carry it only as a subsequent event. The tracker entry for FN-01 belongs to Q3 FY27. |
| FN-05 | F16 | M01 | 41-43 | "the Group's expansion into power electronics and energy storage technologies, complementing its established portfolio of high-voltage equipment and power quality solutions" | AMBIGUOUS | The letter frames power electronics and energy storage as a new business strand, separate from the "established portfolio". It gives no revenue share, capex, segment or margin figure for the new strand. Two readings: (a) a planned diversification that adds a growth line; (b) capital and management attention moving away from the HVDC and power-quality core that carries the Section 1B strategic premium. Lean bear until a figure separates them. A4 questions: will PCS and BESS be reported as a separate segment or line in the Q2/Q3 FY27 filings; what share of the Rs700 Cr QIP (memory) or group capex goes to power electronics; target revenue share of the new strand by FY28. |

No CONFIRMATORY-NEGATIVE findings. Flagged for A4: FN-01 (FORWARD-SIGNAL), FN-02, FN-03 and FN-05 (AMBIGUOUS).

## 3. CHECKLIST SCORECARD

| Check | Status | Basis |
|---|---|---|
| F1 | N.A. | No financial tables; A2 ZERO_STANDING: none. |
| F2 | N.A. | No standalone or consolidated figures in the letter. |
| F3 | N.A. | No cost lines. |
| F4 | N.A. | No auditor letter or Other Matters paragraph. |
| F5 | N.A. | No going concern or EoM language; no prior-quarter extract supplied. |
| F6 | FINDING | Lexicon hit "commenc" (lines 29, 35); forward "will" ramp (line 50). FN-01, FN-02, FN-04; register below. M01 (lines 41-43) and M02 (line 45) checked: no lexicon hit, no dated commitment. |
| F7 | PASS | Lexicon searched (may sometimes, could have an effect, no assurance, subject to, evaluating, exploring, in discussions, endeavour) across all 30 units including M01 and M02: zero hits. The one conditional ("customer delivery schedules", line 51) is carried in FN-02, not counted twice. |
| F8 | N.A. | No tax data. |
| F9 | N.A. | No OCI data. |
| F10 | N.A. | No share capital or EPS in the letter. |
| F11 | N.A. | No net worth or reserves figure in the letter. |
| F12 | N.A. | No segment data. FN-05 asks whether the new strand will get segment reporting. |
| F13 | N.A. | Not a board outcome; no AGM, director or enabling-resolution content. |
| F14 | PASS | Names consistent within the letter: "Endoks Energy Systems" (line 35), "Quality Power Electrical Equipments Limited" (line 60), "Group" (lines 41, 45). No auditor letter to compare. Location rendering defect ("Nide", line 30, 35) is extraction damage (A1 header line 16), not drafting. |
| F15 | N.A. | No consolidation list. Endoks described as "our subsidiary" (line 35), consistent with memory (51%-owned). |
| F16 | FINDING | Presentation check. No prior deck to diff. The letter cites the order book with no figure (FN-03) and frames a new business strand with no figure (FN-05). |
| F17 | N.A. | Not a concall. Checklist cross-reference in section 5 is informational; a single-topic Reg 30 letter carries no silence count. |

All 17 checks marked. GATE A3: pass.

## 4. COMMITMENT REGISTER (F6)

| commitment | implied date | ref | status word |
|---|---|---|---|
| Endoks PCS facility, Nigde, Turkiye: start manufacturing | 16-Oct-2026 (memory target: Dec 2026) | lines 34-36 (R011, R013, R023) | completed |
| Progressive production ramp-up "in accordance with its operational plans and customer delivery schedules" | undated | lines 50-51 (R020) | initiated |
| Facility supports execution of the international BESS order book | undated; no order-book figure | lines 45-46 (R016, R021) | underway (implied, present tense) |

M01 and M02 add no register line: both are positioning and capability statements with no date and no deliverable.

## 5. NOTION CHECKLIST CROSS-REFERENCE (informational; F17 N.A.)

| Notion item (memory) | Touched by letter? | Note |
|---|---|---|
| Growth trigger: Endoks PCS Nigde Dec 2026 ON TRACK ($2M Phase 1) | Yes, lines 34-36 | Commencement 16-Oct-2026; $2M Phase 1 not restated (FN-01, FN-02). |
| Growth trigger: BESS Europe scaling ($30M order book; $60-80M FY27) | Partly, line 46 | Order book named, no figure (FN-03). |
| Growth trigger: PCS standalone line (1725 kW inverter launch Q1-Q2 FY27) | Partly, lines 38-39, 41-43 | "converters and inverters ... and other grid-connected applications"; framed as Group "expansion into power electronics" (FN-05); no product rating named. |
| Tracker: Endoks % of consol PAT (falsifier >55%) | Indirectly | New capacity sits in Endoks (FN-03 inference). |
| Checklist items 1-17 (revenue, margins, CFO/PAT, Sangli, WSIL, QIP, ESOP, auditors) | No | Out of scope for a single-event letter; not counted as silence. |

## 6. PIPELINE NOTES

- A1 quarter tag R028 is wrong: the event date (line 36) is in Q3 FY27. A4 should log FN-01 against Q3 FY27.
- A1 line cites for R003, R011, R016 and R019 are one line off; content verified at the correct lines.
- A1 did not index lines 41-43 and the first clause of line 45; A2 rows M01 and M02 cover them (loop iteration 1). Reconciliation now runs over 30 units.
- Reg 30 timing: disclosure signed 17-Oct-2026 15:30:33 IST (line 65); the letter does not state the commencement time on 16-Oct, so the 24-hour window cannot be tested. Observation only, not a finding.

```yaml
stage: A3-forensics
company: "QPOWER"
quarter: "Q2 FY27"
doctype: "presentation"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/qpower-q2fy27/work/forensics_turkiye_qpower_q2fy27.md"
ledger_reconciled_pct: 100        # 30 of 30 units (R001-R028 + M01-M02)
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
  F13: N.A.
  F14: PASS
  F15: N.A.
  F16: FINDING
  F17: N.A.
findings:
  - {id: "FN-01", check: "F6", line: "34-36", classification: "FORWARD-SIGNAL", implication: "\"commenced manufacturing operations on 16 October 2026\": Endoks PCS Nigde delivered about 2 months ahead of the Dec 2026 target in memory; tracker DELIVERED (early), provisional until commercial vs trial production is confirmed."}
  - {id: "FN-02", check: "F6", line: "50-51", classification: "AMBIGUOUS", implication: "\"will progressively ramp up production in accordance with its operational plans and customer delivery schedules\": no capacity, capex, utilisation or first-revenue quarter; ramp demand-paced and possibly lumpy; scope includes non-BESS grid applications (line 39)."}
  - {id: "FN-03", check: "F16", line: "45-46", classification: "AMBIGUOUS", implication: "\"supports the execution of its international BESS order book\": order book cited with no figure; memory $30M / $60-80M FY27 neither restated nor updated; [INFERENCE] M02 capability clause suggests in-house PCS lifts content per BESS unit inside 51%-owned Endoks and feeds the Endoks-concentration tracker."}
  - {id: "FN-04", check: "F6", line: "36", classification: "NEUTRAL-FACT", implication: "\"operations on 16 October 2026.\": event falls in Q3 FY27, not Q2 FY27 as A1 R028 tags it; no facility contribution in Q2 numbers; log the delivery against Q3 FY27."}
  - {id: "FN-05", check: "F16", line: "41-43", classification: "AMBIGUOUS", implication: "\"the Group's expansion into power electronics and energy storage technologies, complementing its established portfolio\": new business strand framed with no revenue, capex, segment or margin figure; diversification vs capital drift from the HVDC core; ask about segment reporting and QIP/capex share."}
forward_signals: ["FN-01"]
ambiguous: ["FN-02", "FN-03", "FN-05"]
commitments:
  - {commitment: "Endoks PCS facility Nigde Turkiye starts manufacturing", implied_date: "2026-10-16 (memory target Dec 2026)", ref: "fulltext lines 34-36; R011 R013 R023", status_word: "completed"}
  - {commitment: "Progressive production ramp-up per operational plans and customer delivery schedules", implied_date: "undated", ref: "fulltext lines 50-51; R020", status_word: "initiated"}
  - {commitment: "Facility supports execution of international BESS order book", implied_date: "undated, no order-book figure", ref: "fulltext lines 45-46; R016 R021", status_word: "underway"}
gate_a3: pass
blank_checks: []
analyst_note: "A single-event Reg 30 letter, so 13 of 17 checks are N.A. Its value is one dated delivery. Notion memory (not evidence) carried Endoks PCS Nigde Dec 2026 ON TRACK ($2M Phase 1). Commencement on 16-Oct-2026 lands about two months early, against the logged pattern that capex slips 1-2 quarters (Sangli). Bear reading: manufacturing operations may mean trial output, not commercial production. The letter gives no capacity, capex, first-revenue quarter or order-book figure. The observation that separates the readings is PCS revenue or units disclosed for Q3 FY27. M01 frames power electronics as a new Group strand beyond the established portfolio, with no figure; FN-05 asks whether it gets its own segment and capital. Quarter tag: A1 R028 marks the event Q2 FY27, but 16-Oct-2026 falls in Q3 FY27; nothing from the facility sits in Q2 numbers. A1 line cites for R003, R011, R016 and R019 are one line off; quotes verified at the correct lines. Commencement time not stated, so the Reg 30 24-hour window cannot be tested."
```
