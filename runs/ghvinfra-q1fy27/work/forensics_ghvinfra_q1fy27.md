# A3 FORENSIC NOTES — GHVINFRA (GHV Infra Projects Ltd, BSE 505504) — Q1 FY27 — doctype: results (SEBI Reg 30 MEDIA RELEASE)

Formerly Sindu Valley Technologies Ltd. Source: 3-page Reg 30 media release
(182-line A1 extract). A2 ledger reconciled 100% (all 59 positive-count rows
across Tables A-I read verbatim at cited lines before judging).

Document-type ceiling: this is a Reg 30 media release, NOT a Reg 33 statement.
The entire standard results architecture (consolidated results, full P&L, notes,
cash flow, balance sheet, segment table, auditor's limited-review report, Board
Outcome agenda) is absent by document type. Per A3 rules, such absences are
marked N.A. with the doctype reason UNLESS the absence is itself decision-relevant
against the AVOID thesis (parent-dependency / captive-customer / working-capital-
funded growth), in which case it is raised as a FINDING and flagged for A4.

---

## FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|----|-------|----------------|------|----------------------|----------------|---------------------|
| A3-01 | F2 | I1 / F3 | 101, 144 | "On a standalone basis, Company's Revenue from Operations surged 171.67% YoY" | AMBIGUOUS | Only standalone disclosed. Given 100% of FY25 receivables from parent GHV (India) Pvt Ltd and the 22-Jun-26 Rs 213 Cr RPT work order, the consolidated view (which would carry the parent/BCA royalty-management-fee extraction and eliminations) is exactly the number withheld. Cannot decompose S-vs-C gap. Flag for A4. |
| A3-02 | F8 | C1-C5 / D1 | 95-98, 110-112 | "PBT ... increase to Rs. 15.53 crore ... PAT ... Rs. 11.25 crore" | AMBIGUOUS | Below-EBITDA forensics: EBITDA% expanded +245 bps (10.38%→12.83%) yet PAT% CONTRACTED −71 bps (5.86%→5.15%). The EBITDA→PBT gap (D&A + finance cost proxy) widened from 2.52% to 5.73% of revenue (+321 bps), and implied ETR rose to 27.56% from 25.32% (both above 25.17% statutory). A finance-cost surge would corroborate the debt/working-capital-funded-growth AVOID driver (FY25 CFO −Rs 55.63 Cr). Neither the interest/depreciation split nor the tax line is disclosed. Flag for A4. |
| A3-03 | F10 | D2 / I15 | 112 | "Diluted EPS stood at Rs. 1.48 in Q1FY27." | AMBIGUOUS | Diluted EPS is the ONLY headline metric shown without a Q1FY26 comparator or YoY% (every other metric carries both periods). No basic EPS, no paid-up capital, no share count disclosed. Implied count = 11.25 Cr ÷ 1.48 ≈ 7.6 Cr shares. In a reverse-merger vehicle that issued shares, omitting the PY EPS comparator is the classic tell of a non-comparable (diluted) share base. Flag for A4. |
| A3-04 | F13 | E3 / G1-G3 | 88-91, 131-145 | "Appoints Shri Manoj Aggarwal ... Shri Dhanraj O. Tawade ... and Shri Swarup Dasgupta ... as Additional Independent Directors" | FORWARD-SIGNAL | Three simultaneous Additional Independent Director appointments. "Additional" directors must be regularised by shareholders at the next AGM = an AGM resolution event is incoming. Against the thesis governance-instability driver (3 CFO + 3 CS changes in 13 months, active CBI matter naming the promoter), a board rebuild is material. Independence caveat: Dasgupta is ex-Bank of India and currently Advisor–Corporate Credit at Punjab & Sind Bank (lender-relationship / independence consideration, G3). No DIN and no term/effective date given (I11, I12). Flag for A4. |
| A3-05 | F14 | A1 / A2 / B1 | 20, 25, 52, 55, 99 | "Mumbai, 10th August 2026" (release) vs "Date: August 11, 2026" (letter) / "Formally known as" | NEUTRAL-FACT | Drafting inconsistencies: media-release dateline (10-Aug-26, line 99) precedes the BSE letter + digital-signature date (11-Aug-26, lines 25, 55) by one day; "Formally" for "Formerly" (line 52); malformed brackets in bullet E3. Individually immaterial; cumulatively a mild governance-hygiene data point consistent with the churn thesis. Not flagged (no management question). |

---

## CHECKLIST SCORECARD (all 17 checks — GATE A3: no blanks)

| Check | Status | One-line basis |
|-------|--------|----------------|
| F1  ZERO-VALUE STANDING LINE ITEMS | N.A. | A2 zero_standing count = 0; only 5 aggregate headline metrics, no full P&L template exists to carry anticipatory nil lines (absent by document type). |
| F2  STANDALONE vs CONSOLIDATED | FINDING | Consolidated absent; standalone-only explicitly stated (line 101). Decision-relevant vs parent-dependency thesis. → A3-01. |
| F3  SHELL-ENTITY DETECTION | N.A. | No consolidated statement, no cost lines, no entity list to compare (absent by document type — Reg 30 media release, not Reg 33 statement). |
| F4  UNAUDITED CONTRIBUTION RATIO | N.A. | No auditor's Other Matters / no component-auditor disclosure exists (absent by document type). |
| F5  GOING CONCERN / EoM SCOPE | N.A. | No auditor's limited-review report and no prior-quarter extract provided to verbatim-diff (absent by document type). |
| F6  FORWARD-COMMITMENT PHRASE MINING | PASS | No notes exist; prose scanned for lexicon. Only non-dateable boilerplate hits ("is expected to support GHV Infra's growth ambitions", line 149-150; "well positioned to capture", "remains focused on"). No dated/dateable management commitment. Commitment register empty. |
| F7  HEDGE PHRASE MINING | PASS | Full text scanned (case-insensitive); none of the hedge lexicon ("no assurance", "subject to", "evaluating", "exploring", "in discussions", "endeavour", "may sometimes", "could have an effect") appears. Promotional register, no pre-emptive legal hedging. |
| F8  TAX FORENSICS | FINDING | Derived ETR 27.56% (Q1FY27) vs 25.32% (Q1FY26) vs 25.17% statutory; below-EBITDA charge (D&A+interest proxy) doubled as % of revenue. → A3-02. |
| F9  OCI FORENSICS | N.A. | No OCI / actuarial disclosure present (absent by document type). |
| F10 SHARE COUNT AND DILUTION | FINDING | Diluted EPS Rs 1.48 disclosed alone; no basic EPS, no PY comparator, no share count/paid-up capital. → A3-03. |
| F11 RESERVES / NET WORTH TIE-OUT | N.A. | No balance sheet, other equity, or paid-up capital disclosed (absent by document type). |
| F12 SEGMENT FORENSICS | N.A. | No segment table; only qualitative vertical descriptions (Table H), zero figures allocated (absent by document type; I6). |
| F13 BOARD OUTCOME BEYOND RESULTS | FINDING | Three Additional Independent Directors appointed; AGM ratification event incoming; governance signal vs churn thesis. → A3-04. |
| F14 NOTE DRAFTING INCONSISTENCIES | FINDING | Date discrepancy (10-Aug vs 11-Aug), "Formally"/"Formerly" typo, malformed brackets. → A3-05. |
| F15 ENTITY LIST DIFFS | N.A. | No consolidation entity list exists and no prior-quarter extract provided to diff (absent by document type). Note: listco NAME_CHANGE (Sindu Valley Technologies → GHV Infra, line 20) is a standing/known reverse-merger datum already in the thesis, not a new consolidation-list change. |
| F16 PRESENTATION-SPECIFIC | N.A. | Doctype is results, not a presentation (per prompt applicability rule). |
| F17 CONCALL SILENCE AUDIT | N.A. | Doctype is results, not a concall transcript (per prompt applicability rule). |

Tally: 5 FINDING, 2 PASS, 10 N.A. All 17 statused; no blanks.

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/ref | status word |
|------------|--------------|----------|-------------|
| (none) — no dated or dateable management commitment present; all forward language is qualitative outlook boilerplate (lines 116-122 MD quote; 149-160 outlook) | — | — | — |

---

## DERIVED-METRICS APPENDIX (audit trail for F8 / F10; all inputs are ledger rows C1-C5, D1, D2)

- ETR Q1FY27 = (15.53 − 11.25) / 15.53 = 4.28 / 15.53 = 27.56%.
- ETR Q1FY26 = (6.32 − 4.72) / 6.32 = 1.60 / 6.32 = 25.32%. Statutory = 25.17%.
  Note vs COMPANY MEMORY prior deferred-tax-shield: a shield would push ETR BELOW
  statutory; observed ETR is ABOVE statutory and rising YoY — shield appears absent
  or exhausted this quarter (or offset by non-deductibles / prior-year adjustments).
- PBT% Q1FY27 = 15.53 / 218.59 = 7.10%; Q1FY26 = 6.32 / 80.46 = 7.85% (−75 bps).
- EBITDA→PBT gap Q1FY27 = 28.05 − 15.53 = 12.52 = 5.73% of revenue;
  Q1FY26 = 8.35 − 6.32 = 2.03 = 2.52% of revenue → +321 bps. This is the mechanical
  reason EBITDA% rose +245 bps while PAT% fell −71 bps: below-EBITDA charges
  (depreciation + finance cost) grew far faster than revenue. Finance-cost intensity
  is the corroboration point for the working-capital/debt-funded-growth AVOID driver.
- Implied diluted shares = 11.25 Cr ÷ Rs 1.48 = ~7.6 crore shares (unverifiable; no
  share count disclosed).

## A4 HANDOFF — MANAGEMENT QUESTIONS (FORWARD-SIGNAL + AMBIGUOUS findings)

1. (A3-01, F2) Provide consolidated Q1FY27 results and quantify the standalone-vs-
   consolidated gap on revenue, EBITDA and PAT; state parent/BCA royalty and
   management-fee outflows and RPT eliminations.
2. (A3-02, F8) Decompose the below-EBITDA charge growth into depreciation vs finance
   costs; what was gross debt and interest expense in Q1FY27, and why did ETR rise to
   27.6% (above statutory) given the prior deferred-tax position?
3. (A3-03, F10) Reconcile diluted EPS Rs 1.48 to PAT 11.25 Cr: state basic and diluted
   share count, the Q1FY26 EPS comparator, and any dilutive instruments outstanding
   post reverse-merger.
4. (A3-04, F13) Provide DINs, effective dates and proposed AGM-ratification terms for
   the three new Additional Independent Directors; confirm independence of Shri Swarup
   Dasgupta given his current Advisor–Corporate Credit role at Punjab & Sind Bank.

Re-entry-trigger scan (per Notion checklist): NONE of the three re-entry conditions
(>40% non-RPT order book over 4 quarters; CBI matter closed; 2 consecutive years
positive cumulative CFO) is addressed or advanced by this document. No order-book,
customer-mix, CFO, or CBI disclosure is present. AVOID status unchanged; nothing here
fires a re-entry trigger, and F2/F8 absences mildly deepen the parent-dependency and
cash-conversion AVOID drivers.

```yaml
stage: A3-forensics
company: "GHVINFRA"
quarter: "Q1 FY27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/ghvinfra-q1fy27/work/forensics_ghvinfra_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: N.A.
  F2: FINDING
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: PASS
  F7: PASS
  F8: FINDING
  F9: N.A.
  F10: FINDING
  F11: N.A.
  F12: N.A.
  F13: FINDING
  F14: FINDING
  F15: N.A.
  F16: N.A.
  F17: N.A.
findings:
  - {id: "A3-01", check: "F2", line: "101", classification: "AMBIGUOUS", implication: "Standalone-only; consolidated (parent/BCA extraction + eliminations) withheld — cannot decompose S-vs-C gap under parent-dependency thesis"}
  - {id: "A3-02", check: "F8", line: "110-112", classification: "AMBIGUOUS", implication: "EBITDA% +245bps but PAT% -71bps; below-EBITDA charge doubled to 5.73% of revenue and ETR 27.56% (>statutory) — possible finance-cost/debt-funded-growth signal"}
  - {id: "A3-03", check: "F10", line: "112", classification: "AMBIGUOUS", implication: "Diluted EPS Rs 1.48 shown alone (no PY comparator, no basic EPS, no share count) — non-comparable reverse-merger share base likely concealed"}
  - {id: "A3-04", check: "F13", line: "88-91", classification: "FORWARD-SIGNAL", implication: "Three new Additional Independent Directors -> AGM ratification event incoming; board rebuild amid churn thesis; Dasgupta lender-independence caveat"}
  - {id: "A3-05", check: "F14", line: "99", classification: "NEUTRAL-FACT", implication: "Date discrepancy (10-Aug vs 11-Aug) plus 'Formally'/'Formerly' typo and malformed brackets — cumulative governance-hygiene data point"}
forward_signals: ["A3-04"]
ambiguous: ["A3-01", "A3-02", "A3-03"]
commitments: []
gate_a3: pass
blank_checks: []
```
