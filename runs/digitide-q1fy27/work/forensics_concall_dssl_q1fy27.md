# A3 FORENSIC NOTES — Digitide Solutions Limited (DSSL) — Q1 FY27 — Doctype: CONCALL

Inputs read in full before judging:
- A1 extract: `runs/dssl-q1fy27/work/extract_concall_dssl_q1fy27.txt` (194 lines; verbatim body lines 36-193; DECODE KEY lines 14-29 used only to read ASR garble, all cites are to the verbatim line).
- A2 ledger: `runs/dssl-q1fy27/work/ledger_concall_dssl_q1fy27.md` (GATE A2 pass).
- Prior-quarter extract: none (first concall in this run) — verbatim EoM/entity diffs not possible; noted where it constrains a check.

Ledger reconciliation: 100%. Every row read at its cited line —
participants P1-P13 (ledger L34-46), turns 1-94 (L56-149), questions Q1-Q27
(L159-185), numbers N1-N34 (L195-228), forward-commitments F1-F18 (L238-255),
hedges H1-H13 (L261-273). No unread row.

Doctype gate applied per task: F6/F7/F17 are the core of a concall forensic and
APPLY. F2/F8/F10/F12 applied only where management SPOKE a number (or a
number was put to management and engaged) that reconciles-or-conflicts with the
Reg 33 baseline — the Role 5 arithmetic spine (sequential-EBITDA bridge, D&A
split, PAT 2.9cr, DSO 82 days, S-vs-C value-dilution). Pure
balance-sheet/auditor/entity checks (F1,F3,F4,F5,F9,F11,F13,F14,F15,F16) are
N.A. — "concall transcript, no statements/notes/auditor report/deck."

---

## FINDINGS TABLE

| id | check | ledger row ref | line/turn | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-F01 | F2 | H8 / turns 33,41 (N17 PAT 2.9cr) | L88, L97 (turn 33/41) | "optically it would look like it is incurring losses while is profitable" ... "Not all of the corporate expenses are crossed to the entities at this moment... some of them are shareholder activities" | FORWARD-SIGNAL | Consolidated PAT +2.9cr is carried by Alldigi (100% dividend up-streamed, L51/L80); Digitide-parent ex-Alldigi is loss-making because group corporate/shareholder cost is housed in the parent and NOT fully cross-charged to subs. Structural value leakage to Digitide minorities persists until legal-entity consolidation, which the board has declined to timeline (A3-F17 register). A4 question. |
| A3-F09 | F2 | N7,N8,N9,N10,N11 / turn 4 | L42 (turn 4) | "Sequential AITA was lower by about 11 crores... 9.9 crores related to a one-off... The sequential operation decline was about 1 cr... reconstructed wage cost... about 10 crores" | AMBIGUOUS | Top-line QoQ EBITDA bridge closes (-11 = -9.9 one-off base effect -1 net operational), but the ~10cr new wage headwind is implicitly netted to only -1cr operational, i.e. ~9cr of offset (repricing/portfolio/mix) is asserted but not itemized. If the offset is one-off, the 200bps FY27 expansion (A3-F02) is over-committed. A4 question. |
| A3-F02 | F6 | F15, N29 / turn 81 | L168 (turn 81) | "we will be in track with our 200 bits [bps] margin expansion in this uh fiscal" | FORWARD-SIGNAL | 200bps on the 9.9% Q1 base (N2/N7) implies ~11.9% FY27 exit = a steep H2 recovery. This is the decisive FLAG-CASH tripwire variable (Q1 9.9% = leg 1 of the <11% two-consecutive-quarter STRUCTURAL falsifier). No Q2 number and no quantified H2 bridge given. A4 question. |
| A3-F03 | F6 | F6, N16 / turn 4 | L42 (turn 4) | "a total lease out loss [outflow] for fi 27 in the range of 175 to 180 crores in line with our previous guidance" | NEUTRAL-FACT | Cash lease drag 175-180cr vs normalized D&A 55-57cr/qtr (N13); sizes the reported-EBITDA-to-cash gap the new COO/CFO office is chartered to close (L42). Commitment register. |
| A3-F04 | F7 | H11, H12 / turns 79,87 (vs Q23 L162) | L164 (turn 79) | "revenue is not the only metric we are managing for this year... measure us on profitability growth rather than the revenue itself" | FORWARD-SIGNAL | Prior "double digit revenue growth for FY27" guidance (analyst restates it, Q23 L162) is effectively WITHDRAWN/de-emphasised; management refused a replacement revenue % for the next 2 or 5 years — "We'll come back in the subsequent quarters" (L179). Prominent guidance change on a new-CEO first call = strategy reset (Get Unified / Strengthen Core / Go West Go Digital / Go All Out-BPA). A4 question. |
| A3-F05 | F7 | H5, H6, N34 / turns 16,18 | L63 (turn 18) | "there are no immediate plans of monetizing it at the moment" | AMBIGUOUS | Reverses/reframes the company-secretary's prior ~150cr land-monetization indication (analyst cite L61, N34). A previously-flagged cash source is withdrawn just as the cash-conversion narrative tightens. A4 question. |
| A3-F06 | F10 | H4, N31, N25 / turns 14,12 | L57 (turn 14) | "we do not see that [equity dilution] as one of the options that we will uh execute. Not... something that we have uh decided or thought about" | AMBIGUOUS | Analyst's ~1,800cr inorganic funding need (N31, ANALYST_SOURCED) left unfunded: equity dilution denied, no debt plan stated, and "not one big acquisition... two or three" (L53, N25). Funding mechanism for the BPA-"Acquire" track is unresolved. No share-count/EPS number was spoken (F10 numeric spine otherwise dormant). A4 question. |
| A3-F07 | F12 | N18, N22, N23 / turns 4,9 | L49 (turn 9), L42 | "our book to build conversion for the quarter has been on an average between 11 to 13%" ; "we didn't shy away walking away from opportunities" | FORWARD-SIGNAL | TCV 205cr (N18) vs ~500cr close-book (N22) at 11-13% conversion, PLUS deferment of book-and-bill work into Q2/Q3 (L49) and deliberate exit of margin-dilutive core India BPM accounts, points to continued sequential revenue softness (already -3.1% QoQ, N4). Revenue headwind is a choice, not an accident — reconciles with the withdrawn revenue guide (A3-F04). A4 question. |
| A3-F08 | F17 | H12 + monitorables a-e / turn 87 | L179 (turn 87) | "We'll come back in the subsequent quarters. What does it mean in terms of percentages and many other markers around that?" | CONFIRMATORY-NEGATIVE | Silence-audit bundle (full table below): DaaS/CBaaS unit economics, ~90cr PPE/capital-intensity gap, the specific Q2 margin number, the 6 other-auditor-reviewed subs (90.1% of PAT), and governance items (Cybercons/RPT advances/RMC) are STILL-SILENT (call 1). Sustained silence on the decisive margin path is a confirmatory negative per Role 5. |

---

## CHECKLIST SCORECARD (all 17; one status each)

| # | Status | One-line basis |
|---|---|---|
| F1 | N.A. | Concall transcript, no statements/notes; no ZERO_STANDING line-item template. (Mgmt did state "no exceptional items", L42/N17 — noted, not a template row.) |
| F2 | FINDING | S-vs-C value-dilution structure disclosed (A3-F01, L88/L97) and the sequential-EBITDA-bridge offset is un-itemized (A3-F09, L42). Both on management-spoken numbers. |
| F3 | N.A. | Concall transcript, no statements/notes; no standalone-vs-consol cost lines to test for shells. |
| F4 | N.A. | Concall transcript, no auditor report; the 6 component-auditor subs / 90.1%-of-PAT ratio is unquantified on the call → carried as F17 silence, not an F4 measurement. |
| F5 | N.A. | Concall transcript, no auditor report/EoM; no prior-quarter EoM paragraph to verbatim-diff. |
| F6 | FINDING | Forward-commitment mining live: 18 dateable commitments extracted (register below); chief = 200bps FY27 margin (A3-F02) and 175-180cr FY27 lease outflow (A3-F03). |
| F7 | FINDING | Hedge mining live: prior double-digit revenue guide withdrawn/de-emphasised (A3-F04, L164) and ~150cr land monetization walked back (A3-F05, L63). |
| F8 | PASS | Tax addressed positively and cleanly: "receipt of our income tax refund for FI26" and "closure of several GST matters with clean orders" (L42). No ETR/deferred-tax number to reconcile; no adverse earlier-year tax adjustment. |
| F9 | N.A. | Concall transcript, no statements/notes; no OCI/actuarial line disclosed. |
| F10 | FINDING | No share-count/EPS number spoken, but equity dilution was directly put to management and DENIED against an unfunded ~1,800cr inorganic need (A3-F06, L57). |
| F11 | N.A. | Concall transcript, no statements/notes; no reserves/net-worth figure to tie out. |
| F12 | FINDING | Segment numbers spoken: TCV 205cr vs 500cr close-book at 11-13% conversion + deliberate BPM rationalization = revenue-headwind signal (A3-F07, L49/L42). |
| F13 | N.A. | Concall transcript, no Board's Report/AGM notice/director-term disclosure. |
| F14 | N.A. | Concall transcript, no note text vs auditor-letter to cross-check (ASR name garble is an A2 transcription issue, not a drafting inconsistency). |
| F15 | N.A. | Concall transcript, no consolidation entity list; no prior quarter to diff. |
| F16 | N.A. | Concall transcript, no deck/prior deck to diff for dropped metrics or axis changes; the guidance softening is captured under F7 (A3-F04) and F17. |
| F17 | FINDING | Silence audit run against the F6 register + Role-4 monitoring checklist + the logged Questions-for-Management (A3-F08 + table below). |

GATE A3: pass — every check marked exactly one of PASS / FINDING / N.A.; no blanks.

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | ledger / line ref | status word |
|---|---|---|---|
| ~200bps margin expansion | FY27 (full year) | F15 / N29 / L168 | committed (reaffirmed) |
| Total lease cash outflow 175-180cr | FY27 | F6 / N16 / L42 | reaffirmed |
| "working towards... margin expansion... demonstrating our numbers in upcoming quarters" | FY27, H2-weighted | F7 / L42 | underway |
| Client repricing / cost-of-living adjustments to offset wage code | ongoing, through the year | F5,F11 / L42,L101 | underway ("active discussions") |
| Portfolio rationalization / walk away from low-margin accounts | through the year | F1 / L42 | initiated ("already started to happen") |
| BPA program (build-partner-acquire) | multi-quarter | F3 / L42 | initiated |
| Invest/build payroll, insurance, collections platforms | ongoing | F4,F10 / L42,L69 | underway |
| Convert AI funnel 100-150cr | through the year | F12 / N28 / L148 | underway (confidence "very high") |
| Stand up AI business unit with own P&L | future / conditional | F13 / L150 | evaluating ("are we there yet? no") |
| Headcount on a declining trend | next couple of quarters | F17 / L183 | underway |
| $1bn / 3x3x3 "northstar" | FY31 | N30,F16 / L177 | reaffirmed (path reprioritised to profitability) |
| M&A — not one big deal, likely 2-3 | next few quarters | N25,F8 / L53 | evaluating ("considering options... yes") |
| Guide the market IF land-monetization plans arise | conditional | F9 / L63 | conditional (no plan now) |
| Revenue growth % for next 2yr / 5yr | "subsequent quarters" | H12 / L179 | deferred (withheld this call) |

---

## F17 — SILENCE AUDIT ("What Was NOT Discussed")

Cross-referenced against (a) the F6 commitment register, (b) the Role-4
monitoring checklist / monitorables a-e, and (c) the logged
Questions-for-Management. Each reference point verified at its line, not taken
on trust. Q-cluster silence counts start at this call (first concall in run).

### Reference points ADDRESSED on the call
| item | status | turn / line | verbatim anchor |
|---|---|---|---|
| Owners-vs-NCI / value-dilution (parent optically loss-making; corporate/shareholder costs housed in Digitide not fully cross-charged) | ADDRESSED | turns 33,41 / L88,L97 | "Not all of the corporate expenses are crossed to the entities at this moment... some of them are shareholder activities" |
| Alldigi-merger timeline | ADDRESSED (declined) | turn 31 / L84 | "We don't have a specific timeline or an action plan against it at this moment... the board will decide" |
| Q4->Q1 EBITDA bridge (~11cr QoQ) | ADDRESSED (offset un-itemized — see A3-F09) | turn 4 / L42 | "lower by about 11 crores... 9.9 crores... a one-off... about 1 cr... wage cost... about 10 crores" |
| DSO 82 days | ADDRESSED | turn 4 / L42 | "Neither reflect the deterioration of collection quality... we expect this to normalize" |
| Book-to-bill 11-13% | ADDRESSED | turn 9 / L49 | "book to build conversion for the quarter has been on an average between 11 to 13%" |
| Wage / labour-code ~10cr + repricing | ADDRESSED | turns 4,43 / L42,L101 | "This is about 10 crores in this quarter... in active discussions with our clients on repricing" |
| Tax matters (IT refund FY26, GST clean orders) | ADDRESSED | turn 4 / L42 | "receipt of our income tax refund for FI26... closure of several GST matters with clean orders" |

### GUIDANCE CHANGE (flag prominently)
| item | status | turn / line | verbatim anchor |
|---|---|---|---|
| Prior "double-digit revenue growth FY27" | WITHDRAWN / de-emphasised | turn 79 / L164 | "revenue is not the only metric we are managing for this year... measure us on profitability growth rather than the revenue itself" |
| $1bn / 3x3x3 by 2031 | REAFFIRMED as "northstar", path reprioritised | turn 86 / L177 | "the northstar stays but the path to that northstar is more profitability" |
| Revenue-growth % for next 2yr / 5yr | DEFERRED (no number) | turn 87-88 / L179 | "We'll come back in the subsequent quarters" |

### FORWARD GUIDE given
| item | status | turn / line | verbatim anchor |
|---|---|---|---|
| ~200bps margin expansion FY27 (FLAG-CASH decisive variable) | GIVEN → FORWARD-SIGNAL (A3-F02) | turn 81 / L168 | "we will be in track with our 200 bits [bps] margin expansion in this uh fiscal" |
| Normalized D&A 55-57cr/qtr | GIVEN | turn 4 / L42 | "think about the depreciation at roughly 55 to 57 crores a quarter" |
| FY27 lease outflow 175-180cr | GIVEN | turn 4 / L42 | "175 to 180 crores in line with our previous guidance" |
| Headcount declining trend | GIVEN (directional only) | turn 90 / L183 | "headcount will be on a declining trend for the next couple of quarters" |

### DENIED / WALKED-BACK (flag)
| item | status | turn / line | verbatim anchor |
|---|---|---|---|
| Equity dilution for M&A | DENIED | turn 14 / L57 | "we do not see that as one of the options that we will uh execute" |
| Land/building monetization (~150cr prior CS indication) | WALKED-BACK / reframed | turns 16,18 / L59,L63 | "no immediate plans of monetizing it at the moment" |

### STILL-SILENT (confirmatory negatives; consecutive-quarter silence count = 1, this call)
| item | status | basis |
|---|---|---|
| DaaS/CBaaS As-a-Service unit economics — IRR / ROCE / gross-margin (monitorable a) | STILL-SILENT | Whole-transcript sweep; BPA "build" emphasised (L42) but no unit economics disclosed. |
| ~90cr PPE / capital-intensity gap (monitorable b) | STILL-SILENT | Whole-transcript sweep; PPE unaddressed; land-monetization instead walked back (L63). |
| Specific Q2 margin number | STILL-SILENT | Only "we'll come back in the subsequent quarters" (H12, L179); no Q2 figure vs the 200bps FY27 promise. |
| Names of the 6 other-auditor-reviewed subs (90.1% of PAT) | STILL-SILENT | Whole-transcript sweep; component-auditor scope never named on the call. |
| Governance items — Cybercons, RPT advances, RMC meetings | STILL-SILENT | Whole-transcript sweep; no governance/RPT disclosure. |

### Logged Questions-for-Management — resolution this call
- ANSWERED-THIS-CALL: value-dilution mechanism, Alldigi-merger stance, EBITDA
  bridge, DSO, wage/repricing, tax, dividend-income S-vs-C distortion (Q1/Q10-Q12/Q14).
- PARTIALLY-ANSWERED → carry to A4: margin path (200bps given, no Q2/quarterly
  bridge, Q1/Q3/Q24); revenue growth (guidance withdrawn, no replacement %,
  Q8/Q23/Q26); inorganic funding (equity denied, no alternative, Q4/Q5).
- STILL-SILENT → carry to A4: DaaS economics, PPE gap, sub names, governance
  (monitorables above). Q15 (BPM growth granularity) went UNANSWERED on-call
  (connection dropped, L117-125) — re-log for A4.

### BINDING TRIPWIRE status (FLAG-CASH falsifier)
Q1 FY27 EBITDA margin printed 9.9% (N2/N7, L42) = leg 1 of the "near 9% (<11%)
for two consecutive quarters => STRUCTURAL" falsifier. Q2 FY27 margin is the
decisive second leg and management withheld it (STILL-SILENT). The 200bps FY27
commitment (A3-F02) is the sole management datapoint against the tripwire and is
H2-loaded — assess as FORWARD-SIGNAL, escalate to A4 as the primary management
question.

---

## FOR A4 — questions to convert
- FORWARD-SIGNAL: A3-F01 (value-dilution / merger timeline), A3-F02 (200bps
  path + Q2 margin), A3-F04 (revenue guidance withdrawal / replacement metric),
  A3-F07 (BPM rationalization revenue trajectory).
- AMBIGUOUS: A3-F05 (land-monetization reversal), A3-F06 (1,800cr inorganic
  funding mechanism), A3-F09 (EBITDA-bridge wage-offset repeatability).
- CONFIRMATORY-NEGATIVE carried as monitorables: A3-F08 (DaaS economics, PPE
  gap, Q2 margin, 6-sub names, governance).

```yaml
stage: A3-forensics
company: "DSSL"
quarter: "Q1 FY27"
doctype: "concall"
model: claude-opus-4-8
status: complete
forensics_path: "runs/dssl-q1fy27/work/forensics_concall_dssl_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: N.A.
  F2: FINDING
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: PASS
  F9: N.A.
  F10: FINDING
  F11: N.A.
  F12: FINDING
  F13: N.A.
  F14: N.A.
  F15: N.A.
  F16: N.A.
  F17: FINDING
findings:
  - {id: "A3-F01", check: "F2", line: "L88,L97", classification: "FORWARD-SIGNAL", implication: "Parent ex-Alldigi loss-making; group corporate/shareholder cost not cross-charged to subs = value leakage to Digitide minorities until board-timelined merger"}
  - {id: "A3-F09", check: "F2", line: "L42", classification: "AMBIGUOUS", implication: "~10cr wage headwind implicitly netted to -1cr operational; ~9cr offset asserted but not itemized, questions durability of 200bps promise"}
  - {id: "A3-F02", check: "F6", line: "L168", classification: "FORWARD-SIGNAL", implication: "200bps on 9.9% base implies ~11.9% FY27 exit / steep H2 recovery; decisive FLAG-CASH tripwire variable, no Q2 bridge"}
  - {id: "A3-F03", check: "F6", line: "L42", classification: "NEUTRAL-FACT", implication: "175-180cr FY27 lease cash outflow vs 55-57cr/qtr D&A sizes the reported-EBITDA-to-cash gap"}
  - {id: "A3-F04", check: "F7", line: "L164", classification: "FORWARD-SIGNAL", implication: "Prior double-digit FY27 revenue guidance withdrawn/de-emphasised; no replacement revenue % for 2yr/5yr; new-CEO strategy reset"}
  - {id: "A3-F05", check: "F7", line: "L63", classification: "AMBIGUOUS", implication: "~150cr land-monetization cash source (prior CS indication) walked back to no-immediate-plans amid tightening cash narrative"}
  - {id: "A3-F06", check: "F10", line: "L57", classification: "AMBIGUOUS", implication: "~1,800cr inorganic need unfunded: equity dilution denied, no debt plan, funding mechanism for BPA-acquire unresolved"}
  - {id: "A3-F07", check: "F12", line: "L49", classification: "FORWARD-SIGNAL", implication: "TCV 205cr vs 500cr close-book at 11-13% conversion + work deferment + deliberate BPM exit = continued sequential revenue softness by design"}
  - {id: "A3-F08", check: "F17", line: "L179", classification: "CONFIRMATORY-NEGATIVE", implication: "STILL-SILENT on DaaS unit economics, ~90cr PPE gap, Q2 margin, 6 component-auditor subs (90.1% PAT), governance; Q2 margin = decisive tripwire leg withheld"}
forward_signals: ["A3-F01", "A3-F02", "A3-F04", "A3-F07"]
ambiguous: ["A3-F05", "A3-F06", "A3-F09"]
commitments:
  - {commitment: "~200bps margin expansion", implied_date: "FY27", ref: "F15/N29/L168", status_word: "committed"}
  - {commitment: "Total lease cash outflow 175-180cr", implied_date: "FY27", ref: "F6/N16/L42", status_word: "reaffirmed"}
  - {commitment: "Working towards margin expansion, numbers in upcoming quarters", implied_date: "FY27 H2", ref: "F7/L42", status_word: "underway"}
  - {commitment: "Client repricing / COLA to offset wage code", implied_date: "through FY27", ref: "F5,F11/L42,L101", status_word: "underway"}
  - {commitment: "Portfolio rationalization / walk away from low-margin accounts", implied_date: "through FY27", ref: "F1/L42", status_word: "initiated"}
  - {commitment: "BPA build-partner-acquire program", implied_date: "multi-quarter", ref: "F3/L42", status_word: "initiated"}
  - {commitment: "Invest/build payroll, insurance, collections platforms", implied_date: "ongoing", ref: "F4,F10/L42,L69", status_word: "underway"}
  - {commitment: "Convert AI funnel 100-150cr", implied_date: "through FY27", ref: "F12/N28/L148", status_word: "underway"}
  - {commitment: "Stand up AI business unit with own P&L", implied_date: "future/conditional", ref: "F13/L150", status_word: "evaluating"}
  - {commitment: "Headcount declining trend", implied_date: "next couple of quarters", ref: "F17/L183", status_word: "underway"}
  - {commitment: "$1bn / 3x3x3 northstar", implied_date: "FY31", ref: "N30,F16/L177", status_word: "reaffirmed"}
  - {commitment: "M&A 2-3 deals (not one big)", implied_date: "next few quarters", ref: "N25,F8/L53", status_word: "evaluating"}
  - {commitment: "Guide market if land-monetization plans arise", implied_date: "conditional", ref: "F9/L63", status_word: "conditional"}
  - {commitment: "Revenue growth % for 2yr/5yr", implied_date: "subsequent quarters", ref: "H12/L179", status_word: "deferred"}
gate_a3: pass
blank_checks: []
```
