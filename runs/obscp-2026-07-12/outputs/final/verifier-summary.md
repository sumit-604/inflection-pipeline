# Verifier summary (phase 1 + phase 3)

Confidence delta

| Component | Score |
|---|---|
| Numerical acceptance (B12a) | 97 |
| Redflag coverage (B12b) | 82 |
| Framework adherence (B12c, both halves) | 96 |
| Peer utilisation (B12d) | 88 |
| Overall | 82 |

Acceptance rates: Verifier A 97%, Verifier B 82%, Verifier C 96% combined (Gate 0 and Emerging Moat 95%, valuation adherence 97%), Verifier D 94%.

REWORK not triggered: all four verifiers, including Verifier C on both halves, returned zero CRITICAL; minimum acceptance rate is 82; overall 82 sits in the normal band (75 to 89).

Findings, sorted CRITICAL first, then MAJOR, then MINOR

| Severity | Verifier | Location | Note |
|---|---|---|---|
| MAJOR | B (red flags) | B05 4D red flag #1 / 2C Accountability / 4C | Broken quarterly disclosure flag (HIGH) rests on an over confident evidentiary basis; the promise is real and anchored (M25 p.11) but "broken / only one call" is inferred from an input set B05 itself labels a known collector defect, and "quarterly updates" is not necessarily "quarterly concalls". Calibration, not fabrication. |
| MAJOR | D (peers) | B06 Part 2E, MFT GmbH insolvency item | Write off stated as Rs 48.8 Cr; PRECAM Dec 2025 call states the exceptional item was Rs 49.7 Cr. Underlying claim (insolvency, full write off) correctly sourced and used; only the rupee figure is wrong. |
| MINOR | A (numerical) | B03-ardeep Phase 3C (P&L margin section) | FY25 tax provision transcribed as Rs 4.65 Cr; AR P&L p.72 shows Rs 4.85 Cr (465 vs 485 lakh). Rs 0.20 Cr error, under 0.3% of total income; effective tax rate 18.8% should read about 19.7%. Not on the verdict card. |
| MINOR | B (red flags) | B05 4D red flags / 2C Over-promotion | Humanoid treated only as aspirational and over promotion scored 4/5; M26 p.10 has a specific near term revenue over promise ("This year itself" on a trial phase >4,000 part program) not elevated to the red flag list. Partially caught. |
| MINOR | B (red flags) | B05 4D red flag #5 / B06 Part1 Q5 | Margin ambition described as "quietly cut" from +4-5pp/3-4yrs to ~1% FY27; M25 p.10 vs M26 p.4 is arithmetically within the multi year envelope and management neither restated nor abandoned the target. "Cut" overstates a low end reaffirmation; B06 Q5 premise inherits the imprecision. |
| MINOR | B (red flags) | B05 (capital allocation) | Rs 43.3 Cr preferential issue within ~18 months of the Oct 2024 IPO while Rs 20 Cr IPO proceeds still unutilized (M26 p.3; M25 p.3) noted only as a funding source, not surfaced as a capital allocation / dilution flag. |
| MINOR | C (framework, valuation, phase 3) | B11 Section 1B, Pillar 2 growth offset | +0.20 growth offset justified on PAT CAGR 48.7% and single year revenue 54%; the anchored 3yr revenue CAGR 38.5% maps to the 25-40% band and +0.10. The 1.00x multiplier holds independently via cumulative CFO/PAT 0.31 in the neutral band, so destination PE, Hurdle STOP and the AVOID decision are unchanged; the stricter +0.10 reading only lowers destination PE and reinforces AVOID. 33 of 34 valuation rules clean. |
| MINOR | C (framework, Gate 0 + EM) | B01 report end | Mandatory closing stage:B01-gate0 fenced YAML block absent from the persisted report .md; values propagated to B07 and to the block file, but the report artifact is incomplete. |
| MINOR | C (framework, Gate 0 + EM) | B01 Classification section | Grand Total labelled 66/100; correct denominator is 160 (Core 100 + Moat 60). Classification is core based and unaffected. |
| MINOR | C (framework, Gate 0 + EM) | B07 Section 2C | Unrendered {{B07_CAPEX_FIGURE}} template token leaked into 2C prose; the numeric handoff (~18%) is intact in text and YAML. |
| MINOR | D (peers) | B06 Part 2E, road tax linked export benefit | Benefit stated as halved, ~Rs 1 Cr annual hit; RACLGEAR Mar 2026 says a RoDTEP type benefit cut ~50% with management estimating "around a crore of rupees" next year. Substance and figure correct; scheme name gloss imprecise. |
| MINOR | D (peers) | B06 Part 3 coverage map, RACLGEAR Q3 row | Labelled CITED-ONLY and not decisive for Part 1; the same transcript is the sole source for a quantified Part 2E risk finding. Accurate for Part 1; undersells the Part 2 contribution. |
| MINOR | D (peers) | B06 Part 3 coverage map, RACLGEAR Q3 quarter label | Labelled Feb 2026; filed Mar 3 2026 for a call held Feb 27 2026. Call date vs filing date labeling difference, not a wrong transcript. |

Note on Verifier A: the first pass returned two false CRITICALs (faithfully transcribed company anomalies, the diluted EPS above basic EPS and the negative short term provisions, mislabelled by severity). The orchestrator sanity checked against LESSONS (KARNIKA 2026-07-11) and re invoked once; the source grounded re run returned 0 CRITICAL and 97%. Both anomalies MATCH the audited AR exactly, so they are company accounting issues, not pipeline errors, and do not trigger REWORK.

Note on Verifier C valuation half (phase 3): 34 rules checked, 33 clean; recomputed destination PE concurs at 20.1x additive and 16.5x RRM, and the Hurdle STOP and AVOID decision both recompute and concur.
