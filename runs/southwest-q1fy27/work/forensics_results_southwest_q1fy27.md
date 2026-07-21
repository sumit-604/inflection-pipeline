# A3 FORENSIC NOTES — SOUTHWEST (South West Pinnacle Exploration Ltd) — Q1 FY27 — doctype: results (4-page investor/press release, NOT Reg 33)

Source extract: `extract_results_southwest_q1fy27.txt` (pressrelease_southwest_q1fy27.pdf, 4 pp).
A2 ledger: `ledger_results_southwest_q1fy27.md` — 70 rows (categories A-L). All 70 read at cited lines. Reconciliation: 100%.
Prior-quarter extract: none (first quarterly run for this ticker) — no EoM / entity diff possible.

DOCTYPE GOVERNING NOTE: This is a press release, not a "Statement of Unaudited Financial Results." It structurally lacks a standalone results column, numbered notes, an auditor's limited-review report, a Board Outcome letter, a cash-flow statement, a balance sheet, and a segment schedule (ledger Category K, 15 absent Reg-33 unit classes, K1-K15). Every check that requires those units is marked N.A. with reason "source absent from this doc (press release only; Reg 33 filing not provided)" — not left blank, and no numbers imported from memory to fill them.

---

## FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|----|-------|----------------|------|----------------------|----------------|---------------------|
| F6-01 | F6 | E9/F8/G6, E12/F9/G7, F6, E5, E13 | 98-99, 108-111, 135, 143-148, 160-169 | "GR preparation and submission is on the anvil ... shall be undertaken now on fast track mode"; "company has ordered new rigs and other equipments"; "commences operations to execute single largest order value of Rs. 307 Cr" | FORWARD-SIGNAL | Multiple dated/dateable management commitments (coal-block GR submission, post-GR mine development, Oman JV2 GR, new-rig capex, Rs 307 Cr Rajasthan execution). Feeds Role 5 promise-vs-delivery tracker as the FY27 baseline — no prior quarter to score status transitions against. |
| F10-01 | F10 | E10 | 105-106 | "Balance 75% amount of warrants, issued on preferential basis received and converted into equity shares" | FORWARD-SIGNAL | Warrant overhang stated fully cleared (final 75% converted → 100%), but NO share count, paid-up capital, or basic/diluted EPS disclosed anywhere (ledger K8). EPS base has stepped up; quantum unquantifiable from this doc. Question for A4: post-conversion share count and diluted EPS base. |
| F14-01 | F14 | B5 / D0b (`TITLE_LABEL_MISMATCH`) | 43-44 vs 74 | cover: "Grows 53% **Q on Q**"; headline: "Grows 53% **Y on Y**" | AMBIGUOUS | Same 53% revenue and 287% PAT growth labelled "Q on Q" in the exchange cover letter but "Y on Y" everywhere in the release body (E1-E4, F1). Growth basis is internally contradictory; if the true basis is Y on Y, the cover overstates sequential momentum. Lean bear → A4 question on the correct growth basis and the actual QoQ trajectory. |
| F14-02 | F14 | G3/G7/L1, L2, J2 | 111 vs 168, 168-169, 204 | "Alara Resources **Ltd, Australia**" vs "Alara Resources **LLC., Oman**"; Oman "second JV" (unnamed); CFO phone "+91 124 423540" | NEUTRAL-FACT | Entity-name inconsistency (Alara "Ltd, Australia" vs "LLC., Oman" — parent vs JV vehicle unclear), the Oman JV2 never given a proper name across all 4 pages, and a CFO phone digit-count mismatch vs letterhead (9 vs 10 digits). Individually immaterial; cumulatively a drafting-quality/governance data point. A4: confirm Alara relationship structure. |
| F17-01 | F17 | Category K + monitoring checklist | doc-wide | (silence — see table below) | CONFIRMATORY-NEGATIVE | Press release is SILENT on the decisive Aug-concall metric (CFO / operating cash flow, CFO/PAT), receivable/debtor days, segment liabilities movement, and the standalone-vs-consolidated PAT gap (asserted "on similar lines" at line 120 but with zero figures). Per Role 5, silence on a decisive/watched metric is a confirmatory negative. Consecutive quarters of silence = 1 (baseline). |

Supporting (checked, not scored as findings): E11 line 107 "Zero (0) LTIs" is the sole `ZERO_STANDING` row and is an operational safety metric, not a hidden financial transaction-class line (F1 basis). E3 line 96 PBT "8% to 19%" appears only in a bullet with no tabulated PBT line (noted under F14, immaterial).

---

## CHECKLIST SCORECARD (all 17; one status each)

| Check | Status | One-line basis |
|-------|--------|----------------|
| F1 ZERO-VALUE STANDING LINE ITEMS | PASS | Sole `ZERO_STANDING` row is E11 (line 107, "Zero (0) LTIs") — operational safety metric, not a financial template line; financial table D1-D5 has no zero/nil/dash line (D6). No hidden exceptional/subsidiary-sale/impairment line exists because there is no Reg-33 results table. |
| F2 STANDALONE vs CONSOLIDATED DECOMPOSITION | N.A. | Source absent from this doc (press release only; Reg 33 filing not provided). Table is consolidated-only ("* On Consolidated Basis," line 91, K5); standalone appears once, unquoted/unanchored, line 120. No S-vs-C gap computable. |
| F3 SHELL-ENTITY DETECTION | N.A. | Source absent (Reg 33 not provided). No standalone cost lines (Cost of Materials / Employee Benefits / Depreciation absent, K9-K11) to compare against consolidated; shell test not computable. |
| F4 UNAUDITED CONTRIBUTION RATIO | N.A. | Source absent (Reg 33 not provided). No auditor Other Matters / limited-review report (K4); unaudited-JV % of consolidated PAT not computable. |
| F5 GOING CONCERN / EoM SCOPE TRACKING | N.A. | Source absent (Reg 33 not provided). No auditor report / EoM paragraph (K4); and no prior-quarter extract to verbatim-diff against. |
| F6 FORWARD-COMMITMENT PHRASE MINING | FINDING | F6-01. Lexicon hits present and extracted: "is underway"/"presently underway," "will be undertaken," "shall be undertaken," "has been completed"/"have since been completed," "commences," "in progress," "upon submission," "fast track." See Commitment Register. |
| F7 HEDGE PHRASE MINING | PASS | Only generic Safe Harbor boilerplate present: "subject to numerous risks and uncertainties" / "may differ materially" (lines 185-186, I1). No newly-added note-level hedge on revenue lumpiness or customer concentration (RIL). Nothing pre-emptive beyond standard disclaimer. |
| F8 TAX FORENSICS | N.A. | Source absent (Reg 33 not provided). No tax-expense line, no deferred-tax, no ETR derivable (K12); PAT given without tax bridge. |
| F9 OCI FORENSICS | N.A. | Source absent (Reg 33 not provided). No OCI / actuarial / Total Comprehensive Income line (K13). |
| F10 SHARE COUNT AND DILUTION | FINDING | F10-01. Warrant conversion completed (E10, lines 105-106) but no share count / paid-up capital / basic-vs-diluted EPS disclosed (K8). Dilution event confirmed, quantum absent. |
| F11 RESERVES AND NET WORTH TIE-OUT | N.A. | Source absent (Reg 33 not provided). No balance sheet / Other Equity / paid-up capital (K7); net-worth tie-out not computable. |
| F12 SEGMENT FORENSICS | N.A. | Source absent (Reg 33 not provided). No segment schedule — no segment assets/liabilities/revenue disclosed. |
| F13 BOARD OUTCOME BEYOND THE RESULTS | N.A. | Source absent (Reg 33 not provided). No Board Outcome letter / AGM / dividend / director / AR-approval items (K2, K15); this is a press-release cover letter only. |
| F14 NOTE DRAFTING INCONSISTENCIES | FINDING | F14-01 (Q-on-Q vs Y-on-Y `TITLE_LABEL_MISMATCH`, cover line 43-44 vs headline line 74) and F14-02 (Alara entity-name inconsistency; unnamed Oman JV2; CFO phone digit-count). |
| F15 ENTITY LIST DIFFS | N.A. | No prior-quarter ledger/extract (first quarterly run) — no consolidation list to diff; and no formal Reg-33 consolidation schedule exists in this doc anyway (K14). Baseline entity list noted (Category L) for future diffs. |
| F16 PRESENTATION-SPECIFIC: DROPPED/REFRAMED | N.A. | Doctype is a results press release, not an investor presentation, and there is no prior-quarter baseline to detect dropped metrics or reframed baselines. (The one cross-deck-style reframing, Q-on-Q vs Y-on-Y, is scored under F14-01.) |
| F17 CONCALL-SPECIFIC: SILENCE AUDIT | FINDING | F17-01. Repurposed per task as a silence audit of this press release against the Notion monitoring checklist. Silent on CFO/OCF, receivable days, segment liabilities, standalone PAT gap, RIL concentration, order-book conversion pace. See table below. |

Scorecard tally: PASS 3 (F1, F7), plus... correction below. FINDING 4 (F6, F10, F14, F17). N.A. 10 (F2, F3, F4, F5, F8, F9, F11, F12, F13, F15, F16). PASS 3 (F1, F7). Total 17. No blanks (GATE A3: pass).

Wait-check: PASS = F1, F7 → 2. Recount: FINDING {F6,F10,F14,F17}=4; N.A. {F2,F3,F4,F5,F8,F9,F11,F12,F13,F15,F16}=11; PASS {F1,F7}=2. 4+11+2 = 17. Correct.

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/line ref | status word |
|------------|--------------|---------------|-------------|
| Jharkhand coal-block exploration | completed this quarter | E9 (104), F8 (143), G6 (160) | completed |
| Jharkhand definitive GR preparation & submission | near-term; "on the anvil" / "presently underway" (no explicit date in doc; thesis tracks targeted end-July 2026) | E9 (104), F8 (143-144), G6 (163) | underway |
| Post-GR mine development activities (Jharkhand) | after GR submission; "on fast track mode" (undated) | F8 (144-145), G6 (163-164) | initiated (contingent on GR submission) |
| Rajasthan single-largest order Rs 307 Cr execution | in-progress; "commences operations to execute" | E5 (98-99) | underway |
| RIL CBM contract extension Rs 166 Cr | won this quarter | E6 (100) | completed |
| Oman JV2 airborne survey | recently completed | E12 (108), F9 (147) | completed |
| Oman JV2 GR preparation | near-term; "on cards" (undated) | E12 (108-109), F9 (148) | underway |
| New rigs & equipment ordered (capex) | undated; no amount/count/delivery date | F6 (134-136) | initiated (ordered) |
| Participation in Alara Resources Ltd Rights issue | "ongoing" | E13 (110-111) | underway |
| OIL empanelment (2D/3D seismic) | granted this quarter | E8 (102-103) | completed |
| Warrant conversion (balance 75%) into equity | completed this quarter | E10 (105-106) | completed |

---

## F17 SILENCE AUDIT — "What Was NOT Discussed" (vs Notion monitoring checklist)

| checklist item | addressed? | consecutive quarters silent | note |
|----------------|-----------|------------------------------|------|
| CFO / operating cash flow, CFO/PAT ratio | NO | 1 (baseline) | Decisive Aug-concall metric. CFO Dinesh Agarwal named as contact (201) but zero cash-flow disclosure (K6). CONFIRMATORY-NEGATIVE. |
| HZL Rs 307 Cr Rajasthan order — revenue recognition / segment rev >Rs 15 Cr | PARTIAL | — | Order named ("commences operations to execute," E5, line 98) but no recognised-revenue or segment figure. |
| Receivable / debtor days / WC cycle | NO | 1 (baseline) | Silent. Active tripwire (bull <=175, bear >200); unmeasurable here. |
| Segment liabilities movement | NO | 1 (baseline) | Silent; no segment schedule (F12 N.A.). Prior print fell Rs 14.65 Cr QoQ — WC-unwind vs debt-reduction ambiguity unresolved. |
| Coal-block GR submission (targeted end-July 2026) & mine timeline | PARTIAL | — | GR "on the anvil"/"underway" (F8, G6) but no explicit end-July date; FY29 mine timeline not addressed. |
| RIL / Reliance CBM extension Rs 166 Cr & customer concentration | PARTIAL | — | Extension win disclosed (E6, Rs 166 Cr); customer-concentration risk not addressed. |
| Oman two JVs (Alara LLC; JV2 airborne/GR) | YES | — | Both covered (G7, H2); JV2 remains unnamed (F14-02). |
| Order-book Rs 761 Cr conversion into revenue | PARTIAL | — | Order book stated at "all time high 761 Crores" (E7, F4) but conversion pace/schedule not addressed. |
| Accreditation (1 of 21 accredited coal+lignite agencies) | PARTIAL | — | "accredited prospecting agency" stated (line 158-159); the "1 of 21" scarcity framing / Growth Trigger 4 not quantified. |
| Warrant conversion (balance 75%) | YES | — | Disclosed (E10); no share-count quantum (F10-01). |
| Standalone vs consolidated PAT gap; unaudited-JV share of consolidated PAT | NO | 1 (baseline) | Asserted "standalone performance is also on similar lines" (line 120) with zero figures; unquantifiable (K5, F2 N.A.). |

---

## RECONCILIATION SUMMARY
All 70 A2 ledger rows (A1; B1-B6; C1; D0a-D0d, D1-D6; E1-E13; F1-F9; G1-G7; H1-H3; I1; J1-J2; K1-K15; L1-L2) read at their cited extract lines and judged. Ledger reconciled: 100%. GATE A3: pass (no blank checks).

```yaml
stage: A3-forensics
company: "SOUTHWEST"
quarter: "Q1 FY27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/southwest-q1fy27/work/forensics_results_southwest_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: PASS
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: PASS
  F8: N.A.
  F9: N.A.
  F10: FINDING
  F11: N.A.
  F12: N.A.
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: N.A.
  F17: FINDING
findings:
  - {id: "F6-01", check: "F6", line: "98-99,108-111,135,143-148,160-169", classification: "FORWARD-SIGNAL", implication: "Dated/dateable commitments: Jharkhand GR submission, post-GR mine dev, Oman JV2 GR, new-rig capex, Rs 307 Cr Rajasthan execution; FY27 promise-vs-delivery baseline."}
  - {id: "F10-01", check: "F10", line: "105-106", classification: "FORWARD-SIGNAL", implication: "Warrant overhang fully cleared (final 75% converted) but no share count/paid-up/EPS disclosed; EPS base stepped up, quantum unknown -> A4 question."}
  - {id: "F14-01", check: "F14", line: "43-44 vs 74", classification: "AMBIGUOUS", implication: "Cover letter labels growth 'Q on Q'; release body labels same 53%/287% 'Y on Y'. Basis contradiction; if truly Y on Y, cover overstates sequential momentum -> A4 question."}
  - {id: "F14-02", check: "F14", line: "111 vs 168, 168-169, 204", classification: "NEUTRAL-FACT", implication: "Alara 'Ltd, Australia' vs 'LLC., Oman' name inconsistency; Oman JV2 unnamed across doc; CFO phone digit-count mismatch. Drafting-quality/governance data point -> A4 confirm Alara structure."}
  - {id: "F17-01", check: "F17", line: "doc-wide (K1-K15; line 120)", classification: "CONFIRMATORY-NEGATIVE", implication: "Silent on decisive CFO/OCF & CFO/PAT, receivable days, segment liabilities, standalone-vs-consolidated PAT gap, RIL concentration, order-book conversion pace. Silence on watched/decisive metrics = confirmatory negative; baseline quarter (count=1)."}
forward_signals: ["F6-01", "F10-01"]
ambiguous: ["F14-01"]
commitments:
  - {commitment: "Jharkhand definitive GR preparation & submission", implied_date: "near-term (on the anvil/underway; no explicit date; thesis tracks end-July 2026)", ref: "F8/G6 lines 143-144,163", status_word: "underway"}
  - {commitment: "Post-GR Jharkhand mine development (fast track)", implied_date: "after GR submission (undated)", ref: "F8/G6 lines 144-145,163-164", status_word: "initiated"}
  - {commitment: "Rajasthan Rs 307 Cr order execution", implied_date: "in-progress from Q1 FY27", ref: "E5 line 98-99", status_word: "underway"}
  - {commitment: "Oman JV2 GR preparation", implied_date: "near-term (on cards; undated)", ref: "E12/F9 lines 108-109,148", status_word: "underway"}
  - {commitment: "New rigs & equipment ordered (capex)", implied_date: "undated; no amount/count", ref: "F6 lines 134-136", status_word: "initiated"}
  - {commitment: "Participation in Alara Resources Rights issue", implied_date: "ongoing", ref: "E13 lines 110-111", status_word: "underway"}
  - {commitment: "Warrant conversion (balance 75%) into equity", implied_date: "completed this quarter", ref: "E10 lines 105-106", status_word: "completed"}
  - {commitment: "RIL CBM contract extension Rs 166 Cr", implied_date: "won this quarter", ref: "E6 line 100", status_word: "completed"}
  - {commitment: "Oman JV2 airborne survey", implied_date: "recently completed", ref: "E12/F9 lines 108,147", status_word: "completed"}
  - {commitment: "OIL empanelment (2D/3D seismic)", implied_date: "granted this quarter", ref: "E8 lines 102-103", status_word: "completed"}
gate_a3: pass
blank_checks: []
```
