# FTTCP DELIBERATION RECORD — Entero Healthcare Solutions Ltd (ENTERO)
Signed off 2026-08-30 (operator). Run folder runs/entero-2026-07-27.
Authoritative for Phase 3 per the orchestrator Phase-3 authority rule.

## FINAL RULINGS (as they stand after review)

Setup calls: forward window 3m/6m/12m(ROCE); business type standard operating
distributor; workup REFRESH; sector cap 18-20x (operator-approved, overrides
the manifest "Pharma / CDMO" collector default).

Transition forward verdicts (unchanged from draft after review):
- Revenue FIRING (+2)
- Margin STARTING (+1) — rounded down from FIRING; Q1 FY27 5.0% hit but not
  yet two clean quarters, print contaminated twice.
- Cash STAGNANT (0), determination INDETERMINATE — FCF uncomputable; caps the
  disposition at PROCEED WITH CAVEATS; resolves H1 FY27 (~Nov 2026).
- ROCE RECOVERING (+1) — backward TEMPORARILY DEPRESSED; reverts to DECLINING
  (12x) on new M&A above ~Rs 200 Cr / rolling 12m.
Composite +4 of 8 (DEEP WATCH leaning BUY-ON-DIPS). Kernex cap not engaged;
TRIM not engaged; signal gate satisfied (15 tracker rows written).

## OPERATOR OVERRIDES (each with draft determination, ruling, reasoning)

1. Halt 1 decision.
   - Draft / claude.ai recommendation: SHALLOW WATCH (re-rating priced in;
     price ~45% above the entry zone).
   - Operator ruling: PROCEED with the full pipeline.
   - Operator's words: "Claude AI has told shallow watch, but I want to
     proceed with the full pipeline."
   - Default-track sensitivity: on the conservative track the name is a WATCH,
     not a trade at CMP; the cost of proceeding is running Phase 3 valuation at
     a price ~45% above the FTTCP entry zone.

2. Pillar 1 ROCE base.
   - Two drafts agreed: Claude Code 19x, dossier flagged the ROCE contested
     (21.1% vs ~10.5%). Operator ruled 19x on the forward-capital basis.
   - Operator's words (2026-08-30 ruling): ROCE base 20-25%, ROCE Base
     Multiple 19x; incremental capital is working capital earning 20-25% with
     M&A paused, accumulated goodwill from ~50 deals sunk.
   - Default-track sensitivity: the recorded dissent is 12x (standard EBIT /
     average capital employed incl. goodwill, ~9.9% FY26 / ~14% annualised Q1
     FY27). If Phase 3 were run on 12x instead of 19x, the exit base and every
     fair value fall by roughly a third. Condition on the 19x ruling: reverts
     to 12x if new M&A above ~Rs 200 Cr consideration is announced in any
     rolling 12-month window.

3. Destination PE base and earnings basis (valuation gate, 2026-08-30).
   - Both drafts recommended 18-20x; operator APPROVED 18-20x. No override
     cost (drafts and ruling agree).
   - Earnings basis: operator CHOSE one-year-forward P/E.
   - Operator's words: "take the destination price-to-earnings between 18 and
     20x, and use the forward price-to-earnings."

## FINAL FTTCP VERDICT (in the operator's own words)

"I want to proceed with the full pipeline." Destination PE 18-20x on a
one-year-forward earnings basis. (Mechanical FTTCP composite: +4 of 8, DEEP
WATCH leaning BUY-ON-DIPS, carried into Phase 3 under the operator's PROCEED
override, with the INDETERMINATE cash cap and the price gap as the two live
caveats.)

## CROSS-FAMILY GRADE OUTCOME

Cross-family check DID NOT RUN this session (no provider key configured;
verifiers/fttcp_crossgrade.py exited SKIPPED). Per the skill, FTTCP confidence
is treated one notch lower. No grader divergence to resolve.

## OPERATOR-APPROVED VALUATION PILLARS (authoritative for Phase 3)

Phase 3 / stage 11 MUST use this approved base and basis; it may not silently
derive a different exit PE.

- Pillar 1 (ROCE): base 20-25%, ROCE Base Multiple 19x via the continuous
  formula (Amendment 5/v3.6: 0.5 x ROCE + 7.5). Route: operator forward-capital
  ruling; dissent 12x (standard, goodwill-inclusive) recorded; reverts to 12x
  on new M&A > ~Rs 200 Cr / rolling 12m. ROCE recovery credited via Pillar 1;
  Strategic Premium ROCE re-rating route BARRED (single-credit).
- Pillar 2 (cash multiplier): INDETERMINATE (FCF uncomputable, no consolidated
  capex line). Treated <=1.0x, never a clean pass; caps the disposition at
  PROCEED WITH CAVEATS. Resolves at H1 FY27 (~Nov 2026); Phase 3 carries the
  cap until then.
- Pillar 3 (growth / EM premium): MODEST (EM 19, understated pending a B07
  recheck for master-data + 15% exclusive tie-ups). Growth-premium eligibility
  (Amendment 16) opens on the 20-25% forward ROCE basis. Premiums are capped
  away by the sector cap (see below).
- Strategic premium: none (barred, single-credit).
- Undiscovered Alpha: DOES NOT APPLY. FII+DII ~19.8% at Jun-26 (>3%); the
  institutional-absence qualifier fails.
- Sector cap: 18-20x (operator-approved). No pharma/MedTech distribution row
  exists in Section 1B; this ruling overrides the manifest "Pharma / CDMO"
  default. Absolute ceiling. Amendment 20 Step 1C (live dated peer table:
  Apollo HealthCo/Keimed once listed, MedPlus) runs in Phase 3; where the
  pillar sits >30% below the adjusted peer base the relative multiple governs,
  bounded by this cap.
- DESTINATION (exit) PE, both tracks: 18-20x. Additive track = Pillar 1 19x
  capped at the sector cap. RRM track ~= 19x at r 13.5% (Amendment 4.4),
  lower if r is set higher for risk. Premiums do not lift the exit because the
  cap binds.
- EARNINGS BASIS: ONE-YEAR-FORWARD P/E. Operator's reason: a fast-growing
  distributor is valued on forward earnings, consistent with the entry-zone
  math already built on FY30 forward EPS. Amendment 18 exit-basis symmetry:
  the exit multiple is applied on the same forward basis as the entry.

## PHASE 3 CARRY-FORWARD FLAGS

- SHARED CATALYST: the M&A pause drives both the ROCE recovery (Pillar 1) and
  the margin/MedTech growth story (Pillar 3). Role 3 must stress-test that
  single lever.
- Verify manifest.yaml sector_cap_row before stage 11 (auto-populates
  incorrectly); use the 18-20x operator ruling.
- ROCE denominator dissent (12x) and its M&A reversion condition must appear
  in the Role 1 worksheet and the devil's advocate.
- Operating EPS (Module B4) must strip the FY26 exceptional item and the NCI
  put/call fair value that ran through equity; single-segment disclosure means
  Phase 3 computes it from the results PDFs.
