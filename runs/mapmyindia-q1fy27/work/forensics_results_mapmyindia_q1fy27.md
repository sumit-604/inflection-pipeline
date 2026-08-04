# A3 FORENSIC NOTES — C.E. Info Systems Ltd / MapMyIndia (MAPMYINDIA) — Q1 FY27 — doctype: results

Source extract: `runs/mapmyindia-q1fy27/work/extract_results_mapmyindia_q1fy27.txt`
Ledger reconciled against: `runs/mapmyindia-q1fy27/work/ledger_results_mapmyindia_q1fy27.md`
Unit convention: Rupees in lakhs (Lakhs x0.01 = Cr). Four periods on the face:
Q1FY27 (30.06.2026, Unaudited) | Q4FY26 (31.03.2026, Audited) | Q1FY26 (30.06.2025, Unaudited) | FY26 (31.03.2026, Audited).
Ledger reconciliation: 9 ledger sections + all 77 line_items + 12 notes + 11 auditor paras + 6 entities + 7 signature blocks + 5 annexure rows read verbatim at cited lines. 100% reconciled. No unread rows.

Doctype note: this is a P&L-only Reg 33 quarterly filing. There is NO balance sheet, NO cash-flow statement, NO receivables/ageing, NO segment assets/liabilities. That scope limitation drives several findings and the binding falsifier below.

---

## BINDING FALSIFIER — assessed explicitly (FLAG-CASH / receivables)

The thesis pre-committed that Q1 FY27 consolidated receivables ABOVE the Rs176.4 Cr FY26 close, on flat/up sequential revenue, with the 6-month+ ageing bucket widening, confirms FLAG-CASH as structural.

**Resolution: UNRESOLVABLE FROM THIS FILING.** The filing discloses no balance sheet and no receivables figure of any kind. The only balance-sheet datum present is "Other equity," and it is populated in the FY26 year-end column ONLY (consolidated 89,400 at line 272; standalone 92,027 at line 458), blank in all three interim columns per standard interim convention. There is no trade-receivables line, no ageing schedule, no contract-asset (unbilled) line, and no cash-flow statement anywhere in the nine pages. Per operating rule, I do NOT infer a number. The falsifier cannot be tested on this document; escalate to the Q1 FY27 concall / the FY27 interim balance sheet. Logged as finding **BF**.

---

## FINDINGS TABLE

| id | check | ledger row ref | line | verbatim quote | classification | forward implication |
|----|-------|----------------|------|----------------|----------------|---------------------|
| F2-1 | F2 | Sec.4 rows 18/22 (245,251) + Sec.5 row 18 (450) | 245 / 251 / 450 | consol "5,038" / "4,974" vs standalone "5,542" | FORWARD-SIGNAL | Subsidiaries+JV net contribution = -504 lacs in Q1FY27 (consol NPAT 5,038 below standalone 5,542), the deepest drag of the four periods (Q1FY26 -297, Q4FY26 +556, FY26 +283). Consol-vs-standalone PAT gap swung ~19.5pp of standalone PAT QoQ (+9.3% -> -10.2%), far beyond the 5pp trigger. Subsidiary block is loss-making this quarter; ties to Gtropy concentration. |
| F2-2 | F2 | Sec.4 row 2 (227) + Sec.5 row 2 (432) | 227 / 432 | "Other income 1,965 1,775 1,367 5,240" | FORWARD-SIGNAL | Consolidated other income Rs1,965 lacs = 29.6% of PBT (6,644) and +43.7% YoY (1,367 -> 1,965). Standalone other income 1,838 of parent's 1,965 — treasury income sits at the parent (the ~Rs517 Cr idle-treasury book, checklist item 10). Earnings quality increasingly non-operating; rate-cut / deployment risk to run-rate. |
| F3-1 | F3 | Sec.2a para 7 (line 168-181) | 169 | "1 subsidiary ... total revenue of Rs. Nil, total net loss after tax of Rs. 11 lacs" | AMBIGUOUS | One consolidated subsidiary is a Nil-revenue, loss-making, wholly-unreviewed (management-furnished) entity — a dormant/shell. Identity not disclosed (3 subs listed: Gtropy, Mappls DT, C.E. Info International USA; the USA WOS is the likely candidate). Winding-down vs future vehicle unknown — A4 question. |
| F8-1 | F8 | Sec.4 row 16 (243) + Sec.5 row 16 (448) | 243 / 448 | "Taxation related to earlier years ... 364 ... 374" | NEUTRAL-FACT | Prior-year tax true-up of Rs364 lacs (consol) / Rs363 lacs (standalone) booked in Q4FY26 (nil in Q1FY27). Non-zero earlier-years tax = FINDING per rule; signals a FY26 assessment/reassessment true-up. Historical, contained. |
| F8-2 | F8 | Sec.4 row 15 (242) | 242 | "Deferred tax charge / (benefit) (93) (1,696) (183) (1,653)" | FORWARD-SIGNAL | Persistent deferred-tax CREDITS every period (consol). Q1FY27 ETR = 1,606/6,644 = 24.2%, BELOW statutory 25.17%; the 93-lac deferred credit shields ~140bps. Persistent DTA credits = future ETR step-up risk as the shield exhausts. (Standalone deferred flipped to a +73 charge — subsidiary DTA drives the consolidated credit.) |
| F12-1 | F12 | Sec.6a Note 5 (316-318) + Note-1 breakup (297-300) | 316 / 297-300 | "single primary business segment" ; "Sale of devices 2,311 1,785 760 5,468" | FORWARD-SIGNAL (A4) | Single-segment claim suppresses Map-vs-IoT economics. The Note-1 revenue split (the only quasi-segment data) shows device revenue +204% YoY (760 -> 2,311) while Map-data & services grew just +2.3% (11,401 -> 11,661) and fell -8.3% QoQ. Map-data share of revenue dropped ~10pp to 83.5%. Consolidated operating EBITDA margin (ex-other-income) fell ~570bps YoY to 40.2% (Q1FY26 45.9%). Margin-dilutive hardware mix; statutory single-segment reporting hides it. |
| F13-1 | F13 | Sec.1 agenda item 2 (52) + Sec.7 Annexure-B | 53 / 565-569 | "Mr. Nikhil Kumar ... stepped down as the Whole Time Director of Mappls DT Private Limited, Material Wholly Owned Subsidiary ... w.e.f closure of business hours of August 03, 2026" | AMBIGUOUS | WTD of a Material WOS departed one day before the board meeting; reason field "NA" (line 572), no successor disclosed. Leadership gap at Mappls DT (the "DT" digital-twin/new-vehicle WOS). Only substantive board action beyond results this quarter. A4/A5 governance question. |
| F14-1 | F14 | Sec.5 sig block (224) + Sec.3 row 4 (109) | 462-469 / 128 | standalone sign-off ends "Place: New Delhi" with no Date line; entity "Koga Tech Labs Private Limited" | NEUTRAL-FACT | Cumulative minor drafting inconsistencies: the standalone STATEMENT sign-off (462-469) omits the "Date:" line that all other six sign-offs carry (Aug 4, 2026); entity rendered "Koga Tech Labs" (128) vs the thesis's "Kogo Tech Labs." Both plausibly OCR, but the missing-date on a signed statement is a completeness data point. |
| F15-1 | F15 | Sec.3 entity list (102-121) | 128 | "Koga Tech Labs Private Limited Associate" | AMBIGUOUS | No prior-quarter consolidation list was provided — additions / deletions / subsidiary<->JV relationship changes CANNOT be verified (verbatim diff impossible; stated plainly per rules, not invented). Live verification item: "Koga" vs thesis "Kogo," and Gtropy's stake move (baseline: raised to 96%) is undisclosed on the face. Verify entity roster and stakes at the AR. |
| BF | Falsifier / BS-scope | Sec.4 row 37 (272) + Sec.5 row 24 (458) | 272 / 458 | "Other equity attributable to owners of the Company 89,400" (FY26 column only) | AMBIGUOUS | No balance sheet, no receivables, no ageing, no cash-flow statement in the filing. FLAG-CASH falsifier (receivables > Rs176.4 Cr, 6m+ bucket widening) is untestable here. Escalate to concall / interim BS. No number inferred. |

---

## CHECKLIST SCORECARD (F1-F17)

| Check | Status | One-line basis |
|-------|--------|----------------|
| F1 ZERO-VALUE STANDING | PASS | Ledger zero_standing = 0; no line item is zero/nil/dash across all four periods. No exceptional / discontinued-ops / profit-on-sale-of-subsidiary / impairment template lines exist to interrogate. Three partial-blank rows (earlier-years tax, standalone cost of materials, other equity) noted in ledger Sec.9, none all-period-zero. |
| F2 STANDALONE vs CONSOLIDATED | **FINDING** | F2-1: subsidiary+JV drag -504 lacs (consol NPAT below standalone), QoQ gap swing ~19.5pp of standalone PAT > 5pp trigger. F2-2: other income 29.6% of PBT, +43.7% YoY. |
| F3 SHELL-ENTITY DETECTION | **FINDING** | F3-1: auditor para 7 identifies one Nil-revenue, Rs11-lac-loss, unreviewed subsidiary = dormant/shell (identity undisclosed). Group in aggregate is NOT a shell (subs carry ~1,203 lacs employee cost, 1,524 lacs revenue). |
| F4 UNAUDITED CONTRIBUTION RATIO | PASS | Non-MSKA-reliance amounts: associates -37 (other auditors), subsidiary -11 + JV -27 (mgmt-furnished) = Rs75 lacs abs = ~1.5% of consol PAT 4,974; below 10%. No YoY jump — associate+JV drag NARROWED YoY (-157 -> -64 lacs). |
| F5 GOING CONCERN / EoM | PASS | Both LRRs unmodified (lines 153-158, 385-389); no going-concern paragraph, no Emphasis of Matter; only standard Other-Matter reliance paras. Verbatim prior-quarter EoM diff NOT performed — no prior-quarter extract available (stated, not invented). Nothing adverse. |
| F6 FORWARD-COMMITMENT MINING | PASS | Lexicon sweep of notes/letter: only "commenced" (line 42, board-meeting timing) and completed corporate action (Nikhil Kumar cessation). No "expected to be / will be / underway / proposes to / intends to / in the process of / subject to approval." No forward-dated OPEN commitments. Register below carries the one completed action. |
| F7 HEDGE PHRASE MINING | PASS | Only hedge-adjacent phrase is auditor scope language "not subject to review" (line 168) — F4 territory, not a management business hedge. No newly-added note hedge on revenue lumpiness or customer concentration. |
| F8 TAX FORENSICS | **FINDING** | F8-1: non-zero "earlier years" tax Rs364/363 lacs (Q4FY26). F8-2: persistent deferred credits, Q1FY27 ETR 24.2% < 25.17% statutory, ~140bps DTA shield, future step-up risk. |
| F9 OCI FORENSICS | PASS | Q1FY27 actuarial remeasurement -12 lacs (consol) / -11 (standalone), small; FY26 full year was +281 / +220. No single-quarter swing exceeding prior year; no assumption-change signal. |
| F10 SHARE COUNT & DILUTION | PASS | Paid-up flat QoQ at 1,095 lacs; +7 lacs YoY (1,088 -> 1,095) = ~3.5 lakh shares, traces to ESOP allotment. Basic-diluted spread NARROWED YoY (0.09 -> 0.04), fewer dilutive instruments — benign. No warrant/round on the face. |
| F11 RESERVES & NET-WORTH TIE-OUT | PASS | Net worth (FY26 close): consol 89,400+1,095 = Rs904.95 Cr; standalone 92,027+1,095 = Rs931.22 Cr. Standalone EXCEEDS consolidated by ~Rs26 Cr — cumulative subsidiary/JV/associate losses eroded consol reserves (corroborates F2). No third-party number in the filing to reconcile against; no gap identifiable. |
| F12 SEGMENT FORENSICS | **FINDING** | F12-1: Note 5 declares single segment (no segment assets/liabilities disclosed); Note-1 device-vs-map-data split reveals device +204% YoY vs map-data +2.3%, EBITDA margin -570bps YoY, margin-dilutive mix hidden from statutory segment disclosure. |
| F13 BOARD OUTCOME BEYOND RESULTS | **FINDING** | F13-1: WTD of Material WOS Mappls DT stepped down (line 53), reason "NA," no successor. No AR/AGM/record-date/dividend/capital-raise resolutions this meeting (Q1 board, AR approval not expected). |
| F14 NOTE DRAFTING INCONSISTENCIES | **FINDING** | F14-1: standalone statement sign-off missing the "Date:" line (462-469) that six other blocks carry; "Koga" vs "Kogo" entity name (128). Individually immaterial, cumulatively a governance data point; OCR possibility caveated. |
| F15 ENTITY LIST DIFFS | **FINDING** | F15-1: no prior-quarter consolidation list provided — additions/deletions/relationship-changes UNVERIFIABLE (diff impossible, stated per rules). Live items: Koga/Kogo name, undisclosed Gtropy stake move. Verify at AR. |
| F16 DROPPED/REFRAMED DISCLOSURES | N.A. | Presentation-specific check; this is a results filing. |
| F17 CONCALL SILENCE AUDIT | N.A. | Concall-specific check; no transcript in scope. (Notion checklist items 1-10 remain unaddressed by a P&L-only filing — noted for A4 concall prep, not a silence-audit row here.) |

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/turn ref | status word |
|------------|--------------|---------------|-------------|
| Nikhil Kumar cessation as Whole Time Director of Mappls DT Private Limited (Material WOS) | w.e.f. close of business Aug 03, 2026 | Agenda item 2 (line 53); Annexure-B (lines 565-569) | completed |
| Board approval of Q1 FY27 unaudited standalone + consolidated results with limited-review report | Aug 4, 2026 | Agenda item 1 (line 45); Notes 2 (lines 307-311 / 502-506) | completed |

No forward-dated OPEN management commitments present in the notes (bare Reg 33 filing — no capex, product-launch, order-execution, or approval-pending language to date-track for the Role 5 promise tracker).

---

## FORWARD-SIGNAL SUMMARY (for A4 -> management questions)

1. **Margin-dilutive mix shift (F12-1, F2-1).** Device revenue tripled YoY (760 -> 2,311 lacs) while Map-data & services grew +2.3% and fell -8.3% QoQ; consolidated operating EBITDA margin -570bps YoY to 40.2%. Ask management for the Map-core organic growth ex-hardware and the IoT/Gtropy standalone margin.
2. **Subsidiary block loss-making this quarter (F2-1).** Consol NPAT (5,038) below standalone (5,542) by 504 lacs, deepest drag of four periods, reversing Q4FY26's +556. Ask for Gtropy P&L and overdraft utilisation.
3. **Earnings increasingly treasury-driven (F2-2).** Other income = 29.6% of PBT, +43.7% YoY. Ask for the treasury deployment / capital-allocation plan (checklist item 10).
4. **ETR below statutory on persistent DTA credits (F8-2).** 24.2% vs 25.17%; ~140bps shield. Ask when normalization is expected.

## AMBIGUOUS / ESCALATE (for A4/A5)

- **BF** — receivables/FLAG-CASH untestable; take to concall/interim BS.
- **F3-1** — identity and purpose of the Nil-revenue unreviewed subsidiary.
- **F12-1** — why single-segment when Map and IoT economics diverge sharply.
- **F13-1** — reason for Mappls DT WTD departure and succession.
- **F15-1** — entity roster / Gtropy stake diff unverifiable without prior list; Koga/Kogo name.

---

```yaml
stage: A3-forensics
company: "MAPMYINDIA"
quarter: "Q1 FY27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/mapmyindia-q1fy27/work/forensics_results_mapmyindia_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: PASS
  F2: FINDING
  F3: FINDING
  F4: PASS
  F5: PASS
  F6: PASS
  F7: PASS
  F8: FINDING
  F9: PASS
  F10: PASS
  F11: PASS
  F12: FINDING
  F13: FINDING
  F14: FINDING
  F15: FINDING
  F16: N.A.
  F17: N.A.
findings:
  - {id: "F2-1", check: "F2", line: "245/251/450", classification: "FORWARD-SIGNAL", implication: "Subsidiary+JV net drag -504 lacs (consol NPAT below standalone); QoQ S-vs-C PAT gap swing ~19.5pp > 5pp trigger"}
  - {id: "F2-2", check: "F2", line: "227/432", classification: "FORWARD-SIGNAL", implication: "Other income 29.6% of PBT, +43.7% YoY; earnings quality increasingly treasury-driven"}
  - {id: "F3-1", check: "F3", line: "169", classification: "AMBIGUOUS", implication: "One Nil-revenue, loss-making, unreviewed subsidiary = dormant/shell; identity undisclosed"}
  - {id: "F8-1", check: "F8", line: "243/448", classification: "NEUTRAL-FACT", implication: "Prior-year tax true-up Rs364/363 lacs booked Q4FY26"}
  - {id: "F8-2", check: "F8", line: "242", classification: "FORWARD-SIGNAL", implication: "Persistent deferred credits; ETR 24.2% below 25.17%, ~140bps DTA shield, future step-up risk"}
  - {id: "F12-1", check: "F12", line: "316/297-300", classification: "FORWARD-SIGNAL", implication: "Single-segment reporting hides device +204% vs Map +2.3% YoY mix; EBITDA margin -570bps YoY"}
  - {id: "F13-1", check: "F13", line: "53", classification: "AMBIGUOUS", implication: "WTD of Material WOS Mappls DT departed, no reason/successor disclosed"}
  - {id: "F14-1", check: "F14", line: "462-469", classification: "NEUTRAL-FACT", implication: "Standalone statement sign-off missing date line; Koga/Kogo name; cumulative drafting data point"}
  - {id: "F15-1", check: "F15", line: "128", classification: "AMBIGUOUS", implication: "No prior list -> entity additions/deletions/relationship diff unverifiable; verify Koga/Kogo and Gtropy stake at AR"}
  - {id: "BF", check: "Falsifier/BS-scope", line: "272/458", classification: "AMBIGUOUS", implication: "No balance sheet/receivables disclosed; FLAG-CASH falsifier untestable, escalate to concall; no number inferred"}
forward_signals: ["F2-1", "F2-2", "F8-2", "F12-1"]
ambiguous: ["F3-1", "F12-1", "F13-1", "F15-1", "BF"]
commitments:
  - {commitment: "Nikhil Kumar cessation as WTD of Mappls DT Private Limited (Material WOS)", implied_date: "2026-08-03", ref: "agenda item 2 line 53 / Annexure-B lines 565-569", status_word: "completed"}
  - {commitment: "Board approval of Q1 FY27 unaudited standalone + consolidated results with LRR", implied_date: "2026-08-04", ref: "agenda item 1 line 45 / Notes 2 lines 307-311, 502-506", status_word: "completed"}
gate_a3: pass
blank_checks: []
```
