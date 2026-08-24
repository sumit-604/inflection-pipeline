# Verifier Summary: MANINDS, Phase 1

## Phase 1 confidence delta and acceptance rates

Overall 80 of 100. Band: normal (75 to 89), note specifics. No REWORK: 0 CRITICAL, all four acceptance rates above the 60 floor.

| Verifier | Component | Score | Acceptance rate |
|---|---|---|---|
| A (numerical) | Numerical acceptance | 96.6 | 96.6% |
| B (red flags) | Red flag coverage | 80 | 80% |
| C (framework, phase 1) | Framework adherence | 98 | 98% |
| D (peers) | Peer utilisation | 83.3 | 75% |
| Overall | min of four | 80 | — |

Phase 1 scope: Verifier C covers Gate 0 and Emerging Moat only. Valuation framework adherence is pending phase 3.

---

## CRITICAL

None across all four verifiers.

---

## MAJOR

| Verifier | Location | Finding | Disposition |
|---|---|---|---|
| A | 03-ardeep.md Phase 3A, standalone CFO/PAT 0.693x | Verifier A could not recalculate 0.693x; it used the screener Data_Sheet CFO (Rs 67.99 Cr), which is the consolidated line, giving 0.444x. Marked source_fidelity true. | FLAG CLEARED. Source re-check found the figure correct at the AR standalone cash flow statement (CFO Rs 95.06 Cr / PAT Rs 137.12 Cr = 0.693x). Consolidated 0.444x also verifies. FLAG-CASH direction unaffected; both below 0.7x. Re-checked by orchestrator 2026-08-21. |
| D | B06 Part 1, Q4 verdict, Jindal SAW hedging quote | The "we don't accumulate or hold steel in anticipation of getting the order" quote is attributed to Jindal SAW Oct 2025 (Q2 FY26) p.16; it does not appear there. It is in Jindal SAW May 2026 (Q4 FY26) p.8, same speaker. Underlying Q4 corroboration stands; the citation as written is not locatable. | Noted for live verification. No stage 6 re-run: the load-bearing order-book finding is independently anchored. |
| D | B06 Part 5, Saudi ownership hypothesis | Part 5 groups Ratnamani with Jindal SAW and Welspun under a "minority or joint local partner" framing, citing only Ratnamani Nov 2025 p.6-7. The CITED-ONLY Ratnamani May 2025 p.4 discloses the Saudi JV is 75% Ratnamani owned / 25% local partner, majority control. Available but unused; makes the grouping more confident than the evidence supports. | Noted for live verification. Does not flip the company-specific order-book finding. |

---

## MINOR

| Verifier | Location | Finding |
|---|---|---|
| B | Q4 FY26 concall p.16 vs p.3/p.7 | NPC margin step down (press release 20 to 25% EBITDA vs guided sustainable 15 to 18%) noted numerically but not flagged as a red flag; a downshift in the metric the deal was sold on. |
| B | Q4 FY26 concall p.16/p.18 vs Jindal SAW Jul 2026 p.4 | Hormuz disruption under disclosed vs peers: Man claims only 20 to 25% shipments affected and no decline, while Jindal SAW reports all outward MENA shipments suspended since March 2026; peer fact surfaced but not confronted as a contradiction. |
| B | Q1 FY26 concall p.11 | Q1 other income add back (incentives, forex) inflates the highest ever EBITDA margin narrative; operating margin ex other income fell 10% to 7% QoQ; management deflected. Not carried into the margin quality assessment. |
| B | 05-concall.md 2A / analyst note | FY26 consolidated growth framed as plus 13% off a pipe only FY25 base (about Rs 3,178 Cr); including the about Rs 369 Cr FY25 Merino one off makes consol growth roughly flat, understating the revenue miss vs 20% guidance. |
| A | 04-bizmodel.md revenue base year label | FY25 consolidated revenue Rs 3,505.35 Cr split (89.5% steel Rs 3,136.75 Cr + 10.5% RE Rs 368.60 Cr) exact per AR Note 44A p.247; minor clarity gap on stating "consolidated" basis upfront. Not source fidelity. |
| A | 07-emoat.md FY27 guidance anchor form | FY27 consolidated revenue guidance Rs 5,000 to 5,500 Cr including NPC verified against the Jun 2026 concall; anchor uses transcript position not a printed page number. Not source fidelity. |
| C | B01 Block A ROCE basis | ROCE denominator EBIT/(NetWorth+Borrowings) substituted for framework EBIT/(Total Assets minus Current Liabilities); data forced (no current liability split in screener), anchored, no score band change. |
| C | B01 Block B FCF (B2/B3) | FCF proxied as CFO+CFI for framework CFO minus capex; data forced (no capex line), stated as proxy, no score band change. |
| C | B01 Block B4 WC days | WC days computed ex payables (receivable + inventory only) as payables not separately disclosed; framework subtracts payable days; stated basis, no score band change. |
| D | B06 Part 1, Q4 verdict, "Peers silent" paragraph | Citation Ratnamani May 2025 p.9 for raw material / margin variance commentary off by one page; relevant exchange on p.10. Content accurate, page anchor imprecise. |
| D | Ratnamani H2 FY25 (Nov 2024), graded UNUSED | UNUSED grading reasonable overall, but one on theme line ("countries being protective and the local content required," p.7) supports the protectionism thread and was left unused. |

Verifier C Emerging Moat scan: 51 rules checked, 0 findings, adherence 100%. Recomputed classifications concur: Gate 0 AVERAGE (core 49), Emerging Moat STRENGTHENING (em 32).

---

## Verifier disagreement log

| Date | Run | Number/claim | Verifier A verdict + anchor | Downstream step + position | Disposition | Note |
|---|---|---|---|---|---|---|
| 2026-08-21 | maninds-2026-08-21 | B03 standalone CFO/PAT 0.693x FY25 | MAJOR, source_fidelity true; "does not recalculate" (used screener consolidated CFO Rs 67.99 Cr, giving 0.444x) | B03 sourced it from the AR standalone cash flow statement | FLAG CLEARED. Source re-check found the number at a correct anchor (AR standalone CF: CFO Rs 95.06 Cr / PAT Rs 137.12 Cr = 0.693x). Re-checked by orchestrator 2026-08-21. | FLAG-CASH direction unaffected; both standalone 0.693x and consolidated 0.444x below the 0.7x threshold. |
