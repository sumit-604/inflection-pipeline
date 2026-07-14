# VERIFIER C — FRAMEWORK ADHERENCE, PHASE 3 (VALUATION-ADHERENCE HALF, EXTENDED)
## AURUM (Aurum Proptech Ltd) | run_date 2026-07-14 | Model: claude-opus-4-8 | FRESH CONTEXT

Scope: deferred valuation-adherence audit of B10/B11 and B14 (Role 2 decision
rules + position sizing), against Master v3.3 (Role 1 + Role 2), Section 1B v3.3
Amendments, FTTCP v1.2 handoff (fttcp-deliberation.md). Gate 0 (B01) and Emerging
Moat (B07) were audited in Phase 1 and are NOT re-done here. I audit rule
application, not raw numbers (Verifier A owns numbers) and not company quality.

Authoritative inputs taken as given (from the deliberation, not re-litigated):
ROCE forward STAGNANT; cash INDETERMINATE; sector cap row Platform/SaaS 45x;
SOTP primary; ROCE recovery credited via NEITHER route.

---

## A. PILLAR 1 — ROCE BASE MULTIPLE (Section 1B Amendment 5 + FTTCP handoff)

| # | Rule | Applied in B11 | Verdict |
|---|---|---|---|
| 1 | STAGNANT verdict → Pillar 1 uses CURRENT ROCE, no forward uplift | ROCE 3.32% (FY26), no uplift | PASS |
| 2 | Continuous formula 0.5×ROCE+7.5, floor 9x, cap 24x | 0.5×3.32+7.5 = 9.16 → 9.2x (1 dp) | PASS |
| 3 | Amendment 4.5 Normalized-ROCE anchor applies ONLY if backward TEMPORARILY DEPRESSED AND forward RECOVERING | Correctly excluded (backward not TEMP-DEPRESSED, forward STAGNANT) | PASS |
| 4 | Single-credit route stated explicitly ("credited via …") | "NOT CREDITED" — matches handoff (neither Pillar 1 nor Strategic) | PASS |

Recompute check: 0.5×3.32 = 1.66; +7.5 = 9.16; floor 9x does not bind (9.16>9);
rounds to 9.2x. **Confirmed 9.2x.** The "floored at 9x → 9.2x" phrasing is loose
(the floor is not what produces 9.2) but the value is correct — presentational,
not a fail.

## B. PILLAR 2 — CASH CONVERSION MULTIPLIER (INDETERMINATE)

| # | Rule | Applied in B11 | Verdict |
|---|---|---|---|
| 5 | INDETERMINATE → use the more conservative multiplier and say so | 0.80x band on negative 5-yr cumulative CFO/PAT (−0.29), stated | PASS |
| 6 | Growth offset applies only to CONFIRMED growth-induced drag | Offset DENIED (structural-vs-growth INDETERMINATE) | PASS |
| 7 | 0.65x structural band requires rating-agency confirmation; NOT FOUND cannot be manufactured | 0.65x NOT invoked (rating rationale NOT FOUND); downside to 0.65x flagged | PASS |
| 8 | Quality-Adjusted Base = A × B | 9.2 × 0.80 = 7.36x | PASS |
| — | INDETERMINATE never silently resolves to PROCEED (CLAUDE.md) | Disposition capped at PROCEED WITH CAVEATS, both missing items named | PASS |

Judgment note (not a fail): between a neutral/offset-relieved 0.80x and the
structural 0.65x, B11 lands on 0.80x-with-offset-denied because the 0.65x band
needs positive rating-agency evidence that is NOT FOUND, and manufacturing 0.65x
would violate "NOT FOUND is the only fill." This is the correct conservative
floor given the evidence, and the drop-to-0.65x downside is explicitly carried.
Consistent with the INDETERMINATE determination.

## C. PILLAR 3 — GROWTH PREMIUM (Amendments 4.1 / 4.2, decoupled)

| # | Rule | Applied in B11 | Verdict |
|---|---|---|---|
| 9 | 3a: +2x if any two 📄 qualifiers hold; grade caps (C→+2, D→+0) | Two qualify — SOM-implied CAGR ≥20% (B09 bottom-up 57.8%, ARR ₹500→1,000 Cr ~26%, capacity cross-check passes) + delivery grade B; +2x. Grade B does not cap. | PASS |
| 10 | 3b: EM-gated table, unchanged. EM 25-29 any timeline → +1x | EM 25.2, catalyst 0-12m FY27 → +1x | PASS |
| 11 | 3c: Duration Premium +1x only if visibility ≥2.5 yr (📄) | Not met (ARR/Rev 1.18x, no LoA/contract tenor) → +0x | PASS |
| 12 | Combined 3a+3b+3c hard cap +6x | +2+1+0 = +3x (within cap) | PASS |

## D. STRATEGIC PREMIUM (single-credit; no double-count)

| # | Rule | Applied in B11 | Verdict |
|---|---|---|---|
| 13 | ROCE re-rating optionality only if recovery NOT credited in Pillar 1; SM-REIT optionality already in Pillar 3b (no double-count) | +0x — recovery not credited anywhere (STAGNANT); SM-REIT unmonetized/slipped 4 calls, captured in 3b | PASS |

## E. FOUR-PILLAR SUMMARY, UA, SECTOR CAP (Track 2; Amendment 3)

| # | Rule | Applied in B11 | Verdict |
|---|---|---|---|
| 14 | F. Raw = C + D + E | 7.36 + 3.0 + 0 = 10.36x | PASS |
| 15 | UA qualifier 1 — listed ≥12 months | TRUE; long-listed (ex-Majesco, BSE 539289). B11 correctly re-verified the suspect "listed_12m" field: the genuine qualifier is "listed ≥12m," satisfied by a long-listed co. | PASS |
| 16 | UA qualifier 2 — Gate 0 ≥60 OR EM ≥25 | TRUE via EM 25.2 (Gate 0 = 58 fails leg; OR satisfied) | PASS |
| 17 | UA qualifier 3 — FII+DII combined <3% | TRUE; FII 0.13%, no separate DII row (3-row view, embedded in Public/negligible). Institutional absence genuinely evidenced. | PASS (see minor) |
| 18 | UA ordering: F2 = F × 1.25 applied to RAW, BEFORE the cap | 10.36 × 1.25 = 12.95x | PASS |
| 19 | Final = min(F2, Sector Cap); cap ABSOLUTE | min(12.95, 45) = 12.95x | PASS |
| 20 | Sector cap = Platform/SaaS 45x; quality uplift on cap only if durability ≥Moderate-Strong documented | 45x, no uplift (durability weak, HIGH governance/goodwill/cash flags) | PASS |
| 21 | H rounds; Range = H ±7.5%, nearest 0.5x | 12.95 → 13.0x; 11.98–13.92 → 12.0x–14.0x | PASS |
| 22 | No round-number or outside-Section-1B exit PE anywhere | Confirmed. Exit PE 13.0x is fully derived. SOTP uses EV/Rev + EV/EBITDA (method-appropriate, sanctioned by deliberation), which are NOT exit PEs — no violation of the sole-authority rule. | PASS |

## F. RRM TRACK 1 (Amendment 4.4 percentage-points) & DUAL-TRACK GOVERNANCE

| # | Rule | Applied in B11 | Verdict |
|---|---|---|---|
| 23 | r base small/micro 14%, adjust for durability/governance, bound [9,18] | r = 16% (weak durability + HIGH governance) | PASS |
| 24 | RRM = 1 + (13.5 − r)×0.12, percentage-point reading, bounds [0.70,1.60] | 1 + (−2.5×0.12) = 0.70 (hits floor) | PASS |
| 25 | Track 1 = Fundamental Base × RRM, capped | 10.36 × 0.70 = 7.25 → 7.3x; range 6.5–8.0x | PASS |
| 26 | BOTH tracks carried through fair values + verdict card | Present throughout | PASS |
| 27 | Divergence >15% → state which track is more appropriate | 44%; Track 1 (7.3x) named the more conservative PE anchor; SOTP primary governs entry per deliberation | PASS |

Note (not a fail): the Master rule "the more conservative track sets the entry
zone" is subordinated here to SOTP-primary (the deliberation directs SOTP primary
because FY26 is barely profitable and PE is unreliable). Entry is derived from
SOTP Year-3 base, not either PE track. This is a correct, evidenced application of
the SOTP-primary instruction, and both PE tracks agree "expensive," so the intent
of the conservative-track rule is preserved.

## G. HURDLE RATIO (Amendment 2) & 4D WEIGHTS

| # | Rule | Applied in B11 | Verdict |
|---|---|---|---|
| 28 | HR = (1+EPS CAGR)³ × (Dest PE mid ÷ Current PE) | Dest 13.0 / Current ~908 = 0.0143 | PASS |
| 29 | HR(Base) computed | (2.51)³ × 0.0143 = 0.23 | PASS |
| 30 | Bull row usable only if credibility grade A or B | Grade B → Bull permitted; HR(Bull) = (3.07)³ × 0.0143 = 0.41 | PASS |
| 31 | HR(Bull) < 1.953 → STOP | 0.41 < 1.953 → STOP | PASS |
| 32 | 4D weights match grade (B → 25/50/25) | 25/50/25; Expected CAGR = 0.25(−31.9)+0.50(−10.3)+0.25(8.9) = −10.9% | PASS |
| 33 | SOM cross-check performed | Base rev CAGR 20% < 26% ARR-implied < 40.8% historical — consistent | PASS |

PE-denominator distortion (current PE ~908x on near-zero EPS) is correctly
caveated and the independent SOTP expected CAGR (−10.9%) is used to confirm STOP.

## H. SOTP PRIMARY TREATMENT & UNRESOLVED-INPUT DISCIPLINE

| # | Rule | Applied in B11 | Verdict |
|---|---|---|---|
| 34 | SOTP primary given FY26 barely profitable; PE cross-check only | SOTP 70% primary; PE dual-track 20% cross-check; explicit | PASS |
| 35 | Rental valued separately (not 45x stretched) | Rental on EV/Rev 0.8–1.8x; 45x reserved for Distribution/platform earnings | PASS |
| 36 | Every unresolved input handled by the stated conservative rule, no silent fills | Rating rationale, FY26 receivables ageing, segment note, Jul-2026 raise — all named NOT FOUND / conservative-held; no silent fills | PASS |

## I. ROLE 2 (B14) — DECISION RULES, ENTRY/MoS, POSITION SIZING (Master Role 2)

| # | Rule | Applied in B14 | Verdict |
|---|---|---|---|
| 37 | AVOID triggers: Gate0 AVERAGE/AVOID OR Promoter CONCERN/AVOID OR U/D <2x OR Hurdle STOP | AVOID on all four independently (Gate0 58 AVOID; Promoter CONCERN; U/D 0.4x; HR STOP) | PASS |
| 38 | Gate 0 <60 → default at least WATCHLIST | Noted; superseded by the harder AVOID; consistent | PASS |
| 39 | Promoter CONCERN/AVOID → AVOID regardless of everything | Applied as binding | PASS |
| 40 | ENTRY CONJUNCTION (anti-value-trap) stated in verdict box | Present: re-engage only in ₹71–89 AND after clean operating-profit print | PASS |
| 41 | Entry = base FV ÷ (1+hurdle)³; Tier A divisor 1.953 | 173 / 1.953 = ₹88.6 → ₹89 | PASS |
| 42 | MoS = 20% below entry | 89 × 0.80 = ₹71 | PASS |
| 43 | Tier assignment: FII+DII <3% → Tier A (25%) | Tier A; Tier B barred (promoter CONCERN + structural FLAG-CASH fail Tier B gates) | PASS |
| 44 | Position ceiling: Large needs Gate0 EXCELLENT+Promoter TRUSTWORTHY+EM EXPANSION; Medium needs Promoter TRUSTWORTHY; Promoter cap binds over all | Small (2-3%) ceiling; Large & Medium correctly excluded; CONCERN cap binds | PASS |
| 45 | FLAG-GATE0 override recorded; operator override to sizing = NONE | Both recorded and honoured (deliberation: overrides NONE) | PASS |

---

## RECOMPUTE SUMMARY

- **Destination PE (recomputed):** Track 2 additive 10.36 raw → ×1.25 UA = 12.95x
  → **13.0x mid (12.0x–14.0x)**; Track 1 RRM **7.3x (6.5x–8.0x)**. **CONCUR with
  B11 exactly.**
- **Decision (recomputed):** **AVOID** (Hurdle STOP, Upside/Downside 0.4x,
  Promoter CONCERN, Gate 0 AVOID — any one sufficient); position **Small** ceiling;
  **Tier A**; entry **₹71–89**, MoS **₹71**. **CONCUR with B14 exactly.**

No fabricated multiple. No exit PE from outside Section 1B. No decision-rule
violation. FTTCP handoff (STAGNANT sole Pillar 1 authority; INDETERMINATE cash;
single-credit via NEITHER; sector cap 45x; SOTP primary) applied as written.

## MINOR OBSERVATIONS (no fails; MINOR severity)
- M1: UA qualifier 3 rests on FII 0.13% plus the absence of a separate DII row
  (DII technically NOT FOUND, embedded in Public). Immaterial — the 3-row
  structure and 0.13% FII leave no room for an undisclosed >2.87% DII; the <3%
  test is genuinely satisfied and transparently handled.
- M2: Pillar 1 "floored at 9x → 9.2x" phrasing is muddled (9.16 clears the floor;
  the 9.2 is a rounding, not a floor result). Value correct; presentational only.
- M3: Entry zone derived from SOTP (primary) rather than the "more conservative PE
  track"; correctly justified by the SOTP-primary instruction, both PE tracks
  concur, so the conservative-track intent is preserved.

Rules checked: 45. Fails: 0. Framework adherence: 100%.

---

```yaml
stage: B12c-valuation
company: "AURUM"
run_date: "2026-07-14"
model: claude-opus-4-8
status: complete
valuation:
  rules_checked: 45
  fails: []
framework_adherence_pct: 100
recomputed_destination_pe: ""   # concur — Track2 12.95x->13.0x (12.0-14.0x); Track1 RRM 7.3x (6.5-8.0x); matches B11
recomputed_decision: ""          # concur — AVOID; Small ceiling; Tier A; entry Rs71-89, MoS Rs71; matches B14
findings:
  - {severity: "MINOR", location: "B11 UA qualifier 3 / B10 ua_qualifiers", note: "FII+DII<3% rests on FII 0.13% + no separate DII row (DII NOT FOUND, embedded in Public); test genuinely satisfied, transparently handled"}
  - {severity: "MINOR", location: "B11 Pillar 1", note: "'floored at 9x -> 9.2x' phrasing muddled; 9.16 clears floor and rounds to 9.2; value correct, presentational only"}
  - {severity: "MINOR", location: "B11 dual-track governance", note: "entry zone set by SOTP (primary) not the more-conservative PE track; correctly justified by SOTP-primary instruction; both PE tracks concur expensive"}
critical_count: 0
major_count: 0
minor_count: 3
acceptance_rate: 100    # rules passed 45 / rules checked 45
```
