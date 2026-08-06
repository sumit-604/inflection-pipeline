# QUARTERLY PIPELINE A5 — ADVERSARY / COMPLETENESS AUDIT — ANUP — Q1 FY27

Auditor: A5 ADVERSARY | Model: claude-opus-4-8
Inputs seen: A4 review, A1 extracts (results/PR/deck), A2 ledgers (results/PR/deck). Fresh context; A3 reasoning NOT seen (re-derived independently).
Unit re-run: results filing in Lakhs, x0.01 -> Rs Cr. I re-performed every conversion from raw Lakhs.

**VERDICT: INCOMPLETE.** Two FAILs, both loop back to A4 (one arithmetic, one finding-coverage orphan). Details below.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate, run FIRST)

Plain-Language Brief present at L465-485. All four labelled parts present and carrying real, non-placeholder content:

| Part | Heading present | Lines | Content check | Status |
|---|---|---|---|---|
| 1. Summary narrative | yes | L467-473 | 3 substantive paras (~14 lines); numbers anchored | PRESENT |
| 2. Sector intelligence | yes | L475-477 | end-market/air-pocket/capex read, provenance tagged | PRESENT |
| 3. Business-model intelligence | yes | L479-481 | ETO fabrication, utilisation + WC economics | PRESENT |
| 4. Competition intelligence | yes | L483-485 | moat, KRN peer, pricing-pressure risk | PRESENT |

Gate 0: **PASS.** (Does not by itself carry the run; the two FAILs below govern.)

---

## AUDIT 1 — COVERAGE (fresh grep/sweep vs A2 ledgers)

### 1a. A2 ledger-row re-count (independent)

| Category | A2 count | My fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Results: notes (6 std + 7 consol) | 13 | 13 (std L229-253=6; consol L438-470=7) | none | PASS |
| Results: line-items (33+33+5) | 71 | 71 (std tbl 33; consol tbl 33; Note-6 subtable L461-465=5) | none | PASS |
| Results: agenda items | 1 | 1 (board approves results, L37-41) | none | PASS |
| Results: auditor paras (5 std + 6 consol) | 11 | 11 (std L93-122=5; consol L300-335=6) | none | PASS |
| Results: consolidation entities | 2 | 2 (Parent + Mabel, L323-324) | none | PASS |
| Results: signature blocks | 5 | 5 | none | PASS |
| PR: bulleted claims | 20 | 20 (4+8+8 across L50-113) | none | PASS |
| PR: forward-looking stmts | 13 | 13 | none | PASS |
| PR: section headers | 5 | 5 (L49,67,84,121,135) | none | PASS |
| PR: business/financial numbers | 14 | 14 | none | PASS |
| Deck: slides | 26 | 26 (PDF pages 1-26) | none | PASS |
| Deck: footnotes | 6 | 6 | none | PASS |
| Deck: numbers | 217 | 217 (spot-checked slides 5/10/12/14; sum-check reconciles) | none | PASS |
| Deck: zero-standing | 0 | 0 | none | PASS |

No row my fresh pass found is missing from a ledger (nothing to return to A2). Every A2 disclosure CATEGORY is addressed in A4 (notes -> Step 0D; line items -> Step 1; auditor paras -> opinion check; entities -> Mabel treatment; PR claims -> R5 Step 1 corpus + Step 5B silence audit; deck slides/numbers -> Step 1 cross-check, order-book, segment). **A2-row coverage: PASS.**

### 1b. A3 finding-incorporation coverage (task-required check)

A4 asserts (L22-25, YAML L501) that it incorporated 36 A3 finding IDs and that "every A3 finding classified FORWARD-SIGNAL or AMBIGUOUS is carried into the Questions-for-Management table." I traced each claimed ID to a citation in the review body (Questions table / monitorables / flags / silence audit):

- Results F2-1(Q6), F6-1(Q9+mon), F7-1(Q9), F8-1(Q7), F9-1(Q8+mon), F11-1(0C/Step7/flags/mon): all placed.
- PR A3-01(Q3),02(Q2),03(Q2),04(Q4),05(Q12),06(Q5),07(Q13),08(Q13),09(Q10),10(monitorable L453),11(Q10),12(Q10),13(Q10/mon),14(Q11),15(Q4/mon),17(Q15),18(Q13),19(Q13): all placed.
- Deck F16-01..08 (Q1/Q3/Q5/Q2/Q4/Q14/Q14/Q15), F6-01(Q10/mon), F7-01(Q13), F14-01(Step1 consol cross-check): all placed.

**ORPHAN FOUND — A3-16.** It appears ONLY in the incorporation list (L24) and the YAML (L501). It is cited NOWHERE in the review body — not in the 15-row Questions table, not in monitorables, not in flags, not in the Step 5B silence audit. A4 claims it incorporated but provides no home for it. I cannot see A3's file, so I cannot confirm whether A3-16 is FORWARD-SIGNAL/AMBIGUOUS (owed a Questions row) or NEUTRAL (owed a monitorable/flag) — that unresolvable placement is, per conservative-bias rule, a **FAIL**. **Loop back to A4:** either cite A3-16 in a Questions/monitorable/flag row cross-checked to A3's classification, or mark it explicitly "reviewed, no finding." Coverage rule: an incorporated-but-uncited finding is an orphan.

---

## AUDIT 2 — ARITHMETIC (recomputed from raw Lakhs; x0.01 -> Rs Cr)

All Step-1 extraction cells (standalone + consolidated, 4 periods) reconcile to the raw Lakhs after x0.01. All headline derived metrics reconcile within rounding EXCEPT one. Key recomputations:

| Metric (source line) | A4 value | My recompute | Source | Status |
|---|---|---|---|---|
| Std Op EBITDA Q1FY27 = PBTbex+D+Fin-OI | 9.42 | 1.2093+7.2714+1.4335-0.4974 = 9.42 | L173/168/167/159 | OK |
| Std Op EBITDA margin Q1FY27 | 7.99% | 9.417/117.893 = 7.99% | L158 | OK |
| Std reported EBITDA margin Q1FY27 | 8.41% | 9.914/117.893 = 8.41% | L173/168/167 | OK |
| Std gross margin Q1FY27 | 48.82% | (117.893-50.502-9.838)/117.893 = 48.82% | L158/164/165 | OK |
| **Std gross margin Q4FY26** | **47.55%** | **(194.801-92.772-8.817)/194.801 = 47.85%** | **L158/164/165 (31.03.26 col)** | **MISMATCH (0.30pp)** |
| Std gross margin Q1FY26 | 51.64% | (169.422-71.359-10.578)/169.422 = 51.64% | L158/164/165 | OK |
| Std gross margin FY26 | 51.47% | (789.437-353.351-29.591)/789.437 = 51.49% | L158/164/165 | OK (rounding) |
| Std ETR Q1FY27 | 8.4% | 0.1012/1.2093 = 8.37% | L180/175 | OK |
| Std ETR Q1FY26 | 25.9% | 8.9166/34.448 = 25.9% | L180/175 | OK |
| Std OI/PBT Q1FY27 | 41.1% | 0.4974/1.2093 = 41.1% | L159/175 | OK |
| Std Rev YoY | -30.4% | 117.893/169.422-1 = -30.4% | L158 | OK |
| Std Op EBITDA YoY | -76.1% | 9.417/39.374-1 = -76.1% | derived | OK |
| Std margin YoY (bps) | -1,525 | 7.99-23.24 = -15.25pp | derived | OK |
| Std finance cost YoY | +69.1% | 143.35/84.78-1 = +69.1% | L167 | OK |
| Std depreciation YoY | +14.3% | 727.14/636.15-1 = +14.3% | L168 | OK |
| Std core PBT (ex-OI) YoY | -97.8% | 0.7119/32.16-1 = -97.8% | derived | OK |
| Std PAT YoY | -95.7% | 1.1081/25.5314-1 = -95.7% | L182 | OK |
| Consol Op EBITDA Q1FY27 | 9.47 | 0.9344+7.4345+1.6176-0.5209 = 9.47 | L381/376/375/367 | OK |
| Consol Op EBITDA margin Q1FY27 | 7.56% | 9.466/125.249 = 7.56% | L366 | OK |
| Consol margin YoY (bps) | -1,547 | 7.56-23.03 = -15.47pp | derived | OK |
| Consol PAT YoY | -97.8% | 0.5702/26.261-1 = -97.8% | L390 | OK |
| Consol ETR Q1FY27 | 39.0% | 0.3642/0.9344 = 39.0% | L388/383 | OK |
| PAT bridge total (std YoY) | -24.42 | 1.1081-25.5314 = -24.42 | L182 | OK |
| — Op EBITDA change | -29.96 | 9.417-39.374 = -29.96 | derived | OK |
| — PBT change | -33.24 | 1.2093-34.448 = -33.24 | L175 | OK |
| — tax offset | +8.82 | 8.9166-0.1012 = +8.82 | L180 | OK |
| SC-vs-consol PAT gap Q1FY27 | -48.5% | (0.5702-1.1081)/1.1081 = -48.5% | L182/390 | OK |
| Mabel implied loss | ~-0.54 | 0.5702-1.1081 = -0.54 | L182/390 | OK |
| Mabel implied revenue | ~7.4 | 125.249-117.893 = 7.36 | L158/366 | OK |
| Net worth tie (consol) | 691.01 | 670.98 (67,097.50L) + 20.03 (2,003.15L) = 691.01 | L405/404 | OK |
| Share base | 2.003 Cr | 20.0315 Cr / Rs10 = 2.003 Cr | L196/404 | OK |
| Annualised Q1x4 revenue proxy | ~472 | 117.893 x4 = 471.6 | L158 | OK |

**ARITHMETIC FAIL — one:** Standalone Q4 FY26 gross margin. A4 prints **47.55%**; recompute from raw Lakhs = **47.85%** (materials+WIP as % of revenue = (9,277.15+881.69)/19,480.07 = 52.15%, so gross margin = 47.85%). Discrepancy 0.30pp, ~30x the 2-dp quoting precision, so above rounding. It is an isolated slip on the Q4 FY26 balancing-figure column (Step-1 derived table only) and does NOT propagate to any YoY conclusion or the thesis verdict (the thesis uses the Q1FY27-vs-Q1FY26 -282bps gross-margin move, which is correct). Still a reproducible arithmetic error in an A4 table. **Loop back to A4:** correct 47.55% -> 47.85%.

### Trigger arithmetic + UNTESTABLE claims (task-required)
- Margin leg (<19%): 7.99% operating / 8.41% reported, both < 19%. FIRED — arithmetically correct.
- CFO leg / Debtor-days leg marked UNTESTABLE: I confirmed against ALL THREE extracts that no cash-flow statement and no balance sheet appear (results extract carries P&L only: std L157-200, consol L365-408, plus notes/auditor reports; Other Equity is blank in all interim columns L197/L405; PR and deck carry none either). The "no cash-flow / no balance sheet at Q1" basis for UNTESTABLE is **TRUE**. Trigger assessment (PARTIALLY FIRED; margin decisively, cash-legs untestable) is sound.
- "Below Bear on 2 metrics": revenue proxy 472 < bear 871; margin 7.99% < bear 17%. Correct.

---

## AUDIT 3 — ADVERSARIAL READ (strongest bear counter to A4's most positive claims, from the same extracts)

A4 is already a bearish review, so its "positive" load-bearing claims are the few constructive ones. I stress-tested the three strongest:

1. **Positive: "Highest-ever quarterly order booking ~Rs315 Cr; Rs985 Cr book; pipeline intact" (PR L74/L89, deck L203).**
   Bear counter from extract: the Rs985 Cr is "including LOI" (undisclosed split), ~Rs240 Cr is FY28 (PR L89), so FY27-executable ~Rs745 Cr < the Rs800 Cr green line; the inquiry pipeline is Rs1,100 Cr (PR L102/deck L334) vs Rs1,200 Cr prior (Notion); record bookings coincide with revenue -30%. **Counter SURVIVES — but already incorporated** in A4 (checklist item 5 AMBER L248, Q4 L329, flag L545). No graft needed.

2. **Positive: "Auditor UNMODIFIED / clean on both statements" (results Note 2, paras 4/5).**
   Bear counter from extract: it is a limited REVIEW, not an audit — SRE 2410 "moderate assurance... less than an audit... we do not express an audit opinion" (L108-111 std / L317-319 consol); and neither report states whether Mabel's figures were independently reviewed or management-furnished (ledger results Section 7). **Counter SURVIVES — already incorporated** (A4 L53 interpretive gap; scope caveat implicit). No graft needed.

3. **Positive: "Strategic premium intact — licences/niche products, thermal-HX elite entry, two proprietary-licence products, German ACHE" (A4 Step 7 "Hold", deck L574-578, PR L75-80).**
   Bear counter from extract: every one is binary/unquantified with no revenue-recognition timeline; management itself warns the rising complex-project mix "may lead to periodic revenue volatility due to longer execution cycles" (PR L117-118); services only "good traction," no number (PR L106-108). The strategic wins are back-ended and lumpy, not near-term margin support. **Counter SURVIVES — already incorporated** (Q10 L335, Q15 L340, growth-trigger DELAYED L282). No graft needed.

**No NEW surviving bear counter requires grafting into A4.** The review already carries the bear side of each positive claim. (This is the completeness device only; Role 3 Devil's Advocate still runs separately.)

---

## FAIL SUMMARY

| # | Audit | Gap | Loop back to |
|---|---|---|---|
| 1 | Arithmetic | Std Q4 FY26 gross margin printed 47.55%; recomputes to 47.85% (0.30pp, above rounding) — Step-1 derived table | A4 |
| 2 | Coverage (A3 finding mapping) | A3-16 listed as incorporated (L24, YAML L501) but cited nowhere in the review body — orphan; place it (with A3 classification) or mark "reviewed, no finding" | A4 |

Both are surgical, single-point fixes. No arithmetic error touches a thesis conclusion; the A3-16 orphan is a completeness gap in the incorporation trail. Deliverable brief, trigger arithmetic, headline YoY math, PAT bridge, unit conversions, and A2-row coverage all pass.

---

## VERDICT: **INCOMPLETE** — loop back to **A4**.
Gap: (1) correct standalone Q4 FY26 gross margin 47.55% -> 47.85%; (2) place or explicitly clear A3-16 (currently claimed-incorporated but uncited in the body). Re-submit for A5 re-check before Notion save.

```yaml
stage: A5-adversary
company: "ANUP"
quarter: "Q1 FY27"
model: claude-opus-4-8
status: complete
verdict: INCOMPLETE
plain_language_brief:
  narrative: present
  sector: present
  business_model: present
  competition: present
coverage:
  orphan_rows:
    - "A3-16: listed as incorporated (review L24, YAML L501) but cited nowhere in review body (no Questions/monitorable/flag/silence-audit row)"
  missing_from_ledger: []
arithmetic_mismatches:
  - {metric: "Standalone Q4 FY26 gross margin", a4_value: "47.55%", recomputed: "47.85%", source_line: "results L158/L164/L165 (31.03.2026 column): (19480.07-9277.15-881.69)/19480.07"}
surviving_bear_counters: []
loop_back_to: "A4"
gap: "A4 must (1) correct standalone Q4 FY26 gross margin 47.55% -> 47.85% in the Step-1 derived table, and (2) cite A3-16 in a Questions/monitorable/flag row (cross-checked to A3's FORWARD-SIGNAL/AMBIGUOUS/NEUTRAL classification) or explicitly mark it 'reviewed, no finding'. Only COMPLETE proceeds to Notion save."
```
