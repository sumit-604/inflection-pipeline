# A3 FORENSIC NOTES — ECOS (INDIA) MOBILITY & HOSPITALITY LTD
## Q1 FY27 (quarter ended 30 June 2026) | DOCTYPE: PRESENTATION (press release + investor deck) — NEW DOCS
### F1–F17 forensic checklist | Model claude-opus-4-8 | BSE 544239 / NSE ECOSMOBLTY | Docs dated 11 Aug 2026

---

## RECONCILIATION PREAMBLE (contractual, before F1)

**Ledger reconciled 100%.** The A2 combined ledger carries **257 discrete units** (47 press-release + 210 presentation rows across 28 slides). Every row was read at its cited line in the two A1 extracts before judging. Count-test `gate_a2: pass` (24 categories matched). No ledger row left unread.

**Figure authority.** The deck is a graphical/infographic PDF; A1 flagged OCR corruption on chart/table pages (7–11, 13, 15, 19, 20, 22, 25). Per orchestrator rule, all chart/table values are taken from `verified_supplement_deck_pressrelease.md` (vision-verified off the primary PDF), with individual anchors to the A1 extract line. Units: **₹ million; ×0.1 = ₹ Crore** (except deck page 13 industry TAM = INR Bn, not used in forensics).

**Doctype applicability (per instruction file L128–131).** Presentation → **F16 is ACTIVE and central**; F6/F7/F10/F11 apply to the numbers the deck carries; the deck uniquely carries a **FY26 consolidated balance sheet (page 10)**, a **consolidated income statement (page 9)** and a **6-year history (page 11)**, so F8 (tax/DTA) and balance-sheet-derived tripwire checks are live here even though they were N.A. on the Q1 results filing. **F2/F3 are N.A.** — neither new document discloses standalone figures (both present consolidated only). **F4/F5/F9/F15 N.A.** — no auditor report, no OCI statement, no consolidation entity-list in either doc. **F17 N.A.** — no transcript (no concall); the Notion-tripwire cross-reference is folded in explicitly below.

**Consistency with the completed results review (Step 6C).** The pre-committed thesis-break trigger (consolidated REPORTED EBITDA margin sub-12% for 3 consecutive quarters) is **MEASURE-CONDITIONAL — NOT formally fired** (Q4 FY26 reported 13.43% resets any run; Q1 FY27 a single borderline quarter). These forensics do NOT re-open that verdict; they assess only the NEW docs and stay consistent with it. Decision Status remains WATCHLIST / HOLD-NOT-ADD; nothing here asserts AVOID.

---

## FINDINGS TABLE

| id | check | ledger row ref | line / slide | short verbatim quote | classification | forward implication |
|----|-------|----------------|--------------|----------------------|----------------|---------------------|
| **F1-01** | F1 | #76, #99, #100, #61–62 | deck p10 L293 (intangibles), L326 (NCI), L331 (borrowings) | "Intangible assets \| (blank) \| (blank)"; "Non-controlling interest \| 1.35 \| —" | **AMBIGUOUS** | Company touts a "major upgrade to proprietary in-house technology platform" and "new technology for CCR" yet carries **zero capitalised intangibles** (only ₹22.44 Mn intangibles-under-development); tech spend appears expensed → a drag on the very margins under pressure. NCI newly at ₹1.35 Mn confirms a non-wholly-owned subsidiary in the group (ties results F15-02, Consulttrans). Non-current borrowings deleveraged to nil (₹1.08 Mn → —). |
| **F6-01** | F6 | #42, #43, #44, #20–23, #238–243 | PR L94–95, L164–171; deck p6 L183–184, p27 L731–736 | "the launch of our new technology for CCR"; "further progress in our SIXT partnership"; "Board … has recommended a final dividend of ₹2.38 per equity share for FY26, subject to approval" | **FORWARD-SIGNAL** | Dateable management commitments → Commitment Register below. SIXT India-GSA (exclusive) is a new inbound/leisure channel beyond core B2B; CCR tech platform launched (completed); leadership-bandwidth "investment ahead of the next phase of growth" signals **more overhead ahead = continued margin pressure**; dividend + AGM = FY26 AR imminent. |
| **F7-01** | F7 | #17, #33 | PR L90; deck p6 L179 | "While margins during the quarter reflected changes in business mix and the operating cost environment" | **FORWARD-SIGNAL** | Newly-added, pre-emptive, unquantified margin hedge in the CMD quote — no recovery path, no dated crossover. Pre-emptive cover of the kind that tells you **Q2 margins remain under pressure**. Paired with the written omission of the 13–15% band (F16-01). |
| **F8-01** | F8 | #70, #82 | deck p9 L269 (tax); p10 L300 (DTA) | "Tax Expense \| 46.14 \| 53.81"; "Deferred tax assets (net) \| 64.98 \| 27.85" | **AMBIGUOUS** | Consolidated ETR fell **28.82% → 24.08% YoY** (below statutory 25.17%), flattering the +9.5% PAT while core operating profit fell ~2.4% (results Step 4). Deck balance sheet (NEW disclosure vs the results filing) shows **DTA net more than doubled, ₹27.85 → ₹64.98 Mn (+133%)** — a persistent DTA build = future ETR step-up risk, and a question of what recognised ₹3.7 Cr of DTA (relevant to the Sec 153C tripwire). No "tax relating to earlier years" line. |
| **F13-01** | F13 | #44 | PR L170–171 | "recommended a final dividend of ₹2.38 per equity share for FY26, subject to approval of the shareholders at the upcoming Annual General Meeting" | **FORWARD-SIGNAL** | FY26 final dividend + upcoming AGM ⇒ **FY26 Annual Report drops within weeks → schedule Role 6 AR Deep Dive.** The AR is the event that resolves the four still-open tripwires (provisions, debtor days, Sec 153C CL, cash conversion). Deck disclaimer L124–125 ("based on … Annual Reports") corroborates AR availability. Ties results F13-03. |
| **F14-01** | F14 | #26/#65, #29/#72, #113, #56, #217 | PR L113 vs deck p9 L264; PR L117 vs deck p9 L271; deck p10 L317 vs L348; deck p8 L240; deck p22 L396 | "EBITDA … 218.47 \| 219.18" (PR) vs "218.47 \| 218.55" (deck); "Total assets 4,134.93 / 3,414.02" vs "Total equity and liabilities 4,134.93 / 3,414.20" | **BENIGN** | Multiple drafting inconsistencies across two same-day IR documents, all immaterial and all confined to **comparative-period cells** — see "A2-flag run-down" below. Current-quarter Q1FY27 figures are identical across both docs and tie to the results filing + supplement. Cumulatively a mild governance-hygiene / drafting-control data point, not a red flag. |
| **F16-01** | F16 | #238–243; supplement §F | deck p27 L729–736 | "Way Ahead: Increasing wallet share … Strengthen on: technology and talent pool" | **FORWARD-SIGNAL** | **NO QUANTIFIED GUIDANCE.** The deck omits, in writing, the analyst-corroborated **13–15% EBITDA / 8.5–10% PAT bands** and the **FY28 ₹1,000–1,200 Cr revenue inflection**; "Way Ahead" is entirely qualitative. In the quarter margins hit 10.34% (lowest on record), the refusal to put a number on the recovery is itself a bearish signal / hedge. |
| **F16-02** | F16 | #13/#18, #116, #119, #115, #117 | PR L87/L91, deck p6 L176/L180 vs deck p11 L372, L380 | "improving operating efficiency as we scale" vs "EBITDA Margin (%): FY23 16.5% … FY26 11.6%"; "ROCE: FY24 42.9% … FY26 29.4%" | **AMBIGUOUS** (Role-5 core; leaning bear) | **Narrative-vs-numbers gap adjudicated:** growth claims (revenue +16.7%, trips +27%, clients +18%) are corroborated and real; the **margin/efficiency claims are contradicted by the company's OWN 6-year chart** — EBITDA margin 16.5%(FY23)→11.6%(FY26)→10.34%(Q1FY27), absolute EBITDA flat ₹900/924/939 Mn FY24–26, ROCE 42.9%→29.4%, ROE 42.8%→23.7%. "Improving operating efficiency" is not visible anywhere in the disclosed trend. Management framing runs ahead of results. |
| **F16-03** | F16 | #35, #31 | PR L141 (trips) vs L128 (revenue) | "~1.48 million trips … a growth of ~27% YoY"; "Revenue from Operations … a YoY growth of 16.70%" | **FORWARD-SIGNAL** | Trips +27% vs revenue-from-ops +16.7% ⇒ **revenue-per-trip down ~8% YoY** (₹1,554 → ₹1,428/trip). The mechanical driver of margin compression: realisation/mix is falling as volume is added. |
| **F16-04** | F16 | #35 | PR L141–142 | "ETS contributing 59% and CCR contributing 41% of revenue" | **AMBIGUOUS** | ETS (volume-heavy, lower-yield employee commute) at 59% vs CCR (premium chauffeured) 41% is the stated margin cause ("changes in business mix"). **But no prior-period ETS/CCR split is disclosed in either doc**, so the shift magnitude cannot be sized → generate a management question (what was the Q1FY26/FY26 mix, and target mix). Consistent with the revenue-per-trip drop (F16-03). |
| **F16-05** | F16 | #40, #235–237 | PR L155–156; deck p25 L709–710 | "Around 51% of revenue … for more than five years"; deck chart "FY25 3,806 (61%) … FY26 4,266 (55%)" | **AMBIGUOUS** | Long-standing (>5yr) customer revenue share **drifting down 61%(FY25) → 55%(FY26) → 51%(Q1FY27)** — stickiness/quality softening; newer clients growing faster than the legacy base, consistent with realisation-down. **Chart-framing note:** the deck plots the FY26 55% as the highlighted/boxed "latest year" and stops there; the further step-down to 51% appears only in press-release text, not on the deck chart. Absolute ₹Mn series (355→4,266) rises and visually reads as growth while the quality ratio has turned. |
| **F16-06** | F16 | #194–195, #146, #38 | deck p20 L601; deck p15 L469; PR L150–151 | "Q1 FY27 Vehicle Ownership Mix: Owned 5% \| Vendor Operated 95%"; "continuing to operate on an asset-light model" | **BENIGN** (confirmatory-positive) | The explicit **5% owned / 95% vendor** mix (and slide 15 "90%+ vendor") **REBUTS/mitigates the earlier "asset-light drift" concern** raised by the new Fleet Management WOS (results F15-01): no material owned-fleet drift is visible in the mix. Not fully closed — the WOS's own gross block/capex is not shown — but the disclosed mix says no drift. |

---

## CHECKLIST SCORECARD (all 17; no blanks)

| # | Check | Status | One-line basis |
|---|-------|--------|----------------|
| F1 | Zero-value standing line items | **FINDING** | 5 ZERO_STANDING rows read; intangibles blank vs tech narrative + NCI newly ₹1.35 Mn + non-current borrowings → nil (F1-01). |
| F2 | Standalone vs consolidated decomposition | **N.A.** | Neither new doc discloses standalone; deck p9/p10 and PR are consolidated only — no S-vs-C gap to compute. |
| F3 | Shell-entity detection | **N.A.** | Requires standalone-vs-consolidated cost lines; not available (consolidated-only docs). |
| F4 | Unaudited contribution ratio | **N.A.** | No auditor report / Other Matters paragraph in a press release or deck. |
| F5 | Going concern / EoM scope | **N.A.** | No auditor report or EoM language in either doc; no prior-quarter deck to diff. |
| F6 | Forward-commitment phrase mining | **FINDING** | CCR tech launch, SIXT partnership, dividend/AGM, leadership-bandwidth, Tier-II/III expansion — dated/dateable commitments (F6-01, register below). |
| F7 | Hedge phrase mining | **FINDING** | New pre-emptive margin hedge "changes in business mix and the operating cost environment," undated/unquantified (F7-01). |
| F8 | Tax forensics | **FINDING** | ETR 28.82%→24.08% YoY flatters PAT; DTA net +133% (₹27.85→64.98 Mn) = future ETR step-up risk (F8-01). |
| F9 | OCI forensics | **N.A.** | Deck income statement stops at PAT; no OCI/comprehensive-income statement in either doc. |
| F10 | Share count & dilution | **PASS** | Equity share capital ₹120.00 Mn unchanged FY25/FY26 (deck p10 L322) → 6.00 Cr shares; single EPS line 2.42, no dilutive instruments/corporate action. |
| F11 | Reserves & net-worth tie-out | **PASS** | Other equity 2,529.37 + share capital 120.00 = Total equity 2,649.36 (deck p10 L322–324), reconciles within ₹0.01 Mn rounding; ties results-filing consolidated other equity ₹252.937 Cr; net cash ~₹137.6 Cr confirmed. |
| F12 | Segment forensics | **N.A.** | Single reportable segment (Ind AS-108, results Note 4); no segment assets/liabilities disclosed. ETS/CCR revenue mix handled under F16-04, not a segment. |
| F13 | Board outcome beyond results | **FINDING** | FY26 final dividend ₹2.38/share + upcoming AGM ⇒ FY26 AR imminent → Role 6 AR Deep Dive (F13-01). |
| F14 | Note-drafting inconsistencies | **FINDING** | PR-vs-deck EBITDA & PAT-margin disagreements, FY25 BS cross-foot ₹0.18 Mn, PAT growth label 10.28%, awards 10-vs-9 — all benign (F14-01). |
| F15 | Entity-list diffs | **N.A.** | No consolidation entity-list in deck or PR; no prior-quarter deck baseline. NCI appearance noted under F1-01. |
| F16 | Presentation-specific: dropped/reframed disclosures | **FINDING** | No quantified guidance; narrative-vs-numbers; trips-vs-revenue realisation; ETS/CCR mix; long-standing-customer drift; asset-light rebuttal (F16-01…06). |
| F17 | Concall silence audit | **N.A.** | No transcript. Notion-tripwire cross-reference folded into the Tripwire Reconciliation below. |

**PASS: 2 (F10, F11) · FINDING: 6 (F1, F6, F7, F8, F13, F14, F16 — 7 checks) · N.A.: 8 (F2, F3, F4, F5, F9, F12, F15, F17).** No check blank → **GATE A3: PASS.**

*(Count note: FINDING checks = F1, F6, F7, F8, F13, F14, F16 = 7; PASS = 2; N.A. = 8; total 17.)*

---

## COMMITMENT REGISTER (from F6)

| commitment | implied / dated date | source ref | status word |
|-----------|----------------------|------------|-------------|
| New in-house technology platform for **CCR** launched | This quarter (Q1 FY27) | PR L94; deck p6 L183 | **completed** |
| Major upgrade to proprietary in-house technology platform "unveiled" | This quarter | PR L161–162 | **completed** |
| **SIXT India-GSA** partnership (exclusive) — "further progress", "early traction" | Ongoing; no dated milestone | PR L95, L164–165; deck p6 L184 | **underway** |
| FY26 final dividend **₹2.38/share** — recommended, pending AGM approval | Record date 18 Aug 2026; payment post-AGM (AGM ~21 Sep 2026 per prior work) | PR L170–171 | **initiated** (board-recommended) |
| Leadership bandwidth strengthened "ahead of the next phase of growth" | This quarter (cost already incurring) | PR L167–168 | **underway** (cost signal) |
| Expansion into **Tier-II/III cities + new geographies** | Ongoing (+20 cities this quarter → 151) | PR L98–99, L147; deck p27 L733 | **underway** |
| Increasing wallet share from existing customers; expand skilled sales team | Undated | deck p27 L731–732 | **initiated** |

---

## MANAGEMENT-CREDIBILITY SUBSECTION (narrative vs numbers — for A4 Role 5)

**Verdict: management framing runs ahead of the numbers on margin/efficiency; growth claims are corroborated; transparency of operational disclosure is GOOD (no number-hiding). The gap is interpretive, not evidentiary — but it is the central Role-5 item.**

| CMD claim (PR L87–92 / deck p6) | Company's own disclosed number | Adjudication |
|--------------------------------|--------------------------------|--------------|
| "healthy operating momentum" | Rev-from-ops +16.7%, trips +27%, clients +18% | **Corroborated** (top-line real). |
| "disciplined **profitable** growth" | Reported PAT +9.5% **but ~130% of it non-operating** (other income + lower tax); core operating PBT ex-OI −2.4% YoY (results Step 4) | **Not corroborated** — growth is profitless at the operating line. |
| "**improving operating efficiency** as we scale" | Deck p11: EBITDA margin 16.5%(FY23)→11.6%(FY26)→**10.34%**(Q1FY27); absolute EBITDA flat ₹900/924/939 Mn FY24–26; ROCE 42.9%→29.4%; ROE 42.8%→23.7% | **Contradicted by the company's own 6-year chart** — efficiency is deteriorating, not improving. |
| margin decline = "changes in business mix and the operating cost environment" | ETS 59% / CCR 41%; revenue/trip −8%; no prior mix given; no quantified recovery path | **Euphemistic + unquantified** — a pre-emptive hedge (F7-01); no crossover date. |
| "next phase of growth" / "strengthen technology" | Leadership bandwidth added ("deliberate investment"); no capitalised intangibles | **Signals more overhead** ahead → further near-term margin pressure. |

**Disclosure-quality credit:** the deck is thorough — full FY26 balance sheet, 6-year history, city mix, 5/95 ownership mix, trip count, long-standing-customer series. It **openly discloses the realisation drop** (trips +27% vs revenue +16.7%) and its own margin erosion. There are **no red-flag omissions and no number games** (every Q1FY27 figure ties to the results filing). The single presentation choice worth naming: the deck's long-standing-customer chart stops at FY26 55% and the further slip to 51% appears only in the press-release text (F16-05); and the 6-year chart is titled "Healthy Performance" over a period showing 5 points of margin erosion. Role-5 read: **framing optimism, not disclosure evasion.**

---

## UPDATED TRIPWIRE RECONCILIATION (Notion monitoring checklist × NEW docs)

The deck's FY26 balance sheet (page 10) and KPIs let several tripwires that were UNKNOWN on the Q1 results filing now be **resolved on an FY26 year-end basis**.

| # | Tripwire | Prior status (results review) | NEW-doc reading | Updated status |
|---|----------|-------------------------------|-----------------|----------------|
| 1 | EBITDA margin (the whole thesis) | AMBER — soft; 3-qtr reported break NOT met | Deck 6-yr chart company-confirms structural decline; Q1FY27 operating 10.34% (lowest), reported ~12.1% | **AMBER (unchanged)** — literal 3-quarter reported break still NOT met; compression now visible in the company's own chart. |
| 2 | Fresh provision >₹3 Cr | UNKNOWN (no notes at Q1) | Total provisions FY26 ₹9.44 Cr (73.19+21.17 Mn) vs FY25 ₹7.46 Cr (55.54+19.03 Mn) = **+₹1.98 Cr** | **RESOLVES → BENIGN** — under the ₹3 Cr trigger (FY26 basis). |
| 3 | Debtor days >60 | UNKNOWN | Trade receivables ₹107.02 Cr ÷ FY26 rev-from-ops ₹808.16 Cr × 365 = **~48 days** | **RESOLVES → AMBER-benign** — below 60-day red, above <45 green (FY26 basis; Q1 ageing still undisclosed). |
| 4 | Top-10 client concentration / loss | UNKNOWN | Deck discloses **city** mix (top-3 cities ~51%), not **client** concentration; client base ~1,400 (+18%), +61 new, 70+ F500 / 75+ BSE500 → breadth intact, no loss signal | **UNKNOWN (client)** — client concentration still not disclosed; no loss evidence. |
| 5 | Sec 153C IT dispute movement | AMBER (no P&L hit) | No contingent-liability schedule in deck/PR; DTA net +₹3.7 Cr and provisions +₹1.98 Cr disclosed but not attributed to 153C | **UNKNOWN** — resolves at FY26 AR CL schedule. |
| 6 | Cash conversion (CFO/PAT) | UNKNOWN / INDETERMINATE | Deck carries **NO cash-flow statement** | **INDETERMINATE (unchanged)** — does not resolve silently; resolves at FY26 AR / Q2 half-yearly. |
| 7 | Revenue inflection → FY28 ₹1,000–1,200 Cr | AMBER | Q1FY27 annualised ~₹845 Cr; FY26 ₹808 Cr; growing below pace; **deck omits the FY28 target in writing** | **AMBER (unchanged)** — growth without margin; target dropped from written guidance (F16-01). |
| — | Near-zero leverage (Notion assumption) | Implied | Net cash **~₹137.6 Cr ex-lease** FY26 (cash 241.88 + bank 69.86 + inv 1,060.79 + 4.26 − borrowings 1.07 Mn); PR ₹1,558 Mn (₹155.8 Cr) by 30-Jun-26; non-current borrowings → nil | **CONFIRMED** — near-zero leverage validated; balance-sheet strength is the clean part of the story. |

**Net:** the deck **resolves tripwires 2 and 3** (both to benign/amber-benign on FY26 basis) and **confirms near-zero leverage**; tripwires 1 and 7 stay AMBER; 4 and 5 stay UNKNOWN pending the FY26 AR; **6 stays INDETERMINATE** (no cash-flow statement — must not resolve silently to PROCEED).

---

## A2-FLAG RUN-DOWN (benign vs substantive)

| A2 flag | Location | Run-down | Verdict |
|---------|----------|----------|---------|
| `SUPPLEMENT_DISAGREEMENT` (EBITDA) | PR L113 (219.18 / −0.32%) vs deck p9 L264 (218.55 / −0.03%) | The **deck** ties to the results filing (Q1FY26 op EBITDA ₹21.855 Cr = 218.55 Mn); the **PR** KFS figure 219.18 is the outlier. Prior-period comparative only; Q1FY27 EBITDA (218.47) identical in both. | **Benign** — PR transcription/label slip in a comparative cell. |
| `SUPPLEMENT_DISAGREEMENT` (PAT margin) | PR L117 (Q4FY26 7.48%) vs deck p9 L271 (7.22%) | 157.37 ÷ total income 2,103.78 = **7.48%** (PR correct); the **deck** appears to have copy-pasted the Q1FY26 column value 7.22%. Comparative cell only. | **Benign** — deck copy error; does not touch Q1FY27. |
| `SUPPLEMENT_DISAGREEMENT` (Total income YoY) | deck 16.92% vs PR 16.91% | Rounding of the same figure. | **Benign** — rounding. |
| `NUMBER_DISCREPANCY` | deck p10 L317 (assets 3,414.02) vs L348 (equity+liab 3,414.20) | FY25 comparative column does not cross-foot by **₹0.18 Mn** (0.005% of a ₹341 Cr balance sheet) — a `02`↔`20` digit transposition. FY26 column balances exactly (4,134.93 = 4,134.93). | **Benign** — transcription typo in the FY25 comparative. |
| `GROWTH_LABEL_INCONSISTENCY` | deck p8 L240 (PAT +10.28%) | Bar label 10.28% is arithmetically wrong (146/133 = +9.77% rounded; +9.50% on unrounded 145.50/132.87). Authoritative table (deck p9, PR) shows +9.50%. Underlying figures correct everywhere. | **Benign** — mislabeled growth arrow on a rounded-bar chart. |
| `AWARDS_COUNT_MISMATCH` | deck p22 L396 (caption "10 items", 9 transcribed) | Slide caption says 10 awards; A1 extract captured 9. Most likely an **A1 extraction gap** (10th award not OCR-captured), not a company disclosure defect; non-financial. | **Benign** — extraction/count housekeeping, no forensic weight. |
| `DUPLICATE_ACROSS_DOCS` | PR L87–102 = deck p6 L176–190 | CMD quote identical verbatim across the two same-day documents (expected). | **Benign** — normal same-filing reuse. |
| `ZERO_STANDING` (5) | deck p9/p10 | See F1-01 — intangibles blank (interpretive), NCI/borrowings structural-confirmatory, purchase-of-stock/change-in-stock confirm a trading subsidiary in the group. | Mixed → **AMBIGUOUS** on intangibles; rest benign. |
| `NO_QUANTIFIED_GUIDANCE` | deck p27 | See F16-01. | **Substantive (forward-signal)** — the one flag that is NOT benign. |

**Overall:** every numeric disagreement is **benign** (rounding / comparative-cell transcription / copy error / chart-label), none affects the current-quarter reported figures, which are identical across both docs and tie to the results filing and supplement. The only **substantive** A2 flag is `NO_QUANTIFIED_GUIDANCE`, carried as F16-01.

---

## FORWARD-SIGNAL / AMBIGUOUS LIST (flagged for A4 → management questions)

**FORWARD-SIGNAL (5):**
- **F6-01** — SIXT India-GSA (new inbound/leisure channel beyond core B2B) + new CCR tech platform + leadership-bandwidth cost build. Commitment register seeded.
- **F7-01** — pre-emptive, unquantified margin hedge → Q2 margins likely still soft.
- **F13-01** — FY26 AR imminent (dividend/AGM) → schedule Role 6 AR Deep Dive; resolves 4 open tripwires.
- **F16-01** — no quantified guidance; 13–15% EBITDA band and FY28 inflection dropped from writing.
- **F16-03** — revenue-per-trip down ~8% (trips +27% vs revenue +16.7%); realisation/mix falling.

**AMBIGUOUS (5):**
- **F1-01** — zero capitalised intangibles vs "proprietary tech platform" narrative (expensed vs capitalised?); NCI newly present.
- **F8-01** — ETR drop flatters PAT; DTA +133% → future ETR step-up risk (and Sec 153C link).
- **F16-02** — narrative "improving operating efficiency" contradicted by the company's own 6-year margin/ROCE trend (Role-5 core).
- **F16-04** — ETS 59% / CCR 41% mix as margin cause, but no prior-period mix to size the shift.
- **F16-05** — long-standing-customer share drifting 61→55→51%; deck chart stops at FY26 55%, 51% only in PR text.

**BENIGN (2):** F14-01 (drafting inconsistencies, all comparative-cell); F16-06 (asset-light 5/95 mix rebuts drift concern — confirmatory-positive).

**Suggested A4 management questions (new-doc-specific, additive to the 8 already in the results review):**
1. What was the ETS/CCR revenue mix in Q1FY26 and FY26, and the target mix? (F16-04)
2. Is the "proprietary in-house technology platform / new CCR technology" capitalised or expensed — why are capitalised intangibles nil while ₹22.44 Mn sits in intangibles-under-development? (F1-01)
3. What drove the DTA build to ₹64.98 Mn (+133%), and is any of it linked to the Sec 153C matter? (F8-01)
4. SIXT India-GSA: what FY27–28 revenue and margin do you underwrite for the leisure/inbound channel vs the ~10% core? (F6-01)
5. Why does the deck omit the previously-guided 13–15% EBITDA band and the FY28 ₹1,000–1,200 Cr target, and in which quarter do you expect the margin crossover? (F16-01 / F7-01)

---

## GATE A3

**GATE A3: PASS.** All 17 checks carry exactly one status (2 PASS / 7 FINDING / 8 N.A.); no blanks. Ledger reconciled 100% (257/257 rows read at cited lines). 12 findings recorded, each with a line/slide cite and a short verbatim quote. Findings classified; FORWARD-SIGNAL (5) and AMBIGUOUS (5) flagged for A4. Consistent with the completed results-review Step 6C verdict (trigger MEASURE-CONDITIONAL, NOT fired; Decision Status WATCHLIST / HOLD-NOT-ADD; no AVOID asserted).

```yaml
stage: A3-forensics
company: "ECOSMOBILITY"
quarter: "Q1 FY27"
doctype: "presentation"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/ecosmobility-q1fy27/work/forensics_newdocs_ecosmobility_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: N.A.
  F10: PASS
  F11: PASS
  F12: N.A.
  F13: FINDING
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: N.A.
findings:
  - {id: "F1-01", check: "F1", line: "deck p10 L293/L326/L331", classification: "AMBIGUOUS", implication: "Zero capitalised intangibles vs proprietary-tech narrative (expensed?); NCI newly Rs1.35 Mn confirms non-WOS subsidiary; non-current borrowings to nil"}
  - {id: "F6-01", check: "F6", line: "PR L94-95/L164-171; deck p6 L183-184; p27 L731-736", classification: "FORWARD-SIGNAL", implication: "CCR tech launched; SIXT India-GSA new inbound/leisure channel; leadership-bandwidth cost build; dividend+AGM -> AR imminent"}
  - {id: "F7-01", check: "F7", line: "PR L90; deck p6 L179", classification: "FORWARD-SIGNAL", implication: "Pre-emptive unquantified margin hedge, no crossover date -> Q2 margins likely still soft"}
  - {id: "F8-01", check: "F8", line: "deck p9 L269; p10 L300", classification: "AMBIGUOUS", implication: "ETR 28.82->24.08% flatters PAT; DTA net +133% (27.85->64.98 Mn) = future ETR step-up risk; Sec 153C link"}
  - {id: "F13-01", check: "F13", line: "PR L170-171", classification: "FORWARD-SIGNAL", implication: "FY26 final dividend + AGM -> FY26 AR imminent -> Role 6 AR Deep Dive; resolves 4 open tripwires"}
  - {id: "F14-01", check: "F14", line: "PR L113 vs deck p9 L264; PR L117 vs deck p9 L271; deck p10 L317 vs L348; p8 L240; p22 L396", classification: "BENIGN", implication: "PR-vs-deck comparative-cell disagreements + BS cross-foot Rs0.18 Mn + mislabeled growth arrow + awards 10-vs-9; all immaterial, drafting-hygiene only"}
  - {id: "F16-01", check: "F16", line: "deck p27 L729-736", classification: "FORWARD-SIGNAL", implication: "No quantified guidance; 13-15% EBITDA band + FY28 Rs1,000-1,200 Cr target dropped from writing in the quarter margins hit 10.34%"}
  - {id: "F16-02", check: "F16", line: "PR L87/L91; deck p6 L176/L180 vs deck p11 L372/L380", classification: "AMBIGUOUS", implication: "Narrative improving-efficiency contradicted by own 6-yr chart: EBITDA margin 16.5->11.6->10.34%, ROCE 42.9->29.4%; Role-5 core"}
  - {id: "F16-03", check: "F16", line: "PR L141 vs L128", classification: "FORWARD-SIGNAL", implication: "Trips +27% vs revenue +16.7% -> revenue/trip -8%; realisation/mix falling = margin-compression driver"}
  - {id: "F16-04", check: "F16", line: "PR L141-142", classification: "AMBIGUOUS", implication: "ETS 59%/CCR 41% stated margin cause but no prior-period mix disclosed to size the shift"}
  - {id: "F16-05", check: "F16", line: "PR L155-156; deck p25 L709-710", classification: "AMBIGUOUS", implication: "Long-standing-customer share 61->55->51%; deck chart stops at FY26 55%, 51% only in PR text; stickiness softening"}
  - {id: "F16-06", check: "F16", line: "deck p20 L601; p15 L469; PR L150-151", classification: "BENIGN", implication: "5% owned / 95% vendor mix REBUTS asset-light-drift concern from results F15-01 (WOS gross block still not shown)"}
forward_signals: ["F6-01", "F7-01", "F13-01", "F16-01", "F16-03"]
ambiguous: ["F1-01", "F8-01", "F16-02", "F16-04", "F16-05"]
commitments:
  - {commitment: "New in-house CCR technology platform launched", implied_date: "Q1 FY27", ref: "PR L94; deck p6 L183", status_word: "completed"}
  - {commitment: "Major upgrade to proprietary in-house technology platform unveiled", implied_date: "Q1 FY27", ref: "PR L161-162", status_word: "completed"}
  - {commitment: "SIXT India-GSA exclusive partnership (early traction)", implied_date: "ongoing, undated", ref: "PR L95/L164-165; deck p6 L184", status_word: "underway"}
  - {commitment: "FY26 final dividend Rs2.38/share pending AGM", implied_date: "record date 18 Aug 2026; payment post-AGM ~21 Sep 2026", ref: "PR L170-171", status_word: "initiated"}
  - {commitment: "Leadership bandwidth strengthened ahead of next phase of growth (cost signal)", implied_date: "Q1 FY27", ref: "PR L167-168", status_word: "underway"}
  - {commitment: "Expansion into Tier-II/III cities and new geographies", implied_date: "ongoing (+20 cities this qtr -> 151)", ref: "PR L98-99/L147; deck p27 L733", status_word: "underway"}
  - {commitment: "Increasing wallet share from existing customers; expand skilled sales team", implied_date: "undated", ref: "deck p27 L731-732", status_word: "initiated"}
gate_a3: pass
blank_checks: []
```
