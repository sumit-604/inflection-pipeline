# A3 FORENSIC NOTES — Tata Power (TATAPOWER) — Q1 FY27 — Doctype: PRESENTATION

Source spine: `runs/tatapower-q1fy27/work/extract_presentation_tatapower_q1fy27.txt` (PDFium layout reconstruction, 71 slides, 100% coverage; poppler unavailable — this extract is the trusted evidence spine).
Ledger reconciled: 100% (all 71 Table-1 slide rows, all 13 Table-2 ZERO_STANDING rows, all 61 Table-3 footnotes read at their cited lines).
Line citations below use the extract's embedded line numbers (the `NNNN|` column) plus the slide number.
Doctype rule applied: F16 is the primary presentation check; F6/F7/F11 run on the numbers/phrases the deck carries; auditor/notes-only checks (F4, F5, F9) and concall/board checks (F13, F17) are marked N.A. with reason. Every check carries exactly one status.

---

## FINDINGS TABLE

| id | check | ledger row ref | slide / line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-01 | F2 | Slide 43 / Slide 40 | s43 ln1265 / ln1253 ; s40 ln1150 | "PAT for the period 277 … (47%)"; "Other Income 191 521 (63%)"; consol "Net Profit for the period 1,401 1,262 11%" | FORWARD-SIGNAL | Standalone (the listed parent) PAT fell 47% and EBITDA fell 15%, driven by a ₹330 Cr collapse in standalone Other Income; consol PAT still +11%. S-vs-C PAT gap widened from 742 to 1,124 (≈73% of standalone-PAT base, far above the 5pp trigger). Parent-level earnings deterioration is being masked by subsidiaries/associates. |
| A3-02 | F2 / F4-analogue | Slide 40 / Slide 41 | s40 ln1142–1143 | "Share of Associates & JV's results 241 130 86%"; "…partly offset by loss in one of the associate companies" | AMBIGUOUS | Associate/JV share jumped 86% to ₹241 Cr = 17.2% of consol PAT (above 10%), and one unnamed associate is loss-making. Consol is UNAUDITED (cover letter ln15). Which associate is bleeding (Tata Projects / Nelco / Resurgent)? -> A4 question. |
| A3-03 | F6 | Slides 7,15,27,28,30,32,36,37,58 | s27 ln773; s32 ln940; s37 ln1059/1069/1073 | "On track to deliver 2.5 GW of RE capacity addition in FY 2027"; "Full Commissioning in H1 FY2027"; "Expected commissioning in FY 2029 / FY 2032"; "main civil works package scheduled for award in Q2 FY27" | FORWARD-SIGNAL | Dense dated commitment set (see Commitment Register). Feeds Role 5 promise-vs-delivery tracker and FTTCP catalyst timeline. |
| A3-04 | F7 | Slide 59 | s59 ln1729 | "*Subject to completion of contractual obligations and useful life" | AMBIGUOUS | Pre-emptive hedge attached to the flagship "100% Clean & Green by 2045 / 70% by 2030" decarbonization claim — the thermal-exit target is explicitly conditional. -> A4 question on what contractual obligations gate the thermal run-off. |
| A3-05 | F8 | Slide 45 (Tbl2 #11) | s45 ln1317 | PPGCL "Tax - - -" on "PBT 143 110" | FORWARD-SIGNAL | Prayagraj books ZERO current tax on ₹143 Cr PBT (both periods, 100%-basis) = carryforward/DTA utilisation on the acquired stressed asset. Future ETR step-up risk when shields exhaust. |
| A3-06 | F8 | Slide 44 | s44 ln1288 | "Tax 32 13 148%" | NEUTRAL-FACT | Maithon ETR stepped from 12.6% to 23.7% YoY (tax +148%) — normalising toward statutory; a headwind to MPL PAT growth going forward. |
| A3-07 | F8 | Slide 50 | s50 ln1474 / ln1472 | "Tax 79 20 284%" on "PBT 449" | FORWARD-SIGNAL | TP Solar ETR ≈17.6%, well below 25.17% statutory (manufacturing incentive/DTA). As the plant's profit scales (PAT +287%), an eventual ETR normalisation is a latent earnings drag. |
| A3-08 | F12 | Slide 42 | s42 ln1232 | "Others (Incl. Tata Projects, Nelco) 123 121 1 51 (330) (213)" | AMBIGUOUS | The "Others" cluster EBITDA collapsed from ₹51 Cr to ₹1 Cr and PAT loss widened from (213) to (330). Likely the "loss in one associate" of A3-02. Deteriorating and undisclosed granularly. -> A4 question. |
| A3-09 | F12 | Slide 53 | s53 ln1556 / ln1564 | TPDDL regulated assets "4,940 … 3,666"; Total "10,790 … 9,009" | FORWARD-SIGNAL | Regulatory assets (under-recovery, cash locked) accreting fast: TPDDL +35% YoY, consolidated regulated assets +20% YoY. Growing regulated-asset base = future tariff-true-up dependency and working-capital drag; ties to the QoQ net-debt build. |
| A3-10 | F12 | Slide 47 / Slide 33 | s47 ln1368 | "Actual AT&C losses* 31% 28% 32% 31% 26% 22% 17% 17%" | FORWARD-SIGNAL | Odisha AT&C losses WORSENED YoY at 3 of 4 discoms (TPCODL 28->31, TPSODL 31->32, TPWODL 22->26) and every discom sits ABOVE its vesting-order target (e.g. TPCODL target 16% vs actual 31%). Deck headline "26.7%" (s15/s33) masks the worsening trend. Regulatory under-recovery risk. |
| A3-11 | F12 | Slide 42 (Tbl2 #7 area) | s42 ln1220 | Renewables "Eliminations (1,803) (1,425) (216) 23 (106) 39" | AMBIGUOUS | Intra-Renewables EBITDA elimination swung from +23 to (216) — a ₹239 Cr adverse swing, likely rising captive/DCR module-profit elimination as TP Solar sells internally. Distorts YoY Renewables EBITDA quality. -> A4 question on elimination drivers. |
| A3-12 | F14 | Slides 27,36,37,41,42 | s27 ln767 vs s36/37 ln1033/1035 ; s41 ln1196 vs s42 ln1238 | "Khorluchu … Dorjiliung" (s27) vs "Khorlochhu … Dorjilung" (s36/37); "***…88.57%" (s41) vs "***TPCL stake-20%" (s42) | NEUTRAL-FACT | Project-name spelling inconsistencies across tables and reuse of the "***" footnote marker to mean two different stakes on adjacent slides. Individually immaterial; cumulatively a drafting/governance data point. |
| A3-13 | F16 | Slides 41,42,48,49,50 | s41 ln1195 (repeats ln1237,1414,1443,1481) | "Prior period segment figures are restated to include segmental corporate cost" | AMBIGUOUS | A metric-definition RESTATEMENT that re-bases every Q1FY26 entity/cluster comparative used in the YoY growth and CAGR panels (s20-22). Quantum of reallocated corporate cost not disclosed -> YoY growth rates are not on a like-for-like reported base. -> A4 question on restatement quantum. |
| A3-14 | F16 | Slide 23 / Slide 55 | s23 ln642/643 ; s23 title ln626 ; s55 ln1618 | "Net Debt to Underlying EBITDA … 3.41"; "1.25"; slide titled "Comfortable Debt Position For Sustainable Growth" | FORWARD-SIGNAL | Leverage rising for a 3rd straight year: Net Debt/Underlying EBITDA 2.66(FY23)->3.34(FY26)->3.41(Q1FY27); Net Debt/Equity 0.99(FY24)->1.25. Net debt jumped ₹5,116 Cr QoQ (56,122->61,238) on record ₹5,375 Cr quarterly capex. Positive slide framing sits on a deteriorating leverage trend. |
| A3-15 | F16 | Slides 30,31,69 | s30 ln876 ; s31 ln906/901 | "639 Crores … Order book"; "Order Book at Q1 FY27 stands at ₹639 crore"; "387 MW orders won in Q1 FY27" | FORWARD-SIGNAL | 3rd-party rooftop order book stands at only ₹639 Cr after ₹1,350 Cr orders received and ₹898 Cr revenue billed in the quarter — the closing book is below both the intake and the quarterly revenue run-rate, i.e. the book is being drawn down faster than replenished. Forward rooftop-demand signal. |
| A3-16 | F16 | Ledger note (NO_PRIOR_LEDGER) | ledger ln3/158 | "prior-quarter deck/ledger not supplied … DROPPED_SLIDE comparison could not be performed" | NEUTRAL-FACT | Dropped/reframed-metric and axis-baseline detection could not be run quarter-over-quarter this cycle. Re-run F16 retrospectively once the Q4 FY26 deck ledger is available. |
| A3-17 | F1 | Slide 55 (Tbl2 #12) | s55 ln1615 | "Less: Related Party Debt - - 203" | NEUTRAL-FACT | Standing balance-sheet line dormant (nil Q1FY27 and Q4FY26) but ₹203 Cr one year ago. Reappearance is a related-party-funding tell; keep on watch. (All 13 ZERO_STANDING rows reconciled; remainder are structural template lines — exceptional-items and equity-method-only-at-PAT rows.) |

---

## CHECKLIST SCORECARD (F1–F17)

| # | Status | One-line basis |
|---|---|---|
| F1 | FINDING | 13 ZERO_STANDING rows all read/reconciled; structural except the "Less: Related Party Debt" line (nil now, ₹203 Cr a year ago) flagged for reappearance — A3-17. |
| F2 | FINDING | Standalone PAT -47% / EBITDA -15% vs consol PAT +11%; S-vs-C PAT gap widened 742->1,124 (~73% of standalone base); associate share now 17% of consol PAT with an unnamed loss-making associate — A3-01, A3-02. |
| F3 | PASS | No shell pattern: every subsidiary table (s44-50) carries its own generation/fuel/opex; associate-only-at-PAT entities (IEL, PPGCL, Powerlinks) are equity-method presentations, not shells. Deck lacks standalone-vs-consol cost-line split for a full identical-cost test, but affirmative operations are visible. |
| F4 | N.A. | Investor deck carries no auditor "Other Matters" paragraph; unaudited component Rs-amount cannot be extracted. Analogue surfaced under A3-02 (consol unaudited; JV/associate = 17% of PAT). |
| F5 | N.A. | No auditor Going-Concern / Emphasis-of-Matter paragraph exists in a Reg-30 analyst presentation. |
| F6 | FINDING | Extensive dated management commitments mined (2.5 GW FY27; H1 FY27 / FY27 / FY28 / FY29 / FY32 commissioning dates; Q2 FY27 civil-works award; FY30E financial aspirations) — A3-03, see Commitment Register. |
| F7 | FINDING | Operational hedge "subject to completion of contractual obligations and useful life" attached to the 2045/2030 decarbonization target (s59), beyond boilerplate disclaimer (s3) — A3-04. |
| F8 | FINDING | PPGCL zero tax on ₹143 Cr PBT (DTA/carryforward, ETR step-up risk); TP Solar ETR ~17.6% (sub-statutory); MPL ETR normalising 12.6%->23.7% — A3-05, A3-06, A3-07. No "earlier-years tax adjustment" line disclosed in deck. |
| F9 | N.A. | No OCI / actuarial gains-losses disclosure in the deck. |
| F10 | N.A. | Deck shows a single adjusted EPS (₹3.7, s8) only; no paid-up capital, no basic-vs-diluted spread to test. No corporate action indicated. |
| F11 | PASS | Consol Net Worth ₹49,026 Cr ties to Net Debt/Equity 1.25 (61,238/49,026) internally (s23=s55); YoY +₹4,990 Cr consistent with retained earnings; no third-party net-worth figure to reconcile against and no >5% gap. |
| F12 | FINDING | Segment deterioration: "Others (Tata Projects/Nelco)" EBITDA 51->1 & PAT (213)->(330); regulated-asset accretion (TPDDL +35% YoY); Odisha AT&C worsening & above vesting targets; Renewables intra-segment elimination swing -239 Cr — A3-08 to A3-11. |
| F13 | N.A. | No Board's Report / AGM notice / director-appointment term dates in an analyst deck. |
| F14 | FINDING | Project-name spelling inconsistencies and reused "***" footnote marker across adjacent tables — A3-12. |
| F15 | N.A. | Entity-list diff requires prior-quarter deck/ledger — NO_PRIOR_LEDGER (ledger ln3/158). Note: Solar EPC/TPSSL merger into TPREL (eff 1-Apr-2023, s49 ln1444) is an already-historical structural change, not this quarter's. |
| F16 | FINDING | Prior-period segment restatement (corporate-cost reallocation); rising leverage under positive framing; drawn-down rooftop order book; dropped-metric detection blocked by NO_PRIOR_LEDGER — A3-13 to A3-16. |
| F17 | N.A. | Concall silence audit requires a transcript; doctype is presentation and no Notion monitoring checklist was injected this run. |

Blank checks: none (GATE A3 satisfied — 17/17 carry exactly one status).

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | slide / line ref | status word |
|---|---|---|---|
| Deliver 2.5 GW of RE capacity addition | FY2027 | s27 ln773 | underway ("on track") |
| Jalpura Khurja Transmission full commissioning | H1 FY2027 | s32 ln940 | underway (partially commissioned) |
| Bikaner Transmission (692 CktKm) commissioning | FY2027 | s32 ln934 | under construction |
| MSEDCL 400MW Hybrid commissioning | FY2027 | s28 ln793 | signed / under execution |
| Dorjilung main civil works package award | Q2 FY27 | s37 ln1073 | scheduled ("scheduled for award") |
| SJVN 460MW / NTPC 200MW / Mumbai DISCOM 80MW FDRE commissioning | FY2028 | s28 ln793 | LoA received, PPA signed |
| Jejuri / Gopalpur / Paradeep TBCB commissioning | FY2028 | s32 ln926–932 | under construction |
| Khorlochhu HPP (600MW) commissioning | FY2029 | s37 ln1059 | construction started |
| Ryapte Power Transmission (491 CktKm) commissioning | FY2029 | s32 ln922 | LOI received / under construction |
| Dorjilung HPP (1,125MW) commissioning | FY2032 | s37 ln1069 | pre-construction started |
| SJVN RTC 88MW PPA execution | 24 months post PPA signing | s28 ln801 | PENDING (PPA not yet signed) |
| FY30E: Revenue ~₹1,00,000 Cr, EBITDA ~₹30,000 Cr, PAT ~₹10,000 Cr, capacity >30 GW | FY2030 | s7 ln129–152 | aspiration ("what we aim to achieve") |
| Rooftop: 30 lakh households served, ~₹30,000 Cr cumulative revenue | 2030 | s30 ln876 | aspiration |
| ESG: DJSI EM 80/100 (2027); Clean&Green 70% (2030); Net Zero (2045) | 2027 / 2030 / 2045 | s58 ln1710 / s59 ln1724 | in progress (hedged, see A3-04) |
| Mundra SPPA (signed Mar'26 w/ Gujarat DISCOM); plant runs under Section 11 | ongoing | s15 / s70 ln2082 | completed (signed) / regulatory-directed operation |

---

## RECONCILIATION NOTE (cluster-vs-consolidated, task-requested)

The three presentations of Q1FY27 results tie out exactly to consolidated ₹18,898 Cr revenue / ₹4,249 Cr EBITDA / ₹1,401 Cr PAT:
- Slide 40 (consolidated P&L) = 18,898 / 4,249 / 1,401.
- Slide 41 (entity-wise): TOTAL-A 21,822/4,539/1,219 + JV&Assoc PAT 241 + Eliminations (2,924)/(291)/(60) -> 18,898/4,249/1,401. Reconciles.
- Slide 42 (cluster-wise): Thermal 635 + Renewables 612 + T&D 492 + Others(Tata Projects/Nelco) (330) + inter-cluster elim (8) = 1,401 PAT. Reconciles.
- Slide 69 "Elimination/Others" (338) = slide 42 Others (330) + inter-cluster (8). Consistent.
The reconciliation is clean (no arithmetic break); the forensic content is in the composition — restated comparatives (A3-13), the "Others" cluster drag (A3-08), and the standalone-vs-consol divergence (A3-01), not in a footing error.

---

```yaml
stage: A3-forensics
company: "TATAPOWER"
quarter: "Q1 FY27"
doctype: "presentation"
model: claude-opus-4-8
status: complete
forensics_path: "runs/tatapower-q1fy27/work/forensics_presentation_tatapower_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: FINDING
  F3: PASS
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: N.A.
  F10: N.A.
  F11: PASS
  F12: FINDING
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: N.A.
findings:
  - {id: "A3-01", check: "F2", line: "s43 ln1265/ln1253; s40 ln1150", classification: "FORWARD-SIGNAL", implication: "Standalone PAT -47%/EBITDA -15% (Other Income -63%) masked by subs/associates; S-vs-C PAT gap widened to ~73% of standalone base"}
  - {id: "A3-02", check: "F2", line: "s40 ln1142-1143", classification: "AMBIGUOUS", implication: "Associate/JV share +86% = 17% of consol PAT with one unnamed loss-making associate; consol is unaudited"}
  - {id: "A3-03", check: "F6", line: "s27 ln773; s32 ln940; s37 ln1059/1069/1073", classification: "FORWARD-SIGNAL", implication: "Dense dated commissioning/capacity/civil-works commitments feed promise-vs-delivery and FTTCP timeline"}
  - {id: "A3-04", check: "F7", line: "s59 ln1729", classification: "AMBIGUOUS", implication: "Hedge subordinates the 2045/2030 decarbonization target to unstated contractual obligations"}
  - {id: "A3-05", check: "F8", line: "s45 ln1317", classification: "FORWARD-SIGNAL", implication: "PPGCL zero tax on 143 Cr PBT = DTA/carryforward; future ETR step-up risk"}
  - {id: "A3-06", check: "F8", line: "s44 ln1288", classification: "NEUTRAL-FACT", implication: "Maithon ETR normalising 12.6%->23.7%, a PAT headwind"}
  - {id: "A3-07", check: "F8", line: "s50 ln1474", classification: "FORWARD-SIGNAL", implication: "TP Solar ETR ~17.6% sub-statutory; normalisation is a latent drag as profit scales"}
  - {id: "A3-08", check: "F12", line: "s42 ln1232", classification: "AMBIGUOUS", implication: "Others (Tata Projects/Nelco) EBITDA 51->1, PAT loss (213)->(330) widening; likely the loss-making associate"}
  - {id: "A3-09", check: "F12", line: "s53 ln1556/ln1564", classification: "FORWARD-SIGNAL", implication: "Regulated assets accreting (TPDDL +35% YoY, consol +20%) = under-recovery/WC drag and true-up dependency"}
  - {id: "A3-10", check: "F12", line: "s47 ln1368", classification: "FORWARD-SIGNAL", implication: "Odisha AT&C losses worsening at 3/4 discoms and all above vesting targets; headline 26.7% masks trend"}
  - {id: "A3-11", check: "F12", line: "s42 ln1220", classification: "AMBIGUOUS", implication: "Renewables intra-segment EBITDA elimination swung +23->(216); rising captive/DCR module-profit elimination"}
  - {id: "A3-12", check: "F14", line: "s27 ln767 vs s36/37 ln1033/1035; s41 ln1196 vs s42 ln1238", classification: "NEUTRAL-FACT", implication: "Project-name spelling and reused footnote marker inconsistencies; cumulative drafting/governance datapoint"}
  - {id: "A3-13", check: "F16", line: "s41 ln1195 (+1237,1414,1443,1481)", classification: "AMBIGUOUS", implication: "Prior-period segment restatement (corporate-cost reallocation) re-bases all YoY/CAGR comparatives; quantum undisclosed"}
  - {id: "A3-14", check: "F16", line: "s23 ln642/643/626; s55 ln1618", classification: "FORWARD-SIGNAL", implication: "Net Debt/Underlying EBITDA 3.41 and D/E 1.25 rising 3rd year; +5,116 Cr net debt QoQ on record capex, framed positive"}
  - {id: "A3-15", check: "F16", line: "s30 ln876; s31 ln906/901", classification: "FORWARD-SIGNAL", implication: "3rd-party rooftop order book drawn down to 639 Cr, below quarterly intake and billing run-rate"}
  - {id: "A3-16", check: "F16", line: "ledger ln3/158", classification: "NEUTRAL-FACT", implication: "Dropped/reframed-metric detection blocked; re-run F16 once prior-quarter deck ledger available"}
  - {id: "A3-17", check: "F1", line: "s55 ln1615", classification: "NEUTRAL-FACT", implication: "Related Party Debt line dormant (nil vs 203 a year ago); watch for reappearance as related-party funding tell"}
forward_signals: ["A3-01", "A3-03", "A3-05", "A3-07", "A3-09", "A3-10", "A3-14", "A3-15"]
ambiguous: ["A3-02", "A3-04", "A3-08", "A3-11", "A3-13"]
commitments:
  - {commitment: "Deliver 2.5 GW RE capacity addition", implied_date: "FY2027", ref: "s27 ln773", status_word: "underway"}
  - {commitment: "Jalpura Khurja full commissioning", implied_date: "H1 FY2027", ref: "s32 ln940", status_word: "underway"}
  - {commitment: "Bikaner Transmission commissioning", implied_date: "FY2027", ref: "s32 ln934", status_word: "underway"}
  - {commitment: "MSEDCL 400MW Hybrid commissioning", implied_date: "FY2027", ref: "s28 ln793", status_word: "underway"}
  - {commitment: "Dorjilung main civil works package award", implied_date: "Q2 FY27", ref: "s37 ln1073", status_word: "scheduled"}
  - {commitment: "SJVN/NTPC/Mumbai DISCOM FDRE commissioning", implied_date: "FY2028", ref: "s28 ln793", status_word: "underway"}
  - {commitment: "Jejuri/Gopalpur/Paradeep TBCB commissioning", implied_date: "FY2028", ref: "s32 ln926", status_word: "underway"}
  - {commitment: "Khorlochhu HPP commissioning", implied_date: "FY2029", ref: "s37 ln1059", status_word: "initiated"}
  - {commitment: "Ryapte Transmission commissioning", implied_date: "FY2029", ref: "s32 ln922", status_word: "initiated"}
  - {commitment: "Dorjilung HPP commissioning", implied_date: "FY2032", ref: "s37 ln1069", status_word: "initiated"}
  - {commitment: "SJVN RTC 88MW PPA execution", implied_date: "24 months post PPA signing", ref: "s28 ln801", status_word: "pending"}
  - {commitment: "FY30E Revenue ~1,00,000 Cr / EBITDA ~30,000 Cr / PAT ~10,000 Cr / capacity >30 GW", implied_date: "FY2030", ref: "s7 ln129-152", status_word: "aspiration"}
  - {commitment: "Rooftop 30 lakh households / ~30,000 Cr cumulative revenue", implied_date: "2030", ref: "s30 ln876", status_word: "aspiration"}
  - {commitment: "DJSI EM 80/100; Clean&Green 70%; Net Zero", implied_date: "2027/2030/2045", ref: "s58 ln1710", status_word: "underway"}
gate_a3: pass
blank_checks: []
```
