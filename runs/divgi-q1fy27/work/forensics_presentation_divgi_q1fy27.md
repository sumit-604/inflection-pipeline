# A3 FORENSIC NOTES — Investor Presentation — DIVGI — Q1FY27

Source extract: `runs/divgi-q1fy27/work/extract_presentation_divgi_q1fy27.txt` (1344 lines, 41 slides)
Ledger reconciled against: `runs/divgi-q1fy27/work/ledger_presentation_divgi_q1fy27.md` (Tables 1-8, all rows read verbatim at cited lines) — **100% reconciled**
Doctype: presentation (investor deck). Balance-sheet / auditor / consolidation checks (F2-F5, F9, F12, F15) are largely N.A. by doctype and are marked so with a one-line reason. F16 is the primary presentation check.
Classification taxonomy (per task): RED-FLAG / AMBIGUOUS / FORWARD-SIGNAL / BENIGN. AMBIGUOUS and FORWARD-SIGNAL findings are flagged for A4 to convert into management questions.

Cross-document context (per orchestrator): the RESULTS filing is STANDALONE-ONLY (no consolidated). No prior-quarter presentation ledger exists (PRIOR_LEDGER_UNAVAILABLE), so DROPPED/REFRAMED diffs vs a prior deck could not be run. DIVGI is fresh to the pipeline — no companies/DIVGI.md, no prior Decision Status / tripwire / monitoring checklist. Checklist run on the deck's own merits.

---

## FINDINGS TABLE

| id | check | ledger row ref | slide / line | verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-01 | F1 | Table 5 #1 | slide 39 / L1263 | "(i) Non-current investments   0.0   0.0   0.0   0.0" | FORWARD-SIGNAL | Investment line stands at zero across Mar-23…Mar-26. With a US subsidiary now being formed/funded (slides 6, 34), this is the exact line that first populates in the FY27 standalone balance sheet. A non-zero here next period = cash left India into the US entity; watch it. |
| A3-02 | F6 | Table 4 #17/#24, #31, #15, #20, #22 | slides 10/18/20/34/13 | "Sigma production expected to commence in Q2FY27" (L362); "SOP expected to commence from Q2 FY27" (L607); "The board has approved setting up a 100% wholly owned subsidiary" (L1073); "production expected from CY26" (L471); "estimated completion by Q3 FY27" (L473) | FORWARD-SIGNAL | Dense set of dated, checkable management commitments with hard quarters attached (Q2FY27 Sigma SOP, Q3FY27 AT PoC, CY26 Indonesia production). These become the Role 5 promise-vs-delivery tracker. Sigma SOP is the single most load-bearing near-term catalyst and already slipped once (see A3-03). |
| A3-03 | F7 | Table 4 #6, #23, #2 | slides 7/13/6 | "EV business impacted in Q1 due to higher inventory at OEM in Q4, product mix change at OEM and delay in Sigma program launch" (L249-256); "OEMs assessing upcoming policy… to decide on investment for mass production" (L490-493); "Continue assessing business case for local manufacturing in US" (L211) | FORWARD-SIGNAL / AMBIGUOUS | Pre-emptive hedges. The EV/Sigma hedge is an explicit admission Q1 already missed on a delayed launch — the "expected from Q2" guidance is a re-date of a slipped milestone, not a fresh promise. Hybrid line is contingent on OEM (not company) decisions. US manufacturing is still "assessing", i.e., not committed. |
| A3-04 | F13 | Table 4 #31 | slide 34 / L1073-1076 | "The board has approved setting up a 100% wholly owned subsidiary to strengthen presence and expand opportunities in the US Markets" | FORWARD-SIGNAL | A board outcome beyond the results: formal approval to establish a US subsidiary foreshadows capital deployment / funding into the US. Pair with A3-01 (zero investments line) and A3-05 (timing conflict). |
| A3-05 | F14 | Table 4 note (slide 6 vs 34) | slide 6 / L208; slide 13 / L483; slide 34 / L1073 | slide 6: "Wholly owned subsidiary established in South Carolina"; slide 13: "Wholly owned subsidiary established in North America"; slide 34: "The board has approved setting up a 100% wholly owned subsidiary" | AMBIGUOUS | TIMING_INCONSISTENCY. Same US entity is described as already **established** (past tense, slides 6 & 13) yet only **board-approved to be set up** (prospective, slide 34) in the same deck. Either the entity is incorporated and slide 34 is stale boilerplate, or approval is fresh and slides 6/13 overstate. Management question: incorporation date vs board-approval date; is the SC entity legally live and funded? |
| A3-06 | F16 | Table 6 #9 | slide 37 / L1208 | "* As of 31st March 2026" (qualifying "~Rs. 96.92 crores already deployed" of IPO capex) | AMBIGUOUS | STALE_FOOTNOTE_DATE. A Q1FY27 deck (quarter ended 30-Jun-2026) reports IPO-proceeds deployment as of 31-Mar-2026 — one full quarter stale. Likely an intentional carryover of the year-end IPO-utilisation disclosure, but it means no Jun-26 deployment figure is given. Management question: deployed amount as of 30-Jun-2026 and remaining ~Rs 72.7 cr timeline. |
| A3-07 | F16 | Table 2c / 2d | slides 39 & 40 / L1248-1312 | Balance Sheet columns "Mar-26 Mar-25 Mar-24 Mar-23"; Cashflow columns "Mar-26 Mar-25 Mar-24 Mar-23" | AMBIGUOUS / FORWARD-SIGNAL | Disclosure-asymmetry item. The deck carries a Balance Sheet and Cashflow that the STANDALONE-ONLY Q1 results filing does not, AND both are dated to prior year-end (Mar-26), not to the Jun-26 quarter end. Investors get a P&L for Q1FY27 but no Jun-26 balance sheet / cashflow. Working-capital build (inventory 58.8, receivables 79.3 at Mar-26) is un-updated for the quarter. A4 to tie slide-14 Q1FY27 P&L to the filed standalone P&L. |
| A3-08 | F14 | Table 2a note | slide 14 / L519-522 | "EBIT 33.8 … Interest Expense 0.1 … Profit Before Tax 33.8" | BENIGN | ARITHMETIC_ROUNDING_NOTE. EBIT 33.8 − Interest 0.1 = 33.7 ≠ stated PBT 33.8 (also Q1FY26 12.1−0.1=12.0≠12.1; FY26 63.1−0.3=62.8≠62.7; PAT 33.8−8.5=25.3≠25.2). All are 0.1 artifacts of rounding unrounded underlyings; Q4FY26 and FY25 tie exactly. Not an error; noted for completeness. (Also note: deck's "Gross Profit" = Total Income − Raw Materials, i.e., includes Other Income — non-standard GP base, benign.) |
| A3-09 | F14 | Table 2d note | slide 40 / L1305 | "Net Decrease in Cash and Cash equivalents   16.1" | BENIGN | LABEL_SIGN_AMBIGUOUS — resolved. Row is labelled "Net Decrease" but Mar-26 value +16.1 is a net **increase** (Op 41.1 − Inv 16.1 − Fin 8.9 = +16.1; begin 15.4 + 16.1 = end 31.5, ties exactly). Static template label "Net Decrease" not toggled to Increase for the positive year. Value is correct and reconciles; label is a benign drafting artifact. |
| A3-10 | F16 | Table 1 slides 11/33/35/37; Table 7 | slides 11/33/35/37 | multi-panel bar/donut layouts | BENIGN (resolved) | CHART_LAYOUT_AMBIGUOUS — re-verified against rendered PDF (pages 11, 33, 35, 37). Resolutions below. Two of A2's tentative orderings were WRONG in the text-layer guess and are corrected here; had A4 anchored to A2's tentative order it would have mis-stated FY23 cash and the PAT series. |

---

## RESOLUTION OF A2 CHART-LAYOUT AMBIGUITIES (F16 / re-render from PDF)

Verified by reading rendered PDF pages 11, 33, 35, 37 and tying against the balance sheet (slide 39):

- **Slide 11 — Total Income Mix (%) Q1FY27:** Transfer Case **53%**, Components **24%**, Others **18%**, E-Gear Drive **4%**. (A2 tentatively had E-Gear 18% / Others 4% — swapped; now corrected.) Geographic Mix: Domestic **84%**, Exports **16%** (confirmed).
- **Slide 33 — Total Income FY23-FY26:** 278.7 / 273.0 / 240.1 / 375.2 (confirmed, ties slide 38 table). Segment % rows confirmed (TC 68/57/46/49; EGD 0/9/11/8; Comp 12/13/21/30).
- **Slide 35 — PAT FY21-FY26:** 38 / 46 / 51 / 40 / 24 / 47 (confirmed vs slide 38 PAT 38.3/46.2/51.2/39.7/24.4/46.9). Total Income 195/242/279/273/240/375 and EBITDA 60/74/82/73/59/92 confirmed. (A2 tentative "24/40/47/51/46/38" order was wrong.)
- **Slide 37 — Cash Reserves FY21-FY26:** 159 / 173 / **311** / 264 / 285 / 295. **FY23 = 311**, tied to Mar-23 balance sheet (Bank balances 306.6 + Cash 4.8 = 311.4). Capex FY21-FY26: 26/40/68/78/27/44 (confirmed). (A2 tentative "…295/311" put 311 at FY26 — wrong; corrected.)

Net: all four ambiguous slides are now anchored. No thesis figure is left unverified.

---

## CHECKLIST SCORECARD (all 17 — no blanks)

| Check | Status | One-line basis |
|---|---|---|
| F1  ZERO-VALUE STANDING ITEMS | **FINDING** | Two ZERO_STANDING rows read: (i) Non-current investments 0.0×4 (slide 39, L1263) → A3-01 FORWARD-SIGNAL (US-sub funding will populate it). Leverage ratios 0.0×6 (slide 36, L1163) = benign, corroborates net-cash (Net Debt (232.6) Cr). |
| F2  STANDALONE vs CONSOLIDATED | **N.A.** | Deck and results filing are STANDALONE-ONLY; no consolidated figures exist to decompose. US subsidiary newly formed, not yet consolidated. |
| F3  SHELL-ENTITY DETECTION | **N.A.** | No consolidated cost lines to compare. Single reporting entity; US sub has only "Initial headcount on-boarded" (L210), pre-operational, no financials disclosed. |
| F4  UNAUDITED CONTRIBUTION RATIO | **N.A.** | No auditor Other-Matters paragraph in a presentation; no JV/associate/component-auditor numbers. |
| F5  GOING CONCERN / EoM SCOPE | **N.A.** | No auditor report / EoM in an investor deck. Nothing to verbatim-diff. |
| F6  FORWARD-COMMITMENT PHRASE MINING | **FINDING** | Lexicon hits dense: "board has approved" (L1073), "expected to commence Q2FY27" (L362/L607), "expected from CY26" (L471), "estimated completion by Q3 FY27" (L473), "quote submitted"/"Proposal submitted"/"Prototype submitted" (L465/L478/L482). → A3-02 FORWARD-SIGNAL. See Commitment Register. |
| F7  HEDGE PHRASE MINING | **FINDING** | "EV business impacted in Q1… delay in Sigma program launch" (L249), "OEMs assessing… to decide on investment" (L490), "Continue assessing business case for local manufacturing in US" (L211), "evaluate manufacturing footprint in US" (L661). → A3-03. |
| F8  TAX FORENSICS | **PASS** | ETR each period near statutory 25.17%: Q1FY27 8.5/33.8=25.1%; Q1FY26 26.4%; Q4FY26 23.3%; FY26 25.2%; FY25 26.1% (slide 14, L522-523; slide 38, L1237-1239). No current/deferred split or "earlier-year" tax line in the deck; nothing anomalous. |
| F9  OCI FORENSICS | **N.A.** | Deck carries P&L, BS, CF only — no OCI / actuarial statement. Nothing to trend. |
| F10 SHARE COUNT & DILUTION | **PASS** | Equity Share Capital 15.3 constant Mar-23→Mar-26 (slide 39, L1253); no corporate action, no EPS / diluted-EPS spread disclosed. Post-IPO (2023) count stable. |
| F11 RESERVES / NET WORTH TIE-OUT | **PASS** | Other Equity 620.2 + Paid-up 15.3 = 635.5 net worth (Mar-26). Equity+liabilities foot to Total 731.4 within ~0.9 rounding across lines. No conflicting third-party net-worth figure in deck. |
| F12 SEGMENT FORENSICS | **N.A.** | Deck shows segment **revenue** only (Transfer Case / E-Gear Drive / Components, slides 8/13/33); no segment assets or liabilities disclosed to trend. |
| F13 BOARD OUTCOME BEYOND RESULTS | **FINDING** | Board-approved US subsidiary (slide 34, L1073) → A3-04 FORWARD-SIGNAL. No AGM notice, AR approval, or director term dates in the deck (roster names only, slides 30-31) — those checks not exercisable here. |
| F14 NOTE / DRAFTING INCONSISTENCIES | **FINDING** | US-sub described "established" (L208/L483) vs "board has approved setting up" (L1073) → A3-05 AMBIGUOUS. Entity typo "Toyota Susho" (L370) vs "Toyota Tsusho" (L581/L793) = BENIGN. P&L 0.1 arithmetic drift → A3-08 BENIGN. Cashflow "Net Decrease" mislabel → A3-09 BENIGN. |
| F15 ENTITY LIST DIFFS | **N.A.** | No consolidation entity list in deck; no prior-quarter ledger to diff (PRIOR_LEDGER_UNAVAILABLE). Note: US subsidiary is the incoming addition to any future consolidation list — carry forward. |
| F16 PRESENTATION-SPECIFIC (dropped/reframed) | **FINDING** | STALE_FOOTNOTE_DATE (A3-06), presentation-only BS/CF dated to Mar-26 not Jun-26 (A3-07), chart-layout ambiguities re-rendered & 2 corrected (A3-10). Prior-deck DROPPED diff not runnable (PRIOR_LEDGER_UNAVAILABLE) — known gap, not a finding. |
| F17 CONCALL SILENCE AUDIT | **N.A.** | Doctype is presentation, not a concall transcript; and no prior Notion monitoring checklist exists for this fresh company. |

**Status counts: PASS = 3 (F8, F10, F11) · FINDING = 6 (F1, F6, F7, F13, F14, F16) · N.A. = 8 (F2, F3, F4, F5, F9, F12, F15, F17). Total 17, no blanks. GATE A3: PASS.**

---

## COMMITMENT REGISTER (from F6) — feeds Role 5 promise-vs-delivery tracker

| commitment | implied date | slide / line ref | status word |
|---|---|---|---|
| US wholly-owned subsidiary (Divgi Transmission Technologies and Systems Inc, South Carolina) | Q1FY27 (claimed done) | slide 6 / L208 | established (claimed) |
| Initial headcount on-boarded at US sub | Q1FY27 | slide 6 / L210 | completed |
| Board approval to set up 100% US subsidiary | Q1FY27 | slide 34 / L1073 | approved / initiated |
| Sigma EV programme production / SOP | Q2FY27 (Jul-Sep 2026) | slide 10 / L362; slide 18 / L607; slide 20 / L665 | underway (re-dated after Q1 slip) |
| Indonesia Pik-Up 4x4 transfer-case production | CY26 | slide 13 / L471 | underway |
| Automatic Transmission PoC on customer vehicle | Q3FY27 | slide 13 / L473 | underway |
| AT commercial quote to leading Indian OEM | submitted | slide 13 / L465 | submitted |
| 5-speed Manual Transmission proposal (commercial truck) | open | slide 13 / L478 | submitted |
| Synchronizer prototype to market-leader OEM (off-highway) | open | slide 13 / L482 | submitted |
| FY27 component exports target ~Rs 80 cr | FY27 | slide 10 / L356 | guidance (numeric) |
| Export parts final production approval → ~Rs 10-12 cr/month potential | ramping | slide 20 / L664-667 | approved / ramp |

---

## HOW THE FIVE A2-FLAGGED ISSUES WERE RESOLVED

1. **TIMING_INCONSISTENCY (slide 6 vs 34)** → A3-05, F14, **AMBIGUOUS** (management question). Slides 6 (L208) and 13 (L483) call the US subsidiary "established"; slide 34 (L1073) calls it "board has approved setting up". Same-deck tense conflict — cannot be reconciled from the deck alone (no results-filing note text available here). Question for management: incorporation date and funding status of the SC entity vs the board-approval date.
2. **STALE_FOOTNOTE_DATE (slide 37)** → A3-06, F16, **AMBIGUOUS**. Footnote "* As of 31st March 2026" confirmed present in the rendered PDF, qualifying "~Rs 96.92 cr already deployed" of Rs 169.66 cr IPO capex, inside a Jun-26-quarter deck. Read as an intentional year-end IPO-utilisation carryover, but it leaves no Jun-26 figure. Question: deployment as of 30-Jun-2026 and remaining ~Rs 72.7 cr timeline.
3. **ARITHMETIC_ROUNDING_NOTE (slide 14)** → A3-08, F14, **BENIGN**. EBIT 33.8 − Interest 0.1 = 33.7 ≠ PBT 33.8; same 0.1 pattern on Q1FY26, FY26, and PAT. Q4FY26/FY25 tie exactly. Pure rounding of unrounded underlyings, not an error.
4. **LABEL_SIGN_AMBIGUOUS (slide 40)** → A3-09, F14, **BENIGN (resolved)**. "Net Decrease in Cash and Cash equivalents" = +16.1 is actually a net increase (Op 41.1 − Inv 16.1 − Fin 8.9 = +16.1; 15.4 + 16.1 = 31.5). Value correct and reconciles; label is a static template artifact for the positive-cash year.
5. **CHART_LAYOUT_AMBIGUOUS (slides 11, 33, 35, 37)** → A3-10, F16, **BENIGN (resolved)** by re-rendering the PDF and tying to the balance sheet. Corrections made: slide 11 mix is TC 53 / Comp 24 / Others 18 / EGD 4 (A2 swapped Others & EGD); slide 35 PAT series is 38/46/51/40/24/47; slide 37 Cash Reserves is 159/173/311/264/285/295 with FY23 = 311 (ties Mar-23 BS 306.6+4.8). A2's tentative orderings for slides 35 and 37 were wrong and are corrected — A4 must use the corrected values.

**Cross-document disclosure-quality flag (A3-07, F16):** the deck presents a Balance Sheet (slide 39) and Cashflow (slide 40) that the STANDALONE-ONLY results filing does not, and both are dated to Mar-26, not the Jun-26 quarter end — investors get a Q1FY27 P&L but no matching quarter-end balance sheet or cashflow. A4 to (a) tie slide-14 Q1FY27 P&L to the filed standalone P&L and (b) raise the missing Jun-26 balance-sheet / working-capital position as a question.

---

```yaml
stage: A3-forensics
company: "divgi"
quarter: "q1fy27"
doctype: "presentation"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/divgi-q1fy27/work/forensics_presentation_divgi_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: PASS
  F9: N.A.
  F10: PASS
  F11: PASS
  F12: N.A.
  F13: FINDING
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: N.A.
findings:
  - {id: "A3-01", check: "F1", line: "slide 39 / L1263", classification: "FORWARD-SIGNAL", implication: "Zero non-current investments line is where imminent US-subsidiary funding first appears in FY27 BS"}
  - {id: "A3-02", check: "F6", line: "slides 10/18/20/34/13 / L362,L607,L1073,L471,L473", classification: "FORWARD-SIGNAL", implication: "Dated checkable commitments: Sigma SOP Q2FY27, AT PoC Q3FY27, Indonesia CY26, board-approved US sub"}
  - {id: "A3-03", check: "F7", line: "slides 7/13/6 / L249,L490,L211", classification: "FORWARD-SIGNAL", implication: "EV/Sigma Q1 miss re-dated to Q2; hybrid contingent on OEM; US manufacturing still 'assessing'"}
  - {id: "A3-04", check: "F13", line: "slide 34 / L1073", classification: "FORWARD-SIGNAL", implication: "Board-approved US subsidiary foreshadows US capital deployment"}
  - {id: "A3-05", check: "F14", line: "slide 6 L208 vs slide 34 L1073", classification: "AMBIGUOUS", implication: "US sub 'established' vs 'board approved setting up' in same deck; needs incorporation-date clarification"}
  - {id: "A3-06", check: "F16", line: "slide 37 / L1208", classification: "AMBIGUOUS", implication: "IPO capex deployment dated 31-Mar-2026 in a Jun-26 deck; no Q1FY27 update given"}
  - {id: "A3-07", check: "F16", line: "slides 39-40 / L1248-1312", classification: "AMBIGUOUS", implication: "Presentation-only BS/CF absent from standalone filing and dated to Mar-26, not Jun-26 quarter end"}
  - {id: "A3-08", check: "F14", line: "slide 14 / L519-522", classification: "BENIGN", implication: "0.1 rounding drift EBIT-Interest vs PBT; not an error"}
  - {id: "A3-09", check: "F14", line: "slide 40 / L1305", classification: "BENIGN", implication: "'Net Decrease' label on a +16.1 net increase; value reconciles, label is template artifact"}
  - {id: "A3-10", check: "F16", line: "slides 11/33/35/37", classification: "BENIGN", implication: "Chart layouts re-rendered from PDF; A2 orderings for slides 35 & 37 corrected (FY23 cash=311)"}
forward_signals: ["A3-01", "A3-02", "A3-03", "A3-04"]
ambiguous: ["A3-05", "A3-06", "A3-07"]
commitments:
  - {commitment: "US wholly-owned subsidiary established (South Carolina)", implied_date: "Q1FY27", ref: "slide 6 / L208", status_word: "established (claimed)"}
  - {commitment: "Initial headcount on-boarded at US sub", implied_date: "Q1FY27", ref: "slide 6 / L210", status_word: "completed"}
  - {commitment: "Board approval to set up 100% US subsidiary", implied_date: "Q1FY27", ref: "slide 34 / L1073", status_word: "approved"}
  - {commitment: "Sigma EV production / SOP", implied_date: "Q2FY27", ref: "slide 18 / L607", status_word: "underway"}
  - {commitment: "Indonesia Pik-Up 4x4 production", implied_date: "CY26", ref: "slide 13 / L471", status_word: "underway"}
  - {commitment: "Automatic Transmission PoC completion", implied_date: "Q3FY27", ref: "slide 13 / L473", status_word: "underway"}
  - {commitment: "AT commercial quote to Indian OEM", implied_date: "open", ref: "slide 13 / L465", status_word: "submitted"}
  - {commitment: "5-speed Manual Transmission proposal", implied_date: "open", ref: "slide 13 / L478", status_word: "submitted"}
  - {commitment: "Synchronizer prototype to OEM", implied_date: "open", ref: "slide 13 / L482", status_word: "submitted"}
  - {commitment: "FY27 component exports ~Rs 80 cr", implied_date: "FY27", ref: "slide 10 / L356", status_word: "guidance"}
  - {commitment: "Export parts approval -> ~Rs 10-12 cr/month", implied_date: "ramping", ref: "slide 20 / L664", status_word: "approved"}
gate_a3: pass
blank_checks: []
```
