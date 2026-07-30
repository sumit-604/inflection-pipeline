# A5 ADVERSARY / COMPLETENESS AUDIT (RE-AUDIT, loop 1) — MTAR Technologies (MTAR), Q1 FY27

**Agent:** A5 ADVERSARY | Fresh context: A4 merged review + 3 A1 extracts + 3 A2 ledgers only. Re-derived independently; A4 cites checked, not deferred to.
**Under audit:** review_merged_mtar_q1fy27.md (rev. 1, A4 loop-1 corrections). **Date:** 2026-07-30.
**Scope:** three audits (coverage / arithmetic / adversarial) in one pass, PLUS targeted verification of the four A4 corrections flagged by the prior A5 pass.

---

## PART A — VERIFICATION OF THE FOUR A4 CORRECTIONS

### Correction 1 — NET DEBT (Mar-26): VERIFIED PASS
Recomputed from balance-sheet slide cites (all anchors confirmed against presentation ledger):
- Gross debt = 147.7 (Borrowings NC, S26-4, ledger L410) + 221.6 (Borrowings Current, S26-10, L416) = **369.3**. A4 = 369.3. TIE.
- + leases 6.7 (NC, S26-5, L411) + 0.6 (Current, S26-11, L417) = 7.3 → borrowed 369.3 + 7.3 = **376.6**. A4 = 376.6. TIE.
- Net debt ex-MF = 376.6 − cash 1.0 (S27-13, L443) − bank 20.2 (S27-14, L444) = **355.4 ≈ 355**. A4 = ≈355. TIE.
- Net debt incl-MF = 355.4 − MF 215.3 (S27-11, L441) = **140.1 ≈ 140**. A4 = ≈140. TIE.
- Basis is now explicit (turns on whether the ₹215.3 Cr MF counts as cash). The unreconciled ~₹389 Cr figure is **GONE as an active number** — it survives only as three explicit withdrawal annotations (review L210, YAML L514, flag L563: "did not reconcile to either basis" / "unanchored ~389 dropped"). Correct traceability, not a live claim.
**RESULT: correction properly made.**

### Correction 2 — PROMOTER PACE: VERIFIED PASS
Series (S31-8/12/16/20, ledger L546/550/554/558): 31.41 / 30.59 / 30.44 / 29.35. TIE.
- Steps: 30.59−31.41 = **−0.82**; 30.44−30.59 = **−0.15**; 29.35−30.44 = **−1.09**. A4 = −0.82 / −0.15 / −1.09. TIE.
- Series-average: total drop 31.41−29.35 = 2.06 over 3 steps = 0.687 ≈ **0.69 pp/qtr**. A4 = ~0.69. TIE.
- The erroneous "~1.02 pp/qtr" is **GONE** (grep: zero occurrences of an active 1.02 pace anywhere in the review).
**RESULT: correction properly made.**

### Correction 3 — QUARTERS-TO-<25%: VERIFIED PASS
- Distance = 29.35 − 25 = **4.35 pp**. TIE.
- At latest pace 1.09 pp/qtr: 4.35 / 1.09 = 3.99 ≈ **4.0 quarters**. A4 = ~4.0. TIE.
- At average pace 0.69 pp/qtr: 4.35 / 0.69 = 6.30 ≈ **6.3 quarters**. A4 = ~6.3. TIE.
- Both scenarios stated in Section (d) (L384) and the verdict (L461). BOTH present.
**RESULT: correction properly made.**

### Correction 4 — MARGIN GRAFT (operating-leverage fragility clause): VERIFIED PASS
- Gross margin Q1 FY26 = 54.2% (S11-7, ledger L227); Q1 FY27 = 45.5% (S11-9, L229). Change = **−8.7 pp**. Independent tie: GP/rev = 84.9/156.6 = 54.21%; 164.2/360.7 = 45.52%. TIE.
- Products & Others mix = **28% Q1 FY27** (S10-10, L206), up from 15% FY26 (S10-9). TIE.
- EBITDA +550 bps = 23.6% − 18.1% = 5.5 pp. Confirmed **scale/operating-leverage-driven, NOT gross-margin-driven** (gross margin fell). Clause present at YoY table (L120), Step 2 diag 2 (L132), Section b (L355), verdict (L461), and YAML flag (L561).
**RESULT: correction properly made, gross-margin figures verified against slides.**

---

## PART B — COVERAGE AUDIT (fresh independent enumeration vs A2 ledgers)

| Category | A2 count | My fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Results: notes | 11 (6 consol L429-441 + 5 std L358-369) | 11 | none | PASS |
| Results: line items | 68 (34 std + 34 consol) | 68 | none | PASS |
| Results: zero_standing | 8 | 8 | none | PASS |
| Results: agenda items | 7 (L104-121) | 7 | none | PASS |
| Results: auditor paras | 26 (10 std + 16 consol) | 26 | none | PASS |
| Results: entities | 3 (MTAR + Gee Pee + Magnatar) | 3 | none | PASS |
| Results: annexure profiles | 2 | 2 | none | PASS |
| Results: signature blocks | 4 | 4 | none | PASS |
| Press rel: financial numbers | 26 (16 "Rs." + 10 "%") | 26 | none | PASS |
| Press rel: segment claims | 5 | 5 | none | PASS |
| Press rel: operational metric | 1 (16 units) | 1 | none | PASS |
| Press rel: MD sentences | 3 | 3 | none | PASS |
| Press rel: footnotes/disclaimer | 5 | 5 | none | PASS |
| Press rel: administrative | 14 | 14 | none | PASS |
| Presentation: slides | 32 | 32 | none | PASS |
| Presentation: numbers | 535 (per-slide checksum sums 535) | 535 | none | PASS |
| Presentation: footnotes | 7 | 7 | none | PASS |
| Presentation: zero_standing | 9 | 9 | none | PASS |

Every material/forensic ledger row is cited or reviewed in A4: results forensics F6-a/F8-a/F13-a/F14-a/F14-b/F14-c; press-release A3-F6-01/02, A3-F7-01, A3-F14-01, A3-F16-01; presentation F-01..F-13 — all incorporated (preamble L14-17), each generating a Step 8.5 question. No orphan row (ledger row absent from A4). No row my fresh pass found that the ledger lacks. The A4 corrections edited Steps 2/5, Sections b/d, verdict and YAML only — no coverage row removed; nothing regressed.
**COVERAGE: PASS.**

---

## PART C — ARITHMETIC AUDIT (recomputed from raw extracted numbers; results filing INR M ÷10)

| Metric | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| Order-book waterfall | 5,143.3 | 2,581.9 + 2,895.1 − 333.7 = 5,143.3 | S13-5/6/7/8 | PASS |
| Guidance target | 1,577 | 876.2 × 1.8 = 1,577.16 | S25 / S4-1 | PASS |
| Q1 % of target | 22.9% | 360.7 / 1,577.16 = 22.87% | S11-3 | PASS |
| Implied Q2-Q4 avg | 405.5/qtr | (1,577.16 − 360.7)/3 = 405.5 | derived | PASS |
| Flat-Q1 annualised | +64.7% | 360.7×4 / 876.2 − 1 = 64.7% | derived | PASS |
| Segment sum Q1FY27 | 360.7 (Δ0.1) | 3.2+36.4+220.8+100.4 = 360.8 | S7-5/S8-5/S9-5/S10-5 | PASS (rounding) |
| OCL change | +210.4 to 254.9 | 254.9 − 44.5 = 210.4 | S26-16 (L422) | PASS |
| NWC days | 274→172→59 | ties (146+128; 84+88; 3+56) | S14-3/9/12 | PASS |
| D/E | 0.24→0.45 | S30-11 / S30-12; recomp 0.243→0.449 | L533/534 | PASS |
| Revenue YoY | +130.4% | 360.72/156.58 − 1 = 130.4% | L396 | PASS |
| Revenue QoQ | +17.9% | 360.72/306.07 − 1 = 17.86% | L396 | PASS |
| Op EBITDA Q1FY27 | 85.05 | 67.402+9.692+15.847−7.887 = 85.05 | L410/404/403/397 | PASS |
| Op EBITDA Q1FY26 | 28.39 | 14.813+8.366+5.815−0.610 = 28.38 | L410/404/403/397 | PASS |
| Op EBITDA Q4FY26 | 61.80 | 59.542+9.038+9.621−16.395 = 61.81 | L410/404/403/397 | PASS |
| Op EBITDA margin YoY | 18.1%→23.6% (+550bps) | 28.39/156.58=18.1%; 85.05/360.72=23.6% | derived | PASS |
| Op EBITDA YoY % | +199.6% | 85.05/28.39 − 1 = 199.6% | derived | PASS |
| Gross margin YoY | 54.2%→45.5% (−8.7pp) | 84.9/156.6=54.2%; 164.2/360.7=45.5% | S11-4/6/7/9 | PASS |
| ETR Q1FY27 | 25.5% | 17.175/67.402 = 25.48% | L415/410 | PASS |
| ETR Q1FY26 | 27.0% | 4.000/14.813 = 27.0% | L415/410 | PASS |
| Core PBT ex-OI YoY | +319.1% | (67.402−7.887)/(14.813−0.610) − 1 = 319.0% | derived | PASS |
| PAT YoY change | +39.42 (+364.5%) | 50.227 − 10.813 = 39.41; /10.813 = 364.5% | L416 | PASS |
| PAT bridge: GP change | +79.3 | 164.2 − 84.9 = 79.3 | S11-4/6 | PASS |
| — volume effect | +110.7 | 204.14 × 0.542 = 110.6 | derived | PASS |
| — GP-margin effect | −31.4 | 360.72 × 0.087 = 31.4 | derived | PASS |
| — employee+other exp | +22.64 | (46.52+32.64)−(34.32+22.20) = 22.64 | L402/405 | PASS |
| — finance-cost change | +10.03 | 15.847 − 5.815 = 10.03 | L403 | PASS |
| — D&A change | +1.32 | 9.692 − 8.366 = 1.33 | L404 | PASS |
| — OI change | +7.28 | 7.887 − 0.610 = 7.28 | L397 | PASS |
| S-vs-C PAT gap Q1FY27 | 0.53% | (50.504−50.227)/50.504 = 0.55% | L345/416 | PASS (rounding, non-verdict) |
| S-vs-C PAT gap FY26 | 1.35% | (95.324−94.030)/95.324 = 1.36% | L345/416 | PASS (rounding) |
| Subsidiary rev share | 0.47% | 1.679/360.72 = 0.47% | L641/396 | PASS |
| Subsidiary loss share | 1.44% | 0.722/50.227 = 1.44% | L642/416 | PASS |
| Net debt ex-MF | 355.4 | 376.6 − 1.0 − 20.2 = 355.4 | S26/S27 | PASS |
| Net debt incl-MF | 140.1 | 355.4 − 215.3 = 140.1 | S27-11 | PASS |
| Promoter avg pace | 0.69 pp/q | 2.06/3 = 0.687 | S31 series | PASS |
| Quarters-to-25% (latest) | ~4.0 | 4.35/1.09 = 3.99 | derived | PASS |
| Quarters-to-25% (avg) | ~6.3 | 4.35/0.69 = 6.30 | derived | PASS |

No mismatch above rounding on any metric, verdict-bearing or otherwise. The S-vs-C PAT gaps reflect A4 computing (diff of rounded figures ÷ standalone); my recompute lands within 0.02 pp — immaterial, non-verdict-bearing. No new above-rounding error was introduced by the four corrections.
**ARITHMETIC: PASS.**

---

## PART D — ADVERSARIAL READ (three most positive A4 claims + strongest bear counter from the same extract)

1. **Positive:** "Core operating PBT +319.1% YoY — genuinely strong, not treasury-driven" (L125/133).
   **Bear counter (same extract):** the base Q1 FY26 (₹156.6 Cr = 17.9% of FY26, softest quarter) inflates the %; and the operating gain rides a gross-margin drop of 8.7 pp, so it is scale-contingent not structural.
   **Survives / grafted?** ALREADY GRAFTED — soft-base caveat (L131) + operating-leverage fragility clause (L132). Does NOT survive as a new addition.

2. **Positive:** "Op EBITDA margin +550 bps to 23.6%, clears the monitorable" (L120/234).
   **Bear counter:** gross margin −8.7 pp; the +550 bps is entirely fixed-cost spreading over a 2.3x revenue base, vulnerable if volume slows or the 28% Products mix (lower gross margin) persists.
   **Survives / grafted?** ALREADY GRAFTED — fragility clause at L120/132/355 and verdict L461. Does NOT survive.

3. **Positive:** "Order book ₹5,143.3 Cr ~2x baseline; highest-ever single-quarter inflow" (L272/328).
   **Bear counter:** the closing book is on a "restated" basis (net of forex/price escalation/scrap, F3/S13-7); gross-vs-net-of-GST and executed-vs-pending are undisclosed; the "highest ever" ₹2,895.1 Cr is a flow figure vs FY26's ₹2,453.3 Cr flow; three of four segment-mix slices are unassignable.
   **Survives / grafted?** ALREADY GRAFTED — DEFINITION_WATCH, quantum held (Section c, L359-368) + Q7 to management. Does NOT survive.

No bear counter survives un-incorporated. Nothing new needs grafting into A4.
**ADVERSARIAL: PASS.**

---

## VERDICT

**COMPLETE.** All four A4 loop-1 corrections are properly made and independently re-verified (net-debt basis + anchors with the ~389 figure withdrawn; promoter series/steps/0.69 avg with the 1.02 pace removed; both quarters-to-<25% scenarios at 4.35 pp distance; margin graft with slide-verified gross-margin −8.7 pp). Coverage reconciles to all three A2 ledgers with zero orphan and zero missing rows. Every derived metric recomputes within rounding; no new arithmetic error introduced. No surviving bear counter requires grafting. Cleared to proceed to Notion save.

```yaml
stage: A5-adversary
company: "MTAR"
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
```
