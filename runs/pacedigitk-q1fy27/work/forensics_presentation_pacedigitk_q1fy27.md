# A3 FORENSIC NOTES — Pace Digitek Ltd (PACEDIGITK) — Q1 FY27 — Doctype: INVESTOR PRESENTATION

Source extract: `extract_presentation_pacedigitk_q1fy27.txt` (26 pages, 740 lines).
Reconciliation source: `extract_results_pacedigitk_q1fy27.txt` (10 pages, 552 lines).
Ledger: `ledger_presentation_pacedigitk_q1fy27.md` (357 numeric rows, 7 notes, 2 ZERO_STANDING, 1 DISCREPANCY, SCRAMBLED_LAYOUT).
Ledger reconciliation: 100% — every Table 1/2/3/4 row read at its cited line in the A1 extract and cross-checked against the results filing where a filing line exists.

Doctype scope (per prompt): F16 applies, plus any F6/F10/F11 numbers the deck carries. Balance-sheet / auditor / concall checks marked N.A. with basis. Every check carries an explicit status.

---

## HEADLINE RECONCILIATION (priority focus 1) — deck vs results filing

CONSOLIDATED (deck slide 7 lines 222-238 vs filing consolidated p.8 lines 438-486): every line ties within rounding.
- Revenue 5,554 = 5,553.64 ✓ | Q1FY26 3,671 = 3,670.79 ✓ | Q4FY26 10,968 = 10,967.79 ✓
- Employee 333 = 332.63 ✓ | Other exp 362 = 361.63 ✓ | Finance 283 = 283.41 ✓ | D&A 44 = 44.37 ✓
- PBT 816 = 816.29 ✓ | Taxes 191 = 191.24 ✓ | PAT 625 = 625.05 ✓ | Other income 283 = 283.41 ✓
- Gross profit 1,555 rebuilds from filing (5,553.64 - COGS 3,753.16 - EPC 974.54 - stock-in-trade 3.25 + inventory build 732.23 = 1,554.92) ✓; GP margin 28.0% ✓.
- Note: finance costs and other income are BOTH exactly 283.41 mn in the filing — a genuine coincidence carried verbatim, not an error.

STANDALONE (deck slide 8 lines 248-270 vs filing standalone p.3 lines 158-191): every line ties within rounding.
- Revenue 2,642 = 2,642.40 ✓ | PBT 572 = 572.43 ✓ | PAT 425 = 425.14 ✓ | D&A 32 = 31.94 ✓ | Finance 79 = 78.93 ✓.

VERDICT on the A2-flagged DISCREPANCY and SCRAMBLED_LAYOUT:
- DISCREPANCY (CIN L- vs U-prefix): BENIGN typo — see FND-05.
- SCRAMBLED_LAYOUT (slide 5 waterfall + slide 14 donut): the numbers are internally consistent once de-scrambled; the deck reconciles. A2's Table-2 opening/closing LABELS on the waterfall are inverted — see FND-04. One residual unreconciled label (78.1%) — see FND-09.

No headline number on the deck fails against the filing. The forensic signals are in composition, framing, and silence, not in a fabricated headline.

---

## FINDINGS TABLE

| id | check | ledger row ref | line/slide | verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| FND-01 | F2 | S7:L237 / S8:L270 | slides 7 & 8 | "Profit After Tax 625 ... 547" (cons) vs "Profit After Tax (PAT) 425 ... 510" (SA) | FORWARD-SIGNAL | Subsidiary share of consolidated PAT swung 6.8% (Q1FY26) -> 61.7% (Q4FY26) -> 32.0% (Q1FY27); subsidiary share of revenue 7.5% -> 52%. Consolidated earnings are now majority Energy-subsidiary (Lineage Power / PREPL) driven. Earnings quality and cash conversion increasingly ride on subsidiaries whose numbers include unreviewed components (filing p.7 Other Matters). Directly feeds the CFO gate. |
| FND-02 | F16 | S8:L248 / S8:L253-262 | slide 8 | "Revenue from operations* 2,642 ... (22.2)%" vs "*Adjusted standalone revenue ... increased by 52% YoY" | FORWARD-SIGNAL | Reported standalone revenue FELL 22.2% YoY; the asterisk reframes to +52% on a gross, pre-elimination basis. Inter-company eliminations jumped from ~nil (Q1FY26 gross 3,389 vs net 3,397) to Rs 2,509 mn (49% of gross 5,151). Standalone now runs massive captive EPC for its own subsidiaries (PREPL / MSEDCL BESS BOO). Non-GAAP "adjusted" growth is the headline the deck leans on; related-party / revenue-quality question for A4. |
| FND-03 | F16 | S24:L676 vs S5:L146 / S10:L307 | slides 24, 5, 10, 15, 16 | "Order Book of Rs.113,379 Mn" (S24) vs "108,033" (S5/S10; = S15 84,530 + S16 23,503) | AMBIGUOUS | Two different order-book totals in one deck. Delta = 5,346 mn, exactly the Q1 sales-execution figure. Which is the true order book, and what does 113,379 include (gross of Q1 execution? O&M annuity tail? later cut-off)? A4 management question. |
| FND-04 | F16 | S5:L145-148 | slide 5 | "16,766 ... 108,033 ... -5,346 ... 96,613" waterfall | NEUTRAL-FACT | De-scrambled: opening 96,613 (31-Mar-26) + incoming 16,766 - sales 5,346 = closing 108,033 (30-Jun-26). Order book GREW. A2 Table-2 labelled 108,033 as opening and 96,613 as closing (inverted). Footnote reconciles: sales 5,346 + 208 excluded = 5,554 consolidated revenue (L170-171). Benign at company level; correct A4 not to read the order book as shrinking. |
| FND-05 | F14 | S1:L48 vs S26:L728 | slides 1 & 26 | "L31909KA2007PLC041949" vs "U31909KA2007PLC041949" | NEUTRAL-FACT | CIN status letter differs within one document (L=listed, U=unlisted). Results filing shows L throughout (listed 06-Oct-2025); slide 26 carries the stale pre-IPO U-prefix = typo, benign. Compounding minor: order-book table spells "MESDCL" (S15:L437) vs "MSEDCL" elsewhere (S4:L117, S18:L511). Cumulatively a document-control data point, not a substantive misstatement. |
| FND-06 | F16 | S15 / S16 tables | slides 15 & 16 | client roster "NLC India ... DVC ... BSNL ... SECI ... KPTCL ... NTPC ... MAHAGENCO ... Indian Railways" | CONFIRMATORY-NEGATIVE | No Tier-1/Tier-3 or PSU-vs-private mix is disclosed anywhere, despite concentration being the thesis's central bear risk (~96% government). The named clients confirm heavy government concentration; non-government orders are small (Reliance 1,200; Tata Teleservices 1,923; RNS 1,149; Bondada 2,920; Yaqin 123). Section 22 BUY condition (c) non-government revenue pathway remains unaddressed — capability signals (NEC XON "five African countries", "three MoUs", RJE Tech 3 GWh cell MSA) are partnerships/MoUs, not booked orders. |
| FND-07 | F6 | slides 4,18,19,21,24 | see Commitment Register | "Expected to be operational by Q3 FY27" (S21:L613-614) et al. | FORWARD-SIGNAL | Dense dated commitment set — feeds Role 5 promise-vs-delivery tracker. Notably the NEW 5 GWh line slips to Q3 FY27 (machines only expected Oct 2026), while the "additional 2.5 GWh" line reaches operational Aug 2026. See register for all milestones + Notion-trigger cross-refs. |
| FND-08 | F16 | (absent) | whole deck | no cash-flow / CFO / receivables / inventory-level slide | CONFIRMATORY-NEGATIVE | Deck is silent on cash flow, CFO, receivables and inventory levels — i.e. on the single most thesis-relevant number this quarter (Notion trigger #1, the binding CFO gate; first of two). The quarterly results filing also omits a cash-flow statement. The one working-capital tell that IS visible sits in the filing, not the deck: consolidated "Changes in inventories (732.23)" = an inventory BUILD of ~Rs 73.2 Cr in the quarter (cash consumption), consistent with the historic CFO-lags-PAT concern. A4 must source CFO from elsewhere; do not infer it from the deck. |
| FND-09 | F14 | S14:L416 | slide 14 | "84.2% 78.1%" with "Telecom & ICT Energy" | AMBIGUOUS | The order-wins split reconciles as Energy 84.2% (14,119/16,766) / Telecom & ICT 15.8% (2,647/16,766). A third label, 78.1%, ties to neither and sits in the scrambled overlapping text objects; it ~= Energy share of the TOTAL order book (84,530/108,033 = 78.2%). Likely a layout scramble but the association is unresolved by the extract — A4 clarify which chart 78.1% belongs to. |
| FND-10 | F16 | S24:L664 / S24:L675 | slide 24 | "FY27E Rs.32,000 - 34,000 mn ... FY28E Rs.40,000 - 42,000 mn" | FORWARD-SIGNAL | Explicit forward revenue guidance vs FY26 actual consolidated 26,413 mn: FY27E midpoint 33,000 = +25%, FY28E midpoint 41,000 = +24%. First-time guidance (no prior deck to diff). Sets a public bar against which Q2-Q4 FY27 execution will be judged. |
| FND-11 | F6 / context | S7:L229 / S7:L232 / S7:L233 | slide 7 | "Depreciation & amortisation 44 ... 112.6%"; "Finance costs 283 ... 191.5%"; "Other income 283 ... 402.9%" | FORWARD-SIGNAL | Fixed-cost and leverage lines are ramping far ahead of revenue (+51.3%): D&A +112.6%, finance costs +191.5% YoY. This is the BOO/manufacturing capex cycle inflating the cost base pre-revenue (filing note 6, L236-238: PREPL has already incurred Rs 4,860.45 mn capex on the MSEDCL project). Other income +402.9% is IPO proceeds parked (Rs 1,469 mn unutilised, filing L228). Watch net D/E (Notion trigger #14) and the CFO gate. |
| FND-12 | F12 | S5:L144 vs results L490 | slide 5 / filing note 1 | "Energy contributed 79.5% of Q1 FY27 revenue" vs filing "Consolidated segment wise information for the quarter ended June 30, 2026" (no table follows) | AMBIGUOUS | Deck gives a segment REVENUE split only (Energy 79.5% / Telecom & ICT 20.5%); no segment assets or liabilities, so the equity-funded-build test cannot run on the deck. The split cannot be tied out: the filing's consolidated segment note (note 1) is blank/uncaptured in the extract. Implied Energy revenue = 79.5% x 5,554 = ~4,415 mn (~Rs 442 Cr), which sits BELOW the Notion trigger #6 Green threshold (Rs 500 Cr) and above Red (Rs 300 Cr) = amber. A4: obtain the full segment note; verify Energy segment size and segment-level cash conversion. |

---

## CHECKLIST SCORECARD (all 17)

| # | Status | Basis |
|---|---|---|
| F1 | PASS | Only 2 ZERO_STANDING rows exist — slide 15 GWh-column dashes for MAHAGENCO (L446) and Bondada (L450), both pure-solar EPC with no BESS-GWh scope. Structural blanks, not a P&L standing-zero line anticipating a transaction class. Deck carries no P&L template with standing-zero items. Nothing forensic. |
| F2 | FINDING | FND-01. S-vs-C gap computed for every period on deck: subsidiary share of PAT 6.8% -> 61.7% -> 32.0%; of revenue 7.5% -> 52%. Both swings exceed the 5pp-of-standalone-PAT threshold by a wide margin. |
| F3 | N.A. | Shell detection needs per-entity cost lines; the deck carries only aggregate cons/SA. (Cross-ref only: filing p.7 shows a Rs NIL-revenue subsidiary and 2 unreviewed subs with Rs 5.20 mn revenue — a results/AR check, not a deck check.) |
| F4 | N.A. | No auditor Other Matters section in a deck. (Cross-ref: filing p.7 para 6-7 quantifies unreviewed subsidiary contribution — belongs to results forensics.) |
| F5 | N.A. | No EoM / going-concern language in a deck. Results carry an unmodified limited-review opinion (filing L48-50). |
| F6 | FINDING | FND-07 + FND-11. Rich dated-commitment lexicon on slides 4/18/19/21/24 ("expected to receive by October 2026", "Expected to be operational by Q3 FY27", "operational in August 2026", "commenced", "under survey phase"). Commitment Register below. |
| F7 | PASS | Only boilerplate forward-looking-statement hedges on the disclaimer (slide 25: "no assurance", "subject to risks", "differ materially"). No NEW substantive hedge about revenue lumpiness or customer concentration added in the body. Lone soft dependency ("awaiting grid connectivity", MAHAGENCO, S19:L544) logged in the register, not a note-level legal hedge. |
| F8 | PASS | Deck ETR: consolidated 23.4% (191/816), standalone 25.7% (147/572) vs 25.17% statutory — both in range. Deck carries no deferred-tax or earlier-year line; filing confirms "Taxes relating to earlier years" = NIL this quarter (was 4.24/7.15 in prior periods), so no earlier-year adjustment to flag. |
| F9 | N.A. | Deck carries no OCI. (Filing OCI immaterial: cons remeasurement (4.32), FX (0.82).) |
| F10 | N.A. | Deck carries no share count, paid-up capital or EPS. (Cross-ref: filing basic=diluted EPS -> no dilutive spread; paid-up stable 431.70; YoY rise 356.88->431.70 = Oct-2025 IPO, filing note 4.) |
| F11 | N.A. | Deck carries no reserves / net worth line. (Filing: other equity cons 21,641.28 + paid-up 431.70 = ~22,073 mn at Mar-26.) |
| F12 | FINDING | FND-12. Deck has segment revenue split only, no segment assets/liabilities; and it cannot be tied to the filing's blank consolidated segment note. |
| F13 | N.A. | Board-outcome content (approvals, AGM notice, director terms) lives in the results filing / separate intimations, not this deck. Slide-4 "Corporate Development" bullets are partnership announcements, not board resolutions. |
| F14 | FINDING | FND-05. CIN L- vs U-prefix (S1:L48 vs S26:L728) and MESDCL/MSEDCL entity-name spelling (S15:L437 vs S4/S18). Individually immaterial, cumulatively a document-control data point. |
| F15 | N.A. | Deck carries no consolidation entity list, and no prior-quarter deck supplied. (Filing p.6 lists 1 parent + 7 subs + 1 step-down = 9 entities; entity-diff belongs to results forensics with a prior period.) |
| F16 | FINDING | FND-02, 03, 04, 06, 08, 10. Standalone revenue reframing; two conflicting order-book totals; waterfall label inversion (order book grew); customer-mix silence; CFO/working-capital silence; forward guidance. Dropped-slide diff itself is un-testable (no prior deck). |
| F17 | N.A. | No concall transcript in this run's scope. The most consequential silence (CFO / working capital) is captured under F16/FND-08 rather than left unrecorded. |

---

## COMMITMENT REGISTER (F6)

| Commitment | Implied date | Ref | Status word | Cross-ref |
|---|---|---|---|---|
| MSEDCL Standalone BESS BOO: 375 MWh commissioned in Q1 (975 MWh cumulative), "well ahead of completion targets" | Q1 FY27 (done) | S4:L116-119 / S18:L511-514 | completed | Notion trigger #5 (BOO revenue) / #15 (MSEDCL VGF) |
| Additional 2.5 GWh BESS manufacturing line operational | August 2026 | S4:L113-115 / S21:L601-604 | operational (near-term) | Notion trigger #3 (5 GWh commissioning) — combined capacity reaches 5 GWh Aug-26, a ~1-month slip vs Jul-26 expectation |
| In-house container fabrication facility ready for commissioning / "nearing completion" | August 2026 | S4:L118-119 / S21:L601-603 | ready-for-commissioning | Notion trigger #4 (container fab, Green Q2 FY27) |
| New 5 GWh facility: construction completed; machines to be received | October 2026 | S21:L606-611 | expected-to-receive | — |
| New 5 GWh line operational | Q3 FY27 | S21:L613-614 | expected | Notion trigger #3 — later leg of manufacturing scale-up slips to Q3 FY27 |
| 10 GWh total manufacturing capacity ("On track to achieve") | end FY2027 | S21:L601-604 / S10:L302-303 / S24:L661 | on-track | — |
| SECI (Solar+BESS BOO): PPA executed; engineering/layouts completed; civil works progressing; "ground work started" | ongoing | S4:L123-124 / S19:L529-536 | commenced / executed | Notion trigger #6 (Energy segment) |
| KPTCL (Standalone BESS BOO): BESPA executed; land allotted; civil works commenced | ongoing | S19:L529-536 | commenced | — |
| Bondada (Solar EPC 300 MW): site mobilization + equipment procurement completed; civil works progressing | ongoing | S19:L541-546 | completed / progressing | — |
| MAHAGENCO (Solar EPC 200 MW): land identified; "awaiting grid connectivity" | pending (dependency) | S19:L541-547 | awaiting | Soft execution dependency (F7 borderline) |
| BSNL BharatNet & Railways Kavach "under survey phase" | ongoing | S4:L127-129 | under-survey | Telecom pipeline |
| RJE Tech: 3 GWh li-ion cell supply agreement | signed | S4:L122-123 | agreement | Notion: proximate trigger for position initiation 29-Jun-26 |
| NEC XON OEM partnership to market BESS across five African countries | signed (capability) | S4:L129-133 | signed (partnership, not order) | Notion trigger #10 (NEC XON Africa — needs a SIGNED CONTRACT; this is an OEM-to-market MoU, not revenue) |
| Three MoUs for supply of BESS | signed (non-binding) | S4:L134-135 | MoU | Section 22 condition (c) — capability, not booked non-govt revenue |
| Megmeet partnership to enter AI data-center power infrastructure | signed (capability) | S4:L125-127 | partnered | Optionality, not revenue |
| FY27E revenue Rs.32,000-34,000 mn; FY28E revenue Rs.40,000-42,000 mn | FY27 / FY28 | S24:L664 / L675 | guidance | First-time public guidance (FND-10) |

---

## NOTES FOR A4

- Convert to management questions (FORWARD-SIGNAL + AMBIGUOUS): FND-01, FND-02, FND-03, FND-07, FND-09, FND-10, FND-11, FND-12.
- Priority A4 questions implied: (1) Q1 FY27 CFO and receivables/inventory levels — absent from the deck (FND-08), and this is the first leg of the binding EXIT gate; (2) the Rs 2,509 mn inter-company elimination and whether the +52% "adjusted" standalone figure is being used to mask a -22.2% reported decline (FND-02); (3) reconcile the Rs 113,379 mn vs Rs 108,033 mn order book (FND-03); (4) customer mix / PSU-vs-private disclosure that the deck omits (FND-06); (5) full segment note and Energy segment size vs the Rs 500 Cr trigger (FND-12).
- CONFIRMATORY-NEGATIVES (weigh, no question needed): FND-06 (concentration unaddressed), FND-08 (CFO silence).
- BENIGN, do not escalate: FND-04 (waterfall labels — deck reconciles; A2 label inverted), FND-05 (CIN typo / spelling).

```yaml
stage: A3-forensics
company: "pacedigitk"
quarter: "q1fy27"
doctype: "presentation"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/pacedigitk-q1fy27/work/forensics_presentation_pacedigitk_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: PASS
  F2: FINDING
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: PASS
  F8: PASS
  F9: N.A.
  F10: N.A.
  F11: N.A.
  F12: FINDING
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: N.A.
findings:
  - {id: "FND-01", check: "F2", line: "slides 7 & 8 (L237/L270)", classification: "FORWARD-SIGNAL", implication: "Subsidiary share of consolidated PAT 6.8%->61.7%->32.0%, of revenue 7.5%->52%; earnings now majority Energy-subsidiary driven, feeds CFO gate"}
  - {id: "FND-02", check: "F16", line: "slide 8 (L248/L253-262)", classification: "FORWARD-SIGNAL", implication: "Reported standalone revenue -22.2% YoY reframed to +52% adjusted; inter-co eliminations jumped ~nil->2,509mn (49% of gross); captive EPC / revenue-quality question"}
  - {id: "FND-03", check: "F16", line: "slide 24 (L676) vs slides 5/10/15/16", classification: "AMBIGUOUS", implication: "Two order-book totals 113,379 vs 108,033 (delta = Q1 sales 5,346); clarify definition"}
  - {id: "FND-04", check: "F16", line: "slide 5 (L145-148)", classification: "NEUTRAL-FACT", implication: "Order book grew 96,613->108,033; A2 Table-2 opening/closing labels inverted; deck reconciles"}
  - {id: "FND-05", check: "F14", line: "slide 1 (L48) vs slide 26 (L728)", classification: "NEUTRAL-FACT", implication: "CIN L- vs U-prefix typo + MESDCL/MSEDCL spelling; document-control data point, benign"}
  - {id: "FND-06", check: "F16", line: "slides 15 & 16", classification: "CONFIRMATORY-NEGATIVE", implication: "No Tier / PSU-vs-private customer-mix disclosure; roster confirms heavy government concentration; Section 22(c) non-govt pathway unaddressed"}
  - {id: "FND-07", check: "F6", line: "slides 4/18/19/21/24", classification: "FORWARD-SIGNAL", implication: "Dated commitment set; new 5 GWh line slips to Q3 FY27; feeds promise-vs-delivery tracker"}
  - {id: "FND-08", check: "F16", line: "whole deck (absent)", classification: "CONFIRMATORY-NEGATIVE", implication: "Silent on CFO/receivables/inventory - the binding CFO gate; filing shows inventory build (732.23) consistent with CFO-lags-PAT risk"}
  - {id: "FND-09", check: "F14", line: "slide 14 (L416)", classification: "AMBIGUOUS", implication: "Unreconciled 78.1% label in scrambled donut (~Energy share of total order book); clarify chart association"}
  - {id: "FND-10", check: "F16", line: "slide 24 (L664/L675)", classification: "FORWARD-SIGNAL", implication: "First-time guidance FY27E 32,000-34,000mn (+25%) / FY28E 40,000-42,000mn (+24%); public execution bar"}
  - {id: "FND-11", check: "F6", line: "slide 7 (L229/L232/L233)", classification: "FORWARD-SIGNAL", implication: "D&A +112.6%, finance costs +191.5% outpacing revenue +51.3% = BOO/manufacturing capex-leverage ramp (PREPL Rs4,860mn capex); watch net D/E and CFO"}
  - {id: "FND-12", check: "F12", line: "slide 5 (L144) vs filing note 1 (L490)", classification: "AMBIGUOUS", implication: "Segment revenue split (Energy 79.5%) not tie-able to blank filing segment note; implied Energy ~Rs442 Cr below Rs500 Cr trigger; obtain full segment note"}
forward_signals: ["FND-01", "FND-02", "FND-07", "FND-10", "FND-11"]
ambiguous: ["FND-03", "FND-09", "FND-12"]
commitments:
  - {commitment: "MSEDCL BESS 375 MWh commissioned in Q1 (975 MWh cumulative)", implied_date: "Q1 FY27", ref: "S18:L511-514", status_word: "completed"}
  - {commitment: "Additional 2.5 GWh manufacturing line operational", implied_date: "August 2026", ref: "S21:L601-604", status_word: "operational"}
  - {commitment: "In-house container fabrication facility ready for commissioning", implied_date: "August 2026", ref: "S21:L601-603", status_word: "ready-for-commissioning"}
  - {commitment: "New 5 GWh facility machines received", implied_date: "October 2026", ref: "S21:L610-611", status_word: "expected"}
  - {commitment: "New 5 GWh line operational", implied_date: "Q3 FY27", ref: "S21:L613-614", status_word: "expected"}
  - {commitment: "10 GWh total manufacturing capacity", implied_date: "end FY2027", ref: "S21:L601-604 / S24:L661", status_word: "on-track"}
  - {commitment: "SECI Solar+BESS BOO ground work / civil works", implied_date: "ongoing", ref: "S19:L529-536", status_word: "commenced"}
  - {commitment: "KPTCL Standalone BESS BOO civil works", implied_date: "ongoing", ref: "S19:L529-536", status_word: "commenced"}
  - {commitment: "Bondada Solar EPC 300 MW civil works", implied_date: "ongoing", ref: "S19:L541-546", status_word: "progressing"}
  - {commitment: "MAHAGENCO Solar EPC 200 MW awaiting grid connectivity", implied_date: "pending", ref: "S19:L541-547", status_word: "awaiting"}
  - {commitment: "BSNL BharatNet & Railways Kavach survey phase", implied_date: "ongoing", ref: "S4:L127-129", status_word: "under-survey"}
  - {commitment: "RJE Tech 3 GWh li-ion cell supply agreement", implied_date: "signed", ref: "S4:L122-123", status_word: "agreement"}
  - {commitment: "NEC XON OEM partnership across five African countries", implied_date: "signed", ref: "S4:L129-133", status_word: "partnership"}
  - {commitment: "Three MoUs for BESS supply", implied_date: "signed", ref: "S4:L134-135", status_word: "MoU"}
  - {commitment: "FY27E revenue Rs.32,000-34,000mn; FY28E Rs.40,000-42,000mn", implied_date: "FY27/FY28", ref: "S24:L664/L675", status_word: "guidance"}
gate_a3: pass
blank_checks: []
```
