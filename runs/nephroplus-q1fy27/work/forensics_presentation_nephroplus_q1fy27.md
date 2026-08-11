# A3 FORENSIC NOTES — NephroPlus (Nephrocare Health Services Limited) — Q1 FY27 — Investor Presentation

Source extract: `extract_presentation_nephroplus_q1fy27.txt` (46 slides, 341 disclosure units; OCR pages 7,15,28,40; unit convention Rs Crores x1)
A2 ledger: `ledger_presentation_nephroplus_q1fy27.md` (gate_a2: pass)
Ledger reconciliation: 100% — every A2 ledger row (DU001-DU428, 341 dedup units, plus Tables 3-6) read at its cited slide/line in the A1 extract before judging. Flag-bearing rows (ZERO_STANDING, NEW_LINE_ITEM, CAPITAL_STRUCTURE_CHANGE, KSA_MILESTONE, FORWARD_LOOKING, DATA_AMBIGUOUS, CROSS_CHECK, ORPHAN_FOOTNOTE) read verbatim: slides 3, 8, 9, 12, 13, 14, 16, 19, 20, 21, 32, 33, 38, 39, 42, 43, 44.

Doctype rule applied: statutory-apparatus checks (standalone vs consolidated, shell detection, auditor Other Matters, going-concern EoM, OCI/actuarial, segment assets/liabilities, board outcome, consolidation-list diff, concall silence audit) are N.A. for a slide deck — marked N.A. with a one-line reason. High-value presentation checks (F1 zero-standing, F6 forward commitments, F7 hedges, F8 tax, F10 capital structure, F14 drafting, F16 dropped/reframed) run in full.

---

## HEADLINE: KSA STATUS (the thesis-critical metric) — reported explicitly

Verbatim, slide 21, lines 672-673:
> "Saudi Arabia: Home Dialysis Treatments Commenced; Medical Operator License Obtained, MoH Tender RFI Submitted"

Slide 21, lines 683-684:
> "A 51:49 JV established with publicly listed Arabian International Healthcare Holding Company (Tibbiyah)"

Slide 32, line 1065: KSA "No of Clinics* 1" (*as on 30 June 2026); launch year 2023 (line 1061).

Status decode for A4: three of the three gating milestones the Notion thesis was waiting on have moved. License = **Obtained** (was "expected shortly" at Q4 FY26). Home-dialysis first activity = **Commenced** (first-revenue signal, but NOT quantified — no KSA revenue rupee figure anywhere in the deck). Government tender = **Submitted** RFI, outcome still **pending** (FORWARD-SIGNAL, unresolved). KSA is equity-accounted, not consolidated: the P&L carries KSA/JV as "Share of Profit/(Loss) of Associate (3.6)" in Q1FY27 (line 339), added back to reach "Adjusted PAT". So KSA today is a margin **drag** of Rs 3.6 Cr/quarter pre-scale, masked by the adjusted-PAT presentation. See findings A1, A3, A4, A14.

---

## FINDINGS TABLE

| id | check | ledger row | slide/line | verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A1 | F1 | DU058 / DU068 | s9 L333, L339 | "Add: Expenses related to Saudi Operations 0.0 0.0 0.0" and "Share of Profit / (Loss) of Associate -3.6 0.0 -3.1" | FORWARD-SIGNAL | KSA now flows through the equity-method associate line as a (3.6) Cr/qtr loss; the EBITDA-level Saudi add-back stays 0.0 because KSA costs sit below the line. Pre-scale JV drag will persist/grow until KSA breaks even. |
| A2 | F1 | DU069 | s9 L344 | "Add: Impact on Finance cost on account of CCPS conversion 0.0 0.0 0.0" | CONFIRMATORY-NEGATIVE | Standing add-back line kept at nil; CCPS already converted (BS "Instruments entirely equity in nature" 3.7 -> nil, line 1474). Template anticipates the item; it is spent, not future. |
| A3 | F6 | DU178-180 (Table 6 KSA) | s21 L672-673 | "Home Dialysis Treatments Commenced; Medical Operator License Obtained, MoH Tender RFI Submitted" | FORWARD-SIGNAL | THE thesis metric. License Obtained + Home Dialysis Commenced = 2 of 3 KSA milestones fired since Q4 FY26 ("expected shortly"). First revenue signalled but not quantified. |
| A4 | F6 | DU180 (G6) | s21 L673 | "MoH Tender RFI Submitted" | FORWARD-SIGNAL | Government tender outcome pending — the biggest KSA volume lever and unresolved. A4 question: expected RFI decision date and tender size. |
| A5 | F6 | DU113 (G3) | s13 L487-488 | "aggregated at the Clinic, Cluster, Zone, and Country levels over the next few quarters" | FORWARD-SIGNAL | Dated management commitment (Dialysis Index rollout) — feeds promise-vs-delivery tracker. |
| A6 | F6 | DU103 (G2) | s13 L485-488 | "We will continue to invest in identifying and understanding new geographies" | FORWARD-SIGNAL | New-country entry intent via acquisition/partnership; capital-deployment signal. |
| A7 | F6 | DU116 (G4) | s13 L470-472 | "the confidence to scale into the higher price-point international markets, while preserving margin discipline" | FORWARD-SIGNAL | International mix-up guidance (KSA price/treatment US$300 vs India US$22, s25). Margin-vs-growth tension flagged by management itself. |
| A8 | F7 | DU103 | s13 L482-483 | "we are also exploring entry into new countries via strategic acquisitions or long-term partnerships" | AMBIGUOUS | Hedge word "exploring" — no committed geography/date. Pre-emptive optionality language; A4 to convert to a question on the pipeline. |
| A9 | F8 | DU066 / DU362 | s9 L341, s42 L1461 | "Tax 9.1 4.8 ... 2.8" (Q1FY27/Q1FY26/Q4FY26) and FY24 "Tax ... (2.0)" | FORWARD-SIGNAL | ETR volatile and sub-statutory: Q1FY27 22.2%, Q4FY26 8.4%, FY24 a net credit (DTA recognition; DTA 34.0 Cr on BS L1483). Convergence toward 25.17% statutory = future PAT headwind not visible in the "adjusted" cascade. |
| A10 | F10 | DU387-388 | s43 L1473-1474 | "Equity Share capital 20.1 1.8 1.7" and "Instruments entirely equity in nature - 3.7 3.4" | FORWARD-SIGNAL | Capital structure reset: paid-up 1.8 -> 20.1 and CCPS ("instruments entirely equity in nature") 3.7 -> nil; total equity 584.1 -> 1,116.5. Consistent with recent IPO fresh issue + CCPS conversion. Non-current borrowings fully repaid 96.0 -> 0.0 (L1477). Newly listed (Reg 30 cover letter, BSE 544647). |
| A11 | F14 | DU269 / F25 | s31 L1044, s39 L1385 | "CIS: Commonwealth of Independent States." (footnote with no CIS reference on the slide); duplicate CKD footnote block on s31 | AMBIGUOUS | Orphan footnotes = remnants of dropped bullets between deck versions. CIS orphan hints at a removed CIS/Central-Asia-market line. Cumulatively a drafting/governance data point. |
| A12 | F16 | DU273 | s32 L1056-1066 | "Share of International Revenues ... 12% 24% 32% 42% FY23 FY24 FY25 FY26" | AMBIGUOUS | Trend chart stops at FY26 42% and does NOT restate the Q1FY27 45% figure (which appears only on s12/s16) on the trend line itself. Continuation implied, not plotted — mild framing choice; verify no deceleration. |
| A13 | F1 / NEW_LINE_ITEM | DU064 / DU360 | s9 L339, s42 L1459 | "Share of Profit / (Loss) of Associate -3.6 0.0 -3.1" / "(3.1) - -" | FORWARD-SIGNAL | New line item, live only from FY26/FY27 (nil/dash prior). It is the KSA-JV equity-method loss; scales negatively pre-breakeven. Watch its trajectory as the cleanest KSA P&L tell. |
| A14 | F16 / CROSS_CHECK | DU286 / DU290 | s33 L1098, L1104 | "# of Clinics1 272 200 78" (=550) and "Additions (Q1FY27) 6 18 8" (=32) | AMBIGUOUS | Clinic-type table sums to the GLOBAL 550 total, yet "Examples" row lists India-only states (L1112-1114); Q1FY27 additions 32 vs slide-19 Philippines-only "+7". India-only vs global scope not stated — reconcile before scoring clinic-adds. |
| A15 | F16 (DATA_AMBIGUOUS) | DU262 | s31 L1016-1039 | organized-share chart raw values "15%, 19%, 7%" with axis "2019"/"2029", series "India"/"Global" | NEUTRAL-FACT | Layout-jumbled chart; year-to-series mapping not resolvable from native text. Do not cite the mapping. Enumerator correctly declined to assert it. |
| A16 | CROSS_CHECK vs statutory | DU055/059, DU067/071 | s9 L330,334,342,346 | "Adjusted EBITDA 65.1" vs "EBITDA 63.9"; "Profit After Tax 32.0" vs "Adjusted Profit After Tax 36.8" | NEUTRAL-FACT | Every headline number is non-GAAP: EBITDA/PAT "adjusted" for Saudi + ESOP + notional CCPS. Reported EBITDA 63.9 / PAT 32.0 are the statutory-comparable figures. A4/A5 must cross-check these against the filed Q1FY27 results, not the adjusted cascade. |

---

## CHECKLIST SCORECARD (all 17, one status each)

| # | Check | Status | Basis (one line) |
|---|---|---|---|
| F1 | Zero-value standing line items | FINDING | Saudi add-back 0.0 all periods while KSA "Commenced" (KSA sits in equity-method associate line -3.6); CCPS conversion add-back 0.0 (already converted). A1, A2, A13. |
| F2 | Standalone vs consolidated decomposition | N.A. | Deck carries consolidated figures only; no standalone P&L to decompose. |
| F3 | Shell-entity detection | N.A. | Requires standalone vs consolidated cost lines; not in a presentation. |
| F4 | Unaudited contribution ratio | N.A. | No auditor "Other Matters" paragraph in a slide deck. |
| F5 | Going concern / EoM scope tracking | N.A. | No auditor going-concern/EoM paragraph; statutory apparatus absent. |
| F6 | Forward-commitment phrase mining | FINDING | KSA "Commenced/Obtained/Submitted"; Dialysis Index "over the next few quarters"; "will continue to invest"; "scale into higher price-point markets". A3-A7. See Commitment Register. |
| F7 | Hedge phrase mining | FINDING | "exploring entry into new countries" (s13 L482); "subject to renewal" (s33 tenor); disclaimer "subject to known and unknown risks". A8. |
| F8 | Tax forensics | FINDING | ETR Q1FY27 22.2% / Q4FY26 8.4% / FY24 net credit (2.0); DTA 34.0 Cr; convergence-to-25.17% headwind. A9. |
| F9 | OCI forensics | N.A. | No OCI / actuarial statement in the deck. |
| F10 | Share count and dilution | FINDING | Paid-up 1.8 -> 20.1; CCPS 3.7 -> nil; equity 584 -> 1,116; recent IPO + conversion. No EPS disclosed. A10. |
| F11 | Reserves and net worth tie-out | PASS | Total Equity 1,116.5 = share cap 20.1 + other equity ~1,096.4; assets 1,470.9 = equity+liab 1,470.9 (balances). No third-party net-worth number in deck to reconcile against. |
| F12 | Segment forensics | N.A. | Geographic revenue split only (India/International); no segment assets/liabilities disclosed. |
| F13 | Board outcome beyond results | N.A. | No board-meeting outcome / AGM notice; Reg 30 cover letter transmits the deck only. |
| F14 | Note drafting inconsistencies | FINDING | Orphan CIS footnote (s39 L1385) + duplicate CKD footnote (s31 L1044); "EBIDTA" typo (s8 L310, s14 L517). A11. |
| F15 | Entity list diffs | N.A. | No consolidation/entity list in deck; no prior-quarter deck to diff. |
| F16 | Presentation-specific: dropped/reframed | FINDING | Orphan CIS footnote = dropped market bullet; intl-rev trend chart omits Q1FY27 45%; clinic-type table scope ambiguity; jumbled s31 chart. No prior deck so full dropped-metric diff not evaluable. A12, A14, A15. |
| F17 | Concall silence audit | N.A. | Document is a presentation, not a concall transcript; no Q&A to audit. |

Blank checks: none. GATE A3: pass.

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | ref | status word |
|---|---|---|---|
| KSA Home Dialysis Treatments | Q1 FY27 (now) | s21 L672 | commenced |
| KSA Medical Operator License | achieved | s21 L672-673 | obtained |
| KSA MoH Tender (RFI) | pending decision | s21 L673 | submitted (underway) |
| NephroPlus Dialysis Index — Clinic/Cluster/Zone/Country aggregation | "over the next few quarters" | s13 L487-488 | underway |
| Invest in identifying/understanding new geographies | ongoing/open | s13 L485-488 | initiated |
| Scale into higher price-point international markets, preserving margin discipline | ongoing | s13 L470-472 | underway |
| Explore entry into new countries via acquisitions/partnerships | open (hedged) | s13 L482-483 | exploring |
| Growth Strategy 5 pillars (consolidate India; scale PH/UZ/KSA; new markets; leverage scale; digital) | multi-year | s39 L1352-1379 | initiated |

---

## MONITORING CHECKLIST — every KPI value needed to score (for A4)

| Notion watch-item (G/R band) | Q1 FY27 value | slide/line | score | note |
|---|---|---|---|---|
| Intl revenue mix (G>40% / R<35%) | ~45% intl / 55% India | s12 L435-448; s16 L573-576 | GREEN | FY-trend 12/24/32/42% to FY26 (s32); Q1FY27 45% not restated on trend chart (A12). |
| Pre-tax ROCE (G>20% / R<18%) | 21.04% | s16 L584-586, fn8 L592 | GREEN | Single point; no prior-period ROCE series in deck (trend NOT FOUND). EBIT / avg adj. capital employed, excl. Saudi+ESOP. |
| Clinics added rolling 12m (G+25-40/yr / R<15/yr) | Q1FY27 gross adds: India-type 6/18/8 = 32 (s33); Philippines +7 (s19). FY23-26 clinics acquired 4/12/10/11 (s35) | s33 L1104; s19 L651; s35 L1202-1214 | AMBIGUOUS | Scope of s33 additions (India-only vs global) not stated (A14); rolling-12m net not derivable (no year-ago global count). |
| Implied bed count (+12-15% YoY) | NOT FOUND (network-wide bed count not disclosed; only 165-bed Tashkent, 10-bed mid, 5-bed small formats) | s16, s22 | N/A | Cannot score. A4 concall question. |
| Bed utilisation (toward 70-75%) | NOT FOUND | — | N/A | No utilisation % disclosed. A4 concall question. |
| Treatments/clinic/yr (+8-12% YoY) | Q1FY27 10,31,084 treatments / 550 clinics ≈ 1,875/clinic/qtr (~7,500 annualised) | s8 L306; s45 L1536 | partial | Q1FY26 clinic count not given, so clean YoY not computable. |
| Revenue growth YoY (G>15% / R<12%) | +23.7% (281.8 vs 227.8) | s8 L290 | GREEN | QoQ +6.1% (s14). |
| Adj EBITDA margin (G>22% / R<20%) | 23.1% adj (22.7% reported) | s8 L310; s9 L331,335 | GREEN | +120bps YoY, +220bps QoQ. Reported EBITDA margin 22.7% also >22%. |
| Goodwill % net worth (<15%, was 9.5%) | 86.7 / 1,116.5 = 7.8% (Mar-26) | s43 L1477, L1472 | GREEN | Improved vs prior 9.5%; goodwill rose 55.5 -> 86.7 (acquisitions) but NW rose faster (IPO). |

Additional balance-sheet notes for A4/A5 (presentation gives only annual BS Mar-24/25/26 — NO Q1FY27 balance sheet):
- Net cash (Mar-26): cash 123.9 + bank balances 131.6 + current investments 170.6 = 426.1 Cr gross liquid; borrowings non-current 0.0 + current 23.0 = 23.0; net ~403 Cr excl. leases (s43). This does NOT reconcile with the Notion-memory "net cash Rs 1,533 Cr" at Q4 FY26 (total assets are only 1,470.9 Cr) — treat the 1,533 figure as suspect memory; anchor to the filed balance sheet. A4 to reconcile.
- Receivable days (Mar-26): trade receivables 316.9 / FY26 revenue 998.8 x 365 ≈ 116 days (annual basis). No Q1FY27 receivables in deck.
- Capex: NOT isolated; Net Cash from Investing (410.4) Cr FY26 includes M&A + investment purchases (s44 L1518).
- ETR: see F8/A9.

---

## CLASSIFICATION ROLL-UP
- FORWARD-SIGNAL (flag to A4): A1, A3, A4, A5, A6, A7, A9, A10, A13
- AMBIGUOUS (flag to A4 -> management questions): A8, A11, A12, A14, A15
- CONFIRMATORY-NEGATIVE: A2
- NEUTRAL-FACT: A16

Priority A4 questions seeded: (1) KSA MoH tender expected decision date + size (A4); (2) quantify KSA first revenue and JV loss trajectory/breakeven (A1/A3/A13); (3) reconcile clinic-add scope India vs global (A14); (4) ETR normalisation path to 25.17% and its PAT impact (A9); (5) confirm no CIS/new-market bullet was dropped between decks (A11/A12); (6) network bed count + utilisation disclosure (missing KPIs).

---

```yaml
stage: A3-forensics
company: "nephroplus"
quarter: "q1fy27"
doctype: "presentation"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/nephroplus-q1fy27/work/forensics_presentation_nephroplus_q1fy27.md"
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
  F9: N.A.
  F10: FINDING
  F11: PASS
  F12: N.A.
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: N.A.
findings:
  - {id: "A1", check: "F1", line: "s9 L333/L339", classification: "FORWARD-SIGNAL", implication: "KSA runs through equity-method associate line as (3.6)Cr/qtr loss; EBITDA Saudi add-back stays 0.0; pre-scale drag persists"}
  - {id: "A2", check: "F1", line: "s9 L344", classification: "CONFIRMATORY-NEGATIVE", implication: "CCPS conversion add-back nil; conversion already complete (instruments->nil), item is spent not future"}
  - {id: "A3", check: "F6", line: "s21 L672-673", classification: "FORWARD-SIGNAL", implication: "KSA license Obtained + home dialysis Commenced = 2 of 3 milestones fired; first revenue signalled but not quantified"}
  - {id: "A4", check: "F6", line: "s21 L673", classification: "FORWARD-SIGNAL", implication: "MoH tender RFI submitted, outcome pending — biggest KSA volume lever unresolved"}
  - {id: "A5", check: "F6", line: "s13 L487-488", classification: "FORWARD-SIGNAL", implication: "Dialysis Index rollout dated 'over the next few quarters' — promise-vs-delivery item"}
  - {id: "A6", check: "F6", line: "s13 L485-488", classification: "FORWARD-SIGNAL", implication: "New-geography entry intent via acquisition/partnership — capital deployment signal"}
  - {id: "A7", check: "F6", line: "s13 L470-472", classification: "FORWARD-SIGNAL", implication: "Guidance to scale higher-price intl markets while preserving margin; growth-vs-margin tension"}
  - {id: "A8", check: "F7", line: "s13 L482-483", classification: "AMBIGUOUS", implication: "Hedge 'exploring' new countries; no committed geography/date — A4 pipeline question"}
  - {id: "A9", check: "F8", line: "s9 L341 / s42 L1461", classification: "FORWARD-SIGNAL", implication: "ETR volatile sub-statutory (Q1 22.2%, Q4FY26 8.4%, FY24 credit); DTA 34Cr; convergence to 25.17% = PAT headwind"}
  - {id: "A10", check: "F10", line: "s43 L1473-1474", classification: "FORWARD-SIGNAL", implication: "Capital reset: paid-up 1.8->20.1, CCPS 3.7->nil, equity 584->1116, NCL borrowings->0; recent IPO+conversion"}
  - {id: "A11", check: "F14", line: "s39 L1385 / s31 L1044", classification: "AMBIGUOUS", implication: "Orphan CIS + duplicate CKD footnotes = dropped bullets between deck versions; drafting/governance data point"}
  - {id: "A12", check: "F16", line: "s32 L1056-1066", classification: "AMBIGUOUS", implication: "Intl-rev trend chart ends FY26 42%, omits Q1FY27 45%; continuation implied not plotted — verify no deceleration"}
  - {id: "A13", check: "F1", line: "s9 L339 / s42 L1459", classification: "FORWARD-SIGNAL", implication: "New associate line = KSA JV equity-method loss; scales negatively pre-breakeven; cleanest KSA P&L tell"}
  - {id: "A14", check: "F16", line: "s33 L1098/L1104", classification: "AMBIGUOUS", implication: "Clinic-type table sums to global 550 but examples India-only; adds 32 vs s19 PH +7; scope not stated"}
  - {id: "A15", check: "F16", line: "s31 L1016-1039", classification: "NEUTRAL-FACT", implication: "Layout-jumbled organized-share chart; year-to-series mapping unresolvable, do not cite"}
  - {id: "A16", check: "CROSS_CHECK", line: "s9 L330/334/342/346", classification: "NEUTRAL-FACT", implication: "Headline EBITDA/PAT non-GAAP (adj. Saudi+ESOP+CCPS); reported EBITDA 63.9/PAT 32.0 to cross-check vs filed results"}
forward_signals: ["A1","A3","A4","A5","A6","A7","A9","A10","A13"]
ambiguous: ["A8","A11","A12","A14","A15"]
commitments:
  - {commitment: "KSA Home Dialysis Treatments", implied_date: "Q1FY27", ref: "s21 L672", status_word: "commenced"}
  - {commitment: "KSA Medical Operator License", implied_date: "achieved", ref: "s21 L672-673", status_word: "obtained"}
  - {commitment: "KSA MoH Tender RFI", implied_date: "pending", ref: "s21 L673", status_word: "submitted"}
  - {commitment: "Dialysis Index Clinic/Cluster/Zone/Country aggregation", implied_date: "next few quarters", ref: "s13 L487-488", status_word: "underway"}
  - {commitment: "Invest in identifying new geographies", implied_date: "open", ref: "s13 L485-488", status_word: "initiated"}
  - {commitment: "Scale into higher price-point intl markets, preserving margin", implied_date: "ongoing", ref: "s13 L470-472", status_word: "underway"}
  - {commitment: "Explore entry into new countries via acquisitions/partnerships", implied_date: "open", ref: "s13 L482-483", status_word: "exploring"}
  - {commitment: "Growth Strategy 5 pillars", implied_date: "multi-year", ref: "s39 L1352-1379", status_word: "initiated"}
gate_a3: pass
blank_checks: []
```
