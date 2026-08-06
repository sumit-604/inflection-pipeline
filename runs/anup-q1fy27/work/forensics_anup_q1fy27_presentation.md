# FORENSIC NOTES — A3 — The Anup Engineering Limited (ANUP) — Q1 FY27 — DOCTYPE: PRESENTATION (Investor Deck)

Model: claude-opus-4-8 | Agent: A3 FORENSIC NOTES
Extract: `extract_presentation_anup_q1fy27.txt` (26 pages, 686 lines, 8 OCR'd)
Ledger: `ledger_presentation_anup_q1fy27.md` (Tables 1, 1a, 2, 3, 4, 5 — all rows read)
Ledger reconciliation: 100% (26 slides, 217 numbers, 6 footnotes, 0 zero-standing all read at cited lines)
Prior-deck mechanical diff: NOT AVAILABLE (NO_PRIOR_LEDGER). F16 reframing judged against the Notion prior-deck baseline; this is institutional memory, not an anchored mechanical diff — limitation noted on every F16 sub-finding.

Applicability (per prompt + task): F16 primary; F6/F7/F14 run on deck prose and tables; F10/F11 checked but deck carries no share-count/net-worth figures; all balance-sheet/P&L forensics with no deck data marked N.A.; F17 N.A. (not a concall).

---

## FINDINGS TABLE

| id | check | ledger row ref | line/slide | verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| F16-01 | F16 | T1 r6 (contents), r10 (fin. section); T5 (no prior ledger) | slide 6 L159-162; slide 10 L233 | "1. Operational Highlights ... 2. Financial Performance – Q1 FY27 ... 4. Annexures"; "FINANCIAL INDICATORS – CONSOLIDATED" | FORWARD-SIGNAL | No balance sheet, no cash-flow statement, no debtor-days slide anywhere in the deck. Two of the three thesis-broken triggers (Quarterly CFO < ₹100 Cr; Debtor days > 175) are UN-READABLE from this deck. Omission during a demonstrably weak quarter continues the Q3-FY26 balance-sheet-omission pattern. Lean bear; A4 must source the CFO/DD from the results filing. |
| F16-02 | F16 | T1 r10; T2 slide 10 (L235-247) | slide 10 L233, L243 | "FINANCIAL INDICATORS – CONSOLIDATED"; "EBIDTA % 7.6% 23.0% ... 21.2%" | FORWARD-SIGNAL | Deck presents CONSOLIDATED-only. The standalone EBITDA-margin trigger (< 19%) cannot be read directly. Consolidated margin is 7.6% (down from 23.0% YoY); standalone almost certainly also breaches. Standalone breakout absent vs the standalone figures the thesis tracks (FY26 21.9% std). |
| F16-03 | F16 | T2 slide 15 (L332-341) | slide 15 L335-337 | "the focus of the company this year will be more on Stabilization of current operations, better Execution, Consolidation and Risk mitigation, which seemingly getting in to low impact phase" | FORWARD-SIGNAL | Margin/growth guidance DROPPED entirely. Prior decks carried a numeric margin frame ("industry leading 22%" -> "guided 21%"); this outlook slide gives no margin or revenue target and reframes FY27 as a stabilisation year. Softened guidance = management expects no near-term recovery. |
| F16-04 | F16 | T3 fn5; T2 slide 8/10 | slide 10 L238-240; slide 8 L201 | "EBITDA margins were impacted entirely by lower revenue leading to under-absorption of fixed costs, while our gross margin remain intact" | AMBIGUOUS | The 76.5% EBITDA collapse is framed as PURELY fixed-cost under-absorption; the "gross margin remain intact" claim is unverifiable — no gross-margin figure is disclosed anywhere in the deck. A4 question: produce the gross-margin bridge Q1FY27 vs Q1FY26. |
| F16-05 | F16 | T2 slide 8 (L203), slide 15 (L332); T2 slide 14 | slide 8 L203; slide 15 L332 | "best pending orderbook visibility (including LOI) of ₹985 Cr"; "₹985 Cr (of which ~₹240 Cr booked for FY28)" | AMBIGUOUS | Order-book composition change. The explicit LOI ₹ value (prior decks: ₹49 / ₹73 / ₹146) is NO LONGER broken out — bundled into the ₹985 Cr headline, so Notion's "LOI < 20%" test is not computable. ₹240 Cr is FY28-booked, so FY27-executable book is ~₹745 Cr, BELOW the ₹800 Cr green threshold. Headline flatters. |
| F16-06 | F16 | T2 slide 17 (L365) | slide 17 L365 | "A net debt free company" | AMBIGUOUS | The "net debt free" framing — quietly dropped from Q4 operational bullets per Notion — is RE-ADDED, but relegated to an annexure company-fact panel and carries no net-cash figure. Reframing to reassure; verify against balance sheet (which is itself absent, see F16-01). |
| F16-07 | F16 | T2 slide 5 (L132), slide 3 (L83-85) | slide 5 L132; slide 3 L83-85 | "Market Cap 14600 ... 6300 ... 4500 ... 2800"; "does not constitute an offer or invitation to purchase or subscribe for any shares" | AMBIGUOUS | The Lalbhai-group market-cap dashboard (added Q4 IP) PERSISTS at the front of the deck; safe-harbor retains the equity-subscription clause. Continue monitoring for a capital-raising signal, especially with the balance sheet withheld. |
| F16-08 | F16 | T2 slide 8 (L211), slide 15 (L340), slide 21 (L513) | slide 8 L211; slide 15 L340 | "Good traction in the Technical Services business"; "wishes to strategically grow the Technical services business vertical" | CONFIRMATORY-NEGATIVE | Four monitored metrics are asserted qualitatively but NOT quantified: services-vertical revenue (Notion wants > ₹10 Cr/q), high-volume mix (> 15%), dividend, and FY27 capex (Kheda Phase 3 is only "Future Plan", slide 21 L513). Silence on monitored line items during a weak quarter. |
| F6-01 | F6 | T2 slide 8 (L204-209), slide 15 (L338-341), slide 21 (L510-513) | slide 8 L204-205, L209; slide 15 L338-341 | "which is expected to see significant growth in near future"; "Started execution of two large Air-Cool Hear Exchanger for a marquee customer in Germany" | FORWARD-SIGNAL | Seven dateable/status commitments mined (see Commitment Register). Thermal-Power >₹150 Cr order booked (new), German ACHE execution "Started" (initiated->underway), Nuclear/thermal/clean-energy foray restated, services-growth intent, Kheda Phase-2A open bay "commissioned in Jan'26" (completed). Feeds Role 5 promise-vs-delivery tracker. |
| F7-01 | F7 | T2 slide 8 (L199), slide 15 (L335-337, L341) | slide 8 L199; slide 15 L341 | "we chose to wait out, protecting profitability over short term growth"; "Continuous endeavor to add new critical and proprietary products" | FORWARD-SIGNAL | Newly foregrounded hedge cluster: "wait out", "global volatile business scenarios due to wars & geopolitics", "endeavor". Pre-emptive cover framing FY27 around defense not growth — signals continued weak revenue/execution near term. |
| F14-01 | F14 | T1 r10 note; T2 slide 10 (L236-247) | slide 10 L238, L242-243 | "Change / QoQ%" (over columns "Q1 FY27" and "Q1 FY26"); "EBIDTA" / "EBIDTA %" | NEUTRAL-FACT | Drafting/period-basis inconsistency: the change column is labelled "QoQ%" but compares Q1 FY27 vs Q1 FY26 — a YoY delta mislabelled as sequential. "EBITDA" is misspelled "EBIDTA" throughout the table. Individually immaterial; a data-integrity/period-basis (PERIOD_BASIS_NOTE) data point A4 must read as YoY, not QoQ. |

---

## CHECKLIST SCORECARD (all 17 — every check marked; GATE A3)

| Check | Status | Basis (one line) |
|---|---|---|
| F1 Zero-value standing line items | N.A. | Ledger Table 4: no zero/nil/dash line item in any deck table (slides 10/12/14 all fully populated); nothing to interpret. |
| F2 Standalone vs consolidated decomposition | N.A. | Deck carries CONSOLIDATED-only (slide 10 L233); no standalone column to decompose. Consequence flagged under F16-02. |
| F3 Shell-entity detection | N.A. | No standalone-vs-consolidated cost lines in a deck; Mabel named as 100% sub (slide 19) but no cost data. |
| F4 Unaudited contribution ratio | N.A. | No auditor Other-Matters paragraph in a presentation. |
| F5 Going concern / EoM scope | N.A. | No auditor EoM in a presentation; no prior deck for verbatim diff. |
| F6 Forward-commitment phrase mining | FINDING | F6-01: seven status/dateable commitments mined (Register below). |
| F7 Hedge phrase mining | FINDING | F7-01: new macro-hedge cluster ("wait out", "wars & geopolitics", "endeavor", L199/L335-337/L341). |
| F8 Tax forensics | N.A. | Not a deck check (prompt: deck runs F16+F6/F10/F11); PBT/PAT rounded to ₹0.9/₹0.6 Cr make Q1FY27 ETR non-meaningful. Note for the results-filing run: FY26 consol ETR = 28.9/139.3 = 20.7%, ~4.4pp below statutory 25.17% (possible shield / future ETR step-up). |
| F9 OCI forensics | N.A. | No OCI / actuarial disclosure in a presentation. |
| F10 Share count and dilution | N.A. | Deck carries no paid-up capital, no share count, no EPS. (Slide 5 "Market Cap" figures are group-level, not ANUP share data.) |
| F11 Reserves and net-worth tie-out | N.A. | Deck carries no Other Equity / net-worth figure; only the unquantified "net debt free" claim (handled at F16-06). |
| F12 Segment forensics | N.A. | Revenue split by product/market/industry only (slides 11-12); no segment assets or liabilities. |
| F13 Board outcome beyond results | N.A. | Investor presentation carries no board resolutions / AGM notice / director terms. |
| F14 Note drafting inconsistencies | FINDING | F14-01: "Change QoQ%" mislabels a YoY delta; "EBIDTA" misspelling on slide 10. |
| F15 Entity list diffs | N.A. | No consolidation list in a deck; no prior ledger for diff. Mabel/TAEL naming consistent (slides 19, 22). |
| F16 Dropped / reframed disclosures | FINDING | F16-01..08: balance-sheet/CF/DD absent, consolidated-only, margin guidance dropped, under-absorption framing, LOI unbundled, "net debt free" re-added, Lalbhai dashboard persists, monitored metrics unquantified. |
| F17 Concall silence audit | N.A. | Not a concall; per task, N.A. |

Blank checks: none. GATE A3: PASS.

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/slide ref | status word |
|---|---|---|---|
| Thermal-Power order >₹150 Cr booked; sector "expected to see significant growth in near future" | near future (undated) | slide 8, L204-205 | booked / expected |
| Execution of two large Air-Cool Heat Exchangers for a marquee customer in Germany | in progress | slide 8, L209 | initiated -> underway ("Started execution") |
| Two proprietary-license products bagged; move into niche segment | ongoing | slide 8, L207 | initiated |
| Foray into Nuclear, Thermal energy and clean-energy storage segment | long-term (undated) | slide 15, L338-339 | intended / underway |
| Strategically grow the Technical Services business vertical | FY27 | slide 15, L340 | intends ("wishes to") |
| Continuous endeavour to add new critical and proprietary products | ongoing | slide 15, L341 | endeavour (also F7 hedge) |
| Kheda Phase-2A open bay commissioned | Jan'26 | slide 21, L511-512 | completed (milestone confirmation) |
| Kheda Phase-3 (3 bays) | future | slide 21, L513 | proposes ("Future Plan") |

Status-transition note: "Started execution" (German ACHE) and the Jan'26 Kheda open-bay commissioning are the two hardest status confirmations this quarter; the Nuclear/thermal/clean-energy "foray" language is unchanged vs the Q4 IP bloom (no status advance) — restated intent, not a milestone.

---

## RECONCILIATION AND CROSS-DOC NOTES (not findings)

- Ledger reconciled 100%: every slide (T1), OCR page (T1a), number (T2, sum-check 217), footnote (T3), zero-standing scan (T4), dropped-slide row (T5) read at its cited line. A2 flags assessed: EXTRACTION_LAYOUT_AMBIGUITY (slide 5 panel alignment) — cross-checked, ANUP's own FY26 822/174/21%/21% ties to slide 10 FY26 column and slide 17, no contradiction; PERIOD_BASIS_NOTE — confirmed two basis mixes: slide 5 is FY26-annual inside a Q1FY27 deck (footnote L148 "Financial performance is as on FY26"), slide 10 change column is YoY mislabelled QoQ (F14-01); BLANK_CELL — slide 10 three margin-% change cells empty (not zero), consistent with the YoY-only presentation; EXTRACTION_AMBIGUITY (slide 18 10-icon/9-label) — non-numeric, no forensic impact; NO_PRIOR_LEDGER — limits F16 to Notion baseline.
- Cross-doc (informational, outside this deck's ledger): deck consol EBITDA = ₹9.5 Cr / 7.6% (L242-243); Notion cites press-release EBITDA ₹9.2 Cr / ~7.4%. ~₹0.3 Cr / 20bps gap likely standalone-vs-consolidated or rounding; A4 to confirm against the results filing.
- Group-slide juxtaposition (informational): slide 5 shows ANUP EBITDA margin 21% (FY26) at the front of a deck whose actual Q1FY27 consolidated margin is 7.6% — disclosed via footnote L148 but the placement flatters. Not a mislabel; noted for A4 framing.

---

```yaml
stage: A3-forensics
company: "ANUP"
quarter: "Q1 FY27"
doctype: "presentation"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/anup-q1fy27/work/forensics_anup_q1fy27_presentation.md"
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
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: N.A.
findings:
  - {id: "F16-01", check: "F16", line: "slide 6 L159-162; slide 10 L233", classification: "FORWARD-SIGNAL", implication: "No balance sheet / cash flow / debtor-days slide; CFO<100Cr and DD>175 triggers unreadable; continues Q3 omission pattern"}
  - {id: "F16-02", check: "F16", line: "slide 10 L233,L243", classification: "FORWARD-SIGNAL", implication: "Consolidated-only; standalone EBITDA-margin<19% trigger not directly readable; consol margin 7.6% vs 23.0% YoY"}
  - {id: "F16-03", check: "F16", line: "slide 15 L335-337", classification: "FORWARD-SIGNAL", implication: "Margin/growth guidance dropped; FY27 reframed to Stabilization/Risk mitigation; softened guidance"}
  - {id: "F16-04", check: "F16", line: "slide 10 L238-240; slide 8 L201", classification: "AMBIGUOUS", implication: "76.5% EBITDA fall framed as pure under-absorption; gross margin claim unverifiable, no gross-margin figure disclosed"}
  - {id: "F16-05", check: "F16", line: "slide 8 L203; slide 15 L332", classification: "AMBIGUOUS", implication: "LOI value no longer broken out of 985Cr headline; 240Cr is FY28-booked so FY27 book ~745Cr below 800Cr threshold; LOI<20% test not computable"}
  - {id: "F16-06", check: "F16", line: "slide 17 L365", classification: "AMBIGUOUS", implication: "'Net debt free' re-added but relegated to annexure with no net-cash figure; verify vs (absent) balance sheet"}
  - {id: "F16-07", check: "F16", line: "slide 5 L132; slide 3 L83-85", classification: "AMBIGUOUS", implication: "Lalbhai group market-cap dashboard persists + equity-subscription safe-harbor clause; capital-raising watch while balance sheet withheld"}
  - {id: "F16-08", check: "F16", line: "slide 8 L211; slide 15 L340", classification: "CONFIRMATORY-NEGATIVE", implication: "Services vertical, high-volume mix, dividend, FY27 capex all asserted or omitted but unquantified; silence on monitored metrics"}
  - {id: "F6-01", check: "F6", line: "slide 8 L204-205,L209; slide 15 L338-341; slide 21 L510-513", classification: "FORWARD-SIGNAL", implication: "Seven dateable commitments; German ACHE execution started, Kheda Phase-2A open bay commissioned Jan26, Thermal-Power >150Cr booked; feeds promise-vs-delivery tracker"}
  - {id: "F7-01", check: "F7", line: "slide 8 L199; slide 15 L335-337,L341", classification: "FORWARD-SIGNAL", implication: "New macro-hedge cluster (wait out / wars & geopolitics / endeavor); pre-emptive cover signals continued near-term weakness"}
  - {id: "F14-01", check: "F14", line: "slide 10 L238,L242-243", classification: "NEUTRAL-FACT", implication: "'Change QoQ%' header over Q1FY27-vs-Q1FY26 columns is a YoY delta mislabelled sequential; EBITDA misspelled EBIDTA; read change as YoY"}
forward_signals: ["F16-01", "F16-02", "F16-03", "F6-01", "F7-01"]
ambiguous: ["F16-04", "F16-05", "F16-06", "F16-07"]
commitments:
  - {commitment: "Thermal-Power order >150Cr booked; sector expected significant growth near future", implied_date: "near future", ref: "slide 8 L204-205", status_word: "booked/expected"}
  - {commitment: "Two large Air-Cool Heat Exchangers for German marquee customer", implied_date: "in progress", ref: "slide 8 L209", status_word: "underway"}
  - {commitment: "Two proprietary-license products bagged, niche-segment move", implied_date: "ongoing", ref: "slide 8 L207", status_word: "initiated"}
  - {commitment: "Foray into Nuclear/Thermal/clean-energy storage segment", implied_date: "long-term", ref: "slide 15 L338-339", status_word: "intended"}
  - {commitment: "Grow Technical Services business vertical", implied_date: "FY27", ref: "slide 15 L340", status_word: "intends"}
  - {commitment: "Continuous endeavour to add critical/proprietary products", implied_date: "ongoing", ref: "slide 15 L341", status_word: "endeavour"}
  - {commitment: "Kheda Phase-2A open bay commissioned", implied_date: "Jan-2026", ref: "slide 21 L511-512", status_word: "completed"}
  - {commitment: "Kheda Phase-3 (3 bays)", implied_date: "future", ref: "slide 21 L513", status_word: "proposes"}
gate_a3: pass
blank_checks: []
```
