# Chunk 04. Strategic asset premium and the single-credit rule

Loaded by: Role 1 Section 1B Strategic Premium, row E of the summary. Pipeline: stage 11; stage 15 (stress-tests every SHARED CATALYST); Verifier C (12c).
Sources in force: Master v3.7 §1B Strategic Asset Premium and Consumption Clause; Section 1B v3.3 Amendment 4; v3.5.1; v3.6 Amendments 12, 13; v3.7 Amendment 17.1; v3.8 Amendment 18.3; v3.9 Amendments 20.5, 22; v3.10 Amendment 26; FTTCP v2.3 Pillar 1 Integration, empirical context and Part B single-credit map; Rule G.

## Strategic asset premium

For documented rare or monopoly positions that the market structurally premiums: genuine scarcity that limits new entry, not merely a strong moat.

| Strategic position type | Premium |
|---|---|
| Rare licence / regulatory monopoly (e.g. phosgene licence, defence MMIC, sovereign cloud) | +4 to +6x |
| Strong brand / franchise with limited competition and documented pricing power | +2 to +4x |
| ROCE re-rating optionality (ONLY if recovery was NOT credited in Pillar 1) | +1 to +2x |
| Turnaround with institutional backing (GIC, Tata group, etc.) | +1 to +2x |
| No strategic scarcity | +0x |

Catalysts behind a strategic premium are credited at increment × probability under Amendment 22 (chunk 09). See open ruling OR-3 in SKILL.md.

## ROCE re-rating optionality

- Default home for ROCE recovery is Pillar 1. The Strategic Premium route is permitted only when the FTTCP ROCE forward verdict is STAGNANT or FIRING (no forward uplift entered Pillar 1) and archetype-supported re-rating optionality genuinely exists.
- Sizing is archetype-dependent: asset-light recovering to ROCE >25% → +2x; asset-heavy recovering to >20% → +1x; BOO / infrastructure treadmill (ROCE cycles, does not expand) → 0x.
- The empirical ROCE-led re-rating tables end at FY21-22 peak-cycle multiples. For planning, use the lower bound of the 1.5-2.5x re-rating estimate. The +1x/+2x sizing already reflects this.

## The single-credit map (one quality improvement, one mechanism)

Each distortion or improvement is credited in exactly one place. Role 1 verifies this map before valuing. State the choice in writing wherever the table says so.

| Improvement or distortion | Credited in exactly one of | Source |
|---|---|---|
| ROCE recovery | Pillar 1 (FTTCP ROCE table) OR Strategic Premium | A4; FTTCP Pillar 1 Integration |
| Capital-cycle ROCE normalization | Route A (operational) OR Route B (pre-cycle) | v3.5.1 consolidated A9 |
| Capital-base distortion | Route A/B OR FTTCP Module B6 | FTTCP Part B map |
| Depressed base year | FTTCP Module B3 OR Route B | FTTCP Part B map |
| Converter through-cycle ROCE | computed after the declared route, never a second credit | A17.1 |
| Cash quality | Pillar 2 only; never also in r | A12A |
| Short public record | Unproven durability band only; no r surcharge | A12C |
| Cyclicality docked in the durability band | cyclical r surcharge capped at +0.75 | A12B |
| Structural complexity | r only (+0.5); never a pillar, premium or cap | A13 |
| Catalyst in base-case revenue | revenue at probability OR Pillar 3 at full weight; state the split | A26 interaction with A22 |
| Entrepreneur Ledger fact | Pillar 3 OR Strategic Premium | Rule G |
| Quality already inside the pillar build | not re-credited through a peer multiple | A20.5 |
| Converter option slice resolving successfully | exits on its own converter multiple, never the core multiple | A18.3 |
| Every credited expectation | on the Expectation Ledger once, at its probability | A22, A23 |

Crediting the same ROCE improvement through Pillar 1, the Strategic Premium and a lower discount rate is triple-counting and must be caught.

## Shared-catalyst flag

If the same catalyst (for example a capex commissioning) drives both the Pillar 1 forward ROCE and the Pillar 3 premium, this is permitted, because the premiums measure different things. Flag it "SHARED CATALYST" so Role 3 stress-tests the single point of failure.

## Worksheet lines

- "Strategic position: ___ | Strategic Premium: +___x"
- "ROCE recovery credited via: [Pillar 1 / Strategic Premium / not credited]"
- "Single-credit map verified: [ROCE recovery ___ | capital base ___ | base year ___ | catalyst split revenue ___% / Pillar 3 ___%]"
