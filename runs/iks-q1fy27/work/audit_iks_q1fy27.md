# A5 ADVERSARY / COMPLETENESS AUDIT — IKS (Inventurus Knowledge Solutions Ltd) — Q1 FY27

**Agent:** A5 ADVERSARY | **Model:** claude-opus-4-8 | **Independence:** fresh context — re-derived from A1 extracts and A2 ledgers only; A4/A3 cites checked, not trusted.
**Under audit:** `review_iks_q1fy27.md` (A4). **Verdict:** **INCOMPLETE** (see foot).

Units: filing/deck report INR Million; review converts to Rs Crore at ÷10. I re-derived from the raw Mn figures throughout.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate, run first)

Plain-Language Brief is Section E of the A4 review. All four labelled parts present and carry real, non-placeholder content:

| Part | Location | Present | Content check |
|---|---|---|---|
| 1. Summary narrative | Sec E.1, L407–413 | PRESENT | 2 substantive paragraphs, ~14 lines, numbers anchored to L319/L345/deck L305 etc. |
| 2. Sector intelligence | Sec E.2, L415–419 | PRESENT | US healthcare RCM/coding TAM, policy exposure, AI double-edge; GENERAL KNOWLEDGE labelled |
| 3. Business-model intelligence | Sec E.3, L421–427 | PRESENT | unit economics, parent-vs-sub margin, acquisition-led drift, ND list |
| 4. Competition intelligence | Sec E.4, L429–435 | PRESENT | named peer field (R1/WNS/Firstsource/Sagility/EXL), win/loss vectors, "no anchored peer numbers" caveat |

Gate 0 = **PASS**. All four present and non-empty.

---

## AUDIT 1 — COVERAGE (fresh grep pass vs A2 ledger; then ledger row → A4 disposition)

Independent enumeration (my grep/manual sweep vs the A2 counts):

| Category | A2 count | My fresh count | Orphan (in ledger, absent from A4) | Status |
|---|---|---|---|---|
| **RESULTS ledger** | | | | |
| agenda_items | 3 | 3 (grep `^\s+[0-9]\.\s` L37/45/77) | none | OK |
| annexures | 4 | 4 (A/B/C-garbled/D) | none | OK |
| annexure_disclosure_rows | 10 | 10 (5 Annexure B + 5 Annexure D) | none | OK |
| auditor_paras | 11 | 11 (4 standalone + 7 consolidated) | none | OK |
| entities | 11 | 11 (3 WOS + 7 SDS + 1 assoc, L228–239) | none | OK |
| notes | 10 | 10 (grep `^\s{0,2}[0-9]{1,2}\s+[A-Z(]` L406–446) | none | OK |
| line_items | 37 | 37 | **line item #28 — FVOCI "Changes in fair value of equity investments" (L377, Rs 226.42 Mn, the Abridge revaluation)** | **ORPHAN** |
| zero_standing | 4 | 4 | none | OK |
| signature_blocks | 5 | 5 | none | OK (administrative, reviewed-no-finding via preamble) |
| **PRESENTATION ledger** | | | | |
| pages/slides | 18 | 18 | none | OK |
| financials_summary rows | 24 | 24 | none | OK (all tie — see Audit 2) |
| other_kpi rows | 8 | 8 | none (FCF-yield substance covered via F16c) | OK |
| footnotes | 11 | 11 | **footnote #10 — "*ROE declined due to increased equity base from revaluation of Abridge…" (L443)** | **ORPHAN** |
| per-slide units | 161 | reconciled (spot-verified slides 3/8/9/10/13/14/15/16) | **Slide 12 ROE units 32.3% / 31.3% / 26.4% (L420–423) — the YoY ROE decline** | **ORPHAN** |

**Rows my fresh pass found that the ledger lacks:** NONE. A2 enumeration is complete on both files; the counts reconcile. A2 does **not** fail.

**Orphan analysis (the failing thread).** Three enumerated units all point at one uncovered disclosure: **return-on-equity fell 590 bps YoY (32.3% Q1 FY26 → 26.4% Q1 FY27)** while the deck slide-12 title claims "**maintaining high ROE**" (L415). The deck's own footnote (L443) concedes "ROE declined," attributing it to an **increased equity base from the revaluation of Abridge** (the FVOCI equity investment, filing line item #28, L377, +Rs 22.6 Cr through OCI), alongside the forex/acquisition-cost drivers A4 already covers.

A4 touches ROE only once (Step 7 pillar table: "deck ROE 26.4%… not ROCE") and **does not**: (a) state that ROE fell YoY, (b) challenge the "maintaining high ROE" framing — even though A4 catches the exactly-parallel "unsigned QoQ EPS decline" framing at Q14, or (c) mention the Abridge FVOCI revaluation anywhere. No A3 forensic in A4's incorporation list (F1/F6/F7/F8/F10/F13/F14/F15/F16a–f) covers it. This is a material disclosure unit with no finding and no management question → **coverage FAIL, return to A3** (missed forensic), which A4 must then graft.

Note: the A2 presentation ledger row-19 note mislabels the P&L associate (WWMG) as "Abridge." A4 correctly used WWMG for the associate and did not inherit that slip — but then left the *actual* Abridge FVOCI item untouched. Not scored against A2 (its counts are complete); it reinforces that the Abridge revaluation fell through the net.

**Concall "NOT SUPPLIED" — verified a true absence, not a dropped document.** The four A1 headers are results_board_outcome.pdf, results_press_release.pdf, results_change_directors.pdf, presentation.pdf. None is a call transcript; the deck is an "Investor Presentation," not Q&A; no document references a concall being part of the package. A4's Role 5 NOT SUPPLIED handling is correct.

---

## AUDIT 2 — ARITHMETIC (recomputed from raw INR Mn; ÷10 to Rs Cr)

Every headline and derived metric in A4's tables was recomputed from the raw statement lines (L319–393) and deck Table 2/3. **All Step 1 data cells, all Step 1C/1D derived metrics, all Step 2 YoY, Step 3 QoQ, Step 4C standalone-vs-consol gap, and the Step 4A/4B PAT-bridge reconciled totals tie to the source within rounding.** Representative confirmations:

| Metric | A4 value | My recompute (source) | Status |
|---|---|---|---|
| Consol revenue YoY | +20.7% | (8,936.29−7,400.95)/7,400.95 = 20.74% | OK |
| Consol Op EBITDA Q1FY27 | 294.94 | 256.25+34.29+10.11−5.71 (L331/327/326/320) | OK |
| Consol Op EBITDA margin Q1FY27 | 33.0% | 294.94/893.63 = 33.005% | OK |
| Consol ETR Q1FY27 | 22.8% | 57.203/250.944 = 22.79% (L343/338) | OK |
| Consol ETR Q4FY26 | 18.6% | 46.987/252.955 = 18.58% | OK |
| Core PBT ex-OI YoY | +27.9% | (245.23−191.77)/191.77 = 27.88% | OK |
| PAT YoY | +27.8% | (1,937.41−1,515.39)/1,515.39 = 27.85% | OK |
| QoQ PAT | −5.9% | (1,937.41−2,059.68)/2,059.68 = −5.94% | OK |
| Standalone revenue YoY | +48.8% | (4,752.68−3,194.69)/3,194.69 = 48.77% | OK |
| Standalone other-exp QoQ | +117.0% | (573.57−264.30)/264.30 = 117.02% | OK |
| Std/consol PAT gap Q1FY27 (consol premium) | 19.2% | 31.19/162.55 = 19.19%; collapse 34.3→19.2 = 15.1pp | OK |
| PAT bridge reconciled total | +42.20 | 57.19−6.39+7.97+2.60−5.31−13.86 = +42.20 (=1,937.41−1,515.39) | OK |
| Unadjusted CFO/PAT (INDETERMINATE cap) | ≈0.29x | (1,999−1,430)/10 = 56.9 ÷ 193.74 = 0.294x | OK |
| Unadjusted FCF | ≈31.2 Cr | (1,742−1,430)/10 = 31.2 | OK |
| Net debt YoY | −40.8% | (2,654−4,486)/4,486 = −40.8% | OK |

**One arithmetic defect found:**

| Metric | A4 value | My recompute | Source line | Status |
|---|---|---|---|---|
| Step 4A "Total Expenses ex-D&A/finance" operating-cost-growth intermediate | **+82.85** | **+96.35** (employee +59.05 [L325] + other-exp +37.46 [L328] − inventory 0.16 [L324]); ex-inventory = +96.51 | review L215 | **FAIL** |

The "+82.85" is a genuine table mismatch above rounding: it **contradicts its own row**, whose impact column already carries **−96.51**, and its own listed components (59.05 + 37.46 + 0.16) sum to 96.67, not 82.85. Severity is **low / non-propagating** — the reconciled bridge total (+42.20) and every headline/derived metric are exact, so no conclusion is corrupted — but per the arithmetic rule it is a mismatch in a derived table and must be corrected before save. Loop-back: **A4** (also flag the inventory sign: the −0.16 is a benefit to EBITDA, so the correct operating-cost growth is +96.35).

**INDETERMINATE cash-conversion cap — justified.** The Rs 1,430 Mn "upfront guarantee payment of economic value add made to a customer" (deck L370) is real and its nature/recurrence genuinely undisclosed; it swings CFO/PAT from 1.03x (adjusted, 199.9/193.74) to 0.29x (unadjusted) and FCF from 174.2 to ~31.2 Cr. Per house rule this may not resolve silently and caps at PROCEED WITH CAVEATS with the missing evidence named — A4 does exactly this. Correct.

---

## AUDIT 3 — ADVERSARIAL READ (three most-positive claims, strongest bear counter from the same extract)

**Positive claim 1 — "Growth is core-operating, not treasury… the single cleanest positive" (Step 2 diag 3; core PBT ex-OI +27.9%, OI only 2.3% of PBT).**
Bear counter from the extract: consolidated core growth is partly borrowed from a **non-repeatable TruBridge software-license sale** inflating the group (Note 9, L442) and from a **−44.1% finance-cost drop** (L326); and it reverses sequentially — QoQ PAT −5.9%, margin −2.0pp (deck L457/L468).
Survives? **NO — already incorporated** (F-02 at Step 4B/2B; F-03 QoQ correction is A4's own "single most important framing correction," Step 3). No graft needed.

**Positive claim 2 — Revenue +20.7% YoY, Op EBITDA +24.1% with +0.9pp YoY margin expansion; "genuinely high margins," "maintaining high ROE."**
Bear counter from the extract: (a) ~8–9pp of the 20.7% is rupee depreciation (USD +12%) — A4 states this; (b) the "expansion" is YoY only, −2.0pp QoQ — A4 states this; **(c) reported ROE FELL 590 bps YoY (32.3%→26.4%, deck L420–423) while the deck titles the slide "maintaining high ROE" (L415), the decline driven partly by the Abridge FVOCI revaluation inflating the equity base (footnote L443; filing FVOCI line #28, L377).**
Survives? **YES for part (c).** The ROE decline, the "maintaining high ROE" framing contradiction, and the Abridge revaluation are absent from every A4 finding, monitorable and management question. This is the same class of selective-framing catch A4 already makes for QoQ EPS. **Must be grafted into A4** (caution flag + a management question on the Abridge revaluation quantum and normalised ROE). This is the surviving counter and the coverage orphan, same root.

**Positive claim 3 — De-levering: net debt −40.8% YoY to Rs 265.4 Cr; finance costs −44.1%.**
Bear counter from the extract: this is **pre-TruBridge**; the US$557 Mn EV acquisition (Note 9) closed 9-Jul-2026 with undisclosed funding and net debt already ticked up +5.7% QoQ (2,510→2,654, deck L304–305).
Survives? **NO — already incorporated** (F-10; Step 4A/Q7; monitorable #9). No graft needed.

---

## VERDICT

**INCOMPLETE.**

Two threads fail the gate:

1. **Coverage / adversarial (primary) — loop back to A3.** An enumerated disclosure cluster — Slide-12 ROE units (32.3%→26.4%, deck L420–423), footnote #10 "revaluation of Abridge" (L443), and filing FVOCI line item #28 (L377, Rs 226.42 Mn) — carries **no A3 forensic and no A4 finding or management question**. The deck claims "maintaining high ROE" while ROE fell 590 bps YoY; the disclosed Abridge equity-base driver is untouched. A3 must generate the forensic (ROE YoY decline + "maintaining high ROE" framing + Abridge FVOCI revaluation as the equity-base driver); A4 must then graft a caution flag and a management question, and add ROE to the monitorables.

2. **Arithmetic (secondary) — loop back to A4.** Step 4A operating-cost-growth intermediate "+82.85" (review L215) is wrong and self-contradictory (correct value +96.35; the row's own impact already reads −96.51); inventory −0.16 should carry a benefit sign. Non-propagating (reconciled bridge +42.20 and all headline metrics are exact) but must be corrected before save.

A2 enumeration is complete and passes (no rows missing from either ledger). All other arithmetic ties. All four Plain-Language-Brief parts present. INDETERMINATE cash-conversion cap justified. Concall NOT-SUPPLIED confirmed a true absence.

```yaml
stage: A5-adversary
company: "IKS"
quarter: "q1fy27"
model: claude-opus-4-8
status: complete
verdict: INCOMPLETE
plain_language_brief:
  narrative: present
  sector: present
  business_model: present
  competition: present
coverage:
  orphan_rows:
    - "Presentation Slide 12 ROE units (32.3%/31.3%/26.4%, deck L420-423) — YoY ROE decline not surfaced in A4"
    - "Presentation footnote #10 (deck L443) — 'ROE declined due to increased equity base from revaluation of Abridge' not carried into any A4 finding/question"
    - "Results line item #28 — FVOCI 'Changes in fair value of equity investments' (L377, Rs 226.42 Mn, the Abridge revaluation) untouched by A4"
  missing_from_ledger: []
arithmetic_mismatches:
  - {metric: "Step 4A operating-cost-growth intermediate (Total Expenses ex-D&A/finance)", a4_value: "+82.85", recomputed: "+96.35 (or +96.51 ex-inventory)", source_line: "review L215; raw L324/L325/L328"}
surviving_bear_counters:
  - {claim: "genuinely high margins / deck 'maintaining high ROE' (slide 12 title, L415)", counter: "reported ROE fell 590 bps YoY 32.3%->26.4% (deck L420-423); deck's own footnote L443 concedes the decline, driven partly by the Abridge FVOCI revaluation inflating the equity base (filing line #28, L377); absent from all A4 findings, monitorables and management questions", source_line: "deck L415/L420-423/L443; filing L377"}
loop_back_to: "A3"
gap: "A3 generated no forensic on the YoY ROE decline (32.3%->26.4%, deck slide 12 L415/L420-423), the deck's 'maintaining high ROE' framing contradiction, or the disclosed Abridge FVOCI revaluation driver (footnote L443; filing FVOCI line item #28, L377, Rs 226.42 Mn) — an enumerated ledger cluster absent from A4. A3 must produce the forensic and A4 must graft a caution flag + a management question (Abridge revaluation quantum, normalised ROE) and add ROE to monitorables. Separately, A4 must correct the Step 4A operating-cost-growth intermediate '+82.85' (review L215) to +96.35 (it contradicts its own -96.51 impact; inventory -0.16 is an EBITDA benefit) before save."
```
