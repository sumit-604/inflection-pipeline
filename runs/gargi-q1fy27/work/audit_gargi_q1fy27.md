# A5 ADVERSARY / COMPLETENESS AUDIT — GARGI Q1 FY27

Company: PNGS Gargi Fashion Jewellery Ltd (GARGI, BSE 543709) | Quarter: Q1 FY27 (qtr ended 30-Jun-2026)
Auditor: A5 (adversary), Opus 4.8 | Date: 2026-08-01
Under audit: review_gargi_q1fy27.md (A4)
Fresh-context basis: A4 review + A1 extracts (results, presentation) + A2 ledgers only. I re-derived every unit conversion and every derived metric independently; I did not defer to A4's or A3's cites.

**VERDICT: INCOMPLETE.** Two A4 defects found (one arithmetic error, one unsupported over-claim), both propagate into the Notion-bound flags/YAML. Loop back to A4. Detail below.

---

## AUDIT 1 — COVERAGE (independent re-enumeration vs A2 ledgers)

Fresh grep/sweep of each A1 extract, diffed against the two A2 ledgers.

| Category (doc) | A2 count | My fresh count | Orphan rows (in ledger, absent from A4) | Status |
|---|---|---|---|---|
| Results — notes | 9 | 9 (main 1-7 @ L196/200/208/213/216/221/224 + outlook 1-2 @ L243/251) | none | PASS |
| Results — line items | 28 | 28 (table L124-171, data+subtotal rows) | none | PASS |
| Results — zero-standing | 3 | 3 (Exceptional L141, Prev-period tax L148, Other equity L169) | none | PASS |
| Results — agenda items | 1 | 1 (results approval, L18) | none | PASS |
| Results — auditor paras | 4 | 4 (L53/59/67/78; no EOM/Other Matters/GC) | none | PASS |
| Results — consolidation entities | 0 | 0 (standalone only) | none | PASS |
| Results — signatory blocks | 4 | 4 (CS L25-32; auditor L87-99; Gadgil L187-190 & L263-267) | none | PASS |
| Presentation — slides | 33 | 33 (pages 1-33) | none | PASS |
| Presentation — data-unit rows | 221 | 221 (U1-U221 present and continuous) | none | PASS |
| Presentation — numeric content lines | 210 | consistent with ledger deterministic filter | n/a | PASS |

**No orphan rows** (every ledger row is either specifically cited by A4 or covered by A4's blanket "all 33 slides / 221 rows reviewed" + "no ledger row is unreviewed" attestation). **No missing-from-ledger rows** (my fresh pass surfaced nothing the ledgers lack). Both A2 gates independently reproduce.

Note: I cannot re-verify the *content* of A3 finding IDs (FN01-FN21, A3-01..A3-07) because A5 does not see A3 by design. I verified instead that every extract-visible FORWARD/AMBIGUOUS disclosure (guidance U71/U76/U77/U78/U79; forward U25/U26/U127; contradictions res L251-254; RPT/base items U61/U70/U107; reconciliation gaps U96/U208) maps to a management question in Step 8.5 — it does (see Audit 4). One interpretation defect traced to A4's use of FN13 is raised in Audit 2 (Mismatch 2).

---

## AUDIT 2 — ARITHMETIC (recomputed from raw Lakhs / Rs Mn)

Conversions re-derived independently: results Lakhs x0.01 -> Cr; presentation Rs Mn x0.1 -> Cr. I confirmed the deck "EBITDA" is *operating* EBITDA ex-Other-Income (59.7 Mn = Rs 5.97 Cr = A4 op EBITDA), so no Lakh/Mn/Cr or revenue-vs-total-income basis mix-up exists in A4's core P&L.

### 2a. Metrics recomputed and CONFIRMED (sample of the full re-run; all tie to A4 within rounding)

| Metric | A4 value | My recompute | Source | Status |
|---|---|---|---|---|
| Revenue Q1FY27 (Cr) | 30.22 | 3021.62/100 = 30.22 | res L124 | PASS |
| Total Income Q1FY27 (Cr) | 32.10 | 3209.70/100 = 32.10 | res L127 | PASS |
| Op EBITDA Q1FY27 (Cr) | 5.97 | 6.7859+0.7525+0.3128−1.8808 = 5.97 | res L139/134/133/125 | PASS |
| Op EBITDA margin Q1FY27 | 19.76% | 5.9704/30.2162 = 19.76% | derived | PASS |
| Op EBITDA margin Q1FY26 | 23.23% | 6.3454/27.3110 = 23.23% | derived | PASS |
| Op EBITDA margin YoY | −347 bps | 19.76−23.23 = −3.47pp | derived | PASS |
| Reported EBITDA margin Q1FY27 | 25.98% | 7.8512/30.2162 = 25.98% | derived | PASS |
| Core PBT ex-OI Q1FY27 (Cr) | 4.91 | 6.7859−1.8808 = 4.91 | res L143/125 | PASS |
| Core PBT ex-OI YoY | −17.34% | (4.9051−5.9340)/5.9340 = −17.34% | derived | PASS |
| Revenue YoY | +10.64% | 2.9052/27.3110 = +10.64% | res L124 | PASS |
| Total income YoY | +12.56% | 3.5815/28.5155 = +12.56% | res L127 | PASS |
| Depreciation YoY | +175.85% | 0.4797/0.2728 = +175.85% | res L134 | PASS |
| Finance cost YoY | +125.68% | 0.1742/0.1386 = +125.68% | res L133 | PASS |
| Other Income YoY | +56.15% | 0.6763/1.2045 = +56.15% | res L125 | PASS |
| Reported PBT YoY | −4.94% | −0.3526/7.1385 = −4.94% | res L143 | PASS |
| PAT YoY | −4.96% | −0.2636/5.3132 = −4.96% | res L152 | PASS |
| EPS YoY | −6.04% | (4.82−5.13)/5.13 = −6.04% | res L165 | PASS |
| ETR Q1FY27 | 25.59% | 1.7363/6.7859 = 25.59% | res L150/143 | PASS |
| OI/PBT Q1FY27 | 27.72% | 1.8808/6.7859 = 27.72% | derived | PASS |
| PAT margin (rev-ops) Q1FY27 | 16.71% | 5.0496/30.2162 = 16.71% | res L152/124 | PASS |
| PAT margin (total income) | 15.73% | 5.0496/32.0970 = 15.73% | derived | PASS |
| Gross profit Q1FY27 (Cr) | 12.75 | 30.2162−(24.5597−7.0957) = 12.75 | res L124/130/131 | PASS |
| Gross margin Q1FY27 | 42.20% | 12.7522/30.2162 = 42.20% | derived | PASS |
| GM YoY | +154 bps | 42.20−40.66 = +1.54pp | derived | PASS |
| QoQ revenue | +2.13% | 0.6295/29.5867 = +2.13% | res L124 | PASS |
| QoQ op-EBITDA margin | −371 bps | 19.76−23.47 = −3.71pp | derived | PASS |
| PAT bridge (all legs) | ties to −0.26 | GP +1.65 − emp 0.35 − oth 1.67 − D 0.48 − fin 0.17 + OI 0.68 + tax 0.09 = −0.26 | res | PASS |
| CFO/PAT FY26 | 0.352x | 11.03/31.33 = 0.352x | pres U203/U168 | PASS |
| CFO/PAT FY25 | 0.511x | 14.71/28.81 = 0.511x | pres U203/U168 | PASS |
| CFO/PAT FY23 | 0.362x | 1.70/4.69 = 0.362x | pres U203/U168 | PASS |
| Inventory days FY26 | 206.5 | 482.4/852.7×365 = 206.5 | pres U190/U155 | PASS |
| Receivable days FY26 | 33.3 | 136.3/1494.0×365 = 33.3 | pres U191/U154 | PASS |
| Payable days FY26 | 26.8 | 62.5/852.7×365 = 26.8 | pres U179/U155 | PASS |
| CCC FY26 | 213.0 | 33.3+206.5−26.8 = 213.0 | derived | PASS |
| PPE growth FY25->26 | +186% | (5.30−1.85)/1.85 = +186% | pres U184 | PASS |
| **Cash gap FY26 (Mn)** | **718.9** | **727.5 − 8.6 = 718.9 Mn (Rs 71.9 Cr)** | pres U192/U208 | **PASS** (deposits/liquid funds 31.0+77.7 = 108.7 Mn do NOT bridge; flag legitimate) |
| FY26 reported rev growth | +18.2% | 230.5/1263.5 = +18.24% | pres U154 | PASS |
| FY26 ex-one-time growth | ~49% | 490.5/1003.5 = +48.9% | pres U154/U70 | PASS |
| TTM EPS / current PE | 29.74 / 21.3x | 30.05−5.13+4.82 = 29.74; 632/29.74 = 21.3x | res/pres | PASS |
| Pref allotment shares | 1,12,500 | 90,000+22,500; capital 1035.78->1047.03 L = +11.25 L @ Rs10 = 1,12,500 | res L168/L243 | PASS |
| FY23 EPS inconsistency | implied ~Rs4.9 | 46.9 Mn PAT / 9.63 M sh = Rs 4.87 vs deck Rs 10.2 | pres U168/U171/U170 | PASS (flag legitimate) |

Binary-test legs, four Notion REDs, the Rs 718.9 Mn cash gap, all growth rates, and all margin computations reproduce. **All PASS except the two below.**

### 2b. ARITHMETIC MISMATCHES (FAIL — loop to A4)

**MISMATCH 1 — Non-EBO revenue YoY.**
- A4 value: **~−5.3% YoY** (review L228 binary-leg; L271 growth-trigger table; L320 Q3; L440 flag; also YAML flags "non-EBO -5.3%").
- My recompute: **−6.3% YoY.** EBO Q1FY27 = Rs 69 Mn / 6.90 Cr (pres U16); EBO +186% YoY (pres U23) -> EBO Q1FY26 = 69/2.86 = 24.13 Mn / 2.41 Cr. Non-EBO Q1FY27 = 302.2 − 69 = 233.2 Mn / 23.32 Cr; Non-EBO Q1FY26 = 273.1 − 24.13 = 248.97 Mn / 24.90 Cr. YoY = 233.2/248.97 − 1 = **−6.34%**. Even using A4's *own printed operands* (23.32 vs 24.89 Cr, L228) the result is (23.32/24.89 − 1) = **−6.31%**, not −5.3%. A4 appears to have divided the non-EBO decline (1.57) by *total* revenue (~30.2) rather than by prior non-EBO — a wrong denominator for a segment YoY.
- Source lines: review L228/L271/L320/L440; pres U16/U23/U31.
- Materiality: the leg still FAILS the >=stable test either way, so no binary-test verdict flips — but the magnitude is wrong and is carried verbatim into the Notion flags and Q3.

**MISMATCH 2 — Q1FY27 net store additions / "~4 undisclosed closures."**
- A4 value: **"9 gross / 5 net in Q1"** with **"~4 undisclosed closures"** (review L240 checklist item 5 -> AMBER; L270 growth-trigger; L325 Q8; L379 & L445 flag). Attributed to FN13.
- My recompute: **+9 NET.** FY26 POS = 126 (pres U53 slide 12; total series in chart U112); Q1FY27 POS = 135 (pres U85 slide 14). 135 − 126 = **+9 net**. Corroborated: "9 new additions during Q1FY27" (U86) and "Added 32 new POS in FY26" (U102: FY25 94 + 32 = 126). **No closure count appears anywhere in either extract.** The "~4 undisclosed closures / 5 net" has no evidentiary basis in the artifacts; the plain reconciliation is 9 gross = 9 net, 0 evidenced closures.
- Source lines: review L240/L270/L325/L379/L445; pres U53/U85/U86/U102/U112.
- Consequence: checklist item 5 should read **GREEN** (>=5/q) absent any closure evidence, not AMBER; the flag "~4 undisclosed store closures under a parent no-closures halo (FN08/FN13)" is an unsupported over-claim and must be removed or backed with a specific cite. (Q8 itself — asking management to split gross adds vs closures — remains a legitimate disclosure question and can stand, but its premise "9 gross vs 5 net hides closures" must be corrected.) If the ~4-closure figure originates in A3's FN13, A3 must produce the closure cite; otherwise A4 must correct the plain 126->135 = +9 net reading.

---

## AUDIT 3 — ADVERSARIAL READ (three most-positive A4 claims; bear counter from the SAME extract)

A4's review is already bear-leaning, so the "most positive" claims are the few green/pass readings. Each bear counter is drawn only from the extracted text.

**Positive claim 1 — "PAT margin 16.71% = binary-test PASS (>=15%)" and Notion item still >15% floor (review L227/L238).**
Bear counter (survives, partial): the margin is propped by non-recurring Other Income at 27.72% of PBT vs 12.61% FY26 (res L125/L143). Normalising OI to the FY26 run-rate (A4's own Step 4b: ~Rs 0.5 Cr lower PAT) gives PAT ~4.55 Cr and margin ~15.06% — the 15% floor is barely cleared and only because of OI; on total income the margin is already 15.73% and −274 bps YoY. **Graft:** state at the binary leg that the sole passing leg is OI-dependent and one OI reversion from failing.

**Positive claim 2 — Gross margin "expansion +154 bps YoY" (review L104/L161/Step 6E premiumisation).**
Bear counter (survives): the +154 bps is measured off a soft Q1FY26 (40.66%). Sequentially GM fell **−389 bps** (Q4FY26 46.11% -> Q1FY27 42.20%, pres U34) and FY26 full-year GM (42.93%, U157) *exceeds* Q1FY27 (42.20%). So the "expansion" is a low-base artifact, not evidence of realised premiumisation. **Graft:** pair every "+154 bps YoY" mention with the −389 bps QoQ / below-FY26 context.

**Positive claim 3 — Preferential allotment at Rs 970 a "premium to CMP" -> item 14 GREEN + trigger 6 confirmatory-positive "promoter PURCHASE, not sale" (review L249/L262/L447).**
Bear counter (survives): the Rs 970 pref was a *prior-year* (FY26) raise; current CMP is Rs 632 (pres U215), so promoters are ~35% underwater and the raise predates the demand-softening note (res L251-254). Framing a year-old issue price as a "premium to CMP" GREEN inverts the actual signal — today's price is 35% below what insiders paid. **Graft:** re-cast item 14 to note promoters are now ~35% below the pref price; it is not a current-quarter confidence signal.

All three counters are supported by the extract and should be grafted into A4 before save. (These are completeness grafts, not the full Role 3 Devil's Advocate.)

---

## AUDIT 4 — TARGETED CONFIRMATIONS REQUESTED

- **Binary-test scorecard legs (4):** CFO/PAT FAIL (FY26 0.352x, Q1 undisclosed) — confirmed; comparable growth FAIL (+10.64%) — confirmed; PAT margin PASS marginal (16.71%) — confirmed (but OI-dependent, see Audit 3); non-EBO stabilisation FAIL — confirmed *as a fail*, though the stated magnitude is wrong (see Mismatch 1). 3/4 fail pattern stands.
- **Four Notion RED calls (items 1-4):** all arithmetically supported (growth 10.64%<20%; op-EBITDA margin 19.76%<22%; PAT margin 16.71%<18%; CFO/PAT 0.352x<0.50x). Confirmed.
- **Rs 718.9 Mn cash reconciliation gap:** confirmed (727.5 − 8.6 Mn; Financial Assets 31.0 + Other Financial Assets 77.7 do not bridge). HIGH flag legitimate.
- **Growth-rate computation:** +10.64% rev-ops, +12.56% total income — confirmed.
- **PAT/EBITDA margin computations:** all confirmed (see Audit 2a).
- **Every AMBIGUOUS/FORWARD-SIGNAL finding -> a management question:** extract-visible guidance/forward/contradiction/ambiguity items all map to Step 8.5 questions (Q4, Q5, Q6, Q13, Q14, Q16, plus Q1/Q10/Q11/Q15/Q17). Confirmed for all items I can classify from the extract; A3 internal classifications not visible to A5 (design), so this is confirmed to the extent of the artifacts.
- **Role 5 N.A. legitimacy:** confirmed. No concall transcript exists in the artifact set (only results + presentation extracts/ledgers supplied; no transcript ledger; 0 turns). The deck's mention of "investor concalls" (U87) does not create one for this filing. Role 5 N.A. is correct.

---

## VERDICT

**INCOMPLETE.** Loop back to **A4** (Mismatch 2's closure figure may originate in A3/FN13; if so, A3 must supply the closure cite, else A4 corrects it).

Exact gaps to fix before Notion save:
1. **Correct non-EBO YoY from −5.3% to −6.3%** everywhere it appears (review L228, L271, L320, L440, and the YAML flag). Wrong denominator; leg verdict (FAIL) unchanged, magnitude wrong.
2. **Correct the store-adds reading:** the extract supports **+9 net** additions (FY26 126 -> Q1FY27 135, corroborated by "9 new additions" U86 and "+32 in FY26" U102), not "5 net / ~4 undisclosed closures." Downgrade the unsupported closure flag (review L379/L445) unless a specific closure cite is produced; re-rate Notion checklist item 5 to GREEN (>=5/q) absent closure evidence (review L240); fix the growth-trigger row (L270) and the premise of Q8 (L325).
3. **Graft the three surviving bear counters** (Audit 3): OI-dependence of the PAT-margin pass; the −389 bps QoQ / below-FY26 context on the "+154 bps" gross-margin claim; and the promoters-now-~35%-underwater re-cast of the Rs 970 "premium/GREEN" item 14.

Everything else — coverage enumeration, unit conversions, the full P&L/margin/tax/bridge/cash-quality arithmetic, the Rs 718.9 Mn gap, the four REDs, the binary 3/4-fail pattern, and Role 5 N.A. — reproduces cleanly and passes.

```yaml
stage: A5-adversary
company: "GARGI"
quarter: "Q1 FY27"
model: claude-opus-4-8
status: complete
verdict: INCOMPLETE
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches:
  - {metric: "Non-EBO revenue YoY", a4_value: "-5.3%", recomputed: "-6.3%", source_line: "review L228/L271/L320/L440; pres U16/U23/U31"}
  - {metric: "Q1FY27 net store additions / undisclosed closures", a4_value: "5 net / ~4 closures", recomputed: "+9 net, 0 evidenced closures (126->135)", source_line: "review L240/L270/L325/L379/L445; pres U53/U85/U86/U102/U112"}
surviving_bear_counters:
  - {claim: "PAT margin 16.71% = binary PASS (>=15%)", counter: "pass is OI-dependent (OI/PBT 27.72% vs 12.61% FY26); normalised margin ~15.06%, one OI reversion from failing", source_line: "review L227/L238; res L125/L143"}
  - {claim: "Gross margin expansion +154 bps YoY", counter: "-389 bps QoQ (46.11%->42.20%) and below FY26 42.93%; +154 bps is a low-base artifact", source_line: "pres U34/U157"}
  - {claim: "Pref at Rs970 = premium to CMP, item 14 GREEN / promoter purchase confirmatory-positive", counter: "prior-year raise; CMP Rs632 leaves promoters ~35% underwater, predates demand-softening note", source_line: "review L249/L262/L447; pres U215; res L251-254"}
loop_back_to: "A4"
gap: "A4 must (1) correct non-EBO YoY -5.3% -> -6.3% (wrong denominator; review L228/L271/L320/L440); (2) correct '5 net / ~4 undisclosed closures' to +9 net (126->135, pres U85/U86/U102), re-rate Notion item 5 to GREEN absent closure evidence, and remove/substantiate the closure flag (review L240/L270/L325/L379/L445) - if the ~4-closure figure is A3 FN13, A3 must supply the closure cite; (3) graft the three surviving bear counters (OI-dependent PAT-margin pass, -389 bps QoQ gross-margin context, promoters ~35% underwater vs Rs970 pref)."
```
