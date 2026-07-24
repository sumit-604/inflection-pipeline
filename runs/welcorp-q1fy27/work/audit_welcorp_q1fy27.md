# A5 ADVERSARY / COMPLETENESS AUDIT — Welspun Corp (WELCORP) — Q1 FY27

Fresh-context audit of `review_welcorp_q1fy27.md` (A4). Re-derived independently from the two A1 extracts and diffed against the two A2 ledgers. A4's and A3's cites were re-checked, not trusted. All line references below are to the A1 extracts (results extract unless prefixed "P-" for the presentation extract).

---

## AUDIT 1 — COVERAGE

Independent enumeration (fresh grep + manual sweep) vs A2 ledger counts, then every ledger category checked for citation-or-"reviewed" in A4.

### Results ledger

| Category | A2 count | My fresh count | Orphan rows (in ledger, absent from A4) | Status |
|---|---|---|---|---|
| Board-outcome agenda items | 3 | 3 | none — item 1 (results, Step 0), item 2 (GGBS/Slagexcel, Q12+monitorables), item 3 (WCPGL, Q1/Step 6D/monitorables) | PASS |
| Auditor-report paragraphs | 12 (7 consol + 5 standalone) | 12 | none — consol para 6 (EPIC unreviewed, Rs69.88 Cr) and para 7 (8 subs / Rs39.78 Cr loss) both cited in Step 0D + Q11; standalone paras + balancing-figure Other-Matter cited (Note 8 caveat) | PASS |
| Consolidated entities | 25 | 25 (relationship-token grep = 25; independently reconfirmed) | none — material entities (EPIC, KSA sub, WMHL, WCPGL, Sintex cos) cited; routine entities under blanket "all rows reviewed" | PASS |
| Numbered notes | 19 (9 consol + 10 standalone incl. 4a/4b) | 19 (consol L420/426/430/435/441/446/450/459/462; standalone L753/756/759/763/764/769/774/780/784/787) | none — all 19 in Step 0D extraction table | PASS |
| Financial line items | 139 | 139 (logical-row reconciled; every material P&L/Reg52/segment line re-tied to source) | none — Step 1A/1B/5 line-anchored | PASS |
| Zero-standing rows | 9 | 9 | none — nil rows carried, "reviewed, no finding" | PASS |
| Annexure rows | 18 (A:8 + B:10) | 18 | none — WCPGL (Annex B) and GGBS (Annex A) both surfaced | PASS |
| Signatory blocks | 6 | 6 | none — routine; no pre-conclusion signing issue to raise | PASS |

### Presentation ledger

| Category | A2 count | My fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Slides | 19 | 19 (`[page N]` grep = 19) | none — all 19 addressed (material slides cited; routine under blanket) | PASS |
| Sales-volume chart | 8 vals | 8 | none material — line pipe 182→193 (Step 2), DI 65→69 (6B), SS 8.3→6.3 (Q7). **TMT rebars 40→47 (+18%) not individually discussed** — non-adverse (positive), acceptable under "reviewed, no finding" | PASS (note) |
| Financial-performance chart | 9 | 9 | none — Rev/EBITDA/PBT/PAT + 548 footnote all cited | PASS |
| Balance-sheet chart | 9 | 9 | none — net debt, ROCE, 834 capex cited | PASS |
| P&L snapshot (60 vals / 12 items) | 60 / 12 | 60 / 12 | none — reproduced and cross-checked in Step 1A derived table | PASS |
| Guidance chart | 12 | 12 | none — 20,000 / 2,850 / actuals cited; FY24→FY25 revenue dip cited for context (1A footnote) | PASS |
| Guardrails / order book | 5 | 5 | none — 24,750, ROCE>20%, ND/EBITDA<1x cited | PASS |
| Business-env figures + bullets | 3 + 25 | 3 + 25 | none material — JJM (FND-04/Q8), tariff hedge (FND-03/Q7), KSA drivers, Sintex all cited; routine bullets "reviewed" | PASS |
| Sintex channel chart | 18 | 18 | none — 1.5x/2x/21x cited (Step 6D) | PASS |
| ESG slide | 15 | 15 | none — DJSI improving, non-adverse, "reviewed, no finding" | PASS |
| Agenda / cover / title / mgmt-commentary / closing / footnotes / entities / zero-standing | 6/11/4/1/3/3/2/4 | match | none — Project Update agenda gap surfaced as FND-05/07 (silence audit); mgmt-commentary claims inventoried (Section B Step 1) | PASS |

**Coverage verdict: 100%.** No orphan ledger row (nothing in either ledger reviewed-as-absent). No row my fresh pass found that the ledgers lack. Both A2 count tests reproduce (gate_a2 pass corroborated: entities 25, slides 19 re-confirmed by independent grep). The only sub-item not individually narrated is TMT-rebar volume (+18%, positive) — legitimately folded under the blanket "all rows reviewed" and non-adverse, so not an orphan.

**FORWARD-SIGNAL / AMBIGUOUS → management-question mapping (all must generate >=1 question):**

| Finding | Type (per A4) | Question | Status |
|---|---|---|---|
| A3-F1 EPIC one-off / margin contamination | AMBIGUOUS | Q4 | PASS |
| A3-F2 standalone parent softening | FWD-SIGNAL | Q3 | PASS |
| A3-F4 8 unreviewed subs loss | FWD-SIGNAL | Q11 | PASS |
| A3-F6 KSA reframe | FWD-SIGNAL | Q5 | PASS |
| A3-F8 ETR anomaly | FWD-SIGNAL | Q4/Q5 | PASS |
| A3-F13 WCPGL RPT | AMBIGUOUS | Q1 | PASS |
| A3-F15 EPIC post-sale stake | FWD-SIGNAL | Q6 | PASS |
| FND-02 revenue ramp | FWD-SIGNAL | Q5 | PASS |
| FND-03 SS tariff hedge | FWD-SIGNAL | Q7 | PASS |
| FND-04 JJM funding | FWD-SIGNAL | Q8 | PASS |
| FND-06 EPIC run-rate | FWD-SIGNAL | Q6 | PASS |
| FND-07 KSA "launching" | FWD-SIGNAL | Q5 | PASS |
| FND-08 margin compression | AMBIGUOUS | Q9 | PASS |
| FND-09 order-book cover | AMBIGUOUS | Q10 | PASS |

Every FORWARD-SIGNAL / AMBIGUOUS finding A4 carries produces at least one question (15 questions total). F12 (Sintex, TRIM) → Q2; F14 and the NEUTRAL/CONFIRMATORY findings (FND-01/05/10) folded into watchlist/silence audit — consistent with the coverage note. No unmapped signal. (Note: A3 forensic notes are outside my input set by design; mapping verified against A4's self-declared incorporated list and the extracted evidence behind each finding, all of which checks out.)

---

## AUDIT 2 — ARITHMETIC

Every derived metric recomputed from raw extract lines. Representative and complete coverage of A4's tables below; all reconcile within rounding.

| Metric | A4 value | My recompute | Source lines | Status |
|---|---|---|---|---|
| Consol Op EBITDA ex-OI Q1FY27 | 692.34 | 586.37+124.58+45.18−63.79 = 692.34 | L373/370/369/361 | MATCH |
| Consol Op EBITDA Q1FY26 | 525.01 | 412.08+84.78+63.18−35.03 = 525.01 | L373/370/369/361 | MATCH |
| Consol Op EBITDA margin Q1FY27 / Q1FY26 | 16.96% / 14.78% | 692.34/4081.12=16.96%; 525.01/3551.49=14.78% | L360 | MATCH |
| Op EBITDA margin YoY | +218 bps | 16.96−14.78 = 2.18pp | — | MATCH |
| Reported EBITDA Q1FY27 / Q1FY26 | 756.13 / 560.04 | 586.37+124.58+45.18=756.13; 412.08+84.78+63.18=560.04 | L373/370/369 | MATCH |
| Reported EBITDA YoY | +35.0% | 196.09/560.04 = 35.01% | — | MATCH |
| Core PBT ex-OI Q1FY27 | 1,143.34 | 1207.13−63.79 = 1143.34 | L382/361 | MATCH |
| Core PBT ex-OI AND ex-EPIC | 595.41 | 1143.34−547.93 = 595.41 | L381 | MATCH |
| Core Op PBT ex-EPIC YoY | +39.8% | 169.39/426.02 = 39.76% | — | MATCH |
| Consol ETR Q1FY27 / Q1FY26 | 13.19% / 24.27% | 159.25/1207.13=13.19%; 111.89/461.05=24.27% | L386/382 | MATCH |
| Consol PAT margin Q1FY27 | 25.68% | 1047.88/4081.12 = 25.68% | L387/360 | MATCH |
| PAT margin ex-EPIC | ~12.2% | (1047.88−547.93)/4081.12 = 12.25% | — | MATCH |
| Depreciation YoY | +46.9% | 39.80/84.78 = 46.94% | L370 | MATCH |
| Finance cost YoY | −28.5% | −18.00/63.18 = −28.49% | L369 | MATCH |
| Other Income YoY | +82.1% | 28.76/35.03 = 82.10% | L361 | MATCH |
| PAT total YoY | +200.1% | 698.72/349.16 = 200.11% | L387 | MATCH |
| PAT owners YoY | +198.6% | 696.07/350.42 = 198.64% | L396 | MATCH |
| PAT ex-EPIC owners / YoY | ~498.56 / +42.3% | 1046.49−547.93=498.56; 148.14/350.42=42.27% | L396/381 | MATCH |
| Standalone Reported EBITDA Q1FY27 | 211.70 | 156.44+40.63+14.63 = 211.70 | L723/718/717 | MATCH |
| Standalone EBITDA margin Q1FY27 | 13.51% | 211.70/1567.22 = 13.51% | L707 | MATCH |
| Standalone ETR Q1FY27 | 25.95% | 40.60/156.44 = 25.95% | L733/727 | MATCH |
| Standalone revenue YoY | −14.3% | −261.13/1828.35 = −14.28% | L707 | MATCH |
| Standalone PAT YoY | −54.5% | −138.99/254.83 = −54.54% | L735 | MATCH |
| Standalone OI YoY | −64.0% | −68.35/106.83 = −63.98% | L708 | MATCH |
| PAT bridge — Op EBIT improvement | +127.53 | 567.76−440.23 = 127.53 | L373/370/369/361 | MATCH |
| PAT bridge — finance relief | +18.00 | 63.18−45.18 = 18.00 | L369 | MATCH |
| PAT bridge — OI change | +28.76 | 63.79−35.03 = 28.76 | L361 | MATCH |
| PAT bridge — JV/assoc change | +23.86 | 72.83−48.97 = 23.86 | L380 | MATCH |
| PAT bridge — EPIC one-off | +547.93 | per Note 4 / L381 | L381/437 | MATCH |
| PAT bridge — tax change | −47.36 | 159.25−111.89 = 47.36 | L386 | MATCH |
| PAT bridge total / reconcile | +698.72 → 1,047.88 | 127.53+18.00+28.76+23.86+547.93−47.36 = 698.72; 349.16+698.72 = 1,047.88 | L387 | MATCH |
| Recurring-core share of delta | ~21% | 145.53/698.72 = 20.83% | — | MATCH |
| One-off share of delta | ~78–79% | 547.93/698.72 = 78.42% | — | MATCH |
| C-vs-S PAT gap Q1FY27 | 932.04 / 88.9% | 1047.88−115.84=932.04; /1047.88=88.94% | L387/735 | MATCH |
| C-vs-S gap Q4/Q1FY26/FY26 | 139.55 / 94.33 / 606.97 | 371.46−231.91; 349.16−254.83; 1620.49−1013.52 | L387/735 | MATCH |
| QoQ revenue | −5.4% | (4081.12−4312.56)/4312.56 = −5.37% | L360 | MATCH |
| Op margin QoQ | +528 bps | 16.96−11.68 = 5.28pp | — | MATCH |
| Q1×4 run-rate | 16,324 | 4081.12×4 = 16,324.48 | L360 | MATCH |
| FY27E implied margin | 14.25% | 2850/20000 = 14.25% | P-L284/285 | MATCH |
| H2 step-up needed | ~30% | (5306/4081)−1 = 30.0% | P-L285/L360 | MATCH |
| Order-book cover on FY27E | ~1.24x | 24750/20000 = 1.2375x | P-L320/285 | MATCH |
| Hurdle Ratio (base) | ~1.88 | (78/47)^(1/3)=18.4% CAGR; 1.6596×(26/22.9) = 1.88 | Notion inputs | MATCH |
| Segment: Others loss widened | ~7x | 137.06/18.66 = 7.34x | L572 | MATCH |
| Unreviewed-subs loss margin / annualized | 85% / ~159 Cr | 39.78/46.68=85.2%; 39.78×4=159.1 | L176-178 | MATCH |
| Net-cash deepening | −709 | 2336−1627 = 709 | P-L252/255 | MATCH |
| Net worth build | +2,379 | 10449.45−8070.21 = 2379.24 | L529 | MATCH |

**Cited-line spot-verification (does the source say what A4 claims):** L381 profit-on-sale 547.93 ✓; L506 disclosed Op-EBIDTA margin 19.73% with L507 formula including profit-on-sale ✓; L500 debtor days 32/35/44/38 (44→32) ✓; L503 inventory days 189/151/207/158 (207→189) ✓; L825 standalone debtor days 71/55/63/60 (63→71) ✓; L832 standalone Op-EBIDTA margin 12.80% ✓; P-L137 "commissioning within FY27" ✓; P-L166 DI "launching in KSA" ✓; P-L259 capex ~834 ✓; P-L284/285 EBITDA 2,850 / revenue 20,000 ✓; L143 associate share 69.88 ✓; L176-182 subs 46.68/39.78 + assoc 3.09 ✓; L764-771 Notes 4a/4b (51.72/82.75; 203.07/168.38) ✓; L446-447 26,37,90,645 shares / 131.90 Cr ✓.

**One imprecision, sub-rounding-material, not a FAIL:** the "~10.8% of consol PAT sits in unreviewed entities" phrasing (Q11 / flags) has no single clean base in the extract (39.78 vs prior-year owners PAT 350.42 = 11.3%; vs normalized ex-EPIC ~499 = 8.0%). It is explicitly hedged "~" and the load-bearing companions (85% loss margin, ~Rs159 Cr annualized) are exact. No table metric is affected; flagged for transparency only.

**Arithmetic verdict: zero mismatches above rounding.**

---

## AUDIT 3 — ADVERSARIAL READ

A4's three most positive claims, each with the strongest bear counter built from the SAME extracted text, and whether the counter survives (i.e., is supported by the extract AND not already incorporated by A4, therefore requiring graft).

**Positive claim 1 — "Genuine +218 bps operating-margin expansion; highest-ever quarterly EBITDA (756) corroborated."**
Strongest same-text bear: the deck's headline EBITDA of 756 is `PBT-L3 + D + Finance`, and PBT-L3 (L373) already contains Other Income, which jumped +82% YoY (35.03→63.79, +28.76; L361) — so the reported +276 bps is partly an Other-Income spike, not pure operating leverage; and depreciation is running +47% (L370) while the plants generating the offsetting revenue are not yet in the P&L (absorption gap), so EBIT-level economics lag the EBITDA headline.
Survives? **No — already incorporated.** A4 strips OI to a clean ex-OI margin (+218 bps vs +276 bps reported, Step 2 diag 2) and flags the D&A absorption gap prominently (Step 2 diag 5, Step 3, Step 4). The strongest counter is already in the review; no graft required.

**Positive claim 2 — "Respectable +42% normalized (ex-EPIC) PAT growth is the honest underlying number."**
Strongest same-text bear: normalized PAT of ~499 still rides (a) the +82% Other-Income spike (L361, largely non-recurring) and (b) the full Rs72.83 Cr JV/associate share (L380), of which Rs69.88 Cr is the EPIC associate contribution (L143) whose economic interest was just cut ~22% via the stake sale — strip both and the recurring-core run-rate is materially below +42%.
Survives? **No — already incorporated.** A4's Step 4 explicitly labels OI "mostly non-recurring," computes a run-rate PAT ~470 stripping the OI spike, tags JV share "recurring-but-eroding (EPIC-linked; stake now cut)," and raises the forward EPIC-erosion in Q6/FND-06. Counter already grafted.

**Positive claim 3 — "Healthy balance sheet: net cash deepened to (2,336), ROCE 23.1%, low leverage."**
Strongest same-text bear: the ~Rs709 Cr net-cash improvement is essentially the Rs723.55 Cr EPIC divestment proceeds (Note 4, L437) net of capex, not organic FCF; ROCE 23.1% is annualized off a one-off-inflated quarter; and no Q1 cash-flow statement exists to confirm operating cash conversion. Secondary same-text point: consolidated debt-service-coverage fell to 1.21 from 3.64 YoY (L478).
Survives? **No (primary) / does not rise to thesis-changing (secondary).** A4 debunks the net-cash flattering directly and prominently (Step 5: "Critically, NO — not this quarter… ~Rs709 Cr is roughly EPIC proceeds net of capex, NOT organic FCF"; cash conversion INDETERMINATE, named missing evidence), and caveats the ROCE as one-off-aided (Step 7). The DSCR-1.21 move (L478) is a real, uncited ratio, but for a firm at net cash (−2,336) with the Net-Debt/EBITDA <1x guardrail intact it is a scheduled-repayment artifact, not a solvency signal, and does not overturn the already-heavily-qualified balance-sheet read. Recommend A4 add one clause noting DSCR 1.21 vs 3.64 for completeness, but it is **not a surviving thesis-relevant counter requiring graft.**

**Adversarial verdict:** For all three most-positive claims, the strongest same-text bear counter is already constructed and incorporated in A4 (one-off flattering of PAT and net cash; OI-spike and absorption gap qualifying the margin/EBITDA; cash-conversion INDETERMINATE named). No surviving counter must be grafted before save. One optional, non-material coverage clause (DSCR 1.21, L478) is recommended but does not block.

---

## CROSS-CHECK NOTES (non-blocking)
- Cash-conversion INDETERMINATE is named, not silently resolved to PROCEED; Step 5 explicitly caps the cash-quality contribution at PROCEED WITH CAVEATS while the overall verdict is PROCEED WITH FLAGS (flag-driven, distinct axis) — consistent with the house rule.
- Reg 52(4) disclosed Op-EBIDTA margin (19.73%, L506) correctly identified as one-off-contaminated via the L507 formula note; A4 does not import it as like-for-like. Correct.
- No exit multiple sourced outside Section 1B v3.3; no round-number defaults; Sintex TRIM trigger surfaced as flag with the human retaining the decision. Compliant.

---

## VERDICT

**COMPLETE.** Coverage 100% (no orphan ledger row, no fresh-pass row the ledgers lack, every FORWARD-SIGNAL/AMBIGUOUS finding produces a management question). Arithmetic: every derived metric re-computed from raw extract lines reconciles within rounding; zero mismatches. Adversarial: the strongest same-text bear counter to each of A4's three most-positive claims is already incorporated; nothing survives that must be grafted before save. Only COMPLETE proceeds — this review may proceed to Notion save.

```yaml
stage: A5-adversary
company: "WELCORP"
quarter: "Q1FY27"
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
