# A5 ADVERSARY / COMPLETENESS AUDIT — Digitide Solutions Limited (DSSL)

**Agent:** A5 ADVERSARY | **Model:** claude-opus-4-8
**Quarter:** Q1 FY27 (quarter ended 30 June 2026) | **Audited:** 2026-07-28
**Under audit:** `runs/dssl-q1fy27/work/review_dssl_q1fy27.md` (A4)
**Fresh context:** A4 review + A1 extracts (results / press release / presentation) + A2 ledgers. All A4/A3 cites independently re-checked at their line numbers; unit conversion re-run from raw (results filing INR mn / 10 = Rs Cr; PR and deck already Rs Cr).

---

## AUDIT 1 — COVERAGE (fresh enumeration vs A2 ledgers, and ledger-vs-A4)

Fresh grep/sweep re-run on each extract, diffed against each ledger COUNT TEST; then each material ledger row checked for A4 citation or explicit "reviewed, no finding."

| Category | A2 count | My fresh count | Orphan rows (in ledger, absent from A4) | Status |
|---|---|---|---|---|
| Results — notes | 11 | 11 (consol 5 @ L591/595/598/606/617 + demerger para L614; std 6 @ L883/888/896/899/902/914) | none | PASS |
| Results — line items | 81 | 81 (consol P&L C1-C36 =36; consol segment S1-S21 =21; std T1-T24 =24) | none | PASS |
| Results — entities | 24 | 24 (Annexure-1 12 @ p4 L195-219; Appendix-1 12 @ p8 L634-657) | none | PASS |
| Results — auditor paras | 11 | 11 (consol 7 @ p2-3; std 4 @ p9) | none | PASS |
| Results — signature blocks | 5 | 5 (SB1 CS; SB2/SB3 auditor; SB4/SB5 CEO notes) | none (blanket "reviewed"; timestamps benign) | PASS |
| Results — UDINs | 2 | 2 (26110128CHYFAI5661 L185; 26110128CRFPZH3202 L712) | none | PASS |
| Results — agenda items | 1 | 1 (results approval only, L38-44) | none | PASS |
| Results — zero-standing | 5 | 5 (C10, S12, T10 exceptional nil; T12 current tax nil; T13 prior-yr tax nil, Q1FY27) | none | PASS |
| Press release — disclosure units | 148 | 148 (10+7+16+24+25+24+5+12+2+15+3+5) | none | PASS |
| Presentation — slides | 34 | 34 ([[PAGE 1]]..[[PAGE 34]]) | none | PASS |
| Presentation — numbers | 554 | reconciles (per-slide tallies sum 554; spot-checked slides 22=38, 23=75, 24=102, 25=72, 33=54) | none | PASS |
| Presentation — footnotes | 5 | 5 (slides 8/22/23/24/33) | none | PASS |
| Presentation — line items | 28 | 28 (slide 22 =7; slide 23 =6; slide 33 =15) | none | PASS |

**Rows my fresh pass found that the ledger lacks:** none. **Missing_from_ledger: [] (no FAIL to A2).**

**Material-flag → A4 traceability (orphan check to A3):**
- ZERO_STANDING exceptional nil Q1FY27 → A4 L48 ("Q1 FY27 exceptional = NIL"). Cited.
- ZERO_STANDING std current/prior-yr tax nil → A4 L352 / Q3. Cited.
- ENTITY_CHANGE Manila "Allsectech"/"Alldigi Tech" (E7/E15) → A4 DF10/M1, L360/L289/Q11. Cited.
- ENTITY_CHANGE Digitide ESOP Trust new-in-perimeter (E12/E24) → A4 0D/DF9/DF11, L44/L358. Cited.
- ENTITY_CHANGE Quess GTS Canada "Holding"/"Holdings" (E10/E22) → **not individually surfaced** by A4, but the ledger itself classes it "likely OCR/typo, verify" (trivial singular/plural, same obvious entity). A4's blanket "no ledger row unreviewed" + treating it as OCR noise (while surfacing the materially different Manila *rebrand*) is defensible "reviewed, no finding." NOT an orphan FAIL.
- Other Matters AP6/AP7 unnamed 6 + 4 subs → A4 L50/L230/DF3/DF4/Q6/Q7. Cited.
- Cross-statement exceptional-items arithmetic (ledger flagged FOR A5) → reconciles cleanly (see Audit 2, row X); A4 handled via Notes N4/N5. No orphan.
- Deck MECHANICAL_INCONSISTENCY (slide 23 "32%/Q4FY26" header) → A4 M1/Q11. Cited.
- Deck SOLE_SOURCE Q2/Q3 FY26 PAT → A4 Step 3 ("deck-sole-source, not in filing"). Cited.
- Deck DECK_COLOR_INVERSE (Top-30 concentration 57.7→59.5) and UNIT_MISMATCH (slide 15 "$2M-$6M+" USD use-case stat) → not individually discussed by A4; both immaterial to any P&L/valuation line (marketing/qualitative). Acceptable "reviewed, no finding." NOT orphan FAILs.

**COVERAGE VERDICT: PASS.** Fresh counts tie to every ledger; no orphan rows rise to FAIL; nothing found that the ledgers lack.

---

## AUDIT 2 — ARITHMETIC (every A4 derived metric recomputed from raw)

Raw ties first (results filing / 10): every anchored cell in A4 Tables 1A/1B re-derived from the INR-mn source and matches (Rev 7,750.72→775.07; EmpBen 5,832.98→583.30; Fin 151.22→15.12; D&A 551.76→55.18; OthExp 1,148.84→114.88; PBExcep 109.19→10.92; PAT 29.33→2.93; Owners (18.91)→(1.89); NCI 48.24→4.82; std PAT (105.81)→(10.58); reserves consol 6,891.08→689.11 / std 7,500.49→750.05; garbled consol paid-up "1.4q1,11," = 1,491.10 = std T21 = 149.11 Cr, matching A4's raster read). No raw-extraction error.

| Metric | A4 value | Recomputed | Source line(s) | Status |
|---|---|---|---|---|
| Consol Op EBITDA Q1FY27 (Rev−EmpBen−OthExp = PBExcep+D+Fin−OI) | 76.89 | 775.07−583.30−114.88 = 76.89 | ext L244/261/276 | PASS |
| Consol Op EBITDA Q4 | 87.89 | 87.90 (12.03+66.41+14.66−5.20) | ext L262-276 | PASS (0.01 rounding) |
| Op EBITDA margin Q1FY27 | 9.92% | 76.89/775.07 = 9.92% | — | PASS |
| Op EBITDA margin YoY | −130 bps | 9.92−11.22 = −130 | — | PASS |
| Op EBITDA YoY % | −6.9% | −5.69/82.58 = −6.89% | — | PASS |
| Revenue YoY % | +5.3% | 39.33/735.74 = +5.35% | — | PASS |
| D&A YoY % | +19.7% | 9.10/46.08 = +19.75% | — | PASS |
| Finance YoY % | +34.8% | 3.90/11.22 = +34.76% | — | PASS |
| EBIT(op) Q1FY27 / YoY | 21.71 / −40.5% | 76.89−55.18=21.71; −14.79/36.50=−40.5% | — | PASS |
| Core Op PBT (EBIT−Fin) Q1FY27 / YoY | 6.59 / −73.9% | 21.71−15.12=6.59; −18.69/25.28=−73.9% | — | PASS |
| Reported PBT YoY | −45.4% | −9.07/19.99 = −45.4% | ext L287-299 | PASS |
| PAT total YoY | −69.7% | −6.76/9.69 = −69.8% | ext L327 | PASS |
| Owners YoY swing | −7.62 Cr to loss | −1.89−5.73 = −7.62 | ext L374 | PASS |
| Effective Tax Rate Q1FY27 | 73.2% | 7.99/10.92 = 73.2% | ext L321/299 | PASS |
| ETR FY26 | 82.4% | 26.03/31.57 = 82.4% | — | PASS |
| Std Op EBITDA Q1FY27 / margin | 34.93 / 7.34% | 475.99−365.05−76.01=34.93; /475.99=7.34% | ext L736/753/768 | PASS |
| Std Op EBITDA YoY | −30.1% | −15.04/49.97 = −30.1% | — | PASS |
| Std revenue YoY | +2.6% | 12.16/463.83 = +2.62% | — | PASS |
| PAT bridge (sum of components) | −6.76 | −5.69−9.10−3.90+0.75+8.87+2.31 = −6.76 | ext (all) | PASS (ties to reported ΔPAT) |
| S-vs-C gap Q1FY27 | −13.51 | −10.58−2.93 = −13.51 | — | PASS |
| Owners decomposition | −105.81 +86.90 = −18.91 (mn) | ties | ext L820/374/379 | PASS |
| Reserves inversion (consol vs std) | 8.1% below | 60.94/750.05 = 8.12% | ext L432/856 | PASS |
| Unallocated seg liab YoY | +97.3% | 150.17/154.38 = +97.3% | ext L573-576 | PASS |
| BPM seg assets QoQ | +6.1% | 79.20/1,299.12 = +6.10% | ext L541-544 | PASS |
| BPM seg result margin YoY | −284 bps | 14.13−16.97 = −284 (76.00/537.72 vs 91.408/538.71) | ext L490/489/473 | PASS |
| T&D seg result margin QoQ | −408 bps | 7.98−12.06 = −408 | ext L494/495 | PASS |
| **T&D seg result margin YoY** | **−156 bps** | **7.976−9.796 = −182 bps** (189.32/2,373.55 vs 193.01/1,970.27) | ext_results L494/478 & L496/480 | **FAIL** |
| Deck seg-EBITDA total 91.7 vs filing seg-result 94.93 | as stated | 949.32/10 = 94.93; deck 91.7 | ext L500; deck L963 | PASS |
| Capital-employed proxy / ROCE (Step 7 indicative) | 918.27 / ~9.5% | 2,032.45−1,114.18=918.27; 86.84/918.27=9.46% | ext L556/578 | PASS |
| **Cross-statement exceptional reconciliation (ledger flag for A5)** | — | Q4 consol 16.12 − std 12.32 = 3.80 = sub labour-code (15.85−12.05); FY consol 64.76 = 41.22+23.54; std 56.94 = 33.41+23.54 | ext N4/N5, L611/907 | PASS (reconciles cleanly) |

**The one FAIL — detail:**
- **A4 review L267** (Step 5-SEGMENT table) states the T&D **segment-RESULT** margin fell "**−408 bps QoQ, −156 bps YoY**" beside filing segment-result margins **9.80% (Q1FY26) → 12.06% (Q4) → 7.98% (Q1FY27)**.
- On that stated (filing segment-result) basis the YoY delta is **7.98% − 9.80% = −182 bps**, not −156 bps. The QoQ −408 is correct on this basis; the YoY −156 is not.
- **−156 bps is the deck's *Segment-EBITDA* cut** (excl. unallocated corporate cost): 9.5% → 8.0% = −156 bps (`extract_presentation` L957 / presentation ledger Table 4 L178). A4 imported the deck's pre-computed EBITDA-basis YoY delta but placed it against the filing segment-result margins — a basis-mix. Discrepancy 26 bps, above rounding.
- **Direction of conclusion is unaffected** (T&D 8.0% sits below BPM 14.1%; margin-dilutive either way), but the printed derived metric is internally inconsistent with its own row and must be reconciled before save.
- **Loop back to A4.** Fix: set T&D segment-result YoY to **−182 bps**, OR relabel the row's margins to the deck's segment-EBITDA basis (9.5/12.1/8.0) so −156 is internally consistent. Pick one basis per cell.

**ARITHMETIC VERDICT: FAIL (1 mismatch, → A4).** All other derived metrics (incl. the PAT bridge, S-vs-C gap, ETR, reserves inversion, and the A5-flagged cross-statement exceptional reconciliation) recompute clean.

---

## AUDIT 3 — ADVERSARIAL READ (three most-positive A4 claims; strongest bear counter from the SAME extract)

A4 is already a symmetric-to-bearish review that pre-empts the bull case. Testing whether any bear counter survives *un-incorporated*:

**Claim 1 (L124):** "Management EBITDA is a genuine *operating* measure … the 9.9% margin is a clean operating-margin read … NOT flattered by treasury/OI."
- **Bear counter (same text):** 9.9% is struck *after* only the past-service *catch-up* was carved to exceptional; the ongoing New-Labour-Code service cost now sits inside Employee Benefits, and minimum-wage revisions (PR L87, deck L835) are recurring — so 9.9% embeds a rising cost floor, not a clean base. Revenue "+5.3% YoY" also masks a −3.1% QoQ dip (deck L1094: 800.0→775.1) and BPM (69% of rev) flat −0.2% (ext L472/489).
- **Survives?** NO. A4 already states exactly this (L124 caveat; Step 2 diagnostics 1-3; Step 3 QoQ dip). Already incorporated.

**Claim 2 (L84/L48 framing):** "Reported PAT turned positive at Rs 2.9 Cr … no exceptional items … clean base."
- **Bear counter (same text):** the Rs 2.93 Cr is 100% NCI; owners lost Rs 1.89 Cr (ext L374) and the standalone parent lost Rs 10.58 Cr (ext L820); the QoQ turn is the roll-off of the Q4 labour-code exceptional, not recovery.
- **Survives?** NO. A4 elevates precisely this as "the single most important reconciliation" (Step 4B, L228; flags 2-3). Already incorporated.

**Claim 3 (Step 6D, L305 / L303):** T&D + International growth trigger "ON TRACK (volume)"; AI-led revenue "~Rs 15 Cr+ … emerging as a distinct growth driver."
- **Bear counter (same text):** both "growth engines" fell QoQ (T&D −4.7%, Intl −2.9%, PR L125/L202), so "on track" is YoY-only; and "~Rs 15 Cr+ AI-led revenue" (deck L784) is not reconcilable to the slide-14 ACV components (~2 + ~13 + 6 Cr = 21, and ACV is a bookings metric ≠ revenue), so the AI-revenue figure is definitionally loose.
- **Survives?** NO (net). A4 already tags AI-led "DELAYED / UNVERIFIED … Undefined KPIs (FN-08); unit economics undisclosed" (L305), logs the QoQ declines in the segment table (L266/L304), and raises Q14 to define TCV/AI-interaction/annuity. The ACV-vs-revenue conflation is the only genuinely new sliver, but it is subsumed by A4's existing "undefined KPI / unverified" treatment and does not change any number or verdict. Not material enough to graft.

**ADVERSARIAL VERDICT: no surviving bear counter requires grafting.** A4's completeness against its own positive claims is strong. `surviving_bear_counters: []`.

---

## VERDICT

**INCOMPLETE.** One arithmetic FAIL survives: A4 review **L267** prints the T&D segment-**result** YoY margin as **−156 bps** (the deck's segment-**EBITDA**-basis delta) while the row's own filing segment-result margins (9.80% → 7.98%) yield **−182 bps**. Discrepancy 26 bps, above rounding; internally inconsistent within the cell. Coverage PASSES (all fresh counts tie to the three ledgers; no orphan rows; nothing missing from ledgers) and the adversarial read surfaces no un-incorporated surviving bear counter. Only this single, mechanically-fixable derived-metric mismatch blocks save.

**Loop back to:** A4. **Exact gap:** reconcile the Step 5-SEGMENT T&D YoY margin delta to **−182 bps** on the stated filing segment-result basis (or relabel that row's margins to the deck's segment-EBITDA basis 9.5/12.1/8.0 so −156 is consistent). Re-emit, then A5 re-clears for Notion save.

```yaml
stage: A5-adversary
company: "DSSL"
quarter: "Q1 FY27"
model: claude-opus-4-8
status: complete
verdict: INCOMPLETE
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches:
  - metric: "T&D segment-result margin YoY (Step 5-SEGMENT table)"
    a4_value: "-156 bps"
    recomputed: "-182 bps (7.976% Q1FY27 vs 9.796% Q1FY26, filing segment-result basis)"
    source_line: "review L267; extract_results L494/478 (Q1FY27 189.32/2373.55) & L496/480 (Q1FY26 193.01/1970.27); note -156 is the deck segment-EBITDA basis, extract_presentation L957"
surviving_bear_counters: []
loop_back_to: "A4"
gap: "Step 5-SEGMENT T&D YoY margin delta reads -156 bps (deck segment-EBITDA basis) but the row's own filing segment-result margins (9.80%->7.98%) yield -182 bps; basis-mixed, above rounding. Reconcile to -182 bps on the filing segment-result basis (or relabel that row's margins to the deck segment-EBITDA basis so -156 is internally consistent) before Notion save."
```
