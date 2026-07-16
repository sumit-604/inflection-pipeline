# Phase 1 verifier summary — Fluidomat Ltd

## Confidence delta and acceptance rates

| Component | Score | Verifier | Acceptance rate |
|---|---|---|---|
| Numerical | 94 | A (B12a, haiku) | 94.0 (182 numbers; 0 CRITICAL, 4 MAJOR, 2 MINOR, 4 UNANCHORED) |
| Redflag coverage | 79 | B (B12b, opus, no concall) | 79 (14 flags; 8 caught, 3 partial, 3 missed all MINOR) |
| Framework adherence (Gate 0 + Emerging Moat only) | 96 | C (B12c, opus) | 96 (76/79 rules; valuation half deferred to phase 3) |
| Peer utilisation | 80 | D (B12d, sonnet) | 80 (5 audited, 4 substantive; all 5 claim verdicts hold) |
| Overall | 79 | min, redflag bound | normal band (75-89); no confidence driven downgrade; REWORK not triggered |

No CRITICAL defects across any verifier. No acceptance rate below 60%. No REWORK.

## Findings sorted by severity

### MAJOR

| Verifier | Location | Finding |
|---|---|---|
| C | B07 Section 5 scorecard, R1 row | Non framework "blended 0.85x" evidence multiplier; reported EM total 12.0 sits on the MODEST boundary and depends on the invented multiplier. Defined tier recompute gives 11.5 (NONE) or 12.4 (MODEST). Combined assessment AVERAGE survives either way. |
| D | Claim 2, peer evidence bullet 1 | Quoted "18.2 percentage" for ELECON Q2 FY26 EBIT margin decline is a blend/mismatch; the actual Q2 FY26 transcript states 19.2 percentage (18.2 belongs to a different quarter's comparison). Underlying mix/employee cost margin claim remains independently supported. |
| D | Claim 1, peer evidence bullet 1 | ELECON Q4 FY26 Gear revenue decline quote attributed to Chintan Shah, CFO, but actually spoken by Aayush Shah, Director, in the opening overview. |
| A | B05 Section 1 (p.6-9) | FY26 revenue growth stated +0.4% (7246.14 vs 7218.29 lakh, AR/results basis); screener basis gives +2.55% (72.46 vs 70.66cr). Rooted in the FY25 screener versus AR regrouping already flagged by B01 as a known restatement effect. |
| A | B05 Section 2A (p.48-50) | Capex completion date conflicts within one document: "by end 2027" (Journey slide) vs "FY26-FY29E" (Capex slide) for the same Rs 35cr programme, span 14+ months. Correctly identified as a genuine internal inconsistency. |
| A | B04/B05 order booking (p.130-131) | FY25 order booking Rs 5,815.76L (-3.12% YoY) verified internally; the metric then disappeared from all FY26 filings. Risk signal flagged by B05. |
| A | B05 Section 1 (p.165-166) | Rs 35cr capex is single sourced to the 29-Jun-2026 Investor Presentation; no primary board resolution or SE announcement provided. B05 flags this as a single source anchor. |

### MINOR

| Verifier | Location | Finding |
|---|---|---|
| C | B07 Section 2C / capex_embedded_growth_pct | Framework prescribes capex x historical FAT (Method B, +245%); maker reported capacity unit Method A (+133%). Both shown, deviation reasoned. |
| C | B07 YAML evidence_mix vs completionist_recount | documented:15 versus "6 documented items" unreconciled scopes; no guard breach, no score impact. |
| C | B01 Block B, B2/B3 | Band thresholds applied to the 2 year FY25-26 subset while B1 uses the full 10 year window; compliant with grounded claims and flagged; no classification impact. |
| B | B05 4D/red_flags | Missed related party lease from ED Kunal Jain to the Company (Rs 2.48 lakh, Note 45c); folded into the generic family concentration flag. |
| B | B05 4D/red_flags | Missed related party purchase from Focus Eye Technocraft P.Ltd (Rs 2.69 lakh, Note 45c). |
| B | B05 2D | Under weighted: Investor Presentation omits the 9M/Q3 FY26 trough (Q3 PAT -58% YoY), showing only Q4 rebound and flat FY; selective framing mechanism not named. |
| B | B05 2C/2D | Missed presentation internal inconsistency: slide 24 PAT margin/EPS charts mislabelled versus slide 23. |
| B | B05 2D | Under weighted stale related party list (Note 45a lists former IDs as current; Fluidomat UK shown as present wholly owned subsidiary post divestment). |
| B | B05 3D | Under weighted cash conversion deterioration: FY26 CFO 1074.98 lakh vs PAT 2006.18 lakh (about 54%), CFO -25% YoY on receivables +32%, management narrative silent. |
| B | B06 inputs | Peer transcripts absent from run inputs; B06 peer quotes unverifiable from provided artifacts. Deferred to Verifier D; sourcing traceability limitation, not asserted fabrication. |
| D | Claim 3, peer evidence bullet 2 | ELECON Q1 FY26 capex quote ("FY26 to FY28 is INR400 crores") attributed to Kamlesh Shah; actual speaker was Narasimhan Raghunathan, CFO. |
| D | Claim 5, peer evidence bullet 2 | International revenue share stated as "21-24% in earlier FY26 quarters"; Q1 FY26 was actually 25% overseas, outside the stated range. Cosmetic, no verdict effect. |
| D | Part 2E, risk 5 (defense order margin drag) | Q3 FY26 Navy order margin commentary attributed to "Chintan Shah/Dipak Dalwadi"; actual speaker was Narasimhan R. ELECON's own figure is internally inconsistent (0.5% Q3 vs 1-2% Q4); B06 does not flag this self contradiction. |
| D | Part 2E, risk 1 (tariff/geopolitical) | "50% US tariffs under Section 2(32)" attributed to Aayush Shah, Director; transcript tags this specific answer as unnamed "Management". |
| D | Claim 3 / peer_coverage_map, Q3 FY26 | Q3 FY26 EP/CP mix (48%/52%) attributed to Narasimhan R.; transcript tags this line as unnamed "Management". |
| A | B02 Pass 3 finding #5 (p.87) | Disinvestment proceeds CFS Rs 16.54L vs Note/Annexure Rs 13.70L (FY24), unreconciled Rs 2.84L gap within the AR. Immaterial quantum, disclosure quality gap. |
| A | B02 Pass 3 finding #6 (p.88) | Headline EPS 45.15/28.23 computed on Total Comprehensive Income rather than net profit; mathematically correct but non standard versus Ind AS 33. |

### UNANCHORED (source PDFs not text extractable, not defects)

| Verifier | Location | Note |
|---|---|---|
| A | B01 Block B (p.69-70) | FY25 capex Rs 6.4423cr, FY26 capex Rs 3.2656cr anchored to results FY26 annual p.6; internally consistent across B01/B03 but original PDF not independently verifiable. |
| A | B01 Block B (p.76-77) | FY25 trade payables Rs 3.2544cr, FY26 Rs 3.9542cr anchored to results FY26 annual p.5; not in screener data. |
| A | B03 Phase 1E (p.65-66) | Audit fee Rs 2.00L, non audit Rs 3.70L, ratio 1.85x; ratio consistent but rupee amounts unverifiable from accessible sources. |

### Verified clean (high priority checks, no defect)

- Verifier A recomputed and confirmed the Gate 0 verdict card numbers: FY26 ROCE 27.88%, revenue CAGR 11.94% and PAT CAGR 24.71%, zero borrowings and zero finance cost FY26, and peer EBITDA margins (ELECON 18.01%, SHANTIGEAR 16.07%, TRF 2.93%). No critical mismatch on any Section 1B or verdict card numerical input.
- Verifier B concurs credibility grade C is correct under the no concall cap; promise delivery spot checks 5 of 5 confirmed.
- Verifier C Gate 0 audit: 49 rules checked, 0 fails (1 MINOR presentational note, no decision impact). Combined assessment AVERAGE holds under either Emerging Moat band.
- Verifier D: all quoted material traces to a real transcript passage (no wholesale fabrication); all 5 of 5 Part 1 claim verdict directions survive independent re verification despite the citation accuracy defects logged above.
