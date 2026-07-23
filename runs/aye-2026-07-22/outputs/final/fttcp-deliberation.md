# FTTCP Deliberation Record: Aye Finance Limited (AYE)

Company: Aye Finance Limited. Ticker: AYE. Run date: 2026-07-22. Mode: first workup, lender transition set. CMP not provided in the run inputs (manifest cmp 0.0); entry zone and Hurdle Ratio are a Phase 3 job once price is sourced.

This record is authoritative for Phase 3. The OPERATOR-APPROVED VALUATION PILLARS block at the end is mandatory for /finalize and fixes the exit multiple base and earnings basis the valuation must use.

## Final rulings (draft rulings as they stand after review)

- Forward window: 3 months primary, 6 months secondary, 12 months for RoA and RoE. Unchanged.
- Business type: lender. Lender Transition Set applied. Unchanged.
- Workup intent: first workup. Role 1 derived fields N/A. Unchanged.
- Sector cap row: corrected from the manifest's "Pharma / CDMO" to Banks / NBFCs / MFIs, 18x, P/B primary and PE cross-check only (Section 1B Amendments 7 and 8). Unchanged, carried to Phase 3.
- AUM growth transition: forward FIRING (+2). Unchanged.
- NIM and spread transition: forward STAGNANT (0), management guides NIM down on a deliberate secured mix shift. Unchanged.
- Asset quality transition (the critical one): forward STARTING (+1). Unchanged as a transition verdict. Note: the valuation-pillar asset-quality multiplier is a separate object and was moved by the operator (see overrides).
- RoA and RoE transition: backward TEMPORARILY DEPRESSED, forward RECOVERING (+1). Unchanged.
- Cash determination: STRUCTURAL for the lender CFO signal, with a residual INDETERMINATE element on earnings quality (gain on derecognition rising to 3.65% of income). Unchanged; keeps the Phase 1 gate at PROCEED WITH CAVEATS.
- Pillar 1 normalization route: Route A governs (post IPO excess capital denominator fix); Route B condition present but suppressed per the single credit rule. Unchanged.
- Composite: +4 out of 8, DEEP WATCH leaning BUY-ON-DIPS. No Kernex cap, no TRIM. Unchanged; not contested by the operator.
- Tier: A, 25% hurdle. Unchanged.
- Undiscovered Alpha: not applied (FII+DII about 35%). Unchanged.

## Operator overrides

**Override 1: destination (exit) PE base.**
- Draft determination: provisional destination PE roughly 11x to 14x on conservative inputs, up to about 17x on the operational RoE anchor plus a 1.00x asset-quality multiplier, all under the 18x cap; the mechanical RRM track sat lower at roughly 10x to 11.5x and could govern on divergence. The draft left the asset-quality multiplier at a conservative 0.80x (GNPA above 4%) with 1.00x named as the live alternative.
- Operator ruling: destination price to earnings of 15x by FY29.
- Operator's reasoning, in the operator's words: "we can take a destination price turning of 15 by FY29."
- How it reconciles to the pillars (so the exit PE stays pillar derived, not a round number default): 15x is within the 18x Banks/NBFCs/MFIs sector cap and within the pillar derived additive band (about 12.7x to 17x). It corresponds to the Sound asset-quality multiplier at 1.00x (up from the drafted 0.80x) times a Pillar 1 RoE base near current (about 13.4x on RoE about 11.7%) plus Pillar 3 at +2x, which lands about 15.4x. The operator's 15x therefore rules the asset-quality multiplier up to 1.00x. That is defensible: GNPA at 4.49% is only marginally above 4% and has fallen for four quarters, PCR at 63.8% sits in the 60 to 70 Sound band, and the ECL cushion is 3.4 times the RBI floor.
- Phase 3 note: on the mechanical dual track the RRM track would pull below 15x; stage 11 must show the divergence, but the operator approved base of 15x governs per the valuation approval gate.

**Override 2: earnings basis.**
- Draft determination: left to the operator; the draft noted forward looked the better fit for a lender mid recovery because trailing EPS is depressed by the credit cost trough.
- Operator ruling: forward P/E, the forward price to earnings model, applied to forward EPS.
- Operator's reasoning, in the operator's words: "since the growth is strong, we can use the forward price turning model."

## Final FTTCP verdict in the operator's words

The operator did not give a verbatim one line verdict. The operator accepted the +4 DEEP WATCH leaning BUY-ON-DIPS composite by not contesting it and moving directly to approve the valuation base, and ruled the destination PE at 15x by FY29 on a forward earnings basis "since the growth is strong." This gap is recorded, consistent with the SFL, AURUM, MAPMYINDIA and VOEPL precedent where the operator signed off through explicit rulings rather than a dictated one line verdict.

## Cross-family grade outcome

The cross-family FTTCP grader did not run this session: no Gemini or GPT provider key was configured (verifiers/fttcp_crossgrade.py exited SKIPPED). Per protocol, FTTCP confidence is treated as one notch lower, on top of the reduction already applied for the single collected concall (Q3 FY26 maiden; the Q4 FY26 and Q1 FY27 calls were not collected and reach the analysis only through the non-anchored operator digest). There was no grader divergence to resolve because no grade was produced.

## OPERATOR-APPROVED VALUATION PILLARS (authoritative for Phase 3)

Phase 3 stage 11 MUST use this approved base and basis; it may not silently derive a different exit PE.

- Business type: lender (NBFC, MSME / micro-enterprise). P/B is the primary method; the destination PE is the secondary cross-check (Section 1B Amendment 7).
- Pillar 1 (ROE, not ROCE): normalization route A governs (operational RoE, post IPO excess capital stripped from the base); Route B pre-depression anchor condition also present but suppressed per the single credit rule. RoE recovery credited via Pillar 1; the Strategic Premium ROE re-rating route is barred. Finalize the RoE anchor so the pillars reproduce the approved 15x destination: near current RoE about 11.7% to 13% with the approved 1.00x asset-quality multiplier reaches 15x; do not double count by also lifting the RoE anchor to operational 15% while holding 1.00x, which would overshoot 15x.
- Pillar 2 (lender Asset-Quality Multiplier): 1.00x (Sound), operator approved via the 15x destination, overriding the drafted 0.80x. Basis: GNPA 4.49% marginally above 4% but falling four quarters, PCR 63.8% in the 60 to 70 band, ECL 3.4 times the RBI floor. No growth offset applies to this multiplier.
- Pillar 3: +2x. 3a growth visibility +2x on documented AUM growth about 26% (lender growth machinery), capped at +2x by delivery grade C. 3b moat formation +0x (EM 19.6, MODEST, below the premium threshold). 3c duration +0x (no documented multi year contracted revenue).
- Strategic premium: +0x (barred by single credit; RoE recovery is in Pillar 1).
- Undiscovered Alpha: not applied (FII+DII about 35%, far above the 3% institutional absence test).
- Sector cap: 18x, Banks / NBFCs / MFIs, absolute. Corrected from the manifest's Pharma / CDMO.
- Approved DESTINATION (exit) PE base: 15x, by FY29. Within the 18x cap and the pillar derived additive band. On the dual track, additive reconciles to about 15x on the approved 1.00x multiplier; the RRM track sits lower and its divergence must be shown but does not override the approved 15x.
- Approved EARNINGS BASIS: FORWARD (one year forward P/E applied to forward EPS), horizon FY29. Operator reason: "since the growth is strong."
- Tier: A, hurdle 25%.
- SHARED CATALYST flag for the devil's advocate: asset-quality normalisation drives both the asset-quality transition and the RoA/RoE recovery; stress-test this single point of failure.
- Open Phase 3 inputs: CMP and market cap (manifest 0.0) must be sourced before the Hurdle Ratio and entry zone can be computed.

## Active tripwires carried forward

- Gross Stage III (GNPA) reversing upward from 4.49% in the next anchored quarter. The single print the whole call turns on; it would weaken asset quality and RoA/RoE together.
- Net gain on derecognition rising above about 4% of total income while reported profit growth still depends on it. The residual INDETERMINATE earnings-quality falsifier.
- AUM growth below 20% year on year for two consecutive quarters.
- The 14 unwaived covenant breach instances (23.6% of borrowings) failing to resolve.
- Over-lending check: AUM per borrower or repeat-loan share rising while GNPA rises (the verifier-B major flag).
