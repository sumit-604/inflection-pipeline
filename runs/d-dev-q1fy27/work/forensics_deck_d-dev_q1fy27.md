# A3 FORENSIC NOTES — DEE Development Engineers (D-DEV / DEEDEV / BSE 544198)
## Q1 FY27 (quarter ended 30 June 2026) — doctype = PRESENTATION (Investor Deck, 36 slides, filed 05 Aug 2026)

Model: claude-opus-4-8 | Stage: A3-forensics
Inputs read verbatim: deck A1 extract (lines 1-1243, all 36 pages); A2 ledger (all 132 FM / 34 FL / 26 OB / 34 CAP / 80 CH / supplementary rows, 100% read at cited lines); audited results A1 extract (DOC1, 17 pp) as the reconciliation authority; Notion thesis extract.
Ledger reconciliation: 100% (every A2 row read at its cited extract line before judging).

Doctype note: this is a **company-authored, unaudited, promotional** deck. F2/F3/F4/F5/F9/F13/F15 are structurally inapplicable (no standalone columns, no entity cost lines, no auditor Other-Matters / EoM / going-concern paragraph, no OCI line, no board-outcome resolutions, no prior-quarter deck baseline) and are marked N.A. with a one-line reason and a cross-reference to the same-day results filing where the item actually lives. F16 carries the selective-disclosure findings. Nothing is left blank (GATE A3).

---

## PART 1 — DECK-vs-FILING RECONCILIATION (the filing is the authority)

Every deck P&L figure ties to the same-day audited/limited-reviewed consolidated filing within rounding. **No genuine divergence found.**

| Line (Cr) | Deck (p16/p32) | Filing consol (DOC1 p11, lacs→Cr) | Tie |
|---|---|---|---|
| Revenue from Operations | 294.5 (p33 bar rounds to 295) | 29,446.22 = 294.46 | ✓ rounding |
| Op. EBITDA | 49.7 | 49.75 (anchor; margin 16.89%) | ✓ |
| Op. EBITDA margin | 16.9% | 16.89% | ✓ |
| Add: Other Income | 2.5 | 247.89 = 2.48 | ✓ |
| Less: Interest | 17.2 | 1,716.30 = 17.16 | ✓ |
| Less: D&A | 15.0 | 1,500.77 = 15.01 | ✓ |
| PBT | 20.1 | 2,005.43 = 20.05 | ✓ |
| Taxes | 4.0 | 397.13 = 3.97 | ✓ |
| PAT | 16.1 | 1,608.30 = 16.08 (parent-attributable 16.15) | ✓ |
| EPS (Diluted) | 2.32 | 2.32 | ✓ |

**Adjudication of A2's flagged Revenue ₹294.5/₹295 vs filing ₹294.46:** immaterial rounding (deck rounds to 0.1 Cr on p16/p32 and to whole Cr on the p33 bar label, line 1103). BENIGN. No basis divergence, no genuine restatement. The deck's "Op. EBITDA" is a non-GAAP construct (EBITDA before other income) that internally foots to PBT (49.7 + 2.5 − 17.2 − 15.0 = 20.0 ≈ 20.1). The tie is the *good* news of this deck; the forensic weight is entirely in what the deck does NOT say (Part 3, F16).

---

## PART 2 — FINDINGS TABLE

| ID | Check | Ledger ref | Line (deck / results) | Verbatim quote | Class | Forward implication |
|---|---|---|---|---|---|---|
| DF-01 | F1 | FM-016, OB-017/021/022, CAP-025 | deck 457; 508/510; 689-690 | "ROCE … NA"; Gas/Power "share not separately visible"; "Chennai … Engineering Service" (no MT) | AMBIGUOUS | Current ROCE suppressed to "NA" on the quarterly snapshot while p34 charts ROCE up to FY26 only — the one return metric that would expose ~10% returns against a high leverage base is the one blanked. A4 question. |
| DF-02 | F6 | FL-002/003/004/006/008/010/011 | deck 373, 380, 382, 392, 400, 475 | "expected to be recognized in the coming quarter"; "full benefit expected from Q2 FY27"; "supporting a gradual reduction in debt" | FORWARD-SIGNAL | Dateable commitments → promise-vs-delivery tracker (Commitment Register below). ~₹25 Cr deferred revenue and pellet "full benefit" both explicitly pinned to Q2 FY27 = testable next quarter. |
| DF-03 | F7 | FL-003, FL-013, FN-001, p28 | deck 371-373, 380, 821, 834-836 | "temporary disruptions arising from the geopolitical situation in the Middle East, along with customer-related issues"; "APTEL appeal ongoing for further optimization"; "near-term losses from tariff revisions are being addressed" | FORWARD-SIGNAL | Pre-emptive hedges. The Middle East / customer deferral hedge tells you Q2 revenue is contingent on those specific dispatches clearing; the "near-term losses" phrasing concedes the non-core segment is loss-making now. |
| DF-04 | F8 | FM-103/109/115 | deck 964-966 | Taxes 4.0 on PBT 20.1 | AMBIGUOUS | ETR ≈ 19.8% vs 25.17% statutory (~537 bps shield); deck gives no current/deferred split (filing shows consol deferred-tax *charge* 30.72 lacs vs a *credit* 26.41 in Q1 FY26 — a sign flip). Sub-statutory ETR (Thailand mix / one-offs) is a PAT-normalisation risk. A4 question. |
| DF-05 | F10 | SH-005; results item 6 | deck 1172 / results 88-98, 789 | deck: "No. Shares Outstanding 7.52 Cr"; results: "loan facility of Rs. 2,000 Crores from Bank of India … option … to convert the whole or part … into Equity Shares" | RED-FLAG | Deck shows only post-preferential share count and diluted EPS; it is silent on the ₹2,000 Cr Section 62(3) lender loan-to-equity conversion enabling resolution approved the SAME DAY — a large contingent dilution overhang. A4 must question. |
| DF-06 | F11 | SH-004; DECK_NO_BALANCE_SHEET | deck 1169 | "Market Capitalization ₹4,952 Cr." | AMBIGUOUS | Deck prints market cap and CMP but no net worth / book value / other-equity anywhere → P/B not computable from the deck. Filing tie-out: FY26 Other Equity 82,112.20 + paid-up 6,926.34 lacs = net worth ₹890.4 Cr (Notion match) → P/B ≈ 5.6x, undisclosed. |
| DF-07 | F12 | FM-046/047/048; CH-011 | deck 535-536 | "Heavy Fabrications: Q1 FY27 revenue stood at ₹15.3 crore in comparison to ₹14.8 crore in Q1 FY26, up 3.6% YoY" | CONFIRMATORY-NEGATIVE | +3.6% YoY is far below the 20% floor. This is potentially the FIRST of the two consecutive sub-20% Heavy-Fab quarters that trip Notion thesis-broken trigger #4. Deck shows no segment assets/liabilities (filing: Heavy-Fab liabilities 1,476→2,140 lacs QoQ). |
| DF-08 | F14 | FM-052/062/065; TARIFF_INCONSISTENCY | deck 391, 543, 818-820 | "₹5.224 per kWh" (p13) / "₹5.44/kWh" (p18) / "₹5.22/kWh … ₹5.437/kWh" (p27) | AMBIGUOUS | One tariff, four printed values across three slides. p27 (₹5.22) matches filing PSERC final ₹5.224 (results 658); p18's "revised … ₹5.44" is the FY27-escalated ₹5.437 rounded but mislabelled "revised" — reader-conflation risk. |
| DF-09 | F16 | (selective omission) | deck 818-821 vs results 462-468, 486-494 | deck: "APTEL appeal ongoing for further optimization"; results: "we are unable to determine whether any impairment is required" (Malwa, ₹5,082.67 lacs) + PSPCL EoM | RED-FLAG | The deck reframes the exact matter that carries a QUALIFIED review conclusion (Malwa impairment) and an Emphasis of Matter (PSPCL tariff) as an unambiguously positive tariff win. The words "unaudited," "limited review," "qualified," "impairment," "Emphasis of Matter" appear NOWHERE in 36 slides. Audit-qualification cure is a live thesis trigger; selective omission is itself the finding. |
| DF-10 | F16 | DECK_NO_BALANCE_SHEET; CH-058-067 | deck 1123-1136 (charts); 962 (interest) | p34 charts "FY22 … FY26"; "Interest Expenses … 49.8%" YoY | RED-FLAG | Leverage is the live concern (Notion ND/EBITDA 3.18x). The only leverage disclosure (p34 Debt/Equity and Net-Debt/EBITDA trend charts) STOPS at FY26 and omits the current Q1 FY27 value — the quarter that just absorbed a ₹300 Cr raise and a +49.8% YoY interest jump. No net debt / borrowings / working-capital figure anywhere. |
| DF-11 | F16 | FL-022; CH vs Notion | deck 862, 873, 888 | "Op.EBITDA Guidance: 19-20% margin by FY30" | FORWARD-SIGNAL | Notion recorded management's ">19% consol margin for FY27." The deck now shows 19-20% only "by FY30," with Q1 at 16.9%. The near-term margin bar appears to have been quietly pushed ~3 years out. Watch-item #1 not met and arguably softened. |
| DF-12 | F16 | FN-002 | deck 970 | "Q4FY26 Op. EBITDA includes a net positive impact on account of Labour Code" | AMBIGUOUS | The QoQ EBITDA decline (−24.5%, margin −134 bps) is measured against a Q4 base flattered by an unquantified Labour-Code one-off. In the filing that item sits in EXCEPTIONAL items (below EBITDA); folding it into "Op. EBITDA" for the comparator echoes the Q3 FY26 EBITDA-misclassification governance flag. Quantum undisclosed. |
| DF-13 | F16 | FL-016; CH-032-036 | deck 869, 885 (chart); vs 457/958 | "FY27E … 1,500 Cr" vs "Revenue ₹294.5 … (18.6)% QoQ" | FORWARD-SIGNAL | FY27E ₹1,500 Cr implies +31% on FY26 and requires ~₹402 Cr/qtr over 9M vs Q1's ₹294.5 Cr (annualised ~₹1,178 Cr) — and Q1 revenue fell 18.6% QoQ. Internally the Vision arithmetic is consistent (₹1,142→₹2,500 = ~21.6% CAGR ≈ stated ~22%); the tension is FY27 vs the current run-rate. |
| DF-14 | F17 (adapted) | monitoring checklist | deck 174-186 (order wins); DECK_NO_BALANCE_SHEET; OB-011/018 | order-win list contains no "BHEL," "HRSG," "Nooter Eriksen"; no working-capital line; no 30-Jun-2025 order-book comparative | CONFIRMATORY-NEGATIVE | Silence audit vs the 5 pre-committed watch items: WC normalisation (silent), BHEL conversion (silent; deck substitutes ₹387 Cr BPCL), HRSG additions ahead of Jun-27 Nooter Eriksen start (absent). The +92.5% YoY order-book claim's 30-Jun-2025 base is not shown (deck gives only FY25/FY26 year-end ₹1,228/₹1,940 and Jun-26 closing ₹2,428). |

---

## PART 3 — CHECKLIST SCORECARD (all 17; every check has exactly one status)

| # | Check | Status | One-line basis |
|---|---|---|---|
| F1 | Zero-value standing line items | **FINDING** | DF-01: ROCE "NA" (l.457), Gas/Power order-share slices blank (l.508/510), Chennai no capacity (l.689) — line items present, values withheld. |
| F2 | Standalone vs consolidated decomposition | **N.A.** | Deck presents CONSOLIDATED only (p16 "Consolidated," p32 "Consolidated P&L"); no standalone columns to decompose. Cross-ref filing: standalone PAT 10.52 vs consol 16.08. |
| F3 | Shell-entity detection | **N.A.** | Deck carries no entity-level cost lines (Cost of Materials / Employee Benefits by entity). Cross-ref filing p11 for the consol cost stack. |
| F4 | Unaudited contribution ratio | **N.A.** | Derives from the auditor's Other-Matters paragraph, which the deck does not reproduce. Cross-ref results para 8: 5 subsidiaries = PAT 555.96 lacs ≈ 34.6% of consol PAT, reviewed by other auditors — route to results-forensics. |
| F5 | Going concern / EoM scope tracking | **N.A.** | Deck reproduces no auditor EoM / going-concern paragraph; no prior-quarter deck to verbatim-diff. The *omission* of the qualified conclusion + EoM is captured as a FINDING under F16 (DF-09). |
| F6 | Forward-commitment phrase mining | **FINDING** | DF-02: dense dated commitments ("expected … coming quarter," "full benefit … Q2 FY27," "gradual reduction in debt") — see Commitment Register. |
| F7 | Hedge phrase mining | **FINDING** | DF-03: newly-framed hedges on revenue lumpiness (Middle East/customer deferral), ramp ("as utilization improves"), tariff ("further optimization"). |
| F8 | Tax forensics | **FINDING** | DF-04: ETR ≈19.8% vs 25.17% (~537 bps), no current/deferred split on deck; filing shows a deferred-tax sign flip (credit→charge). |
| F9 | OCI forensics | **N.A.** | Deck P&L (p32) stops at EPS; no OCI line. Cross-ref filing: consol OCI Q1 (4.98) driven by forex translation (56.76) offsetting actuarial 69.20 — verify at AR. |
| F10 | Share count and dilution | **FINDING** | DF-05: only diluted EPS + post-preferential 7.52 Cr shown; deck silent on same-day ₹2,000 Cr Sec 62(3) loan-to-equity conversion overhang. |
| F11 | Reserves and net-worth tie-out | **FINDING** | DF-06: market cap ₹4,952 Cr shown but zero net-worth/book-value disclosure → P/B (~5.6x vs filing net worth ₹890.4 Cr) not derivable from deck. |
| F12 | Segment forensics | **FINDING** | DF-07: Heavy Fabrication +3.6% YoY (₹15.3 vs ₹14.8 Cr) — possible first of two sub-20% quarters (thesis trigger #4); no segment assets/liabilities on deck. |
| F13 | Board outcome beyond the results | **N.A.** | Deck carries no board-outcome/AGM resolutions. Cross-ref results: 37th AGM + FY26 AR imminent (schedule Role-6 AR deep dive); authorised capital raised to ₹95 Cr "for future fund-raising" (results 713-720); director re-appointment term dates (Shikha Bansal→31.10.2030, Shruti Aggarwal→13.04.2030, B.K. Gupta continuation→11.07.2028). |
| F14 | Note-drafting inconsistencies | **FINDING** | DF-08: Malwa/Muktsar tariff printed four ways (₹5.224/₹5.22/₹5.437/₹5.44) across p13/p18/p27. |
| F15 | Entity-list diffs | **N.A.** | No prior-quarter deck/entity list to diff (A2 §11). Note: deck names 3 entities (DFIPL, MPPL, DEE Thailand); filing consolidates 6 (adds Molsieve Designs Ltd and Atul Krishan Bansal Foundation — the latter also a same-day related-party rent counterparty). |
| F16 | Dropped & reframed disclosures | **FINDING** | DF-09/10/11/12/13: selective omission of the qualified conclusion + Malwa impairment + PSPCL EoM; no balance sheet / net debt / WC, and p34 leverage charts stop at FY26; FY27 >19% margin bar deferred to FY30; Q4 EBITDA base flattered by unquantified Labour-Code one-off; FY27E ₹1,500 Cr vs ₹1,178 Cr annualised run-rate. |
| F17 | Silence audit | **FINDING** | DF-14 (adapted: no concall transcript this run; run against the deck as the quarter's disclosure vehicle). 3 of 5 watch items silent (WC, BHEL, HRSG/Nooter-Eriksen); Heavy-Fab addressed but negative. See Watch-Item table. |

**Tally: 0 PASS / 10 FINDING / 7 N.A.** (every check carries a status; every FINDING carries a line cite → GATE A3 satisfied.)

---

## PART 4 — WATCH-ITEM / SILENCE TABLE (deck tested against the 5 pre-committed Q1 FY27 monitoring items)

| # | Watch item | Deck coverage | Cite | Read |
|---|---|---|---|---|
| 1 | FY27 EBITDA margin path toward >19% | NOT met / SOFTENED — deck shows only "19-20% by FY30"; Q1 = 16.9% | 862/873/888; 960 | The near-term >19% bar (Notion) is deferred ~3 yrs. |
| 2 | Heavy Fabrication scaling | ADDRESSED — NEGATIVE, +3.6% YoY | 535-536 | Below 20%; possible trigger-4 quarter 1 of 2. |
| 3 | Working-capital normalisation | SILENT | (no BS in deck) | No WC / net-debt / borrowings figure anywhere. |
| 4 | BHEL order conversion | SILENT (substituted) | 180-182; 465 | Deck touts ₹387 Cr BPCL and a "USD 40 Mn+ LOI … conversion underway"; no BHEL. |
| 5 | HRSG additions ahead of Jun-27 Nooter-Eriksen start | ABSENT | 174-186 | No "HRSG" / "Nooter Eriksen" in the 36-slide deck. |
| open Q | 30-Jun-2025 base for +92.5% YoY order-book claim | NOT shown | OB-001/002/018 | Deck gives FY25/FY26 year-end (1,228/1,940) and Jun-26 closing (2,428) only — no Jun-25 comparative → the +92.5% claim base is unverifiable from the deck. |
| answered | Order book ₹2,428 Cr composition | ANSWERED | 500-511 | Closing book split: Process Piping 93% / Heavy Fab 7% (Gas, Power negligible). YTD Order Intake ₹780.87 Cr split 89/9/2. |

Terminology note (A2 TERMINOLOGY_CHECK, adjudicated): "Order Executed (YTD) ₹294.37 Cr" (p7, l.215) and "YTD Order Intake ₹780.87 Cr" (p17, l.494) are two DIFFERENT metrics (execution vs new-order intake) both labelled "YTD" — genuine reader-conflation risk, but not a data error. Route to A4 as a definitional-clarity question.

---

## PART 5 — COMMITMENT REGISTER (from F6, feeds Role-5 promise-vs-delivery tracker)

| Commitment | Implied date | Deck ref | Status word |
|---|---|---|---|
| ~₹25 Cr deferred revenue recognised | Q2 FY27 (coming quarter) | l.373 / l.478 | expected / deferred |
| Biomass pellet facility full benefit | Q2 FY27 | l.475 | expected |
| Pellet business meaningful revenue/profit/cash contribution | coming quarters | l.394 | expected |
| Pellet + power segment revenue ₹80 Cr | FY27 | l.392 / l.823 | estimated |
| Seamless pipe facility contributes meaningfully | as utilisation improves (undated) | l.380 | expected / ramp-up |
| Anjar pipe-fab unit scale-up | ongoing (undated) | l.382 | "continues to scale up steadily" |
| ₹300 Cr preferential proceeds reduce leverage & finance costs | near-term (₹225 Cr earmarked for debt) | l.386-388; l.459 | expected |
| Gradual reduction in debt | over coming quarters | l.400 | expected |
| Malwa tariff further optimisation (APTEL appeal) | ongoing / sub-judice | l.821 | "appeal ongoing" |
| Additional pellet capacity housed under InVIT | proposed (undated) | l.852-855 | proposed |
| Vision-2030: Rev ₹1,500/1,800/2,500 Cr (FY27E/28E/30E); EBITDA 19-20% & PAT 9-10% by FY30; FY27 order visibility ₹2,000 Cr | FY27E → FY30E | l.862-889 | guidance / estimate |

All the above are blanket-qualified by the p36 Safe Harbor (l.1200-1219), which the deck relies on in lieu of naming the audit qualification.

---

## GATE A3: PASS — all 17 checks carry an explicit status; all 10 FINDINGs are line-cited; ledger 100% reconciled.

```yaml
stage: A3-forensics
company: "D-DEV"
quarter: "Q1 FY27"
doctype: "presentation"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/d-dev-q1fy27/work/forensics_deck_d-dev_q1fy27.md"
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
  F11: FINDING
  F12: FINDING
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: FINDING
findings:
  - {id: "DF-01", check: "F1", line: "deck 457/508/510/689", classification: "AMBIGUOUS", implication: "ROCE 'NA' + blank order-share/capacity slices; current return metric suppressed while p34 charts ROCE only to FY26"}
  - {id: "DF-02", check: "F6", line: "deck 373/475/400", classification: "FORWARD-SIGNAL", implication: "dated commitments (deferred rev + pellet full benefit both Q2 FY27; gradual debt reduction) -> tracker"}
  - {id: "DF-03", check: "F7", line: "deck 371-373/821/834", classification: "FORWARD-SIGNAL", implication: "pre-emptive hedges signal Q2 revenue contingency and conceded non-core losses"}
  - {id: "DF-04", check: "F8", line: "deck 964-966", classification: "AMBIGUOUS", implication: "ETR ~19.8% vs 25.17%; no current/deferred split; deferred-tax sign flip -> PAT normalisation risk"}
  - {id: "DF-05", check: "F10", line: "deck 1172 / results 91,789", classification: "RED-FLAG", implication: "deck silent on same-day Rs2,000 Cr Sec 62(3) loan-to-equity conversion dilution overhang"}
  - {id: "DF-06", check: "F11", line: "deck 1169", classification: "AMBIGUOUS", implication: "market cap shown, net worth/book value omitted; P/B ~5.6x undisclosed"}
  - {id: "DF-07", check: "F12", line: "deck 535-536", classification: "CONFIRMATORY-NEGATIVE", implication: "Heavy Fab +3.6% YoY; possible first of two sub-20% quarters (thesis trigger 4)"}
  - {id: "DF-08", check: "F14", line: "deck 391/543/818-820", classification: "AMBIGUOUS", implication: "Malwa tariff printed four ways; 'revised Rs5.44' mislabels FY27-escalated figure"}
  - {id: "DF-09", check: "F16", line: "deck 818-821 / results 462-468,486-494", classification: "RED-FLAG", implication: "selective omission: qualified conclusion + Malwa impairment + PSPCL EoM reframed as tariff win; 'unaudited/qualified/impairment' absent from 36 slides"}
  - {id: "DF-10", check: "F16", line: "deck 1123-1136/962", classification: "RED-FLAG", implication: "no balance sheet/net debt/WC; p34 leverage charts stop at FY26, omitting post-raise Q1 FY27 amid +49.8% YoY interest"}
  - {id: "DF-11", check: "F16", line: "deck 862/873/888", classification: "FORWARD-SIGNAL", implication: "FY27 >19% margin expectation deferred to '19-20% by FY30'; Q1 at 16.9%"}
  - {id: "DF-12", check: "F16", line: "deck 970", classification: "AMBIGUOUS", implication: "Q4 FY26 EBITDA base flattered by unquantified Labour-Code one-off folded into 'Op EBITDA'"}
  - {id: "DF-13", check: "F16", line: "deck 869/885", classification: "FORWARD-SIGNAL", implication: "FY27E Rs1,500 Cr vs Rs1,178 Cr annualised Q1 run-rate; Q1 revenue -18.6% QoQ"}
  - {id: "DF-14", check: "F17", line: "deck 174-186", classification: "CONFIRMATORY-NEGATIVE", implication: "silence on WC, BHEL, HRSG/Nooter-Eriksen; +92.5% YoY order-book base (30-Jun-2025) not shown"}
forward_signals: ["DF-02", "DF-03", "DF-11", "DF-13"]
ambiguous: ["DF-01", "DF-04", "DF-06", "DF-08", "DF-12"]
red_flags_to_a4: ["DF-05", "DF-07", "DF-09", "DF-10", "DF-14"]   # CONFIRMATORY-NEGATIVE/RED-FLAG; A4 must convert to management questions
commitments:
  - {commitment: "~Rs25 Cr deferred revenue recognised", implied_date: "Q2 FY27", ref: "deck l.373/478", status_word: "expected"}
  - {commitment: "Biomass pellet facility full benefit", implied_date: "Q2 FY27", ref: "deck l.475", status_word: "expected"}
  - {commitment: "Pellet + power segment revenue Rs80 Cr", implied_date: "FY27", ref: "deck l.392/823", status_word: "estimated"}
  - {commitment: "Preferential proceeds reduce leverage/finance costs", implied_date: "near-term", ref: "deck l.386-388", status_word: "expected"}
  - {commitment: "Gradual reduction in debt", implied_date: "coming quarters", ref: "deck l.400", status_word: "expected"}
  - {commitment: "Malwa tariff further optimisation (APTEL)", implied_date: "sub-judice", ref: "deck l.821", status_word: "ongoing"}
  - {commitment: "Additional pellet capacity under InVIT", implied_date: "undated", ref: "deck l.852-855", status_word: "proposed"}
  - {commitment: "Vision-2030 Rev Rs2,500 Cr / EBITDA 19-20% / PAT 9-10%", implied_date: "FY30", ref: "deck l.862-889", status_word: "guidance"}
gate_a3: pass
blank_checks: []
```
