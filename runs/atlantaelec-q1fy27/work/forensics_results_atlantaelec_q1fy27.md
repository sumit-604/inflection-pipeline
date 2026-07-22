# A3 FORENSIC NOTES — Atlanta Electricals Limited (ATLANTAELEC) — Q1 FY27 — DOCTYPE: RESULTS

Inputs read verbatim: A1 extract (`extract_results_atlantaelec_q1fy27.txt`, 481 lines, 9 pages) and A2 ledger (`ledger_results_atlantaelec_q1fy27.md`, 29 line items + 22 auditor paras + 3 entities + 2 agenda items + 6 notes). Every ledger row was read at its cited line before judging. **Ledger reconciliation: 100% (all rows read).** Prior-quarter extract NOT supplied (`PRIOR_LEDGER_PATH` absent) — entity-diff and EoM-diff done in-filing only, gaps flagged for A4.

Doctype rule applied: **F1–F15 apply; F16 and F17 are N.A. (marked so).**

---

## DERIVED METRICS (computed from verified extract lines; cross-referenced to Notion Section 8 checklist)

| Metric | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Source lines |
|---|---|---|---|---|---|
| SA EBITDA (excl. Other Income) | 77.55 | 148.40 | 48.77 | 346.81 | 258–270 |
| **SA EBITDA margin (on Rev from Ops)** | **16.63%** | 19.86% | 15.48% | 18.73% | 258, 263–269 |
| SA PAT | 53.09 | 106.30 | 31.14 | 217.07 | 284 |
| CON PAT | 46.84 | 102.19 | 31.14 | 201.77 | 284 |
| **S-vs-C PAT gap (Rs / % of SA)** | **6.25 / 11.8%** | 4.11 / 3.9% | 0.00 / 0% | 15.30 / 7.1% | 284 |
| SA ETR (tax/PBT) | 24.63% | — | — | — | 277, 280–281 |
| CON ETR (tax/PBT) | 26.33% | — | — | — | 277, 280–281 |

**Margin verdict vs Notion checklist item 3:** SA EBITDA margin Q1FY27 = **16.63%, BELOW the 17% red line**, but **ABOVE the 15% thesis-broken line**. This is the FIRST quarter below 17% (Q4FY26 was 19.86%), so the "below 17% for 2 consecutive quarters" red is **NOT yet triggered** — one more sub-17% quarter would trip it. Reads directly onto the Voltamp sector margin-shock watch (Notion tripwire). FY26 recompute (18.73%) matches the thesis 18.7% baseline, validating the EBITDA definition used.

---

## FINDINGS TABLE

| id | check | ledger row ref | line | verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-F01 | F2 | §4 Sr8 Net Profit | 284 | "Net Profit / (Loss) for the Period … 53.09 … 46.84" | FORWARD-SIGNAL | S-vs-C PAT gap widened 0% (Q1FY26) → 11.8% (Q1FY27), an 11.8 pp jump vs the 5 pp threshold; also +7.9 pp QoQ. Consolidated earnings are being eroded by the subsidiary bloc; the drag scales with the pre-commissioning burn and will reverse (favourably) only when subsidiaries book revenue. Track the gap each quarter as a commissioning proxy. |
| A3-F02 | F2 | §4 Sr1/Sr3 block | 258, 263–269 | "Revenue from Operations … 466.33" / "Total Expenses … 400.28" | FORWARD-SIGNAL | SA EBITDA margin 16.63%, below the 17% Notion red line for the first time (Q4FY26 19.86%). Not yet a 2-quarter red; a second sub-17% quarter trips checklist item 3. Consistent with the Voltamp sector-margin read-through the thesis flagged. Above the 15% thesis-broken line, so thesis intact. |
| A3-F03 | F3 | §3 CON-LRR para 6; §4 Dep/Emp rows | 223–227, 266, 268 | "total revenues of Rs. NIL … total net profit after tax of Rs. (4.40) Crores" | FORWARD-SIGNAL | Subsidiaries are NOT shells: Cost of Materials identical SA=CON (322.46), but CON Depreciation 10.13 vs SA 5.76 (~2x) and CON Employee 12.62 > SA 12.45 — an asset-heavy, staffed cost base with zero booked revenue = pre-commissioning build (maps to Atlanta Trafo 765 kV + AE Components backward integration in thesis). No Going Concern EoM (correct — it is a build, not a cleanup). The (4.40) loss is ~depreciation on idle assets. Revenue inflection at these entities is the swing factor. |
| A3-F04 | F8 | §4 Deferred tax row | 281 | "Deferred … 0.35 … (0.26)" | AMBIGUOUS | CON ETR 26.33% > statutory 25.17% while SA ETR 24.63% < statutory. Subsidiary pretax loss (~Rs 5.0 Cr) generated only ~Rs 0.61 Cr tax benefit (~12%), i.e. subsidiary losses are largely NOT tax-effected → DTA on pre-commissioning losses appears unrecognized. Consolidated ETR stays elevated while subsidiaries burn; unrecognized carry-forward losses could later shield subsidiary profits OR a DTA write-up hits when commissioning becomes probable. A4 question: is DTA being recognized on subsidiary losses, and what is the unrecognized carry-forward? |
| A3-F05 | F9 | §4 Sr9 OCI rows | 288–291 | "Equity Instruments through Other Comprehensive Income … 0.49" | NEUTRAL-FACT | Actuarial remeasurement line is NIL this quarter (booked annually — no assumption-change trigger). But total OCI 0.49 exceeds the FULL FY26 total OCI of 0.02, driven entirely by an FVTOCI equity-instrument markup (Q1FY27 0.49 ≈ full-FY26 equity OCI 0.50). Surfaces that the company carries FVTOCI equity investments with a volatile fair value. Small (0.9% of PAT); verify the holding at the FY26 Annual Report. |
| A3-F06 | F13 | §1 Board Outcome item 2 | 60–63 | "Independent Auditors' Certificate for Utilization of Proceeds of Initial Public Offering (IPO) … placed before the Board" | NEUTRAL-FACT | Only board item beyond the results is the routine Reg-32 IPO-utilization certificate. IPO proceeds 99.5% deployed (398.09 of 400.00; residual 1.91) → CARE Rating monitoring near closure. NO AR approval, AGM notice, dividend, capital-raise or director-appointment resolution present → no near-term governance catalyst foreshadowed and FY26 AR deep-dive not yet schedulable from this filing. |
| A3-F07 | F14 | §6 IPO table row 4 + Total | 410–413, 444 | "Public Issue … 21.31 2.63 21.31 … Total … 2.63 398.09" | AMBIGUOUS | Source-document arithmetic inconsistency (A1 confirms at 800 DPI, not OCR): row 4 "At 30 June 2026" prints 21.31, IDENTICAL to "At 31 March 2026" (21.31) despite 2.63 utilized in-quarter; the printed Total 398.09 requires row 4 = 23.94 to foot. The auditor nonetheless certified "ensuring the arithmetic accuracy of the figures presented" (line 444) and "no material deviation" — an audit-quality/governance data point. A4 question: which figure is authoritative and does residual unutilized 1.91 reconcile? |
| A3-F08 | F14 | §2 SA-LRR para 1 vs §3 CON-LRR para 1 | 99–100, 172 | "30th June, 2025" (SA) vs "for the quarter ended 30th June, 2026" (CON) | NEUTRAL-FACT | Drafting asymmetry: SA LRR para 1 scopes YTD + the 30 Jun 2025 comparative; CON LRR para 1 names only the current quarter. The "30th June, 2025" reference is legitimate as the Q1FY26 comparative but the two reports are worded inconsistently. Individually immaterial; logged cumulatively per F14. |
| A3-F09 | F15 | §3a entity 3 | 211–212 | "Atlanta Trafo Limited (formerly known as BTW Atlanta Transformers India Private Limited)" | FORWARD-SIGNAL | Subsidiary renamed BTW → "Atlanta Trafo Limited" AND converted Private → public "Limited" — disclosed in-filing. This is the 765 kV / BTW-facility entity (thesis trigger T3). Rename + corporate-form conversion often precede integration, ring-fenced fundraising, or a step-up at the entity. No prior ledger to diff other list changes → A4 to compare against Q4FY26 / Q1FY26 consolidation list. |

---

## CHECKLIST SCORECARD (all 17; exactly one status each)

| # | Check | Status | One-line basis |
|---|---|---|---|
| F1 | Zero-value standing line items | **PASS** | All 8 ZERO_STANDING rows explained: Labour-Codes exceptional line (nil Q1FY27; hit Q4FY26 0.11 / FY26 1.24 — standing one-off statutory line, forward exposure noted); Short/Excess tax provision (prior-year true-up line, nil); actuarial remeasurement (annual-only line, nil interim); Paid-up capital & Other Equity (annual-only presentation, nil quarterly); IPO rows 1–3 "During-quarter" nil (fully pre-deployed). None anomalous. |
| F2 | Standalone vs Consolidated decomposition | **FINDING** | A3-F01: S-vs-C PAT gap widened 0%→11.8% YoY (>5 pp). A3-F02: SA EBITDA margin fell to 16.63%, below the 17% red line. Gap decomposes to subsidiary loss (4.40) + eliminated intra-group other income (2.07). |
| F3 | Shell-entity detection | **FINDING** | A3-F03: subsidiaries carry identical materials cost but ~2x depreciation and higher employee cost with Rs NIL revenue = asset-heavy pre-commissioning build, not shells; no GC EoM (correct). |
| F4 | Unaudited contribution ratio | **PASS** | No "Other Matters" para and no component/JV/associate auditor: CON-LRR para 6 states all subsidiaries were "reviewed by us" (principal auditor PSCA & Co). Rs 0 / 0% of consolidated PAT rests on unreviewed numbers. |
| F5 | Going Concern / EoM scope tracking | **PASS** | Neither SA-LRR nor CON-LRR contains any Emphasis of Matter or Going Concern language; both conclusions unmodified/clean (SA-LRR para 4 line 133; CON-LRR para 5 line 214). No prior quarter supplied; nothing to diff. |
| F6 | Forward-commitment phrase mining (notes) | **PASS** | Notes 1–5 are IND-AS/Audit-Committee/single-segment/balancing-figure boilerplate. Only "will be"/"commenc" hits are administrative ("will also be made available on the Company's website", line 63; meeting "commenced at 11:00 am", line 65). No dateable operational commitment (results filing carries no MD&A). |
| F7 | Hedge phrase mining | **PASS** | No hedge lexicon in the notes; "to the extent applicable" (line 198) and the IPO-certificate use-restriction language (lines 462–465) are standard legal boilerplate. No newly-added hedge on revenue lumpiness or customer concentration. |
| F8 | Tax forensics | **FINDING** | A3-F04: CON ETR 26.33% > statutory 25.17% (SA 24.63% < statutory); subsidiary losses under-tax-effected (deferred (0.26) CON vs 0.35 SA) → unrecognized DTA signal. "Short/Excess provision of tax" (earlier-years adj) is NIL in Q1FY27 (was 0.14 Q4 / 3.92 FY26). |
| F9 | OCI forensics | **FINDING** | A3-F05: actuarial line nil (no assumption-change trigger), but total OCI 0.49 exceeds full FY26 (0.02) via an equity-instrument FVTOCI markup; small, verify holding at AR. |
| F10 | Share count and dilution | **PASS** | EPS reported as a single "Basic and Diluted" line (6.90 SA / 6.09 CON) — zero basic-vs-diluted spread → no dilutive instruments evident. Paid-up capital 15.38 (annual only, Rs 2 FV → 7.69 Cr shares; 53.09/6.90 ≈ 7.69 Cr, ties). No corporate action within the quarters shown. |
| F11 | Reserves and net-worth tie-out | **PASS** | Other Equity annual-only: SA 929.13 / CON 913.81; +Paid-up 15.38 → SA NW 944.51 / CON NW 929.19; SA-CON gap 15.32 consistent with subsidiary accumulated losses. No third-party net-worth figure in the filing to reconcile against (CARE monitoring cert carries no NW number). |
| F12 | Segment forensics | **PASS** | Note 3: "only one reportable segment" — no segment asset/liability table exists in this filing. The de-facto "assets with zero revenue" signal (subsidiaries) is captured under F2/F3. |
| F13 | Board outcome beyond the results | **FINDING** | A3-F06: sole additional board item is the routine Reg-32 IPO-utilization certificate (proceeds 99.5% deployed); no AR/AGM/dividend/capital-raise/director resolution → no near-term catalyst foreshadowed. |
| F14 | Note-drafting inconsistencies | **FINDING** | A3-F07: IPO table row 4 fails to foot (21.31 unchanged despite 2.63 utilized; Total 398.09 implies 23.94) yet auditor certified "arithmetic accuracy". A3-F08: SA vs CON LRR comparative-period wording asymmetry. Note-vs-letter language consistent (all "unaudited"/"review", no "audit" mislabel). |
| F15 | Entity-list diffs | **FINDING** | A3-F09: Atlanta Trafo Limited disclosed in-filing as renamed from BTW Atlanta Transformers India Pvt Ltd + Pvt→Ltd conversion (the 765 kV entity). No prior ledger to diff remaining changes → A4 cross-check vs Q4FY26/Q1FY26 list. |
| F16 | Presentation-specific (dropped/reframed) | **N.A.** | Doctype = results, not a presentation deck. |
| F17 | Concall-specific (silence audit) | **N.A.** | Doctype = results, no transcript. Notion checklist cross-reference performed in the Derived Metrics section (margin item 3, S-vs-C/CFO context item 4, SBPDCL item 8 untouched by this filing). |

Status tally: PASS 8 (F1,F4,F5,F6,F7,F10,F11,F12) · FINDING 7 (F2,F3,F8,F9,F13,F14,F15) · N.A. 2 (F16,F17) = 17. No blanks. **GATE A3: PASS.**

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/ref | status word |
|---|---|---|---|
| Financial Results + LRR to be uploaded to www.aetrafo.com | on/around 21 Jul 2026 | Board Outcome item 1, line 57–58 | initiated |
| IPO Utilization Certificate to be made available on Company website | on/around 21 Jul 2026 | Board Outcome item 2, line 63 | initiated |
| Audit Committee review of results | 21 Jul 2026 (done) | Note 2, line 306 | completed |

No substantive operational or capex commitments (order book, 400/765 kV timelines, AE Components capex) appear in this results filing — those live in the concall/MD&A, not here. Register is administrative only. Notion checklist items 1, 2, 5, 6, 7, 8, 9 are UNADDRESSED by this document (expected for a bare results filing) and pass to A4/A5 and the Role-5 promise-vs-delivery tracker.

---

## NOTES FOR A4

- **Escalate to management questions (AMBIGUOUS):** A3-F04 (DTA recognition on subsidiary losses / unrecognized carry-forward) and A3-F07 (IPO row-4 arithmetic that the auditor certified as arithmetically accurate).
- **Forward signals to weight:** A3-F01 (widening S-vs-C gap as commissioning proxy), A3-F02 (margin at 16.63%, one quarter from the 2-quarter <17% red; Voltamp read-through), A3-F03 (subsidiary pre-commissioning burn), A3-F09 (Atlanta Trafo rename/conversion = 765 kV entity restructuring).
- **Thesis-trigger status from this filing:** margin 16.63% is above the 15% thesis-broken line (intact); no 400/765 kV quality failure and no new debarment disclosed here (SBPDCL not referenced in this doctype — item 8 remains open for the concall).

```yaml
stage: A3-forensics
company: "atlantaelec"
quarter: "q1fy27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/atlantaelec-q1fy27/work/forensics_results_atlantaelec_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: PASS
  F2: FINDING
  F3: FINDING
  F4: PASS
  F5: PASS
  F6: PASS
  F7: PASS
  F8: FINDING
  F9: FINDING
  F10: PASS
  F11: PASS
  F12: PASS
  F13: FINDING
  F14: FINDING
  F15: FINDING
  F16: N.A.
  F17: N.A.
findings:
  - {id: "A3-F01", check: "F2", line: "284", classification: "FORWARD-SIGNAL", implication: "S-vs-C PAT gap widened 0%->11.8% YoY (>5pp); subsidiary drag scales with pre-commissioning burn"}
  - {id: "A3-F02", check: "F2", line: "258,263-269", classification: "FORWARD-SIGNAL", implication: "SA EBITDA margin 16.63% below 17% red line, first sub-17% quarter; one more trips checklist item 3"}
  - {id: "A3-F03", check: "F3", line: "223-227,266,268", classification: "FORWARD-SIGNAL", implication: "Subsidiaries asset-heavy pre-commissioning build (2x depreciation, zero revenue), not shells"}
  - {id: "A3-F04", check: "F8", line: "281", classification: "AMBIGUOUS", implication: "CON ETR 26.33% > statutory; subsidiary losses under-tax-effected, DTA likely unrecognized"}
  - {id: "A3-F05", check: "F9", line: "288-291", classification: "NEUTRAL-FACT", implication: "Total OCI 0.49 > full FY26 0.02 via equity-instrument FVTOCI markup; verify holding at AR"}
  - {id: "A3-F06", check: "F13", line: "60-63", classification: "NEUTRAL-FACT", implication: "Board item 2 = routine IPO-utilization cert; proceeds 99.5% deployed; no AR/AGM/director catalyst"}
  - {id: "A3-F07", check: "F14", line: "410-413,444", classification: "AMBIGUOUS", implication: "IPO row-4 fails to foot (21.31 vs required 23.94) yet auditor certified arithmetic accuracy"}
  - {id: "A3-F08", check: "F14", line: "99-100,172", classification: "NEUTRAL-FACT", implication: "SA vs CON LRR comparative-period wording asymmetry; immaterial, logged cumulatively"}
  - {id: "A3-F09", check: "F15", line: "211-212", classification: "FORWARD-SIGNAL", implication: "Atlanta Trafo Ltd rename + Pvt->Ltd conversion (765 kV entity); precede integration/fundraise/step-up"}
forward_signals: ["A3-F01", "A3-F02", "A3-F03", "A3-F09"]
ambiguous: ["A3-F04", "A3-F07"]
commitments:
  - {commitment: "Results + LRR uploaded to www.aetrafo.com", implied_date: "2026-07-21", ref: "line 57-58", status_word: "initiated"}
  - {commitment: "IPO Utilization Certificate made available on website", implied_date: "2026-07-21", ref: "line 63", status_word: "initiated"}
  - {commitment: "Audit Committee review of results", implied_date: "2026-07-21", ref: "Note 2 line 306", status_word: "completed"}
gate_a3: pass
blank_checks: []
```
