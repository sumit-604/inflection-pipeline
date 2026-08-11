# A3 FORENSIC NOTES — Macfos Limited (MCFOS), Q1 FY27, doctype: RESULTS

Source extract: `/home/user/inflection-pipeline/runs/mcfos-q1fy27/work/extract_results_mcfos_q1fy27.txt`
A2 ledger: `/home/user/inflection-pipeline/runs/mcfos-q1fy27/work/ledger_results_mcfos_q1fy27.md`
Prior-quarter extract: none (first pipeline run for MCFOS)
Ledger reconciliation: 100% — every A2 row read at its cited line before judging.
Unit convention: Lakhs (x0.01 = Rs Cr). Glyph-spaced pages (1,2,5,9,10,11,12) de-spaced when parsing numbers; OCR pages (3,4,6,7,8) read normally.
Bias: conservative; lean bear and generate a question on ambiguity.

---

## FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|----|-------|----------------|------|----------------------|----------------|---------------------|
| F3-01 | F3 | §3 para 7 / §4 row 2 | 383-394 | "total assets of Rs. 0.99 lakhs as at 30 June 2026 and total revenue of Rs. Nil ... furnished to us by the management, are certificated by the board of directors of this subsidiary" | AMBIGUOUS | Nuo Zhan Technologies (HK) is a shell: nil revenue, Rs 0.99L assets, unaudited, management-furnished. Robu.in imports electronics from China; a dormant HK entity is a live conduit candidate. Ask what it is for and whether related-party flows are planned. |
| F6-01 | F6 | §1 items 1,3,4,5,13 | 52-98 | "To Approve the Annual Report for Financial Year 2025-26 and Draft Notice for Calling of 9th Annual General Meeting" | FORWARD-SIGNAL | Board-approved dated commitments: Ind AS live FY27; AR FY26 + 9th AGM notice imminent (record date, eVoting, special resolutions). Schedule Role 6 AR deep-dive. |
| F7-01 | F7 | §2 para 5 / §3 para 6-7 | 183-197, 362-394 | "These comparative quarterly Ind AS financial results have not been subjected to Limited Review by us" | CONFIRMATORY-NEGATIVE | Every Q1FY26 and FY26 Ind AS comparative the thesis benchmarks against is management-converted and unreviewed; consolidated conclusion on Nuo Zhan rests "solely on such certified information". YoY comps carry weaker assurance than they appear. |
| F8-01 | F8 | §5 row 17 / §6 row 17 | 251, 464 | "S h o r t / ( e x c e s s ) in c o m e t a x o f e a r l ie r ye a r s ... ( 2. 6 5 )" | NEUTRAL-FACT | Non-zero prior-year tax adjustment Rs 2.65L in FY26 (nil in quarters) — per F8 rule any earlier-year tax item is flagged. Deferred tax also flips from persistent credits (FY26 -29.79) to a small charge (+0.44) in Q1FY27. Immaterial quantum; ETR ~26.5% vs 25.17% statutory. |
| F11-01 | F11 | §5 row 25 (paid-up only) | 270, 235 | "Changes in Inventory of Stock-in-Trade ... ( 1, 7 9 1. 3 6 )" | FORWARD-SIGNAL | No balance sheet / no Other Equity / no cash flow in the filing: statutory net worth cannot be tied out, and five Notion balance-sheet monitors go dark (inventory days, receivable days, ST borrowings Rs 35Cr tripwire, slow-moving inv%, CFO/PAT). Meanwhile finance cost +79% YoY (56.05->100.40) and a Rs 17.9Cr inventory build this quarter — exactly the metrics now unverifiable. |
| F12-01 | F12 | §7 orphan note | 534-536 | "The company is engaged in only one business, hence no separate segment information has been furnished in accordance with Ind AS 108" | FORWARD-SIGNAL | Single-segment declaration suppresses the B2B corporate share (Notion green 50-60%) and Robu 2.0 revenue share (>5% trigger) splits the thesis is built to monitor. No statutory segment table will ever surface these. |
| F13-01 | F13 | §1 items 3,5 | 58-66 | "who retires by rotation ... being eligible, offers himself for re-appointment" | FORWARD-SIGNAL | AR FY26 + 9th AGM approved (item 3). Director re-appointment: Nileshkumar P. Chavhan (DIN 07936897, appointed 11/01/2023), a domain expert (M.E. Mech IISc; robotics/electronics) holding 23.04% — retained through the growth window; no independent director non-renewal present. |
| F13-02 | F13 | §1 items 6,8,9,11 | 67-94 | "To consider if any outstanding statutory liability is pending for more than 3 months" | AMBIGUOUS | Four compliance-hygiene agenda items (overdue statutory dues >3m, MSME non-payment >45d, litigation >Rs1L, statutory-return delays) all phrased "if any" with NO value and NO explicit Nil disclosed (only investor complaints are confirmed Nil, Note 8). Silence on exposure, not confirmation of none. |
| F14-01 | F14 | §1 items 7&12 / §7 gap / §6 rows 34-35 | 76-97, 531-541, 281/501 | "To take note of the Quarter ended listing compliances ... for the period ended on 30th June 2026" (item 12, duplicate of item 7) | NEUTRAL-FACT | Cumulative drafting hygiene: agenda items 7 and 12 near-verbatim duplicates; note-number markers 3 and 5 absent (content present, numbers missing) at 531-536/541; EPS share count differs standalone 1,03,58,503 vs consolidated 1,03,58,504 by one share. Each immaterial; together a governance data point. |
| F15-01 | F15 | §3 para 7 / §4 row 3 | 343, 396-398 | "Macfos Electronics Private Limited it reflects total assets of Rs.12.23 lakhs ... total revenue of Rs. 1.16 lakhs" | FORWARD-SIGNAL | New subsidiary vs prior known structure (Company Memory: Macfos + Nuo Zhan only). Early-stage (Rs 12.23L assets, Rs 1.16L revenue). An "Electronics" entity may signal a move from pure trading toward assembly/vertical integration. Baseline entity list for future diffs. |

---

## CHECKLIST SCORECARD (all 17)

| Check | Status | One-line basis |
|-------|--------|----------------|
| F1 ZERO-VALUE STANDING LINES | PASS | 25 zero-standing rows read at cited lines; all are standard template lines (Exceptional Item nil, NCI lines nil for 100%-owned group, OCI reclass lines, investor complaints Nil). Earlier-years tax non-zero routed to F8; no line anticipates an undisclosed transaction class. |
| F2 STANDALONE vs CONSOLIDATED | PASS | S-vs-C PAT gap: Q1FY27 -0.79L, Q1FY26 -0.62L, Q4FY26 +1.46L, FY26 -0.91L — all <0.3% of standalone PAT, no period swings >5pp. Revenue gap +0.14L (Macfos Electronics 1.16 net of ~1.02L elimination). |
| F3 SHELL-ENTITY DETECTION | FINDING | Cost lines near-identical S vs C (materials 28.71=28.71, purchases 7,953.00=7,953.00, employee 368.68=368.68); Nuo Zhan is a shell (nil revenue, Rs 0.99L assets, unaudited). See F3-01. |
| F4 UNAUDITED CONTRIBUTION RATIO | PASS | Only unaudited entity (Nuo Zhan) contributes nil revenue and Rs 0.99L assets to the Group; PAT contribution ~0%, well below the 10% threshold; auditor deems it "not material to the Group" (line 394). Qualitative assurance weakness captured in F7. |
| F5 GOING CONCERN / EoM SCOPE | PASS | No going concern emphasis-of-matter present. "Other Matter" paragraphs are Ind AS first-adoption scope (transition, unreviewed comparatives, unaudited subsidiary) — catalogued here as the baseline for future QoQ verbatim diffs; substantive audit-language content routed to F7. No prior quarter to diff. |
| F6 FORWARD-COMMITMENT MINING | FINDING | Board-approved dated commitments (Ind AS FY27, AR FY26 + 9th AGM notice, scrutinizer/eVoting, director re-appointment, ROC e-Forms). See F6-01 and Commitment Register. |
| F7 HEDGE PHRASE MINING | FINDING | Auditor pre-emptive limitation language: comparatives "have not been subjected to Limited Review by us"; Nuo Zhan conclusion "based solely on such certified information". See F7-01. |
| F8 TAX FORENSICS | FINDING | ETR Q1FY27 ~26.5% (vs 25.17% statutory), all periods 25.3-26.5%; deferred tax flips credits->charge; earlier-years tax adjustment Rs 2.65L (FY26) non-zero. See F8-01. |
| F9 OCI FORENSICS | PASS | Current-quarter OCI ~nil (standalone —, consolidated 0.00); no single-quarter swing exceeding the full prior year. FY26 gratuity remeasurement (22.01L) sits entirely in the unreviewed Q1FY26 comparative — immaterial to PAT; verify actuarial assumptions at the AR (Role 6). |
| F10 SHARE COUNT AND DILUTION | PASS | Paid-up rise 941.68->1,035.85L (+94.17L) traces exactly to 941,682 bonus shares 1:10 on 11-Mar-2026 (Note 6, line 541). Basic = diluted EPS every period; no dilutive instruments. One-share S-vs-C count mismatch routed to F14. |
| F11 RESERVES / NET WORTH TIE-OUT | FINDING | No Other Equity / reserves / balance sheet in the filing; net worth un-tieable; the omission blacks out five Notion balance-sheet monitors amid +79% YoY finance cost and a Rs 17.9Cr inventory build. See F11-01. |
| F12 SEGMENT FORENSICS | FINDING | Single-segment declaration (Ind AS 108) removes B2B corporate share and Robu 2.0 visibility the thesis monitors. See F12-01. |
| F13 BOARD OUTCOME BEYOND RESULTS | FINDING | AR FY26 + 9th AGM approved (Role 6 trigger); domain-expert director re-appointed; compliance-hygiene items disclose no values. See F13-01, F13-02. |
| F14 NOTE DRAFTING INCONSISTENCIES | FINDING | Duplicate agenda items 7/12; missing note numbers 3 and 5; one-share EPS count mismatch S vs C. See F14-01. |
| F15 ENTITY LIST DIFFS | FINDING | New subsidiary Macfos Electronics Pvt Ltd vs prior known structure. See F15-01. |
| F16 PRESENTATION-SPECIFIC | N.A. | Doctype is results; no presentation deck in scope. |
| F17 CONCALL SILENCE AUDIT | N.A. | Doctype is results; no transcript. Silence-audit logic run against the filing's monitoring-checklist coverage and folded into F11-01 (balance-sheet/cash-flow omission blacks out inventory days, receivable days, ST borrowings, slow-moving inv%, CFO/PAT) and F12-01 (B2B / Robu 2.0 segment opacity). |

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/item ref | status word |
|------------|--------------|---------------|-------------|
| Voluntarily adopt IND AS for financial statements | FY2026-27 onwards (live this quarter) | agenda item 1, line 52-54; Note 2, line 524 | commenced / completed |
| Approve Annual Report FY2025-26 and Draft Notice for 9th AGM | within weeks (AR release + AGM) | agenda item 3, line 58-60 | board approved |
| Appoint CZ & Associates LLP as Scrutinizer for eVoting | ensuing AGM | agenda item 4, line 61-63 | board approved |
| Re-appoint director retiring by rotation (N. P. Chavhan) | at upcoming AGM | agenda item 5, line 64-66 | proposed, subject to AGM approval |
| Authorize Directors to file e-Forms with ROC | ongoing | agenda item 13, line 98 | board approved |
| Special Purpose Independent Auditor's Report on Ind AS FY26 statements | dated 11-Aug-2026 | LRR Other Matter, line 194-195, 373-374 | has been completed/issued |

---

## FORWARD-SIGNAL SUMMARY (for A4 -> management questions)

- FORWARD-SIGNAL: F6-01, F11-01, F12-01, F13-01, F15-01
- AMBIGUOUS (lean-bear, question not resolved): F3-01, F13-02
- These seven feed A4. Highest-value questions: (1) purpose and future use of the Nuo Zhan HK shell given China-import sourcing [F3-01]; (2) why the balance sheet / cash flow is withheld when finance cost is up 79% YoY and inventory built Rs 17.9Cr [F11-01]; (3) B2B corporate share and Robu 2.0 revenue share under single-segment reporting [F12-01]; (4) purpose of the new Macfos Electronics subsidiary — trading vs assembly [F15-01]; (5) any actual figures behind the statutory-liability / MSME / litigation compliance items [F13-02].

Notion monitoring read (context, not a check): Revenue +37.2% YoY = green; EBITDA margin ~10.6% = green; PAT margin 7.16% (down from 8.38% YoY) = amber, drifting toward the 6.5% red; CFO/PAT, inventory days, receivable days, ST borrowings = UNVERIFIABLE this filing (F11-01). Mainboard-listing catalyst: no BSE migration filing referenced.

---

```yaml
stage: A3-forensics
company: "MCFOS"
quarter: "Q1 FY27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/mcfos-q1fy27/work/forensics_mcfos_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: PASS
  F2: PASS
  F3: FINDING
  F4: PASS
  F5: PASS
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: PASS
  F10: PASS
  F11: FINDING
  F12: FINDING
  F13: FINDING
  F14: FINDING
  F15: FINDING
  F16: N.A.
  F17: N.A.
findings:
  - {id: "F3-01", check: "F3", line: "383-394", classification: "AMBIGUOUS", implication: "Nuo Zhan HK is a nil-revenue unaudited shell; live conduit candidate for China-import related-party flows"}
  - {id: "F6-01", check: "F6", line: "58-60", classification: "FORWARD-SIGNAL", implication: "AR FY26 + 9th AGM notice approved; Role 6 AR deep-dive and record-date/eVoting imminent"}
  - {id: "F7-01", check: "F7", line: "183-197", classification: "CONFIRMATORY-NEGATIVE", implication: "Q1FY26/FY26 Ind AS comparatives unreviewed; consolidated conclusion rests solely on certified subsidiary info; YoY comps weakly assured"}
  - {id: "F8-01", check: "F8", line: "251", classification: "NEUTRAL-FACT", implication: "Earlier-years tax adjustment Rs 2.65L non-zero (FY26); deferred tax flips credit->charge; immaterial quantum"}
  - {id: "F11-01", check: "F11", line: "270", classification: "FORWARD-SIGNAL", implication: "No balance sheet/cash flow; net worth un-tieable; five Notion BS monitors dark while finance cost +79% YoY and Rs 17.9Cr inventory build"}
  - {id: "F12-01", check: "F12", line: "534-536", classification: "FORWARD-SIGNAL", implication: "Single-segment reporting hides B2B corporate share and Robu 2.0 revenue share the thesis monitors"}
  - {id: "F13-01", check: "F13", line: "58-66", classification: "FORWARD-SIGNAL", implication: "AR + 9th AGM approved; domain-expert 23.04%-holder director re-appointed through growth window"}
  - {id: "F13-02", check: "F13", line: "67-94", classification: "AMBIGUOUS", implication: "Statutory-liability/MSME/litigation/return-delay items disclose no values and no explicit Nil; silence on exposure"}
  - {id: "F14-01", check: "F14", line: "76-97", classification: "NEUTRAL-FACT", implication: "Duplicate agenda items 7/12, missing note numbers 3&5, one-share S-vs-C EPS count mismatch; cumulative governance hygiene"}
  - {id: "F15-01", check: "F15", line: "343", classification: "FORWARD-SIGNAL", implication: "New subsidiary Macfos Electronics Pvt Ltd vs prior structure; possible trading-to-assembly vertical integration"}
forward_signals: ["F6-01", "F11-01", "F12-01", "F13-01", "F15-01"]
ambiguous: ["F3-01", "F13-02"]
commitments:
  - {commitment: "Adopt IND AS from FY2026-27 onwards", implied_date: "FY27 (live)", ref: "item 1 / Note 2, line 52-54,524", status_word: "commenced"}
  - {commitment: "Approve AR FY2025-26 + Draft Notice 9th AGM", implied_date: "within weeks", ref: "item 3, line 58-60", status_word: "approved"}
  - {commitment: "Appoint CZ & Associates LLP scrutinizer for eVoting", implied_date: "ensuing AGM", ref: "item 4, line 61-63", status_word: "approved"}
  - {commitment: "Re-appoint director retiring by rotation (Chavhan)", implied_date: "upcoming AGM", ref: "item 5, line 64-66", status_word: "proposed"}
  - {commitment: "Authorize e-Form filing with ROC", implied_date: "ongoing", ref: "item 13, line 98", status_word: "approved"}
  - {commitment: "Special Purpose Independent Auditor Report on Ind AS FY26", implied_date: "11-Aug-2026", ref: "LRR Other Matter, line 194-195,373-374", status_word: "completed"}
gate_a3: pass
blank_checks: []
```
