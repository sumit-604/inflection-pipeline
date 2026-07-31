# A5 ADVERSARY / COMPLETENESS AUDIT — Ram Ratna Wires Ltd (RAMRAT), Q1 FY27
# Fresh-context audit of A4 review. Re-derived independently from A1 extracts + A2 ledgers.
# Reviewed 2026-07-31 | model claude-opus-4-8

Independence note: I re-derived every count and every derived metric from the raw extract
lines (results filing reports in ₹ Lakhs; ÷100 to ₹ Cr). I did not defer to A4's or A3's
cites; where A4 cites a finding ID I checked the underlying extract row it points to.

---

## 1. COVERAGE AUDIT

Fresh grep/sweep re-enumeration of each A1 extract, diffed against the A2 ledger counts, then
each flagged ledger row traced into A4.

| Category | A2 count | My fresh count | Method / reconciliation | Orphan rows | Status |
|---|---|---|---|---|---|
| results — notes | 19 | 19 | SA 8 roman (L262,267,273,276,281,292,295,298) + SA asterisk EPS fn (L202) = 9; CN 9 roman (L586,591,595,600,605,609,619,622,624) + CN asterisk EPS fn (L523) = 10; 17 roman + 2 asterisk = 19 | none | PASS |
| results — line_items | 121 | 121 | SA P&L 29 (L166-200) + SA segment 25 (L222-252) + CN P&L 37 (L474-522) + CN segment 30 (L541-576) = 121 | none | PASS |
| results — zero_standing | 3 | 3 | SA OCI B(i) L191, SA OCI B(ii) L192, CN OCI B(ii) L506 (dash in all shown periods) | none | PASS |
| results — agenda_items | 1 | 1 | Board letter L30-33 (single item: approve Q1 results); "inter alia" hedge, nothing else named | none | PASS |
| results — auditor_paras | 15 | 15 | SA LRR 4 narrative blocks (L81-130) + CN LRR 11 units (L330-438) | none | PASS |
| results — entities | 3 | 3 | TPPL (L381), EEPL (L383), RRIEL (L385); cross-checks CN Note iii (L595-598) | none | PASS |
| results — signature_blocks | 5 | 5 | L52, L136, L304, L444, L628 (all "Digitally signed") | none | PASS |
| presentation — slides | 31 | 31 | `[page N]` markers 1-31, sequential, no gaps | none | PASS |
| presentation — numeric points | 530 | 530 (spot-verified) | Slide-level subtotals sum to 530; verified Slides 5 (31), 7 (41), 27 (22), 28 (9), 29 (84), 30 (176) directly against extract | none | PASS |
| presentation — footnotes | 8 | 8 | Section C: 3 qualifying fns (Slides 9,27,28) + 5 source-citation lines (Slides 20,21,23,24,25) | none | PASS |
| pressrelease — units | 50 | 50 | summary-table 5 (L80-84) + quantified claims 11 + MD forward phrases 18 + structural units 16 | none | PASS |
| turns (concall) | 0 | 0 | no transcript filed/supplied — Role 5 correctly N.A. | n/a | PASS |

**Flagged-row trace (the rows most at risk of being orphaned):**
- results ZERO_STANDING (3 nil OCI reclassification rows): immaterial nil lines; covered by A4's
  blanket "121 line items — all reviewed." No independent finding warranted. Not orphaned.
- results LABEL_INCONSISTENCY — SA Capital-Employed row 22 reads "Enamelled wires and strips"
  (L249) vs "Winding wires and strips" everywhere else: carried into A4 M8 governance flag
  ("label/entity inconsistencies (A3-10, FND-05)"). Cited.
- presentation LABEL_AMBIGUITY Slide 5 (H1 header over full-year values, L146/153): A4 FND-08 /
  QFM Q14. Cited.
- presentation LABEL_AMBIGUITY Slide 27 dividend ("5.0#" on FY26 bar L778 vs footnote FY23-24
  L789): this was the A2 orphan flag. A4 documents it was folded into FND-05 by the first A3
  pass, then explicitly reviewed via a post-A5 A3 revision as **FND-12** / QFM Q16 / M8 /
  monitorable. Now cited — no longer orphaned.
- presentation EMERGING_LINE_ITEM Slide 29 (first-ever ₹3.6 Cr exceptional after 3 nil years,
  L844): A4 FND-01 / QFM Q11. Cited.
- presentation SIGNATURE_TIMESTAMP Slide 1: immaterial; no board-time to cross-check in this
  doctype. Reviewed, no finding.
- pressrelease "continued improvement in working capital efficiency" asserted with zero metric
  (L100): A4 A3-F6-01/A3-F17-01 / QFM Q1 / Role-5 carry-forward. Cited.
- pressrelease 26% copper-mix UNVERIFIABLE_STANDALONE (L94): A4 notes the filing segment note
  discloses the absolute (489.98 Cr, L223) so the narrative omission is framing, not a data gap.
  Cited.
- pressrelease ROUNDING (₹90/₹35/+89%/+121% vs table 89.6/35.2/88.6%/120.8%): A4 deck-accuracy
  reconciliation (Step 1D cross-check). Cited.

**A3-findings incorporation count check:** A4 lists 31 (results A3-01..A3-11 = 11; presentation
FND-01..FND-12 = 12; pressrelease 8). 11+12+8 = 31. Internally consistent with the YAML
`a3_findings_incorporated` array (31 entries).

**Fresh-pass rows the ledger lacks:** none. Every row I enumerated appears in the corresponding
A2 ledger; no undercount forcing a loop-back to A2.

**Coverage verdict: PASS.** No orphan rows (none in ledger yet absent from A4); no missing rows
(none in my fresh pass yet absent from ledger).

---

## 2. ARITHMETIC AUDIT

Every mandated derived metric recomputed from raw extract Lakhs (÷100). "src" = results-extract
line for the raw inputs unless noted.

### 2A. Standalone derived (A4 §1C)
| Metric (period) | A4 value | Recomputed | Source lines | Status |
|---|---|---|---|---|
| Op EBITDA = PBT+D+FC−OI (Q1FY27) | 87.49 | 47.64+11.77+30.36−2.28 = 87.49 | L181,175,174,167 | PASS |
| Op EBITDA (Q1FY26) | 39.85 | 20.67+7.66+15.41−3.89 = 39.85 | L181,175,174,167 | PASS |
| Op EBITDA (Q4FY26) | 90.28 | 57.72+11.87+26.85−6.16 = 90.28 | same cols | PASS |
| Op EBITDA (FY26, +3.33 excep add-back) | 250.98 | 154.42+35.09+80.72−19.25 = 250.98 | L178,175,174,167 | PASS |
| Op EBITDA margin (Q1FY27) | 4.78% | 87.49/1831.99 = 4.78% | L166 | PASS |
| ETR = Tax/PBT (Q1FY27) | 22.92% | 10.92/47.64 = 22.92% | L186,181 | PASS |
| ETR (Q1FY26) | 29.66% | 6.13/20.67 = 29.66% | L186,181 | PASS |
| ETR (Q4FY26) | 30.68% | 17.71/57.72 = 30.68% | L186,181 | PASS |
| ETR (FY26) | 28.31% | 42.77/151.09 = 28.31% | L186,181 | PASS |
| Core PBT ex-OI (Q1FY27) | 45.36 | 47.64−2.28 = 45.36 | L181,167 | PASS |
| PAT margin (Q1FY27) | 2.00% | 36.72/1831.99 = 2.00% | L187,166 | PASS |

### 2B. Consolidated derived (A4 §1D)
| Metric (period) | A4 value | Recomputed | Source lines | Status |
|---|---|---|---|---|
| Op EBITDA = PBTbeforeJV+D+FC−OI (Q1FY27) | 89.59 | 47.51+12.77+31.65−2.34 = 89.59 | L487,483,482,475 | PASS |
| Op EBITDA (Q1FY26) | 42.88 | 22.18+8.25+16.12−3.67 = 42.88 | same cols | PASS |
| Op EBITDA (Q4FY26) | 93.21 | 58.76+12.64+27.83−6.02 = 93.21 | same cols | PASS |
| Op EBITDA (FY26, +3.56 excep) | 263.61 | 160.42+37.87+83.82−18.50 = 263.61 | L487,483,482,475 | PASS |
| Op EBITDA margin (Q1FY27) | 4.83% | 89.59/1853.28 = 4.83% | L474 | PASS |
| Reported EBITDA (FY26) | 278.55 | 156.86+37.87+83.82 = 278.55 (post-excep PBTbJV) | L490-492 | PASS |
| ETR (Q1FY27) | 23.72% | 1093.13/4609.48 = 23.72% | L499,494 | PASS |
| ETR (Q1FY26) | 28.88% | 6.47/22.40 = 28.88% (rounded-Cr); raw 647.42/2239.66 = 28.91% | L499,494 | PASS (rounding) |
| ETR (Q4FY26) | 31.65% | 18.16/57.38 = 31.65% | L499,494 | PASS |
| ETR (FY26) | 29.01% | 44.37/152.97 = 29.01% | L499,494 | PASS |
| Core PBT ex-OI (Q1FY27) | 43.75 | 46.09−2.34 = 43.75 | L494,475 | PASS |
| PAT margin (Q1FY27) | 1.90% | 35.16/1853.28 = 1.90% | L500,474 | PASS |

### 2C. YoY % (A4 §2A/2B) and QoQ (A4 §3)
| Metric | A4 value | Recomputed | Status |
|---|---|---|---|
| CN Revenue YoY | +88.6% | (1853.28−982.47)/982.47 = 88.63% | PASS |
| CN Op EBITDA YoY | +108.9% | 46.71/42.88 = 108.93% | PASS |
| CN Op EBITDA margin YoY | +47 bps | 4.83−4.36 = 0.47pp | PASS |
| CN Depreciation YoY | +54.8% | 4.52/8.25 = 54.79% | PASS |
| CN Finance cost YoY | +96.3% | 15.53/16.12 = 96.34% | PASS |
| CN operating EBIT YoY | +121.8% | 76.82/34.63−1 = 121.8% | PASS |
| CN Other Income YoY | −36.2% | −1.33/3.67 = −36.24% | PASS |
| CN Core op PBT (ex-OI) YoY | +133.6% | 25.02/18.73 = 133.6% | PASS |
| CN Reported PBT YoY | +105.8% | 23.69/22.40 = 105.76% | PASS |
| CN PAT YoY | +120.8% | 19.24/15.92 = 120.85% | PASS |
| CN EPS Basic YoY | +127.1% | 2.11/1.66 = 127.1% | PASS |
| SA Revenue YoY | +90.8% | 871.59/960.40 = 90.75% | PASS |
| SA Core op PBT YoY | +170.3% | 28.58/16.78 = 170.3% | PASS |
| SA PAT YoY | +152.5% | 22.18/14.54 = 152.5% | PASS |
| CN Revenue QoQ | +5.7% | 100.43/1752.85 = 5.73% | PASS |
| CN Op EBITDA QoQ | −3.9% | −3.62/93.21 = −3.88% | PASS |
| CN PAT QoQ | −10.4% | −4.07/39.23 = −10.37% | PASS |
| Copper-tube rev YoY (L223) | +256.6% | 489.98/137.39−1 = 256.6% | PASS |
| Copper-tube margin Q4→Q1 | 6.58%→4.69% | 22.86/347.20=6.58%; 22.99/489.98=4.69% | PASS |
| Winding-wire rev QoQ (L222) | −2.5% | (1356.90−1392.04)/1392.04 = −2.52% | PASS |
| Winding-wire margin Q4→Q1 (L229) | 5.08%→4.41% | 70.68/1392.04=5.08%; 59.90/1356.90=4.41% | PASS |

### 2D. PAT bridge (A4 §4, consolidated YoY)
| Component | A4 Δ | Recomputed Δ | Status |
|---|---|---|---|
| Gross profit (96.26→164.77) | +68.51 | +68.51 (GP: Rev−COGS−purch−Δinv reconciles to deck 96.3/164.8) | PASS |
| Employee (20.14→26.77) | −6.63 | −6.63 | PASS |
| Other expenses (33.24→48.42) | −15.18 | −15.18 | PASS |
| = Op EBITDA change | +46.70 | 68.51−6.63−15.18 = +46.70 | PASS |
| Depreciation (8.25→12.77) | −4.52 | −4.52 | PASS |
| Finance (16.12→31.65) | −15.53 | −15.53 | PASS |
| Other income (3.67→2.34) | −1.33 | −1.33 | PASS |
| = PBT-before-JV change | +25.33 | 47.51−22.18 = +25.33 | PASS |
| JV share (0.22→−1.42) | −1.64 | −1.64 | PASS |
| = Reported PBT change | +23.69 | 46.09−22.40 = +23.69 | PASS |
| Tax (6.47→10.93) | −4.46 | −4.46 | PASS |
| = Reported PAT change | +19.24 | 35.16−15.92 = +19.24 | PASS |
| ETR-hold counterfactual PAT | ~32.8 | 46.09×(1−0.2888) = 32.78; shield 2.4 (~7% of 35.16) | PASS |

### 2E. Standalone-vs-consolidated gap (YAML `sc_gap_pat_pct`) and related flags
| Metric | A4 value | Recomputed | Status |
|---|---|---|---|
| SC PAT gap Q1FY26 | +9.52 | (15.9224−14.5379)/14.5379 = +9.52% | PASS |
| SC PAT gap Q4FY26 | −1.95 | (39.23−40.01)/40.01 = −1.95% | PASS |
| SC PAT gap Q1FY27 | −4.23 | (3516.35−3671.62)/3671.62 = −4.23% | PASS |
| SC PAT gap FY26 | +0.26 | (108.60−108.32)/108.32 = +0.26% | PASS |
| SC gap swing (FLAG) | 13.7pp | 9.52−(−4.23) = 13.75pp | PASS |
| CN reserves vs SA (FLAG) | 8.7 Cr below | 539.99−531.28 = 8.71 Cr | PASS |
| Residual share capital (FND-04) | ~263 lakh / ~52.6 lakh sh / +2.7 Cr | 4667.45−4404.20 = 263.25 lakh; /5 = 52.65 lakh sh; deck 46.7−44.0 = 2.7 Cr | PASS |
| Balance-sheet YoY moves (Step 5) | +64.2/+108.0/+269.6/+38.9/+60.8/−70.4% | all reconcile to Slide-30 pairs | PASS |

### Two supplementary figures noted (non-blocking; conclusions unchanged)
1. **CN ETR base 28.88% vs 28.91%.** A4 computed the Q1FY26 base rate on the 2-decimal ₹ Cr
   figures (6.47/22.40 = 28.88%); the raw-Lakhs value is 647.42/2239.66 = 28.91%. Difference
   0.03pp — a rounding artifact of dividing rounded inputs, not a computational error. Every
   downstream conclusion (ETR fell ~5-7pp, ~2.4 Cr / ~7% of PAT tax shield) is unchanged at
   either input precision. **Within rounding — PASS.**
2. **"True" net debt ≈660.5 Cr (A4 §5, FND-07).** A4's own listed components
   (265.3+388.8+18.2+2.8−7.8−6.0) sum to **661.3**, not 660.5 — a 0.8 Cr slip in an explicitly
   approximate ("≈") parenthetical. The derived ratio is 661.3/584.9 = 1.13x vs A4's 660.5/584.9
   = 1.129x — **both round to ~1.1x**, and the headline conclusion ("~2.4x the deck's 0.46x") is
   unchanged. This is not one of the mandated core metrics and does not alter any verdict.
   Surfaced for A4 tidy-up, **not a verdict-failing mismatch.**

**Arithmetic verdict: PASS.** All mandated core derived metrics (Operating EBITDA, margins,
effective tax rate, SA-vs-CN gaps, YoY and QoQ percentages, the PAT bridge) reconcile exactly
to the raw extract. No mismatch above rounding in any core metric.

---

## 3. ADVERSARIAL READ

A4's three most positive claims, each with the strongest bear counter buildable FROM THE SAME
EXTRACTED TEXT, and whether the counter survives (and must be grafted in).

**Positive claim 1 — "Core operating PBT ex-OI +133.6% YoY, not treasury-driven; the operating
engine genuinely scaled" (the review's stated cleanest positive, §2C-3).**
Strongest bear counter (same extract): the +133.6% is measured off a Q1FY26 base the review
itself labels pre-Bhiwadi; on a *sequential* basis the same engine is decelerating — CN core PBT
ex-OI fell 51.36 (Q4FY26) → 43.75 (Q1FY27), −14.8% QoQ (L494/L475 cols), Op EBITDA margin
5.32%→4.83%, GP% 9.6%→8.9% (deck L209), and BOTH segments lost margin QoQ (winding
5.08%→4.41% L229; copper 6.58%→4.69% L230). So "genuine scaling" is a low-base YoY artifact
masking sequential profit contraction.
**Survives? Yes — but already fully incorporated in A4** (Step 3, FND-06, QFM Q5,
FLAG-QOQ-MARGIN, §2C-2 "thin-margin," combined-verdict "QoQ margin reversal hidden behind the
YoY headline"). No grafting required.

**Positive claim 2 — "Copper-tube ramp real (489.98 Cr, T2 favourable and NOT fired), +256%
YoY" (growth thesis on track).**
Strongest bear counter (same extract): the ramp is volume bought with balance-sheet expansion at
collapsing profitability — copper-tube segment result was FLAT QoQ (22.86→22.99 Cr, L230) while
revenue jumped +41%, so incremental copper revenue earned ~0 incremental profit; segment margin
halved toward winding-wire levels (6.58%→4.69%); copper-tube segment liabilities roughly DOUBLED
QoQ (180.58→380.79 Cr, CN L565) even as copper-tube capital employed FELL (362.99→287.84 Cr, CN
L573). The "success of diversification" is dilutive volume funded by a payables/liability build.
**Survives? Yes — but already incorporated** (FND-10/QFM Q6 margin, A3-09/M3/T3 segment-liability
doubling, 6D "WEAKENED (margin)"). No grafting required.

**Positive claim 3 — "The YoY PAT bridge is overwhelmingly recurring/operating (Op EBITDA +46.70
vs +19.24 net); growth is REAL and operating, not treasury-driven" (§4).**
Strongest bear counter (same extract): reported PAT growth is flattered by two non-operating
wedges the bridge itself exposes — an unexplained ETR drop to 23.72% (below 25.17% statutory,
L499/L494) worth ~2.4 Cr / ~7% of PAT, and finance costs +96.3% YoY (16.12→31.65, L482) nearly
doubling, confirming the "operating" growth is debt-funded working-capital growth, not
self-funding. Strip the tax benefit and PAT growth is ~106%, not 121%.
**Survives? Yes — but already incorporated** (A3-06/FND-03 ETR, Step 2 diag 5 + Step 4
finance-cost drag, FLAG-ETR, §4 "low-quality wedges"). No grafting required.

**Adversarial verdict:** the three strongest extract-supported bear counters are each ALREADY
present in A4's review. No surviving counter is absent from A4; nothing needs to be grafted in
before save.

---

## VERDICT

**COMPLETE.**

- Coverage: PASS — every A2 ledger row (results 19 notes / 121 line items / 15 auditor paras / 3
  entities / 5 signatures / 3 zero-standing / 1 agenda; presentation 31 slides / 530 points / 8
  footnotes; pressrelease 50 units; 0 turns) reconciles to my fresh count and is cited in A4 or
  covered as reviewed-no-finding. The one formerly-orphan row (Slide-27 dividend LABEL_AMBIGUITY)
  is now explicitly reviewed via FND-12. No orphans, nothing missing from the ledger.
- Arithmetic: PASS — all mandated core derived metrics reconcile exactly to the raw Lakhs
  extract. Two supplementary non-core figures carry sub-rounding / explicitly-approximate slips
  (ETR base 28.88 vs 28.91; net-debt 660.5 vs 661.3 → ~1.1x either way) that change no
  conclusion; surfaced for A4 tidy-up but not verdict-failing.
- Adversarial: PASS — the three strongest extract-supported bear counters are all already in A4.

Only COMPLETE proceeds to Notion save. This audit clears A4 for save.

```yaml
stage: A5-adversary
company: "RAMRAT"
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
