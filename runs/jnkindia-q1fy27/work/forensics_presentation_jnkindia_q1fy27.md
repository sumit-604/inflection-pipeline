# A3 FORENSIC NOTES — JNK India Limited (JNKINDIA) — Q1 FY27 — DOCTYPE: PRESENTATION

Source extract: `extract_presentation_jnkindia_q1fy27.txt` (591 lines, 21 pages / 20 deck slides).
Ledger: `ledger_presentation_jnkindia_q1fy27.md` (36 P&L line items + 44 chart/commentary rows + 7 footnotes + §6 dropped-slide table). **Ledger rows read verbatim at cited lines: 100%.**
Prior-quarter deck: **none supplied.** F16 dropped-slide items are judged against standard industrial-EPC IR-deck expectation, **not a literal prior-deck diff** — flagged as risk, not confirmed drop. No prior deck is fabricated.

Doctype applicability (per prompt + injected directive): F16 is primary; F6/F7/F10/F11/F14 run on numbers/text the deck carries; balance-sheet / auditor / segment / entity / concall checks (F1-F5, F8, F9, F12, F13, F15, F17) are N.A. and marked so. F2 is N.A. per the presentation doctype rule ("On a presentation, F16 applies plus any F6/F10/F11 numbers"); the standalone-vs-consolidated divergence the ledger routed as "F2/F10" is therefore recorded under **F10**, its applicable leg.

---

## FINDINGS TABLE

| id | check | ledger row ref | line/slide | verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| F-01 | F10 | S16 / C16 | L248 (std PAT) vs L221 (cons PAT) | std PAT "-0.8" ; cons PAT "9.6" | FORWARD-SIGNAL | The ENTIRE consolidated profit sits outside the parent. Standalone (core JNK India) is a **loss of Rs 0.8cr**; consolidated PAT Rs 9.6cr is 100% subsidiary/consolidation-derived. S-vs-C PAT gap widened from Rs 0.0cr (Q1FY26: 1.1 vs 1.1) to Rs 10.4cr in one year — far beyond the 5pp threshold. Core franchise is not making money this quarter. Tax Rs 5.0cr > PBT Rs 4.2cr (L247/L245) drives the loss — an ETR >100% that itself needs explanation. |
| F-02 | F10 | S18 | L250 | Basic EPS "2.42" | AMBIGUOUS | Standalone Basic EPS printed **+2.42** in the same statement where standalone PAT is **-0.8** (L248). A positive EPS cannot arithmetically follow a negative PAT on the same share base. Historically standalone EPS tracks consolidated tightly (Q4FY26 5.66 vs 5.84; FY26 11.59 vs 11.61); here standalone 2.42 even exceeds consolidated 2.05 (L223) despite a standalone loss. Either the loss numerator or the EPS is mis-stated. Question for management. |
| F-03 | F10 | S16 | L248 | YoY "11.6x" | AMBIGUOUS | The standalone YoY column prints "11.6x" across a **sign flip** (+1.1 → -0.8). A positive multiple cannot describe a swing into loss. Misleading presentation of a deterioration as a growth multiple. |
| F-04 | F10 | S4/S8 vs C4/C8 | L236/L240 vs L209/L213 | std EBITDA Margin "5.6%" (was "6.9%") ; cons EBITDA Margin "11.8%" | FORWARD-SIGNAL | Core (standalone) margins **deteriorated YoY**: GP margin 23.3%→20.1%, EBITDA margin 6.9%→5.6%. The flattering consolidated EBITDA-margin "expansion" 7.0%→11.8% is a **consolidation artifact**, not core operating improvement. The CMD's "maintained an EBITDA margin of 11.8%" narrative (L105) masks core margin erosion. Consolidated margin also fell QoQ (Q4FY26 15.2% → 11.8%). Both EBITDA lines are stated "(Includes Other Income)" (L212/L239), a further quality caveat. |
| F-06 | F6 | Table B / commentary | L114, L116, L396, L400, L188 | "They are executing the green hydrogen project" ; "has been set up by JNK India" | FORWARD-SIGNAL | Dateable management commitments seeded for the promise-vs-delivery tracker (see Commitment Register). Green-hydrogen execution = underway; Faridabad IOC fuelling station = completed milestone; JNK Renewable "building capabilities" = initiated; entry into offshore / metals & minerals = intended. Track status transitions next quarter. |
| F-07 | F7 | Footnote F4 | L181-184 | "an isolated incident, with no material costs incurred and no execution having commenced" | AMBIGUOUS | Pre-emptive legal/IR cover on a cancelled large export order. The cancellation cause — "inability to secure the requisite technical approval from the licensor" — reveals a **structural licensor-technology dependency** (ties to the JNK Global 82% reliance in the thesis) and export-order fragility. A newly-added hedge about order lumpiness signals what export execution risk looks like next quarter. |
| F-08 | F14 | masthead vs cover | L72 vs L31 | deck masthead "BSE: 544220" ; cover "Scrip code: 544167" | NEUTRAL-FACT | Deck title slide prints **BSE: 544220**, contradicting the actual BSE scrip code 544167 on the SEBI cover letter (L31) — a live data-integrity error in the published deck. Compounded by Chemdist footnote wording variance ("not part it" L129/226 vs "not part of it" L168) and typos ("Cracking Fumaces" L482, "Entry Barries" L471). Individually immaterial; cumulatively a weak-disclosure-control governance data point. |
| F-09 | F16 | PARTIAL_YOY_DISCLOSURE | L207-222 / L234-249 | YoY cells blank on all cost lines and every margin% row | AMBIGUOUS | Only the 6 flattering headline lines (Total Income, Gross Profit, EBITDA, EBIT, PBT, PAT) carry a YoY figure; all 12 cost lines and **every margin% row are blank** in both statements. Selective disclosure that suppresses exactly the rows (cost growth, margin trend) that would show core deterioration. Ask why cost/margin YoY is omitted. |
| F-10 | F16 | Table B rows L177-198 | L177-178 (book) vs L188-198 (inflow) | Order Book "1,961" (Mar-26) → "1,801" (Jun-26) ; Order Inflow chart ends "Mar-26" | FORWARD-SIGNAL | Order book **declined QoQ -8.2%** (1,961 → 1,801), confirming the thesis' Rs 1,961cr Q4FY26 base and a negative direction. Simultaneously the **Q1FY27 order-inflow figure is omitted**: the inflow chart stops at Mar-26 (annual bars 229/933/1,694) while the order-book chart runs to Jun-26 — asymmetric framing that hides a likely weak current-quarter inflow. |
| F-11 | F16 | §6 dropped-slide table | §6 (L240-251) | 10 standard IR disclosures "ABSENT" | FORWARD-SIGNAL | Judged vs standard IR-deck expectation (no prior deck to diff). Weighted absences: (a) **order-book segment/geography split** absent — hides the JNK Global 82% dependency and export concentration; (b) **balance sheet / net debt** absent despite a Rs 4.4cr finance cost implying borrowings; (c) **cash-flow slide** absent — hides the operating-CFO monitorable (Notion check #1) and debtor-days (check #2); (d) **no forward guidance** (qualitative only); (e) no customer concentration; (f) no shareholding pattern; (g) director slide carries no DIN/tenure/shareholding. |
| F-12 | F16 | commentary + slides 13-15 | L114-121, L381-401 | "focusing more on renewable energy" ; "JNK Chemdist has started adding value to our focus on renewable energy" | FORWARD-SIGNAL | **Narrative-rotation risk realised.** Commentary and Slides 13-15 give heavy billing to renewables / waste-gas / green-hydrogen / Chemdist, while the **core fired-heater standalone entity just posted a loss (F-01)**. The core is de-emphasised precisely as it deteriorates; the growth story is being relocated onto a newly-consolidated subsidiary. |
| F-13 | F16 | MINOR_FIGURE_VARIANCE | L141/149 vs L221 ; L152 | chart "64.7" vs table PAT "64.8" | NEUTRAL-FACT | FY26 consolidated PAT is 64.7 on the Slide-4 chart but 64.8 in the Slide-6 table (0.1cr rounding). Chart value 41.1 (L152) does not tie to any Q4FY26 table figure (Q4FY26 EBIT 49.3) — an unreconciled chart label, unverifiable without the source image. Chart-vs-table hygiene gap; low forward content. |
| F-14 | F16 | Footnote F1/F2 | L129/L168 | "includes Revenue of Rs 16.5 cr from JNK Chemdist Limited which was not part ... in Q1FY26" | AMBIGUOUS | The 80.6% YoY Total-Income headline is inflated by **Rs 16.5cr inorganic, newly-consolidated Chemdist revenue (~9% of Q1FY27 income)**; organic growth is overstated. Sharper: the consolidated-minus-standalone gap is Rs 15.9cr revenue but Rs 12.4cr EBITDA (L212 vs L239) — a **~78% incremental margin** on the newly consolidated slice, implausibly high and unexplained (eliminations? one-offs?). The entire consolidated beat rests on this subsidiary. |

---

## CHECKLIST SCORECARD (all 17)

| # | Status | Basis (one line) |
|---|---|---|
| F1 | **N.A.** | Zero-standing line items: ledger `zero_standing = 0`; no template zero/Nil/exceptional rows in a deck P&L. Balance-sheet template check does not apply to a presentation. |
| F2 | **N.A.** | Standalone-vs-consolidated decomposition is not a presentation-doctype check per the framework rule; the divergence the ledger flagged (F2/F10) is recorded under **F10** (F-01/F-04/F-14). |
| F3 | **N.A.** | Shell-entity detection needs entity-level cost lines / consolidation detail absent from a deck. |
| F4 | **N.A.** | No auditor report / Other Matters paragraph in a presentation. |
| F5 | **N.A.** | No going-concern / EoM language in a presentation; no prior deck to verbatim-diff. |
| F6 | **FINDING** | F-06: forward commitments mined (green-hydrogen underway, Faridabad station completed, renewable build initiated, offshore/metals entry). |
| F7 | **FINDING** | F-07: pre-emptive hedge framing the cancelled export order as "isolated," exposing licensor-approval dependency. |
| F8 | **N.A.** | Tax forensics N.A. per injected directive (no ETR reconciliation / deferred-tax detail in deck); the tax-Rs5.0cr-> PBT-Rs4.2cr anomaly is carried inside F-01. |
| F9 | **N.A.** | No OCI / actuarial disclosure in a presentation. |
| F10 | **FINDING** | F-01/F-02/F-03/F-04: standalone loss vs consolidated profit, EPS sign incoherence (+2.42 vs -0.8 PAT), incoherent "11.6x" YoY, core-margin deterioration. |
| F11 | **N.A.** | Deck carries no reserves / paid-up / net-worth figure to tie out. |
| F12 | **N.A.** | No segment assets/liabilities tables in the deck (segment-split absence is instead logged as an F16 dropped disclosure, F-11). |
| F13 | **N.A.** | No board-meeting outcome / AR / AGM / director term-dates in the deck; Slide 19 gives bios only (thinness routed to F16 F-11). |
| F14 | **FINDING** | F-08: BSE code mismatch (544220 vs 544167), Chemdist footnote wording variance, typos — cumulative disclosure-control signal. |
| F15 | **N.A.** | No consolidation entity list in a deck; no prior deck to diff. |
| F16 | **FINDING** | F-09/F-10/F-11/F-12/F-13: partial-YoY selective disclosure, order-book QoQ decline + inflow omission, 10 dropped standard disclosures, narrative rotation, chart-vs-table variance. Primary check for this doctype. |
| F17 | **N.A.** | No concall transcript in scope; silence audit not runnable on a deck. |

No check left blank. **GATE A3: pass.**

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | slide/line ref | status word |
|---|---|---|---|
| JNK Chemdist executing the green hydrogen project | ongoing / FY27 | Slide 4, L116 | underway |
| Fuelling station at Indian Oil (Faridabad) R&D Centre set up by JNK India | done (as-stated) | Slide 15, L400 | completed |
| JNK Renewable Energy Pvt Ltd "building capabilities" in clean-energy infrastructure | ongoing / FY27 | Slide 15, L396 | initiated |
| Entering off-shore, metals & minerals; "focusing more on renewable energy" | FY27+ (undated) | Slide 4, L114-115 | initiated |
| Convert Rs ~6,000cr bidding pipeline (50:50 domestic:export) into orders | FY27+ (undated) | Slide 6, L188-190 | initiated |
| Expansion "will broaden our addressable market" | undated | Slide 4, L119 | initiated |

Note: the deck carries **no explicitly dated** commitment (no "expected by <date>", no "shall be completed by"). All implied dates are ongoing/FY27; low commitment specificity is itself an F16-adjacent observation (no guidance).

---

## FORWARD-LOOKING SUMMARY (for A4)

- **FORWARD-SIGNALS (6):** F-01 (core is loss-making; all profit is subsidiary-derived), F-04 (core-margin deterioration masked by consolidation), F-06 (forward commitments to track), F-10 (order book down QoQ + inflow hidden), F-11 (cash-flow/net-debt/segment-split all absent — the monitorables are the ones dropped), F-12 (narrative rotation onto renewables/Chemdist as core weakens).
- **AMBIGUOUS -> A4 questions (5):** F-02 (positive EPS on a loss), F-03 (11.6x across a sign flip), F-07 (licensor-dependency / export fragility), F-09 (why cost & margin YoY suppressed), F-14 (inorganic Chemdist boost + implausible ~78% incremental EBITDA margin).
- **Conservative read:** every uncertain item is leaned bear and converted to a question. The headline (TI +80.6%, PAT +8.5x, EBITDA "maintained 11.8%") is a consolidated-and-inorganic story; the standalone core posted a loss with deteriorating margins and a shrinking, partially-undisclosed order book.

---

```yaml
stage: A3-forensics
company: "JNKINDIA"
quarter: "Q1 FY27"
doctype: "presentation"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/jnkindia-q1fy27/work/forensics_presentation_jnkindia_q1fy27.md"
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
  F10: FINDING
  F11: N.A.
  F12: N.A.
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: N.A.
findings:
  - {id: "F-01", check: "F10", line: "L248/L221", classification: "FORWARD-SIGNAL", implication: "Standalone PAT -0.8cr loss vs consolidated +9.6cr; all consol profit is subsidiary-derived; S-vs-C PAT gap 0.0->10.4cr YoY; tax>PBT drives loss"}
  - {id: "F-02", check: "F10", line: "L250", classification: "AMBIGUOUS", implication: "Basic EPS printed +2.42 against standalone PAT -0.8; sign-incoherent; EPS or loss mis-stated"}
  - {id: "F-03", check: "F10", line: "L248", classification: "AMBIGUOUS", implication: "YoY '11.6x' shown across a +1.1->-0.8 sign flip; misleading multiple on a swing into loss"}
  - {id: "F-04", check: "F10", line: "L236/L240", classification: "FORWARD-SIGNAL", implication: "Core standalone margins deteriorated YoY (GP 23.3->20.1, EBITDA 6.9->5.6); consolidated margin expansion is a consolidation artifact masking core erosion"}
  - {id: "F-06", check: "F6", line: "L116/L400/L396/L114", classification: "FORWARD-SIGNAL", implication: "Dateable commitments: green-hydrogen underway, Faridabad station completed, renewable build initiated, offshore/metals entry intended"}
  - {id: "F-07", check: "F7", line: "L181-184", classification: "AMBIGUOUS", implication: "Pre-emptive framing of cancelled export order as isolated; exposes licensor-technology dependency and export execution fragility"}
  - {id: "F-08", check: "F14", line: "L72/L31", classification: "NEUTRAL-FACT", implication: "Deck masthead BSE:544220 contradicts actual scrip code 544167; footnote wording variance + typos; weak disclosure-control signal"}
  - {id: "F-09", check: "F16", line: "L207-222/L234-249", classification: "AMBIGUOUS", implication: "YoY shown only on 6 flattering headline lines; all cost lines and margin% rows blank; selective disclosure suppressing core-deterioration rows"}
  - {id: "F-10", check: "F16", line: "L177-178/L188-198", classification: "FORWARD-SIGNAL", implication: "Order book down QoQ -8.2% (1961->1801); Q1FY27 order inflow omitted (inflow chart stops Mar-26) hiding weak current-quarter inflow"}
  - {id: "F-11", check: "F16", line: "sec6-L240-251", classification: "FORWARD-SIGNAL", implication: "10 standard IR disclosures absent vs deck norm; order-book split (JNK Global 82%), balance sheet/net debt, cash flow (CFO monitorable), guidance, customer concentration all missing"}
  - {id: "F-12", check: "F16", line: "L114-121/L381-401", classification: "FORWARD-SIGNAL", implication: "Narrative rotation onto renewables/waste-gas/Chemdist while core fired-heater standalone posts a loss"}
  - {id: "F-13", check: "F16", line: "L141/L221", classification: "NEUTRAL-FACT", implication: "FY26 PAT chart 64.7 vs table 64.8; chart value 41.1 unreconciled to tables; chart-vs-table hygiene gap"}
  - {id: "F-14", check: "F16", line: "L129/L168", classification: "AMBIGUOUS", implication: "80.6% TI growth inflated by Rs16.5cr inorganic Chemdist (~9%); ~78% incremental EBITDA margin on the consolidated slice is implausible and unexplained"}
forward_signals: [F-01, F-04, F-06, F-10, F-11, F-12]
ambiguous: [F-02, F-03, F-07, F-09, F-14]
commitments:
  - {commitment: "JNK Chemdist executing green hydrogen project", implied_date: "ongoing/FY27", ref: "Slide4-L116", status_word: "underway"}
  - {commitment: "Faridabad IOC R&D fuelling station set up", implied_date: "as-stated/done", ref: "Slide15-L400", status_word: "completed"}
  - {commitment: "JNK Renewable Energy Pvt Ltd building clean-energy capabilities", implied_date: "ongoing/FY27", ref: "Slide15-L396", status_word: "initiated"}
  - {commitment: "Entry into offshore, metals & minerals; more renewable focus", implied_date: "FY27+ undated", ref: "Slide4-L114", status_word: "initiated"}
  - {commitment: "Convert Rs~6,000cr bidding pipeline (50:50 dom:exp) into orders", implied_date: "FY27+ undated", ref: "Slide6-L188", status_word: "initiated"}
  - {commitment: "Expansion will broaden addressable market", implied_date: "undated", ref: "Slide4-L119", status_word: "initiated"}
gate_a3: pass
blank_checks: []
```
