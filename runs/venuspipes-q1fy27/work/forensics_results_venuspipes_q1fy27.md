# A3 FORENSIC NOTES — Venus Pipes & Tubes (VENUSPIPES) — Q1 FY27 (qtr ended Jun 30, 2026) — DOCTYPE: results

Sources read verbatim: A1 extract `extract_results_venuspipes_q1fy27.txt` (230 embedded
lines, every ledger row read at its cited line); A2 ledger `ledger_results_venuspipes_q1fy27.md`.
Prior-quarter extract: **none available** — every check that needs a verbatim prior-quarter
diff (F5, F15) is marked with that limitation, not guessed.

Ledger reconciliation: 100%. All 35 line items, 6 notes, 1 agenda item, 4 auditor paras,
3 signature blocks, 1 entity read at their cited lines. 0 annexures (confirmed).

SCOPE BASIS (governs F2/F3/F4/F15): the filing is a **single, unlabelled (presumptively
standalone/entity-only) results statement**. The strings "consolidated" and "standalone"
do not appear anywhere in the 5-page source (A1 grep = 0 matches); one auditor report,
addressed to Venus Pipes & Tubes Limited alone; no subsidiary/associate/JV disclosure;
Note 4 confirms a single operating segment. The task briefing's "both standalone and
consolidated" description does **not** match the source as supplied (`SCOPE_DISCREPANCY`).
Consequently F2, F3, F4 are N.A. on a no-consolidation basis, and F15 is N.A. (no
consolidation list to diff, and no prior ledger).

DATA-INTEGRITY CARRYOVER (from A1/A2, respected here, never guessed):
- `TEXT_GARBLED_UNRESOLVED`: Revenue from operations Q1FY27 cell "3,20S.37" (line 66) and
  Deferred tax FY26 cell "SS.71" (line 94) are glyph-corrupted and were NOT in A1's OCR
  cross-check pass. Treated as unconfirmed; any ratio using them is flagged.
- `OCR_USED` (confirmed by A1 supplementary pass): Total Income (line 71), Total Expenses
  (line 82), Total Comprehensive Income FY26 (line 109).
- `ILLEGIBLE_UDIN` (line 229-230): auditor UDIN unreadable by text-layer AND OCR; flagged,
  not relied on.
- `NAME_GARBLED` (line 152-161): Director signatory printed name illegible; DIN 00926613 legible.

---

## FINDINGS TABLE

| id | check | ledger row ref | line | verbatim quote | classification | forward implication |
|----|-------|----------------|------|----------------|----------------|---------------------|
| F1-a | F1 | §2 #14 (ZERO_STANDING) | 87 | "ExceDtional Item (Impact of Labour Codes)" | FORWARD-SIGNAL | Line is nil in Q1FY27 and Q1FY26 but carried (1.87) in Q4FY26 and 4.58 for FY26. It exists to absorb the India Labour Codes provisioning estimate. On notification/implementation of the four Labour Codes this line reactivates with a P&L (gratuity/leave/wage-base) hit. Q4FY26's (1.87) was a partial *reversal* of a prior estimate — the number is management-estimated and volatile. Question for A4. |
| F8-a | F8 | §2 #19 Deferred tax | 94 | "Deferred tax   21.28   13.29   12.10" | FORWARD-SIGNAL | Deferred-tax charge (a debit each period, not a credit) rises 12.10 -> 21.28 YoY (+75.9%). Alongside depreciation 52.16 -> 72.16 (+38.3%, line 79) and finance costs 97.90 -> 112.83 (+15.2%, line 78), this is a coherent capex-commissioning cluster: new capacity coming online creates accelerated-depreciation timing differences and a growing DTL. Near-term margin/tax drag; medium-term volume optionality. Not a DTA shield (no persistent credits). |
| F8-b | F8 | §2 #18 & #19 | 93, 94 | "Adjustments of earlier years ... (2.72) ... (10.01)" | NEUTRAL-FACT (+ data-integrity flag) | "Tax adjustments relating to earlier years" is non-zero in the comparative columns (Q4FY26 (2.72), FY26 (10.01)) though nil in Q1FY27 — an earlier-year tax true-up reducing tax, standard Q4/year-end behaviour, low forward weight. FY26 deferred-tax cell "SS.71" is glyph-corrupted and unconfirmed (`TEXT_GARBLED_UNRESOLVED`); do not rely on the FY26 deferred-tax figure downstream. |
| F10-a | F10 | §2 #30 Paid-up capital; #34/#35 EPS | 110, 118-119 | "Paid up equity share capital   207.16 ... 204.92" / "Diluted EPS (Rs.)  12.75 ... 12.08" | AMBIGUOUS | Paid-up capital rose 204.92 -> 207.16 (+2.24 Rs Mn at Rs 10 FV = +224,000 shares) between Q1FY26 and Q4FY26. Concurrently the basic-vs-diluted EPS spread present in Q1FY26 (12.12 vs 12.08 = 0.04) has closed to zero in Q1FY27 (12.75 = 12.75): dilutive instruments (likely ESOP options) appear to have been exercised. NO note in this filing explains the corporate action (grep for ESOP/warrant/option = 0 hits). A4 to source the corporate-action record and any residual option pool. |

Findings flagged for A4 conversion into management questions: **F1-a, F8-a** (FORWARD-SIGNAL); **F10-a** (AMBIGUOUS).

---

## CHECKLIST SCORECARD (all 17, exactly one status each)

| Check | Status | Basis (one line) |
|-------|--------|------------------|
| F1 ZERO-VALUE STANDING | **FINDING** | 3 ZERO_STANDING rows read (lines 87, 93, 113): #14 Labour-Codes exceptional = forward signal (F1-a); #18 earlier-year tax true-up = year-end line (see F8-b); #32 Other Equity nil in quarterly cols = standard SEBI year-end-only format, not an anomaly. |
| F2 STANDALONE vs CONSOLIDATED | **N.A.** | Single-entity filing; no consolidated statement exists (SCOPE_DISCREPANCY, A1 lines 20-31; "consolidated"/"standalone" = 0 grep hits). No gap to decompose. |
| F3 SHELL-ENTITY DETECTION | **N.A.** | No subsidiaries/associates disclosed; single cost stack, one entity. Nothing to compare. |
| F4 UNAUDITED CONTRIBUTION RATIO | **N.A.** | No Other Matters paragraph, no component/JV auditors (A2 §5: EoM none, Other Matters none). Single-entity limited review; no carve-out to ratio. |
| F5 GOING CONCERN / EoM SCOPE | **PASS** | Auditor report (lines 178-214) carries NO going-concern paragraph and NO EoM (A2 §5). Nothing to track. LIMITATION: prior-quarter verbatim EoM/GC diff impossible — no prior extract supplied; carry forward for next quarter. |
| F6 FORWARD-COMMITMENT PHRASE MINING | **PASS** | Notes N1-N6 (lines 129-150) swept against full lexicon; only completed-action language ("approved by the Board", "has been reviewed", line 129-133). No dated/dateable forward commitment. Commitment register empty. |
| F7 HEDGE PHRASE MINING | **PASS** | Notes + auditor report swept; only boilerplate SRE-2410 assurance-limitation wording (lines 194-202). No newly-added hedge on revenue lumpiness or customer concentration. |
| F8 TAX FORENSICS | **FINDING** | ETR ~26.0% (92.98/357.06) vs statutory 25.17%, consistent across periods (26.0-27.1%). Growing deferred-tax charge = capex-timing forward signal (F8-a). Earlier-year tax adjustment non-zero in comparatives + FY26 deferred-tax cell garbled/unconfirmed (F8-b). |
| F9 OCI FORENSICS | **PASS** | Q1FY27 DBP remeasurement 0.13, FX-hedge OCI 0.94 (lines 102-106) — small, no single-quarter swing exceeding a full prior year. FX cash-flow-hedge line confirms export/forex exposure (thesis-relevant) but no anomaly. |
| F10 SHARE COUNT & DILUTION | **FINDING** | Paid-up 204.92 -> 207.16 YoY + basic/diluted EPS spread closed to zero = undisclosed corporate action, likely ESOP exercise (F10-a). |
| F11 RESERVES & NET WORTH TIE-OUT | **PASS** | Other Equity 6,477.63 (FY26 only col, line 113) + Paid-up 207.16 = net worth 6,684.79 Rs Mn (~Rs 668.5 Cr) at 31-Mar-26. Internally consistent; NO third-party number (rating/deck) in context to reconcile against. |
| F12 SEGMENT FORENSICS | **N.A.** | Note 4 (lines 142-143): "the Company operates in a single operating segment"; no segment assets/liabilities table exists. |
| F13 BOARD OUTCOME BEYOND RESULTS | **PASS** | Sole agenda item = approval of Q1FY27 unaudited results (lines 23-24). Grep confirms NO AGM/dividend/AR/director change/capital-raise/auditor change (A2 §3). Routine single-item meeting. |
| F14 NOTE DRAFTING INCONSISTENCIES | **PASS** | Note 1 "subjected to limited review" (line 132) matches auditor's "we do not express an audit opinion" (line 202). Entity-name variance ("Venus Pip6", line 179) is font/glyph corruption, not drafting. Signature timestamp 13:19 vs meeting close 13:15 tight but not a violation. No substantive inconsistency. |
| F15 ENTITY LIST DIFFS | **N.A.** | No consolidation list exists (single entity). Prior-quarter verbatim diff impossible — no prior extract; carry forward for next quarter. |
| F16 PRESENTATION-SPECIFIC | **N.A.** | Doctype = results, not presentation. |
| F17 CONCALL SILENCE AUDIT | **N.A.** | Doctype = results, no transcript. Monitoring-checklist cross-reference handled in scorecard below per task note. |

No blanks. GATE A3 = pass.

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/turn ref | status word |
|------------|--------------|---------------|-------------|
| (none) | — | — | — |

No dated or dateable management commitments in this filing. Notes N1-N6 are boilerplate
(Reg 33 compliance, balancing-figure disclosure, Ind AS basis, single-segment, regrouping,
website availability). This is a forward-signal vacuum in the notes themselves — the signals
in this quarter are numeric (F8-a capex cluster, F10-a dilution) rather than textual.

---

## NOTION MONITORING CHECKLIST — CROSS-REFERENCE SCORECARD
(F17 is N.A. on a results filing; thesis-relevant items surfaced here per task instruction.
Ratios using the two garbled cells are flagged. Green/Red are the Notion thresholds.)

| # | Metric | Reading from this filing | Signal | Note |
|---|--------|--------------------------|--------|------|
| 1 | DRI investigation | NO mention anywhere (grep DRI/demand/notice/contingent = 0). No exceptional item beyond Labour Codes, no contingent-liability note. | GREEN (no new development) — but UNINFORMATIVE: a bare limited-review quarterly omits the contingent-liability schedule, so silence ≠ resolution. DRI remains a watch item; first mention would be the trigger. | Flag for A4: absence here does not clear the DRI risk. |
| 2 | Fittings plant utilisation | Not disclosed (no MD&A/utilisation data). | UNASSESSABLE this doc | — |
| 3 | Export revenue % | Not disclosed (single segment, no geographic split). FX cash-flow-hedge OCI 0.94 (line 105) confirms forex/export exposure exists. | UNASSESSABLE this doc | — |
| 4 | BHEL/NTPC approval | No mention. | Silent | — |
| 5 | Revenue growth YoY | Rev from ops ~3,205.37/2,764.14 = **+15.96%** (cell garbled, unconfirmed); Total Income 3,232.27/2,803.30 = **+15.30%** (OCR-confirmed). | AMBER — near the 15% RED line, well below 25% GREEN target. Growth decelerating vs thesis. | Rev-from-ops figure is `TEXT_GARBLED_UNRESOLVED`; use Total Income (+15.3%) as the reliable read. Flag for A4. |
| 6 | ROCE trend | Not computable (no debt/capital-employed detail; only equity + finance-cost line). | UNASSESSABLE this doc | Net worth ~Rs 668.5 Cr; finance costs Rs 11.28 Cr/qtr imply material debt. |
| 7 | Margin trend PAT% | PAT/Total Income: Q1FY27 **8.17%**, Q4FY26 8.38%, Q1FY26 8.83% (FY26 8.65%). | GREEN (>6%) but gently COMPRESSING three periods running. | Compression consistent with F8-a capex cluster (rising dep + finance costs). |

Additional numeric observations (thesis-relevant, surfaced for A4; not mapped to an F-check
because a P&L-only filing has no working-capital/segment schedule to anchor them):
- **Large inventory build**: Changes in inventories of FG/WIP = **(244.02)** in Q1FY27 (line 76)
  vs (11.44) in Q4FY26 and +304.53 in Q1FY26 — a swing of ~256 Rs Mn into inventory this quarter.
  AMBIGUOUS: either a Q2 dispatch pipeline building, or slowing offtake. Cash-conversion question for A4.
- **Capex-commissioning cluster** (see F8-a): depreciation +38.3% YoY, finance costs +15.2% YoY,
  deferred-tax charge +75.9% YoY — three independent lines all pointing to new capacity going live.

---

## SUMMARY FOR A4
Three FINDINGs (F1, F8, F10) plus N.A. on all consolidation/segment/presentation/concall
checks by scope. The document's forward signals are numeric, not textual: (1) a Labour-Codes
exceptional-item line waiting to reactivate on code notification; (2) a capex-commissioning
cluster in depreciation/finance-cost/deferred-tax; (3) an undisclosed paid-up-capital increase
with the EPS dilution spread closing. Two soft-negatives for the thesis to weigh: revenue YoY
+15.3% (near the RED line, far below the 25% GREEN target) and a three-quarter PAT-margin
compression (still GREEN at 8.2%). Data-integrity flags to carry: Rev-from-ops Q1FY27 and
Deferred-tax FY26 cells garbled/unconfirmed; auditor UDIN illegible; Director signatory name
illegible. Prior-quarter verbatim diffs (F5 EoM, F15 entity list) impossible this cycle — no
prior extract.

```yaml
stage: A3-forensics
company: "VENUSPIPES"
quarter: "Q1 FY27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/venuspipes-q1fy27/work/forensics_results_venuspipes_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: PASS
  F6: PASS
  F7: PASS
  F8: FINDING
  F9: PASS
  F10: FINDING
  F11: PASS
  F12: N.A.
  F13: PASS
  F14: PASS
  F15: N.A.
  F16: N.A.
  F17: N.A.
findings:
  - {id: "F1-a", check: "F1", line: "87", classification: "FORWARD-SIGNAL", implication: "Labour-Codes exceptional line nil now but carried Q4FY26/FY26; reactivates on Labour Codes notification; management-estimated and volatile"}
  - {id: "F8-a", check: "F8", line: "94", classification: "FORWARD-SIGNAL", implication: "Deferred-tax charge +75.9% YoY with dep +38.3% and finance costs +15.2% = capex-commissioning cluster; near-term margin/tax drag, medium-term volume optionality"}
  - {id: "F8-b", check: "F8", line: "93,94", classification: "NEUTRAL-FACT", implication: "Earlier-year tax adjustment non-zero in comparative columns (year-end true-up); FY26 deferred-tax cell garbled/unconfirmed, do not rely"}
  - {id: "F10-a", check: "F10", line: "110,118", classification: "AMBIGUOUS", implication: "Paid-up 204.92->207.16 YoY + EPS spread closed to zero = undisclosed corporate action (likely ESOP exercise); source record and residual option pool"}
forward_signals: ["F1-a", "F8-a"]
ambiguous: ["F10-a"]
commitments: []
gate_a3: pass
blank_checks: []
```
