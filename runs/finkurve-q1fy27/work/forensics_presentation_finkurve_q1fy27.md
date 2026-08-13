# A3 FORENSIC NOTES — Finkurve Financial Services Ltd (Arvog) — Q1 FY27 — DOCTYPE: PRESENTATION (Analyst/Institutional Investor Meet deck, 37 slides)

Primary document: `extract_presentation_finkurve_q1fy27.txt` (A1 extract; embedded body lines 1-1100).
Reconciliation contract: `ledger_presentation_finkurve_q1fy27.md` (A2; 253 numeric rows, 7 zero_standing, 5 footnotes, 78 entities, 1 guidance statement).
Cross-doc: `extract_results_finkurve_q1fy27.txt` / `ledger_results_finkurve_q1fy27.md` (Reg 33 results filing, Rs in Lakhs; x0.01 -> Cr).

Line-number convention: all deck cites use the extract's OWN embedded body line numbers (field 1 of each body line, 1-1100), matching the A2 ledger. Results-filing cites use the results ledger's file-line numbers.

Ledger reconciliation: every A2 ledger row (Sections A-G, all 253 numeric rows + zero-standing + footnotes + entities + KPI cross-ref) was read verbatim at its cited line in the A1 extract before judging. Reconciled 100%.

Doctype applicability note: F2, F3, F4, F5, F9, F13, F15, F17 are marked N.A. with basis (a marketing deck carries no consolidation columns, no auditor Other-Matters/EoM paragraphs, no statutory segment table, no board-resolution list, no prior-quarter deck to diff, and no concall transcript). F1, F6, F7, F8, F10, F11, F12, F14, F16 are live and adjudicated.

---

## CROSS-DOC RECONCILIATION (deck KPI vs filed KPI) — done first, per task CROSS-DOC mandate

| KPI | Deck value (line) | Filed value (results line) | Verdict |
|---|---|---|---|
| Interest income Q1FY27 | 74.79 Cr (930/931) | 7,478.68 L = 74.79 Cr (288) | MATCH |
| Total revenue from ops Q1FY27 | 75.10 Cr (934) | 7,510.30 L = 75.10 Cr (291) | MATCH |
| PAT Q1FY27 | 8.44 Cr (947) / 8.4 (186) | 843.81 L = 8.44 Cr (305) | MATCH |
| Net Worth Q1FY27 | 354.4 Cr (188) | 35,436.80 L = 354.37 Cr (365) | MATCH |
| Debt/Equity Q1FY27 | 2.88x (184, 915) | 2.88 (360) | MATCH |
| NNPA % Q1FY27 | 0.48% (190) | 0.48% (383) | MATCH |
| GNPA % Q1FY27 | NOT in headline; chart only, ambiguous (769-774) | 0.54% (381) | **DIVERGENCE (omission)** -> F16-6 |
| Off-book AUM quantum | never quantified; footnote only (191,762,815,855,892) | CLA outstanding 37.86 Cr (results 337) | **DIVERGENCE (undisclosed split)** -> F16-2 |
| Deferred tax (net) | Mar'26 DTL 1.87 Cr (997) | Jun'26 Appendix-I DTL 2,325.74 L = 23.26 Cr (results 550) | **DIVERGENCE (12x jump / basis)** -> F8-1 |
| Preferential issue size | "111.5 cr raised" (375) | Rs 141.50 Cr issued; 111.50 Cr utilised; 30 Cr warrants pending (results 587, 613-627) | **DIVERGENCE (framing)** -> F16-8 |
| Paid-up equity capital | 14.01 Cr Mar'26 (1004); 14,01,43,988 shares (1066) | 1,401.28 L = 14.01 Cr Q1FY27 (310) | MATCH |
| Other Equity | 330.90 Cr Mar'26 (1005) | 33,089.57 L = 330.90 Cr (311) | MATCH |

The six audited headline KPIs the deck shares with the filing (interest income, revenue, PAT, net worth, D/E, NNPA) all tie exactly. Four cross-doc issues are omission/framing/valuation divergences, not arithmetic contradictions; each is carried as a finding below.

---

## FINDINGS TABLE

| id | check | ledger row ref | line/slide | verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| F6-1 | F6 | A2 §Slide21, GUIDANCE | slide 21, line 675 | "rapid branch rollout (30–45 days from planning to launch)" | FORWARD-SIGNAL | Only dated execution commitment in the deck; sets a promise-vs-delivery clock on branch adds (105->118 QoQ). A4/Role5 to track rollout cadence. |
| F6-2 | F6 | A2 §Slide23 | slide 23, lines 705, 716 | "Company has entered a strategic co-lending partnership with Godrej Finance"; "This milestone marks a major advancement" | FORWARD-SIGNAL | Co-lending is the off-book AUM growth vehicle; "entered" = live. No volumes/economics disclosed -> future off-book AUM ramp of unknown size. |
| F8-1 | F8 | A2 §Slide32, ZERO_STANDING #5/#6 | slide 32, lines 995, 997 | "Deferred Tax Assets (Net) — (Mar'26)/0.16 (Mar'25)"; "Deferred tax liabilities (net) 1.87 (Mar'26)/—" | AMBIGUOUS | Net deferred-tax position flipped asset->liability YoY. Cross-doc: filing Jun'26 DTL 23.26 Cr vs deck Mar'26 DTL 1.87 Cr (12x, one quarter) — verify basis/OCR. Sign flip can foreshadow ETR normalisation. |
| F10-1 | F10 | A2 §Slide36 / §Slide32 | slide 36 line 1066; slide 32 line 1004 | "No. of Shares outstanding 14,01,43,988"; "Equity Share Capital 14.01/12.69" | FORWARD-SIGNAL | Deck shows share count but not the outstanding share warrants. Cross-doc (results 613-627): 75% of warrant subscription (~Rs 30 Cr) "yet to be received" -> pending dilution + capital inflow the deck does not flag. |
| F14-1 | F14 | A2 §Slide4 / §Slide7 / §Slide9 | lines 86, 176/91/229, 190/237 | "Augmont Enterprises Ltd ... Turnover (FY26): INR 94,186 Cr"; "AUM 1,270.4" vs "1,271"; "NNPA 0.48%" vs "0.5%" | AMBIGUOUS | Deck credits promoter legacy to "Augmont Enterprises Ltd", but the filing's RPT counterparty is "Augmont Goldtech Private Limited" (results agenda 7) — different Augmont-group entities. Which entity actually sources/charges Finkurve? Rounding restatements (AUM/NNPA) benign. |
| F16-1 | F16 | A2 KPI_GUIDANCE_ABSENT (§F) | deck-wide; only guidance = line 675 | "every KPI ... is a trailing actual" (A2); no forward AUM/ROE/ROA/NIM/branch target stated | AMBIGUOUS | Notion thesis hinges on a guided ROE re-rating and an FY29 AUM target; the deck gives ZERO numeric guidance. A4 must ask management for forward targets — none are on the record. |
| F16-2 | F16 | A2 §D footnotes 1-5; §Slide28 | lines 191, 762, 815, 855, 892; 874 | "*Includes Off book AUM"; "Off book AUM included in the over all AUM" | AMBIGUOUS | Off-book blended into EVERY AUM chart, never quantified. Cross-doc: co-lending outstanding 37.86 Cr (results 337) ~3% of 1,270.4 headline; deck's Mar'26 on-book Loans 1,070.34 (line 986) vs Q4FY26 headline 1,096.1 implies ~26 Cr off-book. Small today, but the split and its economics are hidden. |
| F16-3 | F16 | A2 §Slide7 lines 176/178; §Slide28 881-884 | lines 176, 178, 881-884 | "AUM 1,270.4 ... ▲134.5%"; "Gold Kgs 1,167.5 ... ▲46.6%"; "LTV 69.1/64.4/65.8/72.2/77.3%" | FORWARD-SIGNAL | AUM +134.5% YoY on gold-tonnage +46.6% and customers +61.5% => roughly half of AUM growth is gold-price/LTV, not volume. LTV rose to 77.3% (from 64.4%); ticket size 1.31->1.87 L. Growth quality is price-levered; a gold-price reversal compresses AUM and breaches LTV headroom. Deck never decomposes price vs volume. |
| F16-4 | F16 | A2 §Slide32 lines 975, 996, 998, 1000 | slide 32, lines 975, 996, 998, 1000 | "Balance Sheet as on 31st March 2026"; "PP&E 15.66/3.63"; "Capital Work-in-progress —/7.56"; "Right Of Use Assets 10.78/3.88" | FORWARD-SIGNAL | Deck's only full balance sheet is Mar'26 (stale by a quarter; Q1FY27 BS undisclosed). Within it: PP&E ~4x, ROU assets ~2.8x, CWIP 7.56->nil (commissioned). Branch-build capex is ramping ahead of AUM -> future opex/branch drag. |
| F16-5 | F16 | A2 §Slide31 line 962 | slide 31, line 962 | "Fees And Commission Expenses 69.73/61.93" | FORWARD-SIGNAL | Rs 69.73 Cr FY26 fee-and-commission EXPENSE shown as a plain P&L line. Cross-doc (results agenda 7): payments to Augmont Goldtech Pvt Ltd (Service Fees, Commission, Brand Usage, Tech Support) are Material RPTs up for AGM approval. The deck does not disclose the related-party pass-through nature of this ~34% of revenue expense line. |
| F16-6 | F16 | A2 §Slide7 line 190; §Slide25 769-774 | lines 190, 769-774 | "NNPA (%) 0.48% ... ▲39 bps" (Q1FY27 vs Q4FY26 0.09%); GNPA chart 0.4%-1.1% range | AMBIGUOUS | Asset quality DETERIORATED: NNPA 0.09%->0.48% QoQ (+39 bps), rendered with the same ▲ up-arrow used for growth metrics. GNPA (filing 0.54%) is omitted from the headline table and survives only in an ambiguous chart. Notion's cached "GNPA 0.09%" is actually a prior-quarter NNPA; true current GNPA is ~6x that. |
| F16-7 | F16 | A2 MACRO_NOT_COMPANY §Slide3/4/10/16 | lines 57-66, 86, 262, 486-512 | "4 Cr+ Customers"; "Turnover (FY26): INR 94,186 Cr"; "serving 37+ mn customers"; "Household Gold Wealth Rs. 394 Lakh Cr" | AMBIGUOUS | Augmont-group and HDFC-Securities sector figures are interleaved with Finkurve KPIs. The "37+ mn customers" Augmont funnel is presented as a strength but the deck gives NO metric on customers actually sourced via Augmont into Finkurve's book — the funnel is "not yet switched on". Do not read group scale as company KPI. |
| F16-8 | F16 | A2 §Slide13 line 375 | slide 13, line 375 | "INR 111.5 cr raised through preferential issue of equity shares" | AMBIGUOUS | Deck states 111.5 Cr "raised"; filing (results 587/613-627) shows the issue was Rs 141.50 Cr with Rs 30 Cr (75% of warrant subscription) still uncalled. Deck presents received-only and omits the warrant overhang -> understates issue size and pending dilution (ties F10-1). |

Note (NEUTRAL-FACT, not tabled as an A4 question): slide 36 line 1072 discloses "Thomas John Muthoot (On behalf of Muthoot Bankers) 13.2%" — a Muthoot-affiliated 13.2% holder in a competing gold-loan NBFC; ownership fact, recorded for A4 governance context.

---

## CHECKLIST SCORECARD (all 17; GATE A3)

| Check | Status | One-line basis |
|---|---|---|
| F1  | PASS   | 7 zero_standing lines (A2 §C) are standard Schedule III template counterparts (Net Loss on FV mirrors Net Gain, line 939/963; nil Bank Balance line 984). No anomalous anticipated-transaction class. Substantive transitions (DTA->DTL, CWIP) routed to F8/F16-4. |
| F2  | N.A.   | Filing is STANDALONE-ONLY (results ledger §6, single entity); deck carries single-entity figures only. No S-vs-C gap exists. |
| F3  | N.A.   | No consolidated cost lines / no subsidiaries; shell-entity test inapplicable. |
| F4  | N.A.   | Deck carries no auditor Other-Matters paragraph; unaudited-contribution ratio not computable from a marketing deck. |
| F5  | N.A.   | No Going Concern / Emphasis-of-Matter paragraph in a deck; nothing to verbatim-diff. |
| F6  | FINDING| 2 dated/dateable commitments mined: branch rollout 30-45 days (line 675, F6-1) and Godrej co-lending "has entered ... major advancement" (lines 705/716, F6-2). |
| F7  | PASS   | Hedge-lexicon sweep of all deck prose returned no pre-emptive legal hedges on revenue lumpiness/concentration; deck is promotional, hedge-light. |
| F8  | FINDING| ETR clean vs 25.17% statutory (Q1FY27 24.7%, Q4FY26 22.8%, Q1FY26 25.5%, FY26 24.7%, FY25 26.3%). But deferred-tax net position flipped DTA 0.16 (Mar'25) -> DTL 1.87 (Mar'26), lines 995/997; cross-doc DTL 23.26 Cr at Jun'26 (F8-1). |
| F9  | N.A.   | Deck P&L (slides 30/31) omits OCI / Total Comprehensive Income entirely; filing OCI immaterial (37.49 L FY26, nil Q1FY27) — no actuarial swing to assess. Omission noted under F16. |
| F10 | FINDING| Share count 14,01,43,988 / equity capital 14.01 (up from 12.69) disclosed, but outstanding share warrants (~Rs 30 Cr uncalled per filing) not flagged (F10-1). Deck shows no EPS. |
| F11 | PASS   | Net worth ties: Other Equity 330.90 + Share Capital 14.01 = 344.91 = deck headline Q4FY26 344.9 (line 188); Q1FY27 354.4 = filed 354.37. Zero gap. |
| F12 | N.A.   | Single reportable segment ("financial services", filing Note 6); deck shows product-MIX (gold/personal/other), not a statutory segment assets/liabilities table to trend. Branch-capex accretion captured under F16-4. |
| F13 | N.A.   | Deck is not a board outcome; director bios (slide 11) carry no term/re-appointment dates; board resolutions (Rs 5,000 Cr borrowing power, NCD issue, Himadri Bhattacharya post-75 continuation, Augmont RPTs) live only in the filing, out of this doc's scope. |
| F14 | FINDING| Augmont entity-name inconsistency: "Augmont Enterprises Ltd" (line 86) in deck vs RPT counterparty "Augmont Goldtech Private Limited" (filing); plus benign rounding restatements AUM 1,270.4/1,271 and NNPA 0.48%/0.5% (F14-1). |
| F15 | N.A.   | No consolidation entity list in a deck; no prior-quarter deck supplied (PRIOR_LEDGER_UNAVAILABLE) — additions/deletions diff impossible. |
| F16 | FINDING| Eight presentation-specific findings F16-1..F16-8: guidance-absent, off-book unquantified, price/LTV-driven growth, stale BS + capex ramp, RPT fee pass-through undisclosed, asset-quality up-arrow framing + GNPA omission, macro/group conflation, preferential-issue framing. |
| F17 | N.A.   | Concall-specific silence audit requires a transcript; none in scope. The equivalent "what the deck presents around" audit against the Notion checklist is performed under F16 (LTV F16-3/6, cost-of-funds note below, off-book F16-2, Augmont sourcing F16-7). |

Scorecard counts: PASS 3 (F1, F7, F11); FINDING 5 (F6, F8, F10, F14, F16); N.A. 9 (F2, F3, F4, F5, F9, F12, F13, F15, F17). All 17 marked; no blanks.

Cost-of-funds note (F17/checklist pass-through, folded here): deck slide 24 shows cost of borrowing 11.5%/11.2%/11.1%/10.2% (FY24->Q1FY27, lines 728-729) — a drop to 10.2% in Q1FY27, against the Notion's "~11.2% flat" expectation. Single-quarter point on a chart with no basis stated (incl/excl which instruments; period-average vs spot). Flagged for A4 to verify the 10.2% and whether it is comparable to the trailing series.

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | ref | status word |
|---|---|---|---|
| Branch rollout 30-45 days from planning to launch | ongoing / per-branch | slide 21, line 675 | underway (stated as operating norm) |
| Co-lending partnership with Godrej Finance (gold loans, RBI co-lending framework) | live in FY26 | slide 23, lines 705/716 | entered / "milestone ... major advancement" (completed) |
| Co-lending partnership with RBL Bank (gold loans) | FY25 | slide 13, line 377 | completed (prior year) |
| Augmont group DRHP filed / SEBI approval received; MOU with NSE for EGRs [MACRO — Augmont group, NOT Finkurve] | 2025-2026 | slide 4, lines 99-109 | filed / approval received (group-level catalyst, do not attribute to Finkurve) |

---

## ADJUDICATION OF A2 LEADS (all four closed)

1. **Off-book AUM quantification** — CLOSED as F16-2. The "*Includes Off book AUM" footnote recurs on all 5 headline AUM charts (A2 §D). Deck never states the split. Reconciliation: filing co-lending outstanding = 37.86 Cr (results 337) ~= 3% of 1,270.4 Cr headline; deck's own Mar'26 on-book Loans = 1,070.34 (line 986) vs Q4FY26 headline AUM 1,096.1 (line 176) implies ~26 Cr off-book at Mar'26 (~2.4%). Off-book is immaterial in SIZE today, but (a) it is undisclosed as a quantum, and (b) the Godrej co-lending vehicle (F6-2) is expressly designed to grow it. The on-book figure does reconcile to the filing at Mar'26; the CURRENT-quarter on-book figure is NOT in the deck (stale BS, F16-4).
2. **DTA->DTL sign flip** — CLOSED as F8-1 (AMBIGUOUS). Plus cross-doc magnitude flag (deck Mar'26 1.87 Cr vs filing Jun'26 23.26 Cr).
3. **KPI_GUIDANCE_ABSENT** — CLOSED as F16-1 (AMBIGUOUS). Confirmed: zero forward numeric targets deck-wide; the thesis's guided-ROE / FY29-AUM pillars have no management figure to anchor to.
4. **MACRO_NOT_COMPANY** — CLOSED as F16-7 (AMBIGUOUS). Augmont-group (37 mn customers, Rs 94,186 Cr turnover) and HDFC-Securities sector figures (slides 3,4,10,16) must not be read as Finkurve KPIs; Augmont funnel not yet demonstrably converted into Finkurve's book.

---

## YAML

```yaml
stage: A3-forensics
company: "finkurve"
quarter: "q1fy27"
doctype: "presentation"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/finkurve-q1fy27/work/forensics_presentation_finkurve_q1fy27.md"
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
  F10: FINDING
  F11: PASS
  F12: N.A.
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: N.A.
findings:
  - {id: "F6-1",  check: "F6",  line: "slide 21 / line 675", classification: "FORWARD-SIGNAL", implication: "Only dated commitment; branch-rollout cadence clock for Role 5"}
  - {id: "F6-2",  check: "F6",  line: "slide 23 / lines 705,716", classification: "FORWARD-SIGNAL", implication: "Godrej co-lending live = off-book AUM growth vehicle; volumes undisclosed"}
  - {id: "F8-1",  check: "F8",  line: "slide 32 / lines 995,997", classification: "AMBIGUOUS", implication: "DTA->DTL sign flip; cross-doc DTL 1.87 vs 23.26 Cr; possible ETR normalisation"}
  - {id: "F10-1", check: "F10", line: "slide 36 / line 1066; slide 32 / line 1004", classification: "FORWARD-SIGNAL", implication: "Undisclosed share warrants ~Rs 30 Cr uncalled -> pending dilution + capital"}
  - {id: "F14-1", check: "F14", line: "slide 4 / line 86", classification: "AMBIGUOUS", implication: "Augmont Enterprises Ltd vs Augmont Goldtech Pvt Ltd; which entity transacts with Finkurve"}
  - {id: "F16-1", check: "F16", line: "deck-wide (only guidance line 675)", classification: "AMBIGUOUS", implication: "No forward targets; thesis needs guided ROE / FY29 AUM - none on record"}
  - {id: "F16-2", check: "F16", line: "lines 191,762,815,855,892", classification: "AMBIGUOUS", implication: "Off-book blended into every AUM chart, never quantified; ~3% today via co-lending 37.86 Cr"}
  - {id: "F16-3", check: "F16", line: "slide 7 / lines 176,178; slide 28 / 881-884", classification: "FORWARD-SIGNAL", implication: "AUM +134.5% on kg +46.6% = price/LTV-driven; LTV 77.3%; gold-price reversal risk"}
  - {id: "F16-4", check: "F16", line: "slide 32 / lines 975,996,998,1000", classification: "FORWARD-SIGNAL", implication: "Stale Mar'26 BS; PP&E/ROU/CWIP show branch-build capex ramp ahead of AUM"}
  - {id: "F16-5", check: "F16", line: "slide 31 / line 962", classification: "FORWARD-SIGNAL", implication: "Rs 69.73 Cr fee expense is Augmont Goldtech RPT pass-through, undisclosed in deck"}
  - {id: "F16-6", check: "F16", line: "slide 7 / line 190; slide 25 / 769-774", classification: "AMBIGUOUS", implication: "NNPA +39bps QoQ shown with up-arrow; GNPA 0.54% omitted from headline"}
  - {id: "F16-7", check: "F16", line: "slides 3,4,10,16 / lines 57-66,86,262,486-512", classification: "AMBIGUOUS", implication: "Augmont-group/sector figures conflated with Finkurve KPIs; 37mn funnel not switched on"}
  - {id: "F16-8", check: "F16", line: "slide 13 / line 375", classification: "AMBIGUOUS", implication: "Deck '111.5 cr raised' vs filing 141.50 Cr issued (30 Cr warrants pending); understates dilution"}
forward_signals: ["F6-1","F6-2","F10-1","F16-3","F16-4","F16-5"]
ambiguous: ["F8-1","F14-1","F16-1","F16-2","F16-6","F16-7","F16-8"]
commitments:
  - {commitment: "Branch rollout 30-45 days from planning to launch", implied_date: "ongoing/per-branch", ref: "slide 21 line 675", status_word: "underway"}
  - {commitment: "Godrej Finance co-lending partnership (gold loans)", implied_date: "FY26 live", ref: "slide 23 lines 705,716", status_word: "entered/completed"}
  - {commitment: "RBL Bank co-lending partnership (gold loans)", implied_date: "FY25", ref: "slide 13 line 377", status_word: "completed"}
  - {commitment: "Augmont group DRHP filed / SEBI approval received (MACRO - group, not Finkurve)", implied_date: "2025-2026", ref: "slide 4 lines 99-109", status_word: "approval-received"}
gate_a3: pass
blank_checks: []
```
