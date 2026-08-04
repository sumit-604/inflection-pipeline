# A3 FORENSIC NOTES — Uniparts India Ltd (UNIPARTS), Q1 FY2026-27 (results)

Doctype: **results** (F1-F15 apply; F16/F17 = N.A. per doctype rule).
Source extract: `/home/user/inflection-pipeline/runs/uniparts-q1fy27/work/extract_results_uniparts_q1fy27.txt`
A2 ledger: `/home/user/inflection-pipeline/runs/uniparts-q1fy27/work/ledger_results_uniparts_q1fy27.md`
Ledger reconciliation: 100% — every ledger row (notes 10, line_items 99, zero_standing 13, agenda 2, auditor_paras 15, entities 5) read verbatim at its cited line before judging.
Prior-quarter baseline: **NONE** (first quarterly run). Checks that require a QoQ diff (F5 EoM, F15 entity list) are marked against that absence; the 5-entity list and all EoM/Other-Matter paragraphs are recorded as the baseline for the next quarter.
Unit convention: Rs Millions as filed (A1 header; x0.1 to Crores). All figures below reproduced verbatim from the extract.

A2 pre-flagged two items for verbatim attention — both independently verified below: (1) standalone "Total comprehensive income" blank in 2 of 4 periods despite populated components (line 550) — confirmed and arithmetic-tested under F1/F14; (2) OTHER_AUDITOR_RELIANCE on 3 of 5 consolidated entities (~Rs 2,262.40 mn revenue) — confirmed and quantified under F4.

---

## FINDINGS TABLE

| id | check | ledger row ref | line/turn/slide | verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-01 | F1 | 275 / 528 Impact of Labour Code (ZERO_STANDING) | 275 (consol), 528 (std) | "Impact of Labour Code" … "(34.19)" consol / "(28.05)" std, FY26 only; blank all three interim columns | AMBIGUOUS | Standing exceptional-items line pre-provisioned for India's four Labour Codes; the FY26 one-off hit may recur as Codes are notified — ask whether further gratuity/leave provisioning is expected. |
| A3-02 | F1 / F14 | 550 Total comprehensive income std (ZERO_STANDING; INTERNAL_INCONSISTENCY) | 550 | "Total comprehensiue income for the period   241.48   [blank]   [blank]   1,449.77" | NEUTRAL-FACT | Arithmetic test: Q4FY26 should read 413.29 + (18.83) = 394.46; Q1FY26 should read 146.26 + (15.67) = 130.59. The two blanks are omissions, not zeros — a completeness/drafting gap (components populated, total left blank). Consolidated TCI ties in all 4 periods, so the defect is standalone-only. |
| A3-03 | F1 / F14 | 415-417 Net profit margin consol; 663/667 std margins (ZERO_STANDING) | 415 (consol, blank all 4), 411 (consol op margin Q4 blank), 640 (std LT-debt/WC blank all 4), 667 (std net margin Q4 & Q1FY26 blank) | "m) Net profit margin(%)  [Net profit after tax I Reuenue from operations]" — formula printed, no values | CONFIRMATORY-NEGATIVE | Multiple Reg-33-mandated ratio cells left blank though trivially computable (consol NP margin = 566.09/3,473.76 = 16.3%). Cumulative disclosure sloppiness; low-materiality individually, a governance data point in aggregate. |
| A3-04 | F2 | 259/512 Revenue, 283/536 Profit for the period (S vs C) | 259, 283, 512, 536 | Consol PAT 566.09 vs Standalone 230.01 (Q1FY27) | FORWARD-SIGNAL | Subsidiary PAT contribution to consol swings 5.1% (FY26 FY) → 59.4% (Q1FY27) → 57.6% (Q1FY26) → 19.2% (Q4FY26); swings >>5pp of standalone PAT. The apparent "gap" is distorted by intra-group dividends (see A3-08): standalone FY26 Other Income 1,033.03 upstreamed from subs masks true operating split. Group profit quality rides on foreign subsidiaries. |
| A3-05 | F4 | Auditor para 6 (Other Matter) | 168-176 | "We did not review … two subsidiaries and one step down subsidiary … total revenues of Rs. 2,262.40 million, total net profit … Rs. 260.86 million … for the quarter" | FORWARD-SIGNAL | Unreviewed net profit 260.86 / consol PAT 566.09 = **46.1% of group PAT** and 2,262.40 / 3,473.76 = **65.1% of consol revenue from operations** rest on component auditors (KNAV CPA LLP; FJS Audit GmbH), not the principal auditor. Far above the 10%-of-PAT threshold. No prior baseline to trend — set baseline now. Of the 336.08 subsidiary PAT, 260.86 (78%) is the unreviewed foreign trio. |
| A3-06 | F8 | 281/534 Deferred tax; 280/533 Earlier years; ETR (all periods) | 279-282 (consol), 532-535 (std) | Std deferred tax "(1.29) (4.93) (1.69) (22.34)" — persistent credits; "Earlier years … 0.13 … (0.37)" consol; "(0.03)" std | FORWARD-SIGNAL | Standalone ETR 13.05% (Q4FY26) / 13.33% (FY26) sits ~12pp below statutory 25.17% — driven by exempt intra-group dividend income (Other Income 259.15 Q4 / 1,033.03 FY26). Standalone deferred-tax is a persistent CREDIT every period (FY26 shield 22.34/1,733.38 = 1.29pp) — future ETR step-up risk as the shield unwinds. Non-zero "earlier years" tax adjustments present in comparatives = FINDING per rule. |
| A3-07 | F9 | 287/540 Re-measurement of defined benefit plans (OCI) | 287 (consol), 540 (std) | Consol "(26.84) 3.80 (12.61) (3.21)"; Std "(23.52) 2.94 (11.00) (3.59)" | AMBIGUOUS | Single-quarter actuarial OCI loss exceeds the FULL prior year in both books (consol (26.84) vs FY26 (3.21) = 8.4x; std (23.52) vs (3.59) = 6.6x). Signals a discount-rate / plan-assumption change. Verify assumptions at the Annual Report; generate a management question. |
| A3-08 | F2 / F8 | 513/523 Standalone Other Income | 513 | Standalone "Other Income  84.20  259.15  58.00  1,033.03" vs Consol other income 176.05 FY26 | AMBIGUOUS | Standalone Other Income spikes to 259.15 (Q4) and 1,033.03 (FY26) but consolidated other income is only 176.05 FY26 — the difference is intra-group dividend upstreamed from subsidiaries (eliminated on consolidation). Confirms parent is a dividend conduit; standalone earnings and ETR are not clean read-throughs of operations. |
| A3-09 | F10 | 315/568 Paid-up capital; 318-319/572-573 EPS | 315, 318-319 | Paid-up "451.43 451.43 451.34 451.43"; Basic/Diluted EPS 12.54*/12.50* (Q1FY27) vs 7.64/7.64 (Q1FY26) | FORWARD-SIGNAL | Paid-up capital rose 451.34 → 451.43 mn (+0.09 mn ≈ 9,000 shares, face Rs 10) between Q1FY26 and Q4FY26 — traces to a corporate action (likely ESOP allotment). Basic-vs-diluted spread widened from 0.00 (Q1FY26) to 0.04 (Q1FY27) = live dilutive instruments. Flag spread for A4 to cross-check ESOP/warrant register (no Notion thesis available this run). |
| A3-10 | F6 / F13 | Note 4 (both) + cover agenda item 2 | 39-43, 334, 588 | "approved a 1st interim diuidend of Rs 9.00/- per equity share … aggregating to Rs 406.45 millions … Record Date … 12th August 2026 … shall be paid … within 30 days" | NEUTRAL-FACT | Dated cash commitment: Rs 406.45 mn dividend, record date 12 Aug 2026, payable by ~3 Sep 2026. Board outcome beyond results is dividend-only — no AR/MD&A approval (no Role 6 AR event to schedule), no AGM notice, no director re-appointment, no capital-raising enabling resolution. |
| A3-11 | F14 | Standalone Notes block header | 575 | "Notes to the Standalone **Audited** Financial Results for the Quarter Ended June 30, 2026" | CONFIRMATORY-NEGATIVE | Header says "Audited" while the results are UNAUDITED (limited review only — auditor "do not express an audit opinion", line 463) and the note body (576) itself says "Standalone unaudited financial results." Note-text vs auditor-letter inconsistency; immaterial alone, adds to the drafting-control data point with A3-02/A3-03. |
| A3-12 | F13 | Board Outcome context rows | 45, 601-603 | Meeting "commenced at 05.00 P.M. … concluded at 05:25 P.M." (25 min); standalone signed "Tanushree Bagrodia (Whole-time Director) (DIN: 06965596)" | NEUTRAL-FACT | 25-minute board meeting to approve results + dividend (informational). Signatory Tanushree Bagrodia WTD DIN 06965596 — term dates / re-appointment window NOT FOUND in this extract; establish as director-tenure baseline for the catalyst-window test next quarter. Consolidated sign-off block has no machine-readable signatory name (line 342-348). |

---

## CHECKLIST SCORECARD (all 17)

| Check | Status | One-line basis |
|---|---|---|
| F1 ZERO-VALUE STANDING ITEMS | **FINDING** | 13 ZERO_STANDING rows read; Labour-Code exceptional line (A3-01), standalone TCI blanks that fail arithmetic (A3-02), and blank mandated ratio cells (A3-03). Reserve blanks in interim columns are format-normal (year-end only). |
| F2 STANDALONE vs CONSOLIDATED | **FINDING** | Subsidiary PAT contribution swings 5.1%→59.4% of consol across periods, >>5pp of standalone PAT; distorted by intra-group dividends (A3-04, A3-08). |
| F3 SHELL-ENTITY DETECTION | PASS | Cost lines differ materially S vs C (Cost of materials 1,170.58 vs 799.62; Employee 716.16 vs 388.20) — subsidiaries have real operations; no shells; no Going Concern para. |
| F4 UNAUDITED CONTRIBUTION RATIO | **FINDING** | 46.1% of consol PAT / 65.1% of consol revenue unreviewed by principal auditor — far above 10% threshold (A3-05). No prior baseline to trend. |
| F5 GOING CONCERN / EoM SCOPE | PASS | No Going Concern paragraph in either report. Other-Matter paras (component-auditor reliance; prior-period balancing figures) present; no prior quarter to diff — recorded as baseline. |
| F6 FORWARD-COMMITMENT MINING | **FINDING** | One dated commitment: interim dividend "shall be paid … within 30 days", record date 12 Aug 2026 (A3-10). Note 5 reclassification wording is standard boilerplate, not a commitment. |
| F7 HEDGE PHRASE MINING | PASS | Notes carry only standard "regrouped/reclassified wherever necessary" boilerplate (Note 5); no newly added hedge on revenue lumpiness or customer concentration. No lexicon hits. |
| F8 TAX FORENSICS | **FINDING** | Standalone ETR 13% (Q4/FY26) vs statutory 25.17% from exempt dividend income; persistent standalone deferred-tax credits (step-up risk); non-zero earlier-years adjustments in comparatives (A3-06). |
| F9 OCI FORENSICS | **FINDING** | Single-quarter actuarial OCI loss exceeds full prior year in both books (8.4x consol, 6.6x std) — assumption change; verify at AR (A3-07). |
| F10 SHARE COUNT AND DILUTION | **FINDING** | Paid-up +0.09 mn (451.34→451.43) = corporate action; basic-vs-diluted spread widened 0.00→0.04 = live dilutive instruments (A3-09). |
| F11 RESERVES AND NET WORTH TIE-OUT | PASS | Ties exactly: consol 451.43 + 8,252.96 = 8,704.39 = ratio-d net worth; standalone 451.43 + 5,054.65 = 5,506.08 = ratio-d net worth. Gap 0%. |
| F12 SEGMENT FORENSICS | **N.A.** | Note 3 (both): CODM determined "no reportable segment for the Company" (SINGLE_SEGMENT); no segment asset/liability tables exist to trend. Geographic-concentration opacity is carried instead under F2/F4. |
| F13 BOARD OUTCOME BEYOND RESULTS | **FINDING** | Dividend + record date declared (A3-10); notable absences (no AR/AGM/director re-appointment/enabling resolution); 25-min meeting; director term-date baseline NOT FOUND (A3-12). |
| F14 NOTE DRAFTING INCONSISTENCIES | **FINDING** | Standalone Notes header reads "Audited" on an unaudited limited-review filing (A3-11); plus TCI blanks (A3-02) and blank mandated ratios (A3-03) — cumulative drafting-control data point. |
| F15 ENTITY LIST DIFFS | **N.A.** | First quarterly run, NO_PRIOR_BASELINE — diff not evaluable. 5-entity list (Gripwel Fasteners, Gripwel Conag, Uniparts USA, Uniparts India GmbH, Uniparts Olsen step-down) recorded as next-quarter baseline. |
| F16 DROPPED/REFRAMED DISCLOSURES | **N.A.** | Presentation-specific; doctype = results. |
| F17 CONCALL SILENCE AUDIT | **N.A.** | Concall-specific; no transcript, no Notion monitoring checklist (new company, no prior thesis). No thesis-level monitorables exist yet. |

Blank checks: none. GATE A3 = pass.

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/agenda ref | status word |
|---|---|---|---|
| First interim dividend FY27, Rs 9.00/share (Rs 406.45 mn aggregate) | Record date 12 Aug 2026; payable within 30 days of declaration (~3 Sep 2026) | Cover agenda item 2 (lines 39-43); Consol Note 4 (line 334); Std Note 4 (line 588) | approved (board 4 Aug 2026) — payment pending |

No other dated or dateable management commitments in the notes (no "expected to be", "underway", "in the process of", "proposes to", "commenc" hits). Status-change tracking will begin next quarter against this single register row.

---

## NOTES FOR A4

Convert to management questions: **A3-04, A3-05, A3-06, A3-09** (FORWARD-SIGNAL) and **A3-01, A3-07, A3-08** (AMBIGUOUS). Core themes: (1) ~46% of group PAT / ~65% of group revenue rides on three foreign subsidiaries reviewed only by component auditors, and majority of group profit is a foreign-sub, single-segment black box; (2) standalone ETR and earnings distorted by exempt intra-group dividends with a deferred-tax-credit unwind ahead; (3) actuarial assumption change (verify AR); (4) live ESOP dilution. Baselines to carry forward: 5-entity consolidation list, all Other-Matter paragraphs, director tenure (Tanushree Bagrodia DIN 06965596), and the commitment register.

```yaml
stage: A3-forensics
company: "UNIPARTS"
quarter: "Q1 FY2026-27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/uniparts-q1fy27/work/forensics_results_uniparts_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: FINDING
  F3: PASS
  F4: FINDING
  F5: PASS
  F6: FINDING
  F7: PASS
  F8: FINDING
  F9: FINDING
  F10: FINDING
  F11: PASS
  F12: N.A.
  F13: FINDING
  F14: FINDING
  F15: N.A.
  F16: N.A.
  F17: N.A.
findings:
  - {id: "A3-01", check: "F1", line: "275/528", classification: "AMBIGUOUS", implication: "Standing Labour-Code exceptional line; FY26 one-off may recur as Codes notified"}
  - {id: "A3-02", check: "F1/F14", line: "550", classification: "NEUTRAL-FACT", implication: "Standalone TCI blank in 2 of 4 periods; arithmetic shows omission (394.46, 130.59), not zero"}
  - {id: "A3-03", check: "F1/F14", line: "415/640/667", classification: "CONFIRMATORY-NEGATIVE", implication: "Reg-33 mandated ratio cells left blank though computable; cumulative disclosure sloppiness"}
  - {id: "A3-04", check: "F2", line: "259/283/512/536", classification: "FORWARD-SIGNAL", implication: "Subsidiary PAT contribution swings 5.1%-59.4% of consol; group profit rides on foreign subs"}
  - {id: "A3-05", check: "F4", line: "168-176", classification: "FORWARD-SIGNAL", implication: "46.1% of consol PAT / 65.1% of revenue unreviewed by principal auditor"}
  - {id: "A3-06", check: "F8", line: "279-282/532-535", classification: "FORWARD-SIGNAL", implication: "Standalone ETR ~13% via exempt dividends; persistent deferred-tax credit = future ETR step-up"}
  - {id: "A3-07", check: "F9", line: "287/540", classification: "AMBIGUOUS", implication: "Single-quarter actuarial OCI loss exceeds full prior year (8.4x/6.6x); assumption change, verify AR"}
  - {id: "A3-08", check: "F2/F8", line: "513", classification: "AMBIGUOUS", implication: "Standalone Other Income = intra-group dividend upstream; parent is a dividend conduit"}
  - {id: "A3-09", check: "F10", line: "315/318-319", classification: "FORWARD-SIGNAL", implication: "Paid-up +0.09mn corporate action; basic/diluted spread widened 0.00->0.04 = live dilution"}
  - {id: "A3-10", check: "F6/F13", line: "39-43/334/588", classification: "NEUTRAL-FACT", implication: "Rs 406.45mn dividend, record date 12 Aug 2026, payable ~3 Sep 2026"}
  - {id: "A3-11", check: "F14", line: "575", classification: "CONFIRMATORY-NEGATIVE", implication: "Standalone Notes header says 'Audited' on an unaudited limited-review filing"}
  - {id: "A3-12", check: "F13", line: "45/601-603", classification: "NEUTRAL-FACT", implication: "25-min meeting; director term dates NOT FOUND (Tanushree Bagrodia DIN 06965596) - set baseline"}
forward_signals: ["A3-04", "A3-05", "A3-06", "A3-09"]
ambiguous: ["A3-01", "A3-07", "A3-08"]
commitments:
  - {commitment: "First interim dividend FY27 Rs 9.00/share (Rs 406.45mn aggregate)", implied_date: "2026-08-12 record date; payable by ~2026-09-03", ref: "cover item 2 L39-43 / Note 4 L334 / L588", status_word: "approved"}
gate_a3: pass
blank_checks: []
```
