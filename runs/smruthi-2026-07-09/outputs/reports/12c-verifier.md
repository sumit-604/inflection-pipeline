# B12c — VERIFIER C: FRAMEWORK ADHERENCE AUDIT (RE-RUN on corrected B10 / re-run B11)
## Smruthi Organics Ltd (SMRUTHI) | Run Date 2026-07-09 | Model: Opus 4.8

Scope: rule-application audit only (numbers are Verifier A's domain). Frameworks: Gate 0 rules,
EM 20+1 scan rules, Master Project Prompt v3.3 (Role 1 + Section 1B v3.3 amendments), FTTCP v1.2.
Inputs audited: B01 (gate0), B07 (emoat), B10 (corrected assembly), B11 (corrected valuation).

Headline: the prior-run MAJOR (Pillar 2 cash multiplier 0.80x vs as-written 1.00x) is **RESOLVED** —
B11 now applies 1.00x correctly. One NEW MAJOR found in the RRM (Track 1) computation. Decision
(AVOID, Hurdle STOP) and the primary additive destination PE (11.1x) are unaffected and, if anything,
reinforced by the correction. No CRITICAL.

---

## TABLE 1 — GATE 0 (B01) COMPLIANCE

| # | Rule | As-written threshold | B01 value | Verdict |
|---|------|----------------------|-----------|---------|
| A1 | Median ROCE band | <10 = 0 | 9.29% → 0 | PASS |
| A2 | Min single-yr ROCE band | <8 = 0 | −0.99% → 0 | PASS |
| A3 | Median ROE band | <12 = 0 | 5.66% → 0 | PASS |
| A4 | ROCE trend latest vs earliest | decline 1-3pp = 3 | 7.74 vs 10.72 = −2.98pp → 3 | PASS |
| B1 | Cum CFO/PAT | ≥1.00 = 5 | 2.18 → 5 | PASS |
| B2 | FCF-positive yrs % | 75-99 = 4 | 8/10 = 80% → 4 | PASS |
| B3 | Cum FCF/PAT | ≥0.60 = 5 | 1.34 → 5 | PASS |
| B4 | WC-days change | N/A → 0 (rule 5) | data absent → 0 | PASS |
| C1 | Revenue CAGR | <5 = 0 | 2.83% → 0 | PASS |
| C2 | PAT CAGR | 5-9.9 = 1 | 9.00% → 1 | PASS |
| C3 | Positive YoY yrs % | <50 = 0 | 4/9 = 44.4% → 0 | PASS |
| C4 | PAT−Rev CAGR | ≥+3pp = 5 | +6.17pp → 5 | PASS |
| D1 | ND/EBITDA | 0-1.0x = 4 | 0.48x → 4 | PASS |
| D2 | Interest coverage | 3-4.9 = 2 | 3.77x → 2 | PASS |
| D3 | Debt/Equity | 0.1-0.5 = 4 | 0.11 → 4 | PASS |
| D4 | Current ratio | 1.5-1.99 = 4 | 1.98x → 4 | PASS |
| E1-E4 | Shareholder alignment | N/A → 0 (rule 5, data absent) | all 0 | PASS |
| F | 12 moat tests | ≥3 = present | M10=1, rest 0; 0 present → NONE | PASS |
| — | Core score sum | A+B+C+D+E | 3+14+6+14+0 = 37 | PASS |
| — | Grand total | core+moat | 37+1 = 38 | PASS |
| — | Moat classification | 0 present = NONE | NONE | PASS |
| — | Classification matrix | Core <40 = AVOID | 37 → AVOID | PASS |
| — | Data confidence | 10+ yrs full, no downgrade | 10 yrs → full | PASS |
| — | Deal-breakers | DB1(A<8), DB3(ROCE<10), DB7(rev decline maj.) fire; cap ≥ base | AVOID binds | PASS |
| — | CAGR edge rules | positive endpoints → compute | rev & PAT endpoints positive | PASS |

Gate 0: 26 rules checked, 0 fails. Block scores, core, moat, matrix, deal-breakers, confidence all
re-derived and confirmed as-written. Note: Block E scored 0 on data absence (shareholding pattern not
in Gate 0's inputs), correctly flagged as a data gap, not a governance failure — as-written under rule 5.

---

## TABLE 2 — EMERGING MOAT (B07) COMPLIANCE

| # | Rule | As-written | B07 | Verdict |
|---|------|-----------|-----|---------|
| 1 | All 20+R1 = 21 categories addressed or NO EVIDENCE | required | A1-4,B1-3,C1-2,D1-2,E1-2,F1-2,G1-2,H1-3,R1 all addressed | PASS |
| 2 | Evidence multipliers 📄1.0/🎙️0.7/🔍0.5 | required | applied per row | PASS |
| 3 | Raw matrix HH4/HM-MH3/…/LL1 | required | A3=HM3, B1=MM2, E2=HM3, F2=LL1, G2=MM2, R1=MH3 | PASS |
| 4 | Adjusted total | sum | 3.0+1.4+3.0+1.0+2.0+3.0 = 13.4 | PASS |
| 5 | Completionist 📄 recount | required | 11 docs / 6 categories, stated | PASS |
| 6 | Classification band | 12-24 = MODEST | 13.4 → MODEST | PASS |
| 7 | No 🎙️-only scored as 📄 | required | B1 (🎙️) correctly ×0.7, not 1.0 | PASS |

EM: 7 rules checked, 0 fails. The one obvious trap (B1 backward-integration is a 🎙️ claim) is correctly
discounted at 0.7, not credited as documented. EM 13.4 flows correctly into B11 Pillar 3.

---

## TABLE 3 — VALUATION (B11) COMPLIANCE (deepest audit)

| # | Rule | As-written | B11 | Verdict |
|---|------|-----------|-----|---------|
| V1 | Pillar 1 continuous formula | 0.5×ROCE+7.5 | 0.5×7.2+7.5 = 11.1x | PASS |
| V2 | Floor 9x / cap 24x | apply | 11.1 within, not binding | PASS |
| V3 | FTTCP ROCE verdict = sole Pillar 1 authority; route stated | required | verdict DECLINING; "recovery credited via: NOT CREDITED" | PASS |
| V4 | DECLINING → FY[Y+1] lower-bound ROCE | table | 7.2% conservative floor, no uplift | PASS |
| V5 | Single-credit rule | Pillar1 OR Strategic, never both | not credited anywhere; stated | PASS |
| V6 | Pillar 2 band matches determination | volatile → 1.00x | 1.00x applied | PASS (prior MAJOR RESOLVED) |
| V7 | Elite bands 1.30/1.15 require FCF positive | rule out if FCF not positive | ruled out (FCF neg 2/3 yrs) | PASS |
| V8 | 0.80x needs CFO/PAT <30% OR CFO negative | rule out if neither | ruled out (CFO/PAT high, CFO +ve every yr; FCF-neg ≠ CFO-neg) | PASS |
| V9 | 0.65x needs rating-agency structural WC | rule out if not confirmed | CARE "Adequate" → ruled out | PASS |
| V10 | Growth offset only on 0.80x growth-induced | +0 otherwise | offset +0 (band 1.00x; revenue declining) | PASS |
| V11 | Pillar 3 EM<25 → +0x | table | EM 13.4 → +0x | PASS |
| V12 | Pillar 3 matches injected EM/catalyst/evidence | required | EM 13.4, ANVISA/EDQM unconfirmed, mostly 📄 | PASS |
| V13 | Strategic +0x, single-credit respected | required | +0x, nothing double-counted | PASS |
| V14 | UA all_met test | qualifiers all three | Gate0≥60 OR EM≥25 FALSE → all_met FALSE | PASS |
| V15 | UA Amendment 3 order | min(F×1.25 if qual, cap) | not qual → F2=F=11.1; H=min(11.1,38) | PASS |
| V16 | Sector cap absolute, no uplift | Pharma/CDMO 38x | 38x, UA not triggered → no uplift | PASS |
| V17 | Four-pillar summary A→H arithmetic | C=A×B; F=C+D+E; H=min(F2,G) | 11.1/1.00/11.1/+0/+0/11.1/11.1/38/11.1 | PASS |
| V18 | Destination range ±7.5%, round 0.5x | Amendment 6 | 10.27-11.93 → 10.5-12.0 | PASS |
| V19 | Both tracks produced & carried through FVs + card | required | Track 2 & Track 1 in 4A, verdict card | PASS |
| V20 | **RRM computation** | 1+(13.5−r)×0.12, bounded 0.70-1.60 | **0.996 (decimal read); should be 0.70 floored (pp read)** | **FAIL — MAJOR** |
| V21 | Hurdle Ratio formula & compute | (1+g)³×(DestPE/CurPE) | 122/2.99=40.8; base 0.362, bull 0.414 | PASS |
| V22 | Grade-C gate on Bull | Bull = Base+5% max if C/D | 10%+5% = 15% used | PASS |
| V23 | Hurdle verdict | HR(Bull)<1.953 → STOP | 0.414 < 1.953 → STOP | PASS |
| V24 | 4D probability weights | Mixed(C) = 35/45/20 | 35/45/20 | PASS |
| V25 | Expected CAGR compute | Σ p×CAGR | −10.47−7.97−2.00 = −20.4% | PASS |
| V26 | SOM cross-check performed | required | Base 5% < SOM 9.0% & < 6.7% capacity → CONSISTENT | PASS |
| V27 | Input discipline / no silent fills | conservative rule named per gap | Section 0 ledger, 6 fields, anchored | PASS |
| V28 | One-improvement-one-mechanism | no double-credit | cost-rat'n credited once (margin); ROCE recovery nowhere | PASS |
| V29 | Exit PE = sole Section 1B authority | no other exit PE | P/E method uses 10.5/11.1/12.0 only | PASS |
| V30 | Method selection discipline | P/B excluded (manufacturer) | EV/EBITDA 60% + P/E 40%, P/B 0% | PASS |

Valuation: 30 rules checked, 1 fail (V20, MAJOR).

---

## FINDING DETAIL

### MAJOR — V20: RRM (Track 1) misapplied; false convergence claim
- **Rule (Master v3.3 line 392):** `RRM = 1 + (13.5% − r) × 0.12, bounded ×0.70 to ×1.60`, base r
  small/micro 14%, r bound [9%,18%]. B11 sets r = 17% (14 +2 governance +1 durability) — the r build
  is a defensible judgment and is not itself the error.
- **What B11 did:** read `(13.5% − r)` in decimal units → `1 + (0.135 − 0.17)×0.12 = 0.996`, giving
  Track 1 destination PE 11.1 × 0.996 = 11.05x, divergence vs Track 2 "0.45% (<15%)", tracks "numerically
  identical to within 1%."
- **Why that is wrong:** under the decimal reading the stated bounds ×0.70-×1.60 and the framework's
  entire ">15% material divergence → name the governing track" machinery can NEVER bind (max deviation
  across the whole r∈[9,18] range is ±0.5%). Those rules are only coherent if `(13.5 − r)` is in
  **percentage points**. Correct: `1 + (13.5 − 17)×0.12 = 1 − 0.42 = 0.58 → floored to 0.70`.
- **Recomputed:** Track 1 RRM = **0.70**; Track 1 destination PE = 11.1 × 0.70 = **~7.8x** (not 11.05x).
  Divergence vs Track 2 (11.1x) = **~42% (>15%)**, so the conservative Track 1 genuinely governs entry,
  and the entry zone should be lower than the stated Rs 28-35 (base FV recomputes down, entry ~Rs 20-25).
- **Severity rationale — MAJOR, not CRITICAL:** (a) the primary/headline additive destination PE (11.1x)
  and the Hurdle-Ratio input are unaffected and correct; (b) the error is confined to the RRM cross-check
  track; (c) the direction is conservative — the correct value makes the stock *less* attractive, so the
  decision (AVOID) and the Hurdle verdict (STOP even on bull earnings) do not flip and are in fact
  reinforced; (d) the formula text is genuinely ambiguous (a literal decimal read supports B11).
  Keerti should adjudicate the intended units; if pp is confirmed, restate Track 1 to ~7.8x and the
  divergence to ~42% (Track 1 governing). Nothing here reverses the STOP at Rs 122.

### MINOR — cumulative CFO/PAT cross-reference (observational; Verifier A domain)
- B11/B10 Pillar 2 reasoning cites cumulative CFO/PAT **2.80x**, while B01 computes full-period (FY17-26)
  cumulative CFO/PAT = **2.18x** (121.55/55.88). Likely a 3-5yr vs 10yr window difference (Master Pillar 2
  asks for the 3-5yr cumulative). Either figure is well above the 30% / 1.0x thresholds, so the band
  determination (1.00x volatile; 0.80x ruled out) is unchanged. Flagged for Verifier A; no rule-application
  impact.

---

## CONFIRMATIONS REQUESTED BY THE RE-RUN TASK

- Prior MAJOR (Pillar 2 0.80x → 1.00x): **RESOLVED.** 1.00x is the correct as-written volatile band;
  0.80x required CFO/PAT <30% OR CFO negative, neither of which holds (CFO positive every year; FCF-negative
  is not CFO-negative). Elite 1.30/1.15 ruled out (FCF not positive); 0.65x ruled out (CARE "Adequate").
- Continuous Pillar 1 formula, floor/cap: **applied correctly** (11.1x).
- FTTCP ROCE = sole Pillar 1 authority, route stated: **yes** (DECLINING; not credited).
- Single-credit: **honoured** (nothing double-credited).
- Pillar 2 offset rules / no offset on structural: **correct** (+0).
- Pillar 3 = injected EM 13.4 / catalyst / evidence: **matches** (+0x).
- UA not applied (all_met false) + Amendment 3 order: **correct.**
- Sector cap 38 absolute: **correct.**
- Both tracks carried through every FV and the verdict card: **yes** (RRM value wrong per V20, but both
  tracks are present and carried).
- Conservative track governs entry: **principle applied** (Track 1 named governing); the <1% divergence
  claim is wrong per V20 (true divergence ~42%), but the governing-track selection direction is unchanged.
- Hurdle Ratio + grade-C Bull gate (Base+5%=15%): **correct** → STOP.
- 4D weights 35/45/20 for grade C: **correct.**
- SOM cross-check: **performed** (Base 5% below 9.0% SOM and 6.7% capacity ceilings).
- Every unresolved input handled by a stated conservative rule, no silent fills: **yes** (Section 0 ledger).
- One-improvement-one-mechanism: **honoured.**

---

## SUMMARY

- Rules checked: 63 (Gate 0 26, EM 7, Valuation 30). Fails: 1 (MAJOR, V20 RRM).
- Recomputed primary destination PE: **unchanged, 11.1x (concur).** RRM-track destination PE recomputes
  to **~7.8x** (from 11.05x) under the percentage-point reading of the RRM formula.
- Recomputed decision: **unchanged — AVOID (Hurdle STOP), reinforced.**
- Acceptance rate: 62/63 = **98.4%.**
