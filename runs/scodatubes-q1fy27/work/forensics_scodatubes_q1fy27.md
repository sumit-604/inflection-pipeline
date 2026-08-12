# A3 FORENSIC NOTES — Scoda Tubes Limited (SCODATUBES) — Q1 FY27 — DOCTYPE: RESULTS

Agent: A3 Forensic Notes | Model: claude-opus-4-8
Inputs read: extract_results_scodatubes_q1fy27.txt (185 lines, 3 pages,
Millions convention, x0.1 to Rs Cr), ledger_results_scodatubes_q1fy27.md.
Prior-quarter extract: NONE (first quarterly run for this ticker).
Filing scope: bare Reg 33 results — P&L + 7 notes + limited review report
only. NO balance sheet, NO cash-flow statement, NO segment table.

## LEDGER RECONCILIATION STATEMENT
100% reconciled. Every A2 row read verbatim at its A1 line before judging:
- 32 financial line-items (lines 80-112), 7 notes (115-127), 1 agenda item
  (38-39) + 2 enclosures (42-43), 4 auditor paragraphs (158,162,169,179),
  1 consolidation entity (123), 3 signatory blocks (51-53, 134-143, 188-197).
- 4 ZERO_STANDING rows confirmed at source: Exceptional items (line 93),
  Earlier year taxes (line 97), Discontinued Operation EPS (line 111), and
  the "no subsidiary/JV/associate" statement (Note 5, line 123).

Independent footing tests were run on all four reporting columns as part of
forensics (these are NOT in the A2 ledger; A3 derived them). Result drives
finding A3 below: the Q1 FY27 column foots cleanly; the three comparative
columns (Q4 FY26, Q1 FY26, FY26) contain a repeated 7-rendered-as-1 digit
corruption that A4 must not compute ratios off without source-PDF check.

---

## FINDINGS TABLE

| id | check | ledger row / ref | line | verbatim quote | classification | forward implication |
|----|-------|------------------|------|----------------|----------------|---------------------|
| A1 | F8 | table rows 17,19 (Current tax / Deferred tax) | 96, 98 | "Current tax ... 6.25" (line 96); "Deferred tax liability / (asset) ... 11.22" (line 98) | FORWARD-SIGNAL | Cash (current) tax collapsed to Rs0.63 Cr = 8.9% of Q1 PBT (Rs7.00 Cr) vs 20.4% in Q1 FY26 (18.90 on 92.75) and 22-27% in every prior period. Book ETR held near statutory (~25.0%) only via a deferred-tax charge of 11.22 (Rs1.12 Cr) that is 64% of total tax and ~1,600 bps of PBT this quarter, up from ~326 bps (Q1 FY26) and ~498 bps (Q4 FY26). This is a timing-difference (accelerated-depreciation) shield that reverses: future cash-tax step-up. Corroborated by depreciation Rs4.13 Cr (line 89, 41.31 vs 15.12 Q1 FY26, +173% YoY) and finance costs Rs6.48 Cr (line 88, 64.81 vs 51.04, +27% YoY) = debt-funded capex building the DTL. Management question for A4. |
| A2 | F9 | table row 23 (Re-measurements of defined benefit plans) | 102 | "Re-measu rements of t he defined benefit s plans ... 1.71" | AMBIGUOUS | Q1 FY27 OCI actuarial remeasurement 1.71 (Rs0.17 Cr) EXCEEDS the full prior-year FY26 figure of 1.18, and the series sign-flips (1.47 Q1 FY26, then (1.47) Q4 FY26, then 1.71) — a pattern consistent with a discount-rate / plan-asset assumption change rather than accrual drift. Immaterial in rupees but flags an assumption change to verify against the FY26 Annual Report actuarial note. Management question for A4. |
| A3 | F14 | table rows 2/6/13/15/20 + signatory rows 1-2 | 51, 85-90, 141, 96-99, 83-94 | letter signatory "Jagrutk" (line 51); results signatory "s~ Bh: :;bhal Patel" (line 141); "b Earlier year taxes ... -" (line 97) | NEUTRAL-FACT (data integrity — verify at source, NOT a management question) | Systematic extraction corruption in the three COMPARATIVE columns despite header "ocr_pages: none". Footing tests: (a) Q1 FY26 raw materials 142.49 (line 85) cannot foot to that column's Total Expenses 899.03 (line 91) — implied ~742-743, a 7->1 digit drop; (b) FY26 Total Expenses 4,164.89 (line 91) fails vs Total Income 5,292.21 less PBBET 527.32 = 4,764.89 (7->1); (c) FY26 PBT 521.32 (line 94) vs PBBET 527.32 with Exceptional blank (7->1); (d) Q1 FY26 PAT 10.83 (line 99) vs PBT 92.75 less tax 21.92 = 70.83 (7->1); (e) Total Income lines 83 read 1,259.15 / 1,219.12 / 991.18 vs footed 1,259.75 / 1,279.72 / 991.78 (all 7->1). Plus two OCR-degraded signatory names (DINs 06785595 and 08036100 clean). A4/A1 MUST verify all comparative figures against the source PDF before any YoY ratio, CFO/PAT, or margin computation. |

---

## CHECKLIST SCORECARD (F1-F17)

| Check | Status | Basis (one line) |
|-------|--------|------------------|
| F1 ZERO-VALUE STANDING LINES | PASS | All 4 ZERO_STANDING addressed, none populated: Exceptional items (line 93) anticipates one-off gains/losses/impairment; Earlier year taxes (line 97) anticipates prior-year tax true-ups; Discontinued Operation EPS (line 111) anticipates discontinued ops; "no subsidiary/JV/associate" (Note 5, line 123) is the consolidation ZERO_STANDING. A future quarter populating any of the first three is the watch signal. |
| F2 STANDALONE vs CONSOLIDATED | N.A. | Standalone-only filing. Note 5 (line 123): "The company does not have any subsidiary, joint venture or associate company as on June 30, 2026." S-vs-C gap is STRUCTURALLY ZERO on every period; no consolidated statement exists to decompose. |
| F3 SHELL-ENTITY DETECTION | N.A. | No subsidiaries/JVs to test (Note 5, line 123). No standalone-vs-consolidated cost comparison possible; no shell entities can exist. |
| F4 UNAUDITED CONTRIBUTION RATIO | N.A. | No component auditors, JVs or associates; auditor reviewed the single standalone entity. No Other Matters paragraph (ledger 4b, extract lines 179-185). Unaudited-component contribution = Rs0 / 0% of PAT. |
| F5 GOING CONCERN / EoM SCOPE | PASS | Unmodified conclusion, "nothing has come to our attention" (para 4, lines 179-185). No EoM, Other Matters, or Going Concern paragraph present (ledger 4b: grep = 0 each). First run: no prior paragraph to verbatim-diff; present-filing scope is clean. |
| F6 FORWARD-COMMITMENT MINING | PASS | Full lexicon swept across 7 notes (115-127) and board letter (34-45): zero hits. Notes are boilerplate (Ind AS basis, SEBI format, single segment, no subsidiaries, Q4 balancing-figure, regrouping). Commitment register empty. NOTE the ABSENCE: no welded-plant / capex / order-book progress statement despite live catalysts — silence carried to forward narrative. |
| F7 HEDGE PHRASE MINING | PASS | Hedge lexicon swept across notes: only standard "wherever considered necessary" (Note 7, line 127). No new hedge on revenue lumpiness or customer concentration. NOTE the ABSENCE of any customer-concentration disclosure despite the known FY25 26.7% single-customer figure (carried to forward narrative; trigger 3 pending). |
| F8 TAX FORENSICS | FINDING | See finding A1: current-tax rate collapse to 8.9% with ~1,600 bps deferred-tax (DTL) timing shield; Earlier-year-taxes sub-check is clean (ZERO_STANDING, line 97). |
| F9 OCI FORENSICS | FINDING | See finding A2: Q1 FY27 remeasurement 1.71 (line 102) exceeds full FY26 (1.18); sign-flipping series signals assumption change; verify at AR. |
| F10 SHARE COUNT & DILUTION | PASS | Paid-up equity 599.09 Mn constant across all four periods (line 106); no corporate action. EPS reported as single "Basic / Diluted" figure (lines 110,112) = zero dilution spread, no dilutive instruments. (EPS 0.88 vs 1.44 Q1 FY26 is a performance move, not dilution; see forward narrative.) |
| F11 RESERVES & NET WORTH TIE-OUT | PASS | Other Equity 3,304.00 (FY26 only, line 107) + Paid-up 599.09 = net worth 3,903.09 Mn = Rs390.31 Cr (FY26). No third-party anchor (rating rationale / slide) in this bare filing to reconcile against, so no gap to test. ND: quarterly Other Equity blank by convention; Q1 FY27 net worth not disclosed (no balance sheet). |
| F12 SEGMENT FORENSICS | N.A. | Single reportable segment. Note 4 (line 122): "dealing in manufacturing of stainless-steel (SS) pipes and tubes only. Hence, segment reporting ... is not applicable." No segment assets/liabilities/revenue table. ND: welded-vs-seamless split and utilisation not visible (trigger 8 remains pending). |
| F13 BOARD OUTCOME BEYOND RESULTS | PASS | Single-agenda, one-hour meeting (04:00-05:00 PM, lines 37-39): only the unaudited results + limited review report. No AR/Board's-Report/MD&A approval, no AGM notice or record date, no dividend, no director appointment/term, no auditor change, no ESOP, no capital-raising resolution (ledger 1c). FORWARD note: FY26 Annual Report NOT yet approved -> Note 36 customer-concentration disclosure (trigger 3) still pending; watch for a separate AR board meeting in coming weeks. |
| F14 NOTE DRAFTING / EXTRACTION INCONSISTENCIES | FINDING | See finding A3: systematic 7->1 digit corruption across all three comparative columns (footing-verified) + two OCR-degraded signatory names. DINs clean. Note text vs auditor is consistent (Note 1 "unmodified conclusion" matches the limited review report); minor casing "Scoda Tubes limited" immaterial. |
| F15 ENTITY LIST DIFFS | N.A. | Standalone-only (Note 5, line 123); consolidation list = the single reporting entity. First quarterly run, no prior ledger to diff. S-vs-C entity delta structurally zero. This filing is the Q2 FY27 baseline. |
| F16 PRESENTATION-SPECIFIC | N.A. | Doctype is results; no investor presentation in scope. |
| F17 CONCALL SILENCE AUDIT | N.A. | Doctype is results; no transcript in scope. (Notion checklist cross-referenced in forward narrative below to sharpen forward signals, not as an F17 audit.) |

Gate A3: PASS — all 17 checks marked, no blanks.

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/ref | status word |
|------------|--------------|----------|-------------|
| (none) | — | — | — |

No forward-commitment lexicon hits in the notes (lines 115-127) or board
letter (lines 34-45). This bare Reg 33 filing carries ZERO dated management
commitments. The absence is itself a forward-signal: no progress statement
on the welded plant, marine approvals, BHEL/NTPC tender, or capex despite
all four being live catalysts on the Notion checklist. Nothing to hold
management to from this document; the promise-vs-delivery tracker gains no
new rows and no prior promise is confirmed or retired here.

---

## FORWARD-SIGNAL NARRATIVE (cited; feeds A4 management-question set)

These are cited observations beyond the 17 mechanical checks that bear on the
future. Conservative bias applied — where direction is uncertain, leaned bear.

1. CASH-TAX SHIELD WIDENING (line 96/98) — finding A1. Current tax 8.9% of
   PBT vs 20-27% historically; deferred-tax timing shield jumped to ~1,600
   bps. Q for management: what drives the current-tax drop, and when do the
   accelerated-depreciation timing differences reverse into higher cash tax?
2. CAPEX SIGNATURE (lines 89, 88) — depreciation Rs4.13 Cr (+173% YoY, still
   rising QoQ 36.12 -> 41.31) and finance costs Rs6.48 Cr (+27% YoY) point to
   new assets capitalised and debt-funded, consistent with the welded-plant
   commissioning window (trigger 4). But NO commissioning/revenue statement
   is made (F6 silence). Q: is welded commercial production live, and what
   revenue did it contribute in Q1?
3. INVENTORY BUILD CONTINUES (line 86) — "Changes in inventories ... (156.14)"
   = a Rs15.6 Cr finished-goods/WIP BUILD this quarter (vs Rs5.2 Cr build Q1
   FY26), against flat QoQ revenue (Rs124.3 Cr vs Rs123.6 Cr). ND: no balance
   sheet / cash-flow, so inventory-days (>180 tripwire) and H1 CFO/PAT >0.30x
   (trigger 1) CANNOT be tested this filing. The visible P&L build leans bear
   on the working-capital thesis. Q: inventory days at 30 Jun 2026, and Q1 CFO?
4. REVENUE +27.6% YoY, PAT DOWN QoQ (lines 81, 99/110) — revenue Rs124.3 Cr
   (+27.6% vs Rs97.4 Cr Q1 FY26) but PAT Rs5.25 Cr is -17% QoQ vs Q4 FY26
   Rs6.32 Cr and EPS 0.88 vs 1.02; PBT margin compressed to 5.6% (69.97/1243.45)
   as raw-material cost ran at 80.5% of revenue. Margin (trigger 9, >=14% EBITDA)
   not directly disclosed (ND, no EBITDA line). Q: EBITDA margin bridge and
   raw-material cost trajectory.
5. WHAT THE FILING DOES NOT LET US VERIFY (ND register, itself a forward
   signal for the question set): no balance sheet (net worth movement,
   receivables vs revenue trigger 7, inventory days trigger 2), no cash-flow
   (H1 CFO / cumulative CFO/PAT trigger 1 and thesis-broken test), no segment
   table (welded/seamless utilisation triggers 4/8), no customer-concentration
   note (trigger 3), no order-book / tender update (trigger 5), no marine-
   approval update (trigger 6). A bare Reg 33 filing on a company whose entire
   re-engagement case rests on cash conversion and disclosure breadth: the
   silence is the signal.
6. DATA-INTEGRITY CAVEAT (finding A3) — A4 must treat every 1-containing
   comparative figure as suspect pending source-PDF verification; the 7->1
   corruption already caught nine cells. Do not compute YoY off the raw extract.

---

```yaml
stage: A3-forensics
company: "SCODATUBES"
quarter: "Q1 FY27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/scodatubes-q1fy27/work/forensics_scodatubes_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: PASS
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: PASS
  F6: PASS
  F7: PASS
  F8: FINDING
  F9: FINDING
  F10: PASS
  F11: PASS
  F12: N.A.
  F13: PASS
  F14: FINDING
  F15: N.A.
  F16: N.A.
  F17: N.A.
findings:
  - {id: "A1", check: "F8", line: "96,98", classification: "FORWARD-SIGNAL", implication: "Current tax 8.9% of PBT vs 20-27% prior; ~1,600 bps deferred-tax timing shield (DTL build from accelerated depreciation on debt-funded capex); future cash-tax step-up"}
  - {id: "A2", check: "F9", line: "102", classification: "AMBIGUOUS", implication: "Q1 OCI remeasurement 1.71 exceeds full FY26 (1.18) and sign-flips; probable actuarial assumption change; verify discount-rate/plan-asset assumptions at FY26 AR"}
  - {id: "A3", check: "F14", line: "85,91,94,99,141", classification: "NEUTRAL-FACT", implication: "Systematic 7->1 digit corruption in all three comparative columns (nine footing-verified cells) plus two OCR-degraded signatory names; A4/A1 must verify comparatives against source PDF before any ratio/YoY work"}
forward_signals: ["A1"]
ambiguous: ["A2"]
commitments: []
gate_a3: pass
blank_checks: []
```
