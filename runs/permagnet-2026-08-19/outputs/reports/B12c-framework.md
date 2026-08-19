# B12c — VERIFIER C: FRAMEWORK ADHERENCE (PHASE 1 SCOPE)

Company: Permanent Magnets Ltd (PERMAGNET) | Run date: 2026-08-19
Model: claude-opus-4-8 | Scope: PHASE 1 (Gate 0 B01 + Emerging Moat B07 only)
Valuation audit (B10/B11) NOT run this phase — deferred to phase 3.

Rule sources consulted: prompts/01-gate-0-pipeline.md, prompts/07-emerging-moat-pipeline.md
Artifacts audited: outputs/reports/B01-gate0.md, outputs/reports/B07-emoat.md
Valuation framework docs (Master v3.3, Section 1B, FTTCP v1.2) deliberately NOT loaded — dead context this phase per task scope rule.

Run context that legitimately shapes both reports (verified as documented, not framework errors): NO-CONCALL MODE; no PERMAGNET screener CSV (Gate 0 built from AR-FY26 + results extracts); no shareholding filing (Block E E2/E3 gaps); no peer financials (10 of 12 Block F moat tests peer-data-blocked); F2 run on AR capex-completion evidence in place of the B05 promise-delivery record.

---

## PART 1 — GATE 0 (B01) COMPLIANCE

Method: re-derived every block score from the stated inputs against the stated
thresholds; checked the moat tests, classification matrix, confidence tier,
deal-breaker application, and CAGR edge rules.

### Block A — Return on Capital (ROCE series 31/36/22/14/16; ROE 23/27/17/10/13)
| Rule | Maker | Re-derived | Verdict |
|---|---|---|---|
| A1 Median ROCE | median 22 → band 20-24.9 → 4 | sorted [14,16,22,31,36], median 22 → 4 | PASS |
| A2 Min single-yr ROCE | 14 → band 12-14.9 → 3 | 14 → 3 | PASS |
| A3 Median ROE | median 17 → band 15-19.9 → 4 | sorted [10,13,17,23,27], median 17 → 4 | PASS |
| A4 ROCE trend | 16 vs 31 = -15pp → >5pp → 0 | -15pp → 0 | PASS |
| Block A total | 11 | 11 | PASS |

### Block B — Cash Generation (CFO 39.15/17.59; PAT 15.75/14.77; capex 29.08/43.34)
| Rule | Maker | Re-derived | Verdict |
|---|---|---|---|
| B1 Cum CFO/PAT | 56.74/30.52 = 1.86 → ≥1.00 → 5 | 1.859 → 5 | PASS |
| B2 FCF-positive proportion | 1/2 = 50% → band 50-74 → 2 | 50% → 2 | PASS |
| B3 Cum FCF/PAT | -15.68/30.52 = -0.51 → neg → 0 | -0.514 → 0 | PASS |
| B4 Change in WC days | 136→132 = -4d → band ±5d → 3 | -4d → 3 | PASS |
| Block B total | 10 | 10 | PASS |

Documented data-gap notes (verified as correctly-handled, NOT adherence errors):
(a) B1-B3 computed on a 2-year (FY25-26) window, below the framework's stated
3-year minimum, because only 2 years of audited cash-flow detail exist in the
provided documents; flagged transparently on the report face and in input_gaps.
(b) B4 uses the standalone 5-year WC-days series while B1-B3 use the 2-year
consolidated window — a basis mix, but the only multi-year WC series available,
and flagged. Neither is a scoring error; both are transparently disclosed gaps.

### Block C — Growth (Total Income 133..232; PAT 19/30/23/15/21)
| Rule | Maker | Re-derived | Verdict |
|---|---|---|---|
| C1 Revenue CAGR | (232/133)^.25-1 = 14.94% → 10-14.9 → 3 | 14.93% → 3 | PASS |
| C2 PAT CAGR | (21/19)^.25-1 = 2.54% → <5 → 0 | 2.53% → 0 | PASS |
| C3 Positive YoY yrs | 3/4 = 75% → 75-99 → 3 | 3 of 4 transitions → 3 | PASS |
| C4 PAT-Rev CAGR | 2.54-14.94 = -12.4pp → <-8 → 0 | -12.4pp → 0 | PASS |
| Block C total | 6 | 6 | PASS |
CAGR edge rules: both C1/C2 endpoints positive → no N/M, no synthetic CAGR; correct.

### Block D — Balance Sheet (consolidated FY26)
| Rule | Maker | Re-derived | Verdict |
|---|---|---|---|
| D1 ND/EBITDA | 59.88/42.76 = 1.40x → 1-2x → 3 | 1.40x → 3 | PASS |
| D2 Interest coverage | 28.24/4.10 = 6.89x → 5-9.9 → 4 | 6.89x → 4 | PASS |
| D3 Debt/Equity | 87.99/157.39 = 0.56x → 0.5-1.0 → 3 | 0.559x → 3 | PASS |
| D4 Current ratio | 172.83/42.60 = 4.06x → ≥2.0 → 5 | 4.06x → 5 | PASS |
| Block D total | 15 | 15 | PASS |
Net-debt netting (cash only, not other bank balances) is the conservative choice
(score 3 vs a possible 4); alternative disclosed for downstream re-check. Correct handling.

### Block E — Shareholder Alignment
| Rule | Maker | Re-derived | Verdict |
|---|---|---|---|
| E1 Promoter holding | 58.01% → band 50-59.9 → 4 | 4,987,875/8,598,453 = 58.01% → 4 | PASS |
| E2 3-yr promoter change | N/A (only 1-yr comp) → 0 | not in provided data → 0 per "never estimate" | PASS |
| E3 Pledge | N/A (no disclosure) → 0 | not in provided data → 0 | PASS |
| E4 Contingent liab/NW | 28.85/164.97 = 17.49% → 15-30 → 1 | 17.49% → 1 | PASS |
| Block E total | 5 | 5 | PASS |
E2/E3 scored 0 for absent data is the framework-correct handling (operating rule 5:
absent data = N/A, score 0, no estimate). These are documented gaps, not adherence errors.

### Block F — Quantitative Moat (12 tests)
M1=1 (margin -4pp, rev CAGR ≥10% → "declined 2-5pp despite growth"); M2/M5/M9=0
PEER DATA NEEDED; M3=3 (FAT 2.98x >2, ROCE 16% >15); M4=3 (1 decline yr recovered);
M6=0 (R&D 0.65% <1%); M7=0 (unregulated); M8=0 (direct-to-OEM); M10=3; M11=0
(decelerating, <20%); M12=0 (WC >45d). Sum = 10. Re-derived total = 10. PASS.
Moats present ≥3: M3, M4, M10 = 3 → MODERATE (2-3 band). PASS. Peer-blocked tests
correctly scored 0 with "PEER DATA NEEDED", never guessed — compliant with the rule.

### Classification, confidence, deal-breakers
- Data confidence: 5 years → "5-6 lower, flag may not have seen full cycle"; no tier
  downgrade (downgrade is 3-4yr LIMITED only). history_downgrade: false. PASS.
- Core 47 → matrix band 40-59 → AVERAGE (moat tier does not move the 40-59 band). PASS.
- Grand total 47+10 = 57. PASS.
- Deal-breakers 1-9: all correctly evaluated as not-triggered. #5 (pledge >15%) correctly
  NOT triggered on absent data ("absence of evidence is not evidence of a breach") —
  consistent with the framework and with the CLAUDE.md low-ownership/absent-data posture. PASS.
- FLAG-GATE0 required when classification ≤ AVERAGE with historical depressors: present,
  with depressors named (A4, C2/C4, Block E gaps, Block B swing). PASS.

**Gate 0 verdict: fully self-consistent. 0 fails. All re-derived block totals, moat
count, classification, and deal-breaker calls reproduce exactly.**

---

## PART 2 — EMERGING MOAT (B07) COMPLIANCE

Method: checked all 21 categories addressed/NO EVIDENCE; re-verified each raw
likelihood×impact cell against the matrix; re-applied every evidence multiplier;
re-summed the adjusted total; checked the completionist recount, the active-category
list, the combined-assessment logic, and the F2 NO-CONCALL substitution.

### 21-category coverage
All 21 rows (A1-A4, B1-B3, C1-C2, D1-D2, E1-E2, F1-F2, G1-G2, H1-H3, R1) addressed
with an evidence table or explicit NO EVIDENCE FOUND. PASS. Anchors present on
evidence items; evidence taxonomy (📄/🎙️/🔍) applied per item. PASS.

### Scorecard re-derivation (raw = likelihood×impact; ×evidence multiplier)
| ID | L/I | Raw (matrix) | Mult | Adj | Verdict |
|---|---|---|---|---|---|
| A1 | M/M | MM=2 | 🎙️0.7 | 1.4 | PASS |
| A3 | L/L | LL=1 | 📄1.0 | 1.0 | PASS |
| A4 | M/H | MH=3 | 🎙️0.7 | 2.1 | PASS (0.7 correctly applied to the 🎙️ value-multiplier claim, not 1.0) |
| B1 | M/M-H | 3 | 📄1.0 | 3.0 | PASS |
| B2 | H/M | HM=3 | 📄1.0 | 3.0 | PASS |
| C1 | M/M | 2 | 🎙️0.7 | 1.4 | PASS |
| E2 | M/H | MH=3 | 🎙️0.7 | 2.1 | PASS (conservative 0.7 despite mixed 📄/🎙️) |
| F2 | L/H | LH=2 | 📄1.0 | 2.0 | PASS (1.0 correct — evidence IS documented; low likelihood correctly reflects the unfavourable execution record) |
| G2 | L/L | 1 | 📄1.0 | 1.0 | PASS |
| H2 | H/H | HH=4 | 📄1.0 | 4.0 | PASS on mechanics; see MINOR consistency note below |
| H3 | L/L | 1 | 📄1.0 | 1.0 | PASS |
| R1 | H/H | HH=4 | 📄1.0 | 4.0 | PASS |
| All zero-evidence rows | — | 0 | — | 0.0 | PASS |
| **Adjusted total** | | | | **26.0** | Re-summed = 26.0, PASS |

Classification 26.0 → band 25-39 → MOAT STRENGTHENING. PASS.
No 🎙️-only category is scored as if 📄; the conservative multiplier is used on every
mixed/claim row (A4, E2 at 0.7; A1, C1 at 0.7). Evidence-tier discipline holds. PASS.

### Completionist recount guard
Performed and stated. Active (Strong/Moderate) categories = 6 (A4, B1, B2, E2, H2, R1),
well under the 12-category alarm threshold. Guard outcome (honest-sparse, no force-fit)
is correct. PASS on the guard itself. **MINOR internal inconsistency:** the recount line
(report line 176 and YAML completionist_recount) states "18 documented items across
**9 categories**" but then enumerates **10** categories (A3, A4, B1, B2, E2, F2, G2, H2,
H3, R1). The category count 9 does not match the 10 items listed. No effect on the guard
(both 9 and 10 are far below 12) or on the classification, but it is an internal count
error in a framework-mandated step.

### Active-category list, capex-embedded growth, optionality register
- active_categories = the 6 Strong/Moderate rows; matches the summary-table count of 6. PASS.
- capex_embedded_growth_pct: 25.48 × 2.90 / 226.24 = 32.66% → 32.7%; Section 2C shows the
  arithmetic as required. PASS.
- Optionality register present with all required columns; items are 🎙️/🔍-only or scored 0;
  carried into the YAML. PASS.

### F2 NO-CONCALL substitution
F2 run on AR capex-completion evidence in place of the (unavailable) B05 promise-delivery
record, per the orchestrator's NO-CONCALL degradation instruction. Legitimate documented
mode adaptation, not a framework deviation. PASS.

### Combined assessment (6D)
GOOD+ from AVERAGE-backward + STRENGTHENING-forward. The prompt's "standard matrix"
mapping thresholds for the combined tiers are not contained in prompts/07 (they live in a
framework doc not provided this phase), so the exact GOOD+ vs HIGH POTENTIAL boundary
cannot be independently re-derived from the provided rule source. The maker's reasoning is
internally coherent and consistent with the framework's explicit note that AVERAGE-backward
+ EXPANSION-forward (not STRENGTHENING) is the setup deserving HIGH POTENTIAL; landing one
tier below at GOOD+ is consistent with that spirit. Accepted; flagged only as
non-independently-verifiable from phase-1 inputs. No fail.

### MINOR consistency note — H2 vs F2 likelihood
H2 (REL Developments relay licensing) is rated H/H (raw 4), while F2 rates the same
relay-ramp execution L/H (raw 2) and documents the relay commercialisation as behind
management's own timeline (slipped to H2FY27). The high-likelihood assignment on H2 sits in
mild tension with the low-likelihood execution read on the same underlying relay event. It
is defensible (H2 scores the existence/quality of a signed, documented partnership; F2
scores the execution track record), and the matrix cell H/H is itself valid. Decision
impact is negligible: were H2 re-rated MH=3, em_score = 25.0, still inside the 25-39
STRENGTHENING band, and the GOOD+ combined call is unchanged. Logged MINOR.

**Emerging Moat verdict: methodology applied correctly. 2 MINOR internal-consistency
findings, neither changing em_score band or the combined classification.**

---

## PART 3 — VALUATION (B11) COMPLIANCE

NOT RUN — phase 1 scope. B10/B11 do not exist yet (produced in phase 3). The valuation
framework docs were deliberately not loaded. Status: pending phase 3.

---

## ACCEPTANCE SUMMARY

- Gate 0 (B01): 48 rules checked, 48 passed, 0 fails → self-consistent, reproduces exactly.
- Emerging Moat (B07): 28 checks, 2 MINOR fails (recount category-count 9 vs 10; H2/F2
  likelihood tension) → methodology sound, no band or classification change.
- No CRITICAL, no MAJOR. Neither report's destination decision moves: Gate 0 AVERAGE
  stands; Emerging Moat STRENGTHENING / combined GOOD+ stands.
- The bulk of what depresses both scores is documented data gaps (no screener, no
  shareholding filing, no peer financials, NO-CONCALL) that both makers handled correctly
  under the "never estimate / NOT FOUND only" rule — not framework misapplication.

recomputed_destination_pe: pending phase 3 (valuation not run)
recomputed_decision: concur (Gate 0 AVERAGE; Emerging Moat STRENGTHENING; combined GOOD+)

```yaml
stage: B12c
company: "PERMAGNET"
run_date: "2026-08-19"
model: claude-opus-4-8
status: complete
gate0: {rules_checked: 48, fails: []}
emoat:
  rules_checked: 28
  fails:
    - "completionist_recount states '9 categories' but enumerates 10 (A3,A4,B1,B2,E2,F2,G2,H2,H3,R1); MINOR internal count inconsistency, no effect on the <12 guard outcome or classification"
    - "H2 rated H/H (raw 4) while the same relay-ramp is rated L/H (raw 2) under F2 and documented behind schedule; MINOR consistency tension, em_score would be 25.0 (still STRENGTHENING) if H2 were MH=3"
valuation: {rules_checked: 0, fails: [], status: "pending phase 3"}
recomputed_destination_pe: ""   # pending phase 3, valuation not run
recomputed_decision: ""         # concur: Gate 0 AVERAGE, Emerging Moat STRENGTHENING, combined GOOD+
findings:
  - {severity: "MINOR", location: "B07 line 176 / YAML completionist_recount", description: "Recount line says '18 documented items across 9 categories' but lists 10 categories. Framework-mandated recount step is internally inconsistent on the category count; guard outcome (well under 12) and classification are unaffected."}
  - {severity: "MINOR", location: "B07 scorecard lines 223/227 (F2 and H2)", description: "H2 relay-licensing scored H/H (raw 4) while F2 scores the same relay-ramp execution L/H (raw 2), which the AR documents as behind management's own timeline. Mild internal likelihood tension; defensible (partnership existence vs execution track record) and decision-neutral (re-rating H2 to MH=3 gives em_score 25.0, still STRENGTHENING, GOOD+ unchanged)."}
critical_count: 0
major_count: 0
minor_count: 2
acceptance_rate: 97             # rules passed (74) / rules checked (76); gate0 100%, emoat ~93%
```
