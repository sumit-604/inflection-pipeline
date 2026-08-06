# A3 FORENSIC NOTES — GEE Limited (GEE) — Q1 FY27 — DOCTYPE: RESULTS (standalone unaudited + LRR)

Source A1 extract: `runs/gee-q1fy27/work/extract_results_gee_q1fy27.txt`
Reconciliation contract (A2): `runs/gee-q1fy27/work/ledger_results_gee_q1fy27.md`
Prior-quarter extract: NONE (first pipeline run — no verbatim EoM / entity diff possible)
Ledger reconciliation: 28 line items + 6 notes + 5 agenda + 5 auditor paras + 3 signature blocks + 4 zero-standing + 0 entities — every row read at its cited line. **100% reconciled.**

Doctype scope: standalone unaudited results, single reportable segment (Note 3, line 119-120), no consolidated statement, no presentation, no concall. **F1-F15 apply; F2/F3/F4/F12/F15 fall N.A. for lack of consolidation/segment data; F16/F17 N.A. (no deck, no call).**

---

## CONTEXT CROSS-CHECK vs NOTION (memory to weigh, not evidence)

- Revenue Q1 FY27 = ₹10,285.66 L = **₹102.86 Cr** (line 73), vs Q1 FY26 ₹79.18 Cr = **+29.9% YoY**. Clears Notion monitoring trigger #2 (≥₹95 Cr) and sits far above file-closure trigger #5 (<₹70 Cr) — **closure trigger #5 does NOT fire.**
- Auditor = **SAPD & Associates** (line 190), UDIN present (line 198), conclusion **unmodified** (line 188). Matches the Notion-expected incumbent; **no auditor change, no modified opinion — file-closure trigger #2 does NOT fire on this filing.**
- Notion CRITICAL trigger #1 (operational CFO ex-asset-sales, Aug 2026) is **UNTESTABLE**: an interim results filing carries no cash-flow statement, and this one does not either. Per the Notion re-engagement rule, "undisclosed -> AVOID extends" — carried to A4/A5.
- No M&A announced in this filing (closure trigger #3 not fired).

---

## FINDINGS TABLE

| id | check | ledger row ref | line | verbatim quote | classification | forward implication |
|----|-------|----------------|------|----------------|----------------|---------------------|
| F1.1 | F1 | tbl row 14 (line 89) + Note 4 | 89, 122 | "The resultant profit of Rs.369.55 Lakhs on such sale has been disclosed as an 'Exceptional item'" | AMBIGUOUS | ₹369.55 L property-sale gain = 40.4% of pre-tax profit (914.79). No cash-flow statement in filing, so Notion trigger #1 (operational CFO ex-asset-sales) is undisclosed. Operating PBT ex-exceptional (545.25) still rose 4.2x YoY (margin 1.65%→5.30%), so the quarter is not purely one-off — direction genuinely ambiguous. A4: ask management for Q1 operational CFO stripped of the ₹369.55 L proceeds, and which two Thane/other properties were sold. |
| F6.1 | F6 | agenda 3-4 + Note 6 | 38-43, 126 | "Notice of 65th Annual General Meeting... to be held on 7th September, 2026"; "will remain closed from 01st September, 2026 to 7th September, 2026" | NEUTRAL-FACT | Dated management commitments -> catalyst timeline: 65th AGM 07-Sep-2026; book closure 01-07 Sep 2026; results to be uploaded to website + BSE. Fed to Role 5 promise-tracker (see Commitment Register). |
| F8.1 | F8 | tbl rows 18-19 (lines 95-96) + row 20 (97) | 95, 96, 97 | "Previous Year Tax   -"; "Deferred tax   -" | NEUTRAL-FACT | Deferred tax booked ANNUALLY only (₹104.47 L at Q4 FY26; nil both June quarters). Interim ETR = 230.24/914.79 = exactly 25.17% (statutory) — a flat statutory estimate, not a full computation. Full-year deferred-tax true-up will step H2 ETR up. "Previous Year Tax" ₹1.04 L non-zero in FY26 column (immaterial, per-rule flagged). Property-sale gain appears taxed within current tax (no separate LTCG line). |
| F9.1 | F9 | tbl row 22 (line 100) | 100 | "Other comprehensive income/(Expenses)-net of tax   0.84 ... (0.72)" | NEUTRAL-FACT | Q1 OCI +₹0.84 L exceeds full FY26 OCI −₹0.72 L in magnitude, mechanically tripping the F9 assumption-change test; but both are sub-₹1 L (≈₹84k) and immaterial. Verify DB-plan discount-rate / plan-asset assumption at FY26 AR. |
| F10.1 | F10 | tbl row 24 (line 103) + rows 27-28 (109-110) | 103, 109, 110 | "Paid-up equity share capital... 1,039.54 ... 519.77"; "Diluted earnings... 1.30 ... 0.19" | FORWARD-SIGNAL | Paid-up doubled YoY (₹519.77 L→₹1,039.54 L, ×2) = 1:1 bonus (Oct 2025, Notion); face value ₹2 confirmed. Paid-up UNCHANGED QoQ (1,039.54 = 1,039.54) => 51 lakh promoter warrants at ₹80 NOT yet converted at 30-Jun-26. Basic-diluted spread emerged/widened: nil (Q1 FY26) → ₹0.02 (Q1 FY27), implying ≈6.8 L near-the-money incremental shares under treasury method — understates full-conversion overhang of ~9.8% (51 L / 519.77 L) exercisable within the 18-month window. Dilution is pending, not spent. |
| F13.1 | F13 | agenda 2-3 (lines 36-39) | 36, 38 | "Adoption and approval of the Board's Report... Corporate Governance Report and other annexure(s)... for the Financial Year 2025-26" | FORWARD-SIGNAL | FY26 Board's Report + Corp Gov Report approved at THIS board meeting => full FY26 Annual Report drops within weeks -> **schedule Role 6 AR Deep Dive**. That AR is where Notion trigger #6 (43.36% pledge explanation) and #7 (auditor opinion / EoM) resolve. AGM 07-Sep-2026; scrutinizer appointed (agenda 5, line 44) => voteable resolutions incoming. SCOPE_LIMITATION: those reports are NOT in this extract, so director term-dates / re-appointments through the commissioning window are UNREVIEWED — carry to A4. |
| F14.1 | F14 | signature block 2 (line 140) | 140 | "Date : 06th July, 2026" | AMBIGUOUS | Typed director-signature date (06-Jul-2026) contradicts BOTH the digital-cert timestamp (2026.08.06, line 133-134) and the board-meeting date (06-Aug-2026, line 25). Compounded by entity-name casing drift across the doc ("GEE LTD" line 27 / "Gee Limited" line 129 / "GEE LIMITED" line 156) and note-6 numbering "6.The results" (line 126). Individually trivial; cumulatively a drafting-control / governance data point. Likely stale copy-paste from a July draft, but backdating cannot be excluded on face -> A4 question. |

---

## CHECKLIST SCORECARD (all 17 — GATE A3: no blanks)

| # | Check | Status | One-line basis |
|---|-------|--------|----------------|
| F1 | Zero-value standing line items | **FINDING** | 4 ZERO_STANDING rows read (89, 95, 96, 106). Exceptional-items line (89) is populated with the ₹369.55 L property-sale gain (F1.1); Previous-Year-Tax + Deferred-tax (95/96) are annual-only (→F8.1); Other Equity (106) is annual-only balance-sheet, standard. |
| F2 | Standalone vs consolidated decomposition | **N.A.** | Standalone-only filing; no consolidated statement exists this cycle — no S-vs-C gap to compute. |
| F3 | Shell-entity detection | **N.A.** | No consolidation, no subsidiary/JV cost lines to compare. |
| F4 | Unaudited contribution ratio | **N.A.** | Auditor LRR names no component auditors / JVs / associates and carries no Other Matters paragraph (lines 150-201) — nothing unreviewed to ratio. |
| F5 | Going concern / EoM scope tracking | **PASS** | LRR conclusion unmodified (line 188); no EoM / Other Matters / Going Concern paragraph present. Auditor = SAPD & Associates (line 190) matches Notion incumbent — no auditor change, closure trigger #2 not fired. No prior-quarter LRR to verbatim-diff (first run). |
| F6 | Forward-commitment phrase mining | **FINDING** | "to be held on 7th September, 2026", "will remain closed", "would be uploaded" — dated commitments captured (F6.1 / Commitment Register). |
| F7 | Hedge phrase mining | **PASS** | Only occurrence of "subject to" is boilerplate ("subject to Limited Review", line 113). No new hedge on revenue lumpiness / customer concentration added to the notes. |
| F8 | Tax forensics | **FINDING** | Deferred tax booked annually only (nil both June quarters; ₹104.47 L at Q4 FY26); interim ETR flat at statutory 25.17%; Previous-Year-Tax ₹1.04 L non-zero in FY26 (F8.1). |
| F9 | OCI forensics | **FINDING** | Q1 OCI +₹0.84 L magnitude-exceeds full FY26 −₹0.72 L (mechanical trip), but sub-₹1 L / immaterial; verify DB assumptions at AR (F9.1). |
| F10 | Share count and dilution | **FINDING** | Paid-up doubled YoY via 1:1 bonus; basic-diluted spread emerged (nil→₹0.02); 51 L promoter warrants at ₹80 unconverted overhang (F10.1). |
| F11 | Reserves and net worth tie-out | **PASS** | 31-Mar-26 net worth = Other Equity ₹13,475.96 L + paid-up ₹1,039.54 L = ₹14,515.50 L (₹145.15 Cr). Interim Other Equity blank; no third-party comparator (no rating/slide) in filing, so no >5% gap testable. ₹10.20 Cr warrant application money should reside within Other Equity — verify at FY26 AR. |
| F12 | Segment forensics | **N.A.** | Single reportable segment (Note 3, line 119-120); Ind AS 108 disclosure N/A — no segment assets/liabilities to trend. |
| F13 | Board outcome beyond the results | **FINDING** | FY26 Board's/Corp Gov Report approved => AR imminent, Role 6 AR Deep Dive; AGM 07-Sep-2026; director term-dates unreviewed (SCOPE_LIMITATION) (F13.1). |
| F14 | Note drafting inconsistencies | **FINDING** | Director typed date 06-Jul-2026 vs cert/board 06-Aug-2026; entity-name casing drift; note-6 numbering anomaly (F14.1). |
| F15 | Entity list diffs | **N.A.** | Standalone; no consolidation entity list; no prior-quarter list to diff (first run). |
| F16 | Presentation dropped/reframed disclosures | **N.A.** | No investor presentation in this run. |
| F17 | Concall silence audit | **N.A.** | No concall / transcript in this run. |

Blank checks: NONE. **GATE A3: PASS.**

---

## COMMITMENT REGISTER (from F6 + board outcome letter)

| commitment | implied date | note/ref | status word |
|------------|--------------|----------|-------------|
| 65th Annual General Meeting to be held | 07-Sep-2026 | agenda 3, line 38 | scheduled |
| Register of Members / Share Transfer books closed | 01-Sep to 07-Sep-2026 | agenda 4, lines 40-43 | scheduled |
| FY25-26 Board's Report + Corporate Governance Report + annexures adopted | approved 06-Aug-2026 (full AR to follow within weeks) | agenda 2, lines 36-37 | approved / underway |
| Deep Shukla appointed scrutinizer for AGM e-voting | for 07-Sep-2026 AGM | agenda 5, lines 44-46 | appointed |
| Q1 results to be uploaded to Company website + BSE | on/after 06-Aug-2026 | Note 6, line 126 | committed |

Note: no operational / commissioning commitments (FCAW line, NPCIL orders, Thane cash receipt, WC plan) appear in this filing — those live in the concall/AR, which are absent this cycle. Their silence is logged for A4/A5 (the results filing is not the venue, so not a confirmatory-negative on its own).

---

## HANDOFF TO A4

- **A4 questions (AMBIGUOUS findings):** F1.1 (operational CFO ex the ₹369.55 L property proceeds; which two properties sold) and F14.1 (drafting-control / date-inconsistency; confirm actual signing date).
- **Forward-signals to weigh:** F10.1 (51 L warrant dilution overhang, unconverted at 30-Jun-26) and F13.1 (FY26 AR imminent -> Role 6 AR Deep Dive; pledge + auditor-opinion resolution point).
- **Carry-forward scope gaps:** operational CFO undisclosed (Notion trigger #1 untestable); Board's/Corp Gov Report + director term-dates not captured upstream (SCOPE_LIMITATION); ₹10.20 Cr warrant money to be traced in FY26 AR.
- **Triggers status on this filing:** closure #2 (auditor/opinion) NOT fired; closure #3 (M&A) NOT fired; closure #5 (rev <₹70 Cr) NOT fired; monitoring #2 (rev ≥₹95 Cr) FIRED favourably.

```yaml
stage: A3-forensics
company: "GEE"
quarter: "Q1 FY27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/gee-q1fy27/work/forensics_gee_q1fy27.md"
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
  - {id: "F1.1", check: "F1", line: "89,122", classification: "AMBIGUOUS", implication: "PAT 40.4% dependent on one-off property-sale gain; operational CFO undisclosed (no cash-flow stmt) -> A4 question"}
  - {id: "F6.1", check: "F6", line: "38,126", classification: "NEUTRAL-FACT", implication: "Dated commitments: AGM 07-Sep-2026, book closure 01-07 Sep, results upload -> catalyst timeline"}
  - {id: "F8.1", check: "F8", line: "95,96,97", classification: "NEUTRAL-FACT", implication: "Deferred tax annual-only; interim ETR flat 25.17%; H2 deferred-tax true-up will lift ETR; PY tax 1.04L non-zero"}
  - {id: "F9.1", check: "F9", line: "100", classification: "NEUTRAL-FACT", implication: "Q1 OCI magnitude-exceeds full FY26 (mechanical trip) but sub-1L/immaterial; verify DB assumptions at AR"}
  - {id: "F10.1", check: "F10", line: "103,109,110", classification: "FORWARD-SIGNAL", implication: "Paid-up doubled via 1:1 bonus; 51L promoter warrants at 80 unconverted overhang ~9.8%; basic-diluted spread widening"}
  - {id: "F13.1", check: "F13", line: "36,38", classification: "FORWARD-SIGNAL", implication: "FY26 AR imminent -> Role 6 AR Deep Dive; resolves pledge + auditor-opinion triggers; director terms unreviewed"}
  - {id: "F14.1", check: "F14", line: "140", classification: "AMBIGUOUS", implication: "Director typed date 06-Jul vs cert/board 06-Aug; casing drift; drafting-control question -> A4"}
forward_signals: ["F10.1", "F13.1"]
ambiguous: ["F1.1", "F14.1"]
commitments:
  - {commitment: "65th AGM to be held", implied_date: "2026-09-07", ref: "agenda 3, line 38", status_word: "scheduled"}
  - {commitment: "Book closure (Members/Transfer books)", implied_date: "2026-09-01/2026-09-07", ref: "agenda 4, lines 40-43", status_word: "scheduled"}
  - {commitment: "FY25-26 Board's Report + Corp Gov Report adopted; full AR to follow", implied_date: "2026-08-06+weeks", ref: "agenda 2, lines 36-37", status_word: "underway"}
  - {commitment: "Scrutinizer appointed for AGM e-voting", implied_date: "2026-09-07", ref: "agenda 5, lines 44-46", status_word: "appointed"}
  - {commitment: "Q1 results uploaded to website + BSE", implied_date: "2026-08-06", ref: "Note 6, line 126", status_word: "committed"}
gate_a3: pass
blank_checks: []
```
