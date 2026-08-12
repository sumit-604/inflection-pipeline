# A5 ADVERSARY / COMPLETENESS AUDIT — RE-AUDIT (LOOP 2)
# Stallion India Fluorochemicals Limited (STALLION) — Q1 FY27
# Auditing A4 review r2. Fresh context: A4 review + A1 extract + A2 ledger only.

Scope note: this is a full re-run of all four audits, not a spot-check of the two
claimed fixes. Every number below is re-derived from the A1 extract in raw Lakhs
(x0.01 -> Rs Cr), independent of A4's and A3's cites.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate)

Plain-Language Brief present at review lines 542-619, all four parts labelled and
non-empty:

| Part | Heading | Line(s) | Present / Empty |
|------|---------|---------|-----------------|
| 1 Summary narrative | "### 1. Summary narrative" | 544-571 (27 lines of real content) | PRESENT |
| 2 Sector intelligence | "### 2. Sector intelligence" | 573-585 | PRESENT |
| 3 Business-model intelligence | "### 3. Business-model intelligence" | 588-603 | PRESENT |
| 4 Competition intelligence | "### 4. Competition intelligence" | 606-619 | PRESENT |

Provenance discipline held (general-knowledge / NOT-IN-FILE marked; no fabricated
peer or sector data). GATE PASS.

---

## AUDIT 1 — COVERAGE (fresh independent enumeration vs A2 ledger)

Fresh grep/manual sweep of the A1 extract, diffed against the A2 count block (ledger
lines 13-23) and against A4's reconciliation preamble (review lines 22-33).

| Category | A2 count | My fresh count | Anchors re-walked | Orphan rows | Status |
|----------|---------:|---------------:|-------------------|-------------|--------|
| Financial-results notes (numbered) | 6 | 6 | l.116/118/120/122/124/140 | none | PASS |
| Board agenda items | 7 | 7 | 1 main (l.20-24) + a-f (l.32-45) | none | PASS |
| P&L line items with values (standalone) | 24 | 24 | l.68-97, incl. ZERO_STANDING dash row l.82 | none | PASS |
| P&L section headers (no own value) | 6 | 6 | l.67/71/80/86/87/92 | none | PASS |
| IPO utilisation rows | 5 | 5 | l.127/128-129/130-131/132/133 | none | PASS |
| Auditor limited-review paragraphs | 4 | 4 | l.172/179/188/198 | none | PASS |
| Signature blocks | 4 | 4 | l.50-59/99-108/142-151/209-222 | none | PASS |
| Consolidated P&L lines | 0 | 0 | grep "consolidat|subsidiar" = 0 hits | n/a | PASS |
| Segment rows | 0 | 0 | Note 3 single segment | n/a | PASS |

My fresh counts match the ledger on every category; no row exists in my pass that the
ledger lacks (nothing to loop back to A2). Every ledger row is either cited or marked
reviewed in A4:
- All 6 notes: Step 0D table (l.68-76), Note 5 drives Steps 5/6/8.
- 7 agenda items: results approval (Step 0), items b/c -> Q6/monitorable AR, item d/e
  AGM+book closure monitorable, item f (Swati Ghosh) -> Q7/monitorable.
- 24 P&L lines: Step 1 data table + memo (current/deferred/earlier-period tax l.119-121).
- ZERO_STANDING dash row (l.82) explicitly carried (review l.120, l.281).
- 5 IPO rows: Step 5 utilisation table (review l.311-318).
- 4 auditor paras: Step 0 auditor-opinion check (review l.77-80).
- Both DESIGNATION_MISMATCH signature rows: Q2 + caveat 2 + monitorable.

No orphan rows. COVERAGE PASS. No loop-back to A2 or A3.

---

## AUDIT 2 — ARITHMETIC (recomputed from raw Lakhs)

Every derived cell recomputed independently. "Recomputed" uses unrounded Lakhs then
converts; A4 value in the right column.

| Metric | A4 value | My recompute | Source lines | Status |
|--------|---------:|-------------:|--------------|--------|
| **Gross mat cost/Rev FY26 (the fixed cell)** | **80.14%** | **(36,910.24 − 2,395.94)/43,067.80 = 80.14%** | l.72/73/68 | **PASS (fix confirmed)** |
| Gross mat cost/Rev Q1FY26 | 79.54% | 8,786.70/11,047.19 = 79.54% | l.72/73/68 | PASS |
| Gross mat cost/Rev Q4FY26 | 79.35% | 8,727.78/10,999.43 = 79.35% | l.72/73/68 | PASS |
| Gross mat cost/Rev Q1FY27 | 76.26% | 9,261.60/12,144.60 = 76.26% | l.72/73/68 | PASS |
| YoY gross-margin move (bps) | 328 bps | 79.54 − 76.26 = 3.28 pp | derived | PASS |
| Op EBITDA Q1FY27 | 22.04 | 24.79+0.39+0.09−3.23 = 22.04 | l.79/76/75/69 | PASS |
| Op EBITDA Q1FY26 | 14.30 | 13.86+0.29+0.22−0.07 = 14.30 | l.79/76/75/69 | PASS |
| Op EBITDA FY26 | 57.90 | 58.98+1.48+0.89−3.45 = 57.90 | same | PASS |
| Op EBITDA margin Q1FY27 | 18.15% | 22.04/121.45 = 18.15% | derived | PASS |
| Op EBITDA margin +YoY | +521 bps | 18.15 − 12.94 = 5.21 pp | derived | PASS |
| Reported EBITDA Q1FY27 | 25.27 | 24.79+0.39+0.09 = 25.27 | l.79/76/75 | PASS |
| Core PBT ex-OI Q1FY27 | 21.56 | 24.79−3.23 = 21.56 | l.79/69 | PASS |
| Core PBT YoY | +56.4% | (21.56−13.79)/13.79 = 56.3% | derived | PASS |
| Other Income/PBT Q1FY27 | 13.03% | 322.97/2,478.88 = 13.03% | l.69/79 | PASS |
| Other Income/PBT Q1FY26 | 0.53% | 7.37/1,386.14 = 0.53% | l.69/79 | PASS |
| ETR Q1FY27 | 25.10% | 622.30/2,478.88 = 25.10% | l.84/79 | PASS |
| ETR Q4FY26 | 34.40% | 573.41/1,666.83 = 34.40% | l.84/79 | PASS |
| ETR FY26 | 25.67% | 1,513.85/5,897.96 = 25.67% | l.84/79 | PASS |
| PAT margin Q1FY27 | 15.29% | 1,856.58/12,144.60 = 15.29% | l.85/68 | PASS |
| Revenue YoY | +9.9% | (121.45−110.47)/110.47 = 9.94% | l.68 | PASS |
| Other Income YoY | +4,282.2% | 315.60/7.37 = 4,282% | l.69 | PASS |
| Reported PBT YoY | +78.8% | 1,092.74/1,386.14 = 78.8% | l.79 | PASS |
| PAT YoY | +79.2% | 820.26/1,036.32 = 79.2% | l.85 | PASS |
| EPS YoY | +39.1% | (1.60−1.15)/1.15 = 39.1% | l.93 | PASS |
| Finance cost YoY | −57.8% | (9.18−21.74)/21.74 = −57.8% | l.75 | PASS |
| Depreciation YoY | +33.3% | (38.73−29.05)/29.05 = 33.3% | l.76 | PASS |
| Revenue QoQ | +10.4% | (121.45−109.99)/109.99 = 10.4% | l.68 | PASS |
| Op EBITDA margin QoQ | +329 bps | 18.15 − 14.86 = 3.29 pp | derived | PASS |
| Core PBT QoQ | +40.3% | (21.56−15.37)/15.37 = 40.3% | derived | PASS |
| PAT QoQ | +69.8% | 1,856.58/1,093.42 − 1 = 69.8% | l.85 | PASS |
| PAT bridge total | +8.20 | 1,856.58−1,036.32 = 820.26 → 8.20 | l.85 | PASS |
| — core op PBT component | +7.77 | 21.56−13.79 = 7.77 | derived | PASS |
| — Other Income component | +3.16 | 3.23−0.07 = 3.16 | l.69 | PASS |
| — tax increase | (2.72) | 622.30−349.82 = 272.48 → 2.72 | l.84 | PASS |
| Bridge reconciliation | 7.77+3.16−2.72 = 8.21≈8.20 | ties to PBT chg 10.93 (l.79) | derived | PASS |
| OI after-tax share of PAT growth | ~29% | 3.16×(1−0.251)=2.37; 2.37/8.20=29% | derived | PASS |
| Clean run-rate PAT | ~16.2 | 18.57−2.37 = 16.20 | derived | PASS |
| IPO (a) deploy | 108.8% | 10,270.53/9,441.80 = 108.8%; over 8.29 Cr | l.127 | PASS |
| IPO (b) deploy | 103.4% | 2,661.77/2,574.66 = 103.4% | l.128-129 | PASS |
| IPO (c) deploy | 52.0% | 1,100.75/2,117.53 = 52.0%; idle 10.17 Cr | l.130-131 | PASS |
| IPO (e) deploy | 75.0% | 1,198.92/1,598.00 = 75.0% | l.133 | PASS |
| Net proceeds | 144.75 | 14,474.87 Lakh = 144.75 Cr | l.124 | PASS |
| Paid-up share change | +36.76 | 11,608.57−7,932.53 = 3,676.04 → 36.76 Cr | l.95 | PASS |

Sign-convention re-verification (the r1 defect locus): gross-materials cost = Cost of
materials consumed + Change in inventories carried at filed sign. A bracketed change
(finished-goods build) reduces the cost base; a positive change (drawdown) adds to it.
Applied uniformly across all four columns (79.54 / 79.35 / 76.26 / 80.14), the row is
internally consistent and the FY26 cell is 80.14%, not the r1 value of 76.31%. The
328 bps YoY narrative uses only the Q1 columns (79.54 -> 76.26) and does not touch the
FY26 cell, so the corrected cell introduces no downstream inconsistency.

No arithmetic mismatch above rounding anywhere in the r2 review. No new error was
introduced by the edit. ARITHMETIC PASS. No loop-back to A4.

---

## AUDIT 3 — ADVERSARIAL READ

The three most positive claims in A4 r2, each with its strongest bear counter built
from the SAME extract, and whether the counter already appears in the review (a
surviving counter absent from A4 would be a FAIL back to A4).

**Claim 1 — "Core operating PBT +56.4% YoY is clean core growth" (review l.183-185).**
Bear counter (from l.72-73): cost of materials consumed fell to 75.85 Cr from 95.26 Cr
while the inventory line swung ~24 Cr (7.39 Cr build -> 16.76 Cr drawdown), so part of
the core-PBT step-up is stock liquidation, not a repeatable cost structure; run-rate
unconfirmed until inventory rebuilds. Counter SURVIVES — and is already grafted:
Step 2 answer 3 (l.186-195), caveat 6 (l.527-534), Question 9 (l.467), monitorable
(l.490), Step 4 (l.271), Step 8C secondary metric (l.446-447). No re-graft required.

**Claim 2 — "Op EBITDA margin +521 bps / ~328 bps gross-margin gain" (l.178-182).**
Bear counter (same l.72-73 destock) plus the Other-Income overlay: the 328 bps gross
gain is entangled with the drawdown, and the margin optics also benefit from treasury.
Counter SURVIVES — already incorporated (answer 2 explicitly cross-references the
destocking qualifier at l.181-182; caveat 6). No re-graft required.

**Claim 3 — "Reported PAT +79.2%, net-cash and debt-light" (l.170, l.506).**
Bear counter (from l.69, l.127, l.130-131): ~29% of the PAT increase is Other Income
(FD interest on idle IPO cash, l.69), which fades as proceeds deploy; and the "net-cash"
picture masks that the WC IPO object is overspent to 108.8% (l.127) while the
thesis-critical refrigerant object sits 52% idle (l.130-131) — cash is being absorbed
into working capital and away from the catalyst. Counter SURVIVES — already
incorporated: caveat 4 (treasury, l.522-524), caveat 3 (WC overspend, l.520-521),
caveat 1 (catalyst-vs-spend, l.515-517), Questions 3/4. No re-graft required.

No surviving bear counter is missing from A4. Nothing to loop back.

---

## CROSS-CHECKS ON THE TASK-SPECIFIED INVARIANTS

- INDETERMINATE cash conversion caps at PROCEED WITH CAVEATS: held. Step 5 (l.321-337)
  and Protocol Verdict (l.508-511) both name the missing evidence (H1 FY27 cash flow
  statement + balance sheet, Reg 33 half-yearly). Not silently resolved. PASS.
- NOT FOUND / ND used instead of estimates: Notion projections NOT RECORDED (Step 6),
  CFO/capex/WC rows ND by Reg-33 rule (Step 5), Q2/Q3 FY26 marked ND and explicitly
  not split (l.215-217). No figure estimated. PASS.
- Role 5 (concall) correctly N.A. (no transcript/deck filed); not fabricated. PASS.
- Verdict PROCEED WITH CAVEATS is within the permitted set and consistent with the
  INDETERMINATE cap; no STOP verdict used. PASS.

---

## VERDICT

**COMPLETE.**

Both r1 defects are genuinely fixed in r2:
1. FY26 "Gross materials cost / Revenue" now reads 80.14% and all four columns
   reconcile under a single, correctly applied sign convention (79.54 / 79.35 / 76.26
   / 80.14). The 328 bps YoY narrative remains internally consistent.
2. The inventory-drawdown / destocking earnings-quality bear counter is present in the
   quality-of-earnings discussion, the bear column, the caveat list (caveat 6), the
   monitorables, and a new Question 9, and maps to a management question.

No new arithmetic error was introduced by the edit. Coverage still reconciles
(6 notes / 7 agenda / 24 P&L lines / 6 P&L headers / 5 IPO rows / 4 auditor paras /
4 signature blocks / 0 consolidated). All ledger rows cited or reviewed; no orphans.
Adversarial read produced three surviving bear counters, all already incorporated.
Deliverable brief complete. Proceeds to Notion save.

```yaml
stage: A5-adversary
company: "STALLION"
quarter: "Q1FY27"
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
surviving_bear_counters:
  - {claim: "Core operating PBT +56.4% YoY is clean core growth", counter: "Rs 16.76 Cr inventory drawdown vs Rs 7.39 Cr prior-year build; part of the gain is stock liquidation, not repeatable", source_line: "l.72-73", already_incorporated: true}
  - {claim: "Op EBITDA margin +521 bps / ~328 bps gross-margin gain", counter: "328 bps gross gain entangled with the destock plus treasury overlay", source_line: "l.72-73", already_incorporated: true}
  - {claim: "Reported PAT +79.2%, net-cash and debt-light", counter: "~29% of PAT growth is Other Income on idle IPO cash; WC object 108.8% overspent while refrigerant object 52% idle", source_line: "l.69, l.127, l.130-131", already_incorporated: true}
loop_back_to: ""
gap: ""
```
