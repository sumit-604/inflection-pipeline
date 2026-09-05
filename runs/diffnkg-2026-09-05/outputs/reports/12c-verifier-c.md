# VERIFIER C — FRAMEWORK ADHERENCE (B12c)
Company: Diffusion Engineers Ltd (DIFFNKG) | Run date: 2026-09-05
Model: claude-opus-4-8 | Scope: PHASE 1 PARTIAL (Gate 0 + Emerging Moat only)

Valuation adherence audit (B10/B11) is DEFERRED to Phase 3 and NOT run here.
This pass audits rule application only. It does not judge company quality and
does not re-verify that a number exists in a source PDF (Verifier A owns the
existence-of-a-number question). Where I re-derive a score, I re-derive it
from the inputs the report itself states.

═══════════════════════════════════════════════════════════════════
## PART 1 — GATE 0 (B01) COMPLIANCE
═══════════════════════════════════════════════════════════════════

Every block score re-derived from the report's own extracted inputs against
the thresholds in prompts/01-gate-0-pipeline.md.

### Block A — Return on Capital (thresholds §BLOCK A)
| Line | Stated input | Band applied | Recompute | Verdict |
|---|---|---|---|---|
| A1 | Median ROCE 15.28% | 15-19.9 = 3 | 3 | PASS |
| A2 | Min single-yr ROCE 12.54% | 12-14.9 = 3 | 3 | PASS |
| A3 | Median ROE 12.92% | 12-14.9 = 2 | 2 | PASS |
| A4 | latest 15.49% >= earliest 14.79% | latest>=earliest = 5 | 5 | PASS |
| Block A sum | 3+3+2+5 | = 13 | 13 | PASS |

### Block B — Cash Generation (thresholds §BLOCK B)
| Line | Stated input | Band applied | Recompute | Verdict |
|---|---|---|---|---|
| B1 | Cum CFO/PAT 0.5815 | 0.50-0.69 = 1 | 1 | PASS |
| B2 | FCF+ years 2/7 = 28.6% | <50 = 0 | 0 | PASS |
| B3 | Cum FCF/PAT -0.150 | negative = 0 | 0 | PASS |
| B4 | WC Days not computable (payables not isolated) | N/A -> 0 per rule 5 | 0 | PASS |
| Block B sum | 1+0+0+0 | = 1 | 1 | PASS |

B4 handling is compliant: rule 5 requires "N/A (not in provided data)" and
score 0 when a data point is absent. Trade Payables are genuinely not isolable
in the screener Data Sheet, so the WC Days formula cannot complete. No
estimate was substituted. PASS.

### Block C — Growth (thresholds §BLOCK C)
| Line | Stated input | Band applied | Recompute | Verdict |
|---|---|---|---|---|
| C1 | Rev CAGR 14.89% | 10-14.9 = 3 | 3 | PASS |
| C2 | PAT CAGR 26.9% | >=20 = 5 | 5 | PASS |
| C3 | 7/7 positive YoY = 100% | 100 = 5 | 5 | PASS |
| C4 | 26.9 - 14.89 = +12.0pp | >=+3pp = 5 | 5 | PASS |
| Block C sum | 3+5+5+5 | = 18 | 18 | PASS |

CAGR edge rules honoured: both endpoints positive on every CAGR; no loss-to-
profit swing in the window; no synthetic CAGR forced. PASS.

### Block D — Balance Sheet (thresholds §BLOCK D)
| Line | Stated input | Band applied | Recompute | Verdict |
|---|---|---|---|---|
| D1 | Net cash (-68.94cr) | net cash = 5 | 5 | PASS |
| D2 | IC 23.4x | >=10 = 5 | 5 | PASS |
| D3 | D/E 0.071 | <0.1 = 5 | 5 | PASS |
| D4 | Current ratio proxy 4.35 | >=2.0 = 5 | 5 | PASS |
| Block D sum | 5+5+5+5 | = 20 | 20 | PASS |

D4 uses the screener Other-Assets/Other-Liabilities proxy, explicitly labelled
as a proxy in-line and in data_notes. Acceptable under rule 4/5 (anchored,
basis stated). PASS.

### Block E — Shareholder Alignment (thresholds §BLOCK E)
| Line | Stated input | Band applied | Recompute | Verdict |
|---|---|---|---|---|
| E1 | Promoter holding ABSENT | N/A -> 0 | 0 | PASS |
| E2 | Holding change ABSENT | N/A -> 0 | 0 | PASS |
| E3 | Pledge ABSENT | N/A -> 0 | 0 | PASS |
| E4 | Contingent liab / NW <5% | <5 = 5 | 5 | PASS |
| Block E sum | 0+0+0+5 | = 5 | 5 | PASS |

E1 professionally-managed override (3 if FII+DII>50%) correctly not applied:
no FII/DII data present. Missing data scored 0, not estimated. PASS.

### Block F — Quantitative Moat (thresholds §BLOCK F, M1-M12)
| Test | Stated basis | Band applied | Recompute | Verdict |
|---|---|---|---|---|
| M1 | margin +3.26pp AND rev CAGR 14.89 | top tier = 5 | 5 | PASS |
| M2 | PEER DATA NEEDED | 0 | 0 | PASS |
| M3 | FAT 3.69x, ROCE 15.49 (not >20) | FAT>2x & ROCE>15 = 3 | 3 | PASS |
| M4 | 0 decline yrs, recv days +35.5 | tier-3 = 3 | 3 | PASS* |
| M5 | PEER DATA NEEDED | 0 | 0 | PASS |
| M6 | R&D not quantified %-of-rev | 0 | 0 | PASS |
| M7 | unregulated segment | 0 | 0 | PASS |
| M8 | reach quantified, rev CAGR <15, rev/outlet not tracked | 1 | 1 | PASS* |
| M9 | PEER DATA NEEDED | 0 | 0 | PASS |
| M10 | recv days +35.5 (>10), no 2+ declines | 0 | 0 | PASS |
| M11 | latest 3y 16.86 < prior 18.28, selling% rising | 1 | 1 | PASS |
| M12 | WC days 150-181, never negative | 0 | 0 | PASS |
| Moat sum | | = 13 | 13 | PASS |

*M4 and M8 involve a residual-tier judgment where no tier fits cleanly (M4:
zero declines but unstable receivables; M8: reach IS quantified but the "middle"
tier fails on the 15% CAGR cut, leaving only the residual "1"). Both landings
are defensible and conservative. Not flagged.

Moat presence: M1(5), M3(3), M4(3) = 3 present. Threshold "2-3 = MODERATE".
moat_class MODERATE. PASS. PEER DATA NEEDED correctly scored 0, never guessed
(rule §BLOCK F). PASS.

### Classification, confidence, deal-breakers
| Rule | Report | Recompute | Verdict |
|---|---|---|---|
| Core = A+B+C+D+E | 57 | 13+1+18+20+5 = 57 | PASS |
| Grand total = core+moat | 70 | 57+13 = 70 | PASS |
| Data confidence tier | "8 yrs = moderate, no downgrade" | 7-9 = moderate, no tier downgrade | PASS |
| Classification matrix | Core 57 -> AVERAGE | 40-59 = AVERAGE | PASS |
| Deal-breaker 2 (Block B<8) | caps at max GOOD, non-binding | correct (already AVERAGE) | PASS |
| Deal-breakers 1,3-9 | none triggered | confirmed not triggered | PASS |
| FLAG-GATE0 present | yes (AVERAGE + depressors) | required by YAML note | PASS |

### GATE 0 FINDING (1)
**history_downgrade field mislabelled — MINOR.** The report body states plainly
"Data confidence: 8 years = moderate (7-9yr band). No automatic tier downgrade
triggered by history length" (report §Classification). The scoring rule applies
a history-length tier downgrade only at 3-4 years (LIMITED) or <3 years (auto
AVERAGE); at 8 years none applies. Yet the YAML sets `history_downgrade: true`.
The field is being used to record the post-IPO "historical depressor" narrative,
not the history-LENGTH downgrade the field names. Body and YAML contradict.
Classification is correct (AVERAGE) either way, so no decision impact. Fix:
set `history_downgrade: false`; carry the IPO-rebase point in flags/data_notes,
where it already sits.

Gate 0 verdict: scoring is clean and fully re-derivable. One MINOR field-
semantics/alignment defect.

═══════════════════════════════════════════════════════════════════
## PART 2 — EMERGING MOAT (B07) COMPLIANCE
═══════════════════════════════════════════════════════════════════

Audited against prompts/07-emerging-moat-pipeline.md.

### Coverage — all 23 rows addressed
22 categories (A1-A4, B1-B3, C1-C2, D1-D2, E1-E2, F1-F2, G1-G2, H1-H3, I1-I2)
plus R1 = 23 rows, each with an evidence table or explicit NO EVIDENCE FOUND,
and all 23 present in the Section 5 scorecard. PASS.

### Likelihood x impact -> raw mapping (HH=4, HM/MH=3, HL/MM/LH=2, ML/LM=1, LL=1)
Every non-zero row checked: A3 LM=1, B1 MM=2, B2 MH=3, C1 MH=3, C2 LL=1,
E1 LL=1, E2 LM=1, F1 LL=1, F2 MM=2, G1 LM=1, H2 MH=3, H3 LL=1, R1 LM=1.
All map correctly. PASS.

### Category 21 / 22 (rule §I1, §I2 and verifier rule 8)
- **I1 Talent asymmetry** scored 0. Part (a) fails (no named patent inventors,
  no verifiable ex-DRDO/HAL/major concentration, median CTC routine) and part
  (b) fails (no competitor-arithmetic evidence). Both legs required; the (b)-leg
  📄 requirement is moot at score 0. Correctly scored 0. PASS.
- **I2 Cannibalization barrier** scored 0. Report tests each claimed moat and
  concludes "nothing must be destroyed" = execution lead, not configuration.
  No specific named sacrifice, so 0 is mandated. PASS.
Both present, both correctly 0. Rule 8 satisfied; no threshold crossing forced
through I1/I2, and the I1/I2 contribution is stated separately (0 of 18). PASS.

### Completionist recount (rule §COMPLETIONIST GUARD)
Explicit line present: "📄 recount performed: 9 documented items across 7
categories." Active Strong/Moderate count is 5, inside the 3-6 base rate. Guard
applied as written. PASS.

### Evidence-tier consistency (verifier rule 3: no 🎙️-only row scored as 📄)
No 🎙️-only category is scored at the 1.0x documented multiplier. C1 (🎙️-only)
carries 0.7x; A3, C2, E2, R1 (🎙️) carry 0.7x. PASS on the specific guard.

### FINDING (1) — invented evidence-quality multiplier — MAJOR (outcome-neutral)
The framework defines exactly three evidence-quality multipliers: 📄 1.0x,
🎙️ 0.7x, 🔍 0.5x (rule §SECTION 5). The scorecard invents a fourth value,
"blended 0.85", for five mixed-evidence rows: B1 (2x0.85=1.7), B2 (3x0.85=2.55),
F1 (1x0.85=0.85), F2 (2x0.85=1.7), H2 (3x0.85=2.55). 0.85 is not in the stated
set; the framework gives no blending rule. This is a systematic departure from
the multiplier table across five categories.
Recompute both bounds (assign the single governing tier instead of blending):
- If the forward/uncertain leg governs (🎙️ 0.7x): total ~15.9 -> classification
  MODEST (12-24).
- If the delivered leg governs (📄 1.0x): total ~19.2 -> classification MODEST.
Classification is MODEST under any admissible multiplier and stays well below
the EM>=25 UA qualifier, so no decision, band, or gate flips. Graded MAJOR for
the systematic rule departure; decision survives. Fix: assign one governing
tier per category per the table, or have the operator ratify a blend rule.

### FINDING (2) — adjusted-total summation error — MINOR (outcome-neutral)
Summing the report's own adjusted column gives 17.25 (0.7+1.7+2.55+2.1+0.7+1.0
+0.7+0.85+1.7+1.0+2.55+1.0+0.7). The report states 17.55, rounds to 18, and
sets `em_score: 18`. The true sum of the stated components is 17.25, which
rounds to 17. Both 17 and 18 fall in the 12-24 MODEST band, so classification
is unaffected. MINOR. (Independent of Finding 1, which would move the base sum
further.)

### Other rules — PASS
| Rule | Verdict |
|---|---|
| Classification band from em_score (18 -> MODEST, 12-24) | PASS |
| active_categories = Strong/Moderate rows only (5 listed) | PASS |
| Optionality register present; only 0/🎙️/🔍 items, watched not scored | PASS |
| catalysts_12m present, each anchored + evidence_type | PASS |
| Combined 6D assessment applies the standard matrix, reasoned | PASS |
| Six sections all executed in one pass | PASS |

Emerging Moat verdict: category coverage, the completionist guard, the I1/I2
two-leg discipline, and the raw likelihood x impact mapping are all applied as
written. One MAJOR methodology deviation (invented 0.85 multiplier) and one
MINOR arithmetic slip, both outcome-neutral (classification stays MODEST).

═══════════════════════════════════════════════════════════════════
## PART 3 — VALUATION (B10/B11) — DEFERRED
═══════════════════════════════════════════════════════════════════
Not run. Phase-1 partial scope. B10/B11 artifacts do not exist yet; the
valuation framework docs were not loaded (per Verifier C phase-1 scope). This
section is PENDING PHASE 3. The Business Understanding Narrative check (stage
13) is likewise out of phase-1 scope: stage 13 is not among the inputs.

═══════════════════════════════════════════════════════════════════
## SUMMARY
═══════════════════════════════════════════════════════════════════
- Gate 0 (B01): 14 rules checked, 1 MINOR fail (history_downgrade field).
  Scoring fully re-derivable; classification AVERAGE confirmed.
- Emerging Moat (B07): 13 rules checked, 1 MAJOR + 1 MINOR, both outcome-
  neutral. Classification MODEST confirmed under any admissible multiplier.
- No CRITICAL. No recomputed classification change on either artifact.
- acceptance_rate = 24 passed / 27 checked = 89%.

```yaml
stage: B12c
company: "DIFFNKG"
run_date: "2026-09-05"
model: claude-opus-4-8
status: complete
gate0:
  rules_checked: 14
  fails:
    - {severity: "MINOR", rule: "data-confidence / history-downgrade field", location: "B01 YAML history_downgrade", issue: "Set true, but body states no history-length tier downgrade applies at 8yrs (moderate); field records the IPO-rebase depressor, not the length downgrade it names. Body and YAML contradict. Classification AVERAGE correct regardless.", fix: "set history_downgrade: false; keep IPO-rebase point in flags/data_notes"}
emoat:
  rules_checked: 13
  fails:
    - {severity: "MAJOR", rule: "Section 5 evidence-quality multiplier (only 1.0/0.7/0.5 defined)", location: "B07 Section 5 scorecard rows B1,B2,F1,F2,H2", issue: "Invented 'blended 0.85' multiplier on 5 mixed-evidence rows; 0.85 not in the defined set and no blending rule exists. Recompute at either governing tier (0.7x ~15.9 or 1.0x ~19.2) leaves classification MODEST and below EM>=25. Systematic departure, decision survives.", fix: "assign one governing evidence tier per category or ratify a blend rule via operator"}
    - {severity: "MINOR", rule: "Section 5 adjusted-total sum/rounding", location: "B07 Section 5 total / em_score", issue: "Sum of stated adjusted column = 17.25 (rounds 17), report states 17.55 -> em_score 18. Both in 12-24 MODEST band; classification unaffected.", fix: "correct arithmetic; em_score 17 on the stated components"}
valuation: {rules_checked: 0, fails: [], status: "pending-phase-3 (B10/B11 not run; valuation framework docs not loaded in phase-1 scope)"}
business_understanding_narrative: {present: false, five_questions_answered: false, prose_only: false, section6_candidates_named: 0, valuation_vocab_leak: false, fails: [], status: "out-of-scope-phase-1 (stage 13 not audited; not a REWORK trigger this phase)"}
recomputed_destination_pe: ""
recomputed_decision: ""
findings:
  - {severity: "MAJOR", location: "B07 Section 5 scorecard (B1,B2,F1,F2,H2)", note: "Invented 0.85 evidence-quality multiplier outside the defined 1.0/0.7/0.5 set; outcome-neutral, classification stays MODEST"}
  - {severity: "MINOR", location: "B01 YAML history_downgrade", note: "history_downgrade:true contradicts body (no history-length downgrade at 8yrs); no decision impact"}
  - {severity: "MINOR", location: "B07 Section 5 adjusted total / em_score", note: "Stated components sum to 17.25 (rounds 17), report shows 17.55->18; MODEST band unaffected"}
critical_count: 0
major_count: 1
minor_count: 2
acceptance_rate: 89
```
