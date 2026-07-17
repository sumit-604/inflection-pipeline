# Verifier summary (Phase 3, final)

Confidence delta: overall 87, normal band (75-89): note specifics, no verdict downgrade, no rework. Binding minimum is red-flag coverage at 87.

| Component | Score |
|---|---|
| Numerical acceptance (B12a) | 94.3 |
| Red-flag coverage (B12b) | 87 |
| Framework adherence (B12c, incl. phase-3 valuation audit) | 97 |
| Peer utilisation (B12d) | 100 |
| Overall | 87 |

Acceptance rates:
- Verifier A (numerical, B12a): 94.3%
- Verifier B (red-flags, B12b): 80%
- Verifier C (framework, B12c): 97%
- Verifier D (peers, B12d): 92%

CRITICAL count: 0 across all four verifiers, including the phase-3 valuation-adherence audit. No verifier acceptance rate below 60% (lowest is B12b at 80%), so no rework gate fires. Verifier A's first standalone-only pass raised critical findings that were false positives caused by not accessing the consolidated FY26 statements (p16-19 of the results PDF); the consolidated re-audit is canonical at 0 critical / 0 major / 94.3%, with the superseded pass preserved at outputs/reports/B12a-numerical-v1-standalone-only.md. The phase-3 valuation audit added the destination-PE and Hurdle STOP / no-buy-at-CMP checks: 0 critical, the decision holds under every alternative reading tested.

## CRITICAL

None across all four verifiers.

## MAJOR

| Verifier | Location | Note |
|---|---|---|
| C (framework, phase-3 valuation) | B11 §1B RRM dual-track / §4A-4E | V28 conservative-track-governs default overridden: track divergence 38.6% (>15%), so the Section 1B default is that the RRM track governs the entry; B11 lets the additive track govern on a recorded operator override (deliberation p.74). Authoritative, not silent, but load-bearing: entry Rs 90-93 rests on Track 2; the default (Track 1 base FV Rs 111 / 1.953) would set entry ~Rs 57, MoS ~Rs 45. Buy/no-buy at CMP unchanged (STOP). |
| C (framework, phase-3 valuation) | B14 §7 verdict box / recommendation | R1 verdict returned WATCHLIST vs the mechanical AVOID that Master v3.3 lines 809/916 mandate on Gate 0 AVERAGE, Promoter CONCERN, and Hurdle STOP; reconciled to the authoritative FTTCP deliberation p.63-64 (reachable Rs 90-93 entry). No-buy-at-CMP preserved; position size correctly capped Small by Promoter CONCERN. Label-only departure, operator-authorized. |
| C (framework) | B07 §OUTPUT / end of report | B07-emoat closing YAML block not emitted; breaks the machine-readable Pillar-3 handoff. Prose content intact, no score or decision change; remediated by the orchestrator writing B07-emoat.yaml. |
| B (red-flags) | B05 §1B/§4C, Call p.9-10 | Embryologist-productivity red flag under-weighted: 5 embryologists vs 2,255 pickups (~451 each) against a claimed ~120 each; analyst pushback deflected with "we are hardworking people". |
| D (peers) | B06 Part 3, KAYA Q4 FY25 (29-May-2025) row | Peer-quarter mislabeled CITED-ONLY though a load-bearing Rajiv Suri quote from that call supports the Q2 CONTRADICTED verdict; true peer utilisation is 12/12, not the 11/12 the coverage map implies. |

## MINOR

| Verifier | Location | Note |
|---|---|---|
| A (numerical) | B03 Phase 3 DuPont | Tables lack inline (S)/(C) notation; presentation clarity only, no numerical error. |
| A (numerical) | B05 Concall CFO | Rs 724.72L cash from operations stated on a consolidated pre-interest-paid basis; could clarify the operating-activities basis in future rounds. |
| B (red-flags) | B05 §2C/§4C, Call p.6 vs p.7 | "Almost zero" debt framing not itemised against Rs 24.56 Cr borrowings that rose in absolute terms from Rs 20.61 Cr; only the ratio fell 0.45x to 0.16x. |
| B (red-flags) | B05 §3D/§4C, Call p.9 | Q4 quarterly cycle-count question unanswered; only the full-year 2,255 figure given (this is the single MINOR miss behind the 87 coverage score). |
| B (red-flags) | B06 Q4, Call p.9-10 | International-mix contradiction is sound but conflates bases (Gaudium 25-30% patient-count share vs peers' 2-4% revenue share); contradiction survives, denominator difference should be stated. |
| C (framework, phase-3 valuation) | B11 Pillar 1 / §1B step A | Master v3.3 lines 211-214 carry a second ROCE>33% branch (24 + 0.3×(ROCE-33), cap 30x) giving 25.2x at 37% and dest ~23x; B11 took the conservative cap-24 read. Two-branch HR base 1.38 / bull 1.55, both < 1.953; STOP and decision unchanged. |
| C (framework, phase-3 valuation) | B11 Pillar 3a / §1B step D | Strict read gives one clean documented qualifier (SOM CAGR 31.4%); capex-embedded 335% flagged not decision-useful for asset-light, so +0x on a strict read. +2x held by operator Override 2 (documented IPO earmark as second qualifier). If +0x, raw dest 20.2x; Hurdle still STOP. |
| C (framework) | B01 Block A | RoCE/RoE used RHP KPI definitions rather than framework defaults; source-permitted as the screener CSVs were empty; A3 band unchanged at 5. |
| C (framework) | B01 Block F, M2/M5/M9 | M2 credits foreign-peer EBITDA (score 5) while M5/M9 mark peer data needed; defensible but asymmetric; moat count stays 3. |
| D (peers) | B06 Part 1, Q3 answer | Gurugram/pollution quote anchored to RAINBOW-Concall_Feb_2026 but verbatim in RAINBOW-Concall_Nov_2025; wrong quarter only, verdict unaffected. |
| D (peers) | B06 Part 1, Q3 answer | "~100 clinics (FY18) to 76" figure stated with no inline anchor; fact genuine in KAYA-Concall_Oct_2024 (Prateek Giri Q&A), anchor merely missing at point of use. |
