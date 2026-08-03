# A3 FORENSIC NOTES — Sambhv Steel Tubes Ltd (SAMBHV) — Q1 FY27 — Doctype: RESULTS

Source extract: `extract_results_sambhv_q1fy27.txt` (11 pages, 1944 lines, unit = INR Millions).
Reconciliation contract: `ledger_results_sambhv_q1fy27.md` (115 ledger rows). Every row read at its
cited line before judging. Ledger reconciled: 115/115 = 100%.
Prior-quarter extract: NONE (first pipeline run). Verbatim EoM/entity diffs (F5, F15) not computable
this cycle; Limited Review Reports treated as this-quarter baseline, stated inline.

Doctype applicability: F1-F15 apply; F16 (presentation) and F17 (concall) are N.A.

Conservative bias applied: uncertain-direction findings lean bear and are routed to A4 as management
questions (flagged FORWARD-SIGNAL or AMBIGUOUS below).

---

## OCR RESOLUTION (A2 hand-off, resolved by cross-foot)

A2 flagged the Mar-31-2026 (Q4 FY26) **consolidated** "Total expenses" cell as reconciling two ways
(6,047.92 vs 6,147.95) with "Other expenses" possibly misread (163.66 / 663.66 / 763.66). Cross-footing
the printed column at lines 1369-1425 against the printed PBT row (1431):

`5,126.52 + 82.00 + (401.32) + 359.67 + 97.23 + 120.16 + Other = Total exp; Total income 6,891.98 − Total exp = PBT 744.03`

Only **Other expenses = 763.66 → Total expenses = 6,147.92** foots to the printed PBT (6,891.98 − 6,147.92
= 744.06 ≈ 744.03, 3-paise component rounding). The "663.66 / 6,047.92" clean-pass value is the OCR misread.
This is a **Q4 FY26 comparative, not the current quarter** — no impact on Q1 FY27 numbers. Logged under F14.

---

## FINDINGS TABLE

| id | check | ledger row ref | line / slide | short verbatim quote | classification | forward implication |
|----|-------|----------------|--------------|----------------------|----------------|---------------------|
| FIND-01 | F2 | T5 r13 / r21; T4 r19 | 1437-1438; 1501-1505; 602-605 | "IV. Exceptional item … 3510" (consol Q4/FY26; standalone nil) | AMBIGUOUS | Consol PAT sits BELOW standalone (565.23 vs 566.12 in Q1FY27); S-vs-C PAT gap swings from +1.41% (Q1FY26) to −4.42% (Q4FY26), a 5.83pp swing > 5pp threshold, driven by an unexplained consol-only exceptional Rs 35.10mn carried in NO note. |
| FIND-02 | F3 | T5 r4,r5,r6,r7; T8 r3 | 1369-1397; 1156-1161 | "Sambhv Tubes Limited (Formerly … Sambhv Tubes Private Limited)" | AMBIGUOUS | COGS (5,292.75), Purchases (72.67), Changes (−164.04), Employee benefits (375.21) are IDENTICAL standalone vs consolidated every period → subsidiary has no materials/no employees = operationally dormant shell; renamed Private→"Limited". A clean wholly-owned shell is a candidate vehicle to hold the Kesda build. |
| FIND-03 | F6 | T2 r3,r5,r6 | 51-55; 100-108 | "board has approved the following… 8MW Captive… Solar Power Plant… Phase I – FY 2028; Phase II –FY 2029" | FORWARD-SIGNAL | New capex commitment (up to Rs 250mn) with dated milestones FY2028/FY2029; ties the "captive power cost savings" thesis pillar. Promise-vs-delivery tracker: Phase I due FY2028. IPO proceeds separately reported "fully utilised as of June 30, 2026" (Note 3) = completed milestone. |
| FIND-04 | F7 | T2 r5,r6,r7 | 104-110 | "Subject to Project implementation schedule" / "Upto ₹250 million" / "as may be deemed fit" | AMBIGUOUS | Pre-emptive slippage/cost cover attached to the solar capex at announcement; leans bear on timeline confidence → A4 question. |
| FIND-05 | F8 | T4 r16; T5 r18,r19 | 584-586; 1478-1489 | "(b) Current tax on earlier year … 2.58 / (0.01)" | NEUTRAL-FACT | Non-zero earlier-year tax adjustment (Q1FY26 2.58; Q4FY26 (0.01)) per F8 rule; immaterial (<0.6% of tax). Q1FY27 ETR 26.36% standalone / 26.46% consol > statutory 25.17% (no DTA shield). Deferred tax is a PERSISTENT CHARGE (20.99/27.09/20.22) = DTL building = capex proxy, mild forward signal of continued fixed-asset addition. |
| FIND-06 | F9 | T4 r20; T5 r22 | 619; 1515 | "Remeasurement gains / (losses) on the defined benefit plans (23.53)" | FORWARD-SIGNAL | Single-quarter Q1FY27 remeasurement loss (23.53) vs FULL prior year FY26 gain +0.95 → ~24x magnitude, sign flipped. Signals an actuarial assumption change (discount-rate cut / plan-asset revaluation) = rising gratuity/DBO liability. Verify assumptions at FY27 Annual Report. |
| FIND-07 | F10 | T4 r24,r26,r27 | 649-651; 670-677 | "Basic (In INR) 1.92 … Diluted (In INR) 1.92" (spread nil) | FORWARD-SIGNAL | Paid-up jump 2,410.02→2,946.71 traces to IPO (Note 3, fresh issue Rs 4,400mn). Diluted=Basic (nil spread) NOW, but 86,95,400 convertible warrants at Rs 115 (~Rs 99.99 Cr) approved 15-Jul-2026 (post 30-Jun quarter-end, PRE-signing 03-Aug) are NOT disclosed anywhere in this filing (no subsequent-events note exists). Incoming dilution + a material-event disclosure gap. |
| FIND-08 | F13 | T1 r4; T3 r3; T1 r5 | 58-64; 130-134; 65-68 | "appointed as an Additional Director … with effect from May 09, 2026" vs "cessation shall be effective from May 08, 2026" | FORWARD-SIGNAL | Two unreconciled dates (May 08 vs May 09) for a self-described "simultaneous" appointment/cessation. Appointee Bikash Agrawal (DIN 09231728, CSO & ED) is a warrant allottee (6 of 7 allottees are own management). Additional Director must be regularised at the 9th AGM (10-Sep-2026), which likely carries the warrant/capital enabling resolutions = funding round confirmation over the Kesda commissioning window. |
| FIND-09 | F14 | T6 r2,r7,r10; T3 r6; T5 r11 | 795; 1777; 1860; 141; 1418-1425 | Standalone Note 2 marker printed "*" not "2"; Annexure B row label "6s" | NEUTRAL-FACT | Cumulative drafting/label anomalies (note markers "*", "[=]", "we"; row "6s") mostly OCR twin-pass artifacts; the load-bearing item is the substantive May08/09 date inconsistency (see FIND-08). Q4FY26 consol Total-expenses OCR resolved by cross-foot to 6,147.92 (Other exp 763.66), comparative only. |

---

## CHECKLIST SCORECARD (all 17; each PASS / FINDING / N.A.)

| # | Check | Status | One-line basis |
|---|-------|--------|----------------|
| F1 | Zero-value standing line items | PASS | All 6 ZERO_STANDING lines benign template lines: NCI attribution nil across all 3 rows (lines 1559-60/1571-72/1584-85) confirms 100%-owned single subsidiary; Share-of-equity-investees nil bar (0.01) in Q1FY26 (line 1457) = dormant associate; standalone Exceptional nil (562-564); Annexure A "Existing Capacity Nil" (96) = new project. Consol-only exceptional handled under F2. |
| F2 | Standalone vs consolidated decomposition | FINDING | FIND-01: consol PAT < standalone; S-vs-C PAT gap swing 5.83pp (Q1FY26 +1.41% → Q4FY26 −4.42%); unexplained Rs 35.10mn consol-only exceptional with no note. |
| F3 | Shell-entity detection | FINDING | FIND-02: identical COGS/Purchases/Changes/Employee S-vs-C every period = subsidiary operationally dormant; no Going Concern EoM present, so this is structure not distress. |
| F4 | Unaudited contribution ratio | PASS | No "Other Matters" para in either review report (Table 7); single subsidiary reviewed within scope by same auditor (S S Kothari Mehta); 0% of consol PAT rests on component-auditor / unreviewed numbers. |
| F5 | Going concern / EoM scope tracking | PASS | Both review reports carry unmodified conclusions, NO Emphasis-of-Matter / Going-Concern language (lines 326-355, 1187-1235). No prior-quarter extract → verbatim diff not computable; baseline established this quarter. |
| F6 | Forward-commitment phrase mining | FINDING | FIND-03: solar Phase I FY2028 / Phase II FY2029 (board-approved); AGM notice "will be circulated … in due course" (67); IPO proceeds "fully utilised as of June 30, 2026" (completed). See Commitment Register. |
| F7 | Hedge phrase mining | FINDING | FIND-04: "subject to project implementation schedule" + "upto ₹250 million" + "as may be deemed fit" — pre-emptive timeline/cost cover on the solar capex. Financial Notes 1-5 carry no new revenue/concentration hedge. |
| F8 | Tax forensics | FINDING | FIND-05: non-zero earlier-year tax adjustment (2.58 Q1FY26; (0.01) Q4FY26); Q1FY27 ETR ~26.4% above statutory 25.17%; persistent deferred-tax CHARGE = DTL build (capex proxy), no DTA shield. |
| F9 | OCI forensics | FINDING | FIND-06: Q1FY27 remeasurement loss (23.53) exceeds FULL FY26 (+0.95) by ~24x with sign flip = actuarial assumption change; verify at AR. |
| F10 | Share count and dilution | FINDING | FIND-07: paid-up jump = IPO; diluted EPS spread nil now, but 86,95,400 warrants at Rs 115 (approved 15-Jul-2026, post quarter-end) undisclosed in filing = incoming dilution + disclosure gap. |
| F11 | Reserves and net worth tie-out | PASS | Standalone Other Equity 7,607.58 + Paid-up 2,946.71 = 10,554.29mn ties; consol 7,589.36 + 2,946.71 = 10,536.07mn; consol < standalone by 18.22mn (0.24%) explained by subsidiary cumulative loss/consolidation adj; no third-party rating number in context to gap-test. Warrant money Rs 99.99 Cr not yet in equity (post quarter-end). |
| F12 | Segment forensics | PASS | Note 5 (lines 865-866 / 1860-1867): single operating segment (steel products, India); no segment asset/liability table exists to trend. Note: single-segment reporting gives no line-of-sight into the Kesda pre-commissioning build. |
| F13 | Board outcome beyond the results | FINDING | FIND-08: director-appointment date discrepancy May08/May09; Bikash Agrawal (warrant allottee) regularisation at 9th AGM 10-Sep-2026; AGM likely carries warrant enabling resolutions. No AR/Board's-Report approval in this filing (no AR-deep-dive trigger yet). |
| F14 | Note drafting inconsistencies | FINDING | FIND-09: note-marker/label anomalies (mostly OCR); substantive May08/09 date inconsistency; note text and auditor letter agree ("limited review", not "audit") — consistent. Q4 consol Total-expenses OCR resolved to 6,147.92. |
| F15 | Entity list diffs | PASS | No prior-quarter ledger → diff not computable (first run). Baseline: Holding + 1 subsidiary (Sambhv Tubes Ltd, formerly Sambhv Tubes Private Ltd). Subsidiary Private→"Limited" rename noted as a forward watch (routed via FIND-02); formally no diffable change this cycle. |
| F16 | Presentation: dropped/reframed disclosures | N.A. | Doctype = results filing, not a presentation deck. |
| F17 | Concall: silence audit | N.A. | Doctype = results filing, not a concall transcript. |

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note / ref | status word |
|------------|--------------|-----------|-------------|
| 8MW captive solar Phase I (up to 3.2 MW), Kuthrel | FY2028 | Annexure A, lines 100-106 | initiated (board-approved) |
| 8MW captive solar Phase II (up to 4.8 MW) | FY2029 | Annexure A, lines 100-106 | initiated (board-approved) |
| Solar plant financing (internal accruals / debt / lease) | FY2028-FY2029 | Annexure A, line 109 | intended |
| 9th AGM via VC/OAVM | 10-Sep-2026 | Board Outcome item (e), lines 65-68 | approved / scheduled |
| AGM notice circulation to members | before 10-Sep-2026 ("in due course") | line 67 | pending |
| Bikash Agrawal director appointment (Additional Director) | w.e.f. 09-May-2026 (regularisation at AGM) | item (d)/Annexure B, lines 58-64,130-134 | completed (appointed) / pending regularisation |
| IPO net-proceeds utilisation (Rs 4,400mn) | as of 30-Jun-2026 | Note 3, lines 802-853 / 1802-1842 | completed (fully utilised, nil unutilised) |

---

## ROUTED TO A4 (management questions)

FORWARD-SIGNAL: FIND-03 (solar capex milestones vs Kesda window), FIND-06 (gratuity/discount-rate
assumption change), FIND-07 (undisclosed Rs 99.99 Cr warrant issue + incoming dilution), FIND-08
(director date discrepancy + insider warrant concentration + AGM enabling resolutions).

AMBIGUOUS: FIND-01 (nature of the Rs 35.10mn consol-only exceptional + S/C gap swing), FIND-02
(operational role of dormant subsidiary Sambhv Tubes Ltd / Kesda vehicle), FIND-04 (solar timeline
confidence given "subject to implementation schedule").

---

## RECONCILIATION STATEMENT

115 of 115 A2 ledger rows read verbatim at their cited extract lines (Tables 1-9). Count-test categories
(agenda 7, annexure 14, notes 14, line_items 62, zero_standing 6, auditor_paras 10, entities 3, signature
5) all traced. A2 OCR_AMBIGUOUS resolved by cross-foot (Q4FY26 consol Total exp = 6,147.92). A2
DATE_DISCREPANCY confirmed and elevated to FIND-08. A2 EXCEPTIONAL_ITEM_DIVERGENCE confirmed and
elevated to FIND-01. GATE A3: every check F1-F17 carries exactly one status; no blanks.

```yaml
stage: A3-forensics
company: "SAMBHV"
quarter: "Q1 FY27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/sambhv-q1fy27/work/forensics_results_sambhv_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: PASS
  F2: FINDING
  F3: FINDING
  F4: PASS
  F5: PASS
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: FINDING
  F10: FINDING
  F11: PASS
  F12: PASS
  F13: FINDING
  F14: FINDING
  F15: PASS
  F16: N.A.
  F17: N.A.
findings:
  - {id: "FIND-01", check: "F2", line: "1437-1438;1501-1505;602-605", classification: "AMBIGUOUS", implication: "Consol PAT below standalone; S/C PAT gap swings 5.83pp; unexplained Rs 35.10mn consol-only exceptional carried in no note"}
  - {id: "FIND-02", check: "F3", line: "1369-1397;1156-1161", classification: "AMBIGUOUS", implication: "Identical COGS/Purchases/Changes/Employee S-vs-C = subsidiary operationally dormant shell; renamed Private->Limited; candidate Kesda build vehicle"}
  - {id: "FIND-03", check: "F6", line: "51-55;100-108", classification: "FORWARD-SIGNAL", implication: "8MW solar capex up to Rs 250mn; Phase I FY2028 / Phase II FY2029 dated milestones; captive-power thesis pillar"}
  - {id: "FIND-04", check: "F7", line: "104-110", classification: "AMBIGUOUS", implication: "Pre-emptive slippage/cost cover on solar capex (subject to implementation schedule; upto Rs 250mn)"}
  - {id: "FIND-05", check: "F8", line: "584-586;1478-1489", classification: "NEUTRAL-FACT", implication: "Non-zero earlier-year tax adj (immaterial); ETR 26.4% above statutory; persistent deferred-tax charge = DTL build / capex proxy"}
  - {id: "FIND-06", check: "F9", line: "619;1515", classification: "FORWARD-SIGNAL", implication: "Q1FY27 remeasurement loss (23.53) exceeds full FY26 (+0.95) ~24x with sign flip = actuarial assumption change; verify at AR"}
  - {id: "FIND-07", check: "F10", line: "649-651;670-677", classification: "FORWARD-SIGNAL", implication: "86,95,400 warrants at Rs 115 (~Rs 99.99 Cr) approved 15-Jul-2026 undisclosed in filing; incoming dilution + disclosure gap"}
  - {id: "FIND-08", check: "F13", line: "58-64;130-134;65-68", classification: "FORWARD-SIGNAL", implication: "Director date discrepancy May08/May09; warrant allottee Bikash Agrawal; 9th AGM 10-Sep-2026 likely carries warrant enabling resolutions"}
  - {id: "FIND-09", check: "F14", line: "795;1777;1860;141;1418-1425", classification: "NEUTRAL-FACT", implication: "Note-label anomalies (mostly OCR) plus substantive May08/09 date inconsistency; Q4 consol Total-exp OCR resolved to 6,147.92"}
forward_signals: ["FIND-03", "FIND-06", "FIND-07", "FIND-08"]
ambiguous: ["FIND-01", "FIND-02", "FIND-04"]
commitments:
  - {commitment: "8MW captive solar Phase I (up to 3.2 MW), Kuthrel", implied_date: "FY2028", ref: "Annexure A L100-106", status_word: "initiated"}
  - {commitment: "8MW captive solar Phase II (up to 4.8 MW)", implied_date: "FY2029", ref: "Annexure A L100-106", status_word: "initiated"}
  - {commitment: "Solar plant financing (internal accruals/debt/lease)", implied_date: "FY2028-FY2029", ref: "Annexure A L109", status_word: "intended"}
  - {commitment: "9th AGM via VC/OAVM", implied_date: "2026-09-10", ref: "Board Outcome item e L65-68", status_word: "approved"}
  - {commitment: "AGM notice circulation to members", implied_date: "before 2026-09-10", ref: "L67", status_word: "pending"}
  - {commitment: "Bikash Agrawal director appointment", implied_date: "2026-05-09 (regularisation at AGM)", ref: "item d/Annexure B L58-64,130-134", status_word: "completed"}
  - {commitment: "IPO net-proceeds utilisation Rs 4,400mn", implied_date: "2026-06-30", ref: "Note 3 L802-853/1802-1842", status_word: "completed"}
gate_a3: pass
blank_checks: []
```
