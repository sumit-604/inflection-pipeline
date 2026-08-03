# A5 ADVERSARY / COMPLETENESS AUDIT — Ganesha Ecosphere (GANECOS) — Q1 FY27

Agent: A5 ADVERSARY | Model: claude-opus-4-8 | Fresh context (A4 review + A1 extracts + A2 ledgers only).
Independence: every figure below is re-derived from the raw Lakh cells in the A1 extracts (converted x0.01 to Rs Cr). A4's and A3's cites are checked, not trusted.

Verdict up front: **INCOMPLETE** — one derived-metric arithmetic error survives in A4's consolidated table (Reported EBITDA, Q4 FY26). Loop back to **A4**. Coverage is complete; all other arithmetic ties; no un-incorporated bear counter survives. Details below.

---

## 1. COVERAGE AUDIT

Fresh grep/manual sweep re-run over both extracts, diffed against both A2 ledgers, then each ledger row checked for A4 citation-or-"reviewed".

### 1A. Results filing (`extract_results_ganecos_q1fy27.txt`, 386 lines)

| Category | A2 count | A5 fresh count | Orphan rows (in ledger, absent from A4) | Status |
|---|---|---|---|---|
| Notes | 14 | 14 (std 1-7 L101-113; consol 1-6 L249-260 + 1 unnumbered ESOP footnote L261-264) | none — all in A4 Step 0D notes table | PASS |
| Line items | 64 | 64 (std 31, consol 33; consol carries the extra associate-loss row L217 + split PBT-before/after) | none — all in A4 Step 1 std/consol tables | PASS |
| Zero-standing | 4 | 4 (std B(i)/B(ii) OCI L83/L86; consol B(i)/B(ii) OCI L231/L234) | Retained in ledger; nil in all periods. A4 does not itemise them but does not drop them; treated as reviewed-no-finding (nil rows) | PASS |
| Agenda items (cover letter) | 4 | 4 (results approval + 2 enclosures + meeting-time, L17-29) | none | PASS |
| Auditor paras | 15 | 15 (standalone 4 logical L144-174; consolidated 1-11 L293-377) | none — clean conclusions + Other-Matter 7-10 all in A4 Step 0D/4A | PASS |
| Entities | 6 | 6 (Parent, Ecopet, Ecotech, Nepal/Overseas, Welfare Trust, Recycling Chain associate, L321-335) | none — all traced in A4 Step 4A decomposition | PASS |

### 1B. Board Outcome filing (`extract_boardoutcome_ganecos_q1fy27.txt`, 75 lines)

| Category | A2 count | A5 fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Agenda items | 1 | 1 (re-appointment, L19-23) | none | PASS |
| Annexure particulars | 4 | 4 (Sr 1-4, L51-75) | none — all in A4 Governance section / Q7-Q9 | PASS |
| Meeting-time facts | 2 | 2 (commenced 5:15 / concluded illegible, L43) | none — A4 addresses timing (A3-F14-03) | PASS |
| Signatory block | 1 | 1 (Sajnani digital sig, L33-41) | none | PASS |
| Related-party facts | 2 | 2 (son of EVC L71-75; MD of Ganesha Ecoverse L62-65) | none — A4 Governance section + Q6/Q7 | PASS |
| Regulatory references | 2 | 2 (Reg 30 L15-19; Master Circular L26-50) | none | PASS |
| Entities | 1 | 1 (Ganesha Ecoverse, L62-65) | none — A4 Q6 interlock | PASS |
| notes/line_items/auditor_paras/turns/slides/questions | 0 | 0 | n/a (explicit-absence rows in ledger Table 8; A4 records Doc2 as 0 notes/0 turns/0 slides) | PASS |

**Coverage verdict: PASS.** No orphan rows (no ledger row missing from A4). No row my fresh pass found that the ledgers lack. Standalone and consolidated are both first-class in A4 (full Step 1 tables each, both carried through Steps 2/3/4/4A). Zero-standing rows are retained, not dropped. All 14 A3 findings (F-01…F-08, A3-F6-01/F13-01/F13-02/F14-01/F14-02/F14-03) are traceable to specific A4 passages/questions. No loop-back to A2 or A3 on coverage.

---

## 2. ARITHMETIC AUDIT

Every derived cell recomputed from raw Lakh (x0.01). Only mismatches and the one failing cell are called out in full; all others verified tie within rounding.

### 2A. Standalone derived metrics (A4 lines 80-86) — ALL TIE
Operating EBITDA (PBT+D+Fin−OI): 9.30 / 20.93 / 23.79 / 56.95 — verified. Op EBITDA margin 4.20/8.04/9.07/5.62% — verified. Reported EBITDA 17.47/30.79/27.31/96.75 (Q4: 22.19+7.22+1.38=30.79) — verified. Core PBT 2.11/12.33/14.94/24.67 — verified. OI/PBT 79.5/44.4/19.1/61.7% — verified. ETR 25.5/26.1/25.5/25.8% (raw: Q1FY27 470.58/1845.53=25.5%) — verified. PAT margin 3.46/6.30/5.24/4.72% — verified.

### 2B. Consolidated derived metrics (A4 lines 120-126) — ONE FAIL

| Metric (col) | A4 value | A5 recomputed | Source lines (Lakh) | Status |
|---|---|---|---|---|
| Op EBITDA (V+D+Fin−OI), all cols | 36.31 / 52.35 / 59.78 / 141.71 | 36.31 / 52.35 / 59.78 / 141.71 | L216/L210-211/L209/L201 | PASS |
| Op EBITDA margin | 10.77 / 12.35 / 14.11 / 9.56% | same | on Rev L199 | PASS |
| **Reported EBITDA (PBT+D+Fin), Q1FY26** | 39.66 | 39.66 (14.32+15.50+9.84) | L218/L210-211/L209 | PASS |
| **Reported EBITDA (PBT+D+Fin), Q4FY26** | **62.84** | **56.84** (3088.13 + 1716.04 + 879.41 = 5683.58 Lakh) | L218 / L210-211 / L209 | **FAIL** |
| **Reported EBITDA (PBT+D+Fin), Q1FY27** | 63.31 | 63.31 (3709.47+1734.25+887.26=6330.98) | L218/L210-211/L209 | PASS |
| **Reported EBITDA (PBT+D+Fin), FY26** | 159.09 | 159.09 (5394.98+6481.24+4032.47=15908.69) | L218/L210-211/L209 | PASS |
| Core PBT (PBT−OI) | 10.94 / 26.34 / 33.47 / 36.53 | same | L218/L201 | PASS |
| OI/PBT | 23.6 / 14.7 / 9.8 / 32.3% | same | L201/L218 | PASS |
| ETR ((Cur+Def)/PBT) | 24.9 / 24.8 / 21.7 / 29.2% | same (Q1FY27 806/3709.47=21.7%) | L220/L221/L218 | PASS |
| PAT margin | 3.19 / 5.48 / 6.85 / 2.58% | same | L222/L199 | PASS |

**The single defect.** A4 reports consolidated Reported EBITDA for Q4 FY26 as **Rs 62.84 Cr**. Recomputed from the raw cells: PBT (VII, after associate) L218 = 3,088.13 Lakh + Depreciation L210-211 = 1,716.04 Lakh + Finance costs L209 = 879.41 Lakh = **5,683.58 Lakh = Rs 56.84 Cr**. Cross-check: Reported EBITDA must equal Op EBITDA + Other Income = 52.35 + 4.54 = 56.89 Cr, confirming ~56.84, not 62.84. Discrepancy = **Rs 6.00 Cr**, far above rounding. The other three columns of the same row are correct, so this is an isolated single-cell error (a 5→6 leading-digit slip: 56.84 rendered 62.84), not a systematic method fault. It is not load-bearing to the verdict narrative, but it is a published derived figure and fails the "any mismatch above rounding = FAIL" bar.

### 2C. Step 2 YoY (standalone + consolidated) — ALL TIE
Standalone: Rev +18.4, OpEBITDA +155.8, margin +487bps, Dep +16.7, Fin +51.8 (raw 68.25/131.65=51.8%), EBIT +394.6, OI −57.0, CorePBT +608.4, PBT +79.5, PAT +79.4, EPS +70.4% — all verified.
Consolidated: Rev +25.7, OpEBITDA +64.6, margin +334bps, Dep +11.9, Fin −9.8, EBIT +103.9, OI +7.2, CorePBT +206.0, PBT +159.1, PAT +170.0, EPS +156.5% — all verified.

### 2D. Step 3 QoQ — ALL TIE
Consol rev −0.06% (423.67/423.94), margin +176 bps, core PBT +27.1%. Std rev +0.76%, margin +103 bps, std PAT −16.2% (13.75/16.41). Verified.

### 2E. Step 4 PAT bridge (consol) — TIES
Δrev 86.55 × 10.77% = 9.32; margin +334bps × 423.67 = 14.15; = OpEBITDA Δ 23.47 (A4 23.46, rounding); −D 1.84; +Fin 0.97; +OI 0.24; −assoc 0.06; = PBT Δ 22.77 (ties reported 37.09−14.32); −tax 4.50 (8.06−3.56); = PAT Δ +18.27 ≈ reported +18.28. Standalone bridge: 14.49 OpEBITDA −0.98 D −0.68 Fin = 12.83; −4.65 OI −2.09 tax = +6.09 = 13.75−7.66. Verified.

### 2F. Step 4A S-to-C PAT gap — TIES
FY26 −9.62 / Q1FY26 +3.09 / Q4FY26 +6.80 / Q1FY27 +15.29 (raw 2903.48−1374.95=1528.53). % of std PAT +111/+41/+40/−20%. Q2+Q3 FY26 implied gap −19.5 (−9.62−3.09−6.80). Decomposition: subs +15.04 (1504.03) − Nepal 0.27 (26.81) − assoc 0.09 (8.55) + residual 0.61 = 15.29. All verified. The "~50.6% of consol PAT" claim = (1504.03−26.81−8.55)/2903.48 = 50.6% (component-auditor subs + mgmt-certified associate); reasonable under the "~" and the label is a mild imprecision (it folds the associate in), not an arithmetic error.

### 2G. Step 0C share-count — TIES
Paid-up 25.4570→26.7960 Cr, FV Rs 10 → +1.339m shares = +5.26% of 25.457m pre-issue. Verified. Correctly treated as an issuance (no retrospective EPS restatement), not estimated.

**Arithmetic verdict: FAIL on one cell (consol Reported EBITDA Q4 FY26).** Everything else ties within rounding.

---

## 3. ADVERSARIAL READ — three most positive claims vs strongest bear from the same text

**Claim 1 (A4 L217): "~100% of the YoY consolidated PAT rise is recurring core operations, not treasury."**
Bear counter (same extract): the +Rs 18.28 Cr PAT rise is dominated by the +Rs 15.04 Cr swing at two domestic subsidiaries (para 7, L347-348) that are (a) reviewed only by component auditors, not the principal auditor (L346-353); (b) a one-quarter print off a FY26 loss base; and (c) tax-flattered — consolidated current tax (5.08) equals standalone current tax so the subs paid ~nil current tax, and consol ETR 21.7% sits below the ~25.17% statutory rate (L220-221/L125), i.e. part of the "quality" is a temporary tax shield that will normalise up. **Survives, but ALREADY grafted** into A4 (Step 4A durability caveats, Step 4 ETR step-up watch item, Flag 3, Q3). No new addition required.

**Claim 2 (A4 L168, L391): "Op EBITDA margin expanded +487 bps standalone / +334 bps consolidated — genuine margin recovery."**
Bear counter (same extract): no tonnage/utilisation/product-mix is disclosed anywhere (F-01, tripwire 7), and QoQ consolidated revenue is flat (−0.06%) with margin up — so the gain is mix/timing and could give back; the filing is silent on Warangal commissioning that would evidence structural volume (L192). **Survives, but ALREADY grafted** (A4 Step 3 "margin/mix, not volume", Step 8C bear threshold "margin give-back toward 12%", Q11, tripwire 7). A sharper sub-point — that the large consolidated inventory build (change in inventories −Rs 35.56 Cr, L206) could be deferring cost out of the current-period P&L and flattering gross margin — is only weakly supported (inventory build is standard matching, not per se margin inflation) and does not rise to a must-add counter.

**Claim 3 (A4 L242-243, L391): "Decision-gate pre-condition (i) met — S-to-C PAT gap +Rs 15.29 Cr (+111% of standalone PAT)."**
Bear counter (same extract): within FY26 the Q1 (+3.09) and Q4 (+6.80) gaps were both positive yet the full year was −9.62, so Q2+Q3 summed to roughly −Rs 19.5 Cr — positive single quarters have a track record of not being durable at these subsidiaries; and the Rs 15.04 Cr is component-auditor-reviewed with zero utilisation disclosure. **Survives, but ALREADY grafted** (A4 Step 4A "durability unproven, three explicit caveats", verdict "met on the reported figure … not yet durable").

**Adversarial verdict:** the three strongest bear counters all survive on the text, but each is already incorporated in A4's review. **No surviving, un-incorporated bear counter that must be newly grafted.** No loop-back to A4 on adversarial grounds.

---

## 4. TASK-SPECIFIC CHECKS (as directed)

- **Consolidated-minus-standalone PAT gap:** correctly treated by A4 (Step 4A, +Rs 15.29 Cr = +111%), arithmetic re-verified, durability caveats present. PASS.
- **Absence of balance sheet / net debt not computable:** correctly handled — A4 Step 5 marks CFO, net debt, WC days, PPE/CWIP all ND (Q1 P&L-only Reg-33 format), decision-gate pre-condition (ii) explicitly UNMET, tripwire 3 RED/UNRESOLVED. Nothing estimated. PASS.
- **Every A2 line item and note accounted for:** yes (Section 1 above). PASS.
- **No NOT FOUND silently estimated:** confirmed. FY26 basic EPS OCR-garbled ("1R 1?") is read as 18.12 by table position and flagged — an OCR reconstruction of a printed value, not an estimate of a missing number; share-adjusted EPS marked ND, not estimated. PASS.
- **No Decision-Status change without a committed trigger:** Decision Status stays WATCHLIST; A4 states no committed trigger exists and none fired; entry-gate pushed to FY26 AR + one confirming quarter. PASS.
- **Standalone and consolidated both first-class:** PASS.

---

## 5. FAIL REGISTER

| # | Type | Gap | Loop back |
|---|---|---|---|
| 1 | Arithmetic | Consolidated **Reported EBITDA Q4 FY26 = Rs 62.84 Cr** is wrong; recomputed **Rs 56.84 Cr** from L218 (3,088.13) + L210-211 (1,716.04) + L209 (879.41) = 5,683.58 Lakh. Cross-check Op EBITDA 52.35 + OI 4.54 = 56.89. Discrepancy Rs 6.00 Cr, above rounding. | **A4** |

No coverage FAIL (no loop to A2/A3). No surviving un-incorporated bear counter.

---

## VERDICT

**INCOMPLETE.** One arithmetic error in a published A4 derived-metric cell (consolidated Reported EBITDA, Q4 FY26: 62.84 stated vs 56.84 recomputed). Per protocol, a derived-metric mismatch above rounding is a FAIL and must be corrected before Notion save. Loop back to **A4** to correct that single cell (and confirm no downstream text used the wrong figure — none is visible; the verdict narrative does not depend on this cell). Coverage audit passes fully; all other arithmetic ties; the three strongest bear counters survive but are already incorporated. Once A4 corrects the cell, this review is otherwise save-ready.

```yaml
stage: A5-adversary
company: "GANECOS"
quarter: "Q1 FY27"
model: claude-opus-4-8
status: complete
verdict: INCOMPLETE
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches:
  - {metric: "Consolidated Reported EBITDA (PBT+D+Fin), Q4 FY26", a4_value: 62.84, recomputed: 56.84, source_line: "L218 3088.13 + L210-211 1716.04 + L209 879.41 = 5683.58 Lakh = 56.84 Cr"}
surviving_bear_counters: []
loop_back_to: "A4"
gap: "Consolidated Reported EBITDA Q4 FY26 stated as Rs 62.84 Cr; correct value is Rs 56.84 Cr (PBT 30.88 + Dep 17.16 + Fin 8.79). Rs 6.00 Cr error, above rounding. A4 to correct the cell before save."
```
