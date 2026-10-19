# A3 FORENSIC NOTES: TATVA Q2 FY27, doctype presentation (notice: earnings call cancellation, 19-Oct-2026)

Agent: A3 forensic notes | model: claude-opus-5-5 | date: 2026-10-19
Inputs read: runs/tatva-q2fy27/extracted/tatva-notice-q2fy27-structured.md (28 rows), runs/tatva-q2fy27/extracted/tatva-notice-q2fy27-fulltext.md (65 lines, 1 page), runs/tatva-q2fy27/work/ledger_notice_tatva_q2fy27.md (28 rows), runs/tatva-q2fy27/work/notion-brief.md sections 7 and 8 (memory, not evidence). Prior-quarter fulltext: none supplied. Source PDF and inputs/ not opened.

## 1. LEDGER RECONCILIATION (28 of 28 rows read at fulltext line; 100%)

| Row | A1 line | Verified line(s) | Verbatim at line | Note |
|---|---|---|---|---|
| R001 / R018 | 18 | 18 | "Date: 19 October 2026" | ok |
| R002 | 18 | 18 | "Ref. No.: TCPCL/SEC/2026-27/00055" | ok |
| R003 | 27 | 27 | "Scrip Code: 543321" | ok |
| R004 / R019 | 35 | 34-35 | "intimation dated 13 October / 2026" | quote starts on L34, wraps to L35 |
| R005 | 36 | 36 | "05:00 p.m. (IST)" | ok |
| R006 | 65 | 65 | "M. No.: A37444" | ok |
| R007 / R024 | 58 | 58-59 | "Date: 2026.10.19 / 16:03:53 +05'30'" | wraps to L59 |
| R008 | 53 | 53 | "For Tatva Chintan Pharma Chem Limited" | ok |
| R009 | 23 | 23 | "BSE Limited" | ok |
| R010 | 22 | 22 | "National Stock Exchange of India Limited" | ok |
| R011 | 33 | 33-34 | "Regulation 30 of the SEBI (Listing Obligations and Disclosure Requirements) / Regulations, 2015" | wraps to L34 |
| R012 | 61 | 61 | "Ishwar Nayi" | ok; same person as R013 (A2 flag confirmed) |
| R013 / R028 | 55 | 55-57 | "Digitally signed by / ISHWAR RAMANBHAI / NAYI" | wraps to L57 |
| R014 | 27 | 26 | "Scrip Symbol: TATVA" | A2 correction to L26 confirmed |
| R015 | 44 | 45 | "www.tatvachintan.com." | A1 ANCHOR OFF BY ONE (L45, not L44); A2 did not catch it |
| R016 | 44 | 44 | "The above information shall be made available on the website of the Company at" | ok |
| R017 / R025 | 39 | 39-40 | "the aforesaid Earnings Call has been cancelled due / to unforeseen circumstances." | wraps to L40 |
| R020 | 35 | 35-36 | "scheduled to be held on Monday, 19 October 2026, at / 05:00 p.m. (IST)" | wraps to L36 |
| R021 | 37 | 36-37 | "for the quarter / and half-year ended 30 September 2026" | starts on L36 |
| R022 | 37 | 37 | "half-year ended 30 September 2026" | ok |
| R023 | 33 | 34 | "Regulations, 2015" | A1 ANCHOR OFF BY ONE (L34, not L33); A2 did not catch it |
| R026 | 33 | 34 | "as amended" | A1 ANCHOR OFF BY ONE (L34, not L33); A2 did not catch it |
| R027 | 36 | 36 | "post announcement of the financial results of the Company" | ok |

Every quote exists verbatim in the fulltext. The three one-line anchor offsets (R015, R023, R026) are pipeline housekeeping, not document findings. No row is a gap. A1 and A2 files were not edited.

## 2. FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-01 | F6 | R017, R019, R020, R004, R005 | L34-36, L39-40 | "with reference to our earlier intimation dated 13 October 2026" ... "the aforesaid Earnings Call has been cancelled" | FORWARD-SIGNAL | The 13-Oct commitment (call on 19-Oct at 17:00 IST) moves from scheduled to cancelled. No new date (A2 NO_NEW_DATE). Q2 FY27 has no management commentary venue unless the call is rescheduled. Role 5 promise-vs-delivery logs a missed disclosure commitment. The FTTCP catalyst timeline loses its Q2 checkpoint on the Q1 guidance (FY27 growth 25-30%, EBITDA margin 20-22%). |
| A3-02 | F6 | R007, R024 vs R005, R020 | L58-59; L36 | "16:03:53 +05'30'" vs "05:00 p.m. (IST)" | AMBIGUOUS | Cancellation signed 56 minutes before the call. The notice does not say if the board meeting ended, or if results were filed, before 16:03 IST. Two readings: logistics failure (neutral), or a results-day event (bear). Separating observation: the time stamp of the results filing against 16:03 IST. Question for A4. |
| A3-03 | F7 | R025 | L39-40 | "cancelled due to unforeseen circumstances" | AMBIGUOUS | No lexicon hedge hit. The generic cause still does the same pre-emptive cover job: no cause is named (A2 REASON_UNSPECIFIED). Neutral reading: management or host availability. Bear reading: late board approval, a review-report matter, or numbers management chose not to defend live. Lean bear (rule 6). Ask the cause and whether a reschedule is planned. |
| A3-04 | F16 | R016, R015 | L44-45 | "The above information shall be made available on the website of the Company" | AMBIGUOUS | The notice's only forward promise covers the notice itself. It names no substitute channel: no rescheduled call, no written Q&A, no investor presentation. The live Q&A, the quarter's main commentary channel, is dropped. Ask whether a replacement channel will run, and when. |
| A3-05 | F17 | R017, R025 (Notion brief s.7, s.8) | L39-40 | "Earnings Call has been cancelled" | AMBIGUOUS (lean bear) | All 8 monitoring checklist items and all 8 Q2 questions get no management answer this quarter (table in section 5). Cash conversion and receivable days: 2 consecutive quarters without cash Q&A (Q1 call silent per the Notion 14-Oct note, Q2 no call). The Notion page's own rule says a second quarter without cash Q&A strengthens the structural-cash leaning. Upgrade to CONFIRMATORY-NEGATIVE if the H1 FY27 cash flow shows negative CFO, or receivable days rising, on rising revenue. |

## 3. CHECKLIST SCORECARD

| Check | Status | Basis |
|---|---|---|
| F1 Zero-value standing items | N.A. | No financial line items; A2 zero_standing 0. |
| F2 Standalone vs consolidated | N.A. | No financials in the notice. |
| F3 Shell-entity detection | N.A. | No cost lines. |
| F4 Unaudited contribution ratio | N.A. | No auditor report. |
| F5 Going concern / EoM tracking | N.A. | No EoM paragraph; no prior-quarter fulltext supplied. |
| F6 Forward-commitment phrases | FINDING | No exact lexicon hit. Near-hits: "has been cancelled" (L39) and "shall be made available" (L44). Status change on the 13-Oct call commitment (A3-01); same-day timing (A3-02). |
| F7 Hedge phrases | FINDING | No lexicon hit. Non-lexicon generic cause "unforeseen circumstances" (L39-40) does the cover job (A3-03). |
| F8 Tax forensics | N.A. | No tax lines. |
| F9 OCI forensics | N.A. | No OCI. |
| F10 Share count / dilution | N.A. | Notice carries no share count or EPS. |
| F11 Reserves / net worth | N.A. | Notice carries no equity figures. |
| F12 Segment forensics | N.A. | No segment data. |
| F13 Board outcome beyond results | N.A. | The notice is not a board outcome. It does not say if the 19-Oct board meeting concluded (see A3-02). |
| F14 Drafting inconsistencies | PASS | Issuer name consistent (L18 "TCPCL", L53). Signatory consistent (L55-57 digital name, L61, L63). Opening paragraph L33-37 has no main verb (a grammar fragment). Immaterial boilerplate. |
| F15 Entity list diffs | N.A. | No consolidation list. |
| F16 Dropped / reframed disclosures | FINDING | Earnings call Q&A dropped with no substitute channel named (A3-04). No prior deck to diff for metrics or baselines. |
| F17 Silence audit | FINDING | No transcript exists because the call was cancelled. Silence audit run against the Notion checklist (A3-05; table in section 5). |

## 4. COMMITMENT REGISTER (F6)

| Commitment | Implied date | Ref | Status word |
|---|---|---|---|
| Earnings call per the 13-Oct-2026 intimation | 19-Oct-2026, 17:00 IST | L34-36 (R019, R020, R005) | cancelled (was scheduled) |
| Rescheduled earnings call | none given | L39-40 (R017) | not given |
| Post this intimation on www.tatvachintan.com | not dated in notice | L44-45 (R016, R015) | promised |

The status words fall outside the initiated / underway / completed set. The notice has no project milestone language.

## 5. WHAT WAS NOT DISCUSSED (F17 silence audit)

Basis: Notion brief sections 7 and 8 (memory to weigh, not anchored evidence). "Quarters" counts consecutive quarters with no management answer, Q2 FY27 included. A count of 1 means the brief records no Q1 silence for the item, or gives no Q1 status.

| # | Item (source) | Quarters silent | Basis |
|---|---|---|---|
| 1 | Cash conversion: receivable days, OCF/EBITDA, ECL vs top-3 concentration (checklist #1; Q2 Q#4; Q1 Q#6 OPEN; calendar "Cash vs profit; customer payment days") | 2 | Brief s.9 14-Oct note: "first live test of the Q1 cash/WC silence"; Q1 Q#6 OPEN; Q2 no call |
| 2 | Rs 1.32 Cr exceptional item (Q1 Q#1 OPEN; Q2 Q#1) | 2 | Q1 status OPEN |
| 3 | Standalone PBT / parent profit share (checklist #7; Q1 Q#4 OPEN; Q2 Q#7) | 2 | Q1 status OPEN |
| 4 | ROCE clearing 8%; steady-state ROCE at 1.5x asset turnover (checklist #2; Q2 Q#2) | 1 | Q1 status GREEN |
| 5 | SDA revenue, new-customer invoicing ~Aug 2026 (checklist #3) | 1 | Q1 SDA question answered |
| 6 | EBITDA margin 20-22%, H2 bridge (checklist #4; Q2 Q#3) | 1 | MD answered on the Q1 call ("I would still stick to 20-22%") |
| 7 | Dahej-III milestones: equipment PO by Q3 FY27 (checklist #5 reframed) | 1 | Q1 Jolva question answered |
| 8 | Rating, net debt/EBITDA, Rs 1,000 Cr ceiling draw (checklist #6; Q2 Q#6) | 1 | Brief gives no Q1 status for the funding question |
| 9 | Tax rate 24.3% vs 37.8% (Q1 Q#5; Q2 Q#5) | 1 | Brief gives no Q1 status |
| 10 | Peer demand tone; promoter pay vs PAT (checklist #8; Q2 Q#8) | 1 | Q1 status WAIT |
| 11 | AR Section J: Customer 1 at 36%, CFO departure, R&D at 1.58%, subsidiary receivables Rs 25 Cr to Rs 61 Cr | 1 | First call after the 01-Sep AR deep dive. Status of the #1-#4 IR email channel is not in the inputs |
| 12 | Q1 guidance due in window: two more pharma molecules by Q3 end, hybrid battery initial Oct-Nov CY2026, FY27 growth 25-30% | 1 | No Q2 management update |

Per Role 5, sustained silence on a deteriorating metric is a confirmatory negative. The inputs do not show deterioration: the H1 numbers sit in the results filing, not in this notice. Rows 1-3 therefore stay AMBIGUOUS. A4 cross-checks them against the Q2 results filing.

## 6. A4 HAND-OFF (questions to raise)
- A3-02, A3-03: What were the "unforeseen circumstances"? Did the board approve and file results before 16:03 IST on 19-Oct?
- A3-01, A3-04: Will the call be rescheduled, or replaced by written Q&A? Give the date.
- A3-05: Push the cash-conversion and receivable-days questions (rows 1-3) through a written channel, and log the silence count.

```yaml
stage: A3-forensics
company: "TATVA"
quarter: "Q2 FY27"
doctype: "presentation (notice)"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/tatva-q2fy27/work/forensics_notice_tatva_q2fy27.md"
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
  F14: PASS
  F15: N.A.
  F16: FINDING
  F17: FINDING
findings:
  - {id: "A3-01", check: "F6", line: "L34-36, L39-40", classification: "FORWARD-SIGNAL", implication: "13-Oct call commitment (19-Oct 17:00 IST) cancelled, no new date; Q2 has no management commentary venue; Role 5 logs missed disclosure commitment"}
  - {id: "A3-02", check: "F6", line: "L58-59; L36", classification: "AMBIGUOUS", implication: "signed 16:03:53 IST, 56 min before 17:00 call; notice silent on whether board/results concluded first; check results filing timestamp"}
  - {id: "A3-03", check: "F7", line: "L39-40", classification: "AMBIGUOUS", implication: "'unforeseen circumstances' names no cause; neutral (logistics) vs bear (results-day event) reading; lean bear, ask cause"}
  - {id: "A3-04", check: "F16", line: "L44-45", classification: "AMBIGUOUS", implication: "only promise is posting this notice; no reschedule, written Q&A or deck named; live Q&A channel dropped"}
  - {id: "A3-05", check: "F17", line: "L39-40", classification: "AMBIGUOUS", implication: "all 8 checklist items unaddressed; cash/receivable-days Q&A silent 2 consecutive quarters; upgrade to CONFIRMATORY-NEGATIVE if H1 CFO negative or receivable days rising"}
forward_signals: ["A3-01"]
ambiguous: ["A3-02", "A3-03", "A3-04", "A3-05"]
commitments:
  - {commitment: "Earnings call per 13-Oct-2026 intimation", implied_date: "2026-10-19 17:00 IST", ref: "L34-36 (R019, R020, R005)", status_word: "cancelled"}
  - {commitment: "Rescheduled earnings call", implied_date: "none given", ref: "L39-40 (R017)", status_word: "not given"}
  - {commitment: "Post this intimation on www.tatvachintan.com", implied_date: "not dated", ref: "L44-45 (R016, R015)", status_word: "promised"}
gate_a3: pass
blank_checks: []
analyst_note: "One-page Reg 30 notice; only F6, F7, F16, F17 carry content. The load-bearing facts are timing and vagueness: signed 16:03:53 IST, 56 minutes before the 17:00 call, cause 'unforeseen circumstances', no new date, no substitute channel. The notice does not say whether the board approved results that day, so A4 should compare the results filing timestamp before reading intent into the cancellation. Per the Notion brief, this call was the live venue for the cash-vs-profit and receivable-days questions, and the Q1 call was already silent on cash/WC, so Q2 makes two consecutive quarters with no cash Q&A; the page's own rule says that strengthens the structural-cash leaning. I hold it AMBIGUOUS, not CONFIRMATORY-NEGATIVE, because the silence comes from a cancellation rather than evasion on a live call, and my inputs show no metric deterioration. Upgrade if H1 CFO is negative or receivable days rise on rising revenue. A1 anchors for R015, R023, R026 are one line off (L45, L34, L34); all quotes verbatim, no reconciliation gap."
```
