# FTTCP DELIBERATION RECORD — Shyam Metalics and Energy Ltd (SHYAMMETL)

Run folder: runs/shyammetl-2026-07-19. Date 2026-07-19. First workup. Concall gate CLEARED (three actual transcripts, Q2 to Q4 FY26). Standard four transitions. This record is authoritative for Phase 3. `/finalize` requires it before the valuation can run.

---

## FINAL RULINGS (after operator review)

1. Forward window: 3 months primary, 6 months secondary, 12 months for ROCE. `sure`. Unchanged.
2. Business type: standard operating business (integrated metals manufacturer), standard four transitions. `sure`. Unchanged.
3. Workup intent: first workup. Role 1 derived fields N/A. `sure`. Unchanged.
4. Sector cap row: **20x, operator confirmed.** The draft ruled 20x `genuinely uncertain` (no dedicated steel row in Section 1B; 22x Building materials as the alternative). The operator approved 20x at the valuation gate, which resolves the uncertainty and sets aside the 22x alternative. The manifest value "Pharma / CDMO" (38x) is overridden and must be corrected in the manifest.
5. Cash conversion: GROWTH-INDUCED, not structural, not indeterminate. `fairly sure`. Unchanged. Falsifier: consolidated finished goods inventory growth above twice revenue growth for two straight quarters into FY27, or standalone CFO to profit below 0.7x after capex tapers.
6. ROCE backward verdict: TEMPORARILY DEPRESSED, held over DECLINING. `genuinely uncertain`. Unchanged. Falsifier: the next two return on capital prints keep falling while the commissioned lines run.
7. Revenue forward verdict: FIRING (+2). `sure`. Unchanged.
8. Margin forward verdict: STAGNANT (0). `fairly sure`. Unchanged.
9. Cash conversion forward verdict: FIRING at the consolidated level, flagged (+2). `fairly sure`. Unchanged.
10. ROCE forward verdict: RECOVERING at 40 to 60% probability over 12 months (+1). `genuinely uncertain`. Unchanged.
11. Composite transition score: 5 out of 8, BUY-candidate band. `fairly sure`. Unchanged. Kernex cap not engaged; TRIM rule not engaged.
12. Disposition: constructive transitions, cautious position. Small sizing, strict entry, subject to Phase 3. `fairly sure`. Unchanged. The live promoter money laundering attachment is the single most likely veto at final disposition.
13. Earnings basis: **one-year-forward P/E, operator decided.** The draft left this unpicked for the operator. Resolved below.

SHARED CATALYST flag carries to Phase 3: the capex commissioning drives both the Pillar 1 ROCE recovery and the Pillar 3a growth premium. Role 3 must stress test the single point of failure.

---

## OPERATOR OVERRIDES

### Override 1 — Destination (exit) PE base

- **Draft determination:** four-pillar computed destination of about 17.7x on the additive track and about 15 to 16x on the RRM track, both under the 20x sector cap. The card presented 20x as the sector cap ceiling, not as the computed base.
- **Operator ruling:** set the destination exit PE at 20x. Operator's words: *"approve the PE base at 20x."*
- **Effect:** the operator elects the sector cap ceiling as the exit multiple, an uplift of about +2.3x from the computed 17.7x additive base to the 20x cap. This does not breach the cap; it sits exactly on it. It is the most generous base the framework permits for this sector row.
- **Reasoning:** the operator did not elaborate a reason and was offered the chance to; reasoning is left to operator discretion. Recorded as the operator's election of the sector ceiling.

### Override 2 — Earnings basis

- **Draft determination:** left unpicked; the card laid out one-year-forward versus trailing for the operator to decide.
- **Operator ruling:** one-year-forward P/E. Operator's words: *"use forward earnings"* and *"yes, forward earnings, write the deliberation record."*
- **Effect:** the 20x exit multiple applies to one-year-forward (FY27E) EPS, not trailing FY26 EPS. This fits a cyclical business mid ramp, where trailing earnings are depressed by capacity commissioned but not yet fully earning.

No other determination in the draft was overridden. The FTTCP composite (5 out of 8, BUY-candidate band, cautious disposition) stands.

---

## FINAL FTTCP VERDICT

Recorded as the operator's explicit decisions, since the operator did not restate the composite verdict in their own words beyond the valuation gate. The operator approved the valuation base (exit PE 20x, forward earnings) and directed the record be written. The draft's transition verdict stands unoverridden: composite 5 out of 8, BUY-candidate band on transitions, disposition held cautious (small sizing, strict entry) pending Phase 3 valuation and the live promoter matter. The whole call turns on whether the commissioned capacity converts into earnings, seen first as the FY27 return on capital rising and the core subsidiary profit stabilising.

Honest consequence on the record: even at 20x on forward earnings the hurdle math is tight. FY26 EPS is about Rs 38.5; FY27E at roughly 25 to 30% growth is about Rs 48 to 50; 20x forward implies a base fair value near Rs 960 to 1,000, around or slightly below the current Rs 1,022. On these inputs the 25% hurdle entry lands well below CMP. Phase 3 / Role 1 computes the actual entry and MoS; the operator set the base at the ceiling with that tension recorded.

---

## CROSS-FAMILY GRADE

Did not run this session. `verifiers/fttcp_crossgrade.py` returned SKIPPED: no Gemini or GPT key configured in the environment. Per protocol, FTTCP confidence is treated one notch lower for the absence of the out-of-family adherence check. There is no grader divergence to resolve.

---

## OPERATOR-APPROVED VALUATION PILLARS (authoritative for Phase 3)

Phase 3 (stage 11, Role 1) MUST use the approved base and basis below. It may not silently derive a different exit PE.

| Pillar / input | Approved value |
|---|---|
| Pillar 1 ROCE input | ROCE forward verdict RECOVERING at 40-60%; blend weighted to current and FY[Y+2] per the FTTCP v1.2 Pillar 1 table |
| Pillar 1 normalization route (v3.5.1) | TBD in Phase 3. Route A (operational ROCE) if CWIP plus idle capital exceeds 20% of capital employed; the exact CWIP figure was NOT anchored this run and must be pulled from the balance sheet. Else Route B (pre cycle normalized ROCE, median ~20% capped at the evidenced level, unwind catalyst = the dated commissioning schedule). Route A governs if both hold. |
| ROCE recovery credited via | Pillar 1. Strategic Premium ROCE re-rating route is barred (single credit rule). |
| Pillar 2 cash multiplier | 1.0x, growth-induced, provisional (consolidated conversion strong; standalone drain is intra group). Superseded in effect by the flat 20x election below, but recorded for the pillar audit trail. |
| Pillar 3 growth and moat premium | ~+3x (3a growth visibility +2x on capex-embedded growth and delivery grade B; 3b moat formation +1x on EM 30 STRENGTHENING, provisional; 3c duration +0x). Within the +6x cap. |
| Strategic premium | 0x |
| Undiscovered Alpha | NOT applied. FII plus DII about 16.7% (operator context, non anchored), above the 3% institutional-absence ceiling. |
| Return hurdle tier | Tier A, 25% hurdle. FII plus DII above 3% would allow Tier B, but the promoter CONCERN verdict fails the Tier B quality gate. |
| Sector cap row | **20x** (operator confirmed; manifest "Pharma / CDMO" 38x overridden; correct the manifest before Phase 3) |
| **Approved destination (exit) PE base** | **20x, flat.** Operator override electing the sector cap ceiling over the computed ~17.7x additive / ~15-16x RRM. Applies as a single flat exit multiple; both computed tracks are superseded by the operator's 20x. |
| **Earnings basis** | **FORWARD (one-year-forward, FY27E EPS).** Operator ruling. Reason: fits a cyclical business mid ramp; trailing FY26 EPS understates because commissioned capacity is not yet fully earning. |
| Operator adjustment to PE, with reasoning | +2.3x, from the computed 17.7x additive base up to the 20x sector cap. Operator's words: "approve the PE base at 20x." Reasoning left to operator discretion. |
| SHARED CATALYST flag | YES. Capex commissioning drives both Pillar 1 ROCE and Pillar 3a; Role 3 stress test required. |

---

*Deliberation record ends. Next: /finalize runs/shyammetl-2026-07-19 for Phase 3 (assembly, valuation, thesis, devil's advocate, valuation verification, final synthesis).*
