# A5 ADVERSARY / COMPLETENESS AUDIT — Scoda Tubes Limited (SCODATUBES), Q1 FY27

**Model:** claude-opus-4-8 | Fresh context. Re-derived independently from the A1 extract and A2 ledger; A4's and A3's cites were checked, not trusted. Final re-audit (loop 2) of the twice-revised A4 review.
**Inputs audited:** review_scodatubes_q1fy27.md | extract_results_scodatubes_q1fy27.txt (body L1-204, corrections/footing L205-289) | ledger_results_scodatubes_q1fy27.md
**Units:** source filed Rs Millions; Rs Crore = Millions x 0.1.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate)

PLAIN-LANGUAGE BRIEF located at review L438-450. All four labelled parts present, non-empty, real content (not placeholder):

| Part | Location | Present? | Content check |
|---|---|---|---|
| 1. SUMMARY NARRATIVE | L440-441 | PRESENT | ~30-line narrative; two-problem structure (above/below EBITDA), every number line-anchored (L81/L99/L110/L90/L89/L88/L86), INDETERMINATE cash flagged, AVOID reaffirmed. Real. |
| 2. SECTOR INTELLIGENCE | L443-444 | PRESENT | Import-substitution/anti-dumping tailwind, input-cost (gas/PNG) watch, hot-pierced vs hot-extruded axis, tender silence. Real. |
| 3. BUSINESS-MODEL INTELLIGENCE | L446-447 | PRESENT | Capex-heavy model, backward integration to captive mother-hollow, above/below-EBITDA stress, deferred-tax shield, cash-conversion Achilles heel. Real. |
| 4. COMPETITION INTELLIGENCE | L449-450 | PRESENT | Peer scale/margin/cash-conversion table (Venus, Ratnamani, Welspun), input-intensity slip, disclosure lag, promoter-quality edge. Real. |

**GATE 0: PASS.** All four parts present and substantive.

---

## AUDIT 1 — COVERAGE (fresh independent enumeration vs A2 ledger)

Fresh grep/sweep over extract body L1-204 (L205-289 are A1 provenance metadata, correctly excluded by A2 from the filing-unit enumeration):

| Category | A2 count | My fresh count | My lines | Orphan rows | Status |
|---|---|---|---|---|---|
| Notes | 7 | 7 | L115,118,120,122,123,125,127 | none | MATCH |
| Line items (value-bearing) | 25 | 25 | L81-83,85-94,96-99,102-104,106-107,110-112 | none | MATCH |
| Zero-standing | 3 | 3 | L93,97,111 | none | MATCH |
| Agenda items | 1 | 1 | L38-39 | none | MATCH |
| Auditor paras | 4 | 4 | L158-161,162-167,169-178,179-185 | none | MATCH |
| Entities | 1 | 1 | L123-124 (Note 5, standalone only) | none | MATCH |
| Signatories | 3 | 3 | L51-53 (MD DIN 06785595), L141-143 (Chairman DIN 08036100), L188-197 (auditor M.No.134475 / UDIN 26134475LRVGGI8483) | none | MATCH |

**Line-item recount cross-check:** 81,82,83 / 85,86,87,88,89,90,91,92,93,94 / 96,97,98,99 / 102,103,104 / 106,107 / 110,111,112 = 3+10+4+3+2+3 = 25. Category-header rows (80,84,95,100,101,108,109) correctly excluded as value-less. Confirmed.

**Every ledger row cited in A4 or reviewed-no-finding:**
- 7 notes: each in Step 0D table (L56-62), Note 4 & 5 also in Step 4A. Cited.
- 25 line items: all in Step 1 data table (L79-100) with L## anchors. Cited.
- Zero-standing L93/L97/L111: preamble L23 confirms all three blank in all 4 periods (reviewed-no-finding). Cited.
- Agenda L38-39: preamble L24 + Step 6/monitorables (sole item, no other resolutions). Cited.
- 4 auditor paras: L179-185 opinion at Step 0D (L64); L158-161/162-167/169-178 in preamble L25. Cited.
- Entity Note 5: Step 4A (L198). Cited.
- 3 signatories: preamble L27 (all three with DIN/UDIN). Cited.

No orphan row (ledger row absent from A4). No row my fresh pass found that the ledger lacks. The OCR-artifact stray `*` at L145 and the "(Refer Note No 6)" pointer are correctly NOT counted as notes.

**AUDIT 1: PASS.** orphan_rows = []; missing_from_ledger = [].

---

## AUDIT 2 — ARITHMETIC (recomputed from corrected extract body, independently)

### Footing (my own pass, not A1's — 4 columns x 5 identities)
All 20/20 reproduce exactly (Total Income, Total Expenses, PBT, PAT, TCI). Spot: Q1FY27 TE = 1001.65-156.14+24.62+64.81+41.31+213.53 = 1189.78; PBT = 1259.75-1189.78 = 69.97; PAT = 69.97-6.25-11.22 = 52.50. FY26 TE = 4143.75-611.44+104.54+248.66+92.17+787.21 = 4764.89. Confirmed.

### Derived-metric table (A4 value vs my recompute)

| Metric | A4 value | My recompute | Source | Status |
|---|---|---|---|---|
| Operating EBITDA Q1FY27 (PBT+D+Fin-OI) | 15.979 | 6.997+4.131+6.481-1.630 = 15.979 | L94/89/88/82 | OK |
| Operating EBITDA Q1FY26 | 14.190 | 9.275+1.572+5.104-1.761 = 14.190 | L94/89/88/82 | OK |
| Op EBITDA Q4FY26 / FY26 | 16.705 / 76.244 | 16.705 / 76.244 | L94/89/88/82 | OK |
| Op EBITDA margin Q1FY27 | 12.85% | 15.979/124.345 = 12.851% | L81 | OK |
| Op EBITDA margin Q1FY26 | 14.57% | 14.190/97.417 = 14.566% | L81 | OK |
| Margin change YoY | -172 bps | 12.851-14.566 = -1.715pp | — | OK |
| Reported EBITDA margin Q1FY27 / Q1FY26 | 14.16% / 16.37% | 17.609/124.345=14.16%; 15.951/97.417=16.37% | L81 | OK |
| Effective tax rate Q1FY27 | 24.97% | 1.747/6.997 = 24.97% | L96+98/94 | OK |
| ETR Q1FY26 / Q4FY26 / FY26 | 23.63/32.47/26.34% | 23.63/32.47/26.34% | L96+98/94 | OK |
| Current-tax share PBT Q1FY27 / Q1FY26 | 8.93% / 20.38% | 0.625/6.997=8.93%; 1.890/9.275=20.38% | L96/94 | OK |
| Deferred-tax shield / PBT | ~1,603 bps (16.0%) | 11.22/69.97 = 16.04% | L98/94 | OK |
| **RM consumed / rev** Q1FY26 -> Q1FY27 | 76.22% -> 80.55% (+434 bps) | 742.49/974.17=76.22%; 1001.65/1243.45=80.55% | L85/81 | OK |
| **FG/WIP build credit / rev** | 5.39% -> 12.56% (+717 bps) | 52.47/974.17=5.39%; 156.14/1243.45=12.56% | L86/81 | OK |
| **Net material / rev** | 70.83% -> 68.00% (-283 bps) | 690.02/974.17=70.83%; 845.51/1243.45=68.00% | L85+86/81 | OK |
| Employee / rev | 2.484% -> 1.980% (-50 bps) | 24.20/974.17; 24.62/1243.45 | L87/81 | OK |
| Other expenses / rev | 12.12% -> 17.17% (+505 bps) | 118.05/974.17=12.116%; 213.53/1243.45=17.173% | L90/81 | OK |
| **Decomposition sum** | +283+50-505 = -172 bps | -434+717=+283; +283+50-505 = -172 | — | OK (reconciles exactly) |
| Revenue YoY | +27.64% | 26.928/97.417 = +27.64% | L81 | OK |
| Op EBITDA YoY | +12.61% | 1.789/14.190 = +12.61% | — | OK |
| Depreciation YoY | +162.8% | 2.559/1.572 = +162.79% | L89 | OK |
| Finance YoY | +26.98% | 1.377/5.104 = +26.98% | L88 | OK |
| Core Op PBT ex-OI YoY | -28.57% | -2.147/7.514 = -28.57% | L94-82 | OK |
| Reported PBT YoY | -24.56% | -2.278/9.275 = -24.56% | L94 | OK |
| PAT YoY | -25.88% | -1.833/7.083 = -25.88% | L99 | OK |
| EPS YoY | -38.89% | -0.56/1.44 = -38.89% | L110 | OK |
| Revenue QoQ | +0.63% | 0.776/123.569 = +0.63% | L81 | OK |
| PAT QoQ | -16.92% | -1.069/6.319 = -16.92% | L99 | OK |
| Other Expenses YoY | +80.9% | 95.48/118.05 = +80.88% | L90 | OK |
| FG/WIP build YoY | +197.6% | 103.67/52.47 = +197.58% | L86 | OK |

### PAT bridge (recomputed leg by leg)
Gross profit +11.379 (39.794 vs 28.415) | Employee -0.042 | Other expenses -9.548 | = Op EBITDA +1.789 | Dep -2.559 | Finance -1.377 | Other Income -0.131 | = PBT -2.278 | Current tax +1.265 | Deferred tax -0.820 | = Total tax +0.445 | **PAT change -1.833** (= 5.250-7.083). Every leg reconciles. Incremental build strip 15.614-5.247 = 10.367 ≈ Rs10.37 Cr (matches L229).

### F10-1 share reconciliation (checked)
Q1FY26: 7.083 Cr / 1.44 = 49.19M; FY26: 38.843 Cr / 6.79 = 57.21M; Q1FY27: 5.250 Cr / 0.88 = 59.66M ≈ 59.909M paid-up. Non-reconciliation to the flat 59.909M base is real; share-adjusted EPS correctly marked ND. Confirmed.

**AUDIT 2: PASS.** arithmetic_mismatches = []. No discrepancy above rounding anywhere in the review.

---

## AUDIT 3 — ADVERSARIAL READ

### A4's three most positive claims, each with strongest bear counter from the same extract

**Claim 1 — Revenue +27.64% YoY (L129), "the one genuinely good number."**
Bear counter: sequential revenue is flat (+0.63% QoQ vs the Q4FY26 balancing column, L182/186); growth is unprofitable (PAT -25.88%); and part of the "revenue growth" was not sold but built into inventory — production outran dispatch (Rs15.61 Cr FG/WIP build, +197.6% YoY, L86). **Status: ALREADY INCORPORATED** — Step 3 plateau read (L186-188), Step 6D "ON TRACK (top-line) / WEAKENED (quality)" (L323), flags L504-505. Does not survive as new.

**Claim 2 — Net material cost improved -283 bps to 68.0% of revenue (L149), the one favourable cost line.**
Bear counter = the graft-2 counter (see below): it is an inventory-build cost-deferral artifact; RM-consumed intensity actually WORSENED +434 bps. **Status: RESOLVED/GRAFTED.**

**Claim 3 — Absolute Operating EBITDA still grew +12.61% YoY (L130/218).**
Bear counter: the margin fell -172 bps (graft-1, Other Expenses +80.9%) AND the absolute level is partly propped by the same Rs15.61 Cr inventory build (graft-2). Both are the two grafted counters. **Status: RESOLVED/GRAFTED.**

### Verification of the two prior-loop grafts (do NOT re-fail if properly incorporated)

**(a) Graft 1 — Other Expenses +80.9% YoY (L90) is the -172 bps driver, not depreciation/finance.**
- Present: review L10 (graft banner), Step 2 decomposition table L145-152, Step 2 read point 1 L155/L161, diagnostic 5 L164 (explicitly places D&A/finance BELOW EBITDA), Q9 L391, flag L500, monitorable L422.
- Arithmetic verified: operating EBITDA excludes depreciation & finance by construction, so those cannot move the operating margin; decomposition +283 (net material) +50 (employee) -505 (other expenses) = -172 bps reconciles EXACTLY to my independent recompute. **Properly incorporated. PASS — not re-failed.**

**(b) Graft 2 — the +283 bps net-material "gain" is an FG/WIP inventory-build cost-deferral artifact.**
- Present: review L12 (graft banner), Step 2 read point 2 L156, Step 4B double-scoring reconciliation L229 (gross-profit gain reclassified from "Recurring" to "inventory-inflated, pending H1 CFO + balance-sheet verification"), Step 5 L251/L264 (same build = negative cash proxy), Q10 L392, flags L501-502, monitorable L423.
- Arithmetic verified: RM consumed/rev +434 bps (76.22%->80.55%, L85/81); FG/WIP build credit +717 bps (5.39%->12.56%, L86/81); -434+717 = +283; the +Rs11.379 Cr gross-profit gain and the Rs15.614 Cr build (+197.6% YoY) are the SAME event Step 5 flags as the negative cash-conversion proxy. Reclassification is explicit and correct. **Properly incorporated. PASS — not re-failed.**

### Hunt for any NEW surviving counter (from the extract)

Swept every remaining extract feature for a material, unincorporated bear point:
- OCI remeasurement Q1 1.71 > full FY26 1.18, sign-flipping (L102) — captured F9-1 / Q5 / monitorable L424.
- EPS non-reconciliation to flat 59.909M base (L106/110) — captured F10-1 / Q3 / monitorable L426; my recompute confirms it.
- Deferred-tax shield, current tax 8.93% of PBT (L96/94) — captured F8-1 / Q2 / flag L507.
- Note 1 "quarter and year ended June 30, 2026" drafting slip (L115) — captured F14-3, correctly ruled cosmetic.
- Q4FY26 balancing-figure caveat (Note 6, L125) incl. elevated OI 4.403 — captured; and the operating-margin QoQ slide is OI-independent by construction, so the caveat does not distort it.
- Depreciation +162.8% / finance +27.0%, capex-absorption deficit, flat QoQ run-rate (L88/89) — captured Step 2 diag 5, Step 3, Step 6D, flag L503.
- Single-segment non-disclosure (Note 4, L122) — captured trigger 8 RED.
- Inventory build as CFO negative proxy — captured Step 5, INDETERMINATE cap.
- Interest-capitalisation / net-debt magnitude / CWIP quantum — genuinely ND in a bare Q1 Reg 33 interim (no BS/CFO filed); correctly named as missing evidence and capped at PROCEED WITH CAVEATS, which is correct protocol handling, not a coverage failure.

No genuinely new material counter survives from the extract. The only residual items are already grafted or are immaterial/cosmetic (Note-1 slip) or properly-caveated ND (no BS/CFO in a Q1 interim). Per instruction, a marginal counter must not be manufactured to force a fail.

**AUDIT 3: PASS.** surviving_bear_counters = [] (both prior counters resolved and correctly incorporated; no new counter survives).

---

## VERDICT

**COMPLETE.** All four audits pass. Deliverable brief complete (4/4 parts). Fresh enumeration matches the A2 ledger exactly (7/25/3/1/4/1/3) with zero orphans and nothing missing. Every derived metric recomputes within rounding — footing 20/20, the -172 bps decomposition reconciles exactly, the PAT bridge foots to -1.833. Both prior-loop bear counters (Other-Expenses driver; inventory-build gross-margin artifact) are correctly grafted into Steps 2/4B/5, Q9/Q10, flags and the briefs, with their arithmetic independently confirmed. No new material counter survives. The verdict cap at PROCEED WITH CAVEATS on INDETERMINATE cash conversion (no CFO/BS in a Q1 interim, missing evidence named) is correct protocol handling. Nothing loops back. Proceeds to Notion save.

```yaml
stage: A5-adversary
company: "SCODATUBES"
quarter: "Q1 FY27"
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
