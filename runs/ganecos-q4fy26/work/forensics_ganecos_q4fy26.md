# A3 FORENSIC NOTES — GANECOS Q4FY26 (doctype: results / CORRIGENDUM re-filing)

Document: Corrigendum (dated July 30, 2026) to the Audited Standalone + Consolidated
Financial Results for the quarter and year ended March 31, 2026 (originally filed May 21, 2026).
Corrects the Consolidated Trade Payables split (micro/small 130.04; other creditors 8,601.45;
TOTAL unchanged 8,731.49). Unit: Rs. Lakh (x0.01 -> Cr).

Ledger reconciliation: all 240 line items + 24 notes + 6 corrigendum items + 4 entities + 6
signature blocks + 2 auditor paras read verbatim at their cited lines. Reconciled 100%.
The corrigendum is treated as a first-class forensic subject (F1, F11, F14).

Engaged A2 flags: ILLEGIBLE_VALUE (4 -> all NOT FOUND, never estimated), CORRIGENDUM_CORRECTED
(2 consol trade-payable sub-lines), SIGNATURE_DATE_RETAINED, AUDITOR_REPORT_NOT_INCLUDED,
ENTITY_LIST_NOT_PROVIDED, NOT_A_BOARD_OUTCOME_LETTER, TIMING_NOT_DISCLOSED, OCR_ARTIFACT.

---

## FINDINGS TABLE

| id | check | ledger row ref | line | verbatim quote (short) | classification | forward implication |
|----|-------|----------------|------|------------------------|----------------|---------------------|
| A3-01 | F1 | Consol BS "Assets held for sale/disposal" (Tbl5) / SA BS (Tbl8) | 226, 471 | "Assets held for sale/ disEosal ... 23 .97" | FORWARD-SIGNAL | New held-for-sale line at both levels (nil PY) = a disposal decision taken; expect a small asset sale + gain/cash in FY27. Ask what asset. |
| A3-02 | F2 | Consol "Profit for the period" 124-125 vs SA 379 | 124, 379 | consol FY26 "3,821.35" vs SA FY26 "4,783.24" | FORWARD-SIGNAL | Consolidated PAT is BELOW standalone in FY26 (-961.89) and Q3FY26 (474.84 vs 1,594.29). Subsidiaries (Ecopet/Ecotech) are net loss-making / pre-breakeven — inverts FY25 where consol led standalone. Directly hits monitorable #3. |
| A3-03 | F4 | Consol Note 4 auditor para; associate line 119 | 158, 119 | "issued an unmodified opinion thereon"; "Share of (loss)... of an associate ... (4.49)" | AMBIGUOUS | Full auditor report / Other Matters NOT in extract (AUDITOR_REPORT_NOT_INCLUDED); unaudited-component % unverifiable. Only visible equity-method item is associate loss (4.49) FY26 = immaterial. A4: obtain auditor report + component-auditor split. |
| A3-04 | F6 | SA Notes 6-9 / Consol Note 6 | 162, 405, 407 | "subject to the approval of members ... at the forthcoming Annual General Meeting"; "has made an investment of Rs. 320.00 crore ... 'Ganesha Ecopet'" | FORWARD-SIGNAL | Dividend recommended pending AGM (amount ILLEGIBLE / NOT FOUND — cannot confirm the 3.50 cut, monitorable #7). Rs320cr + Rs90cr CCPS injected into WOS subs this quarter = subsidiary capex funding (monitorable #4). |
| A3-05 | F8 | Consol Deferred tax 123; SA Deferred tax 378 | 123, 378 | consol "(2) Deferred tax ... (216.27)"; SA "(126.89)" | AMBIGUOUS | Deferred tax swung to a credit FY26 (consol -216.27, ~400bps shield) from a charge FY25 (+701.90). Consol ETR 29.2% >> SA 25.8% because subsidiary losses carry no tax benefit. A4: are DTAs being recognised on Ecopet/Ecotech losses? ETR step-up risk on breakeven. |
| A3-06 | F9 | Consol OCI "financial instrument (Equity)" 137; SA 383 | 137, 383 | "Re-measurement loss on financial instrument (Equity) ... (759.82)" | AMBIGUOUS | FVTOCI equity-investment markdown FY26 (759.82) exceeds full prior year (450.23) — a ~7.6cr unrealised loss recurring at both levels. Verify the instrument and impairment risk at the Annual Report. |
| A3-07 | F10 | Paid-up capital 145/388; Issue proceeds 320/563 | 145, 320 | "Paid-up equity share capital ... 2,679.60 ... 2,545.70"; "Proceeds from issue of share capital ... 10,393.28" | FORWARD-SIGNAL | Paid-up +133.90 lakh (+5.3%) traces to a ~Rs103.93cr equity issue in FY26 (dilution occurred). Relevant to monitorable #4 (capex/dilution after Odisha greenfield dropped). Basic-vs-diluted spread narrowed FY25->FY26 (0.85->0.02 consol) = fewer/exercised options. |
| A3-08 | F11 | Consol Total equity 234; SA Total equity 478; Consol current Borrowings 245 | 234, 478 | consol "Total equity 1,27,567.10" vs SA "Total eauitv 129,720.72" | FORWARD-SIGNAL | Tie-out exact at both levels, but consolidated net worth is BELOW standalone by 2,153.62 lakh = subsidiaries' aggregate net assets sit ~21.5cr under their Rs769cr carrying cost (accumulated deficit) despite Rs410cr fresh CCPS. Corroborates A3-02. NOTE: consol current Borrowings (L245) is ILLEGIBLE / NOT FOUND — consol net debt not computable from this filing. |
| A3-09 | F13 | Consol Note 6 / SA Note 9 | 162, 411 | "at the forthcoming Annual General Meeting ... for the financial year 2025-26" | FORWARD-SIGNAL | Forthcoming AGM referenced -> AGM notice + record date + dividend/special resolutions incoming; audited FY results filed -> full Annual Report drops within weeks (schedule Role 6 AR Deep Dive). No director term dates disclosed. |
| A3-10 | F14 | Corrigendum letter 63; corrected BS 247-248; sig date 270; unit mix 405/409 | 63, 247 | "the above correction pertains solely to clerical error and does not impact the audited figures" | AMBIGUOUS | Corrigendum reclassifies Rs56.53 lakh between MSME and non-MSME creditors (247 130.04 / 248 8,601.45) — MSMED-classification changes carry interest/disclosure consequence, not purely "clerical". Financial-statement signatures retain May 21 2026 date (L270) though the consolidated BS figures changed (SIGNATURE_DATE_RETAINED); 70-day gap to catch. Unit mix in notes (Rs320.00 crore L405 vs Rs49.00 Lakh L409). A4 governance questions. |

---

## CHECKLIST SCORECARD (all 17, one status each)

| Check | Status | Basis (one line) |
|-------|--------|------------------|
| F1 ZERO-VALUE STANDING | FINDING | 24 ZERO_STANDING rows read; most pure template, but new "Assets held for sale/disposal" 23.97 (L226/471) = disposal decision taken. See A3-01. |
| F2 STANDALONE vs CONSOLIDATED | FINDING | Consol PAT below standalone FY26 (3,821.35 vs 4,783.24) and Q3 — inverts FY25; >50pp swing in gap %. See A3-02. |
| F3 SHELL-ENTITY | PASS | Consol cost lines materially exceed standalone (CoM 24,411 vs 16,873 L107/364; Emp 2,693 vs 1,993; Dep 1,716 vs 721) — subsidiaries are genuinely operating, not shells; no going-concern EoM. |
| F4 UNAUDITED CONTRIBUTION | FINDING | Auditor Other Matters absent (AUDITOR_REPORT_NOT_INCLUDED, L158); ratio unverifiable; associate pickup (4.49) L119 immaterial. See A3-03. |
| F5 GOING CONCERN / EoM | PASS | Note 4 records an unmodified opinion (L158-159/400-401); no EoM or going-concern paragraph present; nothing to diff. |
| F6 FORWARD-COMMITMENT MINING | FINDING | "forthcoming AGM" dividend (L162/411, amount NOT FOUND); Rs320cr/Rs90cr CCPS "has made" (L405/407). See A3-04 + Commitment Register. |
| F7 HEDGE PHRASE MINING | PASS | Only boilerplate "subject to the approval of members" dividend hedges (L162/411); no new business-risk hedge (revenue lumpiness / customer concentration) added to notes. |
| F8 TAX FORENSICS | FINDING | Deferred-tax credit FY26 (consol -216.27 L123, SA -126.89 L378) vs charge FY25; consol ETR 29.2% >> SA 25.8%; no "earlier years" adjustment. See A3-05. |
| F9 OCI FORENSICS | FINDING | FVTOCI equity re-measurement loss FY26 (759.82 L137/383) exceeds full FY25 (450.23); defined-benefit swing explained by Labour Code plan amendment (Note 7/10). See A3-06. |
| F10 SHARE COUNT / DILUTION | FINDING | Paid-up 2,545.70->2,679.60 (L145/388) traces to Rs103.93cr equity issue (L320/563); basic-diluted spread narrowed. See A3-07. |
| F11 RESERVES / NET WORTH TIE-OUT | FINDING | Tie-out exact both levels; consol net worth < standalone by 2,153.62 (L234 vs L478) = subsidiary erosion; consol current borrowings NOT FOUND (L245). See A3-08. |
| F12 SEGMENT FORENSICS | N.A. | Note 5 both statements: "no reportable segments as per Ind-AS 108" (L160-161/403-404); single-segment manufacturer, no segment tables. |
| F13 BOARD OUTCOME BEYOND RESULTS | FINDING | Forthcoming AGM + dividend approval pending (L162/411) -> AGM notice/record date + AR deep-dive incoming. See A3-09. |
| F14 NOTE DRAFTING INCONSISTENCIES | FINDING | Corrigendum "clerical" label on MSME/non-MSME reclass; signature date retained on changed figures; crore/lakh unit mix. See A3-10. |
| F15 ENTITY LIST DIFFS | N.A. | ENTITY_LIST_NOT_PROVIDED — no consolidation schedule in this filing and no prior-quarter extract supplied (ledger L437-448); diff not runnable. Ecopet/Ecotech (WOS), Ganesha Recycling Chain (Associate) named incidentally only. |
| F16 PRESENTATION-SPECIFIC | N.A. | Doctype is a results filing, not a presentation deck. |
| F17 CONCALL SILENCE AUDIT | N.A. | Doctype is a results filing, not a concall transcript; no F6 transcript cross-ref possible. Notion monitorables instead surfaced against the financials in A3-02/04/05/06/07/09. |

Status count: 10 FINDING / 3 PASS / 4 N.A. (17 total, no blanks — GATE A3 pass).

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/ref | status word |
|------------|--------------|----------|-------------|
| Dividend recommended for FY2025-26 (per-share amount ILLEGIBLE / NOT FOUND) | forthcoming AGM (~Aug-Sep 2026) | Consol Note 6 (L162), SA Note 9 (L411) | recommended (pending member approval) |
| CCPS subscription Rs.320.00 crore into Ganesha Ecopet Pvt Ltd (WOS) | during Q4FY26 (done) | SA Note 6 (L405-406) | completed ("has made") |
| CCPS subscription Rs.90.00 crore into Ganesha Ecotech Pvt Ltd (WOS) | during Q4FY26 (done) | SA Note 7 (L407-408) | completed ("has made") |
| Equity subscription Rs.49.00 lakh into Ganesha Recycling Chain Pvt Ltd (Associate) | during Q4FY26 (done) | SA Note 8 (L409-410) | completed ("has made") |
| Revised (corrected) financial results hosted on company website | at re-filing (July 30, 2026) | Corrigendum letter (L70) | underway/completed ("is being hosted") |

---

## NOT FOUND REGISTER (4 ILLEGIBLE_VALUE — never estimated)

| item | line | consequence |
|------|------|-------------|
| Consol dividend per share (Note 6) | 162 | Cannot confirm FY26 payout / the 3.50 cut (monitorable #7). |
| Standalone dividend per share (Note 9) | 411 | Same. |
| Consol FY25 "Profit for the period" total ("10,3~") | 125 | Prior-year consol PAT imprecise -> FY25 S-vs-C gap % only approximate for A3-02. |
| Consol current Borrowings, Mar-26 | 245 | Consolidated net debt not computable from this filing (A3-08). |

---

## FORWARD-SIGNAL and AMBIGUOUS findings routed to A4

FORWARD-SIGNAL: A3-01 (F1), A3-02 (F2), A3-04 (F6), A3-07 (F10), A3-08 (F11), A3-09 (F13).
AMBIGUOUS: A3-03 (F4), A3-05 (F8), A3-06 (F9), A3-10 (F14).

```yaml
stage: A3-forensics
company: "GANECOS"
quarter: "q4fy26"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/ganecos-q4fy26/work/forensics_ganecos_q4fy26.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: FINDING
  F3: PASS
  F4: FINDING
  F5: PASS
  F6: FINDING
  F7: PASS
  F8: FINDING
  F9: FINDING
  F10: FINDING
  F11: FINDING
  F12: N.A.
  F13: FINDING
  F14: FINDING
  F15: N.A.
  F16: N.A.
  F17: N.A.
findings:
  - {id: "A3-01", check: "F1", line: "226,471", classification: "FORWARD-SIGNAL", implication: "New assets-held-for-sale line both levels = disposal decision taken; FY27 sale/gain."}
  - {id: "A3-02", check: "F2", line: "124,379", classification: "FORWARD-SIGNAL", implication: "Consol PAT below standalone FY26 & Q3 = subsidiaries pre-breakeven (monitorable #3)."}
  - {id: "A3-03", check: "F4", line: "158,119", classification: "AMBIGUOUS", implication: "Auditor Other Matters absent; unaudited-component % unverifiable; obtain report."}
  - {id: "A3-04", check: "F6", line: "162,405", classification: "FORWARD-SIGNAL", implication: "Dividend pending AGM (amount NOT FOUND); Rs410cr CCPS into WOS subs (monitorable #4/#7)."}
  - {id: "A3-05", check: "F8", line: "123,378", classification: "AMBIGUOUS", implication: "Deferred-tax credit + consol ETR 29.2%>SA; DTA on subsidiary losses? ETR step-up risk."}
  - {id: "A3-06", check: "F9", line: "137,383", classification: "AMBIGUOUS", implication: "FVTOCI equity markdown FY26 759.82 > full FY25 450.23; impairment risk, verify at AR."}
  - {id: "A3-07", check: "F10", line: "145,320", classification: "FORWARD-SIGNAL", implication: "Paid-up +5.3% via ~Rs103.93cr equity issue = FY26 dilution (monitorable #4)."}
  - {id: "A3-08", check: "F11", line: "234,478", classification: "FORWARD-SIGNAL", implication: "Consol net worth < standalone by 2,153.62 = subsidiary deficit; consol current borrowings NOT FOUND."}
  - {id: "A3-09", check: "F13", line: "162,411", classification: "FORWARD-SIGNAL", implication: "Forthcoming AGM + dividend resolution + full Annual Report incoming; schedule AR deep-dive."}
  - {id: "A3-10", check: "F14", line: "63,247", classification: "AMBIGUOUS", implication: "'Clerical' MSME/non-MSME reclass Rs56.53L; signatures retain May-21 date on changed figures."}
forward_signals: ["A3-01", "A3-02", "A3-04", "A3-07", "A3-08", "A3-09"]
ambiguous: ["A3-03", "A3-05", "A3-06", "A3-10"]
commitments:
  - {commitment: "FY26 dividend recommended (per-share amount NOT FOUND)", implied_date: "forthcoming AGM ~Aug-Sep 2026", ref: "L162/L411", status_word: "recommended"}
  - {commitment: "CCPS Rs320.00cr into Ganesha Ecopet (WOS)", implied_date: "Q4FY26", ref: "L405-406", status_word: "completed"}
  - {commitment: "CCPS Rs90.00cr into Ganesha Ecotech (WOS)", implied_date: "Q4FY26", ref: "L407-408", status_word: "completed"}
  - {commitment: "Equity Rs49.00L into Ganesha Recycling Chain (Associate)", implied_date: "Q4FY26", ref: "L409-410", status_word: "completed"}
  - {commitment: "Corrected results hosted on company website", implied_date: "2026-07-30", ref: "L70", status_word: "underway"}
gate_a3: pass
blank_checks: []
```
