# Verifier summary (Phase 1)

Phase 1 confidence delta: 87, normal band (75-89): note specifics, no verdict downgrade, no rework.

Acceptance rates:
- Verifier A (numerical, B12a): 94.3%
- Verifier B (red-flags, B12b): 80%
- Verifier C (framework, B12c): 98%
- Verifier D (peers, B12d): 92%

Verifier A canonical result is the consolidated re-audit: 0 critical, 0 major, 2 minor, 94.3%. Its first standalone-only pass raised critical findings that were false positives caused by not accessing the consolidated FY26 statements; that pass is superseded and preserved at outputs/reports/B12a-numerical-v1-standalone-only.md.

Scope note: Verifier C findings below cover the Gate 0 and Emerging Moat portion only. The valuation-adherence component is deferred to Phase 3.

## CRITICAL

None across all four verifiers.

## MAJOR

| Verifier | Location | Note |
|---|---|---|
| B (red-flags) | B05 §1B/§4C, Call p.9-10 | Embryologist-productivity red flag under-weighted: 5 embryologists vs 2,255 pickups (~451 each) against claimed ~120 each; analyst pushback deflected with "we are hardworking people". |
| C (framework) | B07 §OUTPUT / end of report | B07-emoat closing YAML block not emitted; breaks machine-readable Pillar-3 handoff. Prose content intact, no score or decision change; remediated by the orchestrator writing B07-emoat.yaml. |
| D (peers) | B06 Part 3, KAYA Q4 FY25 (29-May-2025) row | Peer-quarter mislabeled CITED-ONLY though a load-bearing Rajiv Suri quote from that call supports the Q2 CONTRADICTED verdict; true peer utilisation is 12/12, not the 11/12 the coverage map implies. |

## MINOR

| Verifier | Location | Note |
|---|---|---|
| A (numerical) | B03 Phase 3 DuPont | Tables lack inline (S)/(C) notation; presentation clarity only, no numerical error. |
| A (numerical) | B05 Concall CFO | Rs 724.72L cash from operations stated on a consolidated pre-interest-paid basis; could clarify the operating-activities basis in future rounds. |
| B (red-flags) | B05 §2C/§4C, Call p.6 vs p.7 | "Almost zero" debt framing not itemised against Rs 24.56 Cr borrowings that rose in absolute terms from Rs 20.61 Cr; only the ratio fell 0.45x to 0.16x. |
| B (red-flags) | B05 §3D/§4C, Call p.9 | Q4 quarterly cycle-count question unanswered; only the full-year 2,255 figure given. |
| B (red-flags) | B06 Q4, Call p.9-10 | International-mix contradiction is sound but conflates bases (Gaudium 25-30% patient-count share vs peers' 2-4% revenue share); contradiction survives, denominator difference should be stated. |
| C (framework) | B01 Block A | RoCE/RoE used RHP KPI definitions rather than framework defaults; source-permitted as the screener CSVs were empty; A3 band unchanged at 5. |
| C (framework) | B01 Block F, M2/M5/M9 | M2 credits foreign-peer EBITDA (score 5) while M5/M9 mark peer data needed; defensible but asymmetric; moat count stays 3. |
| D (peers) | B06 Part 1, Q3 answer | Gurugram/pollution quote anchored to RAINBOW-Concall_Feb_2026 but verbatim in RAINBOW-Concall_Nov_2025; wrong quarter only, verdict unaffected. |
| D (peers) | B06 Part 1, Q3 answer | "~100 clinics (FY18) to 76" figure stated with no inline anchor; fact genuine in KAYA-Concall_Oct_2024 (Prateek Giri Q&A), anchor merely missing at point of use. |
