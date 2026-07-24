# A3 FORENSIC NOTES — STYL (Seshaasai Technologies Ltd) — Q1FY27 — DOCTYPE: results

Source A1 extract: `extract_results_styl_q1fy27.txt` (1,088 lines, 12 pages, INR Million, x0.1 = Rs Cr).
A2 ledger: `ledger_results_styl_q1fy27.md` (gate_a2 pass). Ledger rows read verbatim at cited lines: 100%.
Fidelity regime: filed PDF is an Adobe Paper-Capture scan with a corrupted OCR text layer; A1 preserved an independent tesseract OCR CROSS-CHECK for pages 7,8,11,12. Where the two readings differ, both are cited and the finding is marked NUMBER_FIDELITY-dependent. No missing number estimated — NOT FOUND / illegible left as-is (both UDINs).

All INR Million unless stated. Consolidated (C) columns: Q1FY27 (Jun-26, Unaudited) | Q4FY26 (Mar-26, Audited) | Q1FY26 (Jun-25, Unaudited) | FY26 (Audited FY).

---

## 1. FINDINGS TABLE

| id | F# | ledger row ref | line(s) | verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| F1-01 | F1 | §7 r13, §8 r13, §7 r23, §8 r21 | 421-422 (C exc), 847 (S exc), 453-454 / 875-876 (OCI equity instr) | "4. Exceptional items … -2.51" (C FY26); "4. Exceptional Items" nil (S all periods); "Equity instrument thrQUllh Other Comprehensive Income … 0.00" | AMBIGUOUS | Standalone Exceptional line stands nil all 4 periods, but Consolidated carries an exceptional (Q4FY26 +0.23, FY26 -2.51) — the exceptional originates in a subsidiary, not the parent; standing OCI FVTOCI line signals an equity investment held/anticipated at fair value. Template ready for restructuring/impairment. |
| F2-01 | F2 | §7 r21, §8 r19 | 443-444 (C PAT 603.36), 865 (S PAT 617.45) | "7. Profit for the period / year (5-6) … 603.36" (C); "7. Profit for the period / year (5-6) … 617.45" (S) | AMBIGUOUS | Consolidated PAT is Rs 14.09 Mn BELOW standalone this quarter; the two subsidiaries net only -1.38 Mn (loss 2.15 + profit 0.77), so ~13 Mn of consolidation eliminations sit unexplained. Gap sign-flipped from +1.63 (Q1FY26 C>S) to -14.09 (Q1FY27 C<S). Consolidated rests on unaudited component numbers. → A4 question. |
| F6-01 | F6 | §1a/§2a Table B | 603 / 998 (capex unutil 1,360.92), 609 / 1003 (total unutil 1,700.80) | "Funding capital expenditure for the expansion of existing manufacturing units … 1 360.92" (unutilised) | FORWARD-SIGNAL | Rs 1,700.80 Mn (₹170.1 Cr) IPO proceeds still unutilised, of which Rs 1,360.92 Mn (₹136.1 Cr) earmarked for manufacturing-capacity expansion; only 67.65 deployed this quarter — a dateless but committed capex pipeline = future asset build / commissioning window. |
| F7-01 | F7 | Press Release p2-3 + §7 r4/r6/r1 | 145-151, 175, 387/397/401 | "elevated input costs and pressure on gross margins"; "higher raw material costs weighed on gross margins" | FORWARD-SIGNAL | Newly-added margin hedge in commentary is CONFIRMED by the numbers: gross margin fell ~286bps YoY (44.5%→41.7%). Headline EBITDA margin expansion masks a genuine gross-margin squeeze that management flags as ongoing (geopolitics/fuel/INR). → next-quarter margin risk. |
| F8-01 | F8 | §7 r14/r18, r8 | 424 (PBT 817.87), 436 (tax 215.03), 407-408 (finance cost 18.44) | "5. Profit before tax … 817.87"; "Total Tax Expenses … 215.03"; "Finance Cost … 18 44 / 18.44" | FORWARD-SIGNAL | PAT +63.8% flattered by (i) ETR normalising 33.0%→26.3% and (ii) finance cost collapsing 77.64→18.44 (-76%) after IPO debt repayment (₹300 Cr fully utilised, line 606). Both are largely non-repeatable; ETR now ~statutory (25.17%) leaves no further tax tailwind. Underlying operating EBIT +~27% vs PAT +64%. |
| F9-01 | F9 | §7 r22, §8 r20 | 450 / 543 (C 7.82; FY26 3.66), 872 (S 7.84; FY26 3.79) | "(i) Remeasurements of defined benefit plan … 7.82 … 366 / 3.66" | AMBIGUOUS | Single-quarter actuarial OCI gain (7.82 C / 7.84 S) EXCEEDS the entire prior full year (3.66 C / 3.79 S) → likely discount-rate / plan-asset assumption change. Verify assumptions at Annual Report. → A4 question. |
| F12-01 | F12 | §8 note 3 (C&S) + Press Release | 611-612 / 1005-1006 (single segment), 115-119 (verticals) | "The Company only has a single business segment i.e. business of Security & variable data Printing … does not operate in any other reportable segment" | AMBIGUOUS | The statutory statement discloses ONE reportable segment — NO segment assets/liabilities/results/capex are disclosed. The 3-vertical split (Payments 42% / Comm & Fulfilment 40% / IoT 18%) exists ONLY in the unaudited press release. All segment-level monitoring (IoT, Payments trajectory) rests on marketing percentages, not audited data. |
| F14-01 | F14 | §4 para 5 / unnumbered block; §7 r19/r21 | 323 (para-7 ref), 343-349 (unnumbered block), 440 & 444 (dup "7.") | "based on the consideration of the review report of other auditor referred to in paragraph 7 below"; two rows both "7. Profit for the period / year (5-6)" | NEUTRAL-FACT | Auditor Para 5 cross-refers to "paragraph 7 below" that carries no numeral (Other Matters is numbered 6, sub-block unnumbered); Consolidated statement labels two distinct rows "7."; Note 3 "single segment" vs press-release 3-vertical split. Individually immaterial, cumulatively a drafting/governance data point. |

Cross-document reconciliation findings (deck vs filing) are in Section 5; each cites filing lines.

---

## 2. CHECKLIST SCORECARD (all 17 — no blanks; GATE A3)

| Check | Status | Basis (one line) |
|---|---|---|
| F1 ZERO-VALUE STANDING | **FINDING** | 3 standing-nil rows: S Exceptional (847), C & S OCI equity-instrument (453/875) — plus S-vs-C exceptional asymmetry (subsidiary-origin exceptional in C only). See F1-01. |
| F2 S-vs-C DECOMPOSITION | **FINDING** | C PAT 603.36 vs S PAT 617.45; gap -14.09 exceeds subsidiary net -1.38 → ~13 Mn unexplained eliminations; gap sign-flipped YoY. See F2-01. |
| F3 SHELL-ENTITY DETECTION | PASS | Cost lines differ S vs C (Employee 175.35 vs 166.09; Materials 2,283.14 vs 2,280.48) → subsidiaries have real (small) operations, not shells; no Going Concern EoM. |
| F4 UNAUDITED CONTRIBUTION | PASS | Component NOT reviewed by primary auditor = Rs 0.77 Mn PAT (line 339) = 0.13% of consolidated PAT 603.36; far below 10% threshold. |
| F5 GOING CONCERN / EoM | PASS | No Emphasis-of-Matter, no Going Concern language in either auditor report (verbatim confirmed, pages 5-6 & 9-10); nothing to track. Prior-quarter diff not possible (no prior extract). |
| F6 FORWARD-COMMITMENT MINING | **FINDING** | IPO unutilised ₹170.1 Cr incl ₹136.1 Cr manufacturing-capex earmark; "for the expansion of existing manufacturing units" — dateless committed capex. See F6-01 + Commitment Register. |
| F7 HEDGE PHRASE MINING | **FINDING** | Commentary adds gross-margin hedge ("pressure on gross margins", "higher raw material costs weighed on gross margins"); confirmed by -286bps GM compression. See F7-01. |
| F8 TAX FORENSICS | **FINDING** | C ETR 33.0%→26.3% (26.29% = 215.03/817.87); S ETR 33.0%→25.9%; near statutory 25.17% now; PAT growth flattered vs PBT. See F8-01. |
| F9 OCI FORENSICS | **FINDING** | Q1 actuarial remeasurement 7.82 (C) / 7.84 (S) exceeds full FY26 3.66 (C) / 3.79 (S) → assumption change suspected. See F9-01. |
| F10 SHARE COUNT / DILUTION | PASS | Basic = Diluted every period (3.73/3.73 C; 3.82/3.82 S) → no dilutive spread. Implied shares rose ~147.4M→~161.8M via IPO fresh issue (a known corporate action, not unexplained). |
| F11 RESERVES / NET WORTH | **N.A.** | No Balance Sheet in this Q1 filing (confirmed full-text absence) → Other Equity + Paid-up cannot be tied out. |
| F12 SEGMENT FORENSICS | **FINDING** | Single reportable segment declared (Note 3, 611); no segment assets/liabilities disclosed; verticals only in press release. See F12-01. |
| F13 BOARD OUTCOME BEYOND RESULTS | PASS | Single-item board meeting (results + press release + LR reports + website, lines 52-63). NO AGM notice / dividend / AR approval / director / auditor / capital-raise resolution anywhere. |
| F14 NOTE DRAFTING INCONSISTENCIES | **FINDING** | Para-7 cross-reference with no numbered para 7 (323 vs 343-349); duplicate "7." rows (440/444); single-segment note vs 3-vertical PR. See F14-01. |
| F15 ENTITY LIST DIFFS | PASS | 2 subsidiaries enumerated: Rite Infotech Pvt Ltd (304), Atoll Solutions Pvt Ltd (305). No in-quarter anomaly. Prior-quarter diff not possible (no prior ledger — gap for A4); name-to-review-status mapping unresolved. |
| F16 PRESENTATION-SPECIFIC | **N.A.** | Doctype = results (F16 applies to presentations). Deck reconciliation delivered in Section 5. |
| F17 CONCALL SILENCE AUDIT | **N.A.** | Doctype = results (no transcript). Monitoring-silence overlay delivered in Section 6. |

Tally: PASS 6 (F3,F4,F5,F10,F13,F15) · FINDING 8 (F1,F2,F6,F7,F8,F9,F12,F14) · N.A. 3 (F11,F16,F17). No blanks → gate_a3 pass.

---

## 3. AUDITOR LIMITED-REVIEW PARAGRAPHS — VERBATIM

### 3a. Consolidated (Vatsaraj & Co., pages 5-6, lines 261-362)
- **Conclusion (Para 5, lines 322-328), UNMODIFIED:** "Based on our review conducted and procedures performed as stated in paragraph 3 above and based on the consideration of the review report of other auditor referred to in paragraph 7 below, nothing has come to our attention that causes us to believe that the accompanying Statement … has not disclosed the information required … or that it contains any material misstatement."
- **Other Matters (Para 6, lines 330-349):**
  - (a) line 333-336: "1 subsidiary, whose unaudited interim financial result … reflect total revenue of Rs.2.65 Million, total net Loss after tax of Rs.(2.15) Million and total comprehensive income of Rs.(2.11) Million … which have been reviewed by us."
  - (b) line 338-341: "1 subsidiary, which have not been reviewed by us, whose unaudited interim financial result … reflect total revenue of Rs.18.10 Million, total net profit after tax of Rs.0.77 Million and total comprehensive income of Rs.0.74 Million … reviewed by other auditor."
  - line 343-349 (the unnumbered "paragraph 7" material): "The interim financial information of this entity has been reviewed by other auditor whose report have been furnished to us by the Parent's management, and our conclusion … is based solely on the report of such other auditor … **Our conclusion on the Statement is not modified in respect of this matter.**"
- **Opinion type:** unmodified/unqualified Limited Review conclusion. **No** Emphasis of Matter. **No** Going Concern. **No** qualification.
- **UDIN (line 361): ILLEGIBLE** — OCR reads "1GC:!>30°5\"5L'f'KQ)(Z. °TLtOC)"; page 6 not in A1 re-OCR set → treat as NOT FOUND.
- **Numbering flag:** Para 5 forward-refers to "paragraph 7 below" but no paragraph carries a "7." numeral (MISSING_PARA_NUMBER). Substantive conclusion unaffected.

### 3b. Standalone (Vatsaraj & Co., pages 9-10, lines 708-788)
- **Conclusion (Para 4, lines 766-774), UNMODIFIED:** "Based on our review conducted as above, nothing has come to our attention that causes us to believe that the accompanying Statement … has not disclosed the information required to be disclosed in terms of the Listing Regulations … or that it contains any material misstatement."
- No Other Matters, no entity list (single entity), no Emphasis of Matter, no Going Concern — structurally complete 4-paragraph SRE 2410 review.
- **UDIN (line 787): ILLEGIBLE** — OCR reads "2b0°!>9033 TLKVWV'-155'-i"; page 10 not in A1 re-OCR set → NOT FOUND.

**Consolidated-rests-on-unaudited note:** the entire consolidation is Limited-Review (not audit); the specific portion NOT touched by the primary auditor is Rs 18.10 Mn revenue / Rs 0.77 Mn PAT (0.13% of consolidated PAT). Immaterial by F4, but the two subsidiary names (Rite Infotech / Atoll Solutions, lines 304-305) are NOT individually mapped to the (a)/(b) reviewed/other-auditor split in the source — do not assume order.

---

## 4. STANDALONE vs CONSOLIDATED GAP TABLE (first-class metric)

| Metric | Q1FY27 C | Q1FY27 S | C-S gap | Q1FY26 C | Q1FY26 S | Q1FY26 gap | FY26 C | FY26 S | FY26 gap |
|---|---|---|---|---|---|---|---|---|---|
| Revenue from Ops | 3,764.70 | 3,762.15 | +2.55 | 3,108.73 | 3,108.73 | 0.00 | 14,411.35 | 14,405.58 | +5.77 |
| Other Income | 70.97 | 70.86 | +0.11 | 23.42 | 23.04 | +0.38 | 145.78 | 144.56 | +1.22 |
| Finance Cost | 18.44 | 18.42 | +0.02 | 77.64 | 77.64 | 0.00 | 208.79 | 208.77 | +0.02 |
| PBT | 817.87 | 832.86 | -14.99 | 549.74 | 547.67 | +2.07 | 3,287.44 | 3,329.77 | -42.33 |
| Total Tax | 215.03 | 215.41 | -0.38 | 181.35 | 180.91 | +0.44 | 889.31 | 892.42 | -3.11 |
| PAT (post-NCI for C) | 603.36 | 617.45 | **-14.09** | 368.39 | 366.76 | **+1.63** | 2,400.10 | 2,437.35 | **-37.25** |

Lines: Rev 387/815; OthInc 389/817; FinCost 407-408/834; PBT 424/850; Tax 436/861-862; PAT 443-444/865. NUMBER_FIDELITY-dependent cells (FY26 Rev 14,411.35 per OCR line 511; several C-column cells per §7 flags) noted; gaps computed on the OCR cross-check reading where primary is corrupted.

**Decomposition of the -14.09 Q1FY27 PAT gap:** two subsidiaries net only -1.38 Mn (loss 2.15 + profit 0.77); C pre-NCI PAT is 602.84 (line 439), NCI adds +0.52 → 603.36. Standalone 617.45 + subsidiary net -1.38 = 616.07 expected, vs C pre-NCI 602.84 → **~13.2 Mn of consolidation eliminations** unexplained by the disclosed subsidiary P&L (candidate items: intra-group dividend/service margin elimination). The gap swung from C>S (+1.63) in Q1FY26 to C<S (-14.09) in Q1FY27, a ~2.5pp-of-standalone-PAT swing (below the 5pp FINDING threshold, but the sign-flip + unexplained elimination = A4 question). See F2-01.

---

## 5. CROSS-DOCUMENT RECONCILIATION (deck / presentation-forensics vs the FILING)

| id | Claim under test | Filing figure (line) | Verdict |
|---|---|---|---|
| X1 (F16a) | Deck slide 10 FY26 revenue 15,583 Mn vs slide 16 / Notion 14,410 Mn (₹1,441 Cr) | Consolidated FY26 Revenue from Ops = **14,411.35 Mn = ₹1,441.1 Cr** (line 387 primary corrupted "14,41 1 35" / OCR line 511 = 14,411.35); Standalone FY26 14,405.58 (815) | **Slide 10 (15,583) CONTRADICTED. Slide 16 / Notion base (14,410 ≈ 1,441 Cr) CONFIRMED.** Q1FY27 vs Q1FY26 = 3,764.70 vs 3,108.73 = **+21.1% CONFIRMED** (matches deck & PR line 111). |
| X2 (F16b) | Headline EBITDA margin 25.1% (+135bps) vs Operating EBITDA 23.2% (+22bps); gap = Other Income +203% YoY (₹71.0mn) | Other Income Q1FY27 **70.97** (389), Q1FY26 23.42 → **+203.0% CONFIRMED**. Derived EBITDA = PBT 817.87 + FinCost 18.44 + Dep 107.80 = 944.11 → margin 944.11/3,764.70 = **25.08% ≈ 25.1% CONFIRMED**. Operating EBITDA (ex-Other Income) = 873.14 → 23.19% ≈ **23.2% CONFIRMED**; +22bps vs Q1FY26 22.97% CONFIRMED | **CONFIRMED.** Headline margin expansion is ~entirely Other Income; operating margin barely moved (+22bps). EBITDA is a derived figure — not a disclosed line in the filing. |
| X3 (F8) | PAT +63.8% flattered by ETR 33.0%→26.3%; underlying PBT +48.8% | C PBT 817.87 vs 549.74 = **+48.77% CONFIRMED**; C ETR 215.03/817.87 = **26.29%** vs 181.35/549.74 = **33.02% CONFIRMED**; C PAT 603.36 vs 368.39 = **+63.78% CONFIRMED**. Standalone: PBT 832.86 vs 547.67 = +52.1%; ETR 25.86% vs 33.03%; PAT 617.45 vs 366.76 = +68.4% | **CONFIRMED both C and S.** Additional non-operating flatterer the deck under-weights: finance cost 77.64→18.44 (-76%) post IPO debt repayment (line 606, ₹300 Cr fully utilised). |
| X4 (segment) | Deck: IoT ₹67.4 Cr; Payments segment declines | Filing Note 3 = **single reportable segment** (611-612 / 1005-1006). NO segment revenue/results table. Press release (unaudited): IoT 18% (line 119) → 18% × 3,764.70 = ₹67.8 Cr ≈ deck's ₹67.4 Cr; Payments 42% (115), Comm 40% (117) — single-quarter only, no QoQ | **Filing carries NO statutory segment data.** IoT ₹67.4 Cr is reconcilable to the PR 18% but is NOT audited. Payments "declines" and any QoQ trajectory CANNOT be confirmed or refuted from the filing — do not import the deck split as fact. |

---

## 6. MONITORING CHECKLIST OVERLAY (live Notion thesis — what THE FILING discloses)

| # | Monitor | Filing verdict | Cite / basis |
|---|---|---|---|
| 1 | Revenue YoY >+10% | **CONFIRM** | +21.1% (3,764.70 vs 3,108.73, lines 387/511) |
| 2 | EBITDA margin >27% | **CONTRADICT** | Reported EBITDA margin 25.1%; operating 23.2% — both below 27% (derived from 418/407-408/409-410/389) |
| 3 | IoT revenue >₹55 Cr | **CONFIRM (PR only, unaudited)** | IoT 18% (line 119) → ₹67.8 Cr; NOT a statutory segment figure (Note 3 single segment, line 611) |
| 4 | SIM utilization >40% | **SILENT** | No operational KPI in filing |
| 5 | Inventory days <80 | **SILENT** | No Balance Sheet in filing (confirmed absence) |
| 6 | Receivable days <80 | **SILENT** | No Balance Sheet in filing |
| 7 | FY27 guidance | **SILENT (no numbers)** | Only qualitative "sustaining growth momentum" (line 163); no numeric guidance |
| 8 | eSIM launch date | **SILENT** | Not mentioned anywhere in extract |
| 9 | Reliance RFID volume | **SILENT** | Not mentioned |
| 10 | Promoter lock-in / OFS | **SILENT** | No shareholding pattern in results filing |
| 11 | Promoter pledge 0% | **SILENT** | No shareholding pattern in results filing |
| 12 | Receivables factoring | **SILENT** | No BS/notes on factoring; finance cost fall (77.64→18.44) attributed to "debt reduction" (line 181), not factoring |
| 13 | (concall) | **N.A.** | No transcript in this doctype |
| 14 | Payments QoQ trajectory | **SILENT (QoQ)** | PR gives Payments 42% of Q1FY27 (line 115) single-quarter only; no prior-quarter vertical split in filing |
| 15 | Cash-transition WC initiative | **SILENT (qualitative only)** | CFO: "strengthen cash flows … enhance supply-chain agility … allocate capital efficiently" (lines 185-187); no WC metric disclosed |

Balance-sheet-dependent monitors (#5, #6) confirmed SILENT — no Balance Sheet / Cash Flow in this Q1 Reg 33 filing (expected; A2-confirmed absence).

---

## 7. COMMITMENT REGISTER (from F6)

| commitment | implied date | note/ref | status word |
|---|---|---|---|
| Deploy remaining IPO capex earmark for expansion of existing manufacturing units (₹136.1 Cr / 1,360.92 Mn unutilised) | none stated | Note 2 Table B, lines 603 / 998 | underway (67.65 deployed in quarter) |
| Deploy remaining IPO "general corporate purposes" (₹32.1 Cr / 321.34 Mn unutilised) | none stated | Note 2 Table B, lines 608 / 1002 | underway (137.30 deployed in quarter) |
| Repay/prepay outstanding borrowings from IPO proceeds (₹300 Cr / 3,000.00 Mn) | delivered | Note 2 Table B, lines 606 / 1000 | completed (fully utilised, nil unutilised) |
| "we will continue to maintain financial discipline, enhance supply-chain agility, strengthen cash flows and allocate capital efficiently" | ongoing | Press Release, lines 185-187 | underway (qualitative) |

---

## 8. GATE A3

- Every F1-F17 marked exactly one of PASS / FINDING / N.A. — no blanks. **gate_a3: pass.**
- Ledger reconciliation: all A2 rows read verbatim at cited lines — **100%.**
- Non-estimation honoured: both UDINs left NOT FOUND; NUMBER_FIDELITY cells cite both readings; para-7 numbering gap and subsidiary name-to-status mapping left unresolved, not guessed.

---

```yaml
stage: A3-forensics
company: "STYL"
quarter: "q1fy27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/styl-q1fy27/work/forensics_results_styl_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: FINDING
  F3: PASS
  F4: PASS
  F5: PASS
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: FINDING
  F10: PASS
  F11: N.A.
  F12: FINDING
  F13: PASS
  F14: FINDING
  F15: PASS
  F16: N.A.
  F17: N.A.
findings:
  - {id: "F1-01", check: "F1", line: "421-422/847/453-454", classification: "AMBIGUOUS", implication: "Exceptional item sits in a subsidiary (C only); standing FVTOCI line signals equity investment at fair value"}
  - {id: "F2-01", check: "F2", line: "443-444/865", classification: "AMBIGUOUS", implication: "~13 Mn consolidation elimination exceeds subsidiary net -1.38; C-vs-S PAT gap sign-flipped YoY; consolidated rests on unaudited components"}
  - {id: "F6-01", check: "F6", line: "603/998/609", classification: "FORWARD-SIGNAL", implication: "IPO unutilised Rs 170.1 Cr incl Rs 136.1 Cr manufacturing-capex earmark = committed dateless capex / commissioning window"}
  - {id: "F7-01", check: "F7", line: "145-151/175", classification: "FORWARD-SIGNAL", implication: "New gross-margin hedge confirmed by -286bps GM compression; margin squeeze flagged as ongoing"}
  - {id: "F8-01", check: "F8", line: "424/436/407-408", classification: "FORWARD-SIGNAL", implication: "PAT +63.8% flattered by ETR 33.0->26.3% and finance-cost collapse post debt repayment; both non-repeatable, tax tailwind exhausted"}
  - {id: "F9-01", check: "F9", line: "450/543/872", classification: "AMBIGUOUS", implication: "Single-quarter actuarial OCI gain exceeds full prior year -> assumption change; verify at Annual Report"}
  - {id: "F12-01", check: "F12", line: "611-612/115-119", classification: "AMBIGUOUS", implication: "Single reportable segment declared; verticals (incl IoT, Payments) only in unaudited press release; no segment assets/liabilities"}
  - {id: "F14-01", check: "F14", line: "323/343-349/440-444", classification: "NEUTRAL-FACT", implication: "Auditor para-7 numbering gap + duplicate 7. rows + segment-note vs PR inconsistency = cumulative governance data point"}
  - {id: "X1", check: "F16a", line: "387/511", classification: "CONFIRMATORY-NEGATIVE", implication: "FY26 revenue base = 14,411 Mn (Rs 1,441 Cr); deck slide 10 15,583 contradicted, slide 16/Notion confirmed"}
  - {id: "X2", check: "F16b", line: "389/418", classification: "FORWARD-SIGNAL", implication: "Headline EBITDA margin 25.1% is other-income-driven (+203% YoY); operating EBITDA only 23.2% (+22bps)"}
  - {id: "X3", check: "F8", line: "418/424/436", classification: "CONFIRMATORY-NEGATIVE", implication: "PBT +48.8%, ETR 33.0->26.3%, PAT +63.8% all confirmed; finance-cost deleveraging an added non-operating flatterer"}
  - {id: "X4", check: "F12", line: "611-612/119", classification: "AMBIGUOUS", implication: "Filing carries no statutory segment data; IoT 67.4 Cr and Payments decline unverifiable from filing"}
forward_signals: ["F6-01", "F7-01", "F8-01", "X2"]
ambiguous: ["F1-01", "F2-01", "F9-01", "F12-01", "X4"]
commitments:
  - {commitment: "Deploy remaining IPO manufacturing-capex earmark Rs 1,360.92 Mn", implied_date: "none stated", ref: "Note 2 lines 603/998", status_word: "underway"}
  - {commitment: "Deploy remaining IPO general-corporate-purposes Rs 321.34 Mn", implied_date: "none stated", ref: "Note 2 lines 608/1002", status_word: "underway"}
  - {commitment: "Repay borrowings from IPO proceeds Rs 3,000 Mn", implied_date: "delivered", ref: "Note 2 lines 606/1000", status_word: "completed"}
  - {commitment: "Maintain financial discipline, strengthen cash flows, allocate capital efficiently", implied_date: "ongoing", ref: "Press Release lines 185-187", status_word: "underway"}
gate_a3: pass
blank_checks: []
```
