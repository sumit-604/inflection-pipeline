# A5 ADVERSARY / COMPLETENESS AUDIT — GNG Electronics Limited (EBGNG) — Q1 FY27

Quarter ended June 30, 2026. Audited 2026-07-30. Model: claude-opus-4-8.
Fresh context: only the A4 review, A1 extracts, and A2 ledgers were seen. Every A4 cite was re-derived, not trusted.
Raw source of truth: results filing in Rs Million (x0.1 = Rs Cr); deck already in Rs Cr. Column order in filing = Q1FY27 | Q4FY26 | Q1FY26 | FY26. A4 table order = Q1FY26 | Q4FY26 | Q1FY27 | FY26.

---

## AUDIT 1 — COVERAGE (fresh enumeration vs A2 ledgers)

Method: independent grep passes over both extracts plus a manual row-by-row sweep, diffed against the two A2 ledgers.

| Category | A2 count | My fresh count | Orphan / missing rows | Status |
|---|---|---|---|---|
| Agenda items (results) | 1 | 1 | none | PASS |
| Line items standalone (results) | 21 | 21 | none | PASS |
| Line items consolidated (results) | 22 | 22 | none | PASS |
| Line items total (results) | 43 | 43 | none | PASS |
| Notes (results, 5S+5C) | 10 | 10 (L317-333 / L683-711) | none | PASS |
| Auditor paras (5S+7C) | 12 | 12 | none | PASS |
| Consolidation entities | 6 | 6 (L452,453-4,455,456-7,458-9,460-1) | none | PASS |
| Signature blocks | 5 | 5 | none | PASS |
| Slides (deck) | 8 | 8 (grep `^\[page` = 8) | none | PASS |
| Slide 7 income-statement line items | 16 | 16 | none | PASS |
| Slide 5 embedded KPIs | 6 | 6 | none | PASS |
| Slide 6 chart KPIs | 10 | 10 | none | PASS |
| Absent-disclosure categories (deck) | 5 | 5 | none | PASS |

Notes on the fuzzy line-item grep: a keyword regex returned 45 raw hits vs 43; the +2 are regex double-matches on multi-word labels ("comprehensive income" matching both the OCI-total and TCI rows), NOT extra rows. Manual sweep of both P&Ls confirms exactly 21+22=43 distinct rows with the ledger's anchors. The subsidiary grep returned 7 hits; line 474 is the auditor-para-6 textual reference, not a 7th entity — the entity LIST is 6 (FZC + 5 US step-downs).

**Ledger-row-vs-A4 cross-check (orphan test):** every substantive ledger row is either cited in A4 or covered by A4's blanket "all reviewed" preamble (A4 L13-21) with specific downstream treatment:
- All 43 P&L rows → A4 Steps 1A/1B full tables (every cell anchored).
- 10 notes → A4 Step 0D table (all 5S+5C).
- 12 auditor paras / unmodified opinion → A4 Step 0D.
- 6 entities → A4 FND-04 (FZC component-review + US step-downs unaudited) and FND-08 (Electronic Bazaar B.V. jurisdiction).
- Diluted>Basic EPS rows → FND-06 (Q9).
- Deck slide 5 (Redington, EB Elite, 49 countries, 5,100 touchpoints) → monitorables + Q6/Q7.
- Deck absent-disclosure A.1-A.5 (balance sheet, cash flow, segment split, debt/WC, FY27 guidance) → Step 5 + Note 3 + Q8/Q10.
- A2 open items: (a) B.V. jurisdiction → FND-08 ✓; (d) no prior deck → A4 notes it ✓. Item (b) garbled director-name/DIN/UDIN source-fidelity flags are NOT financial findings and fall under the blanket "reviewed"; not an orphan.

**COVERAGE VERDICT: PASS.** No orphan ledger row (would loop A3); no row my fresh pass found that the ledger lacks (would loop A2). GATE A2 counts independently reproduced.

---

## AUDIT 2 — ARITHMETIC (recomputed from raw Million figures, x0.1)

All values Rs Cr unless stated. Source lines are the results-extract line numbers.

### 2A. Consolidated — load-bearing metrics (the ones the task flagged)

| Metric | A4 value | Recomputed | Source lines | Status |
|---|---|---|---|---|
| Gross Profit Q1FY27 = Rev−DirCost−Δinv = 412.46−272.65−38.16 | 101.65 | 101.65 | L560/577/582 | PASS |
| Gross Margin Q1FY27 | 24.6% | 101.654/412.461 = 24.65% | L560,577,582 | PASS |
| Gross Margin Q4FY26 (with +23.68 Δinv add-back) | 19.2% | 125.262/651.655 = 19.22% | L561,578,583 | PASS |
| Gross Margin Q1FY26 | 21.4% | 66.704/312.279 = 21.36% | L562,579,584 | PASS |
| **Falsification test: consol GM vs 17% line** | 24.6% > 17%, NOT breached | 24.65% > 17% confirmed | L560,577,582 | PASS — claim TRUE |
| Op EBITDA Q1FY27 = PBT+D+Fin−OI = 35.74+3.28+13.86−3.51 | 49.37 | 49.37 | L614,597,592,565 | PASS |
| Op EBITDA margin Q1FY27 | 12.0% | 11.97% | — | PASS |
| Reported EBITDA (deck) Q1FY27 = PBT+D+Fin | 52.88 | 52.878 (deck 52.9) | L614,597,592 | PASS |
| Effective Tax Rate Q1FY27 = 6.81/35.74 | 19.1% | 19.06% | L631,614 | PASS |
| ETR Q1FY26 / Q4FY26 / FY26 | 17.6/9.1/10.6% | 17.58/9.12/10.64% | L631,614 cols | PASS |
| PAT margin Q1FY27 | 7.0% | 28.93/412.461 = 7.01% | L637,560 | PASS |
| Revenue YoY | +32.1% | 412.461/312.279−1 = 32.08% | L560,562 | PASS |
| Op EBITDA YoY | +52.8% | 52.78% | — | PASS |
| Op EBITDA margin YoY | +162 bps | +162 bps | — | PASS |
| Core PBT (ex-OI) YoY = 32.23/19.62−1 | +64.3% | 64.30% | L614,565 | PASS |
| Reported PBT YoY | +59.1% | 59.06% | L614 | PASS |
| PAT YoY | +56.2% | 56.21% | L637 | PASS |
| Revenue QoQ | −36.7% | 412.461/651.655−1 = −36.71% | L560,561 | PASS |
| PAT QoQ | −31.4% | −31.36% (deck −31.3%) | L637,638 | PASS |
| GM QoQ swing | +542 bps | 24.65−19.22 = +542 bps | — | PASS |

### 2B. Standalone-vs-consolidated PAT gap (task-flagged)

| Metric | A4 value | Recomputed (C−S) | Source lines | Status |
|---|---|---|---|---|
| Subsidiary PAT Q1FY26 | 8.34 | 18.52−10.18 = 8.34 | L637,275 | PASS |
| Subsidiary PAT Q4FY26 | 30.02 | 42.15−12.13 = 30.02 | L637,275 | PASS |
| Subsidiary PAT Q1FY27 | 12.99 | 28.93−15.94 = 12.99 | L637,275 | PASS |
| Subsidiary PAT FY26 | 92.09 | 132.02−39.93 = 92.09 | L637,275 | PASS |
| Sub PAT % of consol Q1FY27 | 44.9% | 12.99/28.93 = 44.91% | — | PASS |
| Consol PAT QoQ vs standalone PAT QoQ | −31.4% / +31.4% | −31.36% / +31.38% | L637,275 | PASS |
| Subsidiary revenue QoQ | −48.1% | 182.71/352.33−1 = −48.14% | — | PASS |

### 2C. Standalone GM YoY direction (task-flagged claim)

| Metric | A4 value | Recomputed | Source lines | Status |
|---|---|---|---|---|
| Standalone GM Q1FY26 = (172.14−230.37+92.12)/172.14 | 19.7% | 33.891/172.138 = 19.69% | L198,215,220 | PASS |
| Standalone GM Q1FY27 = (229.76−264.36+75.41)/229.76 | 17.8% | 40.803/229.756 = 17.76% | L198,215,220 | PASS |
| **Standalone GM YoY** | −193 bps (contracted) | −193 bps confirmed | L198,215,220 | PASS — claim TRUE |
| **Consol GM YoY** | +329 bps (expanded) | 24.65−21.36 = +329 bps | L560,577,582 | PASS — claim TRUE |
| Standalone Op EBITDA Q1FY27 | 29.10 | 21.98+2.12+8.52−3.51 = 29.10 | L252,235,230,203 | PASS |
| Standalone Core PBT ex-OI Q1FY27 | 18.47 | 21.98−3.51 = 18.47 | L252,203 | PASS |
| Standalone ETR Q1FY27 | 27.5% | 6.04/21.98 = 27.48% | L269,252 | PASS |

### 2D. PAT bridge (Step 4, consolidated YoY) — fully re-derived

Volume +21.40 (100.18 rev delta × 21.36% prior GM) + margin +13.55 (3.29pp × 412.46) = +34.95 gross-profit delta (ties to GP 101.65−66.70 = 34.95 ✓); less opex −17.89 = Op EBITDA +17.05 ✓ (49.37−32.31); +OI 0.66 = Rep EBITDA +17.71 ✓; −D 1.24 −Fin 3.20 = PBT +13.27 ✓ (35.74−22.47); −tax 2.86 = **PAT +10.41 ✓** (28.93−18.52). Bridge reconciles end-to-end.

### 2E. Deck (Rs Cr) vs filing (Rs Million x0.1) cross-check
412.5≈412.46, GP 101.7≈101.65, EBITDA 52.9≈52.88, PBT 35.7≈35.74, PAT 28.9≈28.93, tax 6.8≈6.81; YoY 32.1%/50.4%/52.4%/59.1%/56.2% and QoQ −36.7%/−17.3%/−22.9%/−31.3% all reconcile within rounding. Deck EBITDA is the REPORTED (PBT+D+Fin) definition, 12.8%; A4 correctly separates it from Operating EBITDA (ex-OI) 12.0%. No unit-conversion error.

### 2F. THE ONE MISMATCH

| Metric | A4 value | Recomputed | Source lines | Status |
|---|---|---|---|---|
| **Standalone Operating EBITDA, FY26 column** (Table 1D) = PBT 53.20 + D 7.41 + Fin 26.40 − OI 4.96 | **81.96** | **82.06** (53.204+7.414+26.396−4.955 = 82.059) | L252,235,230,203 (FY26 col) | **FAIL** |

Discrepancy = 0.10 Cr (Rs ~1M), which exceeds A4's own two-decimal display precision, so it is above rounding. There is no rounding path to 81.96 even from 1-decimal inputs (which give 82.0–82.05); it is a keying slip. **Impact is immaterial to every conclusion:** it is a FY26 (prior full-year) standalone reference cell used nowhere downstream; the derived FY26 standalone Op-EBITDA margin is unchanged at 8.9% (82.06/917.50 = 8.94% vs A4's 81.96/917.50 = 8.93%, both → 8.9%), and no YoY, QoQ, PAT-bridge, S-vs-C, falsification, or verdict figure depends on it. Fix = replace 81.96 with 82.06 in Table 1D. Because the mandate is "any mismatch above rounding = FAIL, discrepancy shown," this is recorded as an arithmetic FAIL looped to A4.

Minor secondary note (not a FAIL): A4's "EPS share-adjusted +56.6%" (L164) should equal PAT YoY +56.2% by construction (identical 11.401 Cr share base both periods); the 0.4pp gap is a rounding artifact of dividing the rounded 2.54/1.62 prints. Underlying PAT +56.2% is stated correctly; no correction required, flagged for A4 awareness only.

**ARITHMETIC VERDICT: FAIL (one cell).** All task-flagged load-bearing metrics — consolidated GP/GM, the 24.6% print and 17% falsification test, EBITDA (both definitions), ETR, YoY/QoQ percentages, the S-vs-C PAT gap, and the standalone-contracts / consolidated-expands GM claim — are independently confirmed CORRECT. The sole defect is the FY26 standalone Operating-EBITDA cell.

---

## AUDIT 3 — ADVERSARIAL READ (three most positive claims + strongest bear counter from the same extract)

**Positive claim 1 (L433, L314, L327): "Consolidated gross margin EXPANDED to 24.6%, decisively NOT breaching the 17% falsification line — the single most load-bearing test passed."**
Strongest bear counter from the extract: the 24.6% print sits against revenue −36.7% QoQ; at Q4-scale volume (651.7 Cr) GM was only 19.2%, and the quarter carried a group inventory DRAWDOWN (Δinv +38.16, L582) versus builds in prior quarters — i.e. the high GM is co-incident with low volume and a sell-through quarter. Parent GM contracted to 17.8% (only ~80 bps above the 17% line). So the 24.6% durability at volume is unproven and the group print could compress toward high-teens if the offshore true-up reverses.
**Survives?** Yes, supported by the extract — BUT already grafted into A4 (A3-09; Step 3 QoQ diagnostics L205; monitorable #3; Step 8.5 Q2; Step 6D "durability unproven"). No new addition required.

**Positive claim 2 (L232, L433): "The +10.41 Cr YoY PAT gain is ~100% recurring core; headline growth is real with no Other-Income mask."**
Strongest bear counter from the extract: ~45% of Q1 consolidated PAT (12.99 of 28.93; rising to ~70% at Q4/FY) originates in offshore subs whose figures are only component-reviewed (Electronics Bazaar FZC, by NBN) or UNAUDITED/management-furnished (five US step-downs, auditor para 6, L474-480). "Recurring core" quality is only as good as unaudited management numbers. Additionally, consolidated ETR (19.1%) is structurally below the ~25% statutory rate because of low-taxed foreign earnings and rose YoY from 17.6% — a mean-reverting forward PAT headwind not reflected in the "100% recurring" framing.
**Survives?** Yes — BUT already grafted (FND-04 audit-coverage gap, Step 5S read 3; FND-05 ETR headwind, Step 4, Q5; offshore concentration throughout). No new addition required.

**Positive claim 3 (L167, L317, L433): "Revenue +32.1% YoY and EBITDA margin +156 bps both BEAT the FY27 guide rails — a clean beat, GREEN on monitorable #6."**
Strongest bear counter from the extract: the "~25% revenue / ~50 bps" rails are prior-record MEMORY, not management guidance; the deck discloses NO explicit FY27 numeric guidance (absent-disclosure A.5; A3-04) — so "beat vs guide" measures actuals against an unverified internal rail. The YoY base (Q1 FY26) is a pre-scale/pre-IPO quarter, and sequentially the quarter is DOWN −36.7% off a Q4 that is itself a derived balancing figure (Note 4) with undisclosed seasonality. A +32% YoY that is −37% QoQ off an unexplained peak is not an unambiguous "beat."
**Survives?** Yes — BUT already grafted (Step 6A explicitly labels the rails as memory and the per-quarter projections ND; Q8 requests numeric guidance; the −36.7% QoQ and Note-4 balancing-figure caveats run through Steps 3, 6A, 8.5 Q1). No new addition required.

**ADVERSARIAL VERDICT:** all three bear counters survive on the extract but are ALREADY incorporated in A4's review. No surviving counter is missing; nothing must be newly grafted (no loop to A4 on this axis).

---

## VERDICT

**INCOMPLETE.** Loop back to **A4**.

- COVERAGE: PASS (counts reproduced; no orphan or missing rows).
- ARITHMETIC: one FAIL — Table 1D FY26 standalone Operating EBITDA reads **81.96**; recomputed **82.06** (PBT 53.204 + D 7.414 + Fin 26.396 − OI 4.955, source L252/235/230/203 FY26 column). Above two-decimal rounding, therefore a mandated FAIL, even though immaterial to every downstream conclusion (FY26 standalone Op-EBITDA margin unchanged at 8.9%; no YoY/QoQ/bridge/falisification/verdict figure depends on it).
- ADVERSARIAL: all three bear counters already present in A4; nothing to graft.

Every task-flagged load-bearing claim is independently CONFIRMED: consolidated GM 24.6% is correct and does NOT breach the 17% falsification line; standalone GM contracted YoY (−193 bps to 17.8%) while consolidated expanded (+329 bps to 24.6%); EBITDA (both definitions), ETR, YoY/QoQ percentages, the S-vs-C PAT gap, and the full PAT bridge all reconcile. A4 must correct the single FY26 standalone Op-EBITDA cell (81.96 → 82.06) and re-emit; on that correction the review is otherwise complete and sound.

```yaml
stage: A5-adversary
company: "EBGNG"
quarter: "Q1 FY27"
model: claude-opus-4-8
status: complete
verdict: INCOMPLETE
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches:
  - metric: "Standalone Operating EBITDA, FY26 column (Table 1D)"
    a4_value: "81.96"
    recomputed: "82.06"
    source_line: "results L252/235/230/203 (FY26 col): PBT 53.204 + D 7.414 + Fin 26.396 - OI 4.955 = 82.059"
surviving_bear_counters: []
loop_back_to: "A4"
gap: "Table 1D FY26 standalone Operating EBITDA reads 81.96; correct value is 82.06 (0.10 Cr, above rounding). Immaterial to every conclusion (FY26 standalone Op-EBITDA margin unchanged at 8.9%) but a mandated arithmetic FAIL; A4 must correct the cell and re-emit. All load-bearing metrics independently confirmed correct."
```

---

## LOOP-1 RESOLUTION (orchestrator stamp, 2026-07-30)

The single arithmetic FAIL (Table 1D FY26 standalone Operating EBITDA 81.96 vs correct 82.06 Rs Cr) was looped back to A4. A4 corrected the cell to 82.06 — the exact value A5 independently computed in this audit — and re-emitted the review; the FY26 standalone Op-EBITDA margin is unchanged at 8.9% and no downstream conclusion moves. A5's own audit had confirmed all other coverage and arithmetic correct and found no surviving bear counter. With the sole gap closed to the adversary's independently-derived figure, the audit resolves to:

**VERDICT (post loop-1): COMPLETE.** Loop count 1 of max 2. Proceed to save/report.
