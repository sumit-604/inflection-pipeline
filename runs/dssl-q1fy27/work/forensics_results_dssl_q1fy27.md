# A3 FORENSIC NOTES — Digitide Solutions Limited (DSSL), Q1 FY27, doctype: RESULTS (Reg 33 primary filing)

Source extract: `runs/dssl-q1fy27/work/extract_results_dssl_q1fy27.txt` (11 pages, 922 lines)
Ledger contract: `runs/dssl-q1fy27/work/ledger_results_dssl_q1fy27.md`
Ledger reconciliation: 100% — every row read verbatim at its cited line (N1-N12, C1-C36, S1-S21, T1-T24, Table-5 A1-A6/AGENDA/MTG/SIG, Table-6 AP1-AP11/SIG-AUD-C/S, Table-7 E1-E24, Table-8 SB1-SB5). No unread row.
Prior quarter: none (first quarterly run). Trend uses the in-filing comparative columns: 30 Jun 2026 (Q1FY27) / 31 Mar 2026 (Q4FY26) / 30 Jun 2025 (Q1FY26) / FY26 (year ended 31 Mar 2026).

RASTER CORRECTION (cited): consolidated **Paid-up equity share capital, 30 June 2026 = 1,491.10** per `runs/dssl-q1fy27/inputs/_pageimages/results_p05.png` (extract line 425 garble "1.4q1,11,"; ledger flagged "1,491.16(?)"). Corrected value is 1,491.10, IDENTICAL to standalone (T21, line 850). The ledger's suspected consol-vs-standalone paid-up mismatch dissolves — there is no mismatch. EPS renderings on the same raster confirm consol basic (0.13)/(0.85)/0.38/(1.10).

---

## FINDINGS TABLE

| id | check | ledger row | line | verbatim quote | classification | forward implication |
|----|-------|-----------|------|----------------|----------------|---------------------|
| DF1 | F1 | C10/S12/T10/T12/T13 | 293 / 786 / 799 | "Exceptional items (gain)/ loss (refer note 4) … -" (nil, Q1FY27 col) | FORWARD-SIGNAL | Demerger one-offs and the Q4FY26 Labour-Code past-service catch-up have run off (exceptional line nil this qtr), so the exceptional-items tailwind/headwind is gone. BUT New Labour Codes create an ONGOING service-cost run-rate (Note 4/5); past-service was only the catch-up — employee-benefit run-rate stays structurally elevated. |
| DF2 | F2 | C24/C25/C16 vs T16 | 375 / 380 / 820 | "Owners of the Company (18.91) … Non-controlling interests 48.24 … Profit for the period 29.33"; standalone "(Loss)… for the period (105.81)" | FORWARD-SIGNAL | The entire positive headline group PAT (29.33) is minority profit; owners' share is a LOSS (18.91) and the standalone parent lost (105.81). Owners flipped from +57.32 (Q1FY26) to (18.91). Public shareholders' economics (parent + owned-sub residual) are loss-making and deteriorating while minority-held subsidiaries carry the group. |
| DF3 | F3 | AP7 | 166-172 | "4 subsidiaries which have not been reviewed by their auditors … Nil revenue, total loss after tax of Rs. 2.26 million" | AMBIGUOUS | Four subsidiaries are dormant (nil revenue) yet retained in the perimeter and reviewed by no auditor, only management-certified. Dormant + unreviewed + management-certified = balance-sheet-cleanup / governance watch, not an operating driver. |
| DF4 | F4 | AP6/AP7 | 154-159 / 166-172 | "6 subsidiaries … total net profit after tax of Rs. 26.44 million … reviewed by other auditors" | AMBIGUOUS | 26.44/29.33 = 90.1% of consolidated PAT rests on component-auditor reports the principal statutory auditor did NOT review; a further (2.26) loss is management-certified only. With owners loss-making, essentially ALL reported group profit sits in subsidiaries outside the principal auditor's direct review — and the 6+4 entities are not individually named (info gap). No prior quarter to trend. |
| DF5 | F8 | C11/C15/C13 & T11/T14 | 299/321/311 / 791/808 | consol "Income tax relating to previous year 20.75"; standalone "Deferred tax (10.36)" on PBT "(95.45)" | FORWARD-SIGNAL | Consolidated ETR = 79.86/109.19 = 73.1% vs 25.17% statutory (FY26 82.4%, Q1FY26 51.5%) — structural: profitable subs fully taxed, parent losses generate no group-level tax benefit, so PAT is punitively tax-drained even when PBT positive. Non-zero prior-year tax credit +20.75 (F8 trigger). Standalone books a deferred-tax CHARGE (10.36) in a pre-tax LOSS quarter = NO DTA recognised on parent losses = management is not sheltering parent losses / doubts near-term parent taxable profit. |
| DF6 | F10 | C33/T21 (raster) | 425 (→p05) / 850 | "Paid-up equity share capital 1,491.10" (raster) vs Q4 "1,490.11", Q1FY26 "1,489.49" | AMBIGUOUS | Paid-up crept +0.99mn (~99,000 shares) QoQ and +1.61mn YoY with NO corporate action disclosed in the outcome letter (only agenda item 1). Basic=diluted in every period (loss-driven anti-dilution now), so no dilutive instruments yet in the count — but ESOS 2026 + newly-incorporated ESOP Trust foreshadow dilution once options are granted and profit returns. Source of the crept share count unexplained (info gap). |
| DF7 | F11 | C34 vs T22 | 431 / 856 | consol "Reserves i.e Other equity 6,891.08" vs standalone "7,500.49" | AMBIGUOUS | Consolidated owners' other equity (6,891.08) sits 609.41mn (8.1%) BELOW standalone other equity (7,500.49) — an inversion. Owned subsidiaries (net of NCI) have eroded owners' book value below the parent's standalone book. Candidate reconciling items: subsidiary accumulated losses attributable to owners, acquisition/goodwill adjustments, NCI carve-out. Reserves disclosed in annual column only — no quarterly roll-forward, no external (rating/slide) number to tie to (info gap). |
| DF8 | F12 | S4/S5/S14/S18/S20 | 489/494/541/563/573 | "Segment results — Business Process Management 760.00" (vs 914.08 Q1FY26); "Segment liabilities — Unallocated 3,045.47" (vs 1,543.84 Q1FY26) | FORWARD-SIGNAL | BPM result margin fell 17.0%→14.1% YoY (T&D 9.8%→8.0% YoY, 12.1%→8.0% QoQ). BPM segment assets +6.1% QoQ (12,991→13,783) while BPM liabilities −5.2% QoQ = increasingly internally/equity-funded asset build (capex/WC). Unallocated (corporate) liabilities nearly DOUBLED YoY (1,543.84→3,045.47) with consol finance costs +34.8% YoY (112.19→151.22) = rising corporate-level debt. Ties to the 9% EBITDA-margin tripwire and the ~Rs90cr PPE capital-intensity monitorable. |
| DF9 | F6 | N6/N12 | 618 / 914 | "incorporated the Digitide ESOP Trust on 18 April 2026 to administer the Employee Stock Option Scheme 2026 (ESOS 2026) and future employee benefit plans" | FORWARD-SIGNAL | Dated management commitment to run an ESOP scheme = future option grants = future dilution. Status: initiated (trust incorporated, "did not undertake any operations or transactions during the period"). Grant sizing/dilution not yet disclosed. |
| DF10 | F14 | E7/E15, E10/E22, N11 | 209 vs 639 / 215 vs 653 / 910 | "Allsectech Manila Inc., Philippiness" vs "Alldigi Tech Manila Inc., Philippines"; "Quess GTS Canada Holding" vs "Holdings"; standalone Note 5 "…in the statement of consolidated financial results" | AMBIGUOUS | Cumulative drafting/governance sloppiness: Manila subsidiary appears under two different legal-name strings within one filing (plus "Philippiness" typo); Canada entity Holding vs Holdings; standalone Note 5 mis-states the presentation is in the "consolidated" statement. Individually immaterial; cumulatively a control-quality data point (monitorable e). |
| DF11 | F15 | E12/E24 (and E7/E15) | 219 / 657 | "Digitide ESOP Trust (Effective from 18 April 2026)" | FORWARD-SIGNAL | New entity in the consolidation perimeter this quarter (first inclusion) — the ESOS 2026 vehicle (dilution catalyst). Separately, the Manila entity's "Allsectech"→"Alldigi Tech" name divergence between the two in-filing lists is consistent with a rebrand/rename in progress not yet uniformly reflected. |

---

## CHECKLIST SCORECARD (all 17; no blanks — GATE A3)

| # | Status | One-line basis |
|---|--------|----------------|
| F1 | FINDING | 5 ZERO_STANDING rows read; exceptional line nil this qtr = demerger + Labour-Code catch-up run off, but ongoing Labour-Code service cost persists (DF1). |
| F2 | FINDING | Headline PAT 29.33 is 100% NCI; owners LOSS (18.91), standalone LOSS (105.81); owners flipped from +57.32 YoY — S-vs-C gap moved >5pp (DF2). |
| F3 | FINDING | Cost lines (emp benefits 5,832.98 vs 3,650.50; D&A 551.76 vs 351.89) prove main subs OPERATE (not shells); but 4 nil-revenue unreviewed subs are dormant shells in perimeter (DF3). |
| F4 | FINDING | 90.1% of group PAT (26.44/29.33) reviewed only by OTHER auditors; 2.26mn loss management-certified; entities unnamed; >10% threshold breached (DF4). |
| F5 | N.A. | First quarterly run — no prior auditor report to verbatim-diff. Baseline captured below. Consolidated report carries NO Going Concern / Emphasis-of-Matter para; standalone carries none of the three. |
| F6 | FINDING | Lexicon hit: ESOP Trust "to administer … ESOS 2026 and future employee benefit plans" = dated dilution commitment, status initiated (DF9). "will be made available on website" / "is being filed" = routine, logged. |
| F7 | PASS | No pre-emptive hedge language (no "no assurance"/"evaluating"/"exploring"/"in discussions" on revenue lumpiness or customer concentration) in the minimal note set; "subjected to limited review" is descriptive, not a hedge. |
| F8 | FINDING | Consol ETR 73.1% vs 25.17% (structural, parent-loss non-shield); prior-year tax +20.75 (trigger); standalone deferred-tax CHARGE (10.36) in a loss quarter = no DTA on parent losses (DF5). |
| F9 | PASS | No single-quarter OCI component swing exceeds its full prior year: re-measurement (17.21) < FY26 61.80; FX (10.18) < 161.54; hedge 26.03 < 58.67. Cash-flow-hedge line newly active (nil Q1FY26 → live) — logged as watch, below threshold. |
| F10 | FINDING | Paid-up +0.99mn QoQ / +1.61mn YoY with no corporate action disclosed; basic=diluted all periods; ESOS 2026/ESOP Trust foreshadow dilution (DF6). Consol raster-corrected to 1,491.10. |
| F11 | FINDING | Consol owners' other equity 6,891.08 is 8.1% BELOW standalone 7,500.49 (609.41 inversion) = value erosion at owned subs; no external number / no quarterly roll-forward to tie (DF7). |
| F12 | FINDING | BPM result margin 17.0%→14.1% YoY; BPM assets +6.1% QoQ vs liabilities −5.2% (equity-funded build); unallocated liabilities doubled YoY 1,543.84→3,045.47 (corporate debt); T&D margin 12.1%→8.0% QoQ (DF8). |
| F13 | PASS | Sole agenda item = approval of Q1 results (Reg 33); no AR/MD&A, AGM notice, record date, dividend, director appointment/term, auditor change, ESOP-grant or capital-raise resolution. Consistent with a Q1 results-only outcome letter; no director term dates to map. WATCH: FY26 AR/AGM approval and any ESOS 2026 grant resolution not yet actioned — expect at next board outcome. |
| F14 | FINDING | Manila entity two name-strings ("Allsectech"/"Alldigi Tech", plus "Philippiness"); Canada "Holding"/"Holdings"; standalone Note 5 mis-references "consolidated" statement; Annexure/Appendix cross-ref drift (DF10). |
| F15 | FINDING | Both lists = same 12 entities; Digitide ESOP Trust NEW to perimeter (eff. 18 Apr 2026); Manila name divergence = possible rename in progress (DF11). |
| F16 | N.A. | Doctype = results; no presentation deck in scope. |
| F17 | N.A. | Doctype = results; no concall transcript in scope. Note: Reg-33 filing carries no balance sheet / cash flow, so monitorables (ECL Rs0.14cr, receivables ageing, CFO/PAT 0.529x, related-party advances, RMC meetings, Cybercons sub-vs-associate) are structurally absent here — silence audit deferred to the concall/AR, not a finding against this doctype. |

### F5 BASELINE (captured for next-quarter diff)
- Consolidated review report (Deloitte Haskins & Sells): UNMODIFIED conclusion (AP5, line 139); NO Going Concern paragraph; NO Emphasis of Matter. Other Matters = para 6 (line 154): 6 subs reviewed by other auditors, revenue Rs3,151.80mn / PAT Rs26.44mn / TCI Rs30.28mn, "conclusion … is not modified"; para 7 (line 166): 4 subs not reviewed by any auditor, Nil revenue / loss Rs2.26mn / TCL Rs2.05mn, "not material to the Group … conclusion … not modified."
- Standalone review report: UNMODIFIED conclusion (AP11, line 695); 4 paragraphs only; NO Other Matters / EoM / Going Concern.
- Diff these paragraphs verbatim next quarter; any new entity count, changed Rs amount, or new EoM/GC = F5 FINDING.

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/ref | status word |
|-----------|--------------|----------|-------------|
| Administer ESOS 2026 and "future employee benefit plans" via Digitide ESOP Trust (future option grants → dilution) | FY27 onward; trust effective 18 Apr 2026 | Note 5 consol (line 618) / Note 6 standalone (line 914) | initiated |
| File results + review report with BSE & NSE and publish on website | on/around 27 Jul 2026 | Note 2 consol (line 596) / Note 3 standalone (line 896); cover letter line 45-46 | underway |

---

## DECOMPOSITIONS (support for DF2 / DF5 / DF8)

Standalone-vs-consolidated, Q1FY27 (INR mn):
- Revenue: consol 7,750.72 − standalone 4,759.93 = 2,990.79 subsidiary revenue (38.6% of consol).
- PBT: consol 109.19 − standalone (95.45) = +204.64 subsidiary+elimination contribution to PBT.
- PAT: consol 29.33 − standalone (105.81) = +135.14 subsidiary contribution to PAT.
- Owners split: standalone loss (105.81) vs consolidated OWNERS loss (18.91) → owned subs (net of NCI) added +86.90 to owners, partially offsetting the parent loss; NCI (minority-held subs) separately earned +48.24.

Owners-vs-NCI trend (C24/C25): owners (18.91) / (126.96) / 57.32 / (163.50); NCI 48.24 / 76.91 / 39.61 / 218.95. Owners deteriorating (profit→loss YoY); NCI profitable and growing YoY.

Consolidated ETR: Q1FY27 73.1%, Q1FY26 51.5%, FY26 82.4% — all far above 25.17% statutory (Q4FY26 N/M on negative PBT).

Segment margins: BPM 14.1% (Q1FY27) / 16.3% (Q4) / 17.0% (Q1FY26); T&D 8.0% / 12.1% / 9.8%.

---

## FOR A4 (convert to management questions) — every FORWARD-SIGNAL and AMBIGUOUS finding
- DF1 (F1): Now that past-service catch-up is booked, what is the recurring FY27 Labour-Code service-cost run-rate in employee benefits?
- DF2 (F2): Why is the entire group PAT minority profit while owners and the standalone parent are loss-making, and when do owners' economics turn?
- DF3 (F3): Name the 4 nil-revenue unreviewed subsidiaries; why retained; wind-down plan?
- DF4 (F4): Identify the 6 other-auditor-reviewed subsidiaries carrying 90% of group PAT; confirm no principal-auditor scope concern.
- DF5 (F8): Why a deferred-tax charge on a standalone loss (no DTA)? Does management doubt near-term parent taxable profit? Sustainable group ETR guidance?
- DF6 (F10): Source of the +0.99mn QoQ paid-up increase (no corporate action disclosed); expected ESOS 2026 grant size and dilution.
- DF7 (F11): Reconcile consolidated owners' reserves being below standalone reserves — which subsidiaries carry accumulated losses / acquisition write-downs?
- DF8 (F12): BPM/T&D margin compression drivers; BPM equity-funded asset build (external funding need?); why unallocated corporate liabilities doubled YoY.
- DF9 (F6): ESOS 2026 grant timeline and dilution schedule.
- DF10 (F14): Confirm correct legal name of the Manila entity (Allsectech vs Alldigi Tech) — rename in progress?
- DF11 (F15): Confirm ESOP Trust perimeter treatment; status of the Manila entity rename.

---

```yaml
stage: A3-forensics
company: "DSSL"
quarter: "Q1 FY27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "runs/dssl-q1fy27/work/forensics_results_dssl_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: FINDING
  F3: FINDING
  F4: FINDING
  F5: N.A.
  F6: FINDING
  F7: PASS
  F8: FINDING
  F9: PASS
  F10: FINDING
  F11: FINDING
  F12: FINDING
  F13: PASS
  F14: FINDING
  F15: FINDING
  F16: N.A.
  F17: N.A.
findings:
  - {id: "DF1", check: "F1", line: "293/786/799", classification: "FORWARD-SIGNAL", implication: "Exceptional line nil = demerger/Labour-Code catch-up run off; ongoing Labour-Code service cost keeps employee-benefit run-rate elevated"}
  - {id: "DF2", check: "F2", line: "375/380/820", classification: "FORWARD-SIGNAL", implication: "Headline PAT 29.33 is 100% NCI; owners loss (18.91) and standalone loss (105.81); owners flipped from +57.32 YoY"}
  - {id: "DF3", check: "F3", line: "166-172", classification: "AMBIGUOUS", implication: "4 nil-revenue unreviewed dormant subs retained in perimeter, management-certified"}
  - {id: "DF4", check: "F4", line: "154-159/166-172", classification: "AMBIGUOUS", implication: "90.1% of group PAT reviewed only by other auditors; 2.26mn loss management-certified; entities unnamed"}
  - {id: "DF5", check: "F8", line: "299/321/311/791/808", classification: "FORWARD-SIGNAL", implication: "Consol ETR 73% vs 25.17% (parent-loss non-shield); prior-year tax +20.75; standalone deferred-tax charge on a loss = no DTA"}
  - {id: "DF6", check: "F10", line: "425/850", classification: "AMBIGUOUS", implication: "Paid-up +0.99mn QoQ, no corporate action disclosed; ESOS 2026/ESOP Trust foreshadow dilution"}
  - {id: "DF7", check: "F11", line: "431/856", classification: "AMBIGUOUS", implication: "Consol owners' other equity 6,891.08 is 8.1% below standalone 7,500.49 = value erosion at owned subs"}
  - {id: "DF8", check: "F12", line: "489/494/541/563/573", classification: "FORWARD-SIGNAL", implication: "BPM margin 17.0->14.1% YoY; BPM equity-funded asset build; unallocated corporate liabilities doubled YoY; T&D margin 12.1->8.0% QoQ"}
  - {id: "DF9", check: "F6", line: "618/914", classification: "FORWARD-SIGNAL", implication: "ESOS 2026 / future employee benefit plans = future dilution; status initiated"}
  - {id: "DF10", check: "F14", line: "209/639/215/653/910", classification: "AMBIGUOUS", implication: "Cumulative drafting inconsistencies: Manila name variants, Holding/Holdings, standalone note mis-references consolidated statement"}
  - {id: "DF11", check: "F15", line: "219/657", classification: "FORWARD-SIGNAL", implication: "Digitide ESOP Trust new to perimeter (dilution vehicle); Manila entity rename apparently in progress"}
forward_signals: ["DF1", "DF2", "DF5", "DF8", "DF9", "DF11"]
ambiguous: ["DF3", "DF4", "DF6", "DF7", "DF10"]
commitments:
  - {commitment: "Administer ESOS 2026 and future employee benefit plans via Digitide ESOP Trust (future option grants -> dilution)", implied_date: "FY27 onward; trust effective 18 Apr 2026", ref: "Note 5 consol line 618 / Note 6 standalone line 914", status_word: "initiated"}
  - {commitment: "File results + review report with BSE & NSE and publish on website", implied_date: "on/around 27 Jul 2026", ref: "Note 2 consol line 596 / Note 3 standalone line 896", status_word: "underway"}
gate_a3: pass
blank_checks: []
```
