# SECTION 1B v3.9 AMENDMENTS — RELATIVE VALUATION CROSS-CHECK (STEP 1C)

*Version 3.9 | 26 August 2026 | Relative valuation cross-check, operator directive 26-Aug-2026, arising from the MANINDS valuation (pillar output 8.1-12.6x against a peer quality cluster ~30x; stale multiples in Claude web's memory caused Correction 6). Layers on top of Section 1B v3.3 + v3.3 Amendments + v3.5.1 + v3.6 + v3.7 + v3.8. It does not modify any prior file in place. Where they overlap on items named here, v3.9 governs. Stage 11 reads this alongside the earlier Section 1B files. Amendments number continuing from v3.8 (whose last amendment is 19).*

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

## INTERACTION WITH THE REST OF THE FRAMEWORK

- **Step 1C changes exit-multiple SELECTION, not pillar math.** Amendment 20 derives no new pillar, ROCE input, or premium. It selects the governing exit multiple between the pillar destination and the adjusted peer base, bounded by the sector cap. Pillar 1/2/3 derivation, single-credit, and the v3.5.1 route selection are untouched.
- **The sector cap remains absolute.** 20.6 restates it: nothing in Amendment 20 raises or lowers a cap. 20.7's annual review is the only channel that moves a cap, and it is an operator ruling logged in the cap table, not a per-run act.
- **Basis symmetry (v3.8 Amendment 18.1) binds the relative exit.** The relative multiple applies to the SAME earnings basis the entry used, on normalised earnings. Mixing bases is barred here as everywhere.
- **Converter placement (v3.7 Amendment 17.1) binds subject placement.** A converter subject is placed against peers on through-cycle earnings, never spot; a converter slice resolving successfully still exits on its own converter multiple (18.3), which step 1C does not lift.
- **Amendment 19's display duty is preserved.** When the relative multiple governs, the FV path, FV CAGR, and return-source label are recomputed on the governing multiple (20.8); the verdict card and Role 2 Section 5 carry the recomputed lines.
- **Team-workflow split.** Step 1C is a Claude web step: it needs live market data Claude Code does not hold. In pipeline mode Code marks the slot PENDING LIVE PEER TABLE and the pillar governs until claude.ai supplies the live table. See the ferry payload `docs/team_workflow_amendments_maninds_2026-08-26.md`.
- **Correction 6 guard.** Every peer multiple carries a live source and date; memory-pulled multiples are barred (20.1). A table without live dated figures cannot govern.

## VERSION HISTORY

| Version | Date | Changes |
|---|---|---|
| 3.7 | 20-Aug-2026 | (prior) Amendment 17, commodity converter cycle integration. See `Section_1B_v3_7_Amendments.md`. |
| 3.8 | 23-Aug-2026 | (prior) Amendments 18-19, exit-basis symmetry, option resolution, and FV-CAGR classification. See `Section_1B_v3_8_Amendments.md`. |
| 3.9 | 26-Aug-2026 | Amendment 20, relative valuation cross-check (new step 1C), operator directive 26-Aug-2026, arising from the MANINDS valuation (pillar output 8.1-12.6x vs peer quality cluster ~30x; stale multiples caused Correction 6). 20.0 step 1C runs after the pillar build, before the verdict card; adds a display step and one governance rule, replaces neither Section 1A method selection nor the Section 1B pillar derivation. 20.1 Claude web supplies a live peer table (4-6 listed peers; trailing P/E, clean/forward P/E, ROCE, growth, net debt, governance), every figure dated and sourced; memory-pulled multiples barred (Correction 6 guard); no live table = PENDING LIVE PEER TABLE, pillar governs. 20.2 quality and value clusters identified on normalised (clean/forward) earnings. 20.3 subject placed against each cluster with stated, signed adjustments (quality, growth, governance, size/liquidity, cyclicality/converter) yielding the adjusted peer base. 20.4 bear/base/bull relative exit multiples on the entry-consistent basis (18.1), spread by observed peer dispersion. 20.5 governance rule: pillar destination >30% below the adjusted peer base (pillar < 0.70x) → relative multiple governs, pillar shown as cross-check; else pillar governs, peer table is the cross-check; divergence printed either way; 30% fixed. 20.6 sector cap still the absolute ceiling, relative multiple bounded by it; excess over cap is a cap-review flag, never silently priced. 20.7 sector caps reviewed annually against live peer medians (operator ruling, logged in the cap table). 20.8 downstream recompute on the governing multiple (exit price, FV path, FV CAGR, return-source label, entry zone); pillar retained as labelled cross-check. 20.9 operator-approved base still binds; step 1C reports divergence, never silently overwrites. Selection and display; alters no pillar math, ROCE input, premium, single-credit, or sector cap. |
