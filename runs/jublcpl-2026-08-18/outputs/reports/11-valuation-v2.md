# STAGE 11 v2 — ROLE 1 SOTP VALUATION, RECOMPUTED ON THE v3.6 STACK

**Company:** Jubilant Agri and Consumer Products Ltd (JACPL) | **Ticker:** JUBLCPL
**Run date:** 2026-08-18 | **Recompute date:** 2026-08-20 | **CMP:** Rs 2,342.40 (18-Aug-2026, B00 via B10) | **Shares:** 1.5152 Cr (B00 via B10) | **Market cap:** Rs 3,549 Cr (B00 via B10)
**Framework authority:** Master v3.6 (Role 1) / Section 1B v3.3 Amendments + v3.5.1 Reconciliation + v3.6 Amendments / FTTCP v2.1 (verdict held from the 18-Aug gate)
**Precedence:** v3.6 governs the items it names, then v3.5.1, then v3.3.
**Method:** SUM OF THE PARTS (operator direction 18-Aug-2026, fttcp-deliberation.md §2 Override 1). Dual track carried through.
**Model:** claude-opus-5 | **Mode:** pipeline, surgical re-run. No interactive gates.
**Supersedes for arithmetic only:** `outputs/reports/11-valuation.md` (19-Aug, pre-Damodaran stack). That file and `B11-valuation.yaml` are untouched and remain the audit record of the old stack.

---

## BANNER — PENDING OPERATOR APPROVAL

**The Business A Pillar 1 base of 30.0x is PENDING OPERATOR APPROVAL.** The 18-Aug gate approved a Pillar 1 base while the pipeline's declared authority was Section 1B v3.3 Amendment 5, whose cap is 24x. The 30.0x figure is now produced by v3.6 Amendment 11 (elite extension, 30x cap). Supersession does not auto-approve the number. The base, and every figure that moves because of it, carries PENDING OPERATOR APPROVAL below.

**Figures that move because of it: NONE.** The 35x Specialty chemicals sector cap absorbs the entire Amendment 11 uplift (math in §4.3). The pending set therefore contains exactly one item: the authority and the value of the Pillar 1 base itself. No fair value, no entry price, no Hurdle Ratio changes.

**The verdict card in §10 is PROVISIONAL until the operator approves the delta.**

**FTTCP verdict held from the 18-Aug gate; v2.1 Signal Gate not applied (no candidates block exists in this run's B09/B10); full FTTCP v2.1 re-deliberation is an open action.**

---

## 1. SCOPE OF THIS RE-RUN

Three guardrails set by the operator govern what may move.

| Guardrail | What it means here |
|---|---|
| 1. Hold the FTTCP verdicts | Blended +3 DEEP WATCH, Business A +3 DEEP WATCH, Business B −2 AVOID with the Kernex cash cap, exactly as approved 18-Aug (fttcp-deliberation.md §3). No re-deliberation. Signal Gate not fired. |
| 2. Recompute Business A Section 1B only | Amendment 11 on Pillar 1; Amendments 12 and 13 tested against the r build; Amendments 14, 15, 16 tested for bite. Business B carried forward verbatim from 19-Aug. Operator-approved bases (A 35x, B 14x, blended 29.5x, ONE-YEAR FORWARD basis) fixed. |
| 3. Pending approval | New Pillar 1 base and anything downstream of it marked PENDING OPERATOR APPROVAL. Verdict card PROVISIONAL. |

### Held-constant register (not re-derived in this run)

| Item | Value held | Source |
|---|---|---|
| Earnings basis | ONE-YEAR FORWARD (blended) | fttcp-deliberation.md, OPERATOR-APPROVED VALUATION PILLARS |
| Exit PE bases | A 35x, B 14x (band 14x to 17.5x), blended 29.5x context | fttcp-deliberation.md §2 Override 2 |
| FTTCP composite | Blended +3 DEEP WATCH; A +3 DEEP WATCH; B −2 AVOID, Kernex cap engaged | fttcp-deliberation.md §3 |
| ROCE forward verdicts | A FIRING; B STAGNANT | fttcp-deliberation.md, pillars block |
| Cash multipliers | A 1.15x; B 0.80x STRUCTURAL | B10 pillar2_cash_business_a / _b |
| Return tier | A, hurdle 25%, divisor 1.953 (FII+DII 0.45%, B10) | B10 return_tier |
| Credibility grade | C (weights 35/45/20) | B10 credibility_grade |
| Projections and EPS ladder | FY27 EPS 83, FY28 98, FY30 base 114, bear 96, bull 125 | 11-valuation.md §2.3 |
| Margin of safety | 20% below entry, as applied 19-Aug | 11-valuation.md §2.4 (see open action OA-3) |

### Earnings perimeter (restated, unchanged)

1. Forward earnings still contain the agri division until the scheme is effective. NCLT First Motion cleared 08-Jul-2026; shareholder and creditor meetings 05-Sep-2026; final order pending (B10 DEMERGER-EXECUTION flag; AR Note 32 p.138-139).
2. Per-entity PAT is illustrative-allocated, not audited. No standalone accounts exist pre-demerger (B10 input_gaps: standalone_accounts).
3. Forward EPS is un-guided. No numeric FY27 guidance exists (B10 input_gaps: forward_guidance).

---

## 2. METHOD SELECTION (unchanged)

| Role | Method | Weight | Justification |
|---|---|---|---|
| PRIMARY | SOTP, P/E per part | 100% | Demerger special situation. Two structurally different businesses. Operator direction 18-Aug-2026. |
| Cross-check A | EV/EBITDA implied | context | 35x PE destination implies roughly 21x to 24x EV/EBITDA for the polymer mix. |
| Cross-check B | Normalized-earnings P/E | context | Agri valued on mid-cycle PAT, not the FY26 placement peak. |

Exit PE comes solely from the Section 1B layer set. No round-number default is used anywhere.

**INTERIM CHECKPOINT (Section 1A):** method unchanged from 19-Aug. Proceeding.

---

## 3. BUSINESS A — SECTION 1B RECOMPUTE ON THE v3.6 STACK

Performance Polymers and Chemicals, retained, becomes Jubilant Industries Ltd. FY26 external revenue Rs 1,164.84 Cr (AR Note 39 p.150, via B10). Segment EBIT Rs 165.46 Cr (AR Note 39, via B10).

### 3.1 Pillar 1 — Amendment 11 (the headline item)

**Input.** FTTCP ROCE forward verdict FIRING (fttcp-deliberation.md). FIRING maps to current ROCE (Master v3.6 Pillar 1 table). Current segment ROCE 67.5% (AR Note 39 segment basis, via B10 unresolved.per_entity_roce_post_demerger).

**Formula (v3.6 Amendment 11, ROCE > 33%):**

    Base PE = 24 + 0.3 x (ROCE% - 33), capped at 30x
            = 24 + 0.3 x (67.5 - 33)
            = 24 + 0.3 x 34.5
            = 24 + 10.35
            = 34.35x
            -> capped at 30x
    Pillar 1 base = 30.0x   [PENDING OPERATOR APPROVAL]

**What the superseded stack produced.** Amendment 5 (v3.3): Base PE = 0.5 x 67.5 + 7.5 = 41.25x, capped at 24x, so **24.0x**. The 19-Aug report printed 30.0x while declaring v3.3 as its authority (11-valuation.md §2.1). The number it printed was the Amendment 11 number. The authority it cited could not produce that number.

**Finding.** Amendment 11 does not change the value of the Business A Pillar 1 base. It makes the 30.0x legal. The 19-Aug run and the 18-Aug gate both anticipated the elite extension: the deliberation records "Continuous formula caps at 30x well below either" (fttcp-deliberation.md, Business A pillar table), and B10 carries `pillar1_base_business_a: "30.0x"`. Against the declared-stack arithmetic the delta is +6.0x. Against the printed 19-Aug figure the delta is 0.0x. Both readings are shown in §7.

**Normalization route (v3.5.1 consolidated Amendment 9):** **NONE.** Route A fails the 20% test, no CWIP plus idle raised capital plus capex advances above 20% of capital employed is evidenced. Route B is barred, it requires TEMPORARILY DEPRESSED or RECOVERING and this verdict is FIRING. Route declared per the v3.5.1 worksheet line. Unchanged from 19-Aug.

**ROCE recovery credited via: not credited.** ROCE is at its current high. There is no recovery to credit. The Strategic Premium ROCE re-rating route stays barred (Amendment 4 single-credit rule). Unchanged.

### 3.2 Pillars 2, 3 and Strategic

| Step | Input (anchor) | Value |
|---|---|---|
| A. Pillar 1 base | ROCE FIRING, segment 67.5%, Amendment 11 elite extension, capped | **30.0x** [PENDING] |
| B. Cash multiplier | 1.15x, clean at segment level, unconfirmable without a standalone cash statement. Structural FLAG-CASH sits in the demerging agri division (B10 FLAG-CASH; deliberation §1). Structural, so no growth offset. | 1.15x |
| C. Quality-adjusted base | A x B = 30.0 x 1.15 | **34.5x** |
| D. Pillar 3 growth premium | EM 22.5, below the 25 gate (B10 em_score). Growth visibility passes 1 of 2 tests, delivery grade C. Amendment 4.1: grade C caps 3a at +2x but the "any two" test fails; EM below 25 pays 3b +0x; 3c not evidenced. | +0x |
| E. Strategic premium | Niche scarcity: VP latex #1 India and #2 global ex-China, sole food-grade PVAc in India (B10 strategic_premium_business_a). Scarcity, not ROCE re-rating, so the single-credit bar is respected. | +2x |
| F. Raw destination PE | C + D + E = 34.5 + 0 + 2 | **36.5x** |
| F2. UA-adjusted raw | UA applies, all three qualifiers met: listed over 12 months, Gate 0 71 at or above 60, FII+DII 0.45% below 3% (B10 ua_qualifiers.all_met true). F x 1.25 = 36.5 x 1.25 | **45.6x** |
| G. Sector cap | Specialty chemicals **35x** (manifest sector_cap_row; Master v3.6 cap table). No quality uplift, operator-approved. Absolute. | 35x |
| G2. Category-Break Override | **N.** Condition 2 (named binding customer or partner commitment) and condition 4 (independently verified competitor absence) are not evidenced in B10. When in doubt, deny. | No |
| G3. Override-adjusted cap | G2 = N, so G3 = G | 35x |
| **H. Final destination PE** | **min(F2, G3) = min(45.6, 35)** | **35.0x** |

**Destination PE range (Amendment 6):** 35.0 ±7.5% = 32.375x to 37.625x, rounded to the nearest 0.5x = 32.5x to 37.5x, upper bound truncated by the absolute cap. **Range 32.5x to 35.0x.** Unchanged from 19-Aug.

### 3.3 Track 1 RRM, with the Amendment 12 and 13 audit

**r-adjustment worksheet line (Amendment 12 format, mandatory):**

> r base 14.0% (small/micro-cap, Master v3.6 RRM base r table); durability adj −0.50 (band: **Moderate-Strong**, reason: VP latex #1 India and #2 global ex-China plus sole food-grade PVAc in India, near-debt-free balance sheet; the band is **not docked for cyclicality**); governance adj 0.00 (promoter CAUTION with no deal-breakers, 0% pledge, external CEO, B10 promoter_verdict; no charge taken at the 19-Aug build, held constant); cyclical surcharge 0.00 (**capped at +0.75 per 12B? N/A**, no surcharge taken and the band is not docked for cyclicality); complexity adj **0.00** (Amendment 13, no trigger, evidence below); cash-conversion r-UP: **none per 12A**; short-record r-UP: **none per 12C**; final **r = 13.5%** (bounded [9%, 18%]).

**Amendment 12A (delete the +0.5 cash-conversion r-UP).** Does not bite. The 19-Aug build took no cash-conversion r-UP. Cash quality is priced once, in Pillar 2 at 1.15x. Confirmed clean.

**Amendment 12B (cap the cyclical surcharge at +0.75).** Does not bite. No cyclical surcharge was taken and the durability band is docked for nothing. The reason for the band is stated above so the cap is auditable.

**Amendment 12C (drop the +0.75 short-record r-UP).** Does not bite. No short-record r-UP was taken. Short-record risk, if any, sits in the durability band alone.

**Amendment 13 (complexity +0.5).** Does not bite. All three triggers tested and absent:
- Subsidiary count: **2** wholly-owned subsidiaries, one of them a dormant shell incorporated 07-Apr-2025 for the demerger (02-notes-pass1.md §Note 7 p.124; 03-ardeep.md). Not a sprawling group.
- Related-party density: total related-party sales **3.84%** of FY26 revenue, down from 8.12% in FY25; no related-party borrowings; stated at arm's length (02-notes-pass1.md, AR Note 40 pp.151-155).
- Audit qualification: **unmodified opinion**, "true and fair view", no Emphasis of Matter, no Other Matter, no going-concern paragraph (03-ardeep.md §1C).

Governance concentration is a real concern in this name (14-thesis.md risk 6), but it is not one of Amendment 13's three triggers, and pricing it in r without a trigger would double-charge against the promoter position-size cap. Not applied.

**RRM (Amendment 4.4 percentage-point reading):**

    RRM = 1 + (13.5 - 13.5) x 0.12 = 1 + 0 = 1.00
    Track 1 destination = fundamental base 36.5x x 1.00 = 36.5x
                        x 1.25 UA                       = 45.6x
                        capped at 35x                   = 35.0x

**Robustness of the cap against r.** Track 1 breaches the cap for any r below 15.44%: the cap stops binding only when 36.5 x [1 + (13.5 − r) x 0.12] x 1.25 falls below 35, which needs RRM below 0.767, which needs r above 15.44%. Amendments 12 and 13 can move r by at most +0.5 here. **The destination PE is insensitive to the whole r-table rewrite.** Even before UA, 36.5x exceeds the 35x cap, so the UA convention does not matter either.

**Track divergence: 0%.** Both tracks land on 35.0x. The cap is the governing constraint, not the pillars. Neither track is "more conservative"; the cap sets the entry zone.

### 3.4 Amendments 14, 15 and 16 — one line each

**Amendment 14 (fade horizon from the Emerging Moat classification).** **Does not bite.** EM 22.5 classifies MODEST (B10 em_score), which requires a fade to industry growth by Year 3, and the 19-Aug EPS ladder already fades: FY27 83 to FY28 98 is +18%, FY28 98 to FY30 114 is +7.9% a year, which is at the audited 7.48% to 8.75% revenue CAGR band that stands for industry growth here (B10 revenue_cagr_3yr_pct). The old report's "13% CAGR" label overstates its own ladder; the numbers used, not the label, satisfy the amendment, and the numbers are what the valuation runs on.

**Amendment 15 (relative PE expression).** **Cannot be computed. NOT FOUND.** The market PE denominator requires a macro-sheet.md, and no macro-sheet exists in the repository; the FTTCP Module B8 re-rating rating does not exist for this run either, because the run used FTTCP v1.2 and Part B modules were never produced. No relative expression is stated and none is invented. Because B8 is NOT FOUND, nothing supports moving H toward the upper end of the range on relative grounds, which is one reason the range low stays where it is.

**Amendment 16 (growth premium eligibility gate from Module B2).** **Does not bite, and cannot.** Pillar 3 is already +0x on the evidence gates (EM 22.5 below the 25 threshold). The gate can only reduce a premium to +0x, and it is already there. FTTCP Module B2 is NOT FOUND for this run, so the gate is recorded as not-applicable rather than passed.

---

## 4. WHY NOTHING MOVES — THE CAP ABSORPTION MATH

### 4.1 Sensitivity of H to the Pillar 1 base

H stops sitting on the cap only when F2 falls below 35x:

    (P1 x 1.15 + 2) x 1.25 = 35
     P1 x 1.15 + 2         = 28.0
     P1 x 1.15             = 26.0
     P1                    = 22.61x

**Any Pillar 1 base above 22.6x produces a destination PE of 35.0x.** Amendment 5 gave 24.0x. Amendment 11 gives 30.0x. Both are above 22.6x. The 35x Specialty chemicals cap absorbs the entire 6.0x uplift.

### 4.2 The ROCE-basis question the recompute exposes

B10 flags the segment ROCE as inflated by segment allocation and records "group ROCE 36% authoritative" (B10 unresolved.per_entity_roce_post_demerger). Under Amendment 5 the choice of basis was immaterial, because both figures capped at 24.0x. Under Amendment 11 the choice is worth 5.1x of Pillar 1 base:

| ROCE basis | Anchor | Amendment 11 base | F | F2 | H |
|---|---|---|---|---|---|
| Segment 67.5% (directed) | AR Note 39 segment basis, via B10 | 24 + 0.3 x 34.5 = 34.35 -> cap **30.0x** | 36.5x | 45.6x | **35.0x** |
| Group 36% (B10 calls authoritative) | AR p.7, via B10 | 24 + 0.3 x 3.0 = **24.9x** | 30.6x | 38.3x | **35.0x** |

**H is 35.0x on either basis.** The sensitivity is real for the cushion, not for the answer. Cushion above the cap: 30% on the segment basis, 9% on the group basis. Recorded so the operator can see that the pending 30.0x approval is not load-bearing for any output number in this run. It would become load-bearing if the sector cap ever rose or if the cash multiplier fell.

### 4.3 What the pending approval actually governs

| Question | Answer |
|---|---|
| Does the Pillar 1 base move? | No. 30.0x before, 30.0x after. Its authority moves from unsupported to Amendment 11. |
| Does any fair value move? | No. |
| Does the entry zone move? | No. |
| Does the Hurdle Ratio move? | No. |
| Then why is it pending? | Because the 18-Aug gate approved a base the then-declared framework could not produce, and the operator has not approved the 30x elite extension as the standing authority for this name. The approval is about the audit trail and about future refreshes, not about today's price. |

---

## 5. BUSINESS B — CARRIED FORWARD VERBATIM (UNCHANGED PER OPERATOR INSTRUCTION)

Business B is UNCHANGED per operator instruction. Its 19-Aug derivation is carried forward verbatim and is not recomputed. Segment ROCE 19.9% sits below 33%, so Amendment 11's elite extension cannot reach it.

| Step | Input (anchor, 19-Aug) | Value |
|---|---|---|
| A. Pillar 1 base | ROCE STAGNANT. Current ROCE 19.9% (AR Note 39 segment). 0.5 x 19.9 + 7.5 = 17.45 ≈ **17.5x**, floor 9x, unaffected by the 30x ceiling change | 17.5x |
| Normalization route | NONE, both routes barred on a STAGNANT verdict (v3.5.1) | NONE |
| B. Cash multiplier | 0.80x, STRUCTURAL (NBS subsidy receivable, FY26 CFO/PAT 0.59x, +92.2% YoY subsidy surge). No growth offset | 0.80x |
| C. Quality-adjusted base | 17.5 x 0.80 | 14.0x |
| D / E | Commodity, no moat, no scarcity | +0x / +0x |
| F / F2 | 14.0x; UA does not apply, JASL is a fresh listing under 12 months | 14.0x |
| G. Sector cap | Agri processing 20x, not binding | 20x |
| **H** | min(14.0, 20) on NORMALIZED earnings; approved band 14x to 17.5x | **14.0x** |
| Track 1 | r 14.0%, RRM = 1 + (13.5 − 14.0) x 0.12 = 0.94; 14.0 x 0.94 = **13.2x**; divergence 6% | 13.2x |

One-line v3.6 check on Business B, for the record only: Amendments 12A, 12B and 12C remove nothing, because the 19-Aug build took no cash-conversion r-UP, no cyclical surcharge and no short-record r-UP; Amendment 13 finds no trigger; Amendments 14, 15 and 16 cannot bite on a +0x-premium value stub.

Fair value (normalized, unchanged): bear Rs 120 Cr, base Rs 250 Cr, bull Rs 400 Cr equity. HR ≈ 1.09, **STOP** as a 25% compounder. **DECISION: AVOID**, consistent with FTTCP composite −2 and the Kernex cash cap. Hold small if received in the demerger; sell into an agri up-cycle.

---

## 6. BLENDED ENTITY (PRE-DEMERGER, CONTEXT ONLY)

| Step | v3.6 recompute | v3.3-declared arithmetic | Result |
|---|---|---|---|
| Pillar 1 | ROCE 36% FIRING (AR p.7): 24 + 0.3 x (36 − 33) = **24.9x** | 0.5 x 36 + 7.5 = 25.5 -> cap 24x = **24.0x** | authority changes, value +0.9x |
| Cash | 1.15x | 1.15x | same |
| Quality base | 28.6x | 27.6x | +1.0x |
| Strategic | +2x | +2x | same |
| Raw / F2 | 30.6x -> 38.3x | 29.6x -> 37.0x | both above cap |
| Cap | 29.5x revenue-weighted (62.7% at 35x, 37.3% at 20x), no quality uplift | 29.5x | same |
| **H** | **29.5x** | **29.5x** | **no change** |

Range 27.5x to 31.5x as operator-approved (fttcp-deliberation.md, blended table). Note plainly: the printed top of 31.5x sits above the 29.5x weighted cap, so the top of that band is context, not a usable multiple. Held constant, not corrected, because the operator approved the band explicitly.

Blended HR: FY27 blended PAT ~Rs 140 Cr (polymer 125 plus agri 15), current PE 3,549 / 140 = 25.35x. HR = (1.12)³ x (29.5 / 25.35) = 1.405 x 1.164 = **1.64, CONDITIONAL.** Unchanged.

---

## 7. THE DELTA TABLE — OLD STACK VERSUS v3.6 STACK

OLD column is what `11-valuation.md` and `B11-valuation.yaml` printed on 19-Aug. It is a reference column only and was not used as an input. The third column shows what the 19-Aug run's own declared stack (Master v3.3 / Section 1B v3.3 Amendment 5, 24x cap) would have produced, because that is the true baseline the operator's directive names.

| # | Item | OLD (19-Aug printed) | Declared-stack arithmetic (Amdt 5, 24x cap) | NEW (v3.6) | Delta vs printed | Driver of the change | Anchor |
|---|---|---|---|---|---|---|---|
| 1 | Business A Pillar 1 base | 30.0x | 24.0x | **30.0x** [PENDING] | 0.0x | Amendment 11 elite extension, 24 + 0.3 x (67.5 − 33) = 34.35 -> 30x cap. The printed number was already the Amendment 11 number; v3.6 supplies the authority it lacked | v3.6 Amdt 11; B10 pillar1_base_business_a; AR Note 39 |
| 2 | Business A quality base (A x B) | 34.5x | 27.6x | **34.5x** | 0.0x | 30.0 x 1.15. Cash multiplier held at 1.15x | B10 pillar2_cash_business_a |
| 3 | Business A raw PE (F) | 36.5x | 29.6x | **36.5x** | 0.0x | 34.5 + 0 (Pillar 3) + 2 (strategic) | deliberation pillars block |
| 4 | Business A UA raw (F2) | 45.6x | 37.0x | **45.6x** | 0.0x | F x 1.25, all three UA qualifiers met | Amdt 3; B10 ua_qualifiers |
| 5 | Track 1 RRM destination | 35.0x | 35.0x | **35.0x** | 0.0x | r 13.5%, RRM 1.00 unchanged; Amdts 12A/12B/12C remove nothing, Amdt 13 finds no trigger; 35x cap binds and is insensitive to r below 15.44% | v3.6 Amdt 12, 13; §3.3 |
| 6 | Track 1 r used / RRM | 13.5% / 1.00 | 13.5% / 1.00 | **13.5% / 1.00** | 0.0 / 0.00 | Worksheet line in §3.3. Complexity 0.00: 2 subsidiaries, RPT 3.84% of revenue, unmodified audit opinion | 02-notes-pass1.md; 03-ardeep.md |
| 7 | Track 2 additive destination | 35.0x | 35.0x | **35.0x** | 0.0x | min(F2 45.6, cap 35). Cap absorbs the whole uplift; break-even Pillar 1 base is 22.6x | §4.1 |
| 8 | Track divergence | 0% | 0% | **0%** | 0 pp | Cap binds both tracks | §3.3 |
| 9 | Blended context PE | 29.5x | 29.5x | **29.5x** | 0.0x | Blended Pillar 1 rises 24.0x to 24.9x under Amdt 11, but the 29.5x revenue-weighted cap binds on both stacks | §6 |
| 10 | Destination range LOW | 32.5x | 32.5x | **32.5x** | 0.0x | Amendment 6 ±7.5% is untouched by v3.6. **The expected rise toward the cap does NOT occur.** H is unchanged at 35.0x, so the low is unchanged; Amendment 15 cannot lift it because market PE and Module B8 are NOT FOUND | Amdt 6; §3.2, §3.4 |
| 11 | Destination range MID | 35.0x | 35.0x | **35.0x** | 0.0x | Pinned at the 35x sector cap, as expected. Verified | §3.2 |
| 12 | Destination range HIGH | 35.0x | 35.0x | **35.0x** | 0.0x | Pinned at the 35x sector cap, as expected. Verified. Uncapped upper bound would be 37.5x | §3.2 |
| 13 | Business A bear fair value (FY30, per share) | Rs 3,360 | Rs 3,360 | **Rs 3,360** | Rs 0 | 35.0x x bear FY30 EPS 96. Both the multiple and the EPS ladder are held | 11-valuation.md §2.3-2.4 |
| 14 | Business A base fair value (FY30, per share) | Rs 3,990 | Rs 3,990 | **Rs 3,990** | Rs 0 | 35.0x x base FY30 EPS 114 | same |
| 15 | Business A bull fair value (FY30, per share) | Rs 4,375 | Rs 4,375 | **Rs 4,375** | Rs 0 | 35.0x x bull FY30 EPS 125 | same |
| 16 | Business A entry zone HIGH | Rs 2,043 | Rs 2,043 | **Rs 2,043** | Rs 0 | 3,990 ÷ 1.953 (Tier A, 25%) = 2,043.0 | Amdt 4.3 |
| 17 | Business A entry zone LOW (MoS) | Rs 1,634 | Rs 1,634 | **Rs 1,634** | Rs 0 | 2,043 x (1 − 0.20), MoS held at 20% (see OA-3) | 11-valuation.md §2.4 |
| 18 | Combined SOTP entry per share | Rs 2,208 | Rs 2,208 | **Rs 2,208** | Rs 0 | (polymer Rs 3,095 Cr + agri Rs 250 Cr) ÷ 1.5152 Cr shares | B10 sotp_tier_a_entry_cr |
| 19 | Combined SOTP MoS per share | Rs 1,766 | Rs 1,766 | **Rs 1,766** | Rs 0 | 2,208 x 0.80 | same |
| 20 | Hurdle Ratio, Business A base | 1.87 | 1.87 | **1.87** | 0.00 | (1.13)³ x (35 ÷ 27) = 1.4429 x 1.2963. Destination mid and imputed current PE both unchanged | Amdt 2 |
| 21 | Hurdle Ratio, Business A bull | 2.13 | 2.13 | **2.13** | 0.00 | (1.18)³ x (35 ÷ 27); grade C caps bull at base + 5% | Amdt 2; B10 credibility_grade |
| 22 | Hurdle verdict | CONDITIONAL | CONDITIONAL | **CONDITIONAL** | none | Base fails 1.953, bull passes. Verdict capped at WATCHLIST / BUY-ON-DIPS | Amdt 2 |
| 23 | Blended HR | 1.64 | 1.64 | **1.64** | 0.00 | (1.12)³ x (29.5 ÷ 25.35) | §6 |
| 24 | Expected CAGR, prob-weighted | 19.9% | 19.9% | **19.9%** | 0.0 pp | Grade C weights 35/45/20 on unchanged scenario CAGRs | Amdt 4.3; B10 |
| 25 | Combined SOTP fair value | Rs 4,625 Cr | Rs 4,625 Cr | **Rs 4,625 Cr** | Rs 0 | 35x x Rs 125 Cr polymer + 14x x Rs 18 Cr agri | B10 sotp_fair_value_today_cr |
| 26 | Decision | WATCHLIST | WATCHLIST | **WATCHLIST** (PROVISIONAL) | none | HR CONDITIONAL; CMP above entry | §10 |

### 7.1 The three checks the operator asked to verify, answered

| Expected outcome | Verified? | Finding |
|---|---|---|
| Mid and high still pinned at the 35x sector cap | **YES** | F2 45.6x exceeds the cap by 30%. H = 35.0x. The uncapped range top would be 37.5x. |
| Track LOW rises from 32.5x toward the cap | **NO** | The low stays 32.5x. The low is H ×0.925 under Amendment 6, and H did not move. Nothing in v3.6 narrows the band. Amendment 15 is the only v3.6 route that could push the operative multiple to the top of the band, and it is NOT FOUND for this run (no macro-sheet market PE, no Module B8 rating). Reported as a miss against expectation, not forced. |
| New entry top versus old Rs 2,043 and versus CMP Rs 2,342 | **Computed** | New entry top is **Rs 2,043**, identical to the old top. CMP Rs 2,342 sits **14.6% above** the entry top (2,342 ÷ 2,043 = 1.146). On the imputed polymer-only price of Rs 2,224 per share, CMP-imputed sits **8.9% above** the entry top. The stock is still above the zone. The v3.6 recompute does not create an entry. |

---

## 8. SANITY CHECKS AND VALIDATION (Section 2D and 4G, run on the new stack)

| Check | Result | Pass |
|---|---|---|
| Year 3 ROCE consistent with the FIRING verdict used in Pillar 1 | Sustained 60% to 67% segment ROCE assumed; matches FIRING | Yes |
| Revenue growth faster than capacity allows | Base polymer CAGR 13% to 14%, well under SOM-implied 24.3%; capacity gap Rs 633 Cr binds only at the SOM ceiling | Yes |
| SOM cross-check | Base 13% to 14% sits far below SOM-implied 24.3% (B10). **Consistent**, conservative against the runway | Yes |
| CFO/PAT trajectory consistent with the 1.15x cash multiplier | Unconfirmable at entity level, no standalone cash statement. Named, not estimated | INDETERMINATE |
| Fade horizon shown year by year (Amdt 14) | +18% FY27-FY28, then ~7.9% a year to FY30, at industry growth by Year 3 | Yes |
| UA ordering correct, min(F x 1.25, Cap) | 45.6x then capped at 35x, cap absolute | Yes |
| Strategic premium still justified at Year 3, single credit respected | +2x paid for VP latex and PVAc scarcity; ROCE re-rating route barred; no double credit | Yes |
| Primary catalyst fired by Year 3 in the base case | Samlaya Phase 1 partial 03-Jun-2026, full run-rate end Q1 FY27, Phase 2 end Q3 FY27 | Yes |
| Complexity priced once, in r only (Amdt 13) | No trigger, so +0.00; not priced anywhere else | Yes |
| Cash quality priced once, in Pillar 2 only (Amdt 12A) | 1.15x in Pillar 2, no r-UP | Yes |

The INDETERMINATE cash-conversion row is named, not resolved. It caps the reading at PROCEED WITH CAVEATS on the missing evidence, which is the first standalone polymer cash flow statement.

**Dispersion sizing (computed fresh, no held figure changes).** Range width = (Bull 4,375 − Bear 3,360) ÷ Base 3,990 = 1,015 ÷ 3,990 = **25.4%**, under 40%, so **normal sizing** applies from the dispersion rule. The binding cap remains the promoter CAUTION cap at Small (14-thesis.md risk 6). Tightest cap wins.

**Shared catalyst, unchanged.** Samlaya drives both Business A revenue STARTING and Business A ROCE FIRING (B10 SHARED-CATALYST). A 2 to 4 quarter slip hits revenue, margin and the ROCE-quality claim at once and pushes FY27 PAT toward the bear Rs 112 Cr. One point of failure, not three risks.

---

## 9. VALUE VERSUS PRICE, MARGIN OF SAFETY, EDGE

**Value.** The business is worth about Rs 4,625 Cr on the SOTP, about 30% above the Rs 3,549 Cr market cap, and about 88% of that value sits in the retained polymer business. The single driver is the polymer segment's return profile at a 35x specialty-chemicals cap on roughly Rs 125 Cr of FY27 forward PAT.

**Price.** The Market-Implied Assumptions block is **NOT FOUND** for this run, so no OPPORTUNITY, FAIRLY PRICED or PRICED-WE-ARE-LATE flag can be cited. What can be said from the model alone: CMP is 14.6% above the entry top and the Hurdle Ratio is 1.87, below 1.953. The price already assumes the polymer earnings arrive. What closes the gap is the first standalone polymer accounts, expected after the scheme becomes effective.

**Margin of safety.** Held at 20%, as applied on 19-Aug. Under Master v3.6 Section 4H-pre the evidence-scaled schedule governs, and on grade C with un-guided forward earnings the mixed row (30%) is the likelier fit, which would move the entry low from Rs 1,634 to Rs 1,430. Not applied, because it sits outside this surgical scope. Logged as OA-3.

**Edge claimed: process**, because the pipeline reads the audited segment note and the scheme filings on a name with 0.45% institutional ownership and no earnings calls.

---

## 10. PROVISIONAL VERDICT CARD (dual track, SOTP)

**PROVISIONAL. Pending operator approval of the Pillar 1 base of 30.0x under v3.6 Amendment 11.**
**FTTCP verdict held from the 18-Aug gate. FTTCP v2.1 Signal Gate not applied.**

**Tier: A | Hurdle: 25% | Method: SOTP | Framework: Master v3.6 / Section 1B v3.3+v3.5.1+v3.6 / FTTCP v2.1 (verdict held)**

| Field | Business A (Polymer) | Business B (Agri) | Combined SOTP |
|---|---|---|---|
| Pillar 1 base | **30.0x [PENDING APPROVAL]** (Amdt 11, ROCE 67.5% FIRING) | 17.5x (unchanged, ROCE 19.9% STAGNANT) | n/a |
| Cash multiplier | 1.15x, drag located in B | 0.80x STRUCTURAL | 1.15x |
| Pillar 3 / Strategic | +0x / +2x | +0x / +0x | +0x / +2x |
| Destination PE, Track 2 additive | 35.0x (32.5 to 35.0) | 14.0x | 29.5x context |
| Destination PE, Track 1 RRM | 35.0x, r 13.5%, RRM 1.00 | 13.2x, r 14.0%, RRM 0.94 | 29.5x |
| Divergence | 0%, cap binds both | 6% | 0% |
| UA applied | Yes, x1.25 then capped | No, fresh listing | Yes, capped |
| Sector cap | 35x specialty chemicals, absolute | 20x agri processing | 29.5x weighted |
| Fair value today | ~Rs 4,375 Cr | ~Rs 250 Cr | **~Rs 4,625 Cr, ~30% above CMP** |
| FY30 base target per share | Rs 3,990 | value stub | package ~Rs 4,155 |
| Hurdle Ratio | base 1.87 / bull 2.13 -> **CONDITIONAL** | 1.09 -> **STOP** by nature | 1.64 -> CONDITIONAL |
| Entry zone per share | Rs 1,634 (MoS) to Rs 2,043 | value ≈ fair | Rs 1,766 (MoS) to Rs 2,208 |
| CMP versus entry top | Rs 2,342 is 14.6% above | n/a | 6% above on market cap |
| Dispersion width / sizing | 25.4% -> normal; promoter cap Small binds | n/a | Small |
| Decision | **WATCHLIST** (BUY-on-dips) | **AVOID** (hold small if received) | **WATCHLIST** |

**Expected CAGR, probability-weighted, grade C (35/45/20): 19.9%.** Below the 25% hurdle at the current price. Not a current BUY.

**Delta versus the 19-Aug card: none.** Every output figure is identical. Only the Pillar 1 base's authority changed, from an unsupported 30x to v3.6 Amendment 11.

**Key valuation swing factors.** Up: first standalone polymer accounts confirming the segment return and the adhesives acceleration, which would move the HR to PASS. Down: Samlaya delay as one point of failure across revenue, margin and ROCE. Down: input-cost spikes in sulphur, VAM and butadiene compressing polymer margin. Down: subsidy-receivable build in agri worsening the blended cash print before the scheme is effective.

**Exit framework.** Target exit at the 35x polymer destination on realized standalone earnings. Thesis broken if retained-entity CFO to PAT stays below 0.70x for a second consecutive quarter with the over-six-month subsidy bucket above 8%, or if Samlaya full run-rate slips beyond Q3 FY27.

**ONE-LINE THESIS (unchanged in substance).** WATCHLIST JACPL at Rs 2,342, because the SOTP fair value of about Rs 4,625 Cr sits about 30% above the Rs 3,549 Cr market cap with about 88% in the retained polymer business, at a 35x specialty-chemicals cap on about Rs 125 Cr of FY27 forward PAT; the imputed 27x forward PE gives a Hurdle Ratio of 1.87, CONDITIONAL, so it is a buy on dips at zone and not a buy now. Key risk: Samlaya delay hits revenue, margin and ROCE together.

---

## 11. PENDING OPERATOR APPROVAL REGISTER

| # | Item | Old authority | New authority | Value before | Value after | Downstream figures affected |
|---|---|---|---|---|---|---|
| P-1 | Business A Pillar 1 base | None valid. The 19-Aug run printed 30.0x while declaring v3.3 Amendment 5, whose cap is 24x | v3.6 Amendment 11, elite extension, 30x cap, Gate D confirmed 13-Aug-2026 | 30.0x printed (24.0x under the declared stack) | **30.0x** | **None.** The 35x cap absorbs the uplift; break-even base is 22.6x |
| P-2 | Blended context Pillar 1 base | Same defect, 24.9x printed under a 24x-capped formula | v3.6 Amendment 11 | 24.9x printed (24.0x under the declared stack) | **24.9x** | None. The 29.5x weighted cap binds on both |

Approve or reject P-1 and P-2. Until then the verdict card is PROVISIONAL.

---

## 12. OPEN ACTIONS

| # | Action | Why |
|---|---|---|
| OA-1 | Full FTTCP v2.1 re-deliberation, including Part B Modules B1 to B8 and the Signal Gate | This run's FTTCP is v1.2. Modules B2, B4, B7 and B8 do not exist, so Amendments 15 and 16 cannot be evaluated on evidence and the operating-EPS discipline of Master v3.6 is unverified here |
| OA-2 | Add a downstream-candidates block to B09/B10 for this name | The v2.1 Signal Gate cannot be applied to a run whose blocks predate it. Firing it retroactively would cap catalysts at MODERATE for a procedural reason only |
| OA-3 | Rule on the evidence-scaled margin of safety (Master v3.6 Section 4H-pre) | The 20% flat MoS was carried from 19-Aug. The mixed row at 30% would move the Business A entry low from Rs 1,634 to Rs 1,430 |
| OA-4 | Rule on the Pillar 1 ROCE basis, segment 67.5% versus group 36% | Under Amendment 11 the two bases differ by 5.1x of Pillar 1 base. Immaterial today because the cap binds either way, material if the cap changes or the cash multiplier falls |
| OA-5 | Produce a macro-sheet.md with the market PE | Amendment 15's relative expression is uncomputable without it, for this and every future run |
| OA-6 | Produce the Market-Implied Assumptions block | Master v3.6's consumption clause requires it, and the value-versus-price statement is incomplete without the flag |

---

## 13. INPUT DISCIPLINE LOG

- **Un-guided forward earnings** (B10 forward_guidance MEDIUM). FY27 and FY28 PAT are operator-engaged illustrative allocations. Used as the approved earnings base, labelled provisional. Not a general-knowledge fill.
- **No standalone accounts** (B10 standalone_accounts). Per-entity PAT, ROCE and cash are illustrative allocations. Stated at every use.
- **rating_wc_quote NOT FOUND** (B10). Cash multipliers 1.15x for A and 0.80x for B are applied on the deliberation-approved structural determination only. No rating-agency confirmation of persistent working capital on the retained entity exists.
- **unit_economics_mt_kg NOT FOUND** (B10). No unit-level validation of growth. Base revenue CAGR held at 13% to 14%, far below SOM 24.3%.
- **Market PE NOT FOUND.** No macro-sheet.md exists in the repository. Amendment 15's relative destination PE is not computed and not estimated.
- **FTTCP Module B2 and B8 NOT FOUND.** This run used FTTCP v1.2. Amendment 16's gate is recorded not-applicable, Amendment 15 is uncomputable.
- **Market-Implied Assumptions block NOT FOUND.** No spread flag cited.
- Amendment 13 trigger tests are evidence checks, not input values, and are anchored to this run's own stage reports (02-notes-pass1.md, 03-ardeep.md), not to general knowledge.
- Exit PE bases used exactly as operator-approved: A 35x, B 14x, blended 29.5x. The independent four-pillar math reproduces all three.

---

```yaml
stage: B11-valuation-v2
company: "JUBLCPL"
run_date: "2026-08-18"
recompute_date: "2026-08-20"
model: claude-opus-5
status: complete
supersedes_arithmetic_of: "outputs/reports/11-valuation.md, outputs/blocks/B11-valuation.yaml (19-Aug, pre-Damodaran stack; left untouched as the audit record)"
scope: "SURGICAL RE-RUN. Business A Section 1B arithmetic recomputed on the v3.6 stack. Business B carried forward verbatim per operator instruction. FTTCP verdicts held from the 18-Aug gate. Signal Gate not applied."
input_gaps:
  - {source: "standalone_accounts", severity: "MEDIUM", note: "no standalone accounts pre-demerger; per-entity PAT/ROCE/cash are illustrative allocations"}
  - {source: "forward_guidance", severity: "MEDIUM", note: "no numeric FY27 guidance; forward EPS operator-engaged illustrative, built off Q1 FY27 annualized"}
  - {source: "unit_economics", severity: "HIGH", note: "no MT/kg volumes; unit-level growth validation not performed"}
  - {source: "rating_pdf", severity: "MEDIUM", note: "rating_wc_quote NOT FOUND; cash multipliers applied on the deliberation-approved structural determination"}
  - {source: "macro_sheet", severity: "MEDIUM", note: "no macro-sheet.md in repo; market PE NOT FOUND; v3.6 Amendment 15 relative destination PE not computable"}
  - {source: "fttcp_part_b", severity: "MEDIUM", note: "run used FTTCP v1.2; Modules B2 and B8 NOT FOUND; Amendment 16 gate not-applicable, Amendment 15 uncomputable"}
  - {source: "market_implied_block", severity: "MEDIUM", note: "Market-Implied Assumptions block NOT FOUND; no OPPORTUNITY / FAIRLY PRICED / PRICED-WE-ARE-LATE flag cited"}
flags:
  - {type: "PILLAR1-BASE-PENDING-OPERATOR-APPROVAL", note: "Business A Pillar 1 base 30.0x now rests on v3.6 Amendment 11 (elite extension, 30x cap). The 18-Aug gate approved it while the declared stack was Amendment 5 (24x cap), which could not produce it. Supersession does not auto-approve. Blended context base 24.9x carries the same defect. Downstream figures affected: NONE, the 35x sector cap absorbs the uplift (break-even Pillar 1 base 22.6x). Verdict card PROVISIONAL until approved."}
  - {type: "FLAG-CASH", applied_multiplier: "0.80x (Business B agri, STRUCTURAL subsidy receivable); Business A 1.15x with the structural drag located in the demerging division", falsification: "retained-entity CFO:PAT <0.70x two consecutive quarters with >6m subsidy bucket >8%"}
  - {type: "SHARED-CATALYST", note: "Samlaya drives Business A revenue STARTING and ROCE FIRING; one point of failure across revenue, margin and ROCE"}
  - {type: "DEMERGER-EXECUTION", note: "scheme not yet effective; forward earnings still contain agri; per-entity PAT illustrative-allocated"}
  - {type: "SIGNAL-GATE-NOT-APPLIED", note: "FTTCP verdict held from the 18-Aug gate; v2.1 Signal Gate not applied (no candidates block exists in this run's B09/B10); full FTTCP v2.1 re-deliberation is an open action"}
  - {type: "CASH-CONVERSION-INDETERMINATE", note: "Business A entity-level CFO/PAT unconfirmable without a standalone cash flow statement; caps the reading at PROCEED WITH CAVEATS with the missing evidence named"}
framework_versions: "Master v3.6 / Section 1B v3.3+v3.5.1+v3.6 / FTTCP v2.1 (verdict held from 18-Aug gate)"
pe_basis: "forward"
exit_pe_base_approved: "Business A 35x (specialty chemicals cap) / Business B 14x (normalized, agri cap 20x not binding) / Blended 29.5x (context)"
method: "SUM OF THE PARTS (operator direction 18-Aug-2026)"
earnings_perimeter: "Forward earnings still contain the agri division until the scheme is effective; per-entity PAT is illustrative-allocated (no standalone accounts exist)."
verdict_card_status: "PROVISIONAL pending operator approval of the Pillar 1 base"
destination_pe:
  track1_rrm: {low: 32.5, mid: 35.0, high: 35.0, r_used: 13.5, rrm: 1.00}
  track2_additive: {low: 32.5, mid: 35.0, high: 35.0}
  divergence_pct: 0
  governing_track: "either; the 35x Specialty chemicals cap binds identically on both tracks, and is insensitive to r below 15.44%"
pillar_detail:
  roce_used: 67.5
  roce_base: 30.0
  roce_base_authority: "v3.6 Amendment 11 elite extension: 24 + 0.3 x (67.5 - 33) = 34.35 -> capped 30x. PENDING OPERATOR APPROVAL."
  roce_base_under_superseded_amendment_5: 24.0
  roce_recovery_route: "not-credited"
  pillar1_normalization_route: "none"
  cash_multiplier: 1.15
  structural_or_growth: "clean-at-segment (structural FLAG-CASH drag located in demerging Business B)"
  growth_offset: 0
  growth_premium: 0
  strategic_premium: 2
  shared_catalyst_flag: true
  ua_applied: true
  sector_cap_used: 35
  category_break_override: false
  amendment_12a_cash_conversion_r_up: "none applied; no change"
  amendment_12b_cyclical_surcharge: "none applied; band not docked for cyclicality; cap N/A"
  amendment_12c_short_record_r_up: "none applied; no change"
  amendment_13_complexity_adj: 0.0
  amendment_13_trigger_evidence: "2 subsidiaries (one dormant shell); RPT 3.84% of FY26 revenue, no RP borrowings; unmodified audit opinion, no EoM. No trigger."
  amendment_14_fade_horizon: "EM 22.5 MODEST -> fade to industry growth by Year 3; the 19-Aug EPS ladder already fades (+18% FY27-28, then ~7.9%/yr to FY30). Does not bite."
  amendment_15_relative_pe: "NOT FOUND (no macro-sheet market PE, no Module B8 rating). Not computed, not estimated."
  amendment_16_growth_premium_gate: "not-applicable; Pillar 3 already +0x on the evidence gates; Module B2 NOT FOUND"
businesses:
  business_a_polymer:
    name: "Performance Polymers & Chemicals (retained -> Jubilant Industries Ltd)"
    destination_pe_track1_rrm: {low: 32.5, mid: 35.0, high: 35.0, r_used: 13.5, rrm: 1.00}
    destination_pe_track2_additive: {low: 32.5, mid: 35.0, high: 35.0}
    fair_values_3yr_target_per_share: {bear: 3360, base: 3990, bull: 4375}
    fair_value_today_cr: 4375
    hurdle_ratio: {base: 1.87, bull: 2.13, bull_used: true, verdict: "CONDITIONAL"}
    entry_range_per_share: {low: 1634, high: 2043}
    mos_price_per_share: 1634
    decision: "WATCHLIST"
    changed_vs_19aug: "no output figure changed; Pillar 1 base authority changed only"
  business_b_agri:
    name: "Agri (P&K Fertilizers + Agri Nutrients -> Jubilant Agri Solutions Ltd)"
    status: "UNCHANGED per operator instruction; 19-Aug derivation carried forward verbatim (ROCE 19.9% < 33%, elite extension cannot reach it)"
    destination_pe_track1_rrm: {low: 13.0, mid: 13.2, high: 13.2, r_used: 14.0, rrm: 0.94}
    destination_pe_track2_additive: {low: 13.0, mid: 14.0, high: 15.0}
    pillar_detail: {roce_used: 19.9, roce_base: 17.5, cash_multiplier: 0.80, growth_premium: 0, strategic_premium: 0, ua_applied: false, sector_cap_used: 20}
    fair_value_today_cr: 250
    hurdle_ratio: {base: 1.09, bull_used: false, verdict: "STOP"}
    decision: "AVOID"
  blended_context:
    pillar1_base: 24.9
    pillar1_base_under_superseded_amendment_5: 24.0
    destination_pe_track1_rrm: {low: 27.5, mid: 29.5, high: 31.5, r_used: 13.5, rrm: 1.00}
    destination_pe_track2_additive: {low: 27.5, mid: 29.5, high: 31.5}
    sector_cap_used: 29.5
    hurdle_ratio: {base: 1.64, verdict: "CONDITIONAL"}
    note: "pre-demerger entity only; the printed 31.5x top sits above the 29.5x weighted cap and is context, not a usable multiple; band held as operator-approved"
combined_sotp:
  fair_value_today_cr: 4625
  market_cap_cr: 3549
  premium_to_cmp_pct: 30
  tier_a_entry_cr: 3345
  tier_a_entry_per_share: 2208
  mos_per_share: 1766
  cmp_vs_entry: "CMP Rs 2,342 sits 14.6% above the Business A entry top of Rs 2,043; market cap Rs 3,549 Cr sits ~6% above the combined Tier A entry"
delta_vs_19aug:
  pillar1_base_business_a: {old: 30.0, new: 30.0, delta: 0.0, driver: "Amendment 11 supplies the authority for a number already printed; declared-stack arithmetic would have been 24.0x"}
  quality_base_business_a: {old: 34.5, new: 34.5, delta: 0.0, driver: "30.0 x 1.15, cash multiplier held"}
  track1_rrm: {old: 35.0, new: 35.0, delta: 0.0, driver: "r unchanged at 13.5%; Amdts 12 and 13 remove and add nothing; cap binds"}
  track2_additive: {old: 35.0, new: 35.0, delta: 0.0, driver: "min(45.6, 35); break-even Pillar 1 base is 22.6x"}
  blended_context_pe: {old: 29.5, new: 29.5, delta: 0.0, driver: "blended Pillar 1 24.0x -> 24.9x, but the 29.5x weighted cap binds on both stacks"}
  destination_range: {old: "32.5 / 35.0 / 35.0", new: "32.5 / 35.0 / 35.0", delta: "0 / 0 / 0", driver: "H unchanged, Amendment 6 band untouched; the expected rise in the LOW does NOT occur"}
  bear_fair_value_per_share: {old: 3360, new: 3360, delta: 0, driver: "35.0x x bear FY30 EPS 96, both held"}
  entry_zone_per_share: {old_low: 1634, old_high: 2043, new_low: 1634, new_high: 2043, delta: 0, driver: "3,990 / 1.953 then -20% MoS; nothing upstream moved"}
  hurdle_ratio: {old: 1.87, new: 1.87, delta: 0.00, driver: "destination mid 35.0x and imputed current PE 27x both unchanged"}
hurdle_ratio: {base: 1.87, bull_used: true, verdict: "CONDITIONAL"}
fair_values:
  track1: {bear: 3439, base: 4155, bull: 4639}
  track2: {bear: 3439, base: 4155, bull: 4639}
expected_cagr_prob_weighted: 19.9
entry_range: {low: 1766, high: 2208}
mos_price: 1766
mos_pct_applied: 20
dispersion_width_pct: 25.4
dispersion_sizing_cap: "Normal from dispersion; Small binds from the promoter CAUTION cap"
upside_downside_ratio: 2.6
decision: "WATCHLIST (PROVISIONAL pending operator approval of the Pillar 1 base)"
unresolved_inputs_used:
  - "per-entity PAT/ROCE/cash: illustrative allocations, no standalone accounts (stated at every use, not estimated)"
  - "forward FY27/FY28 PAT: operator-engaged illustrative, un-guided (used as the approved earnings base, labelled provisional)"
  - "rating WC commentary NOT FOUND: cash multipliers rest on the deliberation-approved structural determination alone"
  - "market PE NOT FOUND: Amendment 15 relative expression omitted, not estimated"
som_cagr_crosscheck: "consistent"
edge_claimed: "process, because the pipeline reads the audited segment note and the scheme filings on a name with 0.45% institutional ownership and no earnings calls"
open_actions:
  - "OA-1 full FTTCP v2.1 re-deliberation including Part B Modules B1-B8 and the Signal Gate"
  - "OA-2 add a downstream-candidates block to B09/B10 for this name"
  - "OA-3 rule on the evidence-scaled margin of safety (30% row would move the Business A entry low to Rs 1,430)"
  - "OA-4 rule on the Pillar 1 ROCE basis, segment 67.5% versus group 36% (5.1x of Pillar 1 base, immaterial only while the cap binds)"
  - "OA-5 produce macro-sheet.md with the market PE"
  - "OA-6 produce the Market-Implied Assumptions block"
one_line_thesis: "WATCHLIST JACPL at Rs 2,342 on the v3.6 recompute: the SOTP fair value of ~Rs 4,625 Cr sits ~30% above the Rs 3,549 Cr market cap with ~88% in the retained polymer business at a 35x specialty-chemicals cap on ~Rs 125 Cr FY27 forward PAT, and the Amendment 11 elite extension changes no output number because the cap absorbs it, so the Hurdle Ratio stays 1.87 CONDITIONAL and CMP stays 14.6% above the Rs 2,043 entry top."
```
