# QUARTERLY PIPELINE A5 — ADVERSARY / COMPLETENESS AUDIT — Finkurve (Arvog) Q1 FY27

**Agent:** A5 ADVERSARY | **Model:** claude-opus-4-8 | Fresh context (A4 review + A1 extracts + A2 ledgers only; A3 reasoning not seen; all figures re-derived).
**Target:** `review_finkurve_q1fy27.md`. Line convention checked and adopted: results `L###` = OS file line of `extract_results_*` (= embedded +84); deck `S##/L###` where `L###` = deck embedded body line (1-1100); reg32 `R-L###` = reg32 embedded line.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate, run first)

Plain-Language Brief (review Section 6) — all four labelled parts present and carrying real, non-placeholder content:

| Part | Present? | Evidence |
|---|---|---|
| (1) Summary narrative | PRESENT | Section 6 "Summary narrative", ~18 lines, substantive (PAT 8.44, provision holiday, GNPA 6x, LTV 77.3, D/E ramp, disclosure gaps) |
| (2) SECTOR intelligence | PRESENT | "SECTOR INTELLIGENCE" heading; gold-loan macro (394 lakh Cr wealth, 17 lakh Cr market, 60% informal), LTV cyclicality, provenance-tagged |
| (3) BUSINESS-MODEL intelligence | PRESENT | "BUSINESS-MODEL INTELLIGENCE" heading; wholesale-borrow/gold-lend spread, 96% gold, Augmont RPT pass-through, Godrej off-book, cost-to-income drift |
| (4) COMPETITION intelligence | PRESENT | "COMPETITION INTELLIGENCE" heading; sub-scale challenger, LTV vs peer 57-61%, ROE trail, Muthoot-affiliated holder |

**Gate 0: PASS** — no missing/empty brief part.

---

## AUDIT 1 — COVERAGE (independent re-enumeration, diffed vs A2 ledgers)

Fresh grep/sweep counts vs A2:

| Category | A2 count | My fresh count | Orphan rows (ledger→absent from A4) | Status |
|---|---|---|---|---|
| RESULTS agenda items | 11 | 11 | none — all 11 in Step 0D table (L107-159) | PASS |
| RESULTS Limited-Review paras | 5 | 5 | none — para 4 (unmodified, L236) + para 5 (predecessor, L253-256) diffed; 1-3 boilerplate reviewed-no-finding | PASS |
| RESULTS Security-Cover paras | 9 | 9 | none — conclusion + cover ratios 1.14x/1.10x (L555) cited; responsibility paras reviewed-no-finding | PASS |
| Auditor paras total | 14 | 14 (5+9) | none | PASS |
| RESULTS notes | 8 | 8 | none — all 8 in Step 0D (L316-387) | PASS |
| RESULTS statement line items | 23 | 23 | none — Step 1L reproduces all | PASS |
| RESULTS ratios rows | 26 | 26 | none — D/E, DSCR, ISCR, NW, EPS x2, GNPA/NNPA/PCR/CRAR all used | PASS |
| CLA sub-table | 10 | 10 | none — WAR 19.96%, 44.23/37.86, NNPA 0.01 cited | PASS |
| Annexure 3 fields | 15 | 15 | none — 141.50/111.50/30, CRISIL cited | PASS |
| Annexure 4 fields | 15 | 15 | none — 199/135, dev "No", MA N/A cited | PASS |
| Appendix I asset/liab/cover rows | 30 | 30 | none material — Loans/Goodwill-nil/DTL 23.26 used; blank OCR rows correctly NOT_FOUND | PASS |
| PRES slides | 37 | 37 | none | PASS |
| PRES mgmt numbers | 253 | 253 | none material — headline KPIs, P&L, BS, ratios all used | PASS |
| PRES zero-standing | 7 | 7 | none | PASS |
| PRES footnotes (off-book) | 5 | 5 | none — F16-2 covers all 5 | PASS |
| PRES entities | 78 | 78 (79 boundary) | none material — Augmont, Godrej, Muthoot, RBL used | PASS |
| PRES guidance | 1 | 1 | none — 30-45 day rollout (S21/L675) used | PASS |
| REG32 disclosure units | 41 | 41 | none — 141.50/111.50/30 warrant, CRISIL, dev "No" cited | PASS |

**No orphan rows. No enumeration category my fresh pass found is missing from a ledger.**
Standalone-only verified independently: full-text sweep of `extract_results` confirms no "consolidated/subsidiary/standalone" token; Note 6 single segment (L348); Goodwill nil (L526). A4's N/A S-vs-C treatment is correct — no consolidated PAT gap silently present.
Every AMBIGUOUS/FORWARD-SIGNAL A3 finding produced a management question (20 Q's map to the 29 findings; NEUTRAL-FACT RES-F13-2/F14-4 correctly parked in governance register, not as questions).

**Two A2 ledger data-quality defects found (non-blocking — A4 overrode #1 correctly, #2 is a reconciliation A4 owns):**
- **A2 results ledger, line-item #2 (Fees & commission INCOME, L289):** ledger recorded Q1FY27 = **58.4 Lakhs (0.58 Cr)** and flagged it "suspect". Correct value = **5.84 Lakhs (0.06 Cr)**: the revenue subtotal ties only at 5.84 (7,478.68 + 5.84 + 25.79 = 7,510.31 = L291's 7,510.30). **A4 used 0.06 Cr correctly** via subtotal reconciliation, so no thesis impact — but the A2 ledger figure is wrong and should be corrected to 5.84 L (loop A2, cosmetic).
- **Neither ledger flagged the deck-vs-filing fee-EXPENSE cross-document mismatch** (each transcribed its own source faithfully). Reconciliation is A4's job — see Audit 2/3. This is the material item and loops to A4, not A2.

**Coverage verdict: PASS (0 orphan rows, 0 missing enumeration units).**

---

## AUDIT 2 — ARITHMETIC (every derived metric recomputed from raw extract lines)

Ties confirmed (recomputed independently, all within rounding):

| Metric | A4 value | My recompute | Source | Status |
|---|---|---|---|---|
| Interest income YoY | +181.2% | 7,478.68/2,659.83 = 2.812 → +181.2% | L288 | TIE |
| Finance cost YoY | +277.4% | 2,672.31/707.82 = 3.774 → +277.4% | L295 | TIE |
| NII Q1FY27 / YoY | 48.07 / +146.3% | 74.79−26.72=48.07; 48.07/19.52=2.463 | L288/L295 | TIE |
| PPOP flat | 11.41 vs 11.61, −1.7% | 11.21+0.20=11.41; 6.83+4.78=11.61; −1.72% | L303/L298 | TIE |
| PAT bridge | +4.38 PBT (prov +4.58, PPOP −0.20) | −0.20+4.58=+4.38; PBT 11.21−6.83=4.38 | L303/L298 | TIE |
| Reported PAT change | +3.35 (5.09→8.44) | 8.44−5.09=3.35 | L305 | TIE |
| Provision-normalised PBT haircut | ~47.6% | (11.21−5.87)/11.21=47.6%; 5.87=11.41−5.54; 5.54=2,217.18/4 | L298/L303 | TIE |
| GNPA / NNPA | 0.54% / 6.66 Cr; 0.48% / 5.96 Cr | 665.65 L=6.66; 596.11 L=5.96 | L380-383 | TIE |
| PCR / CRAR / D/E | 10.45% / 26.63% / 2.88 | as printed | L384/L385/L360 | TIE |
| DSCR / ISCR | 0.41 / 1.38 | as printed | L361/L362 | TIE |
| ETR Q1FY27 / Q1FY26 | 24.7% / 25.5% | 2.77/11.21=24.7%; 1.74/6.83=25.5% | L304/L303 | TIE |
| EPS anomaly (Basic<Diluted) | 0.50 < 0.58 | as printed; cross-table 0.60/0.59 | L313-314/L368-369 | TIE (real anomaly) |
| Employee YoY / QoQ | +240% / +150.8% | 1,347.08/396.45=+240%; /536.56=+151.1% | L299 | TIE (QoQ ~151%, rounding) |
| Total revenue YoY | +88.3% | 7,510.30/3,987.88=+88.3% | L291 | TIE (deck 88.32%) |
| Expense-line under-sum | ~6.06 Cr | 6,461.66−5,855.67=605.99 L=6.06 Cr | L295-302 | TIE (arithmetic correct — but mislocated, see Audit 3) |
| reg32 warrant reconciliation | 141.50−30=111.50 | 141.50−30.00=111.50 | R-L54/R-L77 | TIE |
| Annexure 4 excess | 199−135=64 | 199−135=64, dev "No" | L733/L758 | TIE |

**MISMATCHES (fail — return to A4):**

| # | Metric | A4 value | My recompute | Source | Severity |
|---|---|---|---|---|---|
| M1 | Fees & commission EXPENSE, Q1FY27 | **13.64 Cr** (L296), propagated through Step 1L, Step 4 opex, §3.2 ("13.64 Cr/qtr") | **19.70 Cr** — the filing's own total foots only at 19.70: 64.62 − (26.72+0.20+13.47+1.13+3.39) = **19.70**; and the **deck states 19.70 directly (S30/L938)**. Filing's printed "1,363.74"/13.64 (L296) is the erroneous line, and the 6.06 Cr difference (19.70−13.64) **is exactly A4's unexplained under-sum**. | L296 vs S30/L938 + L302/L303 | **MATERIAL** — A4 both used the wrong figure and, in the preamble, affirmatively claimed deck/filing "tie exactly … divergences are framing/omission, not arithmetic," which this falsifies. Augmont RPT pass-through this quarter is 19.70 Cr, not 13.64. |
| M2 | RoALA, Q1FY27 (derived-metrics table, review line 101) | **4.2%** (cited S29/L915) | **2.9%** — S29/L917 is the last/current point of the 4.2→3.9→3.7→3.3→**2.9** series; independent check PAT 8.44×4 / avg loan assets ≈ 2.9%. 4.2% is the **Q1FY26** value. A4 grabbed the wrong end of the series. | S29/L917 | Minor — A4's own tripwire text (review L267) already says "declining 4.2→2.9%", so the table cell self-contradicts. Correct the cell. |
| M3 | Net-worth decomposition | "Other Equity 330.90 (L311) + paid-up 14.01 (L310)" = 344.91, offered against Net worth **354.37** (L365) | Does not tie: 330.90 is **Mar'26** Other Equity (annual, L311 / deck S32/L1005), not Jun'26. Jun'26 implied Other Equity = 354.37−14.01 = 340.36. | L311 vs L365 | Minor — period-mixing; net-worth headline 354.37 itself is correct. |

Note: **RoAE 9.4% (S29/L901) for Q1FY27 was tested and stands.** Independent check PAT 8.44×4 / avg equity (344.9+354.4)/2 ≈ 9.7%, within rounding of 9.4%; the RoAE series is non-chronological in the linearised extract, but 9.4% is corroborated by computation (Q1FY26 RoAE computes to ~6.5%, so 9.4% cannot be the Q1FY26 point). No error — A4's ROE read is defensible.

---

## AUDIT 3 — ADVERSARIAL READ (three most positive claims; strongest bear counter from the SAME extract)

**Positive claim A — "The deck's audited headline KPIs all tie exactly to the filing; the deck's numbers are the filing's numbers; divergences are framing/omission, not arithmetic."** (Preamble, review L24.)
Bear counter: Deck fee-and-commission expense = **19.70 Cr (S30/L938)**; filing prints **13.64 Cr (L296)** — a **6.06 Cr arithmetic divergence**, not framing. The filing's total expenses (64.62, L302), reported PBT (11.21, L303), and the deck all corroborate **19.70** as the true figure, so the filing's 13.64 line is a genuine data error and the "tie exactly / not arithmetic" claim is false. This divergence is identically the size of A4's own unreconciled expense under-sum.
**SURVIVES → must be grafted into A4:** replace the "ties exactly / not arithmetic" language, set Q1FY27 fee expense = 19.70 Cr, and resolve the data-integrity question (Q18) by localising the error to the filing's fee-expense line rather than leaving it an open mystery.

**Positive claim B — "Capital is ample (CRAR 26.63%) … healthy capital headroom."** (Step 5L / narrative.)
Bear counter: On the deck's own Capital Adequacy series (S29/L901-905), the ratio **halved from 57.3% to 26.6% across five quarters** while D/E ran 0.73→2.88, and Board resolutions target Rs 5,000 Cr borrowing and a 4-4.5x D/E (L148). "Ample" describes the level but omits the trajectory: on a thin-PCR (10.45%), rising-GNPA book, a capital buffer that halved in a year is a diminishing, not a static, cushion.
**SURVIVES (moderate) → graft the CRAR trend (57.3→26.6) into Step 5L; the level-only framing understates the drawdown.**

**Positive claim C — "Interest income +181% / total revenue +88% = real book and leverage growth."** (Step 2 answer 1.)
Bear counter: Growth is provision-flattered — PPOP flat YoY (11.61→11.41), 100% of PBT growth is the 4.58 Cr provision release, normalised PAT ~4.4 Cr < prior 5.09 (Step 4).
**DOES NOT SURVIVE as new — already fully incorporated** (Step 2 answer 3, Step 4 bridge, §3.1). No graft needed.

Two surviving counters (A, B) require incorporation before save.

---

## VERDICT

**INCOMPLETE.** Loop back to **A4**.

Blocking gap (primary): **M1 / Adversarial claim A** — the review's Fees & commission EXPENSE for Q1FY27 is stated as 13.64 Cr (L296) and the preamble claims deck and filing "tie exactly … divergences are framing/omission, not arithmetic," but the deck states **19.70 Cr (S30/L938)** and the filing's own total (L302) and PBT (L303) foot only at **19.70**; the 6.06 Cr gap is exactly the review's unexplained expense under-sum. A4 must (i) correct Q1FY27 fee expense to 19.70 Cr in Step 1L / Step 4 / §3.2, (ii) resolve Q18 by localising the data-integrity error to the filing's printed fee-expense line (deck reconciles the total), and (iii) retract the "ties exactly / not arithmetic" claim.
Secondary graft: **Adversarial claim B** — add the CRAR trend (57.3%→26.6%, S29/L901-905) to the "ample capital" read.
Minor corrections (fix, non-thesis): **M2** RoALA Q1FY27 derived cell 4.2%→2.9% (S29/L917); **M3** net-worth decomposition mixes Mar'26 Other Equity (330.90) with Jun'26 net worth (354.37).
Ledger housekeeping (loop A2, cosmetic): results ledger fee-INCOME L289 Q1FY27 should read 5.84 L (0.06 Cr), not 58.4 L — A4 already used the correct 0.06.

**Counts:** coverage gaps = 0 orphan / 0 missing-enumeration (2 A2 value-accuracy notes); arithmetic mismatches = 3 (1 material M1, 2 minor M2/M3); surviving bear counters = 2 (A material, B moderate).

Coverage is complete and the core earnings-quality thesis (provision-flattered PAT, PPOP flat, spread compression, GNPA/LTV deterioration, disclosure gaps, INDETERMINATE cash-conversion → PROCEED WITH FLAGS) is sound and correctly anchored. It cannot proceed to Notion because A4 made an affirmative arithmetic-integrity claim that the same extract falsifies, and used the wrong fee-expense figure. Fix M1 + graft counters A and B, then re-verify.

```yaml
stage: A5-adversary
company: "finkurve"
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
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches:
  - {metric: "Fees & commission expense Q1FY27", a4_value: "13.64 Cr", recomputed: "19.70 Cr", source_line: "L296 vs deck S30/L938; foots via L302/L303 residual = 19.70; 6.06 Cr = A4 under-sum"}
  - {metric: "RoALA Q1FY27 (derived table)", a4_value: "4.2%", recomputed: "2.9%", source_line: "S29/L917 (4.2 is Q1FY26 endpoint); A4 tripwire text already says 2.9"}
  - {metric: "Net worth decomposition", a4_value: "330.90 + 14.01 = 344.91 vs NW 354.37", recomputed: "330.90 is Mar'26 Other Equity, not Jun'26", source_line: "L311 (Mar'26) vs L365 (Jun'26)"}
surviving_bear_counters:
  - {claim: "Deck KPIs tie exactly to filing; divergences framing/omission, not arithmetic (preamble)", counter: "Deck fee expense 19.70 != filing 13.64; 6.06 Cr arithmetic divergence = the review's own unexplained under-sum; filing 13.64 line is the error", source_line: "S30/L938 vs L296; L302/L303"}
  - {claim: "Capital ample (CRAR 26.63%), healthy headroom", counter: "CRAR halved 57.3%->26.6% in five quarters as D/E ran 0.73->2.88 with 5,000 Cr borrowing / 4-4.5x target; buffer eroding on thin-PCR rising-GNPA book", source_line: "S29/L901-905; L148/L360"}
loop_back_to: "A4"
gap: "A4 preamble claims deck/filing 'tie exactly, not arithmetic' and uses Q1FY27 fee expense 13.64 (L296); deck states 19.70 (S30/L938) and filing total (L302)/PBT (L303) foot only at 19.70 — the 6.06 Cr gap IS the review's unexplained expense under-sum. A4 must set fee expense=19.70, localise the data-integrity error to the filing fee line (Q18), retract 'ties exactly', graft CRAR-halved trend, and fix RoALA cell 4.2->2.9 (S29/L917)."
```
