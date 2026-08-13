# A5 ADVERSARY / COMPLETENESS AUDIT — Scoda Tubes Limited (SCODATUBES), Q1 FY27 (MERGED: results + investor presentation)

Model: claude-opus-4-8 | Fresh context. Re-derived independently from the two A1 extracts and the two A2 ledgers; A4 cites checked, not trusted.
Documents in scope (2): Reg 33 RESULTS filing (LRR) + Q1 FY27 40-slide INVESTOR PRESENTATION.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate)

PLAIN-LANGUAGE BRIEF located at review L501-513. All four labelled parts present, non-empty, real content (not placeholders):

| Part | Heading | Location | Status |
|---|---|---|---|
| 1 | SUMMARY NARRATIVE | L503-504 | PRESENT — dense multi-sentence narrative (~18 lines of prose), numbers anchored, covers revenue/margin/cash/decision |
| 2 | SECTOR INTELLIGENCE | L506-507 | PRESENT — SS pipe demand CAGR, India outlook + anti-dumping, export franchise, input-cost headwind |
| 3 | BUSINESS-MODEL INTELLIGENCE | L509-510 | PRESENT — capex-heavy backward-integrating model, above/below-EBITDA stress, cash-conversion Achilles heel |
| 4 | COMPETITION INTELLIGENCE | L512-513 | PRESENT — peer scale/margin/cash-conversion gap, disclosure lag, promoter-quality offset |

GATE 0: PASS. All four present.

---

## AUDIT 1 — COVERAGE (independent re-grep of BOTH extracts vs BOTH ledgers)

### 1A. RESULTS extract (body L1-204; L205-289 = A1 corrections/footing metadata, correctly excluded from enumeration)

| Category | A2 count | My fresh count | Fresh-pass basis | Orphan/missing | Status |
|---|---|---|---|---|---|
| Notes | 7 | 7 | L115,118,120,122,123,125,127 | none | PASS |
| Line-items | 25 | 25 | L81-112 value-bearing rows minus 7 header rows (80,84,95,100,101,108,109) | none | PASS |
| Zero-standing | 3 | 3 | L93 Exceptional, L97 Earlier-yr tax, L111 EPS-Discontinued (blank all 4 periods) | none | PASS |
| Agenda items | 1 | 1 | L38-39 (approve results + LRR); no other board items on L34-46 sweep | none | PASS |
| Auditor paras | 4 | 4 | L158-161 / 162-167 / 169-178 / 179-185 | none | PASS |
| Entities | 1 | 1 | L123-124 standalone; Note 5 no subsidiary/JV/associate | none | PASS |
| Signatories | 3 | 3 | L51-53 MD DIN 06785595; L141-143 Chairman/WTD DIN 08036100; L188-197 auditor M.No.134475 / UDIN 26134475LRVGGI8483 | none | PASS |

All 7 results notes appear in review Step 0D table (L60-68); auditor opinion (unmodified) at L70; entity/S-vs-C at Step 4A; signatories in preamble L29 and governance flag Q13. Every results ledger row is cited or covered.

### 1B. PRESENTATION extract (40 slides)

| Category | A2 count | My fresh count | Fresh-pass basis | Orphan/missing | Status |
|---|---|---|---|---|---|
| Slides | 40 | 40 | Ledger Table 1 rows slide 1-40, contiguous; source lines 38-1403 | none | PASS |
| Numbers | 624 | 624 (accepted) | net-zero 5-item reconciliation documented (excl 2 footer-pagination + 3 axis-unit "000"; add 3 narrative quantities + 2 zero-standing) | none | PASS |
| Footnotes | 48 | 48 (accepted) | Ledger Table 4, 48 rows | none | PASS |
| Dropped-slide | N.A. | N.A. | first deck for ticker, no prior to diff | n/a | PASS |

Headline-number spot-check (my re-grep of ledger Table 3 vs review):
- Slide 36 Q1 income statement (dL1283-1304): every line enumerated and cross-checked in review Step 1.1 deck block (L108). Confirmed.
- Slide 23/24/25 annual IS/BS/CFO panels (dL790-877): enumerated; folded into review Step 1.3 (L129-136) and Step 5.2. Confirmed.
- Slide 22 consistency ratios (dL751-775): enumerated; review Step 1.3 (L138-139) and Step 5.2/6B. Confirmed.
- Slide 5 Performance Snapshot (dL144-183): the period-blended KPI cards enumerated; review F16-2 handling (Step 5.3). Confirmed.

Key qualitative disclosures spot-check:
- Slide 6 Chairman commentary narrative additions (dL194 "three to four months", dL197 "a couple of weeks", dL198/205-206 "H2 FY27") — enumerated in ledger (GUIDANCE_NARRATIVE_ADDITION); review Step 2/commitment register/Q9. Confirmed.
- Slide 16 marine "currently applied for" (dL569 footnote), 349 clients (dL537) — enumerated; review trigger 6 / F16-8. Confirmed.
- Slide 10 vs 28 capacity cross-slide inconsistency (dL344/936) — enumerated CROSS_SLIDE_INCONSISTENCY; review F16-9 / Q7. Confirmed.
- Slide 7 vs 30 export NUMBER_DISCREPANCY (57.9 vs 57.0; 46.6% vs 45.8%) — enumerated; review F14-2(deck) NEUTRAL-FACT; brief uses "~46% (Rs57 Cr)" approximation. Confirmed, no mis-state.
- Slide 17 donut sum-to-124% AMBIGUOUS_MAPPING, Slide 20 director-experience TEMPLATE_REPEAT asymmetry — extraction-integrity/visual-verification flags, immaterial to analysis; covered by the preamble blanket "all reviewed", no material finding required. Not orphans.

### 1C. Ledger-reconciliation preamble coverage
Review L19-37 explicitly reconciles BOTH ledgers (RESULTS 7/25/3/1/4/1/3; PRESENTATION 40/624/48), lists all 19 A3 findings across both forensics, and states "No ledger row on either ledger is unreviewed." Preamble covers both documents. PASS.

COVERAGE VERDICT: no orphan rows (ledger→A4), no missing rows (fresh pass→ledger). PASS.

---

## AUDIT 2 — ARITHMETIC (recomputed from CORRECTED results grid L81-99; deck cross-checked where overlapping)

Corrected grid independently confirmed against the A1 footing block (L257-289): all four columns foot on the five identities (Total Income, Total Expenses, PBT, PAT, TCI) = 20/20. Q1FY26 PAT = 70.83 (not corrupt 10.83) reproduced.

| Metric | A4 value | My recompute | Source | Status |
|---|---|---|---|---|
| Operating EBITDA Q1FY27 (PBT+D+Fin−OI) | 15.979 | 6.997+4.131+6.481−1.630 = 15.979 | L94/89/88/82 | MATCH |
| Op EBITDA Q1FY26 / Q4FY26 / FY26 | 14.190 / 16.705 / 76.244 | 14.190 / 16.705 / 76.244 | grid | MATCH |
| Op EBITDA margin Q1FY27 | 12.85% | 15.979/124.345 = 12.851% | L81 | MATCH |
| Op EBITDA margin Q1FY26 / Q4FY26 / FY26 | 14.57 / 13.52 / 14.70% | 14.566 / 13.518 / 14.700% | grid | MATCH |
| Reported EBITDA margin Q1FY27 | 14.16% | 17.609/124.345 = 14.16% | grid | MATCH |
| RM-consumed intensity Q1FY27 / Q1FY26 | 80.55% / 76.22% | 100.165/124.345=80.55%; 74.249/97.417=76.22% | L85 | MATCH (+434 bps) |
| FG/WIP build credit Q1FY27 / Q1FY26 | 12.56% / 5.39% | 15.614/124.345=12.56%; 5.247/97.417=5.39% | L86 | MATCH (+717 bps) |
| Net material bps change | −283 bps | 68.00% − 70.83% = −283 bps | L85+L86 | MATCH |
| Employee bps change | −50 bps | 1.980% − 2.484% = −50 bps | L87 | MATCH |
| Other-expenses bps change | +505 bps | 17.173% − 12.117% = +505 bps | L90 | MATCH |
| Op-margin decomposition reconciles | −172 bps | +283 + 50 − 505 = −172 bps | — | MATCH |
| Effective tax rate Q1FY27 | 24.97% | 1.747/6.997 = 24.97% | L96+98/94 | MATCH |
| Current-tax share of PBT Q1FY27 | 8.93% | 0.625/6.997 = 8.93% | L96/94 | MATCH |
| Deferred-tax shield | ~1,603 bps | 1.122/6.997 = 16.035% = 1,603 bps | L98/94 | MATCH |
| Revenue YoY | +27.64% | 26.928/97.417 = 27.64% | L81 | MATCH |
| Op EBITDA YoY | +12.61% | 1.789/14.190 = 12.61% | — | MATCH |
| Depreciation YoY | +162.8% | 2.559/1.572 = 162.8% | L89 | MATCH |
| Finance YoY | +26.98% | 1.377/5.104 = 26.98% | L88 | MATCH |
| EBIT(op) YoY | −6.10% | −0.770/12.618 = −6.10% | — | MATCH |
| Core op PBT YoY | −28.57% | −2.147/7.514 = −28.57% | — | MATCH |
| Reported PBT YoY | −24.56% | −2.278/9.275 = −24.56% | L94 | MATCH |
| PAT YoY | −25.88% | −1.833/7.083 = −25.88% | L99 | MATCH |
| EPS YoY | −38.89% | −0.56/1.44 = −38.89% | L110 | MATCH (deck rounds to −39.1%; A4 notes both) |
| Revenue QoQ | +0.63% | 0.776/123.569 = 0.63% | L81 | MATCH |
| PAT QoQ | −16.92% | −1.069/6.319 = −16.92% | L99 | MATCH |
| PAT bridge foots | −1.833 | +11.379−0.042−9.548−2.559−1.377−0.131+1.265−0.820 = −1.833 | 4B | MATCH |

Deck-vs-filing overlap (deck should confirm, and A4's claims about the deck):
| Deck claim | Deck line | My check | A4 label | Status |
|---|---|---|---|---|
| Revenue 124.3 | dL1283 | =124.345 rounded | Q1 | OK |
| EBITDA margin −172 bps → 12.9% | dL1292 | operating basis, 12.85% rounds to 12.9% | Q1 operating | OK |
| Gross +283 bps | dL1286 | 32.0% vs 29.2% net-material basis | Q1 | OK |
| PAT −25.9% | dL1300 | matches filing −25.88% | Q1 | OK |
| CFO −13.8 = ANNUAL not Q1 | dL867 FY26 col | FY26 column of Historic Cashflow | FY26 ANNUAL | OK — correctly not reported as Q1 |
| Cumulative FY23-26 CFO/PAT ~0.27x | dL867/dL806 | (20.3+2.2+18.4−13.8)/(10.3+18.3+31.7+38.8)=27.1/99.1=0.2735 | annual, NOT formally fired | OK |
| ROCE FY26 11.6% | dL774 | present | FY26 annual | OK |
| FY26 D&A 9.2 vs FY25 18.1 | dL801 | present | annual, understatement flag | OK |
| Debtor 97 / CCC 211 / Inventory 217 | dL770/dL770/dL751 | present | FY26 ANNUAL | OK — all labelled annual |
| ROE FY26 9.9% | dL757 | present | FY26 annual | OK |
| Net D/E 0.3x | dL759 | present | post-IPO / neutral | OK |
| EPS FY25 7.6 > FY26 6.8 | dL809 | present | IPO dilution | OK |

ARITHMETIC VERDICT: zero mismatches above rounding. No annual metric reported as Q1 or vice versa. PASS.

---

## AUDIT 3 — ADVERSARIAL READ (strongest bear counter to the three most thesis-favourable claims + the four new-merged scrutiny points)

The review is an AVOID/bear document; its thesis-FAVOURABLE (bull-leaning) claims are the attack surface.

**Positive claim 1 — "Revenue +27.6% YoY is a genuine re-acceleration; the one good number" (L151, L181, L504).**
Bear counter: revenue is flat sequentially (+0.63% QoQ vs Q4FY26 123.569, L209); the +27.6% is versus a soft Q1FY26 base, and the deck shows FY26 full-year growth had already decelerated to +7.0% (dL360). Worse, sales lagged production — the Rs15.614 Cr FG/WIP build (L86) means dispatched revenue quality is suspect.
Survives? NO — already grafted: Step 2 diagnostic 1 (L181), Step 3 "plateaued QoQ +0.63%" (L209), build discussion (L178). Incorporated.

**Positive claim 2 — "Operating EBITDA still grew +12.6%" (L152, L240, L504).**
Bear counter: the +12.6% is inventory-inflated. The gross-profit leg (+11.379) is propped by the Rs15.614 Cr build; strip the abnormal build increment and operating-EBITDA growth reverses. RM-consumed intensity actually worsened +434 bps.
Survives? NO — already grafted: A5 GRAFT 2 (L15), Step 2 read #2 (L178), Step 4B double-scoring reconciliation (L251). Incorporated.

**Positive claim 3 — "Net D/E improved to 0.3x" (L299, L328).**
Bear counter: this is a Rs220 Cr IPO equity infusion (equity+reserves 150.4→390.3, dL834), not operational deleveraging; borrowings fell only 210.2→185.3 while FY26 CFO was −13.8. It is a financing event, not cash generation.
Survives? NO — already labelled NEUTRAL-FACT/post-IPO: Step 5.2 (L299), Step 5.3 (L311), Step 6A (L328). Incorporated.

(Also-positive claims — corrected-grid corroboration by deck (F16-5) and EPS/IPO-dilution resolution (F10-1) — carry no bull thesis-lift; both are neutral data-integrity/explanatory items, correctly handled.)

**New-merged scrutiny points (a)-(d):**
- (a) Q1-vs-annual conflation: rigorous. Every annual metric (CFO −13.8, inventory 217, debtor 97, CCC 211, ROCE 11.6%, ROE 9.9%, D&A 9.2) is explicitly tagged FY26 ANNUAL; the Slide-5 period-blend is called out (F16-2, Step 5.3, verdict L493, brief L504). Q1 CFO held INDETERMINATE. No conflation survives, including in the prose brief/SECTOR/BUSINESS-MODEL/COMPETITION sections (all annual figures there are labelled FY26; the only Q1-tagged prose figure — exports ~46%/Rs57 Cr — is correctly Q1 per Slide 17 footnote "Based on Q1 FY27 nos."). NO surviving counter.
- (b) "management says transient": flagged as unverified management claim, not evidence — Step 2 "a claim of transience is not proof; testable next quarter" (L177), Q9 marked "[MANAGEMENT-ANSWERED — verify at Q2]" (L432), verdict flag (L575). NO surviving counter.
- (c) cumulative CFO/PAT 0.27x: characterised as NOT-FORMALLY-FIRED (window FY22-FY27 at FY27-end; deck covers FY23-FY26 only) — Step 5.3(b) (L305), 6C (L352), 8A-W (L399). Correct. NO surviving counter.
- (d) net-D/E 0.3x: labelled post-IPO-equity/neutral — see claim 3. NO surviving counter.

ADVERSARIAL VERDICT: all three bull-leaning claims already carry their strongest bear counter; all four new scrutiny points handled rigorously. No new surviving counter to graft. The only residual issues are cosmetic/extraction-integrity flags already logged (Slide 17 donut mapping, Slide 20 template repeat, export 57.9/57.0). No fail manufactured.

---

## VERDICT

**COMPLETE.**

- Gate 0 (brief four parts): PASS.
- Coverage (both ledgers, both extracts): PASS — no orphan, no missing row; preamble covers both documents.
- Arithmetic: PASS — 30+ derived metrics re-derived, all match to rounding; four columns foot 20/20; deck overlaps reconcile; no annual/Q1 mis-labelling.
- Adversarial: PASS — three positive claims each pre-countered; four new scrutiny points rigorous; no surviving counter.

Protocol handling is correct: Q1 cash conversion is properly held INDETERMINATE with named missing evidence (standalone Q1/H1 FY27 CFO, Q1/H1 balance sheet, Q1 ROE/WC days), capping the verdict at PROCEED WITH CAVEATS — this is correct protocol, not a failure. Proceeds to Notion save.

loop_back_to: none. gap: none.

```yaml
stage: A5-adversary
company: "SCODATUBES"
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
```
