# VERIFIER C: FRAMEWORK ADHERENCE — MPS Ltd (MPSLTD)
Run date: 2026-09-03 | Model: claude-opus-4-8 | Scope: PHASE 1 (Gate 0 + Emerging Moat only)

Valuation adherence (B10/B11) is deferred to phase 3. Stages 10 and 11 do not
exist yet. The valuation section of the YAML block is marked pending. The
valuation framework docs (Master v3.6, Section 1B layers, FTTCP v2.1) were NOT
loaded; they are dead context in phase 1.

Audit method: rules re-derived from prompts/01-gate-0-pipeline.md and
prompts/07-emerging-moat-pipeline.md. Numbers were re-computed from the inputs
STATED IN the reports, not re-verified against source PDFs (source fidelity is
Verifier A's non-overridable gate; this audit tests rule application only).

---

## PART 1: GATE 0 (B01) COMPLIANCE

### 1.1 Block scores re-derived from stated inputs

| Rule | Stated inputs | Threshold applied | Recomputed | Report | Verdict |
|---|---|---|---|---|---|
| A1 median ROCE | sorted 10-yr, median avg(29.53,31.55)=30.54% | ≥25→5 | 5 | 5 | PASS |
| A2 min ROCE | FY20 21.67% | ≥15→5 | 5 | 5 | PASS |
| A3 median ROE | median avg(20.24,23.30)=21.77% | ≥20→5 | 5 | 5 | PASS |
| A4 ROCE trend | FY26 35.21 ≥ FY17 29.53 | latest≥earliest→5 | 5 | 5 | PASS |
| Block A total | | | 20 | 20 | PASS |
| B1 CFO/PAT | 971.43/972.30=0.999 | <1.00, 0.85-0.99→4 | 4 | 4 | PASS |
| B2 FCF+ years | capex N/A | N/A→0 | 0 | 0 | PASS |
| B3 cum FCF/PAT | capex N/A | N/A→0 | 0 | 0 | PASS |
| B4 WC days | payables N/A | N/A→0 | 0 | 0 | PASS |
| Block B total | | | 4 | 4 | PASS |
| C1 rev CAGR | (768.36/288.70)^(1/9)-1=11.49% | 10-14.9→3 | 3 | 3 | PASS |
| C2 PAT CAGR | (173.22/70.42)^(1/9)-1=10.52% | 10-14.9→3 | 3 | 3 | PASS |
| C3 pos YoY | 7/9=77.8% | 75-99→3 | 3 | 3 | PASS |
| C4 PAT−Rev CAGR | 10.52−11.49=−0.97pp | ±3pp→3 | 3 | 3 | PASS |
| Block C total | | | 12 | 12 | PASS |
| D1 ND/EBITDA | 60.63−94.55=−33.92 net cash | net cash→5 | 5 | 5 | PASS |
| D2 int cover | 231.30/2.01=115.1x | ≥10→5 | 5 | 5 | PASS |
| D3 D/E | 60.63/596.33=0.102 | 0.1-0.5→4 | 4 | 4 | PASS |
| D4 current ratio | 19305/7645=2.525x (standalone) | ≥2.0→5 | 5 | 5 | PASS |
| Block D total | | | 19 | 19 | PASS |
| E1-E4 | all N/A (no shareholding/CL file) | N/A→0 each | 0 | 0 | PASS |
| Block E total | | | 0 | 0 | PASS |
| CORE | A20+B4+C12+D19+E0 | sum | 55 | 55 | PASS |

### 1.2 Moat tests (Block F)

| Test | Stated inputs | Threshold | Recomputed | Report | Verdict |
|---|---|---|---|---|---|
| M1 pricing power | margin −1.66pp (±2pp) + rev CAGR 11.49%≥10% | stable+≥10→3 | 3 | 3 | PASS |
| M2 cost adv | peer data absent | PEER DATA NEEDED→0 | 0 | 0 | PASS |
| M3 cap efficiency | FAT 1.42x, ROCE 35.21% | FAT>1x+ROCE>12→1 | 1 | 1 | PASS |
| M4 stickiness | 2 decline yrs, CAGR+ | 2 decline→1 | 1 | 1 | PASS |
| M5 scale | peer data absent | PEER DATA NEEDED→0 | 0 | 0 | PASS |
| M6 tech/R&D | no R&D line | N/A→0 | 0 | 0 | PASS |
| M7 reg/license | unregulated | unregulated→0 | 0 | 0 | PASS |
| M8 distribution | no reach metric | none/digital→0 | 0 | 0 | PASS |
| M9 brand | no RM line, no peer GM | N/A→0 | 0 | 0 | PASS |
| M10 switching | 2 decline yrs, growth | 2 decline→1 | 1 | 1 | PASS |
| M11 network | latest 3yr 15.31%>prior 14.74%, selling% rising | >15% + selling rising→1 | 1 | 1 | PASS |
| M12 neg WC | payables N/A | N/A→0 | 0 | 0 | PASS |
| Moat total | | | 7 | 7 | PASS |
| Moat class | M1 only present (≥3) | 1 present→THIN | THIN | THIN | PASS |

M11 two-window recompute confirmed: FY23→FY26 = (768.36/501.05)^(1/3)-1 =
15.31%; FY20→FY23 = (501.05/331.65)^(1/3)-1 = 14.74%. Latest > prior, but
selling%-of-sales rose to 7.71% in FY26 → score 1 is correct (the "rev CAGR
>15% but selling % rising" cell), not the 5-cell (which needs selling %
declining) and not the 3-cell (which needs CAGR ≥20%).

### 1.3 Classification, confidence, deal-breakers

| Check | Rule | Report | Verdict |
|---|---|---|---|
| Data confidence | 10 yrs → full, no downgrade | full, no downgrade | PASS |
| Classification | Core 55 in 40-59 → AVERAGE (moat-independent in this band) | AVERAGE | PASS |
| Uses core not grand total | matrix keys off Core (55), not grand total (62) | used 55 | PASS |
| DB1 Block A<8 | A=20, not fired | not fired | PASS |
| DB2 Block B<8 | B=4 FIRED → cap GOOD; no effect below AVERAGE | fired, noted no net effect | PASS |
| DB3 median ROCE<10 | 30.54%, not fired | not fired | PASS |
| DB4 CFO/PAT<0.50 | 0.999, not fired | not fired | PASS |
| DB5 pledge>15% | N/A, cannot assess, flagged open for Halt 1 | flagged open | PASS |
| DB6 ND/EBITDA>3x & IC<3x | net cash, not fired | not fired | PASS |
| DB7 rev decline majority | 2/9=22%, not fired | not fired | PASS |
| DB8 PAT neg last 3yr | all positive, not fired | not fired | PASS |
| DB9 history<3yr | 10 yrs, not fired | not fired | PASS |
| Which-years disclosure | DB2 driven by B2/B3/B4 data gaps, stated | stated | PASS |
| CAGR edge rules | no negative/zero endpoints; no loss-to-profit swing | not triggered, correct | PASS |

Deal-breaker cap logic is correct: Block B<8 caps at GOOD, and the matrix
result (AVERAGE) already sits below GOOD, so the cap has no net effect. The
report states this explicitly.

### 1.4 Gate 0 minor observations (non-decision-changing)

- MINOR — ROCE computed with Capital Employed = Net Worth + Borrowings, a
  documented substitution for the fixed formula's Total Assets − Current
  Liabilities, because the compressed screener "Other Liabilities" bucket
  could not be split. The substitution excludes non-current liabilities and
  would if anything slightly overstate ROCE, but every ROCE score sits far
  inside its band (median 30.54% vs the 25% cut; min 21.67% vs the 15% cut),
  so no score could flip. Faithful data-gap handling, disclosed as "computed."
  Not a fail; recorded for the record.
- MINOR — the report file ends at the input_gaps prose summary and does not
  contain the mandated terminal fenced YAML block. The B01 block was clearly
  injected into B07 (which cites core 55, moat 1, THIN, AVERAGE verbatim), so
  the block existed at hand-off; this is a report-file completeness gap, not a
  scoring error.

Gate 0 verdict: every scorecard rule, moat test, deal-breaker, the
classification matrix, the confidence tier, and the CAGR edge rules were
applied AS WRITTEN. No CRITICAL, no MAJOR. Two MINOR observations.

---

## PART 2: EMERGING MOAT (B07) COMPLIANCE

### 2.1 Coverage and structure

| Check | Rule | Report | Verdict |
|---|---|---|---|
| All 23 categories addressed | 22 scan + R1, each scored or NO EVIDENCE | A1-I2 (22) + R1 all present | PASS |
| I1 present (Category 21) | must appear | present | PASS |
| I2 present (Category 22) | must appear | present | PASS |
| Completionist recount performed | explicit 📄 recount line | "14 documented items across 7 categories" stated | PASS |
| I1/I2 contribution stated separately | operator ruling 20-Aug-2026 | "I1/I2 contribution: 0 of 24.4" stated | PASS |

### 2.2 Rule-8 structural-asymmetry gates

| Check | Rule | Report | Verdict |
|---|---|---|---|
| I1 scored >0 only if both legs, (b) leg ≥1 📄 | both legs fail: no named inventors/pedigree (a), no competitor-economics arithmetic (b) | scored 0 | PASS |
| I2 scored >0 only if named specific sacrifice | honest answer "nothing must be destroyed"; relationship/switching = execution lead, disqualified | scored 0 | PASS |

Both I1 and I2 correctly resolved to 0 with the framework's own disqualifying
language cited ("a hiring story, scored 0"; "execution leads close"). This is
the intended default for a company whose stated defense is relationship tenure
and switching cost.

### 2.3 Scorecard multipliers re-derived

| # | L×I raw | Evidence tier claimed | Multiplier rule | Recomputed | Report | Verdict |
|---|---|---|---|---|---|---|
| A3 | 1 (LM) | 🎙️ | 0.7 | 0.7 | 0.7 | PASS |
| A4 | 3 (HM) | 🎙️ blended (conservative) | 0.7 | 2.1 | 2.1 | PASS |
| C1 | 4 (HH) | 📄 | 1.0 | 4.0 | 4.0 | PASS |
| C2 | 2 (MM) | 🎙️ | 0.7 | 1.4 | 1.4 | PASS |
| D1 | 3 (HM) | 📄 | 1.0 | 3.0 | 3.0 | PASS |
| F1 | 3 (HM) | 📄 | 1.0 | 3.0 | 3.0 | PASS |
| F2 | 2 (MM) | 📄 | 1.0 | 2.0 | 2.0 | PASS |
| G1 | 3 (HM) | 🎙️ blended (conservative) | 0.7 | 2.1 | 2.1 | PASS |
| H1 | 4 (HH) | 📄 | 1.0 | 4.0 | 4.0 | PASS |
| H2 | 3 (MH) | 🎙️ (unnamed counterparty caps) | 0.7 | 2.1 | 2.1 | PASS |
| Adjusted total | | | | 24.4 | 24.4 | PASS |

Sum of active rows: 0.7+2.1+4.0+1.4+3.0+3.0+2.0+2.1+4.0+2.1 = 24.4. All
zero-scored categories (A1, A2, B1, B2, B3, D2, E1, E2, G2, H3, I1, I2, R1)
carry 0 correctly.

### 2.4 Evidence-tier consistency (rule 3: no 🎙️-only category scoring as 📄)

Every category scored at the 1.0 (📄) multiplier has a genuine documented
anchor: C1 (five-year platform partnership + 1,100+ customers, filed AR), D1
(1M+ expert edits, 1M+ manuscripts, filed AR), F1 (200+ AI engineers, disclosed
twice in the filed AR), F2 (ROCE 38.2% + EBITDA trajectory, filed AR + B05
delivery record), H1 (SPA dates, secretarial-audit-confirmed completions). No
management-claim-only category was inflated to the documented tier. A4 and G1,
which blend documented facts with claim-grade impact narrative, were scored at
the conservative 0.7 tier, not the 1.0 tier. Consistent with the taxonomy.

### 2.5 Classification and combined assessment

| Check | Rule | Report | Verdict |
|---|---|---|---|
| Band | 24.4 < 25 → 12-24 MODEST | MODEST | PASS |
| em_score in YAML | rounds 24.4 | 24 | PASS |
| Completionist guard | 12+ triggers recount; active count below 12 | recount performed anyway; count below trigger | PASS |
| 📄 recount arithmetic | C1:2+D1:2+A4:2+F1:1+F2:2+G1:2+H1:3 = 14 / 7 cats | 14/7 stated, adds up | PASS |
| Combined (6D) | AVERAGE/THIN backward + MODEST forward, no upgrade to transition setup (needs STRENGTHENING/EXPANSION forward) | AVERAGE, reasoned | PASS |
| capex_embedded_growth_pct | asset-light, set 0 with explanation, not estimated | 0 + explanation | PASS |

### 2.6 Emerging Moat minor finding

- MINOR — active-category count inconsistency. Section 3 states "Count with
  Strong/Moderate evidence: 8 categories" but then enumerates NINE distinct
  categories (C1, C2, D1, A4, F1, F2, G1, H1, H2) and the YAML
  active_categories list carries all nine. The parenthetical rationale ("9
  listed rows because D1 straddles Moderate/Strong; treated as one category")
  does not reconcile: D1 is one category listed once, so nine distinct
  categories are genuinely active, not eight. No threshold effect — both 8 and
  9 sit below the 12+ completionist-guard trigger and above the 3-6 base rate,
  so the report's conclusion ("elevated but not guard-tripping, driven by a
  document-rich AR") stands unchanged. Presentational count error only.

Emerging Moat verdict: taxonomy, multipliers, the completionist recount, the
23-category coverage, the I1/I2 rule-8 gates, and the classification band were
all applied AS WRITTEN. No CRITICAL, no MAJOR. One MINOR count inconsistency.

---

## PART 3: VALUATION (B11) — PENDING PHASE 3

Not audited. Stages 10 and 11 do not exist in this run yet. The valuation
framework docs were not loaded. This section runs in phase 3 when B10/B11 are
among the inputs.

The following B12c rules are also out of phase-1 scope and not evaluated here:
Business Understanding Narrative (stage 13), Halt 1 dossier structural check
(fires at /finalize), downstream-candidate block (stage 9), method plurality
(stage 11), Role 1 exit/FV-path construction (stage 11).

---

## SUMMARY

- Gate 0 (B01): all rules applied as written. 0 CRITICAL, 0 MAJOR, 2 MINOR.
- Emerging Moat (B07): all rules applied as written. 0 CRITICAL, 0 MAJOR, 1 MINOR.
- No finding changes a score, a classification, or a decision.
- Verifier C concurs with Gate 0 AVERAGE / THIN and Emerging Moat MODEST.
- Valuation adherence deferred to phase 3.
