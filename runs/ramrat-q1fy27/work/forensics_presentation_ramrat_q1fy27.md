# A3 FORENSIC NOTES — Ram Ratna Wires Ltd (RAMRAT) — Q1 FY27 — DOCTYPE: PRESENTATION (investor deck)

Source extract: `runs/ramrat-q1fy27/work/extract_presentation_ramrat_q1fy27.txt`
Reconciliation contract: `runs/ramrat-q1fy27/work/ledger_presentation_ramrat_q1fy27.md`
Ledger reconciliation: 100% — every slide row in Section A, every numeric data point in Section B (530 across 31 slides), all footnotes (Section C), and Sections D/E read at cited lines before judging.
Prior-quarter deck: none (first quarterly run). DROPPED_SLIDE and ENTITY_CHANGE NOT COMPUTABLE this quarter — noted, not silently skipped.

Doctype scope: this is a management-framed investor deck, not a Reg 33 statement. Auditor-dependent checks (F4 unaudited-contribution, F5 EoM scope, standalone-vs-consolidated decomposition F2/F3, OCI F9, Board-Outcome/AGM F13, entity-list diff F15) are N.A. and marked so. The deck DOES carry a full historical consolidated P&L (Slide 29), balance sheet (Slide 30), ratio slides (Slide 28) and segment revenue mix (Slide 6), so F1/F6/F7/F8/F10/F11/F14/F16/F17 are run against those.

Revision note (post-A5): FND-12 added to resolve an orphan A2 ledger flag (Section E / Slide 27 detail item 22 — dividend `LABEL_AMBIGUITY`) that A2 deferred to A3/A4 and the first A3 pass had folded into FND-05 rather than surfacing as its own finding. All prior findings retained intact.

---

## FINDINGS TABLE

| id | check | ledger row ref | slide / line | verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| FND-01 | F1 | Slide 29 P&L, "Exceptional items"; ledger `EMERGING_LINE_ITEM` (Sec E) | Slide 29, line 844 | "Exceptional items 3.6 0.0 0.0 0.0" | AMBIGUOUS | First non-zero exceptional item in four years (nil FY23-FY25), nature undisclosed on deck; it reduces PBT from 156.5 to 153.0. Could be a one-off charge or the start of a recurring line. A4 question on nature/recurrence. |
| FND-02 | F6 | Slide 10 milestones; Slide 21 footprint | Slide 10, lines 281/285/299/302/300; Slide 21, lines 618-619/621 | "Adding 3,600 MTPA at Silvassa, targeted for commissioning in March 2027"; "Approval by NCLT for the merger of GCPL into RRWL"; "Production Successfully Commenced at Bhiwadi Unit" | FORWARD-SIGNAL | Dated/dateable commitments feed the promise-vs-delivery tracker (see COMMITMENT REGISTER). Silvassa Mar-2027 is the near catalyst; GCPL merger effectiveness and Vadodara 40->80 towers/month are open milestones. |
| FND-03 | F8 | Slide 29, "Total Tax Expense" / "Profit before tax" | Slide 29, lines 846 / 845 | "Total Tax Expense 44.4 ... Profit before tax 153.0" | AMBIGUOUS | Consolidated ETR 29.0% FY26 (44.4/153.0) vs 25.17% statutory, and rising: FY24 26.8%, FY25 27.8%, FY26 29.0%. Deck shows aggregate tax only, no reconciliation. Against the (undisclosed) Sec 132 / Sec 148 contingent-tax overhang this is a bear-leaning open item. |
| FND-04 | F10 | Slide 30, "Equity Share Capital" | Slide 30, line 854 | "Equity Share Capital 46.7 22.0 22.0 22.0" | AMBIGUOUS | Paid-up capital jumps 22.0 -> 46.7 (+24.7). The stated 1:1 bonus (Slide 10) explains only +22.0 (22.0 -> 44.0); a residual +2.7 Cr is unreconciled on the deck (merger-consideration shares? fresh issue?). No EPS anywhere in the deck to test basic-vs-diluted spread. A4 question. |
| FND-05 | F14 | Slide 27 dividend footnote; Slide 6 labels; ledger `LABEL_AMBIGUITY` (Sec E) | Slide 27, lines 778 / 789; Slide 6, lines 173 / 186 | "5.0#" vs "# Rs. 2.50 Special interim & Rs 2.50 final dividend for FY23-24."; "Enamelled" (l.173) vs "Enameled" (l.186) | NEUTRAL-FACT | Individually immaterial drafting inconsistencies (hash attached to FY26 dividend bar but footnote relates to FY23-24; entity/product-name casing; "Singnificantly" l.574). Cumulatively a disclosure-quality/governance data point, consistent with the active FLAG-GOVERNANCE. (Dividend-specific contradiction escalated to its own finding FND-12.) |
| FND-06 | F16 | Slide 5 quarterly panel; Slide 7 P&L table | Slide 5, line 123; Slide 7, lines 206 / 209 / 212 | "1,752.9 1,853.3 ... 93.2 89.6 ... 39.2 35.2"; "GP % 8.9% 9.8% ... 9.6% 10.1%" | FORWARD-SIGNAL | Deck headlines YoY banners (+89% rev, +109% EBITDA, +121% PAT) while sequential (Q4 FY26 -> Q1 FY27) deteriorates: EBITDA 93.2 -> 89.6 (-3.9%), PAT 39.2 -> 35.2 (-10.2%), EBITDA margin 5.3% -> 4.8%, GP% 8.9% is the LOWEST of every period shown (vs 9.6% QoQ, 9.8% YoY, 10.1% FY26). Revenue up +5.7% QoQ but profit down = margin compression management does not narrate. |
| FND-07 | F16 | Slide 28 Net Debt/Equity + footnote formula; Slide 30 current borrowings | Slide 28, lines 804 / 822; Slide 30, line 867 | "0.46"; formula "= (Non-current Borrowings + Non-current Lease Liabilities- Cash..." ; "(i) Borrowings 388.8 105.2 125.2 169.5" | FORWARD-SIGNAL | The 0.46x "Net Debt/Equity" is defined to EXCLUDE current borrowings — the exact line that quadrupled Mar-25 -> Mar-26 (105.2 -> 388.8). Include current debt: net debt approx (265.3+388.8+21.0 leases - 13.8 cash) approx 661 Cr / 584.9 equity approx 1.1x, not 0.46x. Metric definition suppresses the fastest-growing liability. Selective-metric framing with real leverage understated ~2.4x. |
| FND-08 | F16 | Slide 5 second panel; ledger `LABEL_AMBIGUITY` (Sec B, Slide 5) | Slide 5, lines 144 / 146 / 153 | "5,176.6 ... H1FY25 ... H1 ... FY25 FY26" | AMBIGUOUS | Second panel carries "H1"/"H1FY25" labels but the values printed (5,176.6 / 263.6 / 108.6 and 3,676.7 / 156.3 / 70.2) are the FULL-YEAR FY26/FY25 figures from Slide 29, not half-year actuals. Either mislabelled or an H1 comparison is implied and absent. A reader could take a full-year figure for a 6-month run-rate. A4 clarification. |
| FND-09 | F16 | Slide 30 BS (no CFO/WC-days slide anywhere in deck) | Slide 30, lines 871 / 868 / 873 | "(ii) Trade receivables 640.6 390.1 ..."; "Inventories 486.1 233.7 ..."; "Cash and cash equivalents 7.8 1.7 ..." | FORWARD-SIGNAL | No cash-flow statement and no working-capital-days slide anywhere in 31 slides, while the deck's OWN balance sheet shows receivables +64% (390.1->640.6), inventory +108% (233.7->486.1) against just 7.8 Cr cash — funded by the +270% current-borrowings and +54% payables surge. Deck frames "Robust Growth Trajectory" (Slide 27) while omitting cash conversion. Directly corroborates active FLAG-CASH INDETERMINATE. |
| FND-10 | F16 | Slide 6 revenue mix + commentary | Slide 6, lines 181 / 189 | "Copper Tubes & Pipes share improved significantly from 14% to 26% ... positioning the portfolio for long-term growth and profitability." | AMBIGUOUS | Copper-tubes framed purely positively as a % mix gain with NO absolute Rs given, and the correlative enamelled-wire mix fall (84% -> 72%) unremarked. Mix % rises partly because copper is higher-Rs/kg, not necessarily higher-margin (GP% actually fell, FND-06). A4: absolute copper-tubes revenue and its segment margin. |
| FND-11 | F17 | Notion monitoring checklist vs full deck | Slides 6 / 28 / 30 (silence); see SILENCE AUDIT | (absence — no quote; see table) | CONFIRMATORY-NEGATIVE / FORWARD-SIGNAL | Deck is silent on CFO/WC-days, copper-tubes absolute Rs, off-BS supplier-finance Rs 647 Cr / factoring Rs 187 Cr, Sec 132/148 contingent tax, and CTC/HVDC Q2 CY2026 commercial start — every one a monitored deteriorating/unresolved metric. Sustained silence on a deteriorating metric is a confirmatory negative (Role 5). Baseline count = 1 quarter. |
| FND-12 | F14 | Slide 27 dividend bar + footnote; ledger Sec E / Slide 27 detail item 22 `LABEL_AMBIGUITY` (orphan A2 flag) | Slide 27, lines 778 / 781 / 785 / 789 | Bar: "108.6                             5.0#" (l.778); other bars "54.6 ... 2.5           2.5" (l.781) under axis "FY24         FY25   FY26" (l.785); footnote: "# Rs. 2.50 Special interim & Rs 2.50 final dividend for FY23-24." (l.789) | AMBIGUOUS | CONTRADICTORY on its face: the "#" hash sits on the FY26 dividend-per-share bar (5.0#), yet the footnote it points to attributes that Rs 5.00 (Rs 2.50 special interim + Rs 2.50 final) to FY23-24, not FY26. The FY24 and FY25 bars each read 2.5. So either (a) the Rs 5.0 is plotted against the wrong (FY26) column and actually belongs to FY23-24, making FY26's true DPS unstated on the deck, or (b) the footnote year is mis-typed. Cannot be resolved from the deck. Forward implication: the FY26 dividend/payout/yield the deck implies (Rs 5.0/share, an apparent 2x step-up over the 2.5 shown for FY24/FY25) may be overstated or misattributed; A4 must confirm the actual FY26 declared DPS and the year the Rs 5.0 pertains to against board/AGM dividend records before any payout ratio or yield is carried into the thesis. |

---

## CHECKLIST SCORECARD (all 17; one status each)

| Check | Status | One-line basis |
|---|---|---|
| F1 ZERO-VALUE STANDING | FINDING | No all-periods-zero line (ledger confirmed); but "Exceptional items" nil FY23-FY25 then 3.6 FY26, nature undisclosed — FND-01. |
| F2 STANDALONE vs CONSOLIDATED | N.A. | Deck is consolidated-only (header + Slides 5/27/28 "Consolidated"); no standalone column to decompose the S-vs-C gap. |
| F3 SHELL-ENTITY DETECTION | N.A. | No standalone cost lines in deck; cannot compare S-vs-C cost identity. |
| F4 UNAUDITED CONTRIBUTION | N.A. | No auditor's Other Matters in a presentation. |
| F5 GOING CONCERN / EoM | N.A. | No auditor letter; no prior deck to verbatim-diff. |
| F6 FORWARD-COMMITMENT MINING | FINDING | Multiple dated/dateable commitments (Silvassa Mar-2027, GCPL NCLT merger, Bhiwadi commenced, Vadodara 40->80, Tefabo +4%, tech transfer) — FND-02, see COMMITMENT REGISTER. |
| F7 HEDGE PHRASE MINING | PASS | Only generic Safe Harbor boilerplate ("subject to known and unknown risks", Slide 3, l.82-83); no operational hedge newly added on lumpiness/concentration. |
| F8 TAX FORENSICS | FINDING | ETR 29.0% FY26 vs 25.17% statutory, rising FY24->FY26; aggregate tax only — FND-03. |
| F9 OCI FORENSICS | N.A. | Deck P&L (Slide 29) stops at "Profit for the period"/PAT%; no OCI/actuarial line. |
| F10 SHARE COUNT & DILUTION | FINDING | Paid-up 22.0 -> 46.7; 1:1 bonus explains only +22.0, residual +2.7 Cr unreconciled; no EPS shown — FND-04. |
| F11 RESERVES / NET WORTH TIE-OUT | PASS | Other Equity 532.8 + Equity Capital 46.7 + NCI 5.4 = Total Equity 584.9 (Slide 30) ties exactly; no third-party net-worth number in deck to reconcile against. |
| F12 SEGMENT FORENSICS | N.A. | Deck gives revenue mix % only (Slide 6); no segment assets/liabilities/results table — asset/liability trend not computable. (Segment-Rs silence captured under F17.) |
| F13 BOARD OUTCOME | N.A. | Presentation, not a Board Outcome/AGM filing; no director term dates or AGM notice. Board/NCLT actions captured under F6. |
| F14 NOTE DRAFTING INCONSISTENCIES | FINDING | Cumulative drafting/labelling inconsistencies (FND-05) PLUS the dedicated Slide 27 dividend hash-vs-footnote contradiction (FND-12, resolving the orphan A2 flag). |
| F15 ENTITY LIST DIFFS | N.A. | First quarterly run; no prior-quarter entity list baseline to diff (ledger Sec D confirms NOT COMPUTABLE). |
| F16 PRESENTATION-SPECIFIC | FINDING | Selective YoY-over-QoQ framing (FND-06), net-debt metric excludes current borrowings (FND-07), H1/FY mislabel (FND-08), no cash-flow/WC slide (FND-09), copper-tubes mix framing (FND-10). DROPPED_SLIDE not computable (first run). |
| F17 SILENCE AUDIT | FINDING | Deck silent on CFO/WC, copper-tubes absolute Rs, off-BS financing, contingent tax, CTC/HVDC start — FND-11. |

Blank checks: none. GATE A3: PASS.

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | slide / line ref | status word |
|---|---|---|---|
| Silvassa capacity addition +3,600 MTPA | commissioning March 2027 | Slide 10, lines 281 / 285 | underway (board-approved, "Ongoing capex") |
| Merger of Global Copper Pvt Ltd (GCPL) into RRWL | NCLT-approved, effectiveness pending | Slide 10, line 299 | underway (approved) |
| Bhiwadi copper-tubes unit (24,000 MTPA) production start | achieved (this cycle) | Slide 10, line 302; Slide 15, line 454 | completed ("Production Successfully Commenced") |
| Additional 4% stake in Tefabo (to 64%) | effective 1 July 2025 | Slide 10, lines 300-301 | completed |
| PLI Scheme approval, White Goods (Air Conditioners) | received | Slide 10, lines 295-296 | completed |
| RIPS-2024 approval, Bhiwadi plant | received | Slide 10, lines 297-298 | completed |
| Vadodara wind-tower capacity expansion ~40 -> ~80 towers/month | phased, no end date given | Slide 21, lines 618-619 | underway (phased) |
| European technology transfer / Chikmagalur demo wind turbine | "in progress", no date | Slide 21, line 621 | underway |

---

## SILENCE AUDIT DETAIL (F17 — deck as disclosure surface; consecutive-silence count baselined at 1)

| Monitored item | Deck treatment | Verdict | Qtrs silent |
|---|---|---|---|
| FY27 CFO / working-capital-days (FY26 CFO -96 Cr SA / -93 Cr CN vs PAT 108.6; receivables +64%, inventory +108%) | No CFO statement, no WC-days slide; BS (Slide 30) shows the receivable/inventory buildup but no conversion | SILENT — confirmatory negative | 1 |
| Copper tubes absolute revenue vs Rs 347.20 Cr (Q4 FY26) and the 26% mix claim | Only "26%" mix % given (Slide 6, l.181); no absolute Rs. Implied 26% x 1,853.3 approx 482 Cr but not stated | SILENT on absolute | 1 |
| Off-BS financing: Rs 647 Cr supplier-finance / Rs 187 Cr factoring | Not disclosed as such; trade payables (other) 638.9 Cr shown (l.874) but unlabelled as supplier finance | SILENT | 1 |
| Contingent tax approx Rs 67-104 Cr (Sec 132 search + Sec 148 reassessment) | Not mentioned anywhere; ETR elevated (FND-03) but no contingency narrative | SILENT | 1 |
| CTC/HVDC commercial start near Q2 CY2026 | Not mentioned anywhere | SILENT | 1 |
| Silvassa Rs 86 Cr capex; Bhiwadi 24,000 MTPA ramp | Partially addressed: 3,600 MTPA / Mar-2027 commissioning and Bhiwadi "commenced" stated, but the Rs 86 Cr capex figure is NOT given | PARTIAL | — |

---

## RECONCILIATION NOTE
Every A2 ledger row (Section A slide inventory 31/31, Section B numeric detail 530/530 data points, Section C 8 footnotes, Sections D/E flags) was read at its cited line in the A1 extract before judging. The A2 Slide 27 dividend `LABEL_AMBIGUITY` flag (Section E / Section B item 22) is now carried as its own surfaced finding FND-12 (no longer an orphan). Independent internal cross-checks confirmed: Total Equity tie-out 584.9 (F11); Slide 23 copper-tube capacity 36,000 = Bhiwadi 24,000 + Baroda 12,000; Tefabo 60%+4% = 64%; balance-sheet totals 1,993.5 both sides. No unread rows. ledger_reconciled_pct = 100.

```yaml
stage: A3-forensics
company: "RAMRAT"
quarter: "Q1 FY27"
doctype: "presentation"
model: claude-opus-4-8
status: complete
forensics_path: "runs/ramrat-q1fy27/work/forensics_presentation_ramrat_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: PASS
  F8: FINDING
  F9: N.A.
  F10: FINDING
  F11: PASS
  F12: N.A.
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: FINDING
findings:
  - {id: "FND-01", check: "F1", line: "Slide 29 / line 844", classification: "AMBIGUOUS", implication: "First non-zero exceptional item (3.6) after 3 nil years, nature undisclosed"}
  - {id: "FND-02", check: "F6", line: "Slide 10 / lines 281,285,299,302; Slide 21 / lines 618-621", classification: "FORWARD-SIGNAL", implication: "Dated commitments: Silvassa Mar-2027, GCPL merger, Vadodara 40->80 towers"}
  - {id: "FND-03", check: "F8", line: "Slide 29 / lines 846,845", classification: "AMBIGUOUS", implication: "ETR 29.0% vs 25.17% statutory and rising; contingent-tax overhang undisclosed"}
  - {id: "FND-04", check: "F10", line: "Slide 30 / line 854", classification: "AMBIGUOUS", implication: "Paid-up 22.0->46.7; residual +2.7 Cr beyond 1:1 bonus unreconciled; no EPS"}
  - {id: "FND-05", check: "F14", line: "Slide 27 / lines 778,789; Slide 6 / lines 173,186", classification: "NEUTRAL-FACT", implication: "Cumulative drafting/labelling inconsistencies; disclosure-quality data point"}
  - {id: "FND-06", check: "F16", line: "Slide 5 / line 123; Slide 7 / lines 206,209,212", classification: "FORWARD-SIGNAL", implication: "YoY banners mask QoQ EBITDA -3.9%, PAT -10.2%, GP% 8.9% lowest shown = margin compression"}
  - {id: "FND-07", check: "F16", line: "Slide 28 / lines 804,822; Slide 30 / line 867", classification: "FORWARD-SIGNAL", implication: "Net Debt/Equity 0.46x excludes current borrowings that quadrupled to 388.8; true ~1.1x"}
  - {id: "FND-08", check: "F16", line: "Slide 5 / lines 144,146,153", classification: "AMBIGUOUS", implication: "H1/H1FY25 labels over full-year FY26/FY25 values; mislead risk"}
  - {id: "FND-09", check: "F16", line: "Slide 30 / lines 871,868,873", classification: "FORWARD-SIGNAL", implication: "No CFO/WC-days slide while own BS shows receivables +64%, inventory +108%, cash 7.8 Cr"}
  - {id: "FND-10", check: "F16", line: "Slide 6 / lines 181,189", classification: "AMBIGUOUS", implication: "Copper-tubes mix 14->26% framed positively, no absolute Rs, enamelled fall unremarked"}
  - {id: "FND-11", check: "F17", line: "Slides 6/28/30 (silence)", classification: "CONFIRMATORY-NEGATIVE", implication: "Silent on CFO/WC, copper-tubes Rs, off-BS finance, contingent tax, CTC/HVDC start"}
  - {id: "FND-12", check: "F14", line: "Slide 27 / lines 778,781,785,789", classification: "AMBIGUOUS", implication: "FY26 5.0# DPS bar contradicts footnote attributing Rs 5.0 to FY23-24; which year Rs 5.0 pertains to unresolved; FY26 payout/yield may be overstated - confirm vs board/AGM records"}
forward_signals: ["FND-02", "FND-06", "FND-07", "FND-09", "FND-11"]
ambiguous: ["FND-01", "FND-03", "FND-04", "FND-08", "FND-10", "FND-12"]
commitments:
  - {commitment: "Silvassa capacity +3,600 MTPA", implied_date: "March 2027", ref: "Slide 10 / lines 281,285", status_word: "underway"}
  - {commitment: "GCPL merger into RRWL", implied_date: "NCLT-approved, effectiveness pending", ref: "Slide 10 / line 299", status_word: "underway"}
  - {commitment: "Bhiwadi 24,000 MTPA production start", implied_date: "achieved", ref: "Slide 10 / line 302", status_word: "completed"}
  - {commitment: "Additional 4% Tefabo stake (to 64%)", implied_date: "1 July 2025", ref: "Slide 10 / lines 300-301", status_word: "completed"}
  - {commitment: "PLI White Goods (AC) approval", implied_date: "received", ref: "Slide 10 / lines 295-296", status_word: "completed"}
  - {commitment: "RIPS-2024 Bhiwadi approval", implied_date: "received", ref: "Slide 10 / lines 297-298", status_word: "completed"}
  - {commitment: "Vadodara towers ~40 -> ~80/month", implied_date: "phased, undated", ref: "Slide 21 / lines 618-619", status_word: "underway"}
  - {commitment: "European technology transfer / Chikmagalur demo", implied_date: "undated", ref: "Slide 21 / line 621", status_word: "underway"}
gate_a3: pass
blank_checks: []
```
