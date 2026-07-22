# B12c — VERIFIER C: FRAMEWORK ADHERENCE (PHASE 3, VALUATION-ADHERENCE HALF)

**Company:** KCPSUGIND | **Run date:** 2026-07-21 | **Model:** claude-opus-4-8
**Scope this phase:** VALUATION-ADHERENCE only. Audits B11 (11-valuation.md /
B11-valuation.yaml) and B10 (assembled inputs), EXTENDED to B14 (Role 2 thesis)
decision rules and position-sizing logic. Gate 0 (B01) and Emerging Moat (B07)
checks already ran in Phase 1 and are NOT repeated here.
**Authority:** Master v3.3 Role 1/Role 2, Section 1B v3.3 Amendments, Section 1B
v3.5.1 Reconciliation, FTTCP v1.2. Numbers-existence questions belong to Verifier A;
this is rule-application only.
**Authoritative run context accepted:** SOTP-led per operator Override 3, four-pillar
exit PE subordinate operating cross-check; operator-approved pillars used verbatim.

---

## 1. PILLAR-BY-PILLAR VALUATION AUDIT (B11 + B10)

| # | Rule (authority) | Applied value | Verdict | Recompute / note |
|---|---|---|---|---|
| 1 | Continuous Pillar 1 formula 0.5×ROCE+7.5, floor 9x, cap 24x (Amd 5) | 0.5×4+7.5 = 9.5x | PASS | 9.5x, floor 9x non-binding. Correct. Old bands not used. |
| 2 | FTTCP ROCE verdict = sole Pillar 1 authority | DECLINING (−1) (B10 roce_verdict) | PASS | Verdict carried verbatim; Pillar 1 = FY[Y+1] lower bound per DECLINING. |
| 3 | v3.5.1 route selection (Amd 9 consolidated) | Route NONE | PASS | Route A fails (no CWIP/idle-capital >20% CE); Route B barred — v3.5.1 explicitly forbids either route on a STAGNANT/DECLINING verdict. Statutory ROCE feeds Pillar 1. Correct. |
| 4 | Amendment 4.5 retired-as-number, not standalone | Not applied | PASS | Report states 4.5 retired; only survives as Route B, which is barred here. Correct. |
| 5 | Single-credit ROCE recovery, route stated (Amd 4) | "not credited" | PASS | No recovery to credit (DECLINING); Strategic ROCE re-rating route correctly barred. Route explicitly stated. |
| 6 | Pillar 2 multiplier matches determination | 0.65x STRUCTURAL | PASS | Structural band (0.65x). Triggered via the "if growth stopped, WC still high? YES — seasonal agri" test (Master p.254 lists seasonal agri procurement as structural). CFO −30.89 Cr, first cash loss. See observation O1 on the CARE liquidity wording. |
| 7 | No growth offset on structural (Master offset table) | +0 offset | PASS | Structural → 0 offset. Correct. |
| 8 | Quality-adjusted base = ROCE base × cash mult | 9.5×0.65 = 6.175 ≈ 6.2x | PASS | Arithmetic correct. |
| 9 | Pillar 3a growth-visibility (Amd 4.1) | +0x | PASS | Grade C caps 3a at +2x, but no qualifier holds: SOM CAGR 9.7% (<20%), no capex-embedded growth, delivery grade C, Eimco order UNFILED so not 📄-documented. +0x correct. |
| 10 | Pillar 3b moat-formation (EM-gated) | +0x | PASS | EM 5 (<25) → +0x. Correct. |
| 11 | Pillar 3c duration premium (Amd 4.2, 📄-only) | +0x | PASS | Eimco Rs 257 Cr order pending Reg 30, 📄 gate fails; TAM/pipeline talk pays nothing. +0x correct. |
| 12 | Strategic premium single-credit state | +0x | PASS | Nothing to credit; ROCE re-rating barred (DECLINING + single-credit). Correct. |
| 13 | UA in Amendment 3 order, all 3 qualifiers evidenced | NOT APPLIED | PASS | listed≥12m YES; Gate0≥60 OR EM≥25 = NO (26/5); FII+DII<3% UNRESOLVED. all_met=NO → withheld. Withholding on an unresolved qualifier is the conservative call. F2 = F (no 1.25x). Correct. |
| 14 | Sector cap absolute; correct row | Agri processing 20x | PASS | Manifest Pharma/CDMO corrected to Agri processing 20x (operator Override 3, B10). Non-binding (6.2 < 20). See O2. |
| 15 | Raw destination PE = F; H = min(F2, Cap) | Raw 6.2x → H 6.2x | PASS | min(6.2, 20) = 6.2x. Correct. |
| 16 | BOTH tracks present and carried | Additive + RRM both shown | PASS | Additive 5.7–6.7 (mid 6.2); RRM 6.65–7.79 (mid 7.2). |
| 17 | RRM percentage-points reading (Amd 4.4) | r=15→0.82, r=16→0.70, mid 15.5→0.76 | PASS | (13.5−15.5)×0.12 = −0.24 → 0.76. Correct percentage-point reading; bounded [9,18]. |
| 18 | RRM destination = Fundamental Base × RRM | 9.5×0.76 = 7.2x | PASS* | Arithmetic correct. See O3 (base-selection: uses ROCE base 9.5x, not quality-adjusted 6.2x). Decision-invariant. |
| 19 | Track divergence >15% → conservative governs | 16.1%, additive governs | PASS | (7.2−6.2)/6.2 = 16.1%. More conservative additive governs the operating cross-check. Correct. |
| 20 | Hurdle Ratio formula (Amd 2) | (1.10)³×(6.2/22.2) = 0.37 | PASS | 1.331×0.2793 = 0.372. Correct. Operating basis 0.10 also correct (6.2/86.8). |
| 21 | Hurdle threshold Tier A = 1.953 → verdict | STOP | PASS | 0.37 << 1.953 → STOP. Correct. |
| 22 | Bull HR gated on grade (grade C → base+5% max) | 15% CAGR, HR 0.42 | PASS | Grade C, so bull uses base+5%=15%, not a management bull figure. (1.15)³×(6.2/22.2)=0.42. Bull STOPs too. Correct. |
| 23 | Earnings basis trailing (operator-approved) | trailing | PASS | Pillars run on normalized operating TRAILING EPS ~Rs 0.25. Consistent with B10 earnings_basis. |
| 24 | Tier A/B assignment (Amd 4.3) | Tier A, Tier B barred | PASS | Tier B gate "no structural FLAG-CASH" fails (STRUCTURAL) AND Gate0 not GOOD → Tier A 25% hurdle stands. Correct. |
| 25 | Entry = base FV ÷ 1.953 (Tier A) | 22.50/1.953 = 11.52 | PASS | Also 30% entry 22.50/2.197 = 10.24. Correct. |
| 26 | MoS = 20% below 25% entry | 11.52×0.8 = 9.22 | PASS | Correct. |
| 27 | Upside/Downside = base/bear, ≥2x (Master p.654) | 0.07x (base/bear) | PASS* | 3.6/49.5 = 0.073. Correct in report body. See O4: B11 YAML headline field reports 1.06 (bull/bear), not the framework-defined 0.07; both fail 2x. |
| 28 | Prob-weighted expected CAGR (grade C 35/45/20) | −3.6% | PASS | 0.35×−20.3 + 0.45×+1.2 + 0.20×+15.1 = −3.55 ≈ −3.6%. Scenario CAGRs recompute clean. |
| 29 | SOTP internal arithmetic consistency | see §2 | PASS | All cells recompute (§2 below). |
| 30 | Single catalyst credited once (no double-count) | Eimco in SOTP only, not Pillar 3/earnings | PASS | Rs 257 Cr order credited once, as a higher going-concern multiple in SOTP; +0x in Pillar 3; not in base earnings. Single-credit respected. |
| 31 | Unresolved inputs handled by conservative rule, no silent fills | FII+DII, Eimco standalone, ethanol rev | PASS | Each unresolved input is named and handled conservatively (FY25 PAT proxy for Eimco bear; ethanol subsumed; FII+DII withheld). No estimated fills. |
| 32 | P/B secondary cross-check | 0.50–0.55x × 40.52 = 20.3–22.3 | PASS | Brackets base SOTP 22.50 and CMP. Arithmetic correct. |
| 33 | SOM revenue-CAGR cross-check performed | "consistent" | PASS | SOTP does not lean on operating CAGR above SOM 9.7%; only Eimco order visibility credited. Documented. |

\* PASS with observation (O3 / O4 below).

### Observations (all MINOR; none change the destination PE or the decision)

- **O1 (Pillar 2 trigger wording):** The 0.65x band label in Master p.248 reads
  "Structurally negative — rating agency confirms persistent WC." CARE's own quote
  frames liquidity as *strong* (free cash+investments Rs 204.08 Cr, current ratio
  2.73x, nil term debt, avg WC utilisation 37.65%), which does not itself "confirm
  persistent WC." The 0.65x is nonetheless correctly earned through the independent
  structural test (seasonal cane procurement is inherently long-cash-cycle; FY26 first
  actual cash loss; receivable days 31→81). Determination is defensible and is the
  operator-approved pillar; noted only because the rating-agency limb of the band label
  is not the limb actually satisfied.

- **O2 (sector cap source):** "Agri processing 20x" is operator-supplied (Override 3),
  not a literal row in the Master/Amendment-8 cap tables. Because the cap is non-binding
  (raw 6.2x << 20x) it has zero effect on the destination PE. No exit PE from outside
  Section 1B entered the calculation.

- **O3 (RRM base selection):** Track 1 multiplies the ROCE base (9.5x) by RRM, not the
  quality-adjusted base (6.2x). Master p.392 says "Fundamental Base PE × RRM" without
  fixing which base; using the ROCE base is a defensible reading and the cash-quality
  risk is partly folded into the r-uplift (r pushed to 15.5 for weak durability/DECLINING).
  It makes RRM the *less* conservative track, and the framework's "more conservative track
  governs" rule then correctly hands the operating cross-check to the additive track. No
  decision impact.

- **O4 (YAML U/D field):** B11-valuation.yaml `upside_downside_ratio: 1.06` reports the
  bull/bear ratio; the framework-defined field (Master p.654) is base/bear = 0.07x. Both
  appear in the report body (§4F) and both fail the 2x minimum, so the AVOID trigger is
  unaffected. Cosmetic mislabel in the block only.

---

## 2. SOTP CONSTRUCTION — INDEPENDENT RECOMPUTE

Investment book Rs 332.11 Cr (FVTPL 292.76 + cash 39.35), discounts 50/35/20%:

| Slice | Bear | Base | Bull | Recompute |
|---|---|---|---|---|
| Investment book | 166.06 | 215.87 | 265.69 | 332.11×0.50/0.65/0.80 = 166.06 / 215.87 / 265.69 ✓ |
| Eimco (6/8/10x) | 99.00 | 148.00 | 185.00 | 6×16.56=99.4; 8×18.47=147.8; 10×18.47=184.7 ✓ (18.47 = 24.63×0.75) |
| Sugar + others | −13.00 | 19.00 | 52.00 | sugar −25/0/+30 + urad 12/19/22 (4/6/7×3.16) ✓ |
| Less borrowings | −127.71 | −127.71 | −127.71 | B10 total_borrowings 127.71, all cases ✓ |
| **Equity value** | **124.35** | **255.16** | **374.98** | sums recompute exactly ✓ |
| **÷ 11.34 → per share** | **10.97** | **22.50** | **33.07** | 124.35/255.16/374.98 ÷ 11.34 ✓ |

- **Internal consistency:** PASS. Cash counted once (inside the investment book);
  borrowings subtracted gross (not netted against that cash) — a consistent gross approach,
  no double-count. Segment PPE captured via going-concern earnings; sugar hard assets
  credited only in bull. The report's own 2D double-count check is honest and correct.
- **Base SOTP equity Rs 255 Cr ≈ market cap Rs 246 Cr:** the "market already prices the
  asset case" conclusion recomputes cleanly and is the spine of the AVOID.

**O5 (MINOR — largest SOTP swing, NOT part of the operator-approved base):** The Eimco
going-concern multiples (6/8/10x) and urad-dal multiples (4/6/7x) are analyst-selected
round numbers. The operator approved *the method* ("Eimco going concern," Override 3) but
did not fix the multiple; the maker filled it. These are not derived from a Section 1B
four-pillar computation for the subsidiary, and CLAUDE.md carries a "no round-number
defaults" rule. Eimco base (Rs 148 Cr) is the single largest discretionary value driver.
Sensitivity: pushing the Eimco base multiple to 12x lifts base FV only to ~Rs 29 (~+33%
over CMP → ~10% 3yr CAGR, still <25%; entry zone still below CMP), so **the AVOID survives
even a materially higher Eimco multiple.** Decision-invariant; flagged for operator
visibility, not as a decision error. Multiples are bounded by the Engineering 25x sector
cap and are conservative for a 30%+ margin franchise.

---

## 3. B14 (ROLE 2 THESIS) — DECISION RULES & POSITION SIZING

| # | Rule (Master Role 2) | B14 value | Verdict | Note |
|---|---|---|---|---|
| 34 | Verdict per decision rules (Master p.809) | AVOID | PASS | AVOID triggers all fire: Gate0=AVOID, Hurdle=STOP, U/D<2x. Any one suffices. |
| 35 | Decision-rule trace documented | 3 triggers named | PASS | Trace cites Gate0 AVOID default, HR STOP, U/D 0.07x/1.06x. Correct mapping to p.809. |
| 36 | Entry conjunction (anti-value-trap, p.811) | Present in verdict box | PASS | States a starter executes only when price-in-zone AND no thesis-broken trigger fired; withdraws zone if price falls because a trigger fired. Verbatim intent. |
| 37 | Position-size tier derivation (p.813–818) | Small (2–3%) | PASS | Large fails (Gate0 not EXCELLENT, EM not EXPANSION); Medium fails (Gate0 not GOOD+, Promoter not TRUSTWORTHY). Small is the only qualifying band. Correctly framed as re-open-zone starter; executable size at CMP = zero. |
| 38 | Promoter verdict cap binds (p.818) | CAUTION caps size | PASS | Promoter CAUTION treated as a binding position-size cap; consistent with "Promoter Verdict caps always bind." |
| 39 | Position-size override recorded correctly | NONE | PASS | Overrides 1–4 touch method/inputs, not size; B14 position_size_override "" and narrative both state NONE. Correct. |
| 40 | 5yr target — no estimation | NOT FOUND | PASS | Asset-NAV case; 5yr target stated NOT FOUND, not fabricated. Honors "never estimate." |
| 41 | Entry / MoS / targets carried consistent with B11 | 10.24–11.52 / 9.22 / 22.50 | PASS | All figures reconcile to 11-valuation.md §4E/§4H. No drift. |
| 42 | Monitoring checklist specific & measurable (p.830) | 8 items | PASS | Each item has a numeric green/red threshold (book ≥Rs 332 Cr, sugar loss >Rs 25 Cr, RPT >27%, etc.). Compliant. |
| 43 | Cross-reference "hardest verdict wins" | Applied | PASS | Section 4 resolves each tension to the harder read; no unresolved contradiction reverses AVOID. |

No decision-rule or position-sizing misapplication found in B14.

---

## 4. SUMMARY

- **Destination PE:** independently recomputed to **6.2x additive / 7.2x RRM** — CONCUR
  with B11. No exit PE from outside Section 1B entered the calculation.
- **Decision:** **AVOID-on-valuation at Rs 21.71**, Tier A, entry Rs 10.24–11.52, MoS
  Rs 9.22 — CONCUR. Verdict is SOTP-driven (base SOTP ≈ CMP), corroborated by a subordinate
  operating cross-check that STOPs on the Hurdle Ratio; every AVOID trigger recomputes.
- **Operator-approved base:** used verbatim; no silent departure detected in the pillars.
  The only discretionary inputs the maker filled beyond the approved base are the SOTP
  segment multiples (O5) — round numbers, largest swing, but decision-invariant.
- **Findings:** 0 CRITICAL, 0 MAJOR, 5 MINOR (O1 Pillar-2 label limb; O2 cap source;
  O3 RRM base selection; O4 YAML U/D field; O5 Eimco/urad round-number SOTP multiples).
  None move the destination PE by >1x, flip the Hurdle verdict, or change the decision.

---

```yaml
stage: B12c
company: "KCPSUGIND"
run_date: "2026-07-21"
model: claude-opus-4-8
status: complete
phase: 3
scope: "valuation-adherence only (B11 + B10, extended to B14 decision/position rules); Gate0 and Emerging Moat audited in phase 1, not repeated"
gate0: {rules_checked: 0, fails: []}   # out of scope this phase (ran phase 1)
emoat: {rules_checked: 0, fails: []}   # out of scope this phase (ran phase 1)
valuation:
  rules_checked: 43
  fails:
    - {severity: "MINOR", rule: "Pillar 2 0.65x band label 'rating agency confirms persistent WC'", note: "CARE frames liquidity as strong; 0.65x correctly earned via the independent structural test (seasonal agri), not the rating-agency limb. Operator-approved pillar."}
    - {severity: "MINOR", rule: "Sector cap source", note: "Agri processing 20x is operator-supplied, not a literal cap-table row; non-binding (6.2<<20), zero effect."}
    - {severity: "MINOR", rule: "RRM base selection (Master p.392)", note: "Track 1 uses ROCE base 9.5x not quality-adjusted 6.2x; defensible reading; conservative additive track governs anyway. No decision impact."}
    - {severity: "MINOR", rule: "B11 YAML upside_downside_ratio field", note: "Reports bull/bear 1.06 instead of framework-defined base/bear 0.07; both shown in body, both fail 2x."}
    - {severity: "MINOR", rule: "SOTP segment multiples not Section-1B-derived (CLAUDE.md no-round-number)", note: "Eimco 6/8/10x, urad 4/6/7x are analyst round numbers, not four-pillar-derived; largest SOTP swing but AVOID survives even 12x Eimco. Method (Eimco going concern) operator-approved; multiple was maker-filled."}
recomputed_destination_pe: ""   # concur: 6.2x additive / 7.2x RRM
recomputed_decision: ""         # concur: AVOID-on-valuation, Tier A, entry 10.24-11.52
findings:
  - {severity: "MINOR", location: "B11 §1B Pillar 2", note: "O1 — 0.65x earned via structural test, not the rating-agency band limb"}
  - {severity: "MINOR", location: "B11 §1B step G / B10 sector_cap", note: "O2 — Agri 20x operator-supplied, non-binding"}
  - {severity: "MINOR", location: "B11 §1B RRM dual-track", note: "O3 — RRM applied to 9.5x ROCE base; conservative additive governs"}
  - {severity: "MINOR", location: "B11-valuation.yaml upside_downside_ratio", note: "O4 — reports bull/bear not base/bear; both fail 2x"}
  - {severity: "MINOR", location: "B11 §3(b)/(c) SOTP multiples", note: "O5 — round-number segment multiples, largest swing, decision-invariant"}
critical_count: 0
major_count: 0
minor_count: 5
acceptance_rate: 88   # 43 checked, 38 clean-pass, 5 minor imperfections; 38/43 = 88%
```
