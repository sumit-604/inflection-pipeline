# A5 ADVERSARY / COMPLETENESS AUDIT — Kirloskar Electric Company Limited (KECL) — Q1 FY27

**Agent:** A5 ADVERSARY | **Model:** claude-opus-4-8
**Inputs (only):** A4 review `review_kecl_q1fy27.md`; A1 extract `extract_results_kecl_q1fy27.txt` (original -layout 1-878 + VERBATIM RE-EXTRACTION 881-1301); A2 ledger `ledger_results_kecl_q1fy27.md`.
**Method:** Fresh context. Counts re-run with my own grep pass; every derived metric recomputed from raw Lakhs figures (x0.01 -> Rs Cr); every auditor quote checked against the verbatim block 881-1301. I do not defer to A4's or A3's cites.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate)

The A4 review carries a PLAIN-LANGUAGE BRIEF (lines 395-411) with all four labelled parts present and non-empty:

| Brief part | Location | Present? | Content check |
|---|---|---|---|
| (1) Summary narrative | l.397-399 | **present** | ~20-line FILING/ANALYSIS-tagged narrative; revenue, loss, solvency, both fixes, verdict all covered. Real content. |
| (2) SECTOR intelligence | l.401-403 | **present** | Segments, order intake, sector tailwinds/cyclicality; EXTERNAL-GENERAL correctly labelled. |
| (3) BUSINESS-MODEL intelligence | l.405-407 | **present** | Unit economics, operating leverage, balance-sheet-repair framing, Kirsons BV shell. |
| (4) COMPETITION intelligence | l.409-411 | **present** | Capital-disadvantage thesis, niche wins, conversion risk; EXTERNAL-GENERAL labelled. |

**Gate 0 = PASS.** All four parts present with substantive, non-placeholder content.

---

## AUDIT 1 — COVERAGE (fresh independent enumeration vs A2 ledger)

Fresh grep + manual sweep over the extract. Diff against A2 `=== A2 COUNT TEST ===`.

| Category | A2 count | My fresh count | Method / anchors | Orphan rows | Status |
|---|---|---|---|---|---|
| Numbered notes | 14 | 14 | notes 1-14 at l.253-400 (grep `^\s*[0-9]{1,2}\s` in 250-406; sweep 1..14 no gaps) | none | PASS |
| P&L line items | 28 | 28 | value/dash/blank rows l.96-134 (26 value/dash + 2 blank ZERO_STANDING: Adj-earlier-years l.113, Deferred tax l.114) | none | PASS |
| Segment line items | 32 | 32 | segment table l.163-241 / verbatim 907-986 | none | PASS |
| Agenda items | 3 | 3 | grep `^\s*[0-9]\.\s` l.43/47/53 | none | PASS |
| Auditor paras standalone | 10 | 10 | verbatim l.1010-1125: paras 1,2,3,4,5(KAM),6(EOM),6a,6b,7 + signature | none | PASS |
| Auditor paras consolidated | 12 | 12 | verbatim l.1145-1299: 1,2,3,4(SEBI33(8) unnum.),4/5?... -> 1,2,3,+33(8),4(KAM),5(EOM),5a,5b,6(OtherMatters),7(concl),8,signature | none | PASS |
| Annexure-2 rows | 3 | 3 | grep `^\s*[0-9]\.\s` l.781/783/786 | none | PASS |
| Annexure-3 blocks | 9 | 9 | l.807-870 distinctive openers | none | PASS |
| Named entities | 7 (+2 unnamed) | 7 (+2 unnamed) | Kirsons BV, Kelbuzz, SKG Terra, SLPKG, Luxquisite, Kaytee, Kirloskar Power Equipments; +unnamed subsidiary/associate | none | PASS |
| Signature blocks | 4 | 4 | CS Bhat (l.58), Chairman (l.408), auditor standalone (l.553/1113), auditor consol (l.757/1286) | none | PASS |

**Orphan-row check (ledger rows absent from A4):** A4's LEDGER-RECONCILIATION PREAMBLE (l.14-27) explicitly enumerates and marks all 14 notes / 28 P&L / 32 segment / 22 auditor / 3 agenda / 3 Annexure-2 / 9 Annexure-3 / 7 entity / 4 signature rows as reviewed. Load-bearing rows are individually cited downstream (notes in 0D; P&L in Step 1; segment proxies in Step 5 [l.985/965/941/954/960/946/986]; auditor paras in the opinion check l.66-70; entities in the S-vs-C section; annexures in monitorables). Non-load-bearing rows are covered by the explicit "all reviewed" statement (protocol-permitted "reviewed, no finding"). **No orphan rows.**

**Rows my fresh pass found that the ledger lacks:** none. My independent counts equal A2's in every category.

**COVERAGE = PASS.** No loop-back to A2 (nothing missing from ledger); no loop-back to A3 (no unreviewed row).

---

## AUDIT 2 — ARITHMETIC (recomputed independently from raw Lakhs)

### 2A. Headline YoY table (Step 2A) — recomputed from raw

| Metric | A4 value | My recompute (from raw Lakhs) | Source lines | Status |
|---|---|---|---|---|
| Revenue YoY | -21.5% | 10,385/13,224 - 1 = -21.47% | 96 | MATCH |
| Op EBITDA Q1FY27 | (0.37) | -595 +101 +525 -68 = -37 lakhs = (0.37) | 108/105/104/97 | MATCH |
| Op EBITDA Q1FY26 | 6.91 | 45 +107 +635 -96 = 691 = 6.91 | 108/105/104/97 | MATCH |
| Op EBITDA margin change | -559 bps | 5.23% -> -0.36% = -5.59 pp | derived | MATCH |
| Gross margin (consumed) Q1FY27 | 22.2% | (10,385-8,083)/10,385 = 22.17% | 96/100 | MATCH |
| Gross margin (consumed) Q1FY26 | 26.9% | (13,224-9,671)/13,224 = 26.87% | 96/100 | MATCH |
| Gross margin (consumed) change | -470 bps | 26.87% -> 22.17% = -4.70 pp | derived | MATCH |
| Depreciation YoY | -5.6% | 101/107 - 1 = -5.61% | 105 | MATCH |
| Finance costs YoY | -17.3% | 525/635 - 1 = -17.32% | 104 | MATCH |
| Other income YoY | -29.2% | 68/96 - 1 = -29.17% | 97 | MATCH |
| Core PBT ex-OI Q1FY26 | (0.51) | 45 - 96 = -51 = (0.51) | 110/97 | MATCH |
| Core PBT ex-OI Q1FY27 | (6.63) | -595 - 68 = -663 = (6.63) | 110/97 | MATCH |
| Core PBT ex-OI deterioration | -6.12 | -663 - (-51) = -612 = -6.12 | derived | MATCH |
| Reported PAT Q1FY27 | (5.99) | -599 = (5.99) | 115 | MATCH |

Headline YoY table recomputes clean in every cell.

### 2B. PAT bridge (Step 4) — recomputed from raw

Total YoY PAT change = -599 - 45 = **-644 lakhs = -Rs6.44 Cr** (A4: -6.44) MATCH.

| Bridge component | A4 | My recompute | Status |
|---|---|---|---|
| Gross profit change (net-materials) | -4.98 | GP_net Q1FY27 (10,385-8,083+912=3,214)=32.14; Q1FY26 (13,224-9,671+159=3,712)=37.12; delta -4.98 | MATCH |
| Employee + Other exp change | -2.30 | (1,952+1,299) - (1,844+1,177) = 3,251-3,021 = +230 cost -> -2.30 | MATCH |
| = Op EBITDA change | -7.28 | -4.98 -2.30 = -7.28 (ties to 6.91->-0.37) | MATCH |
| Depreciation change | +0.06 | 107-101 = +6 = +0.06 | MATCH |
| Finance cost change | +1.10 | 635-525 = +110 = +1.10 | MATCH |
| Other income change | -0.28 | 68-96 = -28 = -0.28 | MATCH |
| = Reported PBT change | -6.40 | -7.28 +0.06 +1.10 -0.28 = -6.40 (ties to -595 - 45) | MATCH |
| Tax change | -0.04 | nil -> 4 lakhs charge = -0.04 | MATCH |
| Exceptional | 0.00 | nil both quarters | MATCH |
| Reported PAT change | -6.44 | -6.40 -0.04 = -6.44 | MATCH |

PAT bridge recomputes clean and is internally consistent (component sum ties to the endpoint PAT swing).

### 2C. Other derived metrics (Step 1C, S-vs-C, segment proxies)

| Metric | A4 | My recompute | Source | Status |
|---|---|---|---|---|
| Reported EBITDA Q1FY27 | 0.31 | -595+101+525 = 31 = 0.31 | 108/105/104 | MATCH |
| Reported EBITDA margin Q1FY27 | 0.30% | 31/10,385 = 0.30% | derived | MATCH |
| FY26 Op EBITDA ex-exc | 35.60 | 1,684+434+2,548-1,106 = 3,560 | 108/105/104/97 | MATCH |
| FY26 Op EBITDA reported | 27.51 | 875+434+2,548-1,106 = 2,751 | 110/... | MATCH |
| FY26 core PBT ex-OI ex-exc | 5.78 | 875 -1,106 +809 = 578 | 110/97/109 | MATCH |
| Effective tax rate FY26 | 3.4% | 30/875 = 3.43% | 112/110 | MATCH |
| S-vs-C PAT gap FY26 | 0.07 | 845-838 = 7 lakhs | 115 | MATCH |
| Unallocated cap-emp Q1FY27 | (195.05) | (19,505) std [A] | verbatim 985 | MATCH |
| Unallocated cap-emp Q4FY26 | (148.94) | (14,894) std [B] | verbatim 985 | MATCH |
| Unallocated QoQ deterioration | ~46 Cr | 19,505-14,894 = 4,611 = 46.11 | derived | MATCH |
| Others cap-emp Q1FY27 | 79.66 | 7,966 [A] | verbatim 965 | MATCH |
| Total cap-emp std vs consol Q1FY27 | 126.46 vs 125.94, gap 0.52 | 12,646 vs 12,594 = 52 lakhs | verbatim 986 | MATCH |
| Gross margin net-materials Q1FY27 | 30.9% | 3,214/10,385 = 30.95% | 96/100/101 | MATCH |
| Gross margin net-materials Q1FY26 | 28.1% | 3,712/13,224 = 28.07% | 96/100/101 | MATCH |
| **Gross margin net-materials Q4FY26** | **3.99%** | **(16,357-11,306+378)/16,357 = 5,429/16,357 = 33.19%** | **96/100/101** | **MISMATCH** |
| **Gross margin net-materials FY26** | **28.4%** | **(58,934-41,643+677)/58,934 = 17,968/58,934 = 30.49%** | **96/100/101** | **MISMATCH** |

**ARITHMETIC FAIL — two cells (loop back to A4):**

1. **Step 1C, gross margin NET-materials basis, Q4 FY26:** A4 states **3.99%**; recomputed **33.2%** (source l.96/100/101). Off by ~29 pp. The value is not even a plausible gross margin (it sits next to the Op-EBITDA margin 3.94% and appears to be a mis-paste from that adjacent metric). A4's own asterisk note attempts to explain it as "depressed by that quarter's large other expenses" — but other expenses are not in a gross-margin calculation, so the note is incoherent and does not rescue the figure.
2. **Step 1C, gross margin NET-materials basis, FY26:** A4 states **28.4%**; recomputed **30.5%** (source l.96/100/101). Off by ~2.1 pp, unflagged.

**Materiality note (for the A4 fix, not a reprieve):** both erroneous cells are in the supplementary Step-1C derived table and are NON-load-bearing. The load-bearing net-materials pair that A4's GAP-2 argument actually uses — Q1 FY27 (30.9%) vs Q1 FY26 (28.1%) — recomputes correct, as do the entire headline YoY table, the full PAT bridge, the consumed-basis gross-margin series (26.9% -> 22.2%), the segment proxies, and the S-vs-C gaps. The verdict logic (PROCEED WITH FLAGS) does not depend on the two wrong cells. **The required fix is a table correction (Q4FY26 -> ~33.2%, FY26 -> ~30.5%) and deletion/repair of the incoherent Q4 asterisk note; no re-analysis is needed.** Per the A5 arithmetic rule ("any mismatch above rounding = FAIL"), this nonetheless bars a COMPLETE verdict until corrected.

---

## AUDIT 3 — ADVERSARIAL READ (three most-positive claims, strongest bear counter from the same text)

**Claim 1 — "Record Q1 order book Rs184 Cr (+28% YoY, +36% QoQ, book-to-bill 1.79x); the one genuine forward positive" (A4 verdict l.391; press l.813).**
Strongest bear counter from the same extract: it is an unaudited management press figure with no firm-vs-framework split; billing FELL -21.5% while inventory BUILT Rs9.12 Cr [101], so orders are not converting to revenue; and the 1.79x book-to-bill is arithmetically flattered by a collapsed billing denominator (184/103.85), i.e. the ratio rises partly because billing shrank, not only because orders grew.
**Survives?** NO — already carried with an explicit bear qualifier. A4 Step 3 (l.201), Question 9 (l.343, "firm vs framework... pre-positioned or unsold stock"), the verdict (l.391), and the brief (l.399, l.411) all reconcile the order book against the inventory build and demand the firm/framework split. The denominator nuance is a restatement of the already-stated "billing fell while orders rose" fact; not thesis-changing. No graft required.

**Claim 2 — "Finance costs fell 17.3% YoY, a cushion to the loss" (A4 Step 2A l.162; press l.828).**
Bear counter: press ties it to "working capital utilisation" (l.828), the segment unallocated-borrowing proxy WORSENED ~Rs46 Cr QoQ [985], and the auditor flags "certain overdue payments to creditors" [1046] — so it is payable-stretch / lower WC drawdown, not net-debt deleveraging, and may self-reverse.
**Survives?** NO — this is GAP 1, already grafted throughout (Step 2B ans 4-5, Step 4 bridge + answer, Step 5, Question 8, verdict flag, brief). No new graft.

**Claim 3 — "Material cost improved to 69.1% of revenue from 71.9%" (press l.826, cited by A4).**
Bear counter: 69.1% is a NET-materials ratio flattered by the Rs9.12 Cr inventory build [101]; on the materials-CONSUMED basis (what hit COGS) gross margin DETERIORATED ~470 bps to 22.2% from 26.9%, and a Rs9.12 Cr build into a -21.5% revenue quarter is a WC red flag.
**Survives?** NO — this is GAP 2, already grafted (Step 1C note v, Step 2B ans 7, Step 4 bridge, Question 9, verdict, brief). No new graft.

**Other positive claims scanned (all carried with bear qualifiers, none survive):** reported book equity Rs132 Cr (flagged as revaluation-reserve artifact, real net worth negative, F11, Q1); FY26 PBT Rs8.75 Cr (stripped to Rs5.78 Cr core, property-sale-inflated OI, Note 10); promoter Rs40 cr infusion "clear endorsement" (reframed as ~5.2% related-party dilution at a promoter-set floor, Question 10); "consolidation adds nothing / Kirsons BV shell" (flipped into the anomalous "except for" governance flag, Q5).

**ADVERSARIAL AUDIT = no surviving bear counters.** A4's loop-1 grafts (GAP1/GAP2) and its existing bear qualifiers already absorb every attack the extract supports. Nothing to loop back to A4 on adversarial grounds.

---

## VERDICT

**INCOMPLETE.** Loop back to **A4**.

- Gate 0 (deliverable-completeness): PASS (all four brief parts present, substantive).
- Coverage: PASS (fresh counts equal A2 in all 10 categories; no orphan rows; nothing missing from ledger).
- Adversarial: PASS (three most-positive claims each already carried with an explicit bear qualifier; no surviving counter).
- **Arithmetic: FAIL** — two derived gross-margin cells in Step 1C are wrong: Q4 FY26 net-materials **3.99% (should be ~33.2%)** and FY26 net-materials **28.4% (should be ~30.5%)**, both from raw l.96/100/101; plus the incoherent Q4 asterisk note. Per the A5 rule "any mismatch above rounding = FAIL," this bars save even though both cells are non-load-bearing and the headline YoY table, PAT bridge, consumed-basis margins, segment proxies and verdict all recompute clean.

**Exact gap for A4:** In Step 1C "Gross margin — NET-materials basis," correct Q4 FY26 to ~33.2% and FY26 to ~30.5%, and delete/repair the incoherent asterisk note (other expenses do not enter a gross-margin calculation). Re-emit; the correction is mechanical and does not disturb any conclusion or the PROCEED WITH FLAGS verdict.

```yaml
stage: A5-adversary
company: "KECL"
quarter: "q1fy27"
model: claude-opus-4-8
status: complete
verdict: INCOMPLETE
plain_language_brief:
  narrative: present
  sector: present
  business_model: present
  competition: present
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches:
  - {metric: "Step 1C gross margin net-materials basis, Q4 FY26", a4_value: "3.99%", recomputed: "33.2%", source_line: "extract l.96/100/101 (16,357/11,306/378 lakhs)"}
  - {metric: "Step 1C gross margin net-materials basis, FY26", a4_value: "28.4%", recomputed: "30.5%", source_line: "extract l.96/100/101 (58,934/41,643/677 lakhs)"}
surviving_bear_counters: []
loop_back_to: "A4"
gap: "Step 1C net-materials gross-margin cells wrong: Q4 FY26 3.99% should be ~33.2%, FY26 28.4% should be ~30.5% (raw l.96/100/101); fix the two cells and the incoherent Q4 asterisk note. Non-load-bearing (headline YoY table, PAT bridge, consumed-basis margins, verdict all recompute clean) but bars COMPLETE per the any-mismatch-above-rounding rule."
```
