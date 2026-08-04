# A5 ADVERSARY / COMPLETENESS AUDIT — Park Medi World Limited (PARKHOSPS) — Q1 FY27 (MERGED)

Agent: A5 ADVERSARY | Model: claude-opus-4-8 | Date: 2026-08-04
Under audit: review_parkhosps_q1fy27.md (merged: Section A Role 4 filings, Section B Role 5 concall)
Method: fresh context. Re-derived every metric from the A1 extracts; re-ran the A2 enumeration independently; did not defer to A4's or A3's cites. Concall re-verifications performed per task brief (FY27 guidance arithmetic; ETR-dependency of the +32% PAT guide; deferred-tax disclosure-silence; forward/ambiguous -> question mapping). Unit convention confirmed against every extract header: filing docs Rs Millions x0.1 to Cr, column order Q1FY27 | Q4FY26 | Q1FY26 | FY26; concall Rs Crores as spoken.

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate, run FIRST)

The Plain-Language Brief exists (review lines 804-822) with all four labelled parts present and carrying real, non-placeholder content:

| Brief part | Location | Present? | Content check |
|---|---|---|---|
| (1) Summary narrative | L808-810 | **PRESENT** | ~20-line narrative; carries Rs476Cr/+19% revenue, the ~21% normalized-PAT read, the Rs2,080/530/360 Cr guide, the tax-silence governance point, occupancy 56%<-68%, dilution-to-75% signal, WATCHLIST/AVOID conclusion. Real content. |
| (2) SECTOR intelligence | L812-814 | **PRESENT** | Payer mix 77/23 -> 70:30, CGHS 12-15% Oct-25 hike / 7-7.5% benefit routed to capex, tier-2/3 catchment demand, structural 100-140 debtor days. Real content. |
| (3) BUSINESS-MODEL intelligence | L816-818 | **PRESENT** | IPD-heavy 94.4%, ~Rs36 lakh/bed, OPD-as-funnel, Rudrapur unit economics, 1.22%-of-PAT parent, FCF-inflection untestable, ROCE ~18%. Real content. |
| (4) COMPETITION intelligence | L820-822 | **PRESENT** | Cost/capex-per-bed edge, salaried-doctor model, Tricity densification moat, and symmetric weaknesses (disclosure maturity, ARPOB undisclosed, 83.9% PAT outside principal auditor). Real content. |

**GATE 0 result: PASS.** All four brief parts present and non-empty.

---

## 1. COVERAGE AUDIT (fresh enumeration vs A2 ledgers; orphan-row check vs A4)

### 1A. Fresh count vs ledger

| Category (doc) | A2 count | My fresh count | Orphan rows in A4? | Status |
|---|---|---|---|---|
| Concall turns | 87 | 87 (extract lines 1-87, one per turn) | none | PASS |
| Concall questions | 29 | 29 (grep "?" = 29; each maps to a thread) | none | PASS |
| Concall hedge phrases | 6 | 6 (5-phrase lexicon; turn-33 clarification-hedge correctly excluded) | none | PASS |
| Concall participants | 16 | 16 (4 mgmt + 1 PR + 9 analysts + 1 operator + 1 absent Chairman) | none | PASS |
| Concall forward phrases | 34 | 34 (accepted on documented two-pass regex+sweep reconciliation) | none | PASS |
| Concall mgmt numbers | 199 | 199 (168 unit-tagged + 31 documented date/compound/zero supplements) | none | PASS |
| Results notes | 22 | 22 (10 standalone L211-273 + 12 consolidated L476-549) | none | PASS |
| Results line items | 63 | 63 (27 standalone L165-196 + 36 consolidated L418-461) | none | PASS |
| Results entities (Annexure-I) | 23 | 23 (L377-399) | none | PASS |
| Results auditor paras | 12 | 12 (5 standalone + 7 consolidated) | none | PASS |
| Results agenda items | 3 | 3 (L58 results / L62 Mehar / L68 IPO-object variation) | none (all 3 covered) | PASS w/ note (1C) |

### 1B. A3 findings — every ledger finding cited in A4 or marked reviewed

- RES-A3-01..10: all cited (01 Devina Step0D/Q12; 02 Steps1C/2B/4; 03 Steps0D/4/6; 04 Step0D going-concern; 05 Q14; 06 Step4/Q1; 07 Q13; 08 Step0D/5/Q4; 09 EPS-on-total-PAT Step0C; 10 Q15). No orphan.
- PRES-A1..A9, REL-FND-01..07, MON- (F1-01/02, F6-01/02, F7-01, F14-01): all appear across Steps 5/6/8, monitorables and the Questions table. No orphan.
- FN-01..FN-24 (concall): all 24 appear in the review body (guidance table Step 2, Q&A Steps 4-5, silence table 5B, trigger/pillar tables Step 8, monitorables, Questions Q16-Q22). No orphan.

### 1C. Non-gating discrepancies found (no row left uncovered; nothing routed back)

1. **Preamble count mislabel (self-consistency, not a coverage hole).** Review preamble L13 states "5 board/agenda items"; the results A2 ledger enumerates **3** (grep=sweep=3), and the review's own Step 0D works correctly from 3 (results / Mehar item 2 / IPO-variation item 3). The "5" appears to conflate with the 5 named signature blocks (results ledger §9A). All three actual agenda items are covered. No orphan row; cosmetic.

2. **Forward-signal findings dispositioned as baselines/monitorables rather than dedicated questions.** The Step 8.5 header asserts "Every A3 FORWARD-SIGNAL or AMBIGUOUS finding ... generates >=1 question." I verified the mapping directly:
   - **All 8 AMBIGUOUS findings map to a Question:** FN-02->Q1/Q16, FN-05->Q19, FN-12->Q17, FN-14->Q21, FN-15->Q22, FN-19->Q20, FN-21->Q3, FN-24->Q2. Complete.
   - **7 of 12 FORWARD-SIGNAL findings map to a Question:** FN-01->Q16, FN-03->Q14, FN-04->Q10, FN-10->Q18, FN-13->Q18, FN-17->Q17, FN-23->Q7.
   - **5 FORWARD-SIGNAL findings have no dedicated Question row:** FN-06 (ARPOB 10-12%), FN-07 (payer mix 70:30), FN-08 (margin 26.5-27% held), FN-09 (ROCE +150-200bps), FN-11 (occupancy below 64%). These are instead carried as **delivery-scoring baseline commitments B6-B10 (Step 3) and monitorables 18-22**, and each is cited in Steps 2/5/8.
   
   **Adjudication: PASS, not a FAIL.** These five are quantified forward GUIDANCE numbers management supplied; the protocol-appropriate disposition for a given guidance number is a promise-vs-delivery baseline to score at Q2+, which the review does. The clarification-type (AMBIGUOUS) findings — the ones that genuinely require a question — all map. The Step 8.5 header slightly overstates ("question") where the correct treatment is "trackable obligation." None orphaned; substance complete.

**COVERAGE result: PASS.** No orphan rows (nothing in a ledger is absent from A4); nothing in my fresh pass is missing from the ledgers.

---

## 2. ARITHMETIC AUDIT (recomputed from raw extract; nothing deferred to A4)

Raw source: consolidated L418-461, standalone L165-196, concall turns 2/4/7/10.

| Metric | A4 value | My recompute | Source | Status |
|---|---|---|---|---|
| Op EBITDA Q1FY27 (PBT+D+Fin-OI) | 1,260.88 | 1050.84+188.40+98.10-76.46 = **1,260.88** | L430/427/426/419 | MATCH |
| Op EBITDA Q1FY26 | 1,049.31 | 818.99+147.71+151.33-68.72 = **1,049.31** | L430/427/426/419 | MATCH |
| Op EBITDA margin Q1FY27 | 26.51% | 1260.88/4757.09 = **26.505%** | L418 | MATCH |
| Op EBITDA margin Q1FY26 | 26.31% | 1049.31/3988.45 = **26.309%** | L418 | MATCH |
| Reported EBITDA Q1FY27 (incl OI) | 1,337.34 | 1050.84+188.40+98.10 = **1,337.34** | L430/427/426 | MATCH |
| ETR Q1FY27 | 15.69% | 164.91/1050.84 = **15.694%** | L437/430 | MATCH |
| ETR Q1FY26 | 20.02% | 163.93/818.99 = **20.016%** | L437/430 | MATCH |
| ETR Q4FY26 | 25.74% | 266.12/1033.90 = **25.739%** | L437/430 | MATCH |
| Core PBT ex-OI Q1FY27 | 974.38 | 1050.84-76.46 = **974.38** | L430/419 | MATCH |
| Revenue YoY | +19.27% | 4757.09/3988.45-1 = **+19.27%** | L418 | MATCH |
| Op EBITDA YoY | +20.16% | 1260.88/1049.31-1 = **+20.16%** | derived | MATCH |
| Core PBT ex-OI YoY | +29.87% | 974.38/750.27-1 = **+29.87%** | derived | MATCH |
| PAT YoY | +35.24% | 885.93/655.06-1 = **+35.24%** | L438 | MATCH |
| Depreciation YoY | +27.55% | 188.40/147.71-1 = **+27.55%** | L427 | MATCH |
| Finance cost YoY | -35.18% | 98.10/151.33-1 = **-35.18%** | L426 | MATCH |
| PAT bridge to PBT | +231.85 | 211.57-40.69+53.23+7.74 = **+231.85** (=1050.84-818.99) | derived | MATCH |
| PAT bridge total | +230.87 | 231.85-0.98 = **+230.87** (=885.93-655.06) | derived | MATCH |
| Tax tailwind vs 20.02% ETR | ~45.5mn | 1050.84x0.2002-164.91 = **45.5mn** | derived | MATCH |
| Normalized PAT ex-deferred-tax | ~792.5mn | 885.93-93.40 = **792.53** | L438/435 | MATCH |
| Normalized growth | +21.6% | 792.53/(655.06-3.55)=792.53/651.51-1 = **+21.6%** | derived | MATCH |
| Standalone Op EBITDA Q1FY27 | 12.84 | 17.11+33.81+8.60-46.68 = **12.84** | L177/174/173/166 | MATCH |
| Standalone Op EBITDA margin | 3.83% | 12.84/335.32 = **3.83%** | L165 | MATCH |
| Standalone core PBT ex-OI | (29.57) | 17.11-46.68 = **-29.57** | L177/166 | MATCH |
| Standalone OI/PBT Q1FY27 | 272.82% | 46.68/17.11 = **272.8%** | L166/177 | MATCH |
| Std-vs-consol PAT % Q1FY27 | 1.22% | 10.84/885.93 = **1.223%** | L185/438 | MATCH |
| Std-vs-consol PAT % Q1FY26 | 7.48% | 48.97/655.06 = **7.48%** | L185/438 | MATCH |
| EPS reported vs owners basis | 2.05 vs ~1.91 | 885.93/432m=2.05 (total); 825.07/432m=**1.91** (owners) | L446/460 | MATCH (0C valid) |
| **Guidance: Rev 2080 / FY26 1679.36** | +23.9% ~ spoken 24% | 2080/1679.36 = **+23.86%** | turn7 / L418 FY26 | MATCH |
| **Guidance: PAT 360 / FY26 273.56** | +31.6% ~ spoken 32% | 360/273.56 = **+31.60%** | turn7 / L438 FY26 | MATCH |
| **Guidance: EBITDA 530 / FY26 444.32** | +19.3% (NOT +25%) | 530/444.32 = **+19.29%** | turn7 / derived | MATCH — inconsistency real |
| **Q1 annualised: Rev x4** | ~1,902.8 | 475.71x4 = **1,902.84** | L418 | MATCH |
| **Q1 annualised: PAT x4** | ~354.4 | 88.59x4 = **354.36** | L438 | MATCH |
| **ETR-normalised PAT (25%) x4** | ~315 | 105.08x0.75x4 = **315.24** | L430 | MATCH |
| **Guide-to-normalised gap** | ~Rs 45 Cr (12.5%) | 360-315.24 = **44.76 Cr** | derived | MATCH |
| **Embedded ETR in Rs360 PAT** | ~18.5% | 1-360/442 = **18.55%** | Step7A bridge | MATCH |

**Concall re-verifications (task-specified):**
- **FY27 guidance arithmetic:** revenue and PAT-growth-% tie cleanly to the FY26 filing base; the Rs 530 EBITDA absolute and the spoken +25% cannot both hold off Rs 444.32 Cr FY26 op-EBITDA (a ~Rs 25 Cr internal tension) — A4 flags this correctly. CONFIRMED.
- **ETR-dependency of the +32% PAT guide:** independently reproduced — normalising Q1 to a 25% ETR gives ~Rs 315 Cr annualised vs the Rs 360 Cr guide; the guide embeds ~18.5% ETR persisting, i.e. it requires the non-repeatable deferred-tax benefit to recur or a material H2 EBITDA over-delivery. A4's read is correct. CONFIRMED.
- **Deferred-tax disclosure-silence:** turn 4 verbatim attributes the +220 bps PAT-margin lift "largely on account of reduction in interest outgo following the substantial repayment of term debt" with **no mention of the Rs 93.40mn deferred-tax benefit** (L435); the larger flatterer is the ETR fall (15.69% vs 20.02%). A4's FN-16/FN-20 characterisation (competing causal story, not mere omission) is supported by the text. CONFIRMED.

**ARITHMETIC result: PASS.** Zero mismatches above rounding. Every derived metric reproduces from the raw lines.

---

## 3. ADVERSARIAL READ (three most positive claims; strongest bear counter from the SAME extract)

**Positive claim 1 — "Core operating PBT ex-OI grew +29.87% YoY; the operational core is genuinely expanding, not a treasury illusion" (Step 2 diag 3).**
Bear counter (same text): core PBT ex-OI = PBT - OI still embeds the Rs 53.23mn non-recurring finance-cost drop (finance -35% YoY on now-negligible debt); strip that and operating growth collapses toward the +20% EBITDA rate. And the entire consolidated core is a subsidiary story (parent = 1.22% of PAT, core loss-making), 83.9% of which is other-auditor-reviewed and Rs 26mn reviewed by no auditor.
**Survives? NO — already incorporated.** Step 4 bridge quantifies finance +53.23 as "largely spent (net cash)," normalises PAT to ~21%, and Steps 4/6/Section C carry the 1.22%-parent and 83.9%-unaudited flags. No grafting needed.

**Positive claim 2 — "Debtor-days guidance revised to a realistic 125-130 (credibility-positive; corrects the old sub-100 optimism)" (Step 7C / Section C).**
Bear counter (same text): 125-130 is a "medium-term" forward TARGET; the Q1 actual is ND (no balance sheet), FY26 was already 129, and this is a first-call, delivery-unproven management (provisional OVERPROMISER RISK). Crediting a promise as "positive" rewards words over a delivered number.
**Survives? NO — already incorporated.** Step 5 marks debtor days ND/untestable; Step 8B logs it "GREEN-ish (guidance credible; Q1 actual ND)"; credibility explicitly UNSCORED; monitorable B11 scores it at a balance-sheet quarter.

**Positive claim 3 — "FY27 revenue guide Rs 2,080 Cr (+24%) reconciles cleanly to the FY26 base; confidence HIGH" (Step 2 / Step 7A).**
Bear counter (same text): Q1 annualises to only ~Rs 1,903 Cr; the guide needs +Rs 177 Cr (+9.3%) of second-half ramp on top of a flat run-rate, dependent on CGHS full-impact and new-bed fill into a FALLING occupancy base (56%, management pre-warning full-year occupancy below FY26's 64%). If occupancy keeps sliding, the top-line guide is at risk.
**Survives? NO — already incorporated.** Step 7A path (a) shows the +9.3% H2 ramp requirement and its explicit CGHS/new-bed dependencies; Step 6A marks the annualised ~Rs 1,903 Cr "below base run-rate"; Step 8C names occupancy the single cleanest Q2 metric.

**ADVERSARIAL result: PASS.** All three strongest bear counters were constructible from the extract but are already present in A4's symmetric review with anchors. No surviving counter requires grafting.

---

## VERDICT

**COMPLETE.**

- Deliverable-completeness gate: PASS (all four Plain-Language-Brief parts present and substantive).
- Coverage: PASS (fresh counts match every A2 ledger; no orphan rows; every A3/FN finding incorporated; two cosmetic notes recorded, neither leaves a row uncovered).
- Arithmetic: PASS (every derived metric, the PAT bridge, the ETR series, and the full guidance-vs-filing bridge reproduce from raw lines with zero mismatch above rounding).
- Adversarial: PASS (three strongest bear counters already incorporated; nothing to graft).

No loop-back to A2, A3 or A4 is required. The merged review proceeds to Notion save.

```yaml
stage: A5-adversary
company: "PARKHOSPS"
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
