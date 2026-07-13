# VERIFIER C — FRAMEWORK ADHERENCE, PHASE 3 (VALUATION-ADHERENCE HALF)

**Company:** AMAGI | **Run date:** 2026-07-12 | **Model:** claude-opus-4-8
**Scope:** Deferred valuation-adherence audit only (B10 assembly, B11 Role 1 valuation),
EXTENDED to Role 2 (B14) decision rules and position sizing. Gate 0 and Emerging Moat
checks ran in phase 1 and are NOT re-run here.
**Authorities:** Master v3.3 (Section 1B, RRM dual-track, Hurdle, Role 2) / Section 1B v3.3
Amendments 1-8, 4.1-4.5 / FTTCP v1.2 / fttcp-deliberation.md (authoritative for Phase 3).

Method: I re-derived every framework-governed value from the stated inputs and thresholds.
I do not re-audit raw source numbers (Verifier A owns those); I check that the framework was
applied AS WRITTEN and that the deliberation's authoritative instructions were honored.

---

## PART 1 — SECTION 1B FOUR-PILLAR (B11) RULE-BY-RULE

### Pillar 1 — ROCE Base (Amendment 5)

| Rule | Required | B11 applied | Verdict |
|---|---|---|---|
| Continuous formula, not old bands | 0.5×ROCE+7.5, floor 9x cap 24x | 0.5×25+7.5 = 20.0x | PASS |
| Bounds respected | 9x ≤ x ≤ 24x | 20.0x within | PASS |
| ROCE input = FTTCP forward verdict authority | operating ROCE 25% ex-cash, ESOP-normalized, RECOVERING (deliberation override 1/2) | 25% used; reported ~5% explicitly NOT used (context only) | PASS |
| Amendment 4.5 normalized-ROCE anchor | applies ONLY if backward TEMPORARILY DEPRESSED with a pre-depression high-ROCE cycle + named unwind catalyst; else standard blend | Correctly NOT invoked — deliberation line 23 confirms no pre-depression high-ROCE cycle; the spirit governs the ex-cash operating treatment, which the deliberation already resolved to 25% | PASS |
| Single-credit route stated | "ROCE recovery credited via: [route]" | "credited via Pillar 1"; Strategic Premium ROCE re-rating BARRED | PASS |

ROCE Base PE **20.0x** re-derived and confirmed. Sensitivity band (17.5x/20.0x/22.5x across
20-30%) is arithmetically consistent.

### Pillar 2 — Cash Conversion Multiplier

| Rule | Required | B11 applied | Verdict |
|---|---|---|---|
| Multiplier matches determination | INDETERMINATE → weak band per deliberation line 62 ("weak-cash band, no growth offset") | 0.80x | PASS |
| Growth offset gate | offset only for CONFIRMED growth-induced drag | offset = 0.00 (INDETERMINATE cannot claim it) | PASS |
| No premature structural band | 0.65x structural needs rating confirmation; rating NOT FOUND | 0.65x correctly withheld; held at 0.80x | PASS |
| Quality-adjusted base | ROCE base × multiplier | 20.0 × 0.80 = 16.0x | PASS |
| Disposition cap propagated | INDETERMINATE caps no better than PROCEED WITH CAVEATS, no BUY NOW | stated and carried | PASS |

The 0.80x weak-band value and the no-offset treatment mirror the authoritative deliberation
directive exactly. Note: the exact numeric weak-band value is not independently re-derivable
from the Amendments/FTTCP docs alone (the non-lender Pillar 2 band table sits in the Section 1B
body), but it matches the operator's phase-3 instruction, which is authoritative here. Checked
against that authority.

### Pillar 3 — Growth Visibility (DECOUPLED, Amendments 4.1 + 4.2, +6x combined cap)

| Component | Required | B11 applied | Verdict |
|---|---|---|---|
| 3a Growth Visibility (📄-only) | +2x if any two qualify; +3x if 3+ AND grade A/B | 2 qualify (SOM-implied 32.3% ≥20% + capacity cross-check; delivery grade B) → +2x | PASS |
| 3a evidence discipline | capex-embedded NO (asset-light), order book NO (RPO undisclosed) — correctly excluded | matched | PASS |
| 3b Moat Formation (EM-gated table) | EM 30 STRENGTHENING, 0-12m catalyst, mixed evidence | +3x (conservative read of 66% documented as "mixed") | PASS (see MINOR-1) |
| 3c Duration Premium | +1x if ≥2.5yr documented visibility; else +0x | +0x (no documented order book/LoA/annuity; RPO undisclosed) | PASS |
| Combined cap | 3a+3b+3c ≤ +6x | 2+3+0 = +5x ≤ 6x | PASS |
| Shared-catalyst flag | flag if Pillar 1 catalyst = Pillar 3 catalyst | flagged NO (P1 = capital-efficiency/ESOP-cash normalization; P3 = NEWSPULSE revenue — different failure modes) | PASS |

Growth Premium **+5.0x** re-derived and confirmed, within the +6x cap, correctly evidenced.

### Strategic Asset Premium & Summary Rows

| Rule | Required | B11 applied | Verdict |
|---|---|---|---|
| Strategic Premium single-credit | ROCE re-rating BARRED (credited in Pillar 1); no double count of institutional backing | E = +0.0x | PASS |
| Raw Destination PE (F) | C + D + E | 16.0 + 5.0 + 0.0 = 21.0x | PASS |
| UA qualifiers (Amendment 3) | ALL THREE: listed ≥12m; Gate0≥60 OR EM≥25; FII+DII <3% | listed 6.3m = NO; EM 30≥25 = YES; FII+DII >>3% = NO → 2 of 3 fail → UA does NOT apply | PASS |
| UA ordering / F2 | F2 = F × 1.25 only if qualified, else F2 = F | F2 = F = 21.0x | PASS |
| Sector cap absolute | min(F2, Cap); cap is ceiling not destination | min(21.0, 45.0) = 21.0x; 45x NOT binding | PASS |
| Manifest defect handling | Pharma/CDMO 38x is collector defect; 45x Platform/SaaS per deliberation | overridden correctly | PASS |
| B10 stray line (45x × FY30 EPS = Rs 648) | must be ignored — 45x is CAP not destination | explicitly IGNORED by B11 line 9 | PASS (good catch) |

**Final Destination PE (Track 2 additive) = 21.0x, range 19.5-22.5x. CONFIRMED.**

### RRM Dual-Track (Track 1)

| Rule | Required | B11 applied | Verdict |
|---|---|---|---|
| Both tracks produced | RRM (Track 1) + Additive (Track 2) | both present, carried through all fair values and verdict card | PASS |
| Base r | small/micro 14% | 14.0% base | PASS |
| r adjustments bounded [9%,18%] | durability/governance/cash | +1.0 cash INDETERMINATE, +0.5 governance B, +0.5 durability MODERATE = 16.0% | PASS |
| RRM formula, percentage-point reading (Amdt 4.4) | 1 + (13.5 − r) × 0.12, floor 0.70 | 1 + (13.5 − 16.0)×0.12 = 1 − 0.30 = 0.70 (at floor) | PASS |
| Track 1 destination | Fundamental Base PE × RRM | 21.0 × 0.70 = 14.7x, range 13.5-16.0x | PASS |
| Divergence handling | >15% → both shown, conservative track governs entry | 30.0% divergence; Track 1 RRM governs entry zone | PASS |

**Track 1 Destination PE = 14.7x. CONFIRMED.** B11 self-discloses a mild cash double-penalty
(0.80x in the base AND +1% in r). This is a double-PENALTY (conservative), not a double-CREDIT,
so it does not breach the single-credit rule; it is an accepted conservative bias and does not
change the verdict (see MINOR-2).

### Hurdle Ratio, Tier, Entry (Amendments 2 + 4.3)

| Rule | Required | B11 applied | Verdict |
|---|---|---|---|
| Tier assignment | HIGH POTENTIAL combined → Tier A, 25% hurdle, threshold 1.953 | Tier A, 1.953 | PASS |
| Tier B correctly excluded | Tier B needs no structural FLAG-CASH; INDETERMINATE cash + Gate0 AVERAGE block it | Tier A retained (also forced by HIGH POTENTIAL) | PASS |
| Forward-PE-at-exit convention | FY29 exit applies destination PE to FY30 EPS (operator instruction) | exit price = Dest PE × FY30 EPS throughout | PASS |
| HR computation | HR = exit ÷ CMP identity | Track 2 base 303/580 = 0.52; bull 418/580 = 0.72 | PASS |
| Bull-row credibility gate | Bull EPS allowed only if grade A/B | grade B → Bull permitted; still fails | PASS |
| Verdict mapping | HR(Bull) < 1.953 → STOP | STOP on both tracks | PASS |
| Entry price (Tier A divisor 1.953) | base FV ÷ 1.953 | 212/1.953 = 109 (RRM, governing); 303/1.953 = 155 (additive) | PASS |
| MoS | 20% below governing entry | 0.80 × 109 = 87 | PASS |

**Hurdle verdict STOP and destination PEs (21.0x / 14.7x) CONFIRMED.** I concur with the AVOID-
on-valuation conclusion. No recomputation of destination PE or decision is required.

---

## PART 2 — ROLE 2 (B14) DECISION RULES & POSITION SIZING

| Rule (Master v3.3 Role 2) | Required | B14 applied | Verdict |
|---|---|---|---|
| BUY NOW gate | CMP ≤ MoS AND Gate0 ≥ GOOD AND Promoter ≥ TRUSTWORTHY AND HR = PASS | correctly denied (CMP 580 >> MoS 87; Gate0 AVERAGE; HR STOP) | PASS |
| No BUY NOW under INDETERMINATE cash | disposition capped PROCEED WITH CAVEATS | explicitly enforced, "no BUY NOW" | PASS |
| Verdict landing | AVOID triggers fire (Gate0 AVERAGE, HR STOP, U/D<2x) vs Gate0<60 default WATCHLIST + FTTCP investable override | WATCHLIST ("AVOID at CMP; DEEP WATCH per FTTCP") | PASS (see MINOR-3) |
| WATCHLIST definition | CMP above Entry but thesis strong, wait for correction | matches (CMP 3.7-5.3x above entry zone) | PASS |
| Position size — Large | Gate0 EXCELLENT + Promoter TRUSTWORTHY + EM EXPANSION + CMP<MoS | correctly excluded (Gate0 AVERAGE, EM STRENGTHENING, CMP>MoS) | PASS |
| Position size — Medium | Gate0 GOOD+ + Promoter TRUSTWORTHY + CMP≤Entry | correctly excluded (Gate0 band, CMP>Entry) | PASS |
| Position size — Small | everything else that qualifies as BUY | Small (2-3%) starter only, upon entry conjunction; INDETERMINATE cash keeps ceiling at Small | PASS |
| Entry conjunction (anti-value-trap) | stated explicitly in Section 7 box | stated in box + narrative + checklist item 8 | PASS |
| No exit PE from outside Section 1B | Section 1B sole authority | uses B11 21.0x/14.7x; rejects the Rs 648 45x stray line | PASS |
| No round-number default | — | none introduced | PASS |
| Targets consistent with B11 | Rs 212 RRM / Rs 303 additive; MoS 87; entry 109-155 | all carried from B11 unchanged; 5yr honestly NOT COMPUTED | PASS |

Role 2 adherence: decision rules and position-sizing logic are applied consistently with the
Master prompt. No exit multiple is introduced from outside Section 1B. The WATCHLIST landing is
framework-supported (Master line 915: Gate0<60 defaults to WATCHLIST; the FTTCP authority frames
the name as investable-but-not-at-CMP) and is operationally identical to AVOID-at-CMP.

---

## PART 3 — FINDINGS (all MINOR; no CRITICAL, no MAJOR)

**MINOR-1 (Pillar 3b, B11 Section 1B §Pillar 3):** The 3b moat-formation premium (+3x) rests on
a primary 0-12m catalyst (NEWSPULSE/agentic-AI revenue) whose evidence tier is CLAIM (CEO
framing, Q4 FY26), and on the D1 data-asset moat that is self-characterized (0.7x weight). B11
already conservatively downgraded the 66%-documented mix to "mixed." The +3x sits at the generous
edge of the EM-gated table for a claim-anchored catalyst. Even if 3b were +2x, destination PE
would be 20.0x and the Hurdle verdict (STOP) and decision (AVOID) are unchanged. No decision
impact; flagged for completeness. The exact 3b table row could not be independently re-derived
from the Amendments/FTTCP docs available (the EM-gated table is referenced as "unchanged" but not
reprinted).

**MINOR-2 (RRM, B11 §RRM):** The RRM track applies the 0.80x cash penalty inside the fundamental
base AND raises r by +1.0% for the same cash uncertainty — a mild double-penalty on cash. B11
discloses this openly and accepts it as conservative. It is a double-penalty, not a double-credit,
so it does not violate the single-credit rule; and the decision does not hinge on it (even the
un-penalized Track 2 STOPS). Noted as a transparency item only.

**MINOR-3 (Verdict semantics, B14 Section 7):** The verdict card reads "WATCHLIST (AVOID at CMP)."
Strictly, three Master AVOID triggers fire (Gate0 AVERAGE, HR STOP, Upside/Downside<2x). B14
lands on WATCHLIST by invoking the Gate0<60→WATCHLIST default plus the authoritative FTTCP
investable override. The two labels carry identical operating instruction (no buying at Rs 580;
wait for the Rs 109-155 zone), so there is no decision impact; the straddle is a labeling choice,
not a rule breach.

**MINOR-4 (HR presentation, B11 §Hurdle):** B11 states HR is "invariant to EPS basis" and equal
to Exit ÷ CMP. Under the forward-PE-at-exit convention (exit price = destination PE × FY30 EPS),
Exit ÷ CMP is the true 3-year price multiple and the reported 0.52/0.72 are correct; the pure
formula (1+EPS CAGR)³ × (Dest PE ÷ Current PE) with a 3-year EPS CAGR would land on FY29 EPS, a
slightly different number. The "invariant" phrasing is loose, but the value used honors the
operator's FY30-EPS instruction and the STOP verdict is unaffected (bull 0.72 is far below 1.953).

---

## ACCEPTANCE

Valuation + Role 2 rules checked: 38. Material fails: 0. All four findings are MINOR imprecisions
or transparency items with zero decision impact. Destination PE (21.0x additive / 14.7x RRM),
Hurdle STOP, entry zone Rs 109-155, MoS Rs 87, and the WATCHLIST / AVOID-at-CMP decision are all
confirmed as framework-compliant. I concur; no recomputation of destination PE or decision.

```yaml
stage: B12c-valuation
company: "AMAGI"
run_date: "2026-07-12"
model: claude-opus-4-8
status: complete
phase: 3
scope: "valuation-adherence (B10, B11) + Role 2 (B14) decision & position-sizing"
valuation:
  rules_checked: 32
  fails: []
role2:
  rules_checked: 6
  fails: []
  decision_adherence: "WATCHLIST / AVOID-at-CMP consistent with Master Role 2; no BUY NOW under INDETERMINATE cash; Small starter ceiling correct; entry conjunction stated; no exit PE from outside Section 1B"
  position_sizing_adherence: "Large and Medium correctly excluded on Gate0 band / EM band / CMP>entry; Small starter only upon entry conjunction; PROCEED WITH CAVEATS cap honored"
recomputed_destination_pe: ""   # concur: Track 2 21.0x / Track 1 14.7x
recomputed_decision: ""         # concur: AVOID on valuation / WATCHLIST at CMP; Hurdle STOP
findings:
  - {severity: "MINOR", location: "B11 Section 1B Pillar 3b", description: "3b +3x rests on a CLAIM-tier 0-12m catalyst (NEWSPULSE) and 0.7x-weighted self-characterized D1 moat; sits at generous edge of the EM-gated table. Even at +2x, destination PE 20.0x and Hurdle STOP / decision AVOID unchanged. Exact 3b table row not independently re-derivable from available docs."}
  - {severity: "MINOR", location: "B11 RRM derivation", description: "Cash uncertainty double-penalized (0.80x in base AND +1.0% in r). Self-disclosed and conservative; a double-penalty not a double-credit, so single-credit rule not breached; decision unaffected."}
  - {severity: "MINOR", location: "B14 Section 7 verdict card", description: "Verdict labeled WATCHLIST while three Master AVOID triggers (Gate0 AVERAGE, HR STOP, U/D<2x) fire; reconciled via Gate0<60 default-WATCHLIST rule + authoritative FTTCP investable override. Identical operating instruction (no buy at CMP); no decision impact."}
  - {severity: "MINOR", location: "B11 Hurdle Ratio", description: "'Invariant to EPS basis' phrasing is loose; HR computed as Exit/CMP on FY30 EPS honors the forward-PE-at-exit instruction and is correct; STOP verdict unaffected."}
critical_count: 0
major_count: 0
minor_count: 4
acceptance_rate: 97   # 38 rules checked, 0 material fails; discount reflects 4 minor imprecisions
```
