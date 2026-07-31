# A3 FORENSIC NOTES — DATAPATTNS Q1 FY27 — DOCTYPE: CONCALL

Agent: A3 Forensic Notes (Opus 4.8). Source of truth read verbatim:
- A1 extract: `runs/datapattns-q1fy27/work/extract_concall_datapattns_q1fy27.txt` (175 native transcript lines; body file lines 55-225)
- A2 ledger: `runs/datapattns-q1fy27/work/ledger_concall_datapattns_q1fy27.md` (84 turns, 39 questions, 66 mgmt numbers, 29 forward-commitment phrases, 14 hedges)
- Prior-quarter extract: **NONE on file** — every "consecutive quarters of silence" count and every EoM/entity verbatim-diff that requires the prior transcript is flagged UNVERIFIABLE-THIS-RUN and handed to A4/A5 to backfill from Notion. I do not count from memory.

**Ledger reconciliation: 100%.** All 84 turn rows, all 39 question rows, all 66 management-number rows, all 29 forward-commitment rows and all 14 hedge rows were read at their cited file line in the extract before judging. Line/turn cites below use the transcript's native turn numbering (matches A2); file-line equivalents are turn# + 46 for turns 9-173.

**Doctype note.** This is a concall. Per the checklist doctype rule, the balance-sheet/results checks (F1-F5, F8-F14) have no source object in a transcript and are marked N.A. with basis. F6/F7/F17 are the load-bearing checks and are all FINDING. F15 is FINDING (a new group entity was disclosed verbally). F16 is FINDING and is used here as the cross-document reconciliation home (concall spoken numbers vs the investor deck and the filing baseline), per the task's explicit weighting toward cross-doc reconciliation.

Internal arithmetic sanity of the CFO's spoken P&L (turn 11) checks out: GP 91.5/116 = 78.9%; EBITDA 31.4/116 = 27.1%; PAT 22.1/116 = 19.05%. Gross profit +16% YoY against revenue +17% YoY = gross-level compression, consistent with the stated mix/employee-cost drag. The reconciliation exceptions are all cross-document (deck) and are captured in F16.

---

## FINDINGS TABLE

| id | check | ledger row ref | line/turn | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-01 | F6 | fwd-phrase — | turn 9 | "employee cost base is expected to remain elevated over the coming quarters" | FORWARD-SIGNAL | Margin drag is guided to persist beyond Q1; the 27% EBITDA print is not a one-quarter dip. Feeds Q3 (H2 bridge) doubt. |
| A3-02 | F6 | fwd #10-12; num #28-30 | turn 33 | "should happen before December ... maybe next two years time this contract start happen" | FORWARD-SIGNAL | SPJ-230 flight trials dated to Dec-2026; commercial contract ~2yr out. Dated milestone for the promise-vs-delivery tracker. Size withheld (see A3-12). |
| A3-03 | F6 | num #45 | turn 73 | "not the revenue but product intake this year" | FORWARD-SIGNAL | BrahMos seeker = order intake FY27, revenue lags. Answers pre-committed Q12 on timeline; value still unquantified. |
| A3-04 | F6 | num #36 | turn 45 | "we are L1 in one large contract I didn't comment on it because ... we are undergoing negotiation" | FORWARD-SIGNAL | EW/large tender L1 confirmed but value withheld pending negotiation; announcement is a near-term catalyst. Partial answer to pre-committed Q18. |
| A3-05 | F6 | num #54 | turn 117 | "given ourselves in a 3 to four months time to see that we take a decision" | FORWARD-SIGNAL | Space-business go/no-go dated ~Nov-2026, contingent on government funding clarity ("still unsure"). Dateable decision point. |
| A3-06 | F6 | num #56 | turn 153 | "I've given myself 9 months and contacts can happen much before that" | FORWARD-SIGNAL | Self-imposed 9-month deadline on the Rs 20bn single-vendor inflow. A management-set clock A5 can hold them to next 2-3 quarters. |
| A3-07 | F6 | num #52-53 | turn 109 | "200 crores plus ... 15 200 crores minimum that based on the requirements" | FORWARD-SIGNAL | Capex floor set verbally at Rs 200 Cr+; see A3-17 for the deck-vs-call reconciliation (guidance RAISED). |
| A3-08 | F7 | hedge #8, #9 | turns 85, 89 | "I don't know. I'm not classified accordingly" / "I have not classified it ... I don't have a needed answer" | CONFIRMATORY-NEGATIVE (EVASION) | Order-book production-vs-development split refused TWICE consecutively on the same question. Sustained opacity on order-book quality — the single most decision-relevant cut of the Rs 2,654 Cr. A4 must re-ask. |
| A3-09 | F7 | hedge #1 | turn 21 | "we can't be specific because it involves customers and I can't talk about open channel" | CONFIRMATORY-NEGATIVE (EVASION) | Revenue-slippage quantum withheld (pre-committed Q4). Slippage direction admitted, magnitude opaque — lean bear. |
| A3-10 | F7 | hedge #2, #3 | turn 33 | "it's not appropriate to talk about a future order" | NEUTRAL-FACT (EVASION) | SPJ-230 deal size ("several thousand crores") withheld; a number "in mind" exists but is not disclosed. |
| A3-11 | F7 | hedge #14 | turn 165 | "I don't want to say this because I have no control over the market" | AMBIGUOUS (EVASION) | Rs 40,000 Cr TAM realization timeline refused — TAM is undated, so it is a scale claim not a cadence claim. A4 question. |
| A3-12 | F15 | participants; num — | turn 53 | "yesterday only finalized with the go and we need to spend more time" | FORWARD-SIGNAL | New group entity (ST Advance / "STAC"), acquisition closed ~30-Jul-2026, one day before the call. 8 of the 18 pre-committed questions (net worth, outlay, turnover, arm's-length, incorporation/country, accretion basis, approvals, consolidation date) are ALL unanswered. Material entity change; A4 must build the STAC question block. |
| A3-13 | F16 | num #15 | turn 11 | "cash bank balances and investments of rupes 530 cr as on 30th June 2026" | AMBIGUOUS | Concall Rs 530 Cr vs deck Rs 465.9 Cr (Rs 4,659 Mn) = ~Rs 64 Cr unexplained gap on the same 30-Jun date. Lean bear: the higher spoken figure may fold in items the deck excludes. A4 reconcile. |
| A3-14 | F16 | num #16, #1/#17 | turn 11 | "Our audible stands at 920 cr ... the order currently stands at 2654 cr" | AMBIGUOUS | Concall confirmed order book Rs 920 Cr vs deck Rs 927.7 Cr. Note the deck figure reconciles the total cleanly (927.7 + 1,726.3 = 2,654.0) whereas the spoken 920 + 1,726 = 2,646 leaves a Rs 8 Cr gap — the spoken Rs 920 Cr is the rounded/soft number. A4 confirm against filing. |
| A3-15 | F16 | num #52-53 vs deck | turn 109 | "200 crores plus ... 200 crores minimum" | FORWARD-SIGNAL | Capex guidance RAISED vs deck Rs 150 Cr over 2 yr (a ~33%+ step-up, stated verbally only). Against FY26 cash conversion CFO/PAT ~0.30x and no QIP-deployment or funding comment, this widens the funding-gap question (pre-committed Q15). |
| A3-16 | F16 | num #4, #5 vs #12 | turn 9 / 11 | "2025% revenue growth while maintaining aid margins in 35 to 40% range" | AMBIGUOUS | Guidance = 20-25% revenue / 35-40% EBITDA (ASR-garbled "2025%"). Q1 actual EBITDA is 27% — an 8-13pp H2 bridge that management left qualitative (pre-committed Q3). Directional only until deck/filing corroborate. |
| A3-17 | F16 | num #51, #57, #58-60 | turns 105, 153, 161 | "40 to 50 billion ... 40,000 50,000 crores" | AMBIGUOUS | TAM stated three ways with a live unit self-correction; converges on ~Rs 40,000 Cr (30,000 + 10-12,000). Transcription artifact, not an anchored figure — treat as directional. |
| A3-18 | F17 | Section 4/checklist | see table | (multiple metrics with NO utterance on the call) | CONFIRMATORY-NEGATIVE | Silence on CFO/OCF, DSO/receivable days, QIP deployment, Labour Code, OCI swing, customer concentration, STAC financials, and auditor/board sequencing. Sustained silence on the cash-conversion crack is the confirmatory negative per Role 5. See silence table. |

Findings flagged for A4 to convert into management questions (rule 5): FORWARD-SIGNAL and AMBIGUOUS ids — A3-01, A3-02, A3-03, A3-04, A3-05, A3-06, A3-07, A3-11, A3-12, A3-13, A3-14, A3-15, A3-16, A3-17. EVASION findings A3-08 and A3-09 are confirmatory negatives but also handed to A4 (conservative bias, rule 6) as re-ask candidates.

---

## CHECKLIST SCORECARD (all 17)

| Check | Status | One-line basis |
|---|---|---|
| F1 ZERO-VALUE STANDING LINE ITEMS | N.A. | Concall carries no financial line-item table; A2 marks ZERO_STANDING N/A (turn 11 is narrative, not a tabulated statement). |
| F2 STANDALONE vs CONSOLIDATED | N.A. | No standalone/consolidated statements in a transcript; no S-vs-C gap to decompose. |
| F3 SHELL-ENTITY DETECTION | N.A. | No cost lines to compare S vs C; STAC and the aggregation/composites subsidiary are discussed qualitatively only (turns 53, 121) — captured under F12/F15/F17, not here. |
| F4 UNAUDITED CONTRIBUTION RATIO | N.A. | No auditor Other Matters paragraph in a concall. |
| F5 GOING CONCERN / EoM SCOPE | N.A. | No EoM/going-concern language; and no prior-quarter extract on file to verbatim-diff against. |
| F6 FORWARD-COMMITMENT PHRASE MINING | **FINDING** | 29 forward-commitment phrases across 16 mgmt turns (A2 Section 5); dateable milestones extracted to the Commitment Register. See A3-01..A3-07. |
| F7 HEDGE PHRASE MINING | **FINDING** | 14 hedges across 12 turns (A2 Section 6), incl. a clean double-refusal on order-book classification (turns 85/89) and quantum refusal on revenue slippage (turn 21). See A3-08..A3-11. |
| F8 TAX FORENSICS | N.A. | No ETR, deferred-tax sign, or earlier-year tax adjustment disclosed; PAT stated gross only (turn 11). |
| F9 OCI FORENSICS | N.A. | No OCI/actuarial figure on the call; FY26 OCI actuarial swing (pre-committed Q17) is a silence item, logged in F17. |
| F10 SHARE COUNT AND DILUTION | N.A. | No paid-up capital / EPS spread disclosed; QIP Rs 26.25 Cr deployment (pre-committed Q6) is a silence item, logged in F17. |
| F11 RESERVES AND NET WORTH TIE-OUT | N.A. | No reserves/net-worth figure; STAC net worth (pre-committed Q7) is a silence item, logged in F17. |
| F12 SEGMENT FORENSICS | N.A. | No segment asset/liability tables in a transcript. |
| F13 BOARD OUTCOME BEYOND RESULTS | N.A. | No AR/AGM notice/board's report read on the call. Board meeting is referenced (turn 117 "we discussed this in the board meeting yesterday") but no governance outcome disclosed; auditor-vs-board sequencing (pre-committed Q16) logged in F17. |
| F14 NOTE DRAFTING INCONSISTENCIES | N.A. | No notes/auditor letter to cross-check. AMBIGUOUS_SPEAKER (all 28 Q&A answers unattributed CMD vs CFO; CFO's individual answer share unverifiable) noted for A4 but is not a note-drafting defect. |
| F15 ENTITY LIST DIFFS | **FINDING** | New group entity ST Advance / "STAC" disclosed as acquired "yesterday only finalized" (turn 53); an entity-list addition surfaced verbally with no financials. See A3-12. (No consolidation list to formally diff and no prior extract — the change is established from the mgmt utterance, not a table.) |
| F16 PRESENTATION-SPECIFIC / CROSS-DOC RECONCILE | **FINDING** | Concall-vs-deck mismatches: cash Rs 530 vs 465.9 Cr (Rs 64 Cr gap); order book Rs 920 vs 927.7 Cr; capex Rs 200+ vs deck Rs 150 Cr (RAISED); internal order-book arithmetic off Rs 8 Cr; production/development granularity refused. See A3-13..A3-17 and the reconciliation table. |
| F17 CONCALL SILENCE AUDIT | **FINDING** | Multiple monitoring-checklist metrics and pre-committed questions received no utterance (CFO/OCF, DSO, QIP, Labour Code, OCI, customer concentration, STAC financials, auditor/board sequencing). See silence table + 18-question grid. A3-18. |

No blank checks. GATE A3: pass.

---

## COMMITMENT REGISTER (from F6) — promise-vs-delivery tracker feed

| Commitment | Implied date | Turn ref | Status word |
|---|---|---|---|
| FY27 revenue growth 20-25%, EBITDA 35-40% | FY27 full year | 9 | committed / confident |
| ~Rs 2,000 Cr fresh order inflows in FY27 (over and above negotiated) | FY27 | 9, 25 | confident / expect |
| Negotiated Rs 1,726 Cr converts to confirmed order book | "next few months" / ~3 months (could be 2 weeks) | 25 | expect / should happen |
| Additional ~Rs 2,000 Cr simulator contracts | "during the course of this financial year" | 25 | expect |
| SPJ-230 qualification + flight trials | "before December [2026]" | 33 | should happen / believe |
| SPJ-230 commercial contract | "maybe next two years" | 33 | expect |
| BrahMos seeker commercial order (product intake, not revenue) | "this financial year" (FY27) | 73 | expect / should happen |
| Counter-drone contracts "fortified" | "next 3 to 6 months" | 49 | should start |
| UK antenna-redesign export delivery | "next 6 to 8 months" | 49 | will be delivering |
| Export becomes multi-million-dollar business | "next few months" then scale over "two to three years" | 49, 171 | expect / should start |
| Hawk-radar software breakthrough / porting | "next two to three months" | 65 | expect |
| Advanced (2nd-gen) hawk-radar systems ready | "next six months" | 65 | will be available |
| Radar-program (air-defence) contract wins, few thousand Cr | "next 1.5 to 2 years" | 105 | expect |
| Rs 20bn single-vendor prospect converts | "9 months" (self-imposed) | 153 | should happen |
| Space-business investment decision | "3 to 4 months" (~Nov-2026) | 117 | will take a decision |
| Capex Rs 200 Cr+ (minimum) | "next one to two years" | 109 | will spend |
| EW business "maturing to a large stage," large business after qualification | "six months to one year" | 171 | expect |
| AI-driven products | "one to one-and-a-half years" | 171 | come out with |
| L1 large contract announcement | on contract signing | 45 | undergoing negotiation / will announce |

Status-change note: no prior-quarter transcript on file, so no "initiated -> underway -> completed" transition can be verbatim-confirmed this run. A4/A5 to overlay these against the Notion promise tracker and last quarter's register. The BrahMos-seeker item is explicitly a REPEAT commitment ("this question was asked during our AGM," turn 25 context; CMD flagged the Rs 1,726 Cr timeline question as previously asked) — a promise carried forward, not first-made.

---

## F17 SILENCE AUDIT — "What Was NOT Discussed"

Consecutive-quarter silence counts cannot be verbatim-established (no prior extract on file); each row is marked first-observed-this-run and handed to A4/A5 to backfill from Notion. Sustained silence on cash conversion is treated as a confirmatory negative per Role 5.

| Monitoring item | On the call? | Cite / basis | Note |
|---|---|---|---|
| CFO YTD (cash flow from operations) | NO | absent from turn 11 (only closing cash Rs 530 Cr stated) | Structural-crack metric (FY26 CFO/PAT ~0.30x). Silence = confirmatory negative. |
| DSO / receivable days | NO | turn 17 mentions ~Rs 2 Cr additional provision on "long pending receivables" but no DSO | Directionally negative colour (rising provisions) without the metric. |
| Capex YTD (actual Q1) | NO | turn 109 gives forward plan only | Only the Rs 200 Cr+ 2-yr floor; no spent-to-date. |
| Net cash reconciliation to deck | NO | turn 11 "net debtree ... 530 cr" | Conflicts with deck Rs 465.9 Cr (A3-13). |
| Order-book composition: production vs development | REFUSED | turns 85, 89 | Clean double-refusal (A3-08). |
| Order-book Q1 inflow (Rs 117 Cr per checklist) | NO | not disclosed | Total order book given; Q1 gross inflow not. |
| Services / exports % of order book | PARTIAL | turn 9 export book Rs 39 Cr; no % | |
| Customer concentration | NO | not addressed | |
| QIP Rs 26.25 Cr deployment schedule | NO | not addressed ("we took money" generically, turns 33/117) | Pre-committed Q6. |
| Recurring Labour Code P&L impact | NO | not addressed | Pre-committed Q5. |
| FY26 OCI actuarial swing | NO | not addressed | Pre-committed Q17. |
| STAC net worth / outlay / turnover / accretion / arm's-length / country / approvals / consolidation date | NO | turn 53 qualitative only ("small company," "yesterday only finalized") | 8 pre-committed questions (Q7-Q11) unanswered on a day-old acquisition (A3-12). |
| Auditor sign 16:34 vs board 18:30 sequencing | NO | board meeting referenced turn 117, sequencing not | Pre-committed Q16 (governance). |
| AMCA RFP/award status | NO | turn 61 "male program and bigger h programs" is vague, AMCA not named | Pre-committed Q18 (AMCA half). |

### 18 pre-committed questions — answer-status grid (line-cited; A4 confirms the grade)

| # | Question | Status | Cite |
|---|---|---|---|
| 1 | Q1 CFO + receivable days exact | NOT-ADDRESSED | turn 11 (cash only); turn 17 (provision, no DSO) |
| 2 | Signed vs negotiated split of Rs 2,654 Cr | PARTIAL | turns 9/11 (920 confirmed + 1,726 negotiated; per-program refused) |
| 3 | H2 bridge 27% to 35-40% EBITDA | PARTIAL (qualitative) | turn 37 ("uneven revenue ... confident of full year") — no quantified bridge |
| 4 | Which approvals delayed + revenue quantum slipped | EVADED (quantum) | turn 21 ("can't be specific"); turn 25 (programme colour, no Rs) |
| 5 | Recurring Labour Code P&L impact | NOT-ADDRESSED | — |
| 6 | QIP Rs 26.25 Cr deployment schedule | NOT-ADDRESSED | — |
| 7 | STAC net worth / outlay / turnover | NOT-ADDRESSED | turn 53 (qualitative) |
| 8 | STAC arm's-length + incorporation/country | NOT-ADDRESSED | turn 53 (refers to target's promoter, no related-party/country) |
| 9 | Basis for 1.3-2.0x STAC accretion | NOT-ADDRESSED | — |
| 10 | STAC regulatory approvals NA-vs-if-any | NOT-ADDRESSED | — |
| 11 | STAC completion + first-consolidation date | PARTIAL | turn 53 ("yesterday only finalized" ~30-Jul-2026; no consolidation date) |
| 12 | BrahMos seeker conversion timeline/value | PARTIAL | turn 73 (FY27 product intake; value not given); turns 93/97 (in Rs 20bn prospects) |
| 13 | Forward export pipeline vs Rs 39 Cr | PARTIAL (qualitative) | turn 49 (UK antenna 6-8m, US civil aviation; no forward value) |
| 14 | Inflow cadence Rs 2,000 Cr / Rs 20-40bn vs Rs 117 Cr Q1 | PARTIAL | turn 153 ("9 months"); turn 25 ("during this FY") — no quarterly cadence |
| 15 | Rs 150 Cr capex funding vs 0.30x CFO | EVADED (capex RAISED to Rs 200+, funding not addressed) | turn 109 |
| 16 | Auditor signed 16:34 vs board 18:30 sequencing | NOT-ADDRESSED | turn 117 (board referenced, sequencing not) |
| 17 | FY26 OCI actuarial swing | NOT-ADDRESSED | — |
| 18 | EW-L1 tender + AMCA status | PARTIAL | turn 45 (L1 acknowledged, detail declined); AMCA not named (turn 61 vague) |

Tally: 0 fully ANSWERED-SPECIFICALLY, 7 PARTIAL, 2 EVADED, 9 NOT-ADDRESSED. The unanswered mass clusters on (a) cash conversion / working capital and (b) the day-old STAC acquisition — both decision-critical for a WATCHLIST/AVOID name whose thesis crack is cash conversion.

---

## CROSS-DOC RECONCILIATION TABLE (F16) — concall spoken vs deck vs filing baseline

| Item | Concall (spoken) | Deck | Gap | Cite | Read |
|---|---|---|---|---|---|
| Cash + bank + investments, 30-Jun-2026 | Rs 530 Cr | Rs 465.9 Cr (Rs 4,659 Mn) | ~Rs 64 Cr | turn 11 | Unexplained; higher spoken figure. A4 reconcile (lean bear). |
| Confirmed order book, 30-Jun-2026 | Rs 920 Cr | Rs 927.7 Cr | Rs 7.7 Cr | turn 11 | Deck figure reconciles the Rs 2,654 total cleanly (927.7 + 1,726.3 = 2,654.0); spoken 920 is rounded. |
| Order book incl. negotiated | Rs 2,654 Cr | Rs 927.7 confirmed implied | internal Rs 8 Cr (920+1,726=2,646) | turns 9, 11, 23 | Arithmetic closes only with the deck's 927.7, not the spoken 920. |
| Capex, next 2 yr | Rs 200 Cr+ / "minimum" | Rs 150 Cr | +Rs 50 Cr+ RAISED | turn 109 | Guidance raised verbally ~33%+; funding vs 0.30x CFO not addressed. FORWARD-SIGNAL. |
| Revenue / GM / EBITDA / PAT margin Q1 | Rs 116 Cr / 78.9% / 27% / 19% | (reconcile to filing) | internally consistent | turn 11 | Spoken P&L internally arithmetic-consistent; matches checklist targets. Filing tie-out is A4's. |
| Revenue growth guidance | 20-25% ("2025%" ASR) | — | transcription | turn 9 | Directional; corroborate at deck. |

---

```yaml
stage: A3-forensics
company: "DATAPATTNS"
quarter: "q1fy27"
doctype: "concall"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/datapattns-q1fy27/work/forensics_concall_datapattns_q1fy27.md"
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
  F15: FINDING
  F16: FINDING
  F17: FINDING
findings:
  - {id: "A3-01", check: "F6", line: "turn 9", classification: "FORWARD-SIGNAL", implication: "Employee cost guided to stay elevated; 27% EBITDA not a one-quarter dip"}
  - {id: "A3-02", check: "F6", line: "turn 33", classification: "FORWARD-SIGNAL", implication: "SPJ-230 trials by Dec-2026, commercial contract ~2yr; size withheld"}
  - {id: "A3-03", check: "F6", line: "turn 73", classification: "FORWARD-SIGNAL", implication: "BrahMos seeker = FY27 order intake, revenue lags; value unquantified"}
  - {id: "A3-04", check: "F6", line: "turn 45", classification: "FORWARD-SIGNAL", implication: "L1 on one large tender, value withheld; announcement is a catalyst"}
  - {id: "A3-05", check: "F6", line: "turn 117", classification: "FORWARD-SIGNAL", implication: "Space go/no-go dated ~Nov-2026, contingent on govt funding"}
  - {id: "A3-06", check: "F6", line: "turn 153", classification: "FORWARD-SIGNAL", implication: "Self-imposed 9-month clock on Rs 20bn single-vendor inflow"}
  - {id: "A3-07", check: "F6", line: "turn 109", classification: "FORWARD-SIGNAL", implication: "Capex floor Rs 200 Cr+ set verbally over next 1-2 yr"}
  - {id: "A3-08", check: "F7", line: "turns 85,89", classification: "CONFIRMATORY-NEGATIVE", implication: "Order-book production-vs-development split refused twice; sustained opacity on order quality"}
  - {id: "A3-09", check: "F7", line: "turn 21", classification: "CONFIRMATORY-NEGATIVE", implication: "Revenue-slippage quantum withheld; magnitude opaque"}
  - {id: "A3-10", check: "F7", line: "turn 33", classification: "NEUTRAL-FACT", implication: "SPJ-230 deal size withheld though a number is 'in mind'"}
  - {id: "A3-11", check: "F7", line: "turn 165", classification: "AMBIGUOUS", implication: "Rs 40,000 Cr TAM realization timeline refused; scale not cadence"}
  - {id: "A3-12", check: "F15", line: "turn 53", classification: "FORWARD-SIGNAL", implication: "New entity STAC/ST Advance closed 30-Jul-2026; 8 of 18 pre-committed questions unanswered"}
  - {id: "A3-13", check: "F16", line: "turn 11", classification: "AMBIGUOUS", implication: "Cash Rs 530 Cr concall vs Rs 465.9 Cr deck = Rs 64 Cr unexplained gap"}
  - {id: "A3-14", check: "F16", line: "turn 11", classification: "AMBIGUOUS", implication: "Order book Rs 920 spoken vs Rs 927.7 deck; deck value reconciles the Rs 2,654 total"}
  - {id: "A3-15", check: "F16", line: "turn 109", classification: "FORWARD-SIGNAL", implication: "Capex RAISED vs deck Rs 150 Cr; funding vs 0.30x CFO unaddressed"}
  - {id: "A3-16", check: "F16", line: "turn 9", classification: "AMBIGUOUS", implication: "20-25% rev / 35-40% EBITDA guidance vs 27% Q1; H2 bridge left qualitative"}
  - {id: "A3-17", check: "F16", line: "turns 105,153,161", classification: "AMBIGUOUS", implication: "TAM ~Rs 40,000 Cr stated three ways with unit self-correction; directional only"}
  - {id: "A3-18", check: "F17", line: "turn 11 / silence", classification: "CONFIRMATORY-NEGATIVE", implication: "Silence on CFO/OCF, DSO, QIP, Labour Code, OCI, STAC financials, auditor/board sequencing; cash-conversion crack unaddressed"}
forward_signals: ["A3-01","A3-02","A3-03","A3-04","A3-05","A3-06","A3-07","A3-12","A3-15"]
ambiguous: ["A3-11","A3-13","A3-14","A3-16","A3-17"]
commitments:
  - {commitment: "FY27 revenue 20-25% / EBITDA 35-40%", implied_date: "FY27", ref: "turn 9", status_word: "committed"}
  - {commitment: "~Rs 2,000 Cr fresh order inflows FY27", implied_date: "FY27", ref: "turn 9", status_word: "confident"}
  - {commitment: "Rs 1,726 Cr negotiated converts to order book", implied_date: "~3 months", ref: "turn 25", status_word: "expect"}
  - {commitment: "Additional ~Rs 2,000 Cr simulator contracts", implied_date: "FY27", ref: "turn 25", status_word: "expect"}
  - {commitment: "SPJ-230 qualification + flight trials", implied_date: "before Dec-2026", ref: "turn 33", status_word: "should-happen"}
  - {commitment: "SPJ-230 commercial contract", implied_date: "~2 years", ref: "turn 33", status_word: "expect"}
  - {commitment: "BrahMos seeker order intake", implied_date: "FY27", ref: "turn 73", status_word: "expect"}
  - {commitment: "Counter-drone contracts fortified", implied_date: "next 3-6 months", ref: "turn 49", status_word: "should-start"}
  - {commitment: "UK antenna-redesign export delivery", implied_date: "next 6-8 months", ref: "turn 49", status_word: "delivering"}
  - {commitment: "Hawk-radar software breakthrough/porting", implied_date: "next 2-3 months", ref: "turn 65", status_word: "expect"}
  - {commitment: "Advanced 2nd-gen hawk-radar ready", implied_date: "next 6 months", ref: "turn 65", status_word: "available"}
  - {commitment: "Air-defence radar contract wins (few thousand Cr)", implied_date: "next 1.5-2 years", ref: "turn 105", status_word: "expect"}
  - {commitment: "Rs 20bn single-vendor prospect converts", implied_date: "9 months (self-imposed)", ref: "turn 153", status_word: "should-happen"}
  - {commitment: "Space-business investment decision", implied_date: "3-4 months (~Nov-2026)", ref: "turn 117", status_word: "will-decide"}
  - {commitment: "Capex Rs 200 Cr+ minimum", implied_date: "next 1-2 years", ref: "turn 109", status_word: "will-spend"}
gate_a3: pass
blank_checks: []
```
