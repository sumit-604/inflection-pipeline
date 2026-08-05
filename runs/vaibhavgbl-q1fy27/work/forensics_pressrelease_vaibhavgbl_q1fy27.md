# A3 FORENSIC NOTES — Vaibhav Global Limited (VAIBHAVGBL), Q1 FY27
Doctype (as tasked): `presentation`. Actual artifact: NSE/BSE cover letter +
management press release, 5 pages, no slides, no auditor report, no board
agenda, no transcript (`DOCTYPE_LABEL_MISMATCH`, per A2). Forensic checklist run
against the RESULTS-FILING mapping as closest fit; balance-sheet / auditor /
segment checks are marked N.A. explicitly rather than forced.

Ledger reconciliation: all 18 ledger sections (71 disclosure units) read
verbatim at their cited lines in the A1 extract before judging. 100% reconciled.
First-time coverage — Notion monitoring checklist EMPTY, no prior quarter
extract, so all quarter-over-quarter diff checks (F5, F15, F16 dropped-metric,
F17) have no prior baseline and are N.A. on that basis.

---

## FINDINGS TABLE
| id | check | ledger row ref | line / slide | verbatim quote | classification | forward implication |
|----|-------|----------------|--------------|----------------|----------------|---------------------|
| F7-01 | F7 | §13 row 2 (para lines 126-131) | 127 | "on a constant currency basis, revenue remained broadly flat" | FORWARD-SIGNAL | All reported +13% YoY revenue growth is FX-driven; underlying volume/price growth ~0%. Strip the FX tailwind and next quarter's headline is at risk of flat-to-negative. Ask management for constant-currency guidance and FX sensitivity. |
| F8-01 | F8 | §9 row 1 (footnote) | 91, 84, 118 | "PAT is excluding MAT credit of Rs. 47.6 cr" | AMBIGUOUS | Q4FY26 PAT of 44 is shown ex a Rs 47.6 cr MAT credit; on a reported basis Q4FY26 PAT was ~91.6 cr, so the sequential trend is actually DOWN ~39% QoQ, not the +29% displayed. MAT credit = earlier-years minimum-alternate-tax utilisation (an F8 "earlier years" tax item). Is Q1FY27 PAT of 56 similarly clean? Normalised ETR not derivable here. A4 to ask. |
| F16-01 | F16 | §8 row 4 + §7 all | 84, 70, 122 | "44*" / "up 13% YoY" | AMBIGUOUS | Two within-document reframings that flatter the read: (a) the QoQ PAT base is normalised ex-MAT-credit so the sequential drop disappears; (b) the headline banner leads with reported +13% while the MD quote concedes constant-currency revenue was flat. Both choices lift the top-line optics. No prior deck exists to diff (first coverage). |
| F6-01 | F6 | §13 row 5 (para lines 145-150) | 145, 146 | "We have moved all our retail businesses to Shopify Enterprise ECom platform during the quarter" | FORWARD-SIGNAL | Completed milestone (platform migration done in-quarter) paired with the promise it "will accelerate our ECom journey." Feeds the Role 5 promise-vs-delivery tracker: next quarter should show the acceleration, or it becomes a broken promise. Ask for the ECom KPI management will hold itself to. |
| F14-01 | F14 | §11 row 1 vs §15 row 5 | 110 vs 190 | "Over 115 million meals" vs "over 113 million meals" | NEUTRAL-FACT | Same cumulative "since inception" meal-program counter stated two different ways in the same release (A2 `NUMBER_DISCREPANCY`). Immaterial to financials; a data-hygiene / drafting-control governance data point. Not a forward signal on its own. |

---

## CHECKLIST SCORECARD (all 17, exactly one status each — GATE A3)
| Check | Status | One-line basis |
|-------|--------|----------------|
| F1 ZERO-VALUE STANDING ITEMS | N.A. | A2 swept the full table + narrative; zero `ZERO_STANDING` rows exist (§18). Nothing to interrogate. |
| F2 STANDALONE vs CONSOLIDATED | N.A. | Press release carries a single 7-line highlights table (§8); no standalone-vs-consolidated split exists. |
| F3 SHELL-ENTITY DETECTION | N.A. | No cost lines (Cost of Materials / Employee Benefits / Depreciation) disclosed; only Revenue/EBITDA/PAT/Net Cash. |
| F4 UNAUDITED CONTRIBUTION RATIO | N.A. | No auditor report / Other Matters paragraph in this artifact; EY listed as unlabelled contact (§16 row 3), capacity NOT stated. |
| F5 GOING CONCERN / EoM | N.A. | No going-concern / EoM language; first coverage, no prior quarter to verbatim-diff. |
| F6 FORWARD-COMMITMENT MINING | FINDING | F6-01: Shopify Enterprise migration "moved... during the quarter" (completed) + "will accelerate our ECom journey" (forward), line 145-146. |
| F7 HEDGE PHRASE MINING | FINDING | F7-01: MD quote newly states constant-currency revenue "remained broadly flat" and macro uncertainty "may persist" (lines 127, 168) — pre-emptive cover for a soft next quarter. |
| F8 TAX FORENSICS | FINDING | F8-01: Rs 47.6 cr MAT credit excluded from Q4FY26 PAT base (line 91) — earlier-years tax item; ETR not derivable (no tax line disclosed). |
| F9 OCI FORENSICS | N.A. | No OCI / actuarial disclosure in a narrative press release. |
| F10 SHARE COUNT / DILUTION | N.A. | No paid-up capital, no share count, no basic/diluted EPS. Interim dividend Rs 1.5/share stated (line 61) but no share-count math possible. |
| F11 RESERVES / NET WORTH | N.A. | "Net Cash" 287 disclosed (line 86) but no Other Equity / paid-up / net-worth figure to tie out. |
| F12 SEGMENT FORENSICS | N.A. | No segment assets/liabilities/results table; geographies mentioned narratively only. |
| F13 BOARD OUTCOME BEYOND RESULTS | N.A. | No AR/Board's Report/MD&A approval, no AGM notice/record date, no director appointments. Interim dividend declared but with no record/payment/book-closure dates (A2 §6 flag) — a disclosure gap, not a board-agenda item present in this doc. |
| F14 NOTE DRAFTING INCONSISTENCIES | FINDING | F14-01: 115mm (line 110) vs 113mm (line 190) meals, same "since inception" metric, same release (A2 `NUMBER_DISCREPANCY`). |
| F15 ENTITY LIST DIFFS | N.A. | First coverage; no consolidation/subsidiary list and no prior quarter to diff. |
| F16 PRESENTATION REFRAMES | FINDING | F16-01: within-doc reframings (ex-MAT-credit QoQ PAT base; reported +13% headline vs constant-currency-flat). No prior deck exists for dropped-metric diff, so that sub-test is N.A. |
| F17 CONCALL SILENCE AUDIT | N.A. | Not a transcript; no analyst call in this artifact. Notion checklist EMPTY (first coverage), nothing to silence-audit against. |

Status tally: FINDING x5 (F6, F7, F8, F14, F16); N.A. x12; PASS x0. No blanks. GATE A3 = pass.

---

## COMMITMENT REGISTER (from F6)
| commitment | implied date | ref | status word |
|------------|--------------|-----|-------------|
| All retail businesses migrated to Shopify Enterprise ECom platform | Q1 FY27 (in-quarter) | line 145 | completed |
| Shopify "ecosystem of Apps" to accelerate the ECom journey | undated / next several quarters | line 146 | underway (benefit pending) |
| Digital "will continue to be a significant growth engine" via AI-personalization, conversion, disciplined acquisition | ongoing / undated | lines 147-150 | underway |
| Business to "return to its growth trajectory" as external conditions stabilize | conditional / undated | lines 136-137 | intends to (conditional) |

Milestone note for Role 5: the Shopify migration is the one dateable, status-changed ("completed this quarter") commitment. Next quarter must show ECom acceleration evidence or it converts to a promise-vs-delivery miss.

---

## A4 HANDOFF — findings flagged for management questions
- FORWARD-SIGNAL: F7-01 (constant-currency revenue flat — FX-only growth), F6-01 (Shopify migration completed; where is the promised acceleration).
- AMBIGUOUS (lean bear, generate a question): F8-01 (MAT-credit-excluded PAT base masks a ~39% sequential PAT decline; is Q1FY27 PAT clean; normalised ETR), F16-01 (headline optics vs constant-currency reality).
- NEUTRAL-FACT (log, no question required): F14-01 (115mm vs 113mm meals drafting inconsistency).

```yaml
stage: A3-forensics
company: "VAIBHAVGBL"
quarter: "Q1 FY27"
doctype: "presentation"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/vaibhavgbl-q1fy27/work/forensics_pressrelease_vaibhavgbl_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: N.A.
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: N.A.
  F10: N.A.
  F11: N.A.
  F12: N.A.
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: N.A.
findings:
  - {id: "F7-01", check: "F7", line: "127", classification: "FORWARD-SIGNAL", implication: "Reported +13% YoY revenue is FX-driven; constant currency broadly flat — next quarter headline at risk without FX tailwind."}
  - {id: "F8-01", check: "F8", line: "91", classification: "AMBIGUOUS", implication: "Q4FY26 PAT base excludes Rs 47.6 cr MAT credit; reported-basis sequential PAT down ~39% QoQ, not +29%. Earlier-years tax item; normalised ETR not derivable."}
  - {id: "F16-01", check: "F16", line: "84", classification: "AMBIGUOUS", implication: "Within-doc reframings flatter the read: ex-MAT-credit QoQ PAT base and reported-growth headline over constant-currency-flat reality."}
  - {id: "F6-01", check: "F6", line: "145", classification: "FORWARD-SIGNAL", implication: "Shopify Enterprise migration completed in-quarter with promised acceleration; Role 5 must verify the ECom acceleration next quarter."}
  - {id: "F14-01", check: "F14", line: "110", classification: "NEUTRAL-FACT", implication: "115mm vs 113mm meals for the same since-inception metric in one release; drafting-control governance data point, immaterial to financials."}
forward_signals: ["F7-01", "F6-01"]
ambiguous: ["F8-01", "F16-01"]
commitments:
  - {commitment: "All retail businesses migrated to Shopify Enterprise ECom platform", implied_date: "Q1 FY27 in-quarter", ref: "line 145", status_word: "completed"}
  - {commitment: "Shopify app ecosystem to accelerate ECom journey", implied_date: "undated", ref: "line 146", status_word: "underway"}
  - {commitment: "Digital to remain a significant growth engine via AI personalization and disciplined acquisition", implied_date: "ongoing", ref: "lines 147-150", status_word: "underway"}
  - {commitment: "Return to growth trajectory as external conditions stabilize", implied_date: "conditional", ref: "lines 136-137", status_word: "intends"}
gate_a3: pass
blank_checks: []
```
