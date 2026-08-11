# A3 FORENSIC NOTES — Exicom Tele-Systems (EXICOM) — Q1 FY27 — Doctype: INVESTOR PRESENTATION (38 slides)

Source extract: extract_presentation_exicom_q1fy27.txt (1,102 lines, 38 pages, OCR pages 2/6/11/18/26/35/38).
Ledger: ledger_presentation_exicom_q1fy27.md (mgmt_numbers 758, line_items 76, zero_standing 10, footnotes 21).
Prior context: prior_context.md (Notion, WATCHLIST; pre-committed Q1 FY27 metric = consol EBITDA >=0; actual ~ -Rs22 Cr = BEAR outcome).
Ledger reconciliation: 100% — every Table 1 slide, Table 2 numbers-by-slide, Table 3A-3E line item, Table 4 footnote, and Table 5 limitation read at its cited line before judging.

Doctype applicability (per injected inputs): F16 APPLIES; F6/F10/F11/F12 apply to the extent the deck carries them; F4, F5, F14, F17 are N.A. (no auditor letter, no cash-flow statement, no transcript in a deck). F13/F15 N.A. (no board-outcome resolutions, no consolidation entity list, no prior deck to diff). F1/F2/F3/F8/F9 run because the deck reproduces the full standalone AND consolidated P&L and segment tables.

---

## FINDINGS TABLE

| id | check | ledger row ref | slide / line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| F2-01 | F2 | Tbl2 s19; Tbl3B; prior_context | s19 / L108, L551, L570 | "Consolidated EBITDA (21.9) -6.6%" ; trend "0.1% ... -6.6%" | FORWARD-SIGNAL | Standalone-vs-consol EBITDA gap re-widened to -42.8 Cr (SA +20.9 vs C -21.9) from -29.6 Cr in Q4 FY26; consol EBITDA REVERSED from +0.1% (Q4 FY26 breakeven) to -6.6%. The pre-committed decision metric (consol EBITDA >=0) FAILED — bear outcome. Subsidiary/Tritium+overseas-EVSE drag worsened 13.2 Cr QoQ, steepening the path to the promised Q4 FY27 breakeven. Gap change = 269% of standalone PAT (4.9) — far above the 5pp trigger. |
| F6-01 | F6 | Tbl2 s3; Tbl4 #14 | s3 / L95 | "Breakeven remains on track for Q4 FY27" | FORWARD-SIGNAL | Tritium Q4 FY27 EBITDA-breakeven commitment carried forward with status word UNCHANGED ("remains on track") even though group consol EBITDA reversed from breakeven to -6.6% this quarter (see F2-01). Status word held flat against a deteriorating metric = promise-vs-delivery tension for the Role 5 tracker. |
| F7-01 | F7 | Tbl2 s16, s17 | s16 / L489-494 ; s17 / L521-523 | "Large jump in bookings this quarter as our largest customer accelerated purchasing" ; "delivered to a hyperscale customer" | AMBIGUOUS | Tritium upside is single-customer concentrated: the Q1 bookings jump to $20.8m is attributed to "our largest customer"; GRID-FLEX to one hyperscaler; TRI-FLEX to "the largest US open public charging network." Deck pre-emptively discloses concentration — de-rate/lumpiness risk if that one customer slips. Question for A4. |
| F8-01 | F8 | Tbl3B rows 11,13 | s23 / L725, L727 | "PBT (72.0) ... Tax Expenses 1.5" | AMBIGUOUS | Consolidated tax EXPENSE of +1.5 Cr booked on a pre-tax LOSS of -72.0 Cr: profitable standalone entity pays tax while loss-making subsidiaries (Tritium/overseas EVSE) get NO deferred-tax credit — no DTA recognised on the losses. Deck shows only aggregate tax (no current/deferred split), so recoverability/one-time-credit direction is unresolved. Future ETR/DTA event risk. |
| F11-01 | F11 | Tbl2 s19; prior_context L42-43 | s19 / L574 | "Net Debt : 370.1 Cr at consolidated level" | AMBIGUOUS | Deck states net debt 370.1 Cr but gives NO basis (incl-lease vs ex-lease). Reconciles to prior Q4 FY26 ~Rs378 Cr ex-lease (~2% gap, roughly flat) but is ~43% below the ~Rs649 Cr incl-lease figure. Reconciling item = lease liabilities (~Rs270-280 Cr implied). Basis must be pinned before any net-debt trend claim. Deck carries no balance sheet / net-worth figure, so the reserves tie-out proper is not computable. |
| F12-01 | F12 | Tbl3D rows 5,16 | s25 / L787, L801 | "EV Charger (68.6) ... Segment Liabilities EV Charger 802.5" | FORWARD-SIGNAL | Consolidated EV Charger segment liabilities RISING (659.2 -> 752.3 -> 802.5, +21.7% YoY) while the segment posts a deep -68.6 Cr result. Growing liabilities funding a loss-making build = future external-funding pressure in the EV/Tritium leg. Ties to prior_context gate (b) "no distress/dilutive raise." |
| F12-02 | F12 | Tbl3D row 15; Tbl3C row 15 | s25 / L800 ; s24 / L767 | "Segment Liabilities Critical Power 460.3" (was 585.3) | AMBIGUOUS | Critical Power segment liabilities FELL sharply QoQ — consol 585.3 -> 460.3 (-21.4%), standalone 564.8 -> 449.3 (-20.5%). Per F12 this is WC unwinding OR payables/debt reduction (ambiguous direction). With CP revenue also down QoQ (-10.9%), likely payables unwind on lower volume — flag for concall question on WC durability (echoes carried monitoring Q5). |
| F16-01 | F16 | Tbl4 #9, #20 (ORDER_BOOK_DEFINITION_GAP) | s7 / L200 ; s15 / L476 ; s19 / L574 | "Order Book of Rs +1000 Cr as of 30th June'26" ; "+200Cr including Exports of $2Mn" ; "+1400 Cr (As of 1st July'26)" | AMBIGUOUS | Three order-book/backlog figures at three scopes (Critical Power ~1,000 Cr; consolidated ~1,400 Cr; EVSE ~200 Cr), NO gross/net (of cancellations) or executed/pending definition anywhere in 38 slides, and TWO different as-of dates one day apart (30-Jun vs 1-Jul). The +200 Cr EVSE figure carries no as-of date at all. Undefined backlog = uncheckable book-to-bill; A4 must force a definition. |
| F16-02 | F16 | Tbl2 s3 vs s19 | s3 / L87 vs s19 / L108, L551 | CEO: "-₹22.5 crore" vs KPI: "(21.9)" / "-6.6%" | AMBIGUOUS | The deck states TWO different consolidated-EBITDA figures for the same quarter: CEO narrative "-₹22.5 crore" vs the KPI tile / Key Financials table "(21.9)". 0.6 Cr internal inconsistency — likely a rounding/draft-vintage mismatch, but it is the headline decision metric, so pin which is the reported EBITDA. |
| F16-03 | F16 | Tbl2 s7 vs prior_context L31 (T4) | s7 / L200 | "Order Book of Rs +1000 Cr as of 30th June'26" | FORWARD-SIGNAL | Critical Power order book was a PRECISE Rs1,016 Cr at Q4 FY26 (prior_context T4) and is now presented as a ROUNDED "+1000 Cr." The loss of precision obscures whether the CP book is flat or has slipped BELOW 1,016 Cr. Rounding-down of a previously exact figure is a soft de-emphasis — probe the exact 30-Jun CP backlog. |
| F16-04 | F16 | Ledger Table 5 (DROPPED_SLIDE N/A) | deck-wide | "DROPPED_SLIDE cannot be computed — prior-quarter deck not collected" | NEUTRAL-FACT (limitation) | No prior deck was collected, so dropped/reframed-metric and changed-axis-baseline audits are UNKNOWN, not clean. Do NOT infer "nothing dropped." Collect the Q4 FY26 deck next run to enable the F16 diff. |

---

## CHECKLIST SCORECARD (all 17; one status each)

| Check | Status | One-line basis |
|---|---|---|
| F1 | PASS | 10 ZERO_STANDING rows read (Tbl3A/3B row 12 Exceptional Items; Tbl3C/3D rows 8/9/13/17 unallocable expenditure + unallocated segment assets/liabilities). All are standard reproduced-filing template lines: exceptional-items line dormant this quarter (was 8.9 SA / 12.0 C in Q1 FY26 per VRS/restructuring); unallocated segment buckets dash across all four periods (100% of assets/liabs pushed to the two segments). Nothing new. |
| F2 | FINDING | S-vs-C EBITDA gap re-widened to -42.8 Cr and consol EBITDA reversed from +0.1% to -6.6% — pre-committed metric failed (F2-01). |
| F3 | PASS | Shell test: consol employee cost 50.1 vs SA 25.6 (subs carry ~24.5 Cr payroll) and consol COGS 222.1 vs SA 163.8 (L719, L718) — subsidiaries have substantial real operations (Tritium US + overseas EVSE). No shell entities; no going-concern flag in a deck. |
| F4 | N.A. | No auditor's "Other Matters" / unaudited-contribution disclosure exists in a presentation. Per injected inputs, N.A. |
| F5 | N.A. | No Going Concern / Emphasis-of-Matter paragraph in a presentation; verbatim-diff not possible. Per injected inputs, N.A. |
| F6 | FINDING | Dated forward commitments mined and registered below; Tritium Q4 FY27 breakeven "remains on track" status word held flat despite the consol-EBITDA reversal (F6-01). |
| F7 | FINDING | Pre-emptive customer-concentration disclosure on the Tritium upside — "our largest customer," single hyperscaler, single US network (F7-01). |
| F8 | FINDING | Consol tax +1.5 Cr on -72.0 Cr pre-tax loss; no DTA recognised on subsidiary losses; no current/deferred split disclosed (F8-01). |
| F9 | PASS | Consol OCI Q1 FY27 = -18.7 Cr; standalone OCI only -0.4 Cr, so consol OCI is essentially foreign-currency translation of Tritium/overseas net assets, NOT an actuarial assumption change. |-18.7| < full prior-year OCI +52.8 (FY26), so the F9 "single-quarter swing exceeds full prior year" trigger is NOT breached. Neutral note: OCI dragged consol TCI to -92.2 Cr — FX exposure to watch, not a forensic finding. |
| F10 | PASS | Total shares 13,90,79,771 (13.91 Cr, L1043) ties exactly to the post-rights-issue count in prior_context (12.08 -> 13.91 Cr). Promoter 65.2% / Retail 27.8% / FII 3.9% / DII 3.1% (L1039-1049). Basic = Diluted EPS on both SA (0.35) and consol (-5.29) — no dilutive spread (consol diluted=basic is the anti-dilutive convention on a loss). Limits: single-date snapshot (no QoQ comparison), and NO pledge line disclosed on the deck. |
| F11 | FINDING | Deck carries no balance sheet / net-worth; net-debt 370.1 Cr disclosed with undefined lease basis, reconciling only to the ex-lease prior figure (F11-01). |
| F12 | FINDING | EV Charger segment liabilities rising into a deep loss (F12-01); Critical Power segment liabilities fell -21% QoQ (F12-02). Confirmatory tie-out (clean): deck consol segment results Critical Power 12.8 and EV Charger -68.6 (L786-787) TIE to the results filing (+1,277.25 lakh = 12.77 Cr; -6,859.89 lakh = -68.60 Cr). A2's flagged PBT "discrepancies" also RECONCILE — segment "Total Profit before Tax (A)" is stated post-exceptional (SA Q1 FY26: P&L PBT 1.4 - exceptional 8.9 = -7.5 = segment A; consol Q4 FY26: -48.3 - 0.6 = -48.9 = segment A), so no drafting error. |
| F13 | N.A. | Presentation carries no board resolutions beyond the transmittal note that the Board "approved the Financial Results" (L41-42); no AR/AGM notice, record date, dividend, or director-term dates to schedule against the catalyst window. |
| F14 | N.A. | No auditor letter / statutory notes exist in a deck to cross-check note-vs-letter wording. Per injected inputs, N.A. (entity-name and seg-vs-P&L reconciliations handled under F12). |
| F15 | N.A. | Deck carries no consolidation entity list, and no prior deck was collected — additions/deletions/relationship-change diff not computable. (Context only: prior_context Note 5 — Exicom Power Solutions B.V. now 92.2% held, minority interest exists; not evidenced in this deck.) |
| F16 | FINDING | Order-book definition gap + two as-of dates (F16-01); consol-EBITDA figure inconsistency -22.5 vs -21.9 (F16-02); CP order book rounded down from 1,016 to "+1000" (F16-03); DROPPED_SLIDE audit not computable — limitation (F16-04). |
| F17 | N.A. | No concall transcript in this doctype; silence audit against the 11-item monitoring checklist runs on the concall document, not the deck. Per injected inputs, N.A. |

---

## COMMITMENT REGISTER (F6) — dated / dateable management commitments

| commitment | implied date | slide / line | status word |
|---|---|---|---|
| Tritium EBITDA breakeven | Q4 FY27 | s3 / L95 | "remains on track" (carried, unchanged) |
| GRID-FLEX first system delivered to hyperscaler, operating | since June 2026 | s17 / L521-522 | "has been delivered ... operating since June" (COMPLETED / milestone confirmed) |
| GRID-FLEX 100-unit (~USD 15m) follow-on order | by end-September 2026 | s3 / L94-95 | "supporting a potential ... order" (potential / pending) |
| TRI-FLEX + DC Flex public rollout with largest US network | Q2 CY27 | s3 / L95 ; s17 / L527 | "in lab validation" / "expected in Q2'CY27" (underway) |
| Tritium ~20-30Mn (TRI-FLEX) / ~20Mn (GRID-FLEX) contract award for CY27 | CY27 (secure in 2026) | s17 / L523-525, L532 | "expected to be awarded" / "Subject to successful field trials" (expected, hedged) |
| Hyderabad plant launched with 3x production capacity (2,00,000+ AC / 4,000+ DC chargers p.a., *Expandable) | 2026 | s29 / L879 ; s32 / L963-969 | "Launched" (COMPLETED) |
| Won 140Cr+ DC Power Systems orders to be executed | over FY27 (won Q2 FY27) | s8 / L212-213 | "Won ... to be executed" (won, executing) |
| Win further DC Power Systems orders | Q4 FY27 supply | s8 / L214 | "Expectation to win" (expected) |
| Large Li-ion battery supplies to Leading Tower Company-2 | from Q4 FY27 onwards | s8 / L235 | "Gearing to start" (initiated / preparing) |
| BSNL 4G — 2K sites targeted, ~90 Cr contract value | FY27 (250 sites PO won) | s8 / L224 | "Won 250 sites PO; overall 2K sites targeted" (partly won, targeting) |
| BESS scale-up from >10 sub-50kWh pilots | H2 FY27 | s7 / L197-198 | "ability to scale up in H2 of FY'27" (underway) |
| BESS FY27 targets: ~40% wallet share / Rs150 Cr order book / Rs140 Cr export business | FY27 | s10 / L293 | "TARGET" (target, forward) |
| Export pace to increase | Q2 FY27 | s10 / L288 ; s7 / L192-193 | "Pace of exports to increase" (expected) |
| CPO repeat orders INR 50 Cr+ to be delivered | by Oct 2026 | s15 / L466-469 | "to be delivered by Oct 2026" (confirmed orders) |
| Data Centres (high-C-rate battery) | early-stage, no date | s10 / L297 | "still early-stage; building the solution with partners" (de-scoped, no target) |

Status-transition note for Role 5: the only commitments marked COMPLETED this quarter are the Hyderabad plant launch and the first GRID-FLEX delivery ("has been delivered ... operating since June") — genuine milestone confirmations. Everything else is expected/underway/target. The Tritium Q4 FY27 breakeven status word did not advance and sits against a metric that moved the wrong way this quarter (F2-01/F6-01).

---

## NEEDS_VERIFICATION items carried from A2 — resolved by A3
- s7 orphan superscript "1" after "...Smart Racks" (L190): confirmed — no matching footnote text anywhere on the slide. Truncated/orphan marker; NEUTRAL-FACT drafting artifact, no numeric impact.
- s16 Tritium bookings/revenue quarter pairing (L489-509): bookings $9.9/$9.3/$10.3/$10.3/$20.8, revenue $5.0/$5.0/$4.4/$4.0/$10.4, backlog $23Mn. Q1 FY27 bookings $20.8 / revenue $10.4 confirmed; backlog nearly doubled vs prior_context $12.6M (Q4 FY26) — positive forward signal consistent with T2 on-track.
- s21 EBITDA/PAT gridline-vs-label ambiguity: resolved against the P&L table — consol EBITDA -38.6 / +0.3 / -21.9 and PAT -83.1 / -54.3 / -73.6 map cleanly to Q1 FY26 / Q4 FY26 / Q1 FY27.
- Segment PBT "discrepancies" (-7.5 vs -7.8; -48.9 vs -48.3): RECONCILE via exceptional-item placement (segment "Total PBT (A)" is post-exceptional; P&L "PBT (C)" is pre-exceptional). No error — folded into F12 as confirmatory-clean.

---

## GATE A3
All 17 checks marked exactly one of PASS / FINDING / N.A. No blanks. Ledger reconciled 100%. Gate A3: PASS.

```yaml
stage: A3-forensics
company: "EXICOM"
quarter: "Q1 FY27"
doctype: "presentation"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/exicom-q1fy27/work/forensics_presentation_exicom_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: PASS
  F2: FINDING
  F3: PASS
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: PASS
  F10: PASS
  F11: FINDING
  F12: FINDING
  F13: N.A.
  F14: N.A.
  F15: N.A.
  F16: FINDING
  F17: N.A.
findings:
  - {id: "F2-01", check: "F2", line: "s19/L108,L551,L570", classification: "FORWARD-SIGNAL", implication: "Consol EBITDA reversed +0.1% -> -6.6%; S-vs-C EBITDA gap re-widened to -42.8 Cr; pre-committed decision metric failed; Q4 FY27 breakeven path steepened"}
  - {id: "F6-01", check: "F6", line: "s3/L95", classification: "FORWARD-SIGNAL", implication: "Tritium Q4 FY27 breakeven 'remains on track' status word held flat despite consol-EBITDA deterioration; promise-vs-delivery tension"}
  - {id: "F7-01", check: "F7", line: "s16/L489-494; s17/L521-523", classification: "AMBIGUOUS", implication: "Tritium upside single-customer concentrated (largest customer / one hyperscaler / one US network); lumpiness/de-rate risk"}
  - {id: "F8-01", check: "F8", line: "s23/L725,L727", classification: "AMBIGUOUS", implication: "Consol tax +1.5 Cr on -72.0 Cr loss; no DTA recognised on subsidiary losses; no current/deferred split; future ETR/DTA event risk"}
  - {id: "F11-01", check: "F11", line: "s19/L574", classification: "AMBIGUOUS", implication: "Net debt 370.1 Cr with undisclosed lease basis; reconciles to ex-lease 378 but not incl-lease 649; reconciling item = lease liabilities"}
  - {id: "F12-01", check: "F12", line: "s25/L787,L801", classification: "FORWARD-SIGNAL", implication: "EV Charger segment liabilities rising (659->802) into a -68.6 Cr loss; future external-funding pressure in the EV/Tritium leg"}
  - {id: "F12-02", check: "F12", line: "s25/L800; s24/L767", classification: "AMBIGUOUS", implication: "Critical Power segment liabilities fell -21% QoQ; WC unwind vs debt reduction ambiguous; probe WC durability on lower CP volume"}
  - {id: "F16-01", check: "F16", line: "s7/L200; s15/L476; s19/L574", classification: "AMBIGUOUS", implication: "Three order-book figures, no gross/net or executed/pending definition, two as-of dates one day apart, EVSE figure undated; backlog uncheckable"}
  - {id: "F16-02", check: "F16", line: "s3/L87 vs s19/L108,L551", classification: "AMBIGUOUS", implication: "Two consol-EBITDA figures for same quarter (-22.5 vs -21.9); pin the reported number"}
  - {id: "F16-03", check: "F16", line: "s7/L200", classification: "FORWARD-SIGNAL", implication: "CP order book rounded down from precise 1,016 Cr (Q4 FY26) to '+1000 Cr'; obscures possible flat-to-decline; probe exact 30-Jun CP backlog"}
  - {id: "F16-04", check: "F16", line: "ledger Table 5", classification: "NEUTRAL-FACT", implication: "Prior deck not collected; dropped-metric/axis-baseline audit UNKNOWN not clean; collect Q4 FY26 deck next run"}
forward_signals: ["F2-01", "F6-01", "F12-01", "F16-03"]
ambiguous: ["F7-01", "F8-01", "F11-01", "F12-02", "F16-01", "F16-02"]
commitments:
  - {commitment: "Tritium EBITDA breakeven", implied_date: "Q4 FY27", ref: "s3/L95", status_word: "remains on track"}
  - {commitment: "GRID-FLEX first system delivered/operating at hyperscaler", implied_date: "since Jun 2026", ref: "s17/L521-522", status_word: "delivered (completed)"}
  - {commitment: "GRID-FLEX 100-unit (~USD15m) follow-on order", implied_date: "end-Sep 2026", ref: "s3/L94-95", status_word: "potential"}
  - {commitment: "TRI-FLEX/DC Flex public rollout (largest US network)", implied_date: "Q2 CY27", ref: "s3/L95; s17/L527", status_word: "in lab validation / expected"}
  - {commitment: "Tritium ~20-30Mn CY27 contract award", implied_date: "CY27 (secure 2026)", ref: "s17/L523-525", status_word: "expected (hedged)"}
  - {commitment: "Hyderabad plant launched, 3x capacity", implied_date: "2026", ref: "s29/L879; s32/L963", status_word: "launched (completed)"}
  - {commitment: "140Cr+ DC Power Systems orders execution", implied_date: "over FY27", ref: "s8/L212-213", status_word: "won/executing"}
  - {commitment: "Win further DCPS orders (Q4 FY27 supply)", implied_date: "Q4 FY27", ref: "s8/L214", status_word: "expected"}
  - {commitment: "Large Li-ion battery supplies to Tower Co-2", implied_date: "from Q4 FY27", ref: "s8/L235", status_word: "gearing (initiated)"}
  - {commitment: "BSNL 4G 2K sites / ~90 Cr", implied_date: "FY27", ref: "s8/L224", status_word: "partly won/targeting"}
  - {commitment: "BESS scale-up from pilots", implied_date: "H2 FY27", ref: "s7/L197-198", status_word: "underway"}
  - {commitment: "BESS FY27 targets (40% wallet / 150 Cr book / 140 Cr export)", implied_date: "FY27", ref: "s10/L293", status_word: "target"}
  - {commitment: "Export pace increase", implied_date: "Q2 FY27", ref: "s10/L288; s7/L192", status_word: "expected"}
  - {commitment: "CPO repeat orders INR 50 Cr+ delivery", implied_date: "by Oct 2026", ref: "s15/L466-469", status_word: "confirmed orders"}
  - {commitment: "Data Centres high-C-rate battery", implied_date: "no date (early-stage)", ref: "s10/L297", status_word: "de-scoped"}
gate_a3: pass
blank_checks: []
```
