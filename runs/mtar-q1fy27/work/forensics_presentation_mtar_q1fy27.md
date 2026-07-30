# A3 FORENSIC NOTES — MTAR Technologies Limited — Q1 FY27 — DOCTYPE: presentation (32-slide investor deck, July 2026)

Model: claude-opus-4-8 | Ledger reconciled: 100% (32 slides, 535 numbers, 7 footnotes, 9 ZERO_STANDING rows all read verbatim at cited lines)
Cross-document reconciliation performed against: results filing (consolidated, INR millions x0.1) and press release (Rs Cr).
Basis: deck is CONSOLIDATED (slide 12 "Q1FY27 Consolidated P&L", slide 25 "Historical Consolidated P&L"); results filing confirms Group = MTAR + Gee Pee Aerospace + Magnatar Aero Systems.

---

## CROSS-DOCUMENT HEADLINE RECONCILIATION (under F14, extended) — CLEAN

Deck Q1FY27 (slide 11/12) vs results filing consolidated (page 6, 30-Jun-26, x0.1) vs press release (page 2):

| Metric | Deck (S11/S12) | Results filing (x0.1) | Press release | Tie |
|---|---|---|---|---|
| Revenue from Operations | 360.7 | 3,607.21 → 360.7 | 360.7 | ✓ |
| Gross Profit | 164.2 | 3,607.21−(2,043.19−78.16)=1,642.18 → 164.2 | — | ✓ |
| EBITDA | 85.1 (23.6%) | 1,642.18−465.20−326.44=850.54 → 85.1 (23.6%) | 85.1 | ✓ |
| PBT | 67.4 | 674.02 → 67.4 | 67.4 | ✓ |
| Total Tax | 17.2 | 171.75 → 17.2 | — | ✓ |
| PAT | 50.2 (13.9%) | 502.27 → 50.2 | 50.2 | ✓ |
| Other income | 7.9 | 78.87 → 7.9 | — | ✓ |
| D&A | 9.7 | 96.92 → 9.7 | — | ✓ |
| Finance cost | 15.8 | 158.47 → 15.8 | — | ✓ |
| YoY / QoQ % | 130.4% / 17.9% rev | — | 130.4% / 17.9% | ✓ |

All headline values reconcile to the paise across all three documents. The ONLY break is a column-HEADER label (see F-07), not a value. FY26 also ties: deck PAT 94.0 = results year-ended 940.30m→94.0 (note: Notion FY26 PAT baseline "₹98 Cr" is ~4 Cr above the filed 94.0 consolidated / 95.3 standalone — Notion baseline slightly stale, not a deck defect). EPS: results basic=diluted 16.33 = PAT 50.2/3.0759 Cr shares → no dilution.

---

## FINDINGS TABLE

| id | check | ledger row / source | line/slide | verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| F-01 | F1 | S26 r3/r5/r11, S27 r3/r5/r11 | S26 L727,L734 / S27 L750,L753,L760 | "Right-of-use assets 15.0 0.0 0.0 0.0"; "(i) Investments 0.0 0.0 0.0 0.0" | AMBIGUOUS | ROU asset + lease liabilities go nil→live at Mar-26 (ROU 15.0; lease liab 6.7+0.6) = a leasing arrangement first capitalised FY26 — confirm whether it is the greenfield O&G/fuel-cell facility. Investments permanently nil = no strategic equity stakes. Exceptional Items standing line used once (FY26 3.8 = one-time Labour Codes, non-recurring). Current mutual-fund investment jumps 0→215.3 (cash parked). |
| F-02 | F6 | commitment cluster (register below) | S4 L100, S7 L180, S21 L610-611 | "expected to be commissioned by Q3 FY 27"; "will be completed at the new facility by March 2027"; "expecting Rs. 150 Cr of orders in FY 27" | FORWARD-SIGNAL | 16 dated/dateable management commitments mined; feed Role 5 promise-vs-delivery tracker and FTTCP catalyst timeline. |
| F-03 | F10 | S31 r Promoters | S31 L900-902 | "Promoters 31.41% 30.59% 30.44% 29.35%"; "FIIs 9.21% 12.24% 17.31% 24.80%" | FORWARD-SIGNAL | Promoter stake declining ~1pp/quarter (−1.09pp QoQ to Jun-26); now 29.35%, below Notion Mar-26 baseline 30.44%, trending toward tripwire <25%. FII stake nearly tripled (9.21→24.80%). No share-count dilution (paid-up flat 30.8; basic=diluted EPS). |
| F-04 | F12 | S7 revenue+share | S7 L162, L178 | "1%" (Q1FY27 nuclear share); "single largest order inflow of Rs. 504 Cr for the kaiga 5 & 6 projects" | AMBIGUOUS | Civil-Nuclear revenue collapsed to Rs 3.2 Cr / 1% of Q1FY27 (was 8-11% FY23-24) DESPITE the Rs 504 Cr Kaiga order — order sits in backlog, not yet converting; nuclear revenue-timing risk. |
| F-05 | F12 | S10 revenue+share | S10 L265 | "4% 19% 22% 15% 28%" | AMBIGUOUS | "Products & Others" share spiked to 28% (Rs 100.4 Cr) in Q1FY27 from 15% FY26 — largest-ever share; driver undisclosed (import-substitutes / data-centre?), margin and durability of this mix shift unknown. |
| F-06 | F12 | S9 revenue+order book | S9 L230, L249 | "77% 61% 62% 70% 61%"; "robust closing order book of Rs. 3431 Cr in Clean Energy by end of Q1 FY 27" | FORWARD-SIGNAL | Clean-Energy/Fuel-Cell (Bloom) bucket = 61% / Rs 220.8 Cr Q1FY27 (annualises ~883 vs FY26 615.4); order book Rs 3,431 Cr. Bloom monitorable positive on the REVENUE proxy; hot-box unit counts NOT disclosed. |
| F-07 | F14 | S12 header | S12 L333 vs S11 L308 | "Q1 FY27  Q4 FY25  Y-o-Y  Q4 FY26" | NEUTRAL-FACT | Slide-12 comparative column headed "Q4 FY25" but every value (156.6, 28.4, 14.8, 10.8) = slide-11 "Q1 FY26" and = press-release Q1FY26 and = results 30-Jun-25 (1,565.84m→156.6). Confirmed header typo; column IS Q1 FY26. YoY %s themselves correct. |
| F-08 | F14 | S29 r PAT vs S25 r17/r18 | S29 L816 vs S25 L714 | "56.1 53.4" (S29 FY25 PAT) vs "Profit for the year ... 52.9" (S25 FY25) | NEUTRAL-FACT | Deck disagrees with itself on FY25 PAT: 53.4 (7.8% margin, S29) vs 52.9 (7.9%, S25). Immaterial 0.5 Cr; no FY25 in results filing to arbitrate; verify at Annual Report. |
| F-09 | F16 | S4 guidance | S4 L100 | "we have guided for revenue growth of 80%, with an EBITDA margin of 24% ±100 bps" | FORWARD-SIGNAL | Guidance RAISED vs Notion May-26 record (50% revenue growth; 24% margin by FY28): FY27 revenue-growth guide now 80%, and 24% EBITDA margin pulled forward to the current fiscal. FY26 rev 876.2 → implied FY27 ~1,577 Cr. |
| F-10 | F16 | S13 order book waterfall + F3 footnote | S13 L361-385, footnote L383 | "Sales restated at order book excluding forex fluctuations, price escalations and scrap sales"; "highest order inflow ever achieved in a single quarter" | FORWARD-SIGNAL | Closing order book Rs 5,143.3 Cr (30-Jun-26) ≈ 2x Notion Q3FY26 baseline 2,582; Q1 inflow Rs 2,895.1 Cr. DEFINITION_WATCH: book is "restated" (net of forex/escalation/scrap); gross-vs-net-of-GST and executed-vs-pending basis NOT stated; a THIRD distinct inflow figure (FY26 full-year 2,453.3 Cr, L385) not obviously reconcilable to the 2,581.9 opening or 2,895.1 Q1 figures. |
| F-11 | F16 | S21 commissioning | S21 L611 | "The facility is expected to be commissioned by Q3 FY 27" | AMBIGUOUS | Weatherford/O&G greenfield commissioning guided Q3 FY27 (Oct-Dec 2026) vs Notion expectation Jun-Sep 2026 (Q2 FY27) = possible ~1-quarter SLIP; FY27 O&G revenue contribution not quantified. |
| F-12 | F16 | S7-S10 verticals vs results note | S9/S10 charts vs results L439 | results: "business activity falls within a single line of business segment in terms of Ind AS 108" | NEUTRAL-FACT (DEFINITION_WATCH) | The 4 vertical revenue splits in the deck are VOLUNTARY, unaudited management disclosure — statutorily MTAR is a SINGLE Ind AS 108 segment. No segment ASSETS/LIABILITIES disclosed by vertical anywhere, so F12's balance-sheet-by-segment forensics is not answerable; only vertical revenue trend is. |
| F-13 | F16 | S14 WC-days chart + S26 r16 | S14 L397-419, S26 L739 | "59" (Jun-26 total WC days); "Other Current Liabilities 254.9 44.5 31.9 46.6" | AMBIGUOUS | Total NWC days crashed 274 (Sep-25) → 59 (Jun-26); improvement partly advance-funded (Other Current Liabilities +Rs 210 Cr to 254.9 at Mar-26 = likely customer advances on the record order inflow). WC<200 monitorable MET, but is the collapse structural or advance/quarter-end-timing driven? |

---

## CHECKLIST SCORECARD (all 17; exactly one status each — GATE A3)

| # | Status | Basis (one line) |
|---|---|---|
| F1 | FINDING | 9 ZERO_STANDING lines read; ROU/lease liabilities nil→live at Mar-26 and MF-investment 0→215.3 are real events (F-01); Investments permanently nil = template. |
| F2 | PASS | Deck is consolidated; S-vs-C gap from results filing = standalone PAT 50.50 vs consol 50.23 (<1% of PAT, well under 5pp); subsidiary drag immaterial (Gee Pee+Magnatar net loss Rs 0.72 Cr). |
| F3 | N.A. | Deck carries no standalone lines; shell test needs S-vs-C cost split (results-filing scope). Note: results shows subsidiaries have Rs 1.68 Cr revenue + Rs 0.72 Cr net loss = near-shell, not pure shell; NCLT merger scheme filed to fold both into holdco. |
| F4 | N.A. | No auditor "Other Matters" ratio in the deck. Note: results auditor letter — 2 subsidiaries reviewed by other auditors, net loss Rs 0.72 Cr <1% of PAT (below 10% threshold). |
| F5 | N.A. | No going-concern / EoM paragraph in a presentation; no prior-quarter deck for verbatim diff. |
| F6 | FINDING | 16 dated/dateable commitments mined (register below); key: Weatherford commissioning Q3FY27, Phase-3 Mar-2027, Rs150Cr refurb FY27, 80%/24% guidance. |
| F7 | PASS | Only boilerplate Safe-Harbor hedges (slide 2: "no representation or warranty", "subject to known and unknown risks", "assumes no obligation to update"); no NEW pre-emptive hedge on revenue lumpiness or customer concentration added at note level. |
| F8 | N.A. | Deck carries only aggregate Total Tax Expense; ETR sanity-checked ~25-26% every period (Q1FY27 17.2/67.4=25.5%), unremarkable vs 25.17%. No deferred-tax sign or earlier-year adjustment in deck. Note for results-A3: filing shows non-zero "Adjustment of tax relating to earlier periods (8.26)m" in Q4FY26/FY26 = an F8 trigger in that doc. |
| F9 | N.A. | No OCI actuarial series in the deck. Note: results shows OCI (3.61)m in Q4FY26 only, immaterial. |
| F10 | FINDING | No dilution (paid-up 30.8 flat all periods; basic=diluted EPS 16.33 per results) — but shareholding pattern shows promoter stake decline to 29.35% and FII surge to 24.80% (F-03). |
| F11 | PASS | Other Equity 791.8 + Equity Share Capital 30.8 = Total Equity 822.6 (ties exactly, S26); ties to results consol Other equity 7,918.28m→791.8 & paid-up 307.59m→30.8; BVPS 822.6/3.0759=267.4 ≈ Notion 268. |
| F12 | FINDING | Vertical mix shifts: nuclear collapse to 1% (F-04), Products spike to 28% (F-05), Clean-Energy 61%/order book 3,431 Cr (F-06); statutory single-segment caveat (F-12). |
| F13 | N.A. | Presentation carries no board-outcome section. Note (from cross-doc results filing) for A4: AGM 28-Sep-2026; Directors' Report/MD&A/BRSR approved (full AR imminent → schedule AR deep-dive); Rohith Loka Reddy (DIN 06464331) & Anushman Reddy (DIN 08104131) re-appointed retiring-by-rotation; NCLT merger scheme for Gee Pee + Magnatar. |
| F14 | FINDING | Slide-12 column mislabelled "Q4 FY25" (F-07, resolved via cross-doc to Q1FY26); slide-25/29 FY25 PAT discrepancy 52.9 vs 53.4 (F-08); minor: "EBIDTA" typo S11 L295, "Intangibles Assets" S27. Cross-doc HEADLINE reconciliation itself = clean. |
| F15 | N.A. | Deck carries no consolidation entity list; entity diff needs prior quarter (none — first run). Note: results names 2 subsidiaries + NCLT merger (see F13). |
| F16 | FINDING | Guidance raised 50→80% (F-09); order-book definition-watch + doubling to 5,143.3 Cr (F-10); Weatherford Q3FY27 slip (F-11); statutory single-segment vs 4-vertical framing (F-12); WC-days advance-funded collapse (F-13); OCR "55 vs 45 Years" tagline artifact (slide 24, non-substantive). No prior deck ⇒ cross-deck diff N.A. |
| F17 | N.A. | No concall transcript supplied; silence audit not runnable. Monitorable coverage captured in MONITORABLE RESOLUTION table instead (deck silent on: hot-box unit counts, Bloom backlog YoY, Bloom second-source SOFC). |

GATE A3: pass (17/17 marked, no blanks).

---

## COMMITMENT REGISTER (from F6)

| # | Commitment | Implied date | Slide/line | Status word |
|---|---|---|---|---|
| 1 | FY27 revenue growth of 80% | FY27 | S4 L100 | guided |
| 2 | FY27 EBITDA margin 24% ±100 bps | FY27 | S4 L100 | guided |
| 3 | Rs 150 Cr refurbishment orders | FY27 | S7 L180 | expecting |
| 4 | Significant orders from Mahi Banswara (NTPC-NPCIL, 4 reactors) | going forward | S7 L182 | expected |
| 5 | Weatherford/O&G + Phase-2 CE greenfield facility commissioning | Q3 FY27 | S21 L611 | expected to be commissioned / in process |
| 6 | Phase-3 Clean Energy fuel-cell capacity | March 2027 | S21 L610 | will be completed |
| 7 | MNC Aerospace volume ramp-up (first-article → volume) | coming years | S8 L216 | poised / transition underway |
| 8 | LCA Tejas Mark IA actuator assemblies | — | S19 L567 | significant orders expected |
| 9 | Fuselage Door Assembly (structural) | — | S19 L563 | declared L1 |
| 10 | AMCA Main Landing Gear Support Structure Test Box | received | S19 L562 | received order |
| 11 | Z Adapter for Thales Alenia Space | done | S19 L556 | successfully completed |
| 12 | Storage boxes volume production | — | S19 L551 | underway |
| 13 | MNC engine components / sub-assemblies volume production | — | S19 L545 | in progress |
| 14 | SLB data-centre follow-on orders (post-qualification) | — | S9 L252 | robust orders expected |
| 15 | Data-centre infrastructure first articles | — | S5 L131 | under progress |
| 16 | AMCA Main Landing Gear Support Structure (development) | — | S5 L122 | currently engaged / underway |

Status-transition candidates for next quarter (Role 5 tracker): #5 "expected to be commissioned by Q3 FY27" → watch for "commissioned"; #6 "will be completed by March 2027"; #9 "L1" → watch for "received order"; #12/#13 "underway/in progress" → watch for "completed / volume ramp".

---

## MONITORABLE RESOLUTION (Notion monitorables & tripwires → deck reading)

| # | Monitorable / Tripwire | Notion baseline | Deck reading (slide cite) | Verdict |
|---|---|---|---|---|
| 1 | Bloom / Clean-Energy revenue + hot-box ramp | 12k hot-box Mar-26 → 20k Dec-26; track CE revenue | CE Fuel-Cell revenue Rs 220.8 Cr (61%), annualises ~883 vs FY26 615.4; CE order book Rs 3,431 Cr (S9 L230, L249) | REVENUE proxy STRONG (FORWARD-SIGNAL); hot-box UNIT counts SILENT |
| 2 | Civil nuclear Kaiga 5&6 PO ~Rs 500 Cr | ~Rs 500 Cr | "single largest order inflow of Rs. 504 Cr for the kaiga 5 & 6 projects" + Rs 150 Cr refurb expected FY27 (S7 L178-180) | MET (Rs 504 Cr received); but nuclear REVENUE only 3.2 Cr / 1% — backlog not converting (F-04) |
| 3 | Weatherford O&G commissioning + FY27 contribution | Jun-Sep 2026 (Q2 FY27) | "expected to be commissioned by Q3 FY 27"; whipstock first articles delivered (S21 L611, S5 L130) | ~1-QUARTER SLIP (Q2→Q3 FY27); contribution unquantified (F-11) |
| 4 | EBITDA margin sustains Q3FY26 ~23% | ~23% | Q1FY27 EBITDA margin 23.6% (S11/S12 L342) | MET (23.6%; recovered from Q4FY26 20.2%; matches 24% guide) |
| 5 | WC days < 200 | <200 in FY27 | Total NWC days 59 at Jun-26 (S14 L397-419) | MET (59) — but advance-funded, sustainability question (F-13) |
| 6 | Order book total | Q3FY26 Rs 2,582 Cr (highest ever) | Closing Rs 5,143.3 Cr (30-Jun-26); Q1 inflow Rs 2,895.1 Cr "highest ever" (S13 L361-385) | ~2x baseline — STRONG (FORWARD-SIGNAL); definition-watch (F-10) |
| 7 | Net debt / D-E | D/E 0.46x, net debt ~Rs 370 Cr | D/E Mar-26 0.45 (S30 L848); gross debt 369.3 Cr (147.7 NC + 221.6 C); current borrowings 2.3x YoY (S26 L726,L733) | Leverage RISING (0.24→0.45); WC/order build debt-funded |
| 8 | ROCE | tripwire <15% for 2 yrs post-FY28 | RoCE Mar-26 17.2% (S30 L853); FY25 was 11.4% (S30 L859) | Above 15% (17.2%); FY25 dip <15% noted, recovered FY26 |
| 9 | Promoter stake (tripwire <25%) | baseline 30.44% (Mar-26) | Jun-26 29.35% (S31 L900) | NOT breached; DECLINING −1.09pp QoQ, below baseline (F-03) |
| 10 | Bloom backlog growth <20% YoY for 2Q (tripwire) | — | CE order book Rs 3,431 Cr (S9 L249); no prior-quarter figure in deck | CANNOT COMPUTE from deck (no prior deck); revenue growth strong |
| 11 | Bloom second-source SOFC (tripwire) | — | not mentioned anywhere | SILENT |
| 12 | FY27 guidance | 50% rev growth (May-26) | 80% rev growth + 24% EBITDA margin (S4 L100) | RAISED to 80% (F-09) |

Deck SILENCES (feed A4 questions / next-quarter F17 baseline): Bloom hot-box unit counts; Bloom backlog YoY %; second-source SOFC; KMP SEBI insider-trading matter (Feb-26, Notion risk) — not addressed; US tariff / export-concentration risk — export share disclosed (19% Q1FY27, S13) but tariff risk not discussed.

---

```yaml
stage: A3-forensics
company: "MTAR"
quarter: "Q1 FY27"
doctype: "presentation"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/mtar-q1fy27/work/forensics_presentation_mtar_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: PASS
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: PASS
  F8: N.A.
  F9: N.A.
  F10: FINDING
  F11: PASS
  F12: FINDING
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: N.A.
findings:
  - {id: "F-01", check: "F1", line: "S26 L727/L734; S27 L750/L753/L760", classification: "AMBIGUOUS", implication: "ROU asset & lease liabilities nil->live at Mar-26 = leasing event capitalised FY26; confirm if greenfield facility. Investments permanently nil; MF investment 0->215.3."}
  - {id: "F-02", check: "F6", line: "S4 L100; S7 L180; S21 L610-611", classification: "FORWARD-SIGNAL", implication: "16 dated commitments mined -> Role 5 promise-vs-delivery + FTTCP catalyst timeline."}
  - {id: "F-03", check: "F10", line: "S31 L900-902", classification: "FORWARD-SIGNAL", implication: "Promoter stake declining -1.09pp QoQ to 29.35%, below Notion baseline 30.44%, trending toward <25% tripwire; FII surge 9.21->24.80%. No share dilution."}
  - {id: "F-04", check: "F12", line: "S7 L162/L178", classification: "AMBIGUOUS", implication: "Civil-Nuclear revenue collapsed to 1% (Rs 3.2 Cr) despite Rs 504 Cr Kaiga order in backlog; revenue-timing risk."}
  - {id: "F-05", check: "F12", line: "S10 L265", classification: "AMBIGUOUS", implication: "Products & Others share spiked to 28% (Rs 100.4 Cr) from 15% FY26; driver/margin/durability unknown."}
  - {id: "F-06", check: "F12", line: "S9 L230/L249", classification: "FORWARD-SIGNAL", implication: "Clean-Energy/Bloom 61%/Rs 220.8 Cr, order book Rs 3,431 Cr; revenue proxy strong; hot-box units not disclosed."}
  - {id: "F-07", check: "F14", line: "S12 L333 vs S11 L308", classification: "NEUTRAL-FACT", implication: "Slide-12 column mislabelled 'Q4 FY25'; values = Q1 FY26 (confirmed via press release + results). Header typo only."}
  - {id: "F-08", check: "F14", line: "S29 L816 vs S25 L714", classification: "NEUTRAL-FACT", implication: "FY25 PAT self-disagrees 52.9 vs 53.4 (0.5 Cr); verify at AR."}
  - {id: "F-09", check: "F16", line: "S4 L100", classification: "FORWARD-SIGNAL", implication: "Guidance RAISED: FY27 revenue growth 50%->80%, 24% EBITDA margin pulled forward to FY27."}
  - {id: "F-10", check: "F16", line: "S13 L361-385", classification: "FORWARD-SIGNAL", implication: "Order book Rs 5,143.3 Cr (~2x Notion 2,582); Q1 inflow Rs 2,895.1 Cr; DEFINITION_WATCH on 'restated' basis / gross-vs-net-of-GST / executed-vs-pending; 3rd inflow figure 2,453.3 unreconciled."}
  - {id: "F-11", check: "F16", line: "S21 L611", classification: "AMBIGUOUS", implication: "Weatherford commissioning guided Q3 FY27 vs Notion Jun-Sep 2026 = ~1-quarter slip; FY27 contribution unquantified."}
  - {id: "F-12", check: "F16", line: "S9/S10 charts vs results L439", classification: "NEUTRAL-FACT", implication: "4-vertical split is voluntary/unaudited; statutory single Ind AS 108 segment; no segment assets/liabilities disclosed."}
  - {id: "F-13", check: "F16", line: "S14 L397-419; S26 L739", classification: "AMBIGUOUS", implication: "NWC days 274->59; improvement partly advance-funded (Other Curr Liab +210 Cr to 254.9); structural vs timing question."}
forward_signals: ["F-02", "F-03", "F-06", "F-09", "F-10"]
ambiguous: ["F-01", "F-04", "F-05", "F-11", "F-13"]
commitments:
  - {commitment: "FY27 revenue growth of 80%", implied_date: "FY27", ref: "S4 L100", status_word: "guided"}
  - {commitment: "FY27 EBITDA margin 24% +/-100bps", implied_date: "FY27", ref: "S4 L100", status_word: "guided"}
  - {commitment: "Rs 150 Cr refurbishment orders", implied_date: "FY27", ref: "S7 L180", status_word: "expecting"}
  - {commitment: "Mahi Banswara 4-reactor orders (NTPC-NPCIL)", implied_date: "going forward", ref: "S7 L182", status_word: "expected"}
  - {commitment: "Weatherford/O&G + Phase-2 CE facility commissioning", implied_date: "Q3 FY27", ref: "S21 L611", status_word: "in process"}
  - {commitment: "Phase-3 Clean Energy fuel-cell capacity", implied_date: "March 2027", ref: "S21 L610", status_word: "will be completed"}
  - {commitment: "MNC Aerospace volume ramp-up", implied_date: "coming years", ref: "S8 L216", status_word: "underway"}
  - {commitment: "LCA Tejas Mark IA actuator orders", implied_date: "", ref: "S19 L567", status_word: "expected"}
  - {commitment: "Fuselage Door Assembly", implied_date: "", ref: "S19 L563", status_word: "declared L1"}
  - {commitment: "AMCA Main Landing Gear Test Box order", implied_date: "received", ref: "S19 L562", status_word: "received"}
  - {commitment: "Z Adapter for Thales", implied_date: "done", ref: "S19 L556", status_word: "completed"}
  - {commitment: "Storage boxes volume production", implied_date: "", ref: "S19 L551", status_word: "underway"}
  - {commitment: "MNC engine components volume production", implied_date: "", ref: "S19 L545", status_word: "in progress"}
  - {commitment: "SLB data-centre follow-on orders", implied_date: "", ref: "S9 L252", status_word: "expected"}
  - {commitment: "Data-centre infra first articles", implied_date: "", ref: "S5 L131", status_word: "under progress"}
  - {commitment: "AMCA Main Landing Gear development", implied_date: "", ref: "S5 L122", status_word: "underway"}
gate_a3: pass
blank_checks: []
```
