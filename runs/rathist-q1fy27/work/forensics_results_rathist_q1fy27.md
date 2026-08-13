# A3 FORENSIC NOTES — Rathi Steel and Power Ltd (rathist) — Q1 FY27 — DOCTYPE: results

Source A1 extract: `runs/rathist-q1fy27/work/extract_results_rathist_q1fy27.txt`
Source A2 ledger: `runs/rathist-q1fy27/work/ledger_results_rathist_q1fy27.txt`
Ledger reconciliation: 100% — all 5 notes (Table 1), all 35 line items (Table 2),
5 agenda items (Table 3), 11 auditor paragraphs (Table 4), 1 entity row (Table 5)
read verbatim at their cited lines before judging.
Prior-quarter document: NONE supplied. No Notion checklist, no companies/RATHIST.md.
This is a fresh, no-prior-thesis review; every QoQ-diff-dependent check (F5 diff, F15)
is marked N.A. with reason "no prior-period document supplied," never blank.

Unit convention: Rs. in Lakhs (Lacs). Columns throughout:
Q1FY27 (30.06.2026, Unaudited) | Q4FY26 (31.03.2026, Audited) | Q1FY26 (30.06.2025,
Unaudited) | FY26 (31.03.2026, Audited).

## OCR-GARBLE RECONCILIATION (performed before any F-check used a garbled cell)
- Line 204 PBT Q1FY27 reads "341.99" but the true value is **347.99**. Reconciled
  three independent ways: (i) arithmetic — Total Revenue 19,367.25 (line 190) minus
  Total Expenses 19,019.26 (line 199) = 347.99; (ii) internal consistency — the same
  Q1FY27 PBT/PAT figure reads 347.99 at lines 200, 202, 209, 213; (iii) press-release
  PAT of Rs 3.48 Cr = 347.99 Lakhs. Isolated OCR digit substitution (7→1). Not silently
  corrected; used as 347.99 with this note.
- Line 216 (an OCI sub-line) is garbled beyond parsing ("2 | n| | nw | i"). Its
  magnitude is bounded by arithmetic (see F9): Q1FY27 OCI = TCI 360.78 − PAT 347.99 = +12.79.
- Displaced note markers: Note 3 marker rendered as "w" at line 242, Note 4 as "»" at
  line 248, Note 5 marker fully absent (content boundary lines 253-257). Confirmed against
  A2 Table 1.
- Auditor UDIN (line 166 "262))149 y1AR M ¢ 240") and Firm Registration Number (line 160
  "irm Registration", no digits) are not recoverable in valid format. Carried as data gaps,
  not fabricated (see F14).

--------------------------------------------------------------------------
## FINDINGS TABLE
--------------------------------------------------------------------------
| id | check | ledger row / line | verbatim quote | classification | forward implication |
|----|-------|-------------------|----------------|----------------|---------------------|
| A3-01 | F1 | T2 rows 193,201,203,205-208,210-212 | "Purchase of stock-in-trade  -  -  -  -" (l.193); "Total Tax  -  -  -  -" (l.208) | CONFIRMATORY-NEGATIVE | No hidden exceptional/extraordinary/discontinued items; no trading arm; clean template. The 5 NIL tax lines are the leading edge of F8 (see A3-05). |
| A3-02 | F2 | T5 row 1, l.241 (+ A1 header l.19) | "Company does not have any subsidiary associate joint venture entity(ics) for the respective period." | AMBIGUOUS | Standalone-only entity, no consolidated statement to decompose. Press-release context references a group-level WOS/PLI-linked wholly-owned-subsidiary route that does NOT appear in this legal entity — probe whether PLI capex/revenue will sit in an off-statement WOS. |
| A3-03 | F5 | T4 row 8, l.137-143 | "figures for the quarter ended 31% March 2026 ... are the balancing figures between audited figures" | CONFIRMATORY-NEGATIVE | Standard Reg-33 balancing-figure EoM (not a substantive EoM, no going concern). Confirms the Q4FY26 column is derived (FY26 audited minus 9M reviewed), NOT independently reviewed — Q4FY26 cells are lower-confidence and can carry year-end plugs (see A3-04). |
| A3-04 | F5 | T2 row 197, l.197 | "Depreciation and amortisation expenses  220.70   71.04   259.26   86125" | FORWARD-SIGNAL | Q4FY26 depreciation 71.04 is ~73% below the ~265/qtr FY26 run-rate (implied Q2+Q3 FY26 = 861.25−259.26−71.04 = 530.95 ≈ 265 each) = a year-end truing-up/reversal landing in the balancing-figure quarter. Q1FY27 220.70 is also DOWN 14.9% YoY vs Q1FY26 259.26. Depreciation run-rate is falling → maturing/fully-depreciated asset base or useful-life revision; watch for a step-down that flatters PAT. |
| A3-05 | F8 | T2 rows 204/209 vs 205-208 | PBT 347.99 (l.204, corrected) with "Tax expenses  -  -  -" (l.205) | FORWARD-SIGNAL | Effective tax rate = 0% in all four periods against 25.17% statutory. NIL current tax, NIL deferred tax, NIL MAT despite positive PBT every period. Implies brought-forward losses / unabsorbed depreciation / MAT credit shielding profits. Latent haircut: ~25% of PAT (FY26: ~Rs 323.8 L; Q1FY27: ~Rs 87.6 L) crystallises when carryforwards exhaust. |
| A3-06 | F9 | T2 rows 213 vs 217, l.213/217 | TCI "1206 21" (l.217) below PAT "1,286.49" (l.213) | AMBIGUOUS | FY26 annual OCI = 1,206.21 − 1,286.49 = −80.28 L, yet every shown quarter posts POSITIVE OCI (Q1FY27 +12.79; Q4FY26 +9.72; Q1FY26 +12.84). Unshown Q2+Q3 FY26 OCI must total ≈ −102.8 L — a large mid-year actuarial swing (discount-rate / plan-asset remeasurement). Verify assumptions at the Annual Report; possible recurring negative OCI drag. |
| A3-07 | F11 | T2 row 196 (+ row 219), l.196/219 | "Finance cost  208.70   167.36   174.93   742.06" (l.196) | FORWARD-SIGNAL | Finance cost RISING +19.3% YoY (208.70 vs 174.93) and +24.7% QoQ (vs 167.36) while depreciation falls — leverage/interest building against net worth (8,636.30 equity + 5,273.00 reserves). Plus Rs 889.40 L Redeemable Preference Shares (l.219, face Rs 10) = a standing redemption cash-call / debt-like claim on that net worth. |
| A3-08 | F14 | T2 row 200, l.200 | "* 18855" (Q1FY26 PBT cell carries a stray asterisk) | AMBIGUOUS | An asterisk/reference mark on the Q1FY26 PBT with NO corresponding footnote defined anywhere in the Notes (236-257). Likely OCR, but per conservative bias flag as a possible lost footnote. Compounded by governance data gaps: auditor FRN absent (l.160), UDIN unparseable (l.166), results-page signatory NAME absent (l.262, only "Managing Director  DIN : 00174146"). |

--------------------------------------------------------------------------
## CHECKLIST SCORECARD (all 17; exactly one status each — GATE A3)
--------------------------------------------------------------------------
- **F1 — FINDING** (A3-01). 10 ZERO_STANDING rows read (l.193,201,203,205,206,207,208,210,211,212). Purchase of stock-in-trade NIL (no trading arm); Exceptional/Extraordinary/Discontinued NIL (no hidden below-the-line items); all 5 tax lines NIL — the latter routed to F8. Template is clean; no anticipated transaction class hiding.
- **F2 — FINDING** (A3-02). Mechanical S-vs-C gap cannot be computed: no consolidated statement exists (l.241, l.19). Per instruction, the ABSENCE plus the press-release group-level WOS/PLI-subsidiary route is itself the note — flagged, not skipped.
- **F3 — N.A.** No subsidiaries/associates/JVs exist (l.241), so there are no cost lines to compare for shell detection and no Going Concern EoM to reconcile. Re-run if the group-level WOS is ever consolidated into this entity. Assessed and cited, not blank.
- **F4 — N.A.** No consolidated PAT and no component-auditor / JV / associate numbers, so 0% of the results rests on figures outside the statutory auditor's review (scope confirmed standalone-only, Table 4 row 4, l.156). The nearest analog — Q4FY26 figures being un-reviewed balancing figures — is logged under F5 (A3-03), not here.
- **F5 — FINDING** (A3-03, A3-04). Standard Reg-33 balancing-figure EoM present (l.137-143), unmodified conclusion, no going concern. QoQ verbatim EoM diff is N.A. (no prior-period document supplied). The balancing-figure status directly explains the anomalous Q4FY26 depreciation plug (A3-04).
- **F6 — PASS.** Notes 1-5 (l.237-257) and cover letter mined case-insensitively for the forward-commitment lexicon: no "expected to / will be / shall be completed / is underway / commenc[ed as a project] / proposes to / board has approved [a project] / intends to." Only lexical false positive is "commenced at 3.30 pm" (l.72), a meeting-timing fact, not a commitment. Commitment register = empty.
- **F7 — PASS.** Hedge lexicon mined: only false positive is "subject to limited review by us" (l.143), describing the 9M comparative, standard audit language — not a pre-emptive hedge about revenue lumpiness or customer concentration. No newly-added risk hedge in the Notes.
- **F8 — FINDING** (A3-05). 0% ETR across all four periods vs 25.17% statutory; NIL current/deferred/MAT. Standing tax-shield feature quantified above.
- **F9 — FINDING** (A3-06). Full-year FY26 OCI negative (−80.28 L) despite every shown quarter positive; implied Q2+Q3 FY26 swing ≈ −102.8 L. Assumption change to verify at AR.
- **F10 — PASS.** Paid-up equity capital unchanged all four periods (l.218, 8,636.30 L, face Rs 5); Redeemable Pref unchanged (l.219, 889.40 L); Basic EPS = Diluted EPS in every period (0.40 / 0.86 / 0.22 / 1.49, l.222-223) — zero dilution spread, no corporate action, no dilutive instruments. (The redeemable prefs are a capital-structure item carried to F11, not dilution.)
- **F11 — FINDING** (A3-07). Net worth ties out internally (paid-up 8,636.30 + Reserves & Surplus 5,273.00 [FY26 only, l.220] = 13,909.30 L); no third-party number (rating rationale / slide) supplied to reconcile against, so no gap test possible. Elevated to FINDING on the rising finance-cost/leverage read and the standing redeemable-preference claim.
- **F12 — N.A.** Single reportable segment "Steel" (Note 1, l.237); no segment asset/liability disaggregation is disclosed or required, so no cross-segment build/unwind can be trended.
- **F13 — PASS.** Single-item board meeting: only the Q1FY27 results were "considered and approved" (l.63). No AR/Board's-Report approval, no AGM notice, no record date, no dividend, no director appointment/term dates, no auditor change, no capital-raising enabling resolution (Table 3). Nothing to schedule a Role 6 AR event or funding-round watch against this quarter.
- **F14 — FINDING** (A3-08). Stray undefined asterisk (l.200) plus auditor FRN/UDIN gaps and missing results-page signatory name. Consistency check itself passes on substance: Note 2 "unmodified conclusion" (l.240) matches the auditor's unmodified limited-review conclusion (l.144-156); entity name consistent throughout.
- **F15 — N.A.** No prior-period document supplied AND no entities exist to diff (l.241). ENTITY_CHANGE cannot be evaluated.
- **F16 — N.A.** Doctype is a results filing, not a presentation.
- **F17 — N.A.** Doctype is a results filing, not a concall; and no Notion monitoring checklist / prior thesis exists to run a silence audit against.

--------------------------------------------------------------------------
## COMMITMENT REGISTER (from F6)
--------------------------------------------------------------------------
| commitment | implied date | note/turn ref | status word |
|------------|--------------|---------------|-------------|
| (none) | — | Notes 1-5 (l.237-257), cover letter (l.33-89) | none — no dated/dateable forward management commitment in the filing |

Note: the only status-verb tokens present are backward/administrative ("considered and
approved" l.63, "being made available" l.69, "commenced/concluded" l.72). No
"initiated → underway → completed" milestone language for A5's promise-vs-delivery
tracker or the FTTCP catalyst timeline this quarter.

--------------------------------------------------------------------------
## ADDITIONAL FORENSIC OBSERVATIONS (hand-off context for A4/A5)
--------------------------------------------------------------------------
- Changes in inventories swing: +167.02 Q1FY27 (inventory DRAWDOWN, a cost/working-capital
  release) vs (395.73) Q1FY26 (build) (l.194). Normal quarterly WC movement, not
  forensically alarming, but pairs with the rising finance cost (A3-07) for A4's cash-flow read.
- Revenue Q1FY27 19,341.04 vs Q1FY26 15,529.43 = +24.5% YoY (l.188); PAT Q1FY27 347.99 vs
  Q1FY26 188.55 = +84.6% YoY (l.209). Operating leverage plus the falling depreciation
  (A3-04) and zero tax (A3-05) are all flattering the PAT line — A4 should test how much of
  the YoY PAT jump is durable operations vs the depreciation step-down and the 0% ETR.
- WOS/PLI structural question (A3-02) is the single most important forward item for A4 to
  convert into a management question: does PLI-linked capacity and its revenue sit in this
  listed standalone entity or in a group WOS outside these statements?

--------------------------------------------------------------------------
## A4 HAND-OFF — QUESTIONS TO GENERATE (FORWARD-SIGNAL + AMBIGUOUS)
--------------------------------------------------------------------------
FORWARD-SIGNAL: A3-04 (depreciation run-rate step-down), A3-05 (0% ETR / latent 25% PAT
haircut and remaining carryforward quantum), A3-07 (rising finance cost + redeemable-pref
redemption schedule).
AMBIGUOUS: A3-02 (standalone-only vs group WOS/PLI route), A3-06 (negative FY26 OCI /
actuarial assumption change), A3-08 (undefined asterisk + auditor FRN/UDIN/signatory gaps).

```yaml
stage: A3-forensics
company: "rathist"
quarter: "q1fy27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "runs/rathist-q1fy27/work/forensics_results_rathist_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: FINDING
  F3: N.A.
  F4: N.A.
  F5: FINDING
  F6: PASS
  F7: PASS
  F8: FINDING
  F9: FINDING
  F10: PASS
  F11: FINDING
  F12: N.A.
  F13: PASS
  F14: FINDING
  F15: N.A.
  F16: N.A.
  F17: N.A.
findings:
  - {id: "A3-01", check: "F1", line: "193,201,203,205-208,210-212", classification: "CONFIRMATORY-NEGATIVE", implication: "No hidden exceptional/extraordinary/discontinued/trading lines; 5 NIL tax lines feed F8"}
  - {id: "A3-02", check: "F2", line: "241", classification: "AMBIGUOUS", implication: "Standalone-only; group-level WOS/PLI route may hold PLI capex/revenue off these statements"}
  - {id: "A3-03", check: "F5", line: "137-143", classification: "CONFIRMATORY-NEGATIVE", implication: "Standard balancing-figure EoM; Q4FY26 column derived, not independently reviewed"}
  - {id: "A3-04", check: "F5", line: "197", classification: "FORWARD-SIGNAL", implication: "Q4FY26 depreciation 71.04 is a year-end plug; run-rate falling 14.9% YoY, flatters future PAT"}
  - {id: "A3-05", check: "F8", line: "204,205-208,209", classification: "FORWARD-SIGNAL", implication: "0% ETR all periods; ~25% latent PAT haircut when loss/MAT carryforwards exhaust"}
  - {id: "A3-06", check: "F9", line: "213,217", classification: "AMBIGUOUS", implication: "FY26 OCI -80.28L despite positive quarters; mid-year actuarial swing, verify assumptions at AR"}
  - {id: "A3-07", check: "F11", line: "196,219", classification: "FORWARD-SIGNAL", implication: "Finance cost +19% YoY while depreciation falls; Rs 889.40L redeemable prefs = future cash call"}
  - {id: "A3-08", check: "F14", line: "200", classification: "AMBIGUOUS", implication: "Undefined asterisk on Q1FY26 PBT + missing FRN/UDIN/signatory name = governance data gaps"}
forward_signals: ["A3-04", "A3-05", "A3-07"]
ambiguous: ["A3-02", "A3-06", "A3-08"]
commitments: []
gate_a3: pass
blank_checks: []
```
