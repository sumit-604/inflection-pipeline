# DSSL Verifier Summary

**Dynacons Systems & Solutions Ltd | DSSL | Run 2026-07-27 | Phase 3 final (includes phase 3 valuation adherence audit)**

## Confidence delta

| Component | Score | Verifier | Note |
|---|---|---|---|
| Numerical acceptance | 100 | A (B12a) | 0 CRITICAL, 0 MAJOR; 14 material figures verified clean |
| Red flag coverage | 84 | B (B12b) | BINDING; 1 MAJOR miss (capital intensity understated ~2.3x) |
| Framework adherence | 95 | C (B12c) | Gate0+EM 99, valuation 91; 1 MAJOR (UA-in-RRM) |
| Peer utilisation | 87.5 | D (B12d) | 14 of 16 peer calls used |
| Overall | 84 | min of four | Redflag bound, normal band, no downgrade, REWORK not triggered |

Acceptance rates: A 100%, B 75%, C 99% (gate0+EM) / 91% (valuation), D 88%. All at or above the 60% floor; no CRITICAL; REWORK not triggered.

## Findings, sorted by severity

### CRITICAL

None.

### MAJOR

| Verifier | Location anchor | Note |
|---|---|---|
| C (B12c-valuation) | B11 Section 1B RRM track / verdict card; B10 destination-PE table | UA x1.25 applied inside the RRM governing track. Master v3.3 RRM has no UA term (Amendment 3 scopes UA to additive Row F). Corrected: RRM ~19.5x not 24x; entry ~Rs851-1,064 not Rs1,048-1,310; MoS ~Rs851 not Rs1,048; RRM base Hurdle CONDITIONAL 1.69 not PASS 2.08. Decision impact none (WATCHLIST survives); actionability impact material (CMP moves above the conservative zone). Conservative reading governs. |
| B (B12b) | B05 vs Q4 FY26 transcript p4 / p5-6 / p13-14 | Fixed asset build carried only as PPE Rs8cr to Rs68cr; the Rs158cr figure cited by two analysts and the roughly Rs90cr gap left unreconciled; management dodged quantification; capital intensity of the pivot understated about 2.3x. Binds the redflag coverage score to 84. |
| D (B12d) | B06 Part 3 / coverage_map, 3i Infotech Jul-2023 and Jan-2025 rows | Both calls marked UNUSED as unrelated to any claim, yet both are directly and accurately cited in B06 Part 1 (Claim 4 and Claim 2). Internal inconsistency; peer utilisation understated by two transcripts (corrected 75% to 87.5%). Does not change any claim verdict. |

### MINOR

| Verifier | Location anchor | Note |
|---|---|---|
| B (B12b) | B05 red-flags vs Q4 FY26 transcript p7 | PAT flat YoY on +22% revenue (opex model earnings quality) not isolated as its own signal. |
| B (B12b) | B05 2A/1C vs Q3 p9 and Q4 p11 | Two quarter "judge us YoY not QoQ" deflection pattern and buried Q3 minus 3.3% / minus 3.6% QoQ decline not surfaced. |
| B (B12b) | B05 red-flags vs Q4 FY26 transcript p16 | Management admission of deliberate cost absorption to win acquisition customers not extracted (partly caught via B06 peer contrast). |
| B (B12b) | B05 red-flag / 2C vs Q4 transcript | Scripted "temporary blip" line given to five analysts (Akash Jain included), reported as four; undercount understates the flag. |
| C (B12c-valuation) | B11 yaml pillar_detail.roce_recovery_route | Label "pillar1-midpoint" but no midpoint computed (FY[Y+2] ROCE NOT FOUND, route NONE, current 30.17% used as sole anchor). Decision impact none. |
| C (B12c-valuation) | B14 Section 7 verdict box / reasoning point 3 | ENTRY CONJUNCTION (anti value trap) invoked citing an unconfirmed transition, not a fired thesis broken trigger. WATCHLIST correct but on DEEP WATCH grounds. Decision impact none. |
| C (B12c gate0) | B01 Block A ROCE derivation | Framework prefers source supplied ROCE; maker computed hybrid CE basis. Documented, cross validated vs Acuité, immaterial to the GOOD classification (capped by deal breaker 2). |
| C (B12c gate0) | B01 M4 Customer Stickiness = 3 | Borderline PASS; even a downgrade keeps the class GOOD. Internally faithful to the differently worded M4 versus M10 tiers. |
| C (B12c emoat) | B07 capex_embedded_growth_pct = 0 (FLAG-METHOD) | Bare 0 is a placeholder; the 2C formula is genuinely mismatched for an asset light legacy to capex heavy transition. Phase 3 must read the order book cross check (~108%), not the literal 0. |
| C (B12c emoat) | B07 6D combined assessment = GOOD+ | GOOD backward plus MODEST forward lifted a half tier; on the generous edge of latitude, no enumerated matrix cell violated; HIGH POTENTIAL correctly not claimed. |
| D (B12d) | B06 Part 2E / risks_peers_raise item 4 | Aurionpro cash conversion stated as 60 to 90% of EBITDA; transcript says 75 to 80% or more, "90% plus last year". Direction correct; 60% lower bound unsupported. |
| D (B12d) | B06 Part 3 / coverage_map, 3i Infotech Nov-2023 row | Marked UNUSED; contains a loosely analogous scaling pain / margin dilution data point not used. Low materiality; changes no verdict. |

## Notes on the binding and phase 3 components

Red flag coverage is the binding component at 84. Verifier B found 16 independent flags, caught 12, partially caught 3, missed 1 MAJOR (the capital intensity understatement above), and concurred with the B credibility grade (5 promise delivery spot checks, 5 confirmed, 0 wrong).

The phase 3 valuation adherence audit (Verifier C) checked 34 valuation rules, logging 1 MAJOR and 2 MINOR against a 91% acceptance rate. It concurred on the additive 30.0x cap bound destination, the Pillar 1 base 22.6x, the Pillar 2 neutral 1.00x with SOTP carve out, the Pillar 3 +3x, the UA ordering on the additive track, the RRM arithmetic, the Tier A entry mechanics, and the Role 2 WATCHLIST plus Small sizing. The single MAJOR is the UA-in-RRM insertion carried at the top of this file.

Verifier A logged 0 findings at 100% acceptance and raised no source fidelity flags, so no downstream re-derivation is subordinate to a Verifier A flag this run. History downgrade check CORRECT (FALSE); FTTCP conflation CLEAN (B07 firewalled from FTTCP).
