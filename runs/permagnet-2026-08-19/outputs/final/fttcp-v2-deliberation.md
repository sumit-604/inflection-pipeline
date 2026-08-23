# PERMAGNET — FTTCP v2 Deliberation and Sign-Off

Company: Permanent Magnets Ltd | Ticker: PERMAGNET | CMP Rs 882 (screener.in, 20-Aug-2026)
Run: runs/permagnet-2026-08-19 | First workup | NO-CONCALL MODE
Sign-off date: 2026-08-23 | Operator: Keerti Kaushik

This file supersedes the 19-Aug deliberation on three points: the four-layer Section 1B stack
(v3.3 + v3.5.1 + v3.6 + v3.7), the repaired cash series (handover dossier supersession S1), and the
operator option inputs (dossier Section 6). The 19-Aug records stay committed and untouched.

---

## 1. Final FTTCP verdict, in the operator's words

The operator adopted Reading 2 and held the AVOID. In the operator's own framing across this run:
"the future is paid for, in the safe box" — the transformation is priced as option value, not a
core growth premium. The core-ROCE recompute raises the quality base but does not move the decision:
"both ends clear 13.5%" and the AVOID "survives." Composite +2 of 8, DEEP WATCH leaning AVOID.

The whole call turns on one print: the core keeps converting cash while a relay or neodymium order
finally appears, at a price inside the entry zone.

---

## 2. Final rulings after review

The draft rulings stand as written in fttcp-v2-draft.md, with one changed by operator override.

| # | Ruling | Confidence | Status |
|---|---|---|---|
| Forward window | 3m primary, 6m secondary, 12m ROCE | sure | unchanged |
| Business type | Standard four transitions (split archetype, not a lender) | sure | unchanged |
| Workup intent | First workup; Role-1 fields N/A pre-valuation | sure | unchanged |
| Sector cap row | Cables / Industrial products 25x (manifest defect corrected) | fairly sure | unchanged, non-binding |
| Cash conversion | Growth-induced, repaired series (dossier S1) | fairly sure | unchanged |
| ROCE state | STAGNANT backward; NON-CONVERTER | sure | unchanged |
| Core-ROCE basis | Reading 2, core ex-QMPL 16.5% | fairly sure | OVERRIDE, see 3 |
| Composite / position | +2 of 8, DEEP WATCH leaning AVOID | sure | unchanged |

---

## 3. Operator overrides at the P/E gate (23-Aug-2026)

**Override 1 — core ROCE basis. Reading 1 to Reading 2.**
- Draft / block determination: Pillar 1 off CONSOLIDATED ROCE 12.54%, base 13.8x.
- Operator ruling: adopt Reading 2, anchored core ROCE band 15.6-16.5% (operating 16.5% headline, ex
  the Rs 1.74 Cr one-off), Pillar 1 base 15.7x (band 15.3-15.7x).
- Operator reasoning (quoted): "READING 2 ADOPTED per the pre-stated rule ... both ends clear 13.5%.
  ... The 19-Aug approved 13.8x base is superseded by this anchored recompute; record the
  supersession." Anchors in fttcp-v2-core-roce-recompute.md, all AR-FY26.

**Override 2 — Pillar 3, gate open but held.**
- Draft determination: +0x, Amendment 16 gate shut (12.54% < CoC).
- Operator ruling: hold +0x even though the gate now opens at 16.5%.
- Operator reasoning (quoted): "Single-credit: the transformation is priced in the option slices;
  the alloys catalyst is SHARED and already credited in the forward ROCE read. Revisit on audited
  FY27 core revenue growth durably above mid-teens."

**Confirmations (no change from draft):**
- Earnings basis: "ONE-YEAR-FORWARD confirmed, FY27 core operating EPS ~Rs 22.9 (grade-C build)."
- Pillar 2: "1.00x accepted; add the upgrade trigger — a third consecutive strong conversion year in
  FY27 audited numbers lifts it to 1.15x at the next refresh."

---

## 4. Cross-family grade outcome

Cross-family check did NOT run. verifiers/fttcp_crossgrade.py exits SKIPPED (exit 3): no cross-family
key configured. Per the command rule, FTTCP confidence is treated one notch lower for the absence of
the third-family read. No grader divergence to resolve.

---

## 5. OPERATOR-APPROVED VALUATION PILLARS (authoritative for Phase 3)

Phase 3 / Role 1 v2 MUST use this base and basis. It may not silently derive a different exit PE.

| Pillar input | Approved value | Basis / anchor |
|---|---|---|
| Pillar 1 ROCE | Core ex-QMPL 16.5% (band 15.6-16.5%) | fttcp-v2-core-roce-recompute.md, AR-FY26 |
| Pillar 1 normalization route | NONE (Route A fails <20%; Route B barred STAGNANT) | Section 1B v3.5.1 |
| Pillar 1 base PE | 15.7x (band 15.3-15.7x) | Amendment 11: 0.5 x 16.45 + 7.5 |
| Pillar 2 cash multiplier | 1.00x (growth-induced) | operator; 1.15x upgrade trigger on 3rd strong FY27 audited year |
| Pillar 3 growth premium | +0x (Amdt 16 gate OPEN, held) | operator single-credit; revisit on FY27 core rev > mid-teens |
| Strategic premium | +0x | ROCE-recovery route not used |
| Undiscovered Alpha | x1.25 (all 3 qualifiers) | Amendment 3 |
| Sector cap | Cables / Industrial products 25x (non-binding) | Section 1B table; 19.6x < 25x |
| **Destination PE, additive** | **19.6x (band 19.1-19.6x)** | 15.7 x 1.00 x 1.25 |
| **Destination PE, RRM** | **16.1x (band 15.7-16.1x)** | 19.6 x 0.82 |
| Earnings basis | ONE-YEAR-FORWARD | operator; FY27 core operating EPS ~Rs 22.9, grade-C |

Supersession recorded: the 19-Aug approved base (Pillar 1 13.8x, additive 17.3x, RRM 14.1x) is
superseded by this anchored Reading 2 recompute. The 19-Aug B11 record stays committed for audit.

Phase 3 option-slice inputs (operator, dossier Section 6): relay Rs 75 Cr at 45%; NdFeB 12% full /
40% modest. QMPL Rs 47.81 Cr ECB nets in the equity bridge. Outputs versioned fttcp-v2- /
11-valuation-v3 class; committed records untouched.
