# SECTION 1B v3.9 AMENDMENTS — RELATIVE VALUATION CROSS-CHECK (STEP 1C) + FORWARD-EXPECTATION EXIT FRAMEWORK

*Version 3.9 | first issued 26 August 2026, reissued 07 September 2026. Two amendment sets layer in this file. Amendment 20 (relative valuation cross-check, step 1C) arose from the MANINDS valuation, operator directive 26-Aug-2026. Amendments 21-25 (forward run-rate base, probabilistic catalyst credit, expectation ledger, price decomposition, margin of safety as position size) arose from the E2E Networks AR FY25-26 review, adopted and signed off by Keerti 07-Sep-2026. Both layer on top of Section 1B v3.3 + v3.3 Amendments + v3.5.1 + v3.6 + v3.7 + v3.8. This file does not modify any prior file in place. Where they overlap on items named here, v3.9 governs; within v3.9 a later amendment governs an earlier one. Stage 11 reads this alongside the earlier Section 1B files. Amendments number continuing from v3.8 (whose last amendment is 19); v3.9 carries Amendments 20 through 25.*

*v3.9 reissued 07-Sep-2026 as a merged file: Amendment 20 (Step 1C relative-valuation cross-check, 26-Aug-2026, MANINDS) retained verbatim; E2E amendments placed as 21-25.*

*Design principle adopted with Amendments 21-25: the market pays for the probability-weighted future, not the audited past. The E2E review exposed that the framework structurally could not buy a fast-growing name before it re-rated. The April-2026 buy zone was Rs 140-170 (post-split) against a 52-week low of Rs 183; the stock moved from ~Rs 245 to Rs 601 while the framework said "not yet" throughout. Companion artefacts: Expectation Ledger template (Appendix A) and first worked case, E2E Networks (Appendix B).*

---

## AMENDMENT 20 — RELATIVE VALUATION CROSS-CHECK (NEW STEP 1C)

`[v3.9: a new Section 1B step 1C between the pillar build and the verdict card — a live peer table, quality/value clustering on normalised earnings, subject placement with stated adjustments, bear/base/bull relative exit multiples, and a governance rule where the pillar destination sits far below the adjusted peer base — operator directive 26-Aug-2026, arising from the MANINDS valuation]`

**20.0 Placement in the Section 1B flow.** Step 1C runs AFTER the pillar build (the destination PE derived in Section 1B, both tracks) and BEFORE the verdict card. Section 1A (Method Suitability Matrix) selects methods; Section 1B builds the pillar destination PE; step 1C cross-checks that destination against live peers; the verdict card follows. Step 1C is mandatory in every Role 1 that carries a Section 1B destination PE. It adds a display step and one governance rule; it does not replace method selection (Section 1A) or the pillar derivation (Section 1B).

**20.1 The live peer table (Claude web supplies; Code cannot).** Step 1C is executed in claude.ai with live web access, per the TEAM WORKFLOW split: Claude Code holds no live market data, so it CANNOT populate or govern this step. Claude web supplies a peer table of 4-6 listed peers, each row carrying:
- trailing P/E;
- clean / forward P/E (the normalised-earnings multiple; state which and the earnings basis);
- ROCE;
- growth (revenue or EPS, stated);
- net debt (or net cash);
- governance (a one-word read with the basis: pledge, related-party, audit, regulator flags).

Every figure carries its source and date. This is the load-bearing guard behind Correction 6: multiples pulled from Claude web's memory are STALE and BARRED. A peer table without live, dated, sourced figures cannot govern; it displays as PENDING LIVE PEER TABLE and the pillar destination governs by default until the live table lands.

**20.2 Quality and value clusters (on normalised earnings).** From the live table, identify the QUALITY cluster (higher ROCE, higher growth, cleaner governance, commanding the higher clean/forward multiple) and the VALUE cluster (the cheaper, weaker-quality group). Clustering is on NORMALISED (clean / forward) earnings, never on trailing blended P/E. State each peer's cluster and the one-line reason.

**20.3 Subject placement with stated adjustments.** Place the subject against EACH cluster, with every adjustment named and signed:
- quality gap (ROCE and durability vs the cluster);
- growth gap;
- governance discount (a named overhang widens it);
- size / liquidity discount;
- cyclicality / converter position (a converter is placed on through-cycle earnings per v3.7 Amendment 17.1, never spot).

The output is the ADJUSTED PEER BASE: the base-case multiple the subject earns after these adjustments, NOT the raw cluster multiple. A large governance or quality gap can place the subject far below the quality cluster; the adjustments make that placement explicit rather than accidental.

**20.4 Bear / base / bull relative exit multiples.** From the placement, rule three relative exit multiples: bear, base, bull. The base is the adjusted peer base of 20.3. Bear and bull move it by the peer dispersion actually observed in the live table (not by a round-number spread). These are exit multiples on the SAME earnings basis the entry used (v3.8 Amendment 18.1 symmetry) and on normalised earnings (matching the cluster basis of 20.2).

**20.5 The governance rule (>30% below the adjusted peer base).** Compare the pillar destination PE (the governing-track destination that sets the entry zone) against the base-case adjusted peer base of 20.3:
- Pillar destination MORE THAN 30% below the adjusted peer base (pillar < 0.70 x adjusted peer base) → the RELATIVE multiple GOVERNS the exit. The pillar output is shown as a CROSS-CHECK line, not discarded.
- Otherwise → the PILLAR destination governs and the peer table is the cross-check.

Either way, print the divergence explicitly: pillar destination, adjusted peer base, the percentage gap, and which governs. The 30% threshold is a fixed constant, not fuzzy language.

**20.6 The sector cap is still the absolute ceiling.** When the relative multiple governs (20.5), it is still BOUNDED BY the sector cap. Nothing in Amendment 20 raises or lowers a cap (consistent with v3.7 Amendment 17.5 and the v3.6 single-credit regime). The relative multiple governs the choice BETWEEN the pillar destination and the adjusted peer base, within [pillar destination, sector cap]. Where the adjusted peer base exceeds the cap, the cap binds and the excess is recorded as a cap-review flag (20.7), not silently priced in.

**20.7 Annual cap review against live peer medians.** Sector caps are reviewed ANNUALLY against live peer medians. The review is an operator-run maintenance action (not a per-run step): where a sector's live peer median clean/forward multiple has moved durably away from the cap, the cap is re-ruled by the operator against the live median, and the ruling is logged in the Section 1B cap table with its date and evidence. This is the sanctioned channel by which a persistently higher peer median flows into the cap; a per-run cross-check never breaches the cap on its own.

**20.8 Downstream recompute when the relative multiple governs.** When 20.5 hands governance to the relative multiple, that multiple (capped per 20.6) becomes the destination PE base for the exit construction. Recompute on it, in order:
- the Year-N exit price (v3.8 Amendment 18.1, on the entry-consistent basis; within-hold option slices still resolve per 18.3, beyond-hold per 18.4);
- the fair-value path and the one-number FV CAGR (v3.8 Amendment 19.0-19.1);
- the return-source label and its decomposition line (v3.8 Amendment 19.2-19.3);
- the entry zone (entry = exit-consistent fair value / 1.25^N, MoS per evidence scale).

The pillar-based fair values and entry zone are retained as the labelled cross-check. No entry zone is presented without the Amendment 19 FV CAGR and return-source classification recomputed on the governing multiple.

**20.9 Operator-approved base still binds.** Where the operator approved a destination PE base and earnings basis at the FTTCP pillar-approval gate, step 1C is a cross-check against that approved base, not an override of it. If the relative multiple diverges from the approved base, REPORT the divergence plainly (pillar, approved base, adjusted peer base, the governing choice under 20.5); value on the approved base unless the operator re-rules. Step 1C never silently overwrites an operator's call.

---

## AMENDMENT 21 — FORWARD RUN-RATE EARNINGS BASE (replaces the annual-model anchor)

**Problem:** The destination multiple is applied to trailing audited earnings or to the last committed annual model. When a company's run-rate moves faster than the annual model (E2E: Q1 FY27 run-rate ~2.5x the FY26 audited base), the framework values a business that no longer exists and produces a buy zone the stock will never revisit.

**Change:**
- The earnings base for all Section 1B and Role 1 calculations is the **latest reported quarter's run-rate, annualised, adjusted for known one-offs** (treasury income on a depleting cash pile, exceptional items, seasonal distortions must be stated and adjusted).
- The base is **refreshed every quarter** at the Role 4 results review. It is never frozen at the annual model.
- The annual (AR / Role 6) model is retained as a **cross-check and floor**, not the anchor. Where run-rate and annual model diverge by more than 25%, the worksheet must state which is used and why.
- Seasonal or lumpy businesses (project cargo, agri, capital goods) use a trailing-4-quarter base in place of a single-quarter annualisation. The worksheet declares which basis applies.

---

## AMENDMENT 22 — PROBABILISTIC CATALYST CREDIT (replaces binary fired / not-fired)

**Problem:** Pillar 3 and the Strategic Premium credit a catalyst at full value once "fired" and at zero before. The market credits a 60%-likely catalyst at roughly 60%. Waiting for the fire means paying after the re-rating.

**Change:**
- Each catalyst in the FTTCP catalyst table carries an explicit **probability (0.00-1.00)** assigned by the operator, with the evidence basis stated.
- The earnings increment attributable to that catalyst is credited at **increment × probability**.
- Probabilities are **updated each quarter** on new evidence (Bayesian discipline: state the prior, the evidence, the posterior).
- Tiering for Amendment 24: probability ≥ 0.50 is **high-probability expectation**; below 0.50 is **speculative**.
- The evidence-quality symbols (📄 documented / 🎙️ management verbal / 🔍 inferred) are retained as inputs to the probability, not as gates on the credit. Documented evidence raises the probability; it no longer unlocks a premium tier by itself.
- **Downside terms are mandatory.** At least one negative increment (base erosion: cost growth outpacing revenue, margin compression on new capacity, catalyst slippage) must be carried with its own probability, so the distribution is two-sided. A ledger with only positive entries is rejected.

---

## AMENDMENT 23 — EXPECTATION LEDGER WITH EXPIRY (the guard against chasing)

**Problem:** Crediting expectations without an expiry converts the framework from cautious to credulous. The market punishes unmet expectations hard; the framework must too.

**Change:**
- Every expectation credited in the price is logged in the **Expectation Ledger** (template, Appendix A) with: the catalyst, the ₹ Cr earnings increment, the probability, the **confirming evidence** (a specific metric and threshold), and a **confirm-by date**.
- If the confirming evidence does not appear by the confirm-by date, the credit **decays by a fixed step of 25% of the original credit per missed review**, and the position is trimmed in proportion (Amendment 25).
- Two consecutive missed confirm-by dates on the same item **retire the item to zero** and register as a DROPPED commitment in the Role 5 promise-vs-delivery tracker (governance flag).
- Confirmed items move from the ledger to the confirmed run-rate base at the next Amendment 21 refresh.
- The ledger is saved to Notion with every Role 1 / Role 4 / Role 6 output. An expectation not on the ledger may not be credited in the price.

---

## AMENDMENT 24 — PRICE DECOMPOSITION (replaces the single fair-value verdict)

**Problem:** "CMP above fair value → do not buy" is a binary verdict on a probabilistic object. It cannot express that a price above confirmed fair value is still buyable when the excess is high-probability.

**Change:**
- At any CMP, decompose the market capitalisation into three supported tiers plus a residual:

| Tier | Earnings basis | Multiple |
|---|---|---|
| T1 Confirmed | Amendment 21 run-rate base | Destination PE (Section 1B) |
| T2 High-probability expectation | Σ(increment × p) for p ≥ 0.50, net of downside terms | Destination PE |
| T3 Speculative expectation | Σ(increment × p) for p < 0.50 | Destination PE |
| Residual | CMP minus (T1 + T2 + T3) | Unsupported premium |

- The verdict is stated as the four percentages, not as a single "over/under valued."
- **Position size is set to T1 + T2** (Amendment 25). T3 is the explicit bet and is disclosed as such. The residual is the amount the price exceeds anything the framework can support; a residual above 25% of CMP caps the verdict at starter size regardless of conviction.
- The Hurdle Ratio (Amendment 2) is retained and recomputed on the Amendment 21 base with the probability-weighted EPS CAGR. It remains a feasibility check, not a gate.

---

## AMENDMENT 25 — MARGIN OF SAFETY EXPRESSED AS SIZE, NOT PRICE (fast-growth carve-out)

**Problem:** For fast growers the framework stacked three conservatisms: a cautious fair value, a 25% return hurdle, and a further 20-30% price discount. The compound effect is a buy price below the observed trading range.

**Change:**
- For names classified **fast-growth** (Amendment 21 run-rate growth ≥ 40% YoY, or FTTCP Revenue Transition = ACCELERATING), the margin of safety is expressed as **position size**, not as a price haircut below fair value.
- **Starter position:** 2-3% of portfolio (Small) when T1 + T2 ≥ 75% of CMP and the residual ≤ 25%. This is the "pay a small price to be in" entry.
- **Add ladder:** +1 to +2% of portfolio on each ledger item that confirms (moves from T2/T3 to T1), up to Medium (4-6%) when T1 alone ≥ 60% of CMP, and Large (7-10%) only when T1 ≥ 80% of CMP and Gate 0 EXCELLENT and Promoter TRUSTWORTHY or better (existing sizing rules unchanged at the top).
- **Trim ladder:** trim 25% of the position for each ledger item that decays (Amendment 23); trim 50% if the residual exceeds 40% of CMP after a decay.
- **Exit:** thesis-broken triggers are unchanged and remain absolute.
- Non-fast-growth names retain the existing price-based margin of safety. This carve-out does not weaken the framework for steady compounders; it corrects it for inflection names only.

**Accepted cost (recorded for audit trail):** this method will sometimes open starter positions in names whose expectations fail, and those names fall hard. The operator accepts this as the price of not structurally missing compounders. The starter size and the ledger expiry are the two controls that bound the cost.

---

## APPENDIX A — EXPECTATION LEDGER TEMPLATE

| # | Catalyst / expectation | ₹ Cr PAT increment | Probability | Evidence basis (📄/🎙️/🔍) | Confirming metric and threshold | Confirm-by | Status |
|---|---|---|---|---|---|---|---|
| 1 | | | | | | | OPEN / CONFIRMED / DECAYED-1 / DECAYED-2 / RETIRED |
| D1 | Downside term (mandatory) | (negative) | | | | | |

Rules: at least one downside row; every row has a confirm-by date; prob ≥ 0.50 = T2, < 0.50 = T3; decay 25% per missed review; two misses = RETIRED + DROPPED flag.

---

## APPENDIX B — FIRST WORKED CASE: E2E NETWORKS (NSE: E2E), 07-Sep-2026

**Status:** web-side draft for Claude Code Stage 11 consumption. All probabilities are operator-assignable and flagged for confirmation. CMP ₹601 (5-Sep-2026, post-split). Shares 20.56 Cr. Market cap ₹12,366 Cr.

### B1. Amendment 21 base

Q1 FY27 (quarter ended 30-Jun-2026): revenue ₹156.76 Cr, operating EBITDA ₹117.9 Cr (75.2%), PAT ₹43.88 Cr. Annualised PAT run-rate **₹176 Cr**. Adjustment note: ~₹11 Cr/quarter of other income is treasury on a depleting cash pile and will fade; no other one-offs. Confirmed base carried at ₹176 Cr with the treasury fade captured in downside term D1. Classification: fast-growth (run-rate growth +334% YoY). Single-quarter annualisation is appropriate (subscription-like cloud revenue, not seasonal).

### B2. Amendment 22 / 23 Expectation Ledger, FY28 target

| # | Catalyst | ₹ Cr PAT increment | Prob | Basis | Confirming metric | Confirm-by | Tier |
|---|---|---|---|---|---|---|---|
| 1 | Second 1,024 B200 cluster fills at similar margin | +90 | 0.75 | 📄 cluster ordered; 🎙️ arriving "in the next few months" | Quarterly revenue ≥ ₹200 Cr with op-EBITDA margin ≥ 68% | Q3 FY27 (Jan-27 results) | T2 |
| 2 | IndiaAI / sovereign mission orders ramp | +100 | 0.50 | 🔍 broker-reported ~₹2,650 Cr combined orders; 🎙️ sovereign positioning | Disclosed sovereign/mission revenue, or named order execution | Q4 FY27 (Apr-27 results) | T2 |
| 3 | Operating margin holds ≥ 68% through FY28 despite new capacity | +60 | 0.55 | 🎙️ mgmt ~70% medium-term target; 📄 Q1 FY27 75.2% | Reported op-EBITDA margin each quarter | Rolling, each quarter | T2 |
| 4 | Contracts lengthen / TIR durability (churn falls, pricing holds) | +40 | 0.40 | 🎙️ "longer-term contracts"; 📄 FY26 AR: most ≤ 1 year | FY27 AR contract-duration disclosure shows majority > 1 year, or disclosed multi-year % | FY27 AR (Sep-27) | T3 |
| 5 | Next-gen (B300 / Vera Rubin) capacity + platform attach | +24 | 0.35 | 🎙️ roadmap only | Announced deployment with utilisation disclosure | H1 FY28 | T3 |
| D1 | Downside: D&A + finance cost growth outpaces revenue; treasury income fades | −60 | 0.35 | 📄 FY26 D&A ₹169 Cr rising; Q1 FY27 finance ₹10 Cr/qtr; ₹450 Cr loan | Quarterly D&A + finance cost growth vs revenue growth | Rolling, each quarter | (netted) |

Probability-weighted increments: cat 1 = 67.5; cat 2 = 50.0; cat 3 = 33.0; cat 4 = 16.0; cat 5 = 8.4; D1 = −21.0.
T2 net (p ≥ 0.50, less D1) = 67.5 + 50.0 + 33.0 − 21.0 = **₹129.5 Cr**. T3 = 16.0 + 8.4 = **₹24.4 Cr**.
**Probability-weighted FY28 PAT = 176 + 129.5 + 24.4 = ~₹330 Cr** (old binary base ₹260 Cr; old bull ₹490 Cr).

### B3. Amendment 24 price decomposition at ₹601

**RULING REQUIRED (Appendix C, R1):** sector cap. Two cases shown.

**Case 30x** (Amendment 8: "Data centers / cloud infrastructure, capital-heavy"). Destination PE 29-30x is at the cap; multiple used 30x.

| Tier | ₹ Cr PAT | × 30 = mcap ₹ Cr | ₹/share | % of CMP |
|---|---|---|---|---|
| T1 Confirmed | 176 | 5,280 | 257 | 43% |
| T2 High-prob | 129.5 | 3,885 | 189 | 31% |
| T3 Speculative | 24.4 | 732 | 36 | 6% |
| Supported total | | 9,897 | 482 | 80% |
| Residual | | 2,469 | 119 | **20%** |

Verdict (30x): 80% supported, 20% unsupported. Residual ≤ 25% → **starter position permitted (2-3%)**, no add until ledger items 1-3 confirm. Comfortable starter zone ≤ ₹482 (fully supported); ₹601 is a starter that consciously pays a 20% premium to the cap.

**Case 45x** (Platform / SaaS / IT services, the classification the Notion thesis has used). Forward multiple 40x used (reflects expected growth, stays under cap).

| Tier | ₹ Cr PAT | × 40 = mcap ₹ Cr | ₹/share | % of CMP |
|---|---|---|---|---|
| T1 Confirmed | 176 | 7,040 | 342 | 57% |
| T2 High-prob | 129.5 | 5,180 | 252 | 42% |
| T3 Speculative | 24.4 | 976 | 47 | 8% |
| Supported total | | 13,196 | 642 | 107% |
| Residual | | (830) | (40) | **none** |

Verdict (45x): fully supported by T1 + T2 alone (99%). **Starter position comfortable; add ladder opens on each confirmation.** Starter zone up to ~₹640.

### B4. Amendment 25 sizing

- Starter: 2-3% now, under either cap case (residual ≤ 25% in both).
- Add +1-2% on confirmation of item 1 (Jan-27), item 2 (Apr-27), item 3 (rolling). Medium (4-6%) reachable by mid-FY28 if items 1-3 confirm, under the 45x case; under the 30x case, Medium requires the residual to close via earnings growth first.
- Trim 25% per decayed item; trim 50% if residual > 40% after a decay.
- Exit: existing thesis-broken triggers unchanged (utilisation < 60% for 2 quarters; op-EBITDA margin < 52% for 2 quarters; no anchor customer AND MRR stagnant).

### B5. What changed versus the AR review verdict

Old method: FY28 base ₹260 Cr × 29.5x = ~₹373/share → "above fair value, do not add." New method: probability-weighted FY28 ₹330 Cr, decomposed → "starter permitted now; add on confirmation; the size of the unsupported premium depends on the sector-cap ruling." The Decision Status change from WATCHLIST / DO NOT ADD to a starter position is **operator-only** and is not set here.

---

## APPENDIX C — RULINGS REQUIRED FROM OPERATOR BEFORE STAGE 11

| # | Ruling | Options | Effect |
|---|---|---|---|
| R1 | E2E sector cap classification | (a) 30x capital-heavy cloud infra per Amendment 8; (b) 45x Platform/IT per current Notion thesis; (c) blended cap for infra-plus-platform businesses (proposed new row, e.g., 35x) | Decisive: residual 20% vs none |
| R2 | Confirm or adjust the six ledger probabilities in B2 | Operator's anchors | Moves T2/T3 split and FY28 weighted PAT |
| R3 | Decision Status for E2E | Hold WATCHLIST; or open STARTER (2-3%) per Amendment 25 | Operator-only field |
| R4 | Repo ruling line | Add to `companies/E2E.md`: `07-Sep-2026 | RULING | Section 1B v3.9 (A21-A25) signed off; E2E is the first worked case; sector-cap ruling R1 pending.` | Gate record |

---

## INTERACTION WITH THE REST OF THE FRAMEWORK

**Amendment 20 / step 1C (relative valuation cross-check):**
- **Step 1C changes exit-multiple SELECTION, not pillar math.** Amendment 20 derives no new pillar, ROCE input, or premium. It selects the governing exit multiple between the pillar destination and the adjusted peer base, bounded by the sector cap. Pillar 1/2/3 derivation, single-credit, and the v3.5.1 route selection are untouched.
- **The sector cap remains absolute.** 20.6 restates it: nothing in Amendment 20 raises or lowers a cap. 20.7's annual review is the only channel that moves a cap, and it is an operator ruling logged in the cap table, not a per-run act.
- **Basis symmetry (v3.8 Amendment 18.1) binds the relative exit.** The relative multiple applies to the SAME earnings basis the entry used, on normalised earnings. Mixing bases is barred here as everywhere.
- **Converter placement (v3.7 Amendment 17.1) binds subject placement.** A converter subject is placed against peers on through-cycle earnings, never spot; a converter slice resolving successfully still exits on its own converter multiple (18.3), which step 1C does not lift.
- **Amendment 19's display duty is preserved.** When the relative multiple governs, the FV path, FV CAGR, and return-source label are recomputed on the governing multiple (20.8); the verdict card and Role 2 Section 5 carry the recomputed lines.
- **Team-workflow split.** Step 1C is a Claude web step: it needs live market data Claude Code does not hold. In pipeline mode Code marks the slot PENDING LIVE PEER TABLE and the pillar governs until claude.ai supplies the live table. See the ferry payload `docs/team_workflow_amendments_maninds_2026-08-26.md`.
- **Correction 6 guard.** Every peer multiple carries a live source and date; memory-pulled multiples are barred (20.1). A table without live dated figures cannot govern.

**Amendments 21-25 (forward-expectation exit framework):**
- **Forward base, not audited past (Amendment 21).** The earnings base for every Section 1B pillar and Role 1 output is the latest-quarter run-rate annualised (trailing-4-quarter for seasonal names), refreshed each quarter. The annual model becomes a cross-check and floor, not the anchor. This is a base change; the pillar derivation on that base is unchanged.
- **Probabilistic catalyst credit replaces the binary gate (Amendment 22).** The FTTCP catalyst table and the Strategic Premium credit each catalyst at increment × probability, with a mandatory two-sided downside term. The evidence symbols feed the probability; they no longer gate the credit. Pillar 3 and the premium read from this credit.
- **Expiry binds every credited expectation (Amendment 23).** No expectation is credited in the price unless it sits on the Expectation Ledger with a confirm-by date; a missed date decays the credit 25% per review and trims the position; two misses retire it and raise a Role 5 DROPPED flag. The ledger ferries to Notion with every Role 1 / Role 4 / Role 6 output.
- **Decomposition replaces the single fair-value verdict (Amendment 24).** The verdict is four percentages (T1 confirmed, T2 high-probability, T3 speculative, residual), not one over/under-valued line. The Hurdle Ratio (Amendment 2) is recomputed on the Amendment 21 base. The sector cap still caps the destination PE used in each tier.
- **Margin of safety as size for fast growers (Amendment 25).** For fast-growth names the margin of safety is position size (starter 2-3%, add on confirmation, trim on decay), not a price haircut. Steady compounders keep the existing price-based margin of safety. The top-level sizing rules (Gate 0, Promoter) still bind the ladder's ceiling.
- **These amendments do not touch the relative cross-check.** Amendment 20 still runs as step 1C on the Amendment 21 forward base; the adjusted peer base and the 30% governance rule operate on the run-rate earnings, and the relative exit multiple stays bounded by the sector cap.

## VERSION HISTORY

| Version | Date | Changes |
|---|---|---|
| 3.7 | 20-Aug-2026 | (prior) Amendment 17, commodity converter cycle integration. See `Section_1B_v3_7_Amendments.md`. |
| 3.8 | 23-Aug-2026 | (prior) Amendments 18-19, exit-basis symmetry, option resolution, and FV-CAGR classification. See `Section_1B_v3_8_Amendments.md`. |
| 3.9 | 26-Aug-2026 | Amendment 20, relative valuation cross-check (new step 1C), operator directive 26-Aug-2026, arising from the MANINDS valuation (pillar output 8.1-12.6x vs peer quality cluster ~30x; stale multiples caused Correction 6). 20.0 step 1C runs after the pillar build, before the verdict card; adds a display step and one governance rule, replaces neither Section 1A method selection nor the Section 1B pillar derivation. 20.1 Claude web supplies a live peer table (4-6 listed peers; trailing P/E, clean/forward P/E, ROCE, growth, net debt, governance), every figure dated and sourced; memory-pulled multiples barred (Correction 6 guard); no live table = PENDING LIVE PEER TABLE, pillar governs. 20.2 quality and value clusters identified on normalised (clean/forward) earnings. 20.3 subject placed against each cluster with stated, signed adjustments (quality, growth, governance, size/liquidity, cyclicality/converter) yielding the adjusted peer base. 20.4 bear/base/bull relative exit multiples on the entry-consistent basis (18.1), spread by observed peer dispersion. 20.5 governance rule: pillar destination >30% below the adjusted peer base (pillar < 0.70x) → relative multiple governs, pillar shown as cross-check; else pillar governs, peer table is the cross-check; divergence printed either way; 30% fixed. 20.6 sector cap still the absolute ceiling, relative multiple bounded by it; excess over cap is a cap-review flag, never silently priced. 20.7 sector caps reviewed annually against live peer medians (operator ruling, logged in the cap table). 20.8 downstream recompute on the governing multiple (exit price, FV path, FV CAGR, return-source label, entry zone); pillar retained as labelled cross-check. 20.9 operator-approved base still binds; step 1C reports divergence, never silently overwrites. Selection and display; alters no pillar math, ROCE input, premium, single-credit, or sector cap. |
| 3.9 (reissue) | 07-Sep-2026 | Amendments 21-25 added; the file reissued as one merged v3.9 on operator ruling. Numbering reconciled: the E2E set was drafted as "Amendments 20-24" by a session unaware that v3.9 / Amendment 20 (relative valuation cross-check) already existed; it is renumbered to 21-25 and every internal cross-reference is realigned. Origin: the E2E Networks AR FY25-26 review exposed that the framework structurally could not buy a fast-growing name before it re-rated. Design principle: the market pays for the probability-weighted future, not the audited past. 21 forward run-rate earnings base replaces the annual-model anchor (latest quarter annualised, one-offs adjusted, refreshed each quarter; trailing-4-quarter for seasonal names; annual model is cross-check and floor; >25% divergence stated). 22 probabilistic catalyst credit replaces binary fired/not-fired (increment × probability, quarterly Bayesian update, evidence symbols feed the probability not a gate; tier at p ≥ 0.50; mandatory two-sided downside term). 23 expectation ledger with expiry (every credited expectation logged with confirm-by date; 25% decay per missed review with proportional trim; two misses retire and raise a Role 5 DROPPED flag; ledger ferried to Notion). 24 price decomposition replaces the single fair-value verdict (T1 confirmed / T2 high-probability / T3 speculative / residual; verdict is four percentages; position size = T1 + T2; residual > 25% of CMP caps at starter; Hurdle Ratio recomputed on the Amendment 21 base). 25 margin of safety as position size for fast-growth names (starter 2-3%, add ladder on confirmation, trim ladder on decay; steady compounders keep the price-based margin of safety; top-level Gate 0 / Promoter sizing rules still bind). Companion artefacts: Appendix A Expectation Ledger template; Appendix B first worked case, E2E Networks; Appendix C operator rulings R1-R4 pending. Amendments 21-25 change the earnings base, the catalyst-credit method, and the sizing method; they do not alter the relative cross-check (Amendment 20), which now runs on the Amendment 21 forward base. |
