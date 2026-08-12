# A3 FORENSIC NOTES — Stallion India Fluorochemicals, Q1 FY27 (doctype: RESULTS)

Source extract: `extract_results_stallion_q1fy27.txt` (6 pages, 304 lines, header 1-56).
Ledger: `ledger_results_stallion_q1fy27.md`. Ledger reconciliation: 100% — every A2
row read verbatim at its cited A1 line before judging. Unit = Lakhs; x0.01 -> Rs Cr
(not applied; values quoted as-extracted).

Scope note: doctype = results, so F1-F15 apply and F16/F17 are N.A. per the
checklist's doctype-applicability rule. Every check is statused; no blanks.

Carry-forward flags from A1/A2 all independently re-verified at their lines below:
OCR reconciliation on pp.3-4, DESIGNATION_MISMATCH (l.107 vs l.150), DIRECTOR_CHANGE
(item f), two ZERO_STANDING rows (l.82, IPO row d), no consolidated/segment/EoM/going-
concern content (all confirmed absent).

---

## FINDINGS TABLE

| id | check | ledger row ref | line | verbatim quote | classification | forward implication |
|----|-------|----------------|------|----------------|----------------|---------------------|
| A3-01 | F6 | Sec 4, IPO row (c) / Note 5 | 130-131 | "Refrigerant debulking & blending facility ("Mambattu, Andhra Pradesh") ... 2,117.53 \| 1,100.75 \| 1,016.78" | FORWARD-SIGNAL | Refrigerant (R-32-relevant) facility is the LEAST-deployed IPO object: only 52.0% of the Rs 2,117.53L earmark spent, Rs 1,016.78L idle. Notion monitorable says "R-32 commissioning ~4 months away," yet half the earmarked capex is unspent and the filing gives no commissioning date. Spend-vs-timeline tension -> A4 management question. |
| A3-02 | F6 | Sec 4 narrative / Note 5 | 136-139 | "the Company proposed to utilise the IPO proceeds for acquisition of approximately 2 acres of land at Khalapur ... in lieu of the originally proposed warehouse construction. The revised utilisation resulted in a differential cost of Rs 0.13 crore" | FORWARD-SIGNAL | IPO object-of-use changed by Special Resolution (30 May 2026); Khalapur capex row (b) already overspent (2,661.77 vs 2,574.66 = 103.4%), so the land pivot is substantially executed. Rs 0.13cr figure confirmed by A1 visual read (OCR misread the Rs symbol as a leading digit). Track land title/possession at AR. |
| A3-03 | F6 | Sec 4, IPO row (a) | 127 | "Funding incremental working capital requirements ... 9,441.80 \| 10,270.53 \| (828.73)" | FORWARD-SIGNAL | Working-capital object overspent to 108.8% of plan (Rs 828.73L over earmark). Post-IPO WC intensity rising faster than provisioned; combined with row (c) underspend it signals reallocation of cash toward WC and away from the refrigerant build. Ask A4 to probe WC drivers (inventory/receivables) at AR. |
| A3-04 | F6 | Sec 1, items d/e | 38-41 | "AGM ... scheduled to be held on Monday, 21st September, 2026 ... book closure ... shall be from 15th September, 2026 to 21st September, 2026" | FORWARD-SIGNAL | Dated calendar commitments. No dividend recommended in the board outcome (consistent with reinvestment thesis). Book-closure set for AGM record, not a dividend. |
| A3-05 | F13 | Sec 1, items b/c | 34-37 | "Approved the Directors' Report, along with its annexures ... Approved the Management Discussion and Analysis Report and the Corporate Governance Report for the financial year ended" | FORWARD-SIGNAL | Directors' Report + MD&A + CG Report all approved this meeting -> full FY26 Annual Report drops within weeks. Schedule a Role 6 AR Deep Dive; it is the first AR as a listed company and the first venue with segment/related-party/capex-progress detail this filing lacks. |
| A3-06 | F13 | Sec 1, item f / DIRECTOR_CHANGE | 42-45 | "Regularization of Ms. Swati Ghosh (DIN: 08789050) from Additional Independent Director to Woman Independent Director" | FORWARD-SIGNAL | Board putting the mandatory Woman Independent Director slot to shareholder vote at AGM. Regularization (not removal) = continuity, mild positive governance signal. No term-date stated -> A4 should confirm appointment tenure against the R-32 commissioning window. |
| A3-07 | F14 | Sec 2, rows 2 & 3 / DESIGNATION_MISMATCH | 107 & 150 | "Managing Director & CEO" (l.107) vs "Managing Director & CFO" (l.150) | AMBIGUOUS | Same person (Shazad Rustomji), same DIN 01923432, same filing package, titled CEO on the results page and CFO on the notes page. Either (i) the promoter-MD is also the CFO = no independent finance head for a company deploying ~Rs 145cr of IPO proceeds (controls concern), or (ii) a drafting/version-control lapse in a statutory filing. Direction uncertain -> A4 management question: who is the CFO of record? |

---

## CHECKLIST SCORECARD (all 17 statused)

| Check | Status | One-line basis |
|-------|--------|----------------|
| F1 ZERO-VALUE STANDING LINES | PASS | Both ZERO_STANDING rows examined and benign. L.82 "Adjustment of tax relating to earlier periods" = dash in all four periods -> clean, no prior-year tax reopenings (confirmatory-negative). IPO row (d) l.132 "General Corporate Purposes ... 340.88 \| 340.88 \| -" = fully utilised, nil unutilised. No exceptional-items / profit-on-sale / impairment standing lines present to anticipate. |
| F2 STANDALONE vs CONSOLIDATED | N.A. | No consolidated financials in filing; grep "consolidat\|subsidiar" = 0 hits (ledger sec 6). Nothing to decompose. |
| F3 SHELL-ENTITY DETECTION | N.A. | Single standalone entity, no subsidiaries/consolidation to compare cost lines against. |
| F4 UNAUDITED CONTRIBUTION RATIO | N.A. | Auditor's report has no Other Matters paragraph (l.129 ledger) and names no component auditors/JVs/associates. Nothing rests on unreviewed numbers. |
| F5 GOING CONCERN / EoM SCOPE | PASS | No Emphasis of Matter, no Other Matters, no going-concern language (ledger sec 5, l.128-130; re-read auditor paras 1-4, l.172-205). Auditor conclusion unmodified (l.198-205). Confirmatory-negative; no prior-quarter extract supplied for verbatim diff. |
| F6 FORWARD-COMMITMENT MINING | FINDING | Hits: "proposed to utilise" (l.137), "scheduled to be held" (l.39), "shall be from" (l.40), "has received" (l.124). Findings A3-01..A3-04. See commitment register. |
| F7 HEDGE PHRASE MINING | PASS | Swept notes for hedge lexicon. Only Note 6 "regrouped, rearranged and reclassified where necessary" (l.140) — routine comparability boilerplate, not a newly-added hedge on revenue lumpiness or customer concentration. No pre-emptive legal-cover language introduced. |
| F8 TAX FORENSICS | PASS | ETR: Q1FY27 25.10%, Q1FY26 25.24%, FY26 25.67% — all at statutory 25.17%. Q4FY26 34.40% is elevated but is an audited balancing figure (Note 4, l.122-123) reflecting the year-end deferred-tax true-up (Q4 deferred tax 328.93, l.83). Deferred tax is a charge every period (no persistent credit -> no DTA-depletion step-up risk). Earlier-period tax adjustment nil in all periods (l.82). |
| F9 OCI FORENSICS | PASS | Current-quarter remeasurement of DB plans +1.87 (l.88) is immaterial and does not exceed the full prior year. The larger Q4FY26 figure (+41.80) is the annual year-end actuarial revaluation embedded in the FY26 balancing quarter (Note 4), not a Q1FY27 assumption change. Verify discount-rate assumptions at the AR as routine. |
| F10 SHARE COUNT / DILUTION | PASS | Paid-up jumps Q1FY26 7,932.53 -> 11,608.57 (Q4FY26/Q1FY27), traced cleanly to the IPO fresh issue (Note 5, l.124; +3,676.04L = 3.676cr shares at Rs10 face). Paid-up flat QoQ (IPO complete). Basic = Diluted EPS in every period (1.60/1.60, 1.33/1.33, 1.15/1.15, 5.34/5.34, l.93-94) -> zero dilutive overhang. |
| F11 RESERVES / NET WORTH TIE-OUT | PASS | Other Equity + Paid-up = Net Worth to Rs 0.01L rounding in all four periods (e.g. Q1FY27 58,309.75 + 11,608.57 = 69,918.32 vs 69,918.33, l.95-97). Other-Equity roll Q4FY26 56,451.78 + Q1FY27 TCI 1,857.98 = 58,309.76 vs 58,309.75 -> ties, confirming no dividend/no other reserve movement. |
| F12 SEGMENT FORENSICS | N.A. | Single business segment (industrial gases), Ind AS 108 not applicable per Note 3 (l.120-121). No segment table exists to trend. |
| F13 BOARD OUTCOME BEYOND RESULTS | FINDING | AR components approved -> AR imminent (A3-05); Swati Ghosh regularization to AGM (A3-06); AGM 21 Sep / book closure set (A3-04). All 7 agenda items assessed (ledger sec 1). |
| F14 NOTE-DRAFTING INCONSISTENCIES | FINDING | DESIGNATION_MISMATCH CEO(l.107)/CFO(l.150), same DIN (A3-07). Also minor: covering letter says report issued "with an unmodified opinion" (l.46-47) whereas a limited review yields an unmodified conclusion, not an opinion (auditor "do not express an audit opinion", l.197) — loose wording, immaterial. Context (non-finding): statutory results PDF produced via free web tool Online2PDF.com with a corrupted embedded text layer (A1 header) — soft reporting-control signal, mechanical only. |
| F15 ENTITY LIST DIFFS | N.A. | No consolidation/entity list in a standalone-only filing; nothing to diff. Company rename Private Ltd -> Ltd is the historical IPO conversion, disclosed as "(Formerly known as...)", not a consolidation-scope change. |
| F16 PRESENTATION-SPECIFIC | N.A. | Doctype = results, not a presentation. |
| F17 CONCALL SILENCE AUDIT | N.A. | Doctype = results, not a transcript. Standing monitorable (R-32 commissioning) silence is instead surfaced under F6/A3-01 from the IPO-utilisation table. |

Status line: **7 PASS / 3 FINDING / 7 N.A.** (F1,F5,F7,F8,F9,F10,F11 PASS; F6,F13,F14 FINDING; F2,F3,F4,F12,F15,F16,F17 N.A.).

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/turn ref | status word |
|------------|--------------|---------------|-------------|
| AGM to be convened | 21 Sep 2026, 4:00 PM | l.38-39 (item d) | approved (draft notice) |
| Book closure for AGM | 15-21 Sep 2026 | l.40-41 (item e) | approved / "shall be" |
| Regularize Ms. Swati Ghosh as Woman Independent Director (shareholder vote) | at AGM 21 Sep 2026 | l.42-45 (item f) | proposed / to be approved |
| Acquire ~2 acres land at Khalapur in lieu of warehouse | approved via SR 30 May 2026 | l.136-139 (Note 5) | underway (Khalapur capex 103% deployed) |
| Deploy remaining IPO proceeds into Mambattu refrigerant (R-32) facility | no date disclosed | l.130-131 (row c) | in process (52% deployed, Rs 1,016.78L idle) |
| File full FY26 Annual Report (Directors'/MD&A/CG reports approved) | within weeks | l.34-37 (items b/c) | completed (approved) -> AR to follow |

---

## FORWARD-SIGNAL / AMBIGUOUS SUMMARY FOR A4 (seed questions)

FORWARD-SIGNAL: A3-01 (R-32/Mambattu 52% deployed vs "commissioning 4 months away"),
A3-02 (Khalapur land pivot), A3-03 (WC object overspent 108.8%), A3-04 (AGM/no dividend),
A3-05 (AR imminent -> Role 6 event), A3-06 (Swati Ghosh regularization, tenure unstated).
AMBIGUOUS: A3-07 (CEO/CFO designation mismatch — who is CFO of record?).

Quality-of-earnings note attached to A3-01/A3-03 for A4: Other income jumped to 322.97
(Q1FY27) from 7.37 (Q1FY26) at l.69 — FD interest on unutilised IPO cash. As proceeds
deploy (esp. the Rs 1,016.78L still idle), this non-operating tailwind fades; strip it to
see clean operating PBT growth.

---

## GATE A3
PASS — all 17 checks statused (7 PASS / 3 FINDING / 7 N.A.), every FINDING line-cited,
ledger reconciled 100%.

```yaml
stage: A3-forensics
company: "stallion"
quarter: "q1fy27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/stallion-q1fy27/work/forensics_stallion_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: PASS
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: PASS
  F6: FINDING
  F7: PASS
  F8: PASS
  F9: PASS
  F10: PASS
  F11: PASS
  F12: N.A.
  F13: FINDING
  F14: FINDING
  F15: N.A.
  F16: N.A.
  F17: N.A.
findings:
  - {id: "A3-01", check: "F6", line: "130-131", classification: "FORWARD-SIGNAL", implication: "Mambattu refrigerant (R-32) facility least-deployed IPO object: 52% spent, Rs 1,016.78L idle vs 'commissioning ~4 months away' — spend/timeline tension"}
  - {id: "A3-02", check: "F6", line: "136-139", classification: "FORWARD-SIGNAL", implication: "IPO object changed by SR 30-May-2026 to Khalapur land in lieu of warehouse; already overspent (103%), pivot executed; Rs 0.13cr differential"}
  - {id: "A3-03", check: "F6", line: "127", classification: "FORWARD-SIGNAL", implication: "Working-capital object overspent to 108.8% of plan; post-IPO WC intensity rising, cash reallocated away from refrigerant build"}
  - {id: "A3-04", check: "F6", line: "38-41", classification: "FORWARD-SIGNAL", implication: "AGM 21-Sep-2026 and book closure set; no dividend recommended (reinvestment-consistent)"}
  - {id: "A3-05", check: "F13", line: "34-37", classification: "FORWARD-SIGNAL", implication: "Directors'/MD&A/CG reports approved -> first listed-company Annual Report drops within weeks; schedule Role 6 AR Deep Dive"}
  - {id: "A3-06", check: "F13", line: "42-45", classification: "FORWARD-SIGNAL", implication: "Swati Ghosh regularized to Woman Independent Director at AGM; continuity signal, tenure/term date not stated"}
  - {id: "A3-07", check: "F14", line: "107 & 150", classification: "AMBIGUOUS", implication: "Same DIN 01923432 signs as MD & CEO (p.3) and MD & CFO (p.4); either no independent CFO for Rs~145cr IPO deployment or a filing control lapse — confirm CFO of record"}
forward_signals: ["A3-01", "A3-02", "A3-03", "A3-04", "A3-05", "A3-06"]
ambiguous: ["A3-07"]
commitments:
  - {commitment: "Convene AGM", implied_date: "2026-09-21", ref: "l.38-39 item d", status_word: "approved"}
  - {commitment: "Book closure for AGM", implied_date: "2026-09-15/2026-09-21", ref: "l.40-41 item e", status_word: "approved"}
  - {commitment: "Regularize Swati Ghosh as Woman Independent Director", implied_date: "2026-09-21 (AGM)", ref: "l.42-45 item f", status_word: "proposed"}
  - {commitment: "Acquire ~2 acres land at Khalapur in lieu of warehouse", implied_date: "approved SR 2026-05-30", ref: "l.136-139 Note 5", status_word: "underway"}
  - {commitment: "Deploy remaining IPO proceeds into Mambattu refrigerant (R-32) facility", implied_date: "none disclosed", ref: "l.130-131 row c", status_word: "in-process"}
  - {commitment: "File full FY26 Annual Report", implied_date: "within weeks of 2026-08-12", ref: "l.34-37 items b/c", status_word: "completed"}
gate_a3: pass
blank_checks: []
```
