# STAGE 12c — VERIFIER C: FRAMEWORK ADHERENCE (PHASE 3, VALUATION + ROLE 2)
# NORTHARC (Northern Arc Capital Limited) | Run 2026-07-12
# Model: claude-opus-4-8 | Scope: DEFERRED valuation-adherence audit only
# Frameworks: Master v3.3 (Role 1 Sec 1B + Role 2) / Section 1B v3.3 Amendments 1-8, v3.4 4.1-4.4 / FTTCP v1.2
# Gate 0 (B01) and Emerging Moat (B07) adherence: COMPLETED PHASE 1 (not re-run here)

I audit rule APPLICATION only, not company quality and not raw numbers (Verifier A owns
numbers). Inputs read fresh: the three framework docs, B10 (10-valinputs.md + B10 YAML),
B11 (11-valuation.md + B11 YAML), B14 (14-thesis.md + B14 YAML). Lender carve-out (Amendment 7)
governs throughout: Pillar 1 uses ROE; Pillar 2 replaced by Pillar 2L Asset-Quality Multiplier;
P/B primary; 18x cap.

═══════════════════════════════════════════════════════════════════
## PART A — VALUATION (B11) RULE-BY-RULE COMPLIANCE
═══════════════════════════════════════════════════════════════════

### A1. Pillar 1 — ROE Base Multiple (continuous formula + FTTCP sole authority)

| # | Rule as written | Applied in B11 | Verdict |
|---|---|---|---|
| 1 | Continuous formula 0.5×ROE+7.5, floor 9x cap 24x (Amend 5); lender uses ROE (Amend 7) | 0.5×13.46+7.5 = 14.23 → 14.2x; within floor/cap; ROE substituted for ROCE | PASS |
| 2 | FTTCP forward verdict is SOLE authority for the ROE used (FTTCP Pillar 1 Integration; Master Pillar 1 table) | Verdict RECOVERING @ ~50-55% → 40-60% band → 60/40 weighting. No ad hoc trajectory judgment | PASS |
| 3 | RECOVERING 40-60% → 60/40 weighted avg of current & FY[Y+2] (not midpoint, which needs >60% + Strong) | 0.60×11.1% + 0.40×17.0% = 13.46%. Current FY26, FY[Y+2]=FY28. Midpoint route NOT used | PASS |
| 4 | FY[Y+2] expected input carried with its flag, not silently normalised | FY28 17% (16-18% midpoint) carried with STRETCHED flag; applied as directed | PASS |

Note: the 40% weight sits on a management-flagged STRETCHED 17% FY28 figure. The framework
mandates the weight; B11 applies it and flags the stretch. Compliant.

### A2. Single-credit rule (Amendment 4 / FTTCP v1.2)

| # | Rule | Applied | Verdict |
|---|---|---|---|
| 5 | ROE recovery credited in Pillar 1 OR Strategic Premium, never both; route stated in writing | "ROE recovery credited via: Pillar 1 (60/40 weighting)." Strategic re-rating route explicitly BARRED | PASS |
| 6 | One improvement, one mechanism (no double-credit across levers) | Recovery in Pillar 1 only; no re-rating optionality in Strategic; not re-credited via lower discount rate | PASS |

### A3. Pillar 2L — Asset-Quality Multiplier (Amendment 7, lender carve-out)

| # | Rule | Applied | Verdict |
|---|---|---|---|
| 7 | Cash Conversion Multiplier REPLACED by Asset-Quality Multiplier for lenders | Pillar 2L used; CFO/PAT not used as the multiplier driver | PASS |
| 8 | Band must match the stated determination; STRESSED band 0.80x = "GNPA rising OR >4%, PCR <60%, credit-cost guidance missed once" | GNPA 1.2% (<2%), PCR ~44.5% (<60% → breaches 60-70% and >70% bands), credit-cost guidance missed once (2.3-2.5%→2.7-2.8%) → STRESSED 0.80x. Matches B10 FTTCP determination and Amend 7 table | PASS |
| 9 | NO growth offset applies to Asset-Quality Multiplier | No offset applied; stated explicitly | PASS |
| 10 | Band consistent with FTTCP lender Transition 3 verdict / Role 4 Step 5L | 0.80x matches fttcp-deliberation Pillar 2L determination carried on B10 | PASS |
| 11 | No double-penalty: growth-induced negative CFO not punished separately (no Kernex cap) | FLAG-CASH growth-induced (Ind AS); penalty expressed ONCE via 0.80x band; Kernex cap NOT applied | PASS |
| 12 | Quality-Adjusted Base = Pillar 1 × Pillar 2L | 14.23 × 0.80 = 11.38 → 11.4x | PASS |

### A4. Pillar 3 — Growth Visibility Premium (version + inputs)

| # | Rule | Applied | Verdict |
|---|---|---|---|
| 13 | Version applied must be stated; v3.4 (Amend 4.1-4.2, dated 11-Jul-2026) in force on 2026-07-12 run date | v3.4 governs (3a/3b/3c decoupled), v3.3 EM-gate shown as conservative floor. Version stated | PASS |
| 14 | 3a Growth Visibility: +2x if any two 📄 qualifiers; grade C caps 3a at +2x, grade D pays +0x (Amend 4.1) | Two qualifiers cited: SOM-implied revenue CAGR 26% ≥20% w/ capacity cross-check passing; mgmt delivery grade B (A/B qualifies). Grade B does not cap → +2x | PASS |
| 15 | 3b Moat Formation: EM-gated table unchanged; EM <25 → +0x | EM 22 (<25) → +0x | PASS |
| 16 | 3c Duration: 📄 order book / contracted-tenor only; none for this lender → +0x | +0x (no order book / contracted-tenor revenue) | PASS |
| 17 | Combined 3a+3b+3c ≤ +6x cap | +2x total, within cap | PASS |
| 18 | EM/catalyst inputs consistent with B07 injected values | EM 22, 6/20 active, catalyst 12m D2C-mix — consistent with B07/B10 | PASS |

Observation (MINOR, advisory, not a fail): the 3a "SOM-implied revenue CAGR ≥20%" qualifier
rests on B09 TAM modelling (inference-grade), admitted because Amendment 4.1 explicitly lists
SOM-implied CAGR as an eligible qualifier. Capacity cross-check supports ≥20% (CRAR 22.6%,
gearing 3.13x→~4x room → 20-24% AUM); SOM 26% exceeds the modelled 20% base but the qualifier
threshold is ≥20%, which is met. Award defensible. Immaterial to verdict: on the v3.3 floor
(+0x) destination PE = 11.4x, still STOP, still AVOID — so any Pillar 3 error cannot flip the
decision.

### A5. Strategic Premium + Undiscovered Alpha + Sector Cap

| # | Rule | Applied | Verdict |
|---|---|---|---|
| 19 | Strategic Premium: recovery route barred if credited in Pillar 1 (single-credit); scarcity evidenced or +0x | +0x. Re-rating optionality BARRED (Pillar 1 route used); RBI NBFC-ML licence not a scarcity monopoly; institutional-backing turnaround not a discount-to-book distress → +0x | PASS |
| 20 | UA applies only if ALL three qualifiers hold (listed ≥12m; Gate0≥60 OR EM≥25; FII+DII<3%) | Listed ✓; Gate0 AVERAGE + EM 22 ✗; FII+DII >3% ✗. 1 of 3 → UA NOT applied | PASS |
| 21 | UA ordering min(Raw×1.25, Cap), Amend 3; moot when UA not applied | F2 = F (no ×1.25); ordering correctly noted moot | PASS |
| 22 | Sector cap absolute 18x for Banks/NBFCs/MFIs; no exit PE from outside Section 1B | Cap 18x applied; H = min(F2,G) = min(13.4,18) = 13.4x; no external PE anywhere | PASS |
| 23 | Sector-cap quality uplift only when UA triggered AND durability ≥ Moderate-Strong | UA not triggered → no uplift; stated | PASS |

### A6. Four-Pillar Summary + Dual-Track (both tracks carried)

| # | Rule | Applied | Verdict |
|---|---|---|---|
| 24 | Raw Destination PE = Quality base + Growth + Strategic; ±7.5% range, round to 0.5x (Amend 6) | F = 11.38+2+0 = 13.4x; range 13.4 ±7.5% = 12.5-14.5x (correct rounding) | PASS |
| 25 | BOTH tracks (Additive + RRM) produced and carried through EVERY fair value + verdict card | Track 2 Additive 13.4x (12.5-14.5x) and Track 1 RRM 10.0x (9.5-11.0x) present in Sec 1B, Sec 3 targets, Sec 4A/4H, and YAML | PASS |
| 26 | RRM = 1+(13.5−r)×0.12, percentage-point reading (Amend 4.4), bounded ×0.70-×1.60 | r=14.5%; RRM = 1+(13.5−14.5)×0.12 = 0.88; percentage-point reading correct; within bounds | PASS |
| 27 | Base r small/micro 14%, adjusted for durability/governance, bounded [9%,18%] | 14% base +0.5% (asset-quality stress + shared-catalyst SPOF, tempered by AA-) = 14.5%; in bounds | PASS |
| 28 | RRM track capped at (quality-uplifted) sector cap | 10.0x < 18x, no cap bind | PASS |
| 29 | On >15% divergence, state which track more appropriate; MORE CONSERVATIVE governs entry | Divergence 29%; RRM (10.0x) named more conservative/appropriate; for lenders P/B primary governs decision, entry set by conservative P/B base 337 | PASS |

Observation (MINOR, advisory): Track 1 uses "Fundamental Base PE" = the quality-adjusted base
(11.38x) rather than the additive Raw PE (13.4x): 11.38 × 0.88 = 10.0x. The Master term
"Fundamental Base PE" is not defined unambiguously; using the pre-premium quality base (so RRM
replaces, rather than stacks on, the additive premiums) is the conservative reading and the one
that maximises the AVOID margin. Had the raw 13.4x been used, Track 1 = 11.8x and divergence
would fall to ~12% (<15%). Either reading leaves P/B primary governing and the decision
unchanged. Logged as interpretive, not a misapplication.

### A7. Hurdle Ratio (Section 1B sanity check + Amendment 4.3 tier)

| # | Rule | Applied | Verdict |
|---|---|---|---|
| 30 | HR = (1+EPS CAGR)³ × (Dest PE mid ÷ Current PE); Tier A pass ≥1.953 | HR(Base) = (1.141)³ × (13.4/13.0) = 1.4858 × 1.0308 = 1.53; HR(Bull) = (1.228)³ × 1.0308 = 1.91. Both < 1.953 → STOP. Recomputed: matches | PASS |
| 31 | Bull EPS CAGR usable only if credibility grade A/B; else Base+5% max (Amend 2 gate) | Grade B → Bull (22.8%) permitted. Gate honored | PASS |
| 32 | EPS-CAGR basis consistent with the PE basis used | EPS CAGR 14.1% consolidated (24.97→37.1); Current PE 13.0x on consolidated 24.97 — bases consistent | PASS |
| 33 | Two-tier hurdle (Amend 4.3): Tier B only if FII+DII≥3% AND Gate0 GOOD+/EM≥25 AND promoter TRUSTWORTHY+ AND no structural FLAG-CASH; else Tier A 25% | FII+DII≥3% but Gate0 AVERAGE + EM 22 fail Tier B gate → Tier A 25%, divisor 1.953. Correct | PASS |
| 34 | Verdict card first line states "Tier: [A/B] \| Hurdle: [25%/20%]" (Amend 4.3) | 4H first line: "Tier: A \| Hurdle: 25% CAGR" | PASS |

Robustness (compliant, not required): STOP shown to hold on reported PE 14.4x (bull HR 1.72)
and RRM 10.0x (base HR 1.14); the only near-CONDITIONAL basis (standalone 12.3x) is rejected
under conservative bias and the authoritative consolidated basis. Conservative-bias rule honored.

### A8. P/B primary + methods + unresolved inputs

| # | Rule | Applied | Verdict |
|---|---|---|---|
| 35 | P/B (theoretical P/B = ROE ÷ CoE) is PRIMARY for lenders; destination PE SECONDARY cross-check (Amend 7) | P/B weighted 70% PRIMARY; theoretical P/B base = 14.0/14.5 = 0.97x; PE tracks are cross-checks; entry governed by P/B | PASS |
| 36 | Destination PE explicitly treated as cross-check, not decision driver | Additive PE flagged as ceiling (implied exit P/B 1.88x >> theoretical 0.97x); RRM corroborates P/B | PASS |
| 37 | Every unresolved input handled by a stated conservative rule; no silent fills (CLAUDE.md) | R4 table: DPS→0 (generous, flagged, hurdle still STOP); peer medians→no peer premium; EV/FCF→N/A lender; FII+DII exact→moot. All explicit | PASS |
| 38 | SOM cross-check performed | 2D: base revenue CAGR 20% vs SOM-implied 26% ceiling → consistent | PASS |
| 39 | Entry math: Tier A entry = FV ÷ 1.953; MoS 20% below (Amend 4.3 cascade) | 337÷1.953 = Rs 173; 337÷2.197 = Rs 153 (30%); MoS 173×0.8 = Rs 138 | PASS |
| 40 | SHARED CATALYST flag set when one catalyst drives multiple pillars | SET: credit-cost normalisation drives Pillar 1 ROE recovery AND Pillar 2L band; handed to Role 3 | PASS |

Observation (compliant): the framework's shared-catalyst illustration pairs Pillar 1 with
Pillar 3; B11 flags the genuine single point of failure (Pillar 1 + Pillar 2L). This is the
correct, substance-over-form application for a lender — credit-cost normalisation is the real
shared dependency. No issue.

═══════════════════════════════════════════════════════════════════
## PART B — ROLE 2 (B14) DECISION RULES + POSITION SIZING (EXTENDED SCOPE)
═══════════════════════════════════════════════════════════════════

Audited against Master v3.3 Role 2 Section 7 decision rules, position-size rules, entry
conjunction, and 4D probability weights.

| # | Rule | Applied in B14 | Verdict |
|---|---|---|---|
| 41 | AVOID if Gate0 AVERAGE/AVOID OR Promoter CONCERN/AVOID OR U/D <2x OR Hurdle STOP | AVOID on THREE independent grounds: Gate0 AVERAGE; U/D 0.17x <2x; Hurdle STOP. Correct | PASS |
| 42 | Hardest verdict wins when outputs contradict (FTTCP +4 lean vs valuation) | FTTCP +4 "DEEP WATCH leaning BUY-ON-DIPS" read as BUSINESS trajectory; price verdict AVOID governs (hardest verdict). Correct | PASS |
| 43 | U/D ratio = base upside / bear downside, floor 2x | +3.7% / 21.8% = 0.17x; fails floor. Correct construction | PASS |
| 44 | 4D probability weights from credibility grade; Good (B) → 25/50/25 | Grade B → 25/50/25 applied | PASS |
| 45 | Position size Large gate: Gate0 EXCELLENT + Promoter EXEMPLARY/TRUSTWORTHY + EM EXPANSION + <MoS | Fails all → not Large. Correct | PASS |
| 46 | Medium gate: Gate0 GOOD+ + Promoter TRUSTWORTHY + CMP ≤ Entry | Fails (Gate0 AVERAGE; Promoter CAUTION; CMP >> Entry) → not Medium. Correct | PASS |
| 47 | Small = everything else qualifying as BUY; promoter caps bind | Small (2-3%), and only at the Rs 153-173 entry zone; Promoter CAUTION applied as a sizing cap | PASS |
| 48 | Entry conjunction (anti-value-trap) stated explicitly in Section 7 box | Stated: zone withdrawn if price falls BECAUSE credit cost >3.2% + GNPA >1.5% | PASS |
| 49 | Never estimate a missing number (5yr FV not produced by Role 1) | 5yr FV marked "NOT COMPUTED by Role 1", not estimated. Correct (no silent fill) | PASS |
| 50 | Tier A entry math carried consistently into thesis | Entry 153-173, MoS 138, Hurdle STOP carried from B11 unchanged | PASS |

Observation (MINOR, advisory): Promoter verdict is CAUTION (B08), an intermediate,
pipeline-specific tier. The Master's forcing rule names CONCERN/AVOID; CAUTION does not force
AVOID. B14 correctly treats CAUTION as non-forcing on the verdict but binding as a
position-size cap (blocks Medium/Large). This is the conservative reading and is immaterial
to the outcome (verdict is AVOID on three other grounds; sizing is Small only at the entry
zone). Compliant.

═══════════════════════════════════════════════════════════════════
## PART C — RECOMPUTATION & CONCLUSION
═══════════════════════════════════════════════════════════════════

Independent recomputation reproduces every load-bearing figure:
- Pillar 1 ROE 13.46% → base 14.2x
- Quality-adjusted base 11.4x (× 0.80)
- Raw/Destination PE 13.4x (additive), RRM 10.0x, range concurs
- Hurdle HR(Base) 1.53 / HR(Bull) 1.91 → STOP
- Entry Rs 153-173, MoS Rs 138; U/D 0.17x
- Decision AVOID (on valuation)

No misapplication changes the destination PE by >1x, flips the Hurdle verdict, or flips the
decision. **recomputed_destination_pe: concur (blank). recomputed_decision: concur (blank).**

Three MINOR interpretive observations logged (Pillar 3 3a SOM-qualifier provenance; Track 1
"Fundamental Base PE" term ambiguity; Promoter CAUTION tier handling). None is a rule
misapplication; each is either an admissible reading or immaterial to the STOP/AVOID outcome.
No CRITICAL, no MAJOR.

Numerical note (deferred to Verifier A, NOT scored here): the 4D weighted-return column
(-1.98 + 0.60 + 2.30 = +0.92%) sums slightly below the reported "~+1.3%". This is an
arithmetic figure, not a framework-application matter, and does not affect the decision
(every method is far below the 25% Tier A hurdle).

Gate 0 (B01) and Emerging Moat (B07) adherence were audited in Phase 1 and are not re-run here.

```yaml
stage: B12c-phase3
company: "NORTHARC"
run_date: "2026-07-12"
model: claude-opus-4-8
status: complete
scope: "phase3-valuation-adherence (B11) + Role 2 decision/sizing (B14); gate0/emoat deferred to phase1"
gate0: "completed phase 1 — not re-run"
emoat: "completed phase 1 — not re-run"
valuation: {rules_checked: 50, fails: []}
recomputed_destination_pe: ""   # concur — 13.4x additive / 10.0x RRM reproduced
recomputed_decision: ""         # concur — AVOID (on valuation); Hurdle STOP
findings:
  - {severity: "MINOR", location: "B11 Pillar 3 3a (+2x)", note: "SOM-implied CAGR qualifier rests on B09 TAM inference; admissible because Amend 4.1 lists SOM-implied CAGR as an eligible qualifier and capacity cross-check passes for >=20%. Immaterial: v3.3 floor +0x still yields 11.4x -> STOP/AVOID."}
  - {severity: "MINOR", location: "B11 RRM Track 1 (10.0x)", note: "'Fundamental Base PE' taken as quality-adjusted base 11.38x (x0.88) not additive raw 13.4x; Master term ambiguous. Conservative reading; P/B primary governs regardless; decision unchanged."}
  - {severity: "MINOR", location: "B14 Section 7 position sizing", note: "Promoter CAUTION (pipeline-specific tier) treated as non-forcing on verdict but binding as sizing cap. Conservative and immaterial — AVOID stands on Gate0/U-D/Hurdle grounds."}
critical_count: 0
major_count: 0
minor_count: 3
acceptance_rate: 100            # 50 rules passed / 50 checked; 3 MINOR advisory notes (no rule failed)
coverage_note: "Full Sec 1B lender-adapted rule set (Pillars 1/2L/3, Strategic, UA/Amend 3, sector cap, dual-track/RRM Amend 4.4, Hurdle/Amend 2, Tier/Amend 4.3, P/B-primary/Amend 7, unresolved-input discipline, single-credit/Amend 4, SOM cross-check) plus Role 2 AVOID triggers, position sizing, entry conjunction, 4D weights. Numbers deferred to Verifier A; Gate0/EMoat deferred to Phase 1."
```
