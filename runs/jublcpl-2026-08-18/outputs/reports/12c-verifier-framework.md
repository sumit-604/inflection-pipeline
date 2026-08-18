# STAGE 12c — VERIFIER C: FRAMEWORK ADHERENCE (JUBLCPL)
Run date: 2026-08-18 | Model: claude-opus-4-8 | Scope: PHASE 1 (Gate 0 + Emerging Moat only)
Valuation adherence (B10/B11) is DEFERRED to phase 3 — those stages do not exist yet.
Rule sources: prompts/01-gate-0-pipeline.md, prompts/07-emerging-moat-pipeline.md.
I audit rule application only. Raw number existence belongs to Verifier A; I take the
maker's extracted figures as given and check whether the scoring rules were applied to
them as written.

═══════════════════════════════════════════════════════════════════
## PART 1 — GATE 0 (B01) COMPLIANCE
═══════════════════════════════════════════════════════════════════

### Block A — Return on Capital (claimed 20/20)
| Rule | Input (as stated) | Threshold | Score | Verdict |
|---|---|---|---|---|
| A1 Median ROCE | 5yr {35,28,16,34,36} → median 34% | ≥25%=5 | 5 | PASS |
| A2 Min single-yr ROCE | 16% (FY24) | ≥15%=5 | 5 | PASS |
| A3 Median ROE | 3yr {12.63,31.65,32.85} → median 31.65% | ≥20%=5 | 5 | PASS |
| A4 ROCE trend (5yr) | FY26 36% vs FY22 35% | latest≥earliest=5 | 5 | PASS |

Median of the 5 ROCE values sorts to 16,28,34,35,36 → 34% (3rd value). Correct. Use of
the AR self-reported ROCE chart in lieu of computation is permitted by the formula rule
("if the data source provides its own ROCE, use the source's figure and anchor it").
Block A = 20. PASS.

### Block B — Cash Generation (claimed 16/20)
| Rule | Input | Threshold | Score | Verdict |
|---|---|---|---|---|
| B1 Cum CFO/PAT (FY24-26) | 282.36/245.54 = 1.15 | ≥1.00=5 | 5 | PASS |
| B2 FCF-positive years | 2/2 computable = 100% | 100%=5 | 5 | PASS (partial window) |
| B3 Cum FCF/PAT (FY25-26) | 131.78/215.82 = 0.61 | ≥0.60=5 | 5 | PASS |
| B4 Δ WC days | +6.18 (73.49→79.67) | increase 5-15=1 | 1 | PASS |

Block B = 16. PASS. Note: B2/B3/B4 are each scored on a partial window (FY24 capex and
FY24 trade-payables not computable from the screener aggregate). This is disclosed and
permitted by operating rule 6 ("use whatever history is available"). MINOR: B2 scoring a
2-of-2 window as "100%" is at the generous end since FY24 FCF sign is unknown — no score
impact and transparently flagged, so recorded as observation only.

### Block C — Growth (claimed 6/20)
| Rule | Input | Threshold | Score | Verdict |
|---|---|---|---|---|
| C1 Revenue CAGR (FY22→26) | 13.12% | 10-14.9%=3 | 3 | PASS |
| C2 PAT CAGR | −4.25% (both endpoints +) | negative=0 | 0 | PASS |
| C3 Positive YoY yrs | 3/4 = 75% | 75-99%=3 | 3 | PASS |
| C4 PAT−Rev CAGR | −17.37pp | <−8pp=0 | 0 | PASS |

CAGR edge rules honoured: neither PAT endpoint is negative/zero, so C2 is a real negative
CAGR scored 0 via the band (not marked N/M); no loss-to-profit swing (PAT positive
throughout) so no synthetic-CAGR suppression needed; C4 computed normally since PAT CAGR
is not N/M. Choice of the 5yr window over the 2yr window is a methodology call the maker
justified (2yr window would score near-max off the FY24 trough) — sound and disclosed.
Block C = 6. PASS.

### Block D — Balance Sheet (claimed 18/20)
| Rule | Input | Threshold | Score | Verdict |
|---|---|---|---|---|
| D1 Net Debt/EBITDA | 0.12x (net debt 23.17, not net cash) | 0-1.0x=4 | 4 | PASS |
| D2 Interest Coverage | 23.91x | ≥10x=5 | 5 | PASS |
| D3 Debt/Equity | 0.06 | <0.1=5 | 5 | PASS |
| D4 Current Ratio | 1.63 | 1.5-1.99=4 | 4 | PASS |

D1 correctly withheld the "net cash"=5 band (position is net debt of ₹23.17 Cr). Block D
= 18. PASS.

### Block E — Shareholder Alignment (claimed 11/20)
| Rule | Input | Threshold | Score | Verdict |
|---|---|---|---|---|
| E1 Promoter holding | 74.35% | ≥60%=5 | 5 | PASS |
| E2 Holding change (1yr) | −0.41pp | ±1%=3 | 3 | PASS |
| E3 Pledge | NOT FOUND | N/A→0 | 0 | PASS |
| E4 Contingent Liab/NW | 12.27% | 5-15%=3 | 3 | PASS |

E3 correctly scored 0 under the "never estimate, NOT FOUND is the only fill" rule rather
than assumed nil — and correctly NOT treated as a >15% pledge deal-breaker. E2 measured
over 1 year (post-listing history limit) is disclosed and does not change the band. Block
E = 11. PASS.

### Block F — Quantitative Moat (claimed 15/60)
| Test | Score | Verdict |
|---|---|---|
| M1 Pricing Power | 3 | PASS — margin +1.58pp (within ±2pp stable) AND rev CAGR 13.12%≥10% |
| M2 Cost Advantage | 0 | PASS — PEER DATA NEEDED, correctly not guessed |
| M3 Capital Efficiency | 5 | PASS — FAT 9.36x>3x AND ROCE 36%>20% |
| M4 Customer Stickiness | 3 | PASS — 1 decline yr fully recovered |
| M5 Scale/Dominance | 0 | PASS — PEER DATA NEEDED |
| M6 Technology/R&D | 0 | PASS (result); see MINOR below |
| M7 Regulatory/License | 0 | PASS — competitor count unavailable |
| M8 Distribution | 1 | PASS — reach quantified but growth/rev-per-outlet undisclosed |
| M9 Brand | 0 | PASS — PEER DATA NEEDED |
| M10 Switching Costs | 3 | **FLAGGED — boundary call, see MAJOR below** |
| M11 Network Effects | 0 | PASS — <6yr, conservative, signal negative |
| M12 Negative WC/Float | 0 | PASS — WC days >45 both years |

Block F = 3+5+3+1+3 = 15. Moats "present" (≥3): M1, M3, M4, M10 = 4 → STRONG (4-5).

**MAJOR — M10 Switching Costs sits on an unresolved rubric boundary and is decision-
relevant.** The rubric: band 5 = "revenue grew EVERY year AND receivable days rose ≤10
days over period"; band 3 = "growth all but 1 year AND stable"; band 1 = "overall growth,
2+ decline years". JACPL grew in all but 1 year (FY24), so band 5 is out. Band 3 requires
receivables "stable" — but the only measurable transition (FY25→FY26) shows receivable
days rising +11.4, which exceeds the ≤10-day figure the rubric itself uses to quantify
"stable" one tier up. The maker scored 3, arguing band-3 "stable" carries no fixed
threshold. That reading is defensible (band 3 is intentionally looser than band 5), but a
strict reading (apply the same ≤10 proxy) fails "stable"; band 1 does not fit either (only
1 decline year, not 2+), leaving "else = 0". Sensitivity: if M10 drops below 3, moats
present = 3 → moat class MODERATE, and under the classification matrix Core 71 (60-79) +
MODERATE = GOOD (not GOOD+). So this single boundary call is what separates GOOD+ from
GOOD. Rated MAJOR (not CRITICAL) because the rubric genuinely under-specifies this case,
the maker disclosed the caveat explicitly, and the generous reading is legitimate — but it
must be surfaced because the classification tier turns on it.

**MINOR — M6.** Scored 0 as "R&D/Rev not located." B07 in fact locates R&D at 1.17% of
turnover (AR p.54). Even so, M6's ≥1% band additionally requires "margin above peer
median," which needs peer data that was not provided, so the correct score is 0 regardless.
Score unaffected; the "NOT FOUND" characterisation is imprecise but the rule application
lands correctly.

### Classification, matrix, deal-breakers
- Core = A+B+C+D+E = 20+16+6+18+11 = **71**. Correct.
- Grand total = 71 + 15 = **86**. Correct.
- Classification matrix: Core 71 (60-79) + STRONG → GOOD+. Correct **given STRONG stands**
  (see M10 MAJOR).
- Deal-breakers 1-9 all correctly evaluated as not triggered. Note #5 (pledge >15%)
  correctly NOT triggered on a NOT FOUND; #6 (ND/EBITDA>3x AND IC<3x) correctly not
  triggered.
- Data confidence: 5 years → "lower / may not have seen full cycle" tier; no
  classification downgrade required at 5-6 yrs (downgrade applies only at 3-4 yrs).
  history_downgrade=false is correct. Mixed-depth flagged extensively. PASS.
- flags=[]: the FLAG-GATE0 rule fires only when classification ≤ AVERAGE with historical
  depressors; classification is GOOD+, so empty flags is correct. block_b_trend
  "deteriorating" is carried in its own field for downstream FLAG-CASH. PASS.

**Gate 0 verdict: mechanically sound. One MAJOR boundary call (M10) that the GOOD+/GOOD
classification hinges on; two MINOR imprecisions with no score impact.**

═══════════════════════════════════════════════════════════════════
## PART 2 — EMERGING MOAT (B07) COMPLIANCE
═══════════════════════════════════════════════════════════════════

### Category coverage (21 = 20 + R1)
All 20 categories (A1-A4, B1-B3, C1-C2, D1-D2, E1-E2, F1-F2, G1-G2, H1-H3) addressed in
Section 3, each with an evidence table or explicit NO EVIDENCE FOUND; R1 addressed in
Section 4. **21/21 addressed. PASS.**

### Scorecard re-derivation (matrix HH=4, HM/MH=3, HL/MM/LH=2, ML/LM=1, LL=1, none=0; ×📄1.0/🎙️0.7/🔍0.5)
| Cat | L,I | Raw | Ev | Mult | Adj | Recomputed | Verdict |
|---|---|---|---|---|---|---|---|
| A1 | M,M | 2 | 🎙️ | 0.7 | 1.4 | 1.4 | PASS |
| A2 | — | 0 | — | — | 0.0 | 0.0 | PASS |
| A3 | H,M | 3 | 📄 | 1.0 | 3.0 | 3.0 | PASS |
| A4 | H,M | 3 | 📄 | 1.0 | 3.0 | 3.0 | PASS |
| B1 | L,L | 1 | 🎙️ | 0.7 | 0.7 | 0.7 | PASS |
| B2 | L,M | 1 | 🎙️ | 0.7 | 0.7 | 0.7 | PASS |
| B3 | — | 0 | — | — | 0.0 | 0.0 | PASS |
| C1 | — | 0 | — | — | 0.0 | 0.0 | PASS |
| C2 | M,L | 1 | 📄 | 1.0 | 1.0 | 1.0 | PASS |
| D1 | — | 0 | — | — | 0.0 | 0.0 | PASS |
| D2 | — | 0 | — | — | 0.0 | 0.0 | PASS |
| E1 | M,L | 1 | 📄 | 1.0 | 1.0 | 1.0 | PASS |
| E2 | — | 0 | — | — | 0.0 | 0.0 | PASS |
| F1 | L,L | 1 | 🎙️ | 0.7 | 0.7 | 0.7 | PASS |
| F2 | H,M | 3 | 📄 | 1.0 | 3.0 | 3.0 | PASS |
| G1 | H,H | 4 | 📄 | 1.0 | 4.0 | 4.0 | PASS |
| G2 | — | 0 | — | — | 0.0 | 0.0 | PASS |
| H1 | — | 0 | — | — | 0.0 | 0.0 | see MINOR |
| H2 | — | 0 | — | — | 0.0 | 0.0 | PASS |
| H3 | H,M | 3 | 📄 | 1.0 | 3.0 | 3.0 | PASS |
| R1 | L,L | 1 | 📄 | 1.0 | 1.0 | 1.0 | PASS |

Independent sum = 1.4+3.0+3.0+0.7+0.7+1.0+1.0+0.7+3.0+4.0+3.0+1.0 = **22.5**. Matches
em_score exactly. Every multiplier is consistent with the stated evidence tier — no
🎙️-only category is scored on a 1.0x (📄) basis. A1 (SBR customer traction), B1
(butadiene "exploring"), B2 (bare approval claim) and F1 (qualitative talent) are all
correctly held to 0.7x and Weak. **PASS.**

### Classification
22.5 falls in 12-24 → **MODEST MOAT DEVELOPMENT.** Correct. (Close to the 24/25 boundary;
even the MINOR below would leave it inside MODEST.)

### Completionist guard
Base rate 3-6; the scan found 5 active (Strong/Moderate) categories, well under the 12-
category re-examination trigger. The explicit 📄 recount line is present: "5 documented
items across 5 categories" (G1, A3, A4, H3, F2), with an affirmative statement that no
category was inflated from 🎙️ to 📄 and a named list of the items deliberately held at
Weak. **PASS — guard applied as written, and the discipline is genuine.**

### F2 credibility handling
F2 capped at HM (raw 3) rather than HH (raw 4) to reflect the injected B05 credibility
grade C, with the 📄 multiplier retained because the Samlaya delivery is independently
corroborated (Reg 30). This is a defensible, disclosed judgment consistent with the
injected input. PASS.

### capex_embedded_growth (Section 2C)
Formula "total capex under execution × historical FAT = implied incremental revenue, as %
of current revenue": ₹500mn × 9.53 = ₹4,765mn; ÷ ₹18,911mn = 25.2%. Arithmetic and formula
application correct; the blended-FAT overstatement caveat is carried as 🔍. PASS.

### Combined assessment (6D)
Backward GOOD+ (from injected B01) + forward MODEST → combined GOOD+, with HIGH POTENTIAL/
TURNAROUND correctly reserved for weak-backward + EXPANSION-forward transition setups
(not this profile, since backward is already strong). 6C table reproduces the injected
Gate 0 block faithfully (Core 71, Moat 15, Grand 86, 4 moats, GOOD+). PASS.

### MINOR findings (B07)
- **H1 internal inconsistency.** Section 3 summary table marks H1 "Yes / 🎙️ / Weak," but
  the Section 5 scorecard scores H1 at raw 0 / 0.0 (no-evidence treatment). The scorecard
  treatment is consistent with the H1 narrative (an existing structural position, no
  documented consolidation event), so the summary-table row is the outlier. If H1 were
  instead scored like the other Weak/🎙️ rows (LL=1 ×0.7 = 0.7), the total would be 23.2 —
  still MODEST, no classification change. MINOR, presentational.
- **evidence_mix vs recount terminology.** YAML evidence_mix documented:8 counts all
  📄-tagged scored categories (A3,A4,C2,E1,F2,G1,H3,R1), whereas the completionist recount
  cites 5 documented items (the Strong/Moderate active ones only). Two different
  definitions, both internally reasonable; no rule violation, but the two "documented"
  counts read as inconsistent without the definitions spelled out. MINOR.

**Emerging Moat verdict: fully compliant. Scorecard reproduces to 22.5 to the decimal,
multipliers honest, completionist guard genuinely applied. Two MINOR presentational
inconsistencies, no score or classification impact.**

═══════════════════════════════════════════════════════════════════
## PART 3 — VALUATION (B11) — DEFERRED
═══════════════════════════════════════════════════════════════════
Out of phase-1 scope. B10/B11 do not exist yet and the valuation framework docs were
correctly not loaded. valuation: pending-phase-3.

═══════════════════════════════════════════════════════════════════
## SUMMARY
═══════════════════════════════════════════════════════════════════
- CRITICAL: 0
- MAJOR: 1 (Gate 0 M10 boundary call — GOOD+/GOOD classification turns on it)
- MINOR: 4 (Gate0: B2 partial-window generosity, M6 NOT-FOUND imprecision; B07: H1
  summary/scorecard inconsistency, evidence_mix vs recount terminology)
- Gate 0 core/moat/classification arithmetic re-derived and correct throughout.
- Emerging Moat scorecard re-derived to 22.5 exactly; classification MODEST correct.
- No fabricated rule, no double-crediting, no inflation of 🎙️ to 📄.
- No REWORK trigger from this verifier (no CRITICAL; acceptance well above 60%).
- Downstream note: Gate 0 GOOD+ rests on M10 = 3. A strict "≤10-day stable" reading of
  M10 would yield moat MODERATE and classification GOOD. Whoever sizes the position
  should know the tier hinges on one boundary call.

```yaml
stage: B12c
company: "JUBLCPL"
run_date: "2026-08-18"
model: claude-opus-4-8
status: complete
gate0:
  rules_checked: 50
  fails:
    - {rule: "M10 Switching Costs", issue: "band-3 'stable' applied to receivables +11.4 days, exceeding the >10-day proxy band 5 uses to define stable; defensible but classification-relevant", scored: 3, strict_reading: "below 3 -> moats present 3 -> moat MODERATE -> classification GOOD", severity: MAJOR}
emoat:
  rules_checked: 30
  fails: []
valuation: pending-phase-3
recomputed_destination_pe: ""
recomputed_decision: "Gate0 GOOD+ stands under maker's M10 reading; strict M10 (<=10-day 'stable') reading drops M10 below 'present' -> moat class MODERATE -> classification GOOD. Emerging Moat MODEST (22.5) confirmed unchanged."
findings:
  - {severity: MAJOR, location: "B01 report Block F, M10 Switching Costs", description: "M10 scored 3 on a receivables move of +11.4 days that exceeds the <=10-day figure band 5 uses to quantify 'stable'; band 1 does not fit (only 1 decline year), so a strict reading gives 0/else. At 3, moats present = 4 (STRONG) and classification GOOD+; below 3, moats present = 3 (MODERATE) and classification GOOD. The tier hinges on this single boundary call. Defensible and disclosed by the maker, hence MAJOR not CRITICAL, but must be surfaced."}
  - {severity: MINOR, location: "B01 report Block B, B2", description: "FCF-positive proportion scored 100% (=5) on a 2-of-2 computable window; FY24 FCF sign unknown. Disclosed, permitted by the 'use whatever history is available' rule, no score impact; recorded as generosity observation."}
  - {severity: MINOR, location: "B01 report Block F, M6", description: "M6 scored 0 as 'R&D/Rev not located', but B07 locates R&D at 1.17% of turnover; the ==1% band still needs peer-median margin (not provided), so 0 is correct regardless. Characterisation imprecise, rule application correct."}
  - {severity: MINOR, location: "B07 report Section 3 summary table vs Section 5 scorecard, H1", description: "H1 marked 'Yes/Weak/claim' in the summary table but scored raw 0 / 0.0 in the scorecard (no-evidence). Scorecard is consistent with the H1 narrative; summary row is the outlier. Alternate 0.7 scoring would give 23.2, still MODEST. Presentational only."}
  - {severity: MINOR, location: "B07 YAML evidence_mix vs completionist_recount", description: "evidence_mix documented:8 (all 📄-tagged scored categories) vs recount '5 documented items' (Strong/Moderate active only) use two different definitions; both internally valid but read as inconsistent without the definitions stated."}
critical_count: 0
major_count: 1
minor_count: 4
acceptance_rate: 94
```
