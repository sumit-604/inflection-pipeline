# VERIFIER SUMMARY — AVANA (run 2026-07-16)

## CONFIDENCE DELTA AND ACCEPTANCE RATES

| Component | Score | Acceptance / status |
|---|---|---|
| Numerical acceptance (Verifier A, B12a) | 88 | 28 clean of 32 checked; 0 CRITICAL, 0 MAJOR, 4 MINOR |
| Framework adherence (Verifier C phase 1, B12c) | 100 | 61 rules checked (47 gate0 + 14 EM); 0 CRITICAL, 0 MAJOR, 2 MINOR |
| Framework adherence (Verifier C phase 3, B12c-valuation) | 100 | 48 valuation rules; 0 CRITICAL, 0 MAJOR, 5 MINOR; CONCUR on WATCHLIST |
| Red flag coverage (Verifier B) | N/A | Not run: no subject concall / AR / results narrative to audit |
| Peer utilisation (Verifier D) | N/A | Not run: no B06; peer concalls routed to B07 / B09 as sector context |
| Overall | 88 | Min of available components; band 75-89 normal |

Verifier A acceptance rate 88%. Verifier C acceptance rate 100% both passes. No REWORK trigger fired (0 CRITICAL, no acceptance below 60%, overall 88).

Phase 3 valuation adherence: acceptance 100, 0 CRITICAL, 0 MAJOR, 5 MINOR, CONCUR. Recomputed clean and reproduces Pillar 1 26.1x, quality adjusted 20.9x, RRM 18.3x, HR base 2.12 (forward PE, NOT the SFL trailing/forward inconsistency), fair values 202/322/372, entry 145-165, MoS 132, WATCHLIST.

CRITICAL CAVEAT: this delta measures analysis fidelity to sources, not evidence sufficiency. It is high because every stage faithfully reported a very thin evidence base (single screener Data_Sheet plus operator relayed RHP/NSE digest; no primary AR, results, concall, rating or shareholding PDF) and applied the framework exactly. The evidence gate stayed INSUFFICIENT EVIDENCE and cash INDETERMINATE.

## FINDINGS — sorted by severity

No CRITICAL findings. No MAJOR findings.

### MINOR

| Verifier | Location | Note |
|---|---|---|
| A (B12a numerical) | B09 Section 1B | Order book Rs 52.24 Cr (30-Nov-2025) not in screener; sourced from RHP / IPO aggregator. Anchor NOT FOUND in local sources; resolved at interpretation level by the operator relayed RHP/NSE digest which confirms the same figure and cross checks clean vs the screener; still relayed, not a primary PDF. |
| A (B12a numerical) | B07 Section 2C | Implied incremental revenue 4.67 x 15.76 = 73.60 Cr; exact 73.6352 Cr. Rounding within tolerance (<0.1%). |
| A (B12a numerical) | B07 Section 2C | Capex embedded growth stated 87.8%; exact 87.75%. Rounding within tolerance (<0.05pp). |
| A (B12a numerical) | B09 entire TAM section | TAM Rs 1,100-1,700 Cr rests on third party reports (Mordor, Markets & Data, ICRA) behind HTTP 403 paywalls, recovered via search snippets only. Web sourced tier, not local PDF verified; report acknowledges the limitation; no contradiction in peer concalls. |
| C phase 1 (B12c framework) | B01 M9 gross margin proxy | Used (Rev - RawMaterial - ChangeInInventory)/Rev vs framework (Rev - MaterialCost)/Rev. Disclosed in data_notes; +6.45pp vs peer median keeps M9 in the same 3/5 band either way. No score or classification impact. |
| C phase 1 (B12c framework) | B07 YAML evidence_mix | inference:8 counts narrative touchpoints, not the 2 nonzero scored inference categories (G1, R1); unreconciled and potentially misleading downstream. Scorecard, active_categories (1) and completionist_recount are internally correct. No score impact. |
| C phase 3 (B12c-valuation) | B11 Pillar 1 / Section 3 | Cash bridge asymmetry: about Rs 22 Cr removed from ROCE denominator but full net cash Rs 27.06 Cr (Rs 12/sh) added back at 1x; about Rs 5.8 Cr double touched. Under 1% of FV, within Override 1's Rs 22-27 Cr range, offset by the conservative 40% ROCE vs about 44% computed. No decision impact. |
| C phase 3 (B12c-valuation) | B11 Track 1 RRM | Fundamental Base PE set to ROCE base 26.1x (to 18.3x), not quality adjusted 20.9x (to 14.6x). Disclosed and reasoned (avoids double penalising cash); the alternate reading would push divergence 12.4% to about 30% and force the conservative track to govern entry. Moot: Override 1 anchors additive Track 2 as governing; destination PE and WATCHLIST unchanged. |
| C phase 3 (B12c-valuation) | B11 Hurdle Ratio | Authoritative HR written as (1+g)^4 x trailing 28.13x; value 2.12 is identical to the internally consistent forward-forward HR (entry FY27 forward PE 21.63x, exit FY30 forward). Substance correct, NOT the SFL inconsistency; should display forward entry PE for transparency. HR base 2.12 >= 1.953 is a technical PASS; CONDITIONAL is a conservative overlay with no decision impact. |
| C phase 3 (B12c-valuation) | B11 Section 4H | L809 (Gate0 AVERAGE -> AVOID) vs L915 (Gate0 <60 -> WATCHLIST) tension resolved correctly to WATCHLIST via L915 with all other AVOID sub triggers confirmed not firing (U/D 6.9x >= 2x, Hurdle CONDITIONAL not STOP, promoter CAUTION not CONCERN). Correct outcome; the conflict is not surfaced as an explicit cite. Transparency note. |
| C phase 3 (B12c-valuation) | reports/ (B14 absent at audit time) | Role 2 thesis report B14.md not on disk when audited; decision logic audited as carried in B11 Section 4. B14 must reproduce WATCHLIST / Small (2-3%) / entry Rs 145-165 / MoS Rs 132; fresh Verifier C pass required if it diverges. B14 subsequently on disk reproduces all four; no divergence. |

## VERIFIER COVERAGE NOTES

Verifier A confirmed 100% of verdict card figures (Gate 0 classification, core / moat / grand scores, deal breaker application) clean against the screener Data_Sheet, plus all Block A-E and Moat M1-M11 inputs, all AVANA revenue / EPS / P/E figures in B09, and peer moat metrics. No fabrications, no mechanical errors, no material misstatements; all limitations stated in upstream reports.

Verifier C phase 1 recomputed core score 49, classification AVERAGE, moat FORTRESS, grand total 76, em_score 2.5, em_classification NONE, combined AVERAGE, all matching B01 and B07; all 9 Gate 0 deal breakers correctly evaluated; history downgrade verified.

Verifier C phase 3 recomputed all 48 valuation rules clean and reproduces the four pillar build both tracks (Track 2 governing 20.9x, Track 1 RRM 18.3x), HR base 2.12, fair values 202/322/372, entry 145-165, MoS 132, WATCHLIST / Small (2-3%). Verdict CONCUR. Key adjudication carried by C phase 3 and surfaced in the recommendation: the forward Hurdle Ratio 2.12 is internally algebraically consistent, NOT a raw SFL arithmetic error, so the devil's disagreement is about the no multiple compression economic assumption, not a math bug.

## POST-VERIFICATION OPERATOR CONTEXT (not verifier scored)

The operator relayed RHP/NSE digest (2026-07-17) reached the run after verifiers A and C phase 1 completed and was carried into phase 3 as a lead and cross check layer, not a primary PDF; no fresh block was re scored. Its effect: FLAG-CAPEX recast from unspecified to purpose known / commissioning unconfirmed, FLAG-CASH sharpened to evidenced structural intensity (H1 FY26 WC cycle about 245 days), FLAG-CAPITAL-STRUCTURE proceeds partly known plus a new 23-Jun-2026 NSE query, FLAG-PROMOTER adds the CS resignation and the proceeds query, and the B09 order book MINOR resolved at interpretation level.
