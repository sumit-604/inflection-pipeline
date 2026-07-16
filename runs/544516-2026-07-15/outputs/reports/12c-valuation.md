# B12c — VERIFIER C, VALUATION-ADHERENCE HALF (Phase 3)
## Airfloa Rail Technology Ltd (Ticker 544516) | Run 2026-07-15

**Model:** claude-opus-4-8 | **Scope:** deferred valuation-adherence audit of B11 (Section 1B v3.3 / FTTCP v1.2) plus Role 2 (B14) decision-rule and position-sizing adherence. Gate 0 and Emerging Moat halves already audited in Phase 1 (12c-framework.md); NOT redone here.

**Method:** rule application only, not company quality and not raw-number sourcing (Verifier A owns numbers). Frameworks read: Master v3.3 Role 1/Role 2, Section 1B v3.3 Amendments (1-8, 4.1-4.5), FTTCP v1.2. Inputs cross-checked: B10 assembly, B09 TAM/SOM, B11 valuation, B14 thesis.

---

## PART 1 — B11 VALUATION, RULE-BY-RULE

| # | Rule (as written) | Applied? | Verdict |
|---|---|---|---|
| 1 | Pillar 1 continuous formula (Amend 5): 0.5×ROCE+7.5, floor 9x cap 24x | 0.5×24.9+7.5 = 19.95 → 20.0x, within bounds | PASS |
| 2 | FTTCP ROCE forward verdict is sole Pillar 1 authority; STAGNANT → current ROCE; ~24.9% company-reported basis used, NOT Gate 0 41.30%/25.22% | STAGNANT verdict used; 24.9% company basis; Gate 0 split explicitly rejected as formula artifact (B11 line 42; B10 line 59-60) | PASS |
| 3 | Amendment 4.5 normalized anchor applies ONLY to TEMPORARILY DEPRESSED + RECOVERING; here STAGNANT | Correctly NOT applied; no self-reversing trough (B11 line 42) | PASS |
| 4 | Amend 4 single-credit: worksheet states the route | "ROCE recovery credited via: NOT CREDITED" (STAGNANT); Strategic Premium ROCE re-rating route also barred (B11 line 44, 76) | PASS |
| 5 | Pillar 2 multiplier matches deliberation determination (0.80x GROWTH-INDUCED) | 0.80x, operator override from structural 0.65x, falsifier on record (B11 line 50-52; B10 line 103-104) | PASS |
| 6 | Growth offset handled without double-credit; no offset if structural; one-improvement-one-mechanism | growth_offset = 0; the 0.65x→0.80x override already embeds the growth credit; adding a +0.20 CAGR offset would double-credit (CLAUDE.md; Appendix A). Effective 0.80x. | PASS |
| 7 | Pillar 3a per Amend 4.1: SOM-implied CAGR ≥20% qualifier requires the capacity cross-check to PASS | **FAIL — see Finding V-1 (CRITICAL)** | **FAIL** |
| 8 | Pillar 3b EM-gated table; EM 14.5 < 25 | +0x (B11 line 64) | PASS |
| 9 | Pillar 3c duration; contracted book 1.47x < 2.5 yrs | +0x (B11 line 66) | PASS |
| 10 | UA in Amendment 3 order min(F×1.25, Cap); all three qualifiers; withheld if any fails | F2 row present; listed ~10m < 12m fails gate → UA WITHHELD; F unchanged (B11 line 89, 95; B10 line 115-119) | PASS |
| 11 | Sector cap absolute (25x Cables/Industrial products); no round-number exit PE | H = min(18.0, 25) = 18.0; cap not binding; no default multiple introduced | PASS |
| 12 | BOTH tracks present and carried through every fair value + verdict card; conservative governs on >15% divergence | Track 1 RRM 14.8x + Track 2 additive 18.0x, both in fair-value tables and verdict card; divergence 17.8% >15% → Track 1 governs entry (B11 line 105-108) | PASS |
| 13 | Hurdle Ratio computed correctly; grade-C Bull gate (Base+5%=26%); EPS basis consistent (current-share 19.3x, not 16.89x weighted-avg) | HR = (1+g)³×(DestPE/CurrPE); Track 1 base 1.36 / bull 1.53, Track 2 base 1.65 / bull 1.87; all recomputed and tie out; 19.3x current PE used consistently; SFL basis-mixing trap avoided (B11 line 12-19, 110-121) | PASS |
| 14 | 4D probability weights match grade | Grade C (Mixed) → 35/45/20 = Master line 630 exactly (B11 line 244) | PASS |
| 15 | SOM cross-check performed on revenue assumptions | Base 21% pegged at SOM ceiling 21.1%; guidance 56.5% rejected as > SOM and grade-C (B11 line 140) | PASS |
| 16 | Every unresolved input handled by stated conservative rule, no silent fill | rating_wc_quote NOT FOUND → proceed at 0.80x (override with falsifier), documented; no 0.65x structural confirmation invented (B11 line 52, input_gaps) | PASS |
| 17 | One-improvement-one-mechanism (no double-credit) | Growth credited once (in the 0.80x override), not again as an offset; ROCE not credited (STAGNANT); strategic +0x | PASS |

### FINDING V-1 (CRITICAL) — Pillar 3a: SOM qualifier credited despite a FAILED capacity cross-check

**Rule (Amendment 4.1):** the SOM qualifier reads "SOM-implied revenue CAGR ≥20% **with the capacity cross-check passing**." Both conditions are required; the cross-check is not optional.

**What B11 did (line 60):** credited the SOM qualifier — "SOM-implied 21.1% ≥ 20%, capacity supported by 90% utilisation + 14-acre facility expansion → QUALIFIES" — and dismissed B09 as failing only the *guidance* test, not the *SOM* test.

**What B09 actually found (Section 3C; lines 143-147, 240, 297; yaml `capacity_check`):** the capacity cross-check FAILED. SOM_3yr Rs 568 Cr exceeds management's own stated near-term capacity ceiling of ~Rs 450 Cr by ~Rs 118 Cr. B09 states the capex/execution side is "the more optimistic-and-unproven input," the 90% utilisation means limited headroom, the 14-acre facility is delayed (China machinery export-control block, B07 F2 documented-negative), and closing the gap rests on the metric-free channel-partner model (B07 B3, Weak). B11 misread the two conditions: it treated "SOM CAGR ≥20%" alone as sufficient and re-labelled the failed capacity check as a mere guidance-vs-SOM point. The capacity cross-check did not pass, so the SOM qualifier does not count.

**Recompute of 3a:**
- capex-embedded growth ≥15%: not documented → no
- order book ≥1.0x revenue: 1.47x → **YES (the sole legitimate qualifier)**
- SOM-implied CAGR ≥20% WITH capacity passing: capacity FAILED → **NO**
- delivery grade A/B: grade C → no

One qualifier. Amendment 4.1 pays +2x only for two qualifiers; **one qualifier → +0x.** Corrected **3a = +0x** (was +2x). Pillar 3 total = 0 + 0 + 0 = **+0x** (was +2x).

**Downstream effect (recomputed):**

| Item | B11 (as reported) | Corrected | Δ |
|---|---|---|---|
| Pillar 3 total | +2.0x | +0.0x | −2.0x |
| Track 2 Raw / Final Dest PE (mid) | 18.0x | **16.0x** | −2.0x |
| Track 2 range | 16.5-19.5x | 15.0-17.0x | |
| Track 1 Fundamental Base PE | 18.0x | 16.0x | |
| Track 1 RRM Dest PE (mid), RRM 0.82 | 14.8x | **13.1x** (16.0×0.82) | −1.7x |
| Track 1 range | 13.5-16.0x | 12.0-14.0x | |
| Divergence | 17.8% | 18.1% (still >15%, Track 1 governs) | |
| Hurdle (Track 1 governing) | base 1.36 / bull 1.53 → STOP | base 1.20 / bull 1.36 → STOP (more decisive) | verdict robust |
| Hurdle (Track 2) | base 1.65 / bull 1.87 → STOP | base 1.47 / bull 1.66 → STOP | verdict robust |
| Base FV Yr3 (Track 1) | Rs 427 | Rs 378 (28.83×13.1) | |
| Entry (÷1.953) / MoS | Rs 218 / Rs 175 | Rs 193 / Rs 155 | zone tightens down |
| Decision | AVOID (on-valuation) | **AVOID (unchanged)** | robust |

**Severity: CRITICAL.** The misapplication moves the destination PE mid by 2.0x (Track 2) and ~1.7x (Track 1) — both above the >1x CRITICAL threshold in the rubric. The Hurdle verdict (STOP) and the decision (AVOID) are UNCHANGED and in fact more decisive; B11 itself notes the STOP "is robust to the Pillar 3 judgment" (line 123). So the decision does not flip, but the destination PE and the entry zone are overstated: the correct entry zone is ~Rs 155-193, not Rs 175-218, placing CMP Rs 315 even further above the zone. The error is directionally against B11's own conservative bias (it credited a premium the framework does not permit), which is why the correction only hardens the AVOID.

**Note on presentation propagation:** the +2x/18.0x figures flow through the verdict card, the one-line thesis, and into B14 (thesis one-liner, Section 5) verbatim. These are downstream of the same single rule error, not independent fails, but they carry the overstated destination PE forward and should be restated at refresh.

---

## PART 2 — ROLE 2 (B14) DECISION RULES & POSITION SIZING

| # | Rule (Master v3.3 Role 2) | Applied? | Verdict |
|---|---|---|---|
| 18 | AVOID trigger: Gate 0 AVERAGE/AVOID OR Promoter CONCERN/AVOID OR U/D <2x OR Hurdle STOP (line 809) | AVOID on Gate 0 AVERAGE AND Hurdle STOP (two independent grounds); B14 correctly notes Promoter CAUTION does NOT itself force AVOID, only CONCERN/AVOID does (B14 line 144) | PASS |
| 19 | Position size: AVOID → None; Small (2-3%) is "everything else that qualifies as BUY"; Medium (4-6%) needs Gate 0 GOOD+ AND Promoter TRUSTWORTHY (lines 816-817) | Now None (AVOID); re-engage ceiling Small because Gate 0 AVERAGE + Promoter CAUTION fail the Medium gates; no operator override recorded (B14 line 148-149, 191-192) | PASS |
| 20 | Tier A cascade: entry = base FV ÷ 1.953; MoS = 20% below entry; verdict card states "Tier: A \| Hurdle: 25%" | Tier A; entry 427/1.953 = Rs 218; MoS 218×0.8 = Rs 175; verdict card first line "Tier: A \| Hurdle: 25%" (B11 line 291; B14 Section 7) | PASS |
| 21 | Entry conjunction (anti-value-trap) stated in Section 7 verdict box (line 811) | Present: BUY-ON-DIPS only when price in-zone AND no thesis-broken trigger fired; zone withdrawn if entry is because falsifier tripped (B14 line 151) | PASS |

Role 2 adherence is clean. The only knock-on is that B14 inherits B11's overstated entry zone (Rs 175-218); on the corrected destination PE the entry cascade mechanics are identical but resolve to ~Rs 155-193. The cascade *logic* is correct; only the input FV is overstated upstream.

---

## SUMMARY

- Rules checked: 21 (17 valuation + 4 Role 2). Fails: 1 (V-1, CRITICAL).
- Acceptance rate: 20/21 = **95.2%** (reported as 95%).
- The single CRITICAL fail (Pillar 3a SOM qualifier credited over a failed capacity cross-check) overstates the destination PE by ~1.7-2.0x on both tracks and the entry zone by ~Rs 20-25. It does NOT flip the Hurdle verdict (STOP on both tracks, more decisive after correction) or the decision (AVOID stands). No REWORK trigger from this half (acceptance rate >60%); the CRITICAL is a destination-PE/entry-zone restatement, not a decision reversal.
- All other pillar mechanics, the dual-track carry-through, the Hurdle computation with the grade-C Bull cap and the consistent 19.3x current-PE basis, the UA withholding, the sector cap, the 4D weights, the conservative handling of the NOT-FOUND rating quote, and the entire Role 2 decision/position-sizing cascade are applied as written.

---

```yaml
stage: B12c
company: "544516"
run_date: "2026-07-15"
model: claude-opus-4-8
status: complete
gate0: {rules_checked: 0, fails: []}   # audited Phase 1 (12c-framework.md); not redone
emoat: {rules_checked: 0, fails: []}   # audited Phase 1 (12c-framework.md); not redone
valuation:
  rules_checked: 21   # 17 B11 valuation + 4 Role 2 (B14)
  fails:
    - id: V-1
      severity: CRITICAL
      rule: "Amendment 4.1 Pillar 3a — SOM-implied CAGR qualifier requires the capacity cross-check to PASS"
      what_happened: "B11 credited the SOM qualifier (+contributing to 3a +2x) claiming capacity 'supported by 90% utilisation + 14-acre expansion', but B09 Section 3C FAILED the capacity cross-check: SOM_3yr Rs 568 Cr exceeds the ~Rs 450 Cr near-term capacity ceiling by ~Rs 118 Cr. With the SOM qualifier disallowed, only the order-book qualifier (1.47x) holds; one qualifier pays +0x, not +2x."
      recompute: "3a +0x (was +2x); Track 2 destination PE mid 16.0x (was 18.0x); Track 1 RRM destination PE mid 13.1x (was 14.8x); entry zone ~Rs 155-193 (was Rs 175-218). Hurdle STOP and decision AVOID unchanged (more decisive)."
recomputed_destination_pe: "Track 1 RRM mid 13.1x (report 14.8x); Track 2 additive mid 16.0x (report 18.0x). 3a should be +0x not +2x (Amend 4.1 capacity cross-check failed per B09)."
recomputed_decision: ""   # concur — AVOID stands; the correction hardens it, does not flip it
findings:
  - {severity: "CRITICAL", location: "B11 Pillar 3a (line 60) / verdict card / B14 thesis line", claimed: "3a +2x on order-book 1.47x + SOM 21.1%; destination PE Track2 18.0x / Track1 14.8x", source_truth: "Amend 4.1: SOM qualifier needs capacity cross-check passing; B09 3C failed it (SOM 568 > ~450 ceiling). One qualifier → 3a +0x; dest PE Track2 16.0x / Track1 13.1x", note: "Changes destination PE by >1x (CRITICAL by rubric); Hurdle STOP and decision AVOID robust and unchanged."}
critical_count: 1
major_count: 0
minor_count: 0
acceptance_rate: 95   # 20 rules passed / 21 checked
```
