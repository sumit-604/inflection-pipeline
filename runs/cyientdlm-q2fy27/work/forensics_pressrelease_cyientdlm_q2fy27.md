# A3 FORENSIC NOTES: Cyient DLM Ltd (CYIENTDLM) Q2 FY27, doctype presentation (press release, file tag pressrelease)

Agent: A3 forensic notes | Model: claude-opus-5-5 | Run date: 2026-10-17
Inputs read: A1 structured (R001-R060), A1 fulltext (136 lines), A2 ledger. Prior-quarter fulltext: not available. Source PDF and inputs/: not opened.
Context: PRE-THESIS READ. Decision Status NOT SET, Halt 1 pending, mental model unsigned.
Arithmetic note: values marked "implied" come from arithmetic on stated figures and stated growth rates. They are not estimates of missing numbers. The document states no prior-period base. Rounding of the stated growth % moves the implied bases by about +/-5 bps.

## 0. LEDGER RECONCILIATION (100%)

Rows in ledger: 60 (R001-R060). Rows read at the cited fulltext line: 60. Reconciled: 100%.

Every claim value was found verbatim at or next to its cited line. There are three non-material line drifts in A1 citations and one A2 note error:

| Row | A1 cited line | Verbatim actually at | Note |
|---|---|---|---|
| R027 | 28 | 29 | "Regulation 30 of the SEBI (LODR) Regulation, 2015" is on line 29; line 28 is blank |
| R036 | 103 | 104 | "renamed Cyient DLM Electronics Inc." is on line 104 |
| R041 | 79 | 81-82 | line 79 is the quote lead-in; the quoted words are on lines 81-82 |
| R036 (A2 ledger note) | - | 103-104 | **A2 note has the direction reversed.** The ledger reads "renamed (Cyient DLM Electronics Inc. to Altek Electronics)". The fulltext reads "the integration of Altek Electronics, acquisition in Connecticut, U.S. which has been renamed Cyient DLM Electronics Inc." (lines 103-104). The OLD name is Altek Electronics. The NEW name is Cyient DLM Electronics Inc. A4 must use the fulltext direction. |

Arithmetic tie-outs on stated numbers (all pass unless shown elsewhere):
- EBITDA margin: 34.2 / 393.1 = 8.70%, stated 8.7% (line 70). Ties.
- Normalized PAT margin: 15.82 / 393.1 = 4.02%, stated 4.0% (line 71). Ties.
- Reported PAT less one-off: 34.0 - 18.2 = 15.8, against normalized 15.82 (lines 71-72). Ties within rounding. This implies normalization removes only the earn-out gain, with no tax effect on it.
- Order book walk: 2,813.7 - 214.8 = 2,598.9 implied Q1 FY27 book (line 74). This matches the Notion Q1 figure of Rs2,600 Cr.
- Book-to-bill against the order book walk: DOES NOT TIE. See FN-05.

## 1. FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| FN-01 | F16 | R001, R004, R005, R006, R007 | 60, 65, 70 | "Revenue grows 26.5% YoY; Normalized PAT up by 25.8%" (l.60); "EBITDA grew 9.5% YoY to INR 34.2 crore, with an EBITDA margin of 8.7%" (l.70); "healthy profitability" (l.65) | AMBIGUOUS | The headline leads with revenue and normalized PAT. EBITDA growth of 9.5% against revenue growth of 26.5% implies Q2 FY26 EBITDA of about 31.2 on revenue of about 310.7, a margin of about 10.05%. The margin therefore fell about 135 bps YoY. The release calls this "healthy profitability" and gives no cause. The candidate causes are gross margin (component cost or mix) or opex (the sales/strategy/B2S investment at line 97). This runs against Notion test 4 (>=100 bps uplift) and bears on test 2. Lean bear. A4 question: split the 135 bps between gross margin and opex, and say whether the gross margin compressed for a third quarter. |
| FN-02 | F16 | R008, R009, R010, R056 | 71 | "Normalized PAT increased 25.8% YoY to INR 15.82 crore, with a margin of 4.0%." | AMBIGUOUS | The release does not define "normalized" (R056 FOOTNOTE_UNRESOLVED), and it does not state the Q2 FY26 comparison basis. Implied Q2 FY26 normalized PAT is about 12.58, a margin of about 4.05%. So PAT margin held flat while EBITDA margin fell about 135 bps. Costs below EBITDA (D&A, finance cost, other income, tax) improved by about 130 bps of revenue, and the release names no source. If the cause is other income or a lower ETR, it may not recur. A4 question: give the below-EBITDA bridge and the definition of normalized PAT for both periods. |
| FN-03 | F6 / F16 | R011, R012, R057, R035, R055 | 72-73, 103 | "Reported PAT for Q2 FY27 at INR 34.0 crore, including a one-off gain INR 18.2 crore earnout reversal" (l.72-73); "During the quarter, the company completed the integration of Altek Electronics" (l.103) | FORWARD-SIGNAL | The one-off is 18.2 / 34.0 = 53.5% of reported PAT. An earn-out reversal writes down contingent consideration, so the acquired business is tracking below its earn-out targets. The release does not name which acquisition the earn-out belongs to. Linking it to Altek is an INFERENCE from the same-quarter integration completion and from Notion memory (an FY26 Altek earn-out FV gain of about Rs20 Cr, which is not anchored evidence). If the link holds, this is the second reversal. The read is that Altek runs below its acquisition case. That raises goodwill/intangible impairment risk at the FY27 test, and the reversal flatters consolidated PAT in the S-vs-C comparison (Notion test 6). A4 questions: which entity's earn-out; the remaining contingent-consideration balance; Altek revenue/EBITDA against earn-out targets; and goodwill carrying value and impairment headroom. |
| FN-04 | F15 | R035, R036 | 103-104 | "Altek Electronics, acquisition in Connecticut, U.S. which has been renamed Cyient DLM Electronics Inc." | NEUTRAL-FACT | Entity rename: Altek Electronics becomes Cyient DLM Electronics Inc. Later filings (subsidiary list, AR Form AOC-1, related-party notes) will carry the new name, so the A4/Role 5 entity map must update. The A2 ledger note on R036 has the direction reversed (see Section 0). No prior entity list was available, so no other additions or deletions could be tested. |
| FN-05 | F16 | R013, R014, R016, R017, R018, R058 | 74, 94 | "Order Book reached an all-time high of INR 2,813.7 crores, increasing by INR 214.8 crores QoQ" (l.74); "with a book-to-bill ratio of 1.6" (l.94) | AMBIGUOUS | The walk does not tie. Order intake implied by the walk is 393.1 + 214.8 = 607.9, a book-to-bill of 1.546, which rounds to 1.5. A stated 1.6 implies intake of about 629.0, and so a book increase of about 235.9. That leaves about 21 Cr unexplained. Candidate reconciling items: cancellations/de-scoping, FX revaluation of USD orders (Altek), a book-to-bill on a different revenue or intake basis (TTM, or revenue that includes items outside the order book), or rounding of an undisclosed intake figure. The order book basis is undefined (R058): gross or net, executable horizon, inclusion of framework or LTA values. The book covers 2,813.7 / (393.1 x 4) = 1.79 years of current run-rate revenue. "Strong revenue visibility" (l.81) depends on the 12-month executable share, which the release does not give. Notion test 3 (falling book) is NOT triggered: the book rose from about 2,598.9. A4 questions: the book-to-bill definition; Q2 cancellations and FX; the 12-month executable share. |
| FN-06 | F16 | R015, R059 | 75-76 | "Free cash flow for Q2 FY27 stood at INR 17.2 crore, reflecting an improvement in cash generation during the quarter" | AMBIGUOUS | FCF is undefined (R059 FOOTNOTE_UNRESOLVED; pre- or post-acquisition payments, leases, interest). "Improvement" has no stated comparator (QoQ or YoY) and no prior figure. FCF is 1.09x normalized PAT and 0.51x reported PAT. The release gives no CFO, NWC days, inventory or receivables. Notion test 1 (the NWC-days cash falsifier, <=120 days) cannot be tested from this document. Lean bear: one quarter of positive FCF with no baseline is not evidence against STRUCTURAL. A4 questions: the FCF definition; Q2 CFO; H1 FY27 NWC days; the comparator behind "improvement". |
| FN-07 | F6 | R044, R054 | 107-108 | "Cyient DLM remains positive on the outlook for the year, supported by its record order book and continued demand" | AMBIGUOUS | The outlook gives no figure and does not name the fiscal year ("for the year", R054). The guidance-softening test (F16) cannot run, because no prior deck or release was available. If an earlier quarter carried a numeric FY27 growth guide, its absence here is a candidate softening. A4 question: does any earlier numeric FY27 guidance stand, and what growth rate does "positive" mean? |
| FN-08 | F6 | R042, R043, R045, R047, R037 | 85-87, 97, 100-101, 110-111 | "continued to invest in strengthening its sales, strategy and Build to Specifications (B2S) capabilities" (l.97); "while continuing to invest selectively in capabilities and new growth areas" (l.110-111); "AI and data centre infrastructure, robotics, and semiconductor capital equipment" (l.85-86) | FORWARD-SIGNAL | Management signals that investment ahead of revenue continues: sales, strategy, B2S and new verticals, all undated and unquantified. This is the most likely opex cause of the FN-01 margin compression, and it says the reported consolidated EBITDA margin uplift of >=100 bps (Notion test 4) is not imminent. The B2S investment bears on the proof gate, but the release gives no design-led share. The new verticals are "opportunities" (l.100), with no orders named, apart from three new logos "across its core businesses and new growth areas" (l.95). A4 questions: the opex added in H1; revenue or orders booked to date from AI/data centre, robotics and semicap; B2S revenue share. |

## 2. CHECKLIST SCORECARD

| Check | Status | Basis |
|---|---|---|
| F1 Zero-value standing line items | N.A. | Press release. No financial tables; A2 ZERO_STANDING count 0. |
| F2 Standalone vs consolidated | N.A. | No standalone or consolidated split in the document. FN-03 earn-out noted for test 6 at the results filing. |
| F3 Shell-entity detection | N.A. | No cost lines by entity. |
| F4 Unaudited contribution ratio | N.A. | No auditor report or Other Matters paragraph. |
| F5 Going concern / EoM scope | N.A. | No auditor report or EoM; no prior-quarter extract. |
| F6 Forward-commitment phrase mining | FINDING | Strict lexicon: 0 exact hits. Status-change language: "completed the integration" (l.103), "has been renamed" (l.104). Forward statements at l.85-87, 97, 107, 110-113. FN-03, FN-07, FN-08. |
| F7 Hedge phrase mining | PASS | Full lexicon run on all 136 lines: 0 hits. The release also carries no forward-looking safe-harbour disclaimer (recorded, not a finding). |
| F8 Tax forensics | N.A. | No tax lines. The below-EBITDA swing is in FN-02. |
| F9 OCI forensics | N.A. | No OCI lines. |
| F10 Share count and dilution | N.A. | The release carries no paid-up capital, share count or EPS. |
| F11 Reserves and net worth tie-out | N.A. | The release carries no net worth or reserves figure. |
| F12 Segment forensics | N.A. | Segments are named (Aerospace, Industrial led; Defence, Medical contributed; l.92-93) with no revenue, results, assets or liabilities. |
| F13 Board outcome beyond results | N.A. | Reg 30 press release cover letter (l.27-30), not a board outcome. No AR, AGM or director items. |
| F14 Note drafting inconsistencies | N.A. | No notes and no auditor letter. Minor style variance only ("Design-Led Manufacturing" l.64 vs "Design Led Manufacturing (DLM)" l.118; "crores" l.69 vs "crore" l.70). |
| F15 Entity list diffs | FINDING | Rename: Altek Electronics becomes Cyient DLM Electronics Inc. (l.103-104). FN-04. |
| F16 Dropped and reframed disclosures | FINDING | Prior deck not available, so the dropped-slide diff is impossible. Reframing and undefined bases inside this document: FN-01, FN-02, FN-05, FN-06 (and FN-03 normalized-PAT headline framing). |
| F17 Silence audit | N.A. | Concall-specific. This doctype is a press release. A Notion test coverage table follows for A4, for information only. |

## 3. COMMITMENT REGISTER (F6)

| commitment | implied date | ref | status word |
|---|---|---|---|
| Integration of Altek Electronics (Connecticut, U.S.) | Q2 FY27 (quarter ended 30-Sep-2026) | l.103, R035, R055 | completed |
| Altek Electronics renamed Cyient DLM Electronics Inc. | Q2 FY27 or earlier ("has been renamed") | l.103-104, R036 | completed |
| Positive outlook "for the year", no figure | FY27 implied (31-Mar-2027); year not named | l.107, R044, R054 | none (outlook) |
| Execute existing order book; maintain operating discipline; invest selectively | ongoing, undated | l.110-111, R045 | underway ("will remain focused") |
| Invest in sales, strategy and B2S capabilities | ongoing, undated | l.97, R047 | underway ("continued to invest") |
| Invest in AI/data centre infrastructure, robotics, semiconductor capital equipment | long-term, undated | l.85-87, l.100-101, R042, R043 | underway ("investing"; "seeing opportunities") |
| Deepen existing customer relationships, add customers, broaden lifecycle participation | "Over the longer term", undated | l.111-113, R046 | none (intent, "will seek to") |

## 4. NOTION TEST COVERAGE (information for A4; F17 is N.A. on this doctype)

| # | Notion test | Addressed in release? | Evidence |
|---|---|---|---|
| 1 | Cash falsifier: NWC days <=120 by Q4 FY27 with positive CFO | NO | Only FCF 17.2, undefined (l.75). No CFO and no NWC data. FN-06. |
| 2 | Gross margin: third compression quarter without a component-cost cause | NO | Gross margin not disclosed. EBITDA margin about -135 bps YoY implied (l.70), cause not given. FN-01. |
| 3 | Order book: Rs2,600 Cr and 1.5x at Q1; falling book tests momentum | YES | 2,813.7, +214.8 QoQ (l.74); book-to-bill 1.6 (l.94). Book rising; test not triggered. Book-to-bill tie-out gap, FN-05. |
| 4 | Proof gate: design-led share double digits for two quarters plus >=100 bps EBITDA margin uplift | NO (share); margin moved the wrong way | No design-led or B2S share disclosed. Margin about -135 bps YoY implied. FN-01, FN-08. |
| 5 | Related-party flow to parent Cyient Ltd | NO | Not mentioned. The parent appears only as a media contact (l.134-136). |
| 6 | Standalone vs consolidated divergence (India vs Altek; earn-out FV gain) | NO (split); earn-out recurs | 18.2 Cr earn-out reversal (l.72-73); Altek rename and integration (l.103-104). FN-03, FN-04. |

## 5. PIPELINE NOTES
- A2 ledger R036 note has the rename direction reversed. The fulltext governs: OLD Altek Electronics, NEW Cyient DLM Electronics Inc.
- A1 line drifts on R027, R036, R041 (Section 0) are off by one to three lines. They are not material and the quotes were located.
- No source document access was needed or used.

```yaml
stage: A3-forensics
company: "CYIENTDLM"
quarter: "q2fy27"
doctype: "presentation (press release, file tag pressrelease)"
model: "claude-opus-5-5"
status: complete
forensics_path: "C:\\Users\\SUMIT SHARMA\\repos\\inflection-pipeline\\.claude\\worktrees\\q2fy27\\runs\\cyientdlm-q2fy27\\work\\forensics_pressrelease_cyientdlm_q2fy27.md"
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
  F14: N.A.
  F15: FINDING
  F16: FINDING
  F17: N.A.
findings:
  - {id: "FN-01", check: "F16", line: "60, 65, 70", classification: "AMBIGUOUS", implication: "EBITDA +9.5% vs revenue +26.5% implies YoY margin ~10.05% to 8.7% (~-135 bps), cause undisclosed, framed as 'healthy profitability'; runs against Notion test 4, bears on test 2; ask GM vs opex split"}
  - {id: "FN-02", check: "F16", line: "71", classification: "AMBIGUOUS", implication: "Normalized PAT undefined; PAT margin flat ~4.0% while EBITDA margin -135 bps implies ~130 bps below-EBITDA improvement with no source named; possible non-recurring other income or ETR"}
  - {id: "FN-03", check: "F6", line: "72-73, 103", classification: "FORWARD-SIGNAL", implication: "18.2 Cr earn-out reversal = 53.5% of reported PAT; acquiree below earn-out targets; [INFERENCE] Altek, second reversal after FY26; goodwill impairment risk at FY27 test; ask remaining contingent consideration and Altek vs targets"}
  - {id: "FN-04", check: "F15", line: "103-104", classification: "NEUTRAL-FACT", implication: "Altek Electronics renamed Cyient DLM Electronics Inc.; update entity map; A2 R036 note has direction reversed"}
  - {id: "FN-05", check: "F16", line: "74, 94", classification: "AMBIGUOUS", implication: "Order book walk implies intake 607.9 = 1.55x book-to-bill vs stated 1.6 (~21 Cr gap: cancellations, FX, basis); order book basis undefined; 1.79 years cover, 12-month executable share not given; Notion test 3 not triggered (book rising)"}
  - {id: "FN-06", check: "F16", line: "75-76", classification: "AMBIGUOUS", implication: "FCF 17.2 Cr undefined, 'improvement' with no comparator; no CFO or NWC days, so Notion test 1 cash falsifier untestable from this document"}
  - {id: "FN-07", check: "F6", line: "107-108", classification: "AMBIGUOUS", implication: "Outlook 'positive for the year' carries no figure and no named FY; guidance-softening diff impossible without prior deck; ask whether any numeric FY27 guide stands"}
  - {id: "FN-08", check: "F6", line: "85-87, 97, 100-101, 110-111", classification: "FORWARD-SIGNAL", implication: "Continued investment ahead of revenue (sales, strategy, B2S, AI/data centre, robotics, semicap); likely opex cause of margin compression; >=100 bps margin uplift (test 4) not imminent; no design-led share disclosed"}
forward_signals: ["FN-03", "FN-08"]
ambiguous: ["FN-01", "FN-02", "FN-05", "FN-06", "FN-07"]
commitments:
  - {commitment: "Integration of Altek Electronics (Connecticut, U.S.)", implied_date: "Q2 FY27 (qe 30-Sep-2026)", ref: "l.103, R035, R055", status_word: "completed"}
  - {commitment: "Altek Electronics renamed Cyient DLM Electronics Inc.", implied_date: "Q2 FY27 or earlier", ref: "l.103-104, R036", status_word: "completed"}
  - {commitment: "Positive outlook for the year, no figure", implied_date: "FY27 implied, year not named", ref: "l.107, R044, R054", status_word: "none (outlook)"}
  - {commitment: "Execute existing order book, operating discipline, invest selectively", implied_date: "ongoing, undated", ref: "l.110-111, R045", status_word: "underway"}
  - {commitment: "Invest in sales, strategy and B2S capabilities", implied_date: "ongoing, undated", ref: "l.97, R047", status_word: "underway"}
  - {commitment: "Invest in AI/data centre, robotics, semiconductor capital equipment", implied_date: "long-term, undated", ref: "l.85-87, l.100-101, R042, R043", status_word: "underway"}
  - {commitment: "Deepen customer relationships, add customers, broaden lifecycle participation", implied_date: "longer term, undated", ref: "l.111-113, R046", status_word: "none (intent)"}
gate_a3: pass
blank_checks: []
analyst_note: "The release reframes a weak margin quarter. Revenue rose 26.5% but EBITDA rose 9.5%, an implied ~135 bps YoY margin drop. The headline leads with normalized PAT, which matched revenue growth only because costs below EBITDA improved by ~130 bps, source unstated. Reported PAT is 53.5% one-off: an 18.2 Cr earn-out reversal. The release does not name the acquiree. Linking it to Altek is inference, from the same-quarter integration completion and Notion's FY26 earn-out gain. If the link holds, two reversals say the US arm runs below its acquisition case. That points to an impairment test, and it flatters consolidated PAT against standalone. The book-to-bill of 1.6 does not tie to the order book walk (1.55x implied). Only Notion test 3 (order book) is answerable here, and it holds. Tests 1, 2, 4, 5 and 6 need the results filing and the concall. A2 R036 has the rename direction reversed. The fulltext governs: Altek became Cyient DLM Electronics Inc."
```
