# A3 FORENSIC NOTES — Gem Aromatics Limited (GEMAROMA) — Q1FY27 — doctype: PRESENTATION

Source extract: `extract_presentation_gemaroma_q1fy27.txt` (33 PDF pages).
Reconciliation contract: `ledger_presentation_gemaroma_q1fy27.md`.
Ledger rows read verbatim at cited line: 100% (Sections 1-10; 88 table line items,
95 slide KPIs, 3 charts, 11 guidance, 14 capex/capacity, 17 strategic claims, 13 footnotes).
Prior quarter: NONE (first-time coverage). Notion checklist: NONE (first-coverage silence test).

Doctype note: this is a 33-slide investor deck bundling a Reg-30 covering letter (page 1).
Auditor-report checks (F4 unaudited ratio, F5 EoM), OCI (F9), and board-outcome/entity-diff
checks (F13, F15) have no substrate in a deck and are marked N.A. with reason. F16 (presentation
reframing) applies; F6/F7/F8/F10/F11 run against the numbers the deck carries; F17 is run as a
first-coverage silence audit per task instruction.

---

## FINDINGS TABLE

| id | check | ledger row ref | line / slide | verbatim quote | classification | forward implication |
|----|-------|----------------|--------------|----------------|----------------|---------------------|
| A3-01 | F2 | Ledger 2a #14 / 2b #14 (PAT) | p9 L317; p10 L360 | Standalone PAT "7.3"; Consolidated PAT "-7.9" | FORWARD-SIGNAL | Entire consolidated loss is the subsidiary (Krystal/Dahej). S-vs-C PAT gap swung from +1.5 Cr (Q1FY26) to -15.2 Cr (Q1FY27), a 16.7 Cr / ~229%-of-standalone-PAT swing. Inflection date of the subsidiary is the whole thesis; ask when it turns EBITDA-positive. |
| A3-02 | F6 | Ledger §5 #5-7 | p8 L277-280 | "revenue contribution expected from Q3FY27"; "commercial production targeted in Q3FY27, with revenue contribution expected from Q4FY27" | FORWARD-SIGNAL | Dated promise-vs-delivery ladder (Safranal end-Q2FY27; Cooling Agents Q3FY27; Phenol trial end-Q2FY27 / commercial Q3FY27 / revenue Q4FY27). Feeds Role 5 tracker; each is verifiable next 1-3 quarters. |
| A3-03 | F7 | Ledger §5 #3 | p8 L262-263 | "as capacity utilization improves and the contribution from higher-value products increases, we expect margins to gradually improve" | AMBIGUOUS | Margin-recovery language is undated and doubly conditional against a -1361 bps consolidated EBITDA-margin move. Pre-emptive hedge; convert to a "what utilisation % and by when" question. |
| A3-04 | F8 | Ledger §5 #11 / §6 #5 | p22 L760 | "15% Corporate Tax Rate under Government Incentives till perpetuity" | FORWARD-SIGNAL | Unusually strong, uncited forward tax claim (no scheme named, no sunset). Consolidated Q1FY27 tax is a credit (-0.7 on -8.5 PBT) and FY26 annual ETR is anomalous (4.9/6.4 = ~77%). Future ETR path and the perpetuity basis both need sourcing. |
| A3-05 | F12 | Ledger §3 #56 / §3 #22 | p16 L542; p7 L243 | "Rs 5 Cr Revenue ~1% of Total Revenue" (Phenol) vs "~Rs 265 Cr Dahej capex" | FORWARD-SIGNAL | Segment asset/liability data is absent, but the Dahej build (Rs 265 Cr capitalised, Rs 9.1 Cr/qtr depreciation) vastly outpaces the new-segment revenue it was built for (Phenol Rs 5 Cr, Cooling Agents pre-revenue). Classic pre-commissioning / equity-funded build; utilisation ramp is the future funding and margin risk. |
| A3-06 | F14 | Ledger §3 #16 / §8 #10 | p7 L238 vs p10 L348; p23 L816-817 | comparator "16.9%" (tile) vs table "17.0%"; RoW note lists "Uganda ... and Switzerland" | NEUTRAL-FACT | Two internal inconsistencies: Q1FY26 consolidated EBITDA-margin comparator differs by 0.1 pt between tile and table; RoW footnote names Uganda and Switzerland absent from the same slide's map. Individually immaterial, cumulatively a drafting-discipline data point. |
| A3-07 | F16 | Ledger §3 #17-20 / Chart 1 | p7 L220-221, L235-236, L250 | Standalone leads with "Rs 7.3 Cr / 11% YoY" (green up); Consolidated "Rs (7.9) Cr / 199% YoY" and "Cash PAT Rs 1.3 Cr" | AMBIGUOUS | Dashboard reframes a consolidated net loss favourably: standalone positives shown first with green arrows; the sign-flip loss is expressed as "199% YoY"; positive "Cash PAT Rs 1.3 Cr" is placed beside the -7.9 Cr PAT to soften it. YoY growth rounded up ("9%" vs 8.6% table L291; "13%" vs 12.8% L334) while declines shown to the decimal. Baseline to diff Q2FY27 framing against. |
| A3-08 | F17 | Ledger §6 #13-14 (DATA_ABSENT) | §6 L361-362 | "no capacity figure in any unit is disclosed"; "no order-book Rs figure ... disclosed" | CONFIRMATORY-NEGATIVE | First-coverage silence audit: deck omits installed capacity (TPA) for every facility, order book/backlog, capacity-utilisation %, the debt/accruals split of the Rs 270 Cr capex, segment profitability, and any Jun-26 balance sheet / net-debt (only Mar-26 shown). Silences cluster on exactly the metrics a loss-and-heavy-capex quarter would want to duck. |

---

## CHECKLIST SCORECARD (all 17; one status each)

| Check | Status | One-line basis |
|-------|--------|----------------|
| F1 ZERO-STANDING line items | PASS | Ledger `ZERO_STANDING` count = 0; all 88 table cells across 5 tables carry real values (incl. genuine negatives), no nil/dash template rows (ledger §2 L85-89). |
| F2 Standalone vs Consolidated | **FINDING** (A3-01) | S PAT +7.3 vs C PAT -7.9; gap swung +1.5→-15.2 Cr YoY (~229% of standalone PAT), well past the 5 pp threshold. Consolidated loss = subsidiary (Rev gap +15.9, EBITDA gap -5.2, Dep gap +7.5 Cr). |
| F3 Shell-entity detection | PASS | S-vs-C cost lines show subsidiaries operate: COGS gap 14.0, Employee gap 4.0, Depreciation gap 7.5 Cr (p10 L336/342/354). Loss-making but real operations, not shells; no Going Concern EoM in a deck. |
| F4 Unaudited contribution ratio | N.A. | Investor deck carries no auditor "Other Matters" paragraph; component-auditor split not disclosed. |
| F5 Going concern / EoM scope | N.A. | No auditor report / EoM in a presentation; no prior quarter to verbatim-diff. |
| F6 Forward-commitment mining | **FINDING** (A3-02) | Dated commitments: Safranal end-Q2FY27, Cooling Agents Q3FY27, Phenol trial end-Q2FY27 / commercial Q3FY27 / revenue Q4FY27 (p8 L277-280); Brazil WOS "approved" (p8 L272). See Commitment Register. |
| F7 Hedge-phrase mining | **FINDING** (A3-03) | Undated, doubly-conditional "we expect margins to gradually improve" (p8 L263) against a -1361 bps consolidated EBITDA-margin move; pre-emptive cover. |
| F8 Tax forensics | **FINDING** (A3-04) | Standalone ETR ~25.8% (near statutory); consolidated tax is a credit on the loss; FY26 annual ETR ~77% (4.9/6.4); "15% ... till perpetuity" forward claim uncited (p22 L760). |
| F9 OCI forensics | N.A. | No OCI / actuarial statement in the deck. |
| F10 Share count & dilution | PASS | Share capital 1.8→9.4→9.4→10.4 (p28 L952); Mar-26 10.4 / FV 2.0 = 5.2 Cr shares, ties to p32 L1064. Changes trace to pre-IPO bonus (FY24) and Aug'25 IPO; EPS restated on ~4.69 Cr base (FY23 9.53 on PAT 44.7). No diluted-EPS spread disclosed to test. |
| F11 Reserves / net worth tie-out | PASS | Shareholders' Funds Mar-26 449.9 = Share Capital 10.4 + Reserves 439.5 (p28 L952-957), exact. Market cap 914.15 Cr (p32 L1060) ≈ CMP 174.90 × ~5.2 Cr; P/B ~2.0, no reconciling gap. |
| F12 Segment forensics | **FINDING** (A3-05) | Segment assets/liabilities DATA_ABSENT, but Dahej build (Rs 265 Cr capex, Rs 9.1 Cr/qtr dep) dwarfs the new-segment revenue it funds (Phenol Rs 5 Cr; Cooling Agents pre-revenue) = pre-commissioning build. |
| F13 Board outcome beyond results | N.A. | No Board's Report / AGM notice / AR approval / director term dates in an investor deck; Brazil WOS approval captured under F6. |
| F14 Note-drafting inconsistencies | **FINDING** (A3-06) | Tile 16.9% vs table 17.0% comparator (p7 L238 / p10 L348); RoW note lists Uganda + Switzerland absent from the map (p23 L816-817). |
| F15 Entity-list diffs | N.A. | No formal consolidation entity schedule in the deck and no prior quarter to diff; new Brazil WOS is a forward approval captured under F6/Commitment Register. |
| F16 Presentation reframing | **FINDING** (A3-07) | Dashboard leads standalone positives, expresses a sign-flip loss as "199% YoY", pairs positive "Cash PAT 1.3" with PAT -7.9, rounds YoY growth up vs table (p7 L220-236, L250). |
| F17 Silence audit (first-coverage) | **FINDING** (A3-08) | Deck silent on installed capacity, order book, utilisation %, capex debt/accruals split, segment profitability, Jun-26 balance sheet / net debt (ledger §6 L361-362; DATA_ABSENT ×2). |

Blank checks: none. GATE A3: pass.

---

## COMMITMENT REGISTER (from F6 / F2 / F8)

| commitment | implied date | ref | status word |
|------------|--------------|-----|-------------|
| Cooling Agents (GEM Cool 03/05/23) revenue contribution | Q3FY27 | p8 L277 / p22 L743-744 | initiated (audits completed, initial orders secured) |
| Safranal revenue contribution | end Q2FY27; meaningfully Q3FY27 | p8 L278 / p22 L746 | underway (commercial production commenced 26 Feb'26, p12 L396-400) |
| Phenol Derivatives — trial production | end Q2FY27 | p8 L279 / p22 L748 | initiated (pending) |
| Phenol Derivatives — commercial production | Q3FY27 | p8 L279-280 | targeted |
| Phenol Derivatives — revenue contribution | Q4FY27 | p8 L280 | expected |
| Brazil Wholly-Owned Subsidiary incorporation (LatAm distribution) | approved Jun 2026, incorporation pending | p8 L271-273 / p12 L407-408 | board-approved (not yet incorporated) |
| Consolidated margin "gradually improve" | undated / conditional | p8 L263 | hedged, undated |
| Dahej greenfield capex ~Rs 270 Cr (via internal accruals + debt) | ~Rs 265 Cr already capitalised | p7 L243 / p22 L757 | underway (near-complete, split undisclosed) |
| 15% corporate tax rate under Govt incentives | "till perpetuity" | p22 L760 | claimed (uncited) |

---

## NOTES FOR A4 (question generation)

- FORWARD-SIGNAL findings A3-01, A3-02, A3-04, A3-05 → convert to management questions (subsidiary inflection date; delivery vs the Q2-Q4FY27 ladder; basis and durability of the 15% perpetuity rate; Dahej utilisation ramp and any further funding need).
- AMBIGUOUS findings A3-03, A3-07 → questions on margin-recovery timeline/utilisation target and on the reframed loss disclosure.
- CONFIRMATORY-NEGATIVE A3-08 and NEUTRAL-FACT A3-06 are logged; A3-08 is the first-coverage silence baseline for Q2FY27 to diff against.
- REPEAT_DISCLOSURE (9 instances, ledger §Summary) do not double-count: Dahej capex, Krystal guidance block, customer/country stats, scientist count are each single evidence points.

*ends*
