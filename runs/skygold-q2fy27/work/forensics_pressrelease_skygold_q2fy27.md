# FORENSICS pressrelease SKYGOLD q2fy27 (A3)

Company: Sky Gold & Diamonds Ltd (SKYGOLD) | Quarter: Q2 FY27 | Doctype: pressrelease (3 pages)
Inputs: extracted/skygold-pressrelease-q2fy27-structured.md (R001-R180), extracted/skygold-pressrelease-q2fy27-fulltext.md (146 lines), work/ledger_pressrelease_skygold_q2fy27.md
Prior-quarter fulltext: none available. Notion page / companies/SKYGOLD.md: none (PRE-THESIS READ; operator standing watch list used for F17).
Units: Rs crore. Model: claude-opus-5-5.

## LEDGER RECONCILIATION
- Ledger accounts for 180 of 180 structured IDs (R001-R180, contiguous, no orphans). All 180 rows read at their cited fulltext line. Line cites spot-matched on every block (R004 l.26, R014 l.37, R019 l.50, R038-R125 l.80-100, R126 l.102, R156-R159 l.127-128, R160-R161 l.131-132, R162 l.136, R180 l.146). ledger_reconciled_pct = 100.
- A2 flags carried: FOOTNOTE_UNRESOLVED (R156-R159, R169-R170) -> P-A3-06; ENTITY_CHANGE (R172-R173) -> P-A3-08, P-A3-09; RESTATED rows (R014-R018, R127-R155, R162) tie to table cells, no conflict beyond rounding (4,403.45 headline vs 4,403.5 table).
- A2 ledger note on R110-R117 ("Op PAT H1 234.5 vs reported 234.3") did not catch that H1 Operational PAT fails to sum Q1 + Q2. A3 adds P-A3-04.

## ARITHMETIC RE-TIE (table, line 80-100)
All Q2 / Q1 / H1 sums and growth rates tie within 0.1 ppt rounding (Revenue 2,390.7 + 2,012.8 = 4,403.5; EBITDA 189.8 + 156.7 = 346.5; Reported PBT 166.0 + 134.8 = 300.8; Reported PAT 129.4 + 104.9 = 234.3; Operational PBT 173.4 + 134.8 = 308.2). Exceptions:
- Operational PAT H1: 138.56 + 104.9 = 243.46, printed 234.5 (line 98). Printed margin 5.5% and YoY 120.2% fit 243.5, not 234.5 (234.5 / 4,403.5 = 5.3%; 243.5 / 110.6 = +120.2%).
- Operational PAT % QoQ: 5.8% vs 5.2% = ~58 bps, printed "20 bps" (line 100), same figure as the PAT Margin QoQ cell (line 92).
- Immaterial rounding: EBITDA margin QoQ 14 bps printed vs 15 bps computed; Reported PAT Q2 YoY 93.2% printed vs 93.1%; H1 PBT YoY 105.0% vs 104.9%; H1 PAT YoY 111.9% vs 111.8%. Consistent with unrounded source figures; not findings.

Derived tax (Reported PBT less Reported PAT): Q2 FY27 36.6 (ETR 22.0%); Q2 FY26 20.9 (23.8%); Q1 FY27 29.9 (22.2%); H1 FY27 66.5 (22.1%); H1 FY26 36.2 (24.7%).
Operational adjustment (Operational less Reported): PBT Q2 FY27 +7.4, all other columns 0.0; PAT Q2 FY27 +9.16, all other columns 0.0.

## FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| P-A3-01 | F8 | R062-R069, R078-R085 | 86, 90 | "Reported PBT 166.0 87.9" / "Reported PAT 129.4 67.0" | AMBIGUOUS | ETR 22.0% Q2 FY27 vs 23.8% Q2 FY26; H1 22.1% vs 24.7%; every period below statutory 25.17%. H1 shield vs statutory ~9.2 Cr (~306 bps of PBT, ~3.9% of H1 PAT). At H1 FY26's ETR, H1 PAT growth is ~105% not 111.9%: ~7 ppt of the headline is tax. Deferred-tax split NOT FOUND in release. Ask source of sub-statutory rate (DTA credit, exempt income, lower-tax subsidiary) and whether it persists. Lean bear: ETR step-up risk. |
| P-A3-02 | F16 | R094-R109, R126 | 94, 102 | "Operational PBT 173.4 87.9" / "reported PBT / PAT less non operational income (part of other income in financials)" | AMBIGUOUS | Operational exceeds Reported by 7.4 (PBT) in Q2 FY27 only; zero gap in Q2 FY26, Q1 FY27, H1 FY26. Under the stated definition, non-operational income in Q2 was a LOSS of ~7.4 sitting inside other income. The adjusted metric appears in the one quarter it flatters (Op PAT QoQ +32.1% vs reported +23.4%). If the item is a gold hedge or gold metal loan mark-to-market while gold inventory gains stay in EBITDA, classification is one-sided. Ask: nature of the 7.4 Cr item, and why other income carried no non-op component in prior periods. |
| P-A3-03 | F14 | R078, R110, R094, R062 | 98, 94 | "Operational PAT 138.56 67.0" | AMBIGUOUS | PAT add-back 9.16 exceeds PBT add-back 7.4. A pre-tax loss add-back should shrink after tax (~5.5 at 25.17%), not grow. Implied operational ETR 20.1% (34.84 / 173.4) vs reported 22.0% (36.6 / 166.0). Either the non-op item carried a tax charge, or Op PAT is mis-computed. Ask for the bridge reported PAT -> Op PAT with tax effect. |
| P-A3-04 | F14 | R115, R123, R117 | 98 | "Operational PAT 138.56 ... 234.5 110.6 120.2%" | NEUTRAL-FACT | H1 Op PAT printed 234.5; Q1 + Q2 = 243.46; printed 5.5% margin and 120.2% YoY both fit 243.5. Digit transposition in the headline table. Individually immaterial; cumulative governance data point (drafting care on investor-facing numbers). |
| P-A3-05 | F14 | R122 | 100 | "Operational PAT % 5.8% 4.5% 129 bps 5.2% 20 bps" | NEUTRAL-FACT | QoQ change printed 20 bps; 5.8% less 5.2% is ~58 bps. The 20 bps duplicates the PAT Margin QoQ cell (line 92). Second table error in the same block. |
| P-A3-06 | F14 | R156-R159, R169-R170 (FOOTNOTE_UNRESOLVED) | 127-128 | "₹136.7 crore, compared with (₹100.9) crore in H1 FY27" | AMBIGUOUS | Comparison period carries the current-period label; presumably H1 FY26 (NOT FOUND as printed). If so, CFO swung ~237.6 Cr from negative to positive. No cash-flow statement, debt or working-capital figure in the release, so the turn is unverifiable here. In gold jewellery, CFO depends on gold metal loan classification and inventory funding. Ask: correct period label, driver of the turn (inventory, receivables, metal loan, customer advances), and whether H2 holds it. |
| P-A3-07 | F6 | R158-R159, R170-R171 | 128 | "CFO/EBITDA was 39% for H1 FY27 vs earlier guidance of 20%" | FORWARD-SIGNAL | Only forward-type item in the release. Prior guidance of 20% CFO/EBITDA cited as beaten (136.7 / 346.5 = 39.5%). Guidance horizon (FY27? H1?) NOT FOUND. No new or revised guidance issued for H2 / FY27 on revenue, margin or CFO. Feeds Role 5 promise-vs-delivery: track whether management raises the 20% or re-anchors to it. |
| P-A3-08 | F13 | R160-R161, R167, R172-R174 (ENTITY_CHANGE) | 130-132 | "On October 7, 2026, the Board approved completion of acquisition of 100% stake in Purvi Gems & Jewellery (India) Private Limited for total cash consideration of ₹9 crore." | FORWARD-SIGNAL | Board outcome beyond results, post period end. Small in money (9 Cr vs H1 PAT 234.3 Cr) but directional: company renamed from "Sky Gold Limited" (line 50) and describes itself as "studded jewellery" maker (line 137). Purvi's revenue, net worth, product line and goodwill NOT FOUND. Ask: what capability Purvi adds (diamonds / studded), its P&L, and whether more bolt-ons are planned. |
| P-A3-09 | F15 | R172 (ENTITY_CHANGE) | 130 | "Purvi Gems & Jewellery (India) Private Limited" | NEUTRAL-FACT | New 100% subsidiary from 7-Oct-2026; outside the Q2 FY27 perimeter, inside Q3 FY27. Q3 consolidated vs standalone comparability shifts. No prior-quarter entity list available to diff further. |
| P-A3-10 | F17 | R038-R045, R054-R061, R156 (watch-list cross-reference) | 80, 84, 127 | "Revenue 2390.7 1,484.5 61.0%" / "EBITDA Margin (%) 7.94% 6.7% 121 bps" | AMBIGUOUS | Release is silent on 7 of 8 operator watch items and partial on 1 (table below). Revenue +61.0% YoY and EBITDA margin +121 bps with no volume or gold-price split: making-charge expansion cannot be separated from inventory gains on gold price. Release dated 27-Oct-2026 is silent on the QIP of up to Rs 1,800 Cr approved the same day (operator checklist), while its only cash bullet stresses CFO beat. Ask on the 31-Oct-2026 call: why a 39% CFO/EBITDA business needs fresh equity of ~7.7x H1 PAT. |

## WHAT WAS NOT DISCUSSED (F17, operator standing watch list vs release; transcript not yet available, call 31-Oct-2026)

| # | watch item | addressed in release? | ref | consecutive quarters of silence |
|---|---|---|---|---|
| 1 | Volume processed (kg / tonnes) | No | - | 1 (first observed; no prior release) |
| 2 | Revenue growth split, gold price vs volume | No (total revenue +61.0% Q2, +68.3% H1 only) | line 80 | 1 |
| 3 | Gross margin per gram or % | No (EBITDA margin only) | line 84 | 1 |
| 4 | Working-capital days, inventory, receivables | Partial (CFO 136.7 Cr, CFO/EBITDA 39%; no days, no inventory, no receivables) | line 127-128 | 1 |
| 5 | Gold metal loan use and interest cost | No | - | 1 |
| 6 | Customer concentration | No | - | 1 |
| 7 | Net debt | No | - | 1 |
| 8 | Equity raise (QIP up to Rs 1,800 Cr approved 27-Oct-2026; EGM 18-Nov-2026; ESOP grant) | No | - | 1 |

## CHECKLIST SCORECARD

| check | status | basis |
|---|---|---|
| F1 | PASS | A2 ZERO_STANDING count 0; no nil or dash cells in the table. Op rows equal to reported in prior columns are handled at F16. |
| F2 | N.A. | Release carries consolidated only (line 72, 75); standalone not disclosed. |
| F3 | N.A. | No standalone cost lines in a press release. |
| F4 | N.A. | No auditor report or Other Matters paragraph. |
| F5 | N.A. | No EoM / going-concern language; no prior-quarter fulltext. |
| F6 | FINDING | P-A3-07 (guidance reference); register also carries Purvi completion (P-A3-08). |
| F7 | PASS | Hedge lexicon searched across all 146 lines; no hit. No safe-harbour disclaimer either. |
| F8 | FINDING | P-A3-01 (ETR below 25.17% every period, falling YoY). |
| F9 | N.A. | No OCI data in release. |
| F10 | N.A. | No EPS, share count or paid-up capital in release; QIP / ESOP silence carried at F17. |
| F11 | N.A. | No net worth or reserves figure in release. |
| F12 | N.A. | No segment data in release. |
| F13 | FINDING | P-A3-08 (Board approval of Purvi completion, 7-Oct-2026). |
| F14 | FINDING | P-A3-03, P-A3-04, P-A3-05, P-A3-06 (four drafting / arithmetic inconsistencies in a 3-page release). |
| F15 | FINDING | P-A3-09 (new subsidiary Purvi, Q3 perimeter). |
| F16 | FINDING | P-A3-02 (Operational metric diverges from reported only in current quarter). Dropped-metric diff vs prior release not possible: none available. |
| F17 | FINDING | P-A3-10 (silence on 7 of 8 watch items, partial on 1; transcript pending 31-Oct-2026). |

## COMMITMENT REGISTER (F6)

| commitment | implied date | ref | status word |
|---|---|---|---|
| Acquisition of 100% of Purvi Gems & Jewellery (India) Pvt Ltd for Rs 9 Cr cash | 7-Oct-2026 (Board approved completion) | line 130-132, R167/R172-R174 | completed |
| CFO/EBITDA guidance of 20% (prior guidance; H1 FY27 delivered 39%) | horizon NOT FOUND | line 128, R159/R171 | underway |

## FINDING COUNT BY CLASS
FORWARD-SIGNAL 2 (P-A3-07, P-A3-08) | AMBIGUOUS 5 (P-A3-01, P-A3-02, P-A3-03, P-A3-06, P-A3-10) | CONFIRMATORY-NEGATIVE 0 | NEUTRAL-FACT 3 (P-A3-04, P-A3-05, P-A3-09) | total 10. All FORWARD-SIGNAL and AMBIGUOUS findings flagged for A4.

```yaml
stage: A3-forensics
company: "SKYGOLD"
quarter: "q2fy27"
doctype: "pressrelease"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/skygold-q2fy27/work/forensics_pressrelease_skygold_q2fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: PASS
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: PASS
  F8: FINDING
  F9: N.A.
  F10: N.A.
  F11: N.A.
  F12: N.A.
  F13: FINDING
  F14: FINDING
  F15: FINDING
  F16: FINDING
  F17: FINDING
findings:
  - {id: "P-A3-01", check: "F8", line: "86, 90", classification: "AMBIGUOUS", implication: "ETR 22.0% Q2 FY27 vs 23.8% Q2 FY26, H1 22.1% vs 24.7%, all below 25.17%; ~9.2 Cr H1 shield; ~7 ppt of 111.9% H1 PAT growth is tax; ETR step-up risk, source NOT FOUND"}
  - {id: "P-A3-02", check: "F16", line: "94, 102", classification: "AMBIGUOUS", implication: "Operational PBT 173.4 > reported 166.0 only in Q2 FY27 despite 'less non operational income' definition; implies ~7.4 Cr non-op loss in other income; possible one-sided gold hedge / metal-loan MTM exclusion"}
  - {id: "P-A3-03", check: "F14", line: "98, 94", classification: "AMBIGUOUS", implication: "Op PAT add-back 9.16 exceeds Op PBT add-back 7.4; implied op ETR 20.1% vs reported 22.0%; tax bridge needed"}
  - {id: "P-A3-04", check: "F14", line: "98", classification: "NEUTRAL-FACT", implication: "H1 Op PAT printed 234.5 vs Q1+Q2 243.46; margin 5.5% and YoY 120.2% fit 243.5; transposition"}
  - {id: "P-A3-05", check: "F14", line: "100", classification: "NEUTRAL-FACT", implication: "Op PAT % QoQ printed 20 bps vs ~58 bps computed; copied from PAT margin row"}
  - {id: "P-A3-06", check: "F14", line: "127-128", classification: "AMBIGUOUS", implication: "CFO comparison (100.9) labelled H1 FY27, same as current; if H1 FY26, swing ~237.6 Cr; no CF statement, WC or debt in release to verify"}
  - {id: "P-A3-07", check: "F6", line: "128", classification: "FORWARD-SIGNAL", implication: "CFO/EBITDA 39% vs earlier 20% guidance; horizon NOT FOUND; no new guidance for H2 or FY27"}
  - {id: "P-A3-08", check: "F13", line: "130-132", classification: "FORWARD-SIGNAL", implication: "Board approved completion of 100% Purvi Gems acquisition for 9 Cr cash on 7-Oct-2026; with rename (line 50) and studded positioning (line 137) signals diamond / studded build; Purvi financials NOT FOUND"}
  - {id: "P-A3-09", check: "F15", line: "130", classification: "NEUTRAL-FACT", implication: "New 100% subsidiary enters Q3 FY27 consolidation perimeter"}
  - {id: "P-A3-10", check: "F17", line: "80, 84, 127", classification: "AMBIGUOUS", implication: "Silent on 7 of 8 watch items, partial on WC via CFO; no volume / gold-price split behind +61% revenue and +121 bps margin; silent on QIP up to 1,800 Cr approved same day"}
forward_signals: ["P-A3-07", "P-A3-08"]
ambiguous: ["P-A3-01", "P-A3-02", "P-A3-03", "P-A3-06", "P-A3-10"]
commitments:
  - {commitment: "Acquire 100% of Purvi Gems & Jewellery (India) Pvt Ltd for Rs 9 Cr cash", implied_date: "2026-10-07", ref: "line 130-132 (R167, R172-R174)", status_word: "completed"}
  - {commitment: "CFO/EBITDA guidance 20% (H1 FY27 delivered 39%)", implied_date: "NOT FOUND", ref: "line 128 (R159, R171)", status_word: "underway"}
gate_a3: pass
blank_checks: []
analyst_note: "Three items carry the read. (1) Operational rows exceed reported only in Q2 FY27 (PBT +7.4, PAT +9.16), though the note defines them as reported less non-operational income. A non-operational loss sat in other income this quarter. If it is a gold hedge or metal-loan mark-to-market while gold inventory gains stay in EBITDA, the classification is one-sided. A PAT add-back larger than the PBT add-back has no clean tax explanation. (2) ETR sits about 300 bps under 25.17% and fell YoY; about 7 ppt of the 111.9% headline PAT growth is tax, not operations. (3) H1 EBITDA margin rose 132 bps while revenue rose 68%. With no volume or gold-price split, making-charge gains cannot be separated from inventory gains on a rising gold price. The CFO turn (136.7 vs a mislabelled (100.9)) is the bull data point. Yet a QIP of up to Rs 1,800 Cr, about 7.7x H1 PAT, was approved the same day and the release omits it. Ask why a 39% CFO/EBITDA business needs that equity. H1 Operational PAT 234.5 is almost certainly 243.5."
```
