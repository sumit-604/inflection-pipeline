# A5 ADVERSARY / COMPLETENESS AUDIT — R Systems International (RSYSTEMS) Q2 CY2026
## Loop 2 (re-audit after A4 applied FIX 1 / FIX 2 / FIX 3)
Model: claude-opus-4-8 | Auditor: A5 (fresh context) | Date: 2026-08-04
Inputs seen: A4 review + A1 results extract + A1 presentation extract + A2 results ledger + A2 presentation ledger. No forensics, no orchestrator commentary. All numbers below re-derived from the extracts; A4's and A3's cites were checked, not trusted.

Unit convention re-confirmed from source: "Rs. in million, except per share data" (L109, L755). Rs Cr = mn x 0.1.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS GATE (run first)

The A4 review carries **SECTION F — PLAIN-LANGUAGE BRIEF** (L563-585) with all four labelled parts present and carrying real, non-placeholder content:

| Brief part | Location | Present? | Content check |
|---|---|---|---|
| 1. Summary narrative | L565-566 | **PRESENT** | ~18-line narrative; reconciles −26.7% reported PAT vs +51.6% core PBT, names the NOIDA base effect, cash 1.35x with the WC-use caveat, the concall gate. Non-empty. |
| 2. Sector intelligence | L568-573 | **PRESENT** | Mid-cap IT/AI-GCC sector, FX tailwind, vertical mix, named provenance (this-quarter filing vs Notion prior). Non-empty. |
| 3. Business-model intelligence | L575-579 | **PRESENT** | Two segments, unit economics, model drift to inorganic+debt, balance-sheet/dilution. Non-empty. |
| 4. Competition intelligence | L581-585 | **PRESENT** | Where it wins/is weaker, concentration, competitive risk, peer cross-check explicitly absent. Non-empty. |

**GATE 0 result: PASS.** All four parts present and substantive.

---

## AUDIT 1 — COVERAGE (independent grep pass, diffed against A2 ledgers)

Fresh enumeration re-run against both extracts and diffed against the two A2 ledgers. Key independent checks:
- Consolidated entities: last numbered line is "31. Novigo Solutions B.V." (extract L731); count = 31. **Match** (ledger §15 = 31).
- Novigo entities flagged "w.e.f 13 November, 2025": fresh grep = 5 hits (#27-31, L722-731). **Match** (ledger 5 ENTITY_CHANGE).
- Agenda items: 3 main (L36-40) + 5 postal-ballot sub-resolutions 3a-3e (L42-61) = 8. **Match.**
- 21 unreviewed subsidiaries, PAT Rs 114.58 mn Q2 / 147.96 mn 6M (L592-595). **Match** (ledger §16 para 6).
- Presentation: "Novigo" appears in the entire press release exactly **once** — the DSO-exclusion footnote (L520). Independently confirms the Novigo-revenue-silence finding (no management quote names it).

| Category | A2 ledger count | My fresh count | Orphan rows (ledger→A4) | Status |
|---|---|---|---|---|
| Agenda items (results) | 8 | 8 | none | PASS |
| Numbered + unnumbered notes | 31 | 31 (25 numbered + 6 footnotes) | none | PASS |
| P&L / table line items (10 tables) | 281 | 281 (spot-reconciled per table) | none | PASS |
| Zero-standing rows | 6 | 6 (2 NCI attrib., 2 DRR NA, 2 Inventory-turnover NA) | none (all immaterial, correctly non-findings) | PASS |
| Auditor paragraphs | 27 | 27 (10 consol review + 17 SA audit) | none | PASS |
| Consolidated entities | 31 | 31 | none | PASS |
| Signature blocks | 15 | 15 | none | PASS |
| Presentation gated rows (18 cats) | 189 | 189 | none | PASS |
| Presentation zero-standing | 1 | 1 (Assets held for sale, L385) | none | PASS |
| Concall turns / slides | 0 / 0 | 0 / 0 (no transcript; concall ~12 Aug not held) | n/a | PASS |

**Ledger-row → A4 citation check.** A4's Section 0 preamble (L17-22) declares 100% reconciliation and marks every ledger category reviewed; the A3 forensic set (F1-a…F15-a plus PASS checks F3/F7/F11/F14; A1-A12) is enumerated (L24-26) and each finding is traceable to a Step or a Section-C question. I found **no orphan row** (ledger item absent from A4) and **no missing row** (fresh-pass item the ledger lacks).

Two granular, non-blocking observations (NOT failures — the underlying rows are enumerated and reviewed inside A4's cash-flow analysis, so no separate finding is owed):
- Consol CFO carries a Rs 56.26 mn doubtful-debt **provision reversal** (L428) that lifts operating-profit-before-WC; A4 assesses CFO in aggregate but does not itemise this credit. Minor cash-quality colour, not thesis-changing.
- H1 CY25 CFO base (0.52x) was depressed by a Rs 57.22 Cr receivables **build** (L442, −572.18 mn) that reverses this year — the 0.52x→1.35x jump rides an easy comp. A4 captures the direction (net WC USE this half; one-offs) but does not name the base-year distortion. Refinement candidate, below the graft threshold.

**AUDIT 1 result: PASS.** No orphan rows, no missing rows.

---

## AUDIT 2 — ARITHMETIC (every derived metric recomputed from raw extract lines)

All figures recomputed in Rs mn then /10, from the consolidated (L115-135), standalone (L764-784), Reg-52 ratio, cash-flow (L424-448) and presentation contribution (L273-336) lines.

### 2A. Re-verification of the three FIXED items (the loop-1 corrections)

| Item | A4 (post-fix) value | My recomputation (source) | Status |
|---|---|---|---|
| **FIX 1** Reported EBITDA H1 CY25 | 189.99 Cr / 21.00% | PBT 1,559.11 + D&A 304.44 + FC 36.31 = 1,899.86 mn = **189.99 Cr**; /9,044.80 = 21.005% → **21.00%** | **CONFIRMED FIXED** |
| Reported EBITDA — Q2 CY25 | 117.17 / 25.36% | 991.83+158.43+21.41=1,171.67 = 117.17; /4,620.15=25.36% | PASS |
| Reported EBITDA — Q1 CY26 | 120.73 / 21.01% | 896.32+215.07+95.91=1,207.30=120.73; /5,747.68=21.01% | PASS |
| Reported EBITDA — Q2 CY26 | 112.02 / 18.62% | 805.07+220.39+94.77=1,120.23=112.02; /6,017.01=18.62% | PASS |
| Reported EBITDA — H1 CY26 | 232.76 / 19.79% | 1,701.39+435.46+190.68=2,327.53=**232.75**; /11,764.69=**19.78%** | PASS (rounding; see note) |
| **FIX 2** WC change H1 CY26 | −18.30 Cr (net USE) | Cash gen 2,065.14 − op profit pre-WC 2,248.17 = −183.03 mn = **−18.30 Cr USE** | **CONFIRMED FIXED** |
| WC change H1 CY25 | −66.35 Cr (net USE) | 820.17 − 1,483.69 = −663.52 mn = −66.35 Cr USE | PASS |
| WC composition H1 CY26 | receiv +51.19 / other-assets −47.58 / provisions −17.53 / payables −4.38 | L442 +511.92 (+51.19); L443 −475.83 (−47.58); L444 −175.28 (−17.53); L445 −43.84 (−4.38); Σ = −183.03 mn = −18.30 Cr | **CONFIRMED — sign correct, composition ties** |
| **FIX 3** bear counter "WC-neutral half ≈ 1.50x" | ~1.50x | (2,248.17 − 432.56 taxes)/PAT 1,209.84 = 1,815.61/1,209.84 = **1.50x** | **CONFIRMED** |

**Sign-consistency sweep (FIX 2).** The net WC USE of Rs 18.30 Cr is stated as a USE (not a release) at every occurrence: Step 5 table (L235), Step 5 answers (L250-251), Step 5 close (L255), Step 6D (L337), Step 7 (L352), Section B §7 (L474), Flag 11 (L558), Section F narrative + business-model (L566, L577), Q14 (L506), Section D monitorable (L525), and YAML (L606, L629, L634, L651). **Sign fixed everywhere — no residual release-sign left.**

### 2B. Full derived-metric recomputation (consolidated)

| Metric | A4 value | Recomputed (source line) | Status |
|---|---|---|---|
| Operating EBITDA Q2 CY25 / margin | 70.20 / 15.19% | 991.83+158.43+21.41−469.67=702.00; /4,620.15=15.19% | PASS |
| Operating EBITDA Q2 CY26 / margin | 110.66 / 18.39% | 805.07+220.39+94.77−13.68=1,106.55; /6,017.01=18.39% | PASS |
| Op EBITDA Q1 CY26 / H1 CY25 / H1 CY26 | 103.66/18.03%, 140.74/15.56%, 214.31/18.22% | 1,036.56/18.03%; 1,407.40/15.56%; 2,143.11/18.22% | PASS |
| Op EBITDA margin YoY (Q2) | +320 bps | 18.39−15.19 = 3.20 pp | PASS |
| Core PBT ex-OI (all cols) | 52.22/72.56/79.14/106.67/151.70 | 522.16/725.58/791.39/1,066.65/1,516.97 mn | PASS |
| Core PBT ex-OI YoY (Q2) | +51.6% | 791.39/522.16−1 = +51.56% | PASS |
| Reported PBT YoY (Q2) | −18.8% | 805.07/991.83−1 = −18.83% | PASS |
| PAT YoY (Q2) | −26.7% | 555.70/758.54−1 = −26.74% | PASS |
| Revenue YoY (Q2) | +30.2% | 6,017.01/4,620.15−1 = +30.23% | PASS |
| Finance cost YoY (Q2) | +342.7% | 94.77/21.41−1 = +342.6% | PASS |
| D&A YoY (Q2) | +39.1% | 220.39/158.43−1 = +39.11% | PASS |
| Other income YoY (Q2) | −97.1% | 13.68/469.67−1 = −97.09% | PASS |
| Effective tax rate (all cols) | 23.52/27.02/30.98/26.60/28.89% | 233.29/991.83 … 491.55/1,701.39 | PASS |
| Other income / PBT (all cols) | 47.35/19.05/1.70/31.59/10.84% | recomputed identical | PASS |
| PAT margin (all cols) | 16.42/11.38/9.24/12.65/10.28% | recomputed identical | PASS |
| CFO / PAT H1 CY25 → H1 CY26 | 0.52x → 1.35x | 592.16/1,144.47=0.517; 1,632.58/1,209.84=1.349 | PASS |
| CFO YoY | +175.7% | 1,632.58/592.16−1 = +175.7% | PASS |
| Capex H1 CY25 / CY26 | 21.03 / 15.07 | 189.94+20.36=210.30; 130.31+20.39=150.70 | PASS |
| FCF H1 CY25 / CY26 | 38.19 / 148.19 (+288%) | 59.22−21.03; 163.26−15.07; +288% | PASS |
| Net debt incl lease | +35.36 Cr | 270.85 borrow +98.48 lease −333.97 cash = 35.36 | PASS |
| Net cash excl lease | +63.12 Cr | 333.97 − 270.85 = 63.12 | PASS |
| Current-borrowing repayment | Rs 44.37 Cr | 454.39 − 10.73 = 443.66 mn | PASS |

### 2C. Standalone + S-vs-C gap + PAT bridge

| Metric | A4 value | Recomputed | Status |
|---|---|---|---|
| SA Op EBITDA Q2 CY25/Q1/Q2 CY26 | 56.00/80.16/73.16 | 560.03/801.62/731.62 mn | PASS |
| SA Op EBITDA margin | 19.16/25.02/21.36% | recomputed identical | PASS |
| SA ETR Q2 CY26 | 30.46% | 156.82/514.91 = 30.46% | PASS |
| SA PAT margin Q2 CY26 | 10.45% | 358.09/3,425.40 = 10.45% | PASS |
| S-vs-C gap Q2 CY26 / % of SA | +19.76 / +55.2% | 555.70−358.09=197.61; /358.09=55.18% | PASS |
| S-vs-C gap Q1 CY26 / FY25 | +2.52 (+4.0%) / −13.26 (−6.6%) | 25.22/628.92=4.01%; −132.56/1,994.52=−6.65% | PASS |
| SA other-expense QoQ jump | +94% (+Rs 27.56 Cr) | 569.27/293.63−1=+93.9%; Δ 275.64 mn | PASS |
| SA PAT QoQ | −43% | 358.09/628.92−1 = −43.1% | PASS |
| PAT bridge subtotal (adj-EBITDA contrib) | +41.01 (79.74→120.75, L279) | 1,207.50−797.43=410.07 mn = +41.01 | PASS |
| Bridge: GM +69.67 / SG&A −28.67 | L275 / L277 | 2,360.19−1,663.45=696.74; 1,152.69−866.02=286.67 mn | PASS |
| Bridge: non-recurring swing −42.55 | L286 | (−16.17)−409.36 = −425.53 mn = −42.55 Cr | PASS |
| Bridge: OI-net −2.23; RSU −1.37; tax −1.61 | L289/L281/L134 | (−8.73−13.60); (62.37−48.72); (249.37−233.29) | PASS |
| Bridge total | −20.28 (−26.7%) | Σ = −20.29 (rounding) | PASS |
| Adj PAT Q2 +35.4% (62.87 vs 46.44, L296) | +35.4% | 628.74/464.38−1 = +35.4% | PASS |

### 2D. Presentation-sourced metrics used in the review

| Metric | A4 value | Recomputed (source) | Status |
|---|---|---|---|
| Adj. EBITDA margin Q2 / H1 | 20.07% / 20.10% | L280 / L324 verbatim | PASS |
| Adj. EBITDA margin YoY (Q2) | +281 bps | 20.07−17.26 (L280) | PASS |
| Blended utilisation YoY | 82.64% → 81.13% (−151 bps) | L483 verbatim | PASS (CFO "improved utilisation" claim genuinely contradicted) |
| IT-services segment margin QoQ | 16.16% → 12.65% | 841.72/5,208.13; 687.84/5,437.01 (L503/L510) | PASS |
| Gross margin Q2 | 39.23% (from 36.00%) | L276 | PASS |
| USD/INR implied Q2 | ~94.7 | 6,017.01/63.56 = 94.67 (L273) | PASS |
| DSO billed / billed+unbilled | 55 (vs 56) / 75 (vs 73) | L516/L517; excl Novigo (L520) | PASS |
| Debtor turnover consol Q2 / SA Q2 | 1.47x / 1.71x | L313 / L986 | PASS |
| ISCR consol / SA; SA DSCR | 9.35x / 6.52x / 5.43x | L280 / L938 / L932 | PASS |
| Headcount | 5,270 (vs 4,561) | L510 | PASS (QoQ 5,303→5,270 is a slight decline, not stated — not an error) |

### Arithmetic notes (rounding-only, not failures)
- **H1 CY26 Reported EBITDA**: A4 shows 232.76 Cr / 19.79%; exact is 232.753 Cr / 19.784% → rounds to 232.75 / 19.78%. Discrepancy 0.01 Cr and 0.006 pp — **within rounding**, and in the H1 CY26 column (untouched by FIX 1, which corrected only the H1 CY25 column). No conclusion depends on it.
- **Characterisation imprecision (not an arithmetic error)**: at L251 and Flag 11 (L558) A4 phrases the offset as the receivables release being "more than offset by [the] Rs 47.58 Cr other-assets build" read as that single line. Numerically the other-assets build (47.58) alone is 93% of the release (51.19); it is the *package* of other-assets + provisions (17.53) + payables (4.38) that tips the half to a net USE. Every number is correct and the net −18.30 Cr USE is correct; only the "absorbed more than all of it" wording overstates the single line. Recommend A4 tighten the prose, but this changes no metric or verdict — **not a gate failure.**

**AUDIT 2 result: PASS.** All three fixes independently confirmed; no arithmetic mismatch above rounding anywhere in the review; no NEW error introduced by the edits.

---

## AUDIT 3 — ADVERSARIAL READ (three most-positive claims, strongest bear counter from the same extract)

**Claim 1 (most positive): "Core operating PBT +51.6% YoY and operating EBITDA margin +320 bps — the reported −26.7% PAT is a base-effect illusion; operations genuinely accelerated."** (A4 L158, L166, L171)
Strongest bear counter from the extract: the +51.6% core PBT, +30.2% revenue and +320 bps all **blend** Novigo inorganic (5 entities consolidated 13-Nov-2025, L722-731) + Velotio/Scaleworx restated-into-parent comparatives (Note 3) + a ~12.5 pp INR-vs-US$ FX tailwind; organic constant-currency growth is disclosed **nowhere**. "Operating EBITDA" flatters precisely because it strips the finance cost (+342.7%) and D&A (+39.1%) the acquisitions brought — and the actual operating segment, IT-services, saw its margin **compress QoQ 16.16%→12.65%** (L503/L510) while revenue grew, evidence the inorganic mix is segment-dilutive.
Survives? **YES.** Already grafted? **YES** — Step 2 diag 1, Step 5N, Flags 2/3/4, Q1/Q2. No new graft required.

**Claim 2: "Cash conversion FIRING at CFO/PAT 1.35x, structural — above the 1.30x top band."** (A4 L232, L250)
Strongest bear counter: the 1.35x was achieved **despite a net working-capital USE of Rs 18.30 Cr** this half (a WC-neutral half would be ~1.50x), and the Rs 51.19 Cr receivables release was consumed by an **unexplained Rs 47.58 Cr other-assets build** (L443). Additional extract-supported refinement: the 0.52x→1.35x leap also rides an easy prior-year comp — H1 CY25 CFO was depressed by a Rs 57.22 Cr receivables build (L442) — and this half's CFO carries a Rs 56.26 mn doubtful-debt provision reversal (L428).
Survives? **YES.** Already grafted? **YES** — this is exactly the FIX 3 graft (L250, Flag 11 L558, Q14 L506). The easy-comp/provision-reversal refinements are supported but below the thesis-changing threshold and do not independently require grafting; noted for A4 to optionally strengthen.

**Claim 3: "Adjusted EBITDA margin 20.1%, at/above the ~20% bull threshold — margin genuinely expanded."** (A4 L296, L311)
Strongest bear counter: 20.1% is **management's own non-GAAP "adjusted" figure** (strips RSU cost + non-recurring items); the reported/GAAP EBITDA margin is 19.03% (L283) and reported PAT margin **fell** to 9.24% from 16.42%. The CFO attributed the margin to "**improved utilisation**," but the filing's own utilisation table shows blended utilisation **fell** 82.64%→81.13% (L483) — the stated driver is contradicted by the company's own data.
Survives? **YES.** Already grafted? **YES** — Flag 5 (L552) and Section B §7A (L477). No new graft required.

**AUDIT 3 result: PASS.** All three strongest bear counters survive on the extract, and all three are **already incorporated** into A4 (loop-2 state, post FIX 3). **No un-grafted surviving counter remains.**

---

## STANDALONE / CONSOLIDATED COMPLETENESS
Both statements fully covered: consolidated (Steps 1A/1C/2/3/4/5) and standalone (Steps 1B/1D), with the S-vs-C PAT gap treated as a first-class metric (Step 5S). Both auditor opinions correctly characterised — SA full audit UNMODIFIED (L1253-1271, L832), consol SRE 2410 limited review UNMODIFIED with no EoM (L555-590). Same partner Alka Chadha, two distinct UDINs (expected). **Complete.**

---

## VERDICT

**COMPLETE.**

- Gate 0 (plain-language brief, all four parts): PASS.
- Audit 1 (coverage): PASS — 0 orphan rows, 0 missing rows; my independent grep reproduces the ledger counts (31 entities, 5 Novigo w.e.f., 8 agenda, 21 unreviewed subs, Novigo named once in the release).
- Audit 2 (arithmetic): PASS — FIX 1 (Reported EBITDA H1 CY25 189.99 / 21.00%), FIX 2 (WC net USE Rs 18.30 Cr, sign correct at all 15+ occurrences), and FIX 3 (bear counter, WC-neutral ~1.50x) all independently confirmed; every derived metric re-derived clean; no NEW error; two rounding-only / prose items noted, none gate-failing.
- Audit 3 (adversarial): PASS — three strongest bear counters all survive and all are already grafted.

No loop-back required. The review may proceed to Notion save.

Output path: /home/user/inflection-pipeline/runs/rsystems-q2cy26/work/audit_rsystems_q2cy26.md

```yaml
stage: A5-adversary
company: "RSYSTEMS"
quarter: "Q2CY2026"
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
surviving_bear_counters: []      # all three survive but are already grafted into A4 (loop-2, post FIX3)
loop_back_to: ""
gap: ""
```
