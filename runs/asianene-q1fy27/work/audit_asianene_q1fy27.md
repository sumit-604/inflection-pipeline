# A5 ADVERSARY / COMPLETENESS AUDIT — Asian Energy Services Limited (ASIANENE) — Q1 FY27

**Agent:** A5 Adversary | **Model:** claude-opus-4-8 | **Date:** 13 Aug 2026
**Under audit:** `review_asianene_q1fy27.md` (A4 analyst)
**Method:** fresh context; every number re-derived from the A1 extracts (results in Lakhs ×0.01; deck/PR in Rs Cr); coverage re-enumerated by independent grep + manual sweep and diffed against the A2 ledgers. No deference to A3/A4 cites.

Scope check: run has RESULTS + PRESENTATION + PRESS RELEASE, **no concall**. A4 correctly scoped Role 5 = N/A, turns = 0, and fabricated **no** concall analysis (Step 8.5 explicitly routes questions to IR email, not a transcript). Verified — no phantom concall.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate, run first)

The mandatory PLAIN-LANGUAGE BRIEF is present with all four labelled parts non-empty and carrying real content:

| Part | Location | Present? | Non-placeholder? |
|---|---|---|---|
| (1) Summary narrative | L436-438 (~18 lines) | present | yes — provenance-tagged, numbers-anchored |
| (2) SECTOR intelligence | L440-442 | present | yes |
| (3) BUSINESS-MODEL intelligence | L444-446 | present | yes |
| (4) COMPETITION intelligence | L448-450 | present | yes |

**Gate 0: PASS.**

---

## AUDIT 1 — COVERAGE (fresh enumeration diffed against A2)

Independent grep pass (my counts) vs A2 ledger:

| Category | A2 count | My fresh count | Method | Orphan rows | Status |
|---|---|---|---|---|---|
| Results — numbered notes | 17 (9 consol + 8 stand) | 17 | consol notes 1-9 + stand notes 1-8 read at cited lines | none | PASS |
| Results — consolidation entities | 31 (26 subs + 5 JVs) | 31 | grep jurisdictions L194-219 = 26 subs; `Joint Venture$` = 5 | none | PASS |
| Results — auditor paragraphs | 13 (8 + 5) | 13 | read L79-164 / L434-484 | none | PASS |
| Results — P&L line items | 90 | 90 (36+14+6+28+6) | read all tables | none | PASS |
| Results — signature blocks | 5 | 5 | 2 auditor + 2 MD (DIN 01360843 ×2) + 1 CS | none | PASS |
| Presentation — slides | 34 | 34 | `^\[page \d+\]` = 34 | none | PASS |
| Presentation — number rows | 96 | consistent | spot-checked P&L slide 12, highlights 9/10, order-book 26 | none | PASS |
| Presentation — footnotes | 5 | 5 | L255/297/437/872/898 | none | PASS |
| Press release — narrative units | 41 (19+2+8+12) | 41 | 19 headline + 2 quotes + 8 forward + 12 operational | none | PASS |

**Orphan rows (ledger row absent from A4): NONE.** A4's reconciliation preamble (L12-18) asserts 100% review on all three ledgers; every material flagged row is traceable into A4 (ENTITY_COUNT_UNRECONCILED → Q3 + earnings-quality flag; ZERO_STANDING exceptional → Step 1 "armed"; Other-equity blank → Steps 5/7; note-5 OCR "S" corruption → correctly read as Oilmax note; agri subsidiary OC12 → Step 7 no-reclassify).

**Rows my fresh pass found that the ledger lacks: NONE.**

Coverage **PASS** (no A2 loop-back, no A3 loop-back).

One coverage-adjacent note (not a coverage failure): the A2 **presentation** ledger's slide-11 "Profit" chart carries an INFERRED_PAIRING it self-flagged as unverified — it inferred Mineral profit **4.1→4.7 (rising)**. The authoritative filing (results L317) shows Mineral segment result **4.69→4.07 (falling)**, i.e. the deck tokens pair 4.7 (FY26) → 4.1 (FY27). A2 flagged the inference as unverified, so this is not an A2 enumeration failure; but it feeds directly into the arithmetic/adversarial findings below.

---

## AUDIT 2 — ARITHMETIC (every derived metric recomputed from raw extract lines)

Unit conversion audited first (the classic 100× trap): results filing is **Lakhs ÷100 = Rs Cr**. A4 applied this correctly on every cell. **No 100× error anywhere.** Spot-anchors: Revenue 27,118.53 Lakhs → 271.19 Cr; PAT 1,275.65 → 12.76 Cr; paid-up 4,862.90 → 48.63 Cr. All correct.

| Metric | A4 value | My recompute | Source line(s) | Status |
|---|---|---|---|---|
| Consol revenue YoY | +135.1% | 27,118.53/11,536.69 = +135.06% | L245 | PASS |
| Consol op-EBITDA (ex-JV,ex-OI) Q1FY27 | 21.14 | 27,118.53−21,892.76−17.04−1,838.00−1,256.06 = 2,114.67 → 21.15 | L245-255 | PASS (0.01 rounding) |
| Consol op-EBITDA margin Q1FY27 | 7.80% | 21.147/271.19 = 7.80% | derived | PASS |
| Consol op-EBITDA Q1FY26 | 11.45 | 1,146.21 → 11.46 | L245-255 | PASS (0.01 rounding) |
| Consol op-EBITDA margin Q1FY26 | 9.92% | 11.462/115.367 = 9.94% | derived | PASS (2 bps rounding; margin drop −212 vs my −214 bps, immaterial) |
| Deck EBITDA (incl-JV) Q1FY27 / margin | 21.93 / 8.09% | 21.15+0.79 = 21.94 / 8.09% (deck prints 21.9 / 8.1%) | L259, deck L406-408 | PASS |
| **"7.80% operating vs deck 8.1%"** | both cited | 7.80% = op-EBITDA **ex-JV ex-OI**; 8.09%/8.1% = deck EBITDA **incl JV**. Two different definitions; **both correct**, A4 did not conflate | — | **PASS — A4 is right** |
| Standalone op-EBITDA margin Q1FY27 | 10.92% | 1,629.31/14,927.67 = 10.91% | L527-537 | PASS |
| Standalone revenue YoY | +29.4% | 14,927.67/11,536.69 = +29.39% | L527 | PASS |
| S-vs-C PAT gap Q1FY26 (% of standalone) | −7.8% | (563.23−610.92)/610.92 = −7.81% | L269/L550 | PASS |
| S-vs-C PAT gap Q4FY26 | +43.9% | (3,265.19−2,268.79)/2,268.79 = +43.92% | L269/L550 | PASS |
| S-vs-C PAT gap Q1FY27 | +33.5% | (1,275.65−955.28)/955.28 = +33.54% | L269/L550 | PASS |
| S-vs-C swing | ~41.3 pp | −7.81 → +33.54 = 41.35 pp | derived | PASS |
| Revenue gap (subs) Q1FY27 | 121.91 | 271.19−149.28 | L245/L527 | PASS |
| Incremental subsidiary margin | ~4.0% | (21.14−16.30)/121.91 = 3.97% | derived | PASS |
| **17.6% of PAT unaudited** | Rs 2.24 Cr = 17.6% | (145.19+78.85)/1,275.65 = 224.04/1,275.65 = 17.56% | L137-139/L269 | **PASS** |
| Loss-shell subsidiary | Rs (3.26) Cr on nil rev | 325.51 Lakhs → 3.26 Cr, revenue Nil | L112-114 | PASS |
| **+8.7% share count** | +8.7% (447.44→486.29 lakh sh) | (4,862.90−4,474.43)/4,474.43 = +8.68% | L293/L563 | **PASS** |
| Effective tax rate consol Q1FY27 | 25.4% | 435.20/1,710.85 = 25.44% | L268/L262 | PASS |
| PAT bridge total | +Rs 7.13 Cr | 1,275.65−563.23 = 712.42 → +7.12 | L269 | PASS (0.01 rounding) |
| Finance cost YoY | +150.3% | 376.38/150.34 = +150.35% | L253 | PASS |
| Exceptional FY26 consol / standalone | 9.40 / 2.72 | 940.31 / 271.82 Lakhs | L261/L541 | PASS |
| **Mineral segment RESULT YoY** | *(not computed by A4)* | 469.05→406.97 = **−13.2% YoY** | **L317** | see Audit 3 (surviving counter) |

Two op-EBITDA cells (Q1FY26 11.45 vs 11.46; Q1FY27 21.14 vs 21.15) are each 0.01 Cr = 1 Lakh under mine — **at display precision, within rounding, not failures.** Other-income YoY shows the same input-rounding artefact (A4 +66.8% from rounded 3.32/1.99 vs +67.0% from raw 331.93/198.81) — immaterial.

**No arithmetic mismatch above rounding. Arithmetic PASS.** (No A4 loop-back on arithmetic.)

Tripwire discipline verified: all five held at **NOT FIRED / ARMED / CANNOT-ASSESS / AMBER** — none declared fired (Step 6C, L308-318). Cash conversion held **INDETERMINATE** and named the missing evidence (CFO, WC, receivable ageing, net debt); verdict landed PROCEED WITH FLAGS, which is at-or-more-severe than the mandated PROCEED-WITH-CAVEATS cap — the CLAUDE.md cash-conversion NEVER-rule is satisfied (it did not resolve silently to a clean PROCEED). Correct.

---

## AUDIT 3 — ADVERSARIAL READ (three most positive claims; strongest bear counter from the same extract)

**Positive claim 1 — "GSECL Rs 187.6 Cr order won, work commenced" → watchlist item 4 GREEN, growth-trigger GSECL FIRED (order-level)** (Step 6B L302, Step 6D L327). This is the single unambiguously GREEN cell in the entire review.
- **Bear counter (from the extract):** the segment that "won" GSECL — **Mineral & other energy services — saw its own segment RESULT fall YoY, Rs 4.69 Cr → Rs 4.07 Cr (results L317, 469.05→406.97 Lakhs, −13.2%)**, on top of the −68% QoQ revenue A4 already noted. **All** group segment-profit growth is O&G (L316, Rs 18.86 → 33.30 Cr). A won order sitting over a segment whose gross contribution is contracting YoY is a materially weaker "GREEN" than stated.
- **Does it survive?** **YES — un-incorporated.** A4 flags Mineral weakness only via revenue (−68% QoQ) and backlog-vs-run-rate ("thin execution"), and rates order-conversion WEAKENED — but nowhere states that Mineral **segment profit fell YoY**, and it leaves watchlist item 4 flatly GREEN and the trigger FIRED. The counter is supported by L317 and must be grafted before save.

**Positive claim 2 — "Standalone organic quarter decent: revenue +29.4%, PAT +56%, margin +62 bps"** (Step 2, Step 8).
- **Bear counter:** +29.4% is **below** the 30-40% order-backed guide floor, and standalone margin fell hard QoQ from 18.61% (Q4 FY26) to 10.92%.
- **Survives? NO — already incorporated.** A4 books this as TRIPWIRE 4 soft-miss (Step 6C L315), watchlist item 7 AMBER, and caveats Q4 as a balancing-figure seasonal peak. Adequately grafted.

**Positive claim 3 — "~100%+ of the PAT increase is core-operations-driven; growth is real, not treasury/OI-padded"** (Step 4 L217, Step 2 diag 3).
- **Bear counter:** 17.6% of PAT unaudited, Rs 0.79 Cr from unreviewed related-party JVs, ~4% incremental subsidiary margin, +8.7% dilution, EPS lags PAT by ~22 pp, and the whole +135% is a Kuiper base-effect.
- **Survives? NO — already incorporated.** Every element is surfaced prominently (Step 4S, earnings-quality flag, dilution-stack flag, Step 2 diag 4). Adequately grafted.

**One surviving bear counter (claim 1) requires grafting → this is an A4 loop-back.**

---

## VERDICT

**INCOMPLETE.**

- Deliverable gate: PASS (all four brief parts present).
- Coverage: PASS (counts reconcile; no orphan rows; no missing-from-ledger rows).
- Arithmetic: PASS (unit conversion clean, no 100× error; every derived metric — margins, ETR, S-vs-C gaps, 17.6% unaudited, +8.7% shares, PAT bridge, YoY/QoQ — reproduces within rounding; the 7.80% vs 8.1% pair is two correct definitions, not an error).
- Adversarial: **FAIL** — one surviving, extract-supported bear counter is not incorporated.

**Loop back to: A4.**

**Exact gap:** Graft the Mineral & other-energy-services **segment-result YoY decline (Rs 4.69 Cr → Rs 4.07 Cr; results L317, 469.05→406.97 Lakhs; −13.2%)** into the GSECL framing. A4's sole GREEN light — watchlist item 4 "GSECL order won" GREEN and growth-trigger GSECL "FIRED (order-level)" — sits over a segment whose gross profit contribution is shrinking YoY while 100% of group segment-profit growth comes from Oil & Gas (L316). The GREEN rating and the "FIRED" trigger status should be re-cast (at minimum to AMBER / "order won into a declining-profit segment") with the L317 figure cited. Everything else in the review is COMPLETE and may stand unchanged.

---

```yaml
stage: A5-adversary
company: "ASIANENE"
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
arithmetic_mismatches: []
surviving_bear_counters:
  - claim: "GSECL Rs 187.6 Cr order won -> watchlist item 4 GREEN, growth-trigger GSECL FIRED (Step 6B L302 / Step 6D L327), the review's sole GREEN cell"
    counter: "The Mineral & other-energy-services segment that won GSECL saw its segment RESULT fall YoY Rs 4.69 Cr -> Rs 4.07 Cr (-13.2%); all group segment-profit growth is O&G (18.86 -> 33.30 Cr). A won order over a shrinking-profit segment is a weaker GREEN than stated; A4 flags Mineral revenue -68% QoQ but never the YoY segment-profit decline."
    source_line: "results L317 (Mineral 469.05->406.97 Lakhs); L316 (O&G 1,886.34->3,329.93 Lakhs)"
loop_back_to: "A4"
gap: "Graft the Mineral segment-result YoY decline (Rs 4.69 Cr -> Rs 4.07 Cr; results L317) into the GSECL framing and re-cast watchlist item 4 GREEN / growth-trigger GSECL FIRED (at minimum to AMBER: order won into a declining-profit segment, all segment-profit growth being O&G per L316). Deliverable, coverage, and arithmetic all PASS; this is the only blocker to save."
```
