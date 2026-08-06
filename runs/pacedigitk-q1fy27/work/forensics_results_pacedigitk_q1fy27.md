# A3 FORENSIC NOTES — Pace Digitek Ltd (PACEDIGITK), Q1 FY27, DOCTYPE: results

Source extract: `runs/pacedigitk-q1fy27/work/extract_results_pacedigitk_q1fy27.txt` (552 lines, 10 pages, unit = Rs million, x0.1 to Cr).
Ledger read: `runs/pacedigitk-q1fy27/work/ledger_results_pacedigitk_q1fy27.md` — all rows (A1-A6, B1-B6, C1-C25, D1-D9, E1-E11, F1-F9, G1-G36, H1-H8) read verbatim at cited lines. **Ledger reconciled: 100%.**

Doctype = results, therefore F1-F15 apply and F16/F17 are N.A. (per instruction line 128). Unit note: all Rs figures below are millions unless a Cr conversion is stated.

---

## 0. HEADLINE — THE BINDING GATE NUMBER IS NOT IN THIS FILING

The single most thesis-relevant number this quarter — Q1 FY27 cash flow from operations (CFO) — **is absent**. This is a Reg 33 quarterly limited-review filing containing only the Statement of Results (P&L + EPS + paid-up capital + annual-only Other equity). There is **no cash flow statement and no balance sheet** in either the standalone (lines 148-191) or consolidated (lines 427-486) statement. This is normal for an Indian Q1 limited review, but it means the following pre-committed monitoring triggers **cannot be scored from this document**:

| Notion trigger | Needs | Available in this filing? |
|---|---|---|
| 1. Q1 FY27 CFO (BINARY, EXIT gate half-1) | Cash flow statement | **NO** |
| 2. Q1 FY27 Receivables | Balance sheet | **NO** |
| 7. Inventories level Q1 FY27 | Balance sheet | **NO** (but see inventory-build proxy, FN8) |
| 8./16. ROCE annualised | BS capital employed | **NO** |
| 18. Capital employed < Rs3,100 Cr | Balance sheet | **NO** |
| 20. Asset turnover >= 0.85x | BS total assets | **NO** |

Per the priority-focus instruction this is recorded as a **FINDING / data-absence (FN1), not a PASS**. The binding CFO EXIT gate (Q1+Q2 both negative) cannot be evaluated on Q1 alone from this document; A4 must either source a cash-flow filing if one exists or defer scoring to the H1/AR. Corroborating cash-strain evidence that IS in the filing: consolidated "Changes in inventories" of (732.23) = a Rs73.2 Cr inventory BUILD this quarter, +256% vs Q1FY26's Rs20.6 Cr build (FN8) — consistent with the historical bear thesis of working capital absorbing cash.

---

## 1. FINDINGS TABLE

| id | check | ledger row | line | verbatim quote | classification | forward implication |
|----|-------|-----------|------|----------------|----------------|---------------------|
| FN1 | F1 | C-table / G-table scope | 148, 427 | "Statement of standalone unaudited financial results" / "Statement of Unaudited Consolidated Financial Results" (results-only; no cash flow, no balance sheet) | FORWARD-SIGNAL | Binding Q1 CFO gate, receivables, inventory level, ROCE, capital employed, asset turnover all UNSCORABLE this quarter. A4: source CFO elsewhere or defer to H1/AR. |
| FN2 | F1 | C6, C15, C23, G16, G34 | 164, 176, 188, 456, 482 | "(c) Purchases of stock-in-trade  -  -  6.78  747.02" | NEUTRAL-FACT | 5 zero-standing rows benign; note standalone stock-in-trade purchases fell to nil (trading migrated to subsidiaries). No exceptional-item / sale-of-investment lines exist in template. |
| FN3 | F2 | C1/G1, C17/G18 | 158, 438, 178, 458 | consol rev "5,553.64" vs standalone "2,642.40"; consol PAT "625.05" vs standalone "425.14" | FORWARD-SIGNAL | S-vs-C PAT gap widened from 7.2% (Q1FY26) to 47.0% (Q1FY27) of standalone PAT (+~40pp, far above 5pp threshold). Consol revenue +51% YoY while standalone revenue -22% YoY. Growth is now entirely subsidiary/energy-driven; standalone telecom is shrinking. |
| FN4 | F3 | E9, E10, F8, F9 | 356-365, 373-393 | "total revenues (before consolidation adjustments) of Rs NIL" / "total revenue... of Rs. 5.20 million" | AMBIGUOUS | 3 foreign/near-dormant subs (Lineage Power Holdings Singapore, Lineage Power Myanmar step-down, + 1): revenue NIL and Rs5.20mn. Pre-revenue international vehicles (ties to NEC XON Africa thesis) OR dormant shells — no going-concern flag either way. |
| FN5 | F6 | D6, D5b | 236, 238, 228 | "will be utilised for setting up Battery Energy Storage Systems for a project awarded by the Maharashtra State Electricity Distribution Company Limited" | FORWARD-SIGNAL | Live BESS/MSEDCL catalyst: PREPL capex Rs4,860.45mn incurred to date; Rs1,469.00mn IPO proceeds still unutilised (of which Rs514.94mn in PREPL). Deployment underway; feeds FTTCP catalyst timeline + trigger 3/15. |
| FN6 | F8 | G17, C14 | 457, 175 | consol total tax "191.24" on PBT "816.29" = 23.43%; standalone deferred tax "(14.36)" | AMBIGUOUS | Consolidated Q1FY27 ETR 23.43% is ~174bps BELOW statutory 25.17%; standalone posts a deferred-tax CREDIT while consol is ~nil. Future ETR normalisation/step-up risk; sustainability of shield unclear. |
| FN7 | F9 | G19 | 462 | "(i) Remeasurement of defined benefit plans gain/(loss)  (4.32)" | AMBIGUOUS | Consolidated single-quarter actuarial loss (4.32) = 92% of the full prior-year loss (FY26 = 4.71) in one quarter. Possible discount-rate/plan-asset assumption change; verify assumptions at Annual Report. |
| FN8 | F12 | H1, G7 | 490 (491-494 blank), 445 | "Consolidated segment wise information for the quarter ended June 30, 2026" (heading only; table absent) / "(d) Changes in inventories  (732.23)" | FORWARD-SIGNAL | Segment table (energy vs telecom revenue/results/assets/liabilities) entirely absent from extract — EXTRACT_GAP; triggers 5 & 6 unverifiable. Meanwhile Rs73.2 Cr consolidated inventory BUILD (+256% YoY) signals WC absorption/CFO pressure. A4 must pull segment data from source PDF. |
| FN9 | F14 | D4 vs H4; A1 | 214 vs 510; 26 | standalone "fresh issue of 3,73,35,967 number of equity shares" vs consolidated "3,73,53,967" | NEUTRAL-FACT | Standalone Note 4 share count is a transposition error (35<->53); only consol (3,73,53,967 = 3,74,09,047 − 55,080) reconciles to the stated total. Plus ref-no "PDL/2026-27/Q02_21" carries a "Q02" token on a Q1 filing. Individually immaterial; cumulatively a drafting-control data point. |

---

## 2. CHECKLIST SCORECARD (all 17, exactly one status each)

| Check | Status | One-line basis |
|-------|--------|----------------|
| F1 ZERO-VALUE STANDING ITEMS | **FINDING** | 5 zero-standing rows benign (FN2); CRITICAL: no cash flow statement / no balance sheet in filing (FN1) — CFO binding gate absent. |
| F2 S-vs-C DECOMPOSITION | **FINDING** | S-vs-C PAT gap 7.2%->47.0% of standalone PAT YoY (~40pp); consol rev +51% while standalone rev -22% (FN3). |
| F3 SHELL-ENTITY DETECTION | **FINDING** | Aggregate subs have real ops (employee/materials costs), but 3 foreign subs near-dormant (rev NIL / 5.20mn); no going-concern flag (FN4). |
| F4 UNAUDITED CONTRIBUTION RATIO | **PASS** | Para-7 unreviewed net profit 0.75mn = 0.12% of consol PAT 625.05mn; para-6 component loss 0.04mn negligible — far below 10% threshold. |
| F5 GOING CONCERN / EoM | **PASS** | No Emphasis of Matter, no Going Concern in either report; standalone conclusion clean (lines 117-121); consol Other Matters is reliance-only (lines 339-399). |
| F6 FORWARD-COMMITMENT MINING | **FINDING** | 4 dated/dateable commitments extracted (IPO completed, PREPL BESS "will be utilised", proceeds utilisation, PREPL rights subscription) — see Commitment Register (FN5). |
| F7 HEDGE PHRASE MINING | **PASS** | No hedge lexicon ("no assurance", "subject to", "evaluating", "exploring", "endeavour" etc.) present anywhere in the notes. |
| F8 TAX FORENSICS | **FINDING** | Consol Q1FY27 ETR 23.43% (~174bps below statutory 25.17%); standalone deferred-tax credit (14.36); earlier-year tax nil this quarter but 4.24/7.15 in Q4FY26 comparative (FN6). |
| F9 OCI FORENSICS | **FINDING** | Consol remeasurement loss (4.32) = 92% of full FY26 loss (4.71) in one quarter — assumption-change candidate; verify at AR (FN7). |
| F10 SHARE COUNT & DILUTION | **PASS** | Paid-up 356.88->431.70 traces to IPO fresh issue (Note 4); basic = diluted EPS every period, no dilutive-instrument spread. (Note: standalone basic EPS 2.86->1.97 YoY, -31%.) |
| F11 RESERVES / NET WORTH TIE-OUT | **PASS** | FY26 net worth ties (SA 19,272.52+431.70=19,704.22; consol 21,641.28+431.70=22,072.98); quarterly Other equity not disclosed; no third-party number in context to reconcile against — no gap. |
| F12 SEGMENT FORENSICS | **FINDING** | Segment table entirely absent (heading line 490, body 491-494 blank); inventory-build proxy Rs73.2 Cr (FN8). Cannot verify segment assets/liabilities/revenue. |
| F13 BOARD OUTCOME BEYOND RESULTS | **PASS** | Single agenda = results approval (lines 39-46); no AR/AGM notice, no record date, no dividend, no director appointment/term, no capital-raise resolution, no auditor change. (Anomaly noted: 5h20m meeting for single agenda, lines 44/56 — no cited outcome, so PASS.) |
| F14 NOTE DRAFTING INCONSISTENCIES | **FINDING** | Standalone vs consolidated fresh-issue share-count mismatch (3,73,35,967 vs 3,73,53,967); "Q02" ref token on a Q1 filing (FN9). |
| F15 ENTITY LIST DIFFS | **N.A.** | No prior-quarter extract/entity list supplied (PRIOR_EXTRACT_PATH not provided); diff not performable. 9 entities listed (lines 317-326); para6/7-to-entity mapping for 2 entities unresolved in extract (A4 to confirm vs PDF). |
| F16 PRESENTATION-SPECIFIC | **N.A.** | Doctype = results (per instruction line 128). |
| F17 CONCALL SILENCE AUDIT | **N.A.** | Doctype = results (per instruction line 128); silence audit runs on the concall document. Trigger-testability recorded in Section 0 above for A4's use. |

No blank checks. **GATE A3: pass.**

---

## 3. COMMITMENT REGISTER (from F6)

| commitment | implied date | note/ref | status word |
|-----------|--------------|----------|-------------|
| Initial Public Offer of Rs8,191.48mn, listed NSE/BSE | 06 Oct 2025 | Note 4, lines 212-217 / 506-513 | completed |
| PREPL rights-issue subscription (79,36,507 shares, Rs500.00mn) into subsidiary | during Q1 FY27 (SSA dated 08 Sep 2025) | Note 6, lines 232-234 | completed |
| PREPL funds "will be utilised for setting up Battery Energy Storage Systems" for MSEDCL project (capex Rs4,860.45mn incurred to date) | ongoing (thesis: 5 GWh commissioning Jul-Aug 2026) | Note 6, lines 236-239 | underway |
| IPO net-proceeds utilisation; Rs1,469.00mn unutilised (Rs514.94mn in PREPL); fund-util certificate 31 Jul 2026, Crisil monitoring 05 Aug 2026 | ongoing | Note 5 / 5a / 5b, lines 219-230 / 515-528 | underway |

---

## 4. FORENSIC NARRATIVE (supporting detail)

**F1 / FN1-FN2.** Every zero-standing row was read at its line and reconciled: standalone stock-in-trade purchases (C6, line 164) fell to nil in Q1FY27 and Q4FY26 (was 6.78 in Q1FY26, 747.02 FY26) while the consolidated line (G6, line 444) still carries 3.25 — trading activity has migrated into subsidiaries, benign. Earlier-year tax (C15/G16, lines 176/456) is nil this quarter. Other equity (C23/G34, lines 188/482) is annual-only presentation. The template carries NO exceptional-items, profit-on-sale-of-investments, or discontinued-operations lines at all — nothing being quietly pre-positioned. The material F1 point is the absence of a cash flow statement and balance sheet (FN1, Section 0).

**F2 / FN3.** S-vs-C gap by period (% of standalone PAT): Q1FY26 7.2%, FY26 24.7%, Q4FY26 160.8%, Q1FY27 47.0%. The YoY widening (7.2%->47.0%) crosses the 5pp threshold decisively. Decomposition: consolidated revenue doubled the standalone gap YoY (subsidiary revenue = ~52% of consolidated Q1FY27 vs ~7% in Q1FY26), driven by Cost-of-materials at consol 3,753.16 vs standalone 478.78 (subsidiary manufacturing/BESS materials). NCI share of profit is small (11.82 of 625.05 = 1.9%), so the subsidiary earnings are largely wholly owned. The transition-to-Energy thesis is visibly materialising in the numbers, but the standalone (telecom/ICT) base is contracting.

**F3 / FN4.** Not shells in aggregate — consolidated employee cost (332.63) exceeds standalone (250.37) by 82.26, and consol materials dwarf standalone, so operating subsidiaries are real. However para 6 (1 sub, revenue NIL, loss 0.04mn) and para 7 (2 subs incl. Myanmar step-down, revenue 5.20mn) identify near-dormant foreign entities. No going-concern EoM attaches to any of them. Direction is genuinely ambiguous (pre-revenue Africa/international vehicles vs dormant) — escalated to A4.

**F4.** Unreviewed/component contribution is immaterial in Rs terms: para 7 net profit 0.75mn (0.12% of consol PAT), para 6 loss 0.04mn. Below the 10%-of-PAT threshold, so PASS despite the COMPONENT_AUDITOR_RELIANCE and UNAUDITED_MANAGEMENT_FURNISHED flags. No prior-quarter breakdown supplied, so no trend line. The governance point (management-furnished foreign figures) is real but not material this quarter; the Rs5.20mn revenue there is the same near-dormant cluster as FN4.

**F5.** Verbatim confirmed: standalone report is a clean 4-paragraph unmodified conclusion (lines 117-121); consolidated report has an "Other Matters" section (lines 339-399) that is component-auditor reliance only, explicitly "not modified with respect to our reliance" (lines 395-399). No Emphasis of Matter, no Going Concern in either. No prior-quarter text supplied to verbatim-diff, but the absence itself is unambiguous — PASS.

**F6 / FN5.** See Commitment Register. The status-change signal to watch next quarter: PREPL BESS "will be utilised"/capex incurred (underway) should transition to "commissioned/commenced revenue" — the thesis expects 5 GWh commissioning Jul-Aug 2026. No "expected to be", "fast-track", "proposes to", "intends to", or "board has approved" (beyond the results approval itself) hits in the notes.

**F8 / FN6.** ETR by period — Standalone: Q1FY27 25.73%, Q4FY26 41.44%, Q1FY26 25.94%, FY26 28.66%. Consolidated: Q1FY27 23.43%, Q4FY26 27.36%, Q1FY26 25.96%, FY26 28.47%. Consol Q1FY27 sits ~174bps below statutory 25.17% and standalone books a deferred-tax credit (14.36). Not yet a persistent-credit pattern (single quarter), but flagged AMBIGUOUS for a sustainability question. Earlier-year tax is nil this quarter (good) though the Q4FY26 comparative carried 4.24 standalone / 7.15 consolidated (year-end true-up).

**F9 / FN7.** Consolidated remeasurement loss (4.32) in Q1FY27 approaches the entire prior-year loss (4.71) in a single quarter — the F9 red flag. Standalone remeasurement (0.69) is small against its FY26 gain (2.86). Flag to verify actuarial assumptions (discount rate, plan assets) at the Annual Report.

**F10.** Paid-up capital step 356.88->431.70 (Rs74.82mn = 37.41mn shares) traces cleanly to the IPO fresh issue (Note 4). Basic equals diluted in every period and every statement — no warrants/ESOP dilution surfacing (the 55,080 employee shares are already issued). Observation only: standalone basic EPS fell 2.86->1.97 YoY (denominator +21%, standalone PAT -17%).

**F11.** FY26 statutory net worth ties out (standalone Rs1,970.42 Cr; consolidated Rs2,207.30 Cr). The consol-vs-standalone Other equity gap (2,368.76mn) is subsidiary reserves plus NCI. Quarterly Other equity is not disclosed (annual-only), and no rating rationale / presentation number is in the extract to reconcile against — no gap detectable, PASS.

**F12 / FN8.** The consolidated segment table — the only segment disclosure in the entire filing (standalone Note 3 explicitly defers to it, lines 207-210) — is present as a heading but the body (lines 491-494) is blank. Energy-vs-telecom revenue/results and, critically, segment assets/liabilities (equity-funded-build detection) cannot be tested; A4 must source from the PDF. The one usable working-capital datum is the Rs73.2 Cr consolidated inventory build (line 445), up from Rs20.6 Cr in Q1FY26 — a WC drain that corroborates likely CFO weakness (the FN1 gate).

**F13.** The Board Outcome letter carries a single agenda item (results approval). Nothing beyond results — no AR/Board's report approval (no Role 6 AR event to schedule yet), no AGM notice/record date, no dividend, no director appointment/term dates, no capital-raising enabling resolution, no auditor matter. Anomaly logged (not a finding): a 5h20m board meeting (12:10-17:30, lines 44/56) for a single-agenda results approval; digital signatures all timestamp after 17:30 conclusion (no before-conclusion violation).

**F14 / FN9.** The standalone/consolidated fresh-issue share-count mismatch is a genuine drafting inconsistency (only the consolidated figure reconciles arithmetically). Combined with the "Q02" ref-number token on a Q1 filing, these are immaterial individually but note the drafting-control quality. Note text ("subjected to limited review", line 199) is consistent with the auditor's "review not an audit" — no note/letter contradiction.

**F15.** No prior-quarter entity list supplied, so the diff cannot run — N.A. The 9-entity list is captured (lines 317-326); the unresolved item for A4 is mapping which specific entities correspond to para 6 (component-reviewed) vs para 7 (unreviewed), not stated verbatim in the extract.

---

## 5. FOR A4 (question generation)

FORWARD-SIGNAL findings to convert: FN1 (CFO gate absence — how/when will the binding CFO number be obtained), FN3 (standalone revenue contraction vs consolidated surge — sustainability and telecom-base decline), FN5 (BESS commissioning status and IPO-proceeds deployment pace), FN8 (segment split + inventory build — pull segment data, quantify WC absorption).
AMBIGUOUS findings to convert: FN4 (foreign subs — dormant or ramping), FN6 (sub-statutory consol ETR + deferred-tax credit sustainability), FN7 (actuarial assumption change — verify at AR).

```yaml
stage: A3-forensics
company: "pacedigitk"
quarter: "q1fy27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "runs/pacedigitk-q1fy27/work/forensics_results_pacedigitk_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: FINDING
  F3: FINDING
  F4: PASS
  F5: PASS
  F6: FINDING
  F7: PASS
  F8: FINDING
  F9: FINDING
  F10: PASS
  F11: PASS
  F12: FINDING
  F13: PASS
  F14: FINDING
  F15: N.A.
  F16: N.A.
  F17: N.A.
findings:
  - {id: "FN1", check: "F1", line: "148,427", classification: "FORWARD-SIGNAL", implication: "No cash flow statement or balance sheet in filing; binding Q1 CFO gate, receivables, inventory level, ROCE, capital employed, asset turnover all unscorable this quarter"}
  - {id: "FN2", check: "F1", line: "164,176,188,456,482", classification: "NEUTRAL-FACT", implication: "5 zero-standing rows benign; standalone stock-in-trade purchases fell to nil; no exceptional-item lines in template"}
  - {id: "FN3", check: "F2", line: "158,438,178,458", classification: "FORWARD-SIGNAL", implication: "S-vs-C PAT gap widened 7.2%->47.0% of standalone PAT YoY; consol revenue +51% while standalone revenue -22%; growth entirely subsidiary/energy-driven"}
  - {id: "FN4", check: "F3", line: "356,373", classification: "AMBIGUOUS", implication: "3 foreign/near-dormant subs (rev NIL and 5.20mn); pre-revenue international vehicles or dormant shells; no going-concern flag"}
  - {id: "FN5", check: "F6", line: "236,238,228", classification: "FORWARD-SIGNAL", implication: "PREPL BESS/MSEDCL capex Rs4,860.45mn incurred; Rs1,469.00mn IPO proceeds unutilised; live commissioning catalyst underway"}
  - {id: "FN6", check: "F8", line: "457,175", classification: "AMBIGUOUS", implication: "Consol ETR 23.43% ~174bps below statutory 25.17%; standalone deferred-tax credit; future ETR step-up/normalisation risk"}
  - {id: "FN7", check: "F9", line: "462", classification: "AMBIGUOUS", implication: "Consol single-quarter actuarial loss (4.32) = 92% of full FY26 loss; possible assumption change; verify at Annual Report"}
  - {id: "FN8", check: "F12", line: "490,445", classification: "FORWARD-SIGNAL", implication: "Segment table absent (EXTRACT_GAP) so energy-vs-telecom split unverifiable; Rs73.2 Cr inventory build (+256% YoY) signals WC absorption/CFO pressure"}
  - {id: "FN9", check: "F14", line: "214,510,26", classification: "NEUTRAL-FACT", implication: "Standalone vs consolidated fresh-issue share-count transposition; Q02 ref token on Q1 filing; drafting-control data point"}
forward_signals: ["FN1", "FN3", "FN5", "FN8"]
ambiguous: ["FN4", "FN6", "FN7"]
commitments:
  - {commitment: "IPO of Rs8,191.48mn completed and listed NSE/BSE", implied_date: "2025-10-06", ref: "Note 4 lines 212-217/506-513", status_word: "completed"}
  - {commitment: "PREPL rights-issue subscription 79,36,507 shares Rs500.00mn into subsidiary", implied_date: "Q1FY27 (SSA 2025-09-08)", ref: "Note 6 lines 232-234", status_word: "completed"}
  - {commitment: "PREPL funds will be utilised for setting up BESS for MSEDCL project; capex Rs4,860.45mn to date", implied_date: "2026-07/2026-08 commissioning (thesis)", ref: "Note 6 lines 236-239", status_word: "underway"}
  - {commitment: "IPO net-proceeds utilisation; Rs1,469.00mn unutilised; Crisil monitoring 2026-08-05", implied_date: "ongoing", ref: "Note 5/5a/5b lines 219-230/515-528", status_word: "underway"}
gate_a3: pass
blank_checks: []
```
