# A5 ADVERSARY / COMPLETENESS AUDIT — MTAR Technologies Limited (MTAR), Q1 FY27 (4-DOC MERGED)

**Agent:** A5 ADVERSARY | **Model:** claude-opus-4-8 | **Fresh context:** A4 4-doc review + four A1 extracts + four A2 ledgers only (A3 reasoning NOT read; all cites re-derived).
**Under audit:** `review_merged_4doc_mtar_q1fy27.md` (A4). **Second merged audit** (results / press release / presentation / concall).
**Verdict:** COMPLETE (details below). Three audits run in one pass.

---

## AUDIT 1 — COVERAGE (independent fresh enumeration vs the four A2 ledgers; then ledger-row → A4 trace)

Fresh grep/sweep of each extract, diffed against each ledger's A2 count test, then every ledger category traced into A4 (cited OR reviewed-no-finding).

| Doc | Category | A2 ledger count | My fresh count | Orphan rows (ledger→A4) | Status |
|---|---|---|---|---|---|
| Results | notes | 11 (6 consol + 5 std) | 11 | none — all in Step 0D notes table + std/consol notes | PASS |
| Results | line items | 68 (34 std + 34 consol) | 68 | none — Step 1a/1b reproduce both tables | PASS |
| Results | zero-standing | 8 | 8 | none — exceptional/prior-period-tax/OCI carried (Note table, F8-a, F14-c) | PASS |
| Results | agenda items | 7 | 7 | none — AGM 28-Sep, director re-appts, scrutinizer all in Step 8/F13-a | PASS |
| Results | auditor paras | 26 (10 std + 16 consol) | 26 | none — UNMODIFIED opinion, Other-Matters, UDIN/Membership (F14-a/b) all in Step 0D | PASS |
| Results | entities | 3 (MTAR + 2 WOS) | 3 | none — Consol Note 1, NCLT merger (F6-a) | PASS |
| Press rel | financial numbers | 26 | 26 (16 "Rs." + 10 "%") | none — all tie to filing (Step 1/2); PR adds no number absent from filing | PASS |
| Press rel | segment claims | 5 | 5 | none — "highest ever revenue", 5-sector list, 16 units all reviewed | PASS |
| Press rel | zero-standing | 1* | 1 | *A2 shows 0 ZERO_STANDING + 1 operational metric (16 units, OM1); A4 preamble label "1" reconciles to the operational-metric row. No orphan | PASS |
| Press rel | MD sentences | 3 | 3 | none — MD1/2/3 = "inflection point" claims (Step 1 O2, verdict) | PASS |
| Press rel | footnotes/disclaimer | 5 | 5 | none — safe-harbour reviewed (Step 0D concall + PR disclaimer) | PASS |
| Press rel | administrative | 14 | 14 | none — transmittal/contacts reviewed-no-finding (immaterial) | PASS |
| Presentation | slides | 32 | 32 | none | PASS |
| Presentation | numbers | 535 | 535 (per A2 count test) | none material — GP/margin/OB/WC/ROCE/DE/promoter/FII/segment anchors all traced (see below) | PASS |
| Presentation | footnotes | 7 | 7 | none | PASS |
| Presentation | zero-standing | 9 | 9 (ledger l.615) | none — exceptional, lease liab x2, curr-tax-liab, ROU, non-curr invest, non-curr-tax-asset, MF-current all carried (F-01, S26/27) | PASS |
| Concall | participants | 15 | 15 (10 analysts + operator/IR/MD/CFO/Orient) | none — Step 0B roster | PASS |
| Concall | turns | 124 | 124 (odd lines 1–247) | none — Step 0C + Q&A decomposition | PASS |
| Concall | questions | 32 | 32 (Mohit3/Bala2/Gorov7/Sumat3/Vipra3/viral4/Janesh2/Rohit2/Push2/Vipra2nd1/Pria3) | none — Step 4A grades all 32 (Q1–Q32) | PASS |
| Concall | mgmt numbers | 53 | 53 (N1–N53) | none — every N-id traced (see mgmt-number trace) | PASS |
| Concall | forward-hedge | 22 (F1–F12 + H1–H10) | 22 | none — F1–F12 in Step 1/guidance/specificity; H1–H10 = defensive-language count (Step 6C) | PASS |

**Concall 53 mgmt-number trace (task-flagged, verified individually):** N1–N14 (opening) → Step 1 O1–O11; N15–N30 (CFO review) → Step 1c/2/3/5 (incl. N21 gross margin→FF-01, N26 CFO 247.69→FF-02, N27/N28/N29 debt→FF-03, N19/N20 WC→FF-05, N24 ROCE); N31–N34 nuclear → Q3/C7/C8; N35 GST → Q4; N37/N38/N40/N47/N48 capex → Step 5/Q5/Q16-18; N39/N46 order-book drift → FF-04; N41/N42 asset turnover → FF-06; N43–N45 fuel-cell dates → C2/C3; N49/N50 data-center → 5A/C10; N51 Mahi "10 MW" garble → Q19/FF-09; N52 actuator 142 garble → Q26/FF-09; N53 FY30 sizing → C12. **All 53 carried. No orphan.**

**F17 silence set (task-flagged):** A4 Step 5B silence audit populates all sensitive items — promoter-stake decline (FF-14), NCLT merger (FF-15), Bloom concentration + US-tariff/81% export deflected "unwanted noise" (FF-11/FF-17), hot-box units NDA (FF-12), KMP SEBI matter, Weatherford quantum, UDIN, Q1 CFO, subsidiary loans. **All carried; each generates a Questions-for-Management row.**

**Presentation anchor spot-check (fresh grep of ledger):** promoter 31.41/30.59/30.44/29.35 (S31-8/12/16/20) ✓; FII 24.80% (S31-21) ✓; GP 164.2 / margins 54.2%→45.5% (S11-6/7/9) ✓; order book 5,143.3 (S13-8/9) ✓; ROCE 11.4%/17.2% (S30-3/4, recomputed 11.43/17.16) ✓; D/E 0.45 (S30-12, recomputed 0.449) ✓; Kaiga Rs 504 Cr (S7-11) ✓; CE fuel-cell rev 220.8 / 61% (S9-5/10) ✓; MF-current Mar-26 215.3 (S27-11) ✓; ROU 15.0 (S-BS l.433) ✓. **No fabricated anchor; no A4 cite orphaned from source.**

**COVERAGE RESULT: PASS.** Zero orphan rows (ledger present, A4 absent). Zero rows found by my fresh pass that a ledger lacks. No loop-back to A2 or A3.

---

## AUDIT 2 — ARITHMETIC (every derived metric recomputed from raw extracted numbers; results ×0.1 from INR M, concall/PR/deck ×1)

Raw consolidated (INR M ÷10 → Cr) from results ledger §5: Rev 3607.21/1565.84/3060.69; OI 78.87; Mat 2043.19; ΔInv (78.16); Emp 465.20; FC 158.47; D&A 96.92; OthExp 326.44; PBT 674.02/148.13/595.42; Tax 171.75; PAT 502.27/108.13/442.83; EPS 16.33.

| # | Metric | A4 value | My recompute | Source line(s) | Status |
|---|---|---|---|---|---|
| 1 | Op EBITDA Q1FY27 (PBT+D+FC−OI) | 85.05 | 67.40+9.69+15.85−7.89 = **85.05** | L410/404/403/397 | PASS |
| 2 | Op EBITDA margin Q1FY27 | 23.6% | 85.05/360.72 = **23.58%** | derived | PASS |
| 3 | Op EBITDA Q1FY26 / margin | 28.39 / 18.1% | 14.81+8.37+5.82−0.61 = 28.39; /156.58 = **18.13%** | L410/404/403/397 | PASS |
| 4 | Op EBITDA Q4FY26 / margin | 61.80 / 20.2% | 59.54+9.04+9.62−16.40 = 61.80; /306.07 = **20.19%** (concall 20.11%) | L410/404/403/397 | PASS |
| 5 | Core PBT ex-OI Q1FY27 | 59.51 | 67.40−7.89 = **59.51** | L410/397 | PASS |
| 6 | Effective tax rate Q1FY27 | 25.5% | 17.18/67.40 = **25.49%** | L415/410 | PASS |
| 7 | PAT margin Q1FY27 | 13.9% | 50.23/360.72 = **13.92%** | L416/396 | PASS |
| 8 | Revenue YoY | +130.4% | 360.72/156.58−1 = **+130.37%** (CFO 130.4%) | L396 | PASS |
| 9 | Op EBITDA YoY | +199.6% | 85.05/28.39−1 = **+199.6%** | derived | PASS |
| 10 | Core PBT ex-OI YoY | +319.1% | 59.51/14.20−1 = **+319.1%** | derived | PASS |
| 11 | PBT YoY | +355.0% | 674.02/148.13−1 = **+355.0%** (raw M) | L410 | PASS |
| 12 | PAT YoY | +364.5% | 502.27/108.13−1 = **+364.50%** (raw M; Cr-rounded 50.23/10.81 = +364.7%, within rounding; CFO 364.5%) | L416 | PASS |
| 13 | Op margin YoY delta | +550 bps | 23.58−18.13 = **+545 bps** (rounds to +550) | derived | PASS |
| 14 | Finance costs YoY | +172.3% | 15.85/5.82−1 = **+172.3%** | L403 | PASS |
| 15 | D&A YoY | +15.8% | 9.69/8.37−1 = **+15.8%** | L404 | PASS |
| 16 | GP Q1FY27 / margin | 164.2 / 45.5% | 360.72−(204.32−7.82) = 164.22; /360.72 = **45.52%** | L396/400/401 (ties deck S11-6/9) | PASS |
| 17 | GP Q1FY26 / margin | 84.9 / 54.2% | 156.58−(92.77−21.09) = 84.90; /156.58 = **54.22%** | deck S11-4/7 | PASS |
| 18 | **(a) Gross-margin YoY like-for-like** | **−8.7 pp** | 45.52−54.22 = **−8.70 pp**. FY26 full-year GP margin = 417.80/876.21 = **47.68%** (= CFO's 47.65% comparator). A4 correctly states CFO's −2pp uses FY26 full-year, true Q1-vs-Q1 is −8.7pp (FF-01) | derived | **PASS — A4 CORRECT** |
| 19 | PAT bridge YoY total | +39.42 | 50.23−10.81 = **+39.42** | L416 | PASS |
| 20 | Bridge: volume effect | ≈+110.7 | 0.542×204.14 = **+110.6** | derived | PASS |
| 21 | Bridge: GP-margin effect | ≈−31.4 | 0.087×360.72 = **−31.4** | derived | PASS |
| 22 | S-vs-C PAT gap (std denominator, consistent) | Q1FY27 +0.53% / Q1FY26 +3.74% / Q4FY26 +0.14% / FY26 +1.35% | (50.50−50.23)/50.50=0.53%; (11.23−10.81)/11.23=3.74%; (44.34−44.28)/44.34=0.14%; (95.32−94.03)/95.32=1.35% | L345/416 | PASS (uniform std base) |
| 23 | **(b) Net debt Jun-26 MF-as-cash** | ≈45 | 423.6−379 = **44.6** | cc-L63 N27/N28 | PASS |
| 24 | **(b) Net debt Jun-26 ex-MF** | ≈404 | 423.6−~20 cash = **~404** | cc-L63 | PASS |
| 25 | **(b) Gross debt QoQ** | 369.3→423.6, +54.3 | 423.6−369.3 = **+54.3**; ex-MF worsening ~348→~404 ≈ **+56** | cc-L63 / S26 | **PASS — A4 CORRECT (leverage rose QoQ)** |
| 26 | **(c) Verbal CFO 247.69 vs 191.66** | UNVERIFIABLE, does NOT resolve INDETERMINATE | Ties to no filed statement; FY26 CFO = 196.9 (deck S28); comparator reconciles to nothing | cc-L63 N26 | **PASS — A4 CORRECT (INDETERMINATE held)** |
| 27 | **(d) Order book + today** | ~5,943 | 5,143.3+800 = **5,943.3** | S13-8 / cc-L61 N12 | PASS |
| 28 | **(e) Guidance target** | 876.2×1.8 = 1,577 | 876.21×1.8 = **1,577.18**; Q1 22.9% of target; Q2-Q4 avg (1577−360.7)/3 = **405.4**; Q1 annualised +64.7% | derived | PASS |
| 29 | Promoter series steps / distance | −0.82/−0.15/−1.09; avg 0.69; to-trigger 4.35; 6.3 / 4.0 qtrs | steps exact; avg 2.06/3 = 0.687; 29.35−25 = 4.35; 4.35/0.69 = 6.3; 4.35/1.09 = 4.0 | S31-8/12/16/20 | PASS |
| 30 | FY26 CFO/PAT; OpEBITDA/margin; FCF | 2.09x; 167.45/19.1%; −155.7 | 196.9/94.03 = 2.09x; 126.15+35.03+29.36−23.09 = 167.45, /876.21 = 19.11%; 196.9−352.6 = −155.7 | S28 / L-consol | PASS |
| 31 | Nuclear rev share | ~1% | 3.2/360.7 = **0.89%** | S9-1 | PASS |
| 32 | Segment sum check | 360.7 | 3.2+36.4+220.8+100.4 = **360.8** (Δ0.1 rounding) | S8/9/10 | PASS |

**Immaterial rounding items noted (NOT failures, all within ≤0.2pp / ≤0.1 Cr):** PAT YoY 364.5% (raw) vs 364.7% (Cr-rounded); op-margin delta +545bps rounds to +550; segment sum Δ0.1 Cr. The S-vs-C gap uses the standalone denominator uniformly across all four periods (a defensible, internally consistent convention), so 3.74%/0.53%/0.14%/1.35% are each arithmetically correct on their stated base.

**ARITHMETIC RESULT: PASS.** No mismatch above rounding on any derived metric. All five task-flagged reconciliations (a gross margin, b net debt, c verbal CFO, d order book, e all prior 3-doc metrics) confirm A4 states them correctly. No loop-back to A4.

---

## AUDIT 3 — ADVERSARIAL READ (three most-positive claims; strongest same-text bear counter; survives → must already be grafted)

**Positive claim 1 — "Guidance reaffirmed 80% revenue + 24% margin, and 'pretty confident to do better'" (cc-L61, O11/F2/F6/FF-07).**
Strongest bear (same text): Q1 revenue ₹360.7 Cr annualised flat = +64.7% on FY26 — ~15pp BELOW the 80% guide. Hitting ₹1,577 Cr needs Q2-Q4 to average ₹405.5 Cr/qtr (+12% on Q1), so "do better than 80%" is entirely back-half-loaded and unproven by Q1. The guide phrase "80% revenue load" is itself GARBLED (N13/FF-07); the "do better" is paired in the same turn with the H3 hedge "we'll see by end of next quarter" (Sumat, Q13); and the revenue is being bought with a mix that cut gross margin −8.7pp like-for-like (FF-01). **Counter SURVIVES on the text — and is ALREADY grafted** (Step 2 diag 1; Step 3 implied-base; guidance-table diagnostic; verdict caveat "back-half dependence unchanged"; Q7 for management). No incremental graft required.

**Positive claim 2 — "Order book ~2x / ~₹5,943 Cr (5,143 closing + 800 today)" (cc-L61, O10/FF-04; S13-8).**
Strongest bear (same text): the "+₹800 Cr today" is verbal, unfiled, post-quarter (unverifiable); the CFO's own restatement muddies the base ("3,200 already communicated... 5,100+800+", N39/FF-04; Bala echoed "3,200"), and the ₹5,143 Cr basis (gross/net GST, executed vs pending) is undefined (DEFINITION_WATCH, F-10). Near-term conversion is thin: today's order executes "next year" (Mohit Q1), and nuclear — a large slug of the book — converts to revenue only from H2 FY27 (Q1 nuclear revenue was ₹3.2 Cr / 1%). So "2x order book" overstates near-term earnings visibility. **Counter SURVIVES — and is ALREADY grafted** (Step 6D order-book trigger "FIRED with definition caveat"; FF-04 throughout; Q9 for management; verdict caveat). No incremental graft required.

**Positive claim 3 — "Civil-nuclear inflection: Kaiga ₹504 Cr highest-ever + Mahi Banswara 4-reactor optionality" (cc-L61, O3/O4; S7-11).**
Strongest bear (same text): nuclear REVENUE collapsed to ₹3.2 Cr / 1% in Q1 despite the ₹504 Cr order; execution only "commences H2 FY27" and runs 1–3 yrs (Kaiga) / within 2 yrs (refurb) — near-zero contribution this year. Mahi Banswara is pure optionality: tenders merely "floated," allotment a "one year process," MTAR only "qualified" and bidding "through EPC vendors," with the MD conceding "the timeline I cannot really say" (H4) and the TAM answered as "very big... can't say" (Q19/Q20, graded C). The reactor is described as "10 megawatt" (N51) — garbled/implausible for a PHWR program, undermining the specificity. So the nuclear leg is an order/optionality story with negligible near-term earnings and unquantified size. **Counter SURVIVES — and is ALREADY grafted** (Step 6A nuclear rev 1%; Step 6D "FIRED(order)/DELAYED(revenue)"; Q8/Q19/Q20; verdict caveat "nuclear conversion pinned to H2 FY27"). No incremental graft required.

**Cross-document consistency stress (FF-01 / FF-03 / FF-05 / silences):** Each candor flag that could undercut a positive claim is already carried and correctly directed in A4 — FF-01 (gross-margin comparator) tempers the margin/guidance positives; FF-03 (gross debt rose while "no debt" asserted) undercuts the "healthy balance sheet" framing behind the 80%/₹500 Cr-capex story (finance costs +172% YoY corroborate); FF-05 (WC guided UP to ~100 days, 59 is a trough) undercuts the cash-conversion positive; the promoter-stake silence (FF-14) and Bloom/US "unwanted noise" deflection (FF-11/FF-17) undercut the "everything on track" narrative. All appear in the verdict's caveat list and Questions-for-Management table.

**ADVERSARIAL RESULT: PASS.** All three bear counters survive on the extracted text, but each is already fully incorporated into A4 (caveats, trigger tables, and management questions). **surviving_bear_counters requiring graft: NONE.** No loop-back to A4.

---

## VERDICT

**COMPLETE.** Coverage PASS (zero orphan rows across all four ledgers; 53/53 concall mgmt numbers and the full F17 silence set traced into A4; no fresh-pass row missing from any ledger). Arithmetic PASS (every derived metric recomputed from raw extracts ties within rounding; the five task-flagged reconciliations — gross margin −8.7pp like-for-like, Jun-26 net debt ~45 MF-as-cash / ~404 ex-MF with gross debt up ₹54.3 Cr QoQ, verbal CFO 247.69 held UNVERIFIABLE/INDETERMINATE, order book ~5,943, and all prior 3-doc metrics — each confirm A4 states them correctly). Adversarial PASS (the three strongest bear counters survive but are already grafted into A4). No loop-back to A2, A3, or A4. This review proceeds to Notion save.

```yaml
stage: A5-adversary
company: "MTAR"
quarter: "Q1 FY27"
model: claude-opus-4-8
status: complete
verdict: COMPLETE               # COMPLETE | INCOMPLETE
coverage:
  orphan_rows: []               # ledger rows not cited in A4 — none
  missing_from_ledger: []       # rows my fresh pass found that a ledger lacks — none
arithmetic_mismatches: []       # no mismatch above rounding
surviving_bear_counters: []     # all 3 survive but already incorporated in A4; none require new graft
loop_back_to: ""                # COMPLETE — no loop-back
gap: ""                         # none
```
