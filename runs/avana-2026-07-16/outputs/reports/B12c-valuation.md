# VERIFIER C — FRAMEWORK ADHERENCE (PHASE 3, VALUATION + THESIS PASS) — AVANA

**Company:** Avana Electrosystems Ltd (AVANA) | **Run date:** 2026-07-16 | **Verifier run:** 2026-07-17
**Model:** claude-opus-4-8 | **Scope:** Valuation (B11) + Input Assembly (B10) + Role 2 decision logic + the two authoritative operator overrides in fttcp-deliberation.md.
**Framework authority:** Master v3.3 (Section 1B, RRM dual-track, Hurdle Ratio, Role 2 rules, position sizing) / Section 1B v3.3 Amendments (continuous Pillar 1 / ROCE>33% branch / 4.5 / UA ordering / Tier A-B / sector cap) / FTTCP v1.2.

**SCOPE NOTE.** Gate 0 (B01) and Emerging Moat (B07) were audited in Phase 1 (100%, 0 CRITICAL / 0 MAJOR) and are NOT re-audited here. This pass audits the VALUATION and the THESIS decision logic, judging adherence GIVEN the two authoritative operator overrides recorded in the deliberation (an override applied as written and stated is COMPLIANT, not a violation).

**B14 STATUS.** The Role 2 thesis report B14.md is NOT on disk at the time of this audit (reports/ contains up to B12c; blocks/ contains up to B12c). The Role 2 decision rules, position sizing, and entry/MoS cascade were therefore audited AS CARRIED in B11 Section 4 (verdict card, entry/MoS, sizing, hardest-verdict-wins rationale), which is where B11 already renders the decision. When B14 is produced it MUST reproduce WATCHLIST / Small (2-3%) / entry Rs 145-165 / MoS Rs 132; if it diverges it requires a fresh Verifier C pass. This is flagged, not a fail.

---

## PART 1 — THE TWO AUTHORITATIVE OVERRIDES: APPLIED AS WRITTEN?

| # | Override (deliberation) | Required application | B10/B11 as written? | Verdict |
|---|---|---|---|---|
| O1 | Pillar 1 anchors on operating ROCE ~40% (NOT the Amendment 4.5 normalized-30% blend, withdrawn); base PE ~26x via ROCE>33% formula; surplus cash separate at 1x; recovery via Pillar 1, strategic route barred | Pillar 1 = 26.1x from 24+0.3×(40-33); Amdt 4.5 explicitly withdrawn; net cash Rs 27.06 Cr at 1x separate; single-credit stated | Yes. B11 §Pillar 1 states "Amendment 4.5 normalized-30% blend is WITHDRAWN for this name"; base 26.1x; "ROCE recovery credited via: Pillar 1"; Strategic route BARRED (+0x) | PASS |
| O2 | Growth priced in forward earnings (forward-PE-at-exit), not stripped; Pillar 3a +0x, no double count | Destination PE applied to exit-year forward EPS; Pillar 3 = +0x | Yes. Method = forward-PE-at-exit (exit FY29 priced on FY30 forward EPS); Pillar 3 = +0x; growth only in the ladder | PASS |

Both overrides are applied as written and explicitly stated in the worksheet. Compliant.

---

## PART 2 — VALUATION (B11) RULE-BY-RULE

Recomputed value shown beside any item where I re-derived it. "Repro" = my independent recomputation reproduces the report figure.

| # | Rule (framework cite) | Report | My recompute | Verdict |
|---|---|---|---|---|
| V1 | Pillar 1 uses ROCE>33% branch 24+0.3×(ROCE-33), cap 30x, NOT the ≤33% continuous 0.5×ROCE+7.5 (Master L211-214) | 26.1x at 40% | 24+0.3×7 = 26.1x (ref pt 40%→26x, L214). Correctly used the >33% branch (the ≤33% formula would give 27.5→cap24) | PASS (repro) |
| V2 | FTTCP ROCE verdict is sole Pillar 1 authority (RECOVERING; operating ~40%) | RECOVERING, operating ~40% | Matches Ruling 8 + Override 1 | PASS |
| V3 | Amendment 4.5 normalized blend correctly handled | Withdrawn per O1 | O1 withdraws it; report does not apply it | PASS |
| V4 | Single-credit rule, route stated, strategic barred (Amdt 4) | Route = Pillar 1; strategic +0x | Stated verbatim; strategic barred | PASS |
| V5 | Surplus/idle cash valued separately at 1x, not in ROCE denominator (O1) | Rs 27.06 Cr (Rs 12/sh) at 1x; ~22 Cr out of denominator | See MINOR-1 (22 removed vs 27.06 added-back bridge); within O1's stated Rs 22-27 range, offset by conservative 40% ROCE | PASS (MINOR-1) |
| V6 | Pillar 2 multiplier matches determination (0.80x) | 0.80x | Matches Ruling 7 / Override | PASS |
| V7 | Pillar 2 INDETERMINATE; no growth offset while unresolved; no offset on structural | +0 offset | Correct; growth offset withheld | PASS |
| V8 | INDETERMINATE never resolves to a clean pass; caps disposition at PROCEED WITH CAVEATS (CLAUDE.md NEVER) | Capped PROCEED WITH CAVEATS | Correct; 1.0x sensitivity shown as sensitivity only | PASS |
| V9 | Pillar 3a +0x (📄 gates unmet: order book 0.62x<1.0x, SOM 14.8%<20%, grade INSUFFICIENT not A/B) (Amdt 4.1) | +0x | All four gates fail; +0x correct | PASS |
| V10 | Pillar 3b +0x (EM 2.5 < 25) (Amdt 4.1/B07) | +0x | Correct | PASS |
| V11 | Pillar 3c +0x (order book/rev 0.62x < 2.5-yr gate) (Amdt 4.2) | +0x | Correct | PASS |
| V12 | Pillar 4 strategic +0x, single-credit respected | +0x | Correct | PASS |
| V13 | UA in Amendment 3 order: F2 = F×1.25 BEFORE cap; barred here | UA barred, F2=F | Listed <12m; F2=F; no 1.25x | PASS |
| V14 | UA three qualifiers evidenced (listed<12m NO; Gate0/EM NO; FII+DII NOT FOUND) | All documented | Qualifier logic correct; UA No | PASS |
| V15 | Sector cap 25x ABSOLUTE (Cables/Industrial), manifest 38x defect rejected | 25x; 38x rejected | Ruling 4; destination 20.9x < 25x, no breach | PASS |
| V16 | Both tracks present and carried through all FVs and verdict card | Track 1 RRM + Track 2 additive throughout | Both present in §1B, §3, verdict card, YAML | PASS |
| V17 | RRM percentage-point reading (Amdt 4.4): 1+(13.5-16)×0.12 = 0.70 | 0.70 | 1-0.30 = 0.70; floor 0.70 | PASS (repro) |
| V18 | RRM r bounded [9,18]; base small/micro 14, adjusted up for governance/thin evidence | r=16 | Within [9,18]; adjustment reasoned | PASS |
| V19 | Track 1 = Fundamental Base PE × RRM | 26.1×0.70 = 18.3x | 18.27→18.3x. Choice of ROCE base 26.1 (not QAB 20.9) — see MINOR-2 | PASS (MINOR-2) |
| V20 | Track divergence stated; >15% forces conservative track to govern entry (L394) | 12.4%, <15%, Track 2 governs | (20.9-18.3)/18.3 = 14.2%; /20.9 = 12.4% — both <15% on any denominator; rule does not bind | PASS |
| V21 | Destination PE range = ±7.5% nearest 0.5x (Amdt 6) | 19.5-22.5x | 20.9×0.925/1.075 = 19.33/22.47 → 19.5/22.5 | PASS (repro) |
| V22 | Hurdle Ratio formula (1+g)³×(destPE/currentPE), threshold 1.953 Tier A (Amdt 2/4.3) | literal 1.63 shown | (1.30)³×(20.9/28.13)=1.63 | PASS (repro) |
| V23 | Current PE basis stated (trailing FY26) | 28.13x trailing | 146/5.19 = 28.13 | PASS (repro) |
| V24 | EPS-basis CONSISTENCY (SFL 2026-07-14): no trailing-entry / forward-exit mix | forward row 2.12 | Reproduces the CONSISTENT forward-forward HR — see MINOR-3 | PASS (MINOR-3) |
| V25 | HR CONDITIONAL logic + de-rating headwind flagged; bull capped Base+5% on INSUFFICIENT credibility (Amdt 2, L406) | CONDITIONAL; bull 35%; bull_used false | Correct conservative handling; see MINOR-3 note on PASS-vs-CONDITIONAL | PASS |
| V26 | Forward-PE-at-exit per O2; ladder assembled to year AFTER exit (FY30) (AMAGI precedent) | exit FY29 on FY30 EPS | Ladder runs to FY30; consistent with established convention | PASS |
| V27 | Bull discipline: realised 70.7% PAT CAGR NOT used at face value; capped 35% | 35% cap | Correct (Amdt 2 / Section 2A) | PASS |
| V28 | 4D weights match grade: INSUFFICIENT → most-conservative D weights (45/40/15) | D weights | Correct; stated | PASS |
| V29 | SOM cross-check performed | Yes, TENSION-SOM carried | Base 30% > SOM 14.8% and realised 25.8%; justified-excess reasoning + bear anchored to SOM | PASS |
| V30 | Net cash added per share at 1x | Rs 12 | 27.06/2.26 = 11.97 → 12 | PASS (repro; see MINOR-1) |
| V31 | Every unresolved input handled by conservative rule, NO silent fills / no estimates | All NOT FOUND flagged | receivables/FII-DII/FCF/guidance all NOT FOUND, conservative fills | PASS |
| V32 | One-improvement-one-mechanism (no double count growth or cash) | Held | Growth only in ladder; ROCE recovery only Pillar 1; cash only Pillar 2 | PASS |
| V33 | EV/EBITDA + P/B cross-checks performed (secondary/tertiary) | Yes | Directionally consistent, weights 20/10 | PASS |

### Numbers I recomputed independently (all reproduce)

| Quantity | Report | My recompute | Match |
|---|---|---|---|
| Pillar 1 base | 26.1x | 24+0.3×7 = 26.1x | Yes |
| Quality-adjusted base | 20.9x | 26.1×0.80 = 20.88 | Yes |
| Track 2 destination PE | 20.9x | min(20.9, 25) = 20.9x | Yes |
| Track 1 destination PE | 18.3x | 26.1×0.70 = 18.27 | Yes |
| Current PE (trailing) | 28.13x | 146/5.19 = 28.13 | Yes |
| HR base (forward) | 2.12 | (1.30)⁴×0.743 = 2.122 | Yes |
| HR base (trailing) | 1.63 | (1.30)³×0.743 = 1.633 | Yes |
| HR bull (forward) | 2.47 | (1.35)⁴×0.743 = 2.468 | Yes |
| FV base (Track 2) | Rs 322 | 14.82×20.9+12 = 321.7 | Yes |
| FV bear / bull | 202 / 372 | 189.8+12 / 360.1+12 | Yes |
| Expected 3yr CAGR | 22.7% | 11.4(.45)+30.2(.40)+36.6(.15) = 22.70 | Yes |
| Entry Track 2 / Track 1 | 165 / 145 | 322/1.953=164.9 ; 283/1.953=144.9 | Yes |
| MoS | Rs 132 | 165×0.80 = 132 | Yes |
| Downside floor / U-D | Rs 120 / 6.9x | 20.9×5.19+12=120.5 ; 120.5/17.5 | Yes |

---

## PART 3 — THE HURDLE RATIO EPS-BASIS CONSISTENCY (SFL 2026-07-14 lesson), in full

The SFL lesson: do not mix a trailing current PE with a forward-exit destination inconsistently; the forward-PE-at-exit method must be applied consistently.

The report presents the authoritative HR row as **(1+g)⁴ × (20.9 / 28.13)** where 28.13 is explicitly the TRAILING current PE. On its face this looks like the SFL trap — a 4-year-grown exit divided by a trailing entry multiple. I tested it algebraically:

- Consistent forward-forward basis: entry priced on FY27 forward EPS (146/6.75 = **21.63x forward**), exit priced on FY30 forward at the FY29 exit (20.9x). Over the 3-year hold FY27→FY30 EPS grows (1+g)³.
- Consistent HR = (1.30)³ × (20.9 / 21.63) = 2.197 × 0.9663 = **2.123**.
- Report's HR = (1.30)⁴ × (20.9 / 28.13) = 2.856 × 0.7430 = **2.122**.

These are **identically equal** because 20.9/21.63 = (20.9/28.13)×1.30. So the report's number is NOT a trailing/forward inconsistency in substance — it is the internally-consistent forward-forward Hurdle Ratio, merely written with a trailing entry PE and a 4th power. The convention (exit FY29 priced on FY30 EPS) is the established operator forward-PE-at-exit method, matching the AMAGI 2026-07-12 phase-3 precedent (destination on FY30 EPS, Verifier C accepted). The report also shows the pure trailing-trailing HR (1.63) and honestly flags the de-rating headwind — exactly the transparency the SFL lesson demands. Substance is sound. The only defect is presentational (see MINOR-3).

One consequence worth stating plainly: on the authoritative forward method HR(Base) = 2.12 ≥ 1.953 is a framework **PASS**, not CONDITIONAL. The report conservatively downgrades to CONDITIONAL citing the trailing de-rating and INSUFFICIENT credibility. This is more conservative than the framework requires and has NO decision impact (the decision is WATCHLIST regardless, governed by Gate 0 < 60). Acceptable conservative overlay.

---

## PART 4 — ROLE 2 DECISION LOGIC (audited as carried in B11 §4; B14 not yet on disk)

| # | Rule (Master v3.3 L804-819, L915-916) | Report | Verdict |
|---|---|---|---|
| R1 | Hardest-verdict-wins across Gate 0 <60, INDETERMINATE cash, promoter CAUTION, HR CONDITIONAL | WATCHLIST | PASS (see MINOR-4) |
| R2 | Gate 0 < 60 → default WATCHLIST regardless of narrative (L915) | WATCHLIST, cited | PASS |
| R3 | AVOID sub-triggers checked: U/D < 2x? Hurdle STOP? Promoter CONCERN/AVOID? | U/D 6.9x (no); HR CONDITIONAL not STOP (no); promoter CAUTION not CONCERN (no) | PASS |
| R4 | Tier A hurdle 25% / divisor 1.953 stated on verdict card first line (Amdt 4.3) | "Tier: A \| Hurdle: 25% (divisor 1.953)" | PASS |
| R5 | Entry = base FV ÷ 1.953 (Tier A cascade) | 322/1.953 = 165; 283/1.953 = 145 | PASS (repro) |
| R6 | MoS = 20% below entry | 165×0.80 = 132 | PASS (repro) |
| R7 | Position sizing: Small (2-3%), promoter cap binds (L815-818) | Small; AVERAGE Gate 0 + CAUTION bar Medium/Large | PASS |
| R8 | Not AVOID justification (valuation constructive on authoritative method) | Stated: base clears 25% on forward method | PASS |
| R9 | Thesis-broken triggers stated, measurable (KIADB, receivables, FY27 <SOM) | Present | PASS |
| R10 | SHARED CATALYST flag carried for devil's advocate | Carried (KIADB under both Pillar 1 and ladder) | PASS |

MINOR-4: there is a genuine framework tension between L809 ("AVOID: Gate 0 AVERAGE/AVOID …") and L915 ("Gate 0 below 60 → default WATCHLIST regardless of narrative"). Gate 0 here is AVERAGE (49/100). The report resolves to WATCHLIST by citing L915 and by verifying that none of the other L809 AVOID sub-triggers fire (U/D 6.9x ≥ 2x; Hurdle CONDITIONAL not STOP; promoter CAUTION not CONCERN/AVOID). This is the correct resolution and distinguishes AVANA from the prior on-valuation AVOIDs (AURUM/ASIANENE/AMAGI), which all had Hurdle STOP and CMP far above the entry zone; here Hurdle clears on the authoritative method and CMP Rs 146 sits inside the entry zone (below Track 2 entry 165, at Track 1 entry 145) and above MoS 132. WATCHLIST concurs. Logged for transparency; not a fail.

---

## PART 5 — INPUT ASSEMBLY (B10) SPOT CHECK

| Check | Result |
|---|---|
| Overrides carried verbatim to B10 (O1, O2, cash 0.80x, sector 25x, UA barred) | PASS |
| Sector cap corrected 25x, manifest 38x logged as defect | PASS |
| Net-cash SIGN correct (cash 27.83 > borrowings 0.77 → net CASH 27.06; EV = 330.63 − 27.06 = 303.57) — no ASIANENE-style sign error | PASS |
| EPS ladder flagged illustrative; growth assumption anchored; exit-year + FY30 assembled | PASS |
| Every gap = NOT FOUND, no estimates (receivables, FII/DII, FCF, capex, guidance, DPS) | PASS |

---

## FINDINGS (all MINOR; 0 CRITICAL, 0 MAJOR)

**MINOR-1 — Cash bridge asymmetry (B11 §Pillar 1 / §3).** Rs ~22 Cr of idle cash is removed from the ROCE denominator (operating capital 59.85 − 22 = 37.85) but the full net cash Rs 27.06 Cr (Rs 12/share) is added back separately at 1x. The ~Rs 5.8 Cr difference sits both inside operating capital (earning the 26.1x multiple) and in the separate 1x add-back. Immaterial: ~Rs 2.6/share on a Rs 322 FV (<1%), within Override 1's stated "Rs 22 to 27 Cr" range, and offset by the deliberately conservative 40% ROCE choice (computed operating ROCE is ~44%, and would be ~52% if all cash were removed). No decision impact.

**MINOR-2 — RRM Fundamental Base PE definition (B11 §Track 1).** Track 1 uses the ROCE base 26.1x as "Fundamental Base PE" (→ 18.3x), not the quality-adjusted base 20.9x (which would give 14.6x). The report's choice is disclosed and reasoned (avoids double-penalising cash, since heavy WC already raised r to 16). It is a defensible reading, but the alternate reading would push track divergence from 12.4% to ~30%, which under L394 forces the conservative track to govern the entry zone. Moot for the decision because Override 1 anchors the additive Track 2 as governing and the destination PE / WATCHLIST decision do not change either way. Logged because the choice is the one that keeps divergence under the 15% threshold.

**MINOR-3 — Hurdle Ratio presentation (B11 §Hurdle Ratio).** The authoritative HR row is written as (1+g)⁴ × (trailing 28.13x), which on its face resembles the SFL trailing/forward inconsistency. The value (2.12) is in fact identical to the internally-consistent forward-forward HR (entry on FY27 forward PE 21.63x, exit on FY30 forward). Substance is correct; the row should show the forward entry PE (21.6x) to make the consistency explicit rather than leaving a 4th-power-over-trailing expression that an auditor must re-derive. Related: HR(Base) 2.12 ≥ 1.953 is technically a framework PASS; labeling it CONDITIONAL is a conservative overlay (justified by the trailing de-rating and INSUFFICIENT credibility) with no decision impact.

**MINOR-4 — Decision-rule tension navigated, not shown as a rule cite (B11 §4H).** L809 (Gate 0 AVERAGE → AVOID) vs L915 (Gate 0 < 60 → WATCHLIST) conflict; the report resolves correctly to WATCHLIST via L915 and confirms no other AVOID sub-trigger fires, but does not surface the L809/L915 conflict explicitly. Correct outcome; transparency note only.

**MINOR-5 — B14 (Role 2 thesis) not on disk.** The Role 2 stage report is absent at audit time; its decision logic was audited as carried in B11 §4. B14, once produced, must reproduce WATCHLIST / Small (2-3%) / entry Rs 145-165 / MoS Rs 132 and requires a fresh Verifier C pass if it diverges.

---

## RECOMPUTATION SUMMARY

- **Destination PE (governing, Track 2): 20.9x** — reproduces exactly. RRM Track 1 18.3x reproduces. Range 19.5-22.5x reproduces.
- **Hurdle Ratio: base 2.12 (forward, consistent) / 1.63 (trailing) — reproduces.** Verdict CONDITIONAL is a conservative label over a technical PASS; no decision impact.
- **Entry Rs 145-165, MoS Rs 132 — reproduces.**
- **Decision: WATCHLIST (Small 2-3% if it ever qualifies) — reproduces.**

Every rule checked passes on independent recomputation. The five findings are MINOR (imprecision / presentation / a not-yet-written downstream report); none changes the destination PE by >1x, none flips the Hurdle verdict in a decision-relevant way, and none changes the decision. The two operator overrides are applied as written and stated.

**DECISION: CONCUR.** Recomputed destination PE 20.9x (governing) reproduces; recomputed decision WATCHLIST reproduces.

---

```yaml
stage: B12c-valuation
company: "AVANA"
run_date: "2026-07-16"
model: claude-opus-4-8
status: complete
scope: "Phase-3 valuation + thesis adherence pass. Gate 0 (B01) and Emerging Moat (B07) audited in Phase 1 (100%, 0 CRIT/0 MAJ) and NOT re-audited here. B14 (Role 2 thesis) not on disk at audit time; Role 2 decision logic audited as carried in B11 Section 4."
gate0: {rules_checked: 0, fails: [], note: "audited Phase 1; not re-run"}
emoat: {rules_checked: 0, fails: [], note: "audited Phase 1; not re-run"}
valuation: {rules_checked: 48, fails: []}
overrides_applied_as_written: true
findings:
  - {severity: "MINOR", location: "B11 Pillar 1 / Section 3", description: "Cash bridge asymmetry: ~Rs22 Cr removed from ROCE denominator but full net cash Rs27.06 Cr (Rs12/sh) added back separately at 1x; ~Rs5.8 Cr double-touched. <1% of FV, within Override 1's Rs22-27 Cr range, offset by the conservative 40% ROCE (vs ~44% computed). No decision impact."}
  - {severity: "MINOR", location: "B11 Track 1 RRM", description: "Fundamental Base PE set to ROCE base 26.1x (->18.3x), not quality-adjusted 20.9x (->14.6x). Disclosed and reasoned (avoids double-penalising cash), but the alternate reading would push divergence 12.4%->~30% and force the conservative track to govern entry per L394. Moot: Override 1 anchors additive Track 2 as governing; destination PE and WATCHLIST unchanged."}
  - {severity: "MINOR", location: "B11 Hurdle Ratio", description: "Authoritative HR written as (1+g)^4 x (trailing 28.13x); value 2.12 is identical to the internally-consistent forward-forward HR (entry FY27 forward PE 21.63x, exit FY30 forward). Substance correct (NOT the SFL inconsistency); should display forward entry PE for transparency. HR base 2.12>=1.953 is a technical PASS; CONDITIONAL is a conservative overlay with no decision impact."}
  - {severity: "MINOR", location: "B11 Section 4H", description: "L809 (Gate0 AVERAGE->AVOID) vs L915 (Gate0<60->WATCHLIST) tension resolved correctly to WATCHLIST via L915 with all other AVOID sub-triggers confirmed not firing (U/D 6.9x>=2x, Hurdle CONDITIONAL not STOP, promoter CAUTION not CONCERN), but the conflict is not surfaced as an explicit cite. Correct outcome; transparency note."}
  - {severity: "MINOR", location: "reports/ (B14 absent)", description: "Role 2 thesis report B14.md not on disk at audit time; decision logic audited as carried in B11 Section 4. B14 must reproduce WATCHLIST / Small(2-3%) / entry Rs145-165 / MoS Rs132; fresh Verifier C pass required if it diverges."}
critical_count: 0
major_count: 0
minor_count: 5
acceptance_rate: 100   # 48/48 rules passed on independent recomputation; 5 MINOR are imprecision/presentation/pending-report, no rule FAIL
recomputed_destination_pe: ""   # blank: reproduces (Track 2 governing 20.9x; Track 1 RRM 18.3x)
recomputed_decision: ""         # blank: reproduces (WATCHLIST, Small 2-3%)
concur_or_dissent: "CONCUR"
```
