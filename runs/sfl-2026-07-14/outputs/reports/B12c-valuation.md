# B12c — VERIFIER C (FRAMEWORK ADHERENCE): VALUATION SECTION (PHASE 3)

**Company:** Sheela Foam Ltd (SFL) | **Run date:** 2026-07-14 | **Model:** claude-opus-4-8
**Scope:** Deferred valuation-adherence audit, EXTENDED to Role 2 decision rules and position sizing.
**Artifacts audited:** B10 (val input assembly), B11 (Role 1 dual-track valuation), B14 (Role 2 thesis).
**Authorities:** Master v3.3 (Role 1 Four-Pillar, RRM, Role 2), Section 1B v3.3 Amendments, FTTCP v1.2.

> Gate 0 (B01) and Emerging Moat (B07) adherence were audited in Phase 1 and are NOT re-checked here. This report emits the valuation-adherence section only; it merges with the Phase-1 gate0+emoat findings under the same B12c stage.

---

## SUMMARY VERDICT

**Framework adherence (valuation + Role 2): HIGH.** Every pillar, the UA ordering, the sector cap, both RRM tracks, the Hurdle Ratio, the tier assignment, and the Role 2 decision-and-sizing rules were applied as written. Zero CRITICAL, zero MAJOR. Three MINOR advisory findings, all disclosed judgment calls that are decision-neutral (the STOP / AVOID-on-valuation verdict survives on every alternative basis). **I concur with destination PE 17.8x additive / 16.7x RRM and with the AVOID-on-valuation decision.** No recompute required.

---

## PILLAR 1 — ROCE BASE MULTIPLE

| # | Rule | Framework anchor | Applied? | Recompute |
|---|---|---|---|---|
| P1-1 | FTTCP ROCE forward verdict is SOLE Pillar 1 authority | FTTCP v1.2 Pillar 1 Integration | PASS | — |
| P1-2 | RECOVERING @ 40-60% → 60/40 weighted avg of current & FY[Y+2] | FTTCP v1.2 table row 3 | PASS | 0.6×13.0 + 0.4×16.0 = 14.2% ✓ |
| P1-3 | Continuous formula 0.5×ROCE+7.5, floor 9 / cap 24 | Amendment 5 | PASS | 0.5×14.2+7.5 = 14.6x ✓ |
| P1-4 | Base-ROCE choice reasoned (operating/tangible 13%, not reported 6.7%, not pre-acq 17%) | fttcp-deliberation cross-cutting note; B10 stage-11 note | PASS (MINOR note) | see F1 |
| P1-5 | Amendment 4.5 normalized anchor correctly NOT applied | Amendment 4.5 (📄-gated unwind catalyst) | PASS | — |
| P1-6 | Single-credit: recovery via Pillar 1, Strategic Premium ROCE re-rating BARRED, route stated | Amendment 4 / FTTCP v1.2 single-credit | PASS | — |

**Detail.** The verdict is RECOVERING ~55% (40-60% band), which maps to the 60/40 blend row, not the >60% midpoint row. B11 read the blend as 60% current / 40% FY[Y+2] — the conservative reading (weights the trough) and the natural reading of "60/40 of current and FY[Y+2]." 0.6×13.0 + 0.4×16.0 = 14.2%; 0.5×14.2 + 7.5 = 14.6x. Both correct.

**Amendment 4.5 (P1-5).** The amendment applies ONLY when the backward verdict is TEMPORARILY DEPRESSED AND forward is RECOVERING, AND both the pre-depression ROCE series and a specific mechanical unwind catalyst are 📄-evidenced. B11 correctly declines: the pre-acquisition ~17% sat on a smaller goodwill-free base that no longer exists, so the Kurlon goodwill re-basing is permanent, not a self-reversing capital-cycle trough — the unwind catalyst to 17% is absent/barred. This is the framework-sound call. Note that applying 4.5 would have RAISED the ROCE anchor (40% normalized 17% + 30% FY28 16% + 30% current 13% = 15.5% vs the 14.2% used), so declining it is the more conservative outcome as well.

**Single-credit (P1-6).** Worksheet states "ROCE recovery credited via: Pillar 1 (single credit). Strategic Premium ROCE re-rating is BARRED." FTTCP v1.2 permits the Strategic Premium route only for STAGNANT/FIRING verdicts; RECOVERING correctly bars it. Honored.

---

## PILLAR 2 — CASH CONVERSION MULTIPLIER

| # | Rule | Framework anchor | Applied? |
|---|---|---|---|
| P2-1 | Multiplier matches stated determination (FIRING, growth-induced) | Master Pillar 2; fttcp-deliberation ruling #4 | PASS |
| P2-2 | Elite band 1.30x tempered to conservative 1.15x with reasons | fttcp-deliberation ("default 1.15x if uncertain") | PASS |
| P2-3 | No separate growth-offset added on high conversion (avoids double-credit) | Master Pillar 2 offset rule | PASS |
| P2-4 | No offset on structural | Master (offset attaches to 0.80x drag band only) | PASS (N/A — growth-induced, high conversion) |

**Detail.** Cash conversion is FIRING (CFO/PAT 2.56x latest, 1.37x cumulative, FCF +212.49 Cr) — strictly clears the elite band. The 1.15x is the deliberation-sanctioned conservative default, justified by (a) the absent rating PDF (HIGH-severity gap — the CARE/CRISIL/ICRA structural-WC assessment that would be the Pillar 2 precedence authority is missing) and (b) the +27.7% growth-induced receivables build. `growth_offset = 0` is correct: the offset attaches only to the low-conversion 0.80x drag band, so adding one here would double-credit. QA base 14.6 × 1.15 = 16.8x ✓. FLAG-CASH carried forward.

---

## PILLAR 3 — GROWTH VISIBILITY PREMIUM (Amendment 4.1/4.2 decoupled)

| # | Rule | Framework anchor | Applied? | Recompute |
|---|---|---|---|---|
| P3-1 | 3a on 📄-documented qualifiers; +2x needs any two; grade B does not cap | Amendment 4.1 | PASS | Only 1 qualifier (grade B) → +0x ✓ |
| P3-2 | 3b EM-gated table: EM 25-29 → +1x | Amendment 4.1 (3b) / injected EM 27 | PASS | +1x ✓ |
| P3-3 | 3c Duration: 📄 order book ≥2.5yr for +1x | Amendment 4.2 | PASS | none → +0x ✓ |
| P3-4 | Combined 3a+3b+3c ≤ +6x cap | Amendment 4.1 | PASS | +1x ≤ +6x ✓ |
| P3-5 | SHARED CATALYST flag raised | Amendment 4 / FTTCP single-credit | PASS | — |

**Detail.** 3a: SOM CAGR 15.6% (<20%, fails), no order book, capex-embedded ≥15% not documented, management grade B (the single passing qualifier). One qualifier only → +0x (two required for +2x). 3b: EM 27 STRENGTHENING → +1x per the 25-29 band, matching the injected deliberation input. 3c: no documented ≥2.5yr contracted revenue → +0x. Pillar 3 = +1x, inside the +6x cap. SHARED CATALYST (Kurlon integration + deleveraging driving Pillar 1 ROCE, margin, and Pillar 3) correctly flagged for Role 3 stress-test.

---

## STRATEGIC PREMIUM

| # | Rule | Anchor | Applied? |
|---|---|---|---|
| SP-1 | ROCE re-rating route barred (single-credit) | Amendment 4 | PASS |
| SP-2 | Brand/franchise gate needs limited competition AND documented pricing power | Section 1B strategic premium gate | PASS (both sub-conditions fail → +0x) |

Competition is not limited (Wakefit, Duroflex, large unorganized) and pricing power is not documented (H1 RM shock crushed margins; showroom target missed 3x). +0x is correct.

---

## UA MULTIPLIER & ORDERING

| # | Rule | Anchor | Applied? |
|---|---|---|---|
| UA-1 | UA applies only when all three qualifiers hold | Amendment 3 / Master line 334 | PASS |
| UA-2 | Institutional-absence qualifier: FII+DII <3% | Amendment 3 | PASS (24.70% > 3% → fails → UA NOT applied) |
| UA-3 | Ordering min(Raw×1.25, Cap), F2 = F when unqualified | Amendment 3 | PASS (F2 = F = 17.8x) |

FII+DII 24.70% (an institutional REDUCTION from ~31%) is far above the 3% institutional-absence threshold, so the UA qualifier fails and no 1.25x is applied. Correctly, low institutional ownership is NOT treated as a risk (CLAUDE.md), and the UA multiplier simply does not engage. Ordering respected — the 1.25x would attach to Row F before the cap comparison; here F2 = F.

---

## SECTOR CAP

| # | Rule | Anchor | Applied? |
|---|---|---|---|
| SC-1 | Building materials 22x is a genuine Section 1B row | Master v3.3 Sector Cap Table, line 361 ("Building materials | 22x") | PASS |
| SC-2 | Manifest "Agri processing 20x" correctly overridden to Building materials 22x | fttcp-deliberation ruling #5 | PASS |
| SC-3 | Cap absolute (min applied); non-binding here | Amendment 3 / Master | PASS (min(17.8, 22.0) = 17.8x) |
| SC-4 | No exit PE sourced outside Section 1B | CLAUDE.md NEVER rule | PASS |

**Detail — important confirmation.** The 22x is NOT invented by the deliberation: it is the literal Master v3.3 sector-cap row for Building materials (line 361). The deliberation's role was only to correct the manifest's mis-classification ("Agri processing 20x") to the correct sector. Fully compliant, and non-binding since raw 17.8x sits below the cap. No quality uplift applied (UA not triggered), which is correct.

---

## DUAL-TRACK RRM

| # | Rule | Anchor | Applied? | Recompute |
|---|---|---|---|---|
| RRM-1 | BOTH tracks computed and carried through every fair value + verdict card | Master RRM Dual-Track | PASS | — |
| RRM-2 | RRM = 1 + (13.5 − r) × 0.12, percentage-point reading | Amendment 4.4 | PASS | 1 + (13.5−14)×0.12 = 0.94 ✓ |
| RRM-3 | r derivation: mid-cap base 13%, governance CAUTION adjustment, bounded [9,18] | Master RRM | PASS | r = 14% ✓ |
| RRM-4 | Track 1 = Fundamental Base PE × RRM, capped at cap | Master RRM | PASS (MINOR note) | 17.8 × 0.94 = 16.7x; see F2 |
| RRM-5 | Proportional ±7.5% ranges | Amendment 6 | PASS | 16.7→15.5-18.0; 17.8→16.5-19.0 ✓ |
| RRM-6 | On >15% divergence conservative track governs entry | Master RRM | PASS | divergence 6.2% (<15%); conservative Track 1 chosen anyway ✓ |

**Detail.** RRM 0.94 uses the percentage-point reading required by Amendment 4.4 (r=14% gives 13.5−14 = −0.5, not −0.005). r = mid-cap 13% + 1% governance premium for the promoter CAUTION verdict = 14%, inside [9,18]. Divergence is only 6.2%, so the >15% conservative-override does not bind; B11 nonetheless governs on the more conservative Track 1 (16.7x), which is acceptable and prices the governance discount. Both tracks are carried through the fair-value grids and the verdict card.

---

## HURDLE RATIO & TIER

| # | Rule | Anchor | Applied? | Recompute |
|---|---|---|---|---|
| HR-1 | HR = (1+EPS CAGR)³ × (Dest PE mid ÷ Current PE) | Amendment 2 / Master | PASS | — |
| HR-2 | Consistent EPS basis (reported vs cash not mixed) | Amendment 2 / B11 Section 3 | PASS | current PE & EPS CAGR both reported ✓ |
| HR-3 | Current PE reported 55.2x, base 3yr EPS CAGR 37.9% | — | PASS | 807/14.62=55.2; (38.3/14.62)^⅓−1=37.9% ✓ |
| HR-4 | HR(base) = 2.623 × 0.3025 = 0.79 | — | PASS | 0.79 ✓ FAILS |
| HR-5 | Bull EPS permitted only if grade A/B; HR(bull) computed | Amendment 2 conservative note | PASS | grade B → bull permitted; 3.348×0.3025 = 1.01 ✓ |
| HR-6 | HR(bull) < 1.953 → STOP | Amendment 2 table row 3 | PASS | 1.01 < 1.953 → STOP ✓ |
| HR-7 | Tier assignment: Tier B needs promoter TRUSTWORTHY+ | Amendment 4.3 | PASS | CAUTION → Tier B fails → Tier A, divisor 1.953 ✓ |
| HR-8 | Entry = FV ÷ 1.953; MoS = 20% below entry | Amendment 4.3 | PASS | 738/1.953=378; 378×0.8=302 ✓ |
| HR-9 | Verdict card first line states "Tier: A | Hurdle: 25%" | Amendment 4.3 | PASS | B11 4H header present ✓ |

**Detail.** The EPS-basis-consistency call is framework-sound: current PE and EPS CAGR are both read on the reported basis (mixing a low cash-basis current PE with a reported EPS CAGR would artificially inflate the hurdle). B11 additionally runs a cash-EPS robustness pass (current PE 22.9x, cash EPS CAGR ~13%): HR(base)≈1.05, HR(bull)≈1.2 — still well below 1.953. STOP is robust on every consistent basis, including bull and including the additive Track 2 mid (17.8x). The STOP verdict follows Amendment 2 exactly (HR(bull) < 1.953). Tier A is correct (promoter CAUTION bars Tier B).

---

## PROJECTIONS / METHODS / CONSERVATIVE HANDLING

| # | Rule | Anchor | Applied? |
|---|---|---|---|
| PM-1 | SOM cross-check performed (base 12% vs SOM 15.6%) | Master Section 2D | PASS |
| PM-2 | Depreciation held above Rs 140-145 Cr guidance to neutralise the earnings-flattering policy change | B10 flag; conservative-bias | PASS |
| PM-3 | Unresolved inputs handled by conservative rule, no silent fills (rating PDF → 1.15x; forward EPS derived + grade-B discounted) | Master; CLAUDE.md NOT FOUND rule | PASS |
| PM-4 | One-improvement-one-mechanism (no double-credit) | CLAUDE.md; Amendment 4 | PASS |
| PM-5 | Methods business-appropriate & weighted (PE 60 / EV-EBITDA 30 / peer-DCF 10) | Master Section 1A/3 | PASS |

Recovery is credited once (Pillar 1); the same Kurlon catalyst is flagged SHARED rather than credited twice; the depreciation flatter is neutralised in projections rather than allowed to lift PAT. No estimated fills — every gap (rating PDF, segment margins, forward EPS) is named and handled conservatively.

---

## ROLE 2 (B14) — DECISION RULES & POSITION SIZING

| # | Rule | Anchor | Applied? |
|---|---|---|---|
| R2-1 | Hardest-verdict-wins on contradiction | Master line 760/914; FTTCP-first sequencing | PASS |
| R2-2 | AVOID triggered on Hurdle STOP OR U/D <2x OR Gate 0 AVOID | Master line 809 | PASS (all three fire) |
| R2-3 | Promoter CAUTION does not force AVOID (that is CONCERN/AVOID) but binds sizing | Master line 809/916/818 | PASS |
| R2-4 | Position size Small; Tier B barred by promoter CAUTION | Amendment 4.3; Master 815-818 | PASS |
| R2-5 | SMALL-MEDIUM → Small is a rule application (promoter cap), not an undocumented override | Master line 818 ("caps always bind") | PASS |
| R2-6 | Entry-conjunction (anti-value-trap) stated in the verdict box | Master line 811 | PASS |
| R2-7 | Verdict consistent with Role 1 AVOID-on-valuation | Master Role 2 | PASS |

**Detail.** B14 routes AVOID on three independent, individually-sufficient grounds (Hurdle STOP; Upside/Downside −0.2x < 2x; Gate 0 AVOID), fully consistent with B11's AVOID-on-valuation — a clean hardest-verdict-wins application. Promoter CAUTION is correctly held as a sizing cap, not an AVOID trigger (the AVOID-forcing levels are CONCERN/AVOID). Sizing resolves to Small (Tier A): promoter CAUTION bars Tier B (Amendment 4.3 requires TRUSTWORTHY+) and fails the Master Medium gate (which needs Promoter TRUSTWORTHY); Gate 0 AVOID plus the absence of any BUY-NOW condition removes Medium/Large. The down-cap from FTTCP's SMALL-MEDIUM to Small is correctly characterised as a rule application, not an operator override, and applies only conditionally if the price enters the zone with no broken trigger. The entry-conjunction rule is present in the Section 7 box.

---

## FINDINGS (valuation section)

**F1 — MINOR.** *Location: B11 Pillar 1 / B10 roce_cash_basis.* The Pillar 1 "current ROCE" input uses the operating/tangible Cash ROCE (13.0%) in place of the mechanically-reported current ROCE (6.7%). This is authorised by the fttcp-deliberation cross-cutting note and the B10 stage-11 directive (do not anchor on the 6.7% goodwill-depressed trough), and it is disclosed and internally reconciled (implied EBIT add-back ~Rs 231 Cr ≈ the reported-vs-cash EPS gap). It is the less-conservative direction (raises the multiple), but it is decision-neutral: substituting the reported 6.7% would give a 60/40 blend of 10.4%, base PE 12.7x, raw 15.6x, RRM 14.7x — an even harder STOP. Also conservative within the operating family (13% low-end vs B04's 18-21%). Rule satisfied; recorded as a disclosed judgment substitution.

**F2 — MINOR.** *Location: B11 RRM Track 1.* RRM is applied to the full raw destination PE (17.8x, premiums included) read as "Fundamental Base PE." The Master v3.2 spine leaves "Fundamental Base PE" undefined between the ROCE base, the quality-adjusted base, and the full raw. B11's interpretation is defensible (it lets the RRM carry the governance discount that would otherwise be an additive PE point, with Strategic Premium = 0) and is decision-neutral: divergence is only 6.2% and both tracks (16.7x / 17.8x) yield STOP. Presentational/interpretive note only.

**F3 — MINOR.** *Location: B11 Section 3 / Pillar 1 basis interaction.* Mild basis tension: the Pillar 1 multiple is built on operating (cash) ROCE while the destination-PE × EPS math uses reported EPS. B11 handles this conservatively — the reported EPS ladder embeds the PPA-amortization rolloff (reported converging toward cash), the current-PE/EPS-CAGR consistency rule is enforced on the reported basis, and the cash-basis robustness pass still returns STOP. No double-count and no inflated hurdle. Advisory only.

No CRITICAL. No MAJOR. The destination PE and the AVOID-on-valuation / STOP decision are confirmed as framework-compliant.

---

## COMPLIANCE TALLY (valuation section)

- Rules checked: 47 (Pillars 1-3 + Strategic + UA + Sector cap + RRM + Hurdle/Tier + Projections/Methods + Role 2).
- Rules passed clean: 44. Rules passed-with-MINOR-note: 3 (F1, F2, F3). Fails (MAJOR/CRITICAL): 0.
- Recomputed destination PE: concur (17.8x additive / 16.7x RRM).
- Recomputed decision: concur (AVOID-on-valuation; Hurdle STOP).

---

```yaml
stage: B12c-valuation
company: "SFL"
run_date: "2026-07-14"
model: claude-opus-4-8
status: complete
scope: "valuation-adherence (B10/B11) + Role 2 (B14); gate0+emoat done in phase 1, not re-checked"
valuation:
  rules_checked: 47
  fails: []
  minor_notes:
    - "F1: Pillar 1 current-ROCE input = operating/tangible Cash ROCE 13.0% (not reported 6.7%); deliberation-authorised, disclosed, decision-neutral (reported basis yields harder STOP)"
    - "F2: RRM applied to full raw destination PE (17.8x) as 'Fundamental Base PE'; Master term ambiguous; defensible, decision-neutral (divergence 6.2%, both tracks STOP)"
    - "F3: Pillar 1 multiple on operating ROCE vs PE-times-EPS on reported EPS; handled conservatively (reported ladder embeds PPA convergence; cash-basis robustness still STOP)"
findings:
  - {severity: "MINOR", location: "B11 Pillar 1 / B10 roce_cash_basis", description: "Current ROCE input uses operating/tangible Cash ROCE 13.0% not reported 6.7%; deliberation-authorised and disclosed; less-conservative direction but decision-neutral (reported basis gives an even harder STOP)"}
  - {severity: "MINOR", location: "B11 RRM Track 1", description: "RRM applied to full raw destination PE (17.8x) read as 'Fundamental Base PE'; Master spine leaves the term undefined; interpretation defensible and decision-neutral (6.2% divergence, both tracks STOP)"}
  - {severity: "MINOR", location: "B11 Section 3 basis interaction", description: "Pillar 1 multiple built on operating ROCE while PE x EPS uses reported EPS; handled conservatively via reported ladder PPA convergence and a cash-basis robustness pass that still returns STOP; no double-count"}
recomputed_destination_pe: ""   # concur: 17.8x additive / 16.7x RRM
recomputed_decision: ""         # concur: AVOID-on-valuation (Hurdle STOP)
framework_adherence_valuation: "HIGH — Pillars 1-3, single-credit, UA ordering (Amendment 3), Building-materials 22x sector cap (genuine Master row, manifest 20x correctly overridden), both RRM tracks (Amendment 4.4 percentage-point reading), Hurdle Ratio + Tier A (Amendment 2/4.3), and Role 2 hardest-verdict-wins + Small/Tier-A sizing all applied as written; Amendment 4.5 correctly NOT applied (permanent goodwill re-basing, 📄-gated unwind catalyst absent); 0 CRITICAL, 0 MAJOR, 3 MINOR disclosed decision-neutral judgment calls"
critical_count: 0
major_count: 0
minor_count: 3
acceptance_rate: 94    # 44 clean of 47 rules checked; 3 MINOR passed-with-note, 0 fails
```
