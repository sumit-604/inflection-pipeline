# A5 ADVERSARY / COMPLETENESS AUDIT — MTAR Technologies Limited (MTAR) — Q1 FY27

**Agent:** A5 ADVERSARY. Fresh context: this audit was derived only from the A1 extract, the A2 ledger, and the A4 review. A3's reasoning was not consulted; every cite below was re-derived independently against the raw extract.
**Unit convention re-verified:** A1 header line 7-8 = INR Millions; Rs Cr = Millions x 0.1. Applied throughout. Pages 5-6 decimal-glyph artifact handled per A1 verification notes (extract lines 15-72) — VERIFIED values used.

---

## AUDIT 1 — COVERAGE

Fresh independent enumeration (my own grep + manual sweep over the extract) vs the A2 ledger counts.

| Category | A2 count | My fresh count | Method / evidence | Orphan rows | Status |
|---|---|---|---|---|---|
| notes | 11 | 11 | 5 standalone (L359-369) + 6 consolidated (L429-441); standalone leading digits dropped by renderer, structure-matched 1:1 to consol notes and to in-table anchors "(refer note 2)" L320 / "Refer note 5" L338 | none | PASS |
| line_items | 68 | 68 | Standalone table L321-355 = 34 (35 rows minus the 2-line EPS caption wrap L352-353); consolidated L392-425 = 34. 34+34=68 | none | PASS |
| zero_standing | 8 | 8 | Standalone L338/342/347/348; consolidated L409/413/418/419 (exceptional nil, prior-period tax-adj nil, OCI nil, total-OCI nil in the Q columns) | none | PASS |
| agenda_items | 7 | 7 | Grep `^\s*[0-9]+\.` on L104-121 returns exactly items 1-7 (L105/107/109/111/113/117/119) | none | PASS |
| auditor_paras | 26 | 26 | Standalone report 10 structural blocks (L459-547); consolidated 16 blocks (L557-692) incl. 2 enumerated pagination/letterhead artifacts (blocks 11-12). 10+16=26 | none | PASS |
| entities | 3 | 3 | Grep for the two subsidiary names + holding: MTAR + Gee Pee Aerospace + Magnatar Aero Systems (L429-430, auditor list L617-618) | none | PASS |
| annexure_profiles | 2 | 2 | Rohith Loka Reddy + Anushman Reddy (Annexure A L210; matches agenda items 3-4) | none | PASS |
| signature_blocks | 4 | 4 | Grep `Digitally signed by` = 2 (Priyanka Agarwal L150, L279) + `For S.R. Batliboi/BATLIBOI` firm sign-offs = 2 (L527, L679) | none | PASS |

**Ledger-row -> A4-review reconciliation (orphan check).** Every A2 category is cited or reviewed in A4:
- notes -> A4 Step 0D notes table (all 6 subjects) + glyph-numbering note. Cited.
- line_items -> A4 Step 1 data tables 1A/1B (every row line-anchored). Cited.
- zero_standing -> exceptional + prior-period tax-adj carried as F8-a (A4 L43); OCI nil rows reviewed, no finding. Reviewed.
- agenda_items -> A4 Monitorables table cites agenda 3,4,5,6,7 (L390-394); items 1-2 are the filing itself. Cited.
- auditor_paras -> A4 Step 0D auditor-opinion review (UNMODIFIED, both statements) + Step 5X subsidiary Other-Matters disclosure. Cited.
- entities -> A4 Step 5X + F6-a NCLT merger discussion. Cited.
- annexure_profiles -> A4 Q6 (two re-appointees as related parties to MD / WTD). Cited.
- signature_blocks -> A4 F14-a (membership 4777 vs 504777) + F14-b (consolidated UDIN absence), Q7. Cited. The A2 `SIGNATURE_ILLEGIBLE` flag is an immaterial wet-signature text-layer rendering (correctly generates no verdict action; consistent with A4's F14-c claimed-incorporated). Reviewed, no material finding.

**Cross-check of A2's own method claims against the raw extract:** the decimal-glyph second-sweep (A2 §method, "no additional cells beyond A1's six") independently re-confirmed — I re-scanned L310-425 and found only the six A1-flagged cells (171,36 / 48,29 / 3:52 / 26,94 / 16,33 / 352). The signature-timing check (DSC 16:34:40 after 15:35 meeting close) also holds.

**COVERAGE RESULT: PASS.** All 8 categories match my fresh counts. No orphan rows (nothing in the ledger absent from A4). No rows my fresh pass found that the ledger lacks. No loop-back to A2 or A3.

---

## AUDIT 2 — ARITHMETIC

Every derived metric in A4's tables recomputed from raw millions (not from A4's rounded Cr, to catch propagation). Spot table of the load-bearing metrics; all others tested and tie.

| Metric | A4 value | My recompute (from raw M) | Source line | Status |
|---|---|---|---|---|
| Revenue YoY (std/consol) | +130.4% | 3607.21/1565.84 - 1 = +130.37% | L325 / L396 | PASS |
| Op EBITDA std Q1FY27 (PBT+D&A+FC-OI) | 84.93 | 676.40+94.76+158.47-80.36 = 929.27M -> 84.93 | L339/333/332/326 | PASS |
| Op EBITDA margin std Q1FY27 | 23.54% | 84.93/360.72 = 23.545% | derived / L325 | PASS |
| Op EBITDA margin consol Q1FY27 | 23.58% | 85.05/360.72 = 23.577% | L410/404/403/397 | PASS |
| Op EBITDA std Q1FY26 | 28.45 | 151.97+81.94+58.16-7.59 = 284.48M -> 28.45 | L336/333/332/326 | PASS |
| Op EBITDA margin YoY bps (std) | +537 bps | 23.545% - 18.169% = 5.376pp | derived | PASS |
| Effective tax rate std Q1FY27 | 25.33% | 171.36/676.40 = 25.33% (VERIFIED 171.36, A1 L30) | L344 | PASS |
| Core PBT ex-OI std YoY | +312.7% | raw 596.04/144.38 - 1 = +312.8% (rounded-Cr 59.60/14.44 = +312.7%) | derived | PASS (rounding) |
| Reported PAT std YoY | +349.7% | raw 505.04/112.29 - 1 = +349.8% (rounded-Cr 50.50/11.23 = +349.7%) | L345 | PASS (rounding) |
| Revenue QoQ std | +17.9% | 3607.21/3060.30 - 1 = +17.87% | L325 | PASS |
| PAT bridge sum (std, Q1FY26->Q1FY27) | +39.27 | 37.10+19.37-1.28-10.03+7.28-13.17 = +39.27 | Step 4 | PASS |
| — volume (dRev x prior margin) | +37.10 | 204.14 x 18.169% = 37.09 | derived | PASS (rounding) |
| — margin (+5.37pp x cur rev) | +19.37 | 0.05376 x 360.72 = 19.39 | derived | PASS (rounding) |
| — tax change | -13.17 | 39.68-171.36 = -131.68M -> -13.17 | L344 | PASS |
| S-vs-C PAT gap Q1FY26 | 3.70% | (112.29-108.13)/112.29 = 3.70% | L345/L416 | PASS |
| S-vs-C PAT gap Q4FY26 | 0.12% | (443.37-442.83)/443.37 = 0.12% | L345/L416 | PASS |
| S-vs-C PAT gap Q1FY27 | 0.55% | (505.04-502.27)/505.04 = 0.55% | L345/L416 | PASS |
| S-vs-C PAT gap FY26 | 1.36% | (953.24-940.30)/953.24 = 1.36% | L345/L416 | PASS |
| Gap compression YoY | 3.15pp | 3.70% - 0.55% = 3.15pp | derived | PASS |
| Subs net loss / consol PAT | 1.44% | 7.22/502.27 = 1.44% | L642/L416 | PASS |
| Subs revenue / consol revenue | 0.47% | 16.79/3607.21 = 0.47% | L641/L396 | PASS |
| Net worth std FY26 | 825.68 | 794.92 + 30.76 = 825.68 | L351+L350 | PASS |
| Net worth consol FY26 | 822.59 | 791.83 + 30.76 = 822.59 | L422+L421 | PASS |
| FY26 Op EBITDA incl labour add-back (std) | 171.06 (19.52%) | 167.29+3.77 = 171.06; /876.11 = 19.52% | derived / L338 | PASS |

I additionally re-ticked every remaining cell of A4 Step 1 (1A/1B, ~40 line items x 4 periods each), all of 1C's derived rows (reported EBITDA, OI/PBT, PAT margin for both statements and all four periods), and the full 2A/2B YoY grids. **All tie to the raw extract within rounding.**

**Rounding note (not a FAIL).** A4 computed its YoY percentages by dividing 2-decimal Rs Cr values rather than raw millions. This produces systematic sub-0.2pp deltas versus a raw recompute (e.g. PAT YoY raw 349.8% vs A4 349.7%; core-PBT YoY raw 312.8% vs A4 312.7%; consol PBT YoY raw 355.0% vs A4 355.2%). The single largest is Other-Income-consol YoY: A4 +1193.4% vs raw +1193.0% (0.4pp), an artifact of a 6.10M -> 0.61 Cr denominator rounding on a figure A4 itself flags as "tiny base." Every delta is a rounding-propagation artifact, none is an arithmetic error, none crosses a decision threshold. **No mismatch above rounding was found.**

**ARITHMETIC RESULT: PASS.** No loop-back to A4 on arithmetic.

---

## AUDIT 3 — ADVERSARIAL READ

The three most positive claims in A4, each attacked with the strongest bear counter buildable from the SAME extracted text, then tested for survival and for whether A4 already carries it.

**Claim 1 — "Revenue +130.4% YoY, ahead of the 50% FY27 guide; operations running ahead of guidance."** (Verdict L131, Step 8A-W.)
- *Strongest same-text bear:* The +130.4% is measured off Q1 FY26 = Rs 156.58 Cr, the single weakest quarter of FY26 (FY26 quarterly average = 876.11/4 = Rs 219 Cr, extract L325/L323). Comparing the current quarter to the prior-year seasonal trough mechanically inflates the percentage; the annualisation to "+64.7%" also rests on that soft base. The mitigating "sequential read is the sterner test" leans on Q4 FY26 (Rs 306.03 Cr) which is itself a **balancing figure** (note 2, L363-364) — a derived plug, not an independently reported number — so the reassurance uses one caveated base to offset another.
- *Survives?* Yes, supported by extract. **Already grafted in A4:** soft-base caveat stated verbatim (Step 2C diag 1, L161: "base-flattered"); balancing-figure caution stated (Step 3 one-off row L181, L186). No new graft required.

**Claim 2 — "Core operating PBT +312.7% YoY; ~86% of the PBT gain is core, only ~14% Other Income — the headline is real, not a treasury artifact."** (L163, Step 4.)
- *Strongest same-text bear:* Finance costs jumped +172.5% YoY (58.16M -> 158.47M, L332), outpacing revenue +130.4%, on an undisclosed debt base (no balance sheet in a Q1 filing). If the "recurring core" gain is capex-debt-funded, the interest line keeps rising into FY27-28 and erodes the very margin being celebrated. Separately, strip Other Income back to the prior Rs 0.76 Cr and A4's own run-rate PAT falls to Rs 45.07 Cr (not 50.50), i.e. ~11% of the reported beat is treasury.
- *Survives?* Yes. **Already grafted in A4:** finance-cost outpacing flagged as a Question for Management and as a named flag (Step 2 diag 5 L165; Step 4 L212; flag FINANCE_COST_OUTPACING_REVENUE); OI strip-out to Rs 45.07 Cr shown (Step 2C diag 6 L166; Step 4 L211). No new graft required.

**Claim 3 — "Operating EBITDA margin +537 bps YoY to 23.54%, ahead of the FY28 >24% glidepath; GREEN on the sustain-Q3FY26 monitorable."** (L110, L162, Step 6B #4.)
- *Strongest same-text bear:* The +537 bps is a trough-to-current comparison (Q1 FY26 18.17%, the low-absorption soft quarter). Against the fuller FY26 average (19.10%, L110) the lift is +444 bps, and the clean sequential is +342 bps QoQ off the Q4 FY26 **balancing figure**. The "GREEN — sustains Q3 FY26 ~23%" rests on a Q3 FY26 number that is NOT in this filing (Notion, unanchored) and on the possibility the Notion ~23% used a different margin definition than A4's Op-EBITDA basis.
- *Survives?* Yes on the trough-comparison and QoQ points; the Q3-definition point is a Notion issue outside the extract. **Already grafted in A4:** QoQ +342 bps and the balancing-figure caution are shown (Step 3 L185-186); the Q3 FY26 ~23% is explicitly labelled "Notion, unanchored" and italicised (Step 3 L180, L187). No new graft required.

**ADVERSARIAL RESULT: PASS.** All three most-positive claims already carry their strongest same-extract bear counter within A4 (the review is symmetric bull-bear). No surviving bear counter is unincorporated; no loop-back to A4.

---

## VERDICT

**COMPLETE.** Coverage PASS (8/8 categories reconcile to a fresh independent enumeration; no orphan rows; every ledger row cited or reviewed in A4). Arithmetic PASS (every derived metric recomputed from raw INR-millions ties within rounding; the flagged pages 5-6 glyph cells verified against A1's VERIFIED values; no mismatch above rounding). Adversarial PASS (the three most-positive claims each already carry their strongest same-text bear counter). No loop-back to A2, A3, or A4. Proceeds to Notion save.

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
