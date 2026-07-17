# B12c — VERIFIER C: FRAMEWORK ADHERENCE (PHASE 3, VALUATION-ADHERENCE AUDIT)

**Company:** Gaudium IVF and Women Health Ltd (GAUDIUMIVF)
**Run date:** 2026-07-16 | **Model:** claude-opus-4-8 | **Stage:** B12c (phase-3 extension)
**Scope:** Valuation adherence of B10 (val-inputs) + B11 (Role 1 valuation) against Section 1B v3.3 / Master v3.3 / FTTCP v1.2, EXTENDED to Role 2 (B14) decision rules and position sizing. Gate 0 (B01) and Emerging Moat (B07) checks ran in phase 1 and are carried forward unchanged.
**Not in scope:** raw-number accuracy (Verifier A) and company quality. This audit tests rule application only.

---

## CARRY-FORWARD FROM PHASE 1 (unchanged)

- **Gate 0 (B01):** 39 rules re-derived, 0 hard fails. Two MINOR findings recorded (RHP KPI definitions used for RoCE/RoE where screener CSVs were empty — A3 band unchanged; M2/M5/M9 peer-test asymmetry — moat count unchanged). Classification **AVERAGE** stands.
- **Emerging Moat (B07):** 13 rules checked, 1 MAJOR fail (the `stage: B07-emoat` closing YAML block was never emitted; prose content intact, no score/decision change). Classification **MODEST (13/80)** stands.
- Phase-1 result: 51 passed / 52 checked on the two sections; the prior block reported 98% adherence.

---

## VALUATION AUDIT (B10 / B11) — RULE-BY-RULE

### Pillar 1 — ROCE Base

| # | Rule (as written) | Applied in B11 | Verdict |
|---|---|---|---|
| V1 | Continuous formula, not old bands (Amdt 5 / Master §Pillar 1) | 0.5×37+7.5 = 26, capped 24 → 24.0x | PASS |
| V2 | ROCE input = deliberation-authoritative operating ROCE 37%, NOT reported 20.11% | 37.0% operating, surplus removed (Override 1); explicitly rejects 20.11% | PASS |
| V3 | FTTCP ROCE forward verdict is the sole Pillar-1 authority; SUSTAINED-premium → current ROCE (maps to FIRING/STAGNANT row = current ROCE) | Used current 37% per SUSTAINED verdict; no ad-hoc trajectory blend | PASS |
| V4 | Amendment 4.5 normalized anchor applies ONLY to TEMPORARILY DEPRESSED + RECOVERING | Correctly NOT applied (verdict is SUSTAINED, not depressed) — stated | PASS |
| V5 | Surplus cash valued separately, not double-counted | ~Rs 81 Cr removed from ROCE denominator to get 37%; NOT re-added at Year-3 exit (deployed into hubs, captured in FY30E EPS). "One asset, one mechanism" guard stated in §1A | PASS |

**Pillar-1 note (MINOR, framework-internal conflict).** Section_1B_v3.3 Amendment 5 caps the base at **24x** (`0.5×ROCE+7.5`). Master_Project_Prompt_v3.3 §Pillar 1 (lines 211-214) carries a **second branch** for ROCE>33%: `Base PE = 24 + 0.3×(ROCE−33), cap 30x`, with reference point `40% → 26x`. At 37% that branch yields **25.2x**, not 24.0x. B11 took the Amendment-5 cap-24 read — the more conservative branch and the one the phase-3 task itself names ("cap 24x"). Under the Master two-branch read the chain would be 25.2×0.80 = 20.16x quality base → raw 23.16x → dest ~23x. Impact on final destination PE: +0.96x (below the >1x CRITICAL threshold); HR base rises 1.32→1.38, bull 1.49→1.55, both still < 1.953 → **STOP unchanged, decision unchanged.** Recorded as MINOR; B11's choice is defensible and conservative.

### Pillar 2 — Cash Conversion Multiplier

| # | Rule | Applied | Verdict |
|---|---|---|---|
| V6 | Multiplier matches the stated determination | INDETERMINATE (deteriorating), CFO/PAT 0.30x FY26, receivable days ~187 → 0.80x (deliberation p.19/p.72) | PASS |
| V7 | No growth offset when not a clean pass / INDETERMINATE | No offset applied; INDETERMINATE never resolves to clean pass | PASS |
| V8 | Offset rules / structural handling | 0.80x is stricter than a pure band-read (cumulative CFO/PAT 64.1% → 1.15x band; latest 0.33x → 1.00x band); the conservative 0.80x is the operator determination on deteriorating trajectory, consistent with "never let INDETERMINATE silently resolve to PROCEED" | PASS |

Note: 0.80x is below what either the cumulative (64.1% → 1.15x) or the latest-FY (0.33x → 1.00x) Pillar-2 band would produce. The pipeline applied the conservative INDETERMINATE-deteriorating determination (deliberation authority) rather than the mechanical band, which is stricter, not looser — compliant.

### Pillar 3 — Growth (decoupled v3.4)

| # | Rule | Applied | Verdict |
|---|---|---|---|
| V9 | 3a Growth Visibility via decoupled rules, 📄 evidence, +2x if any two qualify, C caps 3a at +2x | +2x on (i) capex-embedded 335% and (ii) SOM-implied CAGR 31.4%>20% with capacity check; held at +2x by C-cap | PASS (see MINOR) |
| V10 | 3b Moat Formation gated on EM; EM 13 < 25 threshold → +0x | +0x | PASS |
| V11 | 3c Duration Premium requires ≥2.5yr 📄 order book / contracted revenue | +0x (no order book) | PASS |
| V12 | Strategic Premium within band, not a monopoly | +1x (founder brand + ART-Act licence), below the +2/+4x franchise band | PASS |
| V13 | Single-credit rule: ROCE recovery credited via Pillar 1 OR Strategic, never both; route stated | "ROCE recovery credited via: Pillar 1"; Strategic ROCE re-rating explicitly BARRED | PASS |
| V14 | Shared-catalyst flag when Pillar-1 catalyst = Pillar-3 catalyst | SHARED CATALYST = TRUE (IPO cash → hubs drives both ROCE and 3a growth) | PASS |

**Pillar-3a note (MINOR).** Amendment 4.1 3a pays +2x only when **two** 📄 qualifiers hold. Of the four listed tests, only the SOM-implied CAGR 31.4% (with capacity cross-check) is a clean qualifier here; the capex-embedded-growth 335% is flagged by B10 itself as "framework formula not decision-useful for asset-light lease model," order-book is N/A, and delivery grade is C. A strict read gives one qualifier → +0x. The +2x is held by **operator Override 2** (deliberation, authoritative; B14 §4 cross-ref), which counts the documented IPO hub earmark as the second qualifier, C-capped at +2x. Recorded as MINOR: the +2x rests on a documented operator override rather than two independently clean 📄 tests. No decision impact (destination already STOP).

### Undiscovered Alpha, Sector Cap, Hurdle

| # | Rule | Applied | Verdict |
|---|---|---|---|
| V15 | UA applies only if all three qualifiers hold (listed ≥12m; Gate0≥60 OR EM≥25; FII+DII<3%) | Listed ~5m (NO); Gate0 AVERAGE / EM 13 (NO); FII+DII 5.23% (NO). All three fail → UA NOT applied | PASS |
| V16 | UA ordering min(F×1.25, Cap), BEFORE the cap; never engages when unqualified | F2 = F = 22.2x (no ×1.25); ordering never engages | PASS |
| V17 | Sector cap absolute; Hospitals/healthcare 35x | H = min(22.2, 35) = 22.2x; cap not binding, not breached | PASS |
| V18 | Proportional ±7.5% range (Amdt 6) | 22.2 ±7.5% = 20.5x–24.0x | PASS |
| V19 | Hurdle Ratio = (1+EPS CAGR)³ × (dest mid ÷ current PE), threshold 1.953 (Tier A) | Base 1.9531×(22/32.5)=1.32; Bull 2.197×(22/32.5)=1.49 | PASS |
| V20 | Current PE on the one-year-forward basis (Override 3) | 137/4.2125 (FY27E EPS) = 32.5x | PASS |
| V21 | Bull EPS CAGR capped at Base+5% when grade is C (Amdt 2 conservative-bias note) | Bull 30% = 25%+5%, grade C | PASS |
| V22 | HR(Bull) < 1.953 → STOP | Both rows < 1.953 → STOP, derived on forward basis | PASS |

### Dual Track, Entry, MoS, Triangulation

| # | Rule | Applied | Verdict |
|---|---|---|---|
| V23 | BOTH tracks produced (additive + RRM) and carried through | Track 2 additive 20.5–24x; Track 1 RRM 12.5–14.5x; both in verdict card and FV matrix | PASS |
| V24 | RRM = 1 + (13.5−r)×0.12, percentage-point reading (Amdt 4.4), bounds ×0.70–×1.60 | r=16% (base 14% + promoter CONCERN/INDETERMINATE/<1yr, bounded [9,18]); RRM = 1+(−2.5)(0.12) = 0.70 | PASS |
| V25 | RRM destination = fundamental base × RRM | 19.2 × 0.70 = 13.4 → 13.5x (quality-adjusted base used; durability/governance priced through r) | PASS |
| V26 | Tier A entry = base FV ÷ 1.953 | 181 ÷ 1.953 = 92.7 → zone Rs 90–93 | PASS |
| V27 | MoS = 20% below entry | 0.80 × 92.7 = 74.2 → Rs 74 | PASS |
| V28 | Conservative track governs entry on >15% divergence (Section 1B default) | Divergence 38.6% (>15%); default → RRM governs. B11 OVERRODE to additive (deliberation p.74) | **FAIL (override)** |
| V29 | SOM cross-check performed | Base 25% < SOM-implied 31.4%; capacity check passes | PASS |
| V30 | EV/EBITDA secondary cross-check | 0.65×22 ≈ 14.5x → Rs 180, agrees with PE Rs 181 (<1% divergence) | PASS |
| V31 | Unresolved inputs handled by conservative rule, no silent fills | Margin NOT FOUND → held flat 36.13%; peer medians NOT FOUND → no relative method; 3yr CAGR NOT FOUND → 25% deliberation, SOM-crosschecked. All declared | PASS |
| V32 | Tier assignment mechanical (Amdt 4.3) | Tier B gates fail (Gate0 AVERAGE, Promoter CONCERN, FLAG-CASH) → stays Tier A 25% | PASS |

**V28 finding (MAJOR).** The Section 1B v3.3 default on >15% track divergence is that the **more conservative (RRM) track governs the entry zone**. B11 instead let the **additive** track govern, on an explicit, recorded operator override (deliberation p.74), retaining RRM as a "conservative floor." This is authoritative per CLAUDE.md, so it is not a silent misapplication — but it is a departure from the written default that is fully load-bearing on the actionable output: entry rests on Track 2 (Rs 181 base FV → entry Rs 90–93). Had the default governed, entry off Track 1 base FV Rs 111 would be **111 ÷ 1.953 ≈ Rs 57**, MoS ~Rs 45. The buy/no-buy decision at CMP is unchanged (STOP either way), but the entry zone the operator will act on is ~60% higher than the framework default would set. Surfaced MAJOR so the operator sees the entry-price sensitivity rests entirely on the override.

---

## ROLE 2 AUDIT (B14) — DECISION RULES & POSITION SIZING

| # | Rule (Master v3.3 Role 2) | Applied in B14 | Verdict |
|---|---|---|---|
| R1 | Verdict per decision rules | See finding below | **FAIL (override)** |
| R2 | Entry consistent with B11 | Rs 90–93, MoS Rs 74 — matches B11 | PASS |
| R3 | Position size: Promoter Verdict caps always bind; Large/Medium gates fail | Gate0 AVERAGE + Promoter CONCERN → neither Large nor Medium; Promoter CONCERN cap binds → **Small (2-3%)**, conditional on reaching zone | PASS |
| R4 | Tier A / hurdle 25% consistent | Tier A, 25%; UA not applied (listed <12m, FII+DII 5.23%) | PASS |
| R5 | Hurdle STOP → not BUY | Verdict is WATCHLIST, not BUY | PASS |
| R6 | Entry conjunction stated in Section 7 | Stated: buy only when price in Rs 90–93 AND latest checklist shows no thesis-broken trigger | PASS |
| R7 | Position-size override handling | `position_size_override` empty; consistent with no recorded override | PASS |

**R1 finding (MAJOR).** The Master v3.3 mechanical decision rules make this an **AVOID** at CMP on three independent triggers: Gate 0 AVERAGE (line 809), Promoter CONCERN ("AVOID regardless of everything else," lines 809 and 916), and Hurdle Ratio STOP (line 809). B14 returns **WATCHLIST**, reconciled against the authoritative FTTCP deliberation (p.63-64, operator-signed), which locks WATCHLIST because a reachable, thesis-intact entry zone (Rs 90–93) exists below CMP. B14 explicitly traces this in §7 ("At CMP the name is AVOID-on-valuation; the watchlist verdict carries the reachable entry"). The practical meaning — no buy at CMP — is preserved under both labels, and position sizing correctly stays capped at Small by the Promoter CONCERN cap. Recorded MAJOR: the verdict label departs from the mechanical AVOID the rules mandate, held by documented operator authority; decision-in-effect (no buy at CMP) survives.

---

## RECOMPUTE SUMMARY

- **Destination PE:** Concur with 22x mid (20.5–24x). The Master v3.3 two-branch Pillar-1 formula would lift the base to 25.2x → destination ~23x, a +0.96x move under the >1x CRITICAL threshold; Hurdle stays STOP. No recompute forced. B11's cap-24 read is the conservative, task-endorsed branch.
- **Decision:** Concur. No buy at CMP under every reading — Hurdle STOP holds under both Pillar-1 branches and under both tracks; the WATCHLIST-vs-AVOID label and the additive-vs-RRM entry are operator-authorized departures that do not change "no buy at Rs 137." Entry zone Rs 90–93 is contingent on the recorded operator override of the conservative-track-governs default (default would set ~Rs 57).

## SEVERITY TALLY (this section)

- CRITICAL: 0
- MAJOR: 2 (V28 conservative-track override; R1 verdict label vs mechanical AVOID)
- MINOR: 2 (Pillar-1 two-branch conflict; Pillar-3a thin second 📄 qualifier)

## ACCEPTANCE

- Valuation + Role 2 rules checked: 39 (32 valuation V1–V32 + 7 Role 2 R1–R7). Passed 37, fails 2. Section acceptance 94.9%.
- Overall across all checked rules (Gate 0 39 + EM 13 + Valuation/Role2 39 = 91 checked): 88 passed, 3 fails (EM YAML block; V28; R1). **Framework adherence ≈ 97%.**

---

```yaml
stage: B12c
company: "GAUDIUMIVF"
run_date: "2026-07-16"
model: claude-opus-4-8
status: complete
gate0: {rules_checked: 39, fails: []}
emoat:
  rules_checked: 13
  fails:
    - "B07 closing YAML block (stage: B07-emoat) NOT emitted; report ends at 'Input gaps carried forward'. Required by framework OUTPUT spec and CLAUDE.md 'done' definition; breaks machine-readable Pillar-3 handoff. Content present in prose; no value changed. MAJOR."
valuation:
  rules_checked: 39
  fails:
    - "V28 Conservative-track-governs default overridden: track divergence 38.6% (>15%) so Section 1B default is that the RRM (conservative) track governs the entry zone; B11 let the additive track govern on a recorded operator override (deliberation p.74). Authoritative, not silent, but load-bearing: entry Rs 90-93 rests on Track 2; default (Track 1 base FV Rs 111 / 1.953) would set entry ~Rs 57, MoS ~Rs 45. Buy/no-buy at CMP unchanged (STOP). MAJOR."
    - "R1 Role 2 verdict WATCHLIST vs mechanical AVOID: Master v3.3 lines 809/916 mandate AVOID at CMP on Gate 0 AVERAGE, Promoter CONCERN ('regardless of everything else'), and Hurdle STOP; B14 returns WATCHLIST reconciled to the authoritative FTTCP deliberation p.63-64 (reachable Rs 90-93 entry). No-buy-at-CMP preserved; position size correctly capped Small by Promoter CONCERN. MAJOR."
recomputed_destination_pe: ""   # concur 22x mid; Master v3.3 two-branch alt 25.2x base -> ~23x dest, +0.96x, below >1x threshold, Hurdle STOP unchanged
recomputed_decision: ""         # concur: no buy at CMP under every reading; Hurdle STOP holds on both Pillar-1 branches and both tracks
framework_adherence: 97         # overall across all checked rules: 88 passed / 91 checked (gate0 39 + emoat 13 + valuation/role2 39)
findings:
  - {severity: "MAJOR", location: "B07 §OUTPUT / end of report", claim: "B07-emoat closing YAML block required by framework", finding: "block absent; downstream structured EM handoff missing", recompute: "none — prose content intact, no score/decision change"}
  - {severity: "MAJOR", location: "B11 §1B RRM Dual-Track / §4A-4E", claim: "conservative (RRM) track governs entry on >15% divergence (Section 1B default)", finding: "divergence 38.6%; additive track governs via recorded operator override (deliberation p.74); entry Rs 90-93 rests on Track 2, not the conservative default", recompute: "default entry = 111/1.953 = ~Rs 57, MoS ~Rs 45; decision (no buy at CMP) unchanged"}
  - {severity: "MAJOR", location: "B14 §7 verdict box / recommendation", claim: "Promoter CONCERN + Gate0 AVERAGE + Hurdle STOP each mandate AVOID (Master lines 809, 916)", finding: "verdict returned as WATCHLIST via authoritative FTTCP deliberation p.63-64; departs from mechanical AVOID label", recompute: "no-buy-at-CMP preserved; position size Small (Promoter cap) correct; label-only departure, operator-authorized"}
  - {severity: "MINOR", location: "B11 Pillar 1 / §1B step A", claim: "ROCE base 0.5x37+7.5 capped 24 = 24.0x (Amendment 5)", finding: "Master v3.3 §Pillar 1 lines 211-214 carry a second branch for ROCE>33% (24+0.3x(ROCE-33), cap 30x) giving 25.2x at 37%; framework-internal conflict; B11 took the conservative cap-24 read", recompute: "two-branch dest ~23x (+0.96x); HR base 1.38 / bull 1.55, both < 1.953; STOP and decision unchanged"}
  - {severity: "MINOR", location: "B11 Pillar 3a / §1B step D", claim: "3a Growth +2x on two documented (📄) qualifiers, C-capped", finding: "only SOM-implied CAGR 31.4% is a clean 📄 qualifier; capex-embedded 335% is flagged by B10 as 'not decision-useful for asset-light', order-book N/A, grade C; strict read -> one qualifier -> +0x. +2x held by operator Override 2 (documented IPO earmark as second qualifier)", recompute: "if +0x, raw dest 20.2x; Hurdle still STOP; decision unchanged"}
  - {severity: "MINOR", location: "B01 Block A", claim: "RoCE/RoE per stated framework formulas", finding: "RHP KPI definitions used (RoCE denom NW+Borrow+Lease+DTL; RoE closing NW) instead of framework defaults; source-permitted as screener CSVs empty; A3 band unchanged", recompute: "A3=5 on either basis"}
  - {severity: "MINOR", location: "B01 Block F M2/M5/M9", claim: "peer-dependent moat tests", finding: "M2 credits foreign-peer EBITDA (score 5) while M5/M9 mark PEER DATA NEEDED; defensible under 'score 0 only if peer data not provided' but asymmetric", recompute: "no change; moat count stays 3"}
critical_count: 0
major_count: 3
minor_count: 4
acceptance_rate: 97             # rules passed / rules checked, all sections: 88 / 91
coverage_note: "Phase 3 valuation-adherence audit of B10/B11 vs Section 1B v3.3 / Master v3.3 / FTTCP v1.2, extended to Role 2 (B14) decision rules and position sizing. Gate 0 (B01) and Emerging Moat (B07) carried forward from phase 1 unchanged. Audited rule application, not raw-number accuracy (Verifier A) nor company quality. Two MAJOR items (V28 conservative-track override; R1 WATCHLIST-vs-AVOID) are documented operator overrides, authoritative per CLAUDE.md; both preserve no-buy-at-CMP but are load-bearing on the actionable entry zone and verdict label, so surfaced. No CRITICAL: destination PE and the Hurdle STOP decision hold under every alternative reading tested."
```
