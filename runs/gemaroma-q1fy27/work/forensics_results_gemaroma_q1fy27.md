# A3 FORENSIC NOTES — Gem Aromatics Limited (GEMAROMA), Q1 FY27, Doctype: RESULTS (Reg 33)

Source extract: /home/user/inflection-pipeline/runs/gemaroma-q1fy27/work/extract_results_gemaroma_q1fy27.txt (466 lines, 8 pages)
Ledger contract: /home/user/inflection-pipeline/runs/gemaroma-q1fy27/work/ledger_results_gemaroma_q1fy27.md
Prior quarter: NONE (first-time coverage; no diff baseline). Notion checklist: NONE (no prior thesis page).
Unit convention: Rs Millions in filing; conversion x0.1 to Rs Cr. All findings stated in Rs Cr.
Ledger reconciliation: 100% — every ledger row (17 notes, 59 line items, 1 zero-standing, 1 agenda, 11 auditor paras, 2 unique entities / 4 mentions, 5 signature blocks) read at its cited line before judging.

---

## HEADLINE

The forensic story of this filing is one number pair: standalone Q1 FY27 PAT is +7.25 Cr while consolidated Q1 FY27 PAT is a loss of 7.87 Cr (lines 199 vs 395). A year ago the subsidiaries ADDED to earnings (Jun-25: standalone 6.52 Cr, consolidated 7.98 Cr). They have flipped from a +1.46 Cr contribution to a -15.12 Cr drag in twelve months, and dragged full-year FY26 consolidated PAT down to 1.43 Cr against standalone 26.71 Cr. Everything else (FIFO policy change with unascertainable prior-period impact, elevated consolidated ETR, drafting sloppiness) is secondary to the subsidiary bleed.

---

## FINDINGS TABLE

| id | check | ledger row ref | line | verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| FIND-01 | F2 | Consol row 19 (PAT) vs Standalone row 19 (PAT) | 395 / 199 | "(5) Profit for the period/ year (3-4) ... (78.74)" (consol) vs "72.52" (standalone) | FORWARD-SIGNAL | Subsidiaries (Gem Aromatics LLC + Krystal Ingredients) swung from +1.46 Cr contribution (Jun-25) to -15.12 Cr drag (Jun-26); FY26 sub drag = 25.28 Cr. Consolidated is now loss-making at the operating line. A4 must ask WHICH subsidiary is bleeding and whether it is stabilising or accelerating. |
| FIND-02 | F5 | Standalone Note 4 (row 4) / Consol Note 5 (row 13); EoM paras 4 & 5 | 250 / 448-449 | "The impact of the change in accounting policy on prior periods is not ascertainable." | AMBIGUOUS | WAC->FIFO change effective Apr 1 2026, applied prospectively, prior periods NOT restated. Q1 FY27 gross margin is therefore not comparable to any prior period shown, and the change lands in the same quarter consolidated margins collapsed. A4 must ask management to quantify the FIFO-vs-WAC impact on Q1 COGS/margin. |
| FIND-03 | F8 | Consol row 17 (prior-year tax) + rows 16 (deferred) + 13 (PBT) | 391 / 385-392 | "(c) Tax expense relating to prior years   -   (0.19)   -   (6.02)" | FORWARD-SIGNAL | Non-zero prior-year tax adjustment at consolidated (auto-FINDING per F8). Consolidated FY26 ETR = 77.6% (49.39/63.64) vs statutory 25.17%, because loss-making sub earnings are non-deductible against the taxed parent. Large persistent consolidated deferred-tax CREDITS (FY26 6.60 Cr, Q1 FY27 3.33 Cr) are DTA build on losses = future ETR step-up risk when/if losses reverse. |
| FIND-04 | F10 | Standalone row 29 / Consol row 30 (paid-up capital) | 218 / 416 | "104.47   104.47   93.71   104.47" | NEUTRAL-FACT | Paid-up capital rose YoY from 93.71 Cr (Jun-25) to 104.47 Cr, i.e. ~5.38 crore fresh shares of FV Rs 2, tracing to a corporate action (IPO fresh issue; company recently listed, BSE 544491 / NSE GEMAROMA). Basic = Diluted EPS in every period, so no overhang of live dilutive instruments as of this filing. |
| FIND-05 | F14 | Consol Notes rows 9 & 10; entity-order row (section 6) | 425 / 428 / 432 | "These Standalone Financial Results for the quarter ended June 30, 2026" (heading inside the CONSOLIDATED notes block) | NEUTRAL-FACT | Cumulative drafting sloppiness: consolidated Notes 1-2 mislabeled "Standalone"; entity order flips between auditor list and Note 3; typos ("resuits", "Stack Exchange", "gemaromatics.cam"); standalone auditor partner name left blank (line 144) while named on consolidated (line 344). Individually trivial, cumulatively a governance/controls data point for a first-year listed filer. |

---

## CHECKLIST SCORECARD (all 17)

| Check | Status | One-line basis |
|---|---|---|
| F1 ZERO_STANDING | PASS | The 1 zero-standing row is standalone "(c) Tax relating to prior years" (line 194), blank in all 4 periods — a benign template line for prior-year tax true-ups that have not occurred at standalone. (Its consolidated twin DOES carry values — handled in F8/FIND-03.) |
| F2 S-vs-C decomposition | FINDING | FIND-01: PAT gap swung from +1.46 Cr (Jun-25) to -15.12 Cr (Jun-26), ~229% of standalone Q1 PAT, far beyond the 5pp threshold; consolidated cost of materials Jun-26 (99.04 Cr, line 376) alone exceeds consolidated revenue (98.85 Cr, line 370). |
| F3 Shell-entity | PASS | Not shells: consol vs standalone cost lines all materially larger — employee benefits 70.64 vs 30.53M (line 378 vs 179), depreciation 51.27 vs 16.06M (line 380 vs 182). Subsidiaries have substantive (and loss-making) operations, not balance-sheet husks. No Going Concern EoM to reconcile. |
| F4 Unaudited contribution | PASS | Consolidated review para 4 (lines 310-314) lists both subsidiaries as within the review scope; no Other Matters paragraph and no unaudited/component-auditor carve-out disclosed (ledger 5B). Disclosed unaudited contribution = 0%. (Noted: no component-auditor disclosure for the foreign LLC — an observation, no value line to cite.) |
| F5 Going Concern / EoM | FINDING | FIND-02: active EoM in both reports on the WAC->FIFO inventory-policy change; no Going Concern language; no prior quarter to diff, so this is the baseline EoM. The "not ascertainable" prior-period impact (line 250) breaks comparability. |
| F6 Forward-commitment mining | PASS | Lexicon sweep of notes returns no forward-dated management commitments. The only "with effect from April 1, 2026" clause (line 122) is an ALREADY-IMPLEMENTED policy change (status: completed, logged in commitment register); "commenced" (line 56) is board-meeting timing, not a commitment. |
| F7 Hedge-phrase mining | PASS | No strict-lexicon hedges ("no assurance", "subject to", "evaluating", "exploring", "in discussions", "endeavour") added in the notes. The accounting-hedge language ("impracticable", "not ascertainable", lines 245/250) is captured under F5/FIND-02. |
| F8 Tax forensics | FINDING | FIND-03: non-zero consolidated prior-year tax line (line 391); consolidated FY26 ETR 77.6% and Q1 74.9% vs statutory 25.17% (standalone clean ~25.5%); large persistent consolidated deferred-tax credits (DTA build on subsidiary losses). |
| F9 OCI forensics | PASS | Actuarial remeasurement immaterial (<0.1 Cr all periods; standalone Jun-26 0.51M line 203, consol 1.02M line 401). The larger OCI item is FX translation on the foreign sub (Mar-26Q -10.42M line 400), a NEUTRAL-FACT consequence of foreign operations, not a benefit-plan assumption change — no F9 trigger. |
| F10 Share count / dilution | FINDING | FIND-04: paid-up capital 93.71 -> 104.47 Cr YoY (line 218/416) tracing to IPO fresh issue; Basic = Diluted EPS in all periods, no live dilutive spread. |
| F11 Reserves / net-worth tie-out | N.A. | This is a P&L-only Reg 33 results filing; no balance sheet, no Other Equity figure, and no third-party net-worth number (rating rationale / slide) in scope to reconcile against. |
| F12 Segment forensics | N.A. | Single-segment company per Note 3 (line 234) standalone and Note 4 (line 435) consolidated — "single operating segment as per Ind AS 108"; no segment asset/liability tables to trend. |
| F13 Board outcome beyond results | PASS | Sole agenda item is approval of Q1 FY27 results (lines 43-54). No AR/Board's-Report/MD&A approval, no AGM notice/record date, no dividend, no director appointment/resignation, no auditor change, no capital-raising resolution (ledger section 4, grep-confirmed absence). Nothing schedules a Role 6 AR event yet. |
| F14 Note drafting inconsistencies | FINDING | FIND-05: mislabeled consolidated notes ("Standalone", lines 425/428), entity-order flip, typos, blank standalone partner name — cumulative governance data point. |
| F15 Entity-list diffs | PASS | Two subsidiaries only — Gem Aromatics LLC and Krystal Ingredients Pvt Ltd (lines 313-314, 432-433). No prior quarter to diff; both current lists agree on entities and relationship (order differs only, folded into F14). This ledger's entity table is the baseline for next quarter's A2 diff. |
| F16 Presentation-specific | N.A. | Doctype is results, not a presentation deck. |
| F17 Concall silence audit | N.A. | Doctype is results, not a concall transcript; and no prior Notion monitoring checklist exists to audit against (first coverage). |

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note / para ref | status word |
|---|---|---|---|
| Change of inventory valuation method from Weighted Average Cost to FIFO, applied prospectively | Effective April 1, 2026 (in force this quarter) | Standalone Note 4 (lines 236-251) & EoM para 4 (lines 120-128); Consol Note 5 (lines 437-449) & EoM para 5 (lines 316-325) | completed |

No forward-dated (future) management commitments were made in this filing; the register carries the single already-implemented policy change for the Role 5 promise-vs-delivery tracker, whose deliverable to verify next is the quantified margin impact management called "not ascertainable."

---

## NOTES FOR A4 (question generators)

- FORWARD-SIGNAL FIND-01 and FIND-03 and AMBIGUOUS FIND-02 must be converted into management questions.
- Priority question: which of the two subsidiaries (Gem Aromatics LLC, the foreign entity, vs Krystal Ingredients) drove the swing from +1.46 Cr to -15.12 Cr, and is the loss one-off (FX/inventory) or structural? The FX translation loss line (line 400) and the FIFO change (FIND-02) both point at Gem Aromatics LLC as a likely locus.
- Second question: quantify the FIFO-vs-WAC effect on Q1 FY27 consolidated COGS, given cost of materials alone exceeded consolidated revenue this quarter.
- Third question: the 77.6% consolidated ETR and the deferred-tax credit build — how much DTA has been recognised on subsidiary losses, and what is the reversal/step-up path.

```yaml
stage: A3-forensics
company: "GEMAROMA"
quarter: "Q1FY27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/gemaroma-q1fy27/work/forensics_results_gemaroma_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: PASS
  F2: FINDING
  F3: PASS
  F4: PASS
  F5: FINDING
  F6: PASS
  F7: PASS
  F8: FINDING
  F9: PASS
  F10: FINDING
  F11: N.A.
  F12: N.A.
  F13: PASS
  F14: FINDING
  F15: PASS
  F16: N.A.
  F17: N.A.
findings:
  - {id: "FIND-01", check: "F2", line: "395/199", classification: "FORWARD-SIGNAL", implication: "Consolidated Q1 PAT loss 7.87 Cr vs standalone profit 7.25 Cr; subsidiaries flipped from +1.46 Cr to -15.12 Cr YoY; FY26 sub drag 25.28 Cr; identify bleeding subsidiary"}
  - {id: "FIND-02", check: "F5", line: "250", classification: "AMBIGUOUS", implication: "WAC->FIFO change applied prospectively, prior-period impact not ascertainable; Q1 margin not comparable; quantify FIFO effect"}
  - {id: "FIND-03", check: "F8", line: "391", classification: "FORWARD-SIGNAL", implication: "Non-zero consolidated prior-year tax; FY26 ETR 77.6% vs 25.17%; persistent deferred-tax credits = DTA build on losses, future ETR step-up risk"}
  - {id: "FIND-04", check: "F10", line: "218", classification: "NEUTRAL-FACT", implication: "Paid-up 93.71->104.47 Cr YoY from IPO fresh issue; basic=diluted EPS, no live dilutive overhang"}
  - {id: "FIND-05", check: "F14", line: "425", classification: "NEUTRAL-FACT", implication: "Consolidated notes mislabeled Standalone plus typos and blank standalone partner name; cumulative governance/controls data point for first-year filer"}
forward_signals: ["FIND-01", "FIND-03"]
ambiguous: ["FIND-02"]
commitments:
  - {commitment: "Inventory valuation method changed WAC->FIFO, applied prospectively", implied_date: "2026-04-01", ref: "Standalone Note 4 lines 236-251 / Consol Note 5 lines 437-449", status_word: "completed"}
gate_a3: pass
blank_checks: []
```
