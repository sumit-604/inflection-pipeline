# A3 FORENSIC NOTES — Venus Pipes & Tubes (VENUSPIPES), Q1 FY27 — doctype: PRESENTATION (4-page press release)

Source extract: `extract_pressrelease_venuspipes_q1fy27.txt` (151 lines, 4 pages)
Ledger: `ledger_pressrelease_venuspipes_q1fy27.md` (76 disclosure units: A4 pages, B21 cells, C8, D12, E3, F11, G4, H13)
Prior-quarter extract: none available (no verbatim EoM / entity / dropped-slide diff possible; noted as gap, not a mismatch).
Ledger reconciliation: 100% — every A2 row read at its cited line before judging.

## RECONCILIATION NOTE (press-release numbers vs results-filing baseline)
All five headline metrics tie to the results-filing baseline supplied in the task and are internally arithmetic-consistent:
- Revenue 320.5cr (B1, line 70) = baseline 320.5cr. YoY 320.5/276.4−1 = 15.95% ≈ 16.0% (B3) ✓; QoQ 320.5/302.2−1 = 6.05% ≈ 6.1% (B5) ✓.
- EBITDA 51.5cr (B6, line 72) = baseline 51.5cr. Implied margin 51.5/320.5 = 16.07% ≈ 16.1% (B11) ✓; YoY +14.7% (B8) ✓.
- PAT 26.4cr (B14, line 78) = baseline 26.4cr. Implied margin 26.4/320.5 = 8.24% ≈ 8.2% (B19) ✓; YoY +6.5% (B16) ✓.
- Export 94cr (C6, line 92) / 320.5 = 29.3%, consistent with "around 30%" (C5) ✓.
The ledger RESTATEMENT flags (C1 headline, C7/C8 MD quote restating B1/B3) all resolve CONSISTENT — headline 320.5 = table 320.5, quote "16%" = table 16.0%. No restatement discrepancy. RESTATEMENT flag cleared.

Notion watch-item scoreboard (for A4): PAT 26.4cr MISSES the >₹28-30cr watch bar; EBITDA margin 16.1% MISSES the >16.5% watch bar. Both misses are real and are picked up under F16.

---

## FINDINGS TABLE

| id | check | ledger row | line/slide | verbatim quote | classification | forward implication |
|----|-------|-----------|-----------|----------------|----------------|---------------------|
| FND-01 | F2 | GAP#1 / B-header | line 68 | "Particulars (INR Cr)" | AMBIGUOUS | Highlights table never states Standalone vs Consolidated; S-vs-C gap the check requires cannot be computed. A4: confirm basis and whether any subsidiary/JV sits outside these figures. |
| FND-02 | F6 | E3 | line 94 | "Forward integration into Pipe spooling remains on track for commencement by December 2026" | FORWARD-SIGNAL | Dated milestone (Dec-2026). Feeds Role 5 promise-vs-delivery tracker; status word "on track." Next-quarter deck must show "commenced" or slippage. |
| FND-03 | F6 | D5 | line 110 | "we intend to steadily increase the contribution of these higher-value products to our overall revenue mix" | AMBIGUOUS | Fittings/value-added mix commitment with NO timeline and NO target %. A4: quantify current fittings % of revenue and the medium-term target. |
| FND-04 | F6 | D6 | line 113-114 | "forward integration into the spooling business is progressing as planned, with the capex execution on track" | FORWARD-SIGNAL | Capex "on track" but NO Rs Cr capex quantum or capacity-add ever disclosed (GAP#3). Rising below-EBITDA cost is already visible (see FND-08). A4: spooling capex Rs and commissioned capacity. |
| FND-05 | F7 | D9/D10/D11 | line 120-122 | "the geopolitical situation remains an area of watch ... freight rates continue to remain a factor that we are monitoring closely ... these external factors may create near-term uncertainty" | FORWARD-SIGNAL | Newly-worded pre-emptive hedge on the EXPORT book (94cr, ~30% of revenue). Hedge inside a results narrative telegraphs export softness/margin risk for Q2 FY27. A4: export order visibility and freight pass-through. |
| FND-06 | F14 | B-header / B5,B10,B18 | line 68 | second column header "YoY" (over Q4FY26 comparison) | AMBIGUOUS | The Q1FY27-vs-Q4FY26 column is a sequential/QoQ compare mislabeled "YoY," identical to the true YoY column. A reader can misread 6.1%/4.3%/3.9% as year-on-year. A4: request corrected labelling. |
| FND-07 | F14 | E2 / F3 | line 91, 135 | "exports continued to remain around 30% of as a share of our revenues" ; "in n two broad categories" | NEUTRAL-FACT | Two drafting/grammar defects in a document filed to BSE/NSE as final. Individually immaterial; a cumulative governance/QA data point. |
| FND-08 | F16 | C1 / B6-B21 | line 58, 72-80 | headline "All time high revenue of INR 320.5 Crores" | FORWARD-SIGNAL | Revenue-record headline masks margin compression: EBITDA margin 16.1% vs 16.2% (Q1FY26) / 16.3% (Q4FY26); PAT margin 8.2% vs 9.0% YoY (−80bps). PAT grew only 6.5% vs revenue 16.0% — sub-EBITDA cost creep (depreciation/interest/tax) consistent with the capex ramp. Table shows NO bps delta for either margin (B13, B21), suppressing the compression. |
| FND-09 | F16 | GAP#2/#3 | lines 66-95 | (absence) — no order-book, no capex Rs, no fittings-utilisation, no BHEL/NTPC, no DRI | AMBIGUOUS | Sector-standard order-book figure absent (GAP#2); capex quantum absent (GAP#3); Notion watch items — fittings utilisation, BHEL/NTPC approval, DRI — all silent. Confirmatory silence risk on catalysts investors were told to watch. A4: raise each as a direct question. |
| FND-10 | F14 | G4 | line 33-34 | "please find attached herewith a copy of the Proposed Press Release to be issued by the Company. The same shall also be uploaded ..." | AMBIGUOUS | Release filed to exchanges as "Proposed" (DRAFT_STATUS) — the final issued version may differ from the version enumerated here. A4/pipeline: reconcile against the final website-uploaded release when available. |

---

## CHECKLIST SCORECARD (all 17 — no blanks)

| Check | Status | Basis (one line) |
|-------|--------|------------------|
| F1 ZERO-VALUE STANDING ITEMS | N.A. | 5-metric highlights extract, not a full statement; ledger `zero_standing: 0` (GAP#4). |
| F2 STANDALONE vs CONSOLIDATED | FINDING | No S/C basis label anywhere (line 68); S-vs-C gap non-computable — FND-01. |
| F3 SHELL-ENTITY DETECTION | N.A. | No consolidated cost lines, no entity list in this doctype. |
| F4 UNAUDITED CONTRIBUTION RATIO | N.A. | No auditor report / Other Matters in a press release (results flagged "unaudited," G2/G3, but no component-auditor split). |
| F5 GOING CONCERN / EoM SCOPE | N.A. | No auditor letter and no prior-quarter text to verbatim-diff. |
| F6 FORWARD-COMMITMENT MINING | FINDING | Hits "commencement by December 2026" (l.94), "intend to" (l.110), "on track/progressing as planned" (l.113-114) — FND-02/03/04. |
| F7 HEDGE PHRASE MINING | FINDING | "area of watch", "monitoring closely", "may create near-term uncertainty" on exports (l.120-122) — FND-05. |
| F8 TAX FORENSICS | N.A. | No PBT/tax/deferred-tax lines; ETR not computable from EBITDA+PAT alone. |
| F9 OCI FORENSICS | N.A. | No OCI / actuarial disclosure in a highlights release. |
| F10 SHARE COUNT & DILUTION | N.A. | Deck carries no share count, paid-up capital, or basic/diluted EPS. |
| F11 RESERVES & NET WORTH | N.A. | No net-worth / other-equity figure disclosed. |
| F12 SEGMENT FORENSICS | N.A. | Segment growth %s given (welded 21%, seamless 15%) but no segment assets/liabilities/absolutes (NO_ABSOLUTE_VALUE); assets-liabilities trend non-computable. |
| F13 BOARD OUTCOME BEYOND RESULTS | N.A. | Press release, not a Board Outcome letter; no AGM/AR/director/resolution items. |
| F14 NOTE-DRAFTING INCONSISTENCIES | FINDING | Mislabeled "YoY" header (l.68), two grammar defects (l.91, l.135), "Proposed" draft status (l.33-34) — FND-06/07/10. |
| F15 ENTITY-LIST DIFFS | N.A. | No consolidation list and no prior quarter to diff. |
| F16 DROPPED/REFRAMED DISCLOSURES | FINDING | Record-revenue headline reframes away margin compression; order-book/capex/fittings-util/BHEL-NTPC/DRI absent — FND-08/09. |
| F17 CONCALL SILENCE AUDIT | N.A. | No concall transcript this document; Notion-checklist silence captured under F16/FND-09 instead. |

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | ref | status word |
|------------|--------------|-----|-------------|
| Forward integration into pipe spooling to commence | December 2026 | line 94 (E3), restated line 113-114 (D6) | on track / underway ("progressing as planned") |
| Increase contribution of fittings & higher-value products to revenue mix | "over the medium term" (no date) | line 110 (D5) | intended / underway ("encouraging response") |
| Spooling capex execution | (tied to Dec-2026 commissioning) | line 114 (D6) | on track (no Rs quantum disclosed) |

---

## CLASSIFICATION SUMMARY (for A4 question generation)
- FORWARD-SIGNAL: FND-02, FND-04, FND-05, FND-08
- AMBIGUOUS (→ A4 management questions): FND-01, FND-03, FND-06, FND-09, FND-10
- NEUTRAL-FACT: FND-07
- CONFIRMATORY-NEGATIVE: none isolated this cycle (FND-09 silence is AMBIGUOUS absent a prior-quarter baseline to prove sustained silence).
