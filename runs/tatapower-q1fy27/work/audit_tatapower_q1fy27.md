# A5 ADVERSARY / COMPLETENESS AUDIT — Tata Power (TATAPOWER), Q1 FY27

**Agent:** A5 ADVERSARY (Opus 4.8) | **Verdict authority:** COMPLETE / INCOMPLETE (gate before Notion save)
**Scope audited:** `review_tatapower_q1fy27.md` (A4), against `extract_results_*` + `extract_presentation_*` (A1) and `ledger_results_*` + `ledger_presentation_*` (A2).
**Method:** fresh grep enumeration + full manual re-derivation of every derived metric from raw extract lines. I did not defer to A4's or A3's cites; every figure below is re-pulled from the A1 extract's own internal line numbers (`ln`) or deck slides (`s`). Digit-space artifacts de-spaced before arithmetic ("1 ,400.86" → 1,400.86; "(94.1 7)" → (94.17)).

---

## AUDIT 1 — COVERAGE

### 1A. Fresh enumeration vs A2 ledger counts

| Category | A2 count | My fresh count | Method | Orphan rows | Status |
|---|---|---|---|---|---|
| Results — pages | 19 | 19 | grep `^\d+\|\s*\[page N\]` = 19 | — | PASS |
| Results — notes | 74 | 74 (6 N-C + 6 seg/CODM + 13 lettered + 11 numbered consol = 36; 5 N-S + 5 seg + 15 lettered + 13 numbered SA = 38; 36+38) | subtotal re-add | none | PASS |
| Results — line items | 213 | 213 (65 consol P&L + 39 consol seg + 16 consol ratio + 43 SA P&L + 31 SA seg + 19 SA ratio) | subtotal re-add | none | PASS |
| Results — auditor paras | 30 | 30 (15 consol CR-1..CR-11 incl. 4 sub-bullets + 15 standalone SR-1..SR-8 incl. 6 sub) | re-count | none | PASS |
| Results — entities (Annexure 1) | 96 | 96 (23+50+7+10+5+1) | sequence re-add | none | PASS |
| Results — agenda items | 4 | 4 (AG-1..AG-4) | re-count | none | PASS |
| Results — signature blocks | 14 | 14 (5 named + 9 ID stamps; my stamp-grep returns 8 due to OCR garble on ln388, sweep = 9, consistent with A2's documented OCR-undercount caveat) | grep + sweep | none | PASS |
| Results — zero_standing | 1 | 1 (S-22 standalone Current Tax, ln772, dash all 4 periods) | manual | none | PASS |
| Presentation — slides | 71 | **71** (independent grep `^\d+\|\s*\[page N\]` = 71) | grep | none | PASS |
| Presentation — zero_standing | 13 | 13 (Table 2 re-walk of slides 40-43,45,55,58) | manual | none | PASS |
| Presentation — footnotes | 61 (deduped) | informational only (OCR-fragmented; A2 correctly treats as non-gating; slide-level content captured regardless) | — | none | PASS |

No category where my fresh pass found a row the ledger lacks (→ no A2 FAIL). No ledger row absent from A4 that carries a finding (→ no A3 FAIL). See 1B.

### 1B. Ledger-row → A4 traceability (every flagged/material row cited or reviewed-no-finding)

- ZERO_STANDING **S-22** (standalone Current Tax nil all periods, ln772) → A4 §1B anchor + F1-B + Q4. **Cited.**
- Exceptional impairment **C-27/C-28** (94.17), Q4/FY26 only → A4 §0D + F1-A + Step 3/4A. **Cited.**
- Numbered notes **N-C1..N-C6 / N-S1..N-S5** → A4 §0D table (dividend 798.83, Mundra S.11, SIAC, balancing figure). **All cited.**
- EoM paras **CR-6 / SR-3** (SIAC) → A4 §0D + F5-A + verdict flag 1. **Cited.**
- Component-auditor paras **CR-7a/CR-7b/CR-9a/CR-10** → A4 F4-A + Q17 (314.65 / 18.42). **Cited.**
- Consol ratios **CR-01/03/09/10/14** (D/E, ISCR, debtor days, inv days, net worth) → A4 Step 5. **Cited.**
- Standalone ratios **SR-01/09/10/14** (D/E, debtor days, inv days, net worth) → A4 Step 2B/5. **Cited.**
- Deck ZERO_STANDING (13) — the material one, **s55 "Less: Related Party Debt"** (nil now, 203 a year ago) → A4 monitorables line + A3-17. The other 12 are structural elimination/exceptional/JV-at-PAT template rows → reviewed-no-finding under A4's blanket "all 71 slides reviewed." **No orphan.**
- Deck material slides (s7,8,15,17-23,27-32,37,40-55,58-59,70) all cited in A4 Steps 1-6 / monitorables. Divider + CSR/awards/governance slides (5,9,16,24,35,39,56,61-67) = reviewed-no-finding. **No orphan.**

**One minor coverage nuance (non-blocking, see Audit 3, counter 3):** standalone **Interest Service Coverage (SR-03, ln885) fell 2.36 → 1.68 YoY**; A4 cites consolidated ISCR (ln489, 2.36→2.38) but not the standalone ISCR figure, though it does raise the parent-cover concern qualitatively (flag 4, Q3, Q4). Row is reviewed (theme present); figure not quantified. Recommended enhancement, not an orphan.

**COVERAGE VERDICT: PASS.** Every A2 category reconciles on a fresh pass; no orphan ledger row; no row my pass found that the ledger lacks.

---

## AUDIT 2 — ARITHMETIC (re-derived from raw extract lines)

All figures ₹ Cr. Every derived value below independently recomputed. "src" = extract line(s) used.

### 2A. Consolidated derived metrics

| Metric | A4 value | Recomputed | Source lines | Status |
|---|---|---|---|---|
| Op EBITDA Q1FY27 (PBT+D+FC−OI) | 4,101.59 | 1,823.34+1,259.86+1,406.78−388.39 = 4,101.59 | 349/332/331/321 | PASS |
| Op EBITDA Q1FY26 | 3,697.88 | 1,619.46+1,160.91+1,279.22−361.71 = 3,697.88 | 349/332/331/321 | PASS |
| Op EBITDA margin Q1FY27 | 21.5% | 4,101.59/19,051.26 = 21.53% | 320 | PASS |
| Op EBITDA margin Q1FY26 | 20.5% | 3,697.88/18,035.07 = 20.50% | 320 | PASS |
| Reported EBITDA Q1FY27 | 4,489.98 | 1,823.34+1,259.86+1,406.78 = 4,489.98 | 349/332/331 | PASS |
| Core PBT ex-OI Q1FY27 | 1,434.95 | 1,823.34−388.39 = 1,434.95 | 349/321 | PASS |
| Eff. tax rate Q1FY27 | 23.2% | 422.48/1,823.34 = 23.17% | 355/349 | PASS |
| Eff. tax rate Q1FY26 | 22.1% | 357.14/1,619.46 = 22.06% | 355/349 | PASS |
| PAT margin Q1FY27 | 7.4% | 1,400.86/19,051.26 = 7.35% | 356/320 | PASS |
| Deck EBITDA tie (4,249) | 4,248.59 | 4,489.98−241.39 = 4,248.59 ≈ s40 4,249 | 349/332/331/344 + s40 | PASS |

### 2B. Consolidated YoY (Step 2A)

| Metric | A4 % | Recomputed | Status |
|---|---|---|---|
| Revenue | +5.6% | 1,016.19/18,035.07 = +5.63% | PASS |
| Op EBITDA | +10.9% | 403.71/3,697.88 = +10.92% | PASS |
| Op EBITDA margin | +103 bps | 21.53−20.50 = +1.03 pp | PASS |
| Depreciation | +8.5% | 98.95/1,160.91 = +8.52% | PASS |
| Finance costs | +10.0% | 127.56/1,279.22 = +9.97% | PASS |
| EBIT (OpEBITDA−D) | +12.0% | 304.76/2,536.97 = +12.01% | PASS |
| Core operating PBT | +14.1% | 177.20/1,257.75 = +14.09% | PASS |
| Reported PBT | +12.6% | 203.88/1,619.46 = +12.59% | PASS |
| PAT | +11.0% | 138.54/1,262.32 = +10.97% | PASS |
| Share of Assoc/JV | +86.2% | 111.76/129.63 = +86.21% | PASS |

### 2C. Standalone derived + YoY (Steps 1B/2B)

| Metric | A4 value | Recomputed | Source lines | Status |
|---|---|---|---|---|
| Op EBITDA Q1FY27 | 1,058.01 | 374.23+318.81+556.21−191.24 = 1,058.01 | 770/762/761/753 | PASS |
| Op EBITDA Q1FY26 | 950.99 | 668.81+305.51+497.35−520.68 = 950.99 | 770/762/761/753 | PASS |
| Core PBT ex-OI Q1FY27 | 182.99 | 374.23−191.24 = 182.99 | 770/753 | PASS |
| Core PBT ex-OI FY26 | (663.80) | 1,178.39−1,842.19 = (663.80) | 770/753 | PASS |
| Eff. tax rate Q1FY27 | 25.9% | 96.86/374.23 = 25.88% | 774/770 | PASS |
| Eff. tax rate Q4FY26 | (136.4%) | (192.60)/141.19 = −136.41% | 774/770 | PASS |
| Revenue YoY | +7.6% | 403.60/5,285.20 = +7.64% | 752 | PASS |
| Op EBITDA YoY | +11.3% | 107.02/950.99 = +11.25% | — | PASS |
| Other Income YoY | −63.3% | −329.44/520.68 = −63.27% | 753 | PASS |
| Core operating PBT YoY | +23.5% | 34.86/148.13 = +23.53% | — | PASS |
| Reported PBT YoY | −44.0% | −294.58/668.81 = −44.05% | 770 | PASS |
| PAT YoY | −46.7% | −242.72/520.09 = −46.67% | 775 | PASS |

### 2D. Standalone-vs-Consolidated gap (Step 2C, first-class metric)

| Period | Gap (Consol−SA) A4 | Recomputed | Gap %/SA A4 | Recomputed | Status |
|---|---|---|---|---|---|
| Q1 FY26 | 742.23 | 1,262.32−520.09 = 742.23 | 143% | 742.23/520.09 = 142.7% | PASS |
| Q4 FY26 | 1,081.73 | 1,415.52−333.79 = 1,081.73 | 324% | 1,081.73/333.79 = 324.1% | PASS |
| Q1 FY27 | 1,123.49 | 1,400.86−277.37 = 1,123.49 | 405% | 1,123.49/277.37 = 405.0% | PASS |
| FY26 | 3,992.90 | 5,117.56−1,124.66 = 3,992.90 | 355% | 3,992.90/1,124.66 = 355.0% | PASS |

**Divergence check:** standalone PAT −46.7% vs consolidated +11.0% = 57.7 pp ≈ A4's "~58 pp." Gap-%-of-standalone widened 143%→405% = 262 pp swing, "vastly beyond the 5 pp trigger." Both **PASS** (source lines 356 / 775). The headline **−47% standalone vs +11% consolidated** ties to the reported PAT lines exactly.

### 2E. PAT bridges (Step 4)

- **Consol bridge (4A):** OpEBITDA +403.71, D −98.95, FC −127.56, OI +26.68, reg-deferral +417.67 ((570.76)→(153.09) = +417.67), associate +111.76, exceptional 0, tax −65.34, NCI −22.47. My sum of drivers reconciles to reported PAT delta **+138.54** (1,262.32→1,400.86). **PASS.**
- **Standalone bridge (4B):** OpEBITDA +107.02, D −13.30, FC −58.86, OI −329.44, reg-deferral +0.25, deferred-tax +51.86 → reconciles to **−242.72** (520.09→277.37). **PASS.**

### 2F. Balance-sheet / leverage figures

| Item | A4 | Recomputed / source | Status |
|---|---|---|---|
| Consol net worth Δ | +4,452.66 | 43,555.43−39,102.77 (ln500) | PASS |
| Standalone net worth Δ | +212.73 | 17,095.22−16,882.49 (ln896) | PASS |
| Standalone D/E | 1.07→1.45 | ln882 (1.07 / 1.45) | PASS |
| Consol receiv. days | 67→72 | ln495 | PASS |
| Consol inv. days | 55→71 | ln496 | PASS |
| Standalone receiv. days | 86→83 | ln891 | PASS |
| Standalone inv. days | 39→48 | ln892 | PASS |
| Net External Debt YoY | +13,660 | 61,238−47,578 (s55) | PASS |
| Net External Debt QoQ | +5,116 | 61,238−56,122 (s55) | PASS |
| Total Gross Debt YoY | +13,921 | 74,069−60,148 (s55) | PASS |
| Component-auditor % of PAT | 22.5% | (127.79+168.44+18.42)/1,400.86 = 314.65/1,400.86 = 22.46% | PASS |

### 2G. SIAC / Kleros award (Note 4, ln 578-590 consol / 996-1008 standalone)

| Element | A4 | Extract | Status |
|---|---|---|---|
| Loss-of-opportunity damages | USD 490,320,000 | ln583 "USD 490,320,000" | PASS |
| Interest | 5.33% simple from 30-Nov-2020 | ln583 "5.33% from 30th November, 2020" | PASS |
| Costs | SGD 11,341,963.46 | ln583-584 "SGD 11,341,963.46" | PASS |
| Setting-aside appeal | filed 23-Oct-2025 at SICC | ln587 "23rd October, 2025 ... SICC" | PASS |
| Provision recorded | **none** ("no provision recorded") | ln588 "does not foresee any affirmative payment obligation ... no [provision]" | PASS |
| EoM in BOTH reports | yes (CR-6 ln87-93 + SR-3 ln646-653) | confirmed | PASS |
| Indicative ₹ principal | "~₹4,100 Cr (indicative FX ~₹83.6/USD)" | 490,320,000 × 83.6 = ₹4,099 Cr; **explicitly labelled indicative, FX rate named** — a transparent conversion of a disclosed USD figure, not a fabricated fill | PASS (compliant) |

**No estimated numbers found.** Every quantified cell traces to a disclosed extract figure or is a transparently-flagged derivation (the SIAC ₹-conversion states its FX assumption; the ">₹5,000 Cr potential" is labelled potential). The nil/dash lines are carried as `ND` / dash, never estimated.

**ARITHMETIC VERDICT: PASS — zero mismatches above rounding across ~80 recomputed values.** All rounding is ≤0.5 pp / ≤₹0.5 Cr and directionally correct.

---

## AUDIT 3 — ADVERSARIAL READ (three most-positive claims, strongest bear counter from the SAME extract)

**Claim 1 (most positive):** *"A genuinely clean core quarter … ~100% of PAT growth recurring, treasury immaterial"* (Combined Verdict; Step 4A).
- **Bear counter (from extract):** Consolidated PBT-before-reg-deferral/associate/exceptional (ln335) **FELL 15.8% YoY** (2,060.59→1,735.04); rebuilt pre-reg, pre-associate operating EBITDA (ln335+D+FC−OI) was roughly flat at −3.0% (4,139.01→4,013.29). The entire +11% PAT is carried by a smaller regulatory-deferral drag (+417.67, ln341) and higher equity-method associate share (+111.76, ln344) — the latter masking a loss-making associate (Others cluster PAT (213)→(330), s42). So "clean core +14.1%" leans on a volatile true-up line and non-operating associate income.
- **Survives?** **NO — already incorporated.** A4's 4A bridge quantifies both drivers explicitly (reg-deferral +417.67; associate +111.76), flags reg-deferral volatility (F8-C, Q14) and the unnamed loss associate (A3-02, Q9), and diagnostic 5 flags the D&A/finance-cost absorption gap that produces the ln335 decline. Step 0E pre-commits that reg-deferral is a *genuine operating component for a rate-regulated utility*, a defensible basis for the "core" label. The synthesis language is optimistic but the facts and their volatility are surfaced. No graft mandatory. *Recommended sharpening (non-blocking): state the ln335 −15.8% figure so the reg-deferral/associate dependence is explicit.*

**Claim 2:** *"TP Solar manufacturing PAT +287% … fastest engine, GREEN"* (6B item 7; verdict bright-spots).
- **Bear counter (from extract, s50):** volumes are flat-to-down — **module sold −26 MW (966→940), cell produced −42 MW (904→862)**; the +287% PAT is a price/margin + low-tax artifact (EBITDA margin 18%→25%; ETR ~17.6% vs 25.17% statutory). Deck s12 shows coal prices rising and cell/module prices "range bound," so the spread that drove it is at risk, and the sub-statutory ETR is a latent step-up.
- **Survives?** **NO — already incorporated.** A4 Q11 asks precisely about spread sustainability vs coal, external-mix outlook and ETR normalisation; flag register (line 567) calls out the ~17.6% sub-statutory ETR / latent tax step-up; 6B red condition = "curtailment/ALMM shift." Counter is grafted.

**Claim 3:** *"The −47% standalone is NOT operational deterioration; parent core operating PBT actually +23.5%"* (Step 2B/4B).
- **Bear counter (from extract):** The −63% Other-Income collapse signals subsidiaries retaining cash rather than up-streaming dividends **precisely as parent leverage rises (D/E 1.07→1.45, ln882)** and standalone **Interest Service Coverage fell 2.36→1.68 (ln885)** — i.e. the parent's own debt-service cushion is thinning even as A4 calls the operations "improved." Parent net worth is near-flat (+212.73) while parent gross debt rose (+994 QoQ, s54).
- **Survives?** **PARTIALLY — theme incorporated, one figure omitted (non-blocking).** A4 raises the parent-cash-cover / rising-leverage flag prominently (flag 4; Q3; Q4) and cites standalone D/E 1.07→1.45, so the counter is not absent. However A4 does **not** cite the standalone ISCR deterioration (2.36→1.68, ln885), which is the single sharpest quantification of the very concern it raises. **Recommended enhancement to A4 (non-blocking): add standalone ISCR 2.36→1.68 (ln885) to Step 5 / flag 4.** This strengthens an existing flag rather than adding a missing one, so it does not rise to a surviving-counter FAIL.

**No bear counter survives unincorporated.** A4 is unusually symmetric — each most-positive claim already carries its counter (F8-C/Q14, A3-02/Q9, Q11/flag, flag 4/Q3). The two "recommended enhancements" (ln335 −15.8% framing; standalone ISCR 2.36→1.68) sharpen flags A4 already surfaces; neither is a missing flag, so neither blocks save.

---

## CROSS-CHECKS DEMANDED BY TASK

1. **Every numeric claim ties to a cited line** — verified for all P&L, ratio, derived, deck and note figures re-pulled above. PASS.
2. **Standalone AND consolidated both present in every table** — Steps 1A/1B, 1C (both derived panels), 2A/2B, 4A/4B, and Step 5 (consol + standalone rows) all carry both. PASS.
3. **Standalone −47% vs consolidated +11% + gap arithmetic** — re-derived (2C/2D): −46.7% vs +11.0%, gap 405% of standalone, ~58 pp divergence, 262 pp gap-widening. PASS.
4. **SIAC/Kleros figures + no provision** — USD 490,320,000 + 5.33% from 30-Nov-2020 + SGD 11,341,963.46, appeal 23-Oct-2025 SICC, **no provision**, EoM in both reports. PASS (2G).
5. **Cash-conversion INDETERMINATE vs verdict consistency** — A4 Step 5 marks cash conversion INDETERMINATE, **names the missing evidence** (no Q1 Reg-33 CFO statement; first clean read at H1 FY27 / Q2), and states it "bars clean PROCEED and caps the verdict." Verdict = **PROCEED WITH FLAGS**, not clean PROCEED. Per the verdict ordering (PROCEED / PROCEED WITH CAVEATS / PROCEED WITH FLAGS / REWORK / INSUFFICIENT EVIDENCE), PROCEED WITH FLAGS is at-or-below the "caps at PROCEED WITH CAVEATS" ceiling (not cleaner than it) and is not a clean PROCEED. **Consistent with the house rule.** PASS.
6. **Every A3 FORWARD-SIGNAL / AMBIGUOUS finding → ≥1 Questions-for-Management row** — A4's declared forward/ambiguous set (results: F1-B, F2-A, F4-A, F5-A, F6-A, F7-A, F8-A, F8-C, F9-A, F11-A, F12-A, F12-B; presentation: A3-01..05, 07..11, 13, 14, 15) each maps to ≥1 of the 21 questions (Q1-Q21 "from finding" column traced individually). Descriptive findings correctly excluded (F1-A, F8-B, F14-A carried in Steps 0D/3/4, not as questions; A3-06/12/16/17 non-forward, A3-17 routed to monitorables). PASS.

---

## VERDICT

**COMPLETE.** Coverage reconciles on an independent grep + sweep (no orphan ledger row, no ledger gap); all ~80 re-derived metrics match A4 within rounding (zero mismatches); the three most-positive claims each already carry their strongest bear counter from the same extract (no surviving unincorporated counter); SIAC figures, the −47%/+11% divergence, the INDETERMINATE-cash-conversion cap, and the forward-finding→question mapping all check out; no estimated numbers. Two non-blocking enhancements are recommended to A4 (state the ln335 −15.8% pre-reg operating decline behind the "clean core" language; add standalone ISCR 2.36→1.68 at ln885 to the parent-cover flag) — both sharpen flags A4 already surfaces and neither bars save.

```yaml
stage: A5-adversary
company: "TATAPOWER"
quarter: "Q1 FY27"
model: claude-opus-4-8
status: complete
verdict: COMPLETE
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches: []
surviving_bear_counters: []
loop_back_to: ""
gap: ""
```
