# A5 ADVERSARY / COMPLETENESS AUDIT — Gem Aromatics Limited (GEMAROMA) — Q1FY27

Auditor: A5 ADVERSARY | Model: claude-opus-4-8 | Date: 2026-08-13
Under audit: review_gemaroma_q1fy27.md (A4 analyst). Re-derived independently from A1 extracts and A2 ledgers; A4/A3 cites checked, not trusted.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate, run first)

PLAIN-LANGUAGE BRIEF present at review L439-455. All four labelled parts present and carry real content:

| Part | Location | Present | Non-empty / real content |
|---|---|---|---|
| (1) Summary narrative | L441-443 | present | Yes — ~18-line narrative, numbers-anchored, states verdict + maiden recommendation |
| (2) SECTOR intelligence | L445-447 | present | Yes — specialty ingredients/aroma chemicals, Madagascar clove floods, Frost & Sullivan provenance caveated |
| (3) BUSINESS-MODEL intelligence | L449-451 | present | Yes — feedstock-to-derivatives model, FY26 revenue mix, named customers, undisclosed-metrics list |
| (4) COMPETITION intelligence | L453-455 | present | Yes — scale/integration edge, small-cap execution risk, thin-institutional note |

GATE 0 = PASS. All four parts present and substantive; no placeholders.

---

## AUDIT 1 — COVERAGE (independent fresh grep vs A2 ledger, then ledger-row → A4)

Fresh structural greps (my pass):
- Results `^\[page N\]` = 8 (matches A1 header page_count 8, A2 results ledger)
- Presentation `^\[page N\]` = 33 (matches A2 presentation ledger 33 slides)
- Press release `\[page` = 5 (matches A2 pressrelease ledger 5 pages)
- Results entities `Gem Aromatics LLC|Krystal Ingredients` = 4 line hits / 2 unique (L313/314 auditor list, L432/433 Note 3) — matches ledger 2 entities / 4 mentions

| Category | A2 count | My fresh count | Orphan rows (in ledger, absent from A4) | Status |
|---|---|---|---|---|
| Results — pages | 8 | 8 | none | PASS |
| Results — numbered notes + footnotes | 17 | 17 (15 numbered incl. mislabeled Consol N1/N2 + Con N5 behind stray quote L437; 2 EPS footnotes L219/L417) | none — all in A4 Step 0D table + FIND-02/FIND-05 | PASS |
| Results — line items (std 29 + con 30) | 59 | 59 (raw table rows L167-218 / L369-416; ZERO_STANDING prior-yr-tax L194 excluded from data; wrapped "(loss)" L404 excluded) | none — every P&L row feeds A4 Step 1A/1B | PASS |
| Results — zero_standing | 1 | 1 (std prior-year tax L194) | none — noted in ledger, immaterial, blanket-reviewed | PASS |
| Results — agenda items | 1 | 1 (board approval of results L43-54) | none — A4 Step 0D N1 | PASS |
| Results — auditor paras | 11 | 11 (std 5 + con 6) | none — EoM paras carried (FIND-02); opinion type in Step 0 | PASS |
| Results — entities | 2 | 2 | none — A4 Step 0D Con N3, Step 4C | PASS |
| Results — signature blocks | 5 | 5 | none — blank std partner name in FIND-05/drafting note | PASS |
| Presentation — slides | 33 | 33 | none | PASS |
| Presentation — financial tables / line items | 5 / 88 | 5 / 88 | none — P&L feeds Step 1/2/3; BS+CF feed Step 5 | PASS |
| Presentation — slide KPIs | 95 | accepted (two-sweep method; spot-checks tie: CMP 174.90 L1056, MktCap 914.15 L1060, shareholding L1075) | none material | PASS |
| Presentation — guidance (11) / strategic (17) / capex-capacity (14, incl 2 DATA_ABSENT) / charts (3) / footnotes (12+1) / OCR (7) | as ledger | accepted; DATA_ABSENT capacity+order-book surfaced by A4 (biz-model brief); 15%-tax "till perpetuity" carried (Q4); Frost&Sullivan provenance caveated | none | PASS |
| Press release — pages 5 / fin items 18 / narrative 21 / mgmt quotes 5 / forward 13 / regulatory 8 / earnings-call 12 (82 units) | as ledger | 5 pages confirmed; MTPA 16,171 (N10) + named customers (N17-21) in A4 biz-model brief; Brazil WOS R6 carried (Q9/flags); call details → Section B | none | PASS |

Orphan-row check: A4 LEDGER-RECONCILIATION PREAMBLE (L9-23) states "All reviewed" and "No ledger row is unreviewed," and enumerates all A3 findings incorporated (FIND-01..05, A3-01..08, F2-1/F6-1/F7-1/F10-1/F13-1/F14-1/F14-2/F15-1/F16-1). Minor ledger internal-consistency notes (Consol Q1FY26 EBITDA margin 16.9% p7 vs 17.0% p10; Rest-of-World footnote Uganda/Switzerland off-map; Diamond Pass Link missing URL) are sub-materiality rounding/admin items covered by the blanket "reviewed, no finding." **No orphan rows. No rows my fresh pass found that the ledger lacks. COVERAGE = PASS.**

---

## AUDIT 2 — ARITHMETIC (recomputed from raw Millions x0.1; A4 value vs my recompute vs source)

Raw→Cr conversion of every P&L line (results extract L168-416, x0.1) reproduces A4 Step 1A/1B exactly. Derived metrics re-run:

| Metric | A4 value | My recompute | Source line(s) | Status |
|---|---|---|---|---|
| Std Op EBITDA Q1FY27 (PBT+D+Fin−OI) | 8.51 | 9.731+1.606+1.334−4.157 = 8.51 | L187/182/180/170 | MATCH |
| Std Op EBITDA margin Q1FY27 | 10.3% | 8.51/82.99 = 10.25% | L168 | MATCH |
| Std Op EBITDA Q1FY26 / margin | 10.51 / 13.8% | 10.514 / 13.76% | L187/182/180/170/168 | MATCH |
| Std ETR (all periods) | 25.3/25.8/25.5/25.5% | 2.206/8.729=25.3; 4.115/15.983=25.8; 2.479/9.731=25.5; 9.14/35.85=25.5 | L196/187 | MATCH |
| Std core PBT ex-OI Q1FY27 | 5.57 | 9.731−4.157 = 5.57 | L187/170 | MATCH |
| Con Op EBITDA Q1FY27 (dep reconciled 9.13) | 3.31 | −8.543+9.127+2.883−0.161 = 3.31 | L385/380*/379/371 | MATCH |
| Con Op EBITDA margin Q1FY27 | 3.3% | 3.31/98.85 = 3.35% | L370 | MATCH |
| Con Op EBITDA Q1FY26 / margin | 14.86 / 17.0% | 14.86 / 16.96% | L385/380/379/371/370 | MATCH |
| Con ETR FY26 | 77.6% | 4.94/6.36 = 77.6% | L392/385 | MATCH |
| Con PAT margin Q1FY27 | (8.0%) | −7.874/98.85 = −7.96% | L395/370 | MATCH |
| **Depreciation reconciliation (load-bearing)** | dep = 9.13 (filing prints 5.13) | Con total expenses 1075.54M ties ONLY with dep 91.27M; sum with 51.27 = 1035.54M, gap = exactly 40.00M = Rs 4.00 Cr → true dep 91.27M = Rs 9.13 Cr; independently corroborated by deck p10 dep 9.1 (L354) and cash-PAT bridge 1.3−(−7.9)=9.2 | L380/382; deck L354 | MATCH — A4 flag CORRECT & load-bearing; PBT/PAT unaffected (printed independently, reconcile) |
| Std Rev YoY | +8.6% | (82.99−76.40)/76.40 = 8.62% | L168 | MATCH |
| Std core PBT YoY | −9.3% | (5.573−6.147)/6.147 = −9.3% | L187/170 | MATCH |
| Std reported PBT YoY | +11.5% | 1.002/8.729 = 11.5% | L187 | MATCH |
| Std PAT YoY | +11.2% | 0.729/6.523 = 11.2% | L199 | MATCH |
| Con Rev YoY | +12.8% | 11.22/87.63 = 12.8% | L370 | MATCH |
| Con Op EBITDA YoY | −77.7% | (3.31−14.86)/14.86 = −77.7% | derived | MATCH |
| Con Op EBITDA margin YoY | −1,361 bps | 3.35% − 16.96% = −13.61pp | derived | MATCH |
| Con dep YoY | +401% | (9.127−1.819)/1.819 = +401.8% | L380*/L380 | MATCH |
| Con PBT YoY | −179.2% | (−8.543−10.786)/10.786 = −179.2% | L385 | MATCH |
| Con PAT YoY | −198.6% | −15.858/7.984 = −198.6% | L395 | MATCH |
| Std PAT bridge subtotal | +1.00 (=PBT Δ) | −2.00−0.17+1.59+1.58 = +1.00 | Step 4A | MATCH |
| Con PAT bridge subtotal | −19.33 (=PBT Δ) | −11.55−7.31+0.64−1.11 = −19.33 | Step 4B | MATCH |
| S→C PAT gap Q1FY27 | (15.13) | −7.874−7.252 = −15.13 | L395/L199 | MATCH |
| S→C gap %/std PAT Q1FY27 | −208.6% | −15.126/7.252 = −208.6% | derived | MATCH |
| S→C gap FY26 % (YAML) | −94.7% | −25.28/26.71 = −94.6% | L199/L395 FY | MATCH (rounding) |
| Trailing P/E (consol / standalone FY26) | ~625x / ~33x | 174.90/0.28=624.6; 174.90/5.33=32.8 | deck L1056/L940; L214 | MATCH |
| Shares implied | 5.2 Cr | 914.15/174.90 = 5.226 Cr | deck L1060/1056 | MATCH |

Within-rounding note (not a FAIL): Std depreciation YoY — A4 prints +11.8% (from displayed 1.61/1.44); raw is (1.606−1.439)/1.439 = +11.6%. Difference is a rounding-of-inputs artifact, below tolerance. Directionally identical, no analytical impact.

**ARITHMETIC = PASS. Zero mismatches above rounding. The consolidated depreciation reconciliation (5.13→9.13) is independently reproducible and correct; every downstream consolidated EBITDA/bridge figure built on 9.13 is sound.**

---

## AUDIT 3 — ADVERSARIAL READ (three most positive A4 claims; strongest bear counter from same extract)

**Positive claim A (most positive, the thesis pivot):** "The consolidated loss is explained and arguably transitional — front-loaded Dahej depreciation + start-up cost ahead of the Krystal revenue ramp; a genuine transition-alpha candidate whose turn the Q3-Q4 FY27 ramp absorbs." (review Step 4B L243, Step 8 L340.)

Strongest bear counter from the extract: The deterioration is visible at the GROSS-PROFIT line, which sits entirely ABOVE depreciation and above fixed opex. Deck/PR show **standalone gross margin −734 bps (25.0% → 17.7%; gross profit 19.1 → 14.7)** — and the parent carries NONE of the Dahej depreciation — alongside **consolidated gross margin −1,282 bps (29.5% → 16.7%)** (presentation ledger 2a #3-4 / 2b #3-4, press-release S3/C3). Consolidated COGS (99.04, L376) exceeded consolidated revenue (98.85, L370) this quarter. Because gross profit is struck before any depreciation, a material share of the collapse is unit-economics / product-mix / raw-material / FIFO — which higher Dahej utilisation does NOT mechanically restore. A4's central "fixed cost ahead of revenue, ramp fixes it" framing is therefore incomplete, and A4 never surfaces the gross-margin line at all (Step 1C/1D and Step 2A/2B omit gross profit/gross margin entirely; the standalone −734 bps signal — the cleanest proof that parent unit economics eroded independent of any subsidiary/Dahej story — is absent). **COUNTER SURVIVES → must be grafted into A4.**

**Positive claim B:** "Standalone revenue grew +8.6% YoY and the parent stayed profitable throughout; standalone PAT +11.2%." (Step 2A L136/145.)

Bear counter from the extract: strip Other Income (+61.1%, L170) and finance-cost relief (−54.4%, L180) and standalone core PBT ex-OI FELL −9.3% (6.15 → 5.57); OI/PBT jumped 29.6% → 42.7%; if OI reverts to the prior 2.58 level, standalone PBT is ~8.15 Cr, below last year. **DOES NOT SURVIVE — A4 already builds this counter into its own claim (Step 2A diagnostics 3-6, Step 4A "recurring core contributed negatively −2.00 Cr").** Fully incorporated.

**Positive claim C:** "Finance costs fell (deleveraging/IPO); net debt fell ~Rs 86 Cr on IPO proceeds; adequate near-term liquidity." (Step 2A L140, Step 5 L286.)

Bear counter from the extract: the group is now loss-making and cash-consumptive — FY25 CFO −24.9 Cr, FY26 investing outflow −101.5 Cr, FCF −71.9 Cr, inventories built +67.6 Cr to 233.7 (deck CF/BS p28-29 / ledger 2d-2e), short-term borrowings still 128.1 Cr at Mar-26; no Jun-26 cash flow or balance sheet is filed so post-IPO liquidity cannot be confirmed. **DOES NOT SURVIVE — A4 caps the verdict at INDETERMINATE and flags every one of these items (Step 5, flag 3).** Fully incorporated.

Surviving counters: **1** (claim A — the gross-margin collapse above the depreciation line, including standalone −734 bps where there is no Dahej burden).

Required graft into A4 before save (to A4): Add a gross-profit / gross-margin row to the Step 1C/1D derived tables and the Step 2A/2B YoY tables (Std GM 17.7% vs 25.0% = −734 bps; Con GM 16.7% vs 29.5% = −1,282 bps), and qualify the "arguably transitional / ramp-absorbs-it" language in Step 4B and Step 8 with: a substantial part of the margin loss is struck ABOVE depreciation (gross level) and appears in the parent too, which carries no Dahej fixed cost, so it is a unit-economics / mix / RM / FIFO problem that utilisation alone will not reverse.

---

## VERDICT

**INCOMPLETE.** Failing agent: **A4.** Exact gap: one surviving, extract-supported bear counter is not incorporated — the gross-margin collapse (standalone −734 bps at 17.7% vs 25.0%, consolidated −1,282 bps at 16.7% vs 29.5%; deck/PR gross-profit rows) sits above the depreciation line and appears in the parent that carries no Dahej burden, materially qualifying A4's central "loss is transitional fixed-cost-ahead-of-revenue" thesis. A4 omits the gross-profit/gross-margin line from every derived and YoY table. Graft the gross-margin evidence and the qualifier (per Audit 3) into Steps 1, 2, 4B, and 8, then resubmit for save.

Gate 0 (deliverable) PASS, Audit 1 (coverage) PASS, Audit 2 (arithmetic) PASS. The sole blocker is the unincorporated surviving bear counter under Audit 3.

```yaml
stage: A5-adversary
company: "GEMAROMA"
quarter: "Q1FY27"
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
arithmetic_mismatches: []
surviving_bear_counters:
  - claim: "The consolidated loss is arguably transitional — front-loaded Dahej depreciation + start-up cost ahead of the Krystal revenue ramp (transition-alpha candidate); Step 4B L243 / Step 8 L340"
    counter: "Margin collapse is visible at the GROSS line, above depreciation: standalone gross margin -734 bps (25.0% -> 17.7%) with the parent carrying NO Dahej depreciation, and consolidated gross margin -1282 bps (29.5% -> 16.7%); consolidated COGS 99.04 exceeded revenue 98.85. A large share of the deterioration is unit-economics/mix/RM/FIFO, which utilisation does not mechanically restore. A4 omits the gross-profit/gross-margin line from all Step 1/2 tables."
    source_line: "deck p9 L295/297 & p10 L338/340; PR S3 L74 / C3 L91; results L376/L370"
loop_back_to: "A4"
gap: "Surviving bear counter not incorporated: add gross-profit/gross-margin rows (Std -734 bps 17.7% vs 25.0%; Con -1282 bps 16.7% vs 29.5%) to Step 1C/1D and Step 2A/2B, and qualify the 'transitional fixed-cost' framing in Steps 4B and 8 — the gross-margin loss is struck above depreciation and appears in the Dahej-free parent, so it is a unit-economics/mix/RM/FIFO problem utilisation alone will not reverse."
```
