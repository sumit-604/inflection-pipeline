# A3 FORENSIC NOTES: TATACOMM q2fy27 (doctype: presentation)

Company: Tata Communications Limited (TATACOMM)
Quarter: Q2 FY27 | Doctype: presentation (9 slides, earnings call deck, filed 15 Oct 2026)
Inputs read: A1 structured (runs/tatacomm-q2fy27/extracted/tatacomm-presentation-q2fy27-structured.md), A1 fulltext (runs/tatacomm-q2fy27/extracted/tatacomm-presentation-q2fy27-fulltext.md), A2 ledger (runs/tatacomm-q2fy27/work/ledger_presentation_tatacomm_q2fy27.md). Prior-quarter fulltext: ND. Notion checklist: NONE (pre-thesis read). Source PDF and inputs/ not opened.
Model: claude-opus-5-5

Scope note. This deck carries no consolidated financial table. It has no revenue, EBITDA, PAT, net debt, capex, share count or segment figures. The only financial numbers are the six Digital Margin labels on slide 6 (fulltext lines 137-151). Most results-filing checks are therefore N.A. by doctype. [DERIVED] marks arithmetic on two disclosed numbers. It is not an estimate of a missing number.

## 1. LEDGER RECONCILIATION (74 of 74 rows read at cited line = 100%)

All 74 structured IDs (R001-R074) were read in the structured file and at their cited fulltext line. Every ledger row is accounted for. A2 count test (74/74, orphan_ids []) confirmed.

Reconciliation exceptions (A1 extraction defects; pipeline QA, not company findings):

| ID | A1 cite | Actual fulltext location | Issue | Load-bearing? |
|---|---|---|---|---|
| R026 | line 122, value "6" levers | lines 122-128 name 5 levers ("Accelerated Network Growth", "Drive Profitability- Digital Portfolio", "Increase Mix - Platforms", "Sales Contribution", "Agility in Operations") | VALUE ERROR. Count is 5, not 6. A2 already flagged COUNT_DISCREPANCY. Fulltext supports 5. | No (deck structure count) |
| R005, R006 | line 21 | "400 051" / "400 001" sit on line 23 | line offset (2) | No |
| R010 | line 48 | "14:14:50 +05'30'" is line 49 (line 48 carries the date) | line offset (1) | No |
| R020 | line 146 | "-INR 886Cr" is line 147 | line offset (1); value correct | Yes (value verified) |
| R025 | line 185 | "with a single contract and a unified SLA" is line 187 | line offset (2) | No |
| R029 | line 20 | "2015" is on lines 29 and 32 (line 20 blank) | line offset (9) | No |
| R059 | line 111 | "Driving absolute EBITDA growth, NPS and ESAT" is line 112 (111 is title) | line offset (1) | No |
| R063 | line 32 | "October 14, 2026" is line 33 | line offset (1) | No |
| R069 | line 71 | "Such statements involve known and unknown risks, uncertainties and other factors" is line 74 | line offset (3) | No |
| R070 | line 78 | Not verbatim. Fulltext lines 77-78 read "These risks may cause actual results and performance of Tata Communications, or industry results, to differ materially from those expressed or implied by the forward-looking statements" | paraphrase in structured file | No |
| R032, R033 | lines 153, 176 (slide titles) | content at lines 158 and 181 | cite points to title | No |

R018 (CHART_LABEL_UNPAIRED). Confirmed. The text layer carries "-6.9%" (line 142) for Q1FY27 and no rupee label for that bar. Slide 6 was not rendered (A1 header, line 11). Absence of a Q1 rupee label is confirmed in the text layer only. Caption pairing: text-layer column positions put "Digital Margins / Q2FY27" (lines 142-143) under the -3.6% / -INR 107 Cr labels, "Digital Margins / Q1FY27" (lines 146-147) under -6.9%, and "Digital Margin in FY25" (line 151) under -9.7% / -INR 886Cr. This matches the A1 pairing.

## 2. FINDINGS TABLE

| id | check | ledger row ref | line / slide | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-01 | F16 | R017, R020, R067, R072 | L138, L147, L151 / slide 6 | "-INR 107 Cr" (Q2FY27) vs "-INR 886Cr" ... "Digital Margin in FY25" | AMBIGUOUS | One chart sets a single-quarter rupee loss beside a full-year rupee loss. The bar heights suggest an 88% cut. Q2 annualised = INR 428 Cr [DERIVED, 107 x 4], which is 48% of FY25. The real improvement is about a halving. A4: ask for the quarterly rupee series on a like-for-like basis. |
| A3-02 | F16 | R018 | L142 / slide 6 | "-6.9%" (Q1FY27, no rupee label in text layer) | AMBIGUOUS | The Q1 bar gives a percent only. The absolute Q1 to Q2 loss change cannot be read. The 330 bps QoQ margin gain [DERIVED] can come from revenue growth or from cost cuts, and the deck does not show which. A4: ask for the Q1FY27 rupee loss and the revenue vs cost split of the gain. |
| A3-03 | F16 | R019, R067, R072 | L151 / slide 6 | "Digital Margin in FY25" | AMBIGUOUS | The base period is two fiscal years back. FY26 and Q2FY26 are absent, so the deck gives no YoY comparator. Lean bear: a skipped year can hide a FY26 setback. A4: ask for FY26 and Q2FY26 Digital margin in percent and rupees. |
| A3-04 | F6 | R061, R016-R020 | L132 / slide 6 | "DIGITAL PORFOLIO ON THE PATH TO BREAKEVEN" | FORWARD-SIGNAL | Management states a breakeven path with no date, no margin definition (EBITDA, EBIT or contribution) and no definition of the portfolio. The trajectory is -9.7% (FY25) to -6.9% (Q1FY27) to -3.6% (Q2FY27), +610 bps in total [DERIVED]. At the last-quarter pace breakeven falls within about 1-2 quarters [DERIVED, linear; not a company statement]. This is a catalyst candidate for the Role 5 tracker. A4: ask for the breakeven quarter, the margin definition and the portfolio perimeter. |
| A3-05 | F16 | R016, R017, R019, R020 | L137-L138, L145-L147 / slide 6 | "-3.6%" "-INR 107 Cr" ; "-9.7%" "-INR 886Cr" | AMBIGUOUS | Implied Digital revenue (if margin = loss / Digital revenue): Q2FY27 about INR 2,930-3,010 Cr. FY25 about INR 9,080-9,190 Cr, or INR 2,270-2,300 Cr a quarter [DERIVED, rounding bands]. That puts Q2 about 30% above the FY25 quarterly average. Two readings fit: real growth, or a change in portfolio perimeter or definition. The observation that separates them is a restated FY25 on the current perimeter. A4 question. |
| A3-06 | F16 | R059, R027, R053 | L112, L115-L117 / slide 5 | "Driving absolute EBITDA growth, NPS and ESAT" | AMBIGUOUS | The plan goal is absolute EBITDA growth. It has no margin target, number or date. The earnings deck carries no consolidated revenue, EBITDA, PAT or net debt. Prior deck ND, so a dropped earlier target cannot be tested. Lean bear: a growth goal stated in absolute terms can sit beside margin dilution. A4: ask whether any earlier quantified target (margin, revenue) stands, changed or was withdrawn. |
| A3-07 | F16 | R042-R052, R058, R059, R060 | L85, L111 / slides 4-5 | "THE TEAM IS IN PLACE" ; "PLAN ON PAGE" | FORWARD-SIGNAL | The deck frames a reset: a new org structure (Network, Infra, Interaction and Services Towers, a Transformation Group, line 98-104) under "MD AND CEO Ganesh Lakshminarayanan" (L107-L109), plus a new one-page plan with 5 levers. A reset deck sets a new baseline for promise-vs-delivery. Prior-quarter tenure and structure ND. A4: ask when the structure took effect, which heads are new, and the timeline for each lever. |
| A3-08 | F16 | R021-R025, R033, R055, R056 | L184-L193 / slide 8 | "700+ agents live" ; "600K+ voice AI mins / month" ; "A leading insurer serving 37 million customers" | AMBIGUOUS | Both AI case studies name no client and attach no revenue, contract value or margin. The counts carry "+" floors and no period base. AI monetisation is unquantified. A4: ask for AI-platform revenue, the number of paying customers, and the contract term of the "single contract" (L187). |
| A3-09 | F6 | R054 | L162-L163 / slide 7 | "We've invested in GPU infrastructure in India" | AMBIGUOUS | This GPU capex is stated as complete, with no amount, capacity, utilisation or funding source. It brings forward depreciation and return-on-capital questions for the Digital portfolio. A4: ask for the GPU capex amount, capacity in use, and whether it sits inside the Digital margin on slide 6. |
| A3-10 | F16 | R011-R015, R040, R041 | L88-L90 / slide 4 | "70% of India's live Financial Services data traffic" ; "300 of Fortune 500 Customers" | NEUTRAL-FACT | The reach claims carry no source, measurement date or revenue share. They need verification before use as evidence. No forward direction. |
| A3-11 | F14 | R061 | L132, L70 / slides 6, 3 | "PORFOLIO" ; "in this presentations" | NEUTRAL-FACT | There are drafting errors on the deck's only quantitative slide title and in the safe harbour. This is immaterial alone. It is logged as a cumulative governance data point. |

## 3. CHECKLIST SCORECARD

| check | status | basis |
|---|---|---|
| F1 Zero-value standing items | N.A. | Presentation has no line-item template. Ledger zero_standing count = 0. |
| F2 Standalone vs consolidated | N.A. | No standalone or consolidated figures in deck. |
| F3 Shell-entity detection | N.A. | No cost lines in deck. |
| F4 Unaudited contribution ratio | N.A. | No auditor report in a presentation. |
| F5 Going concern / EoM tracking | N.A. | No EoM paragraph. Prior fulltext ND. |
| F6 Forward-commitment mining | FINDING | Lexicon hits: only "expected" at L71 inside safe-harbour boilerplate ("expected financial position"), not a commitment. Non-lexicon commitments at L85, L112, L122-L128, L132, L162-L163 were logged (A3-04, A3-09, register below). |
| F7 Hedge phrase mining | PASS | No lexicon hit ("may sometimes", "no assurance", "subject to", "evaluating", "exploring", "in discussions", "endeavour" absent). Safe harbour L70-L83 is standard boilerplate. No hedge is attached to the breakeven claim. |
| F8 Tax forensics | N.A. | No tax figures in deck. |
| F9 OCI forensics | N.A. | No OCI figures in deck. |
| F10 Share count and dilution | N.A. | Deck carries no paid-up capital, share count or EPS (ledger R001-R033 hold none). |
| F11 Reserves and net worth tie-out | N.A. | Deck carries no net worth or other-equity figure. |
| F12 Segment forensics | N.A. | No segment assets or liabilities. The Digital portfolio margin is covered under F16. |
| F13 Board outcome beyond results | N.A. | No board outcome in deck. The cover letter (L28-L34) is a Reg 30 deck filing only. |
| F14 Note drafting inconsistencies | FINDING | A3-11: "PORFOLIO" L132, "this presentations" L70. The cover letter is internally consistent (dated 15 Oct 2026 at L19, signed 2026.10.15 14:14:50 at L48-L49, before the 4:00 pm call at L33). |
| F15 Entity list diffs | N.A. | No consolidation list. Prior ND. |
| F16 Dropped and reframed disclosures | FINDING | A3-01, 02, 03, 05, 06, 07, 08, 10. Quarter vs year rupee mix, Q1 rupee label absent, FY26 skipped, no headline financials, reset framing. A dropped-metric test against the prior deck is not possible (prior ND). |
| F17 Silence audit | N.A. | Concall-specific check. Doctype is presentation. No Notion checklist exists (pre-thesis read). |

## 4. COMMITMENT REGISTER (from F6)

| commitment | implied date | ref | status word |
|---|---|---|---|
| Digital portfolio to reach breakeven | ND (no date stated) | slide 6, L132 | underway |
| Drive absolute EBITDA growth, NPS and ESAT | ND (no number or date) | slide 5, L112 | underway |
| Five plan levers: Accelerated Network Growth; Drive Profitability-Digital Portfolio; Increase Mix-Platforms; Sales Contribution; Agility in Operations | ND | slide 5, L122-L128 | initiated |
| GPU infrastructure in India (sovereign AI) | ND (stated in past tense, amount ND) | slide 7, L162-L163 | completed |
| Leadership team and Tower structure in place | ND | slide 4, L85 | completed |

## 5. QUESTIONS FLAGGED FOR A4 (from FORWARD-SIGNAL and AMBIGUOUS findings)

- A3-04: In which quarter does management expect Digital breakeven? Which margin does "Digital Margin" measure, and which businesses form the Digital portfolio?
- A3-01 / A3-02 / A3-03: What is the quarterly rupee Digital loss for each quarter of FY26, Q1FY27 and Q2FY27, on one perimeter?
- A3-05: Was FY25 Digital restated to the current perimeter? What is Digital revenue in Q2FY27?
- A3-06: Does any earlier quantified margin or revenue target still stand?
- A3-07: When did the Tower structure take effect, and which leaders are new in the last 12 months?
- A3-08: What are AI-platform revenue and the paying-customer count? What is the term of the insurer's single contract?
- A3-09: What is the GPU capex amount and utilisation, and is it inside the Digital margin?

```yaml
stage: A3-forensics
company: "TATACOMM"
quarter: "q2fy27"
doctype: "presentation"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/tatacomm-q2fy27/work/forensics_presentation_tatacomm_q2fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: N.A.
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: PASS
  F8: N.A.
  F9: N.A.
  F10: N.A.
  F11: N.A.
  F12: N.A.
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: N.A.
findings:
  - {id: "A3-01", check: "F16", line: "138,147,151 (slide 6)", classification: "AMBIGUOUS", implication: "Quarter rupee loss (-INR 107 Cr) charted beside full-year loss (-INR 886Cr); Q2 annualised INR 428 Cr [DERIVED] = 48% of FY25, a halving not an 88% cut"}
  - {id: "A3-02", check: "F16", line: "142 (slide 6)", classification: "AMBIGUOUS", implication: "Q1FY27 bar shows -6.9% with no rupee label in text layer; absolute Q1-to-Q2 change and revenue-vs-cost source of 330 bps gain not readable"}
  - {id: "A3-03", check: "F16", line: "151 (slide 6)", classification: "AMBIGUOUS", implication: "Baseline set at FY25; FY26 and Q2FY26 absent, no YoY comparator; lean bear, may mask an FY26 setback"}
  - {id: "A3-04", check: "F6", line: "132 (slide 6)", classification: "FORWARD-SIGNAL", implication: "Undated Digital breakeven claim; -9.7% to -6.9% to -3.6%; linear pace implies 1-2 quarters [DERIVED, not company statement]; catalyst candidate, margin and perimeter undefined"}
  - {id: "A3-05", check: "F16", line: "137-138,145-147 (slide 6)", classification: "AMBIGUOUS", implication: "Implied Digital revenue Q2FY27 ~INR 2,930-3,010 Cr vs FY25 ~INR 2,270-2,300 Cr per quarter [DERIVED], about +30%; growth or perimeter change"}
  - {id: "A3-06", check: "F16", line: "112,115-117 (slide 5)", classification: "AMBIGUOUS", implication: "Goal is absolute EBITDA growth, no margin target or number; deck has no consolidated financials; prior targets untestable (prior ND)"}
  - {id: "A3-07", check: "F16", line: "85,98-109,111 (slides 4-5)", classification: "FORWARD-SIGNAL", implication: "Reset framing: new Tower org and one-page plan with 5 levers; new promise-vs-delivery baseline"}
  - {id: "A3-08", check: "F16", line: "184-193 (slide 8)", classification: "AMBIGUOUS", implication: "AI case studies anonymised, '700+ agents live', '600K+ voice AI mins / month'; no revenue or contract value; AI monetisation unquantified"}
  - {id: "A3-09", check: "F6", line: "162-163 (slide 7)", classification: "AMBIGUOUS", implication: "GPU capex in India stated complete with no amount, capacity or utilisation; depreciation and return drag on Digital unknown"}
  - {id: "A3-10", check: "F16", line: "88-90 (slide 4)", classification: "NEUTRAL-FACT", implication: "Reach claims (70% of India FS live data traffic; 300 of Fortune 500) unsourced and undated; verify before use"}
  - {id: "A3-11", check: "F14", line: "132,70 (slides 6,3)", classification: "NEUTRAL-FACT", implication: "Drafting errors 'PORFOLIO' and 'this presentations'; cumulative governance data point only"}
forward_signals: ["A3-04", "A3-07"]
ambiguous: ["A3-01", "A3-02", "A3-03", "A3-05", "A3-06", "A3-08", "A3-09"]
commitments:
  - {commitment: "Digital portfolio to reach breakeven", implied_date: "ND", ref: "slide 6 L132", status_word: "underway"}
  - {commitment: "Drive absolute EBITDA growth, NPS and ESAT", implied_date: "ND", ref: "slide 5 L112", status_word: "underway"}
  - {commitment: "Five plan levers (Network Growth; Digital Profitability; Platforms Mix; Sales Contribution; Agility in Operations)", implied_date: "ND", ref: "slide 5 L122-128", status_word: "initiated"}
  - {commitment: "GPU infrastructure in India for sovereign AI", implied_date: "ND (past tense, amount ND)", ref: "slide 7 L162-163", status_word: "completed"}
  - {commitment: "Leadership team and Tower structure in place", implied_date: "ND", ref: "slide 4 L85", status_word: "completed"}
gate_a3: pass
blank_checks: []
analyst_note: "The deck's only financial content is the slide 6 Digital margin chart, and its framing flatters. It sets a single-quarter rupee loss (-INR 107 Cr) beside a full-year one (-INR 886Cr), skips FY26, and drops the Q1 rupee label. On a like-for-like annualised basis the loss halved; it did not fall 88%. The percent path (-9.7, -6.9, -3.6) is real and steep, so the undated breakeven claim is the deck's main catalyst candidate. Implied Digital revenue runs about 30% above the FY25 quarterly average [DERIVED]. A perimeter change would produce the same chart, so ask for a restated FY25. 'THE TEAM IS IN PLACE' plus 'PLAN ON PAGE' reads as a reset deck, with absolute EBITDA growth as the goal and no margin number; test against the results filing and the concall. A1 QA: R026 value is wrong (5 levers, not 6); nine rows carry cite offsets of 1 to 9 lines; R070 is a paraphrase. None is load-bearing; R020 value verified at L147."
```
