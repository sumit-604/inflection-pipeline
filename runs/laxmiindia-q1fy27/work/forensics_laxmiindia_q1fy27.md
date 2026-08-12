# A3 FORENSIC NOTES — LAXMIINDIA (Laxmi India Finance Limited) — Q1 FY27 — DOCTYPE: results (Reg 33 filing, NBFC-ML lending)

Source extract: `extract_results_laxmiindia_q1fy27.txt` (18 pages, 2374 lines, unit Lakhs, Lakhs->Cr x0.01).
Ledger: `ledger_results_laxmiindia_q1fy27.md`. Scope: **STANDALONE ONLY** (no consolidated financials; A2 re-verified, independently confirmed here at extract lines 17-19).
New name to pipeline: NO prior Notion thesis, NO companies/LAXMIINDIA.md, NO monitoring checklist, NO active tripwires. Any check mapping to the monitoring checklist is N.A. with that reason; first-thesis tripwire candidates are surfaced in the forward implications.

**Ledger reconciliation: 100%.** Every A2 ledger row was read at its cited line in the extract before judging (Board Outcome 51-303; Limited Review Report 305-486; P&L 487-724; Notes 740-911; Reg 52(4) 1010-1189; Annexure-I Parts A/B 1300-1458; Asset Cover Certificate 1660-1969; Annexure A 1970-2184; Appendix-1 OCR 2185-2374; signature blocks throughout).

**LIMITED REVIEW REPORT DISPOSITION: UNMODIFIED / UNQUALIFIED.** No Emphasis of Matter, no Going Concern paragraph, no Other Matters paragraph anywhere in the report. Para 4 (line 404): "nothing has come to our attention that causes us to believe that the Statement... has not disclosed the information required..." (standard negative-assurance conclusion). Para 5 (line 424) is a year-end balancing-figure explanation, explicitly closed at line 433: "Our conclusion on the Statement is not modified in respect of the above matter." Engagement is SRE 2410 limited review (para 3, line 357), moderate assurance, not an audit (line 365: "We have not performed an audit and accordingly, we do not express an audit opinion"). One entity reviewed: Laxmi India Finance Limited, standalone (line 335).

---

## FINDINGS TABLE

| id | check | ledger row ref | line | verbatim quote (short) | classification | forward implication |
|----|-------|----------------|------|------------------------|----------------|---------------------|
| A3-01 | F1 | Notes 8.1-8.4; Note 11 | 833-838, 857-864 | "Company has not transferred loans not in default through assignment..."; "has entered into an agreement for Co-Lending... has not entered in any Co-lending Arrangement in Quarter ended June 30, 2026" | FORWARD-SIGNAL | Company has stood up the RBI credit-risk-transfer disclosure template AND a co-lending framework agreement, but reports nil activity on both this quarter. These standing lines anticipate assignment / securitisation / co-lending as future capital-light growth and funding levers for an NBFC-ML. Watch for first non-nil entries in coming quarters. |
| A3-02 | F6 | Board item 2; Notes 9,10,11 | 130, 843, 849-853, 857 | "Approved the notice convening of 29th Annual General Meeting... on Wednesday, September 16, 2026"; "granted employee stock options during the quarter, with the grant date being May 12, 2026"; "has entered into an agreement for Co-Lending" | FORWARD-SIGNAL | Three dateable commitments (see Commitment Register). New ESOP grant (12 May 2026) seeds future dilution; co-lending agreement in place signals intent to build a co-lending book; AGM 16 Sep 2026 means the Annual Report drops within weeks. |
| A3-03 | F8 | P&L VIII.2, VIII.3 | 609, 612-614 | "Deferred Tax (11.50)/119.90/(188.43)/(359.95)"; "income Tax ...for Earlier Year ... 503" | FORWARD-SIGNAL | Effective tax rate 24.4% (Q1FY27), 24.2%/23.4%/24.7% prior periods — all below statutory 25.17% (~51-81 bps shield), driven by persistent deferred-tax credits (ECL/provisioning-timing DTA build typical of a growing NBFC book). As DTA accretion normalises, ETR steps up toward 25.17%, a modest forward EPS headwind. Non-zero "Income Tax for Earlier Year" of ~5.03 lakh in FY26 (per F8 rule, any earlier-year adjustment is flagged). |
| A3-04 | F9 | P&L X(A) remeasurement | 641, 651 | "Remeasurement Gains/(Losses) on Defined Benefit Plans (18.94)" | AMBIGUOUS | Q1FY27 actuarial remeasurement LOSS of 18.94 lakh (gross) exceeds the FULL prior-year FY26 remeasurement loss of 10.89 lakh in a single quarter. Per F9 this pattern is consistent with a defined-benefit assumption change (discount rate / salary escalation / plan-asset return). Verify actuarial assumptions at the Annual Report. -> A4 management question. |
| A3-05 | F10 | P&L XIII.a/XIII.b; Reg52(4) h.a/h.b | 685, 687-688, 1066, 1068 | P&L "Basic 3.07 ... Diluted 3.16"; Reg 52(4) "Basic 3.17" | AMBIGUOUS | Basic EPS reported THREE ways in one filing: 3.07 (P&L) vs 3.17 (Reg 52(4)) for the same quarter/company/document; and P&L shows Diluted (3.16) ABOVE Basic (3.07), which is impossible for a company with live dilutive ESOPs. Arithmetic check: PAT 1,657.26 lakh / ~5.24 cr shares ~ 3.16, and PAT incl OCI 1,643.08 ties exactly to Reg 52(4) g -> the 3.16/3.17 figures are internally supported and the P&L "3.07" is the outlier. Diluted EPS is NOT FOUND in the Reg 52(4) table (line 1068). -> A4: which Basic EPS is correct; is 3.07 a genuine filing misprint or extraction artifact (cross-check source PDF). Live ESOPs (Notes 9,10) = ongoing dilution. |
| A3-06 | F13 | Board item 2; agenda absence set | 130, 65-70 (ledger) | "Approved the notice convening of 29th Annual General Meeting" | FORWARD-SIGNAL | AGM notice approved -> Annual Report (Board's Report / MD&A) drops before 16 Sep 2026 -> schedule Role 6 AR Deep Dive. Watch the AGM notice for enabling special resolutions typical of a growing listed NBFC (borrowing-limit / NCD-issuance / ESOP-pool enabling resolutions). ABSENCE SET (recorded, not clean): no dividend, no director appointment/re-appointment, no auditor ratification/change, no capital-raising enabling resolution in this Board Outcome. |
| A3-07 | F14 | Asset Cover Cert para 7, 8 | 1826-1827, 1834 | "on which we issued an unmodified audit opinion vide our Audit report dated 12-08-2026 We have conducted our Audit in accordance with the Standard on auditing" | AMBIGUOUS | The statutory auditor's Security-Cover Certificate calls the engagement an "audit" with an "unmodified audit opinion" and "Audit report," but the actual engagement is a Limited Review under SRE 2410 (LRR para 3 line 357; certificate paras 1/6 lines 1670/1819 call it a review). Same auditor, same date (12-08-2026), same subject. Likely stale certificate-template boilerplate not updated for a review engagement; possible substantive scope mismatch. -> A4 question to management/auditor. |
| A3-08 | F14 | Appendix-1 second note | 2368 vs 2329 | "which are outstanding as on March 31, 2026 has been complied with" (inside a certificate captioned "as on 30th June 2026") | AMBIGUOUS | Covenant-compliance note references a March 31, 2026 date inside the June 30, 2026 security-cover certificate — carried-forward/stale prior-quarter boilerplate not updated. Individually immaterial; cumulatively a drafting-control data point. -> A4 clarification. |
| A3-09 | F14 | Note 11 (Co-Lending) | 857-864 | "The Company has entered into an agreement for Co-Lending... Company has not entered in any Co-lending Arrangement in Quarter ended June 30, 2026" | AMBIGUOUS | Note 11 is internally self-contradictory as drafted: it simultaneously asserts a co-lending agreement was entered AND that no co-lending arrangement was entered this quarter, with garbled derecognition logic ("didn't derecognised... required to be derecognise proportionately... should not be derecognised untill and unless associated risk are not transferred entirely"). -> A4: is there an active co-lending book, and what is the derecognition/retained-risk treatment. |
| A3-10 | F14 | Board meeting timing | 224 | "The above said Board Meeting commenced at 07:30 P.M. and concluded at 04%45 p.m." | NEUTRAL-FACT | Stated conclusion (04:45 PM) precedes stated commencement (07:30 PM); "04%45" also shows character corruption. Most likely extraction/typo artifact rather than substance; recorded per instruction. Cross-check source PDF image. |
| A3-11 | F14 | Annexure A signatory | 2164 | "(Director)" (no printed name) | NEUTRAL-FACT | The director who signed the Statement of Asset Cover / Exhibit 1 is identified only by role "(Director)", no printed name resolvable — governance disclosure gap (which director attested the asset-cover annexure). Cross-check source PDF image. |
| A3-12 | F2 | Ledger scope note; Note 3 | 17-19 (extract), 773 | "grep for 'consolidat*' returned zero hits -> standalone only"; "single reportable segment i.e. lending" | AMBIGUOUS | Standalone-only filing; F2 decomposition not computable (status N.A.). NOT recorded as clean: whether Laxmi India Finance has any subsidiaries / JVs / associates is undisclosed in this document. For an NBFC this is a disclosure gap. -> A4: does the Company have subsidiaries/JVs/associates, and if so why is no consolidated statement filed / what is the S-vs-C gap. |

---

## CHECKLIST SCORECARD (all 17 checks; every one carries exactly one status)

| # | Status | Basis (one line) |
|---|--------|------------------|
| F1 | FINDING | 33 zero-standing lines read; substantive signal = RBI credit-risk-transfer disclosures (Notes 8.1-8.4) and co-lending framework (Note 11) all nil-activity, anticipating future assignment/co-lending (A3-01). Remainder (Annexure-I NA fields, Exceptional Items, OCI-reclassifiable, near-nil FV loss, Appendix-1 nil rows) are neutral template lines. |
| F2 | N.A. | Standalone-only filing; no consolidated financials exist, so S-vs-C gap is not computable. NOT treated as clean: subsidiary/JV existence undisclosed = disclosure gap, surfaced as A3-12 -> A4 question. |
| F3 | N.A. | No consolidated cost lines / no subsidiary financials to compare; single standalone entity. Shell-entity detection not applicable. |
| F4 | N.A. | No JV/associate/component-auditor numbers; 100% of the Statement is covered by the statutory auditor's limited review. No "Other Matters" paragraph exists. Unaudited-contribution ratio not applicable. |
| F5 | PASS | Limited Review Report is UNMODIFIED; no Emphasis of Matter, no Going Concern, no Other Matters (lines 404, 424, 433). No prior-quarter extract available (new name) so no verbatim diff possible; nothing to escalate. |
| F6 | FINDING | Forward-commitment phrases mined in notes/board outcome: AGM 16 Sep 2026, ESOP grant 12 May 2026, co-lending agreement entered (A3-02). See Commitment Register. |
| F7 | PASS | Hedge lexicon ("no assurance", "subject to", "evaluating", "exploring", "in discussions", "endeavour") not present in the notes. Note 11 carries substantive retained-risk language but that is captured as a drafting/ambiguity item (A3-09), not a newly-added pre-emptive hedge. |
| F8 | FINDING | ETR 24.4%/24.2%/23.4%/24.7% all below statutory 25.17% on persistent deferred-tax credits (ECL DTA build); non-zero earlier-year tax adjustment ~5.03 lakh FY26 (A3-03). PBT and Total Tax totals reliable; current-tax cell has COLUMN_MISALIGN but does not affect ETR from totals. |
| F9 | FINDING | Single-quarter DB-plan remeasurement loss (18.94 lakh gross) exceeds full prior-year FY26 loss (10.89 lakh) = assumption-change candidate; verify at AR (A3-04). |
| F10 | FINDING | Basic EPS inconsistent (3.07 P&L vs 3.17 Reg52(4)); Diluted (3.16) reported above Basic (3.07); Diluted EPS absent from Reg52(4) table; live ESOP dilution (A3-05). |
| F11 | PASS | Net worth ties out: Paid-up 2,619.65 + implied Other Equity 45,592.69 = 48,212.34 (Reg52(4) f, line 1054); FY26 book NW 46,547.35 + Q1 PAT 1,657.26 + ESOP inflow ~= 48,212 (<0.1% gap). No third-party (rating) NW figure in the document to reconcile against. Net-worth exact figure is LOW_CONFIDENCE on decimal placement but reconciles. |
| F12 | N.A. | Note 3 (line 773): single reportable segment (lending) and single geographic segment (domestic); Ind AS 108 segment matrix not triggered, so no segment asset/liability trend exists. No product-level (MSME/vehicle/etc.) sub-disclosure to trend. |
| F13 | FINDING | Board approved 29th AGM notice (16 Sep 2026) -> AR imminent (schedule Role 6 AR Deep Dive); absence of dividend/director/auditor/capital-raise resolutions recorded (A3-06). |
| F14 | FINDING | Multiple drafting inconsistencies: audit-vs-review terminology in Asset Cover Certificate para 7/8 (A3-07); stale Mar-31-2026 covenant date in Jun-30-2026 certificate (A3-08); self-contradictory co-lending Note 11 (A3-09); board-meeting time anomaly (A3-10); unnamed "(Director)" signatory + EPS 3.07/3.17 conflict (A3-11, A3-05). Individually minor, cumulatively a governance/controls data point. |
| F15 | N.A. | No consolidation entity list exists (standalone-only) and no prior-quarter filing (new name); no additions/deletions/renames/relationship changes to diff. |
| F16 | N.A. | Doctype is a results filing, not an investor presentation; dropped/reframed-disclosure and chart-baseline checks not applicable. |
| F17 | N.A. | No concall transcript in scope; no Notion monitoring checklist (new name to pipeline) to run a silence audit against. |

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/ref | status word |
|------------|--------------|----------|-------------|
| 29th AGM to be convened via VC/OAVM | 16 Sep 2026 | Board Outcome item 2, line 130 | approved / upcoming |
| New ESOP options granted under Laxmi India ESOP-2023 (future vesting/dilution) | grant date 12 May 2026 | Note 10, lines 849-853 | completed (granted) |
| ESOP exercise: 1,25,203 shares allotted, paid-up 2,613.39 -> 2,619.65 lakh | during Q1 FY27 | Note 9, line 843 | completed |
| Co-Lending framework agreement entered (no arrangement executed yet this quarter) | ongoing | Note 11, lines 857-864 | initiated / framework in place |
| Asset cover of minimum 100% (NCDs) / 1.10x covenant maintained | as on 30 Jun 2026 | Note 6 line 806; Annexure A B.ii line 2014 | complied |

---

## FIRST-THESIS TRIPWIRE CANDIDATES (new name; no existing checklist — surfaced for A4/A5)
- Asset quality baseline: Gross Stage-3 2.08% (line 1125), Net Stage-3 0.94% (line 1127) — set as monitoring tripwire.
- Leverage/capital baseline: Debt/Equity 3.10 (line 1023), CRAR 25.32% (line 1129), Total debt/total assets 74.93% (line 1098).
- Governance/controls: EPS reported inconsistently within one filing (3.07 vs 3.17); auditor certificate calls a review an "audit" — controls-quality tripwire.
- Co-lending book emergence (Note 11) and credit-risk-transfer/assignment activity (Notes 8.1-8.4) — watch for first non-nil entries.
- Dilution: live ESOP scheme with fresh grant (Note 10) — track share-count creep.

## NOTES ON DATA QUALITY BEARING ON FINDINGS
- P&L numeric block carries COLUMN_MISALIGN; period-to-cell mapping is best-effort but ROW TOTALS (PBT, Total Tax, PAT, Paid-up) are reliable and were used for ETR, EPS and net-worth arithmetic. PAT 1,657.26 reconciles to Reg52(4) Net Profit incl OCI 1,643.08 (1,657.26 - 14.17 OCI), a strong internal consistency check.
- Appendix-1 (page 18) is OCR'd, LOW_CONFIDENCE on every numeric cell; the only precision-critical figure used is Debt Securities 5,504.72 lakh, which cross-checks to Annexure A Section A (Rs 55.05 Cr) and is treated as corroborated. Cover-on-Book-Value and Exclusive Security Cover Ratio values did not resolve — precision-critical, flagged low-confidence, not asserted.
- Both statutory-auditor UDINs are unreadable in extraction (UDIN_UNREADABLE) — not a finding, but noted for source-image verification.

---

```yaml
stage: A3-forensics
company: "LAXMIINDIA"
quarter: "Q1 FY27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/laxmiindia-q1fy27/work/forensics_laxmiindia_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: N.A.
  F3: N.A.
  F4: N.A.
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
  - {id: "A3-01", check: "F1", line: "833-838,857", classification: "FORWARD-SIGNAL", implication: "Credit-risk-transfer and co-lending frameworks stood up, nil activity; future assignment/co-lending levers"}
  - {id: "A3-02", check: "F6", line: "130,843,849,857", classification: "FORWARD-SIGNAL", implication: "AGM 16 Sep 2026 (AR imminent), ESOP grant 12 May 2026 (dilution), co-lending agreement entered"}
  - {id: "A3-03", check: "F8", line: "609,612-614", classification: "FORWARD-SIGNAL", implication: "ETR 24.4% vs 25.17% on persistent DTA credits; ETR step-up risk as DTA build normalises; earlier-year tax adj 5.03"}
  - {id: "A3-04", check: "F9", line: "641", classification: "AMBIGUOUS", implication: "Q1 DB-plan remeasurement loss 18.94 exceeds full FY26 10.89 = assumption-change candidate; verify at AR"}
  - {id: "A3-05", check: "F10", line: "685,687-688,1066,1068", classification: "AMBIGUOUS", implication: "Basic EPS 3.07 vs 3.17; Diluted>Basic anomaly; arithmetic supports 3.16-3.17, casts doubt on 3.07; ESOP dilution"}
  - {id: "A3-06", check: "F13", line: "130", classification: "FORWARD-SIGNAL", implication: "AGM notice -> Annual Report imminent (Role 6 AR Deep Dive); watch for enabling special resolutions; absence set recorded"}
  - {id: "A3-07", check: "F14", line: "1826-1827,1834", classification: "AMBIGUOUS", implication: "Auditor certificate calls a limited review an audit ('unmodified audit opinion'/'Audit report'); template mismatch or scope issue"}
  - {id: "A3-08", check: "F14", line: "2368", classification: "AMBIGUOUS", implication: "Stale 'as on March 31, 2026' covenant date inside a 30 Jun 2026 certificate; drafting-control gap"}
  - {id: "A3-09", check: "F14", line: "857-864", classification: "AMBIGUOUS", implication: "Note 11 self-contradictory on co-lending existence and derecognition treatment"}
  - {id: "A3-10", check: "F14", line: "224", classification: "NEUTRAL-FACT", implication: "Board meeting conclusion time precedes commencement time as extracted; likely artifact, verify source"}
  - {id: "A3-11", check: "F14", line: "2164", classification: "NEUTRAL-FACT", implication: "Asset-cover annexure signed only as '(Director)', no printed name; governance disclosure gap"}
  - {id: "A3-12", check: "F2", line: "17-19,773", classification: "AMBIGUOUS", implication: "Standalone-only; subsidiary/JV existence undisclosed; is a consolidated statement owed / what is S-vs-C gap"}
forward_signals: ["A3-01", "A3-02", "A3-03", "A3-06"]
ambiguous: ["A3-04", "A3-05", "A3-07", "A3-08", "A3-09", "A3-12"]
commitments:
  - {commitment: "29th AGM via VC/OAVM", implied_date: "2026-09-16", ref: "line 130", status_word: "approved"}
  - {commitment: "New ESOP options granted (future dilution)", implied_date: "2026-05-12", ref: "Note 10, line 849", status_word: "completed"}
  - {commitment: "ESOP exercise, 1,25,203 shares allotted", implied_date: "Q1FY27", ref: "Note 9, line 843", status_word: "completed"}
  - {commitment: "Co-Lending framework agreement entered", implied_date: "ongoing", ref: "Note 11, line 857", status_word: "initiated"}
  - {commitment: "Minimum 100% NCD asset cover / 1.10x covenant maintained", implied_date: "2026-06-30", ref: "Note 6 line 806; Annexure A line 2014", status_word: "complied"}
gate_a3: pass
blank_checks: []
```
