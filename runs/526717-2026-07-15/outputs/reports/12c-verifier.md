# STAGE 12c — VERIFIER C (FRAMEWORK ADHERENCE)
## HCP Plastene Bulkpack Ltd (526717) | Run date: 2026-07-15 | PHASE 1 SCOPE ONLY

Model: claude-opus-4-8. Fresh context. This verifier audits **rule application**, not
company quality and not raw-number sourcing (Verifier A owns numbers).

**SCOPE LIMIT (enforced):** this run executes ONLY the Gate 0 (B01) and Emerging Moat
(B07) compliance checks. The valuation-adherence audit (B10/B11) is DEFERRED to phase 3
and is NOT run here; those artifacts do not yet exist. The `valuation` section of the
emitted B12c block is explicitly marked `pending phase 3`.

Authorities consulted: prompts/01-gate-0-pipeline.md (scoring tables, deal-breaker list,
CAGR edge rules, classification matrix), prompts/07-emerging-moat-pipeline.md (21-category
scan, likelihood×impact matrix, evidence multipliers, completionist guard, classification
bands), frameworks/Master_Project_Prompt_v3.3.md, Section_1B_v3.3, Section_1B_v3_5_1,
FTTCP_v1.2, and CLAUDE.md house rules (no exit-PE leakage, Emerging-Moat≠FTTCP, single-
credit, UA rules).

---

## PART 1 — GATE 0 (B01) RULE-BY-RULE

Every block score re-derived from the report's own stated inputs against the fixed
thresholds in prompts/01.

### Block A — Return on Capital (report 10/20)
| Rule | Input (from report) | Threshold band | Re-derived | Report | Verdict |
|---|---|---|---|---|---|
| A1 median ROCE | median{8.26, 24.41, 28.62}=24.41% | 20-24.9=4 | 4 | 4 | PASS |
| A2 min ROCE | 8.26% (FY24) | 8-11.9=1 | 1 | 1 | PASS |
| A3 median ROE | median of 6 = 7.64% | <12=0 | 0 | 0 | PASS |
| A4 ROCE trend | FY26 28.62 ≥ FY24 8.26 | latest≥earliest=5 | 5 | 5 | PASS |

A4 note: FY21-23 ROCE unavailable, so "earliest available" = FY24; using the earliest
present year is the only defensible reading of the rule and is not inflationary. PASS.

### Block B — Cash Generation (report 1/20)
| Rule | Input | Band | Re-derived | Report | Verdict |
|---|---|---|---|---|---|
| B1 cumCFO/PAT | -79.95/90.00=-0.888 | <0.50=0 | 0 | 0 | PASS (correctly triggers DB#4) |
| B2 FCF-pos yrs | 1/6=16.7% | <50=0 | 0 | 0 | PASS |
| B3 cumFCF/PAT | -160.59/90.00=-1.784 | <0.20/neg=0 | 0 | 0 | PASS |
| B4 ΔWC days | FY24 109.8 → FY26 117.0 = +7.2 | +5-15=1 | 1 | 1 | PASS |

### Block C — Growth (report 8/20)
| Rule | Input | Band | Re-derived | Report | Verdict |
|---|---|---|---|---|---|
| C1 rev CAGR | (587.51/15.87)^(1/5)-1=105.9% | ≥20=5 | 5 | 5 | PASS |
| C2 PAT CAGR | (23.20/63.62)^(1/5)-1=-18.3% | neg=0 | 0 | 0 | PASS |
| C3 pos YoY yrs | 4/5=80% | 75-99=3 | 3 | 3 | PASS |
| C4 PAT−Rev CAGR | -124.2pp | <-8pp=0 | 0 | 0 | PASS |

CAGR edge rules honoured: C1/C2 use the full available window (FY21→FY26) with the base-
effect FLAGGED but NOT substituted (rule: "do not substitute alternatives"). C2 endpoints
both positive so correctly NOT declared N/M, scored 0 on negative result. The FY24→FY26
loss-to-profit swing is recorded under data_notes and not turned into a synthetic CAGR —
exactly per the edge rules. C4 handled per its own path. PASS.

### Block D — Balance Sheet (report 3/20)
| Rule | Input | Band | Re-derived | Report | Verdict |
|---|---|---|---|---|---|
| D1 ND/EBITDA | 230.22/56.10=4.10x | >3x=0 | 0 | 0 | PASS |
| D2 int cover | 48.33/20.43=2.37x | 1.5-2.9=1 | 1 | 1 | PASS |
| D3 D/E | 245.67/81.97=3.00x | >1.5=0 | 0 | 0 | PASS |
| D4 current ratio | 281.67/209.59=1.34x | 1.2-1.49=2 | 2 | 2 | PASS |

DB#6 leg check: ND/EBITDA 4.10x (>3x) AND EBIT/Interest 2.37x (<3x) both true → AVOID.
Correctly identified as the binding override. PASS.

### Block E — Shareholder Alignment (report 5/20)
| Rule | Input | Band | Re-derived | Report | Verdict |
|---|---|---|---|---|---|
| E1 promoter hold | 75.00% | ≥60=5 | 5 | 5 | PASS |
| E2 3yr change | Jun23 89.00 → Mar26 75.00 = -14pp | dec>3%=0 | 0 | 0 | PASS |
| E3 pledge | NOT FOUND | missing→0 | 0 | 0 | PASS |
| E4 CL/NW | NOT FOUND | missing→0 | 0 | 0 | PASS |

E3/E4 grounding rule applied correctly: missing data scores 0 (prompt rule 5). Critically,
the report does NOT let the E3=0 score confirm deal-breaker #5 (pledge>15%); it explicitly
records pledge as *unverified*, not *>15%*. This is the correct, non-inflationary reading —
scoring 0 for absence without fabricating a deal-breaker trigger. PASS.

### Block F — Quantitative Moat (report 21/60)
| Test | Re-derived | Report | Verdict |
|---|---|---|---|
| M1 pricing power | margin +4.47pp ≥2 AND rev CAGR ≥10 → 5 | 5 | PASS |
| M2 cost adv | HCP 9.55 vs peer med 9.51 = +0.04pp → ±2pp=1 | 1 | PASS |
| M3 cap efficiency | FAT 8.36x>3 AND ROCE 28.62>20 → 5 | 5 | PASS |
| M4 stickiness | 1 decline yr, recovered → 3 | 3 | PASS |
| M5 scale/dominance | top-3 mcap AND margin top-2 → 3 | 3 | PASS* |
| M6-M9 | R&D/reg/distr/brand all fail → 0 | 0,0,0,0 | PASS |
| M10 switching | growth all-but-1 AND recv stable → 3 | 3 | PASS |
| M11 network effects | see finding | 1 | **FAIL (MAJOR)** |
| M12 neg WC | WC days >45 all yrs → 0 | 0 | PASS |

Block F total re-adds to 21 as scored. Moats confirmed (≥3): M1,M3,M4,M5,M10 = 5 →
band 4-5 = STRONG, consistent with the scored values.

\*M5 caveat (MINOR): the rule's "top 3 / top 5 mcap" thresholds are being applied against a
4-company peer universe, where "top 3" is trivially most of the set. The mechanical rule is
technically satisfied (HCP 3rd/4 by mcap, 2nd/4 by margin) and the report flags it as
"indicative only, not a defensible read," so this is a data-adequacy caveat, not a scoring
error. Logged MINOR.

### Classification, confidence, deal-breakers
- Matrix: Core 27 < 40 → AVOID. Correct; the Core<40 row does not condition on moat tier. PASS.
- Data confidence: 6 years → "5-6 lower confidence, flag may not have seen full cycle";
  history_downgrade=false. Correct (downgrade tier is 3-4 years, not 6). PASS.
- Deal-breakers TRIGGERED: #2 (Block B 1<8→max GOOD), #4 (cumCFO/PAT -0.888<0.50→max
  AVERAGE), #6 (ND/EBITDA>3 AND IC<3→AVOID, binding), #8 (PAT neg FY24 in last 3→max
  AVERAGE). All four correctly derived; #6 correctly named binding. PASS.
- Deal-breakers NOT triggered: #1 (Block A 10≥8), #3 (median ROCE 24.41 not <10), #5
  (pledge unverified, not confirmed >15 — correct restraint), #7 (1 of 5 declined, not
  majority), #9 (6 years ≥3). All five correctly excluded. PASS.

**Gate 0 verdict: fully compliant except M11.** Core score, all deal-breaker logic, the
classification matrix, and the confidence tier are applied exactly as written. Final
classification AVOID is CONCUR.

---

## PART 2 — EMERGING MOAT (B07) RULE-BY-RULE

### Scorecard re-derivation (Section 5 matrix + multipliers)
Matrix: HH=4, HM/MH=3, HL/MM/LH=2, ML/LM=1, LL=1, none=0. Multipliers: 📄1.0 / 🎙️0.7 / 🔍0.5.

| Cat | L×I | Matrix raw | Mult | Adjusted (re-derived) | Report | Verdict |
|---|---|---|---|---|---|---|
| A1 | M×M | 2 | 🔍0.5 | 1.0 | 1.0 | PASS |
| B1 | M×L | 1 | 📄1.0 | 1.0 | 1.0 | PASS |
| B2 | M×L | 1 | 🔍0.5 | 0.5 | 0.5 | PASS |
| C2 | H×H | 4 | 📄1.0 | 4.0 | 4.0 | PASS |
| E2 | M×H | 3 | 🔍0.5 | 1.5 | 1.5 | PASS (see finding) |
| F2 | H×M | 3 | 📄1.0 | 3.0 | 3.0 | PASS |
| R1 | M×L | 1 | 📄1.0 | 1.0 | 1.0 | PASS |
| **Total** | | | | **12.0** | 12.0 | PASS |

All matrix lookups and multiplier applications are correct. Where evidence was mixed
(A1 📄+🔍, E2 📄+🔍) the report applied the WEAKER multiplier (0.5) — the conservative and
correct choice. Total ties to 12.0.

### Band, completeness, guard, taxonomy
- Classification band: 12.0 → 12-24 = MODEST. Correct (12.0 is the floor of the band; the
  <12 NONE cutoff is not reached). PASS — but see the C2/E2 boundary finding below.
- All 21 categories addressed: A1-A4, B1-B3, C1-C2, D1-D2, E1-E2, F1-F2, G1-G2, H1-H3 (20)
  + R1 (Section 4) = 21, each with evidence or explicit NO EVIDENCE FOUND. PASS.
- Completionist recount PERFORMED and stated ("📄 recount performed: 12 documented items
  across 4 categories B1, C2, F2, R1"). Rule satisfied. PASS.
- Evidence-tier discipline: no 🎙️-only category is scored as if 📄. D2 (digital) and H3
  (ESG) are vague 🎙️ claims → correctly NOT scored (logged in optionality register). H2
  (Saudi MOU) is 📄-signing/🔍-substance → correctly scored 0 and registered, not credited,
  a non-binding MOU. The two claim→documented upgrades (Chairman capex language, job-work-
  to-export language) were promoted ONLY after an independent source confirmed the outcome,
  which is legitimate; the recount explicitly verified this. PASS.
- F2 in NO-CONCALL mode: the injected promise-delivery cross-reference is degraded to the
  AR/rating capex-completion record plus B05's degraded table. Degradation is stated where
  it binds and the single-data-point limitation is flagged. Acceptable handling. PASS.
- Combined 6D: EXPANSION threshold correctly stated as ≥40; 12.0 far short, so no HIGH
  POTENTIAL / TURNAROUND setup. Correct. PASS.

### House-rule checks (CLAUDE.md)
- **No exit-PE leakage:** neither B01 nor B07 references any exit/destination PE. Section 1B
  authority untouched at this stage. PASS.
- **Emerging Moat ≠ FTTCP:** B07 opens and closes stating it is the Emerging Moat scan, not
  FTTCP. No conflation. PASS.
- **UA rules not misapplied:** the UA multiplier (Amendment 3) is a valuation construct; it
  does not appear — and correctly does not appear — in either phase-1 artifact. The B01
  "sector cap" reference is a peer-selection correction (pharma→plastics), not a UA
  application. No misapplication. PASS.
- **Single-credit / one-improvement-one-mechanism:** see the C2/E2 finding.

---

## FINDINGS

**[MAJOR] 01.md, Block F, M11 (Network Effects).** The report invoked the "<6 years →
score conservatively" fallback and assigned **1**, but 6 years of data ARE available, so the
mechanical two-window test applies as written. Mechanically: latest-3yr rev CAGR
(FY24→FY26 ≈41.2%) < prior-3yr (FY21→FY23 ≈370%), so the top band (=5) fails; the second
band "rev CAGR ≥20% AND selling% stable/declining = 3" is satisfied (latest CAGR 41.2% ≥20%,
selling-exp% flat-to-declining FY21 3.59→FY25 2.58) → **mechanical score = 3, not 1**.
Separately, the assigned score of 1 does not even match its own band definition: band-1
requires selling% *rising*, but selling% is *declining* here. Impact: Block F would be
21→23, moats_confirmed 5→6, moat_class STRONG→**FORTRESS**. **Does NOT change the Gate 0
classification** (AVOID via Core<40 and binding DB#6, neither of which conditions on moat
tier), and the error direction is conservative (understated). Classified MAJOR because it
misapplies the scoring path and alters reported outputs (moat_score, moat_class), but the
decision survives.

**[MINOR] 07.md, Section 5, E2 vs C2 (overlap / band sensitivity).** C2 (customer
concentration improving, 4.0) and E2 (China+1 beneficiary, 1.5) both rest on the identical
direct-export-growth fact (53.70% of FY25 revenue; +145.1% standalone FY25→FY26). The
20-category taxonomy does permit a single development to inform adjacent categories, and the
report already discounted E2 to the conservative 🔍0.5 multiplier and flagged the China+1
attribution as inferred — so this is not a clean single-credit violation. It is flagged
because em_score sits **exactly on the 12.0 MODEST/NONE boundary**: if E2's 1.5 were treated
as an overlap of C2 and removed, em_score → 10.5 → **NONE** rather than MODEST. Decision
unchanged either way (forward score is far below the EXPANSION ≥40 bar, and Gate 0 floors
the combined read at AVOID). Logged MINOR with the band sensitivity surfaced.

**[MINOR] 01.md, Block F, M5 (Scale & Dominance).** The rule's "top 3 / top 5 mcap"
thresholds are applied against a 4-company peer universe, where the ranking test is trivially
easy to clear. Mechanical rule is satisfied and the report flags the read as "indicative
only." Data-adequacy caveat, not a scoring error.

---

## FRAMEWORK ADHERENCE (PHASE-1 PORTION: GATE 0 + EMERGING MOAT)

- Gate 0 rules checked: 43 (20 block line-items + 12 moat tests + matrix + confidence tier +
  moat-class band + 9 deal-breaker evaluations). Fails: 1 (M11, MAJOR). M5 logged as MINOR
  caveat, not counted as a hard scoring fail.
- Emerging Moat rules checked: 25 (21 category scores + 7 matrix lookups + 7 multiplier
  applications + completionist recount + classification band + all-categories-addressed +
  combined-6D threshold + 4 house-rule checks; overlapping items counted once). Fails: 0
  hard; 1 MINOR observation (C2/E2 boundary).
- **framework_adherence (phase-1 portion): ~96%** (65 of 68 checked rules clean; 1 MAJOR
  + 2 MINOR).
- Recomputed classification: **CONCUR — AVOID** (Gate 0 Core 27<40 and binding DB#6; combined
  read AVOID). No decision flips.

Valuation adherence (B10/B11, Section 1B pillars, FTTCP ROCE authority, UA Amendment-3 order,
dual-track, Hurdle Ratio, 4D weights, SOM cross-check): **DEFERRED — pending phase 3.**

---

```yaml
stage: B12c
company: "526717"
run_date: "2026-07-15"
model: claude-opus-4-8
status: complete
scope: "PHASE 1 ONLY (Gate 0 + Emerging Moat); valuation audit deferred to phase 3"
gate0:
  rules_checked: 43
  fails:
    - {severity: MAJOR, rule: "M11 Network Effects", location: "01.md Block F, M11", description: "Used the <6-year conservative fallback despite 6 years available; mechanical two-window test yields 3 (latest-3yr CAGR 41.2% >=20% AND selling% declining), assigned 1 does not match band-1 (which requires selling% rising). Would move moat_score 21->23, moat_class STRONG->FORTRESS. Conservative direction; does NOT change classification (AVOID via Core<40 and binding DB#6)."}
emoat:
  rules_checked: 25
  fails: []
  minor_observations:
    - {severity: MINOR, location: "07.md Section 5, E2 vs C2", description: "C2 (4.0) and E2 (1.5) both rest on the same direct-export-growth fact; em_score 12.0 sits exactly on the MODEST/NONE (12) boundary, so any overlap discount on E2 drops the band to NONE. Decision unchanged (forward far below EXPANSION>=40; Gate 0 floors at AVOID). Taxonomy permits adjacent-category overlap and E2 already conservatively discounted."}
valuation:
  status: "pending phase 3"
  rules_checked: 0
  fails: []
recomputed_destination_pe: ""   # deferred to phase 3
recomputed_decision: ""         # concur: Gate 0 classification AVOID stands
findings:
  - {severity: MAJOR, location: "01.md Block F, M11", description: "Conservative-fallback misapplication with 6 years present; mechanical score 3 not 1; assigned 1 also mismatches band-1 definition. moat_score 21->23, moat_class STRONG->FORTRESS; classification (AVOID) unchanged."}
  - {severity: MINOR, location: "07.md Section 5, E2 vs C2", description: "C2/E2 rest on identical export-growth fact; em_score on the 12.0 MODEST/NONE boundary; decision unchanged."}
  - {severity: MINOR, location: "01.md Block F, M5", description: "top-3/top-5 mcap thresholds applied against a 4-company peer universe; mechanically satisfied and flagged indicative-only by the maker. Data-adequacy caveat."}
critical_count: 0
major_count: 1
minor_count: 2
framework_adherence: 96         # phase-1 portion only (Gate 0 + Emerging Moat)
acceptance_rate: 96             # rules passed / rules checked, phase-1 portion, %
```
