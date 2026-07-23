# A3 FORENSIC NOTES — SONACOMS Q1 FY27 — doctype: presentation (in fact a 4-page PRESS RELEASE + Reg-30 cover letter)

Company: Sona BLW Precision Forgings (SONACOMS) | Quarter: Q1 FY27 | Model: claude-opus-4-8
A1 extract: extract_pressrelease_sona_q1fy27.txt (183 lines) | A2 ledger: ledger_pressrelease_sona_q1fy27.md (51 units)
Cross-check filing: extract_results_sona_q1fy27.txt (Reg-33 results, units Rs Million x0.1 -> Cr)
Prior-quarter extract: NONE — first pipeline run for this ticker. All diff/consecutive-silence checks (F5, F15, F16 baseline-diff, F17 quarter-count) have no prior artifact; consecutive-silence counts start at 1.
Ledger reconciliation: 51/51 disclosure units read at their cited lines = 100%.

Doctype routing note: A2 raised DOCTYPE_MISMATCH — routed as "presentation" but is a press release + cover letter, no slides. Per task instruction, statement/auditor/Board-Outcome checks (F1, F3, F4, F5, F8, F9, F10, F11, F12, F13, F15) are N.A. for this narrative artifact; forensic weight sits on the headline financial claims, forward-looking statements, order-book claims, and any number that disagrees with the Reg-33 filing (F2, F6, F7, F14, F16, F17).

---

## RECONCILIATION OF HEADLINE NUMBERS vs REG-33 FILING (all figures Cr)

| Press claim (line) | Reconciles to (filing line) | Result |
|---|---|---|
| Revenue Rs 1,310 cr, +54% YoY (70) | CONSOL rev from ops 1,301.2 (469) + net forex 9.2 (470) = 1,310.4; YoY vs 850.9 = 54.0% | Ties to CONSOLIDATED (rev-from-ops + forex), not to filing "revenue from operations" line alone |
| EBITDA Rs 303 cr, 23.1%, +49% (72) | CONSOL operating profit 293.4 + forex 9.2 = 302.6; 302.6/1,310.4 = 23.1%; YoY vs 202.6 = 49.4% | Ties to CONSOLIDATED |
| PAT Rs 181 cr, 13.6%, +45% (73) | CONSOL profit attributable to owners 180.5 (506); 180.5/124.7 (owners Q1FY26, 506) = 45.1%; margin 180.5/1,336(total income) ~13.5% | Ties to CONSOLIDATED owners' PAT |
| BEV share 44%, BEV rev +107% (71) | Not separately disclosed in Reg-33 filing (single reportable segment, line 583) | Un-verifiable against filing |

Conclusion: every headline number reconciles to the CONSOLIDATED statement once "Revenue" is read as revenue-from-operations PLUS net forex gain. No hard contradiction, BUT (a) figures are unlabeled standalone-vs-consolidated, and (b) STANDALONE PAT is Rs 220.1 cr (filing line 202) — 22% ABOVE the Rs 181 cr quoted — so the choice of basis materially flatters/deflates depending on line. Flagged FD1/FD13.

---

## FINDINGS TABLE

| id | check | ledger row | line/ref | verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| FD1 | F2 | Sec2 note / R6 | press 30-32, 70-73; filing 202 vs 506 | "unaudited Standalone and Consolidated Financial Results" (30-31); "PAT of Rs. 181 crores" (73) | AMBIGUOUS | Headline set is unlabeled; reconciles to consolidated owners' PAT, but standalone PAT is Rs 220.1 cr. Reader cannot tell basis from the release. A4 question on which basis management intends the market to anchor. |
| FD13 | F2 | F1 (Revenue) | press 70; filing 469-470 | "Revenue of Rs. 1,310 crores with 54% YoY growth" | NEUTRAL-FACT | "Revenue" = consol rev-from-ops (Rs 1,301.2 cr) + net forex (Rs 9.2 cr). Non-standard definition inflates the headline ~Rs 9 cr above the filing's revenue-from-operations line. Definitional, reconciles; note for A4. |
| FD2 | F6 | B1-B3, O1, O2, Q1 | press 99,111,115,121,125,128 | "production is likely to commence in H2 FY29" (121); "aspiration to repeat 10 times revenue growth in the next decade ending FY35" (99) | FORWARD-SIGNAL | Dateable commitments: 3 order-production starts (H2 FY26 / FY28 / FY29) plus 10x-by-FY35 aspiration and Robotics vertical build. Feed Role 5 promise-vs-delivery tracker; earliest testable = B2 H2 FY26. |
| FD3 | F7 | B1-B3, G3 | press 121,125,128,174 | "production is likely to commence" (121/125/128); "subject to certain risks and uncertainties" (174) | AMBIGUOUS | "likely to commence" is a soft hedge on every order timeline — none is a firm SOP date. Timelines can slip without breaking a promise. A4 question: firm vs indicative SOP dates. |
| FD4 | F14 | R1 / DATE_MISMATCH | press 64 vs 15,43,66 | "Gurgaon, India, April 30, 2026" | NEUTRAL-FACT | Body dateline (Apr 30, 2026) predates the quarter it reports (ended Jun 30, 2026) and the actual signature/letter date (Jul 23, 2026). Stale template carried from a prior release = disclosure QC gap, not a results anomaly. |
| FD5 | F14 | G3 / TEMPLATE_ARTIFACT | press 173 | "statements made or discussed at the conference call" | NEUTRAL-FACT | Safe-harbour disclaimer references a "conference call" that this press release never mentions — reused concall-template boilerplate. Reinforces the QC-gap read of FD4. |
| FD6 | F14 | F5 / ORDER_COUNT_AMBIGUITY | press 75 vs 119-128 | "We won three orders which include one EV program, one hybrid program and one ICE program" | AMBIGUOUS | Itemized bullets describe 1 (B1) + 2 (B2, two orders bundled) + 1 (B3) = four individual orders across three programs. "Three orders" vs four undercounts; A4 question on true order count/value. |
| FD7 | F16 | E4 (DENSO) | press 82-83; filing note 4/5, 270-278 | "Our partnership with DENSO also takes us into high-voltage electric and hybrid powertrain systems, completing an important missing piece" | FORWARD-SIGNAL | Press frames DENSO purely as expansion. Filing (270-278) discloses the flip side: Company will SLUMP-SELL its existing EV motors & controllers business into a subsidiary and DENSO buys 49% at EV Rs 17,500 M, "subject to fulfilment of customary conditions." A partial divestment of a core EV asset, reframed as pure upside. Touches Notion tripwire (2) control/block-sale. Highest-priority A4 question. |
| FD8 | F16 | B1-B3 | press 121,125,128; Notion baseline | order additions "Rs 6.4 billion" (121) + "Rs 900 million" (124) + "Rs 2.1 billion" (127) = Rs 9.4 bn / ~Rs 940 cr | AMBIGUOUS | Release discloses order-book ADDITIONS only; total order book (Notion FY26 baseline Rs 23,700 cr) is dropped. Cannot judge net order-book direction (adds vs executions/cancellations) from the release. A4 question: closing order book and book definition. |
| FD9 | F17 | F3 (EBITDA) | press 72; Notion tripwire 6 | "EBITDA of Rs. 303 crores with a margin of 23.1%" | CONFIRMATORY-NEGATIVE | EBITDA margin 23.1% is ~160 bps BELOW the FY26 24.7% baseline (Notion tripwire 6, EBITDA margin compression). Release foregrounds +49% growth and stays silent on the margin step-down. Directional negative on the margin tripwire. |
| FD10 | F17 | Notion checklist | (silence — no line) | n/a (audited by absence) | CONFIRMATORY-NEGATIVE | Silent on tripwires: (1) ROCE trend, (3) Novelic KAM impairment, (4) CFO/PAT conversion, (5) corporate guarantee expansion, (7) working-capital stretch, (8) railway diversification delivery (FY26 railway Rs 973 cr rev). First-run baseline silence = 1 quarter each; sustained silence on a deteriorating metric is a Role-5 confirmatory negative. |
| FD11 | F17 | Q1 / UNSUBSTANTIATED_GEOGRAPHY_CLAIM | press 89-90 vs 119-128; Notion tripwire 10 | "spanning India, Europe and North America and nearly every product category" | AMBIGUOUS | Quote claims new business across India/Europe/North America, but the only itemized counterparties are a "North American OEM" (x2) and an unspecified "New Age OEM" — no India or Europe order named. Bears on India-mix tripwire (10). A4 question: evidence for the Europe/India order wins. |
| FD12 | F16/F17 | F2, F5, B1-B3 | press 71,88,120,124,127; Notion tripwire 9 | "despite continued weakness in the US EV market" (88); orders: "hybrid" (120), "Electric two wheelers" (124), "ICE" (127) | FORWARD-SIGNAL | BEV share hits 44% high, yet management concedes "continued weakness in the US EV market," and of the three NEW program lines only one is EV (one hybrid, one ICE). New-order mix tilts away from pure BEV — bears on BEV-anchor tripwire (9, order book ~70% EV). Watch order-book EV share trend. |

---

## CHECKLIST SCORECARD (all 17)

| Check | Status | One-line basis |
|---|---|---|
| F1 ZERO-VALUE STANDING ITEMS | N.A. | Press release carries no tabular line-item grid; ledger ZERO_STANDING = 0. (Filing note 3 shows exceptional items nil this quarter vs Rs 91.74 M prior — belongs to the Reg-33 artifact.) |
| F2 STANDALONE vs CONSOLIDATED | FINDING | FD1/FD13 — headline set unlabeled; reconciles to consolidated, but standalone PAT (Rs 220.1 cr) differs materially from quoted Rs 181 cr, and "Revenue" adds forex to rev-from-ops. |
| F3 SHELL-ENTITY DETECTION | N.A. | No standalone-vs-consolidated cost decomposition in a press release; requires the statement (Reg-33 filing). |
| F4 UNAUDITED CONTRIBUTION RATIO | N.A. | Auditor "Other Matters" not in the press release. (For reference, filing line 372-374: five overseas subs unreviewed by principal auditor, rev Rs 178.61 M, NET LOSS Rs 29.75 M ~ -1.7% of consol PAT — below 10%, and loss-making so it reduces PAT.) |
| F5 GOING CONCERN / EoM | N.A. | No going-concern / EoM language in the press release; first run, no prior quarter to verbatim-diff. |
| F6 FORWARD-COMMITMENT MINING | FINDING | FD2 — "commence" x3 (production starts H2 FY26/FY28/FY29), "will focus on" Robotics, 10x-by-FY35 aspiration. See Commitment Register. |
| F7 HEDGE PHRASE MINING | FINDING | FD3 — "likely to commence" x3 softens all order timelines; "subject to" in disclaimer. |
| F8 TAX FORENSICS | N.A. | Press release carries no tax figures. (Filing: consol ETR 25.9%, standalone ETR 20.1% vs 25.17% statutory — Reg-33 artifact.) |
| F9 OCI FORENSICS | N.A. | Press release carries no OCI. (Filing consol OCI swing +Rs 21.5 cr driven by cash-flow-hedge portion — Reg-33 artifact.) |
| F10 SHARE COUNT / DILUTION | N.A. | Press release carries no share count or EPS. (Filing: basic=diluted, no spread; ESOP 1,00,000 options + 1,70,747 PSP shares to MD — Reg-33 artifact.) |
| F11 RESERVES / NET WORTH | N.A. | Press release carries no reserves / net-worth figure. |
| F12 SEGMENT FORENSICS | N.A. | No segment data in the press release; company reports a single segment (filing line 583). |
| F13 BOARD OUTCOME BEYOND RESULTS | N.A. | This is a Reg-30 press-release cover, not a Board-Outcome letter; no AR/AGM/director-appointment agenda in this artifact. (AGM dividend Rs 1.80 sits in the filing.) |
| F14 NOTE DRAFTING INCONSISTENCIES | FINDING | FD4 (April-30 dateline), FD5 (disclaimer cites a non-existent concall), FD6 ("three orders" vs four itemized). |
| F15 ENTITY LIST DIFFS | N.A. | No consolidation list in the press release; first run, no prior quarter to diff. (Filing Annexure-1 lists 16 subs incl "Novelic India Private Limited*" incorporated 28-Nov-2025 — noted for next-quarter diffing.) |
| F16 DROPPED / REFRAMED DISCLOSURES | FINDING | FD7 (DENSO divestment reframed as pure upside), FD8 (order-book total dropped, only additions shown), FD12 (BEV-mix reframing). |
| F17 SILENCE AUDIT (vs Notion checklist) | FINDING | FD9 (EBITDA-margin compression tripwire), FD10 (silence on tripwires 1,3,4,5,7,8), FD11 (unsubstantiated geography vs tripwire 10), FD12 (BEV-anchor tripwire 9). First-run silence counts = 1. |

Gate A3: PASS — all 17 checks marked, none blank.

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | ref | status word |
|---|---|---|---|
| Differential assemblies, hybrid PV platform (existing North American OEM); order add Rs 6.4 bn (~Rs 640 cr) | H2 FY29 | press 119-122 | initiated (order won, pre-production) |
| Hub wheel traction motors, EV 2-wheelers (New Age OEM), two orders; add Rs 900 mn (~Rs 90 cr) | H2 FY26 | press 123-125 | initiated (earliest testable SOP) |
| Differential gears, ICE PV platform (North American OEM); add Rs 2.1 bn (~Rs 210 cr) | H2 FY28 | press 126-128 | initiated (order won, pre-production) |
| Sona Comstar 2.0: repeat 10x revenue growth over decade ending FY35 | FY35 | press 99-113 | announced (aspiration) |
| Entry/expansion into "Robotics and Physical AI" vertical (from Sensors & Software) | undated | press 114-118 | initiated (vertical announced) |
| DENSO: two 51:49 JVs for EV/hybrid powertrain; slump-sell EV motors business, DENSO to buy 49% at EV Rs 17,500 mn | "subject to customary conditions" (undated) | press 82-83; filing note 4/5 (270-278) | signed (definitive agreements 22-Jul-2026) |

---

## NOTES FOR A4 (questions to generate)
- FORWARD-SIGNAL findings: FD2, FD7, FD12.
- AMBIGUOUS findings: FD1, FD3, FD6, FD8, FD11.
- Priority: FD7 (DENSO — is the EV-motors slump-sale a divestment of a core EV asset, and how does it interact with control/block-sale tripwire 2?); FD9 (why is EBITDA margin 160 bps below FY26 while growth is foregrounded?); FD8 (closing order book and definition); FD1 (which basis anchors the headline set?).
