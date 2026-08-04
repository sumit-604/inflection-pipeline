# A3 FORENSIC NOTES — DEE Development Engineers Ltd (D-DEV / DEEDEV / BSE 544198)
## Quarter: Q1 FY27 (ended 30 June 2026) | doctype = presentation (Q1 FY27 Earnings Press Release, unaudited)
Source extract: `runs/d-dev-q1fy27/work/extract_presentation_d-dev_q1fy27.txt` (DOC4_press_release.pdf, 4 pages, 175 lines)
Ledger reconciled: 100% (all 7 A2 tables / every cited row read verbatim at its line before judging)
Units: Rs. Crores. Statutory tax reference 25.17%.

Classification taxonomy (per prompt file): FORWARD-SIGNAL / AMBIGUOUS / CONFIRMATORY-NEGATIVE / NEUTRAL-FACT.
(Task-message synonyms: RED-FLAG≈CONFIRMATORY-NEGATIVE, BENIGN≈NEUTRAL-FACT.)

---

## 1. FINDINGS TABLE

| id | check | ledger row ref | line/slide | verbatim quote | classification | forward implication |
|----|-------|----------------|-----------|----------------|----------------|---------------------|
| A3-F01 | F2 | T2 (all 6 rows); T1 cover | 30, 70–79 | "Unaudited Financial Results for the quarter ended June 30, 2026"; table header "₹ Crore" with **no standalone/consolidated label** | AMBIGUOUS | Basis of the entire Financial Summary is unstated. FY26 consol diluted EPS ₹11.14 vs standalone ₹8.13 (Notion); Q1 FY27 EPS ₹2.32 (~₹9.3 annualised) sits between the two — basis materially changes the read. A4 must confirm basis against the audited filing. |
| A3-F02 | F6 | T5 rows 1–9; T4 rows 4–6; T6 claims 3,8,12,15,16,19 | 65, 89–90, 91–93, 94, 119–121, 128–131, 136–140, 145–147 | "the deferred revenue is expected to be recognized in the coming quarter"; "full benefit expected from Q2 FY27"; "The Board has approved seeking shareholders' approval under Section 62(3)" | FORWARD-SIGNAL | 9 dated/dateable management commitments (see Commitment Register §3). Feed Role-5 promise-vs-delivery tracker; deferred ~₹25 Cr and pellet full-benefit are testable at Q2 FY27. |
| A3-F03 | F7 | T4 row 5/6; T6 claim 2 | 91–93, 97–99 | "deferred due to temporary geopolitical disruptions in the Middle East and customer-related issues"; "conversion right may be exercised by the lenders only upon the occurrence of an event of default" | AMBIGUOUS | Two pre-emptive covers: (i) revenue-lumpiness / "customer-related issues" hedge on a quarter that also missed ~₹25 Cr; (ii) a newly surfaced lender-conversion-on-default clause tied to WC facilities. Both signal what could recur next quarter. |
| A3-F04 | F10 | T2 row 6 (FORMAT_ANOMALY) | 79, 128 | "Diluted EPS   2.32   1.90   22.1" (no "%"); "successful completion of our ₹300 crore preferential issue during the quarter" | FORWARD-SIGNAL | (a) FORMAT_ANOMALY confirmed: 22.1% ties arithmetically ((2.32−1.90)/1.90) — a missing glyph, not a data error. (b) Implied weighted diluted share count 16.1/2.32 ≈ 6.94 Cr vs post-issue 7.52 Cr (Notion). ~8% of the preferential dilution is NOT yet in EPS; at full 7.52 Cr base Q1 EPS ≈ ₹2.14. Next-quarter EPS carries a mechanical dilution drag. Basic EPS not disclosed. |
| A3-F05 | F13 | T4 row 6 | 94–99 | "The Board has approved seeking shareholders' approval under Section 62(3) of the Companies Act, 2013 as an enabling provision" | FORWARD-SIGNAL | Board outcome beyond results: a shareholder vote (EGM/postal ballot) on a lender loan-conversion enabling resolution is incoming. Foreshadows a governance event and a contingent equity-conversion overhang on the May-2025 WC facilities. |
| A3-F06 | F14 | T7 row 2 vs T1/T3 | 23, 59, 68, 157 | "DDEL a leading engineering company" (line 157) vs "Dee Development Engineers" (59) vs "DEE Development Engineers Limited" (68) vs ticker "DEEDEV" (23) | NEUTRAL-FACT | Entity name rendered four ways incl. undefined "DDEL". Individually immaterial; logged as a cumulative drafting/governance data point. |
| A3-F07 | F16 | T2 rows 2,3,4,5 | 75, 76, 77, 78 | "Operating EBITDA 49.7 … 38.7%"; "PAT 16.1 … 22.4%"; "86 bps"; "(41) bps" | AMBIGUOUS | **Headline table does not internally reconcile.** EBITDA YoY computes to 38.4% (49.7/35.9) — 38.7% reconciles only at EBITDA≈49.8. PAT YoY computes to 22.9% (16.1/13.1); the claimed 22.4% and (41) bps reconcile at PAT≈16.0, while the printed 5.5% margin reconciles at 16.1 — mutually exclusive. Margin bps also drift (precise 83.5 vs 86; 38.7 vs 41). Small magnitude (rounding of unrounded figures likely), but a data-integrity flag and a hard tie-out point for the audited filing. |
| A3-F08 | F16 | T3 row 5; T4 row 3 | 63, 87–88 | "registering a growth of 92.5% on YoY basis"; "additionally L1 position stood at ₹ 12 Cr" | AMBIGUOUS | Order book ₹2,428 Cr, +92.5% YoY, but the 30-Jun-2025 base is **absent** — implied base ≈ ₹1,261 Cr, unverifiable from the release. Order-book definition (gross/net of GST, executed vs pending) not stated. Notion prior book Mar-31-2026 ₹2,040 Cr (Bansal)/₹1,940 Cr (CFO): +19% QoQ to ₹2,428 is plausible but the YoY base and the CFO/Chairman split must be tied out by A4. |
| A3-F09 | F16 | T3 row 1; T2 row 5; whole doc | 59, 78 (+ absences) | "delivers strong performance across all key parameters, aided by healthy execution" | CONFIRMATORY-NEGATIVE | Selective framing: headline claims "all key parameters" while PAT Margin fell 5.8%→5.5% (line 78) — a declining parameter. Conspicuously ABSENT vs Notion watch list & thesis concerns: cash flow / CFO (FY26 CFO/PAT 0.25x), absolute net debt/borrowings, standalone-vs-consol basis, Heavy Fabrication segment scaling, working-capital normalisation, BHEL order conversion, HRSG/Nooter-Eriksen additions, and any reference to the FY27 >19% EBITDA-margin guidance path (this quarter 16.9%). See §4 silence table. |

---

## 2. CHECKLIST SCORECARD (F1–F17, every check marked)

| # | Check | Status | One-line basis |
|---|-------|--------|----------------|
| F1 | Zero-value standing line items | **PASS** | Sole 6-row Financial Summary (74–79) fully populated both periods; A2 zero_standing_items count = 0. Nothing to interrogate. |
| F2 | Standalone vs consolidated decomposition | **FINDING** (A3-F01) | Basis unlabelled (30, 70–79); S-vs-C gap uncomputable; absence is the finding. |
| F3 | Shell-entity detection | **N.A.** | No entity-level or cost-line breakdown in a press release. |
| F4 | Unaudited contribution ratio | **N.A.** | Unaudited press release (line 30); no auditor "Other Matters" paragraph exists. |
| F5 | Going concern / EoM scope tracking | **N.A.** | No auditor EoM in a press release. Malwa Power impairment/EoM diff (Notion) deferred to audited-filing tie-out. |
| F6 | Forward-commitment phrase mining | **FINDING** (A3-F02) | 9 forward statements + board approval; commitment register built (§3). |
| F7 | Hedge phrase mining | **FINDING** (A3-F03) | Lumpiness/"customer-related issues" cover (91–93) + lender conversion-on-default clause (97–99). |
| F8 | Tax forensics | **N.A.** | No PBT or tax-expense line; ETR uncomputable. |
| F9 | OCI forensics | **N.A.** | No OCI / actuarial disclosure. |
| F10 | Share count and dilution | **FINDING** (A3-F04) | EPS FORMAT_ANOMALY (79); partial-period share base → next-Q dilution drag; basic EPS undisclosed. |
| F11 | Reserves and net worth tie-out | **N.A.** | No balance sheet / reserves figures. ₹300 Cr preferential equity add deferred to audited-filing tie-out. |
| F12 | Segment forensics | **N.A.** | No segment assets/liabilities disclosed. (Heavy Fabrication absence captured under F16/§4.) |
| F13 | Board outcome beyond the results | **FINDING** (A3-F05) | Section 62(3) enabling resolution → shareholder vote incoming (94–99). |
| F14 | Note drafting inconsistencies | **FINDING** (A3-F06) | Entity name DDEL/DEE/DEEDEV inconsistency (23, 59, 68, 157). |
| F15 | Entity list diffs | **N.A.** | No consolidation entity list; NO_PRIOR_LEDGER (A2). |
| F16 | Presentation-specific: dropped/reframed | **FINDING** (A3-F07/08/09) | Headline arithmetic non-tie; order-book base absent; selective framing / absent watch-list metrics. |
| F17 | Concall-specific: silence audit | **N.A.** | No concall transcript (press-release doctype). Notion-checklist silence audit folded into F16/§4 as the presentation-absence audit. |

Tally: **1 PASS / 7 FINDING / 9 N.A.** (F2, F6, F7, F10, F13, F14, F16 = FINDING; F1 = PASS; F3, F4, F5, F8, F9, F11, F12, F15, F17 = N.A.). Every check carries exactly one status; no blanks.

---

## 3. COMMITMENT REGISTER (from F6)

| commitment | implied date | line ref | status word |
|-----------|--------------|----------|-------------|
| ~₹25 Cr deferred revenue to be recognised | "coming quarter" (Q2 FY27) | 93 / 109 | expected |
| Biomass pellet facility full benefit | Q2 FY27 | 89–90 | operational (commenced mid-Q1); full benefit pending |
| Biomass pellet ₹80 Cr revenue in FY27 | FY27 | 136–138 | commenced commercial ops |
| Seamless pipe facility "contribute meaningfully" | "over time" / ramp-up | 119–121 | commissioned Mar-2026, ramp-up underway |
| Anjar fabrication (30,000 MT added FY26) scale-up | ongoing | 121–124 | underway |
| ₹300 Cr preferential issue | Q1 FY27 | 128–129 | completed |
| ~₹225 Cr debt reduction / lower finance costs from proceeds | "ahead" | 65–66 / 129–131 | earmarked (underway) |
| Section 62(3) shareholder approval (lender conversion enabling) | upcoming EGM/ballot | 94–99 | board-approved (initiated) |
| Operating leverage / CFO strengthen, "gradual reduction in debt" | "coming quarters" | 145–147 | expected |

---

## 4. WHAT WAS NOT DISCUSSED (presentation-absence audit vs Notion Q1 FY27 watch list — folded from F17 into F16)

| Watch item / thesis metric | Present in release? | Note |
|----------------------------|---------------------|------|
| FY27 EBITDA margin toward >19% guidance | NO | Q1 margin 16.9% (line 76); no reference to the >19% path or trajectory. |
| Heavy Fabrication segment scaling | NO | Only "Piping & Fittings" (82) and "core/non-core" cited; Heavy Fab silent. (Notion trigger: <20% YoY two quarters.) |
| Working-capital normalisation | NO | No WC / receivables / inventory commentary. |
| BHEL order conversion | NO | Not mentioned. |
| HRSG order-book additions (pre Jun-27 Nooter Eriksen) | NO | Not mentioned; ₹2,428 Cr book given without HRSG/segment split. |
| Cash flow / CFO | NO | Absent; FY26 CFO/PAT 0.25x is an active thesis concern. |
| Absolute net debt / borrowings | NO | Only narrative "~₹225 cr debt reduction" (65) and "gradual reduction in debt" (147); no absolute figure. |
| Standalone vs consolidated basis | NO | See A3-F01. |

Sustained silence on Heavy Fabrication and working capital (both pre-committed watch items) on a quarter that also deferred ~₹25 Cr of revenue is a confirmatory-negative signal for A4 to convert into direct management questions.

---

## 5. TIE-OUT POINTS FLAGGED FOR A4 (cross-check vs audited results filing)
1. Basis (standalone/consolidated) of the entire Financial Summary — line 70–79.
2. Reconcile headline YoY%/bps to audited EBITDA and PAT to the paisa — the printed 49.7 / 16.1 do not internally tie (A3-F07).
3. Order-book 30-Jun-2025 base for the 92.5% claim; and Bansal ₹2,040 vs CFO ₹1,940 Mar-26 split (A3-F08).
4. ₹300 Cr preferential equity add and post-issue 7.52 Cr share count vs EPS weighted base (A3-F04).
5. Malwa Power impairment / prior EoM / audit-qualification status (Notion; thesis trigger by Q3 FY27) — not in this release.

---

```yaml
stage: A3-forensics
company: "D-DEV"
quarter: "Q1 FY27"
doctype: "presentation"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/d-dev-q1fy27/work/forensics_presentation_d-dev_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: PASS
  F2: FINDING
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: N.A.
  F9: N.A.
  F10: FINDING
  F11: N.A.
  F12: N.A.
  F13: FINDING
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: N.A.
findings:
  - {id: "A3-F01", check: "F2", line: "30,70-79", classification: "AMBIGUOUS", implication: "Financial Summary basis (standalone vs consolidated) unstated; changes EPS read materially; tie-out to audited filing"}
  - {id: "A3-F02", check: "F6", line: "65,89-90,91-93,94,119-121,128-131,136-140,145-147", classification: "FORWARD-SIGNAL", implication: "9 dated management commitments; deferred revenue & pellet benefit testable at Q2 FY27"}
  - {id: "A3-F03", check: "F7", line: "91-93,97-99", classification: "AMBIGUOUS", implication: "Revenue-lumpiness/customer hedge + lender conversion-on-default clause signal recurrence risk"}
  - {id: "A3-F04", check: "F10", line: "79,128", classification: "FORWARD-SIGNAL", implication: "EPS missing % suffix (ties to 22.1%); ~8% preferential dilution not yet in weighted EPS; next-Q drag; basic EPS undisclosed"}
  - {id: "A3-F05", check: "F13", line: "94-99", classification: "FORWARD-SIGNAL", implication: "Section 62(3) enabling resolution -> shareholder vote & contingent lender equity-conversion overhang incoming"}
  - {id: "A3-F06", check: "F14", line: "23,59,68,157", classification: "NEUTRAL-FACT", implication: "Entity name DDEL/DEE/DEEDEV inconsistency; cumulative drafting/governance data point"}
  - {id: "A3-F07", check: "F16", line: "75,76,77,78", classification: "AMBIGUOUS", implication: "Headline table does not internally reconcile: EBITDA YoY 38.7% vs 38.4%; PAT YoY 22.4% vs 22.9%; bps drift; audited tie-out"}
  - {id: "A3-F08", check: "F16", line: "63,87-88", classification: "AMBIGUOUS", implication: "Order-book 92.5% YoY base (30-Jun-25) absent/unverifiable; order-book definition unstated; reconcile vs Mar-26 2040/1940 split"}
  - {id: "A3-F09", check: "F16", line: "59,78", classification: "CONFIRMATORY-NEGATIVE", implication: "Selective framing: 'strong across all parameters' while PAT margin down 41bps; Heavy Fab/WC/BHEL/HRSG/cash flow/debt/>19% guidance all absent"}
forward_signals: ["A3-F02", "A3-F04", "A3-F05"]
ambiguous: ["A3-F01", "A3-F03", "A3-F07", "A3-F08", "A3-F09"]
commitments:
  - {commitment: "Recognise ~Rs25 Cr deferred revenue", implied_date: "Q2 FY27", ref: "line 93/109", status_word: "expected"}
  - {commitment: "Biomass pellet facility full benefit", implied_date: "Q2 FY27", ref: "line 89-90", status_word: "commenced"}
  - {commitment: "Biomass pellet Rs80 Cr FY27 revenue", implied_date: "FY27", ref: "line 136-138", status_word: "commenced"}
  - {commitment: "Seamless pipe facility meaningful contribution", implied_date: "over time / ramp-up", ref: "line 119-121", status_word: "underway"}
  - {commitment: "Anjar fabrication scale-up", implied_date: "ongoing", ref: "line 121-124", status_word: "underway"}
  - {commitment: "Rs300 Cr preferential issue", implied_date: "Q1 FY27", ref: "line 128-129", status_word: "completed"}
  - {commitment: "~Rs225 Cr debt reduction / lower finance costs", implied_date: "ahead", ref: "line 65-66/129-131", status_word: "underway"}
  - {commitment: "Section 62(3) shareholder approval", implied_date: "upcoming EGM/ballot", ref: "line 94-99", status_word: "initiated"}
  - {commitment: "Operating leverage/CFO strengthen, gradual debt reduction", implied_date: "coming quarters", ref: "line 145-147", status_word: "expected"}
gate_a3: pass
blank_checks: []
```
