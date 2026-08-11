# A5 ADVERSARY / COMPLETENESS AUDIT — SPAPPAREL Q1 FY27 (thesis-aware re-audit)

**Auditor:** A5 (Opus 4.8). Fresh context: A4 review + A1 extract + A2 ledger, with the Notion thesis-context file used only as the threshold reference for the signal test. Every A4 cite re-checked against the extract; every derived metric re-computed from raw filed millions (x0.1 = Cr). This audit supersedes any prior A5 pass on the thesis-blind review.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate, run first)

PLAIN-LANGUAGE BRIEF is Section 6 of the review (L536–552). All four labelled parts present and carrying real, non-placeholder content:

| Part | Heading present | Location | Content check | Status |
|---|---|---|---|---|
| 1. Summary narrative | yes | L538–540 | ~1 dense para, 25+ lines of substance; walks headline PAT, revenue decline, margin, SPUK tripwire fire, signal count, auditor caveat, cash INDETERMINATE, decision status | PRESENT |
| 2. Sector intelligence | yes | L542–544 | Tirupur knit-export frame, demand cycle, China+1/FTA/PLI tailwinds, FX + new-market-loss headwinds, Salem/US-share deferral | PRESENT |
| 3. Business-model intelligence | yes | L546–548 | Three revenue engines, parent-vs-group leverage split, reinvestment/tax-shield mechanics, overseas-accretion question | PRESENT |
| 4. Competition intelligence | yes | L550–552 | Win/lose vs KPR, Gokaldas; sub-scale loss-making front-end; margin-dilution risk; peer caveat | PRESENT |

Gate PASSES. (Minor blemish, not gate-failing: L540 contains a self-corrected typo "Rs 74.84 Cr... a Rs 7.5 Cr loss" — the magnitude is correctly restated to Rs 7.5 Cr in the same clause. Content intact.)

---

## AUDIT 1 — COVERAGE (fresh independent enumeration vs A2 ledger)

Fresh grep/sweep over the extract, diffed against the A2 counts:

| Category | A2 count | My fresh count | Method | Orphan/missing | Status |
|---|---|---|---|---|---|
| Notes | 12 | 12 | SA notes L392,395,397,400,405 (5) + Consol L575,577,579,581,583,586,588 (7) | none | MATCH |
| Line items | 57 | 57 | SA P&L+OCI 27 + Consol P&L+OCI 30 (zero-standing row carried) | none | MATCH |
| Zero-standing | 1 | 1 | SA tax note (b) all-dash L357 | none | MATCH |
| Agenda items | 7 | 7 | Board letter L33–86 items 1–7 | none | MATCH |
| Auditor paras | 11 | 11 | SA 4 (L272–298) + Consol 7 (L424,430,436,445,464,475,485) | none | MATCH |
| Entities | 9 | 9 | Consol auditor list a–i, L447–455 | none | MATCH |
| Annexure items | 9 | 9 | Split-particulars L128–158 | none | MATCH |
| Signature blocks | 4 | 4 | Vinodhini; Gururaj SA; Gururaj Consol; Sundararajan/Balaji | none | MATCH |

**Every fresh count matches the ledger. No row my pass found is missing from the ledger (nothing to return to A2).**

**Ledger-row → A4 disposition (orphan check).** Every ledger table and flag is either cited in A4 or dispositioned:
- 57 line items → carried in Step 1A/1B tables, line-anchored. Cited.
- Auditor paras 5/6/7 → read verbatim in Section 2.7 (L379–392) and gate item (d). Cited.
- 9 entities / entity-granularity mismatch → C-5 note + Section 2.7. Cited.
- Ritz NEW_ENTITY → C-4 + Q3 + M8. Cited.
- ZERO_STANDING SA tax note vs non-zero consol prior-year line → Q4 (L435). Cited.
- OCI hedge swing → Q5. Adj Revenue/EBITDA (F16) → Q10. Standalone Rs10m subtotal gap (A3-11) → Q7. Paid-up-capital inter-statement mismatch (A3-08) → Step 0C + footnote ‡. Split/MOA/ESOP → Table 2.7 + Q6. All cited.
- A3-01…A3-12 all listed incorporated (L21); F1–F17 state carried (L22).

**One enumerated forensic is carried but not separately dispositioned (noted, NOT gate-failing — see Audit 2 item M):** the A2 flag-summary line 241 ARITHMETIC_MISMATCH on the *consolidated* PBT step (368.21 − 8.72 = 359.49 vs filed 358.49; a 1.00m / Rs 0.1 Cr offset in the current quarter, plus the mirror Q4FY26 offset). A4's Q7 addresses the standalone Rs10m gap and states the "consolidated equivalent ties exactly" — true for the expense subtotal (L529 ties), but the separate associate-to-PBT 1.00m offset is not explicitly surfaced. This is a filed-source offset already enumerated by A2, immaterial (0.1 Cr) and downstream-inert (see Audit 2). Rows themselves are cited; the flag is undispositioned. Recommendation, not a fail: A3/A4 add a one-line "reviewed, 0.1 Cr filed typesetting offset, immaterial."

Coverage verdict: **PASS, no orphan rows, no missing rows.**

---

## AUDIT 2 — ARITHMETIC (recomputed from raw filed millions, x0.1)

Spot-checked every derived metric in A4's tables. Sample of the load-bearing recomputations:

| Metric | A4 value | My recompute (source lines) | Status |
|---|---|---|---|
| SA Op EBITDA Q1FY27 | 46.77 | 35.01+10.60+2.42−1.26 = 46.77 (L354/351/350/341) | OK |
| SA Op EBITDA margin Q1FY27 | 17.0% | 46.77/275.12 = 17.00% (L340) | OK |
| SA ETR Q1FY27 | 24.2% | 8.48/35.01 = 24.22% (L359/354) | OK |
| SA PAT YoY | +33.4% | 26.54/19.89−1 = +33.4% (L360) | OK |
| Consol Op EBITDA Q1FY27 | 61.37 | 36.82+13.24+14.86−3.55 = 61.37 (L536/533/532/521) | OK |
| Consol Op EBITDA margin Q1FY27 | 15.3% | 61.37/401.08 = 15.30% (L520) | OK; ties mgmt 61.36 Cr (L200) |
| Consol EBITDA margin +bps | +220 bps | 15.30% − 13.12% = +2.18pp (52.92/403.44) | OK |
| Consol ETR Q1FY27 | 30.6% | 10.98/35.85 = 30.63% (L547/540) | OK |
| Consol PAT YoY | +20.4% | 24.87/20.66−1 = +20.4% (L548) | OK |
| Consol revenue YoY | −0.6% | 401.08/403.44−1 = −0.58% | OK |
| SA revenue YoY | −5.0% | 275.12/289.68−1 = −5.03% | OK |
| SA finance cost YoY | −66.4% | 2.42/7.21−1 = −66.4% (L350) | OK |
| Consol finance cost YoY | +26.1% | 14.86/11.78−1 = +26.1% (L532) | OK |
| SA PAT bridge total | +6.65 | 26.54−19.89 = 6.65; components 2.21−1.07+4.79−0.02+0.73 ≈ 6.64 | OK (rounding) |
| Consol PAT bridge total | +4.21 | 248.74−206.55 = 42.19m = 4.22 Cr | OK (see M) |
| S-vs-C gap Q1FY27 | −1.66 | 248.74−265.37 = −16.63m = −1.66 Cr | OK |
| S-vs-C gap FY26 | +13.11 (+14.9%) | 100.95−87.84 = +13.11; /87.84 = +14.9% | OK |
| S-vs-C Q1 YoY swing | −2.43 (≈9.2% of SA PAT) | +0.77 → −1.66 = −2.43; /26.54 = −9.2% | OK |
| SPUK EBITDA | −1.04 Cr (−3.1% margin) | Rs(10.4)m = −1.04 Cr; /33.30 = −3.12% (L233–235) | OK |
| Consol OCI swing | +8.2 Cr | 81.88m = 8.19 Cr (L565) | OK |
| Unreviewed loss share | 30.1% of consol PAT | 74.84/248.74 = 30.1% (L478/548) | OK |
| Unreviewed revenue share | ~16% | (201.84+452.55)/4046.26 = 16.2% (L466/477/522) | OK |

Every A4-derived metric reproduces within rounding. **No A4 computational error found.**

**Item M (filed-source residual, not an A4 error).** The consolidated PAT bridge components (using precise millions) sum to +43.20m against an actual PAT delta of +42.19m — a ~1.01m residual. This traces entirely to the filing's own internal 1.00m offset at the consolidated PBT step (L536 368.21 − L539 8.72 = 359.49 vs L540 358.49), already enumerated by A2 (flag-summary L241) and independently confirmed here. It is 0.1 Cr, does not move consol PAT (filed directly at L548 = 24.87), does not move ETR (30.6% vs 30.5% if the 1m were in PBT — still >27% and still explained), and changes no signal, the tripwire, or the S-vs-C gap. Classified as a filed-source data-quality offset, not an A4 arithmetic failure. Disposition recommended (Audit 1), no loopback required.

Arithmetic verdict: **PASS.**

---

## TARGETED RE-VERIFICATION (task-specified)

**1. Early Warning Signals — actual value, line, and FIRED call re-checked against the thesis thresholds (thesis L43–54):**

| # | Threshold | A4 actual (line) | My check | Call defensible? |
|---|---|---|---|---|
| 1 | Consol rev <Rs400 Cr OR sequential decline | 401.08 Cr (L520), QoQ +9.9% | L520 4,010.76m = 401.08; QoQ vs 364.91 = +9.91% | **YES — NOT FIRED.** Above 400 by Rs1.08 Cr; "sequential" = QoQ, which is +9.9% (up). The YoY −0.6% "decline texture" A4 flags is real but is NOT the signal's "sequential" test. Marginal but correctly called; A4 flags the marginality explicitly. |
| 2 | SA EBITDA% <15% sustained | 17.0% (L340/354) | 46.77/275.12 = 17.0% | YES — NOT FIRED |
| 3 | SPUK EBITDA <0% | −1.04 Cr (L233–235) | Rs(10.4)m negative, confirmed L233–235 | YES — FIRED |
| 4 | ETR >27% **no explanation** | Consol 30.6% (L547/540) | 30.63%, breaches 27% | **YES — NOT FIRED defensible.** Both conditions required; the disqualifying "no explanation" is unmet. Standalone ETR is 24.2% (<27%); the entire elevation is a consolidation effect from unrelieved subsidiary losses — evidenced by the consol prior-year tax line being non-zero (L545) while standalone is all-dashes (L357), and by the 30.6% vs 24.2% gap. Thesis itself pre-frames ETR as "structural 28–29%" (thesis L64–66). A4 correctly logs that 30.6% is ~2pp above the band as a mild drift (M14), not a fire. Judgement stands. |
| 5 | Assoc loss >Rs2.5 Cr accelerating | −0.87 Cr (L539) | (8.72)m = −0.87; decelerating QoQ −1.07→−0.87 | YES — NOT FIRED (far below 2.5; not accelerating sequentially) |
| 6–10 | utilisation / order book / insider / US-share / broker | not in Reg 33 filing | confirmed absent | YES — NOT TESTABLE-IN-FILING (thesis L59–60 concurs) |

All 10 signal actuals match the extract at the cited lines; all FIRED/NOT FIRED/NOT TESTABLE calls are correct. Testable count 1-of-5 fired; Master 3+ rule not triggered — correct.

**2. SPUK pre-committed tripwire — independently confirmed:**
- SPUK Q1 FY27 EBITDA is NEGATIVE: extract L233–235 reads "S.P. Apparels UK (P) limited revenue stood @ Rs. 333.0 million... with EBITDA of Rs. (10:4) million" = Rs(10.4)m = **−1.04 Cr**. Confirmed negative, correct line.
- Q4 FY26 SPUK EBITDA −Rs7.8 Cr is thesis/prior-work provenance (thesis L36), correctly labelled by A4 as not-from-this-filing.
- Two consecutive negatives → tripwire FIRES. Correct.
- **FLAG-not-decide check: PASS.** A4 states (5.2 VERDICT, 5.5, 8A-W, YAML `pipeline_action`) that the pipeline FLAGS the fired tripwire and names the pre-committed action (thesis-broken → AVOID) but does NOT itself change the Notion Decision Status property, which remains WATCHLIST pending Keerti's ruling. This matches the orchestrator rule (thesis L70–74) and CLAUDE.md ("flags propagate; Keerti decides; no STOP verdict"). The pipeline nowhere asserts a Decision-Status change. Correct.

**3. Plain-language brief:** present and complete — see Audit 0. PASS.

---

## AUDIT 3 — ADVERSARIAL READ (three most-positive claims, strongest bear from same extract)

| # | A4's positive claim | Strongest bear counter (same extract) | Survives? | Already in A4? |
|---|---|---|---|---|
| 1 | Consol Op EBITDA margin +220bps to 15.3%, "best signal in the print," step-up | Margin rose on −0.6% YoY revenue and ~1% below the derived H1FY26 run-rate (405/qtr); cost/mix not volume; single quarter measured off a soft balancing-figure Q4 base (C-6) | Valid | YES — Step 2 ans 2, Step 3 diagnostics, "needs Q2 confirm ≥15%" (L215, M13). No graft needed |
| 2 | Standalone record PAT +33.4% YoY | 72% of the gain is the finance-cost collapse (7.21→2.42 Cr) + lower ETR, on −5% revenue; normalise finance costs and run-rate PAT drops ~4.8 Cr/qtr | Valid | YES — Step 4A fully walks this. No graft needed |
| 3 | SPUK loss narrowing to near-breakeven (−7.8→−1.04 Cr) tempers the fired tripwire | The SPUK figure is unaudited management-page only (L233–235), plausibly inside the Rs74.84m reviewed-by-NO-auditor basket (L475–483); QoQ revenue ~flat-to-down so the "improvement" could be onboarding-cost timing, not a structural fix; the −7.8 Cr comparator is thesis, not this filing | Valid | YES — 5.2 point 2, gate item (d), provenance caveat L510. No graft needed |

**No surviving bear counter is un-incorporated.** All three positive claims already carry their symmetric bear in the review. Nothing to graft into A4.

---

## VERDICT

**COMPLETE.**

- Deliverable gate: PASS (all four brief parts present, non-empty).
- Coverage: PASS (fresh enumeration matches ledger 8/8; no orphan rows, no missing rows; all A3-01…A3-12 dispositioned).
- Arithmetic: PASS (every A4-derived metric reproduces within rounding; no computational error).
- Signal/tripwire re-verification: PASS (all 10 actuals tie to cited lines; all calls correct; Signal 1 marginal-NOT-FIRED and Signal 4 no-explanation-unmet both defensible; SPUK negative confirmed; FLAG-not-decide discipline intact).
- Adversarial: PASS (no surviving un-incorporated bear counter).

**Non-blocking advisory (does not fail the gate):** one enumerated A2 ARITHMETIC_MISMATCH — the consolidated PBT-step 1.00m (Rs 0.1 Cr) filed-source offset (L536/539/540, mirror at Q4FY26) — is carried but not separately dispositioned by A4, whose Q7 states the consolidated "ties exactly" (true only for the expense subtotal). Immaterial (0.1 Cr, downstream-inert to PAT, ETR, every signal, the tripwire, and the S-vs-C gap). Recommend A4 add a one-line "reviewed, immaterial filed offset" for full closure. Not a FAIL: the rows are cited, the discrepancy is a filed-source item already enumerated by A2, and it moves no conclusion.

Cleared to proceed to Notion save.

```yaml
stage: A5-adversary
company: "SPAPPAREL"
quarter: "q1fy27"
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
advisory_non_blocking: "Consolidated PBT-step 1.00m (Rs0.1 Cr) filed-source offset (L536/539/540) enumerated by A2 (flag-summary L241) is carried but not separately dispositioned by A4; immaterial, moves no signal/tripwire/PAT/ETR; recommend a one-line 'reviewed, immaterial' note. Does not fail the gate."
```
