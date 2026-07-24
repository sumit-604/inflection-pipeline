# A3 FORENSIC NOTES — Welspun Corp Limited (WELCORP) — Q1FY27 (quarter ended 30 June 2026) — DOCTYPE: results

Source extract: `runs/welcorp-q1fy27/work/extract_results_welcorp_q1fy27.txt` (17 pages, 953 lines, 100% coverage).
Ledger contract: `runs/welcorp-q1fy27/work/ledger_results_welcorp_q1fy27.md`.
Prior-quarter extract: none supplied — retrospective EoM / entity-list diffs could not be run; treated as first-seen baseline.
Ledger reconciliation: 100% — all 7 ledger tables read verbatim at cited lines (3 agenda, 12 auditor paras, 25 entities, 19 notes, 139 line items, 9 zero-standing, 18 annexure rows, 6 signatory blocks). No row unread.

OCR caution honoured (per A2): Note 5 rendered "S" (line 441), split auditor paras 6/7 (lines 141/175), dropped signatory letters, illegible dash tokens (lines 527/843/847/849), entity-16 Sr. No. under seal (line 267). Underlying numerals read directly; OCR glyph damage is NOT counted as a drafting inconsistency under F14.

---

## FINDINGS TABLE

| id | check | ledger row ref | line | verbatim quote | classification | forward implication |
|----|-------|----------------|------|----------------|----------------|---------------------|
| A3-F1 | F1 | 5A r.376 / r.381 | 376, 381 | "Exceptional Items  -  -  -  -" (376); "Profit on sale of shares of associate (refer note 4)  547.93" (381) | AMBIGUOUS | The standing Exceptional Items line sits nil all periods while the Rs547.93 Cr EPIC one-off is routed to a bespoke line above PBT, keeping it out of the "exceptional" bucket. Inflates consol PBT/PAT/NPM (25.68% vs ~12% ex-gain); headline profitability reverts next quarter. Ask A4 why non-exceptional classification. |
| A3-F2 | F2 | 5A r.387 vs 5D r.735; 5A r.360 vs 5D r.707 | 387/735; 360/707 | Consol PAT "1,047.88" vs Standalone PAT "115.84"; Consol rev "4,081.12" vs SA rev "1,567.22" | FORWARD-SIGNAL | Standalone (India parent) PAT fell YoY 254.83→115.84 (-55%) and revenue 1,828.35→1,567.22 (-14%), while consolidated ROSE on the EPIC gain + US subs. C-vs-S PAT gap widened 94→932 Cr YoY (>>5% of SA PAT). Consol masks parent-level softening; ex-one-off consol PAT ~500 Cr. |
| A3-F4 | F4 | Consol LRR paras 6, 7 | 141-185 | "8 Subsidiaries which have not been reviewed... total net loss after tax... of Rs. 39.78 Crores" (175-178); associate EPIC "Rs. 69.88 Crores" (143) | FORWARD-SIGNAL | Gross unreviewed contribution (69.88 + 39.78 + 3.09 = 112.75 Cr) ≈ 10.8% of consol PAT — above 10% threshold. The 8 unreviewed subs run an 85% loss margin (Rs39.78 Cr loss on Rs46.68 Cr revenue), an ~Rs159 Cr/yr loss run-rate parked in unreviewed entities (Sintex + KSA pre-commissioning candidates). No prior period to trend. |
| A3-F6 | F6 | Board Outcome items 2,3; Annexure A/B | 56-70, 50-55, 868-874, 932 | "Upon completion of the aforesaid acquisition... will increase from the existing 23% to 74%" (64-66); "On or before 31 August, 2026" (932) | FORWARD-SIGNAL | Two dated management commitments: (i) WCPGL 51% buy completes by 31 Aug 2026 (Q2FY27) → consolidates a power-gen subsidiary; (ii) new GGBS/slag entity to be incorporated (holding co Slagexcel Pvt Ltd, 26%). Feed promise-vs-delivery tracker. |
| A3-F8 | F8 | 5A r.386 / r.382 / r.385 | 382, 385, 386 | Total tax "159.25" on PBT "1,207.13"; deferred tax "(17.61)" | FORWARD-SIGNAL | Consol ETR 13.2% vs statutory 25.17% — ~12 pt / ~Rs145 Cr shield, driven by the low-taxed EPIC capital gain (via Mauritius) + post-tax associate share. Strip the one-off and ETR is ~27%. ETR steps back up ~12 pts next quarter as the gain rolls off. Also note anomalous Q4FY26 pattern: current-tax credit (85.85) against deferred-tax charge 218.40. |
| A3-F12 | F12 | 5C r.566/572/583/590 | 566, 572, 583, 590 | Others segment result "(137.06)" (572); Others assets "1,446.93" vs liabilities "249.32" | CONFIRMATORY-NEGATIVE | "Others (incl. plastic products)" = Sintex cluster: quarterly loss widened to (137.06) from (18.66) YoY and (134.44) QoQ — a 78% loss margin on Rs175.05 Cr revenue. Segment is an equity-funded, loss-making build (assets 5.8x liabilities). Confirms Sintex RED monitoring item and fires the "FY27 deeper loss" trim trigger. |
| A3-F13 | F13 | Board Outcome item 3 / Annexure B | 56-70, 907-941 | "acquisition of additional 51% equity stake in... (WCPGL) from Welspun Living Limited (WLL), a promoter group Company... Rs. 67.66 Crores" (56-60); "will be executed on an arms' length basis" (918-919) | AMBIGUOUS | RPT: capital of Rs67.66 Cr flows from listed co to promoter group (Welspun Living) for 51% of a captive power co (FY26 turnover Rs109.95 Cr; non-monotonic FY24 138.70/FY25 98.13/FY26 109.95). Implied 100% equity ~Rs132.7 Cr. "Arms' length" asserted but — unlike Note 4b LSAW — NO independent valuation report is cited. Governance / capital-leakage watch; ties to #11 RPT (was AMBER 33.44%). Consolidates from Q2FY27. |
| A3-F14 | F14 | Entities T3; Consol LRR para 1 vs Note 5 | 228, 110, 441 | "Welpun Logistics LLC (USA)" (228); "Welspun Corp Employee Welfare Trust" (110) vs "Employees Welfare Trust" (441) | NEUTRAL-FACT | Genuine (non-OCR) drafting inconsistencies: entity-name misprint "Welpun" and singular/plural "Employee"/"Employees" Welfare Trust between auditor letter and company notes. Individually immaterial; cumulative control-hygiene data point. |
| A3-F15 | F15 | Note 4; Board item 3; entities 18/19 | 435-438, 64-67, 288-295 | "14,17,280 shares of... EPIC... were sold" (435); "WCPGL will become a subsidiary of the Company" (66-67) | FORWARD-SIGNAL | Retrospective diff not possible (no prior list). Prospective consolidation-list changes disclosed: EPIC (assoc) stake cut via sale (to ~22% per monitoring); WCPGL associate→subsidiary pending (23%→74%); new GGBS associate to be incorporated. Next-quarter entity list will change on all three. |

---

## CHECKLIST SCORECARD (all 17)

| Check | Status | One-line basis |
|-------|--------|----------------|
| F1 Zero-standing line items | FINDING | 9 nil template lines are routine, BUT Exceptional Items (376) stands empty while a Rs547.93 Cr one-off is routed to a bespoke line (381) — comparability/inflation issue. |
| F2 Standalone vs Consolidated | FINDING | C-vs-S PAT gap blew out to 932 Cr (vs 94 YoY); standalone parent PAT -55% and revenue -14% YoY while consol rose on one-off — parent softening masked. |
| F3 Shell-entity detection | PASS | Consol cost lines materially exceed standalone across materials (2,331.94 vs 1,129.24), employees (313.63 vs 71.99), depreciation (124.58 vs 40.63) — subsidiaries carry real operations; no going-concern EoM to reconcile. |
| F4 Unaudited contribution ratio | FINDING | Gross unreviewed contribution ≈10.8% of consol PAT (>10%); 8 unreviewed subs at Rs39.78 Cr net loss (~Rs159 Cr/yr loss run-rate). |
| F5 Going concern / EoM scope | PASS | No Going Concern / Emphasis-of-Matter paragraph in either LRR; only routine Other-Matter (unreviewed components; balancing figures). No prior extract to diff, nothing to flag. |
| F6 Forward-commitment phrases | FINDING | Two dated commitments mined: WCPGL close by 31 Aug 2026 ("upon completion... will increase"); GGBS entity "shall be incorporated". |
| F7 Hedge phrase mining | PASS | Only routine deal-conditionality "subject to... approvals" (61, 892, 929); no new revenue-lumpiness or customer-concentration hedge in the notes. |
| F8 Tax forensics | FINDING | Consol ETR 13.2% vs statutory 25.17% (~Rs145 Cr shield) from low-taxed EPIC gain; reverts ~12 pts next quarter; Q4FY26 deferred/current-tax sign anomaly noted. |
| F9 OCI forensics | PASS | Actuarial (not-reclassified) OCI small and stable (consol Q1 Rs1.55 Cr vs FY26 Rs(3.49) Cr); no single-quarter swing exceeding prior year; larger moves sit in forex/hedge reclassifiable bucket. |
| F10 Share count & dilution | PASS | Paid-up stable at Rs131.90 Cr / 26,37,90,645 shares; prior 131.61→131.90 traces to FY26 ESOP (Note 6); no ESOP this quarter; basic-diluted spread negligible (Rs0.03) and not widening. |
| F11 Reserves & net worth tie-out | PASS | Standalone ties exactly (131.90+4,802.13+353.69 = 5,287.72); consol within 2.4% (10,197.49 vs 10,449.45; candidate = NCI/treasury), below 5%. |
| F12 Segment forensics | FINDING | Others/plastics (Sintex) loss widened to (137.06) from (18.66) YoY; equity-funded loss-making build (assets 1,446.93 vs liabilities 249.32); fires trim trigger. |
| F13 Board outcome beyond results | FINDING | WCPGL 51% RPT buy from promoter-group Welspun Living for Rs67.66 Cr, no independent valuation cited; new GGBS entity; no AR/AGM/dividend/director item. |
| F14 Note drafting inconsistencies | FINDING | Non-OCR inconsistencies: "Welpun" misprint (228); "Employee" vs "Employees" Welfare Trust (110 vs 441). Immaterial, cumulative hygiene point. |
| F15 Entity list diffs | FINDING | Retrospective diff impossible (no prior list); prospective changes disclosed — EPIC stake cut, WCPGL assoc→sub, new GGBS associate. |
| F16 Presentation-specific | N.A. | Doctype = results, not a presentation. |
| F17 Concall silence audit | N.A. | Doctype = results; no transcript. Silence audit deferred to the Q1FY27 concall — see note below. |

### F17 deferral note (silence to carry into the concall audit)
This results filing is materially SILENT on several Notion monitoring items; these are flagged for the concall F17 (not scored here):
- #1 KSA LSAW+DI commissioning — AMBER, first production expected THIS quarter (Q1FY27). Filing gives no production/commissioning status; only Note 4b (prior-year LSAW plant sale to the KSA subsidiary) and the loss-making 8-subsidiary pool (F4) hint KSA remains pre-revenue. Red trigger = slip beyond Q4FY27.
- JJM receivables normalization (DELAYED) — not addressed.
- India DI commissioning (FIRED) — not addressed.
- Corporate guarantees >Rs6,000 Cr (new trim trigger) — not disclosed in this filing.
- Promoter pledge — not disclosed (full-exit-in-48h tripwire; verify at concall/shareholding).
- #10 EPIC contribution Rs50+ Cr/qtr (deteriorating, stake cut to ~22%) — this filing confirms the stake sale (Note 4) but not run-rate; EPIC associate share Rs69.88 Cr this quarter is ABOVE the Rs50 Cr floor (before the stake reduction fully bites).

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/ref | status word |
|------------|--------------|----------|-------------|
| Acquire additional 51% of WCPGL from Welspun Living Ltd (promoter group), Rs67.66 Cr; WCPGL 23%→74%, becomes subsidiary | On or before 31 Aug 2026 (Q2FY27) | Board Outcome item 3 (lines 56-70); Annexure B item 6 (line 932) | board-approved (subject to transaction docs + statutory/regulatory approvals) |
| Incorporate new India entity for GGBS / slag-granulation business; 26% stake, Rs26,000; holding co Slagexcel Pvt Ltd | not dated ("once the new entity is incorporated") | Board Outcome item 2 (lines 50-55); Annexure A (lines 868-902) | board-approved (subject to regulatory approvals) |

---

## FLAGGED FOR A4 (convert to management questions)
FORWARD-SIGNAL: A3-F2, A3-F4, A3-F6, A3-F8, A3-F15.
AMBIGUOUS: A3-F1, A3-F13.
Priority A4 questions: (1) WCPGL RPT price fairness — independent valuation for the Rs67.66 Cr promoter-group purchase (F13); (2) Sintex/plastics loss trajectory and funding/write-down plan given the deeper loss and equity-funded build (F12/F4); (3) underlying (ex-EPIC) parent-level revenue/PAT decline (F2); (4) normalized ETR and margin base once the EPIC gain rolls off (F1/F8); (5) KSA commissioning status (F17 deferral) — the loss-making unreviewed-subsidiary pool suggests KSA remains pre-revenue.

---

```yaml
stage: A3-forensics
company: "WELCORP"
quarter: "Q1FY27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/welcorp-q1fy27/work/forensics_results_welcorp_q1fy27.md"
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
  F9: PASS
  F10: PASS
  F11: PASS
  F12: FINDING
  F13: FINDING
  F14: FINDING
  F15: FINDING
  F16: N.A.
  F17: N.A.
findings:
  - {id: "A3-F1", check: "F1", line: "376,381", classification: "AMBIGUOUS", implication: "Exceptional line nil while Rs547.93 Cr EPIC gain routed to bespoke line above PBT; inflates PBT/PAT/NPM, reverts next quarter"}
  - {id: "A3-F2", check: "F2", line: "387,735", classification: "FORWARD-SIGNAL", implication: "Standalone parent PAT -55% and rev -14% YoY while consol rose on one-off; C-vs-S PAT gap 94->932 Cr; parent softening masked"}
  - {id: "A3-F4", check: "F4", line: "175-185", classification: "FORWARD-SIGNAL", implication: "Unreviewed contribution ~10.8% of PAT; 8 unreviewed subs at Rs39.78 Cr net loss (~Rs159 Cr/yr loss run-rate; Sintex/KSA)"}
  - {id: "A3-F6", check: "F6", line: "56-70,932", classification: "FORWARD-SIGNAL", implication: "WCPGL 51% buy closes by 31 Aug 2026 (consolidates power-gen sub); new GGBS entity to be incorporated"}
  - {id: "A3-F8", check: "F8", line: "382,385,386", classification: "FORWARD-SIGNAL", implication: "Consol ETR 13.2% vs 25.17% (~Rs145 Cr shield from low-taxed EPIC gain); ETR steps up ~12 pts as one-off rolls off"}
  - {id: "A3-F12", check: "F12", line: "566,572,583,590", classification: "CONFIRMATORY-NEGATIVE", implication: "Sintex/plastics loss widened to (137.06) from (18.66) YoY; equity-funded loss-making build; fires FY27-deeper-loss trim trigger"}
  - {id: "A3-F13", check: "F13", line: "56-70,907-941", classification: "AMBIGUOUS", implication: "Rs67.66 Cr RPT buy of WCPGL from promoter-group Welspun Living, no independent valuation cited; capital-leakage/governance watch; ties #11 RPT"}
  - {id: "A3-F14", check: "F14", line: "228,110,441", classification: "NEUTRAL-FACT", implication: "Non-OCR drafting inconsistencies (Welpun misprint; Employee/Employees Welfare Trust); cumulative control-hygiene point"}
  - {id: "A3-F15", check: "F15", line: "435-438,64-67", classification: "FORWARD-SIGNAL", implication: "Prospective entity-list changes: EPIC stake cut, WCPGL assoc->sub, new GGBS associate; retrospective diff impossible (no prior list)"}
forward_signals: ["A3-F2", "A3-F4", "A3-F6", "A3-F8", "A3-F15"]
ambiguous: ["A3-F1", "A3-F13"]
commitments:
  - {commitment: "Acquire additional 51% of WCPGL from promoter-group Welspun Living Ltd for Rs67.66 Cr; 23%->74%, becomes subsidiary", implied_date: "on or before 31 Aug 2026", ref: "Board Outcome item 3 (56-70); Annexure B (932)", status_word: "board-approved"}
  - {commitment: "Incorporate new India GGBS/slag entity, 26% stake Rs26,000, holding co Slagexcel Pvt Ltd", implied_date: "undated (pending incorporation)", ref: "Board Outcome item 2 (50-55); Annexure A (868-902)", status_word: "board-approved"}
gate_a3: pass
blank_checks: []
```
