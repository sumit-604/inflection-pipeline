# Phase 1 verifier summary

Confidence delta

| Component | Score |
|---|---|
| Numerical acceptance (B12a) | 97 |
| Redflag coverage (B12b) | 82 |
| Framework adherence (B12c) | 95 |
| Peer utilisation (B12d) | 88 |
| Overall | 82 |

Acceptance rates: Verifier A 97%, Verifier B 82%, Verifier C 95%, Verifier D 94%.

Verifier C's valuation half is deferred to phase 3; the framework findings below cover the Gate 0 and Emerging Moat portion only.

Findings, sorted CRITICAL first, then MAJOR, then MINOR

| Severity | Verifier | Location | Note |
|---|---|---|---|
| MAJOR | B (red flags) | B05 4D red flag #1 / 2C Accountability / 4C | Broken quarterly disclosure flag (HIGH) rests on an over confident evidentiary basis; the promise is real and anchored (M25 p.11) but "broken / only one call" is inferred from an input set B05 itself labels a known collector defect, and "quarterly updates" is not necessarily "quarterly concalls". Calibration, not fabrication. |
| MAJOR | D (peers) | B06 Part 2E, MFT GmbH insolvency item | Write off stated as Rs 48.8 Cr; PRECAM Dec 2025 call states the exceptional item was Rs 49.7 Cr. Underlying claim (insolvency, full write off) correctly sourced and used; only the rupee figure is wrong. |
| MINOR | A (numerical) | B03-ardeep Phase 3C (P&L margin section) | FY25 tax provision transcribed as Rs 4.65 Cr; AR P&L p.72 shows Rs 4.85 Cr (465 vs 485 lakh). Rs 0.20 Cr error, under 0.3% of total income; effective tax rate 18.8% should read about 19.7%. Not on the verdict card. |
| MINOR | B (red flags) | B05 4D red flags / 2C Over-promotion | Humanoid treated only as aspirational and over promotion scored 4/5; M26 p.10 has a specific near term revenue over promise ("This year itself" on a trial phase >4,000 part program) not elevated to the red flag list. Partially caught. |
| MINOR | B (red flags) | B05 4D red flag #5 / B06 Part1 Q5 | Margin ambition described as "quietly cut" from +4-5pp/3-4yrs to ~1% FY27; M25 p.10 vs M26 p.4 is arithmetically within the multi year envelope and management neither restated nor abandoned the target. "Cut" overstates a low end reaffirmation; B06 Q5 premise inherits the imprecision. |
| MINOR | B (red flags) | B05 (capital allocation) | Rs 43.3 Cr preferential issue within ~18 months of the Oct 2024 IPO while Rs 20 Cr IPO proceeds still unutilized (M26 p.3; M25 p.3) noted only as a funding source, not surfaced as a capital allocation / dilution flag. |
| MINOR | C (framework, Gate 0 + EM) | B01 report end | Mandatory closing stage:B01-gate0 fenced YAML block absent from the persisted report .md; values propagated to B07 and to the block file, but the report artifact is incomplete. |
| MINOR | C (framework, Gate 0 + EM) | B01 Classification section | Grand Total labelled 66/100; correct denominator is 160 (Core 100 + Moat 60). Classification is core based and unaffected. |
| MINOR | C (framework, Gate 0 + EM) | B07 Section 2C | Unrendered {{B07_CAPEX_FIGURE}} template token leaked into 2C prose; the numeric handoff (~18%) is intact in text and YAML. |
| MINOR | D (peers) | B06 Part 2E, road tax linked export benefit | Benefit stated as halved, ~Rs 1 Cr annual hit; RACLGEAR Mar 2026 says a RoDTEP type benefit cut ~50% with management estimating "around a crore of rupees" next year. Substance and figure correct; scheme name gloss imprecise. |
| MINOR | D (peers) | B06 Part 3 coverage map, RACLGEAR Q3 row | Labelled CITED-ONLY and not decisive for Part 1; the same transcript is the sole source for a quantified Part 2E risk finding. Accurate for Part 1; undersells the Part 2 contribution. |
| MINOR | D (peers) | B06 Part 3 coverage map, RACLGEAR Q3 quarter label | Labelled Feb 2026; filed Mar 3 2026 for a call held Feb 27 2026. Call date vs filing date labeling difference, not a wrong transcript. |
