# Man Industries (MANINDS) — Verifier Summary (Phase 3 Final)

## Confidence delta and acceptance rates

| Component | Verifier | Acceptance rate | Score used |
|---|---|---|---|
| Numerical (A) | B12a Haiku | 96.6% | 96.6 |
| Red flag coverage (B) | B12b Opus | 80% | 80 |
| Framework adherence (C) | B12c Opus, phase 1 + phase 3 | 98% p1 / 91% p3 valuation / 100% decision rules | 97 (Gate 0 97 + Emoat 100 + valuation 91 + decision rules 100) |
| Peer utilisation (D) | B12d Sonnet | 75% acceptance; 83.3% utilisation | 83.3 |
| Overall | — | — | 80 (min; normal band 75 to 89) |

Counts across all four: 0 CRITICAL, 1 MAJOR before orchestrator review that CLEARED to 0 (Verifier A source fidelity), 2 MAJOR from Verifier D, plus MINORs. No REWORK trigger. Verifier C phase 3: destination PE applied faithfully = true; 0 critical, 0 major, 2 minor.

Re-cut note (2026-08-26): Verifier C's two prior MINOR fails (Am4.3 Tier line, Am18.6 Merino dual display) are now fixed in the Phase 3 recommendation verdict card, and the governing track changed from the four pillar output to the operator relative multiples per Section 1B step 1C; the pillar output is retained as a cross-check. Confidence delta is unchanged; the relative override is an operator ruling, not a framework adherence delta.

## Findings, sorted by severity

### CRITICAL
None.

### MAJOR

| # | Verifier | Location | Finding | Disposition |
|---|---|---|---|---|
| 1 | A (B12a) | 03-ardeep.md Phase 3A, standalone CFO/PAT 0.693x | Verifier A flagged the 0.693x standalone CFO/PAT, saying it does not recalculate, having used the screener Data_Sheet CFO Rs67.99 Cr, which is the consolidated line | FLAG CLEARED. Source re-check found the figure at the AR standalone cash flow anchor: CFO Rs95.06 Cr / PAT Rs137.12 Cr = 0.693x exact. Verifier A mis-sourced the consolidated CFO. Re-checked by orchestrator 2026-08-21. FLAG-CASH direction unaffected. major_count_after_review = 0 |
| 2 | D (B12d) | B06 Part 1, Q4 verdict hedging quote | Jindal SAW quote "we don't accumulate or hold steel in anticipation of getting the order" attributed to Jindal SAW Oct 2025 (Q2 FY26) p.16; it appears in Jindal SAW May 2026 (Q4 FY26) p.8, same speaker. Underlying corroboration stands; the citation as written is not locatable at the stated anchor | Noted; tighten at live verification. Does not touch the load bearing order book finding |
| 3 | D (B12d) | B06 Part 5, Saudi ownership hypothesis | Part 5 groups Ratnamani under a "minority or joint local-partner" framing, citing only Ratnamani Nov 2025 p.6-7. The unused Ratnamani May 2025 p.4 discloses the Saudi JV is 75% Ratnamani owned / 25% local partner, majority control. The omission makes the grouping more confident than the evidence supports | Noted; correct at live verification. Does not flip any conclusion |

### MINOR

| # | Verifier | Location | Finding |
|---|---|---|---|
| 4 | C (B12c p3) | 11-valuation.md verdict card first line; B14-thesis | Am4.3: verdict card first line did not print "Tier: A | Hurdle: 25%". Tier A / 1.953 threshold used correctly in the Hurdle math. FIXED in the Phase 3 recommendation verdict card |
| 5 | C (B12c p3) | 11-valuation.md Section 3 Merino within hold slice | Am18.6: Merino slice priced resolution based per 18.2/18.3, but the static carry vs resolution dual display with per share delta was not shown. Immaterial (slice under 5% of FV, bear zero). FIXED in the Phase 3 recommendation card |
| 6 | A (B12a) | 04-bizmodel.md revenue base-year label | FY25 revenue Rs3,505.35 Cr split (steel Rs3,136.75 Cr + real estate Rs368.60 Cr) exact against Note 44A p.247; minor clarity gap on stating "consolidated" upfront. source_fidelity false |
| 7 | A (B12a) | 07-emoat.md FY27 guidance anchor form | FY27 guidance Rs5,000 to 5,500 Cr incl NPC verified against Jun 2026 concall; anchor uses transcript position not a printed page number. source_fidelity false |
| 8 | B (B12b) | Q1 FY26 concall p.11 | Q1 other income add back inflates the highest ever EBITDA margin narrative; operating margin ex other income fell 10% to 7% QoQ. B05 scoped Q1 as baseline only |
| 9 | B (B12b) | Q4 FY26 concall p.5; Q2 FY26 p.14 | Consolidated revenue roughly flat YoY, not +13%, once the about Rs369 Cr Merino one off is stripped; the FY26 revenue miss is larger than a pipe only comparison implies |
| 10 | B (B12b) | Q4 FY26 concall p.16 vs p.3/p.7 | NPC margin step down (press 20 to 25% EBITDA vs guided sustainable 15 to 18%) noted numerically by B05 but not raised as a red flag |
| 11 | B (B12b) | Q4 FY26 concall p.16/p.18 vs Jindal SAW Jul 2026 p.4 | Hormuz disruption under disclosed vs peers: MANINDS claims 20 to 25% shipments affected with no decline, while Jindal SAW reports all outward MENA shipments suspended since Mar 2026 |
| 12 | C (B12c p1) | B01 Block A ROCE basis | ROCE denominator substituted EBIT/(NetWorth+Borrowings) for the framework EBIT/(Total Assets - Current Liabilities); data forced; anchored; no score band change |
| 13 | C (B12c p1) | B01 Block B FCF (B2/B3) | FCF proxied as CFO+CFI for the framework CFO minus capex; data forced; stated as proxy; no score band change |
| 14 | C (B12c p1) | B01 Block B4 WC days | WC days computed ex payables; framework subtracts payable days; stated basis; no score band change |
| 15 | D (B12d) | B06 Part 1, Q4 verdict, "Peers silent" paragraph | Citation "Ratnamani May 2025 p.9" off by one page; the exchange is p.10. Content accurate; anchor imprecise |
| 16 | D (B12d) | Ratnamani H2 FY25 (Nov 2024), graded UNUSED | UNUSED grading reasonable, but one on theme line on protectionism (p.7) was left unused |

## Verifier C phase 3 valuation adherence audit

Scope: framework adherence of B11 and B14 against the operator approved pillars and the Section 1B layer set. 23 valuation rules checked, 21 passed, adherence 91%. Decision rule audit 100%. Audited against the pre-relative pillar build; the 2026-08-26 operator step 1C relative override sits on top of this as an operator ruling.

- Pillar 1 (0.5 x ROCE + 7.5): bear 14.5x, base 15.1x, bull 15.75x, all PASS; floor 9x and ceiling 30x respected; spot ROCE avoided (Am17.1); ROCE anchors match the operator ruling (gradient authorized 2026-08-25).
- Pillar 2 0.80x growth induced, no growth offset: PASS. Pillar 3 +0: PASS.
- RRM r build 16.0% (14.0 + 1.5 gov + 0.75 cyclical + 0.5 concentration - 0.5 durability - 0.25 moat): PASS; cyclical surcharge at the Am12b cap, no double dock.
- RRM multiplier 0.70x at the floor, applied to the full fundamental base in every scenario: PASS.
- Destination PE additive 11.6/12.1/12.6x and RRM 8.1/8.5/8.8x reproduce exactly; sector cap 20x not breached; no exit PE from outside Section 1B: PASS. These are now retained as the pillar cross-check; the governing exit multiple is the operator relative set (12/16/20x).
- Fair values additive 487/870/1271, RRM 340/611/888, each PE applied to its own FY30E op EPS (42.0/71.9/100.9): PASS. Governing relative fair values 504/1150/2018 apply the operator multiples to the same FY30E op EPS.
- Exit basis symmetry (Am18.1) forward both ends; bargain gain excluded from operating EPS: PASS. Horizon reaches Year 4 (Am18.0): PASS. FV path present, FV CAGR 21.2%, COMPOUNDER label on the card (Am19): PASS.
- Hurdle (pillar cross-check): forward PE 17.7x, base additive 1.21, threshold 1.953, Tier A, STOP recomputed: PASS. Divergence 30% > 15% so RRM governs within the pillar: PASS. Pillar entry high 313 = 611 / 1.953; pillar MoS 219 = 313 x 0.70: PASS. Governing relative Hurdle CONDITIONAL (base 1.61 fails / bull 2.09 passes), governing entry Rs412-589, MoS Rs412.
- Role 2 decision audit: verdict WATCHLIST consistent with the CONDITIONAL Hurdle, the U/D 2.08x pass and the governing entry zone; Small governance cap documented; 6 thesis broken conditions present; named BUY condition and entry conjunction present; return source label surfaced. All PASS.

Two MINOR fails, both presentational and now fixed in this synthesis: Am4.3 Tier line not printed on the verdict card first line; Am18.6 Merino dual display not shown. Decision unchanged in both.

Verifier C Emerging Moat scan (phase 1): 51 rules, 0 findings, adherence 100%. Recomputed classifications concur: Gate 0 AVERAGE (core 49), Emerging Moat MOAT STRENGTHENING (em 32). The valuation decision is WATCHLIST after the operator step 1C relative re-cut, Hurdle CONDITIONAL (prior pillar read was AVOID with Hurdle STOP, retained as the cross-check).
