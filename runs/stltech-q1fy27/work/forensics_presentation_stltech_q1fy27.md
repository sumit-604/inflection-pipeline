# A3 FORENSIC NOTES — STLTECH — Q1FY27 — DOCTYPE: PRESENTATION

Source document: `stltech_q1fy27_presentation.pdf` (32 slides, Earnings Call Q1FY27, 24-Jul-2026).
Extract read in full: `extract_presentation_stltech_q1fy27.txt` (lines 32-1133).
Ledger reconciled: `ledger_presentation_stltech_q1fy27.md` — Table 1 (32 slides), Table 2 (all 470 numeric rows), Table 3 (9 footnotes), Table 4 (N.A.). **470/470 rows read at their cited lines = 100%.**

Doctype applicability (per prompt): on a presentation, **F16 is the core check** plus any F6/F10/F11 numbers the deck carries; balance-sheet / auditor-letter / EoM / entity-list checks are structurally N.A. and are marked so with a one-line reason. F17 is applied as a deck-vs-monitoring-checklist silence audit (there is no transcript in scope).

Interpretation bias: conservative. Where a finding's direction is uncertain it is classified AMBIGUOUS and handed to A4 as a management question rather than resolved here.

---

## FINDINGS TABLE

| id | check | ledger row ref | line/slide | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| FND-01 | F1 | rows 411-412 (+ F7 footnote) | line 966 / 888, slide 26/23 | "Exceptional Items 31 0 0" ; "* from continued operations" | AMBIGUOUS | Exceptional-items line is live (+31 Cr booked Q4FY26, nil Q1FY26/Q1FY27); the "from continued operations" asterisk on every headline figure implies a discontinued operation exists off-table. What was the Q4FY26 +31 Cr item, and what is being discontinued? |
| FND-02 | F6 | rows 322/324, 261-262, — | line 803-804 / 553-557 / 1077 / 713 / 985, slides 20/15/29/18/27 | "scaling the attach rate above 20% from Q2 onwards & 25%+ by Q4FY27" ; "supply optical connectivity products from FY27 to FY29" ; "has been commissioned and has successfully started supply" | FORWARD-SIGNAL | Dated management commitments feeding the Role 5 promise-vs-delivery tracker (see Commitment Register). Attach-rate walk and the $1.11Bn FY27-FY29 supply are the load-bearing ones. |
| FND-03 | F8 | rows 413-421 | line 968 / 971, slide 26 | "PBT 109 13 257 … Tax (50) (3) (60)" | AMBIGUOUS | ETR = Q4FY26 45.9%, Q1FY26 23.1%, Q1FY27 23.3% vs statutory 25.17%. Q1FY27 sits ~187 bps below statutory (a shield); Q4FY26 spiked to 45.9%. Sustainability of the sub-statutory rate / future ETR step-up is a question. |
| FND-04 | F10 | rows 427-436, 424-425 | line 985 / 981 / 1017, slide 27/26 | "₹1,500 Cr QUALIFIED INSTITUTIONAL PLACEMENT" ; "~1500 Crs of QIP amount pending allocation as on 30th Jun" | FORWARD-SIGNAL | QIP allotted 3-Jul-2026 (after 30-Jun quarter close), so Q1FY27 PAT/EPS optics are pre-dilution; forward quarters carry the enlarged share count. Promoter holding 25% post-QIP. No per-share EPS (basic/diluted) disclosed in the deck. |
| FND-05 | F14 | ledger note line 487 (slide 22) | line 844 / 41, slide 22/1 | nav-bar "Strategic Priorities for FY26" (slides 4/8/14 read "FY27") ; "© 2022-2023 Sterlite Technologies Limited" | NEUTRAL-FACT | Stale-template drafting inconsistencies (FY26 nav label on the financial-section divider; 2022-2023 copyright on the title slide). Immaterial individually; a governance/care data point. |
| FND-06 | F16 | rows 332-360 (x-axis) | line 868, slide 23 | "Q2FY26 Q3FY26 Q4FY26 Q1FY26 Q1FY27" | NEUTRAL-FACT | The "Highest Ever!" performance chart plots bars in non-chronological order, seating the weak Q1FY26 comparator immediately left of Q1FY27 to maximise the visual step-up. Presentation technique, flagged. |
| FND-07 | F16 | Table 3 F7 (rows 332-379, 390-421) | line 888 / 923 / 978, slides 23/24/26 | "* from continued operations" | FORWARD-SIGNAL | Every headline Revenue/EBITDA/EBITDA%/PAT and the abridged P&L is "from continued operations." A discontinued operation is therefore excluded from "Highest Ever!" — its identity, drag and disposal status are not shown. |
| FND-08 | F16 | rows 340 vs 391; 342/344 vs 394 | line 864 vs 954/956, slides 23 vs 26 | slide 23 "Q1FY26 … 1,034" vs slide 26 "Revenue* … 1,019" | AMBIGUOUS | Same period, same metric, two different values across two slides of the same deck (Q1FY26 revenue 1,034 vs 1,019; Q1FY26 EBITDA reads 129 on the chart vs 140 in the table, though both quote 13.7%). Chart bar-to-period mapping is unreliable (scrambled order); the clean P&L table should govern. |
| FND-09 | F16 | rows 263-265, 383 | line 561-564 / 936, slides 15/25 | "Order Intake … 1.7x … 13,100 … 7,687 … FY26  Q1 FY27" | AMBIGUOUS | The "1.7x" order-intake bar compares a full-year FY26 figure (7,687) against a single quarter Q1FY27 (13,100) — a period-mismatched, flattering comparison. The identical 7,687 is also re-used on slide 25 as the FY26 "open order book" base, so one number serves two different definitions. |
| FND-10 | F16 | rows 396, 423-424 | line 957 / 979 / 981, slide 26 | "Net Debt-Free balance sheet … Net cash balance stands at 483 Cr" ; "#Includes restricted cash items: a) ~391 Crs … legal matter … US entity b) ~1500 Crs of QIP … pending allocation" | FORWARD-SIGNAL | The net-cash / net-debt-free headline is quality-impaired: it is footnoted to include ~391 Cr restricted (litigation) plus ~1,500 Cr un-deployed QIP cash. Deleveraging is QIP-funded (75% of proceeds earmarked to deleverage), not operations-funded; the "net debt-free" status is capital-raise-dependent. |
| FND-11 | F16 | rows 362-378 | line 899-913, slide 24 | segment mix values "82 … 17 … 1 … 61 … 21 … 18" (DC & Cloud / Large Enterprise / Telecom) | AMBIGUOUS | Segment revenue mix is disclosed but the chart text layer extracts in scrambled order (CHART_LABEL_SCRAMBLED_ORDER), so the Enterprise+DC walk (Notion monitoring metric #5, target 22/25/27/30%) cannot be reliably reconstructed from the deck. Ask management for the tabular segment split. |
| FND-12 | F17 | Table 3 F8 (Prysmian proxy) + monitoring checklist | line 979, slide 26 (+ deck-wide silence) | "~391 Crs for a legal matter related to the US entity" (Prysmian never named) | AMBIGUOUS | Deck is silent on: operational/ex-tariff EBITDA (monitor #2), CFO / cash conversion (monitor #7 — no cash-flow statement anywhere), promoter pledge (monitor #8), Prysmian Fourth-Circuit appeal status (only a 391 Cr restricted-cash footnote, litigant unnamed), India +12.5% tariff resolution, and West Asia input costs (helium/polymer). See silence table below. |

---

## CHECKLIST SCORECARD (all 17)

| Check | Status | One-line basis |
|---|---|---|
| F1  ZERO-VALUE STANDING LINES | **FINDING** | Exceptional Items = 0 in Q1FY26 & Q1FY27, +31 in Q4FY26 (rows 411-412, line 966); "from continued operations" asterisk implies an unshown discontinued-ops line. → FND-01 |
| F2  STANDALONE vs CONSOLIDATED | **N.A.** | Deck presents consolidated only ("Consolidated financials: Abridged version", slide 26); no standalone column, so no S-vs-C gap computable. |
| F3  SHELL-ENTITY DETECTION | **N.A.** | No standalone-vs-consolidated cost lines (Materials/Employee/Depreciation) in the deck to compare. |
| F4  UNAUDITED CONTRIBUTION RATIO | **N.A.** | A presentation carries no auditor "Other Matters" paragraph; the % of PAT resting on unreviewed JV/associate/component-auditor numbers is not disclosable here. |
| F5  GOING CONCERN / EoM SCOPE | **N.A.** | No EoM / going-concern language in a deck, and no prior-quarter deck available to verbatim-diff. |
| F6  FORWARD-COMMITMENT MINING | **FINDING** | Multiple dated/dateable commitments (attach-rate walk, $1.11Bn FY27-FY29 supply, green-H2 commissioned, G.654.E commercialized, QIP deployment, net-zero 2030). → FND-02, see Commitment Register |
| F7  HEDGE PHRASE MINING | **PASS** | Only boilerplate Safe Harbour hedges (slide 2, lines 45-68: "may cause actual results … to differ materially", "no … warranty", "not … indicative of future results"); no note-level hedge newly added about lumpiness/concentration, and no prior deck to diff for new hedges. |
| F8  TAX FORENSICS | **FINDING** | ETR volatile: Q4FY26 45.9%, Q1FY26 23.1%, Q1FY27 23.3% vs statutory 25.17%; Q1FY27 runs ~187 bps below statutory. → FND-03 |
| F9  OCI FORENSICS | **N.A.** | No OCI / actuarial gain-loss line disclosed in the deck. |
| F10 SHARE COUNT & DILUTION | **FINDING** | ₹1,500 Cr QIP (allotted 3-Jul-2026), ~1,500 Cr pending allocation, promoter 25% post-QIP; no basic/diluted EPS spread disclosed. → FND-04 |
| F11 RESERVES / NET-WORTH TIE-OUT | **N.A.** | No Other Equity / paid-up / net-worth figure in the deck to reconcile (net-cash headline quality handled under F16/FND-10). |
| F12 SEGMENT FORENSICS | **N.A.** | Slide 24 discloses segment/geography *revenue mix only*; no segment assets or liabilities, so the equity-funded-build / WC-unwind tests cannot run. (Revenue-mix reliability issue raised under F16/FND-11.) |
| F13 BOARD OUTCOME BEYOND RESULTS | **N.A.** | No AGM notice, record date, AR/Board's-Report approval, or director term dates in the deck. (QIP is an already-executed capital action, covered under F10.) |
| F14 NOTE-DRAFTING INCONSISTENCIES | **FINDING** | Slide-22 nav reads "FY26" vs "FY27" on slides 4/8/14 (line 844); title slide copyright "© 2022-2023" (line 41). → FND-05 |
| F15 ENTITY LIST DIFFS | **N.A.** | No consolidation entity list in the deck and no prior-quarter deck to diff. |
| F16 DROPPED / REFRAMED DISCLOSURES | **FINDING** | Non-chronological chart order (FND-06); continued-ops asterisk excludes discontinued ops (FND-07); cross-slide value inconsistency Q1FY26 (FND-08); period-mismatched "1.7x" order-intake comparison + re-used 7,687 (FND-09); net-cash headline quality (FND-10); segment-mix walk unverifiable (FND-11). |
| F17 SILENCE AUDIT (deck vs monitor) | **FINDING** | Deck silent on ex-tariff/operational EBITDA, CFO/cash conversion, promoter pledge, Prysmian appeal status, tariff resolution, West Asia input costs. → FND-12, see silence table |

Blank checks: none. **GATE A3: PASS.**

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | ref (line/slide) | status word |
|---|---|---|---|
| Attach rate above 20% "from Q2 onwards", 25%+ by Q4FY27 | Q2FY27 / Q4FY27 | line 803-804, slide 20 | underway (guidance) |
| $1.11Bn hyperscaler PAL — supply optical connectivity products FY27→FY29 | FY27-FY29 | line 553-557, slide 15 | initiated (secured) |
| Multiple hyperscaler orders $100 Mn+ for Neuralis portfolio | ongoing | line 558-559, slide 15 | initiated (secured) |
| Green hydrogen & oxygen plant "commissioned and successfully started supply" | Q1FY27 | line 1077, slide 29 | completed |
| G.654.E fibre "Moves from NPD to Successful Commercialization" | Q1FY27 | line 713, slide 18 | completed |
| HCF cable "launched" (~46% faster transmission) | Q1FY27 | line 713-714, slide 18 | completed |
| QIP ₹1,500 Cr — 75% deleveraging / 25% GCP; ~1,500 Cr pending allocation | post 30-Jun-2026 | line 981/995/998, slides 26/27 | underway (in process) |
| Net-Zero by 2030 target | 2030 | line 83, slide 3 | underway |
| Reported EBITDA margin walk toward 20% (Q1FY27 already 20.8%) | Q4FY27 | line 861/958, slides 23/26 | underway (ahead) |

---

## WHAT WAS NOT DISCUSSED (F17 silence audit — deck vs Notion monitoring checklist)

First quarterly-pipeline run for STLTECH, so consecutive-quarters-of-silence count is baselined at 1 for each item; Q2FY27's A3 should increment.

| Monitored item (Notion) | Addressed in deck? | Consec. Qs silent | Note |
|---|---|---|---|
| #2 Operational EBITDA ex-tariff (>=21% green / <19% red) | NO | 1 | Only reported 20.8% shown; no ex-tariff/operational bridge. Tariff overlay unquantified. |
| #7 CFO/EBITDA cash conversion (>=75% / <65%) | NO | 1 | No cash-flow statement anywhere in the deck. Per CLAUDE.md, indeterminate cash conversion must not resolve to PROCEED. |
| #8 Promoter pledge (0% / any new pledge) | NO | 1 | Promoter holding 25% post-QIP shown; pledge status absent. |
| Prysmian USD101.25M Fourth-Circuit appeal status | PARTIAL/NO | 1 | Only "~391 Crs for a legal matter related to the US entity" (line 979); Prysmian not named, appeal status/timeline absent. Thesis-broken trigger #4 hinges on this. |
| Additional 12.5% India tariff resolution | NO | 1 | No tariff discussion; a LIVE SECTOR MONITORABLE. |
| West Asia input costs (helium/polymer) | NO | 1 | Input-cost exposure not mentioned. |
| #5 Enterprise+DC revenue mix walk (22/25/27/30%) | AMBIGUOUS | 1 | Shown but chart order scrambled (FND-11); walk not cleanly verifiable. |
| #9 Hyperscaler contract — named multi-year deal | PARTIAL | 1 | $1.11Bn multi-year (FY27-FY29) disclosed but counterparty unnamed — "hyperscaler" generic; red-flag "continued vague language" partially triggered on identity. |
| #1 Reported EBITDA margin walk / 20% reaffirmation | YES | 0 | 20.8% Q1FY27 (line 861); implicit reaffirmation, ahead of the 20%-by-Q4 target. |
| #3 Order intake TTM (>=8,500) | YES (partial) | 0 | Q1FY27 intake 13,100; FY26 7,687 (TTM not explicitly stated). |
| #4 Open order book (7,000+) | YES | 0 | 18,618 Cr (line 931). Green. |
| #6 Net Debt/EBITDA (<=1.2x by Q4FY27) | YES (caveated) | 0 | "Net Debt-Free" claimed — but QIP-funded and restricted-cash-inflated (FND-10). |

---

## RECONCILIATION STATEMENT

All 470 Table-2 rows, the 32-slide Table-1 inventory, the 9-row Table-3 footnote set, and the Table-4 dropped-slides note (N.A., no prior deck) were read verbatim at their cited extract line numbers before judging. The six ledger-raised flags were resolved as follows:
- **ZERO_STANDING** (rows 411-412) → F1 FINDING (FND-01).
- **HEADLINE_QUALIFIER** ("Highest Ever!", "*from continued operations", net-cash restricted-cash footnotes) → F16 FINDINGs (FND-07, FND-10).
- **CHART_LABEL_SCRAMBLED_ORDER** + the non-chronological bar sequence → F16 FINDINGs (FND-06, FND-08, FND-11).
- **PERIOD_LABEL_FRAGMENT** (10 rows) → mechanical grep artifacts, no forensic content; PASS-through, no finding.
- **LOW_CONFIDENCE_OCR** (icon/glyph/brand misreads) → mechanical, no forensic content; no finding.
- **UNIT/FORMULA_ARTIFACT** (CO2, m3) → mechanical, no forensic content; no finding.
- Slide-22 "FY26" nav discrepancy → F14 FINDING (FND-05).
