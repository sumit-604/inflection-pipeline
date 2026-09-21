# Chunk 05. Sector cap table, UA multiplier and the Category-Break Override

Loaded by: Role 1 Section 1B rows F2, G, G2, G3 of the summary. Pipeline: stage 11 (cap row arrives from the manifest via B10); /step1 (writes the manifest sector cap row); /fttcp (sector cap row sanity check against B04); Verifier C (12c).
Sources in force: Master v3.7 §1B Undiscovered Alpha, Sector Reality Cap, Category-Break Override and v3.5 reconciliation note; Section 1B v3.3 Amendments 1, 3, 8; v3.7 Amendment 17.5; v3.9 Amendments 20.6, 20.7, Appendix C R1; v3.10 Amendment 26.5; FTTCP v2.3 Sector Cap and Category-Break Override, SOTP rule.

## The ordering

**Final Destination PE = min( Raw PE × UA multiplier, Sector Cap × Override multiplier )**

- UA multiplier = 1.25 when all three qualifiers hold, else 1.00. It applies to the RAW destination PE before the cap comparison.
- Override multiplier = 1.40 when the Category-Break Override qualifies, else 1.00. The 45x absolute ceiling always binds after the multiplication.
- Absent a qualified override, the sector cap is absolute. UA can never breach it.
- There is no numeric exit-PE ceiling other than the sector cap (Amendment 26.5). Section 1B governs the destination PE through the four pillars, the sector cap, the UA uplift and the Category-Break Override.

## Undiscovered Alpha multiplier

- Qualifiers, ALL three: listed ≥12 months; Gate 0 ≥60/100 OR Emerging Moat ≥25/100; FII+DII combined <3%.
- Institutional absence in quality-cleared micro-caps is a positive alpha signal. SME listing creates structural mandate exclusion, not informed avoidance. Never flag low institutional ownership as a risk.
- The same 1.25x applies to the raw Inflection Alpha ranking score.

## Sector cap table

| Sector | Maximum exit PE |
|---|---|
| Platform / SaaS / IT services | 45x |
| Consumer franchise / Jewellery | 40x |
| Pharma / CDMO | 38x |
| Defence / strategic | 38x |
| Branded apparel / FMCG | 35x |
| Specialty chemicals | 35x |
| Hospitals / dialysis / healthcare services | 35x |
| Fluorochemicals / industrial gases | 30x |
| Hotels | 30x |
| Telecom equipment | 30x |
| Data centers / cloud infrastructure (capital-heavy) | 30x |
| CPaaS / Communications platform | 28x |
| EV charging / energy transition equipment | 28x |
| Cables / Industrial products | 25x |
| Recycling / Manufacturing | 25x |
| Logistics (asset-light) | 25x |
| Cybersecurity / VAD | 25x |
| Consulting / Engineering services | 25x |
| Packaging | 22x |
| Building materials | 22x |
| City gas distribution | 22x |
| Logistics (WC-heavy / project cargo) | 20x |
| EPC / Civil construction | 20x |
| Real estate | 20x |
| Agri processing | 20x |
| Mining / mineral exploration | 20x |
| Banks / NBFCs / MFIs | 18x (P/B primary; PE is cross-check only) |

Pending ruling: Section 1B v3.9 Appendix C R1 (a blended cap row for infra-plus-platform businesses, for example 35x, raised by the E2E Networks case). Until ruled, classify to an existing row and state the classification.

## Quality uplift

When UA is triggered AND durability is at least Moderate-Strong with documented evidence, a minimum 25% quality uplift on the sector cap applies. State the uplifted cap explicitly when used. See open ruling OR-4 in SKILL.md.

## SOTP blended cap (hybrid annuity-EPC)

Revenue-weighted blend: pure EPC 20x; BOO / InvIT-equivalent 14-16x; manufacturing 25-30x. The Pillar 2 SOTP rule is in chunk 02.

## Converters

Amendment 17 does not lower or raise any cap. Caps already price the sector through the cycle.

## Category-Break Override

The narrow, evidence-heavy mechanism for a company establishing a genuinely new category. It is not a general escape for high-growth stories, and it is never automatic.

### Four qualifying conditions (all must hold)

| # | Condition | Test |
|---|---|---|
| 1 | First-mover in a new category | Name the specific market that did not exist as a purchasable good three years ago, or the exclusive partnership, or the technology/regulatory threshold recently crossed |
| 2 | Explicit customer or partner commitment | Named binding contract, framework agreement or exclusive tie-up, signed and disclosed. LOI, MOU and concall commentary do not qualify |
| 3 | Capex commissioning timeline | Documented schedule mapping the category buildout to a specific quarter or half. "In due course" does not qualify |
| 4 | Competitor absence | Independent verification (exports data, customs filings, RBI/DGCI&S, independent sector research) that no listed competitor of comparable scale produces to the same specification or serves the same customer |

If any condition is missing or thin, the override is denied and the sector cap holds.

### Evidence bar: three independent primary sources (📄 only)

- Customer commitment source (exchange filing, customer's own filing, or contractual document).
- Capex commissioning source (audited CWIP note, exchange announcement, or contractor disclosure).
- Competitor-absence source (exports data, RBI/DGCI&S, or independent research; never the target company's narrative).
- Rating agency, sector association or independent research may substitute for the competitor-absence source only. Management concalls and investor presentations count as ZERO sources.

### Magnitude, sunset, documentation, stress test

- Override-adjusted cap = min( Sector Cap × 1.40, 45x ).
- Sunset: four quarters, no automatic renewal. On expiry the cap reverts unless all four conditions are re-documented with fresh primary sources in the current cycle. Renewal without fresh evidence is an error, unwound at the next quarterly refresh.
- Notion COMPANIES MASTER Key Notes entry, prepended: date invoked; sunset date (invocation + 12 months, quarter-end); conditions 1-4 in one sentence each; three primary sources with URL or document reference; baseline cap and override-adjusted cap; Role 3 stress-test summary. An override without complete documentation is invalid and reversed at the next quarterly review.
- Role 3 must produce, for each condition, a plausible 12-month removal scenario. If any scenario is plausible, the override is denied at inception or entered with a 2-quarter sunset.
- The override touches ONE thing: the cap. It does not raise the ROCE base, the cash multiplier, the growth premium, the strategic premium, or the RRM track.

Post-override examples: Data centers 30x → 42x; Pharma/CDMO 38x → 45x (ceiling binds); Specialty chemicals 35x → 45x (ceiling binds); Cables/Industrial 25x → 35x; EPC 20x → 28x.

## Display when both lifts could apply

Show row G as the quality-uplifted cap and row G3 as the override-adjusted cap. The higher effective cap governs. G3 = min(G × 1.40, 45x) when the override qualifies, so H = min(F2, G3). The 45x ceiling binds everything.

## Cap maintenance (Amendments 20.6, 20.7)

- A relative exit multiple is bounded by the sector cap. Where the adjusted peer base exceeds the cap, the cap binds and the excess is recorded as a cap-review flag, never priced in.
- Caps are reviewed annually against live peer medians. Where a sector's live peer median clean/forward multiple has moved durably away from the cap, the operator re-rules the cap, logged in the cap table with date and evidence. A per-run cross-check never breaches a cap.

## Worksheet lines

- "Sector: ___ → Cap: ___x (quality-uplifted: Y/N, basis ___)"
- "UA qualifiers: listed ≥12m ___ | Gate 0 ≥60 or EM ≥25 ___ | FII+DII <3% ___ → UA applied: Y/N"
- If G2 = Y: "Sunset date: ___ | Three primary sources: [1] ___ [2] ___ [3] ___ | Role 3 stress-test outcome: [PASSED / SHORTENED SUNSET / DENIED]"
