# A3 FORENSIC NOTES — RateGain Travel Technologies Limited (RATEGAIN) — Q1 FY27 — Doctype: CONCALL

Agent: A3 Forensic Notes | Model: claude-opus-4-8
Inputs read verbatim: extract_concall (126 lines), ledger_concall (59 mgmt numbers /
14 fwd-hedge / 8 participants / 31 turns / 14 questions), extract_results (filing,
13 pp), extract_presentation (deck, 30 pp).
Ledger reconciliation: 100% (every ledger row read at its cited source line before judging).

Role 5 emphasis applied throughout: promise-vs-delivery, credibility, guidance changes,
tone/specificity, cross-reference to the filing/deck, and "what was NOT discussed"
(silence is signal). Balance-sheet checks (F1-F5, F8-F15) are results/deck-doctype checks
and are marked N.A. for this concall with a one-line reason each; their cross-reference
relevance is surfaced under F17.

---

## A. CROSS-REFERENCE RECONCILIATION (call number vs filing/deck)

Task-specified headline numbers stated on the call, reconciled to the results filing
(`extract_results`) and deck (`extract_presentation`). "PASS" = call figure reconciles;
no genuine contradiction found.

| Call figure (ledger #) | Call line | Filing / deck anchor | Reconciles? |
|---|---|---|---|
| Revenue Rs 785 Cr (#1/#25) | 8 / 34 | Deck p23 `785.0`; filing consol rev 7,850.12 mn = 785.0 Cr | PASS |
| Rev up 187.6% YoY (#25) | 34 | Deck p23 YoY `187.6%` (785.0/272.9−1) | PASS (CEO "188%" line 8 = rounding) |
| Adj EBITDA 24.6% / Rs 193.4 Cr (#4/#31) | 8 / 34 | Deck p9/p23 `193.4 (24.6%)` | PASS |
| Reported EBITDA 21.9% / Rs 171.5 Cr (#32) | 34 | Deck p23 `171.5 / 21.9%` | PASS |
| Adj PAT 14.9% / Rs 116.8 Cr (#34) | 34 | Deck p9/p23 `116.8 (14.9%)`, up 148.8% | PASS |
| Reported PAT 12.1% / Rs 94.9 Cr (#35) | 34 | Deck p23 `94.9 / 12.1%` | PASS |
| FCF Rs 135.2 Cr / 78.8% conversion (#41) | 36 | Deck p11 `78.8%`, p21 FCF `135.2` | PASS |
| Debt outstanding ~USD 77.5 M (#39, garbled "77 and 12 million") | 36 | Filing note 5 original loan USD 125 M; 125 − 47.5 repaid = 77.5 | PASS (arithmetic) |
| Net debt Rs 615.4 Cr (#44) | 36 | Deck p11 `615.4`; balance sheet p24: borrowings 533.5+337.5=871.0 − cash/bank/inv 255.6 = 615.4 | PASS |
| Adj EBITDA growth "289%" (#5) vs CFO "89.3%" (#31) | 8 / 34 | Deck p9/p23 Adj EBITDA YoY `289.3%` | RECONCILED — CFO "89.3%" is a dropped-digit transcription garble of 289.3%, NOT a contradiction; CEO's 289% is correct |

**No number stated on the call CONTRADICTS the filing.** All headline figures tie out.
The single internal `NUMBER_DISCREPANCY` (ledger #5 vs #31) resolves to the deck's 289.3%.
Two figures cannot be cross-verified because the filing/deck do not disclose them:
organic combined-entity growth **17.5%** (#3/#27, confirmed "in INR terms", line 55-56)
and organic MK/MarTech growth **18.2%** (#58, line 98) — management-only metrics, taken
at face value but unverifiable against audited statements (flag for A4).

Note (credibility, in the company's favour): organic 17.5% confirmed in INR resolves the
DIRECTION of thesis-broken trigger 1 (organic <6% for 2+ quarters) — comfortably clear
this quarter. Recorded as a confirmatory positive, not a finding.

---

## B. FINDINGS TABLE

| id | check | ledger row ref | line/turn | verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| FN1 | F6 | #21,#23 / FC3,FC4,FC6 | 28, 67 (T1/T12) | "we are revising 27 guidance ... around 3,100 crores ... adjusted margins of between 22 to 23[%] ... that's the number we should definitely beat" | FORWARD-SIGNAL | Guidance RAISED both lines: revenue to upper-end ~3,100 Cr (~70% YoY) and adj margin 22-23% from 21.5-22.5%. "Definitely beat" sets a hard promise-vs-delivery bar for Q2-Q4. Margin raise moves the goalposts on thesis-broken trigger 3 (miss of 200+bps now measured off 22-23%). |
| FN2 | F6 | FC1 | 8 (T1) | "we remain on track to retire the balance of our acquisition related debt and be net debt free by FY28" | AMBIGUOUS | "Net debt free by FY28" was asserted with NO mention of the USD 65.00 M corporate guarantee the board approved the SAME DAY (filing p13, Annexure B) for RateGain UK + Sojern Inc credit facilities to HSBC/JPM/Citi. Off-balance-sheet/incremental exposure the debt-runway narrative omits. |
| FN3 | F6 | FC7 / #53 | 91 (T20) | "our distribution business at the end of the fiscal year should start to show double digit growth" | FORWARD-SIGNAL | Distribution grew only 3.1% YoY (#29, deck p12 `3.1%`). Commitment to reach double-digit "by end of fiscal" is dateable (FY27 exit). Directly tracks thesis-broken trigger 4 (Distribution must return to positive YoY by Q1FY28 — currently positive but weak). |
| FN4 | F6 | FC8 / H6 | 109 (T26) | "I don't think anything will happen this year ... it'll be an event in 2027 ... we are very judicious about what we will do and what we will pay" | FORWARD-SIGNAL | Signals renewed M&A appetite in CY2027. In direct tension with FN2 (net-debt-free by FY28) and FN9 (new USD 65 M guarantee facility) — a further acquisition would re-lever. Catalyst-timeline item. |
| FN5 | F7 | #14,#15 / H1,H2,H3 | 12, 28 (T1) | "FIFA World Cup ... revenue up[lift] of $2.5 million. And we don't expect [it] to repeat at the same scale in Q2 ... Middle East ... from ~$970,000 a month ... to about $425,000 a month today" | FORWARD-SIGNAL | Q2 base contains a ~$2.5 M FIFA one-off that reverses plus a ~$0.5 M/month Middle East run-rate hole (from ~$970k to ~$425k). Net ~$1.5 M favourable swing this quarter unwinds next quarter — a mechanical Q2 headwind against the "definitely beat" promise. |
| FN6 | F7 | #48 / H4 | 73, 109 (T14/T26) | "our gross margins are 70% ... I would not commit to a higher gross margin at this point ... I'll have to come back to you in a couple of quarters" | FORWARD-SIGNAL | Gross margin declined to 69.2% Q1FY27 (deck p21) from 75.0-76.0% FY22-FY25 and 70.6% FY26 — a ~600bps structural step-down post-Sojern. Management explicitly refused to commit to recovery. Deck p21 itself flags "Increased AdSpend ... has an impact on Gross Margins." Margin-compression signal. |
| FN7 | F7 | #50,#58 / H5 | 79, 97-98 (T16/T22) | "saying that ... the new entit[y] contributing 30% might be a difficult and challenging number to come up with" / "it's very difficult to attribute ... but overall I can tell you our mk business organically grew about 18.2%" | AMBIGUOUS | Management REFUSED to isolate Sojern standalone margin (~30% analyst hypothesis) AND ex-Sojern MarTech growth (both `DECLINED_TO_CONFIRM`), yet volunteered organic MK growth of 18.2%. Internal inconsistency: attribution declared "impossible" then partially given. 18.2% MK-organic > 17.5% combined-organic implies non-MK organic (esp. Distribution 3.1%) is a drag. Masks Sojern actual-vs-plan (thesis-broken trigger 2 / synergies). |
| FN8 | F17 | (silence) | n/a on call; deck p8 | Deck p8: "ANKIT AGGARWAL — Interim + Deputy Chief Financial Officer" | CONFIRMATORY-NEGATIVE | The call never addresses the permanent-CFO timeline; the deck confirms the CFO is still INTERIM. Thesis pre-condition 3 (permanent CFO / no new transition) remains FAILING. Sustained silence on a known deteriorating governance item = confirmatory negative (Role 5). Open question Q10 DODGED. |
| FN9 | F17 | (silence) | n/a on call; filing p1/p13 | Filing: "approved issuance of Corporate Guarantee of up to USD 65.00 million to banks ... in respect of loan facilities to be availed by RateGain Technologies Limited, UK and Sojern, Inc." | AMBIGUOUS | Board-approved same day, disclosed in the results filing (Annexure B), NEVER mentioned on the call. Whether refinancing vs incremental is unstated. Undercuts the net-debt-free narrative (FN2). Open question Q7 DODGED — flag for A4 (total debt+guarantees; refinancing vs incremental; why omitted). |
| FN10 | F17 | #41 (silence) | 36 | "Free cash flow generation this quarter was strong at INR 135.2 cr with a conversion at 78.8% highest ever" | CONFIRMATORY-NEGATIVE | FCF/conversion asserted as a headline with NO cash-flow statement and no reconciliation of the 78.8% conversion base. First post-Sojern quarter; H1 cash-flow bridge not provided. Open question Q5 DODGED. |
| FN11 | F17 | (silence) | n/a on call; filing note 5/12 | Filing note 12: "Sojern Hong Kong Limited ... has been liquidated w.e.f 10 July 2026"; goodwill Rs 1,591.5 Cr (deck p24) | CONFIRMATORY-NEGATIVE | Call silent on goodwill/impairment triggers, Sojern actual-vs-plan, and the Sojern HK subsidiary liquidation (subsequent event in the filing). No liquidation gain/loss quantified. Open questions Q9 & Q15 DODGED. |
| FN12 | F17 | (silence) | n/a on call | Auditor report (filing p3/p8) carves out only the Employees Benefit Trust as other-auditor reviewed; ETR/FX/Labour/QIP untouched on call | CONFIRMATORY-NEGATIVE | No discussion of component-auditor coverage of Sojern subs (Q11), steady-state ETR (Q12; deck-implied ETR 25.7/120.6 = 21.3%, below 25.17% statutory), FX hedging (Q13), Labour Code provisioning (Q17), or the Rs 1,115 Cr QIP footprint (Q14). Five monitoring items with zero air-time. |
| FN13 | F17 | (deck cross-ref) | deck p11 / p21 | Deck p11: "10.7x LTV TO CAC — Compared to 14.5x in Q1FY26"; deck p21 gross margins fall to 69.2% | CONFIRMATORY-NEGATIVE | Two disclosed metrics DETERIORATED YoY (LTV:CAC 14.5x -> 10.7x; gross margin ~75% -> 69.2%) and neither was volunteered on the call. Attrition 14.0% (deck p14) also unmentioned. Open question Q6 (NRR/LTV:CAC sustainability) DODGED. Deteriorating metrics + silence = confirmatory negative. |
| FN14 | F7 | #55,#59 / and opening | 91, 103, 20, 44 | "that numbers is in tens of millions of dollars" (#55); "the level of experimentation ... never been higher since the past 20 years" (#59); "about to sign a very large deal in India"; "on the verge of signing a very large customer in the Middle East" | AMBIGUOUS | `UNQUANTIFIED_ANCHOR` + `QUALITATIVE_SUPERLATIVE` used in place of numbers on the highest-leverage claims (ARI booking-uplift value, marquee pipeline deals, record/highest-ever framing throughout). Pipeline optionality asserted without a figure — A4 should convert to a "quantify the pipeline / name the deal size" question. |

Findings raised only on applicable concall checks (F6, F7, F17). All balance-sheet
checks are N.A. by doctype (Section C), with cross-reference relevance rolled into
F17 where a filing/deck item was conspicuously absent from the call.

---

## C. CHECKLIST SCORECARD (all 17; every check has exactly one status)

| # | Status | One-line basis |
|---|---|---|
| F1 ZERO-VALUE STANDING ITEMS | N.A. | Concall transcript carries no financial-table line items; ledger records `ZERO_STANDING` not applicable. |
| F2 STANDALONE vs CONSOLIDATED | N.A. | No S-vs-C statements in the transcript; belongs to the results filing. |
| F3 SHELL-ENTITY DETECTION | N.A. | No standalone-vs-consolidated cost lines spoken; entity-level test is a filing check. |
| F4 UNAUDITED CONTRIBUTION RATIO | N.A. | Auditor "Other Matters" not present in a transcript; component-auditor silence flagged under F17 (FN12). |
| F5 GOING CONCERN / EoM SCOPE | N.A. | No going-concern / Emphasis-of-Matter paragraph in a transcript; no EoM to verbatim-diff. |
| F6 FORWARD-COMMITMENT MINING | **FINDING** | 8 forward commitments (FC1-FC8); raised guidance + net-debt-free FY28 + distribution double-digit + M&A-2027 (FN1-FN4). See Commitment Register. |
| F7 HEDGE PHRASE MINING | **FINDING** | 6 hedges (H1-H6): gross-margin non-commitment, FIFA/Middle East normalization, Sojern attribution refusal, plus unquantified/superlative substitution (FN5-FN7, FN14). |
| F8 TAX FORENSICS | N.A. | No ETR/deferred-tax discussion on the call; deck-implied ETR 21.3% noted, silence flagged F17 (FN12). |
| F9 OCI FORENSICS | N.A. | No actuarial/OCI content in the transcript. |
| F10 SHARE COUNT / DILUTION | N.A. | No paid-up capital / EPS spread discussed on the call. |
| F11 RESERVES / NET WORTH TIE-OUT | N.A. | Balance-sheet check; note CFO net worth Rs 2,114.2 Cr (#42) ties EXACTLY to deck p24 equity 2,114.2 — clean, no gap. |
| F12 SEGMENT FORENSICS | N.A. | Company reports a single segment (filing note 6, Ind AS 108); no segment asset/liability data on the call. |
| F13 BOARD OUTCOME BEYOND RESULTS | N.A. | Board-outcome check is a filing-doc check; the USD 65 M guarantee board approval (filing p13) is surfaced as call-silence under F17 (FN9). |
| F14 NOTE DRAFTING INCONSISTENCIES | N.A. | No note text / auditor letter inside a transcript to cross-check. |
| F15 ENTITY LIST DIFFS | N.A. | No consolidation entity list in the transcript; Sojern HK liquidation (filing note 12) flagged under F17 (FN11). |
| F16 PRESENTATION-SPECIFIC (DROPPED/REFRAMED) | N.A. | Primary doctype is the concall; deck-side reframe (CFO now "Interim + Deputy") captured via cross-reference under F17 (FN8). |
| F17 CONCALL SILENCE AUDIT | **FINDING** | Permanent CFO, USD 65 M guarantee, cash-flow statement, goodwill/impairment, Sojern HK liquidation, component auditor, ETR, FX, Labour Code, QIP, and deteriorating LTV:CAC/gross-margin all unaddressed (FN8-FN13). See Silence Table. |

GATE A3: pass (no blank checks; 17/17 statused).

---

## D. COMMITMENT REGISTER (from F6)

| Commitment | Implied date | Turn / line ref | Status word |
|---|---|---|---|
| Retire acquisition debt; be net debt free (FC1) | by FY28 | T1 / line 8 | underway (38% repaid, USD 47.5 M) |
| FCF conversion 75%+ for full year (FC2) | FY27 | T1 / line 8 | underway (78.8% Q1) |
| FY27 revenue ~Rs 3,100 Cr, upper end (FC3) | FY27 | T1 / line 28 | guidance-raised |
| FY27 adj EBITDA margin 22-23% (FC4) | FY27 | T1 / line 28 | guidance-raised |
| Grow 15-20% near-to-medium term, "higher end" (FC5/#45) | ongoing | T1 / line 28; T10 / line 61 | aspiration |
| Rs 3,100 Cr "the number we should definitely beat" (FC6) | FY27 | T12 / line 67 | committed (hard promise) |
| Distribution to "start to show double digit growth" (FC7) | end FY27 | T20 / line 91 | expected (from 3.1% now) |
| M&A "will be an event in 2027" (FC8) | CY2027 | T26 / line 109 | intended |

---

## E. WHAT WAS NOT DISCUSSED (F17 silence audit; consecutive-quarter count from thesis)

| Item (monitoring / open question) | On call? | Consec. quarters silent | Note |
|---|---|---|---|
| Permanent CFO / transition (Q10; pre-condition 3) | No (deck: "Interim + Deputy CFO") | 2+ (Rohan Mittal resigned May 2026) | FN8 — FAILING pre-condition, confirmed by silence |
| USD 65 M corporate guarantee (Q7) | No (filing Annexure B, board same day) | 1 (new this quarter) | FN9 — refinancing vs incremental unstated |
| H1/quarter cash-flow statement + FCF reconciliation (Q5) | No | 1st post-Sojern | FN10 |
| Goodwill impairment triggers / Sojern actual-vs-plan (Q9) | No | 1st post-Sojern | FN11 |
| Sojern HK liquidation gain/loss (Q15) | No (filing note 12) | 1 (subsequent event) | FN11 |
| Component-auditor coverage of Sojern subs (Q11) | No | 1st post-Sojern | FN12 |
| Steady-state ETR (Q12) | No (deck-implied 21.3%) | recurring | FN12 |
| FX hedging (Q13) | No | recurring | FN12 |
| Labour Code provisioning (Q17) | No (filing note 9, Rs 22.02 mn) | recurring | FN12 |
| Rs 1,115 Cr QIP footprint (Q14) | No | recurring | FN12 |
| NRR / LTV:CAC sustainability (Q6) | No (deck: LTV:CAC 14.5x->10.7x) | metric deteriorating | FN13 |
| Reported PAT margin path / FY27 reported target (Q3) | No | recurring | Not separately rowed; reported margin 12.1% vs adj 14.9% gap left unbridged on call |

Per Role 5: sustained silence on the CFO transition, on a deteriorating LTV:CAC and gross
margin, and on a same-day board-approved USD 65 M guarantee are the strongest confirmatory
negatives of this call.

---

## F. ANSWERED / PARTIAL / DODGED — open-questions scorecard (with cites)

- Q1 organic ex-Sojern growth + organic gross margin: **PARTIAL** — organic MK 18.2% given (line 98) but ex-Sojern attribution refused (line 97); organic gross margin not given.
- Q2 Sojern deferred consideration retention/earnout-linked: **ANSWERED** — "contingent on revenue growth and ITA targets over 3 years ... end in Q3 FI29" (line 34).
- Q3 reported PAT margin path / FY27 reported target: **DODGED** — no reported-margin target given.
- Q4 gross-margin floor: **PARTIAL** — "70% ... would not commit to higher ... come back in a couple of quarters" (lines 73/109).
- Q5 H1 cash-flow statement / FCF reconciliation: **DODGED** (FN10).
- Q6 NRR/LTV:CAC sustainability: **DODGED** (FN13; deck shows LTV:CAC fell to 10.7x).
- Q7 USD 65 M guarantee: **DODGED** (FN9).
- Q8 parent dividend / debt-service capacity: **DODGED**.
- Q9 goodwill impairment triggers / Sojern actual-vs-plan: **DODGED** (FN11).
- Q10 permanent CFO timeline: **DODGED** (FN8).
- Q11 component-auditor coverage: **DODGED** (FN12).
- Q12 steady-state ETR: **DODGED** (FN12).
- Q13 FX hedging: **DODGED** (FN12).
- Q14 Rs 1,115 Cr QIP footprint: **DODGED** (FN12).
- Q15 Sojern HK liquidation gain/loss: **DODGED** (FN11).
- Q16 integration full-completion date: **PARTIAL** — "people integration ... substantially complete" (lines 26); first phase "complete", phase 2 (revenue synergies) ongoing (line 10); no dated full-completion.
- Q17 Labour Code provisioning: **DODGED** (FN12).

Answered 1 / Partial 4 / Dodged 12 of 17 open questions.

---

## G. FLAGGED FOR A4 (management questions)

FORWARD-SIGNAL: FN1 (guidance-raise / "definitely beat" bar), FN3 (distribution
double-digit promise off 3.1%), FN4 (M&A 2027 vs net-debt-free), FN5 (Q2 FIFA/Middle
East reversal), FN6 (gross-margin step-down to 69.2%, no recovery commitment).

AMBIGUOUS: FN2 (net-debt-free claim omits USD 65 M guarantee), FN7 (Sojern attribution
refused yet 18.2% MK-organic given), FN9 (USD 65 M guarantee — refinancing vs incremental,
why omitted), FN14 (unquantified anchors / superlatives on marquee pipeline).

CONFIRMATORY-NEGATIVE (context, not new questions): FN8, FN10, FN11, FN12, FN13.

---

```yaml
stage: A3-forensics
company: "RATEGAIN"
quarter: "Q1 FY27"
doctype: "concall"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/rategain-q1fy27/work/forensics_concall_rategain_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: N.A.
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: N.A.
  F9: N.A.
  F10: N.A.
  F11: N.A.
  F12: N.A.
  F13: N.A.
  F14: N.A.
  F15: N.A.
  F16: N.A.
  F17: FINDING
findings:
  - {id: "FN1", check: "F6", line: "28,67", classification: "FORWARD-SIGNAL", implication: "Guidance raised both lines (rev ~3,100 Cr, adj margin 22-23%); 'definitely beat' sets hard promise bar and resets thesis-broken trigger 3 base"}
  - {id: "FN2", check: "F6", line: "8", classification: "AMBIGUOUS", implication: "Net-debt-free-by-FY28 asserted while same-day board-approved USD 65M guarantee omitted"}
  - {id: "FN3", check: "F6", line: "91", classification: "FORWARD-SIGNAL", implication: "Distribution double-digit-by-fiscal-end promised off just 3.1% YoY; tracks thesis trigger 4"}
  - {id: "FN4", check: "F6", line: "109", classification: "FORWARD-SIGNAL", implication: "M&A 'event in 2027' re-levering risk vs net-debt-free claim"}
  - {id: "FN5", check: "F7", line: "12,28", classification: "FORWARD-SIGNAL", implication: "Q2 mechanical headwind: FIFA $2.5M one-off reverses, Middle East run-rate halved"}
  - {id: "FN6", check: "F7", line: "73,109", classification: "FORWARD-SIGNAL", implication: "Gross margin stepped down to 69.2% (deck p21); management declined to commit to recovery"}
  - {id: "FN7", check: "F7", line: "79,97", classification: "AMBIGUOUS", implication: "Sojern/ex-Sojern attribution refused yet 18.2% MK-organic volunteered; masks Sojern actual-vs-plan (trigger 2)"}
  - {id: "FN8", check: "F17", line: "deck-p8", classification: "CONFIRMATORY-NEGATIVE", implication: "Permanent CFO silence; deck confirms 'Interim + Deputy CFO'; pre-condition 3 FAILING"}
  - {id: "FN9", check: "F17", line: "filing-p13", classification: "AMBIGUOUS", implication: "USD 65M board-approved guarantee never mentioned; refinancing vs incremental unstated"}
  - {id: "FN10", check: "F17", line: "36", classification: "CONFIRMATORY-NEGATIVE", implication: "FCF/78.8% headline with no cash-flow statement or reconciliation in first post-Sojern quarter"}
  - {id: "FN11", check: "F17", line: "filing-note12", classification: "CONFIRMATORY-NEGATIVE", implication: "Silence on goodwill/impairment, Sojern actual-vs-plan, and Sojern HK liquidation"}
  - {id: "FN12", check: "F17", line: "n/a-call", classification: "CONFIRMATORY-NEGATIVE", implication: "Component auditor, ETR, FX, Labour Code, QIP all unaddressed"}
  - {id: "FN13", check: "F17", line: "deck-p11", classification: "CONFIRMATORY-NEGATIVE", implication: "LTV:CAC 14.5x->10.7x and gross margin ~75%->69.2% deteriorated and undiscussed"}
  - {id: "FN14", check: "F7", line: "91,103", classification: "AMBIGUOUS", implication: "Unquantified anchors / superlatives ('tens of millions', 'very large deal', 'highest in 20 years') substitute for figures on marquee pipeline"}
forward_signals: ["FN1", "FN3", "FN4", "FN5", "FN6"]
ambiguous: ["FN2", "FN7", "FN9", "FN14"]
commitments:
  - {commitment: "Retire acquisition debt, net debt free", implied_date: "FY28", ref: "T1/line8", status_word: "underway"}
  - {commitment: "FCF conversion 75%+ full year", implied_date: "FY27", ref: "T1/line8", status_word: "underway"}
  - {commitment: "FY27 revenue ~Rs 3,100 Cr upper end", implied_date: "FY27", ref: "T1/line28", status_word: "guidance-raised"}
  - {commitment: "FY27 adj EBITDA margin 22-23%", implied_date: "FY27", ref: "T1/line28", status_word: "guidance-raised"}
  - {commitment: "Grow 15-20% higher end near-medium term", implied_date: "ongoing", ref: "T1/line28;T10/line61", status_word: "aspiration"}
  - {commitment: "Rs 3,100 Cr 'definitely beat'", implied_date: "FY27", ref: "T12/line67", status_word: "committed"}
  - {commitment: "Distribution double-digit growth", implied_date: "end-FY27", ref: "T20/line91", status_word: "expected"}
  - {commitment: "M&A 'event in 2027'", implied_date: "CY2027", ref: "T26/line109", status_word: "intended"}
gate_a3: pass
blank_checks: []
```
