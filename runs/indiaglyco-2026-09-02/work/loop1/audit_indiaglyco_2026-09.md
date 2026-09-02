# A5 ADVERSARY AUDIT — India Glycols Limited (INDIAGLYCO) | 2026-09
## LOOP-1 RE-AUDIT (over corrected A4 review)

Inputs read: A4 corrected review (loop1), A1 fulltexts + structured (corp
R001-R291, spirits R001-R355, eb R001-R152), A2 ledgers (corp/spirits/eb).
Source PDFs and inputs/ NOT opened. Re-derived independently.

Scope per task: verify the one loop-1 FACTUAL fix landed correctly, confirm the
two STYLE items were logged, then re-run the four audits fresh. Previously-PASS
content re-confirmed briefly, not re-litigated.

---

## FIX VERIFICATION (loop-1 FACTUAL: realisation per case, 10x error)

Raw extract (spirits structured):
- Potable Spirits Net Rev (INR Cr): R126=947 (FY24), R127=1,176 (FY25), R128=1,331 (FY26).
- Potable Spirits cases (Mn): R110=25.0 (FY24), R111=30.1 (FY25), R112=30.0 (FY26).

Recompute (Rs 1 Cr = Rs 10,000,000; cases in millions):
- FY24: 947 Cr / 25.0 mn = 9,470,000,000 / 25,000,000 = Rs 378.8 -> ~379. MATCH.
- FY25: 1,176 Cr / 30.1 mn = 11,760,000,000 / 30,100,000 = Rs 390.7 -> ~391. MATCH.
- FY26: 1,331 Cr / 30.0 mn = 13,310,000,000 / 30,000,000 = Rs 443.7 -> ~444. MATCH.

Restated values Rs ~379 / 391 / 444 at Step 2.5 (lines 166-168) are correct. The
prior Rs ~3,788 / 3,907 / 4,437 was exactly 10x, a Cr-to-rupee conversion error;
it now survives only inside the labelled correction note (lines 30, 169-176),
which is intended.

+14% read preserved: (444 - 391) / 391 = 13.6% -> ~14% on flat volume
(30.1 -> 30.0). MATCH. The fix propagated to the brief: Step 11.1 (line 518)
and business-model brief (line 553) both now read "Rs 444 per case, up ~14%",
no 10x remnant. Downstream conclusions (regulated-pricing vs premiumisation,
Q13, thesis variable B) hold; growth rate is scale-invariant. FIX LANDED,
CORRECT.

## STYLE ITEMS LOGGED (confirm)

1. India Glycols p12 Net Rev: R056=1,163 Cr (p12) vs R026=1,164 (p7) vs
   R139=1,164 (p31). Logged inline at Step 2.3 note (lines 114-117). Entity A
   analysis uses 1,164. CONFIRMED LOGGED.
2. Clariant JV ownership order: 51:49 split (spirits R133 context / corp) read
   as Clariant 51 / IGL 49; IGL takes 49% x 95 = ~46.5 Cr. Logged inline at
   Step 4.1 (lines 240). CONFIRMED LOGGED.
Both are STYLE, no number changed, no loop.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate)

Plain-language brief at Step 11 (lines 492-572), all four parts present and non-empty:
- (1) SUMMARY NARRATIVE — present (lines 494-529), ~30 lines, real content.
- (2) SECTOR INTELLIGENCE — present (lines 531-543).
- (3) BUSINESS-MODEL INTELLIGENCE — present (lines 545-558).
- (4) COMPETITION INTELLIGENCE — present (lines 560-572).
GATE: PASS.

---

## AUDIT 1 — COVERAGE (fresh enumeration vs A2 ledgers)

| Deck | Category | A2 count | Fresh count | Orphans | Status |
|---|---|---|---|---|---|
| corp | numbers | 146 | 146 (R001-R146) | 0 | PASS |
| corp | entities | 73 | 73 | 0 | PASS |
| corp | forward | 26 | 26 | 0 | PASS |
| corp | dates | 27 | 27 | 0 | PASS |
| corp | footnotes | 19 | 19 (R273-R291) | 0 | PASS |
| corp | TOTAL | 291 | 291 | 0 | PASS |
| spirits | numbers | 159 | 159 (R001-R159) | 0 | PASS |
| spirits | entities | 84 | 84 | 0 | PASS |
| spirits | forward | 42 | 42 | 0 | PASS |
| spirits | dates | 50 | 50 | 0 | PASS |
| spirits | qualifiers | 20 | 20 (R336-R355) | 0 | PASS |
| spirits | TOTAL | 355 | 355 | 0 | PASS |
| eb | numbers | 52 | 52 | 0 | PASS |
| eb | entities | 53 | 53 | 0 | PASS |
| eb | forward | 26 | 26 | 0 | PASS |
| eb | dates | 10 | 10 | 0 | PASS |
| eb | footnotes | 11 | 11 | 0 | PASS |
| eb | TOTAL | 152 | 152 | 0 | PASS |
| ALL | disclosure units | 798 | 798 | 0 | PASS |

Every ledger reports orphan_ids empty; A4 Step 1 reconciles 291 + 355 + 152 =
798, all reviewed, all A3 findings incorporated (corp A1-A7, spirits FND-01..08,
eb F6/F14/F16 set). No orphan row absent from A4; no fresh-pass unit missing from
a ledger. COVERAGE: PASS. (Re-confirmed, not re-litigated per task.)

---

## AUDIT 2 — ARITHMETIC (recompute from raw extract)

| Metric | A4 value | Recomputed | Source | Status |
|---|---|---|---|---|
| Realisation/case FY24 | ~379 | 947 Cr / 25.0 mn = 378.8 | R126/R110 | PASS |
| Realisation/case FY25 | ~391 | 1,176 / 30.1 = 390.7 | R127/R111 | PASS |
| Realisation/case FY26 | ~444 | 1,331 / 30.0 = 443.7 | R128/R112 | PASS |
| Realisation +% FY25->26 | ~14% | 53/391 = 13.6% | R127/R128 | PASS |
| Adj-vs-unadj EBITDA gap FY24 | 108 | 247 - 139 | R140/R032 | PASS |
| Adj-vs-unadj EBITDA gap FY25 | 182 | 312 - 130 | R141/R035 | PASS |
| Adj-vs-unadj EBITDA gap FY26 | 161 | 330 - 169 | R142/R038 | PASS |
| JV 49% share | ~46.5 | 0.49 x 95 = 46.55 | R136 | PASS |
| Residual add-back (49% basis) | 114 | 330 - (169+46.5) = 114.5 | R142/R038/R136 | PASS |
| Residual add-back (full-PAT basis) | 66 | 330 - (169+95) = 66 | R142/R038/R136 | PASS |
| Segment build gap | ~94 | 1,164 - (546+474+50=1,070) = 94 | R139/R063-65 | PASS |
| Entity B net-debt trend | 728/900/767 | R145/R146/R147 verbatim | R145-147 | PASS |
| Net-debt-to-cash-profit FY26 | ~1.9x | 767 / 395 = 1.94 | R147/R150 | PASS |
| Residual core rev decline | -26% | (1,164-1,581)/1,581 = -26.4% | R139/R137 | PASS |

All derived metrics reconcile within rounding. ARITHMETIC: PASS.

Transposition re-confirm: p7 IGL Spirits FY26 rev R025=246 / EBITDA R037=29;
p7 Ennature FY26 rev R027=2,801 / EBITDA R039=492. p12 IGL Spirits R053=2,801,
Ennature R059=247. Spirits standalone R125=2,801 / R135=492; EB standalone
R049=246 / R051=29. Standalone decks settle it: p7 columns are transposed. A4
Step 4.2 correct. PASS.

---

## AUDIT 3 — ADVERSARIAL READ (three most positive claims)

1. Claim: "IGL Spirits net debt fell to Rs 767 Cr, below the ~Rs 1,050 Cr
   trigger" (Step 6.1). Bear counter: net debt (R355) = Term Loan + Fund-Based
   WC minus Cash; it EXCLUDES non-fund-based LC/BG, and net worth is undisclosed,
   and the figure is a pre-demerger carve-out, not the filed opening BS (due
   Oct-Nov 2026). Counter SURVIVES but is already grafted (Step 5, Step 6.1
   caveat). No new graft needed.
2. Claim: "RoCE 20.5%, improving 13.0 -> 17.9 -> 20.5%" (Step 2.5). Bear
   counter: RoCE denominator (Net Worth + Term Loan, R355) cannot be tied out
   because net worth is undisclosed. Counter SURVIVES, already in A4 (Step 5,
   Q10). No new graft.
3. Claim: "Residual India Glycols Rs 330 Cr Adj. EBITDA, 28.4% margin, strong
   earnings profile" (Step 4.1/brief). Bear counter: rests on 66-114 Cr of
   unexplained add-backs beyond the single-line JV footnote, on a core top line
   that fell 26%. Counter SURVIVES, already grafted (Step 4.1, Flag-1). No new graft.

ACQUISITION-ECONOMICS PROBE: these decks describe a three-way DEMERGER (a
corporate split), not a purchase. The one acquisition mentioned, "Prestige
Green Classic Whisky, legacy Karnataka brand acquired by IGL" (spirits R226),
carries NO consideration and NO target PAT, so a price/PAT multiple is not
computable from the extract. The Clariant 24% is a future STAKE SALE, not a buy.
No cheap-accretive-acquisition claim exists to stress-test. Logged; no finding.

All three surviving bear counters were already incorporated by A4 in the
corrected pass. No un-grafted survivor remains. ADVERSARIAL: PASS.

---

## FINDINGS

- FACTUAL: none open. The loop-1 realisation-per-case fix is verified landed and
  correct (Rs ~379/391/444; +14% preserved).
- MISSING: none.
- CONTRADICTION: none.
- STYLE (logged, no loop): (1) p12 Net Rev 1,163 vs 1,164 p7/p31 source rounding,
  logged Step 2.3; (2) Clariant 51:49 ownership-order assumption, logged Step 4.1.

---

## VERDICT

COMPLETE. The one loop-1 FACTUAL finding is corrected and verified against the
raw extract; the +14% FY25->FY26 realisation read is preserved and propagated to
the brief. Two STYLE items are logged. Coverage 798/798 with zero orphans,
arithmetic reconciles within rounding, all three surviving bear counters already
grafted, no acquisition purchase to probe. No FACTUAL, MISSING, or CONTRADICTION
finding remains. Proceeds to Notion save.

```yaml
stage: A5-adversary
company: "INDIAGLYCO"
quarter: "2026-09"
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
surviving_bear_counters:
  - {claim: "IGL Spirits net debt 767 below 1,050 trigger", counter: "narrow def excludes LC/BG, net worth undisclosed, carve-out not filed opening BS", source_line: "R147/R355; review Step 5", type: STYLE}
  - {claim: "RoCE 20.5% improving", counter: "denominator net worth undisclosed, cannot tie out", source_line: "R153/R355; review Step 5/Q10", type: STYLE}
  - {claim: "Adj. EBITDA 330 / 28.4% strong earnings", counter: "66-114 Cr add-backs unexplained, core rev fell 26%", source_line: "R142/R038/R136; review Step 4.1", type: STYLE}
findings_by_type:
  factual: []
  missing: []
  contradiction: []
  style:
    - "p12 India Glycols Net Rev 1,163 (R056) vs 1,164 p7/p31 (R026/R139): source rounding, logged Step 2.3"
    - "Clariant 51:49 read as Clariant 51 / IGL 49 for the 49% x 95 = 46.5 Cr JV share, assumption stated Step 4.1"
loop_back_to: ""
gap: ""
style_notes:
  - "p12 Net Rev 1,163 vs 1,164 (R056 vs R026/R139): 1 Cr source rounding, no data conflict; logged Step 2.3"
  - "Clariant JV ownership-order assumption (51 Clariant / 49 IGL) stated inline at Step 4.1; ~46.5 Cr unchanged"
analyst_note: "Re-audit of loop-1 fix. FACTUAL realisation/case verified: 947/25.0=379, 1,176/30.1=391, 1,331/30.0=444; the 10x Cr-to-rupee error survives only in the labelled correction note. +14% (391->444=13.6%) preserved and propagated to Step 11 brief and business-model brief; no 3,788/4,437 remnant. Three carried-forward items re-confirmed against raw extract: corp Adj-vs-unadj EBITDA gaps 108/182/161 with 66-114 Cr unreconciled by the single JV footnote (95 Cr PAT, 49%=46.5); p7 IGL Spirits/Ennature transposition settled by both standalone decks (2,801/492 vs 246/29); Entity B net-debt 728/900/767. Coverage 798/798, zero orphans across all three ledgers. Three positive claims all already carry their surviving bear counter. Demerger, not a purchase, so no acquisition multiple to probe; Prestige-brand buy has no consideration disclosed. Verdict COMPLETE."
```
