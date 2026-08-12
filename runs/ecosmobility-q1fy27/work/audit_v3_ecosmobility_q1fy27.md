# A5 ADVERSARY / COMPLETENESS AUDIT — ECOSMOBILITY — Q1 FY27 (v3 merged review)

**Target:** review_full_v3_ecosmobility_q1fy27.md (Role 4 + Role 5 fully scored; 4 docs)
**Auditor context:** fresh. Re-derived from the A1 concall extract (105 lines), A2 concall ledger, the two figure supplements, and the v2 review for carry-forward. A3 reasoning NOT consulted for conclusions; A3 finding IDs used only to test coverage.
**Verdict: COMPLETE.** No orphan ledger rows, no arithmetic mismatch above rounding, no surviving un-incorporated bear counter, four brief parts present, all 12 concall findings mapped, cash-conversion cap honoured. One non-blocking cross-reference typo noted for A4.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate)

PLAIN-LANGUAGE BRIEF is present at §8 with all four labelled parts non-empty and provenance-tagged ("this quarter's concall/deck/PR" vs "Notion/prior-work"):

| Brief part | Location | Present? | Real content check |
|---|---|---|---|
| (1) Summary narrative | §8.1 (L377-379) | present | ~1 dense paragraph, 20+ lines of substance: guidance cut, third-flat-year math, candour list, trigger status, balance-sheet floor, decision status |
| (2) SECTOR intelligence | §8.2 (L381-385) | present | TAM (F&S deck slide 16), organised-share, pricing-power structural risk — provenance labelled |
| (3) BUSINESS-MODEL intelligence | §8.3 (L387-392) | present | asset-light 5/95, unit economics, forward economics, balance-sheet model, model-drift signals |
| (4) COMPETITION intelligence | §8.4 (L394-397) | present | where-it-wins / structurally-weaker / risk-to-watch; ROCE 42.9→29.4, no-barrier challenge, adjacency risk |

Gate: **PASS.**

---

## AUDIT 1 — COVERAGE (fresh enumeration vs A2 concall ledger; every A3 finding vs the review)

### 1a. Fresh grep re-count of the concall extract vs the A2 ledger

| Category | A2 count | My fresh count | Method | Orphan/missing | Status |
|---|---|---|---|---|---|
| Q&A questioner blocks | 9 | 9 | headers at L31,43,51,55,73,79,85,89,94 | none | PASS |
| Speaker turns | 65 | 65 | intro 1 + CMD opening 6 (L8/10/12/14/16/18) + CFO 4 (L21/23/25/27) + Q&A 53 + closing 1 | none | PASS |
| Formal questions | 28 | 28 | 9 primaries + 19 "Follow-up:" (Q1:4, Q2:2, Q3:0, Q4:7, Q5:1, Q6:1, Q7:0, Q8:1, Q9:3) | none | PASS |
| Zero-standing non-disclosures | 6 | 6 | L37, L65, L69, L83, L91, L92(dropped) | none | PASS |
| Hedge phrases | 10 | 10 | L33,39,45,63,65,75,83,91,98,103 | none | PASS |
| Guidance/forward statements | 14 | 14 (row-level, matches Sec 5) | spot-verified rows | none | PASS |
| Mgmt numbers | 67 | reconciled (29%+14₹+24KPI) | spot-checked buckets; 15+46=61 ties; fleet/util/online tie | none | PASS |
| Participants | 12 | 12 | Sec 1 roster | none | PASS |

No row in my fresh pass is absent from the A2 ledger; no A2 row is a phantom. **No FAIL to A2.**

### 1b. Every concall A3 finding cited/actioned in the review (task list of 12)

| A3 finding | Addressed in v3? | Where | Mapped to Q / Monitorable |
|---|---|---|---|
| F1-01 (segment margin refused L69) | yes | §3.2(5), §3.5-4C(2), §5.1 | Q2; M11 |
| F6-01 (guidance cut ~10%) | yes | §2, §3.2, §5.1 | Q1; M1 |
| F6-02 (op-leverage deferred >₹1,000 Cr) | yes | §3.2, §4.2 tw7, §5.1 | Q11; M7 |
| F6-03 (B2C + CCR automation Q2) | yes | §3.6-5A, §5.1 | Q8, Q12; M3, M4 |
| F7-01 (anchor walk-down) | yes | §2.2, §5.1 | Q4 |
| F7-02 (pricing hedges, live pressure) | yes | §3.6-5B, §5.1 | Q6, Q8; M1 |
| F12-01 (ETS-mix compression) | yes | §2.1, §3.8, §5.1 | Q5; M6 |
| F13-01 (M&A/₹150 Cr/dividend) | yes | §3.2, §4.2, §5.1 | Q7, Q13; M5, M12 |
| F14-01 (9.3% vs 10.34%) | yes | §3.9, §5.1 | Q14 |
| F17-01 (analyst credibility pushback L44) | yes | §3.5-4B, §5.1 | Q3; M1 |
| F17-02 (oil-price dropped L92) | yes | §3.6-5B, §5.1 | Q9 |
| F17-04 (moat narrative vs ROCE) | yes | §3.8, §3.5-4C(3), §5.1 | Q10; M8 |

All 12 mapped to at least one question and/or monitorable. **Contract satisfied. No orphan → no FAIL to A3.**

Every FORWARD-SIGNAL / AMBIGUOUS concall finding (F6-01/02/03, F12-01, F7-02, F13-01, F7-01, F14-01, F17-02, F17-04, F1-01) reaches a question or monitorable — verified above.

### 1c. Carried prior findings (results-filing 11 + deck/PR 12)

Cross-checked against the v2 review (L18-19 there): the results forensics (F1-01, F2-01, F2-02, F6-01, F8-01, F13-01, F13-02, F13-03, F14-01, F15-01, F15-02) and new-docs forensics (F1-01, F6-01, F7-01, F8-01, F13-01, F14-01, F16-01..06) are real v2 findings and are listed as carried in v3 §1 and the v3 YAML `a3_findings_incorporated`. Substantive carry is visible in the brief and tripwire table (F16-05 stickiness 61→55→51 at §8.3; F16-01 dropped bands at §3.3/§3.7; F13-03 FY26-AR resolver at Q15; asset-light-drift WOS residual acknowledged §5 answered/closed). **Carry-forward genuine, not fabricated.**

### 1d. One coverage blemish (non-blocking, → A4)
§2.2 (L70) states F7-01 is "Pinned as **Question 14** below," but §5 and §5.1 actually map F7-01 to **Question 4** (Q14 is the F14-01 9.3%/10.34% item). Internal cross-reference typo. The finding is NOT orphaned — it is genuinely addressed as Q4 — so this does not fail the gate; flag to A4 to fix the "Question 14" → "Question 4" reference.

---

## AUDIT 2 — ARITHMETIC (re-derived from raw figures; ₹ Crore unless noted)

Source figures: consolidated P&L supplement (Q1FY27 rev-from-ops 2,113.72 Mn; OI 37.48; employee 237.63; cost-of-service 1,587.29; other exp 70.32; D&A 61.55; finance 2.77; PBT 191.64; PAT 145.50); deck slide 14 six-year series; press-release cash 1,558 Mn.

| # | Metric (A4 claim) | A4 value | My recompute | Source | Status |
|---|---|---|---|---|---|
| 1 | Concall rev ties filing | 211.37 Cr | 2,113.72 Mn ×0.1 = 211.37 | consol L1a | TIE |
| 2 | Concall EBITDA (excl OI) ties | 218.47 Mn | 2,113.72−1,587.29−237.63−70.32 = **218.48** (0.01 rounding on stock lines) | consol | TIE |
| 3 | Concall PBT ties | 191.64 | filing 191.64 | consol L3 | TIE |
| 4 | Concall PAT ties | 145.50 | filing 145.50 | consol L5 | TIE |
| 5 | Cash ties | 1,558 Mn = 155.8 Cr | press release | PR / L27 | TIE |
| 6 | Operating EBITDA margin | 10.34% | 218.47/2,113.72 = 10.336% | — | TIE (9.3% = transcription artifact, correctly flagged) |
| 7 | Reported EBITDA margin ÷rev | 12.11% | (191.64+61.55+2.77)/2,113.72 = 255.96/2,113.72 = 12.11% | — | TIE |
| 8 | Reported EBITDA margin ÷total income | 11.90% | 255.96/2,151.20 = 11.90% | — | TIE |
| 9 | Operating→reported bridge (OI adds ~1.7pp) | ~1.77pp | reported−operating = OI = 37.48/2,113.72 = 1.77pp | — | TIE (bridge is exactly other income) |
| 10 | Q1FY26 reported margin | 13.65% / 13.44% | (186.68+58.30+2.32)=247.30; /1,811.19=13.65%; /1,839.94=13.44% | — | TIE |
| 11 | Q4FY26 reported margin (resets run) | 13.43% / 13.20% | (196.53+79.43+1.75)=277.71; /2,067.60=13.43%; /2,103.78=13.20% | — | TIE — Q4 above 12% genuinely resets |
| 12 | FY26 rev / EBITDA / margin | 808.2 / 93.9 / 11.6% | 8,081.58→808.16; 939→93.9; 939/8,082=11.62% | deck 14 | TIE |
| 13 | FY27 rev @+15%/+18% | 929.4 / 953.6 | 808.16×1.15=929.4; ×1.18=953.6 | — | TIE |
| 14 | FY27 EBITDA @~10% | 92.9 / 95.4 | 929.4×.10 / 953.6×.10 | — | TIE |
| 15 | FY27 vs FY26 (flat) | −1.1% to +1.6% | 92.9/93.9−1=−1.06%; 95.4/93.9−1=+1.60% | — | TIE — "third flat year" holds |
| 16 | Third-year series | 90.0 / 92.4 / 93.9 / ~93-95 | deck 14: 900/924/939 Mn = 90.0/92.4/93.9 | deck 14 | TIE |
| 17 | Haircut vs 13-15% base | 121-143 Cr → 28-50 Cr (23-35%) | 929.4×.13=120.8≈121; 953.6×.15=143.0; 121−93=28, 143−93=50; 28/121=23.1%, 50/143=35.0% | — | TIE — base correctly = thesis-underwritten 13-15% |
| 18 | Employee cost +20% on FY26 86.05 | ~+₹17 Cr | 860.50 Mn=86.05 Cr; ×.20=17.2 | consol L2d | TIE |
| 19 | Core PBT ex-OI YoY | −2.4% | (191.64−37.48)=154.16 vs (186.68−28.75)=157.93; −2.39% | — | TIE — profitless-at-operating-line confirmed |
| 20 | PAT YoY | +9.5% | 145.50/132.87−1=+9.51% | — | TIE |
| 21 | PAT margin ÷rev / ÷total income | 6.88% / 6.76% | 145.50/2,113.72=6.88%; /2,151.20=6.76% | — | TIE (both denominators correct) |

**No mismatch above rounding.** The only >0.01 wrinkle is item 2 (218.48 vs stated 218.47) which is a filing/deck rounding artifact on the zero stock-in-trade lines, not an A4 error. **No FAIL to A4 on arithmetic.**

---

## AUDIT 3 — ADVERSARIAL READ (three most positive claims + strongest bear counters; then the six load-bearing checks)

### 3a. Three most-positive claims and bear counters (all already incorporated → nothing to graft)

1. **"Balance sheet is the clean part — net cash ~₹137.6→155.8 Cr, near-zero borrowings."** Bear counter from same corpus: cash conversion is INDETERMINATE (no cash-flow statement anywhere), receivables built +₹24.3 Cr YoY, and ₹150 Cr is being staffed for potentially margin-dilutive M&A. **Survives — but already grafted** (§4.2 tw6 INDETERMINATE; §4.3 / flags capital-allocation watch). No new graft required.
2. **"Revenue guidance MAINTAINED 15-18%; growth on pace."** Bear counter: the growth is profitless — flat absolute EBITDA, revenue/trip −8%, driven by lower-yield ETS mix to 59%. **Survives — already grafted** (§2.1 third-flat-year; profitless-growth flag). No new graft.
3. **"Promoter TRUSTWORTHY, present, candid, acknowledged the miss."** Bear counter: the same promoter cut guidance within one quarter, refused segment margins (L69), refused pricing-moderation (L83) and deflected buyback (L39) — candour is selective. **Survives — already grafted** (EVASIVE-on-margin archetype §3.7-6E, segment-refusal flag, durable grade ON DOWNGRADE WATCH). No new graft.

No surviving bear counter is missing from A4.

### 3b. The six load-bearing checks

**Check 1 — Is Role 5 "C (Mixed)" defensible, or should it be D/lower?**
DEFENSIBLE; not a fail. A4 does not hide the tension — it surfaces every adverse element prominently: the guidance-delivery slice scored POOR (Grade D, 31% = 1.25/4, which I re-derive: EBITDA MISSED 0.0 + PAT MISSED 0.0 + revenue DELIVERED 1.0 + FY28 inflection DELAYED 0.25 = 1.25/4 = 31.25% ✓), the mechanical archetype EVASIVE, the guidance cut within one quarter, the segment refusal, and the on-record analyst pushback. The overall communication grade is a distinct axis that also weighs operational disclosure, and A4 gives specific, corroborated evidence for the C-holding mitigant: fleet utilisation, client-count reconciliation (1,400 active/>1,700 total), online-booking %, the 15+46=61 client-add split, candid admission of pricing/competition pressure, and every spoken figure tying to the filing (§3.9). Mechanically the DROPPED/CHANGED rule gives one DROPPED (deck) + one LOWERED (call) → the two-DROPPED auto-downgrade is not triggered, and the three-consecutive-margin-miss rule is at 2 of 3 — so neither mechanical downgrade forces below C this quarter, and the durable Grade B is correctly placed ON DOWNGRADE WATCH. A harsher reviewer could argue C-minus given the EVASIVE archetype, and the call is genuinely close, but because A4 (a) applied the mechanical rules correctly, (b) surfaced the POOR slice and EVASIVE quadrant rather than burying them, (c) discounted forward margin commentary ~50% at the harsh end, and (d) named the exact transparency evidence holding it at C, the grade is a reasoned blend, not a whitewash. **No INCOMPLETE against A4 on the grade.**

**Check 2 — Trigger discipline.**
CORRECT. §4.1 keeps the mechanical trigger NOT-FIRED on actuals ("guidance is not an actual"): Q4 FY26 reported 13.43% resets any run; Q1 FY27 is a single borderline quarter (12.11% ÷rev above 12%; 11.90% ÷total income below). The verdict is carried from v2 UNCHANGED and explicitly NOT re-opened. The guidance cut is NOT allowed to "fire" the trigger or move Decision Status. Conversely it is NOT under-flagged: the HIGH, management-confirmed FORWARD-firing probability is surfaced in the headline (§2), the trigger section (§4.1), tripwire 1 (§4.2), the brief (§8.1), the YAML `thesis_break_trigger`, and a dedicated flag. Discipline is exactly right — "flag, not decision."

**Check 3 — Decision Status.**
CORRECT. Stays WATCHLIST / HOLD-NOT-ADD (branch 8A-W), unchanged, because no actual trigger fired. A4 explicitly "flags; the human decides" and states "does NOT assert AVOID," while honestly noting the weight of evidence has moved toward the bear (actuals below bear on operating EBITDA 10.34% vs ≥12% floor and PAT 6.88% vs ~8%). No wrongful drift toward or away from AVOID.

**Check 4 — 13-15 vs 11-13 reframing.**
HANDLED HONESTLY. §2.2 lays out the walk-down 13-15% (Notion record) → 11-13% (retro "initially indicated") → ~10% (this call) → 10.34% actual, flags it AMBIGUOUS/lean-bear (F7-01), notes analyst Jani independently cited 11-13% at L32 as partial corroboration, and pins the reconciliation as a management question. The haircut math transparently uses 13-15% as the thesis-underwritten base (the correct base for "haircut to what the thesis underwrote"). No sleight of hand.

**Check 5 — INDETERMINATE cash conversion cap.**
HONOURED. §7 states cash conversion is INDETERMINATE (no cash-flow statement in filing, deck OR concall; CFO cited only the cash balance L27), so CFO/PAT cannot be computed and the cash figure does not resolve it. Verdict PROCEED WITH FLAGS sits at/after PROCEED WITH CAVEATS in the CLAUDE.md severity list (PROCEED / PROCEED WITH CAVEATS / PROCEED WITH FLAGS / REWORK / INSUFFICIENT EVIDENCE), so it is no cleaner than the CAVEATS cap; the missing evidence is named (resolves FY26 AR / Q2); it does not silently resolve to a clean PROCEED. Consistent with the NEVER rule.

**Check 6 — Any finding without a question/monitorable; any overstated claim?**
No unmapped finding (Audit 1b). No overstatement on the moat: A4 does NOT call the moat "broken." It reads the "right to win" as **PARTLY SUBSTANTIVE, currently losing** (§3.8) — crediting the real 30-year asset-light vendor supply base while noting it is not defending margin/returns now, with ROCE 42.9→29.4 still above WACC ~12-13%. That is a calibrated read of "ROCE decline + qualitative defence," not an overstatement. The profitless-growth and third-flat-year claims are all arithmetically supported (Audit 2). No claim exceeds its evidence.

---

## VERDICT

**COMPLETE.** The v3 merged review passes the deliverable gate (four-part brief present), the coverage audit (no orphan/phantom rows; all 12 concall findings mapped to questions/monitorables; prior results+deck findings genuinely carried), the arithmetic audit (all 21 re-derived metrics tie within rounding, including the third-flat-year math, the 28-50 Cr / 23-35% haircut against the 13-15% base, the 1.77pp operating→reported bridge, and the 2,113.72 / 218.47 / 145.50 / 1,558 tie-outs), and the adversarial audit (three positive claims' bear counters already incorporated; Role-5 C defensible; trigger kept NOT-FIRED-on-actuals with a prominent forward-firing flag; Decision Status correctly WATCHLIST/HOLD-NOT-ADD as a flag not a decision; walk-down handled honestly; INDETERMINATE cap honoured; no overstated moat claim). The lone defect is a non-blocking internal cross-reference typo (§2.2 "Question 14" should read "Question 4" for F7-01); it does not orphan the finding and does not fail the gate. Proceed to Notion save.

```yaml
stage: A5-adversary
company: "ECOSMOBILITY"
quarter: "Q1 FY27"
model: claude-opus-4-8
status: complete
verdict: COMPLETE
plain_language_brief:
  narrative: present
  sector: present
  business_model: present
  competition: present
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches: []
surviving_bear_counters: []
loop_back_to: ""
gap: ""
notes:
  - "NON-BLOCKING: §2.2 (L70) cross-references F7-01 as 'Question 14'; §5/§5.1 correctly map F7-01 to Question 4 (Q14 is F14-01). Typo only; finding is addressed, gate not failed. Suggest A4 fix on save."
  - "Re-derived independently: operating EBITDA margin 10.34% (218.47/2,113.72); reported 12.11%/11.90%; operating->reported bridge = other income = 1.77pp; FY27e EBITDA 92.9-95.4 Cr vs FY26 93.9 = -1.1% to +1.6% flat; haircut vs 13-15% base = 28-50 Cr / 23-35%; guidance-delivery sub-score 1.25/4 = 31%. All tie."
  - "Trigger: Q4 FY26 reported 13.43%/13.20% (recomputed) genuinely resets the 3-quarter run; NOT-FIRED on actuals is correct; forward-firing HIGH is a flag, not a decision."
  - "Role 5 grade C (Mixed) adjudicated DEFENSIBLE: mechanical rules applied correctly (one DROPPED + one LOWERED; 2-of-3 margin misses), POOR guidance slice and EVASIVE archetype surfaced prominently, operational transparency evidenced. Not a substantive INCOMPLETE against A4."
  - "INDETERMINATE cash conversion cap honoured; PROCEED WITH FLAGS is no cleaner than PROCEED WITH CAVEATS; missing cash-flow evidence named."
```
