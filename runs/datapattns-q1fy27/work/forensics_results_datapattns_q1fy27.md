# A3 FORENSIC NOTES — DATA PATTERNS (INDIA) LTD (DATAPATTNS) — Q1FY27 — DOCTYPE: RESULTS

Source extract: `runs/datapattns-q1fy27/work/extract_results_datapattns_q1fy27.txt` (224 lines, 4 pages, standalone only).
Ledger: `runs/datapattns-q1fy27/work/ledger_results_datapattns_q1fy27.md`.
Prior-quarter extract: NONE on file — verbatim EoM/entity diffs deferred to next run.
Ledger reconciliation: 100% (all 27 line items, 4 auditor paras, 8 notes, 1 agenda item, 3 signature blocks, 0 entities, 0 annexures read at cited lines).

Scope note: this is a bare quarterly results package (Board Outcome letter + Deloitte limited-review report + standalone P&L + 7 notes + QIP table). No consolidated statement exists (Note 5, zero subsidiaries/associates/JVs). No order book, CFO, DSO, net-cash, segment, or programme (EW/BrahMos/AMCA) disclosure lives in a results filing — those checks route to the presentation/concall docs, not here.

---

## FINDINGS TABLE

| id | check | ledger row ref | line/turn/slide | verbatim quote | classification | forward implication |
|----|-------|----------------|-----------------|----------------|----------------|---------------------|
| DP-F1a | F1 | Sec 3 row 12 (ZERO_STANDING); Note 6 | 150-153; 211-212 | "Statutory impact of new Labour Codes (Refer note 6)"; "incremental impact of revised definition of wages under the new Labour Codes notified by the Government of India on 21 November 2025" | FORWARD-SIGNAL | The exceptional-items line is nil in all three quarterly columns and carried Rs 3.01 Cr only at FY26 year-end. The one-time catch-up flags a permanent wage-base redefinition now in force; the recurring PF/gratuity/wage impact flows through Employee benefits from FY27 onward. Employee benefits Q1FY27 Rs 42.53 Cr vs Q1FY26 Rs 36.38 Cr (+16.9% YoY). Margin watch item feeding the "EBITDA <33% sustained 2Q" tripwire. |
| DP-F6a | F6 | Note 4 QIP table rows 2, 4, 7 | 200; 202-204; 207 | "Investment in Product Development ... 167.24 ... 142.59 ... 24.65"; "EMI-EMC Testing Facility ... 15.23 ... 13.63 ... 1.60"; "Total ... 487.74 ... 461.49 ... 26.25" | FORWARD-SIGNAL | Rs 26.25 Cr of QIP proceeds still undeployed as on 30 Jun 2026 — ~3.3 years after the 13 Mar 2023 allotment — of which Rs 24.65 Cr is earmarked Product Development and Rs 1.60 Cr an EMI-EMC testing facility. A standing, dateable deployment commitment; directly relevant to the cash-conversion / "net cash <Rs 100 Cr without capex trail" thesis (money raised but not yet converted to productive capex). |
| DP-F14a | F14 | Sec 7 signature block 2 (SIGNATURE_BEFORE_BOARD_CONCLUSION); Sec 2 para 2 | 112-113 vs 41; 82 | Auditor "Date: 2026.07.30 16:34:57 +05'30'"; Board "commenced at 2.30 p.m. and concluded at 6.30 p.m.IST"; report para 2 "This Statement, which is the responsibility of the Company's Management and approved by the Company's Board of Directors" | AMBIGUOUS | Deloitte's limited-review report — which asserts the Statement was "approved by the Company's Board of Directors" — is digitally signed at 16:34:57 IST, ~1h56m before the Board's own stated conclusion time of 18:30 IST. Either the Board/Audit Committee approved the results early in the meeting (benign) or the sequencing is irregular. Generate an A4 governance question. |

---

## CHECKLIST SCORECARD (all 17)

| # | Check | Status | One-line basis |
|---|-------|--------|----------------|
| F1 | Zero-value standing line items | **FINDING** | Exceptional-items row (line 150-153) nil all quarters, Labour Code catch-up only at FY26 year-end — recurring wage-cost forward signal (DP-F1a). Second ZERO_STANDING (Note 5 entity scope) handled at F15. |
| F2 | Standalone vs consolidated decomposition | **N.A.** | No consolidated statement exists; Note 5 (line 209) "does not have any subsidiary/associate/joint ventures as on 30 June 2026" — S-vs-C gap structurally zero, nothing to decompose. |
| F3 | Shell-entity detection | **N.A.** | Zero subsidiaries (line 209); no cost lines to compare, no shells possible. |
| F4 | Unaudited contribution ratio | **PASS** | No Other Matters paragraph (auditor report lines 76-104); 0% of PAT rests on unreviewed numbers — 100% of results within Deloitte's limited review. |
| F5 | Going concern / EoM scope tracking | **PASS** | No Going Concern and no Emphasis-of-Matter paragraph; unmodified conclusion (line 98-103, Note 1 line 178). No prior extract on file — verbatim diff deferred. |
| F6 | Forward-commitment phrase mining | **FINDING** | QIP Rs 26.25 Cr undeployed (lines 200, 202-204, 207); "will rank pari-passu" (line 188). Deployment commitment DP-F6a. See Commitment Register. |
| F7 | Hedge phrase mining | **PASS** | Lexicon sweep of notes (lines 173-214): no "no assurance / subject to / evaluating / exploring / in discussions / endeavour / could have an effect". No pre-emptive hedges added. |
| F8 | Tax forensics | **PASS** | ETR Q1FY27 7.42/29.48 = 25.17% (dead-on statutory); Q4FY26 26.38%, Q1FY26 24.89%, FY26 25.35%. No "tax adjustments relating to earlier years" line; deferred tax not separately broken out (single line 155). |
| F9 | OCI forensics | **PASS** | OCI Q1FY27 (0.41) vs Q4FY26 1.13, Q1FY26 0.13, FY26 0.61 (line 157). Sign flip to negative but |0.41| < full-prior-year 0.61 and immaterial vs ~Rs 1,736 Cr net worth — below FINDING threshold. Actuarial-assumption watch for AR. |
| F10 | Share count and dilution | **PASS** | Paid-up Rs 11.20 Cr all four periods (line 163) — no corporate action; EPS "Basic and Diluted" single figure 3.94 (line 168), no spread; 5.60 Cr shares x 3.94 = 22.06 = PAT, ties. |
| F11 | Reserves and net worth tie-out | **PASS** | Other Equity Rs 1,724.77 Cr (FY26 audited, line 166) + paid-up Rs 11.20 Cr = Rs 1,735.97 Cr net worth; internally consistent. No third-party (rating/slide) number in this filing to reconcile against. |
| F12 | Segment forensics | **N.A.** | Single business segment, no reportable segment per Ind AS 108 (Note 2, line 180-181) — no segment assets/liabilities disclosed. |
| F13 | Board outcome beyond the results | **PASS** | Single agenda item: results approval (line 34). No AR/Board's-Report approval, no AGM notice, no record date, no dividend, no director appointment/term dates, no capital-raising resolution — normal for a Q1 filing. |
| F14 | Note drafting inconsistencies | **FINDING** | Auditor signature 16:34:57 IST precedes Board conclusion 18:30 IST while report asserts Board approval (DP-F14a). Note 1 wording "unmodified conclusion" (line 178) correctly matches "review/conclusion" not "audit/opinion" — that part consistent. |
| F15 | Entity list diffs | **PASS** | Note 5 (line 209) zero entities, consistent with standalone-only thesis; no prior-quarter extract on file so verbatim diff deferred — carried as open item for next quarter. No change detected this period. |
| F16 | Dropped / reframed disclosures (presentation) | **N.A.** | Doctype is results, not presentation. |
| F17 | Silence audit (concall) | **N.A.** | Doctype is results, not concall — no transcript. Notion must-have items (order book, CFO/capex YTD, DSO, net cash, EW/BrahMos/AMCA, export OB, concentration) are not results-filing content; silence audit routes to the concall doc. |

Blank checks: none. GATE A3: pass.

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/turn ref | status word |
|------------|--------------|---------------|-------------|
| Deploy remaining QIP proceeds into Product Development (Rs 24.65 Cr of Rs 167.24 Cr pending) | ongoing since 13-Mar-2023 allotment; Rs 24.65 Cr still pending as on 30-Jun-2026 | Note 4, line 200 | underway (142.59/167.24 deployed) |
| Fund EMI-EMC Testing Facility capex (Rs 1.60 Cr of Rs 15.23 Cr pending) | ongoing since 13-Mar-2023; Rs 1.60 Cr pending as on 30-Jun-2026 | Note 4, lines 202-204 | underway (13.63/15.23 deployed) |
| QIP equity shares to rank pari-passu with existing shares | 13-Mar-2023 allotment | Note 4, line 188 | completed |

---

## ADDITIONAL FORENSIC OBSERVATIONS (context for A4, not one of the 17 checks)

1. **Other expenses ran ahead of revenue with no explanatory note.** Other expenses Q1FY27 Rs 17.61 Cr (line 143) = 15.2% of revenue-from-ops (Rs 116.03 Cr), vs Q1FY26 Rs 10.77 Cr = 10.8% of Rs 99.33 Cr — up ~63% YoY on revenue up ~17%. No note explains the step-up. This, plus the Labour Code wage-base point (DP-F1a), is the main driver of the seasonally-weak-Q1 margin compression (comparable-quarter operating EBITDA margin ~27% Q1FY27 vs ~32% Q1FY26 on revenue-from-ops). Factual only — margin-vs-Bear/Base/Bull scoring is A4's call. Flagged so it is not lost.
2. **Standalone-only structure is thesis-confirming.** Zero subsidiaries/associates/JVs (Note 5) means the documented cash-conversion weakness (CFO/PAT 0.234x cumulative per Notion) cannot be attributed to consolidation leakage or minority drag — it is a clean-entity signal. Confirmatory-negative.
3. **Q1 seasonality.** Revenue Rs 116.03 Cr is 33.6% of the Rs 344.85 Cr Q4FY26 print (line 132); Q1 is structurally the weakest quarter. Any run-rate extrapolation for the tripwire tests should annualise with care.

---

```yaml
stage: A3-forensics
company: "DATAPATTNS"
quarter: "q1fy27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/datapattns-q1fy27/work/forensics_results_datapattns_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: N.A.
  F3: N.A.
  F4: PASS
  F5: PASS
  F6: FINDING
  F7: PASS
  F8: PASS
  F9: PASS
  F10: PASS
  F11: PASS
  F12: N.A.
  F13: PASS
  F14: FINDING
  F15: PASS
  F16: N.A.
  F17: N.A.
findings:
  - {id: "DP-F1a", check: "F1", line: "150-153; 211-212", classification: "FORWARD-SIGNAL", implication: "Labour Code wage-base redefinition now permanent; recurring employee-cost step-up flows through P&L from FY27 (employee benefits +16.9% YoY); EBITDA-margin tripwire watch"}
  - {id: "DP-F6a", check: "F6", line: "200; 202-204; 207", classification: "FORWARD-SIGNAL", implication: "Rs 26.25 Cr QIP proceeds undeployed 3.3yr post-allotment (Rs 24.65 Cr product development + Rs 1.60 Cr EMI-EMC facility); pending capex commitment feeding cash-conversion/capex-trail thesis"}
  - {id: "DP-F14a", check: "F14", line: "112-113 vs 41; 82", classification: "AMBIGUOUS", implication: "Auditor review report signed 16:34:57 IST, ~1h56m before Board's stated 18:30 conclusion, yet asserts Board approval; governance sequencing question for A4"}
forward_signals: ["DP-F1a", "DP-F6a"]
ambiguous: ["DP-F14a"]
commitments:
  - {commitment: "Deploy remaining QIP proceeds into Product Development (Rs 24.65 Cr pending)", implied_date: "ongoing since 2023-03-13; pending as on 2026-06-30", ref: "Note 4, line 200", status_word: "underway"}
  - {commitment: "Fund EMI-EMC Testing Facility capex (Rs 1.60 Cr pending)", implied_date: "ongoing since 2023-03-13; pending as on 2026-06-30", ref: "Note 4, lines 202-204", status_word: "underway"}
  - {commitment: "QIP equity shares to rank pari-passu with existing shares", implied_date: "2023-03-13", ref: "Note 4, line 188", status_word: "completed"}
gate_a3: pass
blank_checks: []
```
