# Chunk 15. Damodaran cost of capital, ERP, terminal growth cap, and the relative valuation module

Loaded by: Role 1 Section 1B RRM Track 1, relative PE expression and Step 1C; Section 3 DCF and P/B. Pipeline: stage 11 (override 11: marks Step 1C PENDING LIVE PEER TABLE); claude.ai (supplies the live peer table and fetches market data); Verifier C (12c).
Sources in force: macro-sheet.md (live, monthly); Master v3.7 §1B RRM Dual-Track and Relative PE Expression, §3 DCF, P/B and EV/EBITDA; Section 1B v3.3 Amendment 4.4; v3.6 Amendments 12, 13, 15; v3.9 Amendment 20; FTTCP v2.3 Modules B2, B8.

## Macro sheet inputs (read the live file every run)

`macro-sheet.md` sits at the repo root and is refreshed monthly. Every Role 1 run cites it with its month stamp. Never copy a value into an output without that stamp. If the sheet is past its stated next-refresh date, flag it as stale.

Fields used by Section 1B:

| Field | Used for |
|---|---|
| Rupee risk-free rate (10-year G-sec) | terminal growth ceiling; market cost of equity |
| ERP including India country risk (Damodaran) | market cost of equity ≈ risk-free + ERP |
| Nominal GDP growth (current FY) | DCF terminal growth ceiling |
| CPI inflation and outlook; real GDP growth | internal consistency check |
| Market-wide earnings growth | growth-scarcity context for the relative discussion |
| Nifty 50 PE (TTM) | market PE denominator for the relative destination PE |
| Nifty Smallcap 250 PE and its median gap | context for relative bands on small caps |

Framework consistency check carried by the sheet: when market cost of equity (risk-free + ERP) sits 100 bps or more away from the RRM neutral point of 13.5%, flag the RRM for a recalibration review. The sheet's GARP regime note is not a Section 1B input; see open ruling OR-7 in SKILL.md.

## RRM Track 1 (required-return multiplier)

- **Track 1 destination PE = Fundamental Base PE × RRM**, capped at the (quality-uplifted) sector cap.
- **RRM = 1 + (13.5% − r) × 0.12, bounded ×0.70 to ×1.60.**
- (13.5 − r) is in percentage points: r = 16% gives −2.5, not −0.025.
- Base r: small/micro 14%, mid 13%, large-quality 12%. Adjust for durability and governance. Bound r in [9%, 18%].
- Durability and governance drive the discount rate through RRM, not additive PE points.

### r-adjustment single-credit rules (Amendments 12, 13)

- **12A.** No r adjustment for poor cash conversion. Pillar 2 owns it (0.65x structural multiplier).
- **12B.** Where the durability band is Moderate or Unproven BECAUSE of cyclicality, cap the cyclical r-surcharge at +0.75 (its range is otherwise +0.75 to +1.5). Where the band is docked for another reason, the full surcharge range applies. State why the band is docked.
- **12C.** No short-record r surcharge. A record under five years listed defines the Unproven durability band, which owns short-record risk. Other genuine risks of a young company are priced through their own channel on their own evidence.
- **13. Complexity discount.** Any one trigger (high subsidiary count obscuring where profit and cash sit; dense material related-party transactions; a qualified or adverse audit opinion or an emphasis of matter going to the numbers) raises r by +0.5. Complexity lives in r and nowhere else. It is additive to the durability and governance adjustments.
- The numeric r adjustments for each durability and governance band are NOT FOUND in frameworks/. State the adjustment used and its basis; never invent a table.

Worksheet line: "r base ___%; durability adj ___ (band: ___, reason: ___); governance adj ___; cyclical surcharge ___ (capped at +0.75 per 12B? Y/N); complexity adj ___ (Amendment 13); cash-conversion r-UP: none per 12A; short-record r-UP: none per 12C; final r ___% (bounded [9%,18%])."

### Minimum ROCE requirement (FTTCP Module B2)

Minimum ROCE = the r the valuation uses. Where the RRM r is not yet computed at the FTTCP stage, the standing default is 13.5% for micro and small caps (operator Gate E).

## Cash flow and asset methods

### DCF

| Parameter | Bear | Base | Bull |
|---|---|---|---|
| Projection period | 5 years | 5 years | 5 years |
| Revenue CAGR | ___% | ___% | ___% |
| FCF as % of revenue | ___% | ___% | ___% |
| Terminal growth rate | 4% | 5% | 6% |
| WACC / discount rate | 14% | 12% | 11% |

- WACC for Indian equities: 11-14%.
- **Terminal growth may not exceed 6%, AND may not exceed the nominal GDP growth on the latest macro sheet.** Cite the month stamp and the nominal GDP figure. The macro sheet's standing practice also holds terminal growth at or below the risk-free rate, so the effective ceiling is the lowest of the three.
- FCF as % of revenue stays consistent with Pillar 2, with FTTCP Module B1 funded growth and with Module B4 operating earnings. A structural 0.65x cash name does not see cash conversion improve inside the DCF.
- Sensitivity grid: WACC 11 / 12 / 13 / 14% against terminal growth 4 / 5 / 6%.
- Share of value from terminal value above 70% → the DCF is too sensitive and carries lower weight.

### P/B (primary for lenders)

Theoretical P/B = ROE ÷ cost of equity, with CoE of 12-14%. For lenders the Section 1B destination PE (Pillar 2L, ROE-based Pillar 1) is the cross-check.

### EV/EBITDA

EV/EBITDA destination ≈ 0.6-0.7x of the PE destination for most businesses. Where capex runs well above depreciation, EBITDA overstates and the multiple goes lower. Use operating EBITDA; add non-operating asset value in the bridge; subtract the Module B7 Year 3 net debt.

## Relative valuation module

### Relative PE expression (Amendment 15)

- **Relative destination PE = absolute destination PE (H) ÷ market PE** (latest macro sheet), compared against the name's own historical relative band and its sector's historical relative band.
- Cite FTTCP Module B8. B8 HIGH → the convergence target supports H toward the upper end of the H ±7.5% range. B8 NONE → the relative expression checks that H assumes no re-rating the peer set does not support.
- The sector cap stays the binding ceiling. The relative expression only informs where inside the range H sits.
- Show: "absolute H ___x | market PE ___x (macro sheet dated ___) | relative destination PE ___ | name historical relative band ___ | sector historical relative band ___ | B8 rating ___ | conclusion on where in the range H sits."

### FTTCP Module B8 (consumed, not recomputed)

(a) relative position within the peer set; (b) companion-variable test: the discount is not explained by worse growth, worse ROCE or higher risk; (c) sector dislocation check: the sector is not collectively dislocated against its own market-relative history; (d) verdict HIGH (with convergence target and the dated binary gate that starts the migration) / MODERATE / NONE.

### Step 1C: relative valuation cross-check (Amendment 20)

- **20.0 Placement.** After the pillar build (both tracks) and before the verdict card. Mandatory in every Role 1 carrying a Section 1B destination PE. It adds a display step and one governance rule; it replaces neither Section 1A nor the pillar derivation.
- **20.1 Live peer table, supplied by Claude web.** 4-6 listed peers, each with trailing P/E; clean/forward P/E (state which and the earnings basis); ROCE; growth (revenue or EPS, stated); net debt or net cash; governance (one word with basis: pledge, related party, audit, regulator). Every figure carries source and date. Multiples from model memory are stale and barred (Correction 6). Without a live, dated, sourced table the step displays PENDING LIVE PEER TABLE and the pillar destination governs.
- **20.2 Clusters.** QUALITY cluster (higher ROCE, higher growth, cleaner governance, higher clean/forward multiple) and VALUE cluster, identified on normalised clean/forward earnings, never trailing blended P/E. State each peer's cluster and a one-line reason.
- **20.3 Placement with signed adjustments** against each cluster: quality gap (ROCE and durability); growth gap; governance discount; size/liquidity discount; cyclicality/converter position (converters on through-cycle earnings). Output = the ADJUSTED PEER BASE, not the raw cluster multiple.
- **20.4 Bear / base / bull relative exit multiples.** Base = the adjusted peer base. Bear and bull move it by the peer dispersion observed in the live table, not by a round-number spread. Same earnings basis as the entry (18.1), on normalised earnings.
- **20.5 Governance rule.** Pillar destination (governing track) more than 30% below the adjusted peer base (pillar < 0.70 × adjusted peer base) → the RELATIVE multiple governs the exit and the pillar shows as a cross-check line. Otherwise the pillar governs and the peer table is the cross-check. Always print pillar destination, adjusted peer base, % gap and which governs. The 30% threshold is fixed.
- **20.6 Sector cap.** The relative multiple governs within [pillar destination, sector cap]. An adjusted peer base above the cap is a cap-review flag, never priced in.
- **20.7 Annual cap review** against live peer medians, by operator ruling logged in the cap table (chunk 05).
- **20.8 Recompute on the governing multiple, in order:** Year N exit price (18.1; option slices per 18.3 / 18.4); FV path and FV CAGR (19.0-19.1); return-source label and decomposition line (19.2-19.3); entry zone. The pillar-based values stay as the labelled cross-check.
- **20.9 Operator-approved base binds.** Where the operator approved a destination PE base and earnings basis at the FTTCP pillar-approval gate, Step 1C cross-checks that base. Report any divergence plainly (pillar, approved base, adjusted peer base, the 20.5 choice) and value on the approved base unless the operator re-rules.
- Step 1C changes the exit multiple, never the decision rules. A relative multiple that lifts fair value still passes the Hurdle Ratio, the upside/downside gate, the entry conjunction and every active flag. It earns no premium and re-credits no quality already in the pillar build. It runs on the Amendment 21 forward base.
