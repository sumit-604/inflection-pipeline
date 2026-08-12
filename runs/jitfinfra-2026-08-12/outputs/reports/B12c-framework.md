# B12c — VERIFIER C: FRAMEWORK ADHERENCE (PHASE 1 SCOPE)
Company: JITF Infra Logistics Ltd (JITFINFRA) | Run date: 2026-08-12
Model: claude-opus-4-8 | Emits: B12c

SCOPE NOTE: Phase 1 runs Gate 0 (B01) and Emerging Moat (B07) adherence only.
The valuation-adherence audit (B11/B10) is DEFERRED to phase 3; B10 and B11 do
not exist yet. The valuation section below is intentionally left pending and
recomputed_destination_pe / recomputed_decision are blank.

I audit rule application, not company quality and not raw numbers (Verifier A
owns whether a figure actually appears in the source). Every score below is
re-derived from the INPUTS AS STATED in the reports, using the thresholds in
prompts/01-gate-0-pipeline.md and prompts/07-emerging-moat-pipeline.md.

═══════════════════════════════════════════════════════════════════
## PART 1 — GATE 0 (B01) COMPLIANCE
═══════════════════════════════════════════════════════════════════

### Block A — Return on Capital (rulebook lines 56-60)
| Rule | Stated input | Band applied | Re-derived | Verdict |
|------|--------------|--------------|-----------|---------|
| A1 Median ROCE | 5.34% | <10 = 0 | 0 | PASS |
| A2 Min single-yr ROCE | -5.08% (FY18) | <8 = 0 | 0 | PASS |
| A3 Median ROE | N/M (neg net worth all 10y) | <12 = 0 | 0 | PASS (0-band regardless) |
| A4 ROCE trend latest vs earliest | FY26 13.31% ≥ FY17 -2.31% | latest≥earliest = 5 | 5 | PASS |
| Block A total | 5 | | 5 | PASS |

FORMULA DEVIATION (MINOR): rulebook defines ROCE = EBIT ÷ (Total Assets −
Current Liabilities) and directs "if the data source provides its own ROCE
(screener.in does), use the source's figure." The report instead computed ROCE
on a proxy denominator (Equity + Reserves + Borrowings) for FY17-FY24 because
the screener export carried no current/non-current liability split. The
deviation is stated openly and validated: the FY26 proxy (13.31%) was
cross-checked against the literal formula on audited data (Total Assets ₹5,032.96
Cr − Current Liab ₹1,703.27 Cr → 13.72%), a 0.4pp gap. Immaterial to every A-band
and to the classification. Logged as MINOR framework deviation, not a band error.

### Block B — Cash Generation Quality (rulebook lines 62-69)
| Rule | Stated input | Band applied | Re-derived | Verdict |
|------|--------------|--------------|-----------|---------|
| B1 Cumul CFO ÷ Cumul PAT | 727.03 ÷ -896.71 = -0.81 | <0.50 = 0 | 0 | PASS |
| B2 FCF-positive years proportion | 0 of 2 measurable (FY25/26 both neg) = 0% | <50 = 0 | 0 | PASS |
| B3 Cumul FCF ÷ Cumul PAT (FY25-26) | -141.25 ÷ 4.26 = -33.16 | <0.20/neg = 0 | 0 | PASS |
| B4 Change in WC Days | N/A (Trade Payables undisclosed FY17-24) | data gap → 0 | 0 | PASS |
| Block B total | 0 | | 0 | PASS |

B2/B3/B4 partial-window handling: rulebook rule 5 mandates missing data scored 0,
never estimated. Report scored on the 2 disclosed years (both negative) and the
data gap conservatively; result is 0 either way. Compliant, limitation stated.

### Block C — Growth (rulebook lines 71-75, CAGR edge rules 44-52)
| Rule | Stated input | Band applied | Re-derived | Verdict |
|------|--------------|--------------|-----------|---------|
| C1 Revenue CAGR (9y) | 20.03% | ≥20 = 5 | 5 | PASS |
| C2 PAT CAGR | both endpoints negative → N/M | neg/N/M = 0 | 0 | PASS (edge rule honoured) |
| C3 Positive YoY rev years | 7 of 9 = 77.8% | 75-99 = 3 | 3 | PASS |
| C4 PAT CAGR − Rev CAGR | PAT CAGR N/M | N/M → C4 = 0 (rule ln 52) | 0 | PASS |
| Block C total | 8 | | 8 | PASS |

CAGR edge rules: negative-endpoint N/M correctly applied to C2; loss-to-profit /
profit-to-loss swings noted in data_notes without a synthetic CAGR; C4=0 on N/M
PAT CAGR per line 52. All three edge rules honoured. PASS.

### Block D — Balance Sheet Strength (rulebook lines 77-87)
| Rule | Stated input | Band applied | Re-derived | Verdict |
|------|--------------|--------------|-----------|---------|
| D1 Net Debt ÷ EBITDA | 6.71x | >3x = 0 | 0 | PASS |
| D2 Interest Coverage | 1.14x | <1.5x = 0 | 0 | PASS |
| D3 Debt ÷ Equity | negative equity (-₹513.28 Cr) | worst band >1.5 = 0 | 0 | PASS |
| D4 Current Ratio | 1.47x | 1.2-1.49 = 2 | 2 | PASS |
| Block D total | 2 | | 2 | PASS |

Not Bank/NBFC/Insurance — standard D1/D2 tables correctly used (not CAR/PCR). PASS.

### Block E — Shareholder Alignment (rulebook lines 89-96)
| Rule | Stated input | Band applied | Re-derived | Verdict |
|------|--------------|--------------|-----------|---------|
| E1 Promoter holding | N/A (no shareholding filing) | data gap → 0 | 0 | PASS |
| E2 Holding change 3y | N/A | data gap → 0 | 0 | PASS |
| E3 Pledge | N/A | data gap → 0 | 0 | PASS |
| E4 Contingent liab ÷ NW | N/A | data gap → 0 | 0 | PASS |
| Block E total | 0 | | 0 | PASS |

Unanchored COMPANY MEMORY promoter figure (63.03%) correctly NOT scored (weighed,
not anchored). Grounded-claims rule (line 22) honoured. PASS.

### Block F — 12 Moat Tests (rulebook lines 98-137)
| Test | Stated input | Band applied | Re-derived | Verdict |
|------|--------------|--------------|-----------|---------|
| M1 Pricing Power | OPM 8.15→19.14% (+11pp≥2) AND rev CAGR 20.03%≥10 | =5 | 5 | PASS |
| M2 Cost Advantage | JITF 19.9% vs peer median 19.3% (+0.6pp) | ±2pp = 1 | 1 | PASS |
| M3 Capital Efficiency | FAT 1.53x (>1), ROCE 13.31% (>12) | =1 | 1 | PASS |
| M4 Customer Stickiness | 2 decline yrs, CAGR positive | =1 | 1 | PASS |
| M5 Scale & Dominance | smallest mcap of 5 named comps | 0 (see note) | 0/1 | PASS (borderline) |
| M6 Technology/R&D | no R&D disclosure | =0 | 0 | PASS |
| M7 Regulatory/License | regulated, player-count not established | PEER DATA NEEDED → 0 | 0 | PASS |
| M8 Distribution | no data | =0 | 0 | PASS |
| M9 Brand | peer RM data degraded | PEER DATA NEEDED → 0 | 0 | PASS |
| M10 Switching Costs | overall growth, 2+ decline yrs | =1 | 1 | PASS |
| M11 Network Effects | latest 3y CAGR 20.90%≥20 AND selling% declining (3.24→2.77) | =3 | 3 | PASS |
| M12 Negative WC/Float | 2 measurable yrs both >45 days (56, 65) | >45 = 0 | 0 | PASS |
| Block F total | 12 | | 12 | PASS |

M5 borderline (MINOR observation, not a fail): the literal band "top 5 mcap = 1"
would arguably score 1, since JITF is one of five named comparables. The report
scored 0, reasoning that "top 5 of a 5-name sample" is trivially true and the
segment universe is not established as complete. The conservative direction and
1-point magnitude cannot change M5's <3 "not present" status or any downstream
classification; defensible either way. Recorded, not a fail.

M7/M9 correctly invoke the "score 0, mark PEER DATA NEEDED" rule (line 100-101)
rather than guessing peer figures. M11 two-window test correctly applied on a
10-year history (≥6y available): top band failed (latest 20.90% not > prior
23.49%), fell to the ≥20% + selling%-declining band = 3. PASS.

### Moat classification, data confidence, matrix, deal-breakers
| Check | Stated | Rule | Verdict |
|-------|--------|------|---------|
| Moats present (≥3) | M1(5), M11(3) → 2 | 2-3 = MODERATE (ln 138) | PASS |
| Core score | 5+0+8+2+0 = 15 | sum of A-E | PASS (arithmetic) |
| Grand total | 15+12 = 27 | core + moat | PASS |
| Data confidence | 10y → "10+ yrs full" | no downgrade (ln 143) | PASS |
| history_downgrade | false | correct | PASS |
| Classification matrix | Core 15 (<40) → AVOID | ln 150 | PASS |
| DB #1 Block A(5)<8 → max GOOD | triggered | ln 156 | PASS |
| DB #2 Block B(0)<8 → max GOOD | triggered | ln 156 | PASS |
| DB #3 median ROCE 5.34%<10 → max AVG | triggered | ln 156 | PASS |
| DB #4 CFO/PAT -0.81<0.50 → max AVG | triggered | ln 157 | PASS |
| DB #5 pledge >15% | not triggered (no evidence) | correct | PASS |
| DB #6 ND/EBITDA 6.71x>3 AND IC 1.14x<3 → AVOID | triggered | ln 158 | PASS |
| DB #7 rev decline majority | 2 of 9 = 22%, not triggered | ln 158-159 | PASS |
| DB #8 PAT neg in last 3y (FY26 -48.13) → max AVG | triggered | ln 159 | PASS |
| DB #9 history <3y | not triggered (10y) | ln 160 | PASS |

Classification AVOID is independently forced by two paths (Core <40 AND DB#6).
Both correctly derived. Deal-breaker application states the driving years as the
rulebook requires (line 155). Cash-conversion INDETERMINATE is not silently
resolved — it is a mechanical negative-ratio result, correctly flagged.

GATE 0 RESULT: 47 rules checked, 46 pass. One MINOR framework deviation (ROCE
proxy denominator vs the literal formula / source-ROCE preference), immaterial to
every band and to the AVOID classification. No CRITICAL, no MAJOR. Classification
AVOID confirmed by re-derivation.

═══════════════════════════════════════════════════════════════════
## PART 2 — EMERGING MOAT (B07) COMPLIANCE
═══════════════════════════════════════════════════════════════════

### Coverage: all 21 categories addressed (rulebook lines 54-125)
A1 NO EVIDENCE · A2 NO EVIDENCE · A3 Weak 🔍 · A4 NO EVIDENCE · B1 Weak 🎙️ ·
B2 NO EVIDENCE · B3 NO EVIDENCE · C1 Moderate 📄 · C2 Moderate mixed · D1 NO
EVIDENCE · D2 NO EVIDENCE · E1 Moderate 🎙️ · E2 NO EVIDENCE · F1 Moderate 📄 ·
F2 Moderate 📄 · G1 Weak 📄 · G2 NO EVIDENCE (reverses) · H1 NO EVIDENCE · H2 NO
EVIDENCE · H3 NO EVIDENCE · R1 Strong 📄. All 21 present, none force-fit,
NO-EVIDENCE stated explicitly where absent. PASS.

### Scorecard multiplier / evidence-tier application (rulebook lines 126-132)
Matrix: HH=4, HM/MH=3, HL/MM/LH=2, ML/LM=1, LL=1, none=0. Tier: 📄 1.0, 🎙️ 0.7, 🔍 0.5.
| Cat | L×I | Raw | Tier | Mult | Re-derived | Reported | Verdict |
|-----|-----|-----|------|------|-----------|----------|---------|
| A3 | LM | 1 | 🔍 | 0.5 | 0.5 | 0.5 | PASS |
| B1 | LM | 1 | 🎙️ | 0.7 | 0.7 | 0.7 | PASS |
| C1 | HM | 3 | 📄 | 1.0 | 3.0 | 3.0 | PASS |
| C2 | MM | 2 | 🎙️ | 0.7 | 1.4 | 1.4 | PASS |
| E1 | HM | 3 | 🎙️ | 0.7 | 2.1 | 2.1 | PASS |
| F1 | HM | 3 | 📄 | 1.0 | 3.0 | 3.0 | PASS |
| F2 | MM | 2 | 📄 | 1.0 | 2.0 | 2.0 | PASS |
| G1 | LL | 1 | 📄 | 1.0 | 1.0 | 1.0 | PASS |
| R1 | HH | 4 | 📄 | 1.0 | 4.0 | 4.0 | PASS |
| Adjusted total | | | | | 17.7 | 17.7 | PASS |

Re-summed: 0.5+0.7+3.0+1.4+2.1+3.0+2.0+1.0+4.0 = 17.7. Every raw score maps
correctly to the L×I matrix and every multiplier matches the stated tier.

### 🎙️-as-📄 finding check (the specific finding Verifier C must hunt)
No management-claim-only category is scored at the documented multiplier:
- E1 (~50% self-reported market share): tiered 🎙️ 0.7x, NOT 📄. Correct — this is
  the exact trap the rulebook warns about, and it was avoided.
- B1 (Jindal Saw pipe access, related-party claim): tiered 🎙️ 0.7x. Correct.
- C2 (forward concentration improvement): tiered 🎙️ 0.7x despite one 📄 SIPCOT
  data point, because the improving-concentration metric itself (top-5/10 share)
  is NOT FOUND; the conservative tier is the defensible choice. Correct.
- C1 (📄 1.0x): rests on documented O&M/EPC order-book figures (MD&A p.84); the
  "annuity" framing is 🎙️ but the scored evidence is the 📄 order book. Correct.
- F1 (📄 1.0x): ESOP Note 36 is genuinely documented. Correct.
- R1 (📄 1.0x): project grants Note 17 genuinely documented. Correct.
No 🎙️-inflated-to-📄 finding. PASS.

### Completionist recount (rulebook lines 33-36, 115-116)
Recount performed and stated: "📄 recount performed: 18 documented items across 6
categories," with an explicit statement that 🎙️-only items (B1, most of C2, E1's
headline claim, the FY27 target inside F2) were kept OUT of the documented tally.
6 active categories sits at the top of the 3-6 base rate, below the 12+ inflation
alarm. Guard applied as written. PASS.

### Classification & combined assessment (rulebook lines 131-132, 149-161)
| Check | Stated | Rule | Verdict |
|-------|--------|------|---------|
| em_classification | 17.7 → MODEST | 12-24 = MODEST (ln 132) | PASS |
| Combined 6D | AVOID | AVOID backward + MODEST (< EXPANSION) forward → no transition lift | PASS |

Combined logic correctly refuses to lift an AVOID backward score: MODEST is one
tier below the STRENGTHENING/EXPANSION forward intensity the transition matrix
requires. Uses the injected Gate 0 block (core 15, MODERATE, AVOID) faithfully.

### Minor observations (not fails)
- G1 scored LL=1 despite the report noting the "net cash growing" definition is
  NOT met; the non-zero score rests on documented rating upgrade + cost-of-debt
  decline, which are inside G1's what-to-look-for list, so 1.0 is defensible. Had
  it scored 0, em_score would fall to 16.7 — still MODEST, no classification
  change. MINOR, recorded not failed.
- F2 counts "3 completions" (Board's Report) while the injected B05 record reads
  delivered 2 / partial 1; the report reconciles this (Jodhpur is the partial).
  Consistency nuance, not a scoring error; numbers ownership sits with Verifier A.

EMERGING MOAT RESULT: 34 rules checked, 34 pass. No 🎙️-as-📄 inflation, recount
performed, multipliers and classification all correct. No CRITICAL, no MAJOR.

═══════════════════════════════════════════════════════════════════
## PART 3 — VALUATION (B11 / B10) — DEFERRED TO PHASE 3
═══════════════════════════════════════════════════════════════════
Not run in phase 1. B10 and B11 do not yet exist. recomputed_destination_pe and
recomputed_decision left blank pending phase 3.

═══════════════════════════════════════════════════════════════════
## SUMMARY
═══════════════════════════════════════════════════════════════════
Gate 0: 47 checked / 46 pass (1 MINOR: ROCE proxy denominator, immaterial).
Emerging Moat: 34 checked / 34 pass.
Combined phase-1: 81 checked / 80 pass → acceptance 99%.
No CRITICAL, no MAJOR. Both frameworks were applied as written; the AVOID
classification and the MODEST emerging-moat classification both survive
independent re-derivation. Valuation adherence deferred to phase 3.

```yaml
stage: B12c
company: "JITFINFRA"
run_date: "2026-08-12"
model: claude-opus-4-8
status: complete
gate0:
  rules_checked: 47
  fails:
    - {severity: "MINOR", rule: "ROCE formula (ln 34-35)", detail: "ROCE computed on proxy denominator (Equity+Reserves+Borrowings) for FY17-FY24 instead of the literal EBIT/(Total Assets-Current Liabilities) or screener's own ROCE; stated openly and cross-checked to within 0.4pp on FY26 audited data. Immaterial to every band and to the AVOID classification."}
emoat:
  rules_checked: 34
  fails: []
valuation: {rules_checked: 0, fails: []}   # DEFERRED to phase 3 (B10/B11 not yet produced)
recomputed_destination_pe: ""
recomputed_decision: ""
findings:
  - {severity: "MINOR", location: "B01 Block A / ROCE formula", note: "Proxy capital-employed denominator used in place of the rulebook formula / source ROCE; validated within 0.4pp on FY26, no band or classification impact."}
  - {severity: "MINOR", location: "B01 M5 Scale & Dominance", note: "Scored 0; literal 'top 5 mcap = 1' band would arguably give 1 (JITF is 5th of 5 named comps). Conservative direction, cannot change M5 <3 'not present' status or any classification."}
  - {severity: "MINOR", location: "B07 G1 War chest", note: "LL=1 retained though the 'net cash growing' definition is unmet; rests on documented rating upgrade + cost-of-debt fall (within category's look-for list). Zeroing it yields em_score 16.7, still MODEST."}
critical_count: 0
major_count: 0
minor_count: 3
acceptance_rate: 99            # 80 of 81 phase-1 rules passed clean
```
