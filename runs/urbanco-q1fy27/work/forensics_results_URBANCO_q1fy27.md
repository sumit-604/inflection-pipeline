# A3 FORENSIC NOTES — URBANCO Q1 FY27 — DOCTYPE: results

Company: Urban Company Limited (URBANCO) | Quarter: Q1 FY27 (quarter ended June 30, 2026)
Source A1 extract: extract_results_URBANCO_q1fy27.txt (582 lines) | A2 ledger reconciled: 100% (88 line items + 16 notes + 9 zero-standing + 14 auditor paras + 10 entities + 1 agenda item + 3 signature blocks all read at cited lines)
Prior-quarter extract: NONE (first quarterly run) — F5/F15 cross-quarter verbatim diffs not possible; intra-filing evidence used and flagged.
Doctype scope: F1-F15 apply; F16 (presentation) and F17 (concall) are N.A.
Bias: conservative; uncertain-direction findings lean bear and generate an A4 question.

---

## FINDINGS TABLE

| id | check | ledger row ref | line | verbatim quote | classification | forward implication |
|----|-------|----------------|------|----------------|----------------|---------------------|
| N1 | F1 | Sec2 line 260 (TEMPLATE_LINE_ACTIVATED); Sec2 line 264 (ZERO_STANDING) | 260, 264 | "Exceptional items (refer note 8) ... 5.27" and "Current tax ... - (0.21) - -" | NEUTRAL-FACT | Exceptional-items template line fired once for the Saudi step-down subsidiary FCTR reclass (Rs 5.27cr charge, widened PBT from -78.48 to -83.75). "Current tax" is Nil in every period except a Rs 0.21cr Q4 balancing entry — confirms no cash-tax base while loss-making; not a forward driver but baselines the template for next quarter. |
| N2 | F2 | Sec2 line 268 vs Sec4 line 521 | 268, 521 | consol "Profit/ (loss) for the period/ year (7-8) ... (92.12)" vs standalone "(84.28)" | AMBIGUOUS | S-vs-C PAT gap = consol worse by 7.84 (Q1FY27) vs 18.07 (Q1FY26); the swing (10.23) exceeds 5% of standalone PAT (|84.28|). Standalone itself flipped from +25.01 profit (Q1FY26) to -84.28 loss (Q1FY27) while consol went 6.94 to -92.12. Need mgmt to decompose: how much of the standalone deterioration is InstaHelp/SBP vs core. Question for A4. |
| N4 | F4 | Sec7 auditor para 8 (line 153); Annexure I entities 9/10 | 153-159, 215, 218 | "The Statement includes the unaudited financial results of one trust which has not been reviewed ... Rs. Nil ... not material to the Group" | FORWARD-SIGNAL | Unreviewed contribution = Rs Nil = 0% of consol PAT (BELOW 10% threshold), so magnitude passes — BUT the entity is UNNAMED while two trusts are listed (ESOP Trust in-scope per standalone para 1, leaving Partner Welfare Trust by elimination). With Labour Codes / Social Security Central Rules in force 8-May-2026 (aggregator contribution 1-2% of revenue), a Partner Welfare Trust currently at Nil could become the conduit for those flows and turn material next year. Name-and-track. |
| N5 | F5 | Sec7 paras 5,7,8 / note 5 (line 361) | 128-132, 150-159, 361 | "The Financial Results for the quarter ended June 30, 2025, were neither subject to limited review nor audit" | CONFIRMATORY-NEGATIVE | No going-concern EoM (good). But of four presented periods, only Q1FY27 carries a BS R & Co LLP limited review; Q1FY26 has ZERO assurance (management due-diligence only), Q4FY26 is a balancing figure (9M reviewed by predecessor, not audited), FY26 was audited by predecessor PwC. First BSR review; comparative base rests entirely on predecessor/unassured figures. No prior-quarter paragraph to verbatim-diff — this run is the baseline for next quarter's EoM-scope tracking. |
| N8 | F8 | Sec2 lines 261,264,265,268 | 261, 265, 268 | "Deferred tax ... 8.37 61.51 (1.30) 60.21" against PBT "(83.75) (99.86) 5.64 (174.60)" | FORWARD-SIGNAL | Persistent deferred-tax CHARGES booked ON pre-tax LOSSES (8.37 on -83.75 Q1FY27; 61.51 on -99.86 Q4FY26; 60.21 on -174.60 FY26). A loss-maker recognizing DTA would show a deferred-tax CREDIT; a charge means DTA is being derecognized / not recognized on carryforward losses — i.e. management/auditor are not confident enough in near-term taxable profit to book the shield. Directly bears on the FY28 consol adj-EBITDA breakeven thesis. Q4FY26's 61.51 charge is a step-change worth an A4 question (DTA remeasurement/write-down?). No "earlier-year tax adjustment" line present (that sub-trigger clean). |
| N10 | F10 | Sec2 line 281-282 + note 7 (line 367); EPS lines 287-288 | 281, 367, 287-288 | "the 'ESOP Trust' ... has alloted 1,03,59,538 equity shares of ~ 1/- each" ; Basic "(0.60)" = Diluted "(0.60)" | FORWARD-SIGNAL | Paid-up capital rose 146.22 to 147.26 (+Rs 1.04cr = 1.036cr shares), tracing cleanly to the ESOP-2015 exercise (note 7). Basic EPS = Diluted EPS in every period only because losses render options anti-dilutive — this masks live ESOP overhang. Once profitable, diluted EPS will diverge; share count is already creeping via exercises (1.036cr this quarter alone). Flag ESOP pool size / overhang % for A4. |
| N12 | F12 | Sec3 lines 339, 346, 347 | 339, 346 | "InstaHelp ... 11.22 8.94 0.22 17.38" (revenue) and "InstaHelp ... (131.58) (118.73' (9.24) (231.79'" (result) | FORWARD-SIGNAL | InstaHelp segment loss (-131.58) alone EXCEEDS the entire consolidated loss (-92.12) and is accelerating (-9.24 to -118.73 to -131.58) on revenue of just 11.22 (losing ~12x revenue). Core India consumer services (ex-InstaHelp) result improved 40.30 to 82.02 on revenue 271.61 to 356.42 (+31% YoY, clears the >=22% inflection test). International turned positive (+3.16). The group's loss is a single-segment (InstaHelp) story; FY28 breakeven hinges on InstaHelp burn trajectory. NOTE: segment ASSETS/LIABILITIES are NOT disclosed in this interim filing, so the equity-funded-build / capex-proxy test could not be run. |
| N13 | F13 | Sec9 blocks 2 & 3; Sec6 agenda (line 40) | 40, 386-387, 575-576 | board "concluded at 15:25 p.m." vs MD/CEO sign "Date:2026.07.31 15:23:46" (consol) and "15:22:53" (standalone) | AMBIGUOUS | Both results statements are digitally signed by the Chairperson/MD/CEO 1-2 minutes BEFORE the stated board-meeting conclusion time (15:25). Either the 15:25 conclusion is a nominal/rounded time or signing pre-empted formal approval — a governance/attestation data point. No other board actions disclosed (no AR approval, AGM notice, record date, dividend, director appointment, or capital-raising resolution) — nothing to schedule a Role 6 AR event on yet. A4 question on the timestamp. |
| N14 | F14 | note 9 (line 376); Sec7 para 8 vs Annexure I; "Annexure I" collision | 376, 153, 183, 37 | note 9: "financial results for the quarter and year ended June 30, 2026" | NEUTRAL-FACT | Cumulative drafting inconsistencies, individually immaterial: (a) note 9 labels a quarter-end (June 30, 2026) as "quarter and year ended", a copy-forward error; (b) an unnamed unreviewed trust in consol para 8 against two named trusts in Annexure I; (c) two different documents both labelled "Annexure I" (board-letter enclosure vs review-report entity list). OCR-only artifacts (e.g. "Abhira.i Singh Bhat", broken parentheses on standalone lines 514/521/529) excluded as non-substantive. Governance data-quality note. |
| N15 | F15 | Annexure I entity 7 (line 207); note 8 (line 370) | 207-208, 370 | "Urban Company Arabia for Information Technology ... (liquidated as on 24 May 2026)" ; "the Group has closed down its step-down subsidiary" | NEUTRAL-FACT | Entity 7 (Saudi step-down subsidiary) formally dissolved 24 May 2026 during the quarter; FCTR of Rs 5.27cr reclassified to P&L as the exceptional item (N1). A completed wind-down of a non-core international entity; one-off charge is now behind. No prior-quarter entity list supplied, so additions/renames/relationship changes beyond this disclosed liquidation could not be diffed — flagged for next quarter. |

---

## CHECKLIST SCORECARD (all 17)

| Check | Status | One-line basis |
|-------|--------|----------------|
| F1 Zero-value standing lines | FINDING | Exceptional-items template line activated (5.27, note 8 FCTR reclass, line 260); current-tax Nil in all periods bar a Rs 0.21cr Q4 balancing entry (line 264); listing-expense/fire-loss lines dormant (IPO/one-offs complete). See N1. |
| F2 Standalone vs consolidated | FINDING | S-vs-C PAT gap swung 18.07 to 7.84 (>5% of standalone PAT); standalone flipped +25.01 to -84.28 YoY. See N2. |
| F3 Shell-entity detection | PASS | Cost lines diverge S-vs-C (employee 151.15 vs 131.02; purchases 110.82 vs 54.39) — subsidiaries have real operations; depreciation near-identical (15.79 vs 15.09) only shows they are asset-light, not shells. No going-concern EoM. |
| F4 Unaudited contribution ratio | FINDING | Unreviewed trust = Rs Nil = 0% of PAT (below 10% threshold) but UNNAMED; likely Partner Welfare Trust, forward-material under Labour Codes. See N4. |
| F5 Going concern / EoM scope | FINDING | No GC EoM, but only Q1FY27 is BSR-reviewed; Q1FY26 has zero assurance, Q4FY26 is a balancing figure, FY26 was PwC-audited; no prior-quarter diff possible. See N5. |
| F6 Forward-commitment mining | PASS | No dated forward business commitments in notes; only completed actions ("has alloted", "has closed down") and administrative "will also be hosted on the Company's website" (line 43) / "being made available" (line 376). Logged in Commitment Register as completed milestones. |
| F7 Hedge phrase mining | PASS | Only assurance-scope "subject to review" / "not ... subjected to review" phrases (lines 108, 361, 418); no newly-added business hedges on revenue lumpiness or customer concentration. |
| F8 Tax forensics | FINDING | Deferred-tax CHARGES booked on pre-tax LOSSES every period (8.37 / 61.51 / 60.21) = DTA not recognized on losses; ETR non-meaningful; no earlier-year tax-adjustment line. See N8. |
| F9 OCI forensics | PASS | Actuarial remeasurement stable and small (0.21 vs prior-FY 5.08); no single-quarter swing exceeding prior year. The larger translation-FX OCI (5.03 vs FY26 2.33) is explained by the Saudi liquidation/FCTR, not an actuarial assumption change. |
| F10 Share count & dilution | FINDING | Paid-up 146.22 to 147.26 traces to 1,03,59,538 ESOP-2015 shares (note 7); basic = diluted EPS masks live ESOP overhang while loss-making. See N10. |
| F11 Reserves & net-worth tie-out | PASS | Net worth ties out: consol other equity 1,997.37 + paid-up 146.22 = 2,143.59; standalone 2,489.91 + 146.22 = 2,636.13; the 492.54 standalone-over-consol equity gap = cumulative subsidiary/JV losses (expected). No external third-party net-worth figure in context to reconcile; Q1FY27 quarter-end other equity not disclosed (year-end convention); net-cash floor not testable on a P&L filing. |
| F12 Segment forensics | FINDING | InstaHelp segment loss (-131.58) exceeds total consol loss; accelerating; core segments profitable. Segment assets/liabilities not disclosed. See N12. |
| F13 Board outcome beyond results | FINDING | MD/CEO signed both statements (15:23:46 / 15:22:53) before the stated 15:25 meeting conclusion; no AR/AGM/dividend/director/capital-raising actions. See N13. |
| F14 Note-drafting inconsistencies | FINDING | note 9 "quarter and year ended June 30, 2026" mislabel; unnamed unreviewed trust vs two named trusts; dual "Annexure I" labels. See N14. |
| F15 Entity-list diffs | FINDING | Entity 7 (Saudi step-down subsidiary) liquidated 24 May 2026 during the quarter (note 8); no prior list to diff further changes. See N15. |
| F16 Presentation-specific | N.A. | Doctype = results, not a presentation deck. |
| F17 Concall silence audit | N.A. | Doctype = results, not a concall transcript. |

Blank checks: none. GATE A3: pass.

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/turn ref | status word |
|------------|--------------|---------------|-------------|
| ESOP Trust allotment of 1,03,59,538 equity shares under ESOP-2015 | during Q1 FY27 (by 30 Jun 2026) | consol note 7 (line 367) / standalone note 6 (line 562) | completed |
| Closure/dissolution of step-down subsidiary Urban Company Arabia for Information Technology; FCTR Rs 5.27cr reclassified to P&L | dissolved 24 May 2026 | consol note 8 (line 370); Annexure I entity 7 (line 207) | completed |
| Financial results to be hosted on the Company's investor-relations website | on/after 31 Jul 2026 | board letter (line 43) | underway |
| Results being made available on BSE/NSE websites | on/after 31 Jul 2026 | consol note 9 (line 376) | underway |

No forward-dated business/operational commitments (no capex, guidance, or "expected to complete" milestones) present in the notes.

---

```yaml
stage: A3-forensics
company: "URBANCO"
quarter: "Q1 FY27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/urbanco-q1fy27/work/forensics_results_URBANCO_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: FINDING
  F3: PASS
  F4: FINDING
  F5: FINDING
  F6: PASS
  F7: PASS
  F8: FINDING
  F9: PASS
  F10: FINDING
  F11: PASS
  F12: FINDING
  F13: FINDING
  F14: FINDING
  F15: FINDING
  F16: N.A.
  F17: N.A.
findings:
  - {id: "N1", check: "F1", line: "260, 264", classification: "NEUTRAL-FACT", implication: "Exceptional-items template line fired once (Rs 5.27cr Saudi FCTR reclass); current-tax Nil confirms no cash-tax base while loss-making."}
  - {id: "N2", check: "F2", line: "268, 521", classification: "AMBIGUOUS", implication: "S-vs-C PAT gap swung >5% of standalone PAT; standalone flipped +25.01 to -84.28 YoY. A4 to decompose driver."}
  - {id: "N4", check: "F4", line: "153-159", classification: "FORWARD-SIGNAL", implication: "Unreviewed trust Nil/0% now but UNNAMED (likely Partner Welfare Trust); could turn material under Labour Codes aggregator contributions."}
  - {id: "N5", check: "F5", line: "128-132, 150-159, 361", classification: "CONFIRMATORY-NEGATIVE", implication: "Only Q1FY27 is BSR-reviewed; Q1FY26 zero assurance, Q4FY26 balancing figure, FY26 PwC-audited; first BSR review, no prior-quarter diff."}
  - {id: "N8", check: "F8", line: "261, 265, 268", classification: "FORWARD-SIGNAL", implication: "Deferred-tax charges on pre-tax losses = DTA not recognized on carryforwards; signals caution on near-term taxable profit / FY28 breakeven."}
  - {id: "N10", check: "F10", line: "281, 367, 287-288", classification: "FORWARD-SIGNAL", implication: "ESOP-2015 exercise added 1.036cr shares; basic=diluted masks overhang while loss-making; dilution surfaces once profitable."}
  - {id: "N12", check: "F12", line: "339, 346", classification: "FORWARD-SIGNAL", implication: "InstaHelp segment loss (-131.58) exceeds total consol loss and is accelerating; group loss is a single-segment story driving the FY28 breakeven question."}
  - {id: "N13", check: "F13", line: "40, 386-387, 575-576", classification: "AMBIGUOUS", implication: "MD/CEO signed both statements before the stated 15:25 board conclusion; governance/attestation data point. A4 question."}
  - {id: "N14", check: "F14", line: "376, 153, 183", classification: "NEUTRAL-FACT", implication: "Cumulative drafting inconsistencies (note-9 quarter/year mislabel; unnamed trust; dual Annexure I) — governance data quality."}
  - {id: "N15", check: "F15", line: "207-208, 370", classification: "NEUTRAL-FACT", implication: "Saudi step-down subsidiary liquidated 24 May 2026; one-off FCTR charge complete; no prior list to diff further changes."}
forward_signals: [N4, N8, N10, N12]
ambiguous: [N2, N13]
commitments:
  - {commitment: "ESOP Trust allotment of 1,03,59,538 shares under ESOP-2015", implied_date: "by 30 Jun 2026", ref: "consol note 7 (line 367)", status_word: "completed"}
  - {commitment: "Closure of step-down subsidiary Urban Company Arabia; FCTR Rs 5.27cr reclassified", implied_date: "24 May 2026", ref: "consol note 8 (line 370)", status_word: "completed"}
  - {commitment: "Results hosted on Company investor-relations website", implied_date: "on/after 31 Jul 2026", ref: "board letter (line 43)", status_word: "underway"}
  - {commitment: "Results made available on BSE/NSE websites", implied_date: "on/after 31 Jul 2026", ref: "consol note 9 (line 376)", status_word: "underway"}
gate_a3: pass
blank_checks: []
```
