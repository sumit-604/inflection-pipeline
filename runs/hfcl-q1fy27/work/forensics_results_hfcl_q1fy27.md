# FORENSIC NOTES — HFCL Q1 FY27 (doctype: RESULTS filing)

Agent: A3 Forensic Notes | Model: claude-opus-4-8
Source extract: `extract_results_hfcl_q1fy27.txt` (7 pages, 507 lines)
Ledger: `ledger_results_hfcl_q1fy27.md` | Reconciliation: 100% (every ledger row read at its cited line)
Doctype applicability: F1-F15 apply; F16 (presentation) and F17 (concall) = N.A.

All 11 `ZERO_STANDING` rows, and the `AUDITOR_SCOPE_LIMITATION`,
`UNAUDITED_MANAGEMENT_FURNISHED`, `SIGNATURE_BLOCK_INCOMPLETE`,
`ENTITY_LIST_DISCREPANCY`, `MATERIAL_CAPEX`, `CAPITAL_RAISE` flags were read
verbatim before judging. No prior-quarter extract was supplied, so every
quarter-over-quarter verbatim diff (EoM language, entity list) is marked as a
gap where it applies, never silently skipped.

---

## FINDINGS TABLE

| id | check | ledger row ref | line | verbatim quote | classification | forward implication |
|----|-------|----------------|------|----------------|----------------|---------------------|
| A3-01 | F2 | P&L IX (line 371-372) | 371 | "179.21 ... 245.64" (standalone vs consol PAT, Jun-26) | FORWARD-SIGNAL | S-vs-C PAT gap swung from 3.9% of standalone PAT (Q4FY26) to 37.1% (Q1FY27), +33.2pp. NCI jumped 5.95 -> 17.04 QoQ. Subsidiary/foreign earnings (HTL + foreign OFC subs) are now the marginal driver of consolidated growth; parent standalone is flat QoQ (179.21 vs 177.58). |
| A3-02 | F3 | Auditor para 6 (line 257-259) | 257 | "two subsidiaries ... total revenues of Rs. Nil, total net profit after tax of Rs. 0.01 Crore" | NEUTRAL-FACT | Two dormant/shell subsidiaries confirmed (nil revenue). No going-concern language attached, so this is balance-sheet housekeeping not operations. Watch for future strike-off / merger. |
| A3-03 | F4 | AUDITOR_SCOPE_LIMITATION (para 7+8, line 269-284) | 269 | "five subsidiaries ... reviewed by one of the joint auditors" / "two foreign subsidiaries ... reviewed by the independent auditors ... of such foreign countries" | AMBIGUOUS | Rs 84.92 cr (para 7) + Rs 30.38 cr (para 8) = Rs 115.30 cr PAT = 46.9% of consolidated PAT (245.64), and Rs 1,262.06 cr = 65.9% of consolidated revenue, was reviewed by only one of the two joint auditors or by foreign-jurisdiction auditors, not by both signing Indian auditors. Above the 10%-of-PAT threshold. No prior quarter to trend the ratio (gap). |
| A3-04 | F6 | MATERIAL_CAPEX / Board item 2 (line 61-63, 90) | 90 | "Expected to be commissioned by September 2027" | FORWARD-SIGNAL | Dated management commitment: Rs 215 cr Data Center Connectivity facility, 2,70,000 assemblies/annum, live by Sep-2027. Feeds Role 5 promise-vs-delivery tracker and FTTCP catalyst timeline. |
| A3-05 | F8 | Deferred Tax (line 369) | 369 | "(4 .36) ... (23 .56)" (standalone deferred benefit Q1FY27 vs Q4FY26) | FORWARD-SIGNAL | Persistent deferred-tax CREDITS every period. Standalone shield compressed from ~1,089 bps of PBT (Q4FY26: 23.56/216.38) to ~182 bps (Q1FY27: 4.36/240.12); standalone ETR normalised 17.9% -> 25.4% (near 25.17% statutory). Cash-tax headwind to forward EPS as the DTA/carryforward shield exhausts. No "earlier years" tax-adjustment line present (clean on that sub-check). |
| A3-06 | F9 | OCI "Items not reclassified" (line 375) | 375 | "74.24 ... (18 .56)" (Q1FY27 vs full FY26) | AMBIGUOUS | Single-quarter OCI item (+74.24 cr standalone, +74.49 cr consol) exceeds the entire prior-year figure (FY26 -18.56 cr). Rule trigger = assumption change (equity FVOCI revaluation or actuarial discount-rate/plan-asset change). Verify assumptions at the Annual Report. |
| A3-07 | F10 | Diluted EPS (line 403) + CAPITAL_RAISE Note 3(ii) (line 470-474) | 403 | "Diluted (Re I Rs.) 1.17 ... 1.49" (equal to Basic every period) | AMBIGUOUS | Diluted EPS equals Basic EPS in all four periods despite 7,50,00,000 promoter warrants outstanding at Rs 74 exercise vs CMP ~Rs 197 (Notion). At ~4.9% of 153.03 cr shares these should be dilutive and depress diluted EPS. No spread shown = dilution overhang not reflected. Question for A4. |
| A3-08 | F12 | Segment Assets/Liabilities (line 444, 446, 452) | 444 | "5,042 .76 ... 3,977 .84 ... 3,115.09" (consol Telecom segment assets) | FORWARD-SIGNAL | Telecom segment assets +1,065 cr QoQ (+1,928 cr YoY) with segment liabilities +637 cr QoQ (1,306 -> 1,943) = net WC/asset absorption ~428 cr funding the OFC/export ramp. Meanwhile Turnkey (BharatNet EPC) consol revenue is flat-to-down YoY (293.11 -> 280.32) against Rs 3,565.77 cr of segment assets locked and a segment loss of (87.53): BharatNet III ramp is NOT yet visible in segment revenue while WC stays parked. No receivables-aging disclosed in this filing. |
| A3-09 | F13 | MATERIAL_CAPEX Board item 2 (line 61-63, 92) | 92 | "Appropriate mix of internal accruals and/or debt financing" | FORWARD-SIGNAL | Board resolution beyond the results = Rs 215 cr capex with financing left open to debt. Foreshadows a funding decision inside the commissioning window (Sep-2027). Schedule a funding-need watch. No AR/AGM/dividend/director-term items in this board outcome (recorded as absence, normal for a Q1 results-only meeting). |
| A3-10 | F14 | SIGNATURE_BLOCK_INCOMPLETE (line 176-178) + entity naming (line 235 vs 484) | 176 | "For S BHANDARI & CO LLP ... Firm Registration No . 000560C/C400334" (no partner name, membership no. or UDIN in the standalone report) | NEUTRAL-FACT | Cumulative governance data point: (a) S Bhandari's standalone review report carries no partner name / membership no. / UDIN (contrast Oswal Sunil, complete, line 184-187); (b) entity-name drift "Dragon Wave HFCL India" (auditor, line 235) vs "DragonWave HFCL India" (Note 4, line 484), and "HFCL Ply Limited, Australia" (line 492, likely "Pty"). Individually immaterial. |
| A3-11 | F15 | ENTITY_LIST_DISCREPANCY (Note 4 line 477-492 vs auditor para 4 line 227-242) | 238 | "1. HFCL B.V. (Netherlands) (As per consolidated financial results)" | AMBIGUOUS | Auditor para-4 scope list (11 entities) omits the 3 HFCL B.V. step-down subs (HFCL Canada line 490, HFCL UK line 491, HFCL Pty Australia line 492) and the parent, vs Note 4's 15-entity list. Para 8 says the foreign figure "includes ... results of its step-down subsidiaries" without naming them. Confirm the 3 unnamed step-downs are fully captured inside the Rs 712.85 cr para-8 foreign figure. QoQ entity-change diff impossible (no prior-quarter extract) = gap. |

---

## CHECKLIST SCORECARD (all 17, no blanks)

| Check | Status | One-line basis |
|-------|--------|----------------|
| F1 ZERO-VALUE STANDING | PASS | All 11 ZERO_STANDING rows explained by structure: standalone lacks JCE-share (357), NCI/parent attribution (387-393) and the consol-only "d. Others" segment (426/434/447/455); Other Equity (398) is FY-end-only by convention; Exceptional items (363) nil in both blocks all periods (canonical clean template row). Nothing hidden. |
| F2 STANDALONE vs CONSOLIDATED | FINDING | A3-01: S-vs-C PAT gap swung 3.9% -> 37.1% of standalone PAT QoQ (>5pp), NCI 5.95 -> 17.04. |
| F3 SHELL-ENTITY | FINDING | A3-02: para 6 confirms 2 nil-revenue dormant subsidiaries; no going-concern flag (cleanup, not operations). Entity-level cost-line comparison not possible from a two-column filing (noted). |
| F4 UNAUDITED CONTRIBUTION RATIO | FINDING | A3-03: 46.9% of consol PAT / 65.9% of consol revenue under one-joint-auditor or foreign-auditor review; above 10% threshold. |
| F5 GOING CONCERN / EoM | PASS | No going-concern language in either report. Only "Other Matter" balancing-figure paras; standalone (line 171-174) and consolidated (line 289-292) are verbatim-identical and match Note 6 (line 494). Prior-quarter verbatim diff not possible (no prior extract) = noted gap, no scope change within this filing. |
| F6 FORWARD-COMMITMENT MINING | FINDING | A3-04: "board has approved" (61), "Expected to be commissioned by September 2027" (90), warrant balance "shall be payable within 18 months" (472). See Commitment Register. |
| F7 HEDGE PHRASE MINING | PASS | No hedge-lexicon phrases ("no assurance", "subject to", "evaluating", "exploring", "endeavour") present in the notes. The financing "internal accruals and/or debt" ambiguity is captured under F13, not a note-level legal hedge. |
| F8 TAX FORENSICS | FINDING | A3-05: deferred-tax credit shield compressed ~1,089 -> ~182 bps; ETR normalising to statutory. No earlier-year tax adjustment line (clean). |
| F9 OCI FORENSICS | FINDING | A3-06: single-quarter OCI +74.24 cr exceeds full FY26 (-18.56 cr) = assumption change to verify at AR. |
| F10 SHARE COUNT & DILUTION | FINDING | A3-07: paid-up 144.21 -> 153.03 traces cleanly to the QIP (Note 3(i), +8.79 cr shares); BUT diluted EPS = basic every period despite 7.5 cr promoter warrants in-the-money (Rs 74 vs Rs 197). Dilution overhang unreflected. |
| F11 RESERVES / NET WORTH | PASS | Other Equity (FY-end) + paid-up ties internally (consol NW ~4,948.59 cr; standalone ~4,727.44 cr). No third-party net-worth figure inside this filing to test a >5% gap; rating rationale/Notion net-debt figure is not a net-worth anchor. Rs 138.75 cr warrant money (received May-26) will surface in the next Other Equity line. |
| F12 SEGMENT FORENSICS | FINDING | A3-08: Telecom assets +1,065 cr QoQ (WC/capex build); Turnkey/BharatNet revenue flat-down YoY with Rs 3,565 cr assets locked and a segment loss — ramp not visible. No segment carries zero liabilities. |
| F13 BOARD OUTCOME BEYOND RESULTS | FINDING | A3-09: Rs 215 cr capex resolution, financing open to debt, Sep-2027 window. No AR/AGM/dividend/director-term items (absence recorded, normal for Q1). |
| F14 NOTE DRAFTING INCONSISTENCIES | FINDING | A3-10: incomplete S Bhandari standalone signature block + entity-name drift across tables; cumulative governance data point. |
| F15 ENTITY LIST DIFFS | FINDING | A3-11: intra-filing ENTITY_LIST_DISCREPANCY (auditor 11 vs Note 4 15; 3 step-downs unnamed). QoQ diff not possible (no prior extract) = gap. |
| F16 PRESENTATION-SPECIFIC | N.A. | Results filing, not a presentation deck. |
| F17 CONCALL SILENCE AUDIT | N.A. | Results filing, no transcript. Monitoring-checklist silence audit deferred to the concall document. |

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/line ref | status word |
|------------|--------------|---------------|-------------|
| Set up Rs 215 cr Data Center Connectivity facility (2,70,000 assemblies/annum: MMC + SNMT) | announced 22-Jul-2026 | Board item 2, line 61-63 | initiated (board-approved) |
| Commission the new facility | September 2027 | line 90 | initiated |
| Finance the facility via "internal accruals and/or debt" | within commissioning window | line 92 | initiated (mode not fixed) |
| Promoter warrant balance 75% (Rs 55.50/warrant, ~Rs 412.5 cr) payable on exercise | within 18 months of allotment (~Nov-2027) | Note 3(ii), line 472-474 | underway (25% / Rs 138.75 cr received May-2026) |
| Deploy QIP balance Rs 36.28 cr per placement objects | ongoing | Note 3(i), line 466-467 | underway (Rs 513.72 of 550 cr used) |
| Deploy warrant balance Rs 90 cr per preferential objects | ongoing | Note 3(ii), line 474-476 | underway (Rs 48.75 cr used) |

---

## FLAGGED FOR A4 (management questions)

FORWARD-SIGNAL: A3-01 (F2), A3-04 (F6), A3-05 (F8), A3-08 (F12), A3-09 (F13)
AMBIGUOUS: A3-03 (F4), A3-06 (F9), A3-07 (F10), A3-11 (F15)

Notes for A4 continuity (not findings, no line to cite in this doctype): the
results filing carries no receivables-aging, no export-revenue split, no
promoter-holding/pledge table and no Nivetti reference — monitoring-checklist
items 1, 2, 5, 6, 8 and 9 and tripwires 1-4 are therefore unresolved by this
document and pass to the concall silence audit.

---

```yaml
stage: A3-forensics
company: "HFCL"
quarter: "q1fy27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/hfcl-q1fy27/work/forensics_results_hfcl_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: PASS
  F2: FINDING
  F3: FINDING
  F4: FINDING
  F5: PASS
  F6: FINDING
  F7: PASS
  F8: FINDING
  F9: FINDING
  F10: FINDING
  F11: PASS
  F12: FINDING
  F13: FINDING
  F14: FINDING
  F15: FINDING
  F16: N.A.
  F17: N.A.
findings:
  - {id: "A3-01", check: "F2", line: "371", classification: "FORWARD-SIGNAL", implication: "S-vs-C PAT gap 3.9%->37.1% of standalone PAT QoQ; NCI 5.95->17.04; subsidiary/foreign earnings now the marginal consolidated driver"}
  - {id: "A3-02", check: "F3", line: "257", classification: "NEUTRAL-FACT", implication: "Two nil-revenue dormant subsidiaries; no going-concern flag; balance-sheet cleanup not operations"}
  - {id: "A3-03", check: "F4", line: "269", classification: "AMBIGUOUS", implication: "46.9% of consol PAT / 65.9% of consol revenue reviewed by one joint auditor or foreign auditors only; above 10% threshold; no prior quarter to trend"}
  - {id: "A3-04", check: "F6", line: "90", classification: "FORWARD-SIGNAL", implication: "Rs 215 cr DC-connectivity facility commissioning by Sep-2027; dated catalyst for FTTCP timeline and promise-vs-delivery tracker"}
  - {id: "A3-05", check: "F8", line: "369", classification: "FORWARD-SIGNAL", implication: "Deferred-tax credit shield compressed ~1089->~182 bps; ETR normalising to statutory; forward cash-tax headwind to EPS"}
  - {id: "A3-06", check: "F9", line: "375", classification: "AMBIGUOUS", implication: "Single-quarter OCI +74.24 cr exceeds full FY26 (-18.56 cr); assumption change to verify at Annual Report"}
  - {id: "A3-07", check: "F10", line: "403", classification: "AMBIGUOUS", implication: "Diluted EPS = basic despite 7.5 cr promoter warrants in-the-money (Rs74 vs Rs197); ~4.9% dilution overhang unreflected"}
  - {id: "A3-08", check: "F12", line: "444", classification: "FORWARD-SIGNAL", implication: "Telecom assets +1065 cr QoQ WC/capex build for OFC ramp; BharatNet/Turnkey revenue flat-down YoY with Rs3565 cr assets locked = ramp not yet visible"}
  - {id: "A3-09", check: "F13", line: "92", classification: "FORWARD-SIGNAL", implication: "Rs 215 cr capex board resolution, financing open to debt; funding decision foreshadowed in Sep-2027 window"}
  - {id: "A3-10", check: "F14", line: "176", classification: "NEUTRAL-FACT", implication: "Incomplete S Bhandari standalone signature block + entity-name drift across tables; cumulative governance data point"}
  - {id: "A3-11", check: "F15", line: "238", classification: "AMBIGUOUS", implication: "Auditor 11-entity scope omits 3 HFCL B.V. step-downs vs Note 4's 15; confirm captured in Rs712.85 cr para-8 figure; QoQ diff impossible (no prior extract)"}
forward_signals: ["A3-01", "A3-04", "A3-05", "A3-08", "A3-09"]
ambiguous: ["A3-03", "A3-06", "A3-07", "A3-11"]
commitments:
  - {commitment: "Set up Rs215cr Data Center Connectivity facility (2,70,000 assemblies/annum)", implied_date: "2026-07-22 approved", ref: "line 61-63", status_word: "initiated"}
  - {commitment: "Commission the new facility", implied_date: "2027-09", ref: "line 90", status_word: "initiated"}
  - {commitment: "Finance facility via internal accruals and/or debt", implied_date: "commissioning window", ref: "line 92", status_word: "initiated"}
  - {commitment: "Promoter warrant 75% balance (~Rs412.5cr) payable on exercise", implied_date: "~2027-11 (18m from allotment)", ref: "line 472-474", status_word: "underway"}
  - {commitment: "Deploy QIP balance Rs36.28cr per placement objects", implied_date: "ongoing", ref: "line 466-467", status_word: "underway"}
  - {commitment: "Deploy warrant balance Rs90cr per preferential objects", implied_date: "ongoing", ref: "line 474-476", status_word: "underway"}
gate_a3: pass
blank_checks: []
```
