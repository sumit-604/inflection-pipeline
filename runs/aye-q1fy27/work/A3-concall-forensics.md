# A3 FORENSIC NOTES — AYE Finance, Q1 FY27 — DOCTYPE: concall

Source A1 extract: `runs/aye-q1fy27/work/A1-concall-extract.md` (gate_a1: pass)
Source A2 ledger: `runs/aye-q1fy27/work/A2-concall-ledger.md` (gate_a2: pass)
Citation unit: A1 embedded TRANSCRIPT line number (1–130), per A2 convention.
Ledger reconciliation: 100% — every A2 row (Tables 1–6, all cited lines) read
verbatim at its A1 line before judging. No prior-quarter A1 extract available
(this concall was digest-only in the 2026-07-22 workup); F5/F15 verbatim diffs
therefore cannot be run and are marked N.A. on that basis, not skipped.

Doctype applicability (per protocol): on a concall F6/F7/F17 apply; most
balance-sheet / auditor checks (F2, F3, F4, F5, F8, F10, F11, F12, F13, F14,
F15) are N.A.; F16 is presentation-only. Every check is nonetheless marked.

---

## FINDINGS TABLE

| id | check | ledger row ref | line | verbatim quote (short) | classification | forward implication |
|---|---|---|---|---|---|---|
| F1.1 | F1 | T5 line 20 / T2 turn 11 `ZERO_STANDING` | 20 | "we did not... undertake any DA... Last quarter uh DA had contributed to around 20 kores" | FORWARD-SIGNAL | DA gain-on-derecognition ~nil this quarter => tripwire #2 (net gain on derecognition as % of income) is GREEN this quarter; but DA is a discretionary lever mgmt targets at 5–7% of AUM (line 55) and can re-pull, re-introducing PAT-on-DA reliance any quarter. |
| F1.2 | F1 | T5 line 95, T6 line 117 `ZERO_STANDING` | 95, 117 | "we haven't reported slippage number I have not have that number readily available" | AMBIGUOUS | Slippage is the direct feed to credit-cost and PAR trajectory; non-disclosure blocks independent verification of the "structural improvement" claim. A4 question. Touches asset-quality tripwires #1/#5. |
| F6.1 | F6 | T5 line 39, 50; T6 line 50 | 39, 50, 51 | "management overlay created of roughly around 6 crores in this credit... cost for this quarter"; "we... want to create about 5% of the book as overlay" | AMBIGUOUS | Reported credit cost 4.01% (line 8) INCLUDES a ~6cr overlay build (~33bps on ~7,324cr book) => underlying credit cost ~3.7%. Overlay is a stated earnings-smoothing / provisioning-discretion mechanism ("absorb some of the profits... in good years"). Directly qualifies tripwire #5 (credit cost within 3.5–4.0%): the 4.01% print is management-managed, not purely incurred. A4 question. |
| F6.2 | F6 | T5 line 40; T6 line 40 | 40 | "gold loan and... similar... products... is what we will look at. We are in the process of doing a market survey" | FORWARD-SIGNAL | New-product entry (gold, solar) inside 3-yr window; "in the process of" = F6 status word. Sourced from the ~55,000 customers/qtr Aye DECLINES (line 40), of whom "20% plus" take gold loans. Growth-composition optionality; feeds FTTCP catalyst timeline. |
| F6.3 | F6 | T6 line 8, 14 | 8, 14 | "by the end of quarter two we'll be able to narrow down our... guidance to more refined numbers" | FORWARD-SIGNAL | Dated management commitment: refined FY27 guidance at H1/Q2 results. Schedule a Role 5 promise-vs-delivery check on the Q2 call. |
| F6.4 | F6 | T5 line 31; T6 line 31 | 31 | "eventually increasing to about 30%. We can safely assume about a 50 bits lower levels on the... credit cost" | FORWARD-SIGNAL | Mortgage-mix shift is the stated structural lever to pull cross-cycle credit cost to 3–3.25%. Explicitly "not in this financial year" — no FY27 benefit; medium-term only. Tempers tripwire #4/#5 forward optimism. |
| F6.5 | F6 | T5 line 8, 37, 61; T6 line 8, 61 | 8, 61 | "reduce our borrowing cost by approximately 20 to 25 basis points on the incremental borrowings over the course of the year" | FORWARD-SIGNAL | Rating upgrade (IND A->A+, A1->A1+) benefit "not yet factored" (line 61) => forward NIM/spread tailwind still to land; supports the NIM-guidance-conservatism read (F7.2). |
| F7.1 | F7 | T6 line 95, 117 | 95, 117 | "we can share uh that eventually"; "we haven't mentioned the slippages number" | AMBIGUOUS | Deferral pattern on a hard number asked twice by different analysts = pre-emptive non-answer. Conservative read: the metric is not one management wants standing in the record this quarter. A4 question. |
| F7.2 | F7 | T5 line 36, 116; T6 line 116 | 36, 116, 117 | NIM guidance "still remain around... 14.25 to 14.75 despite this decline"; "there's an upside there" | AMBIGUOUS | NIM printed 15.9% (line 8) — ~115bps above the top of the 14.25–14.75% guidance band — yet guidance was NOT raised, with an explicit unpriced upside conceded (line 117). Sandbag/hedge: either guidance is stale or a NIM step-down is expected later in FY27 (mix shift to mortgage). A4 question. |
| F7.3 | F7 | T6 line 75, 80 | 75, 80 | "a good guess would be between about 15% to 20%"; "we don't have that data up front... my guess would be" | NEUTRAL-FACT | Two explicit data-absence hedges on cross-holding/QR questions; no forward-P&L implication, but confirms Aye does not systematically track borrower external leverage — relevant to tripwire #8 (over-lending) as an evidence gap. |
| F9.1 | F9 | T5 line 20, 22; T6 line 22 | 22 | "From this quarter onwards we've moved the foreign exchange movements into OCI and therefore we will not going forward see any fresh movements... on this line" | FORWARD-SIGNAL | Accounting-presentation change: forex volatility reclassified P&L -> OCI. Removes the ~12cr prior-quarter forex P&L benefit (line 20) from future P&L permanently and routes future forex swings below the line. Combined with DA-nil, ~32–35cr of prior-period other income does not recur in P&L => other-income quality/step-down signal. Verify assumption/scope at the Annual Report. |
| F17.1 | F17 | tripwire #6 (PCR) | 8, 95 | (no PCR / provision-coverage figure appears anywhere, lines 1–130) | CONFIRMATORY-NEGATIVE | PCR never stated despite a full asset-quality block (line 8) and product-level PAR bifurcation (line 95). Silence on coverage while GNPA/PAR are foregrounded. Tripwire #6 unverifiable from this call. |
| F17.2 | F17 | tripwire #7 (covenants) | 8, 87–88 | (14 unwaived covenant instances / 23.6% of borrowings never mentioned, lines 1–130) | CONFIRMATORY-NEGATIVE | Covenant-breach resolution absent from management remarks and unraised by any analyst, even in the leverage/capital-runway thread (lines 87–88, 123). Sustained silence on a live governance item. |
| F17.3 | F17 | tripwire #8 (over-lending) | 27, 40 | approval "55% has shrunk down to 45%"; declined "close to 55,000 customers" | CONFIRMATORY-NEGATIVE | Approval tightening disclosed (line 27) but AUM-per-borrower and repeat-loan share NOT disclosed; over-lending cannot be tested. Adding 44,000 while declining 55,000 with 20%+ of declines going to gold lenders (line 40) keeps the over-lending question open. |
| F17.4 | F17 | tripwire #1/#5 (slippage) | 95, 117 | asked twice, "haven't reported slippage number" | CONFIRMATORY-NEGATIVE | Slippage silence recorded twice in one call (lines 95, 117) — first quarter of tracked silence on this metric in this pipeline. |
| F17.5 | F17 | tripwire #4 (FY27 PAT) | 8, 39 | no FY27 PAT / EPS figure given; Q1 PAT "75 crores" (line 8) | AMBIGUOUS | No explicit FY27 PAT guidance offered; only AUM (25–30%) and ratio guidance. Q1 PAT 75cr annualizes to ~300cr in line with thesis, but management did not commit to it. A4 question. |

---

## CHECKLIST SCORECARD (all 17, one status each)

| Check | Status | One-line basis |
|---|---|---|
| F1 ZERO-VALUE STANDING | **FINDING** | Two `ZERO_STANDING` disclosures: DA nil this qtr (line 20, was ~20cr) and slippage not reported twice (lines 95, 117). See F1.1, F1.2. |
| F2 STANDALONE vs CONSOLIDATED | **N.A.** | Concall; no S-vs-C financial statements presented. AYE is a single-entity NBFC in this transcript — no JV/associate/subsidiary split disclosed. |
| F3 SHELL-ENTITY DETECTION | **N.A.** | Concall; no entity-level cost lines (materials/employee/depreciation) to compare. |
| F4 UNAUDITED CONTRIBUTION RATIO | **N.A.** | Concall; no auditor's Other Matters / component-auditor disclosure present. |
| F5 GOING CONCERN / EoM SCOPE | **N.A.** | Concall; no auditor EoM paragraph. Also no prior-quarter A1 extract available for a verbatim diff. |
| F6 FORWARD-COMMITMENT MINING | **FINDING** | 17 dateable management commitments extracted (see Commitment Register); overlay-to-5%, gold-loan entry, Q2 guidance-refinement, mortgage-mix, rating-COB benefit flagged. F6.1–F6.5. |
| F7 HEDGE PHRASE MINING | **FINDING** | Slippage deferral ("share eventually"), NIM-guidance-held-despite-beat, data-absence "guesses," "endeavour." F7.1–F7.3. |
| F8 TAX FORENSICS | **N.A.** | Concall; no ETR, deferred-tax, or prior-year tax-adjustment figures disclosed. Only post-tax PAT 75cr (line 8) given. |
| F9 OCI FORENSICS | **FINDING** | Forex movements reclassified P&L -> OCI from this quarter (line 22); removes ~12cr prior P&L item and future forex volatility from P&L. F9.1. |
| F10 SHARE COUNT / DILUTION | **N.A.** | Concall; no paid-up capital / basic-vs-diluted EPS disclosed. Feb-2026 IPO referenced (lines 20, 39, 122) as capital-injection context only — no share count. |
| F11 RESERVES / NET WORTH TIE-OUT | **N.A.** | Concall; no Other Equity / net-worth line. CAR 41.3% (line 8) and leverage 3.15x (line 88) given but no reconcilable net-worth number vs a third-party figure. |
| F12 SEGMENT FORENSICS | **N.A.** | Concall; product-level PAR/ROI given (lines 17, 95) but no segment ASSET/LIABILITY balances to trend. |
| F13 BOARD OUTCOME | **N.A.** | Concall; no AR/AGM/board-resolution/director-appointment disclosure. (Rating upgrade is an agency action, not a board outcome.) |
| F14 NOTE DRAFTING INCONSISTENCIES | **N.A.** | Concall; no notes/auditor letter to cross-check. Six A2 `NUMBER_VARIANT` items (borrowers 6.7 vs 67 lakh; AUM 7,324 vs 7,384; leverage 3.1 vs 3.15; fee 35 vs 32–33cr; 48k/44k; PAR90 5 vs 5.35%) reviewed and judged transcription noise per task instruction — no check turns on the exact figure, none escalated. |
| F15 ENTITY LIST DIFFS | **N.A.** | Concall; no consolidation list. No prior-quarter A1 extract for a diff. |
| F16 PRESENTATION-SPECIFIC | **N.A.** | Doctype is concall, not the investor presentation. (Deck-carried metrics — PPT foreclosure 5%, line 89/91 — referenced but the deck itself is not this artifact.) |
| F17 SILENCE AUDIT | **FINDING** | Four monitoring-checklist items unaddressed (PCR #6, covenants #7, over-lending #8, FY27 PAT #4) plus slippage silence. See "What Was NOT Discussed." F17.1–F17.5. |

Status tally: 5 FINDING, 12 N.A., 0 PASS, 0 blank.

---

## COMMITMENT REGISTER (from F6; feeds Role 5 promise-vs-delivery + FTTCP timeline)

| # | Commitment | Implied date | Ref (line) | Status word |
|---|---|---|---|---|
| 1 | Narrow / refine FY27 guidance to tighter ranges | End Q2 / H1 FY27 | 8, 14 | initiated |
| 2 | AUM growth 25–30% FY27 | FY27 | 8 | reaffirmed |
| 3 | Credit-cost normalization toward 3.5–4% | Through FY27 | 8 | underway |
| 4 | Add 40–50 branches (~10%/yr), visible Q2–Q3 | FY27, Q2–Q3 | 8, 53, 119 | underway |
| 5 | Gradually raise mortgage share (to 30–35% eventually) | FY27 gradual / 3-yr | 8, 29, 31 | underway |
| 6 | Rating upgrade -> 20–25bps (then +10–15bps) COB cut on incremental | Over FY27 | 8, 61 | initiated |
| 7 | Forex movements moved P&L -> OCI | This quarter (done) | 22 | completed |
| 8 | NIM to "remain flat... not come down" | FY27 | 29 | reaffirmed |
| 9 | Build overlay to ~5% of book; absorb profits in good years | "eventually" | 39, 50, 51 | underway (11cr on BS; ~6cr built this qtr) |
| 10 | Enter gold / solar loans; market survey running | Within 3 yrs | 40 | initiated ("in the process of") |
| 11 | Limit DA to 5–7% of AUM | Long-term | 55 | ongoing |
| 12 | PAR X moderate to 6–6.5% | Q3/Q4 FY27 | 115 | soft-dated |
| 13 | PAR 90 (mortgage) improve via settlements/write-offs | Later in FY27 | 96, 115 | soft-dated |
| 14 | OPEX into 8.25–8.75% band (7–7.5% over 3 yrs) | Q3/Q4 FY27; 3-yr | 118, 119, 122 | soft-dated |
| 15 | Raise capital at 4–4.5x leverage (~2–2.5 yr runway) | ~FY29 | 88, 123 | future |
| 16 | Team growth ~10–15% to support 25–30% AUM growth | FY27 (Q2–Q4) | 68, 119 | underway |
| 17 | Share slippage number "eventually" | undated | 95 | deferred — NOT delivered (see F17.4) |

Milestone note: no prior-quarter A1 extract, so no "initiated -> underway -> completed"
cross-quarter transitions can be confirmed this run. Commitment #1 (guidance
refinement at Q2) and #17 (slippage disclosure) are the two hardest promise-vs-delivery
tests to re-check on the Q2 FY27 call.

---

## WHAT WAS NOT DISCUSSED (F17 silence audit vs F6 commitments + Notion tripwires)

| Item | Maps to tripwire | Consecutive qtrs silent (this pipeline) | Basis / locus |
|---|---|---|---|
| Provision Coverage Ratio (PCR) | #6 (PCR >=60%) | 1 (first tracked) | Absent lines 1–130; asset-quality block (line 8) and PAR bifurcation (line 95) give GNPA/PAR but no coverage. |
| Covenant-breach resolution (14 unwaived, 23.6% of borrowings) | #7 | 1 (first tracked) | Absent lines 1–130; unraised even in leverage/funding threads (lines 87–88, 123, 55). |
| Over-lending metric: AUM per borrower / repeat-loan share | #8 | 1 (first tracked) | Approval tightening 55%->45% disclosed (line 27) but exposure-per-borrower / repeat share never given; mgmt admits no systematic external-leverage tracking (lines 75, 80). |
| Slippage number (asked twice) | #1/#5 | 1 (first tracked) | Deferred lines 95, 117. |
| Explicit FY27 PAT / EPS guidance (~Rs 300cr / EPS ~11.90) | #4 | 1 (first tracked) | Not given; only AUM + ratio guidance (line 8). Q1 PAT 75cr (line 8) annualizes in-thesis but uncommitted. |

Per Role 5: sustained silence on a deteriorating metric is a confirmatory negative.
None of these are yet "sustained" (no prior full-transcript baseline in-pipeline), but
all five are seeded here for the Q2 FY27 re-check. PCR (#6) and covenants (#7) are the
highest-priority silences because both are hard tripwires the operator set and neither
was volunteered nor asked.

---

## TRIPWIRE MAP (forensic findings -> Notion monitoring checklist)

- #1 GNPA <=4.49%: GNPA 4.49% reported (line 8) — at the line, not below; PAR X 7.01% up from ~6.9% (line 115), mgmt attributes to seasonal denominator effect. Watch — not breached.
- #2 net gain on derecognition % income: DA nil this qtr (F1.1) => ~0% => GREEN, but discretionary lever (5–7% target).
- #3 AUM growth >=25%: 28% YoY (line 8) — GREEN.
- #4 FY27 PAT ~300cr: uncommitted (F17.5); Q1 run-rate ~in-line.
- #5 credit cost 3.5–4.0%: 4.01% printed but INCLUDES ~6cr overlay build (F6.1); underlying ~3.7%. Top-of-band, management-managed.
- #6 PCR >=60%: NOT DISCLOSED (F17.1) — unverifiable.
- #7 covenants: NOT DISCUSSED (F17.2).
- #8 over-lending: NOT MEASURABLE from call (F17.3, F7.3).
- SHARED CATALYST (asset-quality normalization): F6.1 (overlay-managed credit cost), F1.2/F17.4 (slippage silence) and F17.1 (PCR silence) all reduce the independent verifiability of the single-point-of-failure normalization thesis — the strongest forensic theme of this call.

---

```yaml
stage: A3-forensics
company: "AYE"
quarter: "Q1 FY27"
doctype: "concall"
model: claude-opus-4-8
status: complete
forensics_path: "runs/aye-q1fy27/work/A3-concall-forensics.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: N.A.
  F9: FINDING
  F10: N.A.
  F11: N.A.
  F12: N.A.
  F13: N.A.
  F14: N.A.
  F15: N.A.
  F16: N.A.
  F17: FINDING
findings:
  - {id: "F1.1", check: "F1", line: "20", classification: "FORWARD-SIGNAL", implication: "DA nil this qtr => gain-on-derecognition ~0% (tripwire #2 green) but 5-7% AUM lever can re-pull PAT reliance"}
  - {id: "F1.2", check: "F1", line: "95,117", classification: "AMBIGUOUS", implication: "slippage not reported twice; blocks verification of structural credit-cost improvement"}
  - {id: "F6.1", check: "F6", line: "39,50,51", classification: "AMBIGUOUS", implication: "reported 4.01% credit cost includes ~6cr overlay build (~33bps); provisioning-discretion / earnings-smoothing to 5% of book target => tripwire #5 print is management-managed"}
  - {id: "F6.2", check: "F6", line: "40", classification: "FORWARD-SIGNAL", implication: "gold/solar loan entry, market survey in process; growth-composition optionality"}
  - {id: "F6.3", check: "F6", line: "8,14", classification: "FORWARD-SIGNAL", implication: "commits to refined FY27 guidance at Q2/H1 - Role 5 re-check point"}
  - {id: "F6.4", check: "F6", line: "31", classification: "FORWARD-SIGNAL", implication: "mortgage-mix credit-cost -50bps lever is medium-term, explicitly no FY27 benefit"}
  - {id: "F6.5", check: "F6", line: "8,61", classification: "FORWARD-SIGNAL", implication: "rating-upgrade COB benefit not yet factored => forward spread/NIM tailwind"}
  - {id: "F7.1", check: "F7", line: "95,117", classification: "AMBIGUOUS", implication: "twice-deferred slippage = pre-emptive non-answer pattern"}
  - {id: "F7.2", check: "F7", line: "36,116,117", classification: "AMBIGUOUS", implication: "NIM 15.9% vs 14.25-14.75% guidance not raised, upside conceded but unpriced => stale guidance or expected step-down"}
  - {id: "F7.3", check: "F7", line: "75,80", classification: "NEUTRAL-FACT", implication: "explicit data-absence on borrower external leverage - evidence gap for tripwire #8"}
  - {id: "F9.1", check: "F9", line: "22", classification: "FORWARD-SIGNAL", implication: "forex reclassified P&L->OCI; removes ~12cr prior P&L item + future forex from P&L => other-income step-down"}
  - {id: "F17.1", check: "F17", line: "8,95", classification: "CONFIRMATORY-NEGATIVE", implication: "PCR never disclosed - tripwire #6 unverifiable"}
  - {id: "F17.2", check: "F17", line: "8,87", classification: "CONFIRMATORY-NEGATIVE", implication: "covenant-breach resolution unaddressed - tripwire #7"}
  - {id: "F17.3", check: "F17", line: "27,40", classification: "CONFIRMATORY-NEGATIVE", implication: "over-lending metric not measurable from call - tripwire #8"}
  - {id: "F17.4", check: "F17", line: "95,117", classification: "CONFIRMATORY-NEGATIVE", implication: "slippage silence recorded twice - first tracked quarter"}
  - {id: "F17.5", check: "F17", line: "8,39", classification: "AMBIGUOUS", implication: "no explicit FY27 PAT guidance - tripwire #4 uncommitted"}
forward_signals: ["F1.1", "F6.2", "F6.3", "F6.4", "F6.5", "F9.1"]
ambiguous: ["F1.2", "F6.1", "F7.1", "F7.2", "F17.5"]
commitments:
  - {commitment: "Refine/narrow FY27 guidance", implied_date: "Q2/H1 FY27", ref: "8,14", status_word: "initiated"}
  - {commitment: "AUM growth 25-30% FY27", implied_date: "FY27", ref: "8", status_word: "reaffirmed"}
  - {commitment: "Credit-cost normalization to 3.5-4%", implied_date: "through FY27", ref: "8", status_word: "underway"}
  - {commitment: "Add 40-50 branches (~10%/yr)", implied_date: "FY27 Q2-Q3", ref: "8,53,119", status_word: "underway"}
  - {commitment: "Raise mortgage share to 30-35%", implied_date: "gradual/3-yr", ref: "8,29,31", status_word: "underway"}
  - {commitment: "Rating upgrade -> 20-25bps COB cut", implied_date: "over FY27", ref: "8,61", status_word: "initiated"}
  - {commitment: "Forex moved P&L->OCI", implied_date: "this quarter", ref: "22", status_word: "completed"}
  - {commitment: "NIM to remain flat, not fall", implied_date: "FY27", ref: "29", status_word: "reaffirmed"}
  - {commitment: "Build overlay to ~5% of book", implied_date: "eventually", ref: "39,50,51", status_word: "underway"}
  - {commitment: "Enter gold/solar loans; market survey", implied_date: "within 3 yrs", ref: "40", status_word: "initiated"}
  - {commitment: "Limit DA to 5-7% of AUM", implied_date: "long-term", ref: "55", status_word: "ongoing"}
  - {commitment: "PAR X moderate to 6-6.5%", implied_date: "Q3/Q4 FY27", ref: "115", status_word: "soft-dated"}
  - {commitment: "Mortgage PAR 90 improve via settlements/write-offs", implied_date: "later FY27", ref: "96,115", status_word: "soft-dated"}
  - {commitment: "OPEX into 8.25-8.75% band; 7-7.5% in 3 yrs", implied_date: "Q3/Q4 FY27; 3-yr", ref: "118,119,122", status_word: "soft-dated"}
  - {commitment: "Raise capital at 4-4.5x leverage", implied_date: "~FY29", ref: "88,123", status_word: "future"}
  - {commitment: "Team growth ~10-15%", implied_date: "FY27 Q2-Q4", ref: "68,119", status_word: "underway"}
  - {commitment: "Share slippage number eventually", implied_date: "undated", ref: "95", status_word: "deferred"}
gate_a3: pass
blank_checks: []
```
