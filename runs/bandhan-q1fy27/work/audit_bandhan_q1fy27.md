# A5 ADVERSARY / COMPLETENESS AUDIT — BANDHAN BANK — Q1 FY27

**Agent:** A5 ADVERSARY (Opus 4.8) | **Audited:** review_bandhan_q1fy27.md (A4) against A1 extracts + A2 ledgers
**Method:** Fresh context. Re-ran enumeration with own pass; recomputed every derived metric from raw extracted numbers (Reg 33 Lakhs ×0.01→Cr; press ×1; deck ₹Bn ×100→Cr, Non-Int-Income ₹Mn ×0.1→Cr; concall native Cr). Did not defer to A4/A3 cites — checked them. Every line number below is mine.

---

## AUDIT 1 — COVERAGE (fresh enumeration vs A2 ledger, then A4 citation check)

| Category | A2 count | My fresh count | Basis of my count | Orphan rows | Status |
|---|---|---|---|---|---|
| Results — notes | 16 | 16 | Read notes 1–16 verbatim, extract L334–L536 | none | MATCH |
| Results — agenda items | 4 | 4 | Board-outcome letter L41–L118 (results, CFO, CIV, AGM) | none | MATCH |
| Results — auditor paras | 6 | 6 | Review report L561–L624 (paras 1–6) | none | MATCH |
| Results — line_items | 112 | 112 (accepted) | Main P&L 34 + Segment 32 + Note6 sub 18 + Note9 16 + Note11 2 + Press 10 = 112; A2 documents the naive-grep undercount + manual re-sweep per table | none | MATCH |
| Results — entities | 1 | 1 | Note 14 standalone-only, no sub/assoc/JV | none | MATCH |
| Concall — turns | 70 | 70 | Counted [TURN 1]…[TURN 70] tags in extract | none | MATCH |
| Concall — questions | 25 | 25 | Q1a(6) Q1b(9) Q2a-e(12/14/16/18/19) Q3a-c(21/23/25) Q4a-b(28/30) Q5a-b(33/36) Q6a-b(39/42) Q7a-d(45/49/51/54) Q8a-b(57/59) Q9a-c(62/64/66) | none | MATCH |
| Concall — participants | 16 | 16 | 5 named mgmt + collective + 9 analysts + 1 moderator | none | MATCH |
| Concall — mgmt_numbers | 149 | 149 (accepted) | Sum-check in ledger §4 reproduces to 149; spot-verified key tokens (advances, PAT, NIM, DPD, bridge) | none | MATCH |
| Presentation — slides | 48 | 48 | [page 1]…[page 48] markers | none | MATCH |
| Presentation — line_items | 87 | 87 (accepted) | Table 3 register rows 1–87 traced by table | none | MATCH |
| Presentation — zero_standing | 8 | 8 | 7 table rows + slide-38 "0 Branch Visits" | none | MATCH |

**Fresh-found rows the ledger lacks:** NONE. My independent read surfaced no note, turn, question, slide, para, or segment row absent from the A2 ledgers.

**Orphan rows (in ledger, absent from A4):** NONE material. Every flagged/material ledger row is surfaced in A4 or carried as reviewed:
- Results flags → AUDITOR_CHANGE (A4 L35/L52), Q4FY26 balancing-figure (L37), UNREVIEWED Pillar-3 (L39), IFR transfer Note 8 (L42/L166), gratuity Note 10 (L44), IT-opex Note 11 (L45), standalone Note 14 (L48/C1), project-finance Note 9 (L43), assignment acquisition ₹1,870.79 Cr Note 6(i) (L40), ARC Note 6(iii) (L185), ZERO_STANDING exceptional/extraordinary (L77), RoA/NNPA blank cells 17(v)/17(iv)(d) (L105).
- Concall F-01…F-10 → all mapped (A4 YAML L579–588; substance in Steps 1–8B). NUMBER_DISCREPANCY ARC 291/290 → A4 uses the filing 291 (L185) [see note below]. GUIDANCE_VS_ACTUAL opex 4% vs 4.2% → A4 addresses the 4.3 breach (L345/L353).
- Presentation F1-1/F6-1/F13-1/F14-1/F16-1…F16-10 → all mapped (A4 YAML L589–602; C4 questions Q1–Q15). NO_FORWARD_GUIDANCE_SLIDE → Q15/F16-8 (L516). CASA Mar'25 base → F16-7/Q13 (L234/L514).

**Coverage note (non-gating, to A3/A4 for tidiness, not a FAIL):** Concall ledger §4 raised `NUMBER_DISCREPANCY` — ARC housing-NPA quantum stated 291cr (turn 4/L87) vs 290cr (turn 65/L221). A4 (L185, L388-cite) reconciles to the audited Note 6(iii) principal ₹291.44 Cr and does not separately narrate the 290/291 wobble. Immaterial (rounding of the same transaction); reviewed, no finding.

**COVERAGE VERDICT: PASS.** Fresh enumeration reconciles to all three ledgers; no orphan row, no missing-from-ledger row.

---

## AUDIT 2 — ARITHMETIC (recomputed from raw extract; A4 value vs my value vs source)

Raw P&L (Reg 33, Lakhs ×0.01→Cr): IntEarned 5,630.55 / 5,428.43 / 5,475.61; IntExp 2,709.97 / 2,632.84 / 2,718.37; OthInc 603.83 / 770.69 / 725.88; Opex 2,166.31 / 2,125.13 / 1,814.72 (Emp 1,358.32 / — / 1,123.61; OthOpex 807.99 / — / 691.11); PPOP 1,358.10 / 1,441.16 / 1,668.40; Prov 682.59 / 677.01 / 1,146.91; PBT 675.52 / 764.15 / 521.49; Tax 173.85 / 230.01 / 149.53; PAT 501.67 / 534.14 / 371.96. (order = Q1FY27 / Q4FY26 / Q1FY26). All 46 raw conversions verified against L162–L232.

| # | Metric | A4 value | My recompute | Source line(s) | Status |
|---|---|---|---|---|---|
| 1 | NII Q1FY27 | 2,920.58 | 5,630.55−2,709.97 = 2,920.58 (press 2,921) | L162/L176; press L720 | PASS |
| 2 | NII YoY | +5.9% | 163.34/2,757.24 = +5.93% | — | PASS |
| 3 | PPOP YoY | −18.6% | −310.30/1,668.40 = −18.60% | L186; deck 3.15 | PASS |
| 4 | C/I Q1FY27 | 61.5% | 2,166.31/3,524.41 = 61.47% | L178/calc; deck slide31 | PASS |
| 5 | C/I Q1FY26 | 52.1% | 1,814.72/3,483.12 = 52.10% | deck slide31 | PASS |
| 6 | Opex YoY | +19.4% | 351.59/1,814.72 = +19.37% | L178 | PASS |
| 7 | Employee cost YoY | +20.9% | 234.71/1,123.61 = +20.89% | L180 | PASS |
| 8 | IT opex YoY | +92.5% | (156.24−81.17)/81.17 = +92.49% | Note 11 L514–515 | PASS |
| 9 | Other income YoY | −16.8% | −122.05/725.88 = −16.82% | L172 | PASS |
| 10 | Provisions YoY (credit-cost relief) | −40.5% | −464.32/1,146.91 = −40.48% (press "40%") | L190; press L691 | PASS |
| 11 | PBT YoY | +29.5% | 154.03/521.49 = +29.54% | L193 | PASS |
| 12 | PAT YoY | +34.9% | 129.71/371.96 = +34.87% | L204; press L722 | PASS |
| 13 | Credit cost calc | 1.76%→1.8% | 682.59×4/155,555 = 1.755% | L190 / press L716; deck 3.12 | PASS |
| 14 | **PAT bridge** | NII +163.34; OthInc −122.05; Opex −351.59; ΔPPOP −310.30; Prov +464.32; ΔPBT +154.02; Tax −24.32; ΔPAT +129.71 | Every leg reproduces; −310.30+464.32=+154.02; 154.02−24.32=+129.70 (0.01 rounding) | Step 4 vs L162–L204 | PASS |
| 15 | ETR Q1FY27 | 25.7% | 173.85/675.52 = 25.74% | L193/L197 | PASS |
| 16 | Gratuity add-back (post-tax) | +45.20 | 60.83×(1−0.2574) = 45.19 | Note 10 L500 | PASS |
| 17 | Mgmt-adjusted PAT / ROA | ≈546.9 / ≈1.1% | 501.67+45.20 = 546.87; ROA 1.0→~1.1% | Step 4; deck ROA 1.0% | PASS |
| 18 | Excess-prov reversal | ₹5.36 Cr | 535.98 lakh ×0.01 = 5.36 | Note 6(iii) L400 | PASS |
| 19 | ARC principal / NBV / consideration | 291.44 / 114.13 / 119.49; SR nil | 29,143.83 / 11,413.00 / 11,948.98 lakh ×0.01; SR row dash | Note 6(iii) L388/390/392/401 | PASS |
| 20 | IFR-to-P&L transfer | ₹215.67 Cr | 21,567.42 lakh ×0.01 = 215.67 | Note 8 L438 | PASS |
| 21 | **Wholesale segment PBT** | −77.11 Cr | (7,711.03) lakh ×0.01 = −77.11 | Segment L263 | PASS |
| 22 | Wholesale annualized vs 400 tripwire | ~308 Cr; ~92 headroom | 77.11×4 = 308.44; 400−308 = 92 | L263 | PASS |
| 23 | Wholesale loss YoY | +82.7% | (77.11−42.20)/42.20 = +82.7% | L263 (Q1FY26 −42.20) | PASS |
| 24 | Wholesale assets YoY | +41% | (42,090.81−29,798.35)/29,798.35 = +41.3% | Segment L271 | PASS |
| 25 | Wholesale liabilities QoQ | −18.5% | (6,665.38−8,183.37)/8,183.37 = −18.55% | Segment L279 | PASS |
| 26 | **40 bps ROA-cut bridge** | ~30 NIM + ~10 opex | 30+10 = 40, quoted verbatim | concall turn 35 / L161 | PASS |
| 27 | **EEB 0-90 DPD** | 3.1%→3.5% (SMA0 1.5→1.8, SMA1 0.8→0.9, SMA2 0.8) | concall "increased to 3.5% from 3.1%"; deck slide24 sums 1.5+0.8+0.8=3.1 → 1.8+0.9+0.8=3.5 | concall L85; deck §18 | PASS |
| 28 | EEB non-paying | 0.4%→0.9% | deck slide23 paying-profile Mar 0.4 → Jun 0.9 | deck §17.6/17.7 | PASS |
| 29 | Gross slippages QoQ | +5% (1,079 vs 1,028) | (1,079−1,028)/1,028 = +4.96% | concall L58 | PASS |
| 30 | **GNPA write-off vs recovery recon** | GNPA fell ₹1.4bn on ₹12.2bn reductions, only ₹4.5bn genuine (6.0 tech w/o + 1.7 ARC + 4.5 rec = 12.2) | Seg GNPA 50.2→48.8 = −1.4bn ✓; 4.5+6.0+1.7 = 12.2 ✓ internally consistent; concall corroborates tech w/o 597, ARC 291 principal | deck §15.1-15.3; concall L60 | PASS |
| 31 | EPS YoY | +34.6% | (3.11−2.31)/2.31 = +34.6% | L219 | PASS |
| 32 | PPOP / PAT QoQ | −5.8% / −6.1% | −5.76% / −6.08% | L186/L204; deck 3.15/3.16 | PASS |
| 33 | CRAR QoQ | +11 bps | 18.15−18.04 = +11 bps (Reg 33 basis) | L215 | PASS |

### CRAR −114 bps — examined per task; **number correct, basis-label imprecise (non-gating)**
A4 writes (L166, L189): "CRAR still fell **114 bps** YoY **(19.08%→18.15%)**."
- On the **Reg 33 pair A4 puts in parentheses**, 19.08→18.15 = **−93 bps**, NOT −114 bps.
- The **−114 bps is real and source-disclosed** on the *including-profit* basis: press L725 (19.4%→18.2%, stated "−114 bps") and deck slide 29 (Jun'25 19.4% → Jun'26 18.2%). Q1FY27 Reg 33 18.15 already includes Q1 profit (Note 8); Q1FY26 Reg 33 19.08 does not — so 19.08→18.15 mixes bases and −93 is not itself a valid consistent-basis YoY.
- **Resolution:** the derived metric A4 reports (−114 bps YoY) is correct on the consistent incl-profit basis; A4's own Step 1L table (L102) correctly lists both the Reg 33 pair AND the press 19.4/18.2 pair. The only defect is the shorthand parenthetical pairing −114 with the Reg 33 numbers. This is a **citation-precision slip, not a computational error** — NOT counted as an arithmetic_mismatch and NOT verdict-gating. **Advisory to A4:** pair "−114 bps YoY" with "19.4%→18.2% incl profit," keeping "+11 bps QoQ" on the Reg 33 pair.

**ARITHMETIC VERDICT: PASS.** All 33 derived metrics + the PAT bridge + wholesale annualization + 40 bps bridge + write-off/recovery reconciliation reproduce within rounding. Zero mismatches above rounding. One non-gating basis-label advisory (CRAR).

---

## AUDIT 3 — ADVERSARIAL READ (3 most-positive A4 claims → strongest bear counter from same extract)

**Claim P1 — "Credit cost 1.8% is within the guided 1.6–1.8% band = met; management reaffirmed the 1.6–1.8% guide" (A4 Step 5L L194; concall L165).**
Bear counter (same text): 1.8% sits at the *top* of the band; EB-level credit cost is 3.3% (concall L95); gross slippages rose to 1,079 Cr (L58); 0-90 DPD 3.1→3.5% (L85); non-paying doubled 0.4→0.9% (deck §17.7); the GNPA headline is engineered by ₹597 Cr tech w/o + ₹291 Cr ARC (L60); and ₹120 Cr of the quarter's "recoveries" is one-off ARC cash (L221). The 1.8% is "met" via balance-sheet actions and an abnormally low charge that funds 100%+ of the PAT step-up — not via genuine asset-quality improvement.
**Survives? NO — already in A4.** Steps 4 (bridge), 5L (write-off-engineered, forward-flow), 8C, and C2 (INDETERMINATE earnings quality) already carry the entire substance.

**Claim P2 — "Secured-mix transition ON TRACK: secured 56.8%, non-EEB +27% YoY, diversification resilient" (A4 L244; press L649; deck 3.2/3.3).**
Bear counter (same text): the secured book is "~0% ROA" (analyst L169, unchallenged); wholesale is ROA-dilutive by management admission (L183), grew 38% YoY into a −77.11 Cr segment loss; and the fastest-growing wholesale sub-book carries non-prime credit — deck slide 14 (ledger §10.8): CBG rating mix has 16% BBB&Below + 8% Unrated/Others (24% sub-BBB+). The "on-track" mix shift is simultaneously the *cause* of the ROA-guidance cut and the C/I deterioration.
**Survives? NO (corroborating only).** A4 already flags the ROA-dilution and segment loss (L244 "WEAKENED (economics)", tripwire #2, Q4/F-04). The CBG rating granularity (24% sub-BBB+) is incremental colour within the already-flagged "low-quality, ROA-dilutive wholesale build" theme, not a new risk vector — does not require grafting.

**Claim P3 — "Ex-treasury non-interest income +22% YoY; TPP +47%; core fee income strong" (A4 L129/L152; concall L91).**
Bear counter (same text): reported non-interest income *fell* 16.8% YoY (725.88→603.83); the "+22%" rests entirely on stripping a ~₹250 Cr prior-year treasury gain — a self-serving reframing (deck §23.1) — and the current-quarter non-interest income line itself contains ARC/recovery one-offs: deck slide 30 (ledger rows 28/29/31) carries "Release of prov on redemption of SR (ARC)", "Collection fees from ARC", and "Bad Debts Recovery (on write-off)", into which the ₹5.36 Cr excess-prov reversal and part of the ₹120 Cr ARC cash flow. So even the ex-treasury "core" figure is partly non-recurring.
**Survives? NO — already hedged in A4.** A4 states the reported line "cannot be leaned on" (L129), flags the ₹250 Cr base and the +22% reframing (Q11/F16-6), and flags the ₹120 Cr ARC recovery as non-recurring (F-09, Step 4C-3). The specific slide-30 ARC income rows are unquantified in the extract, so the counter cannot be sized; substance is already carried. Does not require grafting.

**ADVERSARIAL VERDICT: PASS.** No bear counter survives as a new, material, extract-supported point absent from A4. A4's bear case is already complete and symmetric on all three positive claims.

---

## FINAL VERDICT

**COMPLETE.**

- COVERAGE: PASS — fresh enumeration reconciles to all three A2 ledgers; zero orphan rows; zero fresh rows missing from ledger.
- ARITHMETIC: PASS — all 33 derived metrics + PAT bridge + normalized PAT/ROA + wholesale −77.11 Cr / ~308 Cr annualization + 40 bps ROA bridge + CRAR QoQ + GNPA write-off/recovery reconciliation + EEB 0-90 DPD reproduce within rounding. Zero mismatches above rounding. Single non-gating advisory: CRAR −114 bps is correct on the incl-profit basis (press L725 / deck slide 29) but A4's parenthetical pairs it with the Reg 33 pair 19.08→18.15 (=−93 bps); recommend A4 pair −114 with 19.4%→18.2% incl-profit. Correct number, imprecise label — not a FAIL.
- ADVERSARIAL: PASS — no surviving bear counter to graft; A4 already carries the substance of every counter.

Only COMPLETE proceeds to Notion save. This review proceeds.

```yaml
stage: A5-adversary
company: "BANDHAN"
quarter: "Q1FY27"
model: claude-opus-4-8
status: complete
verdict: COMPLETE
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches: []
surviving_bear_counters: []
loop_back_to: ""
gap: ""
advisories:
  - "NON-GATING: CRAR -114 bps YoY is correct on the incl-profit basis (press L725 19.4%->18.2%; deck slide29); A4 L166/L189 pairs it with the Reg 33 pair 19.08%->18.15% (=-93 bps) — recommend A4 re-label to the incl-profit pair. Number correct, basis label imprecise; not an arithmetic FAIL."
  - "NON-GATING: concall ARC quantum 291cr (turn4/L87) vs 290cr (turn65/L221) is the same transaction; A4 correctly anchors to audited Note 6(iii) principal 291.44 Cr. Reviewed, no finding."
```
