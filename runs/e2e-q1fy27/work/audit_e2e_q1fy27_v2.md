# A5 ADVERSARY / COMPLETENESS AUDIT (v2) — E2E Networks Limited (E2E / E2ENETWORKS), Q1 FY27

**Agent:** A5 ADVERSARY | **Model:** claude-opus-4-8 | **Date:** 2026-07-22
**Under audit:** `review_e2e_q1fy27_v2.md` (A4 v2, three-document merge: results filing + press release + 22-slide deck)
**Independence note:** Every number below was re-derived from the A1 extracts (results Lakhs ×0.01; press-release & deck Mn ×0.1) and diffed against the A2 ledgers by a fresh grep/manual pass. I did not defer to A4's or A3's cites; I checked them. A3 forensic files are NOT in my input set, so A3 coverage is audited (a) by internal-consistency of A4's incorporation roster and (b) by re-deriving each cited forensic against the raw extracts.

**Run-scope confirmation (audited):** Three documents, NO concall transcript. Role 5 marked N/A by A4 is **legitimate and correctly handled** — A4 folded every deck/press forward statement into Role 4 + the Questions/monitorables lists (Role 5 section, lines 381-385), stated the one-line reason, and deferred Steps 1-9 of Role 5 to the next cycle. The audited results FILING is treated as the arithmetic authority throughout; deck-vs-filing conflicts resolve to the filing (verified in Section B7 below).

---

## A. COVERAGE AUDIT — fresh enumeration diffed against all three A2 ledgers

| Category | A2 ledger count | My fresh count | Orphan rows (in ledger, absent from A4) | Status |
|---|---|---|---|---|
| Results — notes | 18 (9C + 9S) | 18 (C: L125-142; S: L208-228) | none — all in Step 0D table C1-C9/S1-S9 | PASS |
| Results — line items | 60 (30+30) | 60 | none — Step 1 data table; S=C identical | PASS |
| Results — ZERO_STANDING | 4 (Exceptional C+S, Current tax C+S) | 4 | none — all noted (line 22, Step 1) | PASS |
| Results — auditor paras | 10 (4 S + 5 numbered C + 1 unnumbered) | 10 | none — unmodified opinion + Other Matters para 4 covered (L62) | PASS |
| Results — entities | 1 (Sovcloud) | 1 | none — Note 9 / A3-F6/F15 | PASS |
| Results — agenda / signatures | 1 agenda + 5 sig blocks | 1 + 5 | none material; single-agenda + signature-after-conclusion are "reviewed, no finding" | PASS |
| Press — slides / KPI metrics | 2 / 42 | 2 / 42 | none — all restatements reconcile to filing (Step 1) | PASS |
| Press — bullets / narrative / footnotes / entities | 12 / 12 / 3 / 2 | match | none — P-F6/7/8/10/14/15/16 all mapped | PASS |
| Deck — slides | 22 | 22 (`^\[page ` = 22) | none — Table A slide inventory | PASS |
| Deck — table line items | 42 (s17/19/20/21) | 42 (4+13+11+14) | **4 slide-21 BS rows dropped from A4's DISPLAY table** (see note N3) — not orphan findings (all unflagged, sheet balances) | PASS (with note) |
| Deck — chart data points | 51 | 51 (5:3, 11:3, 16:10+10, 17:6, 18:19) | none — Step 1-Deck (b)(e)(f) + Step 3 | PASS |
| Deck — footnotes/sources/disclaimers | 16 | 16 | none — CWIP footnote D.16, Safe Harbour D.1, sources → FND-03 | PASS |
| Deck — ZERO_STANDING | 1 (zero named customers) | 1 (+ "Balance funds 0.00" second zero) | none — FND-01; second zero noted line 22 | PASS |
| Deck — entities | 46 (15 persons + 31 orgs) | 46 | none material — Ambastha/Ohrie/Adfactors/board cited; market-data orgs → FND-03 | PASS |
| Deck — forward-looking | 12 | 12 | none — Role 5 section + FND-02 | PASS |

**Every FLAGGED ledger row is reflected in A4.** Cross-checked each A2 flag: Results ZERO_STANDING×4, ENTITY_CHANGE, SINGLE_AGENDA_ITEM, OCR-illegible FY26 tax; Press NUMERIC_INCONSISTENCY (1450 vs 1446), NOT_FOUND (FY26 EBITDA base), UNAUDITED_FIGURES, UNATTRIBUTED_QUOTE, FORWARD_LOOKING; Deck NUMERIC_INCONSISTENCY×4 (→FND-07), ZERO_STANDING customers (→FND-01), DISCLOSED_IN_DECK ×several (→FND-09). **No orphan flagged row. No row my fresh pass found that the ledgers lack.**

**A3 forward/ambiguous coverage (audited via A4 roster + re-derivation):** All A3 IDs A4 lists (Results F1/F6/F8/F9/F10/F14/F15; Press P-F6/7/8/10/14/15/16; Deck FND-01…FND-10) map to ≥1 Questions-for-Management row with an honestly assigned status. I re-derived the substantive claim behind each FORWARD/AMBIGUOUS finding against the extracts and every one holds (nil current tax across all 4 periods L99/183; deferred tax flip L101/185; EPS spread 2.14/2.10 L120-121; OCI −505.01 gross > FY26 +125.47 L107; zero named customers confirmed by full deck read; SovCloud "funding arrangements" L431-435). See note N2 for a roster-completeness discrepancy.

**Status assignment honesty check (ANSWERED / PARTIAL / STILL-OPEN):** Spot-audited every Step-8.5 row. Correct and conservative:
- Q1 Exit MRR → **PARTIALLY ANSWERED** (level Rs71.8 Cr disclosed; recurring split still open) — correct, not over-claimed.
- Q2 utilisation %, Q3 pricing, Q6 OCI, Q7 dilutive instrument, Q10 OI source, Q11 margin durability → **STILL OPEN** — correct; none silently resolved.
- Q5 net debt → **PARTIALLY ANSWERED** (Mar-26 components only; labelled figure + 30-Jun-26 period-end STILL OPEN) — correct and the critical test (see B3).
- Q8/Q9/Q12/Q13 → **PARTIALLY ANSWERED** with the residual explicitly retained — correct.

---

## B. ARITHMETIC AUDIT — independent recomputation from raw extracts

Deck-derived claims the task named, plus the headline filing numbers, each recomputed from source.

| # | Metric (A4 value) | My recomputation from raw line | Source | Status |
|---|---|---|---|---|
| B1 | Exit MRR Rs71.8 Cr | 718 Mn × 0.1 = **71.8 Cr** | deck 16.4 / 18.17 (L456/554) | MATCH |
| B1 | +92% QoQ vs Rs37.4 Cr | (71.8−37.4)/37.4 = 34.4/37.4 = **+92.0%**; 374 Mn×0.1=37.4 | deck 16.4 | MATCH |
| B1 | Annualised 861.6 / 3.5× FY26 / 1.37× qtr-avg / +37% vs Q1-annualised | 71.8×12=861.6; 861.6/245.6=3.51×; 71.8/(156.76/3)=1.374×; 861.6/627.0=1.374 | derived | MATCH |
| B2 | Mar-26 net cash ~Rs239 Cr | Borrowings 1,032Mn=103.2 + Lease 559Mn=55.9 = 159.1 gross; Cur.fin.assets 3,982Mn=398.2; 398.2−159.1 = **239.1 Cr** | deck 21.3/21.4/21.12 (L625/626/637) | MATCH |
| B3 | PPE Mar-25 947.1 → Mar-26 1,496.6 (+549.5) | 9,471Mn×0.1=947.1; 14,966Mn×0.1=1,496.6; Δ=**+549.5 Cr** | deck 21.8 (L633) | MATCH (attribution note N1) |
| B4 | GPUs-deployed CWIP Rs533.4 Cr | 5,334 Mn × 0.1 = **533.4 Cr** | deck D.16 footnote (L506) | MATCH |
| B5 | Q1 capex Rs17.7 Cr vs FY26 Rs696.2 Cr | 177Mn×0.1=17.7; 6,962Mn×0.1=696.2; Δ=−97% | deck 17.6/17.5 (L504) | MATCH |
| B6 | Dry powder Rs132.68 Cr | Total balance 1,326.79 Mn × 0.1 = **132.679 → 132.68 Cr** | deck 17.10 (L520) | MATCH |
| B7 | Revenue 156.76 Cr | 15,675.99 Lakhs × 0.01 = **156.7599 → 156.76** | filing L79/164 | MATCH |
| B7 | Op EBITDA 117.90 / margin 75.21% | PBT 5,862.64 + Dep 6,064.44 + FinCost 1,005.15 − OI 1,142.01 = 11,790.22 Lakhs = **117.90 Cr**; /15,675.99 = **75.212%** | filing L79-93 | MATCH |
| B7 | PAT 43.88 Cr | 4,388.21 Lakhs × 0.01 = **43.88** | filing L104/188 | MATCH |
| B7 | EPS spread 0.04 (~1.9%) | Basic 2.14 − Diluted 2.10 = 0.04; 0.04/2.10 = **1.90%** | filing L120-121 | MATCH |
| B8 | Revenue YoY +334.1% / QoQ +63.9% | (15,675.99−3,611.02)/3,611.02=**+334.12%**; /9,564.27→(6,111.72/9,564.27)=**+63.90%** | filing | MATCH (deck 334.3/64.0 correctly rejected) |
| B9 | Op EBITDA margin QoQ +1,446 bps | 75.212% − (5,810.22/9,564.27=60.749%) = 14.463 pp = **+1,446 bps** | filing | MATCH (deck 1,450 correctly rejected) |
| B10 | Op EBITDA margin YoY | Precise: 75.212% − (1,051.44/3,611.02 = 29.118%) = 46.094 pp = **+4,609.4 bps** | filing | **INTERNAL INCONSISTENCY in A4** — see N4 |
| B11 | PAT bridge +46.72 Cr | Gross contrib +107.37 − Dep 33.21 − FinCost 8.22 − OI 3.58 − Tax 15.65 = +46.71 (0.01 rounding vs PAT Δ 43.88+2.84=46.72) | filing | MATCH |
| B12 | ETR 25.14% / PAT margin 27.99% / EBIT 57.26 / Dep-to-OpEBITDA 51.4% | 14.74/58.63=25.14%; 43.88/156.76=27.99%; 117.90−60.64=57.26; 60.64/117.90=51.4% | filing | MATCH |
| B13 | FinCost +449% YoY / +173% QoQ; Dep +121% YoY | 8.22/1.83=+449.2%; 6.37/3.68=+173.1%; 33.21/27.43=+121.1% | filing | MATCH |
| B14 | Net worth Rs1,685.05 Cr | 2,055.65 + 166,449.53 = 168,505.18 Lakhs = **1,685.05 Cr** (deck 20.6+1,664.5=1,685.1 ties) | filing L116-117 | MATCH |
| B15 | Q1 EBITDA = 93% of FY26 EBITDA | 117.90/126.26 = **93.4%** (FY26 Op EBITDA recomputed −2,119.95+16,922.69+1,224.13−3,400.64 = 12,626.23 = 126.26) | deck s20 + filing | MATCH |

**Arithmetic verdict: every named figure reconciles to source within rounding.** The single discrepancy is internal to A4 and rounding-level (N4).

---

## C. ADVERSARIAL READ — three most positive claims, strongest bear from the same extract

**Positive claim 1 — Checklist #1 Exit MRR RE-RATED to GREEN (Rs71.8 Cr, +92% QoQ).**
Strongest bear from the same text: the MRR series is step-shaped and lumpy (Sep-25 *dips* 165→160 Mn; then 280→374→718), Exit MRR of 71.8 is 1.37× the quarterly average (52.25) and reflects a *mid-quarter* B200 go-live (CWIP "deployed May 2026"), and there are **ZERO named customers across all 22 slides** and **no contract duration** anywhere (deck Table E; G.7). A spot exit rate from one cluster with no contracted-recurring evidence is not durable recurring revenue.
**Survives?** Yes — **but already fully grafted.** A4 re-rated as "**GREEN (level) — durability caveat**," explicitly NOT unconditional GREEN (line 309, 243); routed durability to checklist #3 AMBER/at-risk, #5 UNKNOWN, Q1/Q12, and monitorable #1/#2. **The re-rate is defensible**: checklist item #1 is literally the *Exit MRR level* (green band Rs35-40 Cr), and Rs71.8 Cr is a factual level beat; the durability that "zero named customers / no contract duration" attacks is carried as separate, still-open items, not resolved. No new counter to add.

**Positive claim 2 — "Margin proof FIRED": 75.21% operating margin (growth trigger, line 341).**
Strongest bear from the same text: Q1 carries only **~2 months of B200 depreciation** — the Rs533.4 Cr CWIP "deployed in May 2026" (deck footnote L506), so Q2 (Jul-Sep) absorbs a full quarter; 75.2% is a first-quarter peak of unproven durability, and finance costs are surging (+449% YoY / +173% QoQ) on a rising-borrowings base (Rs11.4→103.2 Cr).
**Survives?** Yes — **already grafted.** A4 raised the Q2 full-quarter-B200-depreciation headwind at FND-09, Step 2 pt 5, Q11, monitorable #5, and set Step-8C secondary metric "margin ≥70% after full quarter of B200 depreciation." **The caveat is arithmetically correct**: deployment May-2026 means Q1 FY27 (Apr-Jun) captures ~May+Jun ≈ 2 months, Q2 captures 3. Verified against the footnote. No new counter to add.

**Positive claim 3 — "Headline growth is REAL, not treasury-driven; operating-leverage inflection is real" (lines 127, 205).**
Strongest bear from the same text: (a) the entire +334% is credited to a **single B200 cluster go-live** (concentration / single point of failure); (b) PAT is **cash-flattered ~Rs14.74 Cr** by a 100%-deferred, nil-current-tax charge (filing L99/101); (c) the "recovers 92% of FY25 peak in one quarter" framing leans on a *depressed* FY26 loss base (−15.6 Cr) created by the depreciation jump 60.1→169.3 Cr, and FY26/FY25 depreciation from the Rs870 Cr FY25 capex is still ramping into the P&L; (d) Other Income Rs11.42 Cr (~19% of PBT) source undisclosed.
**Survives?** Yes — **already grafted.** Cash-flattered PAT (Step 4, A3-F1/F8, FND-04); single-cluster durability (FND-01, Step 2.1); FY26 "capex-absorption trough not demand failure" is stated *with* the Q2 headwind attached (FND-09); OI source open (Q10). No new surviving counter that A4 omitted.

**Adversarial conclusion:** All three top positives carry their strongest bear counter already. This is the expected result for a v2 that ingested the forensics; my job was to confirm none survives *unincorporated*, and none does. No bear counter needs to be grafted back to A4.

---

## D. TASK-SPECIFIC CHALLENGE QUESTIONS (answered)

1. **Is the #1 re-rate to GREEN defensible given zero named customers / no contract duration?** Yes — it is a **GREEN-on-level, durability-caveated** re-rate, not unconditional; durability is held open at #3/#5/Q12. Defensible (Section C1).
2. **Is the Q2 full-quarter-B200-depreciation caveat correct?** Yes — verified against the "deployed in May 2026" footnote; Q1 = ~2 months, Q2 = 3 months (Section C2).
3. **Did A4 keep still-absent items open rather than silently resolving them?** Yes, all four: utilisation % (Q2/#6 UNKNOWN), realised pricing (Q3/#8 UNKNOWN), **labelled net-debt figure** (Q5 — A4 computed a Mar-26 net-cash *from components* but explicitly kept the *labelled* figure and the *30-Jun-26 period-end* OPEN, flagging the post-Mar-26 finance-cost surge, lines 164/282), and named anchor customer (#3 AMBER/at-risk, Q12). **None silently resolved.** The net-debt handling is the sharpest test and A4 passes it cleanly — it did not present the Rs239 Cr Mar-26 read as the resolved current-period net-debt.
4. **Is the unchanged PROCEED WITH FLAGS verdict defensible / should any flag escalate?** Defensible. INDETERMINATE cash conversion caps the review at PROCEED WITH CAVEATS and forbids a silent PROCEED (CLAUDE.md); PROCEED WITH FLAGS honors the cap (more caveated than CAVEATS, not a silent PROCEED) and names the missing evidence (CFO, Q1 BS, labelled net-debt, WC days — Step 5). No thesis-broken trigger fired (Exit MRR 71.8 ≫ 25 floor; no CWIP writedown; Blackwell live; revenue +334% > 40%), no mechanical failure (all A2/A3 gates pass, unmodified audit opinion) — so no REWORK. Zero-named-customer hardened to AMBER/RED-watch but does not cross a fired trigger this quarter. **No flag needs to escalate.**

---

## E. OBSERVATIONS FOR A4 (non-blocking; do not change verdict, coverage, or any anchored figure)

- **N1 (attribution, recommend tighten):** A4 attributes the Mar-25→Mar-26 PPE jump (+Rs549.5 Cr) to the Rs533.4 Cr B200 **CWIP conversion** (checklist #2, Step 5 L278). But the deck footnote states that CWIP was **"deployed in May 2026"** — *after* the Mar-26 balance-sheet date — so it was still CWIP (not PPE) at Mar-26 and cannot be what drove the Mar-26 PPE increase; the true CWIP→in-service conversion is a Q1 FY27 event not yet on the Mar-26 sheet. A4 already hedges #2 as "GREEN (partial; annual, no Q1 BS)" and independently confirms the May-2026 deployment, so the verdict and #2's GREEN (B200 real, no writedown) are unaffected — but the causal wording should be corrected so it does not imply the annual sheet already shows the conversion.
- **N2 (roster completeness):** A4's body cites **A3-F2** (S-vs-C gap, line 421) and **A3-F11** (net-worth tie-out, line 92), but its "A3 findings incorporated (all IDs)" roster (lines 26-29) and the YAML `a3_findings_incorporated` list omit both. The substance of each checks out against the extracts (S=C gap = 0.00 pp; net worth 1,685.05 Cr ties), so this is a roster-listing omission, not a missed finding. Reconcile the roster to include F2/F11 (or confirm the IDs).
- **N3 (display completeness):** A4's Step 1-Deck (d) balance-sheet table displays 10 of the 14 slide-21 line items, dropping Other Non-Current liabilities (197/245/93), Intangible Assets (167/149/122), Non-Current Financial Assets & tax assets (1,506/66/63), and Other current assets (2,104/1,784/232). None carries a flag and the sheet balances (assets = liabilities = 23,282 Mn Mar-26), so no finding is hidden; but the "100% reviewed" claim is stronger than the display. Optional: add the four rows or footnote the elision.
- **N4 (rounding-level internal inconsistency):** A4 states the Op EBITDA margin YoY expansion as **"+4,608 bps"** in Step 2 (table line 192 and diagnostic line 204) but as **"+4,609 bps"** in the Numeric-Conflict Log (line 430), FND-07 (line 416), and the flags block (line 563). Precise recomputation = **+4,609.4 bps**, so 4,609 is correct and the Step-2 "4,608" is the outlier (an artifact of subtracting pre-rounded margins 75.21−29.13). 1-bp, rounding-level — not an arithmetic FAIL — but harmonize Step 2 to 4,609 for internal consistency.

None of N1-N4 is an orphan ledger row, a missing enumeration, a material arithmetic mismatch, or an unincorporated surviving bear counter. They are cleanup items.

---

## VERDICT

**COMPLETE.** Coverage: every A2 ledger row across all three ledgers is reflected in A4 (cited or reviewed-no-finding), no orphan and nothing my fresh pass found is missing from the ledgers; every A3 forward/ambiguous ID A4 lists maps to a Questions-for-Management row with an honestly assigned ANSWERED/PARTIAL/STILL-OPEN status. Arithmetic: all named deck-derived and headline filing figures reconcile to source within rounding; the filing correctly wins every deck conflict. Adversarial: the three most-positive claims each carry their strongest bear counter already grafted; no counter survives unincorporated. Cash conversion INDETERMINATE is honored (verdict not a silent PROCEED); no thesis-broken trigger fired; no mechanical failure. The four observations (N1-N4) are non-blocking cleanup items, not gaps requiring loop-back. This review may proceed to Notion save.

```yaml
stage: A5-adversary
company: "E2E"
quarter: "q1fy27"
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
notes:
  - "N1 non-blocking: A4 attributes Mar-25->Mar-26 PPE jump (+Rs549.5 Cr) to Rs533.4 Cr B200 CWIP conversion, but deck footnote states that CWIP 'deployed in May 2026' (after Mar-26 date) so it was still CWIP at year-end; verdict and checklist #2 GREEN(partial) unaffected; tighten causal wording."
  - "N2 non-blocking: A4 body cites A3-F2 and A3-F11 but omits both from its 'all IDs' incorporation roster and YAML; substance verified against extracts; reconcile roster."
  - "N3 non-blocking: Step 1-Deck (d) displays 10 of 14 slide-21 balance-sheet rows; dropped rows unflagged and sheet balances (23,282 Mn both sides); optional to restore."
  - "N4 rounding-level: Op EBITDA margin YoY shown as +4,608 bps in Step 2 vs +4,609 bps in conflict-log/FND-07/flags; precise = +4,609.4 bps; harmonize Step 2 to 4,609."
```
