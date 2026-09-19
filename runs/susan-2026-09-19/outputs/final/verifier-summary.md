# Verifier summary: SUSAN, run 2026-09-19 (phase 1)

Scope: Verifier A (numerical, B12a), Verifier B (concall red flags, B12b), Verifier C phase 1 portion only (Gate 0 B01 and Emerging Moat B07, B12c), Verifier D (peers, B12d). Verifier C's valuation, expectation ledger and narrative checks are pending phase 3 and stage 13 review.

## Confidence delta (phase 1)

| Component | Score | Verifier | Basis |
|---|---|---|---|
| Numerical acceptance | 95.5 | A (claude-haiku-4-5) | 67 of 87 material figures checked; 0 CRITICAL, 3 MAJOR, 0 MINOR |
| Red flag coverage | 62.5 | B (claude-opus-5) | 8 material of 21 listed; 5 found (3 fully caught, 2 partly caught; partial counted as found per rule 3) |
| Framework adherence | 87.5 | C (claude-opus-5) | 80 phase 1 rules (Gate 0 50, EMoat 30), 70 passed; valuation half pending phase 3 |
| Peer utilisation | NOT APPLICABLE | D (claude-sonnet-5) | 3 peers, below the 4 item floor; reported as count: 3 of 3 substantive, 7 of 7 transcript quarters confirmed; acceptance 100 for information only |
| Overall | 62.5 | set by redflag_coverage | 60 to 74 band: PROCEED family verdicts downgrade one level; not forced REWORK |

Acceptance rates: A 95.5, B 62.5, C 87.5, D 100 (information only). No rate falls below 60.

Verifier B also reports a strict fully caught rate of 37.5% (3 of 8 material items fully caught). The scored 62.5 counts partly caught items as found, per its rule 3. The orchestrator recorded the strict rate and did not use it. Verifier B's note: "The three misses all bear on the margin bridge or the revenue base."

Counts: CRITICAL 0. MAJOR 11 (A 3, B 5, C 3). MINOR 31 (B 16, C 10, D 5).

## CRITICAL

None.

## MAJOR

| # | Verifier | Location | Finding | Disposition |
|---|---|---|---|---|
| 1 | A | B02, Finding #2, p.2 | Claimed "Borrowings +47.4% FY24 to FY26"; source truth FY24 Rs 24.79 Cr to FY26 Rs 66.72 Cr = +169% (RHP Annexure 1). source_fidelity: true | FLAG CLEARED by source re-check (see disagreement row below). +47.4% is year on year at AR FY26 Note 4a p.67 (txt line 2597); +169% FY24 to FY26 also true |
| 2 | A | B04, Section 1B, p.2 | "Manufactured cables and wires 59.71% of FY26 revenue" does not appear on RHP p.136 as an aggregate; named components there sum to 50.88%. UNANCHORED. source_fidelity: true | GATE HELD. The 59.71% figure is not used in any phase 1 final file. Final files use the printed AR Note 18 lines instead: Sales of Manufactured Products Rs 16,082.88 Lakhs and Sales of Traded Products Rs 10,337.16 Lakhs, total Rs 26,935.66 Lakhs (AR FY26 Note 18 p.75-76, txt lines 3001, 3004, 3014). Not cleared: the ratio is a derivation, not a printed figure, and needs a source re-check logged before phase 3 uses it |
| 3 | A | B04, Section 1C, p.2 | "Winding Al/Cu 25.62% (17.36+0.86+3.70)"; stated components sum to 21.92%. Fails internal consistency. source_fidelity: true | GATE HELD, figure removed. Final files use the Q1 FY27 winding wire revenue share of 24.39% (press release 14-Aug-2026 p.3) and do not carry any FY26 winding wire percentage |
| 4 | B | B05 1B/2D/4B; B06 Q6 | MISSED: 24.39% winding-wire margin equals revenue share and contradicts management's own 10-15% range; hold margin-bridge inputs until audio or segment disclosure resolves it | Carried in gate recommendation (LBF1, contradicted claim 1) |
| 5 | B | B05 1A/1B/4A | MISSED: Rs 700-800 Cr peak revenue claim unrecorded and untested against peer asset turns | Carried in narrative and FLAG-TAM note |
| 6 | B | B05 all sections | MISSED: QoQ revenue -17.5%, PBT -38.2%, margin down ~200 bps not stated; seasonal reading also not stated | Carried in narrative and monitorable 5 |
| 7 | B | B05 2D, 4A #3, 4D | OVERSTATED: inventory-change credit is a cost reversal, not unrealised profit; restate as working-capital/cash flag with the seasonal reading | Correction carried; "PBT flips to a loss" not carried; Rs 9.33 Cr FG build moved into FLAG-CASH |
| 8 | B | B05 2C, 3C, 4C | NOT SUPPORTED: segment margins were given in the first answer, not after three prompts | Ground dropped from credibility basis; grade C holds |
| 9 | C | B01 M10 (01-gate0.md L236-239; YAML moat_score/moats_confirmed/grand_total) | M10 scored 3; rule gives 0 (stability condition fails, <2 decline years). Recomputed 0 | Corrected values carried: moat_score 18, moats_confirmed 4, grand_total 70; moat class STRONG and classification AVERAGE unchanged |
| 10 | C | B01 YAML history_downgrade (L27) vs report L270-273 | Field true but no downgrade applied; 6-yr history is the 5-6 lower-confidence tier. Recomputed false | Corrected value carried (false). Verifier C's alternative reading (3-4yr ratio/cash history binds LIMITED) would downgrade AVERAGE to AVOID and make this CRITICAL; operator ruling requested |
| 11 | C | B07 Section 2C (07-emoat.md L81-113) / YAML capex_embedded_growth_pct | Field holds 22.8 from substitute method, not 2C mechanical ~80. Recomputed ~80 (10.30 Cr x 21.0 FAT / 269.36 Cr); ~84 on 10.81 Cr total project | Both values carried to phase 3 with labels; operator rules on the substitution |

## MINOR

| # | Verifier | Location | Finding |
|---|---|---|---|
| 12 | B | B05 1A/1B/1C | PARTIAL: third form of HT/MVCC guidance (FY27 mix ~30-35%) missing |
| 13 | B | B05 methodology/1C | PARTIAL: transcript is edited summary; 50% text out of order; call date 14/18/19 Aug; name audio as LBF4 tie-breaker |
| 14 | B | B05 1B | MISSED: current HT/MVCC share also stated 10-15% |
| 15 | B | B05 1A/1B; B06 Q2 | MISSED: ~20% called net margin in Q3 |
| 16 | B | B05 2A | MISSED: PR says 'significant portion' of order book in 3 months |
| 17 | B | B05; B06 | MISSED: no volume/price split of growth |
| 18 | B | B05 4D; B06 Q5 | PARTIAL: 'ahead of schedule' heading vs 'on track' body |
| 19 | B | B05 3C | PARTIAL: implicit 'last two to three years' growth anchor not recorded |
| 20 | B | B06 Q1/Q2 | PARTIAL: DYCL 10-11% B2B margin ceiling not used; DYCL called silent |
| 21 | B | B06 2A/2E | PARTIAL: DYCL industry-wide Apr-May booking slump not set against SUSAN order book |
| 22 | B | B05 2D; B06 2E | MISSED: DIACABS MV seasonality/site delivery not linked to SUSAN Q1 FG build |
| 23 | B | B06 Q5 | OVERSTATED: 'aggressive' Feb-2027 timeline rests on non-comparable projects |
| 24 | B | B06 Q5 | Anchor misattributed: 'end of H2 only' quote is DYCL Oct-2025 call, not Q3 FY26 |
| 25 | B | B06 2A | NOT SUPPORTED (context): DIACABS 1,900 Cr is revenue, not prior order book |
| 26 | B | B06 Q4 | NOT SUPPORTED (context): DYCL government share rose to 16% |
| 27 | B | B05 2B | Internal inconsistency on which topics analysts raised |
| 28 | C | B01 M7 (L226-230) | Unanchored industry-knowledge player count in basis; score 0 stands |
| 29 | C | B01 YAML flags[] | Missing 'may not have seen full cycle' flag |
| 30 | C | B01 YAML deal_breakers | Driving years not stated |
| 31 | C | B01 output | Moat profile bars absent |
| 32 | C | B01 E1 (L176-179) / input_gaps | Post-listing SHP absence cited 'per input_gaps' but not listed there; rule outcome unchanged |
| 33 | C | B01 M1 (L205) vs M11 (L242) | FY24-26 revenue CAGR stated 61.3% and 61.8%; stated inputs give 61.8%; band unchanged |
| 34 | C | B01 M11 (L240-247) | '3yr' windows are 2-yr CAGRs; selling % trend on FY24-26 only; score 5 unchanged |
| 35 | C | B07 G1/G2/H1, F2 anchors | Evidence anchored to pipeline blocks or missing page/question |
| 36 | C | B07 F2 (L215-223, L368) | Documented multiplier on a category whose on-time leg is a claim; recomputed F2 1.4, em_score 10.1; NONE unchanged |
| 37 | C | B07 YAML evidence_mix vs completionist_recount | Documented 14 vs 7 unexplained |
| 38 | D | B06 Q5 evidence row, DYCL Q1 FY27 citation | Claimed p.13-14; actual transcript marker p.16 (footer Page 15 of 16). Quote accurate and correctly attributed; anchor 2-3 pages early |
| 39 | D | B06 Q3 evidence row, VIDYAWIRES Q2 FY26 citation | Claimed p.9; actual marker p.8. Quote accurate; anchor one page late |
| 40 | D | B06 Q3 evidence row, VIDYAWIRES Q2 FY26 citation | Claimed p.10; actual marker p.9. Quote accurate; anchor one page late |
| 41 | D | B06 risks_peers_raise item 5, VIDYAWIRES Q4/FY26 citation | Claimed p.17; actual marker p.14 (footer Page 13 of 17). Quote accurate; anchor 3 pages early |
| 42 | D | B06 Part 2E / industry cross-read | Omission: VIDYAWIRES customer-concentration disclosure (458 customers, no customer >9%, 94% repeat revenue; Q2 FY26 call p.4) not used beside the DIACABS Adani-concentration point |

## Verifier B: pipeline flags not supported

- B05 2C/3C/4C: 'segment margins given only after three analyst prompts': NOT SUPPORTED (given in first answer, SUSAN-T p.5 l.124-132)
- B05 2B: cash conversion and trading 'raised only when an analyst pushed': NOT SUPPORTED (never raised)
- B05 2D/4A/4D: inventory-change credit as unrealised profit, 'PBT flips to loss': OVERSTATED (cost reversal; real issue is Rs 9.33 Cr cash into FG)
- B06 Q5: Feb-2027 target 'aggressive': OVERSTATED (Rs 10.30 Cr brownfield compared to greenfield/CCV projects)
- B06 2A: DIACABS order book 'grew from INR1,900 crore': NOT SUPPORTED (1,900 is revenue), context only
- B06 Q4: DYCL government share 'falling': NOT SUPPORTED (12/13/13/16%), context only

Promise delivery spot checks: 4 checked, 4 confirmed, 0 wrong. Credibility grade: concur, C holds under the single transcript cap.

## Verifier C: phase 1 recomputed values

| Field | Stated | Recomputed |
|---|---|---|
| Gate 0 moat_score | 21 | 18 |
| Gate 0 moats_confirmed | 5 | 4 |
| Gate 0 grand_total | 73 | 70 |
| Gate 0 history_downgrade | true | false |
| Gate 0 moat_class | STRONG | STRONG (unchanged) |
| Gate 0 classification | AVERAGE | AVERAGE (unchanged) |
| EMoat em_score (if E-m2 applied) | 10.7 | 10.1 |
| EMoat classification | NONE | NONE (unchanged) |
| capex_embedded_growth_pct per 2C | 22.8 | ~80 |

## Verifier disagreement log

| Date | Run (ticker-date) | Number/claim | Verifier A verdict + anchor | Downstream step + its position | Disposition | Note |
|---|---|---|---|---|---|---|
| 2026-09-19 | susan-2026-09-19 | B02 top finding 1: total borrowings +47.4% to Rs 6,671.70 Lakhs | MAJOR, source_fidelity true: read as FY24 to FY26 (+169%); anchor RHP Annexure 1 (Rs 2,479.18 Lakhs FY24 to Rs 6,671.70 Lakhs FY26) | Orchestrator source re-check | FLAG CLEARED: source re-check found the number at a correct anchor, AR FY26 Note 4a Grand Total Rs 6,671.70 Lakhs (31-Mar-2026) vs Rs 4,526.86 Lakhs (31-Mar-2025), PDF page 67 (txt line 2597); +47.4% is year on year. B02 never stated FY24 as the base. Re-checked by the orchestrator session | The +169% FY24 to FY26 figure is also true and B01 carries it as "borrowings tripling". Both readings stand; neither is a fabricated number |

The two remaining Verifier A findings (rows 2 and 3) produced no disagreement. Stage 13 held the gate on both and did not clear either.
