# Chunk 02. Pillar 2: cash conversion multiplier

Loaded by: Role 1 Section 1B Pillar 2, row B of the summary. Pipeline: stage 11; stage 10 (carries the structural/growth-induced determination and the rating agency quote into B10); Verifier C (12c).
Sources in force: Master v3.7 §1B Pillar 2 and Pillar 2L; Section 1B v3.3 Amendment 7; v3.6 Amendment 12A; v3.7 Amendment 17.2; FTTCP v2.3 Pillar 1 Integration (SOTP rule); v3.3 Appendix A operator decision of 02-Jul-2026.

## Cash quality bands (standard businesses)

The multiplier scales the ROCE base up or down on the quality of cash generation.

| Cash quality band | Multiplier | Description |
|---|---|---|
| CFO/PAT above 70% sustained + FCF positive | 1.30x | Elite cash machine |
| CFO/PAT 50-70% + FCF positive | 1.15x | Good cash generation with some WC drag |
| CFO/PAT 30-50% or volatile (some good years, some bad) | 1.00x | Neutral, inconsistent conversion |
| CFO/PAT below 30% or CFO negative (growth-phase drag) | 0.80x | Cash does not flow; run the structural test |
| Structurally negative, rating agency confirms persistent WC | 0.65x | Business model leaks cash |

## Structural vs growth-induced test

Before assigning the multiplier, answer: **"If this company stopped growing tomorrow, would WC days still be high?"**

- YES → Structural. The model inherently needs long cash cycles (project cargo, PSU billing, defence milestone payments, seasonal agri procurement). Assign 0.65x. No growth offset.
- NO → Growth-induced. Drag comes from capacity building, new store rollouts, inventory for new lines, or equity raised but not yet deployed. Assign 0.80x with the growth offset.
- CARE Ratings' structural WC assessment takes precedence over single-year improvements.
- Converters only: run the volume test first (third fork, below).
- An INDETERMINATE or Mixed determination has no multiplier rule in the Section 1B layers. See open ruling OR-5 in SKILL.md. CLAUDE.md caps the run verdict at PROCEED WITH CAVEATS with the missing evidence named.

## Growth offset (growth-induced drag only)

| PAT/Revenue CAGR | Offset to the cash multiplier |
|---|---|
| Above 40% CAGR + growth-induced | +0.20 |
| 25-40% CAGR + growth-induced | +0.10 |
| Below 25% CAGR | +0.05 |
| Structural (rating agency confirms) | 0, no offset |

## Government customer tier rule

The worst tier representing more than 25% of revenue sets the multiplier, not an average. Tier 1 Maharatna/Navratna PSUs → neutral treatment. Tier 3 state DISCOMs → 0.65-0.75x structural multiplier regardless of growth. Tier 4 direct state/municipal → defaults to WATCHLIST.

## Third fork: input-price-driven working capital (CONVERTER names only, Amendment 17.2)

Recompute WC days on volumes or constant prices. If WC per unit is stable while WC in rupees swings, the swing is INPUT-PRICE-DRIVEN: assign 1.00x neutral, no growth offset, no structural penalty. Every converter cash-quality trend claim, including the FTTCP Cash transition feed, is made on volume-denominated WC only. Rating-agency language separating price-led from cycle-led WC is admissible evidence. See chunk 11.

## SOTP rule for hybrid annuity-EPC businesses

For material BOO / Ind AS 116 finance-lease components, do not apply the cash multiplier penalty to the BOO portion; structural cash lag is the business model there. EPC, manufacturing or telecom portion → standard four pillars with the cash multiplier. BOO/annuity portion → InvIT-style multiple of 10-14x EV/EBITDA, set by counterparty quality and equity IRR against cost of capital. Blended destination = weighted average. The blended sector cap is in chunk 05.

## Cash quality is priced once

- Pillar 2 owns cash quality. The required return r carries no cash-conversion adjustment (Amendment 12A).
- Growth and Strategic Premiums are not scaled by the cash multiplier (operator decision, 02-Jul-2026). Cash quality is policed in Pillar 2's structural test and in FTTCP Transition 3, which caps or kills a verdict before valuation when cash conversion is DECLINING with no catalyst.
- FTTCP validates the multiplier against the forward cash verdict.

## Pillar 2L: Asset-Quality Multiplier (lenders only, replaces the cash multiplier)

| Asset-quality band | Multiplier | Description |
|---|---|---|
| Credit costs stable/declining 2+ yrs, GNPA <2%, PCR >70% | 1.15x | Elite underwriting |
| GNPA 2-4% and stable, PCR 60-70%, credit costs within guided band | 1.00x | Sound |
| GNPA rising OR >4%, PCR <60%, credit cost guidance missed once | 0.80x | Stressed |
| Rising credit costs + PCR <50% + growing restructured/written-off book | 0.65x | Structural underwriting weakness |

- No growth offset. Loan growth compounds bad underwriting.
- P/B (theoretical P/B = ROE ÷ CoE) is the PRIMARY method for lenders; the Section 1B destination PE is the SECONDARY cross-check.
- The band must be consistent with the Role 4 Step 5L asset-quality table and the FTTCP lender Transition 3 verdict.
- Part B modules apply to lenders where meaningful (operating-earnings separation, incentive normalization, complexity discount in r). Cash-conversion and reinvestment-funding modules defer to the lender asset-quality and NIM machinery.

## Worksheet lines

- "Cumulative CFO/PAT: ___ | Latest FY CFO/PAT: ___ | FCF positive? ___"
- "Cash quality band: ___ | Base multiplier: ___x"
- "Structural or growth-induced? ___ | Evidence: [rating agency / deep dive finding]"
- "Growth offset applicable? ___ → offset: +___"
- "Effective Cash Multiplier: ___x"
- "Quality-Adjusted Base: ROCE Base × Cash Multiplier = ___x × ___x = ___x"
