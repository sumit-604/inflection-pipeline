# A5 ADVERSARY / COMPLETENESS AUDIT — RateGain Travel Technologies (RATEGAIN), Q1 FY27

Fresh context. Re-derived independently from A1 extracts (results / presentation / press-release / loan-prepay) and A2 ledgers (results / presentation). A4's cites were checked, not trusted. Units: results filing printed Rs million, x0.1 to Rs Cr; deck/PR native Rs Cr; loan intimation USD.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate, run first)

Plain-Language Brief = Section F of the review. All four labelled parts present and carrying real, non-placeholder content:

| Part | Heading | Present | Content check |
|---|---|---|---|
| 1 | F1. SUMMARY NARRATIVE (review L381-382) | present | ~20-sentence dense paragraph; covers inorganic growth, PAT-margin decline, parent 4.4% of PAT, 64% goodwill/intangibles, deleveraging, INDETERMINATE cash, verdict PROCEED WITH FLAGS / WATCHLIST |
| 2 | F2. SECTOR INTELLIGENCE (L384-385) | present | Travel-tech SaaS, three units, demand read, TAM 1.1/1.9/5.8 Bn (Phocuswright/1Lattice), tailwind/headwind, gaps named |
| 3 | F3. BUSINESS-MODEL INTELLIGENCE (L387-388) | present | Subscription 79.1%, retention/LTV:CAC, gross-margin erosion, acquisition-stacked economics, adjusted-vs-reported |
| 4 | F4. COMPETITION INTELLIGENCE (L390-391) | present | Breadth/incumbency, named partnerships, organic-Distribution weakness, concentration 17.6%, no peer benchmarks |

GATE 0: PASS — all four parts present and non-empty.

---

## AUDIT 1 — COVERAGE (fresh grep/sweep vs A2 ledger; A2 ledger vs A4)

### 1a. Fresh enumeration vs A2 ledger

| Category | A2 count | My fresh count | Missing-from-ledger | Status |
|---|---|---|---|---|
| Standalone notes (res) | 10 | 10 (L234,240,250,256,267,271,280,289,302,311; Note 5 "s"-OCR at L267) | none | MATCH |
| Consolidated notes (res) | 12 | 12 (L561,567,577,582,588,625,629,636,640,651,658,660) | none | MATCH |
| Standalone P&L line items | 24 | 24 (L189-224) | none | MATCH |
| Consolidated P&L line items | 33 | 33 (L493-551) | none | MATCH |
| PPA table rows | 7 | 7 (L598-609) | none | MATCH |
| Annexure A entities | 18 | 18 (L432-468) | none | MATCH |
| Auditor paras standalone | 5 | 5 (L94-151) | none | MATCH |
| Auditor paras consolidated | 6 | 6 (L342-403) | none | MATCH |
| Board agenda items | 2 | 2 (L31 results, L40 guarantee) | none | MATCH |
| Annexure B rows | 4 | 4 (L683-703) | none | MATCH |
| Signature/date blocks | 5 | 5 | none | MATCH |
| ZERO_STANDING (res) | 7 | 7 | none | MATCH |
| Deck slides | 30 | 30 ([page 1]-[page 30]) | none | MATCH |
| Deck P&L+BS line items | 58 | 58 (20 P&L + 38 BS) | none | MATCH |
| Deck footnotes | 6 | 6 (L270,322,679,734,769,871) | none | MATCH |
| Deck forward/commitment | 7 | 7 (Table F) | none | MATCH |
| ZERO_STANDING (deck) | 5 | 5 | none | MATCH |

No row found by my fresh pass that the A2 ledgers lack. A2 enumeration is complete; no loop-back to A2.

### 1b. A2 ledger rows vs A4 coverage (orphan check)

Every material ledger row is cited or resolved in A4: all 22 notes (acquisition, segment, ESOP, Labour Code, EPS, HK-liquidation), all 18 entities incl. the 4 ENTITY_CHANGEs and Nrejos SARL (Section C2), both agenda items + Annexure B (guarantee, Sections C2/E), both auditor Other-Matter carve-outs plus the missing Sojern component-auditor point (Q11), all 7 ZERO_STANDING flags (Steps 1A/1B), the full consol/standalone P&L, PPA, balance sheet, segment growth, retention/LTV:CAC, FCF, shareholding baseline. Low-materiality slide rows (slide 29 shareholding detail beyond promoter 48.78%; slide 11 pipeline 664 Cr / new-wins 141 Cr) are covered by the review's blanket "all reviewed" as reviewed-no-finding; acceptable, no red flag suppressed. No orphan row. No loop-back to A3.

COVERAGE: PASS.

---

## AUDIT 2 — ARITHMETIC (recomputed from raw extracted numbers)

Spot-verified the full standalone and consolidated tables tie to source (x0.1 conversion). Representative confirmations (all PASS unless flagged):

| Metric | A4 value | My recompute | Source | Status |
|---|---|---|---|---|
| Standalone PAT Q1FY27 | 4.21 Cr | 42.09 mn x0.1 = 4.21 | res L209 | PASS |
| Standalone PAT YoY | -76.7% | 4.21/18.06-1 = -76.7% | res L209 | PASS |
| Standalone Op EBITDA Q1FY27 | 5.01 | 5.68+1.27+0.23-2.16 = 5.01 | res L200/196/195/190 | PASS |
| Standalone Op EBITDA margin Q1FY27 | 7.4% | 5.01/68.19 = 7.35% | derived | PASS |
| Consol revenue Q1FY27 | 785.0 | 7,850.12 mn x0.1 = 785.01 | res L493 / deck L740 | PASS |
| Consol revenue YoY | +187.6% | 785.0/272.9-1 = 187.6% | res L493 | PASS |
| Consol Op EBITDA Q1FY27 | 171.5 | 785.0-294.8-318.7 = 171.5 | deck L748 | PASS |
| Consol Op EBITDA margin Q1FY27 | 21.9% | 171.5/785.0 = 21.85% | deck L749 | PASS |
| Adj EBITDA Q1FY27 | 193.4 | 171.5+21.9 = 193.4 | deck L751 | PASS |
| Adj EBITDA margin Q1FY27 | 24.6% | 193.4/785.0 = 24.64% | deck L752 | PASS |
| Consol PAT Q1FY27 | 94.9 | 949.10 mn x0.1 = 94.91 | res L515 | PASS |
| Consol PAT YoY | +102.2% | 94.9/46.9-1 = 102.2% | res L515 | PASS |
| Reported PAT margin Q1FY27 vs Q1FY26 | 12.1% vs 17.2% | 94.9/785=12.1%; 46.9/272.9=17.2% | deck L765 | PASS |
| Consol ETR Q1FY27 | 21.3% | 256.45/1,205.55 = 21.27% | res L513/508 | PASS |
| Consol ETR Q1FY26 | 23.5% | 143.95/613.27 = 23.47% | res L513/508 | PASS |
| PAT bridge sum | +48.0 | +121.8-1.8-27.0-16.2-17.6-11.3 = +48.0 | Step 4 | PASS |
| S/C PAT gap Q1FY27 | 90.70; 95.6%; 2,154.7% | 94.91-4.21=90.70; /94.91=95.6%; /4.21=2154 | res L209/L515 | PASS |
| Standalone % of consol Q1FY27 | 4.4% | 4.21/94.91 = 4.44% | derived | PASS |
| Adj-vs-reported EBITDA growth gap | +43.9 pp | 289.3-245.4 = 43.9 | Section C1 | PASS |
| Goodwill+intangibles / assets | 64% | (1,591.5+756.3)/3,659.1 = 64.2% | deck L778/779/785 | PASS |
| Net debt Jun-26 | 615.4 | 871.0-255.6 = 615.4 | deck L336 | PASS |
| Borrowings Jun-26 | 871.0 | 533.5+337.5 = 871.0 | BS L784/796 | PASS |
| Loan outstanding | USD 77.50M of 125M | 9.75+6.25 prepaid Aug-05; = 77.50M | loan L40-44 | PASS |
| Loan % repaid | 38% | (125-77.5)/125 = 38.0% | pr L100-102 | PASS |
| Further prepayment | USD 16.0M | 9.75+6.25 = 16.0 | loan L40-41 / pr L101 | PASS |
| Deferred consideration run-rate | ~80-90 Cr/yr | 21.9 x4 = 87.6 | deck L750 | PASS |
| Acquisition amort run-rate | ~135 Cr/yr | 33.8 x4 = 135.2 | deck L756 | PASS |
| PPA DTL | Rs 130.8 Cr | 1,307.89 mn x0.1 = 130.79 | res L607 | PASS |
| **Sojern PPA goodwill (Step 2 diag 5, L133)** | **Rs 130.2 Cr** | **13,020.01 mn x0.1 = Rs 1,302.0 Cr** | res L609 | **FAIL (10x understated)** |
| **Sojern PPA intangibles (Step 2 diag 5, L133)** | **Rs 65.9 Cr** | **(3,827.18+887.37+1,875.88) mn x0.1 = Rs 659.0 Cr** | res L602-604 | **FAIL (10x understated)** |
| **NRR FY25 characterization (C1-5/F3/Q6/8C/flags)** | **"below 100 in FY25 (100.5)"; "two sub-100 years"; "net contraction"** | **100.5 is ABOVE 100; only FY26 (99.6) is below 100** | deck slide 10 (ledger Table B) | **FAIL (categorical error, repeated 5x)** |

### Arithmetic FAILs — detail (all loop back to A4)

**FAIL-1 (conversion, 10x): Sojern PPA goodwill.** Step 2 diagnostic 5 (review L133) states "Sojern PPA intangibles Rs 130.2 Cr goodwill." Raw PPA goodwill = Rs 13,020.01 mn (res L609) = **Rs 1,302.0 Cr**, not 130.2 Cr. The review applied x0.01 instead of x0.1. Note the review itself carries the CORRECT figure in Section C2 (goodwill Rs 13,020.01 mn; BS goodwill Rs 1,591.5 Cr), so this is an internal inconsistency, not a data problem — but the stated Cr number is wrong by an order of magnitude.

**FAIL-2 (conversion, 10x): Sojern PPA intangibles.** Same sentence states "Rs 65.9 Cr intangibles." Raw recognised intangibles = customer relationships 3,827.18 + trademarks 887.37 + software 1,875.88 = 6,590.43 mn (res L602-604) = **Rs 659.0 Cr**, not 65.9 Cr. Same x0.01 slip.

**FAIL-3 (categorical / interpretive overreach): NRR "below 100 in FY25."** The NRR series (deck slide 10, ledger Table B) is FY24 120.9 / FY25 100.5 / FY26 99.6 / Q1FY27 106.8. The review asserts in five places — C1 finding 5 (L305), F3 (L388), Question 6 (L341/review Section D), Step 8C (L237), and flag (review L456) — that NRR was "below 100 in FY25 (100.5)," describing "two sub-100 years" and "net contraction from existing clients." **100.5 is above 100** (marginal net expansion). Only FY26 (99.6) is genuinely below 100. The multi-year downtrend (120.9 -> 100.5 -> 99.6) is real and survives, but the "two consecutive sub-100 / two years of net contraction" framing overstates the evidence, and Management Question 6 as written ("NRR was below 100 in FY25 (100.5)") is self-contradictory and would be rejected on its face. The review also relied on the ledger's CHART_LABEL_AMBIGUOUS NRR pairing without noting that caveat while making a strong bear claim.

ARITHMETIC: FAIL (3 items, all A4).

---

## AUDIT 3 — ADVERSARIAL READ (three most positive claims + strongest bear from same text)

**Positive claim 1 — "Revenue nearly triples +187.6%; highest-ever EBITDA; record Adj EBITDA margin 24.6%."**
Bear from same extract: growth is ~100% inorganic (Sojern consolidated from 6 Nov 2025; management's own non-comparability disclaimer, res L616-618); organic Distribution only +3.1% (deck slide 12); reported PAT margin FELL 17.2% -> 12.1% (deck L765); the record margin is adjusted, stripping a real dated cash cost (deferred consideration to Q3FY29).
Survives as NEW? NO — already grafted: Step 2 diagnostics 1-3, Section C1, Section B3 AMBER rows, flags, Questions 1/2/3.

**Positive claim 2 — "Deleveraging is real and ahead of schedule (loan down to USD 77.5M of 125M); lowers future finance costs."**
Bear from same extract: the Board approved a NEW USD 65M corporate guarantee the same day (res L42-44) for RateGain UK + Sojern; the existing guarantee only reduces "to the extent" of prepayment (loan L44-45); consolidated net debt is still Rs 615.4 Cr and finance cost Rs 16.5 Cr/qtr persists; the fresh guarantee envelope offsets the deleveraging narrative.
Survives as NEW? NO — already grafted: Section C2 leverage picture, flag (L453), Question 7, monitorable.

**Positive claim 3 — "NRR rebounded to 106.8; platform breadth (33 of top 40 chains); FCF conversion 78.8%."**
Bear from same extract: NRR multi-year downtrend 120.9 -> 100.5 -> 99.6 with LTV:CAC halved 21.3x -> 10.7x (deck slide 10); breadth coexists with high concentration (top 1-10 = 17.6%, deck slide 10) and near-flat organic Distribution (+3.1%); the 78.8% FCF conversion is non-GAAP and unbridged with NO cash-flow statement this quarter (INDETERMINATE).
Survives as NEW? NO — already grafted: Section C1 finding 5, Step 5, flags, Questions 5/6. (NB: the bear side here is where the FAIL-3 overstatement lives — the counter is present but mis-stated, which is why FAIL-3 loops to A4 rather than being a missing counter.)

ADVERSARIAL READ: no un-incorporated surviving bear counter. The review is symmetric and already carries the bear case for each headline positive. No graft required.

---

## VERDICT

**INCOMPLETE.** Coverage is complete (A2 clean, no orphan rows) and the adversarial read finds no missing bear counter, but the ARITHMETIC audit fails on three A4-owned errors: two 10x rupee-conversion mistakes in Step 2 diagnostic 5 (Sojern PPA goodwill stated Rs 130.2 Cr vs correct Rs 1,302.0 Cr; PPA intangibles stated Rs 65.9 Cr vs correct Rs 659.0 Cr), and a repeated categorical error mischaracterising FY25 NRR of 100.5 as "below 100 / net contraction / two sub-100 years" (only FY26 at 99.6 is below 100), which also propagates into the reader-facing brief (F3) and outbound Management Question 6. Loop back to A4 to correct all three before Notion save. No fault found with A2 (enumeration complete) or A3 (all forensic findings mapped to questions per A4's coverage check).

---

```yaml
stage: A5-adversary
company: "RATEGAIN"
quarter: "Q1 FY27"
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
  - {metric: "Sojern PPA goodwill (Step 2 diag 5, review L133)", a4_value: "Rs 130.2 Cr", recomputed: "Rs 1,302.0 Cr", source_line: "res L609 (13,020.01 mn x0.1)"}
  - {metric: "Sojern PPA intangibles (Step 2 diag 5, review L133)", a4_value: "Rs 65.9 Cr", recomputed: "Rs 659.0 Cr", source_line: "res L602-604 (3,827.18+887.37+1,875.88=6,590.43 mn x0.1)"}
  - {metric: "NRR FY25 characterization (review L305/L388/L237/L456 + Q6)", a4_value: "below 100 in FY25 (100.5); two sub-100 years; net contraction", recomputed: "100.5 is ABOVE 100; only FY26 (99.6) is below 100 — one year of net contraction, not two", source_line: "deck slide 10 (ledger presentation Table B, NRR 120.9/100.5/99.6/106.8)"}
surviving_bear_counters: []
loop_back_to: "A4"
gap: "Three A4 arithmetic/accuracy errors to fix before save: (1) Step 2 diagnostic 5 states Sojern PPA goodwill Rs 130.2 Cr — correct is Rs 1,302.0 Cr (10x conversion slip; res L609); (2) same line states PPA intangibles Rs 65.9 Cr — correct is Rs 659.0 Cr (10x slip; res L602-604); (3) NRR of 100.5 in FY25 is repeatedly called 'below 100 / net contraction / two sub-100 years' (C1-5, F3, Step 8C, flags, Management Q6) — 100.5 is above 100, only FY26 (99.6) is below 100, so recast as a single sub-100 year within a declining multi-year trend and repair Question 6."
```
