# B12c — VERIFIER C: FRAMEWORK ADHERENCE (PHASE 1 SCOPE)
Company: Vinyas Innovative Technologies Ltd (VINYAS) | Run date: 2026-09-01
Model: claude-opus-4-8 | Scope: Gate 0 (B01) + Emerging Moat (B07) only.
Valuation audit (B10/B11) deferred to phase 3. Stages 10 and 11 do not exist yet.

Rule sources read: prompts/01-gate-0-pipeline.md, prompts/07-emerging-moat-pipeline.md.
Artifacts audited: outputs/reports/01-gate0.md, outputs/reports/07-emoat.md.
Method: re-derive every block score from the stated inputs using the stated
thresholds; check caps, classification matrix, deal-breakers, evidence tiers,
multipliers, and output format. Numbers-in-source is Verifier A's gate, not mine.

═══════════════════════════════════════════════════════════════════
## PART 1 — GATE 0 (B01) COMPLIANCE
═══════════════════════════════════════════════════════════════════

### Block-by-block re-derivation

| Line | Stated input | Threshold band | Score claimed | Re-derived | Verdict |
|---|---|---|---|---|---|
| A1 Median ROCE | 24.34 / 22.88, median 23.61% | 20-24.9 = 4 | 4 | 4 | PASS |
| A2 Min ROCE | 22.88% | ≥15 = 5 | 5 | 5 | PASS |
| A3 Median ROE | 7 yrs, median (4th of 7) 14.12% | 12-14.9 = 2 | 2 | 2 | PASS |
| A4 ROCE trend | 22.88 vs 24.34 = -1.46pp | decline 1-3pp = 3 | 3 | 3 | PASS |
| Block A | | | 14 | 14 | PASS |
| B1 CFO/PAT | -38.27 / 76.54 = -0.50 | <0.50 = 0 | 0 | 0 | PASS |
| B2 FCF-pos yrs | 1 of 2 = 50% | 50-74 = 2 | 2 | 2 | PASS |
| B3 FCF/PAT | -61.12 / 50.29 = -1.22 | negative = 0 | 0 | 0 | PASS |
| B4 WC-days change | 204.96 → 217.62 = +12.66 | inc 5-15 = 1 | 1 | 1 | PASS |
| Block B | | | 3 | 3 | PASS |
| C1 Rev CAGR | 22.84% | ≥20 = 5 | 5 | 5 | PASS |
| C2 PAT CAGR | 69.1%, both endpoints +ve | ≥20 = 5 | 5 | 5 | PASS |
| C3 +YoY yrs | 100% | 100 = 5 | 5 | 5 | PASS |
| C4 PAT-Rev CAGR | +46.3pp | ≥+3pp = 5 | 5 | 5 | PASS |
| Block C | | | 20 | 20 | PASS |
| D1 ND/EBITDA | 1.72x | 1-2x = 3 | 3 | 3 | PASS |
| D2 Int coverage | 3.70x | 3-4.9 = 2 | 2 | 2 | PASS |
| D3 Debt/Equity | 0.55 | 0.5-1.0 = 3 | 3 | 3 | PASS |
| D4 Current ratio | 1.82 | 1.5-1.99 = 4 | 4 | 4 | PASS |
| Block D | | | 12 | 12 | PASS |
| E1 Promoter hold | 29.40%, not prof-managed | <30 = 0 | 0 | 0 | PASS |
| E2 Promoter change | +0.02pp (18-mo window) | ±1% = 3 | 3 | 3 | PASS |
| E3 Pledge | 0% | 0 = 5 | 5 | 5 | PASS |
| E4 Contingent/NW | 19.59% | 15-30 = 1 | 1 | 1 | PASS |
| Block E | | | 9 | 9 | PASS |

### Block F moat re-derivation

| Test | Rule applied | Score | Verdict |
|---|---|---|---|
| M1 Pricing | margin +4.3pp AND rev CAGR ≥10 | 5 | PASS |
| M2 Cost | PEER DATA NEEDED → 0 | 0 | PASS |
| M3 Cap eff | FAT 7.95x >3x AND ROCE 22.88 >20 | 5 | PASS |
| M4 Stickiness | 0 decline yrs, recv days not ±10 → mid band | 3 | PASS |
| M5 Scale | PEER DATA NEEDED → 0 | 0 | PASS |
| M6 R&D | not disclosed → 0 | 0 | PASS |
| M7 Reg/license | PEER DATA NEEDED → 0 | 0 | PASS |
| M8 Distribution | B2B, no network → 0 | 0 | PASS |
| M9 Brand | GM proxy, no peer median → 0 | 0 | PASS |
| M10 Switching | grew every yr but recv +128d → else 0 | 0 | PASS |
| M11 Network | latest3yr>prior3yr AND selling% declining | 5 | MINOR |
| M12 Neg WC | WC days >45 → 0 | 0 | PASS |
| Block F total | 5+0+5+3+0+0+0+0+0+0+5+0 | 18 | PASS |

M11 note (MINOR): the top band (5) requires BOTH "latest 3yr CAGR > prior 3yr"
AND "selling exp % declining." The CAGR leg holds (30.0% vs 16.16%). The
selling-% leg rests on FY20-FY25 only. The report states FY26 selling expense
is merged into Other Expenses and "not separately disclosed." Scoring the top
band asserts a condition whose latest year is unknown. Immaterial to the
outcome: moats present would drop 4→3 (STRONG→MODERATE) at most, and the final
classification is fixed at AVERAGE by the core score and deal-breaker 4
regardless of moat class. Flagged as an imprecision, not a decision error.

### Moat count, core, totals, classification

| Item | Claimed | Re-derived | Verdict |
|---|---|---|---|
| Moats present (≥3) | M1,M3,M4,M11 = 4 | 4 | PASS |
| Moat class (4-5 = STRONG) | STRONG | STRONG | PASS |
| Core score A+B+C+D+E | 58 | 14+3+20+12+9 = 58 | PASS |
| Grand total | 76 | 58+18 = 76 | PASS |
| Matrix (core 40-59 = AVERAGE) | AVERAGE | AVERAGE | PASS |

### Deal-breaker application

| # | Rule | Report ruling | Re-check | Verdict |
|---|---|---|---|---|
| 1 | Block A <8 → max GOOD | not triggered (14) | correct | PASS |
| 2 | Block B <8 → max GOOD | triggered (3) | correct | PASS |
| 3 | Median ROCE <10 → max AVG | not triggered (23.61) | correct | PASS |
| 4 | Cumul CFO/PAT <0.50 → max AVG | triggered (-0.50) | -0.50 < 0.50 = true | PASS |
| 5 | Pledge >15 → max AVG | not triggered (0) | correct | PASS |
| 6 | ND/EBITDA>3x AND IC<3x → AVOID | not triggered (1.72/3.70) | correct | PASS |
| 7 | Rev decline majority → max AVG | not triggered | correct | PASS |
| 8 | PAT -ve last 3 yrs → max AVG | not triggered | correct | PASS |
| 9 | History <3 yrs → AVERAGE | not triggered (7 yrs) | correct | PASS |

Deal-breaker 4 sits exactly at the boundary (-0.50). The strict inequality
"<0.50" is satisfied by any negative value, so the cap is correctly applied.
The report also correctly notes the cap would bind even if core cleared 60.
The "which years drive the deal-breaker" requirement is met in substance: Block
B lists CFO per year and names FY26 (-Rs32.30Cr) as the worst year.

### Confidence, history downgrade, CAGR edge rules, output

| Check | Rule | Verdict |
|---|---|---|
| Data confidence | 7 yrs → "7-9 moderate," no downgrade | PASS |
| history_downgrade | false | PASS |
| CAGR edge (C2) | both endpoints +ve, no loss-to-profit swing, no synthetic CAGR | PASS |
| Output format | end with the mandated fenced YAML block | FAIL (MINOR) |

Output note (MINOR): 01-gate0.md ends at "INPUT GAPS CARRIED FORWARD." It does
not contain the closing ```yaml B01-gate0 block the prompt OUTPUT section
mandates ("end with exactly this fenced YAML block"; CLAUDE.md WORDS: "done" =
report AND valid YAML). Every field value exists in the prose and B07 Section
6C evidently consumed them (core_score 58, moat_score 18). So the defect is
structural, not a content or math error. VOID this finding if the YAML block is
stored as a separate run artifact.

### Gate 0 verdict
Scoring math, threshold bands, moat count, core score, classification matrix,
deal-breaker application, and CAGR edge rules are all applied as written. Two
MINOR items: M11 top-band on an incomplete selling-% series, and the missing
closing YAML block. Neither changes the AVERAGE classification. No CRITICAL, no
MAJOR. I concur with the AVERAGE ruling.

═══════════════════════════════════════════════════════════════════
## PART 2 — EMERGING MOAT (B07) COMPLIANCE
═══════════════════════════════════════════════════════════════════

### 23-category completeness

All 22 categories plus R1 are addressed or explicitly marked NO EVIDENCE /
disconfirmed. Count = A1-A4, B1-B3, C1-C2, D1-D2, E1-E2, F1-F2, G1-G2, H1-H3,
I1-I2, R1 = 23 rows. No invented category. No missing category. PASS.

### Scorecard re-derivation (raw L×I, multiplier, adjusted)

| # | L×I | Raw check | Evid | Mult check | Adjusted claimed | Re-derived | Verdict |
|---|---|---|---|---|---|---|---|
| A1 | HH | 4 | 🎙️ | 0.7 | 2.8 | 2.8 | PASS |
| A3 | MM | 2 | 🎙️ | 0.7 | 1.4 | 1.4 | PASS |
| B2 | HH | 4 | 🎙️ | 0.7 | 2.8 | 2.8 | PASS |
| C1 | MM | 2 | 🎙️ | 0.7 | 1.4 | 1.4 | PASS |
| E2 | HH | 4 | 🎙️ | 0.7 | 2.8 | 2.8 | PASS |
| F2 | MM | 2 | 🔍 | 0.5 | 1.0 | 1.0 | PASS |
| G1 | HH | 4 | 📄 | 1.0 | 4.0 | 4.0 | PASS |
| H2 | HM | 3 | 🎙️ | 0.7 | 2.1 | 2.1 | PASS |
| I2 | MM | 2 | 🔍 | 0.5 | 1.0 | 1.0 | PASS (borderline) |
| R1 | HH | 4 | 🎙️ | 0.7 | 2.8 | 2.8 | PASS |
| Total | | | | | 22.1 | 22.1 | PASS |

Adjusted total re-summed = 22.1. Classification 22.1 → 12-24 band → MODEST MOAT
DEVELOPMENT. PASS. All 13 zero-evidence rows carry 0. Multipliers match tiers
exactly (📄 1.0, 🎙️ 0.7, 🔍 0.5).

### Evidence-tier discipline

The CORPUS NOTE scores every concall-only "achieved milestone" as 🎙️, not 📄,
because the announcements folder is absent. G1 is the sole 📄 row, anchored to
AR Note 11(v) and Note 35. No 🎙️-only category is scored as if 📄. This is the
exact discipline verifier rule 3 tests. PASS.

Completionist guard: active rows = 10 (above the 3-6 base rate, below the 12-row
mandatory-re-examination trigger). The 📄 recount is performed explicitly: "1
documented item (G1) across 1 category." PASS.

### I1 / I2 structural-asymmetry rules

| Check | Requirement | Report | Verdict |
|---|---|---|---|
| I1 above 0 | needs both legs, (b) leg ≥1 📄 | scored 0; part (a) disconfirmed by management | PASS |
| I2 above 0 | named sacrifice must be specific | named: mass-EMS must accept lower per-line throughput + higher validation overhead vs its high-volume cost structure | PASS (borderline) |
| I1/I2 contribution stated separately | operator ruling 20-Aug-2026 | "I1 = 0.0, I2 = 1.0," no threshold crossing via I-family | PASS |

I2 note (MINOR): I2 scores 1.0 on 🔍-only inference, and the report itself
concedes the sacrifice is "not proven-implausible." The framework warns that
where "nothing must be destroyed... execution leads close." The report does
name an internal cost-structure configuration (a listed valid example), and it
correctly keeps I2 out of the top band (top band needs a 📄 competitor source).
So the above-0 score is defensible by design, not a rule breach. Immaterial:
the MODEST classification holds at 21.1 without the entire I-family. Flag it for
the operator's post-10-15-scan I1/I2 review checkpoint, since it is exactly the
soft-evidence crossing that checkpoint exists to watch.

### Other B07 rules

| Check | Requirement | Verdict |
|---|---|---|
| 2C capex-embedded growth | capex × historical FAT, arithmetic shown, % over revenue | PASS (35.39 × 10.14 = 359 = +69%) |
| capex_embedded_growth_pct source | Method 1 (conservative), Method 2 cross-check only | PASS |
| Optionality register | table with all four mandated columns | PASS |
| Catalysts inventory | 12-month catalysts listed (6E) | PASS |
| No FTTCP conflation | header + 6D defer cash-conversion classification to Stage 11/FTTCP | PASS |
| F2 missing B05 input | gap declared, scored 🔍 by direct cross-call read | PASS |
| Output format | end with the mandated fenced YAML block | FAIL (MINOR) |

Output note (MINOR): 07-emoat.md ends at Section 6E. It does not contain the
closing ```yaml B07-emoat block the prompt mandates. Same structural defect as
Gate 0; content is complete in prose. VOID if the YAML is a separate artifact.

### Emerging Moat verdict
The 23-category scan is complete, multipliers and raw scores are applied as
written, evidence tiers are disciplined (only G1 clears 📄), the completionist
recount is done, and I1/I2 obey their gating rules with contribution stated
separately. Two MINOR items: the borderline I2 above-0 score (compliant by
design, flagged for the operator checkpoint) and the missing closing YAML block.
No CRITICAL, no MAJOR. I concur with MODEST MOAT DEVELOPMENT (22.1).

═══════════════════════════════════════════════════════════════════
## PART 3 — VALUATION (B11) — PENDING PHASE 3
═══════════════════════════════════════════════════════════════════
Not audited. Stages 10 and 11 do not exist in this run. The valuation framework
docs (Master v3.6, Section 1B layers, FTTCP v2.1) were deliberately not loaded;
they are dead context this phase. This section is reserved for the phase-3
valuation-adherence pass.

═══════════════════════════════════════════════════════════════════
## SUMMARY
═══════════════════════════════════════════════════════════════════
- Gate 0: fully compliant on math, caps, matrix, deal-breakers, CAGR edges.
  2 MINOR (M11 top-band on incomplete data; missing YAML block). Concur AVERAGE.
- Emerging Moat: fully compliant on 23-category completeness, multipliers,
  evidence tiers, I1/I2 gating. 2 MINOR (borderline I2 above-0; missing YAML
  block). Concur MODEST.
- No CRITICAL. No MAJOR. Acceptance rate (gate0+emoat scope) ~90%.
- Two of the four MINORs are the same systemic issue (no closing YAML in the
  .md artifact) and are VOID if the YAML lives in a separate run file.
