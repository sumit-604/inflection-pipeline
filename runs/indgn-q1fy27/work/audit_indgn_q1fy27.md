# A5 ADVERSARY / COMPLETENESS AUDIT — INDGN Q1 FY27

Audit target: `work/review_indgn_q1fy27.md` (A4 analyst merged review)
Independent evidence re-derived from: `extract_results_`, `extract_concall_`, `extract_presentation_` (A1) and the three A2 ledgers.
Method: fresh grep enumeration + full manual recompute in Rs crore (÷10 from Rs million). A4/A3 cites checked, not trusted.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate, run first)

Plain-Language Brief (Section D) — all four labelled parts present and carrying real content:

| Part | Heading | Present | Non-empty / real content |
|---|---|---|---|
| 1 | D1 SUMMARY NARRATIVE (review L627-628) | YES | ~20-line narrative, number-anchored, symmetric | 
| 2 | D2 SECTOR INTELLIGENCE (L630-631) | YES | Demand cycle, regulation (MFN/US policy), end-market mix, two-sided read |
| 3 | D3 BUSINESS-MODEL INTELLIGENCE (L633-634) | YES | Revenue engine, unit economics, model drift, segment margins |
| 4 | D4 COMPETITION INTELLIGENCE (L636-637) | YES | Moat claims, concentration, GenAI-deflation bear/bull framing |

GATE 0: PASS. No placeholder or empty part.

---

## AUDIT 1 — COVERAGE (fresh enumeration diffed against A2)

Independent grep pass (my own):
- `\[TURN [0-9]+:` on concall extract → **53** (ledger 53) MATCH; turns run 1..53 no gap.
- `\[page [0-9]+\]` on presentation extract → **22** (ledger 22) MATCH; slides 1..22.
- Annexure I Sr rows 1-29 manual read → **29 entities** (ledger 29) MATCH.
- Notes manual read: 7 consolidated (L276-418) + 6 standalone (L555-611) = **13** (ledger 13) MATCH.
- Agenda items (board letter L34/L39) → **2** (ledger 2) MATCH.
- Auditor paras: consolidated 6 (L96-139) + standalone 4 (L453-480) = **10** (ledger 10) MATCH.
- Q&A questions (turns 7,10,13,17,19,22,26,29,34,36,39,41,44,46,48) → **15** (ledger 15) MATCH.

| Category | A2 count | My fresh count | Orphan rows (in ledger, absent from A4) | Status |
|---|---|---|---|---|
| Results — notes | 13 | 13 | none (all in Step 0D table + Standalone 1-6 row) | PASS |
| Results — line items | 78 | 78 | none material (full consol+standalone P&L, segment note, IPO table cited; OCI sub-rows covered by preamble "ALL reviewed") | PASS |
| Results — agenda items | 2 | 2 | none (item 1 results; item 2 ESOP → A3-07/Q13) | PASS |
| Results — auditor paras | 10 | 10 | none (unmodified opinion + reliance para 6 cited) | PASS |
| Results — entities | 29 | 29 | none (list + 11 unreviewed + 3 TCPA co-defendants absent → Q12) | PASS |
| Concall — turns | 53 | 53 | none (participants + full Q&A decomposition) | PASS |
| Concall — questions | 15 | 15 | none (all in Step 4A) | PASS |
| Concall — mgmt numbers | 67 | 67 (sweep) | none material | PASS |
| Presentation — slides | 22 | 22 | none (KPI/margin/mix/factsheet cited; qualitative slides in Section D) | PASS |

A3 findings incorporation — A4 preamble + YAML carry all 37: Results A3-01..13 (13), Concall A3-F17-01/F6-01..04/F7-01..03/F16-01..02/F17-02..06 (15), Presentation FND-01..09 (9). A3-11 and FND-04 (NEUTRAL-FACT) explicitly subsumed under Q1/Q21. **No orphan finding; nothing my fresh pass found is missing from the ledger.**

COVERAGE: PASS. No return to A2 (nothing under-enumerated), no return to A3 (no unreviewed row).

---

## AUDIT 2 — ARITHMETIC (independent recompute, Rs crore)

Raw source = results extract (Rs million ÷10). Every headline figure recomputed from scratch.

| Metric | A4 value | My recompute | Source line | Status |
|---|---|---|---|---|
| Revenue YoY (consol) | +39.7% | 1063.1/760.8−1 = +39.73% | L216 | OK |
| Revenue QoQ (consol) | +5.9% | 1063.1/1003.4−1 = +5.95% | L216 | OK |
| Operating EBITDA Q1FY27 (Rev−Emp−OthExp) | 174.2 | 1063.1−659.1−229.8 = 174.2 | L216/221/224 | OK |
| Operating EBITDA margin Q1FY27 | 16.39% | 174.2/1063.1 = 16.39% | derived | OK |
| Operating EBITDA margin Q4FY26 | 16.31% | 163.6/1003.4 = 16.31% | derived | OK |
| Operating EBITDA margin YoY | −402 bps | 16.39−20.41 = −4.02pp | derived | OK |
| Deck EBITDA reconciliation | 1795 = op 1742 + oth inc 52, ex-interest 237 | 1742+52 = 1794 ≈ 1795; 1527+64+441−237 = 1795 | deck L399/401, filing | OK (subtle, ties) |
| Ex-MTM QoQ read | ~−190 bps | 16.9% vs (16.4%+2.4%=18.8%) = −190 bps | concall L386-388 | OK |
| Reported EBITDA margin Q1FY27 | 19.11% | 203.2/1063.1 = 19.11% | derived | OK |
| Core operating PBT YoY (PBT−OI) | −4.8% | 123.7/130.0−1 = −4.85% | L231/217 | OK |
| Reported PAT YoY | −0.2% | 116.2/116.4−1 = −0.17% | L238 | OK |
| PAT bridge (vol +61.7 / margin −42.7 / D&A −22.5 / fin −2.7 / OI +6.9 / tax −0.8) | nets −0.2 | 18.9−22.5−2.7+6.9−0.8 = −0.2 (PBT Δ 152.7−152.1=+0.6) | Step 4 | OK |
| D&A YoY | +104.2% | 44.1/21.6−1 = +104.2% | L223 | OK |
| ETR Q1FY27 (consol) | 23.9% | 36.5/152.7 = 23.90% | L236/231 | OK |
| ETR FY26 | 23.6% | 123.9/525.0 = 23.60% | L236/231 | OK |
| Standalone rev QoQ | −7.5% | 340.7/368.2−1 = −7.47% | L508 | OK |
| Standalone PAT QoQ | 72.1→59.9 (−16.9%) | 59.9/72.1−1 = −16.9% | L525 | OK |
| Standalone op EBITDA margin QoQ | 28.0%→17.67% | 103.1/368.2=28.00%; 60.2/340.7=17.67% | L508/513/516 | OK |
| Standalone ETR Q1FY27 | 25.1% | 20.1/80.0 = 25.1% | L523/519 | OK |
| S/C subsidiary share of PAT | 61.3 / 9.5 / 48.5 / 47.2% | 71.3/116.4; 7.6/79.7; 56.3/116.2; 189.2/401.1 | L238/525 | OK |
| Subsidiary swing Q4→Q1 | +48.7cr ≈ 81% of stdln PAT | 56.3−7.6=48.7; 48.7/59.9=81.3% | derived | OK |
| DSO (net) | 71→67, −4 YoY/+4 QoQ (vs 63) | deck 67/63/71 | deck L740 | OK |
| Cash & investments | 1728.0→1460.2, −15.5% YoY/−5.1% QoQ | 14602/17280−1=−15.5%; /15385−1=−5.1% | deck L742 | OK |
| TCPA provision / cap / residual | 20.3cr / 41.7cr / up to 21.4cr | 203mn=20.3; 417mn=41.7; 41.7−20.3=21.4 (417/4.72=88.3 Rs/USD; 203/88.3=2.30mn) | L411/406/229 | OK |
| ECS segment margin | 21.1%(YoY)→16.0%; 16.9%(QoQ)→16.0% | 1099/5211=21.1; 1197/7502=16.0; 1212/7193=16.9 | L344-350 | OK |
| EMS segment margin | ~26% | 716/2736 = 26.2% | L344/349 | OK |
| Others segment loss | −5.0→−11.5cr | −50mn / −115mn | L351 | OK |
| Deferred-tax shield | FY26 −52.4cr credit → Q1 +7.2cr charge | L235 raw (524)/72 | L235 | OK |
| TAM sum vs headline | $157B vs $135B+ | 55+24+21+36+21 = 157 | deck L491-511/495 | OK (real discrepancy, flagged as Q21) |

ARITHMETIC: PASS. Every derived metric reconciles within rounding. **No mismatch above rounding. No return to A4 on arithmetic.**

Note on the one internal-labeling nuance (not an error): A4 calls the +6.9cr YoY other-income swing "treasury/interest timing," but the deck split (L398/401) shows interest income was flat (238→237) and the +6.9cr swing sits entirely in the non-interest "Other income/(loss)" bucket (−1.7→+5.2cr). Magnitude and the conclusion (non-recurring other income propped flat PAT) are correct; label is imprecise, not wrong. Not a FAIL.

---

## AUDIT 3 — ADVERSARIAL READ (three most positive claims; strongest bear from same text)

**Positive claim 1 — "PAT +45.9% sequentially to Rs 116.2cr; both EBITDA and PAT margins expanding sequentially" (deck s8/s13; concall T4).**
Bear from same text: the Q4 FY26 base is thrice-distorted — Rs 20.3cr TCPA exceptional (L229), the ~240 bps MTM drag (concall L386), and it is itself a *balancing figure* (Note 2, L283-285). Strip those and the QoQ jump is base mechanics, not profitability improvement; on the ex-MTM operating basis margin *declined* ~190 bps.
Survives? YES — but **already grafted** into A4 (Step 7A "CONFIRMED but Q4 base one-off-depressed"; C3; tripwire 1 FIRED-underlying). No new incorporation needed.

**Positive claim 2 — margin guidance HARDENED to 19-20% by Q4 FY27, "conviction has increased" (concall T4/T14/T18).**
Bear from same text: requires ~250-310 bps in 3 quarters off a base whose underlying just fell, *through* a wage-hike Q2; management removed its own buffer (6-8→6) the same quarter the measurable number weakened; two growth-quality disclosures withdrawn (T23, T40).
Survives? YES — but **already grafted** (Step 6D WEAKENED; Step 2 guidance-arithmetic tension; 6E OVERPROMISER-WATCH; flags block). No new incorporation.

**Positive claim 3 — revenue +39.7% YoY, "significant growth at scale" (deck s4).**
Bear from same text: bundles M&A (Cake/Trilogy/MJL/BioPharm/Warn/Addressable, Annexure I L183-196) + FX; organic cc only a verbal 2.6-2.7% (T27); parent revenue *fell* −7.5% QoQ (L508); core operating PBT fell −4.8% YoY (L231/217); all sequential growth is subsidiary/offshore.
Survives? YES — but **already grafted** (Step 2 diagnostic 1; Standalone read; C1; flags). No new incorporation.

Management-favourable framings scanned for un-challenged residue:
- RPE "$77.1K, highest in industry" — A4 D3 flags it includes third-party-payroll contractors (deck footnote 2). Challenged.
- "Strong cash" — A4 flags −15.5% YoY. Challenged.
- "Receivable risk not significant" — A4 flags UNVERIFIABLE (no OCF). Challenged.
- Deck "Resilient Margins" headline — A4 FND-06/Q23. Challenged.

**No surviving bear counter is absent from A4. Nothing to graft back. No return to A4.**

Judgment checks (adversarial soundness of A4's calls):
- Tripwire scorecard 1 FIRED / 2 BLINDED / 4 NOT FIRED — totals 7, defensible. Tripwire 1 FIRED-on-underlying is the conservative, correct read (mgmt-conceded ex-MTM decline) while explicitly noting 1-of-2 for the formal two-quarter condition. BLINDED calls (organic split T23; OCF at Q1 per Reg 33) are correct. Defensible.
- PROCEED WITH FLAGS — defensible: standard operating business, unmodified audit, no mechanical failure; multiple live flags; FLAGS sits *below* the PROCEED-WITH-CAVEATS ceiling that the INDETERMINATE cash rule imposes, so the CLAUDE.md cap is honoured, not violated.
- INDETERMINATE cash — correct: no cash-flow statement / balance sheet at Q1 (Reg 33 half-yearly); OCF/PAT not estimated; missing evidence named. Consistent with the NEVER rule.
- Every FORWARD-SIGNAL / AMBIGUOUS A3 finding produces ≥1 management question (Step 8.5, 22 questions; YAML maps all 37 finding IDs). No FS/AMB finding left question-less.

ADVERSARIAL: PASS.

---

## VERDICT

**COMPLETE.** All four brief parts present; fresh enumeration matches every A2 count with zero orphan rows and nothing missing from the ledgers; all 37 A3 findings incorporated; every headline metric recomputes within rounding with no mismatch; all three most-positive claims already carry their surviving bear counters inside A4; tripwire scorecard, PROCEED WITH FLAGS, and INDETERMINATE cash are each defensible. No return to A2, A3, or A4. Cleared to Notion save.

```yaml
stage: A5-adversary
company: "INDGN"
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
surviving_bear_counters: []
loop_back_to: ""
gap: ""
```
