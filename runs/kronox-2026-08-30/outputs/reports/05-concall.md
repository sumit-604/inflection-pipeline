# STAGE 5: CONCALL ANALYSIS — KRONOX Lab Sciences Ltd (NO-CONCALL MODE)

Run date: 2026-08-30. Ticker: KRONOX.

**Mode notice.** `concalls_available: false` in the manifest (B00-inputs.yaml). Kronox
holds no earnings conference calls. Per prompts/05-concall-pipeline.md degraded
procedure, this report substitutes: the AR FY26 Chairman's Letter (p.18-19), the
AR FY26 Board's Report (p.36-38), the AR FY26 Management Discussion & Analysis
(p.58-60), and the commentary in the two results filings (FY26 audited results,
21-May-2026; Q1 FY27 results, 12-Aug-2026). There is no analyst Q&A, no
cross-quarter transcript chronology, and no tone-under-pressure evidence anywhere
in this source set. Sections that depend on transcript material say so plainly
rather than manufacturing content. `credibility_grade` defaults to C in this mode
and may rise only to B on documented guidance-vs-delivery evidence; it can never
reach A.

Sources (page-marked .txt, primary; .pdf identical document):
- AR FY26 (120p): `runs/kronox-2026-08-30/work/annual-report__2f872b7a-c4ab-41c7-9262-12bffaed229c.txt`
- FY26 audited results (21-May-2026, 8p): `runs/kronox-2026-08-30/work/results__4c8de5ae-4d85-4704-bc7d-91f145c970a2.txt`
- Q1 FY27 results (12-Aug-2026, 7p): `runs/kronox-2026-08-30/work/results__03380acb-e15e-46b3-9b74-8ccb58720e10.txt`

---

## SECTION 1: GROWTH TRIGGERS & DRIVERS (from AR + results commentary only)

### 1A. Triggers table

| Trigger | Type | Timeframe | Confidence | Specificity |
|---|---|---|---|---|
| Dahej Unit IV restart: "new deadlines have been finalized" — production start ~2 years, whole unit functional ~3 years, from the FY26 AR date | VOLUME | Long (2-3y) | Stated as "planned/finalized" by management, but zero corroborating capex/CWIP/capital-commitment trail in the same document (see Section 2) | Very low: no rupee capex figure, no output/capacity figure, no month/quarter, only "coming two years" / "coming three years" (AR p.18-19) |
| Q1 FY27 revenue and PAT re-acceleration after a near-flat FY26 | VOLUME | Near (1 quarter reported) | FACT (already reported, not a management claim) | High on the numbers, zero explanatory color: no MD&A or notes accompany the Q1 FY27 filing (results 03380acb, p.3) |
| Rising export mix: 24.75% (FY24) to 26.57% (FY25) to 32.39% (FY26) of revenue | PRICE-MIX | Near-medium | FACT (reported trend); no forward target stated | High on the number, zero commentary on which geography/customer drove the shift (AR p.11) |
| Environmental/regulatory clearances secured for Dahej Unit IV (GPCB, Consent to Establish, GEB, CETP, BEIL, Central Government Environmental Clearance) | REGULATORY-POLICY | Already obtained | FACT (stated as complete) | Moderate: named the approving bodies, no dates given inside the AR itself (dates come from COMPANY MEMORY / B00 load-bearing facts: GPCB 13-Nov-2024, Consent to Establish 10-Nov-2025) |

### 1B. Quantified guidance (every specific number/date management committed to)

| Item | Number | Timeframe | Stated in |
|---|---|---|---|
| Dahej Unit IV production start | Not quantified in rupees or capacity; only "coming two years" | ~FY28 (from AR FY26 date) | AR FY26 Chairman's Letter, p.18-19 |
| Dahej Unit IV full functionality | Not quantified | ~FY29 (from AR FY26 date) | AR FY26 Chairman's Letter, p.18-19 |
| Final dividend FY26 | Rs 0.50/share (5% of Rs 10 face value), Rs 185.40 lakh total | Payable on AGM approval, 16-Sep-2026 | AR FY26 Board's Report, p.36-37 |
| Implicit revenue expectation | Qualitative only: "maintained its revenue as compare to last year" | FY26 | AR FY26 Chairman's Letter, p.18 |

No margin band, no explicit capex rupee figure (for Dahej or otherwise), no return target (ROCE/ROE), no debt-reduction target, and no capacity-in-tonnes figure appears anywhere in the AR or either results filing. This absence is itself a finding (Section 2D).

### 1C. Trigger evolution

Only one AR is held for this run (AR FY25 and AR FY24 are ABSENT per B00-inputs.yaml input_gaps), so a quarter-over-quarter or year-over-year trigger-evolution table from primary text cannot be built. What can be anchored from documents inside this AR plus the B00 load-bearing facts (operator-supplied, weighed not anchored):

- **Land for Unit IV** acquired 2022 (AR FY26 milestones timeline, p.4-5: "2022 — Acquisition of Land admeasuring to 20,471 sq.mtr. for Proposed Unit-IV").
- **GPCB approval**: 13-Nov-2024 (B00 load-bearing fact, not independently dated inside the AR text itself — the AR names the approving bodies (CETP, BEIL, GEB, GIDC, Central Government Environmental Clearance, AR p.18) but gives no dates).
- **Consent to Establish**: 10-Nov-2025 (B00 load-bearing fact).
- **Construction**: still "could not be started" as of the FY26 AR, signed 12-Aug-2026 (AR p.77, signature block) — i.e., at least 9 months after Consent to Establish and 21 months after GPCB approval, construction has not begun.
- **New deadlines "finalized"**: stated in the same FY26 AR, with no cause named for the prior slip beyond "unforeseen circumstances" (AR p.18).

This is a **timeline slippage**, documented from a single AR's internal chronology plus the regulatory-approval dates carried in COMPANY MEMORY. See `timeline_slippages` in the YAML block. There is no way, from the documents in this stage's scope, to test whether the "2 year / 3 year" language itself changed from a prior AR's wording, because no prior AR is held.

---

## SECTION 2: MANAGEMENT CREDIBILITY CHECK

### 2A. Promise vs delivery tracker (AR-guidance-vs-results-delivery, in place of cross-quarter transcript comparison)

| Promised in | Promise | Outcome | Explanation |
|---|---|---|---|
| Implicit, from the regulatory record (GPCB 13-Nov-2024, Consent to Establish 10-Nov-2025 — both precede the FY26 AR) | Construction of Dahej Unit IV to follow once all approvals were in hand | ❌ **Missed** | AR FY26 (signed 12-Aug-2026): "the work at Unit IV, Dahej could not be started" — cause given only as "unforeseen circumstances," never named (AR p.18) |
| AR FY26 Chairman's Letter, p.18-19 | "New deadlines have been finalized": production start "coming two years," whole unit functional "coming three years" | **Partial / not yet testable** — the promise itself is unresolved and forward-dated 2-3 years past this AR; graded on the evidence AVAILABLE NOW, which is zero. Total company-wide CWIP is Rs 87.6 lakh (Note 3, AR p.100), up only Rs 11.6 lakh from Rs 76.0 lakh a year earlier, and none of it is identified as Dahej-attributable in the CWIP aging schedule. Capital commitments are stated as NIL (Note on Contingent Liabilities, AR p.109: "does not have any contingent liabilities and commitments (including capital commitments)... as at 31 March 2026"). A "finalized" multi-year construction restart with zero balance-sheet trace on the day it is announced is a credibility-impairing pattern, not a delivered promise | Same statement gives no capex figure, no output/capacity figure, no month, and does not explain why the prior timeline (implied by the 2022 land purchase and 2024-2025 approvals) slipped |
| AR FY26 Chairman's Letter, p.18 | Implicit: revenue "maintained... as compare to last year" amid a "difficult" year (tariff war, America-Iran conflict cited) | ✅ **Delivered** | Revenue from operations: Rs 10,122.00 lakh FY26 vs Rs 10,019.39/10,018.4 lakh FY25 (+1.03%, Board's Report p.36-37, results filing 4c8de5ae p.2); Total income +3.6%. A low bar, but met |
| AR FY26 Board's Report, p.36-37 / Dividend Distribution Policy | Recommend final dividend consistent with stated policy | ✅ **Delivered** | Rs 0.50/share (5%) recommended for FY26, matching the Rs 0.50/share (5%) actually paid during FY26 for FY25 (Note, AR p.105); payout unchanged year-on-year at Rs 185.40 lakh despite the growth stall |

**Tally: 2 delivered, 1 partial (unresolved, zero-corroboration), 1 missed.**

### 2B. Excuse pattern analysis

Only one excuse instance exists in this source set: the Dahej construction delay, attributed to "unforeseen circumstances" (AR p.18), given no elaboration anywhere in the Chairman's Letter, Board's Report, or MD&A. The same paragraph structure places this excuse directly after a passage blaming the year's difficulty on "tariff war from America" and "the war between American and Iran" — an implicit external-attribution frame, even though the company never explicitly links the Dahej delay to those named macro events. There is no instance anywhere in the document set of management saying "we made a mistake" or naming an internal cause (funding, contractor, land-title, internal capital-allocation choice). Classification: **deflection bordering on external-blame** — a named external "difficult year" narrative sits beside an unnamed internal delay, and the reader is left to infer a connection the company never states outright. `excuse_pattern: external-blame-heavy` (see YAML).

### 2C. Tone ratings (1-5, with evidence)

| Dimension | Rating | Evidence |
|---|---|---|
| Transparency | 2/5 | Zero capex figure for Dahej Unit IV, ever, in this AR — not even the amount already spent on land or approvals. R&D disclosure is a single boilerplate sentence with no rupee figure (AR p.34/38: "incurred legitimate expenses on Research & Development... during the year"). |
| Specificity | 2/5 | "Coming two years," "coming three years" — no month, no quarter, no capex rupee number, no capacity/tonnage figure for the new unit. |
| Consistency | 3/5 | Dividend policy held steady (5%/Rs 0.50 per share) year-on-year; cannot be scored higher because only one AR is held, so cross-year consistency of the Dahej narrative itself cannot be tested from primary text. |
| Accountability | 2/5 | The Chairman does name the delay directly rather than omitting it ("the work at Unit IV, Dahej could not be started"), which is a point in favour — but gives no reason beyond "unforeseen circumstances," and the new multi-year promise is issued in the same breath with no capital backing shown. |
| Defensiveness | 3/5 | Not overtly defensive in tone (no pushback language exists since there is no Q&A), but the MD&A never frames the Dahej delay as a company-specific risk factor anywhere outside the one Chairman's-letter paragraph — a passive, non-defensive silence rather than active deflection. |
| Over-promotion | 3/5 | Standard promotional framing ("1.7 decades," "leading manufacturer," "world class technological adaptations") but not egregious; the MD&A's page and a half of generic global-GDP commentary (p.58-60) reads as filler rather than active over-promotion of the company's own prospects. |

### 2D. What they are NOT saying

- **No capex rupee figure for Dahej Unit IV, ever** — not the amount already spent, not the amount required to complete it, despite claiming environmental clearances are fully in hand and deadlines "finalized" (AR p.18-19; corroborated by CWIP Rs 87.6 lakh company-wide and capital commitments NIL, AR p.100 and p.109).
- **No explanation of "unforeseen circumstances."** A one-line phrase covers what is, per COMPANY MEMORY, a multi-year slip from a 2022 land purchase through 2024-2025 regulatory approvals to still-unstarted construction as of Aug-2026.
- **No declining-ROCE discussion.** ROCE fell from 49.46% (FY23) to 43.15% (FY24) to 38.03% (FY25) to 32.22% (FY26) — a 17-point decline over four years (AR p.11, "Financial Snapshot") — and is never mentioned, explained, or contextualised anywhere in the MD&A or Board's Report, even as cash and fixed-deposit balances grew (Other Financial Assets with >12-month maturity: Rs 1,864.3 lakh FY26 vs Rs 648.1 lakh FY25, Note 5, AR p.99).
- **No sector-specific market intelligence.** The MD&A (p.58-60) is two and a half pages of generic global and India macro-economic commentary (world GDP growth, India's GDP world-ranking, EMDE positioning) with zero mention of the specialty/high-purity fine chemicals industry's own growth rate, capacity additions, pricing environment, or import-export trend — the sector Kronox actually operates in.
- **No customer, product-line, or geographic breakdown** despite naming "about 185 products" across excipients, high purity reagents, pharma, nutraceutical and food chemical categories (AR p.19); no concentration disclosure, no named customers, no segment reporting beyond the single Ind AS 108 operating segment (Note 32, AR p.107).
- **No mention of the Indo Borax control acquisition** in either results filing (FY26 audited results, 21-May-2026; Q1 FY27, 12-Aug-2026) — consistent with the SPA/open-offer disclosures dating from 20-Aug-2026, after both filings, so this is a timing fact rather than an omission finding.

### 2E. Repeated question tracker

**NOT APPLICABLE — NO-CONCALL MODE.** No analyst Q&A transcript exists for this company; there is no source against which a repeated-question pattern can be tested. `NO REPEATED UNANSWERED QUESTIONS FOUND` (vacuously true: no questions exist in this source set to have been evaded).

---

## SECTION 3: COMPETITIVE INTELLIGENCE (from AR + results only)

### 3A. What management says about competitors

**NOT DISCLOSED.** No competitor is named anywhere in the AR, the Chairman's Letter, the Board's Report, or either results filing.

### 3B. Industry and market intelligence

The MD&A (AR p.58-60) contains only generic macro-economic content: global GDP growth 3.1% (2026)/3.2% (2027), India GDP growth 6.4-6.5%, India's nominal-GDP world ranking (6th, ~$4.15 trillion) and PPP ranking (3rd, ~$18.9 trillion), EMDE positioning commentary, and Middle East geopolitical-risk narrative. **None of it is specific to the high-purity specialty fine chemicals sector**: no sector growth rate, no raw-material cost trend, no capacity-addition data, no pricing-environment commentary, no import-export trend for the company's own product categories. This absence is itself the finding, and is the basis for peer_questions #1 and #3 below (Section 4B).

### 3C. Toughest analyst questions

**NOT APPLICABLE — NO-CONCALL MODE.** No Q&A source exists.

### 3D. Customer and order book signals

- Export mix rising: 24.75% (FY24) -> 26.57% (FY25) -> 32.39% (FY26) of revenue (AR p.11, "Financial Snapshot"), with zero commentary on which geography or customer segment drove the increase.
- No customer wins, losses, concentration change, renewal, or pricing-renegotiation disclosure anywhere in the source set.
- Single reportable operating segment (manufacturing of High Purity Specialty Fine Chemicals) per Ind AS 108, Note 32 (AR p.107) — no product-line or geography segmentation is disclosed beyond the aggregate export percentage.

---

## SECTION 4: KEY TAKEAWAYS & TRIGGERS SUMMARY

### 4A. Investment-ready trigger list (ranked)

| Priority | Trigger | Type | Timeframe | Conviction | Confirms it | Kills it |
|---|---|---|---|---|---|---|
| 1 | Dahej Unit IV restart ("finalized" 2y/3y deadlines) | VOLUME | Long (2-3y) | L | CWIP step-up tied to Dahej in FY27/FY28 AR notes, a capital-commitment disclosure, or a Reg-30 capex filing naming Dahej spend | FY27 AR repeats "unforeseen circumstances" with a further deadline reset, or capital commitments remain NIL through FY28 |
| 2 | Q1 FY27 revenue/PAT re-acceleration | VOLUME | Near (1 quarter) | M | Q2/Q3 FY27 results sustain double-digit revenue and PAT growth | Growth reverts to FY26's ~1% pattern in Q2 FY27 |
| 3 | Rising export mix (24.75% to 32.39% over 3 years) | PRICE-MIX | Near-medium | M | Export % of revenue stays above 30% in FY27 | Reverts below the FY25 level of ~27% |

### 4B. Questions for peer verification (handoff to stage 6)

- **Q1**: What growth rate does the specialty/high-purity fine chemicals sector cite for FY26-27, and does it corroborate or contradict Kronox's own near-flat FY26 revenue growth (+1.03%)? **Why it matters**: Kronox's own MD&A gives zero sector-specific data; peer commentary is the only way to test whether Kronox underperformed a growing sector or the sector itself stalled. **Check peers**: DMCC, NEOGEN, TANFACIND.
- **Q2**: Do peer managements disclose brownfield/greenfield capex timelines with rupee figures, capacity numbers, and commissioning quarters, or is undated/uncosted capex guidance (as Kronox gives for Dahej Unit IV) normal disclosure practice in this peer set? **Why it matters**: benchmarks whether Kronox's zero-specificity capex promise is a sector norm or a company-specific red flag. **Check peers**: DMCC, NEOGEN, TANFACIND, INDOBORAX.
- **Q3**: Do peer concalls discuss the tariff-war/geopolitical raw-material or demand impact that Kronox's Chairman cites as making FY26 "difficult"? **Why it matters**: tests whether this is a real, sector-wide headwind (validating the implicit excuse) or a Kronox-specific narrative used to frame a 1.03% growth year as acceptable. **Check peers**: DMCC, NEOGEN, TANFACIND.
- **Q4**: Do any peer concalls name Kronox (market share, competitive dynamics, customer overlap)? **Why it matters**: Kronox discloses zero competitor names or market-share claims of its own; peer commentary may be the only external check on its competitive position. **Check peers**: DMCC, NEOGEN, TANFACIND, INDOBORAX.
- **Q5**: Does Indo Borax's own public commentary (as Kronox's new controlling shareholder from Aug-2026) say anything about the Dahej Unit IV plan or capital-allocation priorities that differs from Kronox's own AR framing? **Why it matters**: Indo Borax now controls Kronox; its forward commentary may be the closest available proxy for real guidance since Kronox itself gives none. **Check peers**: INDOBORAX.

### 4C. Management quality verdict table

| Criterion | Verdict |
|---|---|
| Promise-delivery record | 2 delivered (low-bar dividend/revenue statements), 1 missed (clearances-to-construction gap), 1 unresolved with zero corroboration (the new Dahej deadline) |
| Specificity of forward guidance | Very low: no capex figure, no capacity figure, no dated milestone anywhere in the AR or either results filing |
| Transparency on the central binary (Dahej Unit IV) | Low: delay acknowledged in one sentence, cause never named, new promise issued with zero balance-sheet backing in the same document |
| Silence on adverse trends | Material: 17-point ROCE decline (FY23-FY26) never discussed |
| Boilerplate risk | High: MD&A is macro filler unconnected to the company's own sector; R&D and technology-absorption disclosures are single-sentence boilerplate |
| **Overall grade** | **C** |

### 4D. Concall red flags

| Flag | Severity |
|---|---|
| Dahej Unit IV "finalized" new deadlines (2y production, 3y full functionality) carry zero corroborating capex, CWIP, or capital-commitment trail in the same AR (CWIP Rs 87.6 lakh company-wide, capital commitments NIL, AR p.100 and p.109) | HIGH |
| Multi-year gap between Unit IV land purchase (2022) and construction start (still not begun as of the 12-Aug-2026 AR signing date), through two named regulatory-clearance milestones (GPCB, Consent to Establish), with the delay cause never specified beyond "unforeseen circumstances" | MEDIUM |
| ROCE decline from 49.46% (FY23) to 32.22% (FY26), never discussed anywhere in the MD&A or Board's Report, alongside a growing fixed-deposit balance (Rs 1,864.3 lakh >12-month maturity, FY26) | MEDIUM |
| MD&A contains no sector-specific content: no specialty/fine-chemicals industry growth rate, capacity, pricing, or competitive intelligence — only generic global/India macro-economic filler | LOW |
| R&D and technology-absorption disclosures are single-sentence boilerplate with no rupee figure or project description | LOW |

---

## YAML BLOCK

```yaml
stage: B05-concall
company: "KRONOX"
run_date: "2026-08-30"
model: claude-sonnet-5
status: complete
no_concall_mode: true
input_gaps:
  - "No concall transcripts exist (concalls_available: false); Section 2E and 3A/3C have no source and are marked NOT APPLICABLE"
  - "AR FY24 and AR FY25 absent; Section 1C trigger-evolution cannot be built from primary cross-year AR comparison, only from single-AR internal chronology plus COMPANY MEMORY dates"
flags:
  - "Dahej Unit IV 'finalized' 2y/3y deadlines carry zero corroborating capex/CWIP/capital-commitment trail in the same AR (HIGH)"
  - "17-point ROCE decline FY23-FY26 never discussed in MD&A or Board's Report (MEDIUM)"
quarters_analysed: []          # no concalls; documents used were AR FY26 (Chairman's Letter p.18-19,
                                # Board's Report p.36-38, MD&A p.58-60), FY26 audited results
                                # (21-May-2026), and Q1 FY27 results (12-Aug-2026)
triggers:
  - {priority: 1, name: "Dahej Unit IV restart, finalized 2y/3y deadlines", type: "VOLUME", timeframe: "long (2-3y)", conviction: "L",
     confirm_signal: "CWIP step-up tied to Dahej in FY27/FY28 AR notes, a capital-commitment disclosure, or a Reg-30 capex filing naming Dahej spend",
     kill_signal: "FY27 AR repeats 'unforeseen circumstances' with a further deadline reset, or capital commitments remain NIL through FY28"}
  - {priority: 2, name: "Q1 FY27 revenue/PAT re-acceleration", type: "VOLUME", timeframe: "near (1 quarter)", conviction: "M",
     confirm_signal: "Q2/Q3 FY27 results sustain double-digit revenue and PAT growth",
     kill_signal: "growth reverts to FY26's ~1% pattern in Q2 FY27"}
  - {priority: 3, name: "Rising export mix (24.75% to 32.39% over FY24-FY26)", type: "PRICE-MIX", timeframe: "near-medium", conviction: "M",
     confirm_signal: "export % of revenue stays above 30% in FY27",
     kill_signal: "reverts below the FY25 level of ~27%"}
guidance:
  - {item: "Dahej Unit IV production start", number: "NOT FOUND (no capex/capacity figure given)", timeframe: "~2 years from AR FY26 date (~FY28)", stated_in: "AR FY26 Chairman's Letter, p.18-19"}
  - {item: "Dahej Unit IV full functionality", number: "NOT FOUND", timeframe: "~3 years from AR FY26 date (~FY29)", stated_in: "AR FY26 Chairman's Letter, p.18-19"}
  - {item: "Final dividend FY26", number: "Rs 0.50/share (5% of Rs 10 face value); Rs 185.40 lakh total", timeframe: "payable on AGM approval 16-Sep-2026", stated_in: "AR FY26 Board's Report, p.36-37"}
  - {item: "Implicit revenue expectation", number: "qualitative only: 'maintained' revenue vs prior year", timeframe: "FY26", stated_in: "AR FY26 Chairman's Letter, p.18"}
promise_delivery:
  delivered: 2
  partial: 1
  missed: 1
  rows:
    - {promised_in: "Regulatory record (GPCB 13-Nov-2024, Consent to Establish 10-Nov-2025), implicit", promise: "Dahej Unit IV construction to follow completed approvals", outcome: "Missed", explanation: "AR FY26 (signed 12-Aug-2026): 'the work at Unit IV, Dahej could not be started' due to unnamed 'unforeseen circumstances' (AR p.18)"}
    - {promised_in: "AR FY26 Chairman's Letter, p.18-19", promise: "'New deadlines have been finalized': production start ~2 years, full unit functional ~3 years", outcome: "Partial / unresolved", explanation: "Zero corroborating capex, CWIP, or capital-commitment trail in the same AR: CWIP Rs 87.6 lakh company-wide (Note 3, p.100), capital commitments stated NIL (p.109)"}
    - {promised_in: "AR FY26 Chairman's Letter, p.18", promise: "Implicit: revenue maintained vs prior year despite a difficult macro year", outcome: "Delivered", explanation: "Revenue from operations +1.03% (Rs 10,122.00 lakh vs Rs 10,019.39 lakh FY25); total income +3.6% (Board's Report p.36-37)"}
    - {promised_in: "AR FY26 Board's Report, p.36-37", promise: "Dividend consistent with stated policy", outcome: "Delivered", explanation: "Rs 0.50/share (5%) recommended for FY26, matching the Rs 0.50/share actually paid during FY26 for FY25 (AR p.105); payout unchanged at Rs 185.40 lakh"}
excuse_pattern: "external-blame-heavy"
repeated_evasions: []          # NO REPEATED UNANSWERED QUESTIONS FOUND — no concall Q&A source exists (NOT APPLICABLE, NO-CONCALL MODE)
credibility_grade: "C"
credibility_basis: "Two low-bar promises (flat revenue framing, unchanged dividend) delivered; the single load-bearing promise (Dahej Unit IV) shows a documented miss (clearances-to-construction gap) and its restated 2y/3y deadline carries zero capex/CWIP/capital-commitment corroboration in the same AR, so the grade stays at the NO-CONCALL-MODE default and does not rise to B"
peer_questions:
  - {question: "What growth rate does the specialty/high-purity fine chemicals sector cite for FY26-27, and does it corroborate or contradict Kronox's own near-flat FY26 revenue growth (+1.03%)?", why: "Kronox's own MD&A gives zero sector-specific data; peer commentary is the only way to test underperformance vs a sector-wide stall", check_peers: ["DMCC", "NEOGEN", "TANFACIND"]}
  - {question: "Do peer managements disclose capex timelines with rupee figures, capacity numbers, and commissioning quarters, or is undated/uncosted capex guidance a sector norm?", why: "benchmarks whether Kronox's zero-specificity Dahej promise is a sector norm or a company-specific red flag", check_peers: ["DMCC", "NEOGEN", "TANFACIND", "INDOBORAX"]}
  - {question: "Do peer concalls discuss the tariff-war/geopolitical impact Kronox's Chairman cites as making FY26 difficult?", why: "tests whether the implicit external-blame framing is a real sector-wide headwind or a company-specific narrative", check_peers: ["DMCC", "NEOGEN", "TANFACIND"]}
  - {question: "Do any peer concalls name Kronox (market share, competitive dynamics, customer overlap)?", why: "Kronox discloses zero competitor names or market-share claims of its own", check_peers: ["DMCC", "NEOGEN", "TANFACIND", "INDOBORAX"]}
  - {question: "Does Indo Borax's own public commentary (new controlling shareholder, Aug-2026) say anything about the Dahej Unit IV plan or capital-allocation priorities that differs from Kronox's own AR framing?", why: "Indo Borax now controls Kronox; its commentary may be the closest available proxy for real forward guidance", check_peers: ["INDOBORAX"]}
red_flags:
  - {flag: "Dahej Unit IV 'finalized' new deadlines carry zero corroborating capex/CWIP/capital-commitment trail in the same AR", severity: "HIGH"}
  - {flag: "Multi-year gap between Unit IV land purchase (2022) and construction start (still not begun as of 12-Aug-2026), delay cause never specified beyond 'unforeseen circumstances'", severity: "MEDIUM"}
  - {flag: "ROCE decline from 49.46% (FY23) to 32.22% (FY26) never discussed in MD&A or Board's Report, alongside a growing fixed-deposit balance", severity: "MEDIUM"}
  - {flag: "MD&A contains no sector-specific content, only generic global/India macro-economic filler", severity: "LOW"}
  - {flag: "R&D and technology-absorption disclosures are single-sentence boilerplate with no rupee figure or project description", severity: "LOW"}
dropped_triggers: []           # single AR held; no cross-year AR text exists to test for a dropped trigger
timeline_slippages:
  - "Dahej Unit IV: land acquired 2022 (AR milestones, p.4-5); GPCB approval 13-Nov-2024; Consent to Establish 10-Nov-2025 (both COMPANY MEMORY / B00 load-bearing facts, not dated inside the AR text); construction still not started as of the AR FY26 signing date (12-Aug-2026, AR p.77); deadlines reset in the same AR to '2 years to production, 3 years to full functionality,' cause of the prior slip named only as 'unforeseen circumstances' (AR p.18)"
analyst_note: "The single testable retrospective promise (clearances should lead to construction) was missed; the only forward promise (new 2y/3y deadlines) is untestable today and carries no balance-sheet backing on the day it was made. Grade C reflects a company that meets low-bar commitments (dividend, flat revenue) but has never put a number behind its one growth catalyst. Q1 FY27 (+13.4% revenue, +38.5% PAT YoY, results 03380acb p.3) is a genuine post-FY26 acceleration but arrives with zero management commentary explaining the driver, since no MD&A accompanies interim filings. The Indo Borax control acquisition (Aug-2026, per COMPANY MEMORY) postdates both results filings in this stage's scope and is not sourced here; stage 6/8 should carry it forward."
```
