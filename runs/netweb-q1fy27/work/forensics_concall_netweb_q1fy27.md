# FORENSIC NOTES — Netweb Technologies (NETWEB), Q1 FY27, CONCALL Transcript

Agent: A3 Forensic Notes | Model: claude-opus-4-8
A1 extract: /home/user/inflection-pipeline/runs/netweb-q1fy27/work/extract_concall_netweb_q1fy27.txt
A2 ledger: /home/user/inflection-pipeline/runs/netweb-q1fy27/work/ledger_concall_netweb_q1fy27.md
Ledger reconciliation: 100% (all 64 Table-4 figures, all 138 Table-2 turns, all 24 Table-5 phrases, count test and summary flags read verbatim at cited extract lines).

Doctype rule applied: on a concall F6 / F7 / F17 apply; balance-sheet checks F1-F5, F8-F12, F15 are N.A.; F13 / F14 / F16 are N.A. unless a board-outcome / presentation item appears in the transcript. F13 and F16 fire here (enabling resolution; order-book / strategic-order reframing + inventory-policy restatement). F14 does not (no notes / auditor letter exist in a transcript).

---

## FINDINGS TABLE

| id | check | ledger row ref | line/turn | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A1 | F6 | T4 #44 | line 96 / turn 34 | "it will remain 18 to 24 months but not beyond that" | FORWARD-SIGNAL | Conversion tenure LENGTHENED from prior "18 months" guide; revenue recognition on the ~10,410 Cr pipeline pushes right. |
| A2 | F6 | T4 #48-49 | line 122 / turn 47 | "8 to 12 weeks was earlier now we are measuring basically 16 to 20 weeks" | FORWARD-SIGNAL | Execution cycle roughly DOUBLED. The single most material timeline slip on the call; slows order-book-to-revenue and lengthens WC cycle. |
| A3 | F6 | T4 #38 | line 70 / turn 21 | "our margins will remain between 13 to 14%" | NEUTRAL-FACT | Margin guidance reaffirmed; Q1 operating EBITDA margin printed 14.7% (above range). |
| A4 | F6 | T4 #11,12,13,30-32,37 | line 36 / turn 4; line 44 / turn 8 | "order book stood at 25,069.35 million ... L1 position of 8,480.47 million and a pipeline of ~104,100 million" | NEUTRAL-FACT | Visibility set: OB ~2,506.9 Cr + L1 ~848 Cr + pipeline ~10,410 Cr. Two OB/pipeline figures TRANSCRIPTION_GARBLED (verify against deck). |
| A5 | F6 | T4 #33 vs #7 | line 44 / turn 8 vs line 36 / turn 4 | "order book may be around 40 to 45% ... on the AI side" | AMBIGUOUS | Order-book AI mix (40-45%) sits well below realised Q1 AI revenue mix (62%). Either AI mix reverts toward ~40% or OB understates AI; question for A4. |
| A6 | F6 | T4 #35; T5 10(48) | line 48 / turn 10 | "I'm not guiding on any for any new capex as such" | NEUTRAL-FACT | No major capex guided; capacity stated sufficient for 3,000-plus Cr turnover. Light/routine capex only. |
| A7 | F6/F13 | T4 #52,56; T5 74(176),86(200) | line 176 / turn 74; lines 216-228 / turns 94-100 | "enabling uh resolution which you took to raise capital if need be ... validity of 12 months" | FORWARD-SIGNAL | 1,200 Cr enabling resolution, 12-month validity, working capital for growth, debt or equity, explicitly NOT M&A ("No, M&A. Absolutely"). Funding round foreshadowed within 12 months. |
| A8 | F6 | T4 #53,54 | line 196 / turn 84 | "out of that 1,600 cr strategy order close to 430 cr was executed in this June quarter" | FORWARD-SIGNAL | ~1,170 Cr of the 1,600 Cr strategic order remains to execute; forward revenue runway. Note the Notion checklist milestone (1,734 Cr by H2 FY27) was NOT addressed. |
| A9 | F6 | T5 39(106) | line 106 / turn 39 | "we do not see it softening in next couple of quarter maybe year" | FORWARD-SIGNAL | Memory/component prices not expected to soften for "a couple of quarters maybe a year"; inventory days (110) and WC intensity stay elevated near-term. |
| A10 | F6 | T4 #58 | line 250 / turn 111 | "a 38% CAGGR at the ... national level ... for the next ... four years" | NEUTRAL-FACT | Macro TAM anchor; clarified AI product line only (line 254). |
| A11 | F6 | T4 #63; T5 130(288) | line 288 / turn 130 | "we are not focusing on exports actually" | NEUTRAL-FACT | Exports (4-5%) deprioritised; domestic-only near-term. |
| A12 | F6 | T5 49(126),52(132),76(180) | line 132 / turn 52; line 180 / turn 76 | "investments we cannot quantify at this point of time" | FORWARD-SIGNAL | Physical AI + quantum computing entered as new R&D verticals; zero revenue/capex/timeline quantified. Unquantified optionality and cost drag; question for A4. |
| A13 | F6 | T4 #50,59; T5 117(262) | line 262 / turn 117 | "we do not want the balance sheet to have any kind of fictitious asset ... R&D has been expensed off since day one" | NEUTRAL-FACT | R&D fully expensed, 125-person team, no capitalisation. Conservative; depresses reported PAT vs peers who capitalise. |
| A14 | F6 | T4 #39 (ARITHMETIC_FLAG) | line 70 / turn 21 | "when the turn turnover and company is growing at 90%" | AMBIGUOUS | "growing at 90%" conflicts with the 172.1% YoY revenue growth stated twice (turns 4/36, 5/38). Which base/period? Feeds Role 5 arithmetic check; question for A4. |
| B1 | F7 | T5 (whole table) | multiple | "if and when we need to raise capital we'll raise capital" (line 200) | AMBIGUOUS | Conditional-forward hedge on the capital raise is the one hedge with next-quarter signal; rest are confidentiality/no-guidance boilerplate (see F7 tally). |
| C1 | F13 | T4 #52,56; ZERO_STANDING | line 176 / turn 74; line 200 / turn 86 | "there was an enabling uh resolution ... we haven't raised" | FORWARD-SIGNAL | Board/AGM capital-raising enabling resolution live; 0 raised to date (ZERO_STANDING). Per F13, capital-raising enabling resolutions foreshadow a funding round. |
| D1 | F16 | T4 #42; T5 20(68),102(232) | line 68 / turn 20; line 232 / turn 102 | "we do not want to segregate uh both of them ... the strategic is the new normal" | AMBIGUOUS | Order-book / pipeline DEFINITION reframed: strategic orders (previously "not guiding") now merged into one pipeline pool. Breaks like-for-like comparability; reduces disclosure granularity. |
| D2 | F16 | T4 #40; T5 24(76) | line 76 / turn 24; line 72 / turn 22 | "we don't have the exact number of the last quarter sitting" | AMBIGUOUS | Prior-quarter comparatives withheld (pipeline was ~4,400 Cr ex-strategic; now merged ~10,410 Cr). Like-for-like pipeline/L1 growth unverifiable from the call. |
| D3 | F16 | T4 #61 (ACCOUNTING_POLICY_CHANGE) | line 270 / turn 121 | "we shifted our inventory valuation from FIFO to the moving weighted average method" | AMBIGUOUS | Inventory-policy change with prior-period balance sheet restated; NO magnitude quantified on the call. Verify restatement quantum and margin/PAT impact at the financials; question for A4. |
| E1 | F17 | Notion 10-pt + 13 QfM | see silence table | "we don't have that number handy" / items absent entirely | CONFIRMATORY-NEGATIVE | Nine of the 13 open QfM and five of the ten monitor points went unanswered/evaded (see table); sustained silence on concentration, net-debt composition, software share, promoter action. |

---

## F17 SILENCE AUDIT — "What Was NOT Discussed"

Baseline note: the 13 QfM originate from the same Q1 FY27 Section-A results review, so "consecutive quarters of silence" = 1 call (this one). Prior-quarter transcript was not supplied to this run, so any longer silence streak cannot be verified here and is left for Role 5.

### (a) Notion 10-point monitoring checklist

| # | Monitor item | Status on call | Ref | Note |
|---|---|---|---|---|
| 1 | CFO/PAT (annual) | PARTIAL | line 36 / turn 4 | PAT disclosed (853 Mn, 10.3%). Operating cash flow (CFO) NOT discussed; only net debt 1,999 Mn given. |
| 2 | CCC (80-100 green / >130 red) | ADDRESSED | line 38 / turn 5 | "cash conversion cycle as 30th June stood at 96 days" — GREEN. |
| 3 | Blackwell / strategic order exec (1,734 Cr by H2 FY27) | PARTIAL | line 196 / turn 84; line 296 / turn 134 | 430 Cr of 1,600 Cr executed; DB300/B300 named, "Blackwell" not. The 1,734 Cr-by-H2-FY27 milestone NOT addressed. |
| 4 | EBITDA margin (13-14%) | ADDRESSED | line 38 / turn 5; line 70 / turn 21 | 14.7% printed; 13-14% reaffirmed. |
| 5 | Skylus/Velox software revenue share (toward 8%) | NOT ADDRESSED | line 36 / turn 4 | "Tyron Skylas" named as a platform; NO software revenue share quantified. Velox not mentioned at all. |
| 6 | Customer concentration (Top10 <60%) | NOT ADDRESSED | — | No concentration figure given; competition answered only qualitatively. |
| 7 | Promoter stake sales | NOT ADDRESSED | — | Silent. |
| 8 | Inventory audit remediation | NOT ADDRESSED (as remediation) | line 270 / turn 121 | FIFO->WAvg policy change disclosed, but framed as "getting in line," not as remediation of a prior audit issue. |
| 9 | New strategic AI orders | PARTIAL | line 232 / turn 102 | "strategic is the new normal"; folded into pipeline, no discrete new-order value. |
| 10 | Chandelier Exit | NOT ADDRESSED | — | Silent (internal exit trigger; not a call topic). |

### (b) 13 open Questions-for-Management (Q1 Section-A review)

| Q | Topic | Verdict | Answering turn/line | Basis |
|---|---|---|---|---|
| Q1 | Strategic-order revenue split | ANSWERED SPECIFICALLY | line 196 / turn 84 | "430 cr was executed in this June quarter" (of 1,600 Cr). |
| Q2 | Net-debt swing + recv/inv/CCC | ANSWERED SPECIFICALLY | line 38 / turn 5; line 52 / turn 12 | Net debt 1,999 Mn; recv 86->78; inv 86->110; CCC 96. |
| Q3 | Finance cost / ST borrowings / when they fall | NOT ADDRESSED | — | Only net-debt total given; no finance-cost or short-term-borrowing detail, no "when they fall." |
| Q4 | AI mix 62% vs ~35% guided + durability | PARTIALLY ANSWERED | line 36 / turn 4; line 44 / turn 8 | 62% realised vs 40-45% order-book mix stated; durability EVADED (see A5). |
| Q5 | Customer concentration | EVADED | line 56 / turn 14 | Competition discussed; no Top-10 concentration number. |
| Q6 | EBITDA bridge / consistent margin denominator | EVADED | line 70 / turn 21; line 156 / turn 64 | Margin defended qualitatively (pricing power, not memory); no bridge; "growing at 90%" flag unreconciled (A14). |
| Q7 | HPC / Private Cloud growth & share | PARTIALLY ANSWERED | line 36 / turn 4 | Segment revenue given (HPC 1,252.94 Mn; PC 1,353.46 Mn); no growth rate or share breakout. |
| Q8 | 285k unreconciled share issuance | NOT ADDRESSED | — | Silent. |
| Q9 | Deferred-tax credit / normalised ETR | NOT ADDRESSED | — | Silent; no tax discussion on the call. |
| Q10 | Labour Codes reassessment | NOT ADDRESSED | — | Silent. |
| Q11 | Skylus/Velox software share | EVADED | line 274 / turn 123 | "very difficult at this point of time to give segment wise funnel"; no software share. |
| Q12 | Netweb Foundation materiality | NOT ADDRESSED | — | Silent. |
| Q13 | AGM capital-raising / ESOP resolutions | PARTIALLY ANSWERED | lines 176-228 / turns 74-100 | 1,200 Cr enabling resolution covered extensively; ESOP NOT addressed. |

Silence tally: 5 of 10 monitor points and 6 of 13 QfM NOT ADDRESSED / EVADED (Q3, Q5, Q6, Q8, Q9, Q10, Q11, Q12 unanswered or evaded). Per Role 5, sustained silence on customer concentration, finance-cost composition, software share, promoter action and the 285k share reconciliation is a confirmatory negative to carry into A4/A5.

---

## F7 HEDGE / NON-COMMITTAL TALLY (case-insensitive lexicon sweep)

14 distinct hedge / no-guidance / confidentiality turns (Table 5 confirms representative set; full sweep below):

1. line 48 / turn 10 — "I'm not guiding on any ... new capex" (no-guidance)
2. line 52 / turn 12 — "we've not found out uh what what trajectory will go" (no-decision)
3. line 84 / turn 28 — "we will not like to disclose too much" (confidentiality)
4. line 102 / turn 37 — "slightly difficult to say ... very difficult" (non-committal on 1H split)
5. line 122 / turn 47 — "can stretch a little bit or can be early" (execution-cycle hedge)
6. line 126 / turn 49 — "not guiding on revenue at all" (no-guidance)
7. line 132 / turn 52 — "investments we cannot quantify at this point of time" (no-quantum)
8. line 176 / turn 74 — "if at some stage we think we'll need to raise capital we'll look at it" (conditional)
9. line 200 / turn 86 — "if and when we need to raise capital we'll raise capital" (conditional; B1)
10. line 232 / turn 102 — "the strategic is the new normal" (reframing prior disclosure)
11. line 236 / turn 104 — "difficult beyond that sitting today to address" (non-committal on runway)
12. line 274 / turn 123 — "very difficult at this point of time to give segment wise funnel" (non-disclosure)
13. line 284 / turn 128 — "I would not like to comment anything more" (declines)
14. line 296 / turn 134 — "we are not disclosing it as a separate ... product skew" (non-disclosure, switches)

Assessment: only the two capital-raise conditionals (items 8-9, B1) carry a forward next-quarter signal; the rest are confidentiality/no-guidance boilerplate. On a concall these do not carry the pre-emptive legal-cover weight that a newly added NOTE hedge would, so F7 is a light FINDING (count logged) rather than a strong forward signal.

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | ref (turn/line) | status word |
|---|---|---|---|
| Pipeline conversion ~60% | over 18-24 months (LENGTHENED from 18mo) | turn 34 / line 96; turn 122 / line 272 | underway |
| Execution cycle 16-20 weeks (LENGTHENED from 8-12wk) | current run-rate | turn 47 / line 122 | underway |
| EBITDA margin maintained 13-14% | ongoing / FY27 | turn 21 / line 70 | maintained |
| Order book ~2,506.9 Cr + L1 ~848 Cr + pipeline ~10,410 Cr | as on 30-Jun-2026 | turn 4 / line 36; turn 8 / line 44 | reported |
| AI order-book mix ~40-45% | current | turn 8 / line 44 | reported |
| No major capex; light/routine only | ongoing | turn 10 / line 48 | maintained |
| 1,200 Cr enabling resolution (WC for growth, debt or equity, NOT M&A) | 12-month validity from AGM | turn 74 / line 176; turns 94-100 / lines 216-228 | approved, 0 drawn |
| Strategic order 430 Cr of 1,600 Cr executed | Q1 FY27 done; ~1,170 Cr remaining | turn 84 / line 196 | underway |
| Memory/component prices not softening | "next couple quarters maybe a year" | turn 39 / line 106 | in effect |
| National AI CAGR 38% | next 3-4 years (AI product line) | turn 111 / line 250; turn 113 / line 254 | guided (macro) |
| Exports deprioritised (~4-5%) | near-term | turn 130 / line 288 | maintained |
| Physical AI + quantum R&D verticals | unquantified; "coming quarters" | turn 4 / line 36; turns 50-52 / lines 128-132; turn 76 / line 180 | commenced |
| R&D fully expensed, 125-person team | ongoing policy | turn 117 / line 262; turn 52 / line 132 | maintained |
| Inventory valuation FIFO -> moving weighted average (prior period restated) | effective this quarter | turn 121 / line 270 | completed (magnitude undisclosed) |

---

## CHECKLIST SCORECARD (all 17)

| Check | Status | One-line basis |
|---|---|---|
| F1 Zero-value standing line items | N.A. | Concall, no balance-sheet template. Sole ZERO_STANDING row (capital raised = 0 vs 1,200 Cr resolution) handled under F6/F13 (A7/C1), not a template line item. |
| F2 Standalone vs consolidated | N.A. | No S-vs-C statements in a transcript. |
| F3 Shell-entity detection | N.A. | No entity-level cost lines in a transcript. |
| F4 Unaudited contribution ratio | N.A. | No auditor Other-Matters paragraph in a transcript. |
| F5 Going concern / EoM | N.A. | No EoM paragraph; no prior-quarter transcript supplied to diff. |
| F6 Forward-commitment mining | FINDING | 15-item commitment register; conversion tenure and execution cycle both LENGTHENED (A1, A2); enabling resolution, strategic-order runway, memory-price and new-vertical signals (A7-A12). |
| F7 Hedge-phrase mining | FINDING | 14 hedge/no-guidance turns tallied; only the capital-raise conditionals carry forward signal (B1). |
| F8 Tax forensics | N.A. | No ETR / deferred-tax discussion on the call (open QfM Q9 unanswered -> logged in F17). |
| F9 OCI forensics | N.A. | No OCI / actuarial disclosure in a transcript. |
| F10 Share count / dilution | N.A. | No share-count table; 285k unreconciled issuance (QfM Q8) unanswered -> logged in F17. |
| F11 Reserves / net-worth tie-out | N.A. | No equity schedule in a transcript. |
| F12 Segment forensics | N.A. | Segment revenue mentioned but no segment assets/liabilities to trend. |
| F13 Board outcome beyond results | FINDING | 1,200 Cr capital-raising enabling resolution (12-month validity) surfaced on the call foreshadows a funding round (C1). |
| F14 Note-drafting inconsistencies | N.A. | No notes / auditor letter in a transcript; ARITHMETIC_FLAG ("90%" vs 172.1%) captured as A14 under F6, not a drafting inconsistency. |
| F15 Entity list diffs | N.A. | No consolidation list; no prior-quarter transcript to diff. |
| F16 Dropped / reframed disclosures | FINDING | Order-book/strategic-order definition reframed (D1), prior-quarter comparatives withheld (D2), inventory-policy restatement unquantified (D3). |
| F17 Silence audit | FINDING | 5/10 monitor points and 6-of-13 QfM NOT ADDRESSED / EVADED (E1); confirmatory negative on concentration, finance-cost, software share, promoter action, 285k shares. |

GATE A3: pass — every check carries exactly one of PASS / FINDING / N.A.; no blanks.

---

## NEW DISCLOSURES SURFACED BY THE A2 LEDGER (routed to A4)

1. Inventory accounting-policy change FIFO -> moving weighted average, prior-period balance sheet RESTATED, no magnitude quantified (D3, line 270). AMBIGUOUS.
2. 1,200 Cr enabling resolution, working capital not M&A, 12-month validity (A7/C1, lines 176/216-228). FORWARD-SIGNAL.
3. Physical AI + quantum computing new R&D verticals, no revenue/capex/timeline (A12, lines 36/128/180). FORWARD-SIGNAL.
4. R&D fully expensed, 125-person team, no capitalisation (A13, line 262). NEUTRAL-FACT.

Two timeline LENGTHENINGS (conversion 18mo -> 18-24mo; execution 8-12wk -> 16-20wk) are the highest-priority forward signals for A4 to convert into management questions, alongside the 62%-realised-vs-40-45%-order-book AI-mix tension and the unquantified inventory restatement.

---

```yaml
stage: A3-forensics
company: "NETWEB"
quarter: "Q1 FY27"
doctype: "concall"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/netweb-q1fy27/work/forensics_concall_netweb_q1fy27.md"
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
  F13: FINDING
  F14: N.A.
  F15: N.A.
  F16: FINDING
  F17: FINDING
findings:
  - {id: "A1", check: "F6", line: "96 (turn 34)", classification: "FORWARD-SIGNAL", implication: "Conversion tenure lengthened 18mo -> 18-24mo; pipeline revenue pushes right."}
  - {id: "A2", check: "F6", line: "122 (turn 47)", classification: "FORWARD-SIGNAL", implication: "Execution cycle doubled 8-12wk -> 16-20wk; slower OB-to-revenue, longer WC cycle."}
  - {id: "A3", check: "F6", line: "70 (turn 21)", classification: "NEUTRAL-FACT", implication: "13-14% margin reaffirmed; Q1 printed 14.7%."}
  - {id: "A4", check: "F6", line: "36 (turn 4); 44 (turn 8)", classification: "NEUTRAL-FACT", implication: "OB 2,506.9cr + L1 848cr + pipeline ~10,410cr; two figures garbled, verify vs deck."}
  - {id: "A5", check: "F6", line: "44 (turn 8) vs 36 (turn 4)", classification: "AMBIGUOUS", implication: "Order-book AI mix 40-45% vs 62% realised; mix reverts or OB understates AI."}
  - {id: "A6", check: "F6", line: "48 (turn 10)", classification: "NEUTRAL-FACT", implication: "No major capex guided; capacity sufficient for 3,000+ cr."}
  - {id: "A7", check: "F6", line: "176 (turn 74); 216-228 (turns 94-100)", classification: "FORWARD-SIGNAL", implication: "1,200cr enabling resolution, WC not M&A, 12mo validity; funding round foreshadowed."}
  - {id: "A8", check: "F6", line: "196 (turn 84)", classification: "FORWARD-SIGNAL", implication: "430cr of 1,600cr strategic order executed; ~1,170cr revenue runway remains."}
  - {id: "A9", check: "F6", line: "106 (turn 39)", classification: "FORWARD-SIGNAL", implication: "Memory prices not softening for a couple quarters/year; inventory + WC stay elevated."}
  - {id: "A10", check: "F6", line: "250 (turn 111)", classification: "NEUTRAL-FACT", implication: "38% national AI CAGR 4yrs, AI product line only; macro TAM anchor."}
  - {id: "A11", check: "F6", line: "288 (turn 130)", classification: "NEUTRAL-FACT", implication: "Exports (4-5%) deprioritised; domestic-only near-term."}
  - {id: "A12", check: "F6", line: "132 (turn 52); 180 (turn 76)", classification: "FORWARD-SIGNAL", implication: "Physical AI + quantum new verticals, zero quantification; unquantified optionality/cost."}
  - {id: "A13", check: "F6", line: "262 (turn 117)", classification: "NEUTRAL-FACT", implication: "R&D fully expensed, 125-person team; conservative, depresses reported PAT vs capitalisers."}
  - {id: "A14", check: "F6", line: "70 (turn 21)", classification: "AMBIGUOUS", implication: "'growing at 90%' conflicts with 172.1% YoY stated twice; base/period unclear -> Role 5."}
  - {id: "B1", check: "F7", line: "200 (turn 86); 176 (turn 74)", classification: "AMBIGUOUS", implication: "Conditional capital-raise hedge is the one forward-signal hedge; rest boilerplate."}
  - {id: "C1", check: "F13", line: "176 (turn 74); 200 (turn 86)", classification: "FORWARD-SIGNAL", implication: "Capital-raising enabling resolution live, 0 drawn (ZERO_STANDING); funding round ahead."}
  - {id: "D1", check: "F16", line: "68 (turn 20); 232 (turn 102)", classification: "AMBIGUOUS", implication: "Order-book/pipeline definition reframed; strategic orders merged; comparability broken."}
  - {id: "D2", check: "F16", line: "76 (turn 24); 72 (turn 22)", classification: "AMBIGUOUS", implication: "Prior-quarter comparatives withheld; like-for-like pipeline/L1 growth unverifiable."}
  - {id: "D3", check: "F16", line: "270 (turn 121)", classification: "AMBIGUOUS", implication: "Inventory policy FIFO->WAvg, prior period restated, magnitude undisclosed; verify impact."}
  - {id: "E1", check: "F17", line: "silence table (multiple)", classification: "CONFIRMATORY-NEGATIVE", implication: "5/10 monitor pts and 6/13 QfM unanswered/evaded; concentration, finance-cost, software share, promoter action, 285k shares silent."}
forward_signals: ["A1", "A2", "A7", "A8", "A9", "A12", "C1"]
ambiguous: ["A5", "A14", "B1", "D1", "D2", "D3"]
commitments:
  - {commitment: "Pipeline conversion ~60%", implied_date: "18-24 months (lengthened from 18mo)", ref: "turn 34/line 96; turn 122/line 272", status_word: "underway"}
  - {commitment: "Execution cycle 16-20 weeks (from 8-12wk)", implied_date: "current run-rate", ref: "turn 47/line 122", status_word: "underway"}
  - {commitment: "EBITDA margin 13-14%", implied_date: "ongoing FY27", ref: "turn 21/line 70", status_word: "maintained"}
  - {commitment: "OB ~2,506.9cr + L1 ~848cr + pipeline ~10,410cr", implied_date: "as on 30-Jun-2026", ref: "turn 4/line 36; turn 8/line 44", status_word: "reported"}
  - {commitment: "AI order-book mix ~40-45%", implied_date: "current", ref: "turn 8/line 44", status_word: "reported"}
  - {commitment: "No major capex; light/routine only", implied_date: "ongoing", ref: "turn 10/line 48", status_word: "maintained"}
  - {commitment: "1,200cr enabling resolution (WC, debt or equity, NOT M&A)", implied_date: "12-month validity", ref: "turn 74/line 176; turns 94-100/lines 216-228", status_word: "approved-0-drawn"}
  - {commitment: "Strategic order 430cr of 1,600cr executed (~1,170cr left)", implied_date: "Q1 FY27 done", ref: "turn 84/line 196", status_word: "underway"}
  - {commitment: "Memory/component prices not softening", implied_date: "couple quarters maybe a year", ref: "turn 39/line 106", status_word: "in-effect"}
  - {commitment: "National AI CAGR 38% (AI product line)", implied_date: "next 3-4 years", ref: "turn 111/line 250", status_word: "guided"}
  - {commitment: "Exports deprioritised (~4-5%)", implied_date: "near-term", ref: "turn 130/line 288", status_word: "maintained"}
  - {commitment: "Physical AI + quantum R&D verticals", implied_date: "unquantified/coming quarters", ref: "turn 4/line 36; turns 50-52/lines 128-132", status_word: "commenced"}
  - {commitment: "R&D fully expensed, 125-person team", implied_date: "ongoing policy", ref: "turn 117/line 262", status_word: "maintained"}
  - {commitment: "Inventory valuation FIFO -> moving weighted average (prior period restated)", implied_date: "effective this quarter", ref: "turn 121/line 270", status_word: "completed"}
gate_a3: pass
blank_checks: []
```
