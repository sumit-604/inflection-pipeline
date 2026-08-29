# Verifier summary: Divgi Torqtransfer Systems (DIVGIITTS)

Phase 1 verifier findings. Sorted CRITICAL, then MAJOR, then MINOR. Scope: Verifier A (numerical), Verifier B (red flags), Verifier D (peers), and the Gate 0 plus Emerging Moat portion of Verifier C. The valuation half of Verifier C is out of phase 1 scope (0 rules checked, deferred to phase 3).

## Phase 1 confidence delta

| Component | Score |
|---|---|
| Numerical acceptance (B12a) | 68.4 |
| Red flag coverage (B12b) | 82 |
| Framework adherence (B12c, Gate 0 + Emerging Moat only) | 100 |
| Peer utilisation (B12d) | 75 |
| **Overall** | **68.4** (band 60 to 74) |

Acceptance rates: Verifier A 68.4, Verifier B 76, Verifier C 100, Verifier D 94. All above the 60 REWORK floor.

Counts: CRITICAL 3 (all Verifier A), MAJOR 13 (A 9, B 2, D 1... see note), MINOR 11.

## CRITICAL

| Verifier | Location | Note |
|---|---|---|
| A | B01 Gate 0 (SPEAR load-bearing fact) | "~Rs 275 Cr net cash decline in FY26" claimed. Source truth: net cash rose from Rs 283.76 Cr (FY25) to Rs 292.75 Cr (FY26), up ~Rs 9 Cr. Contradicted by Note 10(a)+(b) and CFO letter p.39. Pipeline (B01/B02/B03) correctly contradicted the Spear brief; wrong figure originates in the brief, not a pipeline report. Disposition GATE HELD, corrected at source. source_fidelity true. |
| A | B03 AR Deep Dive, Section 6D | US subsidiary described as an established FY26 operating fact. Source truth: board approved 25-May-2026, incorporated Delaware 4-Jun-2026, both after FY26 close (31-Mar-2026). B03 flagged the AR internal contradiction; Board's Report Item 13 correctly states no subsidiary existed in the year. Disposition GATE HELD. source_fidelity true. |
| A | B09 TAM / B05 concall context | "Indonesia 70,000-unit transfer case program" claimed. Source truth: B09 web verification confirms 35,000 units (Mahindra Scorpio Pik Up CY2026). B05 accurately transcribed management's 70,000 concall claim (35k Tata + 35k Mahindra); B09 corrected to 35,000 verified. Material downward correction for capex and capacity downstream. Disposition GATE HELD. source_fidelity true. |

## MAJOR

| Verifier | Location | Note |
|---|---|---|
| A | B02/B03 Notes | AOC-2 to Note 34 rent income gap claimed ~19.5x. Source truth: AOC-2 Rs 24 Lakh (Rs 2.4 Mn) vs Note 34 Rs 4.68 Mn = 1.95x. B02 Lakh to Million conversion error; B03 already corrected to 1.95x. Underlying disclosure gap stands at the corrected ratio. |
| A | B02/B03 Notes | Three conflicting FY26 MD remuneration figures in one AR. Note 34 Rs 21.49 Mn vs Corp Gov and Annexure C Rs 17.75 Mn. Implied pay increase is 15% or 73.6% depending on which figure is authoritative; no reconciliation. |
| A | B02/B03 Notes | Note 42 current ratio explanation cites "reduction in current assets". Source truth: current assets rose 13.9%; current liabilities rose 58%. Explanation contradicts the company's own balance sheet. |
| A | B02/B03 Notes | GST contingent liability: Note 37 Nil vs CARO Annexure B Rs 1.63 Mn pending dispute. Same audit, same date, opposite disclosures on whether the dispute is live. |
| A | B02/B03 Related-party | Note 34(a) RPT list claimed complete. Source truth: Tejal Transmission (Note 5 equity holding; Hirendra Divgi on board) absent. Ind AS 24 completeness failure; omission means the entity never entered Audit Committee approval. |
| A | B02/B03 R&D | BRSR states R&D Rs 117.94 crore vs Business Driver page Rs 117.94 million. Source truth: Integrated Value-Creation Report confirms the million reading; BRSR and Annexure D carry a 100x unit error; R&D actually fell 13.6% YoY. |
| A | B01 Gate 0 data | Screener FY25 Interest Rs 0.60 Cr vs AR audited FY25 Finance Cost Rs 0.382 Cr, a 58% discrepancy, cause unresolved. B01 used the PDF audited figure as authoritative. |
| A | B05 concall context | "June 2026 FY25 results resubmission" claimed. Source truth: B08 web verification confirms 11-Jul-2025, a technical XBRL and PDF correction with an unmodified audit. Run brief date does not match the verified date. |
| A | B05 concall context / B01 | "Sigma EV SOP in Q2 FY27" claimed. Source truth: no Q2 FY27 date in the three provided concalls; documented slippage April to July to 12-Aug status still "progressing". If sourced outside the transcripts, unverifiable from the pipeline corpus. |
| B | B05 section 4C / 2C (margin treatment) | MISSED management volunteered negative: Q1 FY27 29.4% EBITDA margin is a one off, guidance back to 20 to 22%+. Anchor: Q1 FY27 call, Jitendra Divgi; margin print by Sudhir Mirjankar. |
| B | B05 SPEAR fact 1 / 3C | PARTIALLY CAUGHT: Indonesia order reframed from Q3 "specific, time bound one off, concludes by FY27 end" to Q1 ">50% recurring"; the cross quarter contradiction was not surfaced. Anchors: Q3 FY26 Jitendra to Karthi; Q1 FY27 Jitendra opening. |
| D | B06 Claim 5, peer evidence item (3) | Quote "growing concern in the government... 20% to cover... across not just automotive" anchored to SONACOMS Q3 FY26 (Jan-2026). Source truth: quote is verbatim in SONACOMS Q4 FY26 (30-Apr-2026), p.15, not in the Jan-2026 transcript. Wrong quarter attribution; Claim 5 CONTRADICTED verdict unaffected (two other correctly anchored peer quotes already satisfy the 2 anchor rule). source_fidelity false. |

Note on MAJOR count: Verifier A logged major_count 10 in its block; 9 individually itemised findings appear in its findings array (the tenth is captured in the aggregate count). B logged 2 MAJOR, D logged 1 MAJOR.

## MINOR

| Verifier | Location | Note |
|---|---|---|
| A | B12a aggregate | minor_count 3 recorded in the block; not individually itemised in the B12a findings array. |
| B | B05 section 1C (FY28 bridge) | PARTIALLY CAUGHT: execution bandwidth constraint and the "opportunities pushed out temporarily because of Indonesia load" admission not surfaced. Anchor: Q1 FY27 Jitendra opening. |
| B | B05 section 1B (component volume) | MISSED: management inconsistent on its own component volume (1mn / 3.3mn / 7 lakhs / 13 lakhs) in the Q4 call. Anchor: Q4 FY26 Karan Gupta / Jitendra / Sudhir. |
| B | B05 section 3C row 2 | Anchor imprecision: strip-Indonesia question attributed to Karan Gupta; actual asker Sumit Ambekar (Parami). Substance stands. |
| B | B05 section 2A promise-delivery table | Wording imprecision: "EV proof of concept demo by July" vs transcript "going into production". Direction correct. |
| C | B01 Block A (A1/A2/A4) | ROCE computable only FY25-FY26 due to a screener data gap; A4 trend scores on a 2 year window. Data constrained, transparently disclosed, not a threshold misapplication; classification already capped AVERAGE by deal breaker 3, so no score or decision impact. |
| C | B07 scorecard C1 | C1 labelled documented and claim mixed but multiplied at 1.0. Load bearing evidence is a filed investor presentation (documented), so 1.0 is defensible; a strict 0.7 read moves total 29.8 to 28.9, still within the 25 to 39 STRENGTHENING band. No classification change. |
| C | B07 completionist recount | Recount narrative bundles E1 into documented item categories though E1 is claim evidenced and correctly scored at 0.7. Cosmetic labelling only; active category count (9) and the 12 alarm threshold applied correctly. |
| D | Coverage map, HAPPYFORGE and SANSERA Q4 FY26 (May-2026) | Both graded CITED-ONLY. Not independently re-read line by line by the verifier (budget prioritised to 12 SUBSTANTIVE rows plus 2 of 4 CITED-ONLY rows, both confirmed accurate). Audit coverage gap on the verifier side, not a confirmed B06 defect; residual risk low. |
