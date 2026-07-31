# A3 FORENSIC NOTES — Ram Ratna Wires Ltd (RAMRAT) — Q1 FY27 — pressrelease

Source extract: `/home/user/inflection-pipeline/runs/ramrat-q1fy27/work/extract_pressrelease_ramrat_q1fy27.txt`
Ledger reconciled: 50 / 50 ledger items read verbatim at cited lines (Tables 1-4). 100%.
Doctype: prose investor / press release (management claim-set). Structurally Reg-33-specific checks
(auditor EoM diff, Board Outcome agenda, note-level items, segment assets/liabilities, tax/OCI/EPS
schedules) are absent from this document and marked N.A. explicitly. No prior-quarter extract exists
(first quarterly run), so all verbatim-diff checks fall back to single-period reasoning.

---

## FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|----|-------|----------------|------|----------------------|----------------|---------------------|
| A3-F2-01 | F2 | T1 hdr / T4 #9 | 66, 105 | "(Consolidated)" | AMBIGUOUS | Every figure is consolidated-only; standalone is NOT disclosed. With an unnamed subsidiary + JV (BLDC/hub motors/HVLS/wind-tower) folded in, the reader cannot see how much of the +89% revenue / +121% PAT is core winding-wire vs the diversification vehicles. S-vs-C gap uncomputable. A4 must ask for the standalone split. |
| A3-F6-01 | F6 | T3 #14, #8, #5 | 100, 95, 90-91 | "continued improvement in working capital efficiency" | FORWARD-SIGNAL | The single most thesis-relevant commitment (FLAG-CASH INDETERMINATE; prior FY26 CFO -96 Cr SA / -93 Cr CN) is stated as an already-achieved "continued improvement" with ZERO supporting metric — no WC days, no cash cycle, no CFO. A dateable claim with no delivery evidence. Feeds Role 5 promise-vs-delivery tracker. |
| A3-F16-01 | F16 | T1 #2,#3,#4,#5 | 81-84 | "PAT 39.2 (Q4 FY26) ... 35.2 (Q1 FY27)" | AMBIGUOUS | Headline is all YoY ("+89% / +109% / +121%"). Sequentially (Q1 FY27 vs Q4 FY26): Revenue +5.7% but EBITDA -3.9% (89.6 vs 93.2), PAT -10.2% (35.2 vs 39.2), EBITDA margin -50 bps (4.8% vs 5.3%), PAT margin -30 bps (1.9% vs 2.2%). Revenue rose while every profit line and both margins FELL QoQ. The QoQ deterioration is present in the table but omitted from all narrative. Selective-highlight; A4 to ask cause of sequential margin compression. |
| A3-F16-02 | F16 | T2 #1,#3,#7,#9 | 61, 74 | "Revenue Up 89% ... PAT Up 121%" | NEUTRAL-FACT | Headline growth rates round UP the table's exact figures (revenue 88.6% -> "89%"; PAT 120.8% -> "121%"), while the exact figure that did NOT need rounding (EBITDA 109.0%) is left as "109%". Directionally favourable rounding. Minor, but a framing tell. |
| A3-F16-03 | F16 | T2 #10 / T3 #6 | 94 | "contribution to revenue rising to 26%" | AMBIGUOUS | Copper-tubes mix given only as a %, no absolute Rs and no prior-quarter comparator despite "rising" implying one. 26% x 1,853.3 = ~Rs 482 Cr implied, which cannot be reconciled inside this document (no segment table) and cannot be tested against the monitoring threshold (Q4 FY26 copper tubes Rs 347.20 Cr). A4 to demand the absolute segment number. |
| A3-F17-01 | F17 | T3 #14 | 100 | "continued improvement in working capital efficiency" | CONFIRMATORY-NEGATIVE | Monitoring item 1 (negative FY27 CFO 2nd consecutive year, WC days not normalising) is NOT addressed with any hard number. The release asserts the conclusion ("improvement") that the thesis flags as the open risk, and supplies no CFO / WC-days / receivables / inventory data. Sustained silence on a deteriorating cash metric = confirmatory negative per Role 5. |
| A3-F17-02 | F17 | (absent) | n/a (whole doc) | no mention of factoring / supplier finance | CONFIRMATORY-NEGATIVE | Monitoring item 3 (off-BS-financing gate: Rs 647 Cr supplier finance / Rs 187 Cr factoring) is NOT addressed. A "working capital efficiency" claim with no cash statement leaves open that any apparent improvement is financed off balance sheet. Silence, no line number because the disclosure is simply absent. |
| A3-F17-03 | F17 | (absent) | n/a (whole doc) | no mention of tax dispute / CTC-HVDC / Silvassa / EoM | CONFIRMATORY-NEGATIVE | Monitoring item 4 wholly unaddressed: no Section 132/148 contingent tax (~Rs 67-104 Cr), no CTC/HVDC commercial-start confirmation (due ~Q2 CY2026), no Silvassa Rs 86 Cr commissioning update, no auditor Emphasis-of-Matter status. Only "continue to invest in capacity expansion" (line 95, unquantified) gestures at capex. |

---

## CHECKLIST SCORECARD (all 17, exactly one status each)

| F# | Status | One-line basis |
|----|--------|----------------|
| F1 | N.A. | Press release carries no line-item template; ledger confirms ZERO_STANDING not triggered anywhere. No zero-value standing rows to interrogate. |
| F2 | FINDING | Table labelled "(Consolidated)" only (lines 66, 105); standalone not disclosed, S-vs-C gap uncomputable — A3-F2-01. |
| F3 | N.A. | No standalone-vs-consolidated cost lines (COGS / employee / depreciation) in a press release; shell-entity test not runnable. |
| F4 | N.A. | No auditor Other Matters / component-auditor disclosure. (Whole result set is "unaudited" per line 27, but no unaudited-contribution ratio is quantifiable.) |
| F5 | N.A. | No auditor EoM / going-concern paragraph in this doctype and no prior quarter to verbatim-diff. |
| F6 | FINDING | Forward commitments present but all undated and unquantified; WC-efficiency pledge is the load-bearing one — A3-F6-01. |
| F7 | PASS | Only boilerplate Safe Harbor hedges ("subject to risks and uncertainties", line 135; risk list incl. "cash flow projections", line 140). No note-level pre-emptive hedge newly added; no prior quarter to diff. |
| F8 | N.A. | No tax line, no PBT, no ETR, no deferred-tax disclosure — tax forensics not computable. |
| F9 | N.A. | No OCI / actuarial disclosure in a press release. |
| F10 | N.A. | No paid-up capital, share count, or EPS (basic/diluted) disclosed. |
| F11 | N.A. | No Other Equity / net-worth figures to tie out. |
| F12 | N.A. | No segment assets/liabilities table; only a single copper-tubes mix % (handled in F16). |
| F13 | N.A. | No Board Outcome, AGM notice, or director-appointment content in this doctype. |
| F14 | PASS | Entity naming consistent across the release (Ram Ratna Wires Ltd / RRWL / brand RR Shramik); no auditor letter present to cross-check note-vs-letter wording. |
| F15 | N.A. | No consolidation entity list and no prior quarter; entity-diff not possible (subsidiary + JV referenced but unnamed, lines 95-96, 117). |
| F16 | FINDING | YoY-only framing masks QoQ profit/margin decline; favourable up-rounding; copper-tubes % with no comparator — A3-F16-01/02/03. |
| F17 | FINDING | Silence audit vs Notion checklist: 3 of 4 monitoring items wholly unaddressed, the 4th asserted without data — A3-F17-01/02/03. |

Checks blank: none. GATE A3: pass.

---

## COMMITMENT REGISTER (from F6 — MD quote, lines 88-104)

| commitment | implied date | ref | status word |
|------------|--------------|-----|-------------|
| "continued investments in expanding our business portfolio and manufacturing capabilities" | none stated | line 90-91 | ongoing ("continued") |
| "continue to invest in capacity expansion" | none stated | line 95 | ongoing ("continue") |
| "strengthen our presence through our subsidiary and joint venture" | none stated | line 95-96 | ongoing |
| "continued improvement in working capital efficiency" | none stated | line 100 | ongoing ("continued") — asserted as already achieved, no metric |
| "disciplined capital allocation" | none stated | line 100 | ongoing |
| "well positioned to capitalize on the opportunities ahead" | none stated | line 102 | forward, boilerplate |
| "committed to creating sustainable value for all our stakeholders" | none stated | line 103-104 | boilerplate |

Register note: every commitment is undated and unquantified. None matches the hard F6 lexicon ("will be", "expected by", "commenc", "board has approved", etc.), i.e. management made no dateable, testable pledge. The WC-efficiency line is phrased as accomplished fact rather than a forward target, which pre-empts scrutiny of the very metric flagged FLAG-CASH INDETERMINATE.

---

## WHAT WAS NOT DISCUSSED (F17 silence audit vs Notion monitoring checklist)

| # | Monitoring item | Addressed? | Consecutive-quarter silence | Note |
|---|-----------------|-----------|-----------------------------|------|
| 1 | FY27 CFO negative 2nd yr / WC days not normalising | NO (asserted "improvement", no data) | 1 (first quarterly run; risk live) | line 100 claim substitutes for evidence |
| 2 | Copper tubes falling 2+ qtrs below Rs 347.20 Cr (Bhiwadi ramp) | PARTIAL — mix 26% only, no absolute Rs | 1 | line 94; absolute unreconcilable |
| 3 | Off-BS financing gate (supplier finance Rs 647 Cr / factoring Rs 187 Cr) | NO | 1 | absent entirely |
| 4 | Contingent tax ~Rs 67-104 Cr; CTC/HVDC start ~Q2 CY26; Silvassa Rs 86 Cr; auditor EoM | NO | 1 | only unquantified "capacity expansion", line 95 |

---

## CROSS-REFERENCE FOR A4 (flagged findings to convert into management questions)

FORWARD-SIGNAL: A3-F6-01.
AMBIGUOUS (lean-bear, convert to questions): A3-F2-01, A3-F16-01, A3-F16-03.
CONFIRMATORY-NEGATIVE (Role 5 silence / deterioration): A3-F17-01, A3-F17-02, A3-F17-03.
NEUTRAL-FACT: A3-F16-02.

```yaml
stage: A3-forensics
company: "RAMRAT"
quarter: "Q1 FY27"
doctype: "pressrelease"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/ramrat-q1fy27/work/forensics_pressrelease_ramrat_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: N.A.
  F2: FINDING
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
  F14: PASS
  F15: N.A.
  F16: FINDING
  F17: FINDING
findings:
  - {id: "A3-F2-01", check: "F2", line: "66,105", classification: "AMBIGUOUS", implication: "Consolidated-only basis; standalone not disclosed, core-vs-diversification split unobservable"}
  - {id: "A3-F6-01", check: "F6", line: "100", classification: "FORWARD-SIGNAL", implication: "Working-capital-efficiency 'improvement' asserted with zero metric against live negative-CFO flag"}
  - {id: "A3-F16-01", check: "F16", line: "81-84", classification: "AMBIGUOUS", implication: "QoQ PAT -10.2% and margins -30/-50 bps hidden behind YoY-only headline"}
  - {id: "A3-F16-02", check: "F16", line: "61,74", classification: "NEUTRAL-FACT", implication: "Growth rates rounded up (88.6->89, 120.8->121); minor favourable framing"}
  - {id: "A3-F16-03", check: "F16", line: "94", classification: "AMBIGUOUS", implication: "Copper-tubes 26% mix, no absolute Rs and no comparator; ~482 Cr implied, unreconcilable vs 347.20 threshold"}
  - {id: "A3-F17-01", check: "F17", line: "100", classification: "CONFIRMATORY-NEGATIVE", implication: "Silence on CFO/WC days while claiming improvement"}
  - {id: "A3-F17-02", check: "F17", line: "n/a", classification: "CONFIRMATORY-NEGATIVE", implication: "No mention of supplier-finance/factoring off-BS gate"}
  - {id: "A3-F17-03", check: "F17", line: "n/a", classification: "CONFIRMATORY-NEGATIVE", implication: "No tax contingency / CTC-HVDC / Silvassa / auditor EoM update"}
forward_signals: ["A3-F6-01"]
ambiguous: ["A3-F2-01", "A3-F16-01", "A3-F16-03"]
commitments:
  - {commitment: "continued investments in expanding business portfolio and manufacturing capabilities", implied_date: "none", ref: "line 90-91", status_word: "ongoing"}
  - {commitment: "continue to invest in capacity expansion", implied_date: "none", ref: "line 95", status_word: "ongoing"}
  - {commitment: "strengthen presence through subsidiary and joint venture", implied_date: "none", ref: "line 95-96", status_word: "ongoing"}
  - {commitment: "continued improvement in working capital efficiency", implied_date: "none", ref: "line 100", status_word: "ongoing-asserted"}
  - {commitment: "disciplined capital allocation", implied_date: "none", ref: "line 100", status_word: "ongoing"}
  - {commitment: "well positioned to capitalize on the opportunities ahead", implied_date: "none", ref: "line 102", status_word: "forward"}
  - {commitment: "committed to creating sustainable value for all stakeholders", implied_date: "none", ref: "line 103-104", status_word: "boilerplate"}
gate_a3: pass
blank_checks: []
```
