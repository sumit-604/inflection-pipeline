# B12c v2 — VERIFIER C FRAMEWORK ADHERENCE (VALUATION SCOPE)

**Company:** PERMAGNET | **Run:** runs/permagnet-2026-08-19 | **Model:** claude-opus-4-8
**Scope:** Phase-3 valuation. Audits B10-assembly, 11-valuation-v3 / B11-v2-valuation.yaml,
14-thesis-v2 / B14-v2-thesis.yaml against Master v3.6 (Role 1 + Role 2), Section 1B
v3.3+v3.5.1+v3.6+v3.7, FTTCP v2.1. This file does NOT touch the 19-Aug B12c records.
**Note:** rule APPLICATION only; raw-number fidelity belongs to Verifier A.

---

## 1. ROLE 1 VALUATION — per-rule compliance

| # | Rule (source) | Verdict | Recompute / note |
|---|---|---|---|
| V1 | Continuous Pillar 1 formula 0.5×ROCE+7.5, floored 9x, not old bands (v3.6 Amdt 11) | PASS | 0.5×16.45+7.5 = 15.725 → 15.7x. Continuous form applied. |
| V2 | Pillar 1 15.7x on core ROCE 16.5%, matches deliberation Section 5 | PASS | Deliberation line 82 = 15.7x (Amdt 11, 0.5×16.45+7.5). Applied exactly, not re-derived. |
| V3 | FTTCP ROCE forward verdict sole Pillar 1 authority (STAGNANT, route NONE) | PASS | Route A fails (CWIP+adv <20% CE); Route B barred on STAGNANT. Recovery NOT credited. Matches FTTCP v2. |
| V4 | Single-credit honoured with route stated (Amdt 4) | PASS | Recovery not credited via Pillar 1 nor Strategic; alloys catalyst credited in forward ROCE read, held out of Pillar 3. Route stated (deliberation Override 2). |
| V5 | Pillar 2 multiplier matches stated determination | PASS | 1.00x growth-induced; FCF -25.75 Cr blocks elite band. Matches deliberation. No structural offset misapplied. |
| V6 | Pillar 3 +0x matches gated determination | PASS | Amdt 16 gate OPEN at 16.5% > ~13.5% CoC but HELD by operator (single-credit). Matches Override 2. |
| V7 | Strategic premium +0x | PASS | ROCE-recovery route not used → +0x. |
| V8 | UA in Amendment 3 order min(F×1.25, cap), 3 qualifiers evidenced | PASS | 15.7×1.25 = 19.625 → 19.6x BEFORE cap. Qualifiers: listed since 1960 (≥12m), EM 26≥25, FII+DII ~0.01%<3%. All evidenced. |
| V9 | Sector cap absolute, not quality-uplifted | PASS | Cables/Industrial 25x. min(19.63, 25)=19.6x. Non-binding, correct. |
| V10 | RRM formula 1+(13.5−r)×0.12, bounded [0.70,1.60] (Master v3.6 §RRM) | PASS | r=15.0% (14 base +0.5 gov +0.5 complexity; 12A/12C no r-UP). 1+(13.5−15)×0.12 = 0.82. 19.6×0.82 = 16.07 → 16.1x. |
| V11 | Both tracks carried through every FV and the verdict card | PASS | Additive + RRM present in Section 4 slices, Section 5 SOTP, hurdle, entry, verdict card. |
| V12 | Conservative track governs entry | PASS | RRM 16.1x sets entry (Rs 252-361). Divergence 12.4% (<15% mandate) but RRM used regardless; conservative, no decision impact. |
| V13 | Hurdle Ratio = (1+CAGR)³ × (Dest PE mid ÷ Current PE), pass ≥1.953, credibility-grade Bull gate (Amdt 2) | PASS | RRM base 1.12³×(16.1/38.5)=0.59; additive base 0.72; Bull capped 17% (grade C = Base+5%): RRM 0.67 / additive 0.82. All << 1.953 → STOP. |
| V14 | SOM cross-check present | PASS | Base core rev growth 12% < SOM-implied 20.1% → CONSISTENT (conservative, no cut). |
| V15 | Every unresolved input handled by stated conservative rule, no silent fills | PASS | Market PE, QMPL EBIT, segment split, FY27 guidance, through-cycle ROCE, restricted-cash all NOT FOUND / flagged; 12% converter ROCE stated generous. No estimate. |
| V16 | One-improvement-one-mechanism, no double-credit | PASS | Transformation priced in option slices; alloys catalyst SHARED, in forward ROCE only; Pillar 3 +0x. SHARED-CATALYST flag MOOT. |
| V17 | NdFeB slice converter multiple 13.5x per v3.7 Amdt 17; did NOT inherit core multiple | PASS | 0.5×12+7.5 = 13.5x on assumed 12% through-cycle ROCE; no UA; both tracks. Key Note 1 sensitivity confirms core PE would lift additive base FV to ~959 > CMP — converter discipline correctly held. |
| V18 | Method plurality — Section 1A matrix + ≥2 methods + triangulation, or justified single-method | PASS | Section 1A matrix present; SOTP primary with core P/E + option valuation triangulating inside; DCF/EV-EBITDA rejected with reason. |

**Recomputed destination PE:** additive 19.6x / RRM 16.1x / NdFeB converter 13.5x — CONCUR, no change.
**Recomputed decision:** AVOID (on valuation) — CONCUR.

---

## 2. ROLE 2 THESIS — per-rule compliance (Master v3.6 Role 2)

| # | Rule (source) | Verdict | Recompute / note |
|---|---|---|---|
| R1 | Five-verdict gate applied; AVOID routing justified vs WATCHLIST/INSUFFICIENT (line 1000, 1020-1024) | PASS | AVOID fires on 3 triggers (Gate 0 AVERAGE, Hurdle STOP, U/D <2x); WATCHLIST rejected (thesis not strong); INSUFFICIENT rejected (no single named resolving event). |
| R2 | AVOID triggers per line 1024 | PASS | Gate 0 AVERAGE ✓, Hurdle STOP ✓, U/D 0.17<2x ✓. Any one sufficient; three hold. |
| R3 | Hurdle consumed, not re-derived; STOP carried | PASS | Consumes Role 1 STOP; verdict card matches. |
| R4 | Upside/Downside ratio computed (line 829: Upside base / Downside bear, ≥2x) | MINOR | Used additive BULL upside (Rs 965) not base, cross-track vs RRM bear (Rs 393) → 0.17. Deviation from literal "Upside (base)"; base upside gives a WORSE ratio (~0.02). More generous than spec, still << 2x. No decision/verdict impact. |
| R5 | Position-sizing caps (lines 1049-1055, 862-870, 1389) | PASS | Gate 0 AVERAGE bars Medium/Large; Promoter CAUTION < TRUSTWORTHY bars Medium; dispersion RRM 52.7% / additive 49.3% (40-80% band) caps Medium; tightest → Small ceiling. Conviction Outlier barred (EM STRENGTHENING not EXPANSION). |
| R6 | Entry conjunction anti-value-trap stated (line 1026) | PASS | Section 7 verdict box states both-conditions gate + ex-full-plan recompute (Rs 216 / MoS 151). |

---

## 3. SUMMARY

- Rules checked: 18 valuation + 6 Role 2 = 24.
- FAILs: 0 CRITICAL, 0 MAJOR, 1 MINOR (R4 upside/downside numerator uses bull not base; no decision impact).
- Destination PE recompute CONCURS (19.6x / 16.1x / 13.5x converter). Decision CONCURS (AVOID).
- The single decision-load-bearing framework trap — extending the core quality multiple to the
  CONVERTER NdFeB slice (which would lift additive base FV to ~Rs 959 > CMP 882) — was correctly
  avoided per v3.7 Amendment 17.
- Framework-adherence confidence component: +0.14 (clean; one MINOR, zero MAJOR/CRITICAL).
