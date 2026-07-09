# STAGE 12C — VERIFIER C: FRAMEWORK ADHERENCE AUDIT
## Smruthi Organics Ltd (SMRUTHI) | Run Date: 2026-07-09 | Model: Opus 4.8 (fresh context)

Scope: rule application only (not company quality, not raw-number sourcing — Verifier A owns numbers).
Frameworks audited as written: Gate 0 rules (prompts/01), Emerging Moat 20+R1 rules (prompts/07),
Master Prompt v3.3 Role 1 + Section 1B v3.3 Amendments + FTTCP v1.2.
Artifacts audited: B01 (01-gate0.md), B07 (07-emoat.md), B11 (11-valuation.md), B10 (10-assembly.md).

Severity: CRITICAL (would change a decision / >1x destination PE / flips Hurdle) | MAJOR (wrong, decision
survives) | MINOR (presentational/procedural).

---

## 1. GATE 0 (B01) — RULE-BY-RULE

Inputs re-derived from the stated ROCE/ROE/CFO/FCF series and the stated thresholds.

| Rule | Stated inputs | Threshold applied | Maker score | Recompute | PASS/FAIL |
|---|---|---|---|---|---|
| A1 Median ROCE | 10 vals, median (7.85+10.72)/2=9.285 | <10 → 0 | 0 | 9.29% → 0 | PASS |
| A2 Min ROCE | -0.99% (FY18) | <8 → 0 | 0 | 0 | PASS |
| A3 Median ROE | median (5.21+6.10)/2=5.655 | <12 → 0 | 0 | 5.66% → 0 | PASS |
| A4 ROCE trend | 7.74 vs 10.72 = -2.98pp | 1-3pp → 3 | 3 | 3 | PASS |
| B1 Cum CFO/PAT | 121.55/55.88=2.175 | ≥1.00 → 5 | 5 | 5 | PASS |
| B2 FCF+ years | 8/10=80% | 75-99 → 4 | 4 | 4 | PASS |
| B3 Cum FCF/PAT | 74.84/55.88=1.339 | ≥0.60 → 5 | 5 | 5 | PASS |
| B4 WC days | N/A (payables absent 8/10 yrs) | data gap → 0 | 0 | 0 (rule 5) | PASS |
| C1 Rev CAGR | (101.97/79.35)^(1/9)=2.83% | <5 → 0 | 0 | 0 | PASS |
| C2 PAT CAGR | (3.43/1.58)^(1/9)=9.00% | 5-9.9 → 1 | 1 | 1 | PASS |
| C3 +YoY prop | 4/9=44.4% | <50 → 0 | 0 | 0 | PASS |
| C4 PAT−Rev CAGR | 9.00−2.83=+6.17pp | ≥+3 → 5 | 5 | 5 | PASS |
| D1 ND/EBITDA | 6.09/12.69=0.48x | 0-1.0 → 4 | 4 | 4 | PASS |
| D2 Int cov | 6.34/1.68=3.77x | 3-4.9 → 2 | 2 | 2 | PASS |
| D3 D/E | 8.36/73.52=0.11 | 0.1-0.5 → 4 | 4 | 4 | PASS |
| D4 Current ratio | 5268.33/2656.44=1.98x | 1.5-1.99 → 4 | 4 | 4 | PASS |
| E1-E4 | no shareholding data in Gate0 inputs | data gap → 0 | 0 | 0 (rule 5) | PASS |
| M1 Pricing | margin −1.33pp, rev CAGR 2.83% | fails all bands → 0 | 0 | 0 | PASS |
| M2/M5/M7/M9 | PEER DATA NEEDED | 0 | 0 | 0 | PASS |
| M3 Cap eff | FAT 2.17x, ROCE 7.74% | FAT>1 & ROCE>12 fails → 0 | 0 | 0 | PASS |
| M4 Cust sticky | 5 decline yrs | 3+ decline → 0 | 0 | 0 | PASS |
| M6/M8 | no R&D line / no reach data | 0 | 0 | 0 | PASS |
| M10 Switching | overall growth + 5 decline yrs | 2+ decline band → 1 | 1 | 1 | PASS |
| M11 Network | latest 3yr −10.24% < prior +2.47% | not > prior → 0 | 0 | 0 | PASS |
| M12 Neg WC | WC days >45 | >45 → 0 | 0 | 0 | PASS |
| CAGR edge rules | C2 endpoints both + (1.58, 3.43); FY18 loss not an endpoint | no N/M | honoured | honoured | PASS |
| Core score | 3+14+6+14+0 | =37 | 37 | 37 | PASS |
| Moat class | 0 moats ≥3 | NONE | NONE | NONE | PASS |
| Data confidence | 10 yrs | 10+ full, no downgrade | applied | applied | PASS |
| Classification | core 37 | <40 → AVOID | AVOID | AVOID | PASS |
| DB1 Block A<8 | A=3 | cap GOOD (fires) | fires | fires | PASS |
| DB2 Block B<8 | B=14 | not triggered | not | not | PASS |
| DB3 med ROCE<10 | 9.29% | cap AVERAGE (fires) | fires | fires | PASS |
| DB4 cum CFO/PAT<0.5 | 2.18 | not triggered | not | not | PASS |
| DB5 pledge>15 | N/A | not asserted | not | not | PASS |
| DB6 ND/EBITDA>3 & IC<3 | 0.48/3.77 | not triggered | not | not | PASS |
| DB7 rev decline majority | 5/9 | cap AVERAGE (fires) | fires | fires | PASS |
| DB8 PAT neg last 3 | all + | not triggered | not | not | PASS |
| DB9 history<3 | 10 yrs | not triggered | not | not | PASS |
| Binding class | caps (GOOD/AVERAGE) less restrictive than base AVOID | AVOID | AVOID | AVOID | PASS |

**Gate 0 verdict: 45/45 rules PASS.** Every block score, moat test, deal-breaker, and the AVOID
classification re-derive exactly. Note (not a fail): Block E scored 0 on a pure data gap; B01 correctly
flags this as availability, not a governance failure, per CLAUDE.md.

---

## 2. EMERGING MOAT (B07) — RULE-BY-RULE

| Rule | Check | Recompute | PASS/FAIL |
|---|---|---|---|
| All 21 categories addressed | A1-A4,B1-B3,C1-C2,D1-D2,E1-E2,F1-F2,G1-G2,H1-H3,R1 each has evidence or NO EVIDENCE FOUND | 21/21 present in Section 3 summary | PASS |
| Raw matrix A3 | High×Medium = HM | 3 | PASS |
| Raw matrix B1 | Medium×Medium = MM | 2 | PASS |
| Raw matrix E2 | High×Medium = HM | 3 | PASS |
| Raw matrix F2 | Low×Low = LL | 1 | PASS |
| Raw matrix G2 | Medium×Medium = MM | 2 | PASS |
| Raw matrix R1 | Medium×High = MH | 3 | PASS |
| Multiplier A3 (📄) | 3×1.0 | 3.0 | PASS |
| Multiplier B1 (🎙️) | 2×0.7 | 1.4 | PASS |
| Multiplier E2 (📄) | 3×1.0 | 3.0 | PASS |
| Multiplier F2 (📄) | 1×1.0 | 1.0 | PASS |
| Multiplier G2 (📄) | 2×1.0 | 2.0 | PASS |
| Multiplier R1 (📄) | 3×1.0 | 3.0 | PASS |
| Adjusted total | sum | 13.4 | PASS |
| Classification band | 13.4 in 12-24 | MODEST | PASS |
| Completionist recount | 11 📄 across 6 categories; <12 categories active, within 3-6 base rate | performed & consistent | PASS |
| No claim-as-documented | B1 (management narrative) correctly scored 🎙️ 0.7x, NOT 📄; E2 scored 📄 rests on genuine 📄 (Note 26 export figure) | no 🎙️-only scored as 📄 | PASS |
| Evidence mix | documented 11 / claim 2 / inference 1 | consistent with recount | PASS |
| Combined assessment | AVOID backward + MODEST forward → not TURNAROUND/HIGH POTENTIAL | AVOID | PASS |

**Emerging Moat verdict: 19/19 checks PASS.** Score 13.4 re-derives exactly; the one place a 🎙️ claim
could have been over-credited (B1 backward integration) was correctly discounted to 0.7x.

---

## 3. VALUATION (B11) — DEEPEST AUDIT, RULE-BY-RULE

| # | Rule (as written) | Maker application | Verifier recompute | PASS/FAIL |
|---|---|---|---|---|
| V1 | Method selection business-appropriate; P/B excluded (manufacturer, no lender carve-out) | EV/EBITDA 60% / P/E 40% / P/B N/A | correct — not a lender | PASS |
| V2 | Pillar 1 continuous formula 0.5×ROCE+7.5, floor 9x (NOT old bands) | 0.5×7.2+7.5=11.1x | 11.1x, above floor | PASS |
| V3 | FTTCP ROCE verdict = SOLE Pillar 1 authority | verdict DECLINING → FY[Y+1] lower-bound ROCE 7.2% | mapping correct for DECLINING | PASS (see M1) |
| V4 | Single-credit rule, route stated | "credited via: NOT CREDITED"; Strategic route also unused | consistent | PASS |
| V5 | Pillar 2 multiplier band matches CFO/PAT + FCF | **0.80x** applied | **band table gives 1.00x** — see FAIL below | **FAIL (MAJOR)** |
| V6 | Offset only on growth-induced; none on structural | no offset (drag not growth-induced) | correct given no offset applies | PASS |
| V7 | Pillar 3 matches EM/catalyst/evidence | EM 13.4 <25 → +0x | +0x | PASS |
| V8 | Pillar 4 Strategic; single-credit respected | +0x (no strategic asset; ROCE not credited) | +0x | PASS |
| V9 | UA three qualifiers all evidenced | listed≥12m T, FII+DII<3% T, Gate0≥60/EM≥25 FALSE → all_met FALSE | not applied — correct | PASS |
| V10 | UA in Amendment 3 order min(F×1.25, Cap) | F2=F (not applied); ordering noted for record | correct | PASS |
| V11 | Sector cap absolute | Pharma/CDMO 38x, no quality uplift (UA off) | 38x | PASS |
| V12 | Track 2 additive summary carried | A11.1×B0.80=C8.88 +0+0 = F8.88, H=min(8.88,38)=8.9x | arithmetic correct given 0.80x | PASS (input flows from V5) |
| V13 | RRM formula 1+(13.5−r)×0.12, r bounds [9,18], mult [0.70,1.60] | r=16 → 1−0.30=0.70 (floor); 8.88×0.70=6.2x | correct | PASS |
| V14 | Both tracks carried through every FV and verdict card | T1 & T2 in 3.1/3.2/4A/4C/4D/4H | present | PASS |
| V15 | Conservative track governs on >15% divergence | divergence 30.3% → Track 1 (RRM) governs | (8.9−6.2)/8.9=30.3%, T1 lower | PASS |
| V16 | Hurdle Ratio (1+g)³×(destPE/CurPE), threshold 1.953 | HR(base)=1.191×0.152=0.181; HR(bull)=1.368×0.152=0.208 → STOP | recompute matches; STOP | PASS |
| V17 | Grade-C gate on Bull EPS CAGR (base+5% max) | Bull CAGR capped 6+5=11% | correct (grade C = Mixed) | PASS |
| V18 | Section 2A Bull face-value only grade A/B | Bull held to SOM 9%, not mgmt face value | correct for grade C | PASS |
| V19 | SOM cross-check performed | base rev CAGR 5% < SOM 9.0% → consistent | performed | PASS |
| V20 | 4D probability weights match grade | grade C → 35/45/20 | correct (Mixed mapping) | PASS |
| V21 | Every unresolved input → stated conservative rule, no silent fill | 7 unresolved inputs each with rule | no silent fills | PASS |
| V22 | One-improvement-one-mechanism | ROCE recovery credited nowhere | no double-credit | PASS |
| V23 | Exit EV/EBITDA traces to Section 1B (0.6-0.7x of dest PE) | 0.65x × dest PE | within sanctioned band; P/E exit = 1B only | PASS |
| V24 | FTTCP run BEFORE Role 1 (structural) | verdict self-derived in-stage; no discrete FTTCP artifact | procedural gap — see M2 | **FAIL (MINOR)** |

### FAIL DETAIL

**M1 (MAJOR) — Pillar 2 cash multiplier: 0.80x applied where the written band table yields 1.00x.**
The Pillar 2 band table keys the multiplier off the CFO/PAT ratio and CFO sign. Smruthi's cumulative
CFO/PAT is 2.80x (B10) / 2.18x (B01 10-yr) and latest FY26 CFO/PAT 6.49x — all far above 0.70x — and
**CFO was positive in every one of the last 10 years** (B01 Block B series). The 0.80x band is defined as
"CFO/PAT below 30% OR CFO negative"; neither condition holds. FCF was negative FY24/FY25, but FCF-negative
is not the CFO-negative band criterion. With volatile/inconsistent conversion (strong cumulative, two
weak FCF years), the as-written placement is the **1.00x "volatile — some good years, some bad"** band.
The maker chose 0.80x on the INDETERMINATE-conservative meta-rule and cited "CFO/FCF negative in recent
years," which conflates FCF with CFO.

Recompute with Pillar 2 = 1.00x:
- Quality-Adjusted Base = 11.1 × 1.00 = 11.1x; Raw/Track 2 destination = min(11.1, 38) = **11.1x** (maker 8.9x).
- Track 1 (governing) = 11.1 × 0.70 = **7.8x** (maker 6.2x).
- Both move destination PE by >1x (Track 2 +2.2x; Track 1 +1.6x).
- Hurdle: HR(bull, T1 7.8x) = 1.368 × (7.8/40.80) = 1.368 × 0.191 = 0.261 → still **STOP**.
- Decision: still **AVOID** (40.8x current vs single-digit destination; every scenario negative CAGR).

Severity call: the >1x destination-PE movement meets Verifier C rule 5's literal CRITICAL threshold, but
the error is (a) in the conservative direction, (b) transparently documented as an INDETERMINATE call,
and (c) does NOT flip the Hurdle verdict or the decision. Per the top-of-file severity definition
(CRITICAL = "would change a decision"), this is **MAJOR**. A stricter reader may escalate to CRITICAL on
the >1x criterion alone; the correction is recommended regardless. It does not affect the AVOID.

**M2 (MINOR) — FTTCP ROCE forward verdict self-derived inside Role 1 rather than injected from a discrete
FTTCP stage.** Master v3.3 / FTTCP v1.2 make FTTCP-before-Role-1 structural and the ROCE forward verdict
the SOLE Pillar 1 authority. B10 carries no FTTCP verdict (listed as unresolved input #6); the valuation
derived DECLINING in-stage. The derivation follows FTTCP rules (backward STRUCTURALLY LOW; "if growth
stopped tomorrow" test → NO; bias-to-DECLINING per rule 12) and adopts the lowest/most-conservative
verdict, so the Pillar 1 input is not distorted. Procedural gap only; no numeric impact.

---

## 4. SUMMARY

- Gate 0: 45/45 PASS. Classification AVOID re-derives exactly.
- Emerging Moat: 19/19 PASS. Score 13.4 re-derives; no claim-as-documented inflation.
- Valuation: 22/24 PASS. One MAJOR (Pillar 2 band 0.80x vs as-written 1.00x, decision-neutral), one MINOR
  (FTTCP verdict self-derived in-stage).
- Recomputed destination PE differs (T2 8.9→11.1x, T1 6.2→7.8x) but Hurdle = STOP and decision = AVOID are
  unchanged and correct. No CRITICAL. No rework trigger from Verifier C (acceptance ~98% >> 60%).

The valuation's overall posture is over-conservative, not over-crediting; for an AVOID call this
reinforces rather than distorts the destination. Every pillar, both tracks, the Hurdle Ratio, the
credibility-grade gates, and the 4D weights are otherwise applied as written.
