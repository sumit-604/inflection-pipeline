# A3 FORENSIC NOTES — DSSL (Dynacons Systems & Solutions Ltd) — Q1 FY27 RESULTS FILING

Doctype: **results** (limited-review, unaudited Standalone + Consolidated, quarter ended 30-Jun-2026)
Company: Dynacons Systems & Solutions Ltd (BSE 532365 / NSE DSSL)
Source A1 extract: `extract_results_dssl_q1fy27.txt` (409-line body + appended corrected page-5 block, lines 411-560)
Source A2 ledger: `ledger_results_dssl_q1fy27.md`
Ledger reconciliation: **100%** — all 8 ledger sections read at cited lines; count-test categories (5 notes / 2 agenda / 11 auditor paras / 3 entities / 36 line-items / 13 segment rows / 5 signatures) all verified against the extract.

NUMERIC AUTHORITY NOTE: per task instruction, ALL page-5 numeric values are taken from the CORRECTED OCR-fallback block (lines 431-461, Rs lakh; lines 464-493, Rs crore), NOT the scrambled -layout portion (lines 237-312). Consolidated LRR paragraph text taken from the recovered list (lines 513-558). Unit = Rs lakh as filed; ÷100 to Rs crore.

---

## DERIVED FORENSIC ANCHORS (Rs lakh unless stated; CON = consolidated, STD = standalone)

| Metric (CONSOLIDATED) | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Source lines |
|---|---:|---:|---:|---:|---|
| Net Sales | 31,368.83 | 40,244.85 | 32,885.17 | 1,42,428.34 | 433 |
| Finance Costs | 720.40 | 673.87 | 494.15 | 2,320.19 | 439 |
| Depreciation | 808.92 | 626.88 | 147.67 | 1,453.03 | 440 |
| PBT | 2,645.19 | 2,543.08 | 2,628.09 | 11,392.13 | 443 |
| Net Profit | 1,979.55 | 1,899.03 | 1,964.51 | 8,481.24 | 445 |
| **Operating EBITDA** (PBT+Dep+Fin−OthInc) | **4,018.87** | **3,630.81** | **3,177.96** | **14,592.83** | ties segment total ln 377 |
| **Op EBITDA margin** | **12.81%** | **9.02%** | **9.66%** | **10.25%** | derived |

- Revenue YoY (CON): 31,368.83 vs 32,885.17 = **−4.61%**. (STD −5.32%.)
- Depreciation YoY: 808.92 vs 147.67 = **×5.48 (+447.8%)**.
- Finance cost YoY: 720.40 vs 494.15 = **+45.8%**.
- Op EBITDA margin YoY: 9.66% → 12.81% = **+315 bps**, yet PBT essentially flat (2,628.09 → 2,645.19 = +0.65%): the entire EBITDA-margin gain was consumed below the line by the depreciation + finance-cost step-up. **Absorption-deficit signature.**
- FY26 op EBITDA margin 10.25% ties exactly to Notion baseline — method validated.

---

## FINDINGS TABLE

| id | check | ledger row ref | line | verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| F1-01 | F1 | §2 rows 19-20, 22 | 448, 450 | "A(i) - Foreign Exchange Gains or loss ... 0.00 0.00 0.00 0.00"; "B(i) Items that will be reclassified to profit or loss [all nil/dash in source]" | AMBIGUOUS | A foreign subsidiary (Dynacons PTE, Singapore) exists yet the reclassifiable-OCI / FX line where foreign-currency-translation reserve (FCTR) would sit is nil across all four periods, both books. Either FX translation is immaterial or it is not being surfaced separately. A4 to ask where FCTR on the Singapore sub is carried. |
| F2-01 | F2 | §7 PAT delta; §4b Other Matter | 445, 453, 189 | CON−STD PAT: Q1FY27 +23.21, Q4FY26 −13.88, Q1FY26 +3.34 (lakh) | AMBIGUOUS | Subsidiary net contribution flipped from a **−13.88 drag in Q4FY26 to +23.21 in Q1FY27** and is ~7× the Q1FY26 contribution (3.34→23.21). Ties to auditor's Rs23.22 lakh subsidiary PAT (ln 189). Lumpy sub earnings around the Cybercons name; mechanical gap-swing 1.9pp of STD PAT (below the 5pp threshold) but the sign flip warrants a question. |
| F3-01 | F3 | §2 rows 9-10; §7 | 439, 440, 433 | "d) Finance Costs | 720.40 ... || 720.40"; "e) Depreciation ... | 808.92 ... || 808.92" | FORWARD-SIGNAL | Finance Costs and Depreciation are **identical standalone and consolidated in every period** (subsidiaries carry zero debt and zero fixed assets), while subsidiaries DO carry revenue (+249.50), materials (+179.68) and employees (+42.30). Therefore the entire ×5.5 depreciation jump and +46% finance cost sit in the **parent book** — an as-a-service / Ind AS 116 lease-capex build in the parent while consolidated revenue fell −4.6%. ROCE compresses until the leased/as-a-service assets generate revenue. |
| F6-01 | F6 | Note 5 | 322-328 | "the Company has identified Technology Workforce Augmentation Services as a focus business segment from the existing services provided by the Company" | FORWARD-SIGNAL | Management is publicly flagging TWAS as a growth focus — a dateable strategic-intent commitment to track for delivery. (But see F12-01: the segment's revenue is shrinking YoY.) |
| F6-02 | F6 | Board letter; Note 3 | 43, 320 | "The Interim Dividend shall be paid on and from, Thursday, August 27, 2026"; "cash outgo on account of interim dividend will be Rs.63.69 lakhs" | NEUTRAL-FACT | Dated capital-return commitment (record date 19-Aug-26, pay 27-Aug-26). Rs63.69 lakh ÷ Rs0.50 = 1,27,38,000 shares — ties to paid-up 1,273.71 lakh ÷ 10. Routine. |
| F10-01 | F10 | §2 row 35 | 459 | "Paid up equity share capital | 1,273.71 1,273.71 1,272.53 1,273.71" | AMBIGUOUS | Paid-up capital rose Rs1.18 lakh (≈11,800 shares) between Q1FY26 (1,272.53) and Q4FY26 (1,273.71); no corporate-action note in this filing explains it. Basic-vs-diluted EPS spread is now nil (15.36/15.36 STD; 15.54/15.54 CON) — negligible live dilution. A4 to identify the instrument (likely ESOP/warrant conversion). |
| F12-01 | F12 | Note 5; §6 segment | 322-331, 370 | "The previous period's figures have accordingly been restated"; TWAS Segment Revenue 307.77 (Q1FY27) vs 387.93 (Q1FY26 restated) | FORWARD-SIGNAL / AMBIGUOUS | New reportable segment "Technology Workforce Augmentation Services" introduced this quarter with prior-period comparatives restated; the restatement basis is stated (carved from existing System Integration services) but NOT quantified as a bridge. The segment flagged as a "focus" growth area is itself **−20.7% YoY** (387.93→307.77) — the growth narrative and the number diverge. |
| F12-02 | F12 | §6 row 13 | 386-389 | "it is currently not practicable to provide segment disclosures relating to total assets and total liabilities" | CONFIRMATORY-NEGATIVE | Segment assets & liabilities standing non-disclosure. Cannot test the F12 equity-funded-build / capex-proxy question by segment; combined with the absent balance sheet this leaves the capex build (F3-01) unquantifiable from the filing. |
| F14-01 | F14 | §2 row 33; reconciliation flag | 457, 497-509 | "[CON only] TCI for period attrib to Shareholders of the Company ** SEE FLAG ** ... 1,966.53" | AMBIGUOUS | Casting/integrity failure on a **restated prior-year comparative**: CON Q1FY26 TCI-attributable-to-Shareholders filed at 1,966.53 does not tie — PAT-Shareholders 1,961.74 + OCI-Shareholders (−4.79) = 1,956.95 (Δ 9.58); and 1,966.53 + NCI 2.77 = 1,969.30 vs the page's own CON Q1FY26 Total comprehensive income 1,959.72 (Δ 9.58, same amount). Isolated to one cell; the Total comprehensive income line itself ties. A4 to raise as a management/accounting-quality question. |

---

## CHECKLIST SCORECARD (all 17; GATE A3 = every check has one status)

| # | Status | One-line basis |
|---|---|---|
| **F1** | **FINDING** | Zero-standing OCI template lines read (FX gain/loss nil all periods ln 448; B(i) reclassifiable nil ln 450; OCI-to-NCI nil ln 456). FCTR-shaped nil despite a Singapore subsidiary → F1-01. |
| **F2** | **FINDING** | S-vs-C decomposed on Revenue/EBITDA-components/PAT all four periods. PAT gap +23.21/−13.88/+3.34/+3.68; sign flip and 7× YoY subsidiary swing → F2-01. Mechanical 5pp-of-STD-PAT threshold NOT breached (max swing 1.9pp), finding raised on the sign flip + Cybercons context. |
| **F3** | **FINDING** | Cost-of-materials, employee, other-exp DIFFER S-vs-C (subs operate); Finance Costs + Depreciation + Changes-in-Inv IDENTICAL S=C → subs have zero debt/fixed assets; entire ×5.5 dep + 46% finance step-up is parent-book (absorption deficit) → F3-01. |
| **F4** | **PASS** | Other Matter (ln 186-197): 2 unaudited subsidiaries, aggregate revenue Rs249.50 lakh, PAT Rs23.22 lakh = **1.17% of CON PAT** (1,979.55) — below 10% threshold. Foreign sub is management-furnished (only Ind-AS conversion adjustments audited); domestic (Cybercons) directly reviewed. Level immaterial; YoY absolute jump captured under F2-01. |
| **F5** | **PASS** | No Going Concern, no Emphasis of Matter in either LRR. Consolidated carries a standard non-modifying **Other Matter** only; "Our opinion on the Statement is not modified in respect of the above matter" (ln 198, 552). Prior-quarter EoM diff not possible (PRIOR_LEDGER_UNAVAILABLE) — none to diff since none present. |
| **F6** | **FINDING** | Phrase-mine of notes/board letter: "shall be paid" (dividend, ln 43); "will be Rs.63.69 lakhs" (ln 320); "has identified ... as a focus business segment" (ln 322); "approved the following matters" (ln 37); "have accordingly been restated" (ln 331). Commitments registered → F6-01/F6-02. |
| **F7** | **PASS** | Lexicon sweep: only hits are boilerplate — "subject to limited review" (Note 2, ln 318) and "to the extent applicable" (SEBI-circular para, ln 163/538). No NEW business hedge on revenue lumpiness / customer concentration. |
| **F8** | **PASS** | ETR by period vs statutory 25.17%: CON 25.16% / 25.33% / 25.25% / 25.55%; STD 25.30% / 24.97% / 25.25% / 25.48% — all in line. No separate deferred-tax line, no "tax relating to earlier years" line. Clean. |
| **F9** | **PASS** | Current-quarter OCI immaterial (CON total 4.87 lakh; remeasurement 0.21). No single-quarter swing exceeding prior FY *in this quarter* (the large 38.28 actuarial remeasurement sits in Q4FY26, a comparative, not this filing's quarter). TCI attribution casting error routed to F14. |
| **F10** | **FINDING** | Paid-up +Rs1.18 lakh YoY (1,272.53→1,273.71) unexplained by any note; diluted-vs-basic spread now nil → F10-01. |
| **F11** | **N.A.** | No balance sheet and no Other Equity disclosed (Q1 limited-review filing; Reg 33 provides balance sheet only at H1/FY). Net-worth tie-out cannot be performed. **This is also where the absent receivables ageing / ECL is recorded — cannot be cleared from this document.** |
| **F12** | **FINDING** | New segment TWAS with restated (un-bridged) comparatives; "focus" segment revenue −20.7% YoY (F12-01); segment assets & liabilities not disclosed (F12-02). |
| **F13** | **PASS** | Board Outcome carried exactly 2 items: (1) results, (2) interim dividend Rs0.50/sh, cash outgo Rs63.69 lakh. Item 2 fully assessed (ties to paid-up & F6-02). **No AR/annual-accounts approval, no AGM notice, no director appointment/term dates, no auditor change, no capital-raising enabling resolution** — nothing forward beyond results; no under-assessed agenda item. |
| **F14** | **FINDING** | Casting/integrity: CON Q1FY26 TCI-to-Shareholders 1,966.53 fails to tie by 9.58 lakh on a restated prior-year comparative → F14-01. Minor entity-name inconsistencies noted (see below). |
| **F15** | **PASS** | Entity list = 1 holding + 2 subsidiaries: Dynacons PTE (foreign) and **Cybercons Infosec Pvt Ltd — labelled "Subsidiary Company" (ln 175, 543), consolidated line-by-line, its result inside the Rs23.22 lakh sub aggregate**. NO reclassification, NO restatement, NO EoM/qualification touching Cybercons in this document → **HARD-OVERRIDE trigger NOT fired.** Prior-quarter diff not possible (PRIOR_LEDGER_UNAVAILABLE) — A4 must diff vs Q4FY26 to fully clear classification continuity. |
| **F16** | **N.A.** | Doctype = results filing, not a presentation deck. (Per agent doctype rule.) |
| **F17** | **N.A.** | Doctype = results filing, no concall transcript in scope. (Per agent doctype rule.) |

GATE A3: every F1-F17 carries exactly one status. No blanks. **PASS.**

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/line ref | status word |
|---|---|---|---|
| Interim dividend Rs0.50/share paid, cash outgo Rs63.69 lakh | pay 27-Aug-2026; record date 19-Aug-2026 | Board letter ln 43-46; Note 3 ln 320 | approved / declared |
| TWAS made a reportable "focus business segment," comparatives restated | this quarter (Q1FY27) onward | Note 5 ln 322-331 | initiated |
| Prior-period figures regrouped/re-arranged "wherever necessary" | this quarter | Note 4 ln 321-322 | completed |

---

## MINOR / CUMULATIVE (F14 governance data points, individually immaterial)
- Entity-name variance: "Dynacons Systems **and** Solutions Ltd" (LRR) vs "Dynacons Systems **&** Solutions Limited" (statement); "Cybercons Infosec Private Limited" (LRR ln 175) vs "CYBERCONS INFOSEC PVT LTD" (task/prior work).
- Statement header typo "Stndalone" (ln 221); "Unallocable Expences" (ln 380).
- WTD signature blocks differ: "Whole-time Director" (ln 342) vs "Whole-time Director & C[EO]" (ln 395).
- None material alone; logged as accounting-hygiene texture supporting the F14-01 casting finding.

---

## THESIS-BROKEN TRIGGER STATUS (as this document can evidence)

| # | Trigger | Reading from this filing | Status |
|---|---|---|---|
| 1 | EBITDA margin <11% (near 9%) for **two consecutive** quarters (green ≥11% / red <9%) | CON op EBITDA margin Q1FY27 = **12.81% (GREEN)**; Q4FY26 was 9.02% (single borderline-red quarter). Not two consecutive. | **NOT FIRED** (current qtr green; one-quarter dip only) |
| 2 | Debtor days >160 with 1-2yr overdue bucket widening on frozen Rs0.14cr ECL | No balance sheet, no receivables ageing, no ECL disclosure in filing. | **CANNOT EVIDENCE / UNKNOWN** |
| 3 | RBI Rs750.82cr order cancelled / materially slipped | No order-book or RBI-order disclosure anywhere in filing; no cancellation language. | **NOT FIRED (no adverse evidence); go-live date UNKNOWN** |
| 4 | HARD OVERRIDE: any Cybercons consolidated restatement → AVOID | Cybercons consolidated as "Subsidiary Company," no restatement/reclassification/EoM touching it. | **NOT FIRED** |

## MONITORING CHECKLIST STATUS (as this document can evidence)

| # | Monitorable | Reading | Status |
|---|---|---|---|
| 1 | EBITDA margin (green ≥11%, red <9% two qtrs) | CON op EBITDA margin 12.81% | **GREEN** |
| 2 | Trade receivables / ECL & debtor days | Not disclosed (no balance sheet/ageing) | **UNKNOWN — cannot clear** |
| 3 | RBI order dated go-live | Not disclosed | **UNKNOWN** |
| 4 | Order book / book-to-bill (green >1.3x) | Not disclosed; note revenue −4.6% YoY (CON) | **UNKNOWN (with a YoY revenue-decline caution)** |
| 5 | Annuity mix / leverage D/E (green <0.3x, red >0.4x) | D/E not computable (no balance sheet). Finance costs +45.8% YoY and depreciation ×5.5 (F3-01) point directionally to rising lease/debt load. | **UNKNOWN — directional caution (leverage rising)** |
| 6 | Cybercons classification (red = restatement or related-party balances re-accelerating) | No restatement/reclassification in doc; related-party balances not disclosed (no balance sheet). | **GREEN on classification; related-party balances UNKNOWN** |

## EXPLICIT DISCLOSURE ABSENCES (for A4 to record — cannot be cleared from this filing)
- No balance sheet (Q1 Reg 33) → net worth, D/E, receivables, ECL, related-party balances all UNKNOWN.
- No receivables ageing / debtor-days (monitorable 2 cannot be cleared).
- No order-book / book-to-bill / RBI-order go-live disclosure (monitorables 3, 4).
- No segment assets & liabilities (F12-02).
- No cash flow statement (Q1; next reading at H1/Q2).

---

```yaml
stage: A3-forensics
company: "DSSL"
quarter: "Q1 FY27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/dssl-q1fy27/work/forensics_dssl_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: FINDING
  F3: FINDING
  F4: PASS
  F5: PASS
  F6: FINDING
  F7: PASS
  F8: PASS
  F9: PASS
  F10: FINDING
  F11: N.A.
  F12: FINDING
  F13: PASS
  F14: FINDING
  F15: PASS
  F16: N.A.
  F17: N.A.
findings:
  - {id: "F1-01", check: "F1", line: "448,450", classification: "AMBIGUOUS", implication: "FX/reclassifiable OCI nil across all periods despite a Singapore subsidiary — FCTR location unexplained"}
  - {id: "F2-01", check: "F2", line: "445,453,189", classification: "AMBIGUOUS", implication: "Subsidiary PAT contribution flipped -13.88 (Q4) to +23.21 (Q1) and 7x YoY; lumpy sub earnings near the Cybercons name"}
  - {id: "F3-01", check: "F3", line: "439,440,433", classification: "FORWARD-SIGNAL", implication: "Finance cost + depreciation identical S=C -> all x5.5 dep + 46% finance step-up is parent-book; absorption deficit vs -4.6% revenue, ROCE compression until as-a-service assets earn"}
  - {id: "F6-01", check: "F6", line: "322", classification: "FORWARD-SIGNAL", implication: "TWAS flagged a focus growth segment — dateable strategic-intent commitment to track"}
  - {id: "F6-02", check: "F6", line: "43,320", classification: "NEUTRAL-FACT", implication: "Dated interim-dividend payout Rs63.69 lakh, 27-Aug-26; routine capital return"}
  - {id: "F10-01", check: "F10", line: "459", classification: "AMBIGUOUS", implication: "Paid-up +Rs1.18 lakh YoY unexplained by any note; identify the corporate action (ESOP/warrant)"}
  - {id: "F12-01", check: "F12", line: "322-331,370", classification: "FORWARD-SIGNAL", implication: "New TWAS segment, un-bridged restated comparatives; the focus segment is -20.7% YoY — narrative vs number divergence"}
  - {id: "F12-02", check: "F12", line: "386-389", classification: "CONFIRMATORY-NEGATIVE", implication: "Segment assets/liabilities not disclosed; capex build unquantifiable by segment"}
  - {id: "F14-01", check: "F14", line: "457,497", classification: "AMBIGUOUS", implication: "Restated prior-year CON Q1FY26 TCI-to-Shareholders 1,966.53 fails to tie by 9.58 lakh; accounting-quality/management question"}
forward_signals: ["F3-01", "F6-01", "F12-01"]
ambiguous: ["F1-01", "F2-01", "F10-01", "F12-01", "F14-01"]
commitments:
  - {commitment: "Interim dividend Rs0.50/share, cash outgo Rs63.69 lakh", implied_date: "2026-08-27 (record 2026-08-19)", ref: "board letter ln43; Note 3 ln320", status_word: "approved"}
  - {commitment: "TWAS made a reportable focus business segment, comparatives restated", implied_date: "Q1FY27 onward", ref: "Note 5 ln322-331", status_word: "initiated"}
  - {commitment: "Prior-period figures regrouped/re-arranged wherever necessary", implied_date: "Q1FY27", ref: "Note 4 ln321-322", status_word: "completed"}
gate_a3: pass
blank_checks: []
```
