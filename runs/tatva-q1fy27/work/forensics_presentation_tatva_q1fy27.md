# FORENSICS — Tatva Chintan Pharma Chem Limited (TATVA), Q1 FY27, Investor Presentation

Agent: A3 FORENSIC NOTES | Model: claude-opus-4-8
Doctype: presentation (36 slides) | Quarter: Q1 FY27 (quarter ended 30 June 2026)
A1 extract: runs/tatva-q1fy27/work/extract_presentation_tatva_q1fy27.txt (1,613 lines)
A2 ledger: runs/tatva-q1fy27/work/ledger_presentation_tatva_q1fy27.md
Prior-quarter deck: none (first run) — DROPPED_SLIDE / reframe-diff comparisons N.A.
Ledger reconciliation: 100% (every Table-1/2/3/4 row read at its cited line in the extract; Table 5 is N.A. this run).

Doctype scope applied per prompt: on a presentation, **F16 applies plus any F6/F10/F11 numbers the deck carries.** Balance-sheet / auditor checks (F2, F3, F4, F5, F8, F9, F12, F13, F15) are N.A. because a presentation carries no standalone statements, no auditor report / Other Matters, no OCI schedule, no segment asset-liability tables, no board resolutions, and no consolidation entity list. F17 (concall silence) is N.A. (no transcript); the Notion monitoring-checklist silence audit is folded into F16 as the presentation analog.

---

## FINDINGS TABLE

| id | check | ledger row ref | line / slide | verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-01 | F1 | T3b #11 ZERO_STANDING | L634, slide 9 | "Exceptional items - - - 35.87 - - -" | AMBIGUOUS | One-off ₹35.87 mn hit FY23 only; nature undisclosed in deck. Immaterial to forward thesis but unexplained — A4 candidate question. |
| A3-02 | F1 | T3c #15 ZERO_STANDING + #18 | L672 (LT borr.), L676 (ST borr.), slide 10 | "(i) Long-term borrowings 387.09 267.63 131.11 42.30 6.39 - 50.10" ; "(i) Short-term Borrowings … 363.88 1,153.63" | FORWARD-SIGNAL | Company was near debt-free FY25 (LT borrowings = dash) then re-levered in FY26: fresh LT debt ₹50.10 mn AND short-term borrowings +217% (363.88→1,153.63). D/E 0.05→0.15, D/EBITDA 1.00→1.29 (L489-490). Re-leveraging funds the capacity build/working capital — watch FY27 for further draw. |
| A3-03 | F6 | T1 slide 19 / 24 | L939-941 (s19), L1329-1333 (s24) | "started R&D into continuous flow chemistry since 2018" ; "Continuous Flow Chemistry being developed which would involve manufacturing large volumes … that leads to higher margins" | FORWARD-SIGNAL | Continuous Flow Chemistry is still pre-commercial after 8 years of R&D (since 2018); presented as future margin lever ("would involve", "leads to higher margins") with no commercialization date. Promise-vs-delivery tracker item. |
| A3-04 | F6 | T1 slide 28 | L1398-1402 | "Capex to boost the capacities and pave the way for higher revenues." | AMBIGUOUS | Only forward capacity/capex statement in the deck, and it is undated and unquantified — no capex figure, no target capacity, no timeline. A4 should convert to a management question (quantum, assets, commissioning date). |
| A3-05 | F10 | T3c #12 | L667, slide 10 | "Equity share capital 80.35 200.88 221.65 221.65 233.92 233.92 233.92" | AMBIGUOUS | Paid-up capital +150% FY20→FY21 (80.35→200.88) is NOT on the milestone timeline (slide 32) — likely a pre-IPO bonus but unexplained in the deck. Later steps trace cleanly: FY22 IPO (221.65), FY24 QIP ₹200 cr Aug-2023 (233.92, L1500). Share count 2,33,92,055 ties to market cap 27,937 mn @ ₹1,194.30 (L1552-1558). No basic/diluted split disclosed, so no dilution spread to test. |
| A3-06 | F11 | T3c #14 vs #3 | L669 (TNW), L657 (intangibles), slide 10 | "Tangible net worth … 7,81 7.5 9" | NEUTRAL-FACT | "Tangible net worth" = Equity capital 233.92 + Other equity 7,583.67 = 7,817.59 (ties exactly), but it does NOT deduct intangible assets of ₹68.26 mn (FY26). Label is inaccurate: this is book net worth, not tangible net worth. Matters if any covenant / rating uses "TNW". True tangible NW ≈ 7,749.33. |
| A3-07 | F14 | T3b #17-18 vs T3a #3-4 | L640-641 (s9), L443-444 (s6) | "EBIDTA ₹ … EBIDTA %" vs "EBITDA (Excl. Other Income) … EBITDA Margin" | NEUTRAL-FACT | "EBIDTA" (misspelled) on slides 5/8/9 vs "EBITDA" on slide 6 table; plus typos "Sate of the Art" (L710), singular "Research & Development center" title (L1227). Individually immaterial; cumulatively a drafting-quality / governance data point. |
| A3-08 | F16 | T1 slide 6 donut vs slides 15/18 | L454 (s6 donut), L811-812 (s15), L923-924 (s18) | donut "SDA 34% … PASC 35%" vs slide 15 "35% of Revenue" (SDA) and slide 18 "34% of Revenue" (PASC) | AMBIGUOUS | Q1FY27 SDA and PASC shares are SWAPPED between the revenue-split donut (SDA 34 / PASC 35) and the product pages (SDA 35 / PASC 34). Underlying values near-identical (SDA 578/1,671=34.6%, PASC 584/1,671=34.9%), so rounding artifact — but inconsistent presentation of the same quarter. Definitional-consistency flag for A4. |
| A3-09 | F16 | T2 slide 5 vs slide 6 | L430 (s5 chart), L444 (s6 table) | "Q4FY26 281 (21.0%) | Q1FY27 323 (19.0%)" ; table "EBITDA Margin 19% … 21% -8%" | FORWARD-SIGNAL | Deck leads on YoY EBITDA "+86%", but sequentially EBITDA margin COMPRESSED 21.0%→19.0% (QoQ -200 bps) while revenue rose. Q1FY27 margin of 19.0% sits below the FY27 20-22% target band (Notion monitoring) though above the 18% RED line. The QoQ margin fade is downplayed under the YoY headline. |
| A3-10 | F16 | T1 slide 32; monitoring-checklist silence | L1488-1489, slide 32 | "Acquired industrial land at Dahej-III GIDC Estate, Bharuch" (2021 milestone) | CONFIRMATORY-NEGATIVE | Two catalysts the monitoring checklist expected in Q1 FY27 — Dahej-III groundbreaking and semiconductor first dispatch — are ABSENT from the deck. Dahej-III appears only as a 2021 land-acquisition milestone with no construction/groundbreaking update; "semiconductor" appears nowhere in the extract. Silence on expected near-term catalysts. |
| A3-11 | F16 | monitoring-checklist silence (margin target) | deck-wide (no line) — absent | (no restatement of "FY27 op EBITDA 20-22%" anywhere in deck) | FORWARD-SIGNAL | Management's FY27 EBITDA-margin target of 20-22% (per Notion) is NOT restated in this deck. With Q1FY27 already at 19.0% and QoQ falling, the omission of a reaffirmed margin guide is a soft-amber. A4 should ask whether the 20-22% guide still stands. |
| A3-12 | F16 | T2 slide 12 | L717-719, slide 12 | "Exports constitute 75% of revenue in FY25" | AMBIGUOUS | Export intensity is quoted for FY25 in a Q1 FY27 deck; no FY26 or Q1FY27 export % is given despite FY26 being the headline year everywhere else. Stale/reframed metric — A4 should request the current export mix. |
| A3-13 | F16 | monitoring-checklist silence (standalone) | deck-wide — absent | (deck presents only "Consolidated" statements; slides 9-10 headed "Consolidated") | AMBIGUOUS | Deck is consolidated-only; the monitoring item "standalone parent profit share above 50% (from 6%)" cannot be assessed — no standalone P&L. Absence of any standalone split is itself a disclosure gap for a thesis that turns on parent-vs-subsidiary profit mix. |

---

## CHECKLIST SCORECARD (all 17; one status each)

| Check | Status | One-line basis |
|---|---|---|
| F1 ZERO-VALUE STANDING ITEMS | FINDING | Both ledger ZERO_STANDING rows examined: Exceptional items (₹35.87 mn FY23 only, else dash — A3-01) and Long-term borrowings (dash FY25, re-appears ₹50.10 mn FY26 alongside +217% ST-borrowing surge — A3-02). |
| F2 STANDALONE vs CONSOLIDATED | N.A. | Presentation carries only consolidated statements (slides 9-10 headed "Consolidated"); no standalone figures to decompose. |
| F3 SHELL-ENTITY DETECTION | N.A. | No standalone cost lines disclosed; cannot compare standalone vs consolidated COGS/employee/depreciation for shell detection. |
| F4 UNAUDITED CONTRIBUTION | N.A. | No auditor report / Other Matters paragraph in a presentation; no component-auditor Rs amount to ratio. |
| F5 GOING CONCERN / EoM | N.A. | No auditor Emphasis-of-Matter / going-concern paragraph in a presentation; and no prior deck to verbatim-diff. |
| F6 FORWARD-COMMITMENT MINING | FINDING | Lexicon run over all text slides: CFC "being developed"/"would involve" pre-commercial since 2018 (A3-03); slide-28 "Capex to boost the capacities" undated/unquantified (A3-04). Most "commenc-" hits are historical milestones (slide 32). |
| F7 HEDGE PHRASE MINING | PASS | Only qualifier is the boilerplate Safe Harbor (slide 35, L1577-1588): "could cause actual results to differ materially", risks "including but not limited to … COVID-19 pandemic". Standard cover; stale COVID reference in a 2026 deck noted but no newly added specific hedge on lumpiness/customer concentration. |
| F8 TAX FORENSICS | N.A. | Deck carries only a summary ETR row (slide 9, L642) with no tax-expense breakdown, deferred-tax sign, or earlier-year-adjustment line to run forensics. NOTE for A4: FY23 ETR = -2% (tax credit ₹(7.08) mn on PBT ₹447.79 mn) is anomalous vs 25.17% statutory. |
| F9 OCI FORENSICS | N.A. | No OCI / actuarial schedule in a presentation. |
| F10 SHARE COUNT & DILUTION | FINDING | Paid-up capital steps traced (IPO FY22, QIP FY24) but FY20→FY21 +150% jump not on milestone timeline (A3-05); no basic/diluted split disclosed so no dilution spread test. Share count ties to market cap. |
| F11 RESERVES / NET WORTH TIE-OUT | FINDING | Equity capital + Other equity = stated net worth exactly (all 7 years); but "Tangible net worth" fails to deduct intangibles ₹68.26 mn (FY26) — mislabel (A3-06). |
| F12 SEGMENT FORENSICS | N.A. | Deck discloses product-category REVENUE only (slide 20); no segment assets/liabilities to trend. NOTE for A4: SDA Q1FY27 ₹578 mn (~₹231 cr annualised) vs monitoring target Rs 250-300 cr FY27; SDA history is volatile (2,248/1,277/1,655/1,197/2,045). |
| F13 BOARD OUTCOME | N.A. | Presentation carries no board resolutions, AGM notice, dividend/record date, or director term dates (slide 33 lists 3 independent directors with tenure descriptions, no reappointment dates). |
| F14 NOTE DRAFTING INCONSISTENCIES | FINDING | "EBIDTA" (slides 5/8/9) vs "EBITDA" (slide 6); typos "Sate of the Art", singular "…center" title (A3-07). Immaterial individually; cumulative governance data point. |
| F15 ENTITY LIST DIFFS | N.A. | No consolidation entity list in the deck and no prior-quarter baseline; subsidiaries named narratively (Tatva Chintan USA Inc.; Tatva Chintan Europe BV) with no relationship-change diff possible. |
| F16 DROPPED / REFRAMED DISCLOSURES | FINDING | Dropped-slide diff N.A. (no prior deck), but internal-consistency + monitoring-silence findings raised: SDA/PASC % swap (A3-08), QoQ margin compression masked by YoY headline (A3-09), Dahej-III/semiconductor catalyst silence (A3-10), FY27 20-22% margin guide not restated (A3-11), stale FY25 export % (A3-12), consolidated-only / no standalone split (A3-13). |
| F17 CONCALL SILENCE AUDIT | N.A. | No concall transcript in scope; the Notion monitoring-checklist silence audit is captured under F16 (A3-10, A3-11, A3-13) as the presentation analog. |

GATE A3: PASS — all 17 checks marked exactly one of PASS / FINDING / N.A.; no blanks.

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | ref | status word |
|---|---|---|---|
| Continuous Flow Chemistry commercialization (large-volume, higher-margin) | none stated (R&D "since 2018") | slide 19 L939-941 / slide 24 L1329-1333 | underway (pre-commercial) |
| "Capex to boost the capacities and pave the way for higher revenues" | none stated (unquantified) | slide 28 L1398-1402 | intended / underway (vague) |
| Commercial production at expanded Dahej SEZ | 2023 (historical) | slide 32 L1495-1496 | completed |
| Dahej-III GIDC (Bharuch) industrial land | land acquired 2021; groundbreaking not stated | slide 32 L1488-1489 | initiated (land only — no construction update) |

Note for A4 / Role 5 promise-vs-delivery: the deck confirms no milestone advance on Dahej-III (still land-only since 2021) and no mention of semiconductor first dispatch — both were Q1 FY27 catalysts on the monitoring checklist. Sustained silence on a catalyst is treated as a confirmatory negative pending the concall.

---

```yaml
stage: A3-forensics
company: "TATVA"
quarter: "Q1 FY27"
doctype: "presentation"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/tatva-q1fy27/work/forensics_presentation_tatva_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: PASS
  F8: N.A.
  F9: N.A.
  F10: FINDING
  F11: FINDING
  F12: N.A.
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: N.A.
findings:
  - {id: "A3-01", check: "F1", line: "L634 slide 9", classification: "AMBIGUOUS", implication: "One-off exceptional ₹35.87mn FY23 only; nature undisclosed"}
  - {id: "A3-02", check: "F1", line: "L672/L676 slide 10", classification: "FORWARD-SIGNAL", implication: "Re-levered FY26: fresh LT debt 50.10 + ST borrowings +217%; D/E 0.05->0.15"}
  - {id: "A3-03", check: "F6", line: "L939-941/L1329-1333 slides 19,24", classification: "FORWARD-SIGNAL", implication: "Continuous Flow Chemistry still pre-commercial after 8yr R&D; future margin lever, no date"}
  - {id: "A3-04", check: "F6", line: "L1398-1402 slide 28", classification: "AMBIGUOUS", implication: "Capex-to-boost-capacities undated and unquantified; only forward capex statement in deck"}
  - {id: "A3-05", check: "F10", line: "L667 slide 10", classification: "AMBIGUOUS", implication: "Equity capital +150% FY20->FY21 not on milestone timeline; no basic/diluted split"}
  - {id: "A3-06", check: "F11", line: "L669 vs L657 slide 10", classification: "NEUTRAL-FACT", implication: "'Tangible net worth' does not deduct intangibles 68.26mn; mislabel, matters for covenants"}
  - {id: "A3-07", check: "F14", line: "L640-641/L443-444", classification: "NEUTRAL-FACT", implication: "EBIDTA vs EBITDA spelling + typos; cumulative drafting-quality data point"}
  - {id: "A3-08", check: "F16", line: "L454 vs L811-812/L923-924", classification: "AMBIGUOUS", implication: "Q1FY27 SDA/PASC % swapped between donut and product pages; rounding-driven inconsistency"}
  - {id: "A3-09", check: "F16", line: "L430 vs L444 slides 5,6", classification: "FORWARD-SIGNAL", implication: "QoQ EBITDA margin 21%->19% (-200bps) masked under YoY +86% headline; below 20-22% target"}
  - {id: "A3-10", check: "F16", line: "L1488-1489 slide 32", classification: "CONFIRMATORY-NEGATIVE", implication: "Dahej-III groundbreaking & semiconductor first dispatch (Q1FY27 catalysts) absent from deck"}
  - {id: "A3-11", check: "F16", line: "deck-wide (absent)", classification: "FORWARD-SIGNAL", implication: "FY27 20-22% EBITDA margin target not restated; Q1FY27 already at 19% and falling"}
  - {id: "A3-12", check: "F16", line: "L717-719 slide 12", classification: "AMBIGUOUS", implication: "Export intensity quoted for FY25 (75%) in a Q1FY27 deck; no current export mix"}
  - {id: "A3-13", check: "F16", line: "deck-wide (consolidated-only)", classification: "AMBIGUOUS", implication: "No standalone split; monitored parent-profit-share (>50% from 6%) not assessable"}
forward_signals: ["A3-02", "A3-03", "A3-09", "A3-11"]
ambiguous: ["A3-01", "A3-04", "A3-05", "A3-08", "A3-12", "A3-13"]
commitments:
  - {commitment: "Continuous Flow Chemistry commercialization (large-volume, higher-margin)", implied_date: "none stated (R&D since 2018)", ref: "slide 19 L939-941 / slide 24 L1329-1333", status_word: "underway"}
  - {commitment: "Capex to boost capacities / higher revenues", implied_date: "none stated (unquantified)", ref: "slide 28 L1398-1402", status_word: "initiated"}
  - {commitment: "Commercial production at expanded Dahej SEZ", implied_date: "2023 (historical)", ref: "slide 32 L1495-1496", status_word: "completed"}
  - {commitment: "Dahej-III GIDC (Bharuch) build", implied_date: "land acquired 2021; groundbreaking not stated", ref: "slide 32 L1488-1489", status_word: "initiated"}
gate_a3: pass
blank_checks: []
```
