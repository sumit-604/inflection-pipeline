# B12c — VERIFIER C: FRAMEWORK ADHERENCE (DSSL, 2026-07-27)

Model: claude-opus-4-8 | Scope: PHASE 1 ONLY — Gate 0 (B01) + Emerging Moat (B07).
Valuation adherence (B10/B11) DEFERRED to phase 3; B10/B11 do not exist yet.

Authority consulted: prompts/01-gate-0-pipeline.md (scoring bands, formula
definitions, CAGR edge rules, classification matrix, deal-breakers),
prompts/07-emerging-moat-pipeline.md (evidence taxonomy, 21-category scan,
scorecard multipliers, completionist guard, combined-assessment labels),
frameworks/Master_Project_Prompt_v3.3.md (combined rating, Amendment-3 UA
qualifier at line 332), frameworks/Section_1B_v3.3_Amendments.md (spot).

I audit RULE APPLICATION, not raw source fidelity (Verifier A owns numbers)
and not company quality. Where I re-derive a score I use the maker's own
stated inputs against the framework's stated thresholds.

═══════════════════════════════════════════════════════════════════
## PART 1 — GATE 0 (B01) COMPLIANCE
═══════════════════════════════════════════════════════════════════

Data window: 10 years FY17–FY26. Confidence tier "10+ yrs full" → no
confidence downgrade. **history_downgrade = FALSE — CORRECT.** The rule
(prompt 01, line 144-145) reserves the one-tier downgrade for the 3-4yr
LIMITED tier only; DSSL has a full 10-year history, so it cannot apply. The
report states this explicitly (B01 line 5, line 174) and, critically, does
NOT conflate it with any transition/recovery depressor: the only depressor
acting on DSSL is the mechanical Block B < 8 cash-conversion deal-breaker
(deal-breaker 2), which is kept entirely separate from the history tier.
No conflation found. PASS.

### Block-by-block re-derivation (maker inputs vs framework bands)

| Item | Maker input | Band applied | Re-derived | Verdict |
|---|---|---|---|---|
| A1 Median ROCE | 20.38% (median of 10 yrs) | 20-24.9 → 4 | median(sorted)=(18.61+22.15)/2=20.38 → 4 | PASS |
| A2 Min ROCE | 10.14% (FY17) | 8-11.9 → 1 | 1 | PASS |
| A3 Median ROE | 23.84% | ≥20 → 5 | median=(19.72+27.96)/2=23.84 → 5 | PASS |
| A4 ROCE trend | FY26 30.17 ≥ FY17 10.14 | latest≥earliest → 5 | 5 | PASS |
| **Block A** | | **15** | 4+1+5+5=15 | PASS |
| B1 CFO/PAT | 150.09/283.57=0.529 | 0.50-0.69 → 1 | 0.5293 → 1 | PASS |
| B2 FCF+ years | 7/10=70% | 50-74 → 2 | 2 | PASS |
| B3 FCF/PAT | 73.60/283.57=0.260 | 0.20-0.39 → 1 | 0.2596 → 1 | PASS |
| B4 ΔWC days | N/A (payables gap) | scored 0 | grounded-claims: N/A→0 | PASS |
| **Block B** | | **4** | 1+2+1+0=4 → DB-2 fires | PASS |
| C1 Rev CAGR 9yr | 27.65% | ≥20 → 5 | (1424.28/158.29)^(1/9)-1=27.65% → 5 | PASS |
| C2 PAT CAGR 9yr | 60.34% | ≥20 → 5 | (84.74/1.21)^(1/9)-1=60.3% → 5 | PASS |
| C3 +YoY rev yrs | 9/9=100% | 100 → 5 | 5 | PASS |
| C4 PAT−Rev CAGR | +32.69pp | ≥+3 → 5 | 5 | PASS |
| **Block C** | | **20** | 20 | PASS |
| D1 ND/EBITDA | (236.54-111.51)/145.92=0.857x | 0-1.0 → 4 | 4 | PASS |
| D2 Int coverage | 131.39/23.20=5.66x | 5-9.9 → 4 | 4 | PASS |
| D3 Debt/Equity | 236.54/315.08=0.75x | 0.5-1.0 → 3 | 3 | PASS |
| D4 Current ratio | 777.87/577.52=1.35x | 1.2-1.49 → 2 | 2 | PASS |
| **Block D** | | **13** | 13 | PASS |
| E1 Promoter hold | 60.89% (Jun-26) | ≥60 → 5 | 5 | PASS |
| E2 Prom Δ | −0.21pp (~2.75yr) | ±1% → 3 | 3 | PASS (window note below) |
| E3 Pledge | NOT FOUND | N/A → 0 | grounded-claims: N/A→0 | PASS |
| E4 CL/NW | 146.55/230.92=63.47% | >30 → 0 | 0 | PASS |
| **Block E** | | **8** | 8 | PASS |

**CAGR edge rules (prompt 01, lines 44-52):** both C1 and C2 endpoints
strictly positive (FY17 PAT 1.21 > 0, revenue 158.29 > 0) → no "N/M
(negative endpoint)" trigger, no loss-to-profit swing, C4 computed normally.
CORRECT.

### Moat block (F), M1–M12 (0-5 each)

| Test | Maker | Framework literal | Verdict |
|---|---|---|---|
| M1 Pricing power | 5 | margin +7.26pp (≥2) AND rev CAGR 27.65% (≥10) → 5 | PASS |
| M2 Cost adv | 0 | peer data needed → 0 | PASS |
| M3 Capital eff | 5 | FAT 9.02x (>3) AND ROCE 30.17% (>20) → 5 | PASS |
| M4 Cust sticky | 3 | see note below | PASS (borderline) |
| M5 Scale | 0 | peer data needed → 0 | PASS |
| M6 Tech/R&D | 0 | no R&D line → 0 | PASS |
| M7 Regulatory | 0 | unregulated/fragmented → 0 | PASS |
| M8 Distribution | 1 | reach quantified, growth unconfirmed → "mentioned"=1 | PASS |
| M9 Brand | 0 | peer median needed (GM proxy own-trend only) → 0 | PASS |
| M10 Switching | 0 | tiers require "2+ decline yrs" or stable rec days; neither met → 0 | PASS |
| M11 Network | 3 | latest 3yr 20.98% (≥20) AND S&A% declining → 3 (not 5: 20.98<34.75 prior) | PASS |
| M12 Neg WC | 1 | FY25 28.6d / FY26 44.1d both 15-45 band → 1 | PASS |
| **Block F** | **18** | 5+0+5+3+0+0+0+1+0+0+3+1=18 | PASS |

**M4 borderline (advisory MINOR, not a fail).** Tier 5 (zero decline AND
receivable days stable ±10) correctly REJECTED — receivable days blew out
67.9d→154.3d (+86.4d), so the maker did NOT over-award. Tier 3 ("max 1
decline year, fully recovered") is satisfied on a literal reading because
0 decline years trivially meets "max 1". The score is defensible; note only
that M4 and M10 apply the SAME underlying facts (0 declines, rising
receivables) yet score 3 vs 0 — this is not an inconsistency, it is each
rubric's literal tier-wording (M4's lowest positive tier keys on "max 1
decline", M10's on "2+ declines" with no vacuous-satisfaction path). Both
readings are internally faithful. **Destination-insensitive:** even if M4
were downgraded below 3, moat count falls 4→3, moat_class STRONG→MODERATE,
but final classification is already capped at GOOD by deal-breaker 2, so the
Gate 0 output does not move.

**Moat classification:** 4 moats present (M1, M3, M4, M11, each ≥3) → 4-5
band = STRONG. CORRECT.

### Structural checks

- Core score = A15+B4+C20+D13+E8 = **60**. CORRECT.
- Grand total = Core 60 + Moat 18 = **78/160**. CORRECT.
- Classification matrix: Core 60-79 + STRONG → **GOOD+**, then deal-breaker 2
  (Block B < 8) caps at max GOOD → **final GOOD**. CORRECT (prompt 01 lines
  149, 156).
- Deal-breaker sweep (all 9): DB1 Block A 15 (no); DB2 Block B 4 <8 (YES →
  cap GOOD, driving years FY18/FY22 CFO-neg + FY26 FCF-neg correctly named);
  DB3 median ROCE 20.38% (no); DB4 CFO/PAT 0.529 ≥0.50 (no — near-miss
  correctly NOT triggered, absence of rounding down); DB5 pledge >15%
  (UNKNOWN → correctly NOT triggered, absence-of-evidence ≠ breach); DB6
  ND/EBITDA 0.857x & IC 5.66x (no); DB7 rev decline majority 0/9 (no); DB8
  PAT neg last 3yr (no); DB9 history <3yr (no). ALL CORRECT.

### Flags emitted by B01 — framework-consistency assessment

The prompt template only pre-names FLAG-GATE0 (required when classification
≤ AVERAGE with historical depressors). DSSL is GOOD, so FLAG-GATE0 is
correctly NOT required. The three flags actually emitted are additive
propagation, consistent with CLAUDE.md ("Flags propagate; only mechanical
failures halt") and the INDETERMINATE-cash-conversion caveat rule:

- **FLAG-CASH** — framework-consistent. Directly reflects deal-breaker 2
  (Block B 4/20) plus the FY26 FCF −Rs18.87cr / CFO −30.1% YoY facts. This
  is precisely the "cash conversion caps at PROCEED WITH CAVEATS" doctrine.
- **FLAG-DATA-GAP** — framework-consistent. Pledge (E3) NOT FOUND, scored 0
  per grounded-claims, correctly NOT read as confirmed 0% or >15%.
- **FLAG-STALE** — framework-consistent. E4 on FY25 AR (FY26 AR unpublished),
  ~16 months stale, correctly disclosed as latest-available.

### Gate 0 — one adherence deviation (MINOR, immaterial to destination)

**ROCE source-preference (formula rule, prompt 01 lines 29-31).** The rule
says "If the data source provides its own ROCE (screener.in does), use the
source's figure … compute only when absent." The maker COMPUTED ROCE for all
10 years on a hybrid CE basis (Net Worth + Borrowings proxy for FY17-24;
Total Assets − Current Liabilities for FY25-26) rather than lifting
screener's own ROCE column. The deviation is (a) documented and justified by
a genuine data limitation (screener Data_Sheet does not split current vs
non-current liabilities pre-FY25, so the precise formula is uncomputable for
those years) and (b) cross-validated against Acuité (FY25 gearing 0.60x exact
match). A1 median lands at 20.38%, 0.38pp inside the 20-24.9 band, so even a
small shift toward a source-supplied series is unlikely to move A1, and the
final classification is capped at GOOD regardless. Logged as MINOR: prefer
the source ROCE per the literal rule, but no CRITICAL/MAJOR consequence.

**Gate 0 verdict: fully compliant. Classification GOOD stands. 0 CRITICAL,
0 MAJOR, 1 MINOR advisory (ROCE source-preference), plus 1 borderline PASS
noted (M4).**

═══════════════════════════════════════════════════════════════════
## PART 2 — EMERGING MOAT (B07) COMPLIANCE
═══════════════════════════════════════════════════════════════════

### Coverage & taxonomy

- **All 21 categories addressed** (A1-A4, B1-B3, C1-C2, D1-D2, E1-E2, F1-F2,
  G1-G2, H1-H3, R1). 14 rows explicitly NO EVIDENCE FOUND, 7 scored. No
  category silently dropped. CORRECT (prompt 07 line 111).
- **NOT conflated with FTTCP.** Scope note (B07 line 4) and prompt 07 lines
  3-6 both firewall this scan from FTTCP; no FTTCP scoring appears anywhere
  in B07. CORRECT.

### Scorecard multiplier re-derivation (raw L×I × evidence multiplier)

Matrix: HH=4, HM/MH=3, HL/MM/LH=2, ML/LM=1, LL=1, none=0. Multipliers
📄 1.0 / 🎙️ 0.7 / 🔍 0.5.

| ID | Raw | Type | Mult | Maker adj | Re-derived | Verdict |
|---|---|---|---|---|---|---|
| B1 | 1 (ML) | 🎙️ | 0.7 | 0.7 | 0.7 | PASS |
| B2 | 4 (HH) | 📄 | 1.0 | 4.0 | 4.0 | PASS |
| C1 | 3 (HM) | 📄 | 1.0 | 3.0 | 3.0 | PASS |
| E1 | 1 (LL) | 📄 | 1.0 | 1.0 | 1.0 | PASS |
| F1 | 1 (ML) | 📄 | 1.0 | 1.0 | 1.0 | PASS |
| F2 | 3 (HM) | 📄 | 1.0 | 3.0 | 3.0 | PASS |
| G2 | 3 (HM) | 📄 | 1.0 | 3.0 | 3.0 | PASS |
| H2 | 3 (HM) | 📄 | 1.0 | 3.0 | 3.0 | PASS |
| H3 | 1 (LL) | 📄 | 1.0 | 1.0 | 1.0 | PASS |
| R1 | 3 (HM) | 📄 | 1.0 | 3.0 | 3.0 | PASS |
| (14 others) | 0 | — | — | 0.0 | 0.0 | PASS |

**em_score = 0.7+4.0+3.0+1.0+1.0+3.0+3.0+3.0+1.0+3.0 = 22.7. CORRECT.**
Band 12-24 → **MODEST MOAT DEVELOPMENT. CORRECT** (prompt 07 line 132).

**Evidence-tier discipline (the key Verifier-C EM check — no 🎙️-only
category scored as if 📄):** the only single-🎙️ category, B1, correctly
carries the 0.7x multiplier. Every category taking the 1.0x multiplier has a
genuine documented anchor driving the score — C1 (revenue-mix disclosure
Inv.Pres. p.16-17), F2 (project completions + FY26 audited results), G2
(NWC/net-debt chart data), R1 (signed RBI/NABARD government contracts) — even
where the narrative is mixed 📄+🎙️. No inflation of a claim-only category to
documented. PASS.

### Completionist guard

Report states "📄 recount performed: 11 documented items across 5 non-R1
categories … plus R1's signed government contracts; 6 of 21 rows
Strong/Moderate, within the 3-6 base rate; 14 rows left NO EVIDENCE FOUND
rather than force-fit." The recount is explicitly performed and the active
count (6) sits inside the stated 3-6 realistic base rate (prompt 07 lines
33-35, 111). Well below the 12-category over-credit tripwire. PASS.

### Combined assessment (6C/6D) & mapping to Gate 0

- 6C table faithfully carries the INJECTED B01 block: core 60/100, blocks
  A15/B4/C20/D13/E8, grand 78/160, 4 confirmed moats STRONG, classification
  GOOD. CORRECT — matches B01 exactly.
- 6D combined = **GOOD+**. Gate 0 GOOD (backward) + MODEST emerging (forward).
  The prompt supplies the label SET (EXCEPTIONAL/EXCELLENT+/HIGH POTENTIAL/
  GOOD+/GOOD/TURNAROUND/AVERAGE/AVOID) but not enumerated cells; HIGH
  POTENTIAL is reserved for GOOD/AVERAGE-backward + EXPANSION-forward, which
  MODEST does not reach, so the maker correctly did NOT claim HIGH POTENTIAL.
  Lifting GOOD→GOOD+ on a MODEST (not even STRENGTHENING) forward read is a
  half-tier, watch-and-confirm call; it is well-reasoned and defensible, on
  the generous edge of latitude. Advisory MINOR — within judgment tolerance,
  no enumerated cell is violated.

### FLAG-METHOD (capex_embedded_growth_pct = 0) — framework consistency

The Section 2C requirement is "total capex under execution × historical
fixed-asset turnover = implied incremental revenue; show the arithmetic"
(prompt 07 lines 50-52). The maker **DID show the arithmetic** (Rs148cr ×
193x ≈ Rs28,564cr, ~2,006% above revenue), then judged the historical FAT
(193x) a non-applicable artefact of the pre-FY25 capex-light EPC/reseller
model and set the YAML field to 0, substituting an order-book cross-check
(Rs2,964cr / Rs1,424cr ≈ +108%) reported in the body.

Assessment: **framework-consistent judgment, with one downstream caveat.**
The 2C formula genuinely breaks for an asset-light-legacy → capex-heavy
transition (193x FAT is an artefact, not a base rate), so discarding the
2,006% figure is sound, and the arithmetic-shown requirement was honoured.
CLAUDE.md's "never estimate a missing number" is respected — 0 is a
deliberate not-populated sentinel, not an estimate, and the flag names the
mismatch loudly. **Caveat (advisory MINOR):** capex_embedded_growth_pct feeds
Pillar 3 downstream (phase 3); a bare 0 could be mis-read as "no embedded
growth" when the body clearly evidences ~+108% order-book-implied growth.
Recommend phase-3 valuation read the FLAG-METHOD note / the 108% cross-check
rather than the literal 0. Not a fail — the maker did exactly what the
"don't force a misleading number" instinct requires and documented it.

### FLAG-CASH-LINK — framework consistency

Flags that the FY26 capex/lease build generating the strongest emerging
evidence (C1, F2, G2, H2) is the SAME build tripping B01's FLAG-CASH. This is
the correct application of "never credit one quality improvement through two
mechanisms" (CLAUDE.md): the maker explicitly refuses to treat the emerging
moat and the backward cash flag as two independent facts (6C note, 6E). It
also correctly separates backward M11 (network effects, already credited in
B01) from forward B3 (NO EVIDENCE of a NEW/expanding network effect), avoiding
double-count. Framework-consistent. PASS.

### Other EM structural checks

- evidence_mix {documented:15, claim:11, inference:4} — item-count field,
  plausible against the body; not a rule threshold. Noted, not audited for
  exactness (that is item-tally, near Verifier-A territory).
- optionality_register present, 6 rows, each with converting-evidence /
  first-appears / window per prompt 07 lines 134-147. PASS.
- catalysts_12m populated with anchors and evidence types, feeding Pillar 3
  catalyst proximity. The digest-only Central Bank of India order is
  correctly quarantined as "operator digest only … NOT independently
  verified." PASS.
- Amendment-3 UA qualifier pre-work (Master v3.3 line 332): B01 notes FII+DII
  ~1.36% <3% and Gate 0 core ≥60 — both UA qualifiers evidenced for the
  phase-3 valuation to consume. Correctly staged, not scored here. Noted.

**Emerging Moat verdict: fully compliant. em_score 22.7 / MODEST and combined
GOOD+ stand. 0 CRITICAL, 0 MAJOR. FLAG-METHOD and FLAG-CASH-LINK are both
framework-consistent judgments; 2 advisory MINORs (capex-field downstream
read-through; GOOD+ on the generous edge).**

═══════════════════════════════════════════════════════════════════
## PART 3 — VALUATION (B10/B11): DEFERRED
═══════════════════════════════════════════════════════════════════

Out of phase-1 scope. B10 and B11 do not exist yet; the continuous Pillar 1
formula, FTTCP ROCE authority, single-credit routing, Pillar 2 multiplier /
offset rules, Pillar 3 EM-catalyst inputs, Amendment-3 UA ordering, dual-track
carry, Hurdle Ratio, 4D weights and SOM cross-check audits are ALL deferred to
phase 3. No valuation rule was checked. valuation: {status: pending-phase-3}.

═══════════════════════════════════════════════════════════════════
## SUMMARY
═══════════════════════════════════════════════════════════════════

No CRITICAL or MAJOR framework misapplications in either in-scope stage. Gate 0
re-derives cleanly to GOOD (grand total 78/160) with every band, the CAGR
edge rules, the classification matrix, the deal-breaker sweep and
history_downgrade=FALSE applied as written and with no history/transition
conflation. Emerging Moat re-derives cleanly to 22.7 / MODEST with correct
multipliers, an honest completionist recount, disciplined evidence tiers, and
no FTTCP conflation. All five flags in question (FLAG-CASH, FLAG-DATA-GAP,
FLAG-STALE, FLAG-METHOD, FLAG-CASH-LINK) are framework-consistent judgments.
Findings are limited to advisory MINORs that do not move any classification or
decision.

recomputed_destination_pe: (n/a — deferred to phase 3)
recomputed_decision: (blank — concur; Gate 0 GOOD and combined GOOD+ stand)

```yaml
stage: B12c
company: "DSSL"
run_date: "2026-07-27"
model: claude-opus-4-8
status: complete
scope: "phase-1 (gate0 + emerging-moat only); valuation deferred to phase-3"
gate0:
  rules_checked: 39
  fails:
    - {severity: "MINOR", rule: "ROCE source-preference (prompt-01 formula: use screener's own ROCE if provided, compute only when absent)", detail: "ROCE computed on a hybrid CE basis for all 10yr (NW+Borrowings proxy FY17-24; TotalAssets-CurrentLiab FY25-26) rather than lifting screener's own ROCE; documented and justified by missing current/non-current liability split pre-FY25, cross-validated vs Acuite. A1 median 20.38% sits 0.38pp inside the 20-24.9 band; classification capped at GOOD regardless — no destination impact."}
emoat:
  rules_checked: 29
  fails: []
valuation: {status: pending-phase-3}
recomputed_destination_pe: ""
recomputed_decision: ""
findings:
  - {severity: "MINOR", stage: "B01", location: "Block A ROCE derivation", note: "Framework prefers source-supplied ROCE; maker computed hybrid CE. Documented, cross-validated, immaterial to GOOD classification. Prefer source series per literal rule."}
  - {severity: "MINOR", stage: "B01", location: "M4 Customer Stickiness = 3", note: "Borderline PASS. Tier-5 correctly rejected (receivable days 67.9d->154.3d not stable). Tier-3 satisfied on literal 'max 1 decline year' (0 declines). Destination-insensitive: even a downgrade keeps final class GOOD (capped by DB-2). Same facts score M10=0 due to M10's differently-worded tiers — internally faithful, not inconsistent."}
  - {severity: "MINOR", stage: "B07", location: "capex_embedded_growth_pct = 0 (FLAG-METHOD)", note: "Framework-consistent: 2C arithmetic was shown (~2,006% via 193x artefact FAT), correctly judged non-applicable for asset-light-legacy->capex-heavy transition, order-book cross-check (~+108%) substituted in body. Caveat: field feeds phase-3 Pillar 3; a bare 0 can be mis-read as no embedded growth. Phase-3 must read the FLAG-METHOD note / 108% figure, not the literal 0."}
  - {severity: "MINOR", stage: "B07", location: "6D combined assessment = GOOD+", note: "GOOD-backward + MODEST-forward lifted a half-tier to GOOD+. HIGH POTENTIAL correctly NOT claimed (reserved for EXPANSION forward). Well-reasoned, on the generous edge of latitude; no enumerated matrix cell violated."}
gate0_flags_assessed:
  - {flag: "FLAG-CASH", verdict: "framework-consistent — reflects deal-breaker 2 (Block B 4/20) + FY26 FCF -18.87cr; aligns with INDETERMINATE-cash caveat doctrine"}
  - {flag: "FLAG-DATA-GAP", verdict: "framework-consistent — E3 pledge NOT FOUND scored 0 per grounded-claims, not read as 0% or >15%"}
  - {flag: "FLAG-STALE", verdict: "framework-consistent — E4 on FY25 AR (FY26 AR unpublished), disclosed as latest-available"}
emoat_flags_assessed:
  - {flag: "FLAG-METHOD", verdict: "framework-consistent judgment — arithmetic shown as required, 2C formula genuinely mismatched for this business model, order-book cross-check substituted; downstream read-through caveat noted (MINOR)"}
  - {flag: "FLAG-CASH-LINK", verdict: "framework-consistent — correct application of one-improvement-one-mechanism; refuses to double-count the FY26 capex as both backward flag and independent forward moat"}
history_downgrade_check: "CORRECT — history_downgrade=FALSE; 10yr history, LIMITED-tier rule inapplicable; NOT conflated with the Block B cash deal-breaker (the sole depressor)"
fttcp_conflation_check: "CLEAN — B07 firewalled from FTTCP, no FTTCP scoring present"
critical_count: 0
major_count: 0
minor_count: 4
acceptance_rate: 99   # 67 of 68 in-scope rules passed clean (1 MINOR soft-fail: ROCE source-preference); no CRITICAL/MAJOR
```
