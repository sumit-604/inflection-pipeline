# A5 ADVERSARY / COMPLETENESS AUDIT — SUGS LLOYD LIMITED (SUGSLLOYD, BSE 544501) — Q1 FY27 (quarter ended 30 June 2026)

Fresh context. I saw only the A4 review, the A1 extract, and the A2 ledger. I re-ran the enumeration with my own grep + line-sweep, recomputed every derived metric from the raw lakh figures at their cite, and constructed bear counters from the same extracted text. I did not defer to A4's or A3's cites; each is re-checked below.

---

## AUDIT 1 — COVERAGE

Fresh enumeration passes (my own grep + manual line sweep over `extract_results_sugslloyd_q1fy27.txt`):

- **notes**: standalone 7 (lines 116-131), consolidated 7 (lines 278-297). Confirmed notes 5 and 7 each appear twice (grep hits 128/292 and 130/295). = **14**.
- **line_items**: standalone table 35 rows (lines 79-114), consolidated 35 rows (lines 217-276). = **70**.
- **zero_standing**: standalone 8 (lines 83, 92, 94, 102, 103, 104, 105, 106), consolidated 7 (lines 224, 239, 242, 255, 256, 258, 262; consolidated line 260 associate share is NON-zero and correctly excluded). = **15**.
- **agenda_items**: single-item board meeting, lines 42-47; my sweep for dividend/AGM/record-date/director/auditor-change/ESOP/capital-raise language returned zero further hits. = **1**.
- **auditor_paras**: standalone 5 (paras 1-4 + Other Matter para 5, lines 149-190), consolidated 7 (paras 1-5 + 6a "We did not review" line 375 + 6b balancing-figure line 400-406). Confirmed 3 distinct "not modified" conclusions at lines 190 / 385 / 406. = **12**.
- **entities**: parent + associate (Vyna Electric, formerly Levana Infra). = **2**.
- **signature_blocks**: 5 (board letter, standalone table DIN block, consolidated table CMD block, standalone auditor sign-off, consolidated auditor sign-off). = **5**.

| Category | A2 count | My fresh count | Orphan rows (in ledger, absent from A4) | Status |
|----------|----------|----------------|------------------------------------------|--------|
| notes | 14 | 14 | none — 7-note table in 0D, S=C substance stated | PASS |
| line_items | 70 | 70 | none — Step 1 standalone + consolidated tables | PASS |
| zero_standing | 15 | 15 | none — blanket "all 15 reviewed" (preamble); exceptional/discontinued cited lines 92/239 | PASS |
| agenda_items | 1 | 1 | none — Role 5 N.A. stub + Monitorables F13 | PASS |
| auditor_paras | 12 | 12 | none material — see note [A] on consolidated para 4 | PASS |
| entities | 2 | 2 | none — S-vs-C gap section + Q1/Q2 | PASS |
| signature_blocks | 5 | 5 | none — Question 7 covers sign-off asymmetry; see note [B] | PASS |

**Rows my fresh pass found that the ledger lacks: NONE.** No missing-from-ledger rows; A2 enumeration is complete.

**Note [A] — consolidated auditor para 4 (Reg 33(8) carve-out, lines 358-361).** The ledger flagged this "for A3/A4" because it has no standalone counterpart. A4 does not name it individually; it is covered only by the blanket "auditor_paras: 12 — all 12 reviewed" reconciliation. This is defensible: the Reg 33(8) carve-out is routine consolidated-review boilerplate and A3 correctly did not elevate it to a finding. Covered as "reviewed, no finding" at category level — **not an orphan**, but it is the thinnest coverage point in the review.

**Note [B] — standalone results-table sign-off (ledger sig-block item 2, lines 132-134) captures DIN only, no name/designation**, vs the consolidated block which captures "Chairman & Managing Director." A4 Question 7 addresses the standalone AUDITOR sign-off missing firm-reg/partner name (lines 191-197 vs 409) and the documentation cluster (A3-04/F14). The results-table designation asymmetry is subsumed in that same documentation cluster. Covered.

**A3 AMBIGUOUS / FORWARD-SIGNAL findings → management-question check:**

| A3 finding | Type | Management question | Status |
|------------|------|---------------------|--------|
| A3-01 (F4 associate ramp) | FORWARD-SIGNAL | Q2 (stake %, drivers of 0.51→4.03) | PASS |
| A3-03 (F10 IPO / EPS) | FORWARD-SIGNAL | Q3 (proceeds, deployment, listing date) | PASS |
| A3-05 (F15 associate rename) | AMBIGUOUS | Q1 (Levana→Vyna reason/effect) | PASS |
| A3-02 (F8 prior-year tax) | NEUTRAL-FACT | Q7 (settlement confirm) | PASS (covered though not required) |
| A3-04 (F14 doc-quality) | NEUTRAL-FACT | Q7 (dup para / missing firm-reg) | PASS (covered though not required) |

Every AMBIGUOUS and FORWARD-SIGNAL finding produced at least one management question. No un-questioned finding.

**COVERAGE VERDICT: PASS. No orphan rows, no missing-from-ledger rows.**

---

## AUDIT 2 — ARITHMETIC

Every value recomputed from raw lakh figures at cite. Rs Cr = lakh × 0.01. "PASS*" = within rounding, with the rounding source noted.

**Tax build (line 97-100):** Q1FY26 194.28+4.61=198.89 ✓ | Q4FY26 374.07−2.80=371.27 ✓ | Q1FY27 275.61−1.79=273.82 ✓ | FY26 998.36+0.04+0.08=998.48 ✓. PASS.

| Metric | A4 value | My recompute (raw lakh) | Source line | Status |
|--------|----------|--------------------------|-------------|--------|
| Op EBITDA Q1FY27 (PBT+D+Fin−OI) | 11.99 Cr | 1024.09+8.78+244.63−78.15=1199.35 | 79-95 | PASS |
| Op EBITDA Q1FY26 | 8.90 Cr | 890.25 | 79-95 | PASS |
| Op EBITDA Q4FY26 | 15.37 Cr | 1537.49 | 79-95 | PASS |
| Op EBITDA FY26 | 43.55 Cr | 4354.80 | 79-95 | PASS |
| Op EBITDA margin Q1FY27 | 15.30% | 1199.35/7840.13=15.298% | 79 | PASS |
| Op EBITDA margin Q1FY26 | 14.98% | 890.25/5941.32=14.984% | 79 | PASS |
| Op EBITDA margin Q4FY26 | 13.36% | 1537.49/11512.35=13.356% | 79 | PASS |
| Op EBITDA margin FY26 | 14.48% | 4354.80/30072.55=14.481% | 79 | PASS |
| Reported EBITDA Q1FY27 | 12.78 Cr | 1277.50 | 79-95 | PASS |
| Core PBT ex-OI Q1FY27 | 9.46 Cr | 1024.09−78.15=945.94 | 80,95 | PASS |
| Core PBT ex-OI Q1FY26 | 7.34 Cr | 733.66 | 80,95 | PASS |
| OI/PBT Q1FY27 | 7.63% | 78.15/1024.09=7.631% | 80,95 | PASS |
| Effective tax rate Q1FY27 | 26.74% | 273.82/1024.09=26.738% | 97-100,95 | PASS |
| Effective tax rate Q1FY26 | 25.58% | 198.89/777.49=25.581% | 97-100,95 | PASS |
| Effective tax rate FY26 | 25.82% | 998.48/3867.92=25.815% | 97-100,95 | PASS |
| PAT margin Q1FY27 | 9.57% | 750.26/7840.13=9.569% | 101,79 | PASS |
| Revenue YoY | +31.96% | 7840.13/5941.32−1=31.960% | 79 | PASS |
| Op EBITDA YoY | +34.72% | 1199.35/890.25−1=34.721% | 79-95 | PASS |
| Op EBITDA margin YoY | +32 bps | 15.298−14.984=**31.3 bps** precise; 15.30−14.98=32 (rounded) | 79-95 | PASS* [C] |
| Depreciation YoY | +8.13% | 8.78/8.12−1=8.128% | 88 | PASS |
| Finance cost YoY | +64.77% | 244.63/148.47−1=64.767% | 87 | PASS |
| EBIT operating Q1FY27 | 11.91 Cr | 1199.35−8.78=1190.57 | 88 | PASS |
| EBIT YoY | +34.96% | 1190.57/882.13−1=34.965% | 88 | PASS |
| Other Income YoY | +78.30% | 78.15/43.83−1=78.302% | 80 | PASS |
| Core Op PBT YoY | +28.94% | 945.94/733.66−1=28.934% | 80,95 | PASS |
| Reported PBT YoY | +31.72% | 1024.09/777.49−1=31.718% | 95 | PASS |
| PAT standalone YoY | +29.67% | 750.26/578.60−1=29.668% | 101 | PASS |
| EPS standalone YoY | −4.21% | 3.41/3.56−1=−4.213% | 113 | PASS |
| PAT consolidated YoY | +30.25% | 754.30/579.11−1=30.251% | 265 | PASS |
| EPS consolidated YoY | −3.65% | 3.43/3.56−1=−3.652% | 274 | PASS |
| Reported EBITDA margin YoY | +57 bps | 16.294−15.722=57.2 bps | 79-95 | PASS |
| **PAT bridge — EBIT change** | +3.08 Cr | 1190.57−882.13=+308.44 lakh | 88-95 | PASS |
| PAT bridge — finance | −0.96 Cr | 148.47−244.63=−96.16 lakh | 87 | PASS |
| PAT bridge — OI | +0.34 Cr | 78.15−43.83=+34.32 lakh | 80 | PASS |
| PAT bridge — tax | −0.75 Cr | 198.89−273.82=−74.93 lakh | 97-100 | PASS |
| PAT bridge — sum ties | +171.66 (rnd +171.67) | +308.44−96.16+34.32−74.93=+171.67 vs reported 750.26−578.60=171.66 | 101 | PASS (1-paisa) |
| Bridge — pre-tax gain | +246.60 lakh | 1024.09−777.49=246.60 | 95 | PASS |
| Bridge — OI share of pre-tax | ~14% | 34.32/246.60=13.9% | 80,95 | PASS |
| Bridge — OI-haircut pre-tax | ~+212.28 lakh | 246.60−34.32=212.28 | — | PASS |
| Consol PAT change | +175.19 lakh | 754.30−579.11=175.19 | 265 | PASS |
| Associate incremental YoY | +3.52 lakh | 4.03−0.51=3.52 | 261 | PASS |
| Associate % consol PAT Q1FY27 | 0.535% | 4.03/754.30=**0.534%** | 261,265 | PASS* [D] |
| Associate % consol PAT Q4FY26 | 0.971% | 10.56/1087.80=0.971% | 261,265 | PASS |
| Associate % consol PAT FY26 | 0.441% | 12.71/2882.16=0.441% | 261,265 | PASS |
| Consol PAT tie Q1FY27 | 754.29 vs 754.30 | 750.26+4.03=754.29 (+0.01 rnd) | 265 | PASS (noted) |
| Implied equity interest | ~21% | 4.03/19.21=20.98% | 261,376-379 | PASS |
| Associate YoY rate | ~+690% | 4.03/0.51−1=690.2% | 261 | PASS |
| Gross margin Q1FY27 | ~59.5% | (7840.13−(3667.25−495.36))/7840.13=59.54% | 79,84,85 | PASS |
| Gross margin Q1FY26 | ~41.2% | (5941.32−(3294.14+199.83))/5941.32=41.19% | 79,84,85 | PASS |
| Employee exp YoY | +121% | 1118.90/506.19−1=121.0% | 86 | PASS |
| Other exp YoY | +124% | 2350.00/1050.91−1=123.6% | 89 | PASS |
| Finance cost / revenue Q1FY27 | 3.1% | 244.63/7840.13=3.12% | 87,79 | PASS |
| Derived 9M FY26 revenue | 185.60 Cr | 30072.55−11512.35=18560.20 lakh=185.60 | 79 | PASS* [E] |
| IPO fresh issue (shares) | 69.64 lakh sh | (2321.40−1625.00)/10=69.64 | 109,110 | PASS |

**No arithmetic mismatch above rounding tolerance.** Notes on the three sub-rounding items:

- **[C] Op EBITDA margin YoY +32 bps.** Precise unrounded expansion is 31.3 bps. A4's "+32 bps" comes from subtracting its own 2-decimal margins (15.30−14.98=0.32). Internally self-consistent and 0.7 bps from precise — within rounding. Not a FAIL. Cosmetic: the sharper statement is "+31 bps."
- **[D] Associate as % of consolidated PAT Q1FY27.** A4 states 0.535%; precise is 0.534% (4.03/754.30). Third-decimal slip on a sub-1% figure, immaterial, within rounding. Not a FAIL.
- **[E] Derived 9M FY26 revenue.** A4 shows 185.60 (correct to lakh precision); its parenthetical "300.73 − 115.12" would read 185.61. The reported 185.60 is the more precise value; no error.

**ARITHMETIC VERDICT: PASS.**

---

## AUDIT 3 — ADVERSARIAL READ

The three most positive claims in A4, each with the strongest bear counter I could build FROM THE SAME EXTRACTED TEXT, and whether the counter survives un-incorporated (which would force a graft into A4).

**Positive claim 1 — "Headline growth is real and operating-led": revenue +31.96% YoY, Op EBITDA outgrew it (+34.72%), margin +32 bps, core PBT ex-OI +28.94% (verdict; Step 2 diagnostics 1-3).**

Bear counter (same text): The EBITDA out-growth is manufactured by the Rs 4.95 Cr inventory swing, not by operations. Combined YoY increase in employee expense (+612.71 lakh, line 86) and other expenses (+1,299.09 lakh, line 89) totals **+1,911.80 lakh — larger than the entire revenue increase of +1,898.81 lakh** (line 79). The only reason EBITDA rose at all is the favourable move in purchases + change-in-inventories (a +495.36 lakh P&L credit vs a −199.83 lakh drawdown a year ago, line 85). So "EBITDA outgrew revenue" rests on a non-cash inventory build, and the operating margin gain is 31-32 bps of noise.

Does it survive? **Substantively YES — and A4 already incorporates it.** Step 5 states the ~18pp gross-margin jump "partly sits in unsold inventory" and that "Employee (+121%) and Other Expenses (+124%) then absorbed most of that gross-margin gain"; Question 4 asks the margin bridge; the verdict is capped at PROCEED WITH CAVEATS explicitly for margin quality. **No new graft required.** One sharpening A4 could add (optional, not a FAIL): the combined opex increase absolutely exceeds the revenue increase (1,911.80 > 1,898.81 lakh) — a crisper way to state the same point.

**Positive claim 2 — "~86% of the pre-tax improvement is operating/core; growth survives an OI haircut (still +24-25%)" (Step 4).**

Bear counter (same text): The "86% operating" figure counts EBIT that itself contains the inventory build; strip the build and the operating contribution shrinks materially. Separately, the finance-cost drag is real and accelerating: −96.16 lakh YoY (+64.77%, line 87), growing at 2x revenue on net debt that is ND. The "quality" of the PAT gain is therefore contingent on the same inventory question plus an unquantified debt build.

Does it survive? **YES, and A4 already incorporates both legs** — the inventory-quality caveat (Step 5, Question 4) and the finance-cost flag (Step 2 diagnostic 5, Question 6, verdict secondary caveat, tripwire 6C(i)). **No new graft required.**

**Positive claim 3 — "Results are clean on their face: unmodified review both S and C, ETR near statutory, no exceptional items, no going-concern/EoM flag" (verdict; 0D).**

Bear counter (same text): "Clean" carries two disclosed data-reliance carve-outs. (i) The consolidated conclusion rests on the associate being reviewed by OTHER auditors and "furnished to us by the Management" (para 6a, lines 380-384) — the principal firm did not review it. (ii) The Q4 FY26 comparative is a balancing figure, not independently reviewed (note 7 lines 130-131; Other Matter paras 185-190 / 400-406), so the QoQ base is soft. Also, ETR did not help — it ROSE 25.58%→26.74% YoY (a drag, not a tailwind).

Does it survive? **YES, and A4 already incorporates all three points** — the associate other-auditor/management-furnished reliance (0D, S-vs-C section, Question 7), the Q4 balancing-figure softness (Step 3, note 7 row, monitorable 8), and the rising ETR (Step 4 bridge, "a mild drag"). **No new graft required.**

**ADVERSARIAL VERDICT: no surviving un-incorporated bear counter.** Each of the three strongest counters is already grafted into A4's caveats, questions, tripwires, and PROCEED WITH CAVEATS cap. The optional sharpening under claim 1 (opex increase exceeds revenue increase in absolute lakh) is an enhancement, not a completeness gap.

---

## VERDICT

**COMPLETE.**

- Coverage: 7/7 categories reconcile between my fresh enumeration and the A2 ledger (14 notes, 70 line items, 15 zero-standing, 1 agenda, 12 auditor paras, 2 entities, 5 signature blocks). No orphan rows; no rows missing from the ledger. Every A3 AMBIGUOUS/FORWARD-SIGNAL finding produced a management question.
- Arithmetic: every derived metric in A4's tables recomputed from raw lakh at cite. No mismatch above rounding. Three sub-rounding cosmetics noted (32 vs 31.3 bps; 0.535 vs 0.534%; 185.60 vs 185.61) — all within tolerance and internally consistent.
- Adversarial: the three strongest bear counters are all already incorporated into A4; none survives un-grafted.

The review may proceed to Notion save.

```yaml
stage: A5-adversary
company: "SUGSLLOYD"
quarter: "Q1 FY27 (quarter ended 30 June 2026)"
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
