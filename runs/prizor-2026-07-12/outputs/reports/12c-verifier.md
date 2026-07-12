# VERIFIER C — FRAMEWORK ADHERENCE AUDIT (B12c)

Company: Prizor Viztech Ltd (PRIZOR) | Run date: 2026-07-12 | Model: claude-opus-4-8
Scope: PHASE 1 — Gate 0 (B01) and Emerging Moat (B07) adherence ONLY.
Valuation adherence (B11/B10) DEFERRED TO PHASE 3 (artifacts do not yet exist).

Authority documents consulted:
- prompts/01-gate-0-pipeline.md (block thresholds, moat tests, classification matrix, deal-breaker overrides, data-confidence rule, CAGR edge rules)
- prompts/07-emerging-moat-pipeline.md (evidence taxonomy, 21-category scan, likelihood×impact matrix, evidence multipliers, completionist guard)
- frameworks/Master_Project_Prompt_v3.3.md and frameworks/Section_1B_v3.3_Amendments.md (govern the deferred valuation stage; the Pillar-3a capex-embedded-growth threshold in Amendment 4.1 was used to test the downstream materiality of the one B07 method deviation)

Method: I audit RULE APPLICATION, not company quality and not raw source numbers (Verifier A owns numbers). Every block score below is re-derived from the inputs the maker stated, using the thresholds as written.

═══════════════════════════════════════════════════════════════════
## PART 1 — GATE 0 (B01) COMPLIANCE
═══════════════════════════════════════════════════════════════════

### 1.1 Block-by-block re-derivation (thresholds from prompts/01, lines 55-96)

| Rule | Stated input (maker) | Threshold applied | Re-derived score | Maker score | Verdict |
|---|---|---|---|---|---|
| A1 Median ROCE | 50.56% (avg of 69.82/31.29) | ≥25%=5 | 5 | 5 | PASS |
| A2 Min single-yr ROCE | 31.29% | ≥15%=5 | 5 | 5 | PASS |
| A3 Median ROE | 61.90% (avg 82.79/41.02) | ≥20%=5 | 5 | 5 | PASS |
| A4 ROCE trend | 31.29 vs 69.82 = −38.5pp | decline >5pp=0 | 0 | 0 | PASS |
| B1 Cum CFO/PAT | −1.02 | <0.50=0 | 0 | 0 | PASS |
| B2 FCF+ yrs | 0% | <50%=0 | 0 | 0 | PASS |
| B3 Cum FCF/PAT | −1.66 | negative=0 | 0 | 0 | PASS |
| B4 ΔWC days | +46.3 | increased >15=0 | 0 | 0 | PASS |
| C1 Rev CAGR | 99.07% | ≥20%=5 | 5 | 5 | PASS |
| C2 PAT CAGR | 83.88% (both endpoints +) | ≥20%=5 | 5 | 5 | PASS |
| C3 +YoY rev yrs | 100% | 100%=5 | 5 | 5 | PASS |
| C4 PAT−Rev CAGR | −15.19pp | <−8pp=0 | 0 | 0 | PASS |
| D1 ND/EBITDA | 0.49x (net debt +7.39) | 0-1.0x=4 | 4 | 4 | PASS |
| D2 Int coverage | 12.02x | ≥10x=5 | 5 | 5 | PASS |
| D3 Debt/Equity | 0.176 | 0.1-0.5=4 | 4 | 4 | PASS |
| D4 Current ratio | 5.08x | ≥2.0=5 | 5 | 5 | PASS |
| E1 Promoter hold | 68.28% | ≥60%=5 | 5 | 5 | PASS |
| E2 Promoter Δ | −31.71pp | decreased >3%=0 | 0 | 0 | PASS |
| E3 Pledge | 0% | 0%=5 | 5 | 5 | PASS |
| E4 Cont.Liab/NW | 0% | <5%=5 | 5 | 5 | PASS |

Core total re-derived: A15 + B0 + C15 + D18 + E15 = **63**. Maker = 63. PASS.

### 1.2 Block F moat tests (thresholds prompts/01, lines 103-139)

| Test | Stated input | Threshold | Re-derived | Maker | Verdict |
|---|---|---|---|---|---|
| M1 Pricing | margin −1.61pp (±2pp) + rev CAGR 99% | stable±2pp & CAGR≥10%=3 | 3 | 3 | PASS |
| M2 Cost adv | no peer data | PEER DATA NEEDED=0 | 0 | 0 | PASS |
| M3 Cap.eff | FAT 8.58x + ROCE 31.3% | >3x & >20%=5 | 5 | 5 | PASS |
| M4 Stickiness | 0 decline yrs + rec.days −0.57 | 0 decline & ±10=5 | 5 | 5 | PASS |
| M5 Scale | no peer data | PEER DATA NEEDED=0 | 0 | 0 | PASS |
| M6 Tech/R&D | R&D NIL | <1%=0 | 0 | 0 | PASS |
| M7 Reg/License | "unregulated" per AR | unregulated=0 | 0 | 0 | PASS (minor caveat, 1.4 below) |
| M8 Distribution | no network in AR | none=0 | 0 | 0 | PASS (minor caveat, 1.4 below) |
| M9 Brand | no peer data | PEER DATA NEEDED=0 | 0 | 0 | PASS |
| M10 Switching | growth + rec.days −0.57 | grew every yr & rose≤10=5 | 5 | 5 | PASS |
| M11 Network | <6yr, CAGR≥20% + selling% rising | growth>15% & selling% rising=1 | 1 | 1 | PASS |
| M12 Neg WC | WC 168/214 both >45 | >45=0 | 0 | 0 | PASS |

Moat total re-derived: 3+0+5+5+0+0+0+0+0+5+1+0 = **19**. Maker = 19. PASS.
Moats present (≥3): M1, M3, M4, M10 = 4. Rule (line 138): 4-5 = STRONG. Maker = STRONG. PASS.

### 1.3 Classification, data-confidence, deal-breakers

- Grand total = 63 + 19 = **82**. PASS.
- Raw classification-matrix lookup (line 149): Core 60-79 + STRONG = GOOD+. Maker states this correctly before override. PASS.
- Data-confidence rule (line 144): "<3 auto AVERAGE." 2 years available → auto AVERAGE. Correctly applied. PASS.
- Deal-breaker overrides (lines 156-160), re-checked one by one:

| # | Rule | Trigger? | Cap | Maker | Verdict |
|---|---|---|---|---|---|
| 1 | Block A <8 | No (15) | — | not triggered | PASS |
| 2 | Block B <8 | Yes (0) | max GOOD | triggered | PASS |
| 3 | Median ROCE <10% | No (50.56%) | — | not triggered | PASS |
| 4 | Cum CFO/PAT <0.50 | Yes (−1.02) | max AVERAGE | triggered | PASS |
| 5 | Pledge >15% | No (0%) | — | not triggered | PASS |
| 6 | ND/EBITDA >3x AND IC <3x | No (0.49x/12.0x) | — | not triggered | PASS |
| 7 | Rev decline majority yrs | No | — | not triggered | PASS |
| 8 | PAT negative any last 3yr | No (both +) | — | not triggered | PASS |
| 9 | History <3 yrs | Yes (2) | AVERAGE | triggered | PASS |

- Most-restrictive selection: breakers #4 and #9 → AVERAGE; #2 → GOOD. Most restrictive = **AVERAGE**. Correctly chosen. PASS.
- "State WHICH years drive any deal-breaker" (line 155): maker names both FY24+FY25 for the cash breaker and the full post-IPO dataset for history. Satisfied. PASS.
- CAGR edge rules (lines 45-52): all endpoints positive; both CAGRs labelled single-period (n=1), no synthetic CAGR fabricated, no loss-to-profit swing. Handled correctly. PASS.

**FINAL CLASSIFICATION AVERAGE — CONCUR.** The mechanical destination is exactly what the rules produce. No tier was inflated or suppressed.

### 1.4 Minor adherence caveats (Gate 0) — none change any score, moat count, or classification

- **[MINOR] M7 (Regulatory/License) scored 0 "unregulated."** A BIS mandatory-certification regime for CCTV (IS 13252) does exist and surfaces prominently in the stage-7 inputs. Under the M7 ladder this is at most "regulated but >10 players = 1," never ≥3, so the moat is not "present" either way. Gate 0's input set was AR + screener only (no investor presentation), and the AR states no licensing regime, so scoring 0 on the evidence in front of the maker is defensible. No moat-count or classification impact.
- **[MINOR] M8 (Distribution) scored 0.** Stage 7 (with the investor presentation) documented a 5,200→11,000+ dealer network; Gate 0 (AR only) found none. This is a differing-input-set artefact, not a rule misapplication. Even "mentioned unquantified = 1" is <3, so no moat-count impact.
- **[MINOR] ROCE computed from the AR rather than taken from the source per the formula-definition preference (line 31).** The maker justifies this because the screener P&L/BS/CF CSVs were empty templates, so a source ROCE was effectively unavailable. Resulting values land in the same threshold bands. No score impact. This is chiefly a numbers-provenance matter and falls primarily to Verifier A.

Gate 0 rules checked: 48. Clean passes: 48 (three minor caveats are defensible applications, logged not counted as fails). No CRITICAL, no MAJOR.

═══════════════════════════════════════════════════════════════════
## PART 2 — EMERGING MOAT (B07) COMPLIANCE
═══════════════════════════════════════════════════════════════════

### 2.1 Category completeness (21 categories)

All 21 categories (A1-A4, B1-B3, C1-C2, D1-D2, E1-E2, F1-F2, G1-G2, H1-H3, R1) are addressed in both the Section-3 summary table (lines 217-238) and the Section-5 scorecard (lines 291-311); every unevidenced category is explicitly "NO EVIDENCE FOUND." PASS.

### 2.2 Likelihood×impact matrix + evidence-multiplier arithmetic (prompt lines 128-130)

Matrix key: HH=4, HM/MH=3, HL/MM/LH=2, ML/LM=1, LL=1, none=0. Multipliers: 📄1.0 / 🎙️0.7 / 🔍0.5.

| Cat | Raw label | Raw val correct? | Ev.type | Mult correct? | Adjusted stated | Recompute | Verdict |
|---|---|---|---|---|---|---|---|
| B1 | HH=4 | yes | 📄 1.0 | yes | 4.0 | 4.0 | PASS |
| B3 | MH=3 | yes | 🎙️ 0.7 | yes | 2.1 | 2.1 | PASS |
| F2 | LH=2 | yes | 🎙️ 0.7 | yes | 1.4 | 1.4 | PASS |
| G2 | LM=1 | yes | 🎙️ 0.7 | yes | 0.7 | 0.7 | PASS |
| H2 | LH=2 | yes | 🎙️ 0.7 | yes | 1.4 | 1.4 | PASS |
| R1 | HH=4 | yes | 📄 1.0 | yes | 4.0 | 4.0 | PASS (minor caveat, 2.6) |
| all others | none=0 | yes | — | — | 0.0 | 0.0 | PASS |

Adjusted total = 4.0+2.1+1.4+0.7+1.4+4.0 = **13.6**. Maker = 13.6. PASS.
Classification band (line 131-132): 12-24 = MODEST MOAT DEVELOPMENT. Maker = MODEST. PASS.

### 2.3 Evidence-tier consistency (verifier rule 3 — no 🎙️-only category scored as if 📄)

Checked every scored row. The two 1.0x rows (B1, R1) rest on financial-statement facts (B1: Purchase of Stock-in-Trade falling / Cost of Materials rising across FY25→FY26; R1: obtained BIS-ER certification). All four soft rows (B3, F2, G2, H2) are 🎙️ and correctly carry the 0.7x discount; none is dressed up as 📄. F2 is explicitly "🎙️/📄 mixed, net WEAK" and conservatively multiplied at 0.7x. PASS.

### 2.4 Completionist guard (prompt lines 30-36, 114)

Explicit recount present (lines 242-245): "📄 recount performed: 18 documented items across 2 categories with Strong evidence (B1, R1)." Active-category count = 3 (B1, B3, R1), squarely inside the 3-6 base rate and far below the 12+ inflation trip-wire. active_categories YAML lists only Strong/Moderate rows (B1 Strong, B3 Moderate, R1 Strong); the Weak rows (F2, G2, H2) score points but are correctly excluded from "active." PASS.

### 2.5 Double-credit discipline (CLAUDE.md house rule; prompt "never force-fit")

A1 (cross-ref B1), E2 and H1 (cross-ref R1), and B2/E2 (BIS-ER folded into R1) are deliberately NOT double-scored — each such row is 0 with a stated cross-reference. This is correct application of the one-improvement-one-mechanism rule and is the right call, not a gap. PASS.

### 2.6 Minor adherence caveats (Emerging Moat) — none change the score band or the MODEST classification

- **[MINOR] 2C capex-embedded growth used the capacity-based method (116%) as the headline, not the framework's prescribed FAT-turnover method.** Prompt 2C literally specifies "total capex under execution × historical fixed asset turnover." The maker computed that (Method 2 ≈ 237%) but flagged it unreliable because FY25's 8.6x FAT reflects an asset-light *trading* model, then reported the lower capacity-based 116% as `capex_embedded_growth_pct`. Downstream materiality: in Section-1B Amendment 4.1, capex-embedded growth is a Pillar-3a qualifier at a ≥15% threshold — both 116% and 237% clear it, so the destination-PE effect is nil. The substitution is conservative (chose the lower figure) and reasoned. MINOR, no decision impact.
- **[MINOR] R1 rated HH (impact = High) while the maker's own Section 4C calls durability "Moderate, not structural-forever."** An HM rating (=3, adjusted 3.0) would arguably be more internally consistent, which would drop the total to 12.6 — still inside the 12-24 MODEST band. No classification change. Judgment call within tolerance.

Emerging-moat rules checked: 24. Clean passes: 24 (two minor caveats logged, not counted as fails). No CRITICAL, no MAJOR.

═══════════════════════════════════════════════════════════════════
## PART 3 — VALUATION (B11/B10) COMPLIANCE
═══════════════════════════════════════════════════════════════════

**PENDING — DEFERRED TO PHASE 3.** B11 (valuation) and B10 (assembly) artifacts do not yet exist for this run. The Four-Pillar / FTTCP / UA / Hurdle-Ratio / dual-track audit prescribed by Verifier C rule 4 will run in phase 3 once those reports are produced. No valuation rules were checked in this pass.

═══════════════════════════════════════════════════════════════════
## SUMMARY
═══════════════════════════════════════════════════════════════════

Both in-scope frameworks were applied as written. Every Gate 0 block score, the moat total, the classification matrix, the data-confidence auto-AVERAGE, all nine deal-breaker overrides, and the most-restrictive selection re-derive exactly to the maker's figures — final AVERAGE is the correct mechanical output. The Emerging Moat scan addressed all 21 categories, applied the likelihood×impact matrix and 📄/🎙️/🔍 multipliers correctly, performed the completionist recount (3 active categories, base-rate compliant), honoured the one-improvement-one-mechanism rule, and lands correctly at 13.6 MODEST. Findings are five MINOR items only — three defensible input-set/provenance caveats in Gate 0 and two conservative method/rating choices in B07 — none of which changes any score, the moat count, or either classification. No CRITICAL, no MAJOR. Concur with both destinations.

recomputed classification: AVERAGE (concur) | recomputed EM: 13.6 MODEST (concur).

```yaml
stage: B12c
company: "PRIZOR"
run_date: "2026-07-12"
model: claude-opus-4-8
status: complete
gate0:
  rules_checked: 48
  fails: []
emoat:
  rules_checked: 24
  fails: []
valuation:
  rules_checked: 0
  fails: []
  note: "deferred to phase 3 (B11/B10 not yet produced)"
recomputed_destination_pe: ""   # valuation deferred; not computed this pass
recomputed_decision: ""         # concur: Gate 0 AVERAGE, EM 13.6 MODEST
findings:
  - {severity: "MINOR", location: "B01 Block F / M7", issue: "Regulatory/License scored 0 'unregulated'; a BIS mandatory-cert regime (IS 13252) exists, at most M7=1 (>10 players), never >=3. Defensible on Gate 0's AR-only inputs; no moat-count or classification impact.", rule_ref: "prompts/01 lines 118-120"}
  - {severity: "MINOR", location: "B01 Block F / M8", issue: "Distribution scored 0 (no network in AR); stage 7 with investor presentation documented an 11,000+ dealer network. Differing input set, not a rule error; even M8=1 is <3, no moat-count impact.", rule_ref: "prompts/01 lines 121-123"}
  - {severity: "MINOR", location: "B01 Blocks A/B", issue: "ROCE computed from AR rather than taken from source per formula-def preference; justified by empty screener CSV templates. Same threshold bands; primarily a numbers-provenance matter (Verifier A).", rule_ref: "prompts/01 line 31"}
  - {severity: "MINOR", location: "B07 Section 2C / capex_embedded_growth_pct", issue: "Headline 116% is capacity-based, not the prescribed FAT-turnover method (~237%). Conservative and reasoned; both clear the >=15% Pillar-3a qualifier, so zero destination-PE impact.", rule_ref: "prompts/07 line 50-52; Sec1B Amdt 4.1"}
  - {severity: "MINOR", location: "B07 Section 5 / R1", issue: "R1 rated HH (impact High) despite the maker's own 'Moderate durability' finding; HM (=3.0) would drop total to 12.6, still MODEST. Within-tolerance judgment.", rule_ref: "prompts/07 lines 128-132"}
critical_count: 0
major_count: 0
minor_count: 5
acceptance_rate: 94   # 68 clean of 72 in-scope rules checked; 5 minor caveats, 0 CRITICAL/0 MAJOR
```
