# A3 FORENSIC NOTES — INDGN Q1 FY27 — DOCTYPE: RESULTS

Source document: Reg 33 unaudited Standalone + Consolidated results + Limited Review Report, Indegene Limited, quarter ended 30 June 2026.
Inputs read: A1 extract `work/extract_results_indgn_q1fy27.txt` (654 lines, 10 pages, unit Rs millions, ÷10 to crore); A2 ledger `work/ledger_results_indgn_q1fy27.md`.
Ledger reconciliation: 100% — every A2 row read at its cited line in the A1 extract before judging. Prior-quarter extract NOT supplied (A2-flagged gap): F5 EoM diff and F15 QoQ entity diff run only on internal evidence.
Model: claude-opus-4-8. All 17 checks carry a status (GATE A3). F16/F17 are N.A. per results-doctype applicability.

---

## FORENSIC CORRECTION CARRIED INTO THIS REPORT (A2 reconciliation error caught at source)
A2 (§4 Note 6 flag, line 155) read the TCPA provision as "Rs.103mn (USD 2.30mn at ~Rs.44.8/USD)." That is wrong. The settlement cap is stated as Rs.417mn = USD 4.72mn (line 406), which implies Rs.88.3/USD. At that rate USD 2.30mn = **Rs.203mn**, which ties exactly to the Q4 FY26 exceptional-item line of **(203)** (line 229) and to the recovered segment-block values (203) at lines 368/374, and matches the Notion spine ("TCPA provision Rs 203 mn"). The provision is Rs.203mn, not Rs.103mn. This correction sharpens F1/F7 below (provision Rs.203mn vs cap Rs.417mn = up to **Rs.214mn** residual exposure).

---

## FINDINGS TABLE

| id | check | ledger row / line | short verbatim quote | classification | forward implication |
|----|-------|-------------------|----------------------|----------------|---------------------|
| A3-01 | F1 | line 229 (exceptional); lines 308-312 & 581-589 (IPO table) | "Exceptional items (net) (refer note I 0) ... -" | FORWARD-SIGNAL | Exceptional line dormant (nil) this quarter but the litigation behind it is under-provisioned (Rs.203mn booked vs Rs.417mn cap). IPO proceeds 100% utilised, nil unutilised on every row → no IPO buffer to fund the next capex/M&A; future inorganic growth must draw cash/debt. |
| A3-02 | F2 | consol lines 216/238; standalone lines 508/525 | consol rev "10,631" vs standalone "3,407"; consol PAT "1,162" vs standalone "599" | FORWARD-SIGNAL | Consolidated EBITDA margin FLAT sequentially (16.4% Q1FY27 vs 16.3% Q4FY26) and DOWN ~400bps YoY (20.4% Q1FY26) → PRIMARY Notion tripwire (margin expansion) FAILS. Standalone (Indian parent) revenue FELL -7.5% QoQ (3,682→3,407) while consolidated ROSE +5.9%; all sequential growth is subsidiary/offshore. Other expenses +85% YoY vs revenue +40%; D&A +104% YoY — M&A-integration dilution signature. |
| A3-03 | F2 | consol line 238 vs standalone line 525 | subsidiary PAT = 1,162-599 = "563" (Q1FY27) vs 797-721 = "76" (Q4FY26) | FORWARD-SIGNAL | Subsidiary PAT contribution swings from 9.5% of consol PAT (Q4FY26) to 48.5% (Q1FY27); the QoQ gap move of Rs.487mn is ~81% of standalone PAT, far above the 5pp-of-standalone-PAT FINDING threshold. Consolidated earnings quality is volatile and subsidiary-led; the parent alone contracted (PAT 721→599). |
| A3-04 | F6 | Note 6 lines 407-414; Note 7 line 417 | "remains subject to execution of definitive agreements and approval by the Court"; "will be formalizing into the Settlement agreement post approval by the court"; "subject to the approval of shareholders at the ensuing Annual General Meeting" | FORWARD-SIGNAL | Dateable management commitments feeding the FTTCP catalyst timeline: (i) TCPA settlement to be formalised post court approval (term sheet signed 25 May 2026); (ii) FY26 final dividend Rs.2.25/share, ~Rs.542mn outflow, pending the ensuing AGM. |
| A3-05 | F7 | Note 6 lines 406-407, 411 | "the actual outflow is contingent upon valid claims submitted by eligible class members, and unclaimed amounts, if any, revert to the Group" | FORWARD-SIGNAL | Claims-made contingency = pre-emptive cover. Provision Rs.203mn vs settlement cap Rs.417mn → up to Rs.214mn additional exceptional charge possible if all valid claims are filed. "does not estimate any change in the amount of provision as on 30 June 2026" (line 413) is a management judgement, not a legal ceiling. |
| A3-06 | F8 | consol line 235 (deferred tax) | deferred tax "(524)" FY26 vs "72" Q1FY27 | FORWARD-SIGNAL | FY26 audited deferred-tax CREDIT of Rs.524mn shielded consolidated ETR to 23.6% (vs ~33.6% without it, ~1,000bps shield); Q1FY27 deferred tax reverted to a Rs.72mn CHARGE. As the DTA unwinds, ETR normalises upward. No "tax relating to earlier years" line present (that specific trigger nil). Confirm DTA composition at the AR. |
| A3-07 | F10 | agenda line 39; capital lines 259/539 | "Approved allotment under ESOP Scheme 2020." | AMBIGUOUS | Fresh ESOP allotment approved with NO share count, grant date or tranche disclosed (A2 bare-disclosure flag). Paid-up capital rose 479→481 YoY (~1mn shares, FV Rs.2). Diluted-vs-basic EPS spread stable (~0.6%), so no new heavy dilutive instrument, but allotment size is an information gap → A4 management question. |
| A3-08 | F12 | Note 5 narrative lines 392-393 | "not practicable to provide segment disclosures relating to total assets and liabilities ... a meaningful segregation of the available data is onerous" | AMBIGUOUS | Standing refusal to disclose segment assets/liabilities blocks the equity-funded-build / capex-proxy / future-funding-need analysis F12 exists for. Recurring qualitative limitation; the "onerous" justification is soft for a two-segment group → A4 question on segment capital intensity. |
| A3-09 | F12 | segment result line 351; lines 350/345 | Others result "(115)" vs "(50)" Q1FY26; ECS result "1,197" on rev "7,502" | FORWARD-SIGNAL | "Others" (consultancy + clinical business) loss widened YoY -50→-115. Enterprise Commercial Solutions margin compressed 16.9% (Q4FY26) → 16.0% (Q1FY27) despite revenue growth; Enterprise Medical Solutions held ~26%. The consolidated margin flatness (A3-02) is ECS-led. |
| A3-10 | F13 | agenda line 39; Note 7 line 417 / standalone Note 6 line 610 | "Approved allotment under ESOP Scheme 2020."; "ensuing Annual General Meeting ... cash outflow of approximately t542" | FORWARD-SIGNAL | Board Outcome carries a corporate action (ESOP dilution) beyond results. FY26 AGM is foreshadowed in the notes (not formally noticed in this letter) and carries the Rs.542mn dividend and any special resolutions — schedule an AGM/dividend calendar event. No AR-approval, no director-term item this quarter. |
| A3-11 | F14 | consol P&L line 229 | "Exceptional items (net) (refer note I 0)" | NEUTRAL-FACT | The exceptional line cross-references "note 10"; the filing's consolidated notes run only 1-7 and the litigation note is Note 6. Stale/garbled cross-reference (OCR or drafting). Individually immaterial, logged as a governance-drafting data point. |
| A3-12 | F14 | Note 6 line 400 | "Indegene Encima Inc., Indegene Wincere Inc., and lndegene Healthcare, LLC" | AMBIGUOUS | Three named co-defendants in the TCPA note do NOT appear anywhere in the 29-entity Annexure I consolidation list (lines 162-196). Also "Exception Item" typo (line 395) and the CFO declaration's singular "Financial Results / an unmodified opinion" (line 625) not distinguishing standalone vs consolidated. Cumulative drafting-control weakness. |
| A3-13 | F15 | Note 6 line 400 vs Annexure I lines 162-196 | co-defendants "Indegene Encima Inc., Indegene Wincere Inc." absent from the 29-entity list | AMBIGUOUS | Consolidation-scope inconsistency: entities that existed at the 2020-21 litigation vintage are absent from the current group list — likely merged/dissolved/renamed. Direct QoQ additions/deletions diff is deferred (prior-quarter entity list not supplied). → A4 question: what happened to Encima/Wincere/Healthcare LLC. |

Neutral / no-action items recorded for completeness: standalone FX-translation line (line 532) zero across all four periods = parent has no foreign branch (expected); Other-equity quarterly blanks (lines 260/540) = annual-only convention; board-meeting duration 45 min and signature timestamp 18:39 IST after 18:15 conclusion (A2 §1b) = clean, no pre-conclusion-signature pattern.

---

## CHECKLIST SCORECARD (F1-F17, one status each)

| Check | Status | One-line basis |
|-------|--------|----------------|
| F1 Zero-value standing lines | FINDING | 14 ZERO_STANDING rows read; exceptional-item line (229) is a live, under-provisioned litigation slot; IPO table fully utilised → nil future buffer (A3-01). |
| F2 Standalone-vs-consolidated | FINDING | S/C gap computed on revenue, EBITDA, PAT all four periods; consol margin flat/-400bps YoY, parent revenue -7.5% QoQ, subsidiary PAT swing >5pp (A3-02, A3-03). |
| F3 Shell-entity detection | PASS | Consol employee 6,591 vs standalone 2,217; D&A 441 vs 114 — subsidiaries carry real cost/operations; no shell signature; no Going Concern EoM. Per-entity isolation not possible (aggregate only). |
| F4 Unaudited contribution ratio | PASS | Auditor para 6 (lines 130-139): 11 unreviewed entities, revenue Rs.413mn (3.9% of consol), LOSS Rs.12mn = ~1.0% of consol PAT — below the 10%-of-PAT FINDING threshold. Loss-making + unnamed noted; no prior-period trend available. |
| F5 Going concern / EoM tracking | PASS | Neither review report contains any Emphasis of Matter, Other Matters or Going Concern paragraph (consol para 6 is a reliance paragraph, not EoM). Nothing to track; prior-quarter verbatim diff not available (gap named). |
| F6 Forward-commitment phrase mining | FINDING | "subject to ... approval by the Court", "will be formalizing", "subject to the approval of shareholders", "proposed a final dividend", "Approved allotment" — dated commitments extracted to the register (A3-04). |
| F7 Hedge phrase mining | FINDING | "contingent upon valid claims", "unclaimed amounts, if any, revert", "remains subject to execution of definitive agreements" — litigation contingency cover; Rs.214mn residual exposure (A3-05). |
| F8 Tax forensics | FINDING | ETRs 23.6-25.1% (all ≤ statutory 25.17%); FY26 deferred-tax credit Rs.524mn = ~1,000bps shield now reversing (Q1FY27 +72 charge) → ETR normalization risk (A3-06). No earlier-year tax line. |
| F9 OCI forensics | PASS | Actuarial remeasurement (29) Q1FY27 is the largest single-quarter DB loss (line 241) but magnitude 29 < full-prior-year +41 → assumption-change threshold NOT breached; verify DB discount-rate at AR. FX-translation swing (599→97) is currency-driven, not an assumption change. |
| F10 Share count & dilution | FINDING | Paid-up 479→481 traced to ESOP; basic-vs-diluted spread stable ~0.6% (no new heavy instrument); but fresh ESOP allotment approved with undisclosed size (A3-07). |
| F11 Reserves & net-worth tie-out | PASS | Consol net worth ties internally: Other equity 30,906 + paid-up 481 = 31,387 (line 260/259); standalone 20,324 + 481 = 20,805. No third-party number in this filing to diff; goodwill/net-worth (51.5% per memory) not assessable from a results filing → deferred to AR deep dive. |
| F12 Segment forensics | FINDING | Segment assets/liabilities withheld as "onerous" (lines 392-393); "Others" losses widening -50→-115; ECS margin 16.9%→16.0% (A3-08, A3-09). |
| F13 Board outcome beyond results | FINDING | Agenda item 2 ESOP allotment (dilution); FY26 AGM + Rs.542mn dividend foreshadowed in notes (A3-10). No AR/AGM-notice/director item in this letter. |
| F14 Note drafting inconsistencies | FINDING | "refer note I 0" vs actual Note 6 (line 229); three litigation defendants absent from Annexure I (line 400); "Exception Item" typo; CFO-declaration singular imprecision (A3-11, A3-12). |
| F15 Entity list diffs | FINDING | Litigation co-defendants (Encima, Wincere, Healthcare LLC) absent from current 29-entity consolidation list (A3-13); QoQ additions/deletions diff deferred — prior-quarter list not supplied (named gap). |
| F16 Presentation-specific (dropped/reframed) | N.A. | Doctype is a results filing, not an investor presentation. |
| F17 Concall silence audit | N.A. | Doctype is a results filing; no transcript. Monitoring-checklist non-disclosures instead logged in the coverage note below for A4. |

Status roll-up: **FINDING ×10 (F1,F2,F6,F7,F8,F10,F12,F13,F14,F15) · PASS ×5 (F3,F4,F5,F9,F11) · N.A. ×2 (F16,F17)**. No blank checks → GATE A3 PASS.

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note / ref | status word |
|-----------|--------------|-----------|-------------|
| TCPA class-action settlement to be formalised into definitive Settlement Agreement post US court approval | FY27 (court approval pending) | consol Note 6, line 414 | underway (term sheet signed 25 May 2026) |
| FY26 final dividend Rs.2.25/share, ~Rs.542mn cash outflow, subject to shareholder approval | ensuing AGM (~Aug-Sep 2026) | consol Note 7 line 417 / standalone Note 6 line 610 | proposed (board 29 Apr 2026) |
| Allotment under ESOP Scheme 2020 | 30 July 2026 board | Board Outcome agenda item 2, line 39 | approved (size undisclosed) |
| Rs.2mn residual IPO amount earmarked for office-premises capex | post 29 Jan 2026 board resolution | consol Note 4, lines 319-320 | earmarked (deployment not confirmed) |

---

## NOTION MONITORING CHECKLIST COVERAGE (F17 is N.A. for results; non-disclosures routed to A4)

1. **Operating/EBITDA margin sequential expansion** — ADDRESSED in filing → FAILS. Consol EBITDA margin 16.4% Q1FY27 vs 16.3% Q4FY26 (flat, +9bps) and 20.4% Q1FY26 (-402bps YoY). Covered in A3-02. This is the primary thesis tripwire and it did not expand.
2. **Organic constant-currency ex-M&A revenue growth** — NOT DISCLOSED in the results filing. Consol revenue +39.7% YoY includes acquired entities (Cake, Trilogy, MJL, BioPharm, Warn, Addressable Health all in Annexure I). Organic/cc split not isolable → A4 concall question.
3. **OCF/PAT, receivables/unbilled vs revenue, cash conversion** — NOT DISCLOSED. No cash-flow statement or balance sheet in this Reg 33 quarterly filing → deferred to half-year/AR; A4 concall question.
4. **Treasury / non-operating cash deployment / new acquisition** — Consol other income 290 (vs 221 YoY); standalone other income 339 (parent treasury). NO new acquisition disclosed in this quarter's Board Outcome. Monitor.
5. **Goodwill/intangibles & impairment** — No balance sheet; no impairment line (only TCPA exceptional). Rising D&A (+104% YoY) confirms acquired-intangible amortisation build. Goodwill/net-worth check deferred to AR (F11).
6. **TCPA provision status + transfer-pricing/Section 144B matter** — TCPA: Rs.203mn provision, cap Rs.417mn, term sheet signed 25 May 2026, court approval pending (A3-04/A3-05). Transfer-pricing / Section 144B matter: SILENT in this filing → A4 concall question (was on the monitoring spine, not addressed).
7. **Exceptional items / other-income swings / standalone-vs-consolidated PAT gap** — Covered A3-01 (exceptional), A3-03 (S/C PAT gap volatility 9.5%→48.5%), A3-06 (tax).

---

```yaml
stage: A3-forensics
company: "INDGN"
quarter: "Q1FY27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/indgn-q1fy27/work/forensics_results_indgn_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: FINDING
  F3: PASS
  F4: PASS
  F5: PASS
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: PASS
  F10: FINDING
  F11: PASS
  F12: FINDING
  F13: FINDING
  F14: FINDING
  F15: FINDING
  F16: N.A.
  F17: N.A.
findings:
  - {id: "A3-01", check: "F1", line: "229", classification: "FORWARD-SIGNAL", implication: "Exceptional slot dormant but litigation under-provisioned (203 vs 417 cap); IPO 100% utilised, nil future buffer"}
  - {id: "A3-02", check: "F2", line: "216/508", classification: "FORWARD-SIGNAL", implication: "Consol EBITDA margin flat 16.4% and -400bps YoY (primary tripwire fails); parent revenue -7.5% QoQ, growth all subsidiary/offshore"}
  - {id: "A3-03", check: "F2", line: "238/525", classification: "FORWARD-SIGNAL", implication: "Subsidiary PAT contribution swings 9.5%->48.5% QoQ (>5pp of standalone PAT); volatile subsidiary-led earnings"}
  - {id: "A3-04", check: "F6", line: "407-417", classification: "FORWARD-SIGNAL", implication: "Dated commitments: TCPA settlement pending court approval; Rs.542mn dividend pending AGM"}
  - {id: "A3-05", check: "F7", line: "406", classification: "FORWARD-SIGNAL", implication: "Claims-made contingency; provision Rs.203mn vs cap Rs.417mn = up to Rs.214mn residual exceptional exposure"}
  - {id: "A3-06", check: "F8", line: "235", classification: "FORWARD-SIGNAL", implication: "FY26 deferred-tax credit Rs.524mn (~1000bps shield) now reversing; ETR normalization risk"}
  - {id: "A3-07", check: "F10", line: "39", classification: "AMBIGUOUS", implication: "Fresh ESOP allotment approved, size undisclosed; paid-up 479->481; ongoing dilution, quantify at A4"}
  - {id: "A3-08", check: "F12", line: "392", classification: "AMBIGUOUS", implication: "Segment assets/liabilities withheld as onerous; blocks capital-intensity/funding-need read"}
  - {id: "A3-09", check: "F12", line: "351", classification: "FORWARD-SIGNAL", implication: "Others segment loss widening -50->-115; ECS margin 16.9%->16.0% compression"}
  - {id: "A3-10", check: "F13", line: "39", classification: "FORWARD-SIGNAL", implication: "ESOP dilution corporate action; FY26 AGM + Rs.542mn dividend calendar event foreshadowed"}
  - {id: "A3-11", check: "F14", line: "229", classification: "NEUTRAL-FACT", implication: "Exceptional line cross-references nonexistent note 10; actual litigation note is 6; drafting-control data point"}
  - {id: "A3-12", check: "F14", line: "400", classification: "AMBIGUOUS", implication: "Three litigation co-defendants absent from 29-entity Annexure I; drafting/consolidation-scope weakness"}
  - {id: "A3-13", check: "F15", line: "400", classification: "AMBIGUOUS", implication: "Encima/Wincere/Healthcare LLC not in current group list; QoQ diff deferred (no prior list); A4 to ask fate of these entities"}
forward_signals: ["A3-01","A3-02","A3-03","A3-04","A3-05","A3-06","A3-09","A3-10"]
ambiguous: ["A3-07","A3-08","A3-12","A3-13"]
commitments:
  - {commitment: "TCPA settlement formalised into definitive agreement post US court approval", implied_date: "FY27 (court approval pending)", ref: "consol Note 6 line 414", status_word: "underway"}
  - {commitment: "FY26 final dividend Rs.2.25/share (~Rs.542mn) subject to shareholder approval", implied_date: "ensuing AGM ~Aug-Sep 2026", ref: "consol Note 7 line 417 / standalone Note 6 line 610", status_word: "proposed"}
  - {commitment: "Allotment under ESOP Scheme 2020", implied_date: "30 July 2026 board", ref: "Board Outcome agenda item 2 line 39", status_word: "approved"}
  - {commitment: "Rs.2mn residual IPO amount earmarked for office-premises capex", implied_date: "post 29 Jan 2026 board resolution", ref: "consol Note 4 lines 319-320", status_word: "earmarked"}
gate_a3: pass
blank_checks: []
```
