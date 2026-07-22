# A3 FORENSIC NOTES — HFCL Q1FY27 — DOCTYPE: PRESENTATION (22-slide Earnings Presentation)

Company: HFCL Limited | Quarter: Q1FY27 (ended 30-Jun-2026) | Doctype: presentation
A1 extract: /home/user/inflection-pipeline/runs/hfcl-q1fy27/work/extract_presentation_hfcl_q1fy27.txt
A2 ledger: /home/user/inflection-pipeline/runs/hfcl-q1fy27/work/ledger_presentation_hfcl_q1fy27.md
Ledger reconciliation: 100% (313/313 numeric tokens, 18/18 income-statement line items, 15/15 footnotes read at cited lines).
Doctype scoping: F16 applies; F6/F10/F11 run against the numbers the deck actually carries; F2-F5, F11 (net-worth), F12, F13, F15, F17 are N.A. (full-filing / concall / balance-sheet content absent from an investor deck) and are marked so with basis.

NOTE ON CHART LABELS: slides 7, 9, 20 carry CHART_LABEL_INFERRED per A2. Bar/pie label-to-slice mapping in pdftotext -layout is scattered; findings that depend on it are hedged and cross-checked against a second on-slide figure wherever one exists (esp. the F16-02 promoter reconciliation, which is anchored to the deck's own "% FREE-FLOAT 71.69%").

---

## FINDINGS TABLE

| id | check | ledger row ref | line/slide | verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| F1-01 | F1 | Table 3 row 10 (ZERO_STANDING) | slide 8, line 253 | "Exceptional Items  -  -  -" | NEUTRAL-FACT | Row stands empty across all 3 periods. Template slot the company keeps live; the "proposed aerospace business being acquired" (slide 15/18) is the transaction class most likely to populate it (acquisition one-offs, fair-value/bargain-purchase, integration charges). Watch this line the quarter the SPA closes. |
| F6-01 | F6 | Table 4 rows 4,13,14 + slide 14/17/18 body | slides 5,14,17,18 (lines 162,449-457,536-546,570,578) | "we will continue to strengthen... expand our global presence"; "expected to meaningfully enhance operating performance... as serial production commences" | FORWARD-SIGNAL | Ten dated/dateable management commitments extracted into the Commitment Register below. These feed the Role 5 promise-vs-delivery tracker and FTTCP catalyst timeline. |
| F7-01 | F7 | Table 4 row 4 (HEDGE_PHRASE) | slide 5, line 162 | "increased our FY27 revenue growth aspiration to the best of our estimates to 40%" | AMBIGUOUS | The headline 40% FY27 growth number is triple-hedged ("aspiration", "best of our estimates"), not committed guidance. Direction of the hedge is unresolved: sandbagging or soft target. A4 question. |
| F7-02 | F7 | Table 4 rows 12,15 (HEDGE_PHRASE/ACQUISITION_CONTINGENT) | slides 15,18, lines 498-499, 570 | "~Rs2,300 Cr total Defence order book ( ~INR 2000 crs through an entity proposed to be acquired)" | AMBIGUOUS | ~87% (₹2,000 cr of ₹2,300 cr) of the touted defence order book is contingent on an acquisition that is still "proposed", not closed. HFCL's own current defence backlog is only ~₹300 cr. A4 question: acquisition timeline, price, order-book transferability. |
| F8-01 | F8 | Table 3 rows 13,11 (Tax, PBT) | slide 8, lines 254,256 | "Tax 85.88 / 43.48 / -15.40" ; "PBT 331.52" | NEUTRAL-FACT | ETR Q1FY27 = 85.88/331.52 = 25.9% (≈ statutory 25.17%, fully taxed = clean earnings). Q4FY26 ETR was 19.1%; Q1FY26 a tax credit on loss. Forward: model ~25-26% ETR; no residual tax shield to flatter future PAT. |
| F9-01 | F9 | Table 3 row 16 (OCI) | slide 8, line 259 | "Other Comprehensive Income 72.16 / -39.23 / 38.92" | AMBIGUOUS | OCI swung +₹111.4 cr QoQ (-39.23 → +72.16) and equals 29% of PAT (72.16/245.64). A swing this large signals a hedge-reserve or FVOCI/actuarial assumption move. Given the export/hyperscaler FX exposure (Notion monitoring #1), the composition matters. A4 question: what drives ₹72.16 cr OCI — cash-flow hedge reserve on export receivables? Verify at AR. |
| F10-01 | F10 | Table 3 row 18 (EPS) + line 622 | slides 8,20, lines 261,622 | "EPS (Diluted ₹) 1.49 / 1.21 / -0.22" ; "SHARES OUTSTANDING 1,53,06,02,463" | FORWARD-SIGNAL | Implied diluted share count Q1FY27 = 245.64/1.49 = 164.9 cr vs 153.06 cr outstanding = ~11.8 cr (7.7%) dilution overhang. QoQ the diluted count rose ~12.4 cr (Q4FY26 diluted = 184.45/1.21 = 152.4 cr). Deck discloses neither basic EPS nor the dilutive instrument. A4 question: source of ~12 cr new dilutive potential shares (warrants issued in Q1FY27?) — bears on promoter stake math (F16-02). |
| F16-01 | F16 | Table 2 lines 279-288 (CHART_LABEL_INFERRED); Notion ref | slide 9, lines 279-293 | "Total Order Book ... 26,665"; category bars "4,227 ... 5,099 ... 17,339" | FORWARD-SIGNAL | The thesis-linchpin $1.1B / ₹10,159 cr hyperscaler OFC order (Notion) is NOT broken out anywhere on the order-book slide. Inferred category split (Networks 17,339 / O&M 5,099 / Products 4,227) puts "Products" — the natural OFC bucket — at only ₹4,227 cr, LESS than the hyperscaler order alone. Either the hyperscaler order is not (fully) in the ₹26,665 cr backlog or categorisation is opaque. Deck is silent on hyperscaler execution pace (Notion monitoring #1, tripwire #1). A4 must ask for hyperscaler-specific order book + drawdown. |
| F16-02 | F16/F11 | Table 2 lines 615,617,618 (CHART_LABEL_INFERRED) | slide 20, lines 615,617,618 | "28.29%" ; "% FREE-FLOAT 71.69%" ; "45.05%" | FORWARD-SIGNAL | Ledger tentatively mapped Promoter = 45.05%. The deck's own "% FREE-FLOAT 71.69%" forces Promoter = 100 - 71.69 = 28.31% ≈ the 28.29% slice. So PROMOTER = ~28.29%, NOT 45.05% (the 45.05% slice is a public/Others bucket). This matches Notion (28%). Consequence: promoter sits exactly at the monitoring #5 green floor (≥28%) and ~3 pts above tripwire #2 (exit <25%) — thin margin, flat. Deck discloses NO pledge status (monitoring #5 / tripwire #3). A4 must confirm the pie mapping and pledge = zero. |
| F16-03 | F16 | Table 2 lines 449-450, 543 (FORWARD_TARGET) | slides 14,17, lines 449-450,543 | "OPTICAL FIBER CABLE CAPACITY EXPANDING TO 42.3 MN FKM/ANNUM" | AMBIGUOUS | Capacity-expansion targets (OFC → 42.3 / ~43 mn fkm; OF → 33.9 / ~34 mn fkm) carry NO completion date on the deck, whereas the preform target is dated ("300 MT/ANNUM BY JULY 2029"). Notion expected 42.36 mn fkm by Dec 2026. Omitting the fkm date removes the ability to track vs the Dec-2026 milestone. A4 question: reaffirm the Dec-2026 capacity date. |
| F16-04 | F16 | Table 2 lines 543-544,572; Notion ref | slides 17,18, lines 543,572 | "exports at 56% of revenues with a target to reach 60%+ from FY27 onwards" | FORWARD-SIGNAL | Export share is now stated as "~56% of revenues" vs Notion FY26 anchor of 41.36%. A ~15 pt reframe upward (present-tense, undated period). Confirms the export/OFC-export ramp thesis but the base period for "56%" is unlabelled (Q1FY27? trailing?). Positive-leaning but needs period-anchoring. |
| F16-05 | F16 | Table 2 lines 287,350; slide 17/18 body | slides 9,17,18, lines 287,538,568-578 | "Networks ... 17,339"; "deliberately shifting from low-profit turnkey work"; "Products segment now ~85% of revenues" | CONFIRMATORY-NEGATIVE | Order-book mix contradicts the margin narrative: inferred Networks (turnkey/EPC incl BharatNet) = ₹17,339 cr = 65% of the ₹26,665 cr backlog, i.e. the backlog is dominated by the exact low-margin turnkey work the deck says it is "deliberately shifting from." Deck carries NO receivables/DSO, NO BharatNet-III revenue/PBT split, NO working-capital data (Notion monitoring #2/#6/#7, tripwire #4). Sustained silence on receivables in the pre-concall doc is a confirmatory negative to carry into F17/A5 at concall stage. |

---

## CHECKLIST SCORECARD (all 17)

| Check | Status | Basis (one line) |
|---|---|---|
| F1 | FINDING | Exceptional Items row (slide 8, line 253) stands empty in all 3 periods; live template slot, likely populated by the proposed aerospace acquisition. |
| F2 | N.A. | Deck presents a single (consolidated) P&L only; no standalone-vs-consolidated split disclosed to decompose. |
| F3 | N.A. | No standalone-vs-consolidated cost lines in an investor deck; shell-entity test not computable. |
| F4 | N.A. | No auditor "Other Matters" / component-auditor disclosure in a presentation. |
| F5 | N.A. | No Going Concern / Emphasis-of-Matter paragraph in a presentation. |
| F6 | FINDING | Ten dated/dateable forward commitments mined (register below); status language "expected to / will continue / commences / being acquired". |
| F7 | FINDING | 40% growth hedged as "aspiration/best estimate" (line 162); ₹2,000 cr defence OB "proposed to be acquired" (lines 499,570). |
| F8 | FINDING | ETR normalised to 25.9% Q1FY27 (≈ statutory) from 19.1% Q4FY26; earnings fully taxed, no forward shield. |
| F9 | FINDING | OCI +₹72.16 cr = 29% of PAT, +₹111 cr QoQ swing (line 259); likely hedge-reserve/FVOCI, composition undisclosed. |
| F10 | FINDING | Diluted share count ~164.9 cr vs 153.06 cr outstanding = 7.7% overhang; +12.4 cr QoQ; instrument undisclosed. |
| F11 | N.A. | Deck carries market cap / shares / free-float but NO Other Equity / net-worth figure to tie out (the free-float % is used instead in F16-02). |
| F12 | N.A. | No segment assets/liabilities table in the deck; only order-book category/customer bars (used in F16). |
| F13 | N.A. | Covering letter records only board approval of results (line 48-49); no AGM notice, dividend, AR, or director-appointment item. |
| F14 | PASS | Entity names and headline figures consistent across tables (HASPL/order book ₹26,665≈"more than 26,000"; defence ₹2,300/₹2,000 consistent slides 15↔18); no auditor letter to cross-check note wording. |
| F15 | N.A. | No consolidation/entity list in the deck; no prior deck for a diff. |
| F16 | FINDING | Five reframes/silences: hyperscaler order not broken out (F16-01); promoter=28.29% via free-float, not 45.05% + pledge silent (F16-02); capacity date dropped (F16-03); export share reframed 41.36%→~56% (F16-04); backlog 65% low-margin Networks vs product narrative + receivables/BharatNet silence (F16-05). |
| F17 | N.A. | Concall-specific silence audit; this is the pre-concall deck, not the transcript. Deck-level silences (receivables, BharatNet, hyperscaler pace, pledge, Nivetti, fuze) captured under F16-01/-05 and the Commitment Register for the A5/concall pass. |

GATE A3: pass (17/17 marked, no blanks).

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | slide/line ref | status word |
|---|---|---|---|
| FY27 revenue growth ~40% | FY27 | slide 5, line 162 | aspiration / "best of our estimates" (hedged) |
| EBITDA margin ~16.7% (FY26) → 22-25% | by FY29 | slide 17, line 536 | target |
| Export revenue 60%+ | from FY27 onwards | slide 17, line 544 | target (vs ~56% now) |
| Products 80-85% of revenue | FY27 (implied) | slide 17, line 537 | targeting |
| OFC capacity → ~43 / 42.3 mn fkm; OF → ~34 / 33.9 mn fkm | UNDATED on deck (Notion: Dec 2026) | slide 14 lines 449-450; slide 17 line 543 | "expanding to" (underway) |
| Preform capacity 300 MT/annum (₹580 cr capex) | by July 2029 | slide 14, lines 455-457 | project capex / backward integration underway |
| MMHG facility Phase 1 (₹275 cr) at Andhra Ammunition Complex | UNDATED | slide 14, lines 455-457 | "for creating facility" (initiated) |
| Aerospace-business acquisition (adds ₹2,000 cr defence OB) | UNDATED ("proposed") | slide 15 line 499; slide 18 line 570 | "proposed to be acquired / being acquired" |
| Defence serial production → operating-performance uplift | UNDATED | slide 18, lines 578-581 | "as serial production commences" (future) |
| Defence platform to "gain global scale" | UNDATED | slide 18, lines 567-570 | "expected to" |

---

## RECONCILIATION NOTE
Every A2 flag was run: ZERO_STANDING → F1-01; HEDGE_PHRASE/ACQUISITION_CONTINGENT → F7-01/F7-02; FORWARD_TARGET → F6-01, F16-03; CHART_LABEL_INFERRED → F16-01 (order book), F16-02 (shareholding, resolved via free-float anchor); OCR_UNCERTAIN (slide 2, "202603") → non-material garbled cover-date token, no financial content, no finding. DROPPED_SLIDE could not be evidenced (no prior deck in runs/); recorded as a methodology gap, not a "no-drops" conclusion — F16 findings above are reframes/silences observable within this deck and against Notion anchors, not asserted prior-deck drops.

```yaml
stage: A3-forensics
company: "HFCL"
quarter: "q1fy27"
doctype: "presentation"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/hfcl-q1fy27/work/forensics_presentation_hfcl_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: FINDING
  F10: FINDING
  F11: N.A.
  F12: N.A.
  F13: N.A.
  F14: PASS
  F15: N.A.
  F16: FINDING
  F17: N.A.
findings:
  - {id: "F1-01", check: "F1", line: "slide 8 / line 253", classification: "NEUTRAL-FACT", implication: "Empty Exceptional Items slot likely populated when proposed aerospace acquisition closes"}
  - {id: "F6-01", check: "F6", line: "slides 5,14,17,18 / lines 162,449-457,536-546,570,578", classification: "FORWARD-SIGNAL", implication: "Ten dated/dateable commitments for Role 5 promise-vs-delivery tracker"}
  - {id: "F7-01", check: "F7", line: "slide 5 / line 162", classification: "AMBIGUOUS", implication: "40% FY27 growth is hedged aspiration, not committed guidance"}
  - {id: "F7-02", check: "F7", line: "slides 15,18 / lines 498-499,570", classification: "AMBIGUOUS", implication: "~87% of defence order book contingent on unclosed acquisition"}
  - {id: "F8-01", check: "F8", line: "slide 8 / lines 254,256", classification: "NEUTRAL-FACT", implication: "ETR normalised to 25.9%; earnings fully taxed, no forward shield"}
  - {id: "F9-01", check: "F9", line: "slide 8 / line 259", classification: "AMBIGUOUS", implication: "OCI +72.16cr (29% of PAT), +111cr QoQ swing; likely FX hedge reserve, verify"}
  - {id: "F10-01", check: "F10", line: "slides 8,20 / lines 261,622", classification: "FORWARD-SIGNAL", implication: "7.7% dilution overhang; diluted count +12.4cr QoQ; instrument undisclosed"}
  - {id: "F16-01", check: "F16", line: "slide 9 / lines 279-293", classification: "FORWARD-SIGNAL", implication: "$1.1B hyperscaler order not broken out; Products bucket smaller than the order itself"}
  - {id: "F16-02", check: "F16", line: "slide 20 / lines 615,617,618", classification: "FORWARD-SIGNAL", implication: "Promoter=28.29% via free-float (not 45.05%); at 28% monitoring floor; pledge undisclosed"}
  - {id: "F16-03", check: "F16", line: "slides 14,17 / lines 449-450,543", classification: "AMBIGUOUS", implication: "Capacity-expansion (42.3 mn fkm) completion date omitted; can't track vs Dec-2026 milestone"}
  - {id: "F16-04", check: "F16", line: "slides 17,18 / lines 543,572", classification: "FORWARD-SIGNAL", implication: "Export share reframed 41.36% (FY26) to ~56%; period base unlabelled"}
  - {id: "F16-05", check: "F16", line: "slides 9,17,18 / lines 287,538,568", classification: "CONFIRMATORY-NEGATIVE", implication: "Backlog 65% low-margin Networks vs product narrative; receivables/BharatNet/DSO silent"}
forward_signals: ["F6-01", "F10-01", "F16-01", "F16-02", "F16-04"]
ambiguous: ["F7-01", "F7-02", "F9-01", "F16-03"]
commitments:
  - {commitment: "FY27 revenue growth ~40%", implied_date: "FY27", ref: "slide 5 line 162", status_word: "aspiration"}
  - {commitment: "EBITDA margin to 22-25%", implied_date: "FY29", ref: "slide 17 line 536", status_word: "target"}
  - {commitment: "Export revenue 60%+", implied_date: "FY27 onwards", ref: "slide 17 line 544", status_word: "target"}
  - {commitment: "Products 80-85% of revenue", implied_date: "FY27", ref: "slide 17 line 537", status_word: "targeting"}
  - {commitment: "OFC capacity ~43/42.3 mn fkm; OF ~34/33.9 mn fkm", implied_date: "undated (Notion Dec-2026)", ref: "slide 14 lines 449-450; slide 17 line 543", status_word: "expanding"}
  - {commitment: "Preform 300 MT/annum (Rs580cr capex)", implied_date: "July 2029", ref: "slide 14 lines 455-457", status_word: "underway"}
  - {commitment: "MMHG facility Phase 1 (Rs275cr), Andhra Ammunition Complex", implied_date: "undated", ref: "slide 14 lines 455-457", status_word: "initiated"}
  - {commitment: "Aerospace-business acquisition (adds Rs2000cr defence OB)", implied_date: "undated (proposed)", ref: "slide 15 line 499; slide 18 line 570", status_word: "proposed"}
  - {commitment: "Defence serial production / operating-performance uplift", implied_date: "undated", ref: "slide 18 lines 578-581", status_word: "commences"}
  - {commitment: "Defence platform to gain global scale", implied_date: "undated", ref: "slide 18 lines 567-570", status_word: "expected"}
gate_a3: pass
blank_checks: []
```
