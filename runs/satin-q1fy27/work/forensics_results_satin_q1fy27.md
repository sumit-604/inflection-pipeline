# A3 FORENSIC NOTES — SATIN CREDITCARE NETWORK LTD — Q1 FY27 — doctype: RESULTS

Source extract: `extract_results_satin_q1fy27.txt` (15 pp, Lakhs -> x0.01 = Rs Cr)
Ledger contract: `ledger_results_satin_q1fy27.md` (144 line items, 32 notes, 13
auditor paras, 6 entities, 1 agenda item — all read at cited lines; reconciled 100%).
Weigh-only input: `thesis_brief_notion.md` (not evidence).
NBFC-MFI; 1L (standalone) and 5L (consolidated) variants both run.

Convention reminder: values below quoted in Lakhs as filed unless "Rs ... Cr" shown
(Lakhs x0.01 = Cr).

---

## HEADLINE RECONCILIATIONS (the numbers A4 will build on)

STANDALONE (1L) — PAT `12,028.68` (Rs 120.29 Cr, ln 203 / Reg 52(4) ln 390);
Total income `67,145.46` (Rs 671.45 Cr, ln 183); PPOP = PBT `15,795.61` + impairment
`10,014.89` = `25,810.50` (Rs 258.11 Cr). Q1FY26 PPOP = `5,462.86` + `13,463.63` =
`18,926.49` (Rs 189.26 Cr) -> PPOP +36.4% YoY. Net worth `3,21,892.58` (Rs 3,218.93 Cr,
ln 389); D/E 3.15 (ln 383); GNPA 2.18% / NNPA 0.33% / PCR 84.66% / CRAR 26.74% /
LCR 134.89% (ln 403-407).

CONSOLIDATED (5L) — PAT `12,264.56` (Rs 122.65 Cr, ln 609 / Reg 52(4) ln 770);
owners `12,267.04`, NCI `(2.48)` (ln 622-623); Total income `76,474.53` (Rs 764.75 Cr,
ln 593); PPOP = PBT `16,119.67` + impairment `10,612.07` = `26,731.74` (Rs 267.32 Cr).
Net worth `2,94,361.98` (Rs 2,943.62 Cr, ln 769); D/E 3.97 (ln 763).

STANDALONE-vs-CONSOLIDATED PAT GAP (first-class metric):
| Period | S PAT | C PAT | C-S gap (L) | gap % of S PAT |
|--------|-------|-------|-------------|----------------|
| Q1FY27 | 12,028.68 | 12,264.56 | +235.88 (Rs 2.36 Cr) | +1.96% |
| Q4FY26 | 13,694.81 | 16,204.57 | +2,509.76 (Rs 25.10 Cr) | +18.33% |
| Q1FY26 | 4,260.14 | 4,509.98 | +249.84 (Rs 2.50 Cr) | +5.86% |
| FY26   | 30,208.07 | 33,220.98 | +3,012.91 (Rs 30.13 Cr) | +9.97% |
Gap collapsed -16.4pp QoQ and -3.9pp YoY -> F2 FINDING.

---

## FINDINGS TABLE

| id | F# | ledger row | line(s) | verbatim quote | classification | forward implication |
|----|----|-----------|---------|----------------|----------------|---------------------|
| FND-01 | F1 | 3.12 / 4.10.20 / 4.14.19 / 7.14.19 | 189, 339, 403-406, 782 | "Impairment of financial instruments ... 10,014.89"; "The company has not transfered any NPA loans"; "GNPA (%) 2.18%"; consol table "NOT PRESENT ... terminates at row 18" | AMBIGUOUS | GNPA 2.18% improvement is NOT reconcilable from the filing: no gross write-off line, no ECL/stage-wise movement, no Rs 36 Cr management overlay disclosed anywhere, and the consolidated Reg 52(4) carries NO sector ratios at all (no group GNPA, hence SFL GNPA trigger uncheckable). Organic-vs-laundered question stays open. |
| FND-02 | F2 | 3.22 / 6.22 | 203, 609 | S PAT "12,028.68" vs C PAT "12,264.56" | FORWARD-SIGNAL | Subsidiary net earnings contribution fell from +18.3% of standalone PAT (Q4) to +1.96% (Q1). Group profit is now almost entirely the parent MFI; SHFL/SFL contribution thin and volatile. |
| FND-03 | F6 | 4.9 / 7.12 | 275-283, 741-749 | "issuance and allotment of upto 38,50,000 fully convertible warrants at an issue price of Rs 260.00 each ... Rs 10,010.00 Lakhs, to Trishashna Holdings & Investments Private Limited ... 'Promoter & Promoter Group'" | FORWARD-SIGNAL | Rs 100.1 Cr promoter capital injection + 38.5L-share dilution overhang; shareholder-approved 04-Jul, in-principle exchange approval 27-Jul; allotment/conversion pending (18-month window). |
| FND-04 | F7 | 3.4 / 3.11 / 6.4 / 6.11 | 178, 188, 588, 597 | fair value changes "(5,711.19)"; FX effects "(6,242.84)" | AMBIGUOUS | Rs 57.11 Cr FV loss above the line offset by a Rs 62.43 Cr FX credit in finance costs (Q1 gain vs Q4 +9,263 charge, Q1FY26 +2,818 charge). No hedge-accounting/derivative-policy note added despite the swing -> reversal risk next quarter; PBT quality question. |
| FND-05 | F8 | 6.19 / 3.20 | 606, 200 | consol "Tax adjustments related to earlier years ... 6.82"; deferred tax "(472.20)" | AMBIGUOUS | Non-zero prior-year tax adjustment (rule: any non-zero = FINDING). Standalone ETR 23.85% (23.85 vs statutory 25.17) held below statutory by a deferred-tax credit shield ~132 bps; persistent Q1 deferred credits (Q1FY26 also credit) flag future ETR step-up as DTA unwinds. |
| FND-06 | F10 | 3.31/3.32 / 6.37/6.38 / 3.29 | 222-223, 635-636, 216 | Basic "10.94" / Diluted "10.94"; paid-up "11,011.32" (was 11,004.32) | FORWARD-SIGNAL | Zero basic-diluted spread despite 38.5L warrants approved + live ESOP pool -> warrants excluded (allotment pending) so dilution lands in later quarters. Paid-up rose Rs 7.00 L = 70,000 ESOP shares (traceable, benign). |
| FND-07 | F11 | 4.14.7 / 7.14.7 | 389, 769 | S net worth "3,21,892.58" vs C net worth "2,94,361.98" | AMBIGUOUS | Consolidated net worth is Rs 275.31 Cr (8.55%) BELOW standalone while consolidated PAT is higher. Subsidiaries in aggregate carry net accumulated losses / their net assets are below the parent's investment carrying value. Reconciling candidates: subsidiary accumulated losses, investment-vs-equity elimination, NCI, any goodwill. |
| FND-08 | F12 | 7.13 / 6.30 / 7.9 | 751-756, 623, 729-733 | "Satin Technologies Limited, Satin Growth Altematives Limited and QTrino Labs Limited currently do not have any reportable segment"; NCI "(2.48)" | FORWARD-SIGNAL | Three build-stage subs (no revenue segment) fed continuous parent equity: Rs 1,000L STL + Rs 5,000L SFL in-quarter, Rs 1,200L SGAL subsequent, Rs 636L STL->QTrino. Negative NCI = QTrino minorities absorbing losses. Equity-funded pre-commissioning build; parent is the funding source (warrant proceeds a likely feed). |
| FND-09 | F14 | 5.1 / 7.9 | 460, 731-732 | consol LRR title "Regulation 52 read with Regulation 53"; "increased from 50.84% to 70.67% ... STL holds 67.88%" | NEUTRAL-FACT | Consol LRR title cites Reg 53 where every other reference says Reg 63; STL stake quoted two ways (70.67% fully diluted vs 67.88% actual) in one note. Individually immaterial, cumulatively a drafting/governance data point. |
| FND-10 | F15 | 7.2.5 / 7.10 / 7.9 | 669-670, 735-736, 729-733 | "QTrino Labs Limited (formerly known as QTrino Labs Private Limited)"; "name ... changed ... vide RoC order dated luly 15, 2026"; STL "50.84% to 70.67%" | FORWARD-SIGNAL | Entity-list change: step-down sub renamed (private -> public, RoC 15-Jul, subsequent event) AND STL raised its QTrino stake 50.84% -> 67.88%. Deepening commitment to the tech step-down; watch for further capital calls / eventual monetisation. |

---

## CHECKLIST SCORECARD (all 17)

| F# | Status | Basis (one line) |
|----|--------|------------------|
| F1 | FINDING | ZERO_STANDING rows benign (N/A ratios, interim-blank equity, nil DA/NPA disclosures), BUT the results template carries no ECL-walk / gross write-off / overlay line, so GNPA improvement + Rs 36 Cr overlay are not reconcilable (FND-01). |
| F2 | FINDING | S-vs-C PAT gap swung -16.4pp QoQ / -3.9pp YoY (>5pp) — subsidiary contribution collapsed (FND-02). |
| F3 | PASS | Not shells: consol employee benefits 18,769.10 > standalone 15,716.41, interest income 71,396.21 > 63,202.99, depreciation 793.51 > 642.64 — SHFL/SFL operate; STL/SGAL/QTrino build-stage (housed in FND-08, not F3). No going-concern EoM on any entity. |
| F4 | PASS | Unaudited subs PAT Rs 606.58 L = 4.95% of consol PAT (<10%); revenue Rs 10,382.78 L = 13.6% and TCI Rs 1,157.83 L = 9.63% noted for A4 awareness; conclusion "not modified" (ln 533-545). No prior extract for trend. |
| F5 | PASS | No Emphasis of Matter / Going Concern paragraph in either LRR (ln 72, 204); nothing to verbatim-diff; unmodified conclusions both. |
| F6 | FINDING | Forward-commitment mining: warrant "board ... had approved", "obtained In-Principle approval(s)", subsequent-event investments (FND-03; see Commitment Register). |
| F7 | FINDING | No hedge/derivative-policy note added despite Rs 62.43 Cr FX finance-cost credit and Rs 57.11 Cr FV loss (FND-04). |
| F8 | FINDING | Consol prior-year tax adjustment 6.82 non-zero; ETR 23.85% < 25.17% on deferred-tax credit shield ~132 bps (FND-05). |
| F9 | PASS | Standalone non-reclassified OCI (916.33) < full FY26 (2,765.03); no single-quarter OCI swing exceeds prior full year on either statement; standalone actuarial losses persistent but sub-threshold. |
| F10 | FINDING | Zero basic-diluted EPS spread despite 38.5L pending warrants + ESOP pool; paid-up +7.00L traces cleanly to 70,000 ESOP shares (FND-06). |
| F11 | FINDING | Consol net worth Rs 275.31 Cr (8.55%) below standalone (FND-07); standalone tie-out (paid-up 11,011.32 + FY26 other equity 3,01,878.50 vs NW 3,21,892.58) within 5% -> ok. |
| F12 | FINDING | Single-segment NBFC (formal segment table N.A.) but three no-revenue subs on continuous equity drip; negative NCI confirms QTrino losses (FND-08). |
| F13 | PASS | Board Outcome letter carries ONE agenda item — approval of results (ln 37-39, 82-min meeting ln 47). No AR/Board's-Report/MD&A approval, no AGM notice/record date, no dividend, no director appointment/term, no auditor change, no ESOP-grant or capital-raise resolution as a separate item. Warrant capital raise is a prior (04-Jun) board action disclosed in notes, tracked under FND-03/06. |
| F14 | FINDING | Consol LRR title "Regulation 53" vs 63; STL stake stated two ways in one note (FND-09). |
| F15 | FINDING | QTrino rename + STL stake 50.84% -> 67.88% (FND-10). No prior extract for additions/deletions diff; list is 6 entities (ln 512-520). |
| F16 | N.A. | Results filing, not a presentation deck. |
| F17 | N.A. | Results filing, no concall transcript in scope. |

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note / ref | status word |
|------------|--------------|------------|-------------|
| Preferential allotment of 38,50,000 warrants @ Rs 260 (Rs 100.1 Cr) to Trishashna Holdings (Promoter Group) | in-principle 27-Jul-2026; allotment pending; conversion within 18 months | Note 9 std (ln 275-283) / Note 12 consol (ln 741-749) | underway (approved + in-principle, not allotted) |
| Investment Rs 1,200 L in Satin Growth Alternatives Ltd (rights, 1,20,00,000 sh @ Rs 10) | subsequent to 30-Jun-2026 | Note 7 std (ln 267-269) / Note 8 consol (ln 725-727) | completed |
| STL raised balance Rs 636 L in QTrino; 27,180 partly-paid -> fully-paid; stake 50.84%->67.88% | 25-May-2026 / as at 30-Jun-2026 | Note 9 consol (ln 729-733) | completed |
| QTrino Labs Private Ltd renamed QTrino Labs Limited | RoC order 15-Jul-2026 | Note 10 consol (ln 735-736) | completed |
| ESOP exercise — 70,000 equity shares (SEWT -> employee demat) | in-quarter (Q1FY27) | Note 8 std (ln 271-273) / Note 11 consol (ln 737-739) | completed |

---

## A4 HAND-OFF — MANAGEMENT QUESTIONS TO GENERATE (FORWARD-SIGNAL + AMBIGUOUS)
- FND-01: Provide the GNPA/ECL movement walk (opening, additions, write-offs, ARC/DA of NPAs, closing) and disclose the Rs 36 Cr management overlay treatment; publish group-level and SFL GNPA (absent from consol Reg 52(4)).
- FND-02: Why did subsidiary PAT contribution collapse from Rs 25.1 Cr (Q4) to Rs 2.36 Cr (Q1)? SHFL vs SFL split.
- FND-03 / FND-06: Warrant allotment/conversion timeline, use of the Rs 100.1 Cr, and pro-forma diluted share count / EPS.
- FND-04: FX/FV hedge policy — is the Q1 FX credit hedged or open? Reversal exposure on an adverse INR move.
- FND-05: Deferred-tax credit sustainability and expected normalized ETR.
- FND-07: Reconcile the Rs 275 Cr consolidated-below-standalone net-worth gap (subsidiary accumulated losses / eliminations / NCI).
- FND-08: Capex/funding plan and commissioning timeline for STL, SGAL, QTrino; expected external funding vs further parent equity.
- FND-10: Strategic intent and monetisation path for the QTrino step-down.

---

```yaml
stage: A3-forensics
company: "SATIN"
quarter: "q1fy27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/satin-q1fy27/work/forensics_results_satin_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: FINDING
  F3: PASS
  F4: PASS
  F5: PASS
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: PASS
  F10: FINDING
  F11: FINDING
  F12: FINDING
  F13: PASS
  F14: FINDING
  F15: FINDING
  F16: N.A.
  F17: N.A.
findings:
  - {id: "FND-01", check: "F1", line: "189, 339, 403-406, 782", classification: "AMBIGUOUS", implication: "GNPA improvement + Rs 36 Cr overlay not reconcilable; no ECL walk/write-off line; consol Reg 52(4) has no sector ratios (no group/SFL GNPA)"}
  - {id: "FND-02", check: "F2", line: "203, 609", classification: "FORWARD-SIGNAL", implication: "S-vs-C PAT gap collapsed 18.3%->1.96% QoQ; subsidiary earnings thin/volatile"}
  - {id: "FND-03", check: "F6", line: "275-283, 741-749", classification: "FORWARD-SIGNAL", implication: "Rs 100.1 Cr promoter warrant (Trishashna) + 38.5L dilution overhang, allotment/conversion pending"}
  - {id: "FND-04", check: "F7", line: "178, 188", classification: "AMBIGUOUS", implication: "Rs 62.43 Cr FX credit offsets Rs 57.11 Cr FV loss; no hedge note; reversal/PBT-quality risk"}
  - {id: "FND-05", check: "F8", line: "606, 200", classification: "AMBIGUOUS", implication: "Non-zero prior-year tax adj 6.82; ETR 23.85% below 25.17% on deferred-tax credit ~132bps; future ETR step-up"}
  - {id: "FND-06", check: "F10", line: "222-223, 635-636, 216", classification: "FORWARD-SIGNAL", implication: "Zero diluted spread despite 38.5L warrants + ESOP; dilution lands later quarters; paid-up +7L ESOP traceable"}
  - {id: "FND-07", check: "F11", line: "389, 769", classification: "AMBIGUOUS", implication: "Consol net worth Rs 275.31 Cr (8.55%) below standalone; subsidiary accumulated losses/elimination unreconciled"}
  - {id: "FND-08", check: "F12", line: "751-756, 623, 729-733", classification: "FORWARD-SIGNAL", implication: "Build-stage subs (STL/SGAL/QTrino) on continuous parent equity drip; negative NCI = QTrino losses; future funding need"}
  - {id: "FND-09", check: "F14", line: "460, 731-732", classification: "NEUTRAL-FACT", implication: "Consol LRR title Reg 53 vs 63; STL stake stated 70.67% vs 67.88% in one note; drafting/governance data point"}
  - {id: "FND-10", check: "F15", line: "669-670, 735-736, 729-733", classification: "FORWARD-SIGNAL", implication: "QTrino rename (RoC 15-Jul) + STL stake 50.84%->67.88%; deepening tech step-down commitment"}
forward_signals: ["FND-02", "FND-03", "FND-06", "FND-08", "FND-10"]
ambiguous: ["FND-01", "FND-04", "FND-05", "FND-07"]
commitments:
  - {commitment: "38,50,000 warrants @ Rs 260 (Rs 100.1 Cr) to Trishashna Holdings, Promoter Group", implied_date: "in-principle 2026-07-27; allotment pending; conversion within 18 months", ref: "Note 9 std ln 275-283 / Note 12 consol ln 741-749", status_word: "underway"}
  - {commitment: "Investment Rs 1,200 L in Satin Growth Alternatives Ltd (rights)", implied_date: "subsequent to 2026-06-30", ref: "Note 7 std ln 267-269 / Note 8 consol ln 725-727", status_word: "completed"}
  - {commitment: "STL raised QTrino stake to 67.88% (Rs 636 L; 27,180 partly->fully paid)", implied_date: "2026-05-25 / as at 2026-06-30", ref: "Note 9 consol ln 729-733", status_word: "completed"}
  - {commitment: "QTrino Labs Private Ltd renamed QTrino Labs Limited", implied_date: "RoC order 2026-07-15", ref: "Note 10 consol ln 735-736", status_word: "completed"}
  - {commitment: "ESOP exercise 70,000 equity shares", implied_date: "in-quarter Q1FY27", ref: "Note 8 std ln 271-273 / Note 11 consol ln 737-739", status_word: "completed"}
gate_a3: pass
blank_checks: []
```
