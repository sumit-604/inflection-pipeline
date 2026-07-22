# Verifier summary — phase 3 (finalize)

## Confidence delta and acceptance rates

| Component | Verifier | Score | Acceptance rate |
|---|---|---|---|
| Numerical acceptance | A (B12a) | 97.9 | 97.9 (47 figures, 0 CRITICAL, 0 MAJOR, 1 MINOR rounding; no source-fidelity MISMATCH) |
| Red-flag coverage | B (B12b) | 70 | 70 (7 of 10 flags caught, 1 partial, 2 MAJOR misses; degraded no-concall Stage 5) |
| Framework adherence | C (B12c) | 88 | 88 binding half; phase-1 gate0+emoat 100, phase-3 valuation-adherence 88, weighted ~95.5 |
| Peer utilisation | D (B12d) | N/A | N/A (no peer transcripts; stage 6 skipped correctly; excluded from the min) |
| Overall | | 70 | min of available components; red-flag-bound; band 60 to 74, not a REWORK trigger |

REWORK check: Verifier A CRITICAL count 0; source-fidelity MISMATCH false; min acceptance rate at or above 60 (numerical 97.9, redflag 70, framework/valuation 88); REWORK not triggered. Verifier C phase-3 valuation-adherence half is complete (no longer pending); its valuation acceptance rate is 88 (38 of 43 rules clean).

No CRITICAL findings in any verifier. No MAJOR findings in the valuation-adherence audit. Findings below are sorted CRITICAL first, then MAJOR, then MINOR.

## CRITICAL

None.

## MAJOR

| Verifier | Location | Finding |
|---|---|---|
| B (B12b) | 05-concall 4C / 4D red-flag table (Q3R pp.4-5) | Stage 5 missed the Q3 FY26 seasonal cost deferral (Rs 1,465.31L other expense plus Rs 111.26L depreciation) that flatters 9M profit and mechanically loads the Q4 loss; the composition of the flagged Q4 loss is mis-weighted. |
| B (B12b) | 05-concall 4C earnings quality (FY26R p.4, pp.12-13 KAM) | Partially caught and under-weighted: operating segments lost Rs 10.72 Cr in FY26; near-breakeven consolidated PBT rests on about Rs 16.27 Cr net unallocable investment income against a Rs 247 Cr FVTPL book. Structural investment-driven earnings not surfaced. |

## MINOR

| Verifier | Location | Finding |
|---|---|---|
| A (B12a) | 02-notes finding 11; 04-bizmodel 2D (Annual_Report.txt p.37) | Distillery output decline stated as both -82.3% and -82%; true figure 11.61 vs 65.41 lakh litres = -82.25%. Rounding artifact within tolerance; underlying numbers verified clean. source_fidelity true (not a fidelity flag; a rounding note). |
| B (B12b) | 05-concall 2D / 4D remuneration flag (FY26R p.16 (g)) | Under-weighted the Schedule V three-year-cap breach and the "subject to shareholder approval" governance angle behind the four-consecutive-years remuneration flag. |
| B (B12b) | 05-concall, cash not covered (FY26R p.7 line 448) | FY26 standalone operating cash flow appears negative about -Rs 23.10 Cr versus +Rs 38.24 Cr prior year; adjacent to the stage-11 cash-conversion domain; p.7 OCR degraded; not noted at stage 5. |
| B (B12b) | 05-concall 4D / 1C framing (FY26R pp.3-4) | Asymmetry: framing omits Others segment PROFIT nearly doubling (+407.24 vs +206.91L) and consolidated FY26 PAT staying positive (+Rs 11.13 Cr). |
| C (B12c) phase-1 | B01 Block D / D1 | D1 anchored to CARE FY25 standalone net-cash basis (=5) rather than framework 'latest' FY26; both shown, decision-immaterial (AVOID either way). |
| C (B12c) phase-1 | B01 Block E / E1 | Promoter holding scored from AR FY25 annual note, not a latest-quarter SHP (none supplied); immaterial to AVOID. |
| C (B12c) phase-1 | B01 DB8 | DB8 evaluated on consolidated PAT; standalone loss would independently trigger; AVOID already more restrictive. No outcome change. |
| C (B12c) phase-1 | B07 R1 | R1 likelihood scored High versus L/M arguable; total under 12 / NONE either way. No classification impact. |
| C (B12c) phase-3 valuation | Pillar 2 0.65x band label | 0.65x correctly earned via the structural test (seasonal agri), not the rating-agency limb; CARE frames liquidity strong. Operator-approved. No decision impact. |
| C (B12c) phase-3 valuation | Sector cap source | Agri processing 20x operator-supplied; non-binding (6.2x far below 20x), zero effect. |
| C (B12c) phase-3 valuation | RRM base selection (Master p.392) | Track 1 RRM applied on ROCE base 9.5x not quality-adjusted 6.2x; conservative additive track governs; no decision impact. |
| C (B12c) phase-3 valuation | B11 upside_downside_ratio field | Reports bull/bear 1.06 not framework base/bear 0.07; both shown in the body; both fail the 2x minimum. |
| C (B12c) phase-3 valuation | SOTP segment multiples | Eimco 6/8/10x and urad 4/6/7x are analyst round numbers, not four-pillar-derived; largest SOTP swing but AVOID survives even a 12x Eimco. Method operator-approved; multiples maker-filled. |
| D (B12d) | B06-peers.yaml skip_reason | Skip reason states there are no B05 peer_questions, but 05-concall Section 4B contains a fully formed 5-question list preserved for downstream use. Wording imprecision only; does not change the correct empty verification output. |

## Phase-3 valuation-adherence audit (Verifier C, B12c valuation half)

43 valuation rules checked (B11, B10, extended to B14), 38 clean, 5 MINOR fails (listed above), 0 MAJOR, 0 CRITICAL. Verifier C re-derived and concurs: destination PE 6.2x additive / 7.2x RRM, decision AVOID-on-valuation, Tier A, entry Rs 10.24 to Rs 11.52. All 9 combined findings across both halves are MINOR and decision-invariant; the SOTP round-number segment multiples are the largest single swing, and AVOID survives even a 12x Eimco. Verifier C concurs with AVOID-on-valuation, Emerging Moat NONE, Gate 0 AVOID, and the SOTP-led destination PE.

## Verifier D scope note

Not applicable this run: no peer-concall transcripts exist (inputs/peer-concalls/ absent; manifest concalls_available false, confirmed independently). The stage 6 skip is correctly recorded and evidenced. Standard coverage checks cannot run against non-existent transcripts. Peer comparison this run exists only as quantitative screening CSVs (KMSUGAR, RAJSREESUG, UGARSUGAR), which is not concall verification; the five B05 peer_questions remain open.
