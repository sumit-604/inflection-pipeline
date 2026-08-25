# Man Industries (MANINDS) — Verifier Summary (Phase 1)

## Confidence delta and acceptance rates

| Component | Verifier | Acceptance rate | Score used |
|---|---|---|---|
| Numerical (A) | B12a Haiku | 96.6% | 96.6 |
| Red flag coverage (B) | B12b Opus | 80% | 80 |
| Framework adherence (C) | B12c Opus, Phase 1 scope | 98% | 98 (Gate 0 97 + Emerging Moat 100) |
| Peer utilisation (D) | B12d Sonnet | 75% (acceptance); 83.3% peer utilisation | 83.3 |
| Overall | — | — | 80 (min; normal band 75 to 89) |

Counts across all four: 0 CRITICAL, 1 MAJOR before orchestrator review that CLEARED to 0, plus 2 MAJOR from Verifier D, and MINORs. No REWORK trigger. Phase 1 scope only; valuation framework adherence pending Phase 3.

## Findings, sorted by severity

### CRITICAL
None.

### MAJOR

| # | Verifier | Location | Finding | Disposition |
|---|---|---|---|---|
| 1 | A (B12a) | 03-ardeep.md Phase 3A, standalone CFO/PAT 0.693x | Verifier A flagged the 0.693x standalone CFO/PAT, saying it does not recalculate, having used the screener Data_Sheet CFO Rs67.99 Cr, which is the consolidated line | FLAG CLEARED. Source re-check found the figure at the AR standalone cash flow anchor: CFO Rs95.06 Cr / PAT Rs137.12 Cr = 0.693x exact. Verifier A mis-sourced the consolidated CFO. Re-checked by orchestrator 2026-08-21. FLAG-CASH direction unaffected; standalone 0.693x and consolidated 0.444x both sit below the 0.7x threshold. major_count_after_review = 0 |
| 2 | D (B12d) | B06 Part 1, Q4 verdict hedging quote | The Jindal SAW quote "we don't accumulate or hold steel in anticipation of getting the order" is attributed to Jindal SAW Oct 2025 (Q2 FY26) p.16. It does not appear there. It appears in Jindal SAW May 2026 (Q4 FY26) p.8, same speaker (Vinay Kumar Gupta). Underlying corroboration stands; the citation as written is not locatable at the stated anchor | Noted; tighten at live verification. Does not touch the load bearing order book finding |
| 3 | D (B12d) | B06 Part 5, Saudi ownership hypothesis | Part 5 groups Ratnamani under a "minority or joint local-partner" framing, citing only Ratnamani Nov 2025 p.6-7. The unused Ratnamani May 2025 p.4 discloses the Saudi JV is 75% Ratnamani owned / 25% local partner, majority control. The omission makes the ownership grouping more confident than the full evidence supports | Noted; correct at live verification. Does not flip any Phase 1 conclusion |

### MINOR

| # | Verifier | Location | Finding |
|---|---|---|---|
| 4 | A (B12a) | 04-bizmodel.md revenue base-year label | FY25 revenue Rs3,505.35 Cr split (steel Rs3,136.75 Cr + real estate Rs368.60 Cr) is exact against Note 44A p.247; minor clarity gap on stating the "consolidated" basis upfront. source_fidelity false |
| 5 | A (B12a) | 07-emoat.md FY27 guidance anchor form | FY27 guidance Rs5,000 to 5,500 Cr including NPC verified against the Jun 2026 concall; anchor uses transcript position not a printed page number. source_fidelity false |
| 6 | B (B12b) | Q1 FY26 concall p.11 | Q1 other income add back (incentives, forex) inflates the "highest ever EBITDA margin" narrative; operating margin ex other income fell 10% to 7% QoQ. B05 scoped Q1 as baseline only and did not carry this into margin quality |
| 7 | B (B12b) | Q4 FY26 concall p.5; Q2 FY26 p.14 | Consolidated revenue is essentially flat YoY, not the +13% B05 states, once the about Rs369 Cr Merino one off is stripped from the FY25 base; the FY26 revenue miss versus 20% guidance is larger than a pipe only comparison implies |
| 8 | B (B12b) | Q4 FY26 concall p.16 vs p.3/p.7 | NPC margin step down (acquisition press 20 to 25% EBITDA vs guided sustainable 15 to 18%) noted numerically by B05 but not raised as a red flag; a downshift in the metric the deal was sold on |
| 9 | B (B12b) | Q4 FY26 concall p.16/p.18 vs Jindal SAW Jul 2026 p.4 | Hormuz disruption under disclosed vs peers: MANINDS claims only 20 to 25% shipments affected with "no decline", while Jindal SAW reports all outward MENA shipments suspended since Mar 2026. B06 surfaced the peer fact but did not confront MANINDS's no decline claim |
| 10 | C (B12c) | B01 Block A ROCE basis | ROCE denominator substituted EBIT/(NetWorth+Borrowings) for the framework EBIT/(Total Assets - Current Liabilities); data forced by no current liability split in screener; anchored; no score band change |
| 11 | C (B12c) | B01 Block B FCF (B2/B3) | FCF proxied as CFO+CFI for the framework CFO minus capex; data forced by no capex line; stated as proxy; no score band change |
| 12 | C (B12c) | B01 Block B4 WC days | WC days computed ex payables (receivable + inventory only) because payables not separately disclosed; framework subtracts payable days; stated basis; no score band change |
| 13 | D (B12d) | B06 Part 1, Q4 verdict, "Peers silent" paragraph | Citation "Ratnamani May 2025 p.9" for raw material margin variance commentary is off by one page; the exchange is on p.10. Content accurate; page anchor imprecise |
| 14 | D (B12d) | Ratnamani H2 FY25 (Nov 2024) transcript, graded UNUSED | UNUSED grading reasonable overall, but one on theme line ("countries being protective and the local content required", p.7) supports the protectionism thread that Part 5/2E build mostly on a single Jindal SAW anchor, and was left unused |

Verifier C Emerging Moat scan: 51 rules checked, 0 findings, adherence 100%. Recomputed classifications concur: Gate 0 AVERAGE (core 49), Emerging Moat MOAT STRENGTHENING (em 32).

## Resolved Verifier A source-fidelity disagreement

| Field | Detail |
|---|---|
| Date | 2026-08-21 |
| Run | maninds-2026-08-21 |
| Number / claim | B03 standalone CFO/PAT 0.693x FY25 |
| Verifier A verdict + anchor | MAJOR, source_fidelity true, "does not recalculate"; Verifier A used screener Data_Sheet CFO Rs67.99 Cr (the consolidated line) |
| Downstream step + position | B03 sourced 0.693x from the AR FY25 standalone cash flow statement |
| Disposition | FLAG CLEARED. Source re-check found the number at the correct anchor: AR standalone CF, CFO Rs95.06 Cr / PAT Rs137.12 Cr = 0.693x. The screener CFO Rs67.99 Cr divided by standalone PAT Rs153.17 reproduces B03's separately stated consolidated 0.444x. Re-checked by orchestrator against the annual report standalone CF extract 2026-08-21 |
| Note | FLAG-CASH direction unaffected: standalone 0.693x and consolidated 0.444x both sit below the 0.7x threshold. Source fidelity gate PASS; 0 CRITICAL; acceptance 96.6% |
