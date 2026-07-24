# A3 FORENSIC NOTES — Route Mobile Limited (ROUTE), Q1 FY27, INVESTOR PRESENTATION

Agent: A3 FORENSIC NOTES | Model: claude-opus-4-8
Inputs reconciled: A1 extract (561 lines) + A2 ledger (121 rows / 381 tokens).
Ledger reconciliation: 121 / 121 rows read verbatim at cited lines = 100%.
Unit convention: Millions (x0.1 to Rs Crores per A1 header).
Prior-quarter ledger: none available -> no verbatim DROPPED_SLIDE diff possible;
F16 run on within-deck reframing + Notion-checklist expectation gap, flagged
`NO_PRIOR_LEDGER` (not a gate failure).

Doctype applicability (per prompt): on a presentation F16 applies plus any
F6/F10/F11 numbers the deck carries; balance-sheet checks (F2-F5, F8, F9, F11,
F12, F15) are N.A.; F17 (concall silence) is N.A. F1 runs because the deck
carries ZERO_STANDING reconciliation rows on Slide 16.

---

## FINDINGS TABLE

| id | check | ledger row | line/slide | verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| FF1 | F1 | R106,R107,R103 | 479-480 / slide16 | "(+) Loss allowance – Capital advance (one time impact) ... 49.0"; "(+) Professional fees related to Masivian security incident remediation ... 13.6" | FORWARD-SIGNAL | Two brand-new add-back lines appear only in the 30.06.2026 column. Masivian security-incident remediation is an emerging recurring cost class (also hits GP, line 413); loss allowance on a capital advance signals a soured advance. ESOP-expense line (R103) fell to nil vs 5.7 a year ago. |
| FF2 | F6 | R85 | 412 / slide14 | "transitory traffic reduction at a large account pending new solution deployment - recovery expected" | FORWARD-SIGNAL | Dateable management commitment that gross-profit softness reverses once a new solution is deployed at one large account. Promise-vs-delivery item for next quarter; also a single-account concentration/lumpiness tell. |
| FF3 | F6 | (map graphic) | 219 / slide8 | "omin Soon)" [OCR: "Coming Soon)"] | FORWARD-SIGNAL | RCS direct-operator coverage in new markets flagged as forthcoming; soft, undated capability commitment to track for delivery. |
| FF4 | F13 | R26 | 120 / slide4 | "Board recommended ₹ 4 per share interim dividend" | NEUTRAL-FACT | Board outcome beyond results: interim dividend foreshadows a record date and cash outflow; capital-return signal, decision human. |
| FF5 | F14 | R59/R83,R82 | 236,273 vs 393 | chart "New Products Revenue"; bullet "New gen product revenues grew at 10.5% Q-o-Q and 13.9% Y-o-Y" | AMBIGUOUS | Same metric labelled two ways ("New Products" chart vs "New gen product" bullet). Bears directly on watchpoint (b): what is inside "New Products" and whether Truecaller BM is folded in. A4 question. |
| FF6 | F16 | R85 | 407-408 / slide14 | "Gross Profit Margin declined to 20.9% in Q1 26-27 vs. 23.3 % in Q4 25-26 as against 21.4% in Q1 25-26" | FORWARD-SIGNAL | Consol GM 20.9% BREACHES the pre-committed Q1 FY27 gate (GM >= 23%). Below the Section-8 red line (<22%), first of the two-quarter test. Decline reframed as transitory ("recovery expected"; Masivian). Gate-leg failure. |
| FF7 | F16 | R90,R92,R109,R102,R105,R106,R107 | 426,483,472,478-480 / slide15-16 | "EBITDA margin % on a Non-GAAP basis ... 9.5%"; "Adj. EBITDA decreased by 18.9% Q-o-Q and 5.6% Y-o-Y" | FORWARD-SIGNAL | Adj EBITDA margin 9.5% is BELOW the 10% thesis-broken line (Trigger 1) — first such quarter. Even 9.5% is flattered by net +34.5 mn of non-GAAP add-backs (−28.1 intangibles +49.0 loss allowance +13.6 Masivian); reported EBITDA margin = 1,054.8/11,515 = ~9.2%, deeper below 10%. One more sub-10% quarter = THESIS BROKEN. |
| FF8 | F16 | R53,R59,R82,R83 | 248,273,393,398 | "13.9% Y-o-Y growth"; chart "830 / 855 / 945"; "New gen product revenues grew at ... 13.9% Y-o-Y" | FORWARD-SIGNAL | New Products revenue YoY 13.9% is BELOW the 15% Trigger-3 threshold (checklist item 5). Mix = 945/11,515 = 8.2% of revenue, LOWER than the FY26 11.3% mix the thesis flagged — new-gen contribution shrinking as a share, not scaling to 15%. |
| FF9 | F16 | R48 (Truecaller); absent | 188 / slide7; deck-wide | "Expanded global enterprise visibility through a strategic partnership with Truecaller" | AMBIGUOUS | Truecaller BM shown as a partnership narrative with ZERO revenue/KPI attribution (watchpoints a/b, checklist item 13). Heltar acquisition (2026-07-13, item 14) is entirely absent from the deck. Both monitored items undisclosed -> A4 questions. |
| FF10 | F16 | R95,R111,R114 | 447,489,492 / slide15-16 | "Adj. PAT includes Forex gain of INR 6 mn in Q1 26-27, INR 181 mn in Q4 25-26 and forex loss of INR 247mn in Q1 25-26" | AMBIGUOUS | Adjusted PAT = Reported PAT for all three quarters (685.5/1,144.3/587.8) — forex is left INSIDE Adj PAT while the Adj EBITDA recon strips forex out. Q4's 1,144 Adj PAT carried a 181 mn forex tailwind, so the -40.1% QoQ Adj PAT drop is partly a forex-gain reversal, not pure operations. Inconsistent adjustment basis across the two recon tables. |

Non-finding context (checked, GREEN / not flagged):
- Top 10 client concentration (checklist item 6): R74, line 351 = 44% / 48% / 43% / 43%; Q1 FY27 = 43%, inside the <=45% green band. Top 50 = 75%, Top 5 = 31%. No concentration finding.
- Net Cash (checklist item 10): R22, line 109 = ₹13,452 mn = Rs 1,345.2 Cr, above the Rs 800 Cr green line. No finding.
- Revenue YoY (Q1 gate leg / binary): R79, line 390 = +9.6% YoY, clears the +1.8% bull binary and the >=0% gate leg. GM leg is what fails (FF6).
- DSO (checklist item 4): not computable — deck discloses no trade receivables; noted as an absent metric under F16/FF9 scope but not itself a finding.

---

## CHECKLIST SCORECARD (all 17)

| Check | Status | One-line basis |
|---|---|---|
| F1 ZERO-VALUE STANDING ITEMS | FINDING | FF1 — two new one-time add-back lines (loss allowance 49.0; Masivian remediation 13.6) appear only this quarter; ESOP line fell to nil. |
| F2 STANDALONE vs CONSOLIDATED | N.A. | Presentation carries consolidated figures only; no standalone column to decompose. |
| F3 SHELL-ENTITY DETECTION | N.A. | No standalone vs consolidated cost lines in a deck. |
| F4 UNAUDITED CONTRIBUTION | N.A. | No auditor Other-Matters paragraph in a presentation. |
| F5 GOING CONCERN / EoM | N.A. | No EoM/going-concern language; no prior ledger for diff. |
| F6 FORWARD-COMMITMENT MINING | FINDING | FF2 "recovery expected"; FF3 RCS "Coming Soon". |
| F7 HEDGE PHRASE MINING | N.A. | Hedge mining targets NOTES; deck is not a notes document. Substance (large-account/customer-specific softness) captured under FF2/FF6. |
| F8 TAX FORENSICS | N.A. | No PBT/tax breakdown or ETR derivable; only a TTM 166.9 tax-on-exceptional cell. |
| F9 OCI FORENSICS | N.A. | No OCI/actuarial disclosure in a deck. |
| F10 SHARE COUNT & DILUTION | PASS | EPS ₹9.94 (R24) and DPS ₹4 (R26) disclosed; no share count, no basic-vs-diluted spread — nothing dilutive to flag. |
| F11 RESERVES / NET WORTH | N.A. | No Other Equity / paid-up / net worth disclosed; net cash (₹13,452 mn) is treasury, not equity, and cannot tie to net worth without the balance sheet. |
| F12 SEGMENT FORENSICS | N.A. | No segment assets/liabilities in a deck. |
| F13 BOARD OUTCOME | FINDING | FF4 — board recommended ₹4/share interim dividend; record date/payout incoming. |
| F14 NOTE-DRAFTING INCONSISTENCY | FINDING | FF5 — "New Products Revenue" vs "New gen product revenues" naming drift for the same tracked metric. |
| F15 ENTITY LIST DIFFS | N.A. | No consolidation entity list in a deck; no prior ledger. |
| F16 DROPPED / REFRAMED DISCLOSURE | FINDING | FF6 GM gate breach 20.9%; FF7 Adj EBITDA 9.5%<10%; FF8 New Products YoY 13.9%<15%; FF9 Truecaller/Heltar undisclosed; FF10 Adj-PAT forex inconsistency. |
| F17 CONCALL SILENCE AUDIT | N.A. | Doctype is a presentation, not a transcript; silence items folded into FF9. |

Blank checks: none. GATE A3: pass (17/17 marked).

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | ref | status word |
|---|---|---|---|
| Gross-profit recovery once "new solution deployment" completes at one large account | near-term (next 1-2 quarters, undated) | line 412, slide 14 | underway |
| RCS direct-operator coverage in new markets ("Coming Soon") | undated | line 219, slide 8 | initiated |
| Interim dividend ₹4 per share (board recommended) | record date to follow | line 120, slide 4 | board-approved (initiated) |

---

## FORWARD-SIGNAL SUMMARY FOR A4

Gate/trigger status carried by this deck (for A4 to convert into management questions):
- Pre-committed Q1 FY27 gate: revenue leg PASS (+9.6% YoY) but GM leg FAIL (20.9% < 23%). Gate breached on GM.
- Trigger 1 (EBITDA margin <10% for 2 consecutive Q = THESIS BROKEN): Q1 FY27 Adj EBITDA margin 9.5% is the FIRST sub-10% quarter (reported basis ~9.2%). One more = broken.
- Trigger 3 / checklist item 5 (New Products YoY >=15%): 13.9%, below threshold; mix fell to 8.2% of revenue vs FY26 11.3%.
- Watchpoints a/b/13/14: Truecaller BM revenue unattributed, Truecaller-vs-"New Products" boundary unclear (naming drift FF5), Heltar acquisition unmentioned.
- Green/confirmatory: Top 10 concentration 43% (<=45%), net cash Rs 1,345 Cr (>= Rs 800 Cr), revenue YoY +9.6%.

---

```yaml
stage: A3-forensics
company: "ROUTE"
quarter: "Q1 FY27"
doctype: "presentation"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/route-q1fy27/work/forensics_presentation_route_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: N.A.
  F8: N.A.
  F9: N.A.
  F10: PASS
  F11: N.A.
  F12: N.A.
  F13: FINDING
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: N.A.
findings:
  - {id: "FF1", check: "F1", line: "479-480", classification: "FORWARD-SIGNAL", implication: "New one-time add-backs this quarter only: loss allowance on capital advance 49.0 and Masivian security-incident remediation 13.6; emerging recurring cost class."}
  - {id: "FF2", check: "F6", line: "412", classification: "FORWARD-SIGNAL", implication: "'recovery expected' after new solution deployment at one large account; dateable promise + concentration/lumpiness tell."}
  - {id: "FF3", check: "F6", line: "219", classification: "FORWARD-SIGNAL", implication: "RCS new-market coverage 'Coming Soon'; undated capability commitment to track."}
  - {id: "FF4", check: "F13", line: "120", classification: "NEUTRAL-FACT", implication: "Board recommended Rs 4/share interim dividend; record date and cash outflow incoming."}
  - {id: "FF5", check: "F14", line: "393", classification: "AMBIGUOUS", implication: "'New Products Revenue' vs 'New gen product revenues' naming drift; ambiguity on what is inside the tracked New Products line and Truecaller BM inclusion."}
  - {id: "FF6", check: "F16", line: "407", classification: "FORWARD-SIGNAL", implication: "Consol GM 20.9% breaches pre-committed 23% gate and Section-8 <22% red line; reframed as transitory."}
  - {id: "FF7", check: "F16", line: "483", classification: "FORWARD-SIGNAL", implication: "Adj EBITDA margin 9.5% below 10% thesis-broken line (first quarter); reported ~9.2%; flattered by net +34.5mn add-backs."}
  - {id: "FF8", check: "F16", line: "248", classification: "FORWARD-SIGNAL", implication: "New Products YoY 13.9% below 15% Trigger-3 threshold; mix 8.2% of revenue vs FY26 11.3% — contribution shrinking."}
  - {id: "FF9", check: "F16", line: "188", classification: "AMBIGUOUS", implication: "Truecaller BM revenue/KPI unattributed and Heltar acquisition absent from deck; monitored items 13/14 undisclosed."}
  - {id: "FF10", check: "F16", line: "447", classification: "AMBIGUOUS", implication: "Adj PAT leaves forex in (=Reported PAT all 3Q) while Adj EBITDA strips it out; Q4 Adj PAT carried 181mn forex tailwind, distorting the -40.1% QoQ."}
forward_signals: ["FF1", "FF2", "FF3", "FF6", "FF7", "FF8"]
ambiguous: ["FF5", "FF9", "FF10"]
commitments:
  - {commitment: "Gross-profit recovery after new solution deployment at one large account", implied_date: "near-term (undated)", ref: "line 412 / slide 14", status_word: "underway"}
  - {commitment: "RCS direct-operator coverage in new markets ('Coming Soon')", implied_date: "undated", ref: "line 219 / slide 8", status_word: "initiated"}
  - {commitment: "Interim dividend Rs 4 per share", implied_date: "record date to follow", ref: "line 120 / slide 4", status_word: "board-approved"}
gate_a3: pass
blank_checks: []
```
