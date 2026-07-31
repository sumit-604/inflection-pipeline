# A5 ADVERSARY / COMPLETENESS AUDIT — GNG Electronics Limited (EBGNG) — Q1 FY27

Quarter ended June 30, 2026. Audited 2026-07-31. Model: claude-opus-4-8.
This audit OVERWRITES the prior results-only audit at this path. The A4 review now under audit is the merged Role 4 + Role 5 review (filing + presentation + concall).
Fresh context: I re-derived every number from the A1 extracts and re-ran the A2 enumeration independently. I did not defer to A4's or A3's cites.
Raw source of truth: results filing in Rs Million (x0.1 = Rs Cr); deck and concall already Rs Cr. Filing column order = Q1FY27 | Q4FY26 | Q1FY26 | FY26; A4 table order = Q1FY26 | Q4FY26 | Q1FY27 | FY26.

Verdict: **COMPLETE**.

---

## AUDIT 1 — COVERAGE (fresh grep pass vs A2 ledgers; every ledger row cited in A4 or reviewed-no-finding)

### 1A. Results filing

| Category | A2 count | My fresh count | Orphan rows (in ledger, absent from A4) | Status |
|---|---|---|---|---|
| Agenda items | 1 | 1 | none — Step 0 / preamble | PASS |
| Line items (21 SA + 22 CO) | 43 | 43 | none — all in Step 1A/1B tables, every cell anchored | PASS |
| Notes (5 SA + 5 CO) | 10 | 10 (L317-333 / L683-711) | none — Step 0D notes table | PASS |
| Auditor paras (5 SA + 7 CO) | 12 | 12 | none — Step 0D; para 6 (US step-downs unaudited, L474-480) load-bearing in FND-04 | PASS |
| Consolidation entities | 6 | 6 (L452-461) | none — FZC + 5 US step-downs, Step 5S / Q5 / Q16 | PASS |
| Signature blocks | 5 | 5 | none — auditor/CS/director blocks; B.V. jurisdiction -> Q16/FND-08 | PASS |
| Zero-standing rows | 0 | 0 | n/a | PASS |

Fuzzy-grep note: a keyword regex over P&L labels returns extra hits from multi-word labels ("comprehensive income" double-matching OCI-total and TCI); manual sweep confirms exactly 21+22=43 distinct rows. Subsidiary grep returns a 7th hit at L474 which is the auditor-para-6 textual reference, not a 7th entity — the list is 6. A2 open items all land in A4: (a) B.V. jurisdiction -> FND-08; (b) garbled director names/DIN/UDIN -> extraction artifact, correctly not surfaced as a financial finding; (c) auditor-para numbering gap -> A4 confirms clean unmodified opinion; (d) no prior-quarter ledger -> A4 does not fabricate an ENTITY_CHANGE.

### 1B. Presentation

| Category | A2 count | My fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Slides | 8 | 8 (grep `^\[page` = 8) | none — preamble + Step 0B cross-check | PASS |
| Slide 7 income-statement line items | 16 | 16 | none — the QoQ source (Step 3A) | PASS |
| Slide 6 chart KPIs | 10 | 10 | none — match slide 7, match filing | PASS |
| Slide 5 embedded KPIs (6) + qual claims (9) | 6 / 9 | 6 / 9 | none — Redington -> Q7/mon #5; EB Elite -> Q8; reach -> A3-03 | PASS |
| Absent-disclosure categories | 5 | 5 | none — no BS / no CFS / no segment split / no debt-WC / no forward numeric guide -> Step 5A ND + monitorables | PASS |

Deck slide-7 EPS-basic row shows no growth% despite PAT +56.2% (implied share-count change) -> A4 FND-06 / A3-06 dilution check. The 32% (prose) vs 32.1% (table) variance -> A4 uses 32.1%. No orphan.

### 1C. Concall

| Category | A2 count | My fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Turns | 61 | 61 (4 preamble + 26 Q + 30 A + 1 close) | none — Step 4A + participants | PASS |
| Questions | 26 | 26 (Chirag 3, Shanik 2, Sunil 6, Shri 1, Paras 7, Abhin 7) | none — Step 4A inventory Q-1..Q-26 | PASS |
| Management numbers | 79 (N1-N79) | 79 | none — referenced across Sections A/B; N38-41/N42-46/N53-54/N65-66 all used | PASS |
| Zero-standing claims | 7 (Z1-Z7) | 7 | none — Z1/Z2 competition (Q14/tone), Z3 UAE (Q13), Z4 opex (Q11), Z5 no-fixed-capital (A3F-03), Z6 procurement, Z7 no-slowdown | PASS |
| Participants | 10 | 10 | none — Step 0B (5 mgmt/mod) + Step 4A (5 analysts); silent Pancholi/Arora flagged | PASS |

N79 check (analyst's "revenue fell almost 37%", A2-flagged CONTRADICTION): I confirm this is the QoQ move (651.66 -> 412.46 = -36.7%, Step 3A), not a YoY contradiction of +32.1%. A4 handles both correctly; the "37%" reconciles to the QoQ figure. Substance covered. Not an orphan.

**COVERAGE VERDICT: PASS.** No orphan ledger row (would loop A3); no row my fresh pass found that the ledger lacks (would loop A2). GATE A2 counts independently reproduced.

---

## AUDIT 2 — ARITHMETIC (recomputed from raw Million figures, x0.1). All values Rs Cr.

### 2A. Consolidated — load-bearing metrics (task-flagged)

| Metric | A4 value | Recomputed | Source lines | Status |
|---|---|---|---|---|
| Gross Profit Q1FY27 = Rev-DirCost-Δinv = 412.46-272.65-38.16 | 101.65 | 101.65 | L560/577/582 | PASS |
| Gross Margin Q1FY27 | 24.6% | 101.654/412.461 = 24.65% | — | PASS |
| Gross Margin Q4FY26 / Q1FY26 | 19.2% / 21.4% | 125.262/651.655 = 19.22% ; 66.704/312.279 = 21.36% | — | PASS |
| **Falsification test: consol GM vs 17% line** | 24.6% > 17%, NOT breached | 24.65% > 17% confirmed | L560,577,582 | PASS — claim TRUE |
| Op EBITDA Q1FY27 = PBT+D+Fin-OI = 35.74+3.28+13.86-3.51 | 49.37 | 49.37 | L614,597,592,565 | PASS |
| Op EBITDA margin YoY | +162 bps | 11.97%-10.35% | — | PASS |
| Reported EBITDA (deck) = PBT+D+Fin | 52.88 | 52.878 (deck 52.9), margin 12.82% | L614,597,592 | PASS |
| Effective Tax Rate Q1FY27 = 6.81/35.74 | 19.1% | 19.05% | L631,614 | PASS |
| PAT margin Q1FY27 | 7.0% | 28.93/412.461 = 7.01% | L637,560 | PASS |
| Revenue YoY | +32.1% | 32.08% | L560,562 | PASS |
| Core PBT ex-OI YoY = 32.23/19.62-1 | +64.3% | 64.30% | L614,565 | PASS |
| Reported PBT YoY / PAT YoY | +59.1% / +56.2% | 59.06% / 56.21% | L614,637 | PASS |
| Revenue QoQ / PAT QoQ | -36.7% / -31.4% | -36.71% / -31.36% | L560/561, L637/638 | PASS |
| GM YoY / QoQ swing | +329 / +542 bps | 24.65-21.36 / 24.65-19.22 | — | PASS |

### 2B. Standalone-vs-consolidated PAT gap (task-flagged)

| Metric | A4 value | Recomputed (C-S) | Source lines | Status |
|---|---|---|---|---|
| Subsidiary PAT Q1FY26/Q4FY26/Q1FY27/FY26 | 8.34/30.02/12.99/92.09 | 18.52-10.18 / 42.15-12.13 / 28.93-15.94 / 132.02-39.93 | L637,275 | PASS |
| Sub PAT % of consol / of standalone Q1FY27 | 44.9% / 81.5% | 12.99/28.93=44.91% ; 12.99/15.94=81.49% | — | PASS |
| Consol PAT QoQ vs standalone PAT QoQ | -31.4% / +31.4% | -31.36% / +31.38% | L637,275 | PASS |
| Subsidiary-implied GM Q1FY27 | 33.3% | 60.85/182.70 = 33.30% | — | PASS |

### 2C. Standalone GM 17.8% vs management's 21%, and direction (task-flagged)

| Metric | A4 value | Recomputed | Source lines | Status |
|---|---|---|---|---|
| Standalone GP Q1FY27 = 229.76-264.36-(-75.41) | 40.80 | 229.756-264.358+75.405 = 40.803 | L198,215,220 | PASS |
| **Standalone GM Q1FY27** | **17.8%** | **40.803/229.756 = 17.76%** | L198,215,220 | PASS |
| Standalone GM Q1FY26 | 19.7% | 33.891/172.138 = 19.69% | L198,215,220 | PASS |
| **Standalone GM YoY** | -193 bps (CONTRACTED) | -193 bps confirmed | — | PASS — claim TRUE |
| **Consol GM YoY** | +329 bps (EXPANDED) | +329 bps | — | PASS — claim TRUE |
| Standalone ETR Q1FY27 | 27.5% | 6.04/21.98 = 27.48% | L269,252 | PASS |

Management's stated India/standalone GM of 21% (N42) does NOT tie to the filed standalone P&L (17.8%); the gap is ~3.2pp. A4 correctly refuses to defer to the 21%, states "filing wins per protocol," and carries the basis gap as Step 8.5 Q12 and a flag. **A4 did not over-credit the management number.**

### 2D. PAT bridge (Step 4, consolidated YoY) — fully re-derived
Volume +21.40 (100.18 rev delta x 21.36% prior GM) + margin +13.55 (3.29pp x 412.46) = +34.95 GP delta (ties to GP 101.65-66.70 = 34.95); less opex -17.89 = Op EBITDA +17.05 (ties 49.37-32.31); +OI 0.66 = Rep EBITDA +17.71; -D 1.24 -Fin 3.20 = PBT +13.27 (ties 35.74-22.47); -tax 2.86 = **PAT +10.41** (ties 28.93-18.52). Bridge reconciles end-to-end.

### 2E. Net-debt sources-and-uses / cash bridge (task-flagged; test A4's ~Rs100cr+ unexplained-use claim and precision discipline)
Concall gives (all approximate/round): net debt ~300 (Mar-26, CFO "rounding off", N38) -> 406 (Q1FY27, N39), "about 100 odd crores" increase (N40); group inventory 740 -> 700 = -40 (N53/N54); WC "marginally gone down," no magnitude (N41); capex negligible (A3F-03). Net-debt rise = 406-300 = **+106** (~35%: 406/300-1 = 35.3%).
- Narrow framing: an inventory drawdown of 40 is a cash SOURCE, yet net debt still ROSE 106, so cash use unexplained by inventory = 106+40 = **~146**. A4's "~Rs 146 Cr" is correct.
- Broad framing: add cash-profit proxy PAT 28.93 + D&A 3.28 = 32.21; identified sources ~72 (32.21+40+~0 WC); net debt "should" have fallen ~72 to ~228 but rose to 406, gap = 72+106 = **~178**. A4's "~Rs 178 Cr" is correct. Range 100-178 is arithmetically sound.
- Independent OCF corroboration: with capex ~0 and no dividend/equity event, ΔNetDebt ≈ -(OCF net of interest/tax), so net debt +~106 implies OCF ≈ **-~106 (NEGATIVE)**. Inventory RELEASED ~40 yet OCF was still negative -> another WC line (receivables / supplier advances for the buy-ahead lot) absorbed cash, exactly A4's read.
- **Precision discipline PASS:** every figure carries "~", the gap is a range, the Step 5C table is labelled "indicative," and the conclusion is hedged ("strongly implies," "likely still negative") without resolving the INDETERMINATE flag. A4 did NOT over-claim precision on the verbally-given round numbers.

### 2F. Volume / ASP internal consistency (task-flagged)
Volume +18% (N47), revenue +32% (N1/N49). Per-unit realization (multiplicative) = 1.32/1.18 - 1 = **+11.9% (~12%)**, which reconciles with laptop ASP +12% YoY (30,763 vs 27,500 = +11.9%, N56/N58) and others ASP +10% YoY (N62): 1.18 x 1.12 = 1.322 = **+32.2% revenue**. **The internal-consistency check HOLDS at ~12%.**
Non-blocking clarity note (NOT a mismatch): A4 twice characterizes the non-volume contribution as "realization/mix +~14%" (Step 2A diag 1; Section B 5A). The +14% is the additive residual (32-18), a valid growth-attribution figure; as a per-unit *realization* figure it is ~2pp high (true per-unit realization ~12%, matching laptop ASP +12%). A4 never uses "14%" inside a false identity (it does not claim 1.18 x 1.14 = 1.32), the underlying cited numbers (18%, 12% ASP, 32%) are all correct, and no flag/metric/verdict depends on 12 vs 14. Recommend A4 state per-unit realization ~12%. Does not block save. (Separately, the others-ASP QoQ "1.5% better" vs 19,326<19,900 = -2.9% inconsistency is already caught by A4 as Q15.)

### 2G. Deck vs filing cross-check and the previously-flagged cell
Deck (412.5/101.7/52.9/35.7/28.9/6.8) reconciles to filing within rounding; deck EBITDA is the REPORTED (PBT+D+Fin) definition, which A4 correctly separates from Operating EBITDA (ex-OI). The one cell flagged in the prior (results-only) audit — Table 1D FY26 standalone Operating EBITDA — now reads **82.06** in the review under audit (Section A Table 1D), matching my recompute 53.204+7.414+26.396-4.955 = 82.059 -> 82.06. **That prior FAIL is corrected and confirmed. No open arithmetic mismatch remains.**

**ARITHMETIC VERDICT: PASS.** Every A4 table metric ties to raw within rounding; the two task-flagged reconstructions (standalone GM 17.8% vs mgmt 21%; net-debt +106 / gap 146-178 with OCF likely negative) are independently confirmed and appropriately hedged; one non-blocking realization-label clarity note.

---

## AUDIT 3 — ADVERSARIAL READ (three most positive claims; strongest bear counter from the same extract; survival test)

**Positive claim 1: "Consol GM 24.6%, +329 bps YoY, the GM<17% falsifier decisively NOT breached — the single most load-bearing test passed."**
Strongest bear counter from the extract: the 24.6% is entirely an offshore phenomenon — parent/India GM CONTRACTED YoY to 17.8% (only ~80 bps above the 17% line); the lift sits in subs where ~45% of consol PAT (up to ~70% at Q4/FY) is UNAUDITED (5 US step-downs, management-furnished) or component-reviewed only (FZC by NBN; para 6, L474-480). GM rose +542 bps QoQ while revenue FELL -36.7% and the quarter carried a group inventory drawdown; part of the print is a strategic buy-ahead inventory holding-gain (MD, line 83) that requires ever-rising memory prices and ever-growing inventory (net debt +35%). Durability at Q4-scale volume is unproven and management EVADED underwriting a blended GM (T13 L71, grade C/D).
Survives on the extract? Yes — BUT already grafted (Step 1D(ii), Step 5S reads 2/3, Step 3 QoQ, Step 6D "durability unproven", monitorable #3, Q3/Q12, archetype, Section C). No new addition required.

**Positive claim 2: "Revenue +32.1% YoY BEATS even the RAISED 30% guide — GREEN on monitorable #6."**
Strongest bear counter: growth DECELERATED ~40% -> ~30% (Q-25 L123) with only "low seasonality quarter" and no numeric bridge (Q2/Q3 FY26 undisclosed, Note 4 balancing figure); the beat is REALIZATION-led (volume only +18%) riding an external memory supercycle the MD calls a "tailwind" and mis-stated (2x -> 5x, N7/N51); and the +32% was accompanied by net debt +35% QoQ and OCF likely negative — growth "bought" with WC cash burn. A +32% YoY that is -37% QoQ off an unexplained derived peak is not an unambiguous beat.
Survives? Yes — BUT already grafted (Step 2A diag 1, Step 3A, Step 6A/6D, tone 6A, Section B Step 1/5A, Step 5C, Q A3F-06). No new addition required.

**Positive claim 3: "Guidance RAISED (rev 25->30%, PAT margin 0.5->0.75-1%) as a confidence signal."**
Strongest bear counter: the raise was delivered as a DEFLECTION — management raised the topline guide (Q-5) at the exact moment it REFUSED the blended-GM-at-volume question (Q-4), "answering a topline question it was not asked while withholding the margin-durability answer it was" (A4 Exchange 2). Management is CREDIBILITY-UNPROVEN (first post-listing call) with an OVERPROMISER-RISK signature: high specificity on flattering items, withholding on testing items, specificity WITHOUT arithmetic consistency (net-debt gap; ETR guide 10-12% vs 19.1% print). Raising to 30% while growth decelerates toward 30% may be guidance catching up to reality; the PAT-margin raise sits against an ETR that may normalize UP, not down.
Survives? Yes — BUT already grafted (Step 6E archetype, Section C, flags, 5A "confidence signal — topline only", Step 2 asymmetric-confidence diagnostics, Exchange 2, ETR tension). No new addition required.

**ADVERSARIAL VERDICT:** all three strongest bear counters are supported by the extract but ALREADY incorporated in A4's review. No surviving counter is missing; nothing must be newly grafted (no loop to A4 on this axis).

---

## HOUSE-RULE CHECKS
- **cash_conversion stays INDETERMINATE (not silently resolved):** confirmed. A4 YAML `cash_conversion: "INDETERMINATE"`; verdict capped at PROCEED WITH CAVEATS; Step 5D/8/Section C state it "never resolves silently to PROCEED" and hardens as a bearish-tilt caveat, not a resolution. Complies with CLAUDE.md.
- **No pre-committed trigger claimed to have fired:** confirmed. GM<17% falsifier NOT breached (24.6%); third-negative-OCF-YEAR hardening trigger explicitly "not yet testable on a QoQ net-debt move"; <1.5x leverage tripwire not tripped (implied ~0.7x). Decision Status UNCHANGED at WATCHLIST / AVOID; A4 flags, human decides.
- **Exit/destination PE:** 20x is the operator/Notion authority; A4 HOLDs all four pillars (Step 7), no round-number default introduced. Complies.

---

## VERDICT

**COMPLETE.** Coverage reconciles with no orphan rows and nothing missing from the ledgers; every A4 derived metric ties to the raw filing within rounding (standalone GM 17.8% and the net-debt +106 / gap 146-178 both independently confirmed and appropriately hedged; the previously-flagged FY26 standalone Op-EBITDA cell now correctly reads 82.06); the three strongest bear counters are already grafted into A4; the INDETERMINATE cash flag is preserved and no trigger is claimed fired. One non-blocking clarity note (per-unit realization ~12% vs A4's additive "+14%") is recommended for A4 but does not block save. Proceed to Notion save.

```yaml
stage: A5-adversary
company: "EBGNG"
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
