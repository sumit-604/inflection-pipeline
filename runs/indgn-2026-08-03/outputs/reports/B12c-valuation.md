# B12c — VERIFIER C: FRAMEWORK ADHERENCE (VALUATION HALF)
## Indegene Limited (INDGN) | Run 2026-08-03 | Phase 3, valuation-adherence audit
### Model: Opus 4.8 | Scope: B10 assembly, B11 Role 1 valuation, B14 Role 2 thesis vs Section 1B v3.3 / v3.5.1 + FTTCP v1.2

Fresh context. Gate 0 and Emerging Moat adherence were audited in phase 1 and are NOT
re-run here. This report covers the deferred valuation-adherence audit, extended to Role 2
(B14) decision rules and position sizing. Numbers-in-source is Verifier A's gate, not mine;
I audit rule application only. Every FAIL carries a rule reference and the recomputed value.

---

## PART 1 — SECTION 1B PILLAR-BY-PILLAR ADHERENCE (B10 → B11)

### Pillar 1 — Return Normalization

| # | Rule (authority) | Applied as written? | Recompute / note |
|---|---|---|---|
| 1 | Continuous formula 0.5 × ROCE + 7.5, floor 9x cap 24x (Amendment 5) — NOT the old band table | PASS | 0.5 × 25.8 + 7.5 = 20.4x; inside [9, 24]. B11 §1B and B10 both carry 20.4x. |
| 2 | Route selection A-governs-B-suppressed (v3.5.1 Consolidated Amendment 9) | PASS | Non-operating cash+investments 41.8% of CE > 20% trigger → Route A governs (denominator fix). FTTCP RECOVERING would open Route B (numerator fix) but it is SUPPRESSED per single-credit. B11 worksheet states exactly "A-governs-B-suppressed" and 9.1 blend = "blend skipped, operational ROCE feeds formula alone." Correct v3.5.1 worksheet discipline. |
| 3 | Single-credit: ROCE recovery in Pillar 1 OR Strategic Premium, never both (Amendment 4) | PASS | Credited via Pillar 1; Strategic re-rating BARRED. Both B10 and B11 state it explicitly. |
| 4 | FTTCP RECOVERING verdict is the sole Pillar 1 ROCE authority | PASS | RECOVERING (prob 50-55%, catalyst Moderate) carried verbatim from FTTCP p.114; not re-derived. |
| 5 | Operational-ROCE mandatory disclosure line (statutory %, stripped items, operational %) — v3.5.1 Route A | PASS | Statutory 15.4%; non-operating capital 41.8% stripped; operational 25.8%. Disclosure line present in B11 §1B worksheet. |

### Pillar 2 — Cash Conversion

| # | Rule (authority) | Applied? | Recompute / note |
|---|---|---|---|
| 6 | Multiplier matches the stated determination (GROWTH INDUCED, not structural) | PASS | 1.30x carried from FTTCP p.119; consistent with GROWTH INDUCED + elite CFO/PAT 1.62x. |
| 7 | Growth offset rule applied correctly (no offset in this band) | PASS (limited) | B11 states "no growth offset in this band." The band table itself is not reproduced in the amendment docs I hold; 1.30x is operator-approved and carried faithfully, so adherence is confirmed at the carry level, not independently re-derived from a band table. No contradiction found. |
| 8 | No offset on structural cash (Amendment 7 / Appendix A logic) — N/A, determination is growth-induced not structural | PASS | Correctly treated as growth-induced; Pillar 2 policed independently, premiums not scaled by multiplier (Appendix A stands). |

### Pillar 3 — Growth Premium (decomposed, Amendments 4.1 / 4.2)

| # | Rule (authority) | Applied? | Recompute / note |
|---|---|---|---|
| 9 | 3a Growth Visibility: +2x if any two qualify (Amendment 4.1) | PASS | Two qualifiers documented: SOM-implied 3yr CAGR 20.0% ≥ 20% with capacity cross-check passing (B09/B11 2D checks), AND management delivery grade B. +3x barred (needs ≥3 qualifiers + grade A/B). +2x correct. |
| 10 | 3b Moat Formation: EM-gated table (unchanged) | PASS (carried) | EM 31/80 STRENGTHENING → +3x, carried verbatim from FTTCP p.120. The 3b table lives in base Section 1B (not in the amendment set I hold); verified as faithfully carried, not re-derived. |
| 11 | 3c Duration Premium: +1x ≥2.5yr / +2x ≥4yr documented order book (Amendment 4.2) | PASS | +0x. No 📄 executable order book ≥2.5yr tenor. Correct. |
| 12 | Combined 3a+3b+3c ≤ +6x hard cap (Amendment 4.1) | PASS | +2 +3 +0 = +5x ≤ +6x. |
| 13 | SHARED CATALYST flagged where the same driver powers Pillar 1 recovery and Pillar 3 premium (Amendment 4 interaction) | PASS | Revenue-on-fixed-capital drives both; B11 and B10 flag SHARED CATALYST for Role 3 stress-test. Permitted-and-flagged, not a double-credit. |

### Strategic Premium, UA, Sector Cap

| # | Rule (authority) | Applied? | Recompute / note |
|---|---|---|---|
| 14 | Strategic Premium +0x (re-rating barred under single-credit) | PASS | +0x; no licence monopoly; recovery credited only via Pillar 1. |
| 15 | UA NOT applied — <3% FII+DII qualifier fails (Amendment 3) | PASS | Institutions 18.66% > 3% → gate fails. UA correctly not applied. All three qualifiers named; the failing one is decisive. |
| 16 | UA ordering min(Raw × 1.25, Cap) (Amendment 3) | PASS (moot) | F2 = F = 31.5x because UA not applied. Ordering correctly stated as moot. |
| 17 | Sector cap Platform/SaaS/IT services 45x, ABSOLUTE (Amendment 3 / manifest correction) | PASS | 45x confirmed (manifest Pharma/CDMO 38x defect corrected). H = min(31.5, 45) = 31.5x; cap does not bind. |

### Destination PE — both tracks

| # | Rule (authority) | Applied? | Recompute / note |
|---|---|---|---|
| 18 | Additive track: C = P1 × P2, F = C + P3 + Strategic | PASS | C = 20.4 × 1.30 = 26.5x; F = 26.5 + 5 + 0 = 31.5x. Reproduced exactly. |
| 19 | RRM track: fundamental base × RRM, capped at sector cap | PASS | 26.5 × 1.06 = 28.09 → 28.1x, capped 45x → 28.1x. |
| 20 | RRM formula 1 + (13.5 − r) × 0.12 in PERCENTAGE POINTS (Amendment 4.4) | PASS | r = 13.0 → 1 + (13.5 − 13.0) × 0.12 = 1 + 0.06 = 1.06. Percentage-point reading correct (decimal reading would give ~1.00, wrong). |
| 21 | Proportional ±7.5% range, round to nearest 0.5x (Amendment 6) | PASS | Additive 31.5 → 29.0–34.0x; RRM 28.1 → 26.0–30.0x. Rounding correct. |
| 22 | Divergence handling: conservative track governs entry on >15% divergence | PASS | Divergence = (31.5 − 28.1)/28.1 = 12.1% < 15% → immaterial; the >15% conservative-override rule does NOT trigger. Operator election of additive is within tolerance; RRM carried in full; CMP inside BUY-on-dips band on BOTH tracks so choice cannot flip the verdict. Handled correctly. |
| 23 | Destination PE sourced only from Section 1B via operator-approved FTTCP; 31.5x base used, not silently re-derived | PASS | 31.5x is the operator-elected additive base (FTTCP Decision 2 p.21). B11 independently reproduces 31.5x and matches — reproduction confirms, does not replace, the approved base. No exit PE from outside Section 1B anywhere. |
| 24 | Both tracks carried through every fair value and the verdict card | PASS | Additive and RRM present in Section 3 matrix, Section 4 entry table, verdict card, and B14 Section 5. |

### Hurdle Ratio, EPS basis, forward-PE-at-exit

| # | Rule (authority) | Applied? | Recompute / note |
|---|---|---|---|
| 25 | HR = (1 + EPS CAGR)³ × (Dest PE mid ÷ Current PE) (Amendment 2) | PASS | (1.219)³ × (31.5/26.97) = 1.811 × 1.168 = 2.12. Reproduced. |
| 26 | Tier B threshold 1.728 (Amendment 4.3) | PASS | 2.12 ≥ 1.728 PASS; also clears Tier A 1.953. |
| 27 | **EPS BASIS CONSISTENCY (SFL discipline)** — numerator and denominator both on the operator-approved FORWARD basis, no mixed cash-vs-reported basis | PASS | Denominator current forward PE = CMP / FY27 EPS 20.22 = 26.97x. Numerator EPS CAGR = FY27→FY30 (20.22→36.62) = 21.9%. Both legs are forward, reported-basis EPS, anchored to FY27, a clean 3-year gap. No cash-EPS vs reported-EPS mixing, no FY26-vs-FY27 straddle. SFL discipline held. Checked explicitly. |
| 28 | Bull EPS CAGR usable only if delivery grade Good/Excellent (Amendment 2 conservative note) | PASS | Grade B (Good) → bull row permitted; HR(bull) 2.37 computed and used correctly. |
| 29 | Forward-PE-at-exit: exit-year multiple on the year-AFTER EPS; ladder built to year after exit | PASS | Exit FY29 (Year 3); destination PE applied to FY30 EPS; ladder runs FY27→FY30. Convention applied correctly. FV = 31.5 × 36.62 = 1,154 (additive); 28.1 × 36.62 = 1,029 (RRM). |
| 30 | 4D probability weights match grade (Good = 25/50/25) | PASS (carried) | 25/50/25 applied; expected additive CAGR = 15.9×.25 + 28.4×.50 + 36.7×.25 = 27.4%. Reproduced. Weight table itself not in my doc set; verified as internally consistent and correctly summed. |

---

## PART 2 — ROLE 2 (B14) DECISION RULES + POSITION SIZING

| # | Rule (authority) | Applied? | Recompute / note |
|---|---|---|---|
| 31 | Tier B assignment: ALL four gates hold (Amendment 4.3) | PASS | FII+DII 18.66% ≥ 3% ✓; Gate 0 GOOD+ / EM 31 ≥ 25 ✓; promoter TRUSTWORTHY ✓; FLAG-CASH growth-induced not structural ✓. Tier B correctly assigned; verdict card first line "Tier: B \| Hurdle: 20%" present. |
| 32 | Entry = base fair value ÷ 1.728 (Tier B divisor, Amendment 4.3) | PASS | Additive 1,154 / 1.728 = 668; RRM 1,029 / 1.728 = 596. Correct. |
| 33 | MoS = 20% below entry | PASS | 668 × 0.80 = 534 (additive); 596 × 0.80 = 477 (RRM). Correct. |
| 34 | BUY / WATCHLIST / AVOID mapping vs Hurdle + entry-conjunction rules | PASS | HR PASS (not CONDITIONAL) → not capped at WATCHLIST. CMP 545.25 inside entry zone 534–668 but above MoS floor 534 → BUY-on-dips, not BUY-NOW (BUY-NOW requires CMP ≤ MoS). Entry conjunction (price-in-zone AND no thesis-broken trigger) enforced. Mapping correct. |
| 35 | Position size respects Tier B Medium 4-6% ceiling; override documented if any (Amendment 4.3) | PASS | Medium 4-6% ceiling; Large correctly barred (needs Gate 0 EXCELLENT + EM EXPANSION + CMP < MoS, none met). Staged Small-starter-to-Medium sits INSIDE the ceiling and is not an override; B14 states no operator override recorded. Correct. |
| 36 | Fair values / destination PE carried verbatim from B11, not re-derived in Role 2 | PASS | B14 Section 5 carries additive/RRM tracks verbatim; explicitly states exit PE not re-derived. |

---

## PART 3 — KNOWN UNITS SLIP (checked as instructed)

**FINDING (MINOR, decision-neutral) — combined contingent-liability units label.**
- B10 line 224: "Combined Contingent Liability Exposure | **Rs 1,531 crore** (38.2% of FY26 PAT)."
  B10 line 222: TP dispute "**Rs 1,114 crore** (21.2% of FY26 PBT)."
  B11 YAML line 399: "Rs 1,531 cr = 38.2% of PAT."
- Correct magnitude: **Rs 1,531 mn = Rs 153 cr** (TP Rs 1,114 mn + TCPA max Rs 417 mn). The
  percentages confirm the correct magnitude: 153 / 401.1 PAT = 38.2% ✓, and 111.4 / 525.0 PBT
  = 21.2% ✓. A literal "Rs 1,531 cr" would be 382% of PAT, so the "cr" label is the slip; the
  "mn/cr" figure is right and the ratios are right.
- **Decision-neutral:** the figure is a carried disclosure flag (FLAG-CONTINGENT-LIABILITY),
  not a valuation input — it never touches the pillars, the destination PE, the Hurdle, or the
  entry zone. The 38.2%-of-PAT threshold read is correct either way.
- **To B14's credit:** Role 2 CAUGHT and corrected this. B14 Section 6 and Input Discipline
  Notes state "Rs 1,531 mn (Rs 153 cr) = 38.2% of FY26 PAT; B11 YAML labels this 'Rs 1,531 cr',
  a units slip; the mn/cr figure is used." Severity held at MINOR because it is decision-neutral
  and already corrected downstream. (Source-of-number fidelity is Verifier A's gate; recorded
  here only as instructed.)

---

## PART 4 — CONCLUSION

Every valuation mechanic reproduces exactly: Pillar 1 20.4x, quality base 26.5x, additive
destination 31.5x, RRM 28.1x, divergence 12.1%, Hurdle 2.12 PASS, entry 668 / MoS 534, expected
additive CAGR 27.4%. Route selection, single-credit, UA gate, sector cap, ±7.5% range, RRM
percentage-point reading, forward-PE-at-exit convention, SFL EPS-basis consistency, Tier B
assignment, entry-conjunction, and Medium 4-6% position ceiling are all applied as written.

I **CONCUR** with the destination PE (31.5x additive / 28.1x RRM) and the decision (BUY on-dips,
Medium 4-6%, staged). No CRITICAL, no MAJOR. One MINOR, decision-neutral units-label slip in
B10/B11, already corrected in B14.

- Rules checked: 36
- Passed: 36 (mechanics); the single MINOR finding is a decision-neutral units label on a
  carried flag, not a valuation-rule misapplication. Counting it as the one blemish against the
  audited chain gives 35/36 clean.
- framework_adherence_valuation: 97%

```yaml
stage: B12c-valuation
company: "INDGN"
run_date: "2026-08-03"
model: claude-opus-4-8
status: complete
phase: "3-valuation-half"
scope: "B10 assembly + B11 Role 1 valuation + B14 Role 2 thesis vs Section 1B v3.3/v3.5.1 + FTTCP v1.2"
valuation:
  rules_checked: 36
  fails: []          # no mechanical/decision fails; one decision-neutral MINOR recorded in findings
pillar_checks:
  pillar1_formula: "PASS — 0.5x25.8+7.5=20.4x, within [9,24]"
  pillar1_route: "PASS — A-governs-B-suppressed (v3.5.1); 41.8% non-op capital >20% trigger; blend skipped"
  pillar1_single_credit: "PASS — recovery via Pillar 1, Strategic barred (Amendment 4)"
  pillar1_authority: "PASS — FTTCP RECOVERING is sole ROCE authority"
  pillar2_multiplier: "PASS — 1.30x consistent with GROWTH INDUCED; no offset in band"
  pillar3_3a: "PASS — +2x, two qualifiers (SOM 20% + grade B); +3x correctly barred"
  pillar3_3b: "PASS — +3x EM 31 STRENGTHENING, carried verbatim"
  pillar3_3c: "PASS — +0x, no >=2.5yr documented order book"
  pillar3_cap: "PASS — +5x <= +6x combined cap"
  strategic_premium: "PASS — +0x, re-rating barred"
  ua: "PASS — NOT applied, institutions 18.66% fails <3%; min(Rawx1.25,cap) moot"
  sector_cap: "PASS — 45x Platform/SaaS/IT absolute; 31.5x<45x non-binding"
  rrm_formula: "PASS — 1+(13.5-13.0)x0.12=1.06 percentage-point reading (Amdt 4.4); 28.1x"
  divergence: "PASS — 12.1% < 15%, conservative-override not triggered; both tracks carried"
  range_pm75: "PASS — 29.0-34.0x additive / 26.0-30.0x RRM, rounded to 0.5x (Amdt 6)"
  hurdle_ratio: "PASS — 2.12 >= Tier B 1.728 (also clears Tier A 1.953)"
  sfl_eps_basis: "PASS — numerator FY27->FY30 CAGR and denominator FY27 forward PE both on one FORWARD reported basis; no cash-vs-reported mixing"
  forward_pe_at_exit: "PASS — FY29 exit, destination PE on FY30 EPS, ladder to year-after"
role2_checks:
  tier_b_assignment: "PASS — all four gates hold"
  entry_divisor: "PASS — base FV / 1.728 = 668 additive / 596 RRM"
  mos: "PASS — 20% below entry = 534 additive / 477 RRM"
  decision_mapping: "PASS — BUY-on-dips (CMP 545.25 in zone, above MoS 534); HR PASS not CONDITIONAL; entry conjunction enforced"
  position_size: "PASS — Tier B Medium 4-6% ceiling; Large barred; staged entry inside ceiling, no undocumented override"
  carry_discipline: "PASS — B14 carries B11 fair values verbatim, exit PE not re-derived"
findings:
  - {severity: "MINOR", location: "B10 line 224 / line 222; B11 YAML line 399", claimed: "combined contingent liability 'Rs 1,531 cr' (TP 'Rs 1,114 cr')", rule_ref: "units/accuracy — carried FLAG-CONTINGENT-LIABILITY, not a valuation input", note: "Correct figure Rs 1,531 mn = Rs 153 cr (TP 1,114 mn + TCPA 417 mn); 38.2% of PAT and 21.2% of PBT confirm the mn/cr magnitude. Decision-neutral: never enters pillars/destination PE/Hurdle/entry. B14 caught and corrected it (Section 6, Input Discipline Notes)."}
recomputed_destination_pe: ""   # concur: 31.5x additive / 28.1x RRM reproduced exactly
recomputed_decision: ""         # concur: BUY (on-dips), Medium 4-6%, staged
framework_adherence_valuation: 97
critical_count: 0
major_count: 0
minor_count: 1
acceptance_rate: 97             # rules passed (35 clean + 1 decision-neutral minor) / 36 checked
```
