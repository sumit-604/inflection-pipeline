# A5 ADVERSARY / COMPLETENESS AUDIT — Kirloskar Electric Company Ltd (KECL) — Q1 FY27

**Agent:** A5 ADVERSARY | **Model:** claude-opus-4-8 | **Doctype:** results (single document; no concall, no presentation)
**Under audit:** `review_kecl_q1fy27.md` (A4) | **Diffed against:** `ledger_results_kecl_q1fy27.md` (A2), re-derived from `extract_results_kecl_q1fy27.txt` (A1)
**Method:** Fresh context. Every number below re-derived from raw extract lines (financial-statement tables Rs Lakhs x0.01 = Rs Cr; Annexure 3 native Rs Cr). Auditor / going-concern / EoM / Other-Matters / "except for" / segment quotes verified against the VERBATIM RE-EXTRACTION (lines 881-1301), not against A4's or A3's cites.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (HARD GATE, run first)

The A4 PLAIN-LANGUAGE BRIEF (review lines 396-412) carries all four labelled parts, each with real, non-placeholder content:

| Brief part | Location | Present? | Content check |
|---|---|---|---|
| (1) Summary narrative | l.398-400 | **PRESENT** | ~1 dense paragraph, [FILING]/[ANALYSIS] tagged, covers revenue fall, operating loss, both low-quality tailwinds, solvency/going-concern, two fixes, "except for", initiation framing. Substantive. |
| (2) SECTOR intelligence | l.402-404 | **PRESENT** | Segments, order intake, [EXTERNAL-GENERAL] T&D/transformer/data-centre tailwinds, cyclicality — labelled and non-empty. |
| (3) BUSINESS-MODEL intelligence | l.406-408 | **PRESENT** | Unit economics, operating-leverage breakeven ~Rs120-130 Cr, balance-sheet-repair subordination, Kirsons BV shell, model-drift watch. |
| (4) COMPETITION intelligence | l.410-412 | **PRESENT** | Larger better-capitalised peers, capital as structural weakness, niche wins, derisking risk — labelled EXTERNAL-GENERAL where beyond filing. |

**Gate 0 result: PASS.** All four brief parts present and non-empty.

---

## AUDIT 1 — COVERAGE (fresh independent enumeration vs A2 ledger)

Fresh manual sweep of each enumerable category, read directly from the extract, then diffed against A2 and checked for A4 citation.

| Category | A2 count | My fresh count | Orphan rows (in ledger, absent from A4) | Status |
|---|---|---|---|---|
| Numbered notes (1-14) | 14 | 14 (read sequentially l.253-400, no gaps) | none — all 14 in A4 Step 0D table | PASS |
| P&L line items | 28 | 28 (l.96-134: 26 value/dash rows + 2 blank ZERO_STANDING) | see note below (7 OCI rows) | PASS (blanket-reviewed) |
| Segment line items | 32 | 32 (6 revenue + 8 results + 6 assets + 6 liab + 6 cap-employed, verbatim l.908-986) | none — proxies + Others + revenues cited | PASS |
| Auditor paras — standalone | 10 | 10 (paras 1-4, 5 KAM, 6 EOM a/b, 7 + sig; verbatim l.1010-1125) | none | PASS |
| Auditor paras — consolidated | 12 | 12 (1-3, SEBI 33(8) addendum, 5 KAM, 5 EOM a/b, 6 Other Matters, 7 concl, 8 + sig; l.1145-1299) | none | PASS |
| Board agenda items | 3 | 3 (l.43-54: results, cost auditor, press release) | none | PASS |
| Annexure-2 rows | 3 | 3 (l.781-790) | none | PASS |
| Annexure-3 blocks | 9 | 9 (l.807-870) | none | PASS |
| Named entities | 7 (+2 unnamed) | 7 distinct (Kirsons BV, Kelbuzz, SKG Terra, SLPKG, Luxquisite, Kaytee Switchgear, Kirloskar Power Equipments) + 2 placeholders | none | PASS |
| Signature/signatory blocks | 4 | 4 (CS l.58-68, Chairman l.408, auditor std l.1113, auditor consol l.1286) | none | PASS |
| Concall turns / slides | 0 / 0 | 0 / 0 (no such document in scope) | n/a | PASS |

**Rows my fresh pass found that the ledger lacks:** NONE. No return to A2.

**Orphan-row note (non-blocking):** A4's visible Step 1 data table (l.83-129) stops at PAT/EPS/equity and does not individually display the 7 OCI rows the ledger enumerates inside the 28 (Remeasurements of DBP l.118, Taxes l.119, MTM of Investments l.121, Revaluation gain on land l.122, Taxes on above l.123, Total OCI l.124, Total comprehensive income l.126). These are NOT orphans: (a) A4's ledger-reconciliation preamble (l.18) explicitly marks "28 P&L line items … all 28 reviewed," which is a valid blanket reviewed-no-finding marking; (b) 5 of the 7 are ZERO_STANDING in both quarter columns (values only in the FY26 annual column); (c) the one substantive item, Revaluation gain on land (366 lakhs, FY26 only), feeds the revaluation-reserve theme A4 does address (Note 5, Question 1). No finding is buried in the omitted rows. Recorded as an observation, not a FAIL.

**Coverage verdict: PASS.** No orphan rows to A3; no missing enumerations to A2.

---

## AUDIT 2 — ARITHMETIC (every derived metric recomputed from raw lines)

Raw standalone lines (Rs Lakhs), column order in source is Jun-26 | Mar-26 | Jun-25 | FY26; A4 re-orders to Q1FY26 | Q4FY26 | Q1FY27 | FY26. All Step 1A/1B level-1 cells (revenue, income, materials, inventory, employee, finance, D&A, other exp, total exp, PBT-pre-exc, exceptional, PBT, tax, PAT, EPS, equity) were re-derived from lines 96-134 (standalone) and their consolidated counterparts and **every one ties out exactly** (spot list omitted for length; zero discrepancies). Derived metrics:

| Metric | A4 value | My recompute | Source lines | Status |
|---|---|---|---|---|
| Revenue YoY | −21.5% | (103.85−132.24)/132.24 = −21.47% | 96 | MATCH |
| Revenue QoQ | −36.5% | (103.85−163.57)/163.57 = −36.51% | 96 | MATCH |
| Op EBITDA Q1FY26 (PBT+D+Fin−OI) | 6.91 | 0.45+1.07+6.35−0.96 = 6.91 | 108/105/104/97 | MATCH |
| Op EBITDA Q4FY26 | 6.45 | −0.53+1.13+6.66−0.81 = 6.45 | " | MATCH |
| Op EBITDA Q1FY27 | (0.37) | −5.95+1.01+5.25−0.68 = −0.37 | " | MATCH |
| Op EBITDA FY26 ex-exc / reported | 35.60 / 27.51 | 8.75+4.34+25.48−11.06 = 27.51; +8.09 = 35.60 | 110/105/104/97/109 | MATCH |
| Op EBITDA margin Q1FY26 / Q1FY27 | 5.23% / (0.36)% | 6.91/132.24 = 5.23%; −0.37/103.85 = −0.36% | " | MATCH |
| Op EBITDA margin bps YoY | −559 bps | −0.36 − 5.23 = −5.59 pp | " | MATCH |
| Reported EBITDA all periods | 7.87/7.26/0.31/38.57 | 0.45+1.07+6.35=7.87; etc.; 8.75+4.34+25.48=38.57 | 110/105/104 | MATCH |
| **GM net-materials Q1FY26** | 28.1% | (132.24−96.71+1.59)/132.24 = 37.12/132.24 = 28.07% | 96/100/101 | MATCH |
| **GM net-materials Q4FY26** | 33.2% | (163.57−113.06+3.78)/163.57 = 54.29/163.57 = 33.19% | 96/100/101 | MATCH (loop-2 fix confirmed) |
| **GM net-materials Q1FY27** | 30.9% | (103.85−80.83+9.12)/103.85 = 32.14/103.85 = 30.95% | 96/100/101 | MATCH |
| **GM net-materials FY26** | 30.5% | (589.34−416.43+6.77)/589.34 = 179.68/589.34 = 30.49% | 96/100/101 | MATCH (loop-2 fix confirmed) |
| **GM consumed Q1FY26** | 26.9% | (132.24−96.71)/132.24 = 26.87% | 96/100 | MATCH |
| **GM consumed Q4FY26** | 30.9% | (163.57−113.06)/163.57 = 30.88% | 96/100 | MATCH |
| **GM consumed Q1FY27** | 22.2% | (103.85−80.83)/103.85 = 22.17% | 96/100 | MATCH |
| **GM consumed FY26** | 29.4% | (589.34−416.43)/589.34 = 29.34% | 96/100 | MATCH |
| GM consumed YoY | −470 bps | 22.17 − 26.87 = −4.70 pp | 96/100 | MATCH |
| Net-materials cost ratio (press check) | 69.1% / 71.9% | 71.71/103.85 = 69.05%; 95.12/132.24 = 71.93% | 100/101/96 | MATCH (ties press l.826) |
| Core PBT ex-OI Q1FY26/Q4/Q1FY27 | (0.51)/(1.34)/(6.63) | 0.45−0.96; −0.53−0.81; −5.95−0.68 | 110/97 | MATCH |
| Core PBT ex-OI FY26 rep/ex-exc | (2.31)/5.78 | 8.75−11.06; 16.84−11.06 | 110/108/97 | MATCH |
| Effective tax rate FY26 | 3.4% | 0.30/8.75 = 3.43% | 112/110 | MATCH |
| PAT margin Q1FY27 | (5.77)% | −5.99/103.85 = −5.77% | 115/96 | MATCH |
| Finance cost YoY | −17.3% | (5.25−6.35)/6.35 = −17.32% | 104 | MATCH |
| **PAT bridge total** | −6.44 | −5.99 − 0.45 = −6.44 | 115 | MATCH |
| Bridge: gross profit chg (net-mat) | −4.98 | 32.14 − 37.12 = −4.98 | 96/100/101 | MATCH |
| Bridge: emp+other chg | −2.30 | (19.52+12.99) − (18.44+11.77) = +2.30 cost | 103/106 | MATCH |
| Bridge: = Op EBITDA chg | −7.28 | −4.98 − 2.30 = −7.28 | " | MATCH |
| Bridge: D chg / Fin chg / OI chg | +0.06 / +1.10 / −0.28 | 1.07−1.01; 6.35−5.25; 0.68−0.96 | 105/104/97 | MATCH |
| Bridge: = Reported PBT chg | −6.40 | −7.28+0.06+1.10−0.28 = −6.40 | " | MATCH |
| Bridge: tax chg → PAT chg | −0.04 → −6.44 | 0 − 0.04; −6.40 − 0.04 | 112/115 | MATCH |
| S-vs-C PAT gap FY26 | 0.07 (0.8%) | 8.45 − 8.38 = 0.07; /8.45 = 0.83% | 115 | MATCH |
| Unallocated proxy QoQ | −195.05 → worsened ~46 | −195.05 −(−148.94) = −46.11 | 985 | MATCH |
| Others cap employed / rev | 79.66 / 6.24 | 7,966 / 624 lakhs x0.01 | 965/911 | MATCH |
| Total cap employed std/consol gap | 126.46 / 125.94 = 0.52 | 12,646−12,594 = 52 lakhs | 986 | MATCH |
| Preferential dilution | ~5.2% | 34,68,007 / 6,64,10,000 = 5.22% | 128/371 | MATCH |

**Arithmetic mismatches above rounding: NONE.** The full Step 1C gross-margin table (both bases, all four periods), the headline YoY table, and the PAT bridge all reconcile to raw lines 96/100/101/104/105/108/110/115. The two loop-2 corrections (net-materials Q4FY26 33.2%, FY26 30.5%) are independently confirmed correct.

**Verbatim-quote integrity (lines 881-1301):** going-concern KAM "net worth (after excluding Revaluation Reserve) is eroded … certain overdue payments to creditors" (std l.1043-1046 ✓, consol l.1179-1183 ✓); opinion "not modified" conditional on restructuring plan + fund infusion (std l.1063-1066 ✓, consol l.1195-1198 ✓); consolidated "except for the effects in respect of the matter stated in the paragraph on Other Matters" (l.1248-1249 ✓) tied to the Kirsons BV foreign-sub conversion in Other Matters (l.1231-1240 ✓), NOT to the going-concern KAM; EOM(a) Note 4 merger and EOM(b) Note 6 Rs527-lakh SLP both "not modified" (✓). Every load-bearing auditor characterisation in A4 is faithful to the verbatim text.

**Arithmetic verdict: PASS.**

---

## AUDIT 3 — ADVERSARIAL READ (three most positive claims, strongest bear counter from the SAME extract)

| # | Most-positive A4 claim | Strongest bear counter from the extract | Already carried in A4 with a bear qualifier? | Survives? |
|---|---|---|---|---|
| 1 | "The one genuine forward positive — record Q1 order booking Rs184 Cr (+28% YoY, book-to-bill 1.79x), transformer/data-centre traction" (Verdict l.392; Step 3 l.202) | "Order booking" is intake, not firm backlog; +28% YoY intake against a −21.5% billing collapse and a Rs9.12 Cr inventory BUILD (l.101/l.813) is exactly the divergence that signals soft/framework orders or non-conversion. 1.79x book-to-bill means nothing if dispatches keep deferring. | YES — Step 3 ("orders rising while billing fell"), Question 9 explicitly asks firm-vs-framework split and pre-positioned-vs-unsold inventory, Verdict says the order book "must be reconciled against the Rs9.12 Cr inventory build (demand pre-positioning vs unsold stock)." | NO |
| 2 | Finance costs fell 17.3% YoY to Rs5.25 Cr, cushioning the loss (Step 2A l.163; press l.828) | The fall is NOT deleveraging: press ties it to "working capital utilisation" (l.828), the segment unallocated-borrowing proxy WORSENED ~Rs46 Cr QoQ to −195.05 (l.985), and the KAM flags "certain overdue payments to creditors" (l.1046). It is payable-stretch / lower WC drawdown and can self-reverse. | YES — fully grafted as GAP 1 across Step 2B ans 4-5, Step 4 bridge + answers, Step 5, Question 8, Verdict, and brief. | NO |
| 3 | "Material cost improved to 69.1% of revenue from 71.9%" gross-margin improvement (press l.826; net-materials GM rose to 30.9% from 28.1%) | The improvement is a net-materials artifact of the Rs9.12 Cr inventory build; on the materials-CONSUMED basis (what actually hit COGS) gross margin DETERIORATED ~470 bps to 22.2% from 26.9% (l.100/101/96). Building stock into a −21.5% revenue quarter is a WC red flag, not cost discipline. | YES — fully grafted as GAP 2 across Step 1C note v, Step 2B ans 7, Step 4 bridge + answer, Question 9, Verdict, brief; the consumed basis is shown alongside the net basis in every load-bearing table. | NO |

**Scan for an UN-countered positive:** the "Rs40 cr promoter equity infusion is a clear endorsement" line (press l.833) is already balanced by A4 (framed as ~5.2% dilution, use-of-proceeds unknown — Question 4 bear "proceeds to fund operating losses," floor-price/minority governance — Question 10, brief reframes as balance-sheet repair not endorsement). The FY26 PBT Rs8.75 Cr, the reported Rs132 Cr book equity, and the "term loans repaid" (Note 5) claims are each explicitly countered (property-inflated OI; revaluation-reserve artifact; worsening borrowing proxy). No positive claim survives without a bear qualifier already in the review.

**Surviving bear counters requiring a graft into A4: NONE.**

---

## SURVIVING GAPS → LOOP-BACKS

- To **A2 (enumeration):** none. Fresh counts match the ledger on every category.
- To **A3 (unreviewed row / missed forensic):** none. Every ledger row is cited or blanket-reviewed; no orphan.
- To **A4 (arithmetic error / unincorporated surviving bear counter):** none. Zero arithmetic mismatches; all three top positives already carry explicit bear qualifiers.

**Non-blocking observations (do NOT change the verdict):**
1. A4's visible Step 1 table omits the 7 OCI rows; they are blanket-reviewed in the preamble and are ZERO_STANDING/immaterial — no finding buried. Cosmetic only.
2. A4's note that standalone Diluted EPS FY26 "reads 1.27, consistent with basic 1.24" is internally loose (1.27 > 1.24 would be anti-dilutive; with no dilutive instruments diluted = basic = 1.24, matching the consolidated 1.26 = 1.26 pattern). A4 explicitly flags the cell as a non-load-bearing OCR artifact (F10) and uses it in no computation, so it is immaterial. Recorded, not a FAIL.

---

## VERDICT

**COMPLETE.** Gate 0 passes (all four brief parts present). Coverage reconciles with zero orphan rows and zero missing enumerations. Every derived metric — the headline YoY table, the full Step 1C gross-margin table on both the net-materials and consumed bases across all four periods, and the PAT bridge — recomputes from raw lines 96/100/101/104/105/108/110/115 with no mismatch above rounding, and the two loop-2 corrections are independently confirmed. All verbatim auditor / going-concern / EoM / Other-Matters / "except for" quotes match lines 881-1301. The three most positive claims each already carry an explicit extract-supported bear counter, so no counter survives to be grafted. The review proceeds to Notion save.

```yaml
stage: A5-adversary
company: "KECL"
quarter: "q1fy27"
model: claude-opus-4-8
status: complete
verdict: COMPLETE
plain_language_brief:
  narrative: present
  sector: present
  business_model: present
  competition: present
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches: []
surviving_bear_counters: []
loop_back_to: ""
gap: ""
```
