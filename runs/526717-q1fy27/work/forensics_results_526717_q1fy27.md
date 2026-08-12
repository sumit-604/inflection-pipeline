# A3 FORENSIC NOTES — 526717 (HCP Plastene Bulkpack Ltd) — Q1 FY27 — doctype: results

Source A1 extract: `extract_results_526717_q1fy27.txt` (18 pages, 793 lines, Lakhs)
A2 ledger: `ledger_results_526717_q1fy27.md` — 149 line_items / 24 zero_standing / 18 agenda_items / 9 auditor_paras / 6 notes / 3 entities.
Ledger reconciliation: **100%** — every A2 row read verbatim at its cited line before judging.
Doctype scope: F1-F15 apply; F16 (presentation) and F17 (concall) are N.A. on a results filing.

---

## FINDINGS TABLE

| id | check | ledger row ref | line | verbatim quote | classification | forward implication |
|----|-------|----------------|------|----------------|----------------|---------------------|
| A3-01 | F1 | S-P&L 10/11/12 (486-488), C-P&L 10/11/12 (689-691), S-Tax 8a (482) | 486, 689, 482 | "Profit (Loss) from discontinuing operations before tax ... - - - -" | CONFIRMATORY-NEGATIVE | Discontinued-ops template rows stand empty in the same quarter the Malaysia LLP subsidiary was dissolved (line 107): the dissolution was NOT routed through discontinued operations, so no gain/loss/asset write-off is visible. Standalone Current Tax is zero all four periods while PBT is positive — cash-tax anticipated but never booked (see F8). |
| A3-02 | F2 | S-P&L 13 (489) vs C-P&L 13 (692) | 489, 692 | S "900.08 ... 805.25 ... 69.78 ... 1,724.63" vs C "1,834.64 ... 832.30 ... 712.44 ... 2,879.23" | FORWARD-SIGNAL | Consolidated-minus-standalone PAT gap swings violently: Q1FY27 +934.56 (104% of standalone PAT), Q4FY26 +27.05 (3%), Q1FY26 +642.66 (921%), FY26 +1,154.60 (67%). The entire Q1FY27 gap of 934.56 equals subsidiary KP Woven's PAT of 934.56 (line 628) to the paisa; earnings quality now rides on one lumpy, unreviewed subsidiary. Swing far exceeds the 5pp-of-standalone-PAT threshold. |
| A3-03 | F4 | Consolidated Other Matters para 5 (625-637) | 628 | "total net profit after tax of Rs. 934.56 lakhs ... furnished to us by the Management" | FORWARD-SIGNAL | KP Woven PAT 934.56 / consolidated PAT 1,834.64 = **50.9% of group PAT is management-furnished, not independently reviewed**; its assets 37,246.46 / consolidated 56,913.94 = 65% of the balance sheet. Well above the 10% threshold and rising, against a backdrop of auditor churn (internal auditor withdrew consent 17-Jul-2026, CFO resigned 12-Aug-2026). |
| A3-04 | F6 | Board items 6, 7, 5a-5f, 10a, 11 | 93, 72, 139 | "The Board has also approved the Re appointment of Mr. Prakash Hiralal Parekh ... with effect from 1st November 2026, subject to approval of shareholders" | FORWARD-SIGNAL | Multiple dated management commitments crystallise at the 42nd AGM on 25-Sep-2026 (record date 18-Sep, e-voting 19-24 Sep): MD reappointment effective 1-Nov-2026, ID reappointment w.e.f. 9-Aug-2026, and adoption of a new set of Articles of Association. See Commitment Register. |
| A3-05 | F8 | S-Tax 8a Current (482), 8b Deferred (484); C-Tax 8a (684), 8b Deferred (687) | 482, 484 | Current Tax "- - - -"; "Deffered Tax (Income)/Expense 357.05 ... 240.92 ... 30.38 ... 683.41" | FORWARD-SIGNAL | Standalone books **zero current tax in all four periods** on positive PBT (Q1FY27 PBT 1,257.13); the whole standalone tax charge is deferred. A cash-tax shield of roughly Rs 3.1cr/quarter (≈25% x 1,257) is being deferred, implying a future ETR/cash-tax step-up when the shelter (carryforward / MAT credit / DTA) is exhausted. Consolidated ETR 30.2% (793.74/2,628.36) already exceeds standalone book ETR 28.4%. "Tax for Earlier Years" is nil, so no prior-year adjustment finding. |
| A3-06 | F10 | S-EPS 18a/18b (504-505), C-EPS 19a/19b (718-719) | 719 | Consolidated FY: "(a) Basic 27.01 ... (b) Diluted 21.60" | FORWARD-SIGNAL | Basic-vs-diluted spread confirms live dilutive ESOP-2022 options (2,50,000 pool, 17,680 vested, 16,780 exercised, 29,450 lapsed — Annexure D). Paid-up capital shown as 1,067.48 in all periods will step to 1,069.16 next quarter (line 133, +16,780 shares). The FY consolidated diluted EPS of 21.60 vs basic 27.01 (20% spread) is wildly inconsistent with the ~0.5% quarterly spreads — flagged AMBIGUOUS, likely a typo but material if real. |
| A3-07 | F11 | S-P&L 17 (501), C-P&L 18 (715) | 501, 715 | "Other Equity exluding revaluation reserve" (row printed with NO value in any of the four columns) | AMBIGUOUS | Other Equity is omitted entirely in both standalone and consolidated statements, so statutory net worth (Paid-up 1,067.48 + Other Equity) cannot be tied out from this filing. Reconciliation impossible; A4 should request the reserves figure and reconcile against any rating/AR number. |
| A3-08 | F12 | C-Segment Assets 3a (769) & Liabilities 4a (774) | 769, 774 | Woven Sacks assets "55,189.49 ... 34,476.90 ... 27,296.77"; liabilities "35,746.08 ... 17,421.93 ... 21,460.01" | FORWARD-SIGNAL | Consolidated Woven Sacks segment assets jumped +60% QoQ (+Rs 207cr) while its liabilities more than doubled +105% QoQ (+Rs 183cr): a debt/WC-funded build, not equity-funded. Total consolidated segment liabilities Rs 443.56cr. Directly feeds FLAG-GATE0 leverage and the monitoring tripwire (bank WC borrowings > Rs 98.68cr). Label Division holds Rs 17.0cr assets against only Rs 0.54cr revenue = idle capacity. |
| A3-09 | F13 | Board items 3 (51), 4 (56), 5 (60), 6 (93), 7 (98), 11 (139) | 56, 93 | "The Board approved the Board Report together with all the Annexures ... for the financial year ended March 31, 2026" | FORWARD-SIGNAL | Board Report + Annexures for FY26 approved -> full Annual Report drops within weeks -> schedule Role 6 AR Deep Dive. New Articles of Association (special resolution) and both director reappointments go to the 25-Sep-2026 AGM. Promoter-family MD Prakash Hiralal Parekh (father of ED Aman Parekh, line 208) reappointed for 3 years through the commissioning window; new ID Sandeep Shah is a CA / PSU-bank auditor. |
| A3-10 | F14 | Board item 10a (132-135), C Other Matters (631-634), consolidated results title (657) | 134, 634 | item 10a capital-increase cites "(Annexure C is attached for reference)" [ESOP detail is in Annexure D]; Other Matters "furnished to us by the Management ... based solely on the report of such auditor" | CONFIRMATORY-NEGATIVE | Cluster of drafting defects: wrong annexure cross-reference on the capital-increase disclosure; Other Matters paragraph internally contradicts itself (says management-furnished with no component auditor, yet relies on "the report of such auditor"); consolidated results titled "for the Year ended 30th Jun 2026" (line 657) instead of Quarter; Annexure C row "5" printed twice (lines 290, 293); duplicate "b)" labels in both P&Ls; Board items 6-9 unnumbered. Individually immaterial, cumulatively a FLAG-GOVERNANCE / FLAG-DISCLOSURE data point in the same filing as a CFO exit. |
| A3-11 | F15 | Entities E2 Malaysia (107-109), E3 unnamed JV (681, 764) | 107, 681 | "dissolution of HCP Plastene Bulkpack PLT, a Limited Liability Partnership incorporated in Malaysia and a subsidiary"; "Share of Profit / (Loss) of Joint Venture using Equity Method - - 2.53" | AMBIGUOUS | Malaysia LLP subsidiary removed from the group this quarter (deletion). An equity-method Joint Venture is referenced in both the consolidated P&L (line 681) and consolidated segment table (line 764) but is **never named anywhere in the 18-page filing**; its share of profit fell from 2.53 (Q1FY26) to nil/blank in Q1FY27 and Q4FY26 — a JV that has gone silent and unidentified. A4 must ask for the JV name and status (ties to the Saudi BOPP JV monitoring item). No prior-quarter extract was supplied, so the entity list could not be verbatim-diffed. |

---

## CHECKLIST SCORECARD (all 17, one status each)

| Check | Status | One-line basis |
|-------|--------|----------------|
| F1 ZERO-VALUE STANDING LINES | FINDING | 24 zero-standing rows; discontinued-ops lines (486-488/689-691) empty while Malaysia LLP dissolved; standalone current tax zero all periods (482). |
| F2 STANDALONE vs CONSOLIDATED | FINDING | PAT gap swings 3% -> 921% -> 104% of standalone PAT across periods; Q1FY27 gap = subsidiary PAT 934.56 exactly. |
| F3 SHELL-ENTITY DETECTION | PASS | Subsidiary KP Woven has genuine operations (C materials 12,350 vs S 9,627; C employee 718 vs S 214; revenue 8,636); no shell, no going-concern EoM. |
| F4 UNAUDITED CONTRIBUTION | FINDING | 50.9% of consolidated PAT and 65% of assets are management-furnished/unreviewed (KP Woven, para 5, line 628). |
| F5 GOING CONCERN / EoM SCOPE | PASS | No going-concern/EoM paragraph exists; only a standard subsidiary-reliance Other Matters para (drafting defect logged under F14); no prior extract to diff. |
| F6 FORWARD-COMMITMENT MINING | FINDING | Dated commitments: MD reappt 1-Nov-2026, ID reappt 9-Aug-2026, AGM 25-Sep-2026, new AOA — all "subject to approval". |
| F7 HEDGE PHRASE MINING | PASS | Only "subject to [shareholder] approval" corporate-action conditionality (already in F6/F13); no new risk/revenue-lumpiness/customer-concentration hedges added. |
| F8 TAX FORENSICS | FINDING | Standalone current tax zero all four periods on positive PBT; entire charge deferred -> future cash-tax step-up; earlier-year tax nil. |
| F9 OCI FORENSICS | PASS | Actuarial/OCI swings tiny (S remeasurement -1.08; C FY OCI 4.09 vs Q1FY27 0.64); no single-quarter swing exceeding prior year. |
| F10 SHARE COUNT / DILUTION | FINDING | Dilutive ESOP-2022 spread present; paid-up steps 1,067.48 -> 1,069.16 next quarter; FY consolidated diluted EPS 21.60 vs basic 27.01 anomaly. |
| F11 RESERVES / NET WORTH TIE-OUT | FINDING | Other Equity omitted (blank rows 501/715); statutory net worth cannot be reconciled from the filing. |
| F12 SEGMENT FORENSICS | FINDING | Consolidated Woven Sacks assets +60% QoQ, liabilities +105% QoQ = debt-funded build; Label assets 17.0cr vs revenue 0.54cr idle. |
| F13 BOARD OUTCOME BEYOND RESULTS | FINDING | FY26 Board Report approved (AR imminent -> Role 6); AGM 25-Sep; new AOA; promoter-family MD reappt through commissioning window. |
| F14 NOTE DRAFTING INCONSISTENCIES | FINDING | Wrong annexure cross-ref (line 134); self-contradictory Other Matters para; "Year"-vs-"Quarter" title; duplicate row/labels; unnumbered items 6-9. |
| F15 ENTITY LIST DIFFS | FINDING | Malaysia LLP subsidiary deleted (dissolution); equity-method JV referenced (681/764) but never named; JV share fell 2.53 -> nil. |
| F16 PRESENTATION-SPECIFIC | N.A. | Doctype is a results filing, not an investor presentation. |
| F17 CONCALL SILENCE AUDIT | N.A. | No transcript in this filing; silence audit deferred to a concall document if one is filed. |

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/item ref | status word |
|------------|--------------|---------------|-------------|
| Re-appoint Prakash Hiralal Parekh as Managing Director for 3 years (promoter family) | effective 1-Nov-2026, AGM approval 25-Sep-2026 | line 93-95 / item 6 | board has approved (subject to shareholders) |
| Re-appoint Sandeep Shah as Non-Executive Independent Director for 5 years | w.e.f. 9-Aug-2026, AGM approval | line 98-100 / item 7 | board has approved (subject to shareholders) |
| Re-appoint Prakash Parekh (retire by rotation) as Director | at 42nd AGM 25-Sep-2026 | line 51-54 / item 3 | recommended to shareholders |
| Hold 42nd AGM via VC/OAVM | 25-Sep-2026 | line 72 / item 5a | to be held / scheduled |
| Record date for 42nd AGM | 18-Sep-2026 | line 86 / item 5e | shall be |
| Remote e-voting window | 19-Sep to 24-Sep-2026 | line 89-91 / item 5f | will commence |
| Register of Members closure | 19-Sep to 25-Sep-2026 | line 82 / item 5d | approved |
| Adopt new set of Articles of Association | at ensuing AGM 25-Sep-2026 | line 139 / item 11 | board adopted (subject to shareholders) |
| Board Report + Annexures for FY ended 31-Mar-2026 approved -> Annual Report | within weeks (Role 6 AR Deep Dive) | line 56 / item 4 | board has approved |
| ESOP allotment of 16,780 shares; paid-up increase | post-period (next quarter capital 1,069.16) | line 111-114, 132-135 / items 10, 10a | board has approved / allotted |

---

## CROSS-REFERENCE TO ACTIVE FLAGS
- FLAG-GATE0 (leverage): A3-08 (F12) segment liabilities +105% QoQ, total Rs 443.56cr.
- FLAG-CASH (INDETERMINATE): A3-05 (F8) zero current tax; A3-01 no OCF statement in this filing (results-only) — cash conversion stays INDETERMINATE, cannot resolve to PROCEED.
- FLAG-RPT / FLAG-PROMOTER: A3-09 (F13) promoter-family MD reappointment; relationship disclosure line 208.
- FLAG-GOVERNANCE / FLAG-DISCLOSURE: A3-10 (F14) drafting cluster; CFO resignation (item 8) atop Jan-2026 CS exit and 17-Jul-2026 internal-auditor withdrawal.
- FLAG-EMOAT: A3-11 (F15) unnamed JV (watch vs Saudi BOPP JV / dissolved Malaysia JV).

```yaml
stage: A3-forensics
company: "526717"
quarter: "q1fy27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "runs/526717-q1fy27/work/forensics_results_526717_q1fy27.md"
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
  F9: PASS
  F10: FINDING
  F11: FINDING
  F12: FINDING
  F13: FINDING
  F14: FINDING
  F15: FINDING
  F16: N.A.
  F17: N.A.
findings:
  - {id: "A3-01", check: "F1", line: "486,689,482", classification: "CONFIRMATORY-NEGATIVE", implication: "Discontinued-ops lines empty while Malaysia LLP dissolved; standalone current tax zero all periods"}
  - {id: "A3-02", check: "F2", line: "489,692", classification: "FORWARD-SIGNAL", implication: "PAT gap swings 3%->921%->104% of standalone PAT; Q1FY27 gap equals subsidiary PAT 934.56 exactly"}
  - {id: "A3-03", check: "F4", line: "628", classification: "FORWARD-SIGNAL", implication: "50.9% of consolidated PAT and 65% of assets unreviewed (KP Woven) amid auditor churn"}
  - {id: "A3-04", check: "F6", line: "93,72,139", classification: "FORWARD-SIGNAL", implication: "Dated commitments crystallise at 25-Sep-2026 AGM: MD/ID reappointments, new AOA"}
  - {id: "A3-05", check: "F8", line: "482,484", classification: "FORWARD-SIGNAL", implication: "Standalone current tax zero all periods on positive PBT; deferred-only charge = future cash-tax step-up"}
  - {id: "A3-06", check: "F10", line: "719", classification: "FORWARD-SIGNAL", implication: "Live ESOP dilution; paid-up steps to 1,069.16; FY consolidated diluted EPS 21.60 vs basic 27.01 anomaly"}
  - {id: "A3-07", check: "F11", line: "501,715", classification: "AMBIGUOUS", implication: "Other Equity omitted; statutory net worth cannot be reconciled from filing"}
  - {id: "A3-08", check: "F12", line: "769,774", classification: "FORWARD-SIGNAL", implication: "Woven Sacks assets +60% QoQ, liabilities +105% QoQ = debt-funded build; feeds leverage tripwire"}
  - {id: "A3-09", check: "F13", line: "56,93", classification: "FORWARD-SIGNAL", implication: "FY26 Board Report approved (AR imminent, Role 6); AGM special resolutions; promoter-family MD reappt"}
  - {id: "A3-10", check: "F14", line: "134,634", classification: "CONFIRMATORY-NEGATIVE", implication: "Wrong annexure cross-ref, self-contradictory Other Matters para, title/label defects = governance data point"}
  - {id: "A3-11", check: "F15", line: "107,681", classification: "AMBIGUOUS", implication: "Malaysia LLP subsidiary deleted; equity-method JV referenced but never named, share fell 2.53->nil"}
forward_signals: [A3-02, A3-03, A3-04, A3-05, A3-06, A3-08, A3-09]
ambiguous: [A3-07, A3-11]
commitments:
  - {commitment: "Re-appoint Prakash Hiralal Parekh as Managing Director for 3 years", implied_date: "2026-11-01", ref: "line 93-95 / item 6", status_word: "board has approved"}
  - {commitment: "Re-appoint Sandeep Shah as Independent Director for 5 years", implied_date: "2026-08-09", ref: "line 98-100 / item 7", status_word: "board has approved"}
  - {commitment: "Re-appoint Prakash Parekh (retire by rotation) as Director", implied_date: "2026-09-25", ref: "line 51-54 / item 3", status_word: "recommended"}
  - {commitment: "Hold 42nd AGM via VC/OAVM", implied_date: "2026-09-25", ref: "line 72 / item 5a", status_word: "to be held"}
  - {commitment: "Record date for 42nd AGM", implied_date: "2026-09-18", ref: "line 86 / item 5e", status_word: "shall be"}
  - {commitment: "Remote e-voting window", implied_date: "2026-09-19", ref: "line 89-91 / item 5f", status_word: "will commence"}
  - {commitment: "Adopt new Articles of Association", implied_date: "2026-09-25", ref: "line 139 / item 11", status_word: "board adopted"}
  - {commitment: "Board Report + Annexures FY26 approved (Annual Report forthcoming)", implied_date: "2026-09", ref: "line 56 / item 4", status_word: "board has approved"}
  - {commitment: "ESOP allotment 16,780 shares; paid-up increase to 1,069.16", implied_date: "2026-09-30", ref: "line 111-135 / items 10,10a", status_word: "board has approved"}
gate_a3: pass
blank_checks: []
```
