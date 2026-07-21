# Verifier summary, phase 1

## Confidence delta and acceptance rates

| Component | Verifier | Score | Acceptance rate |
|---|---|---|---|
| Numerical acceptance | A (B12a) | 97.9 | 97.9 (47 figures, 0 CRITICAL, 0 MAJOR, 1 MINOR) |
| Red-flag coverage | B (B12b) | 70 | 70 (7 of 10 caught, 1 partial, 2 MAJOR misses) |
| Framework adherence, phase-1 portion | C (B12c) | 100 | 100 (72 of 72 Gate 0 + Emerging Moat rules) |
| Peer utilisation | D (B12d) | N/A | N/A (no peer transcripts; stage 6 skipped, correctly) |
| Overall | | 70 | band 60 to 74; not a REWORK trigger |

REWORK check: Verifier A CRITICAL count 0; min acceptance rate at or above 60; source-fidelity MISMATCH false; REWORK not triggered. Valuation-framework adherence pending phase 3 (B12c valuation half deferred, stages 10 and 11 not yet built).

No CRITICAL findings in any verifier. Findings below are sorted MAJOR first, then MINOR.

## MAJOR

| Verifier | Location | Finding |
|---|---|---|
| B (B12b) | 05-concall 4C / 4D red-flag table (Q3R pp.4-5) | Stage 5 missed the Q3 FY26 seasonal cost deferral (Rs 1,465.31L other expense plus Rs 111.26L depreciation) that flatters 9M profit and mechanically loads the Q4 loss; the composition of the flagged Q4 loss is mis-weighted. |
| B (B12b) | 05-concall 4C earnings quality (FY26R p.4, pp.12-13 KAM) | Partially caught and under-weighted: operating segments lost Rs 10.72 Cr in FY26; near-breakeven consolidated PBT rests on about Rs 16.27 Cr net unallocable investment income against a Rs 247 Cr FVTPL book. Structural investment-driven earnings not surfaced. |

## MINOR

| Verifier | Location | Finding |
|---|---|---|
| A (B12a) | 02-notes finding 11; 04-bizmodel 2D (Annual_Report.txt p.37) | Distillery output decline stated as both -82.3% and -82%; true figure 11.61 vs 65.41 lakh litres = -82.25%. Rounding artifact within tolerance; underlying numbers verified clean. source_fidelity true. |
| B (B12b) | 05-concall 2D / 4D remuneration flag (FY26R p.16 (g)) | Under-weighted the Schedule V three-year-cap breach and the "subject to shareholder approval" governance angle behind the four-consecutive-years remuneration flag. |
| B (B12b) | 05-concall, cash not covered (FY26R p.7 line 448) | FY26 standalone operating cash flow appears negative about -Rs 23.10 Cr versus +Rs 38.24 Cr prior year; adjacent to the stage-11 cash-conversion domain; p.7 OCR degraded; not noted at stage 5. |
| B (B12b) | 05-concall 4D / 1C framing (FY26R pp.3-4) | Asymmetry: framing omits Others segment PROFIT nearly doubling (+407.24 vs +206.91L) and consolidated FY26 PAT staying positive (+Rs 11.13 Cr). |
| C (B12c) | B01 Block D / D1 | D1 anchored to CARE FY25 standalone net-cash basis (=5) rather than framework 'latest' FY26; instruction-driven, both figures shown, FLAG-DATA-JUDGMENT raised. Swings Block D 14 to 9 but classification AVOID under both. Decision-immaterial. |
| C (B12c) | B01 Block E / E1 | Promoter holding scored from AR FY25 annual note, not a latest-quarter SHP (none supplied); figure is filing-anchored and disclosed. Immaterial to AVOID. |
| C (B12c) | B01 deal-breaker DB8 | DB8 evaluated on consolidated PAT (all three years positive); standalone core was loss-making FY25/FY26 and would independently trigger DB8's max-AVERAGE cap. Classification already AVOID (more restrictive), no outcome change. |
| C (B12c) | B07 Section 5 / R1 | R1 likelihood scored High while report text stresses zero company-specific capture; L/M arguable. Total falls to 3.0 either way, still under 12 / NONE. No classification impact. |
| D (B12d) | B06-peers.yaml skip_reason | Skip reason states there are no B05 peer_questions, but 05-concall Section 4B contains a fully formed 5-question peer_questions list preserved for downstream use. Wording imprecision only; does not change the correct empty verification output. |

## Verifier D scope note

Verifier D is not applicable this run: no peer-concall transcripts exist (inputs/peer-concalls/ absent; manifest concalls_available false, confirmed independently). The stage 6 skip is correctly recorded and evidenced. Standard coverage checks cannot run against non-existent transcripts. Peer comparison this run exists only as quantitative screening CSVs (KMSUGAR, RAJSREESUG, UGARSUGAR), which is not concall verification; the five B05 peer_questions remain open into downstream stages.

## Gate 0 and Emerging Moat framework check (Verifier C, phase-1 scope)

Gate 0: 45 rules checked, 0 fails. Emerging Moat: 27 rules checked, 0 fails. All 72 rules applied as written; the four MINOR items above are disclosed basis choices, not rule failures. Verifier C concurs on the phase-1 outcome: Gate 0 AVOID, Emerging Moat NONE, combined AVOID. Valuation rules deferred to phase 3 (B10/B11 artifacts do not exist yet).
