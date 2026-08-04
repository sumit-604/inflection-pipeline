# A5 ADVERSARY / COMPLETENESS AUDIT — MAPMYINDIA (C.E. Info Systems Ltd) Q1 FY27 (v2, concall-merged)

Agent: A5 ADVERSARY | Model: claude-opus-4-8 | Independence: absolute (re-derived from A1 extracts + A2 ledgers; A4/A3 cites re-checked, not trusted)
Review under audit: `review_mapmyindia_q1fy27_v2.md` (867 lines)
Unit rule applied: results filing Lakhs x0.01 = Rs Cr; deck/PR/concall in Rs Cr; concall "80 lakhs" = Rs0.80 Cr.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate, run first)

PLAIN-LANGUAGE BRIEF — four labelled parts, checked for presence + real content:

| Part | Heading present | Non-empty / real content | Provenance-labelled |
|---|---|---|---|
| 1. Summary narrative | YES (L784 "Part 1 — SUMMARY NARRATIVE") | YES — ~22-line narrative, write-off geometry, cash INDETERMINATE, decision | YES ("Provenance: … prior Notion work") |
| 2. SECTOR intelligence | YES (L788) | YES — AEG demand read, government-receivable sector pattern, AI/sovereignty | YES |
| 3. BUSINESS-MODEL intelligence | YES (L792) | YES — Map-led vs IoT economics, hardware-first/SaaS-later, treasury, SC drag | YES |
| 4. COMPETITION intelligence | YES (L796) | YES — moat, OEM wins, IoT commoditisation, Zenrin/PhonePe holders | YES |

**Gate 0: PASS.** All four parts present, substantive, provenance-labelled (each closes with a "Provenance:" line separating this-quarter filing/concall from prior Notion work). Not placeholders.

---

## AUDIT 1 — COVERAGE (fresh independent enumeration vs A2 ledger)

I re-swept the concall extract (source lines 1-187) by hand, classifying every content line by speaker turn.

**Fresh turn count** (opening 4 + Q1 11 + Q2 7 + Q3 13 + Q4 21 + Q5 13 + Q6 7 + Q7 7 + closing 3):
4+11+7+13+21+13+7+7+3 = **86**.

**Fresh question count** (analyst turns 42; non-question closings/acks 9; questions 42−9): Q1=5, Q2=3, Q3=4, Q4=10, Q5=6, Q6=3, Q7=2 = **33**.

**Fresh mgmt-number count**: walked every management turn atomically; reconciles to the ledger's **46** (spot-verified #1-9 opening block, #18-21 write-off, #32-34 order book, #36 receivables, #37-41 geometry).

| Category | A2 ledger count | My fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Turns | 86 | 86 | none | MATCH |
| Questions | 33 (42−9) | 33 | none | MATCH |
| Mgmt numbers | 46 | 46 | none | MATCH |
| Participants | 13 | 13 | none | MATCH |
| Forward/hedge phrases | 11 | 11 (spot-checked) | none | MATCH |
| Results notes (0D) | 12 (6 consol + 6 standalone mirror) | 12 | none | MATCH |
| Results P&L line items | 77 | reconciled at row level in Step 1 | none | MATCH |

**Ledger-row → review disposition:** the review preamble (L26-37) asserts every ledger row reviewed; individual turns are cited T3-T82 throughout, and the blanket "all 86 turns / 33 questions / 46 numbers reviewed" satisfies the "reviewed, no finding" standard for the non-material remainder. No orphan row (in ledger, absent from A4). No row in my fresh pass that the ledger lacks.

**F17 silence findings → mapped?** Step 5B lists 7 silences; each maps to a management question and/or monitorable:
- FY28 Rs1,000 Cr target → Q4 + monitorable ✓
- Treasury/capital-allocation plan → Q4 + monitorable ✓
- Gtropy overdraft/ageing → Q6 + AGM monitorable ✓
- ClarityX/Zenithra RPT ceiling → Q9 ✓
- Government YoY growth number → Q1/Q5 ✓
- A&M/C&E→AEG bridge → Q7 + monitorable ✓
- Mappls DT WTD departure → Q12 + monitorable ✓
All 7 mapped. **PASS.**

**Forward-signal / ambiguous A3 findings → question or monitorable?** Independently re-deriving the material forward signals from the transcript (write-off recurrence, government-receivable cycle, 35%+ guide/H2 dilution, order-book conversion, FY28 silence, treasury silence, IoT SaaS uplift, auto H2 time-shift, digital-twin receivable gating, JMD ratification, WTD succession) — every one lands in the Updated Questions table (Q1-Q12) and/or the Monitorables list. **PASS.**

**Minor coverage note (non-blocking):** finding IDs **A3-11** and **A3-15** appear only in the incorporation roster (L35) and closing YAML (L816); they are not individually surfaced with content anywhere in the review body (unlike A3-01…A3-10, A3-12…A3-14, A3-16…A3-22, all of which carry a cited finding). Against my mandate this is not a coverage FAIL — the A2 ledger universe (turns/questions/numbers/participants/hedges) is fully covered, and every material forward-signal I independently derive is mapped; A3 finding-ID bookkeeping is A4-internal. Flagged for A4 tidy-up only: either surface A3-11/A3-15 with their substance or drop them from the "incorporated" roster so the claim of full incorporation is literally true.

---

## AUDIT 2 — ARITHMETIC (recomputed from raw Lakhs; independent of A4)

Raw consol (Lakhs→Cr): Rev Q1FY27 139.72 / Q1FY26 121.61; OI 19.65 / 13.67; FC 0.18 / 0.82; D&A 9.15 / 6.88; PBT 66.44 / 61.84; OthExp 23.12 / 17.44; Tax 16.06 / 14.46; PAT-incl 49.74 / 45.81.

| Metric | A4 value | My recompute | Source | Status |
|---|---|---|---|---|
| Op EBITDA Q1FY27 (PBT+D+FC−OI) | 56.12 | 66.44+9.15+0.18−19.65 = **56.12** | lines 236/235/227/239 | MATCH |
| Op EBITDA Q1FY26 | 55.87 | **55.87** | same | MATCH |
| Op EBITDA margin Q1FY27 | 40.2% | 56.12/139.72 = **40.17%** | derived | MATCH |
| Op EBITDA margin Q1FY26 | 45.9% | 55.87/121.61 = **45.93%** | derived | MATCH |
| Margin YoY compression | −574 bps | 45.93−40.17 = **−577 bps** | derived | MATCH (rounding; ~577 precise vs 574; also 45.9−40.2=570; immaterial) |
| Op EBITDA YoY | +0.4% | 56.12/55.87 = **+0.45%** | derived | MATCH |
| Core PBT ex-OI Q1FY27 | 46.79 | 66.44−19.65 = **46.79** | derived | MATCH |
| Core PBT ex-OI YoY | −2.9% | 46.79/48.17 = **−2.86%** | derived | MATCH |
| Other income YoY | +43.7% | 19.65/13.67 = **+43.7%** | derived | MATCH |
| Effective tax rate Q1FY27 | 24.2% | 16.06/66.44 = **24.17%** | derived | MATCH |
| PAT margin on revenue | 35.6% | 49.74/139.72 = **35.6%** | derived | MATCH |
| PAT margin on total income (deck 31.2%) | 31.2% | 49.74/159.37 = **31.21%** | derived | MATCH |
| D&A YoY | +33.0% | 9.15/6.88 = **+33.0%** | derived | MATCH |
| Reported EBITDA Q1FY27 (PBT+D+FC) | 75.77 | **75.77** | derived | MATCH |
| **STANDALONE** Op EBITDA Q1FY27 | 60.30 | 73.07+5.44+0.17−18.38 = **60.30** | lines 444/441/440/432 | MATCH |
| STANDALONE core PBT ex-OI YoY | +6.2% | 54.69/51.50 = **+6.19%** | derived | MATCH |
| STANDALONE margin YoY | −614 bps | 54.57−48.44 = **−613 bps** | derived | MATCH (rounding) |
| SC gap Q1FY27 (% of standalone PAT) | −10.2% | (49.74−55.42)/55.42 = **−10.25%** | lines 251/450 | MATCH |
| SC gap QoQ swing | 19.5 pp | +9.29% → −10.25% = **19.5 pp** | derived | MATCH |
| TTM EPS | 25.17 | 24.56−8.48+9.09 = **25.17** | lines 274/275 | MATCH |
| Trailing PE | ~47.1x | 1185/25.17 = **47.08x** | derived | MATCH |

### PAT bridge (4A) recompute
Op EBITDA +0.25; D&A −2.27; FC +0.64 → core op PBT change **−1.38** ✓; OI +5.98 → PBT change **+4.60** ✓ (66.44−61.84); tax −1.60; NPAT-before-assoc **+3.00** ✓; assoc/JV [(−0.64)−(−1.57)] **+0.93** ✓; total incl assoc/JV change **+3.93** ✓ (49.74−45.81 = 3.00+0.93). Reconciles.

### UNDERLYING (ex-one-time) walk — the load-bearing v2 correction, checked against the write-off geometry
Geometry as stated by mgmt: Rs4.0Cr write-off in **Other Expenses (inside EBITDA)** + Rs3.2Cr payable-write-back in **Other Income (below EBITDA)** = **Rs0.80Cr net** (T12/L34, T37/L87, T39/L91, T41/L95). Verbatim confirmed in transcript.

| Underlying metric | A4 value | My recompute | Status |
|---|---|---|---|
| Op EBITDA (add back 4.0 to opex) | 60.12 | 56.12+4.0 = **60.12** | MATCH (~60.1Cr as briefed) |
| Underlying op EBITDA margin | ~43.0% | 60.12/139.72 = **43.03%** ("43 plus") | MATCH |
| Underlying op EBITDA YoY | +7.6% | 60.12/55.87 = **+7.61%** | MATCH |
| Underlying other income (remove 3.2 write-back) | 16.45 | 19.65−3.2 = **16.45** | MATCH (~16.45Cr as briefed) |
| Underlying other income YoY | +20.3% | 16.45/13.67 = **+20.34%** | MATCH (~+20%) |
| Underlying core op PBT (add back 4.0) | 50.79 | 46.79+4.0 = **50.79** | MATCH (~50.8Cr as briefed) |
| Underlying core op PBT YoY | +5.4% | 50.79/48.17 = **+5.44%** (flips reported −2.9%) | MATCH |
| Underlying PBT (add back 0.80 net) | 67.24 | 66.44+0.80 = **67.24**; cross-check 50.79+16.45 = **67.24** | MATCH, internally consistent |
| One-time bps of compression | ~287 bps | 4.0/139.72 = **286 bps**; genuine mix 577−287 = ~290 | MATCH |

**Over-correction test (critical):** The recompute is NOT over-corrected. The Rs4.0Cr sits wholly in operating expenses, so adding it back to both Op EBITDA and core-op-PBT is correct; the Rs3.2Cr write-back sits in Other Income (below EBITDA), so it is removed only from OI, never double-counted into the operating add-back. Core-op-PBT = PBT − OI already excludes the 3.2, so only the 4.0 is restored to it. Net PBT restoration is exactly 4.0 − 3.2 = 0.80. Geometry is arithmetically clean and matches every value in the task brief (60.1 / 43% / 50.8 / +5.4% / 16.45 / +20%). **PASS.**

### Single flagged discrepancy — IMMATERIAL, non-propagating
- **NCI Q1FY27:** A4 shows non-controlling interest = **(0.01)** Cr in Step 1A and **+0.29** as the NCI change memo line in the 4A bridge. Raw filing: owners 4,977 (line 260) − total 4,974 (line 262) → NCI = **(0.03)** Cr; the OCR artifact "(J)" on line 261 = (3), not (1). Correct NCI change = (0.03)−(0.30) = **+0.27**, not +0.29.
- **Materiality: nil.** NCI is a memo/reconciling line; it does not enter the +3.93 PAT-incl-assoc bridge total (3.00 + 0.93), affects no margin, ratio, YoY/QoQ %, the underlying walk, the SC-gap, or the verdict. A 0.02 Cr display slip on a 49.74 Cr PAT. **Does not gate the save.** Recommend A4 correct NCI to (0.03) / bridge memo to +0.27 at save. Not a loop-back.

**Audit 2 verdict: PASS.** Every decision-relevant derived metric reconciles to the raw numbers. The v2 underlying-vs-reported correction is correct and not over-corrected.

---

## AUDIT 3 — ADVERSARIAL READ (strongest bear for the 3 most positive claims, from the same extract)

**Positive claim 1 — "The business itself grew; underlying op EBITDA +7.6% and core op PBT +5.4%; reported softness was mostly a one-off."**
Bear (same text): the +5.4% underlying is a *single* quarter, rests entirely on management's uncorroborated write-off geometry, and the **CFO who owns that reconciliation never spoke** (ledger SILENT_PARTICIPANT; both promoters answered). Worse, a Rs4Cr government *receivable* with a "back to back" near-matching Rs3.2Cr *payable* (T37/L87) is an unusual pairing that could indicate a pass-through/circular arrangement — a revenue-*quality* question, not just a collection one. Add-back legitimacy depends on the 3.2 write-back being genuinely non-recurring, which it is, but the pairing invites the deeper question of whether the original revenue had economic substance.
**Survives?** YES, but **already grafted:** the review retains the reported number as the conservative valuation anchor, calls the write-off a "realized collection failure," flags CFO silence (Step 0B / 6D), and Question 2 explicitly asks whether the Rs3.2Cr payable was to the same/related counterparty with "Related/circular exposure" as the bear answer. The revenue-substance angle is substantively inside Q2. No new graft required.

**Positive claim 2 — "Order book Rs1,750 Cr (up from 1,500/1,350) is a genuine visibility positive."**
Bear (same text): the number is **concall-only and UNVERIFIABLE** (review 7A confirms it is in no filed document); the segment mix is withheld "for competitive reasons" (T27/L66); intake value and conversion timeline are refused; it is disclosed once a year. A rising *aggregate* with withheld mix can mask concentration or slow conversion — and it was volunteered in the same call where the **FY28 Rs1,000 Cr target the order book should underwrite went silent** (A3-16).
**Survives?** YES, but **already grafted:** 7A marks it UNVERIFIABLE, Step 6D pairs "order book up" against "target silent," Pillar-3 treats it as only "a small positive," and Q8 demands the mix/intake. Treated as "confirmatory, not thesis-changing at ~47x." No new graft required.

**Positive claim 3 — "Map-led core marginally positive (+0.5%), recovery ON TRACK."**
Bear (same text): +0.5% (Rs98.2→98.7 Cr, T17/L45) is statistically flat and *fell* QoQ off the Q4 peak; the analyst on the line called it **"very very flat"** (T20/L51); 100% of the consolidated growth is low-margin IoT hardware. Labelling a stalled core "ON TRACK," even "marginal," risks over-reading noise as a trend.
**Survives?** YES, but **already grafted:** the review self-downgrades to "WEAKENED → marginal ON TRACK," writes "materially stalled," and quotes the "very very flat" pushback verbatim (6B item 5, 6D). No new graft required.

**Adversarial verdict:** all three most-positive claims attract surviving bear counters, and in every case A4 has **already incorporated** the counter with the conservative anchor retained. No un-incorporated surviving bear counter. **No over-bull drift:** the review consistently frames the write-off as a realized collection failure and the Gtropy→government reframe as "mild adverse," not benign — exactly the adverse posture required. INDETERMINATE cash is NOT silently resolved: despite the improved operating read, Step 5 keeps CFO/PAT ND, cash INDETERMINATE, and caps the verdict at PROCEED WITH CAVEATS, with the transcript's "Q1 we've not given the balance sheet" (T33/L78) cited as the binding confirmation and the Q1 receivables number correctly left un-inferred per the NEVER-estimate rule.

---

## VERDICT

**COMPLETE.**

- Gate 0 (plain-language brief, 4 parts): PASS.
- Coverage: fresh counts 86 turns / 33 questions / 46 numbers reconcile exactly to the A2 concall ledger; results notes and P&L rows reconcile; no orphan rows; all F17 silences and all material forward-signals map to a management question or monitorable. PASS. (One non-blocking A4 tidy-up: A3-11/A3-15 listed as incorporated but not surfaced.)
- Arithmetic: every decision-relevant derived metric reconciles to raw Lakhs; the UNDERLYING-vs-REPORTED ex-one-time walk is correct and NOT over-corrected (60.1Cr/43% / core 50.8Cr/+5.4% / OI 16.45Cr/+20% / net 0.80Cr all tie). One immaterial, non-propagating NCI memo-cell slip (−0.01 should be −0.03; bridge +0.29 should be +0.27) that does not affect any total, ratio, or verdict — recommend correction at save, does not gate.
- INDETERMINATE cash preserved; no silent resolution; verdict correctly capped at PROCEED WITH CAVEATS.
- Adversarial: three positive claims each attract a surviving bear counter, all already grafted; no over-bull drift; write-off and government reframe kept adverse.

Only COMPLETE proceeds to Notion save. This review may proceed.

```yaml
stage: A5-adversary
company: "MAPMYINDIA"
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
arithmetic_mismatches:
  - {metric: "NCI Q1FY27 / PAT-bridge NCI memo line", a4_value: "(0.01) Cr / +0.29 change", recomputed: "(0.03) Cr / +0.27 change", source_line: "results lines 260-262; review Step 1A + 4A", materiality: "IMMATERIAL — non-propagating memo cell; does not affect the +3.93 bridge total, any margin/ratio, the underlying walk, or the verdict; OCR artifact '(J)'=(3) read as (1); recommend correction at save, does not gate COMPLETE"}
surviving_bear_counters: []   # all 3 already grafted into A4 with the conservative anchor retained
loop_back_to: ""
gap: ""
```
