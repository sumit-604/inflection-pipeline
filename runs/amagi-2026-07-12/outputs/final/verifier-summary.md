=== FILE: verifier-summary.md ===

# Phase 1 verifier summary

## Confidence delta and acceptance rates

| Component | Score | Verifier | Acceptance rate |
|---|---|---|---|
| Numerical accuracy | 93.6 | A (B12a) | 93.6 |
| Red flag coverage | 63 | B (B12b) | 63 |
| Framework adherence (Gate 0 + Emerging Moat) | 96.7 | C (B12c) | 96.7 |
| Peer utilisation | 92 | D (B12d) | 92 |
| Overall | 63 | min | band 60 to 74 |

Overall 63, red flag bound. Band 60 to 74 downgrades any PROCEED family verdict one level; not forced REWORK (no CRITICAL, no acceptance rate below 60). Verifier C valuation adherence half is pending phase 3.

## Findings, sorted by severity

### CRITICAL

None across A, B, D, or the Gate 0 and Emerging Moat scope of C.

### MAJOR

| Verifier | Location | Note |
|---|---|---|
| B | B05 cash conversion gap (Feb call p.5-6; May call p.9) | No cash conversion red flag raised: FY26 adjusted FCF Rs 38cr is about 24% of adjusted EBITDA Rs 156cr; 9M reported OCF negative Rs 76cr; adjusted OCF strips IPO and ESOP buyback cash, against the INDETERMINATE cash conversion rule. |
| B | B05 sections 2A/4D revenue quality | FX flattered growth not flagged: 30% reported versus 23% constant currency, about 7 points of FX; NRR ticked 127 to 126; constant currency NRR only north of 120%. |
| B | B05 section 3C customer adds | Net logo adds decelerated more than 50%, 67 to 29, and Q4 net negative (27 added, 30 churned); B05 rated the risk Low, under weighted alongside softening constant currency NRR. |
| B | B05 contradiction, Feb call (p.11 vs p.18) | Missed intra call contradiction on perpetual license overhang between Vijay (drove the H1 swing) and Baskar (no overhang), same February 2026 call. |
| D | B06 Part 1 Claim 5 peer evidence row; B06 top level flags (RateGain item) | B06 overstated RateGain disclosure proactiveness: the lost client (4% of MarTech revenue) and NRR figures were first raised by analysts in the November 11 2025 call, not volunteered by management. The underlying comparison to Amagi's initial purely strategic framing still holds; correct the framing. |

### MINOR

| Verifier | Location | Note |
|---|---|---|
| A | B02 Finding #2; B04 Section 1E | AWS Technology Agreement six year commitment Rs 24,176.20mn sourced via B02 secondary report interpretation, not independently extracted from full Prospectus text (Sep 30 2025 contingent Rs 22,531.72mn confirmed). |
| A | B02 Finding #3; B03 Phase 1 p.41 | Transfer pricing contingent Rs 592.48mn and total tax litigation Rs 1,175.07mn cited via Prospectus p.417-420 but not independently extracted; material for governance, does not affect the core scorecard. |
| A | B04 Section 1C line 60 | H1 FY26 segment split (Streaming 52.86%, Monetization 25.28%, Cloud Modernization 21.86%) cited via Prospectus p.236 but not independently verified; percentages sum to 100%, mechanical check passes. |
| B | B05 section 1B | Underlying growth number drifts 30% to 27% to 26% within the Feb call; pipeline fixes it as a single 25 to 30%. |
| B | B05 red_flags | Q3 largely able to hold price versus Q4 rate haircut admission not called out as its own contradiction. |
| B | B05 section 3B | Streaming, more than half of revenue, is the slowest segment (26% reported, about 19% constant currency); all three over 25% is reported INR framing. |
| C | B01 Block C / C2 | PAT CAGR 28.18% scored 5 via the endpoint CAGR edge rule; correct per the literal rubric and the loss path was logged. DECISION SENSITIVE: if C2 were 0, Core = 39 and classification AVOID rather than AVERAGE. Flag for synthesis awareness. |
| C | B01 Block B / B3 | Mechanical band 5 for literal +0.82 overridden to 0 as a double negative artifact; unauthorised by the written rubric but conservative, transparently flagged, and immaterial to destination (Core would be 49, still AVERAGE). |
| C | B01 Block A / ROCE denominator | Used Other Liabilities as a current liabilities proxy for FY2021 to FY2025 because the source does not split current and non current; disclosed and immaterial, every A line scores 0 regardless. |
| C | B07 Section 2C / YAML capex_embedded_growth_pct | NOT APPLICABLE result correctly un estimated in prose but rendered as numeric 0 in the YAML; risks a downstream misread as a scored zero growth input. |
| C | B07 Section 6D combined classification | HIGH POTENTIAL assigned on an AVERAGE backward plus STRENGTHENING forward (30.0, below the 40 EXPANSION threshold) pairing; reasoning disclosed and symmetric, sits at the generous end of a defensible range. Flag for synthesis to confirm mapping. |
| C | B07 D1/D2 throughput KPIs | D1 and D2 both draw on the same KPI dashboard; the maker separated the network effect double count and discounted D1 to 0.7x, so overlap is handled; noted so synthesis does not re credit the throughput KPIs a third time. |
| D | B06 Part 3 Peer Coverage Map, Newgen Q2 FY26 (Nov 2025 call) | The nothing material competitive framing quote attributed to this call appears only in Newgen's Jul 2025 (Q1 FY26) call; does not affect Claim 3, which cites a different verified quote from the Jan 2026 call. |

## Positive confirmations (Verifier C, Gate 0 and Emerging Moat scope)

- FLAG-GATE0 is legitimate driver attribution, not laundering: classification stays AVERAGE, all binding deal breakers stay binding, driver years FY22 to FY25 named, self limited to one clean post-IPO year.
- Deal breaker logic correct and complete; the only AVOID trigger (net debt to EBITDA above 3x and interest cover below 3x) correctly not triggered (net cash, interest cover 15.42x).
- Emerging Moat evidence taxonomy honest; D1 (CEO self characterisation) correctly held at claim tier 0.7x Moderate, not documented Strong.
- No double counting enforced; completionist recount performed (7 active categories below the 12 guard); em_score 30.0 arithmetic correct; EM and FTTCP not conflated.
