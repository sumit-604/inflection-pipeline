# A3 FORENSIC NOTES — The Anup Engineering Limited (ANUP) — Q1 FY27 — Doctype: RESULTS

Source extract: `/home/user/inflection-pipeline/runs/anup-q1fy27/work/extract_results_anup_q1fy27.txt`
Reconciliation contract (A2 ledger): `/home/user/inflection-pipeline/runs/anup-q1fy27/work/ledger_results_anup_q1fy27.md`
Prior-quarter extract: none available (F5/F15 verbatim diffs not possible — noted where relied on).
Units: Lakhs as printed (×0.01 → Rs Cr per A1 header L7-8). Ratios computed on printed lakh figures; Cr shown for readability.
Ledger reconciliation: 100% — all 13 notes, 71 line-items, 1 agenda item, 11 auditor paras, 2 entities, 5 signatures read at cited lines before judging.

---

## MATERIAL CONTEXT (enumerated fact, not thesis analysis — flagged so A4/A5 cannot miss it)

This is the master decision-gate quarter. The bare results filing carries the **P&L only — no balance sheet, no cash-flow statement, no segment assets/liabilities**. Therefore of the three thesis-broken triggers, only one (EBITDA margin) is computable from THIS document; **Quarterly CFO and Debtor Days are NOT evaluable here** and must be sourced by A4 from the concall / BSE XBRL / balance sheet. Recorded as a coverage gap, not a finding.

Standalone Q1 FY27 (30.06.2026), cited lines:
- Revenue from operations ₹117.89 Cr (11,789.29 lakh, L158) vs Q1 FY26 ₹169.42 Cr (16,942.21, L158) = **−30.4% YoY**; vs Q4 FY26 ₹194.80 Cr (19,480.07) = **−39.5% QoQ**.
- Operating EBITDA ₹9.42 Cr (941.68 lakh) → **margin 7.99%** vs Q1 FY26 23.24% and Q4 FY26 18.51% — a ~1,525 bps YoY collapse.
- PAT ₹1.108 Cr (110.81 lakh, L182) vs Q1 FY26 ₹25.53 Cr (2,553.14) = **−95.7% YoY**. EPS ₹0.55 (L199) vs ₹12.75.
- The collapse is **operational, not exceptional**: exceptional item is nil this quarter (L174); the ₹130.52 lakh Labour-Codes charge sat in FY26, not Q1 FY27.

Thesis trigger read (enumeration only): **Margin trigger FIRES emphatically at ~8% (<19% hard / <18% red / well below the 17.5-18.5% mid-band).** CFO and DD triggers not computable from this filing.

---

## FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| F2-1 | F2 | 5b row 7 / 5a row 7 | L390, L182 (rev L366/L158) | Consol PAT "57.02" vs Standalone PAT "110.81" | AMBIGUOUS | Subsidiary Mabel Engineers swung to a net loss of ~₹0.54 Cr (−53.79 lakh) this quarter vs +72.96 lakh profit in Q1 FY26 and +264.60 lakh in FY26 — a ~51 pp swing in subsidiary contribution as % of standalone PAT. Mabel revenue actually grew (581→736 lakh) yet turned loss-making; direction unknown → A4 question on whether Mabel's loss is one-off or structural. |
| F6-1 | F6 | 6a Note 4 / 6b Note 4 | L245-246, L452-453 | "will continue to assess the accounting implications basis such developments/ guidance" | FORWARD-SIGNAL | Labour Codes rules still pending notification; management commits to re-assess. A further past-service-cost / employee-benefit charge can recur in a future quarter once rules are finalised — a dateable (rule-notification-triggered) future P&L hit on an already-collapsed margin. |
| F7-1 | F7 | 6a Note 4 / 6b Note 4 | L245-246, L452-453 | "The Company continues to monitor developments on the rules to be notified" | AMBIGUOUS | Newly-added hedge (Labour Codes only notified Nov-2025) pre-emptively covers uncertain future employee-cost. Magnitude undisclosed; lean bear on employee-cost direction → A4 question quantifying expected recurring impact. |
| F8-1 | F8 | 5a rows 6.1-6.3 / 5b rows 6.1-6.3 | L177-180, L385-388 | Standalone Deferred Tax Credit "(30.88)"; Total Tax "10.12" on PBT "120.93" | AMBIGUOUS | Standalone ETR 8.37% vs statutory 25.17%, driven by a deferred-tax credit (30.88 lakh) on a tiny PBT — flatters PAT by ~20 lakh; will not recur at this ratio. Persistent deferred credits (Q1FY27 30.88 / Q4FY26 5.47 / Q1FY26 50.68 / FY26 40.01) = DTA/carryforward pattern → future ETR step-up risk. Consol ETR diverges sharply at 38.98% (Mabel carries a +26.30 deferred-tax charge). → A4 question on deferred-tax composition and normalised ETR. |
| F9-1 | F9 | 5a row 8(iii)/Total / 5b row 8(iii)/Total | L189, L192, L397, L400 | "Remeasurement Income/(loss) of Cash flow hedge reserve 269.14"; Total OCI "224.48" | FORWARD-SIGNAL | Single-quarter total OCI (224.48 lakh) EXCEEDS the full prior-year FY26 OCI (−105.57 std / −97.71 consol). Driver is a cash-flow-hedge-reserve swing of +269.14 lakh (vs −264.42 for all FY26). Signals large open forex/commodity hedge positions that will reclassify into future P&L as underlying orders execute — gives visibility on hedged future revenue but adds P&L volatility. Verify hedge book + assumptions at the Annual Report. |
| F11-1 | F11 | 5a row 10/11 / 5b row 10/11 | L196, L197, L405 | Paid-up "2,003.15"; Other Equity (consol) "67,097.50" | NEUTRAL-FACT | Net worth ties out cleanly: consol Other Equity 67,097.50 + paid-up 2,003.15 = 69,100.65 lakh = **₹691.01 Cr**, matching Notion baseline ₹691.0 Cr to <0.01%. BUT paid-up capital ₹20.03 Cr / face ₹10 = **2.003 Cr shares**, conflicting with the Notion baseline's "~1.89 Cr shares" (~6% gap). Filing figure governs; per-share/valuation base needs correcting → route to A4. |

---

## CHECKLIST SCORECARD (all 17 — none blank; GATE A3)

| Check | Status | One-line basis |
|---|---|---|
| F1 ZERO-VALUE STANDING LINES | PASS | Only true ZERO_STANDING row is Note 5 "Nil equity shares...under the Employees Stock Option Scheme" (L247-249 std / L454-455 consol) — a standing ESOP-dilution disclosure, nil in Q1FY27/Q4FY26/Q1FY26 (5,000 issued FY26); addressed in F10. Exceptional-item (L174) and excess-tax-provision (L178) lines carry values in some periods (Labour-Codes / earlier-year adjustment), so not nil-standing. No profit-on-sale-of-subsidiary/investments/impairment/discontinued-ops template lines present. |
| F2 STANDALONE vs CONSOLIDATED | **FINDING** | F2-1: Mabel subsidiary swung to a −53.79 lakh net loss (consol PAT 57.02 < standalone 110.81), a ~51 pp swing vs Q1FY26 as % of standalone PAT — exceeds the 5 pp trigger. |
| F3 SHELL-ENTITY DETECTION | PASS | Cost lines differ standalone vs consolidated — Mabel carries own materials (Δ680.95 lakh), employees (Δ149.13), depreciation (Δ16.31), finance (Δ18.41) and ₹7.36 Cr own revenue (L366 vs L158). Real operations, not a shell. No going-concern EoM to reconcile. |
| F4 UNAUDITED CONTRIBUTION | PASS | Consolidated review report (L295-350) has NO Other Matters paragraph; same firm (Sorab S. Engineer & Co.) signs both standalone and consolidated for a single wholly-owned subsidiary. Nothing disclosed as unreviewed → 0% unaudited contribution to quantify. Interpretive gap noted: report is silent on whether Mabel was independently reviewed vs management-certified (ledger §7) — low-priority A4 note, not a numeric finding. |
| F5 GOING CONCERN / EoM | PASS | No going-concern paragraph and no Emphasis-of-Matter in either report; both conclusions "unmodified" (L113-118, L326-331; Notes L233, L442). No prior extract available → verbatim QoQ EoM diff not possible (coverage gap noted), but nothing present to diff. |
| F6 FORWARD-COMMITMENT MINING | **FINDING** | F6-1: Note 4 "will continue to assess the accounting implications" re Labour Codes — a rule-notification-triggered future commitment (see Commitment Register). |
| F7 HEDGE PHRASE MINING | **FINDING** | F7-1: Note 4 "continues to monitor developments on the rules to be notified" — newly-added pre-emptive hedge about uncertain future employee-benefit cost. |
| F8 TAX FORENSICS | **FINDING** | F8-1: Standalone ETR 8.37% vs statutory 25.17% on persistent deferred-tax credits; consol ETR 38.98% divergent; future ETR step-up risk. |
| F9 OCI FORENSICS | **FINDING** | F9-1: Single-quarter OCI 224.48 lakh exceeds full FY26 OCI (−105.57), driven by a +269.14 cash-flow-hedge-reserve swing — large open hedge positions to reclassify into future P&L. |
| F10 SHARE COUNT & DILUTION | PASS | Paid-up 2,002.65→2,003.15 lakh (L196/L404) traces cleanly to 5,000 ESOP shares (Note 5, L248/L455). Basic=Diluted EPS 0.55/0.55 (L199-200) — spread NIL, narrowed from 0.05 in Q1FY26; no new dilutive instrument. (Absolute share-count vs Notion reconciliation raised under F11-1.) |
| F11 RESERVES / NET WORTH TIE-OUT | **FINDING** | F11-1: Net worth ties out (consol ₹691.01 Cr = Notion ₹691.0 Cr) but paid-up implies 2.003 Cr shares vs Notion ~1.89 Cr (~6% gap) — per-share base to correct. |
| F12 SEGMENT FORENSICS | N.A. | Single operating segment "Engineering Products" (Note 3, L236/L444); no segment assets/liabilities/vertical disclosure in this filing — nothing to trend. |
| F13 BOARD OUTCOME BEYOND RESULTS | PASS | Sole agenda item is approval of Q1 FY27 standalone+consolidated results (L37-41). No AR/Board's-Report approval, no AGM notice/record date, no dividend, no director appointment/resignation, no auditor change, no capital-raising enabling resolution anywhere in the filing (ledger §1). No Role-6 AR event triggered by this document. |
| F14 NOTE DRAFTING INCONSISTENCIES | PASS | Note 2 "unmodified conclusion" matches auditor reports (L233/L442 vs L113-118/L326-331). Entity names consistent ("Mabel Engineers Private Limited" L324). Standalone vs consol exceptional-item difference (130.52 vs 145.26 lakh) is the legitimate Mabel layer (Δ14.74), not a drafting error. Only anomalies are OCR-illegible UDINs (L135/L346) — extraction artifacts, not filing inconsistencies. |
| F15 ENTITY LIST DIFFS | PASS | Disclosed list is coherent: Parent + one wholly-owned subsidiary Mabel Engineers Pvt Ltd (L323-324). No prior-quarter extract → verbatim additions/deletions/rename/relationship diff NOT possible (coverage gap named per ledger §4); no in-document indication of any change. |
| F16 PRESENTATION-SPECIFIC | N.A. | Doctype = results filing; no presentation deck in scope. |
| F17 CONCALL SILENCE AUDIT | N.A. | Doctype = results filing; no transcript in scope. (Note for A4: Notion checklist items 5-9 — order book, services vertical, high-volume mix, cash-conversion commentary, customer-advance recovery — are not disclosed in a bare P&L results filing and must be sourced from the concall/deck.) |

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/turn ref | status word |
|---|---|---|---|
| "will continue to assess the accounting implications" of the Labour Codes (further past-service-cost recognition possible) | Ongoing — triggered by regulator notification of Labour-Code rules (pending as of 06-Aug-2026) | Standalone Note 4 (L245-246); Consolidated Note 4 (L452-453) | underway (monitoring) |

Status note: the initial Labour-Codes past-service cost was already **completed/recognised** in FY26 (₹130.52 lakh std / ₹145.26 lakh consol, Note 4, L242-243/L450-451). The live commitment is the forward re-assessment as rules crystallise — a "recognised → will continue to assess" carry that A5 promise-vs-delivery should track next quarter.

---

## RECONCILIATION & COVERAGE GAPS PASSED TO A4/A5
1. No balance sheet / cash-flow in this filing → thesis triggers CFO (<₹100 Cr) and Debtor Days (>175) NOT computable here; only the margin trigger is (fires at ~8%).
2. No prior-quarter extract → F5 EoM and F15 entity verbatim diffs not evaluable.
3. Both UDINs OCR-illegible (L135, L346) → source re-verification if UDIN validation is material.
4. Consolidated review report silent on Mabel's independent-review scope (no Other Matters para) → confirm if material.
5. Share-count base discrepancy (filing 2.003 Cr vs Notion ~1.89 Cr) → correct per-share/valuation inputs (F11-1).

```yaml
stage: A3-forensics
company: "ANUP"
quarter: "Q1 FY27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/anup-q1fy27/work/forensics_anup_q1fy27_results.md"
ledger_reconciled_pct: 100
checklist:
  F1: PASS
  F2: FINDING
  F3: PASS
  F4: PASS
  F5: PASS
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: FINDING
  F10: PASS
  F11: FINDING
  F12: N.A.
  F13: PASS
  F14: PASS
  F15: PASS
  F16: N.A.
  F17: N.A.
findings:
  - {id: "F2-1", check: "F2", line: "L390/L182", classification: "AMBIGUOUS", implication: "Subsidiary Mabel swung to ~-53.79 lakh net loss (consol PAT 57.02 < standalone 110.81); ~51pp contribution swing vs Q1FY26; one-off vs structural unknown"}
  - {id: "F6-1", check: "F6", line: "L245-246/L452-453", classification: "FORWARD-SIGNAL", implication: "Labour-Codes 'will continue to assess' commitment; further past-service-cost charge can recur on rule notification"}
  - {id: "F7-1", check: "F7", line: "L245-246/L452-453", classification: "AMBIGUOUS", implication: "Newly-added hedge on uncertain future employee-benefit cost; magnitude undisclosed"}
  - {id: "F8-1", check: "F8", line: "L177-180/L385-388", classification: "AMBIGUOUS", implication: "Standalone ETR 8.37% on persistent deferred-tax credits vs consol 38.98%; future ETR step-up risk"}
  - {id: "F9-1", check: "F9", line: "L189/L192/L397/L400", classification: "FORWARD-SIGNAL", implication: "Single-quarter OCI exceeds full FY26; +269.14 cash-flow-hedge swing = large open hedge book reclassifying into future P&L"}
  - {id: "F11-1", check: "F11", line: "L196/L197/L405", classification: "NEUTRAL-FACT", implication: "Net worth ties to Notion 691 Cr; but paid-up implies 2.003 Cr shares vs Notion ~1.89 Cr; correct per-share base"}
forward_signals: ["F6-1", "F9-1"]
ambiguous: ["F2-1", "F7-1", "F8-1"]
commitments:
  - {commitment: "will continue to assess the accounting implications of the Labour Codes (further past-service-cost recognition possible)", implied_date: "ongoing / on regulator rule notification (pending)", ref: "Standalone Note 4 L245-246; Consolidated Note 4 L452-453", status_word: "underway"}
gate_a3: pass
blank_checks: []
```
