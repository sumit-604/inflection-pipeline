# A3 FORENSIC NOTES — Macfos Limited (MCFOS), Q1 FY27, doctype: PRESENTATION

Source extract: `/home/user/inflection-pipeline/runs/mcfos-q1fy27/work/extract_presentation_mcfos_q1fy27.txt`
A2 ledger: `/home/user/inflection-pipeline/runs/mcfos-q1fy27/work/ledger_presentation_mcfos_q1fy27.md`
Prior-quarter presentation extract: none (first MCFOS deck; NO_PRIOR_LEDGER — this run sets the baseline for future deck diffs).
Companion document: results-filing A3 at `/home/user/inflection-pipeline/runs/mcfos-q1fy27/work/forensics_mcfos_q1fy27.md` (same quarter, run first). Where the deck confirms/resolves or stays silent on a results forward-signal, it is noted.
Ledger reconciliation: 100% — every A2 slide/line_item/slide_number/footnote row read at its cited line before judging.
Units: Lakhs on P&L (page 16) and KPI charts (pages 14-15, x0.01=Cr); FY-history figures on pages 6 & 8 printed in Crore verbatim.
Doctype lens: F16 is the primary lens (dropped/reframed disclosures). F6/F10/F11 run against any commitment/share/net-worth numbers the deck carries. F1/F2/F3/F4/F5/F8/F9 are N.A. for a deck unless it reproduces the relevant statement (the deck reproduces only the STANDALONE P&L). F17 is N.A. (no transcript); its silence logic is run against the Notion checklist and folded into F16.
Bias: conservative; lean bear and generate an A4 question on ambiguity.

---

## FINDINGS TABLE

| id | check | ledger row ref | slide/line | short verbatim quote | classification | forward implication |
|----|-------|----------------|------------|----------------------|----------------|---------------------|
| F6-01 | F6 | slides 18,19,21,22,23 | s21 / L601-603; s23 / L632-633; s18 / L550-551 | "NEW PRODUCTS TO BE DESIGNED AND DEVELOPED WITH SPECIAL FOCUS ON DRONE AND IT'S PARTS" ; "aligning with our long-term goals for the next 5 to 10 years" | FORWARD-SIGNAL | Every deck commitment is soft, undated and horizon-distant (5-10 yr); no numeric guidance, no near-term dated milestone. Baseline promise set for the Role 5 promise-vs-delivery tracker. Track whether "to be designed" drone/OEM SKUs and ERP/IT build convert to disclosed revenue. |
| F7-01 | F7 | footnotes 7,8,9; slide 18 | s14/16/15 note L455-456, L488-489, L523-524; s18 / L545 | "Comparative figures for Q1 FY 2025-26 have been restated under Ind AS. Ind AS figures for the full year FY 2024-25 have not been presented" ; "despite an uncertain global environment" | CONFIRMATORY-NEGATIVE | Every headline YoY growth number (38%/22%/18%) rests on management-restated, un-reviewed Ind AS comparatives (confirms results-A3 F7-01). FY24-25 Ind AS base withheld, so the multi-year CAGR claims (58%/53%/53%, slide 6) are on a different, non-restated basis than the YoY optics. |
| F14-01 | F14 | slides 6/8, 18; footnotes 2,3,4 | s6 L157-158 vs s8 L238; s18 L542; s10 L314/332; s12 L407-409 | "Reaching Turnover of 256 Cr in FY 24-25" (s6) vs table "257.68" (s8) ; "growth of ... 18% in PAT" (computed 17.15%) | NEUTRAL-FACT | Cumulative drafting hygiene: FY24-25 turnover stated two ways (1.68 Cr gap); PAT growth rounded up (17.15%->18%); "Q1 TY 2026-27" typo on the title slide itself; asterisk markers inconsistent (*** vs **, three sentences on one "*"). Individually immaterial; every rounding error runs in the favourable direction. |
| F16-01 | F16 | s6/8/14/18 LABEL_MISMATCH | s18 / L541; s14 / L438,444,446; s16 / L502-503 | "The Company delivered revenue of Rs 82.46 crore" (= Total Income 8,245.91L; Revenue-from-Operations is 81.34 Cr / 8,133.87L) | AMBIGUOUS | The deck labels Total Income as "Revenue" on 4 slides. Other Income spiked +85% YoY (60.54->112.04L, L502) — the reframing flatters the top line and lifts stated growth (38% vs 37.2% on Revenue-from-Operations). Ask what drove the +85% other-income jump and why it is folded into "Revenue". |
| F16-02 | F16 (F17-logic) | s23 EXPECTED_DISCLOSURE_ABSENT; s18 | s18 / L552; s23 / L638-645 | "We are witnessing increasing traction from corporate customers" (no B2B % anywhere) | FORWARD-SIGNAL | Notion monitors B2B corporate share (hold 50-60%, red <45%). Deck touts corporate traction but never quantifies it; only per-vertical SKU counts (slide 23). Monitor stays dark — confirms results-A3 F12-01 opacity. A4 question: state the B2B/corporate revenue %. |
| F16-03 | F16 (F17-logic) | s19/21/23 EXPECTED_DISCLOSURE_ABSENT | s19 / L571; s23 / L641-646 | "this vertical has gained significant momentum, particularly in the Drone ecosystem" (no revenue share) | FORWARD-SIGNAL | Notion monitors Robu 2.0 revenue share (green any >5% disclosed; red mgmt stops discussing). Management still discusses it (not red) but gives only SKU counts (7 drone, 295 electronics, 650 OEM), never a revenue contribution %. Amber. A4 question: Robu 2.0 % of revenue. |
| F16-04 | F16 | s1 vs s16 EXPECTED_DISCLOSURE_ABSENT | s1 / L30-32; s16 / L498-521 | "Investor Presentation in connection with Unaudited Standalone and consolidated Financial Statement" (only standalone P&L appears) | AMBIGUOUS | Cover letter promises consolidated scope; the deck reproduces the standalone P&L only (cross-check clean vs results ledger). The withheld consolidated view is the one that would surface Nuo Zhan (HK shell, results-A3 F3-01) and Macfos Electronics. A4 question: why is the promised consolidated statement absent from the deck. |
| F16-05 | F16 (F17-logic) | s15 vs missing BS/CF; s16 finance cost | s15 / L465-484 (ROCE/RoNW); s16 / L509 (finance cost); s16 / L507 (inventory) | ROCE "27.42% ... 31.08%" and Return on Net Worth shown, but no net-worth Rs figure, no cash flow, no borrowings slide | FORWARD-SIGNAL | The deck prints balance-sheet-DERIVED ratios (ROCE, RoNW) — proving management holds the balance sheet — yet withholds CFO, borrowings, working capital and the absolute net worth. Meanwhile finance cost is +79% YoY (56.05->100.40L) and inventory built Rs 17.9 Cr this quarter (Changes in Inventory (1,791.36)L). Confirms and sharpens results-A3 F11-01: the data exists and was still not shown. Five Notion balance-sheet monitors (CFO/PAT, inventory days, receivable days, ST borrowings, net worth) stay dark. |
| F16-06 | F16 (F15/F17-logic) | deck entity silence vs results F15-01 | s19 / L569-576; s23 / L630-651 | "move further up the technology value chain—from distributing products to developing products of our own ... engagements with Government and Defense organizations" | FORWARD-SIGNAL | The ROBU 2.0 narrative describes exactly what a new "Macfos Electronics Private Limited" subsidiary (results-A3 F15-01) would house — own-brand/drone/defense productisation — yet the deck never names the entity or gives its financials. Partially resolves F15-01's "what is it for" (Robu 2.0 vehicle) while staying silent on the corporate structure. A4 question: is Macfos Electronics the manufacturing/assembly vehicle for Robu 2.0. |
| F16-07 | F16 (F17-logic) | Notion catalyst silence | deck-wide (no mention); s1 / L24 scrip "ROBU | 543787" | (no mainboard-migration statement anywhere in the deck) | FORWARD-SIGNAL | Notion tripwire: red if no mainboard-listing announcement by Q2 FY27. This Q1 deck — the natural venue to trail a migration — is silent, leaving one quarter of runway. A4 question: any BSE mainboard migration timeline. |
| F16-08 | F16 (F17-logic) | s15 EBITDA%/PAT% charts | s15 / L465,468,474 (PAT% 8.30->7.06; EBITDA% 13.40->11.83); s18 / L542 | "growth of 38% in revenue, 22% in EBITDA and 18% in PAT" (letter frames absolute growth, not margins) | FORWARD-SIGNAL | Pairing resolved computationally (values tie to P&L margins, clearing A2's CHART_OCR_AMBIGUOUS on slide 15): EBITDA margin 13.40%->11.83% and PAT margin 8.30%->7.06% YoY, RoNW 6.88%->5.94%. PAT margin is now below Notion green (7.5%) and below FY26's own 8.21%, drifting toward the 6.5% red. The letter reframes this compression as double-digit absolute "growth". Lean bear: margins decelerating while volume grows. |
| F16-09 | F16 (F17-logic) | s12 slow-moving inventory | s12 / L403-405 | "5.52 % Inventory is Very Slow-moving (Compared to 6.21 % as of Mar-26)" | NEUTRAL-FACT | New monitor the results filing could not show; Notion tripwire green <5%, red >8%. At 5.52% it is amber but improving 69 bps QoQ. Favourable, disclosed. Watch for a cross toward the 5% green. |

---

## CHECKLIST SCORECARD (all 17)

| Check | Status | One-line basis |
|-------|--------|----------------|
| F1 ZERO-VALUE STANDING LINES | PASS | Deck reproduces the standalone P&L (slide 16); 2 zero-standing rows read — Exceptional Item nil all periods (L515) and OCI nil in both quarter columns (L519). Standard Ind AS template lines; values cross-check clean to results ledger; no line anticipates an undisclosed transaction class. |
| F2 STANDALONE vs CONSOLIDATED | N.A. | Deck reproduces the STANDALONE P&L only; no consolidated statement in the deck to decompose. The promised-but-absent consolidated is itself flagged (F16-04); S-vs-C decomposition done at results-A3 F2 PASS. |
| F3 SHELL-ENTITY DETECTION | N.A. | Shell detection needs S-vs-C cost lines; deck carries standalone cost lines only. Nuo Zhan HK shell adjudicated at results-A3 F3-01. |
| F4 UNAUDITED CONTRIBUTION RATIO | N.A. | No auditor "Other Matters" / component-auditor disclosure in a marketing deck. Adjudicated at results-A3 F4 PASS. |
| F5 GOING CONCERN / EoM SCOPE | N.A. | No auditor report / EoM / going-concern paragraph in the deck; nothing to diff. No prior deck. |
| F6 FORWARD-COMMITMENT MINING | FINDING | Deck carries soft, undated forward commitments ("to be designed and developed", "next 5 to 10 years", "next phase of growth", ERP/IT build). See F6-01 and Commitment Register. |
| F7 HEDGE PHRASE MINING | FINDING | Ind AS comparability caveat (comparatives management-restated, FY24-25 Ind AS "not presented", repeated 3x) plus macro hedge "despite an uncertain global environment" qualify the headline growth. See F7-01. |
| F8 TAX FORENSICS | N.A. | Deck aggregates tax into one line (210.18 / 174.50 / 874.55, L517); no deferred-tax sign or earlier-years line reproduced. ETR ~26.5% consistent; disaggregated tax forensics at results-A3 F8-01. |
| F9 OCI FORENSICS | N.A. | Deck reproduces the OCI line (nil both quarters, (16.47) FY26, L519) with no actuarial detail/assumptions; no current-quarter swing. Substantive OCI at results-A3 F9 PASS. |
| F10 SHARE COUNT AND DILUTION | N.A. | Deck carries no share count, no EPS row (P&L stops at Total Comprehensive Income), no paid-up capital figure. Dilution/bonus-issue forensics at results-A3 F10 PASS. |
| F11 RESERVES / NET WORTH TIE-OUT | N.A. | Deck shows RoNW% and ROCE% (slide 15) but no absolute net worth/reserves figure to tie out — nothing to reconcile. The disclosure choice (ratios shown, absolutes/cash-flow withheld) is routed to F16-05. |
| F12 SEGMENT FORENSICS | N.A. | No segment table in the deck (single-segment company). The thesis-critical B2B corporate share and Robu 2.0 revenue share are absent — routed to F16-02 / F16-03 per silence-audit logic; segment declaration adjudicated at results-A3 F12-01. |
| F13 BOARD OUTCOME BEYOND RESULTS | N.A. | A presentation carries no board resolutions / AGM notice / director-appointment terms. Board outcomes (AR FY26, 9th AGM, director re-appointment) adjudicated at results-A3 F13-01/F13-02. |
| F14 NOTE DRAFTING INCONSISTENCIES | FINDING | FY24-25 turnover stated 256 Cr (s6) vs 257.68 (s8); PAT growth 18% stated vs 17.15% computed; "Q1 TY 2026-27" typo on title slide; asterisk-marker inconsistencies. Cumulative governance-hygiene data point. See F14-01. |
| F15 ENTITY LIST DIFFS | N.A. | Deck lists no consolidation entity list to diff; it never names Macfos Electronics or Nuo Zhan. The silence on the new subsidiary amid the Robu 2.0 vertical-integration narrative is routed to F16-06; entity diff adjudicated at results-A3 F15-01. |
| F16 DROPPED / REFRAMED DISCLOSURES | FINDING | Primary lens. Revenue=Total-Income relabel; B2B share, Robu 2.0 share, consolidated P&L, cash-flow/borrowings/net-worth all absent; new subsidiary and mainboard catalyst unmentioned; margin compression reframed as absolute growth; slow-moving inventory newly (favourably) disclosed. See F16-01..F16-09. No prior deck to diff — baseline set. |
| F17 CONCALL SILENCE AUDIT | N.A. | No transcript. Silence logic run against the Notion checklist and folded into F16: deck goes dark on CFO/PAT, inventory days, receivable days, ST borrowings, net worth, B2B share, Robu 2.0 share, promoter pledge and mainboard listing (9 of 13 monitors); adds revenue growth, EBITDA/PAT margins, ROCE/RoNW and slow-moving inventory %. |

---

## SILENCE AUDIT — Notion monitor coverage (F17-logic, folded into F16)

| Monitor (Notion) | Deck coverage | Read | Finding |
|------------------|---------------|------|---------|
| Revenue growth YoY (green >=30, red <20) | Disclosed 38% (Total Income basis; 37.2% Rev-from-Ops) | GREEN | F16-01 (label) |
| EBITDA margin (green >=10, red <9 x2q) | Disclosed s15: 13.40%->11.83% | GREEN, compressing | F16-08 |
| PAT margin (green >=7.5, red <6.5) | Disclosed s15: 8.30%->7.06% | AMBER, toward red | F16-08 |
| CFO/PAT | Not shown | DARK | F16-05 |
| Inventory days (red >90) | Not shown (only Rs 17.9 Cr build visible) | DARK | F16-05 |
| ROCE TTM (green >=28, red <20 x2yr) | Disclosed s15 ~27-31% (OCR-noisy 5.59% ignored) | GREEN | — |
| B2B corporate share (hold 50-60, red <45) | Not shown | DARK | F16-02 |
| Robu 2.0 revenue share (green >5 disclosed) | Qualitative only, no % | AMBER | F16-03 |
| Slow-moving inventory % (green <5, red >8) | Disclosed 5.52% (from 6.21%) | AMBER, improving | F16-09 |
| Promoter pledge (red any) | Not shown | DARK (low weight for a KPI deck) | F16-05 (grouped) |
| Mainboard listing (red no announce by Q2 FY27) | Not mentioned | DARK, 1 qtr runway | F16-07 |
| ST borrowings (red >Rs 50 Cr) | Not shown (finance cost +79% visible) | DARK | F16-05 |
| Receivable days (red >20 x2q) | Not shown | DARK | F16-05 |

Results forward-signals status in the deck: F11-01 CONFIRMED and sharpened (ratios shown, absolutes withheld — F16-05); F12-01 CONFIRMED (B2B + Robu 2.0 still hidden — F16-02/03); F15-01 PARTIALLY RESOLVED on purpose (Robu 2.0 vehicle) but entity unnamed (F16-06).

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | slide/line ref | status word |
|------------|--------------|----------------|-------------|
| New products to be designed & developed, special focus on Drone & its parts | undated | slide 21, L601-603 | to be / intended |
| Continue to invest in R&D and product development (Robu 2.0 / Simplify brand) | ongoing | slide 19, L573 | underway |
| Build own brands/products for "competitive edge ... next 5 to 10 years" | 5-10 yr horizon | slide 23, L632-633 | intended |
| Investments to "create the capacity required for the next phase of growth" | next phase (undated) | slide 18, L550-551 | underway |
| Maximize ERP use in operations; scalable in-house IT infrastructure | undated | slide 21, L612-616 | intended |
| Increase corporate-customer reach / fulfilment speed & warehouse mgmt | undated | slide 21, L603-615 | intended |

All undated, qualitative, no numeric guidance. No prior deck to diff — this is the baseline promise set for the Role 5 promise-vs-delivery tracker.

---

## FORWARD-SIGNAL SUMMARY (for A4 -> management questions)

- FORWARD-SIGNAL: F6-01, F16-02, F16-03, F16-05, F16-06, F16-07, F16-08
- AMBIGUOUS (lean-bear, question not resolved): F16-01, F16-04
- CONFIRMATORY-NEGATIVE: F7-01
- NEUTRAL-FACT: F14-01, F16-09

Highest-value A4 questions: (1) why is Total Income labelled "Revenue" and what drove Other Income +85% YoY [F16-01]; (2) state B2B/corporate revenue share and Robu 2.0 revenue share — both touted, neither quantified [F16-02, F16-03]; (3) why show ROCE/RoNW ratios but withhold cash flow, borrowings and net worth when finance cost is +79% YoY and inventory built Rs 17.9 Cr [F16-05]; (4) is Macfos Electronics Pvt Ltd the Robu 2.0 manufacturing vehicle, and why is the promised consolidated statement absent [F16-06, F16-04]; (5) mainboard-migration timeline before the Q2 FY27 tripwire [F16-07]; (6) PAT margin compressed to 7.06% (below FY26's 8.21% and the 7.5% green) — outlook [F16-08].

Notion read (context, not a check): Revenue +38% = green; EBITDA margin 11.83% = green but down 157 bps YoY; PAT margin 7.06% = amber, below green and below FY26; slow-moving inventory 5.52% = amber, improving; ROCE ~27-31% = green; B2B share, Robu 2.0 share, CFO/PAT, inventory/receivable days, ST borrowings, net worth, promoter pledge, mainboard listing = UNDISCLOSED this deck.

---

```yaml
stage: A3-forensics
company: "MCFOS"
quarter: "Q1 FY27"
doctype: "presentation"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/mcfos-q1fy27/work/forensics_presentation_mcfos_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: PASS
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: N.A.
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
  - {id: "F6-01", check: "F6", line: "s21/L601-603", classification: "FORWARD-SIGNAL", implication: "All deck commitments soft, undated, 5-10yr horizon; no numeric guidance; baseline promise set for Role 5 tracker"}
  - {id: "F7-01", check: "F7", line: "s14/L455-456", classification: "CONFIRMATORY-NEGATIVE", implication: "Headline 38/22/18% growth rests on management-restated unreviewed Ind AS comparatives; FY24-25 Ind AS base withheld"}
  - {id: "F14-01", check: "F14", line: "s6/L157-158 vs s8/L238", classification: "NEUTRAL-FACT", implication: "FY24-25 turnover 256 vs 257.68 Cr; PAT growth 18% vs 17.15%; TY/FY title typo; asterisk inconsistencies; errors favour the deck"}
  - {id: "F16-01", check: "F16", line: "s18/L541", classification: "AMBIGUOUS", implication: "Total Income relabelled Revenue on 4 slides; Other Income +85% YoY flatters top line and growth optics"}
  - {id: "F16-02", check: "F16", line: "s18/L552; s23/L638-645", classification: "FORWARD-SIGNAL", implication: "Corporate traction touted, B2B revenue share never quantified; Notion B2B monitor dark; confirms results F12-01"}
  - {id: "F16-03", check: "F16", line: "s19/L571; s23/L641-646", classification: "FORWARD-SIGNAL", implication: "Robu 2.0 discussed qualitatively (SKU counts only), no revenue share %; Notion monitor amber"}
  - {id: "F16-04", check: "F16", line: "s1/L30-32 vs s16", classification: "AMBIGUOUS", implication: "Cover letter promises consolidated scope; only standalone P&L shown; consolidated would surface Nuo Zhan + Macfos Electronics"}
  - {id: "F16-05", check: "F16", line: "s15/L465-484; s16/L509,507", classification: "FORWARD-SIGNAL", implication: "ROCE/RoNW ratios shown but cash flow/borrowings/net worth withheld while finance cost +79% YoY and Rs17.9Cr inventory build; confirms/sharpens results F11-01"}
  - {id: "F16-06", check: "F16", line: "s19/L569-576; s23/L630-651", classification: "FORWARD-SIGNAL", implication: "Robu 2.0 own-product/drone/defense narrative likely explains new Macfos Electronics subsidiary; entity itself never named; partial resolution of results F15-01"}
  - {id: "F16-07", check: "F16", line: "deck-wide; s1/L24", classification: "FORWARD-SIGNAL", implication: "No mainboard-migration mention; Notion red if no announcement by Q2 FY27; one quarter of runway"}
  - {id: "F16-08", check: "F16", line: "s15/L465,474; s18/L542", classification: "FORWARD-SIGNAL", implication: "EBITDA margin 13.40->11.83%, PAT margin 8.30->7.06% (below green 7.5% and FY26 8.21%); letter reframes compression as absolute growth"}
  - {id: "F16-09", check: "F16", line: "s12/L403-405", classification: "NEUTRAL-FACT", implication: "Slow-moving inventory 5.52% (from 6.21%) newly disclosed; Notion amber, improving 69bps QoQ"}
forward_signals: ["F6-01", "F16-02", "F16-03", "F16-05", "F16-06", "F16-07", "F16-08"]
ambiguous: ["F16-01", "F16-04"]
commitments:
  - {commitment: "New products to be designed & developed, focus on Drone & parts", implied_date: "undated", ref: "slide 21, L601-603", status_word: "intended"}
  - {commitment: "Continue to invest in R&D / product development (Robu 2.0)", implied_date: "ongoing", ref: "slide 19, L573", status_word: "underway"}
  - {commitment: "Build own brands for competitive edge over next 5 to 10 years", implied_date: "5-10yr horizon", ref: "slide 23, L632-633", status_word: "intended"}
  - {commitment: "Invest to create capacity for the next phase of growth", implied_date: "next phase (undated)", ref: "slide 18, L550-551", status_word: "underway"}
  - {commitment: "Maximize ERP use; scalable in-house IT infrastructure", implied_date: "undated", ref: "slide 21, L612-616", status_word: "intended"}
  - {commitment: "Increase corporate-customer reach / fulfilment speed", implied_date: "undated", ref: "slide 21, L603-615", status_word: "intended"}
gate_a3: pass
blank_checks: []
```
