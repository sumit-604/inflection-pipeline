# A5 ADVERSARY / COMPLETENESS AUDIT — GMDCLTD Q1 FY27

Independent audit of `review_gmdc_q1fy27.md` (A4). Fresh context: A4 review, A1 extract,
A2 ledger only. Every number below re-derived from `extract_results_gmdc_q1fy27.txt`
raw lines; A4's and A3's cites were checked, not trusted. Unit Rs Crore throughout.

EPS note honored: the corrected values std 5.13 / cons 5.14 (Basic = Diluted) are NOT
raised as arithmetic errors against the text-layer 2.13/2.14; correction memo accepted
per task instruction (glyph misreads at L212 and L151; parity holds every other column).

---

## 1. COVERAGE AUDIT

Fresh grep passes run independently of A2:
- Agenda items: `^\s*\([0-9]\)` -> L31 (Financial Results), L48 (GNFC MoU), L68 (IREL MoU) = 3. Matches ledger 3.
- Consolidation entities: `(Joint Venture|Associate)$` -> L385-389 = 5. Matches ledger 5.
- Segment structure lines: L237/238 (std Un-alloc/Total Operating Results), L360/361 (cons Un-alloc/Total Results), L243/250/367/372 (assets/liabilities blocks) all present.

| Category | A2 count | My fresh count | Orphan / missing | Status |
|---|---|---|---|---|
| Numbered notes | 9 | 9 (Std 4 L256-279, Con 5 L379-406) | none | PASS |
| Unnumbered footnote | 1 | 1 (L155-159) | none | PASS |
| Agenda items | 3 | 3 (L31, L48, L68) | none | PASS |
| Detailed P&L lines | 57 | 57 (Std 28 + Con 29) | none | PASS |
| Summary-table lines | 18 | 18 | none | PASS |
| Segment rows | 44 | 44 | see note below | PASS (with note) |
| Consolidation entities | 5 | 5 (L385-389) | none | PASS |
| Auditor paragraphs | 10 | 10 (Con 6 L424-484 + Std 4 L506-536) | none | PASS |
| Signature blocks | 6 | 6 | none | PASS |
| Board Outcome items | 3 (results, GNFC MoU, IREL MoU) | 3 | none | PASS |

A4 coverage of each ledger unit:
- All 9 notes + footnote surfaced in Step 0D table. PASS.
- 3 Board Outcome items: item 1 (results) is the whole review; item 2 (GNFC) and item 3
  (IREL) surfaced in the Board-Outcome section, Q7/Q8, and monitorables 2-3. PASS.
- Auditor: both limited reviews, the Other Matter para (Rs 0.42 cr, L471-484), unmodified
  conclusions, separate UDINs — all surfaced. PASS.
- A3-01..A3-10 all incorporated; 8 AMBIGUOUS/FORWARD-SIGNAL findings each map to >=1
  question (Q1->A3-02, Q2->A3-01, Q3->A3-07, Q4->A3-05, Q5->A3-06, Q6->A3-03, Q7->A3-08,
  Q8->A3-04); the 2 BENIGN (A3-09, A3-10) logged without a question, per contract. PASS.

Coverage note (not a fail): Segment Liabilities rows (Mining 1,215.66 / Power 106.37 /
Unallocated 772.93 / Total 2,094.96, L251-254 & L373-376) and Unallocated Segment Assets
(std 4,000.24 L248 / cons 4,004.83 L370) are enumerated in the ledger but are not
individually surfaced in A4's segment table. A4's preamble blanket-marks all rows
"reviewed, 100% reconciled." These carry no material finding, so this stays a note, not an
orphan-row FAIL.

COVERAGE RESULT: PASS. No orphan rows, no rows missing from the ledger.

---

## 2. ARITHMETIC AUDIT

Every derived figure recomputed from raw extract lines. Standalone Step 1C, Step 2, Step 3,
Step 4, S-vs-C gap, ETR, OCI, and segment blocks all tie (samples shown), EXCEPT the
consolidated Step 1C operating rows, which fail.

### Verified correct (representative — all tie to source)

| Metric | A4 value | Recomputed | Source lines | Status |
|---|---|---|---|---|
| Op EBITDA std Q1FY27 (227.25+33.33+6.61-76.15) | 191.04 | 191.04 | L191/187/186/179 | PASS |
| Op EBITDA std Q4FY26 (231.72+48.76+5.37-155.41) | 130.44 | 130.44 | L191/187/186/179 | PASS |
| Op EBITDA margin std Q1FY27 (191.04/906.64) | 21.07% | 21.07% | L178 | PASS |
| Core PBT ex-OI std Q1FY27 (227.25-76.15) | 151.10 | 151.10 | ties seg L238 151.13 | PASS |
| ETR std Q1FY27 ((64.75-0.58+0.07)/227.25) | 28.27% | 28.27% | L195-197/193 | PASS |
| ETR std Q4FY26 (40.56/261.74) | 15.50% | 15.50% | L195-197/193 | PASS |
| Rev YoY (174.04/732.60) | +23.76% | +23.76% | L178 | PASS |
| PAT YoY std (-1.12/164.13) | -0.68% | -0.68% | L198 | PASS |
| Finance YoY (6.11/0.50) | +1,222% | +1,222% | L186 | PASS |
| QoQ rev (92.59/814.05) | +11.37% | +11.37% | L178 | PASS |
| QoQ PAT (-58.17/221.18) | -26.30% | -26.30% | L198 | PASS |
| PAT bridge closes (+2.56 PBT, -3.68 tax -> -1.12) | -1.12 | -1.12 | L191/198 | PASS |
| S-vs-C gap Q4FY26 (194.09-221.18) | -27.09 / -12.25% | -27.09 / -12.25% | L322/198 | PASS |
| S-vs-C gap Q1FY27 (163.43-163.01) | +0.42 / +0.26% | +0.42 / +0.26% | L322/198/316 | PASS |
| Cons OtherExp divergence Q4 (212.81-182.47) | +30.34 | +30.34 | L309/189 | PASS |
| OCI net Q1FY27 (15.31 pre-tax -21.79) | (6.48) | (6.48) | L202-205 | PASS |
| Mining rev YoY (155.77/685.24) | +22.73% | +22.73% | L225 | PASS |
| Mining assets YoY (1,165.45/2,930.20) | +39.77% | +39.77% | L244 | PASS |

### FAIL — Consolidated Step 1C operating rows carry standalone values

A4 defines Operating EBITDA = PBT(before exceptional) + Depreciation + Finance Costs -
Other Income, and Core PBT ex-OI = PBT(before exceptional) - Other Income. Applied to the
CONSOLIDATED inputs (L312 PBT-before-exc, L307 Dep, L306 Finance, L299/300 Other Income),
the prior-period consolidated figures are NOT equal to standalone. A4 copied the standalone
numbers into the "(cons)" rows. Independently corroborated: the correct consolidated
Core PBT ex-OI values equal the CONSOLIDATED segment "Total Results" line L361, which A4
itself printed elsewhere but did not reconcile to.

| Metric | Period | A4 value | Recomputed (cons) | Source lines | Status |
|---|---|---|---|---|---|
| Operating EBITDA (cons) | Q1FY26 | 169.90 | 169.24 (224.43+22.00+0.51-77.70) | L312/307/306/300 | FAIL |
| Operating EBITDA (cons) | Q4FY26 | 130.44 | 104.20 (204.96+48.76+5.37-154.89) | L312/307/306/299 | FAIL |
| Operating EBITDA (cons) | FY26 | 477.20 | 443.77 (745.80+114.71+7.14-423.88) | L312/307/306/298 | FAIL |
| Operating EBITDA (cons) | Q1FY27 | 191.04 | 191.04 | (all lines equal std) | pass |
| Core PBT ex-OI (cons) | Q1FY26 | 147.40 | 146.73 (224.43-77.70); ties L361 146.74 | L312/300/361 | FAIL |
| Core PBT ex-OI (cons) | Q4FY26 | 76.31 | 50.07 (204.96-154.89); ties L361 50.07 | L312/299/361 | FAIL |
| Core PBT ex-OI (cons) | FY26 | 355.35 | 321.92 (745.80-423.88); ties L361 321.93 | L312/298/361 | FAIL |
| Core PBT ex-OI (cons) | Q1FY27 | 151.10 | 151.10; ties L361 151.13 | L312/298/361 | pass |

Largest single discrepancy: consolidated Core PBT ex-OI Q4FY26, A4 76.31 vs actual 50.07
(off by 26.24 cr) and consolidated Operating EBITDA Q4FY26, A4 130.44 vs actual 104.20
(off by 26.24 cr); FY26 off by 33.43 cr. All far above rounding.

Downstream contradiction: the SEGMENT ANALYSIS header claims "standalone page 5 /
consolidated page 7 — identical operating figures." They are identical ONLY for Q1FY27.
A4's own segment rows show they diverge in prior periods — Un-allocable Corporate Results
Q4FY26 std (54.22) vs cons (80.46) (L237/L360), and consolidated Total Results L361 (50.07,
146.74, 321.93) vs standalone L238 (76.30, 147.41, 355.35). The "identical" claim is false
for Q1FY26/Q4FY26/FY26 and the 1C cons rows inherit that error.

Materiality: this does NOT change the Q1FY27 baseline (all Q1FY27 consolidated operating
figures are genuinely equal to standalone and are correct), the YoY analysis (standalone-
anchored, correct), the S-vs-C PAT-gap section (uses reported PAT, correct), or the
verdict logic. But the saved artifact would contain three false consolidated operating-
metric rows and one false "identical operating figures" assertion. Correcting them
actually strengthens A4's own A3-02 thesis: the consolidated operating engine was demonstrably
weaker than standalone in Q4FY26/FY26 (the exact Other-Expenses divergence flagged), which
the corrected 1C rows would make visible instead of masking.

ARITHMETIC RESULT: FAIL. Loop back to A4. Recompute the consolidated Step 1C Operating
EBITDA and Core PBT ex-OI rows for Q1FY26, Q4FY26, FY26 from consolidated inputs
(L298-320), reconcile them to consolidated segment Total Results (L361), and correct the
"identical operating figures" claim in the SEGMENT ANALYSIS header to "identical only in
Q1FY27; prior periods diverge, per A3-02."

---

## 3. ADVERSARIAL READ — three most positive claims, strongest bear counter each

1. CLAIM: "Revenue +23.76% YoY — strong top-line growth" (Step 2).
   BEAR (same text): growth did not reach the bottom line (PAT -0.68%), and a large slice
   is loss-making Power volume (Power revenue +134.9% to 111.25 while Power result swung to
   (6.00) from +10.59, L226/L235). Growth quality is mixed.
   SURVIVES? No new graft needed — A4 already leads with margin -212 bps, the Power loss,
   and the loading-cost conversion failure. Bear case already present and symmetric.

2. CLAIM: "Sequentially operations improved sharply — Op EBITDA +46.46% QoQ, margin +505 bps" (Step 3).
   BEAR (same text): distorted by Q4FY26 base weakness (Power (40.98), op margin 16.02%)
   and by Q1 being the seasonally strongest pre-monsoon mining quarter; not a clean read.
   SURVIVES? No — A4 explicitly caveats both the Q4 base distortion and seasonality in Step 3.

3. CLAIM: "GST Compensatory Cess Rs 79.03 cr -> nil is a structural margin lift" (bull answer, Q2).
   BEAR (same text): margin still FELL 212 bps YoY despite the cess disappearing, i.e. the
   ~79 cr benefit was fully consumed by loading/overburden inflation (+145.88 cr); permanence
   unconfirmed (no concall).
   SURVIVES? No — A4 states exactly this in diagnostic 2 and the Q2 bear answer.

No bear counter survives un-incorporated. A4's bull-bear symmetry is intact. Nothing to
graft on the adversarial axis.

---

## 4. ADVERSARIAL GOVERNANCE CHECKS

- Forward interpretation stated as fact without concall? No. GST-cess permanence, MoU
  scope/capex, Power path, normalized ETR, OCI-tax assumption, and the S-vs-C operating
  divergence are all left explicitly open and routed to Q1-Q8 / monitorables. PASS.
- INDETERMINATE cash conversion prevented from resolving to PROCEED? Yes. CFO is ND (Q1 not
  mandated under Reg 33 half-yearly); A4 caps the verdict at PROCEED WITH CAVEATS and names
  the missing evidence (H1 FY27 cash-flow + balance sheet at Q2 filing). Compliant with the
  house rule. PASS.
- Verdict from the permitted set and justified? "PROCEED WITH CAVEATS" is in the permitted
  set; two named-evidence caps (INDETERMINATE cash + no concall) justify it; no STOP was
  invented; no mechanical failure. PASS.

---

## VERDICT

VERDICT: INCOMPLETE.

Failing agent: A4.
Gap: Consolidated Step 1C operating rows carry standalone values. Operating EBITDA (cons)
and Core PBT ex-OI (cons) for Q1FY26, Q4FY26, FY26 are wrong (Q4FY26 off by 26.24 cr,
FY26 off by 33.43 cr); correct consolidated figures reconcile to consolidated segment Total
Results (L361), and the SEGMENT ANALYSIS "identical operating figures" claim is false for
those prior periods. Coverage, adversarial completeness, and all governance checks PASS;
this is a contained arithmetic/consistency fix. A4 must recompute those six cells from
consolidated inputs (L298-320 / L361) and correct the header claim, then re-emit.

```yaml
stage: A5-adversary
company: "GMDCLTD"
quarter: "Q1FY27"
model: claude-opus-4-8
status: complete
verdict: INCOMPLETE
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches:
  - {metric: "Operating EBITDA (cons) Q4FY26", a4_value: 130.44, recomputed: 104.20, source_line: "L312/307/306/299"}
  - {metric: "Operating EBITDA (cons) FY26", a4_value: 477.20, recomputed: 443.77, source_line: "L312/307/306/298"}
  - {metric: "Operating EBITDA (cons) Q1FY26", a4_value: 169.90, recomputed: 169.24, source_line: "L312/307/306/300"}
  - {metric: "Core PBT ex-OI (cons) Q4FY26", a4_value: 76.31, recomputed: 50.07, source_line: "L312/299 ties L361"}
  - {metric: "Core PBT ex-OI (cons) FY26", a4_value: 355.35, recomputed: 321.92, source_line: "L312/298 ties L361"}
  - {metric: "Core PBT ex-OI (cons) Q1FY26", a4_value: 147.40, recomputed: 146.73, source_line: "L312/300 ties L361"}
surviving_bear_counters: []
loop_back_to: "A4"
gap: "Consolidated Step 1C Operating EBITDA and Core PBT ex-OI for Q1FY26/Q4FY26/FY26 carry standalone values (Q4FY26 off 26.24 cr, FY26 off 33.43 cr); correct cons figures tie to consolidated segment Total Results L361. Also correct the SEGMENT ANALYSIS 'identical operating figures' claim, which holds only for Q1FY27."
```
