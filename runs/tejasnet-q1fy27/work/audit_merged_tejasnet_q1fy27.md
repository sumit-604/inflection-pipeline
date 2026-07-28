# A5 ADVERSARY / COMPLETENESS AUDIT — Tejas Networks (TEJASNET) Q1 FY27
# Auditing: review_merged_tejasnet_q1fy27.md (A4 merged Role 4 + Role 5)
# Fresh context: A4 review + A1 extracts + A2 ledgers only. All A4/A3 cites re-checked, not deferred to.
# All ₹ Crore. Consolidated basis unless stated. Filing anchors = A1 extract line numbers.

---

## AUDIT 1 — COVERAGE

Fresh grep/sweep re-run of each A1 extract, diffed against the A2 ledgers, then every ledger row checked for citation-or-review in A4.

| Category | A2 count | My fresh count | Orphan / missing rows | Status |
|---|---|---|---|---|
| Concall participants | 14 | 14 (6 mgmt/mod + 8 analysts; lines 28/164 + 40..216) | none — Sanjay Malik MGMT_ABSENCE + "co Priam" both carried in A4 Step 0B | PASS |
| Concall turns | 109 | 109 (lines 28–244, even-line paragraphs; (244−28)/2+1) | none | PASS |
| Concall analyst questions | 37 (A2 says 35 subst + 2 proc) | **38 (36 subst + 2 proc)** — ledger TABLE §3 enumerates Q1..Q36 = 36 substantive | **A2 count defect** (see note C1); NO content orphan — A4 reviewed all, incl. ledger Q36 | PASS-with-flag → A2 |
| Concall mgmt-number rows | 40 | 40 (38 disclosed + 2 declines) | none — reviewed via A4 Steps 1/2/7A (18-row reconciliation) + F7-4 declines | PASS |
| Concall forward/hedge phrases | 27 | 27 | none — reviewed via A4 Steps 2/5B/6B/6C/8F | PASS |
| Concall A3 findings (F6-1..6, F7-1..5, F14-1..4, F17-1..6) | 21 | 21 | none — every one cited in A4 (see note C2) | PASS |
| Concall F17 silences (PLI, ₹950 Cr impairment, ₹365 Cr DTA, QIP, BharatNet III, VIL) | 6 | 6 | none — all carried in A4 Step 5B + C.3, each count=1 | PASS |
| Results notes | 14 (6 std + 8 cons) | 14 | none — A4 preamble + Section A restate load-bearing notes (warranty note 4/6, segment note 2/3, balancing-figure note 5/7) | PASS |
| Results line_items | 76 | 76 (36 std + 37 cons + 3 Note-4 summary) | none — load-bearing rows spot-verified against A4 tables A.1/A.3 (all tie) | PASS |
| Results zero_standing / auditor_paras / entities / signatures | 5 / 11 / 4 / 5 | 5 / 11 / 4 / 5 | none | PASS |
| Presentation slides / table rows / data pts / mgmt_numbers | 3 / 3 / 9 / 10 | 3 / 3 / 9 / 10 | none — CFO-quote cash **589** (doc l.82) directly present, corroborates A4 anchor | PASS |

**Note C1 (A2 question-count off-by-one — return to A2, non-blocking).** The A2 concall ledger's COUNT TEST and YAML report `questions: 37 (35 substantive + 2 procedural)`, but the ledger's own §3 table enumerates **Q1..Q36 = 36 substantive** plus P1/P2 = **38 rows**. My fresh sweep confirms 36 substantive (Vay's turn at l.230 explicitly states "I'll just combine two questions in one… That is one. Second…" → edge-router-chip = ledger Q35, FY27-31 growth = ledger Q36; l.218 similarly splits into Q32/Q33). A4 collapsed the final pair into its own Q35 ("AI edge router — own AI accelerator chip? + FY27–31 consistent growth?"), so A4's inventory shows 35 substantive but **reviews the content of all 36**. Net: the enumeration TABLE is complete (nothing missing, no orphan); only A2's count summary/gate arithmetic is off by one (should read 36 substantive / 38 total). Correct the A2 count reconciliation; no A4 content gap, no A3 miss.

**Note C2 (A3 finding citation trace, all 21 present in A4).** F6-1 (l.291/424); F6-2 (l.422/450); F6-3 (l.420/461); F6-4 (l.423); F6-5 (l.422); F6-6 (l.134/356/392/425); F7-1 (l.270/359/426); F7-2 (l.205/317/427); F7-3 (l.229/487); F7-4 (l.159/206/216/223/431); F7-5 (l.207/329/381/496); F14-1 (l.351/352); F14-2 (l.134/346); F14-3 (l.270/359/426); F14-4 (l.40/348); F17-1 (l.298); F17-2 (l.299/429/482); F17-3 (l.300/428/481); F17-4 (l.301/421/464/483); F17-5 (l.302/430/488); F17-6 (l.303/430/488). No orphan A3 row.

**Coverage verdict: PASS.** No orphan row (nothing in a ledger table absent from A4). No missing row (nothing my fresh pass found that a ledger table lacks). One A2 count-summary defect (Note C1) flagged for correction; it does not create an unreviewed row.

---

## AUDIT 2 — ARITHMETIC

Every derived metric recomputed from raw A1 numbers (consolidated results extract lines 359–398; standalone 153–191; note 4 summary 449–453; concall spoken figures; press-release l.82).

| Metric | A4 value | My recompute | Source line(s) | Status |
|---|---|---|---|---|
| Op EBITDA Q1 FY27 (PBT+D&A+FC−OI) | (100.36) | −270.81+94.35+85.07−8.97 = **−100.36** | 375/371/370/363 | PASS |
| Op EBITDA Q4 FY26 | (118.20) | −280.80+100.84+72.04−10.28 = **−118.20** | 375/371/370/363 | PASS |
| Op EBITDA Q1 FY26 | (135.67) | −297.35+96.46+74.77−9.55 = **−135.67** | 375/371/370/363 | PASS |
| Op EBITDA FY26 | (681.83) | −1354.01+402.73+302.83−33.38 = **−681.83** | 375/371/370/363 | PASS |
| Op EBITDA margin Q1FY27 / Q4 / Q1FY26 / FY26 | −24.96 / −35.53 / −67.17 / −61.80% | −100.36/402.16=**−24.96**; −118.20/332.69=**−35.53**; −135.67/201.98=**−67.17**; −681.83/1103.28=**−61.80** | 362 | PASS |
| Revenue YoY | +99.11% | 402.16/201.98−1 = **+99.11%** | 362 | PASS |
| QoQ growth (CEO "20%", cons basis) | +20.88% | 402.16/332.69−1 = **+20.88%** | 362 | PASS |
| QoQ growth (CFO "21%", std basis) | +21.16% | 401.95/331.76−1 = **+21.16%** | 156 | PASS (dual-basis, confirms F14-2) |
| Finance costs YoY | +13.86% | **cons** 85.07/74.77−1 = **+13.78%**; **std** 85.04/74.69−1 = **+13.86%** | 370 / 164 | MINOR — basis-label (see A1) |
| D&A YoY | −2.19% | 94.35/96.46−1 = **−2.19%** | 371 | PASS |
| Core operating PBT ex-OI improvement YoY | +27.12 | (−270.81−8.97) − (−297.35−9.55) = **+27.12** | 375/363 | PASS |
| PAT worsened YoY | −8.37 | −202.24−(−193.87) = **−8.37** | 380 | PASS |
| Deferred-tax benefit swing YoY | −34.90 | (−68.57)−(−103.47) = **+34.90 less benefit** | 378 | PASS |
| PAT bridge YoY | −8.37 = +26.54 PBT − 34.90 tax | ΔPBT −270.81−(−297.35)=+26.54; −34.90 tax; sum **−8.36≈−8.37** | 375/378/380 | PASS |
| S–C PAT gap Q1FY26 / Q4 / Q1FY27 / FY26 | +0.04/+7.12/0.00/+7.54 (0.02/3.26/0.00/0.82%) | −193.87−(−193.91)=**+0.04**; −211.34−(−218.46)=**+7.12**; **0.00**; −908.89−(−916.43)=**+7.54**; %s tie | 174/380 | PASS |
| **Debt identity — cash** | **589** (rejects ASR "489") | gross 4,866 − net 4,277 = **589**; press release l.82 states **589** directly | concall l.32; press l.82 | PASS — A4 correctly anchored 589 |
| PBT −271 comparator map | cons Q4 **−280.80** (not std −287.92) | cons Q4 PBT = −280.80; std Q4 = −287.92 | 375 / 169,451 | PASS — consolidated basis confirmed (F14-4) |
| Net receivables move | +~325 (2,232 vs ~1,907) | 2,232−1,907 = **+325** (ND-filed; base ASR "1,95") | concall l.32/80 | PASS |
| Inventory move | −80 (2,438→2,358) | 2,438−2,358 = **−80** (ND-filed) | concall l.32 | PASS |
| Net debt QoQ | +746 (3,531→4,277) | 4,277−3,531 = **+746**; gross +831 (4,866−4,035) | concall l.32 | PASS |
| Receivables as % of revenue | ~81% | 325/402.16 = **80.8%** | derived | PASS |
| Q1 revenue annualised | ~1,608 | 402.16×4 = **1,608.6** | 362 | PASS |
| Net-debt headroom to ₹4,500 break | 223 | 4,500−4,277 = **223** | concall l.32 | PASS |

**Note A1 (finance-cost basis label — return to A4, non-blocking).** A4 §A.2 is headed "Q1 FY27 YoY (consolidated)" yet the +13.86% finance-cost figure is the **standalone** ratio (85.04/74.69 = +13.86%, l.164); the **consolidated** ratio (matching the rest of §A.2 and table A.1's 85.07/74.77) is **+13.78%** (l.370). Both values are individually correct on their stated basis — this is not a computation error, it mirrors A4's own dual-basis handling of the 20%/21% QoQ — but the standalone number sits inside a consolidated-labelled section. Recommend A4 relabel to +13.78% (consolidated) or annotate as standalone. Immaterial (0.08pp); does not alter "the one adverse scaler" reading. Not a FAIL.

**Note A2 (DTA quantum self-consistency — A4, cannot re-derive from extract).** A4 cites DTA both as "₹365 Cr (52% equity)" (l.71, from Notion TBC) and "~₹434 Cr … 52% of equity" (l.428/481). No Q1 balance sheet exists under Reg 33, so neither is derivable from the provided extract (cumulative P&L deferred-tax benefit FY26 445.10 + Q1 68.57 is a flow, not the DTA balance), and "52% of equity" reconciles to neither against FY26 consolidated equity (share cap 181.01 + reserves 2,749.86 = 2,930.87). Carried thesis-memory, not anchored evidence per CLAUDE.md. Recommend A4/Role-1 reconcile the ₹365-vs-₹434 figure. Out of arithmetic-audit scope (not computable from A1); does not block.

**Arithmetic verdict: PASS.** Every load-bearing derived metric reconciles exactly. The special-attention items all confirm A4: cash anchored to **589** (ASR "489" rejected, and independently corroborated by press-release l.82); PBT −271/−281 mapped to the **consolidated** column (−280.80, not standalone −287.92); the 20%/21% QoQ is a genuine std-vs-cons artifact (+21.16% / +20.88%); receivables +325 and inventory −80 cited to the correct (ND-filed) turns. Two non-blocking notes (finance-cost basis label; DTA quantum) named above.

---

## AUDIT 3 — ADVERSARIAL READ

A4's three most-positive merged claims (C.5 "Positives the concall adds"), each attacked with the strongest bear counter buildable from the same extracted text.

**Positive claim 1 — "The net-debt rise is *explained* and is largely working-capital/receivables-driven with a *credible mechanism* for near-term unwind (IF the BSNL add-on lands)."**
Strongest bear counter (same text): the unwind is contingent on the BSNL add-on order that has slipped a **6th consecutive quarter** ("final stages… probably this quarter", l.34); management **conceded non-BSNL collections are also sticky** (l.82), so receivables are not converting even absent BSNL; net debt is +₹746 QoQ with **no forward peak guided** (l.32); and the **QIP/equity lever went entirely unmentioned** amid RED net debt (F17-4). "Credible near-term unwind" is therefore un-timelined and order-contingent, not credible on the text.
Survives? **Already incorporated.** A4 carries this verbatim in C.1 (structural weighting), C.5 negatives (i)/(iv)/(v), the flag block, and residual questions 2/3/5. No new graft required.

**Positive claim 2 — "International traction is real and named (S. America end-to-end win in the order book, Europe 5G radios, Africa DWDM)."**
Strongest bear counter (same text): the order book is only **7% international** (l.114) against **~50% international *revenue*** (l.104) — the intl revenue is front-loaded one-time shipments, not durable backlog (F6-6); the NEC relationship was **downgraded live from "exclusive" to "preferred partner"** (l.52, F7-2); and every intl win is **unsized** — NEC TAM declined (l.56), site counts declined (l.50), Africa/power-utility values declined (l.34). "Traction" is real on this quarter's revenue but has no backlog durability and no quantification.
Survives? **Already incorporated.** A4 carries the 7%-vs-50% durability gap (F6-6, monitoring #6 AMBER, residual Q6), the NEC downgrade (Step 6A, residual Q8), and the unsized-wins caveats (F7-4). No new graft required.

**Positive claim 3 — "Structural-WC recovery underway: inventory drew down ₹80 Cr; international orders carry no performance-linked payment + 60–90-day cycles (a better cash cycle)."**
Strongest bear counter (same text): the ₹80 Cr inventory drawdown is dwarfed by the **+₹325 Cr receivables build** — net working capital deteriorated sharply this quarter, not improved; the better intl cash cycle (l.68, F7-5) applies to only the **7% of backlog** that is international, so it barely moves the blended cycle; receivables **absorbed ~81% of revenue** and non-BSNL is sticky. "Recovery on track" is contradicted by the same text — WC worsened in Q1.
Survives? **Already incorporated.** A4 weights the read structural (C.1), calls F7-5 "real but secondary," and lists the ₹80 Cr drawdown only as a "partial offset." No new graft required.

**Volunteered fourth counter (completeness) — management's "employee costs… more or less flat" (l.128) vs the filing.** Consolidated employee benefit expense rose **99.78 → 105.24 QoQ (+5.5%)** and **95.82 → 105.24 YoY (+9.8%)** (l.369; std 95.62→101.06, l.163). A4 records "Employee costs flat (l.128)" (Step 4A Q19; monitorables) **without the verbal-vs-filing cross-check it applied to the "one-off" warranty.** This does **not** survive as a thesis-changing counter: against +99% YoY revenue the cost rise is strong operating leverage, so "flat relative to the business" is defensible and the absolute move is modest — materially unlike the recurring ₹35.11 Cr warranty mislabelled "one-off." Recommendation to A4 (optional, non-blocking): add a one-line cross-check noting employee cost +5.5% QoQ / +9.8% YoY consolidated, for symmetry with the warranty treatment.

**Adversarial verdict: PASS.** All three mandated bear counters are already grafted into the merged review — this is a notably bear-aware A4. No surviving bear counter requires new incorporation before save. One optional symmetry note (employee-cost characterisation) offered; does not block.

---

## VERDICT

**COMPLETE.** No orphan ledger row (every table row is cited or reviewed in A4). No row missing from the ledger enumeration (my fresh pass matches every ledger table). Every load-bearing derived metric reconciles exactly, including all four special-attention concall items (cash = ₹589 with ASR "489" rejected and press-release-corroborated; PBT −271/−281 on the consolidated basis −280.80 not standalone −287.92; QoQ +21.16% std / +20.88% cons; receivables +325 / inventory −80 to the correct ND-filed turns). All 21 concall A3 findings and all six F17 silences are carried. All three most-positive claims already carry their surviving bear counters. Three non-blocking corrections are named for the makers — **A2:** concall question count summary is off by one (36 substantive / 38 total, not 35 / 37; enumeration itself is complete); **A4:** relabel the +13.86% finance-cost YoY as standalone-basis (consolidated = +13.78%), reconcile the DTA ₹365-vs-₹434 figure, and optionally add the employee-cost verbal-vs-filing note — none of which withholds a ledger row, breaks a load-bearing metric, or leaves a surviving bear counter un-incorporated. Proceeds to Notion save.

```yaml
stage: A5-adversary
company: "TEJASNET"
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
non_blocking_notes:
  - agent: A2
    note: "Concall question count summary off by one: ledger table enumerates 36 substantive (Q1..Q36) + 2 procedural = 38, but count-test/YAML report 35 substantive / 37 total. Enumeration is complete (no orphan, no missing content; A4 reviewed ledger Q36 within its Q35). Correct the count reconciliation."
  - agent: A4
    note: "Finance-cost YoY +13.86% (section A.2 labelled consolidated) is the STANDALONE ratio (85.04/74.69, l.164); consolidated is +13.78% (85.07/74.77, l.370). Both correct on basis; relabel or annotate. Immaterial 0.08pp."
  - agent: A4
    note: "DTA cited as both Rs.365 Cr (l.71, Notion TBC) and ~Rs.434 Cr (l.428/481), each as '52% of equity'; not derivable from the Reg-33 extract (no Q1 balance sheet). Reconcile the figure; carried memory, not anchored."
  - agent: A4
    note: "Optional symmetry: management 'employee costs flat' (l.128) vs filing employee benefit expense +5.5% QoQ / +9.8% YoY consolidated (l.369). Not thesis-changing (operating leverage vs +99% revenue); add a one-line verbal-vs-filing note for parity with the warranty treatment."
```
