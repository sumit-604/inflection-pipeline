# A5 ADVERSARY / COMPLETENESS AUDIT — TRUALT Q1 FY27

Auditor: A5 ADVERSARY | Model: claude-opus-4-8 | Date: 2026-07-29
Run: **LOOP-1 RE-AUDIT** (prior A5 returned INCOMPLETE→A4; A4 applied 4 corrections). Max 2 loops.
Scope seen: A4 review (restated), A1 extracts (results/presentation/press release/chairman), A2 ledgers (results, presentation). Re-derived independently; A4/A3 cites checked, not trusted.

Units: results Rs Lakhs ×0.01 → Cr; presentation/press/chairman Rs Cr ×1.

---

## PART 0 — VERIFICATION OF THE THREE PRIOR-LOOP GAPS (independent re-derivation)

| Prior gap (loop 0) | A4 restated value | My independent recompute (raw) | Verdict |
|---|---|---|---|
| (a) Standalone QoQ PAT should be −14.9% not −13.9% | −14.9% (change log; Step 3; Q1; Step 7; verdict) | Std PAT Q4FY26 6,462.13L → Q1FY27 5,500.64L: (5,500.64−6,462.13)/6,462.13 = **−14.87% → −14.9%**. Consolidated distinct: (5,927.14−6,883.95)/6,883.95 = **−13.90%** | **RESOLVED** — corrected everywhere; cons/std now separated (change log #1, Step 3, Q1-table, Step 7 cross-check, Combined Verdict). No surviving instance of std −13.9%. |
| (b) A3 F14b deck-vs-filing segment-PBT reconciliation | Incorporated: Step 1E (L146-163), S-vs-C reading pt.2 (L443-449), Q16, FLAG DECK_VS_FILING_SEGMENT_PBT, monitorable #15 | Reviewed CBG PBT 166.02L→513.52L = **+209.3%**; CBG PAT 137.51L→426.55L = **+209.5%**. Reviewed base split Eth 413.93L=4.14 / CBG 166.02L=1.66 vs deck Eth 0.02 / CBG 5.90 → **opposite base**, ethanol gap 4.14−0.02 = **4.12**. Reviewed Ind AS 108 authoritative. | **RESOLVED** — contradiction correctly stated, reviewed number wins, prior "subsidiary shrinking" conclusion withdrawn, nuance added (CBG Segment Result flat 9.29→9.24, PBT rise from lower allocated charges). |
| (c1) Margin: 6% edge cannot fully explain +751 bps; residual utilisation-dependent | Downgraded CONFIRMED→PARTIAL (change log #3; Step 2 diag 2; Step 4; Step 7; FLAG MARGIN_ATTRIBUTION_PARTIAL) | +751 bps = 21.18−13.67 ✓. Ceiling 0.06×0.65 = 3.9pp ✓. Residual 7.51−3.9 = **3.61pp**, tied to utilisation 60.57% ✓ | **RESOLVED** — arithmetic shown, labelled reversible. |
| (c2) Base quarter NOT operationally loss-making; Segment Result Q1FY26 = +84.14 Cr | Corrected (change log #4; 1D note; Step 2 diag 3; Step 2A/2B; FLAG BASE_QTR_NOT_LOSS_MAKING) | Q1FY26 Segment Result = Eth 7,485.04L + CBG 929.19L = 8,414.23L = **+84.14 Cr positive** ✓; the (16.94)/(22.43) "ex-OI" figure correctly re-read as a net-of-everything artefact | **RESOLVED** — no longer read as an operating loss anywhere; "sign flip" tagged "artefact metric." |

All three prior gaps independently confirmed correctly resolved.

---

## AUDIT 1 — COVERAGE (fresh enumeration diffed against A2 ledgers)

| Category | A2 count | My fresh count | Orphan / missing | Status |
|---|---|---|---|---|
| Results — numbered notes | 12 | 12 (cons L308/312/314/316/386/388; std L574/578/580/583/585/587) | none | PASS |
| Results — financial line items | 67 | 67 (cons 37 + std 30; incl. OCI subtotal L253 & OCR "(bl" L213) | none | PASS |
| Results — ZERO_STANDING | 3 | 3 (cons Excep L236; std Excep L531; std Current Tax L534) | none; surfaced (F1/F8, no-exceptional bridge) | PASS |
| Results — board agenda items | 1 | 1 (L50-53); "inter-alia" = chairman doc, separate filing | none | PASS |
| Results — auditor paragraphs | 11 | 11 (cons 6 + std 5) | none; EoM + unmodified-review cited (F5, Step 0D) | PASS |
| Results — consolidation entities | 3 | 3 (TruAlt Bioenergy, Leafiniti, TruAlt Gas) | none; Leafiniti trace → Q11 (F3/F15) | PASS |
| Results — segment sub-tables | 4 | 4 (4A L326-333, 4B L337-340, 4C L345-352, 4D L356-359) | none; reconciled Step 1E (F14b) | PASS |
| Results — signature blocks | 5 | 5 | none (OCR-illegible UDIN immaterial to review) | PASS |
| Presentation — slides | 32 | 32 (`^\[page ` = 32) | none; "ALL 32 reviewed" | PASS |
| Presentation — structured line items | 47 | 47 (B1-B6: 6+5+7+8+14+7) | none | PASS |
| Presentation — mgmt numbers | 104 | 104 (Table C: 3+8+11+3+11+12+10+10+7+4+6+3+4+3+5+3+1) | none | PASS |
| Presentation — ZERO_STANDING | 1 | 1 (CBG Unit-1 Strategic Partner = NA, B3.1) | operational Leafiniti unit needs no JV partner; immaterial | PASS |

**Orphan-row sweep (ledger flags absent from A4):** every material flag surfaced — LABEL_INCONSISTENCY→F14; EPS_FORMAT→0C/1A; Note 5 restatement→0D/Step 3; Unit-4 EoM→F5; Unit-4 300>200→Q7/FLAG; QoQ/YoY LABEL_ERROR→F14/Q15/FLAG; DDGS AMBIGUOUS_PERIOD→Q10/mon.14; Phase-I 3-of-4→Q5/FLAG; Bhima Patas undated→Q14/mon.7; PRIOR_LEDGER_UNAVAILABLE→fresh-coverage framing. **No material orphan.**
**Immaterial non-cited items (do not fail):** consolidated NCI-OCI value present only in Q1FY27 (L267, 0.85L ≈ Rs 85k); CBG Unit-1 NA partner. Both covered by the A4 "ALL reviewed" preamble; non-decision-relevant.
**Rows my fresh pass found that the ledger lacks:** none.

**AUDIT 1 VERDICT: PASS.**

---

## AUDIT 2 — ARITHMETIC (every derived metric recomputed from raw extract)

| Metric (period) | A4 value | Recomputed | Source | Status |
|---|---|---|---|---|
| Op EBITDA cons 26/27/Q4/FY | 41.54/132.76/129.31/300.30 | 5.80+20.69+37.79−22.74; 78.45+24.80+44.03−14.52; 94.25+22.95+43.50−31.39; 140.50+86.23+160.02−86.45 | L237/228/226/213 | MATCH |
| Op EBITDA margin cons 26/27 | 13.67%/21.18% | 41.54/303.89; 132.76/626.88 (+751 bps) | L211 | MATCH |
| Op EBITDA std 26/27/Q4/FY | 34.88/126.61/141.52/293.68 | 0.13+20.06+37.25−22.56; 73.31+24.23+43.52−14.45; 89.55+22.43+42.94−13.40; 120.02+84.09+157.85−68.28 | L532/527/526/519 | MATCH |
| Op EBITDA margin std 26/27 | 11.87%/20.56% | 34.88/293.93; 126.61/615.92 (+869 bps) | L518 | MATCH |
| Core PBT ex-OI cons 26/27/Q4 | (16.94)/63.93/62.86 | 5.80−22.74; 78.45−14.52; 94.25−31.39 | L237/213 | MATCH |
| OI/PBT cons 26/Q4/27 | 392.1%/33.31%/18.51% | 22.74/5.80; 31.39/94.25; 14.52/78.45 | L213/237 | MATCH |
| ETR cons 26/Q4/27/FY | 18.45/26.96/24.44/25.44% | 1.07/5.80; 25.41/94.25; 19.17/78.45; 35.74/140.50 | L239/237 | MATCH |
| ETR std Q1FY26 | 84.6% | 0.11/0.13 | L533/532 | MATCH |
| PAT margin cons 26/Q4/27/FY | 1.56/11.56/9.45/6.06% | 4.73/303.89; 68.84/595.52; 59.27/626.88; 104.76/1727.51 | L245/211 | MATCH |
| YoY rev cons/std | +106.3%/+109.5% | 626.88/303.89−1; 615.92/293.93−1 | L211/518 | MATCH |
| YoY Segment Result cons | +179.4% (84.14→235.09) | 8,414.23L→23,508.57L | L348/329 | MATCH |
| YoY EBIT std | +590.8% (14.82→102.38) | 102.38/14.82−1 | derived | MATCH |
| YoY reported PBT std | +55,481% | (7,331.09−13.19)/13.19 (exact-lakh base) | L532 | MATCH |
| YoY PAT std | +213,933% | (5,500.64−2.57)/2.57 | L536 | MATCH |
| **QoQ PAT cons** | **−13.9%** | (5,927.14−6,883.95)/6,883.95 = −13.90% | L245 | MATCH |
| **QoQ PAT std** | **−14.9%** | (5,500.64−6,462.13)/6,462.13 = −14.87% | L536 | MATCH (prior gap fixed) |
| QoQ rev / core PBT ex-OI cons | +5.3%/+1.7% | 626.88/595.52−1; 63.93/62.86−1 | L211/derived | MATCH |
| PAT bridge cons (80.87/−8.22/72.65/18.10/54.54) | as stated | 63.93−(−16.94); 14.52−22.74; 78.45−5.80; 19.17−1.07; 59.27−4.73 | L237/213/239/245 | MATCH |
| S-vs-C PAT gap 26/Q4/27/FY (& %) | 4.70/99.4; 4.22/6.13; 4.26/7.19; 16.84/16.07 | 4.73−0.03; 68.84−64.62; 59.27−55.01; 104.76−87.92 (÷cons PAT) | L245/536 | MATCH |
| F14b CBG PBT YoY | +209% (1.66→5.14) | 513.52/166.02−1 = +209.3% | L350/331 | MATCH |
| Segment foot PBT/PAT | 78.45 / 59.28≈59.27 | 73.31+5.14; 55.01+4.27 (0.01 rounding) | L331/333/237/245 | MATCH |
| Margin attribution ceiling/residual | ≤3.9pp / ~3.6pp | 0.06×0.65=3.9; 7.51−3.9=3.61 | pres L335/338 | MATCH |

**Minor prose inaccuracies found (NOT in any metric table; do NOT change a value or conclusion; IMMATERIAL / verdict-neutral):**
1. Step 2 diag 6 (L218): "OI was ~7× reported PBT" (Q1FY26). Correct = 22.74/5.80 = **3.92×** (already stated correctly as 392% in the same sentence and table 1C). Recommend "~7×" → "~3.9×".
2. Step 1E cross-tie (L165): "OI was ~55% of reported EBITDA." 55% is OI/**operating** EBITDA (22.74/41.54 = 54.7%); vs **reported** EBITDA 64.28 it is 35.4%. Recommend "of operating EBITDA."

Both are cosmetic characterizations sitting beside the correct derived figure; no table cell, YoY/QoQ %, bridge, margin, ETR, or the verdict depends on them. Per the materiality gate these are not a NEW material gap. Surfaced for optional clean-up at save.

**AUDIT 2 VERDICT: PASS** (all derived-metric-table values reconcile to the paisa/rounding; two immaterial prose slips noted).

---

## AUDIT 3 — ADVERSARIAL READ (3 most positive claims; strongest counter from the SAME extract)

**Positive claim 1 — "Revenue more than doubled YoY (cons +106.3%, std +109.5%); genuine operating scale-up (Segment Result +179%, positive in both periods)."**
Bear counter (same text): Sequentially the platform has already plateaued — QoQ revenue only +5.3% and core PBT ex-OI +1.7%, while **reported PAT FELL QoQ (cons −13.9%, std −14.9%)**; both compared quarters are distorted by inventory timing (Q4FY26 build −243.52; Q1FY27 draw +47.69, L222) and a restated Q4 Other-Expenses base (Note 5, +10.54). **SURVIVES? NO — fully grafted:** Step 3 states the plateau, the QoQ PAT decline (both bases), and inventory/Note-5 distortions; Step 8C sets sequential core PBT ex-OI as the cleanest next test.

**Positive claim 2 — "Operating EBITDA margin expanded +751 bps (cons)/+869 bps (std), OI-independent."**
Bear counter (same text): The ~6% grain edge on ~65% capacity explains ≤3.9pp; the ~3.6pp residual is fixed-cost absorption at 60.57% utilisation and reverses if utilisation/ESY allocations slip; utilisation is unverifiable from the reviewed filing. **SURVIVES? NO — this IS incorporated bear counter #1:** Step 2 diag 2, Step 4, Step 7, FLAG MARGIN_ATTRIBUTION_PARTIAL, plus Q9 on the ESY-vs-demand constraint.

**Positive claim 3 — "Reported PAT +1,153% on a clean bridge (~100% recurring; OI fell, no exceptionals, no tax credit); CBG segment PBT actually rose +209% (deck's 'dip' contradicted)."**
Bear counter (same text): The +1,153%/+213,933%/+334,424% optics are near-zero-*net*-base artefacts collapsing from Q2; 100% of tax is deferred (std current tax zero every period, L534) so cash tax ≈ 0 with a DTL/cash-tax step-up building; and the "+209% CBG" rebuttal is itself soft — CBG **Segment Result was flat** (9.29→9.24 on +12.5% revenue) with EBITDA margin compressing 66.74%→55.64% (deck), so CBG PBT rose only via lower allocated charges, not operating gain; CBG capex leads revenue (segment assets +279% YoY on +12.5% revenue). **SURVIVES? NO — all grafted:** NEAR_ZERO_BASE_OPTICS flag + A3-F16-02; DEFERRED_TAX_100PCT flag + Q2; S-vs-C reading pt.2 (CBG Segment Result flat, margin compression); CBG_CAPEX_BEFORE_REVENUE flag + Q4.

**No new surviving bear counter.** Every strongest counter constructible from the extract is already present in the restated A4.

**AUDIT 3 VERDICT: PASS** (no un-incorporated surviving counter).

---

## VERDICT

**COMPLETE.**

- All three loop-0 gaps independently re-derived and confirmed correctly resolved (standalone QoQ PAT −14.9% distinct from consolidated −13.9%; F14b reviewed CBG PBT +209% contradiction incorporated with the reviewed figure authoritative; margin attribution downgraded to PARTIAL with arithmetic; base quarter reframed as NOT operationally loss-making, Segment Result +84.14 Cr).
- Coverage: every ledger row cited or blanket-reviewed; no orphan, no missing row.
- Arithmetic: every derived-metric-table value reconciles to raw lakhs within rounding. Two immaterial prose slips ("OI ~7× reported PBT" → ~3.9×; "~55% of reported EBITDA" → of operating EBITDA) surfaced for optional clean-up — verdict-neutral, no table or conclusion affected.
- Adversarial read: no new surviving bear counter; the three strongest counters are already grafted.

No NEW material gap. Proceeds to Notion save.

```yaml
stage: A5-adversary
company: "TRUALT"
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
