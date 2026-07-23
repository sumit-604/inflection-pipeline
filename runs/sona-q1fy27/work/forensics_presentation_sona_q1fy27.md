# A3 FORENSIC NOTES — Sona BLW Precision Forgings (SONACOMS), Q1 FY27 — DOCTYPE: PRESENTATION

Source extract: `extract_presentation_sona_q1fy27.txt` (1180 lines, 41 slides).
Ledger reconciled: `ledger_presentation_sona_q1fy27.md` (Sections A-K read in full;
365 numeric rows + 8 guidance + 14 order-book + 39 entities + 27 footnotes all read at
their cited lines). **ledger_reconciled_pct: 100.**

Prior-quarter extract: **NONE** (first pipeline run; `PRIOR_LEDGER_UNAVAILABLE`). Every
quarter-over-quarter check that requires a verbatim prior-period diff (F5 EoM, F15 entity
list, and the "dropped disclosure" half of F16) therefore cannot be executed as a diff this
run; this ledger is the baseline for next quarter. Absence noted explicitly per instruction.

Doctype rule applied: on a presentation F16 applies plus any F6/F10/F11 numbers the deck
carries; checks keyed to auditor paragraphs / Board Outcome / statutory notes are N.A. Per
the launching message, F17 is run as a **silence/movement audit of the deck against the live
Notion monitoring checklist** (not skipped as concall-only).

---

## FINDINGS TABLE

| id | check | ledger row ref | slide / line | verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-F6-01 | F6 | Sec C #4-7; Sec D | s18 L450; s20 L486 | "₹6,400 mn addition in our orderbook / H2 FY29 … ₹900 mn … H2 FY26 … ₹2,100 mn … H2 FY28 … ₹400 mn … H1 FY28" | FORWARD-SIGNAL | Four dated Start-of-Production commitments create a promise-vs-delivery tracker; H2 FY26 (₹900mn E2W) is the near-term test, deliverable this fiscal half. |
| A3-F6-02 | F6 | Sec B L318-319 | s11 L318-319 | "Showcased the prototype of our first AMR platform during CES 2026; In-house development of full AMR is ongoing" | FORWARD-SIGNAL | Status word "ongoing" (=underway); watch for "completed"/first AMR sale next quarter as the Robotics vertical milestone. |
| A3-F6-03 | F6 | Sec C #2 | s6 L160 | "We aspire to replicate the same 10x growth in the next decade" | AMBIGUOUS | Undated, no numeric decade target; an aspiration presented adjacent to a realized figure — A4 to ask for the quantified medium-term revenue/EPS bridge behind it. |
| A3-F7-01 | F7 | Sec H (s21 n1); Sec C #8 | s21 L525-527 | "We have also applied a discount to accommodate any unforeseen delays or changes in program launches that may happen in the future." | AMBIGUOUS | The headline ₹240bn net order book is risk-adjusted by an **undisclosed** discount + undisclosed EOL/phase-out haircut; the gross (un-discounted) book and the discount rate are not given — A4 question. |
| A3-F16-01 | F16 | Sec H (s37 n2); Sec F | s37 L1010,1014 | Indian share "PV 55-60% / CV 80-90% / Tractors 75-85%" … "As per CRISIL report dated Feb 2021" | CONFIRMATORY-NEGATIVE | The dominant-share claim rests on a 4.5-year-old (Feb-2021) source; stale-source `STALE_SOURCE_DATA` confirmed at line 1014 — do not treat as current market position. |
| A3-F16-02 | F16 | Sec B L871-895; Sec C note | s33 L871-895 | "23% Growth 5-year Revenue CAGR … 26% … 20% … For a 5-year period of FY22 to FY26" | AMBIGUOUS | Section header "Guided by Values" places **historical FY22-FY26 trailing** metrics where a reader expects forward targets; `POTENTIAL_MISREAD_AS_GUIDANCE` confirmed — flagged so A4 does NOT recharacterise 23%/26%/20% as guidance. |
| A3-F16-03 | F16 | Sec B L934-937,950 | s35 L934-937 | "44% … 17,420 Q1FY27 (Ann.) … 4,355 Q1FY27" | AMBIGUOUS | Headline "44% BEV share" (s14 L383, s17 L415) is the **annualised** figure (BEV rev annualised 17,420 = 4,355×4); the "Ann." qualifier appears only on s35, not on the headline slides. A4 to confirm quarterly vs annualised framing. |
| A3-F16-04 | F16 | Sec H (s27 n1) | s27 L701 | "Revenue includes net gain from foreign exchange" | AMBIGUOUS | Reported revenue (13,104 mn, +54% YoY) is inflated by an undisclosed forex gain — quality-of-revenue caveat; magnitude not given, A4 question. |
| A3-F17-01 | F17 | Sec E capex note | deck-wide (grep=0) | (no "capex"/"capital expenditure" token anywhere in 41 slides) | FORWARD-SIGNAL | `CAPEX_NOT_DISCLOSED`: zero capex figure despite 4 forward SOP commitments implying capacity build; against thesis baseline (FY26 capex ~37% of revenue, negative FCF) this silence is material — tripwire 4 (CFO/PAT) cannot be checked from the deck. |
| A3-F17-02 | F17 | Sec E; Sec B L709-710,729,735 | s28 L709-710 | "RoCE 18.4% 15.4% 15.8% … RoE 17.7% 13.2% 13.3%" | FORWARD-SIGNAL | ROCE Mar-25→Mar-26→Jun-26 = 18.4%→15.4%→15.8% (down ~260bps YoY, +40bps QoQ), still >14% so tripwire 1 not tripped but trending toward it. Reported ROCE is **normalised** (Railway EBIT annualised, L735) and denominator **includes** NOVELIC/Railway acquisition capital (L729) — two offsetting adjustments; A4 to obtain un-normalised ROCE. |
| A3-F17-03 | F17 | Sec E L682,684,690-691 | s27 L682,690 | "23.8% 23.1% … EBITDA margin was lower by ~0.7% … PAT margin was lower by ~0.7%" | CONFIRMATORY-NEGATIVE | EBITDA margin 23.1% (Q1FY27) vs 23.8% (Q1FY26) and vs FY26 baseline 24.7% = continued compression; corroborates tripwire 6 (margin compression). Cause given: "product mix and higher input prices." |
| A3-F17-04 | F17 | Sec F customer rows | s18 L448; s20 L483-484 | "North American OEM of PVs and EVs … New Age Indian OEM of Electric 2-Wheelers … North American and Indian Customers" | AMBIGUOUS | 3 undisclosed customer names; the same NA OEM anchors two of Q1's wins (s18 ₹6,400mn + s20 ₹2,100mn) — customer-concentration signal (tripwire 9, BEV/anchor). A4 to probe single-customer dependence in the order book. |
| A3-F17-05 | F17 | Notion checklist vs deck | deck-wide silence | (no mention of: Novelic KAM impairment; corporate guarantee; receivable/WC days; CFO; forced block sale/control) | CONFIRMATORY-NEGATIVE | Deck is silent on tripwires 2,3,5,7 and CFO conversion (tripwire 4). First-quarter of tracking, so consecutive-silence count = 1; sustained silence on these would become a confirmatory negative per Role 5. |
| A3-F17-06 | F17 | Sec B L547-577 | s23 L547-577 | "By Geography … 17% … 51% … 49% … By Market segment … PV 49% … 51%" | AMBIGUOUS | India-mix tripwire (10; FY26 51%): the s23 geography donut value-to-region mapping is **not recoverable** from the linearised text (A2 did not flag s23 ambiguous, but it collapses like s6/s23); only "PV 49%→51%" reads cleanly. A4/source-PDF must confirm the India geography share movement. |

---

## CHECKLIST SCORECARD (all 17; one status each — GATE A3)

| Check | Status | Basis (one line) |
|---|---|---|
| F1 ZERO-VALUE STANDING ITEMS | **N.A.** | No `ZERO_STANDING` rows; a presentation carries no full chart-of-accounts (ledger Sec I, `zero_standing: 0`, L709). |
| F2 STANDALONE vs CONSOLIDATED | **N.A.** | Deck shows only consolidated headline financials; no standalone split disclosed (cover letter L33 references both but figures are consolidated-only). |
| F3 SHELL-ENTITY DETECTION | **N.A.** | No entity-level cost lines (materials/employee/depreciation) in a presentation. |
| F4 UNAUDITED CONTRIBUTION RATIO | **N.A.** | No auditor "Other Matters" paragraph in a presentation. |
| F5 GOING CONCERN / EoM SCOPE | **N.A.** | No auditor EoM/Going Concern in a presentation; no prior-quarter deck to diff (`PRIOR_LEDGER_UNAVAILABLE`). |
| F6 FORWARD-COMMITMENT MINING | **FINDING** | 8 forward statements incl 4 dated SOP commitments + AMR "ongoing" + 10x-decade aspiration (A3-F6-01/02/03). |
| F7 HEDGE PHRASE MINING | **FINDING** | Headline order book embeds undisclosed delay-risk discount + EOL haircut (A3-F7-01, s21 L525-527). |
| F8 TAX FORENSICS | **N.A.** | No ETR / deferred-tax disclosure; the ₹301mn labour-code item (L731) is a PAT normalisation for ROE, not a tax line. |
| F9 OCI FORENSICS | **N.A.** | No OCI / actuarial disclosure in a presentation. |
| F10 SHARE COUNT / DILUTION | **N.A.** | No paid-up capital / share count / basic-vs-diluted EPS in the deck (PAT is stated incl. non-controlling interest, L390/702 — minority interest exists but no share data). |
| F11 RESERVES / NET WORTH TIE-OUT | **N.A.** | No absolute net worth or reserves figure disclosed (ROE uses "tangible net worth" as a ratio denominator only, L730). |
| F12 SEGMENT FORENSICS | **N.A.** | No segment assets/liabilities disclosed; deck gives segment order-book and revenue mix only (no balance-sheet-by-segment). |
| F13 BOARD OUTCOME | **N.A.** | No Board's Report / AGM notice / director-appointment term dates in a presentation. |
| F14 NOTE DRAFTING INCONSISTENCIES | **N.A.** | No auditor letter / statutory notes to cross-check; deck footnotes (BEV-scope def repeated s14/17/35, ROCE/ROE defs) are internally consistent and dual-brand naming (Sona BLW legal / Sona Comstar brand) is deliberate. |
| F15 ENTITY LIST DIFFS | **N.A.** | No consolidation entity list in the deck; no prior quarter to diff (`PRIOR_LEDGER_UNAVAILABLE`). |
| F16 DROPPED / REFRAMED DISCLOSURES | **FINDING** | Stale CRISIL-2021 source, "Guided by Values" historical-as-forward framing, annualised 44% BEV headline, forex-gain-in-revenue caveat (A3-F16-01..04). Dropped-disclosure half not executable (no prior deck). |
| F17 SILENCE AUDIT (deck vs Notion) | **FINDING** | Capex silence + ROCE/margin movement + customer concentration + silence on tripwires 2/3/5/7 (A3-F17-01..06). |

**GATE A3: PASS — 17/17 marked, 0 blank.** (13 N.A. with reason, 4 FINDING; N.A. count is expected for a presentation doctype.)

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | slide / line ref | status word |
|---|---|---|---|
| Diff Assembly, Hybrid PV (NA OEM), ₹6,400 mn order-book add | H2 FY29 (SOP) | s18 L450 | awarded / SOP pending |
| Hub-Wheel Traction Motor, E2W (new Indian OEM), ₹900 mn add | H2 FY26 (SOP) | s18 L450 | awarded / SOP pending (near-term) |
| Diff Gears, Non-Electric PV (NA OEM), ₹2,100 mn add | H2 FY28 (SOP) | s20 L486 | awarded / SOP pending |
| Diff Gears, Non-Electric CV/OHV (NA+Indian), ₹400 mn add | H1 FY28 (SOP) | s20 L486 | awarded / SOP pending |
| Full AMR (Robotics vertical) in-house development | undated ("ongoing") | s11 L318-319 | underway / ongoing |
| Robotics & Physical AI vertical to cover "entire value chain" | undated | s11 L299 | intent ("will focus") |
| Railway order book to be executed | within next 12 months | s21 L528 | committed (PO-backed) |
| "10x growth in the next decade" | ~decade (undated) | s6 L160 | aspiration |

---

## THESIS-RELEVANT NUMBERS EXTRACTED (verbatim, for A4 vs FY26 baseline)

- **Revenue** Q1FY27 13,104 mn (Rs 1,310.4 Cr), +54% YoY; Q1FY26 8,509 mn (s14 L375, s27 L675,678). Includes net forex gain (L701).
- **EBITDA** 3,026 mn (Rs 302.6 Cr), +49% YoY; **margin 23.1%** vs 23.8% Q1FY26 vs FY26 baseline 24.7% (s27 L676,682).
- **PAT** 1,805 mn (Rs 180.5 Cr, incl. NCI), +45% YoY; **PAT margin 13.6%** vs 14.3% (s14 L378, s27 L677,684).
- **BEV revenue** 4,355 mn (Rs 435.5 Cr), +107% YoY; **44% of automotive product revenue** (annualised on s35) (s14 L383, s27 L683,693).
- **Net order book** ₹240 bn (Rs 24,000 Cr) = 5.4x FY26 revenue vs FY26 baseline Rs 23,700 Cr; bridge 237 + 18 − 15 = 240 (s21 L495,498,500). Segment mix: Auto-EV ₹154bn (64%), Auto Non-EV ₹66bn (28%), Robotics ₹12bn (5%), Railway ₹8bn (3%) — split `CHART_LABEL_AMBIGUOUS`, sum reconciles (L513).
- **ROCE** Mar-25 18.4% → Mar-26 15.4% → Jun-26 15.8% (vs FY26 baseline ~16%); normalised (Railway EBIT annualised) and denominator includes NOVELIC/Railway capital (s28 L709,729,735).
- **RoE** Mar-25 17.7% → Mar-26 13.2% → Jun-26 13.3%; LTM PAT adjusted for ₹301mn labour-code one-off (s28 L710,731).
- **Net Debt/EBITDA** (2.73) → (0.93) → (1.06) i.e. net cash all three periods (s28 L721-722).
- **WCTR / FATR** tokens 5.0/4.6/3.8 and 3.4/2.9/3.2 — column-to-period split `CHART_LABEL_AMBIGUOUS` (s28 L719-720); receivable/WC-days tripwire 7 not directly computable from deck.
- **Geography / market mix** (s23): only "PV 49%(FY26)→51%(Q1FY27)" reads cleanly; India geography share (tripwire 10, FY26 51%) NOT mappable from linearised donut — source-PDF required.
- **Railway**: order book ~₹8bn, PO-backed, executable within 12 months (s21 L528); no standalone Railway revenue/PAT in deck (baseline FY26 Rs 973 Cr rev / Rs 149 Cr PAT unverifiable here).

### Chart-label items to confirm against source PDF (carried from A2, verified as unrecoverable)
Slide 6 revenue-bridge waterfall (L170-181); Slide 21 Robotics/Railway #Programs & #Customers split (L516-517); Slide 28 RoCE/RoE and WCTR/FATR column mapping (L709-720); Slide 36 EV-programs-by-geography breakdown (L967-980, ~37 vs stated 36 customers). **Added by A3:** Slide 23 geography/product/market donuts (L547-577) — A2 did not flag these `CHART_LABEL_AMBIGUOUS` but the value-to-label mapping is not mechanically recoverable; surfaced for A4 because tripwire 10 (India mix) depends on it.

### "What Was NOT Discussed" (F17 silence audit vs Notion tripwires) — consecutive-silence count = 1 (first tracked quarter)
| Monitoring item | Addressed in deck? | Note |
|---|---|---|
| Capex / FCF | NO | Zero capex token despite 4 SOP commitments (A3-F17-01). |
| Tripwire 3 Novelic KAM impairment | NO | NOVELIC named only in ROCE/ROE denominators (L729-730) and Phase-4 history (L758); no impairment / KAM status. |
| Tripwire 5 corporate guarantee | NO | Not mentioned. |
| Tripwire 7 receivable / WC days | PARTIAL | WCTR shown but days not derivable (label ambiguous). |
| Tripwire 4 CFO / CFO-to-PAT | NO | No cash-flow statement in deck. |
| Tripwire 2 forced block sale / control dispute | NO | Not mentioned (DENSO JV control terms disclosed, s9, unrelated). |
| Tripwire 8 Railway diversification P&L | PARTIAL | Order book only; no Railway revenue/PAT. |

---

```yaml
stage: A3-forensics
company: "SONACOMS"
quarter: "Q1 FY27"
doctype: "presentation"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/sona-q1fy27/work/forensics_presentation_sona_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: N.A.
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: N.A.
  F9: N.A.
  F10: N.A.
  F11: N.A.
  F12: N.A.
  F13: N.A.
  F14: N.A.
  F15: N.A.
  F16: FINDING
  F17: FINDING
findings:
  - {id: "A3-F6-01", check: "F6", line: "s18 L450; s20 L486", classification: "FORWARD-SIGNAL", implication: "Four dated SOP commitments (H2FY26/H1FY28/H2FY28/H2FY29) seed promise-vs-delivery tracker; H2FY26 near-term test."}
  - {id: "A3-F6-02", check: "F6", line: "s11 L318-319", classification: "FORWARD-SIGNAL", implication: "AMR 'ongoing'; watch for first AMR sale/completion next quarter."}
  - {id: "A3-F6-03", check: "F6", line: "s6 L160", classification: "AMBIGUOUS", implication: "Undated 10x-decade aspiration; ask for quantified medium-term bridge."}
  - {id: "A3-F7-01", check: "F7", line: "s21 L525-527", classification: "AMBIGUOUS", implication: "Rs240bn order book risk-adjusted by undisclosed delay discount + EOL haircut; gross book undisclosed."}
  - {id: "A3-F16-01", check: "F16", line: "s37 L1010,1014", classification: "CONFIRMATORY-NEGATIVE", implication: "Indian-share dominance claim rests on Feb-2021 CRISIL source; stale."}
  - {id: "A3-F16-02", check: "F16", line: "s33 L871-895", classification: "AMBIGUOUS", implication: "'Guided by Values' frames historical FY22-FY26 metrics as forward; do not recharacterise as guidance."}
  - {id: "A3-F16-03", check: "F16", line: "s35 L934-937", classification: "AMBIGUOUS", implication: "Headline 44% BEV share is annualised; qualifier absent on s14/s17."}
  - {id: "A3-F16-04", check: "F16", line: "s27 L701", classification: "AMBIGUOUS", implication: "Revenue includes undisclosed net forex gain; quality-of-revenue caveat."}
  - {id: "A3-F17-01", check: "F17", line: "deck-wide (grep=0)", classification: "FORWARD-SIGNAL", implication: "No capex disclosed despite 4 SOP commitments; against FY26 capex ~37% of rev + negative FCF, material silence."}
  - {id: "A3-F17-02", check: "F17", line: "s28 L709-710,729,735", classification: "FORWARD-SIGNAL", implication: "ROCE 18.4->15.4->15.8% (down YoY, still >14%); reported figure normalised (Railway annualised) - obtain un-normalised."}
  - {id: "A3-F17-03", check: "F17", line: "s27 L682,690", classification: "CONFIRMATORY-NEGATIVE", implication: "EBITDA margin 23.1% vs 23.8% YoY and vs FY26 24.7%; continued compression (tripwire 6)."}
  - {id: "A3-F17-04", check: "F17", line: "s18 L448; s20 L483", classification: "AMBIGUOUS", implication: "Same NA OEM anchors two Q1 wins; customer-concentration probe (tripwire 9)."}
  - {id: "A3-F17-05", check: "F17", line: "deck-wide silence", classification: "CONFIRMATORY-NEGATIVE", implication: "Silent on tripwires 2/3/5/7 and CFO; consecutive-silence count=1 (first tracked quarter)."}
  - {id: "A3-F17-06", check: "F17", line: "s23 L547-577", classification: "AMBIGUOUS", implication: "India geography mix (tripwire 10) not recoverable from donut; source-PDF needed; A2 under-flagged s23."}
forward_signals: ["A3-F6-01", "A3-F6-02", "A3-F17-01", "A3-F17-02"]
ambiguous: ["A3-F6-03", "A3-F7-01", "A3-F16-02", "A3-F16-03", "A3-F16-04", "A3-F17-04", "A3-F17-06"]
commitments:
  - {commitment: "Diff Assembly Hybrid PV (NA OEM) Rs6,400mn order-book add", implied_date: "H2 FY29 SOP", ref: "s18 L450", status_word: "awarded"}
  - {commitment: "Hub-Wheel Traction Motor E2W (new Indian OEM) Rs900mn add", implied_date: "H2 FY26 SOP", ref: "s18 L450", status_word: "awarded"}
  - {commitment: "Diff Gears Non-Electric PV (NA OEM) Rs2,100mn add", implied_date: "H2 FY28 SOP", ref: "s20 L486", status_word: "awarded"}
  - {commitment: "Diff Gears Non-Electric CV/OHV (NA+Indian) Rs400mn add", implied_date: "H1 FY28 SOP", ref: "s20 L486", status_word: "awarded"}
  - {commitment: "Full AMR platform in-house development", implied_date: "undated", ref: "s11 L318-319", status_word: "underway"}
  - {commitment: "Railway order book execution", implied_date: "next 12 months", ref: "s21 L528", status_word: "committed"}
  - {commitment: "Replicate 10x growth", implied_date: "next decade", ref: "s6 L160", status_word: "aspiration"}
gate_a3: pass
blank_checks: []
```
