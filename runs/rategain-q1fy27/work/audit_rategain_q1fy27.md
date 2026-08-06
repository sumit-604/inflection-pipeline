# A5 ADVERSARY / COMPLETENESS AUDIT — RateGain Travel Technologies Ltd (RATEGAIN)
# Quarter: Q1 FY27 | Model: claude-opus-4-8 | RE-AUDIT (prior verdict INCOMPLETE)
# Inputs seen: A4 review, A1 extracts (results/presentation/press release/loan-prepay), A2 ledgers (results/presentation). No A3 reasoning, no orchestrator commentary. All figures re-derived independently.

---

## RE-AUDIT OF THE THREE PRIOR-FLAGGED A4 ERRORS (verify first)

| # | Prior error | Source check (re-derived) | A4 review now says | Status |
|---|---|---|---|---|
| 1 | Sojern PPA goodwill | results L609 `Goodwill 13,020.01` mn x0.1 = **1,302.0 Cr** (USD 147.02M, L609) | "Goodwill (PPA) Rs 13,020.01 mn = Rs 1,302.0 Cr / USD 147.02M" (C2 L313; Step 2 diag 5 L133; note L324) | **CORRECTED — PASS** |
| 2 | Sojern PPA intangibles | results L602-604: 3,827.18 + 887.37 + 1,875.88 = **6,590.43** mn x0.1 = **659.0 Cr** | "Customer rel. 3,827.18 + Trademarks 887.37 + Software 1,875.88 = Rs 6,590.43 mn (Rs 659.0 Cr)" (C2 L314; note L324) | **CORRECTED — PASS** |
| 3 | NRR series / sub-100 count | presentation ledger Table B L110: `120.9 / 100.5 / 99.6 / 106.8`; only FY26 = 99.6 < 100 | Stated consistently in C1-5 (L305), F3 (L390), Step 8C (L237), Q6 (L343), flags (L458): "120.9 -> 100.5 -> 99.6 -> 106.8, only FY26 (99.6) below 100, rebound to 106.8" | **CORRECTED — PASS** |

All three prior errors are fixed and correctly sourced. Proceeding to the full independent audit (not assuming the rest is clean).

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate)

Section F PLAIN-LANGUAGE BRIEF present with all four labelled parts, each carrying real content:

| Part | Heading | Present? | Content check |
|---|---|---|---|
| (1) Summary narrative | F1 (L383-384) | present | ~18-line narrative; verdict PROCEED WITH FLAGS, stance WATCHLIST/DILIGENCE, numbers-anchored |
| (2) Sector intelligence | F2 (L386-387) | present | TAM split, demand read, structural tailwind/headwind, "not disclosed" named |
| (3) Business-model intelligence | F3 (L389-390) | present | revenue-by-engagement, NRR/LTV:CAC drift, adjusted-vs-reported caveat |
| (4) Competition intelligence | F4 (L392-393) | present | breadth/incumbency, near-flat Distribution, concentration, inorganic-vs-organic risk |

**Gate: PASS** — all four parts present and non-empty.

---

## AUDIT 1 — COVERAGE (independent grep re-enumeration vs A2 ledgers)

Independent grep + sweep over the extracts:

| Category | A2 count | My fresh count | Method | Orphan / missing rows | Status |
|---|---|---|---|---|---|
| Standalone notes | 10 | 10 | Notes 1-10 present; Note 5 OCR "s" confirmed real (results L267) | none | PASS |
| Consolidated notes | 12 | 12 | Notes 1-12 present (results L561-661) | none | PASS |
| Total numbered notes | 22 | 22 | 10 + 12 | none | PASS |
| Annexure A entities | 18 | 18 | grep `^\s*[0-9]{1,2}\.\s+(RateGain\|Sojern\|Nrejos)` = rows 1-18 (results L432-468) | none | PASS |
| PPA table rows | 7 | 7 | results L598-609 | none | PASS |
| Standalone P&L line items | 24 | 24 | results L189-224 | none | PASS |
| Consolidated P&L line items | 33 | 33 | results L493-551 | none | PASS |
| Auditor paras standalone | 5 | 5 | results L88-171 | none | PASS |
| Auditor paras consolidated | 6 | 6 | results L336-475 | none | PASS |
| Agenda/disclosure items | 6 | 6 | 2 Board (L31/L40) + 4 Annexure B (L683-703) | none | PASS |
| ZERO_STANDING (results) | 7 | 7 | 2 standalone P&L + 5 consol P&L | none | PASS |
| Slides | 30 | 30 | page markers 1-30 | none | PASS |
| Deck P&L+BS line items | 58 | 58 | 20 P&L + 38 BS | none | PASS |
| Deck footnotes | 6 | 6 | E1-E6 | none | PASS |
| Turns / questions | 0 | 0 | no concall transcript in inputs | none | PASS |

**Ledger-row-to-review traceability (every flagged row cited in A4 or reviewed/no-finding):**
- 4 ENTITY_CHANGE rows (Annexure A 4/7/15/16): all cited — C2 entity-structure para (L326) + monitorables + Q15.
- 7 PPA rows: cited in Section C2 (L309-322).
- USD 65M corporate guarantee (agenda item 2 / Annexure B): cited — Q7, FN5, flags, monitorables.
- QIP Rs 11,151.20 mn (Note 4/5): cited — 0C, Q14 (A3-F10).
- Labour Code (Note 8/9): cited — Q17.
- Sojern HK liquidation (Note 12): cited — Q15, monitorables.
- Standalone-vs-consol deal-cost split (25.92 vs 324.16 mn; ledger §12): the ledger itself resolves this as a scope difference "not an inconsistency to chase"; A4 carries both the 4.79 Cr standalone and 34.6 Cr consol exceptional (Step 1A / Step 3). Reviewed, no finding — acceptable.
- ZERO_STANDING exceptional-item rows: A4 records nil both Q1s (bridge L161); reviewed, no finding.
- OCR_ANOMALY rows (UDIN garbles, CMD signature, Note-5 "s"): extraction artifacts flagged for re-sourcing, not disclosures; 0D covers the auditor opinion. No finding required.
- All FN1-FN16 and A3-F1..F15: mapped to questions in the Section D coverage-check line (L358); F3/F4/F5/F11/F12 = PASS, F16/F17 = N.A. (declared, L17).

**No orphan rows. No rows my fresh pass found that the ledger lacks. COVERAGE: PASS.**

---

## AUDIT 2 — ARITHMETIC (recomputed from raw extracted numbers)

Raw source = results extract (Rs mn x0.1) and deck (Rs Cr). Spot of every A4-derived metric:

| Metric | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| Standalone Op EBITDA Q1FY27 (PBT+D+FC−OI) | 5.01 | 5.677+1.269+0.227−2.160 = 5.01 | res L200/196/195/190 | PASS |
| Standalone Op EBITDA margin Q1FY27 | 7.4% | 5.01/68.19 = 7.35% | res L189 | PASS |
| Standalone Op EBITDA Q1FY26 | 6.74 | 24.149+1.133+0.261−18.808 = 6.74 | res L200/196/195/190 | PASS |
| Standalone ETR Q1FY27 | 25.9% | 1.468/5.677 = 25.86% | res L207/203 | PASS |
| Standalone PAT margin Q1FY27 | 6.2% | 4.209/68.19 = 6.17% | res L209/189 | PASS |
| Standalone PAT collapse YoY | −76.7% | 4.209/18.055−1 = −76.68% | res L209 | PASS |
| Standalone Core PBT ex-OI FY26 | 23.76 | 68.154−44.391 = 23.76 | res L203/190 | PASS |
| Standalone Op EBITDA FY26 | 34.24 | uses pre-exceptional PBT 72.948: 72.948+4.690+0.994−44.391 = 34.24 | res L200/196/195/190 | PASS (definitional — see note below) |
| Consol Core PBT ex-OI Q1FY27 | 117.5 | 120.6−3.1 = 117.5 (precise 117.47) | res L508/494 | PASS |
| Consol Core PBT ex-OI Q1FY26 | 40.7 | 61.327−20.658 = 40.67 | res L508/494 | PASS |
| Consol ETR Q1FY27 | 21.3% | 256.45/1205.55 = 21.27% | res L513/508 | PASS |
| Consol ETR Q1FY26 | 23.5% | 143.95/613.27 = 23.47% | res L513/508 | PASS |
| Consol PAT YoY | +102.2% | 949.10/469.32−1 = +102.23% | res L515 | PASS |
| Consol Reported EBITDA incl OI Q1FY27 | 174.6 | 171.5+3.1 = 174.6 | deck L748/L759 | PASS |
| EBIT (Op EBITDA−D&A) Q1FY27 | 134.0 | 171.5−(3.7+33.8) = 134.0 | deck L748/755/756 | PASS |
| EBIT YoY | +226.8% | 134.0/41.0−1 = +226.8% | derived | PASS |
| PAT bridge: Op EBITDA / D / amort / FC / OI | +121.8/−1.8/−27.0/−16.2/−17.6 | 171.5−49.7 / 3.7−1.9 / 33.8−6.8 / 16.5−0.3 / 3.1−20.7 | deck L748/755/756/757/759 | PASS |
| PAT bridge -> reported PAT change | +48.0 | 949.10−469.32 = 479.78 mn = +48.0 | res L515 | PASS |
| S-vs-C gap Q1FY27 (std % of consol) | 4.4% | 4.209/94.910 = 4.44% | res L209/L515 | PASS |
| S-vs-C gap Q1FY27 (gap % of consol) | 95.6% | 90.701/94.910 = 95.56% | res L209/L515 | PASS |
| Sojern goodwill / consideration | 58.6% | 1302.0/2222.08 = 58.6% | res L609/598 | PASS |
| Goodwill+intangibles / assets | 64% | (1591.5+756.3)/3659.1 = 64.2% | deck L778/779/784 | PASS |
| Net debt | 615.4 | 871.0−255.6 = 615.4 | deck L784/796/333/336 | PASS |
| Borrowings change | −50.3 | 921.3−871.0 = 50.3 | deck L784/796 | PASS |
| Adjusted-vs-reported PAT margin gap Q1FY27 | +2.8pp | 14.9−12.1 = 2.8 | deck L765/767 | PASS |
| Reported PAT margin deterioration YoY | −5.1pp | 12.1−17.2 = −5.1 | deck L765 | PASS |
| Loan outstanding / % repaid | USD 77.50M / 38% | loan L44 (77,500,000); pr L102 (38%); 9.75+6.25 = 16.0M | loan L40-44 / pr L100-102 | PASS |
| Gross margin drop | ~680 bps to 69.2% | 76.0−69.2 = 6.8pp | deck L626-627 | PASS |
| LTV:CAC | 21.3x -> 10.7x | ledger slide 10 series endpoints | deck L275/277 | PASS |

Deck-reported percentages that A4 quotes rather than derives (245.4%, 289.3%, 393.9%, 5451.3%, 100.2%, 187.6%) were re-checked against the precise mn figures and reconcile to within the deck's own rounding of the displayed Cr values; A4 correctly attributes each to its deck line, so these are cited-source figures, not A4 derivations.

**One definitional note (not a FAIL).** Standalone FY26 "Operating EBITDA (PBT+D+FC−OI) = 34.24" uses *Profit before exceptional items and tax* (72.948 Cr), whereas the same table's "Core PBT ex-OI = 23.76" uses *Profit before tax* (68.154 Cr, i.e. after the 4.79 Cr exceptional). Taking the formula label literally (PBT = 68.15) would give 29.45, a 4.79 Cr gap. The 34.24 figure is the *correct operating* treatment (an operating EBITDA should exclude the FY26-only exceptional one-off), so the value is right and the shorthand label "PBT" is imprecise. This touches only a standalone (secondary), prior-year cell; it drives no headline, no consolidated metric, and no verdict. Flagged for transparency; below the FAIL threshold because the number is not wrong under the correct definition.

**ARITHMETIC: PASS** — no mismatch above rounding.

---

## AUDIT 3 — ADVERSARIAL READ (three most positive claims, strongest bear counter from the same extracted text)

**Positive claim 1 — "Revenue nearly triples +187.6% YoY; highest-ever EBITDA; Adj. EBITDA margin 24.6%" (pr L43-48; deck slide 9).**
Bear counter from same text: essentially 100% inorganic (Sojern consolidated from 6 Nov 2025; management's own non-comparability note, res L616-618); organic Distribution grew only +3.1% (deck slide 12); reported PAT margin actually *fell* 17.2% -> 12.1%; the 24.6% is *adjusted*, stripping a real dated cash cost (Sojern deferred consideration ~21.9 Cr/qtr to Q3FY29).
Survives? Yes — but **already fully grafted** into A4 (Step 2 diag 1/2, Step 4, FN7/FN10, Section C1, flags). No new graft required.

**Positive claim 2 — "Deleveraging is real: acquisition loan down to USD 77.5M of USD 125M, 38% repaid; will lower future finance costs" (loan L44; pr L100-102; Step 5).**
Bear counter from same text: the same Board meeting approved a *new* USD 65M corporate guarantee to HSBC/JPM/Citi for RateGain UK + Sojern (res L40-44 / Annexure B L693-703), which is *absent from the investor deck* — so contingent off-balance-sheet exposure is being re-loaded even as the facility amortises; the deleveraging narrative and a fresh guarantee envelope must be read together.
Survives? Yes — but **already grafted** (Section C2 leverage para L328, Q7, FN5, flags, monitorables). No new graft required.

**Positive claim 3 — "Operating EBITDA margin expanded +3.7pp to 21.9% (24.6% adjusted)" (deck L749/752; Step 2 diag 2).**
Bear counter from same text: the lift is a *mix effect* from higher-margin acquired revenue, not proven organic operating leverage; concurrently gross margin *compressed* to 69.2% from 76.0% (deck L626-627) on ad-spend (L621); and the adjusted margin removes a genuine cash cost, so the reported operating economics are weaker than headlined.
Survives? Yes — but **already grafted** (Step 2 diag 2, Section C1-4, F3, flags). No new graft required.

**No surviving bear counter is missing from A4.** The review is symmetric bull-bear throughout; every strong-form counter I could construct from the extracts is already present. Nothing to loop back to A4.

---

## VERDICT

**COMPLETE.** The three prior-flagged A4 errors are corrected and correctly sourced. Independent re-enumeration matches both A2 ledgers with zero orphan rows and zero rows the ledger lacks. Every A4-derived metric recomputes from the raw extracts within rounding (one standalone FY26 definitional imprecision noted, below the FAIL threshold, no verdict impact). All four plain-language-brief parts are present and non-empty. All three strongest bear counters are already incorporated. Nothing to loop back to A2, A3, or A4.

```yaml
stage: A5-adversary
company: "RATEGAIN"
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
