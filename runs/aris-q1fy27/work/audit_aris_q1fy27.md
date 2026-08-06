# A5 ADVERSARY / COMPLETENESS AUDIT (FINAL RE-AUDIT, post loop 2) — ARIS Q1 FY27
### Model: claude-opus-4-8 | Auditing: review_aris_q1fy27.md
### Fresh context: A4 review + A1 extracts (results, presentation, press release, ESOP) + A2 ledgers only. Re-derived independently.

Scope note: this is the FINAL re-audit after loop 2. The prior pass rejected A4's original F16-1
finding (which read slide-36 bars 1,302/1,774/361 = 3,437 Mn as a Q1FY27 top-line overstatement).
A4 has recharacterized F16-1 as period-label ambiguity. This audit re-derives the segment split
from scratch, verifies the recharacterization is correct AND complete across every location, and
re-runs all four audits for any remaining or new issue. Not a rubber-stamp.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (HARD GATE)

The PLAIN-LANGUAGE BRIEF (review lines 617-704) carries all four labelled parts, each non-empty
and with real content (not placeholders):

| Part | Heading | Lines | Present | Substantive |
|---|---|---|---|---|
| 1 | SUMMARY NARRATIVE | 619-644 | YES | 26 lines; revenue/PAT/margin, one-off composition, QoQ reversal, debtor-days gap, nil-ECL, HELD |
| 2 | SECTOR INTELLIGENCE | 646-663 | YES | construction end-market, ~140-day credit cycle, Maharashtra 65% / EPC 58% concentration |
| 3 | BUSINESS-MODEL INTELLIGENCE | 665-684 | YES | three streams + EBITDA%, parent vs subs economics, GDV-vs-fee, payables-stretch caveat |
| 4 | COMPETITION INTELLIGENCE | 686-704 | YES | full-stack moat claim, Shankara 11.3x peer, Capacite anchor, "software vs underwriting" bear |

GATE: **PASS.** All four present and substantive.

---

## AUDIT 1 — COVERAGE (fresh independent enumeration vs A2 ledgers)

Fresh grep/sweep over both A1 extracts, diffed against the two A2 ledgers.

| Category | A2 count | My fresh count | Orphan rows (in ledger, absent from A4) | Status |
|---|---|---|---|---|
| results: notes | 16 | 16 (std 1-8 l.225-278; consol 1-8 l.552-604) | none — all in 0D table + Step refs | PASS |
| results: line_items | 77 | 77 (std P&L 27 + std IPO 6 + consol P&L 38 + consol IPO 6) | none material uncited | PASS* |
| results: zero_standing | 1 | 1 (equity-method assoc, l.493) | cited (Step 1B, note on associate) | PASS |
| results: agenda_items | 1 | 1 (board approval l.37-44) | cited (Step 0A / cover) | PASS |
| results: auditor_paras | 13 | 13 (std 5 l.84-136; consol 8 l.308-430) | para 6/7 cited (0D, A3-03); all reviewed | PASS |
| results: entities | 8 | 8 (7 subs + assoc, l.359-374) | cited (Step 2C, Q3, Q16) | PASS |
| results: signatures | 5 | 5 | reviewed, no finding (governance context noted) | PASS |
| results: annexures | 4 | 4 | reviewed, no finding | PASS |
| deck: slides | 42 | 42 ([page 1]..[page 42]) | none | PASS |
| deck: slide_numbers | 211 | 211 (accepted; material cells traced) | none material uncited | PASS |
| deck: line_items | 70 | 70 (sl37 16 + sl38 16 + sl39 38) | sl39 BS cited as ND-source; sl37/38 in Step 1-4 | PASS |
| deck: zero_standing | 15 | 15 | reviewed (exceptional dashes, NIL cap) | PASS |
| deck: footnotes | 10 | 10 | Redseer/Valorem/asterisk-mismatch reviewed | PASS |

A3 findings: all 11 results forensics (A3-01..11) + all 9 presentation forensics
(F16-1..7, F6-1, F10-1) are traceable into a Step, a Question (8.5), a monitorable, or a flag
(review lines 27-32, 720). No orphan A3 finding.

Rows my fresh pass found that the ledger lacks: **none.**

\*ONE DATA MISREAD in an existing ledger row (not a missing row; logged in Audit 2 below):
consol Other Expenses Q1FY26 (l.486, ledger Table 2B row 10) is carried as **79.44 Mn (7.94 Cr)**
by both A2 and A4, but the anchored Total Expenses subtotal forces **59.44 Mn (5.94 Cr)**. The
row exists and is flagged OCR-garbled in both ledger and review; this is a value-accuracy issue,
handled in the arithmetic audit, not a coverage orphan.

COVERAGE: **PASS** (no orphan rows; no rows missing from ledger).

---

## AUDIT 2 — ARITHMETIC (every derived metric recomputed from raw l./sl. numbers)

Unit: Rs Cr = Mn x 0.1. All consolidated unless noted.

| Metric | A4 value | My recompute | Source | Status |
|---|---|---|---|---|
| Op EBITDA Q1FY27 (PBTbe+D&A+Fin-OI) | 30.55 | 26.67+1.90+6.36-4.38 = 30.55 | l.490/484/485/476 | OK |
| Op EBITDA Q1FY26 | 18.16 | 9.19+0.76+11.74-3.53 = 18.16 | l.490/484/485/476 | OK |
| Op EBITDA Q4FY26 | 30.47 | 28.74+1.66+6.13-6.06 = 30.47 | l.490/484/485/476 | OK |
| Op EBITDA FY26 | 100.68 | 81.13+4.15+27.89-12.49 = 100.68 | l.490/484/485/476 | OK |
| Op EBITDA margin Q1FY27 | 10.51% | 30.55/290.81 = 10.51% | derived/l.475 | OK |
| Op EBITDA margin Q1FY26 | 8.56% | 18.16/212.08 = 8.56% | derived/l.475 | OK (deck 8.58% on rounded 182) |
| Margin expansion YoY | +195 bps | 10.51-8.56 = 1.95pp | derived | OK (deck +191 on rounded inputs) |
| ETR Q1FY27 | 24.9% | 6.64/26.67 = 24.9% | l.508/502 | OK |
| ETR Q1FY26 | 19.0% | 1.20/6.31 = 19.0% | l.508/502 | OK |
| ETR Q4FY26 | 24.7% | 7.09/28.74 = 24.7% | l.508/502 | OK |
| ETR FY26 | 23.3% | 18.27/78.55 = 23.3% | l.508/502 | OK |
| PAT margin Q1FY27 | 6.89% | 20.03/290.81 = 6.89% | l.510/475 | OK (deck 6.88% on rounded) |
| Revenue YoY | +37.1% | 290.81/212.08 -1 = +37.1% | l.475 | OK |
| Op EBITDA YoY | +68.2% | 30.55/18.16 -1 = +68.2% | derived | OK (deck +67.6% on rounded) |
| Finance cost YoY | -45.8% | 6.36/11.74 -1 = -45.8% | l.485 | OK |
| Core Op PBT ex-OI YoY | +293.8% | 22.29/5.66 -1 = +293.8% | derived | OK |
| Reported PBT YoY | +322.7% | 26.67/6.31 -1 = +322.7% | l.502 | OK |
| PAT YoY | +291.9% | 20.03/5.11 -1 = +291.9% | l.510 | OK |
| Diluted EPS YoY | +279.6% | 2.05/0.54 -1 = +279.6% | l.542 | OK |
| Revenue QoQ | -15.3% | 290.81/343.36 -1 = -15.3% | l.475 | OK |
| PAT QoQ | -7.5% | 20.03/21.65 -1 = -7.5% | l.510 | OK (deck -7.8% on 200/217) |
| Diluted EPS QoQ | -20.5% | 2.05/2.58 -1 = -20.5% | l.542 | OK |
| D&A YoY | +150.0% | 1.90/0.76 -1 = +150% | l.484 | OK |
| S-vs-C PAT % Q1FY27 | 37.2% | 7.46/20.03 = 37.2% | l.206/510 | OK |
| S-vs-C PAT % Q4FY26 | 68.9% | 14.92/21.65 = 68.9% | l.206/510 | OK |
| S-vs-C PAT % Q1FY26 | -93.5% | (4.78)/5.11 = -93.5% | l.206/510 | OK |
| S-vs-C PAT % FY26 | 41.3% | 24.91/60.29 = 41.3% | l.206/510 | OK |
| Subsidiary PAT % of S Q1FY27 | 168.5% | 12.57/7.46 = 168.5% | derived | OK |
| Unreviewed subs rev share | 55.7% | 1,620.83/2,908.09 = 55.7% | l.388/475 | OK |
| Unreviewed subs PAT share | 63.5% | 127.28/200.31 = 63.5% | l.388/510 | OK |
| Standalone rev % of consol | 44.3% | 128.73/290.81 = 44.3% | l.180/475 | OK |
| Standalone Op EBITDA Q1FY27 | 7.62 | 9.75+1.36+4.81-8.30 = 7.62 | l.194/189/190/181 | OK |
| Standalone ETR Q1FY27 | 23.5% | 2.29/9.75 = 23.5% | l.204/198 | OK |
| Receivable days FY26 | 140 | 4,100/10,675x365 = 140.2 | sl39 L1152/L1089 | OK |
| PAT bridge: EBITDA impr | +12.39 | 30.55-18.16 = 12.39 | derived | OK |
| PAT bridge: finance | +5.38 | 11.74-6.36 = 5.38 | l.485 | OK |
| PAT bridge: D&A | (1.14) | 1.90-0.76 = 1.14 | l.484 | OK |
| PAT bridge: OI | +0.85 | 4.38-3.53 = 0.85 | l.476 | OK |
| PAT bridge: exceptional | +2.88 | 28.81 Mn x0.1 | l.500 | OK |
| PAT bridge: PBT change | +20.36 | 26.67-6.31 = 20.36; sum of components = 20.36 | l.502 | OK (bridge closes) |
| PAT bridge: tax | (5.44) | 6.64-1.20 = 5.44 | l.508 | OK |
| PAT bridge: PAT change | +14.92 | 20.03-5.11 = 14.92 | l.510 | OK (closes) |
| **Consol Other Exp Q1FY26** | **7.94** | **2,064.18-(1,790.21-4.05+93.63+7.57+117.38)=59.44 Mn = 5.94** | l.487/480-485 | **DISCREPANCY** |

Every DERIVED METRIC recomputes within rounding. The one discrepancy is a **raw line-item
misread**, not a derived metric:

- **Consol Other Expenses Q1FY26 = 5.94 Cr, not 7.94 Cr.** A2 read OCR glyph ",9-44" (l.486) as
  79.44; the anchored, un-garbled Total Expenses subtotal 2,064.18 Mn (l.487) forces 59.44 Mn.
  A4 inherited A2's 7.94.
- **Materiality / propagation: NONE.** A4 explicitly flags this line OCR-garbled/suspect across
  all periods (review l.162-164) and derives every EBITDA/margin/bridge figure from the
  subtotals (PBT-bef-exc, D&A, Finance, OI), never from the Other Expenses line. Q1FY26 Op
  EBITDA (18.16) and every downstream metric are correct. No conclusion moves.
- **Disposition:** logged as a correction to be applied before Notion save (A2 to fix the ledger
  cell to 59.44 Mn; A4 to fix the Step 1B table cell to 5.94 Cr). Because it sits on an
  already-flagged OCR-garbled line, is fully resolvable, and propagates to zero derived metrics
  or conclusions, it does NOT trigger the arithmetic-FAIL gate (which is defined over derived
  metrics) and does not block the verdict.

ARITHMETIC (derived metrics): **PASS.** One non-propagating raw-input misread flagged for
correction (Other Exp Q1FY26 consol: 7.94 -> 5.94).

---

## AUDIT 2B — F16-1 RECHARACTERIZATION VERIFICATION (re-derived independently)

The recharacterization claim under audit: slide-36 bars 1,302/1,774/361 (sum 3,437) are the
Q4FY26 column, NOT Q1FY27; true Q1FY27 = 1,092/1,540/277 = 2,909 ~ reported 2,908.09; therefore
NO top-line overstatement, only period-label ambiguity (+ Services axis mislabel F16-2).

I re-derived the bar-to-axis mapping from scratch (bar values cannot be assigned by text-order;
they must be reconciled to reported totals and to the independent single-segment slides):

| Column (x-axis) | B2B | CM | Services | Sum (Mn) | Reported rev (l.475) | Reconciles? |
|---|---|---|---|---|---|---|
| Q1FY26 (left) | 1,095 | 839 | 187 | 2,121 | 2,120.82 | YES |
| Q4FY26 (mid) | 1,302 | 1,774 | 361 | 3,437 | 3,433.57 | YES |
| **Q1FY27 (right)** | **1,092** | **1,540** | **277** | **2,909** | **2,908.09** | **YES** |

Decisive independent corroboration (does not depend on slide 36 at all):
- B2B Q1FY27 = 1,092 — slide 26 L767 (standalone segment slide)
- CM Q1FY27 = 1,540 — slide 27 L786; press release "1,540 from 839, +83%"
- Services Q1FY27 = 277 — slide 29 L847; press release "277 from 187, +48%"

All three single-segment slides confirm Q1FY27 = 1,092/1,540/277 = 2,909, matching reported
2,908.09. The 1,302/1,774/361 bars therefore MUST be Q4FY26 (sum 3,437 ~ reported 3,433.57).
The A2 ledger's line-1025 attribution of "1,302/1,774/361 (Q1-FY27)" is a text-extraction-order
artifact (tallest labels transcribed first); A4 correctly overrode it by reconciliation.
Mix check: 1,092/1,540/277 over 2,908 = 37.6% / 53.0% / 9.5%, matching slide-10 mix 37%/53%/10%.

Verdict on recharacterization: **CORRECT.** There is no Q1FY27 top-line overstatement; the
defect is period-label ambiguity plus the Services x-axis mislabel (Q3-FY26 where Q4-FY26 is
meant, F16-2). Read correctly, 3,434 -> 2,908 corroborates the -15.3% QoQ decline (F16-6).

Completeness of the recharacterization across the review (must be consistent everywhere):
- Step 3 segment reconciliation note (l.299-312): recharacterized, correct. OK
- Step 8.5 Q8 (l.571): "period-label ambiguity — NOT a top-line gap". OK
- Step 8.5 Q9 (l.572): Services axis mislabel F16-2 carried separately. OK
- Flag block (l.769): "RECONCILES ... No top-line overstatement ... bars are the Q4FY26 column". OK
- YAML questions_for_management F16-1 (l.738): matches. OK

No residual location still asserts a top-line overstatement. Revenue is 290.81 Cr (2,908 Mn)
uniformly throughout (Steps 1-6, brief, YAML). Recharacterization is COMPLETE.

---

## AUDIT 3 — ADVERSARIAL READ (three most-positive claims, strongest bear from same extract)

**Claim 1 — "Op EBITDA margin expanded to 10.51%, +195 bps YoY; genuine mix-driven expansion"
(Step 1C/2A, watchlist #4 GREEN).**
Bear counter (same extract): QoQ, Op EBITDA is flat 30.47->30.55 (l.484-490) BUT Q4FY26 was
struck after a 4.46 Cr ECL charge and Q1FY27 after ZERO ECL (l.482); ex-ECL, underlying
operating EBITDA deteriorated ~4.5 Cr QoQ. The margin optics are flattered by the vanished
provision line, on a ~140-day book.
Survives? YES — but ALREADY GRAFTED by A4 (Step 3 l.296-297, A3-05, flags l.762/766). No new
insertion required.

**Claim 2 — "Revenue +37.1% YoY; CM +83% and DaaS +48% growth triggers on track" (Step 2A/6D).**
Bear counter (same extract): revenue is -15.3% QoQ off a Q4 peak that is itself a note-5
balancing figure (l.241/567); the sequential trend decelerates. DaaS "pipeline" is GDV
(18,391 Mn gross), on which ARIS earns only a 10-14% fee (sl.29 L857), so headline pipeline
overstates ARIS revenue by ~7-10x.
Survives? YES — but ALREADY GRAFTED (Step 3 QoQ, Step 6D "GDV not revenue" F16-5, Q7).

**Claim 3 — "PAT +291.9% (~4x); near net-cash (ND/E 0.02); finance costs -46%" (Step 2A/6A).**
Bear counter (same extract): ~40% of the +20.36 Cr PBT uplift is one-time (finance-cost reset
+5.38 from IPO debt repayment; absent Q1FY26 exceptional +2.88 = +8.26 Cr, Step 4). Standalone
core PBT ex-OI is negative in 3 of 4 periods (Step 1C); 63.5% of consol PAT sits in 7
subsidiaries MSKC did not review (l.387). ND/E 0.02 basis is unlabeled/single-quarter (F16-4).
Survives? YES — but ALREADY GRAFTED (Step 4, 6A "annualised-EPS INVALID" l.436-451, flags
l.763/766/767).

Result: the three strongest bear counters are all present in A4's review already (consistent
with this being the post-loop-2 re-audit; A4 has absorbed the adversarial content). **No NEW
surviving bear counter requires grafting.**

Additional adversarial probe (fresh, to avoid rubber-stamping): FY26 non-current "Loans and
advances" jumped 5 -> 1,685 Mn (sl.39 L1136) and "Other non-current assets" nil -> 633 Mn
(L1142) — large non-receivable capital extended, consonant with the "disguised-NBFC" frame. This
is an FY26 historical-balance-sheet item (no Q1FY27 BS exists) and falls inside the cash-quality
INDETERMINATE bucket A4 already flags and caps the verdict on (Step 5). It is an observation for
the H1 FY27 balance sheet, not a new surviving counter that changes this quarter's verdict.

---

## VERDICT

**COMPLETE.**

- Deliverable gate: PASS (all four brief parts present, substantive).
- Coverage: PASS (16/77/1/1/13/8/5/4 results; 42/211/70/15/10 deck — all reconcile; no orphan
  rows; no rows missing from ledger).
- Arithmetic (derived metrics): PASS (Op EBITDA, margins, ETR, S-vs-C gaps, YoY/QoQ, PAT bridge
  all recompute within rounding; bridge closes).
- F16-1 recharacterization: VERIFIED CORRECT and COMPLETE (Q1FY27 split 1,092/1,540/277 = 2,909
  ~ reported 2,908.09, independently confirmed by slides 26/27/29; 1,302/1,774/361 = 3,437 is the
  Q4FY26 column ~ reported 3,433.57; no top-line overstatement; consistent across Step 3, Q8/Q9,
  flag, YAML).
- Adversarial: three strongest bear counters already incorporated; none newly surviving.

One non-blocking correction to apply before Notion save (does NOT change the verdict, propagates
to no derived metric or conclusion, sits on an already-OCR-flagged line): consolidated Other
Expenses Q1FY26 should read **5.94 Cr / 59.44 Mn** (forced by the anchored Total Expenses
2,064.18 Mn), not 7.94 Cr / 79.44 Mn. Fix in A2 ledger Table 2B row 10 and A4 Step 1B table.

Only COMPLETE proceeds to save. Save may proceed after the one-cell correction above.

```yaml
stage: A5-adversary
company: "ARIS"
quarter: "Q1 FY27"
model: claude-opus-4-8
status: complete
verdict: COMPLETE
plain_language_brief:
  narrative: present
  sector: present
  business_model: present
  competition: present
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches:
  - {metric: "Consolidated Other Expenses Q1FY26 (raw line, non-propagating; on OCR-flagged line l.486)", a4_value: "7.94 Cr (79.44 Mn)", recomputed: "5.94 Cr (59.44 Mn)", source_line: "results l.487 Total Expenses 2,064.18 forces l.486 = 59.44 Mn; A2 ledger Table 2B row 10 misread"}
surviving_bear_counters: []
loop_back_to: ""
gap: ""
```
