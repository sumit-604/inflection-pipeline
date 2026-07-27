# A5 ADVERSARY / COMPLETENESS AUDIT — Tejas Networks (TEJASNET), Q1 FY27
# Fresh context: A4 review + A1 extracts + A2 ledgers only. Re-derived independently; A4/A3 cites checked, not trusted.
# Three audits run in one pass: COVERAGE, ARITHMETIC, ADVERSARIAL READ. Verdict: COMPLETE / INCOMPLETE.

---

## AUDIT 1 — COVERAGE (fresh grep pass vs A2 ledgers, then ledger-vs-A4)

Fresh enumeration re-run from the three A1 extracts. Every A2 count reproduced independently below; then each ledger row checked for citation in A4 (or blanket reviewed-no-finding).

### 1a. Results ledger — fresh recount vs A2

| Category | A2 count | My fresh count | Basis of my recount | Orphan rows (ledger absent from A4) | Status |
|---|---|---|---|---|---|
| notes | 14 | 14 | Std 1–6 (l.212,216,218,221,223,225) + Cons 1–8 (l.420,431,436,439,460,464,467,471). Note 5 OCR'd "5S" at l.223 confirmed. | none — all 14 mapped in A4 table 0D | PASS |
| line_items | 76 | 76 | Std P&L 36 rows (l.153–191, two OCR-split rows collapsed) + Cons 37 rows (l.359–398, +FX-translation row) + Cons Note-4 summary 3 rows (l.449,451,453). | none — reproduced in A4 tables 1A/1B; OCI/remeasurement/TCI lines carried under A4 blanket "all reviewed" + F9 for the hedge line | PASS |
| zero_standing | 5 | 5 | Std: current tax l.171, tax-on-remeasurement l.179, tax-on-hedge l.182. Cons: tax-on-remeasurement l.385, tax-on-hedge l.389. | none — Step 4 cites zero current tax l.171; Cons current-tax divergence (l.377) shown in A4 table 1B | PASS |
| agenda_items | 1 | 1 | Board approval of unaudited results only (l.29–33); no AGM/dividend/record-date/ESOP/capital-raise keyword hits. | none — A4 Step 8.5 Q8 probes single-item meeting | PASS |
| auditor_paras | 11 | 11 | Std 4 numbered (l.73–107) + Cons 6 numbered (l.260–333) + 1 unnumbered SEBI 33(8) para (l.290–292). | none — A4 0D covers unmodified opinion, Other-Matters para (l.325–333) | PASS |
| entities | 4 | 4 | Holding + 3 subs (Singapore/Nigeria/Saankhya), each listed twice (l.309–314 auditor, l.420–429 note 1). | none — A4 note Cons 1; naming variants → A3-F14 | PASS |
| signature_blocks | 5 | 5 | CS digital sig l.44–49; PW Partner std l.109–120 & cons l.334–340; CEO std l.227–230 & cons l.474–477. | none — meeting-timing/sign-off addressed; boilerplate blocks reviewed-no-finding | PASS |

### 1b. Presentation ledger — fresh recount vs A2

| Category | A2 count | My fresh count | Basis | Orphan rows | Status |
|---|---|---|---|---|---|
| pages_slides | 3 | 3 | page markers l.15/57/98 (doc lines 1/43/84) | none | PASS |
| table_line_items | 3 | 3 | Net Revenue, PBT, PAT (l.72–74) | none — A4 uses press-release table | PASS |
| table_data_points | 9 | 9 | 3 rows × 3 periods (402/202/1,103; (271)/(297)/(1,354); (202)/(194)/(909)) | none | PASS |
| mgmt_numbers | 10 | 10 | MD quote 4 (100G,400G,5G×2) + CFO quote 6 (402,21%,1,529,4,277,4,866,589) | none — all 6 CFO figures used in A4 Step 5; MD specs in 6D | PASS |
| highlight_bullets | 4 | 4 | GPON Tier-1; power-utility selection; Africa DWDM; 46/722 patents (l.73–78) | none — A4 6D + Step 7 + Q6 | PASS |
| entities | 3 | 3 | Tata Group, Panatone Finvest, Tata Sons (l.91–92) | none — A4 cites Tata parentage l.91–92 | PASS |
| business_profile_nums | 1 | 1 | "75 countries" (l.91) | none — A4 6D cites 75 countries | PASS |
| zero_standing | 0 | 0 | all 9 P&L cells non-zero across 3 periods | n/a | PASS |

### 1c. Reg30 SMP extract (no A2 ledger — governance companion)
COO Preetham Uthaiah designated SMP effective 2026-07-27, ex-Saankhya Labs, ex-Tech Mahindra VP (l.33, 77–88). Fully carried by A4 Step 8.5 Q9 and Step 9. No ledger exists, so no orphan possible; content is not dropped. PASS.

**COVERAGE RESULT: no orphan rows (no ledger row absent from A4); no fresh row my pass found that the ledgers lack. Both A2 count tests reproduced exactly. PASS.**

---

## AUDIT 2 — ARITHMETIC (every derived metric recomputed from raw extract digits)

Raw inputs taken from results extract (Std l.156–191; Cons l.362–398) and press-release CFO quote (l.80–82). "Δrnd" = my value minus A4 value.

### 2a. Standalone derived metrics

| Metric | A4 value | Recomputed | Source lines | Status |
|---|---|---|---|---|
| Op EBITDA Q1FY27 = PBT+D+FC−OI | (100.39) | −270.81+94.35+85.04−8.97 = (100.39) | 169,165,164,157 | PASS |
| Op EBITDA Q1FY26 | (135.78) | −297.38+96.46+74.69−9.55 = (135.78) | 169,165,164,157 | PASS |
| Op EBITDA Q4FY26 | (125.39) | −287.92+100.84+72.01−10.32 = (125.39) | 169,165,164,157 | PASS |
| Op EBITDA FY26 | (689.65) | −1361.53+402.73+302.61−33.46 = (689.65) | 169,165,164,157 | PASS |
| Op EBITDA margin Q1FY27 | −24.98% | −100.39/401.95 = −24.98% | 156 | PASS |
| Op EBITDA margin Q1FY26 | −67.24% | −135.78/201.93 = −67.24% | 156 | PASS |
| Reported EBITDA Q1FY27 | (91.42) | −270.81+94.35+85.04 = (91.42) | 169,165,164 | PASS |
| Core PBT ex-OI Q1FY27 | (279.78) | −270.81−8.97 = (279.78) | 169,157 | PASS |
| Gross Profit Q1FY27 | 144.78 | 401.95−(132.08+16.04+109.05) = 144.78 | 156,160,161,162 | PASS |
| Gross Profit Q4FY26 | 122.72 | 331.76−(297.07+51.53−139.56) = 122.72 | 156,160,161,162 | PASS |
| Gross Margin Q1FY27 | 36.02% | 144.78/401.95 = 36.02% | 156 | PASS |
| Gross Margin Q1FY26 | 42.42% | 85.65/201.93 = 42.42% (42.417) | 156 | PASS |
| ETR Q1FY27 = Tax/PBT | 25.32% | 68.57/270.81 = 25.32% | 172,169 | PASS |
| ETR Q1FY26 | 34.79% | 103.47/297.38 = 34.79% | 172,169 | PASS |
| ETR Q4FY26 | 24.12% | 69.46/287.92 = 24.12% | 172,169 | PASS |
| PAT Margin Q1FY27 | −50.31% | −202.24/401.95 = −50.31% | 174,156 | PASS |

### 2b. Consolidated derived metrics

| Metric | A4 value | Recomputed | Source lines | Status |
|---|---|---|---|---|
| Op EBITDA Q1FY27 | (100.36) | −270.81+94.35+85.07−8.97 = (100.36) | 375,371,370,363 | PASS |
| Op EBITDA Q4FY26 | (118.20) | −280.80+100.84+72.04−10.28 = (118.20) | 375,371,370,363 | PASS |
| Op EBITDA Q1FY26 | (135.67) | −297.35+96.46+74.77−9.55 = (135.67) | 375,371,370,363 | PASS |
| Op EBITDA FY26 | (681.83) | −1354.01+402.73+302.83−33.38 = (681.83) | 375,371,370,363 | PASS |
| Op EBITDA margin Q1FY27 | −24.96% | −100.36/402.16 = −24.96% | 362 | PASS |
| Reported EBITDA Q4FY26 | (107.92) | −280.80+100.84+72.04 = (107.92) | 375,371,370 | PASS |
| Core PBT ex-OI Q1FY27 | (279.78) | −270.81−8.97 = (279.78) | 375,363 | PASS |
| Gross Profit Q1FY27 | 144.98 | 402.16−(132.09+16.04+109.05) = 144.98 | 362,366,367,368 | PASS |
| Gross Margin Q1FY26 | 42.42% | 85.67/201.98 = 42.42% (42.415) | 362 | PASS (rounds up; verified) |
| Gross Margin Q1FY27 | 36.05% | 144.98/402.16 = 36.05% | 362 | PASS |
| ETR Q1FY26 = Tax/PBT | 34.80% | 103.48/297.35 = 34.80% | 379,375 | PASS |
| ETR Q4FY26 | 24.74% | 69.46/280.80 = 24.74% | 379,375 | PASS |
| PAT Margin Q1FY27 | −50.29% | −202.24/402.16 = −50.29% | 380,362 | PASS |

### 2c. YoY / QoQ / bridge / gap checks

| Metric | A4 value | Recomputed | Source | Status |
|---|---|---|---|---|
| Std revenue YoY | +200.02 / +99.05% | 401.95−201.93=+200.02; /201.93=99.05% | 156 | PASS |
| Cons revenue YoY | +200.18 / +99.11% | 402.16−201.98=+200.18; /201.98=99.11% | 362 | PASS |
| Std Op EBITDA margin YoY | +42.26 pp | −24.98−(−67.24) | derived | PASS |
| Std finance cost YoY | +10.35 / +13.86% | 85.04−74.69=+10.35; /74.69=13.86% | 164 | PASS |
| Std core PBT YoY | +27.15 / +8.85% | −279.78−(−306.93); /306.93 | derived | PASS |
| Std reported PBT YoY | +26.57 / +8.93% | −270.81−(−297.38); /297.38 | 169 | PASS |
| Std PAT YoY | −8.33 / +4.30% deeper | −202.24−(−193.91)=−8.33; /193.91 | 174 | PASS |
| Deferred-tax swing YoY | −34.90 (shield shrank) | 68.57−103.47=−34.90 | 172 | PASS |
| Tax@34.79% counterfactual PAT | ~(176.6) | −270.81+ (270.81×0.3479=94.22) = (176.59) | derived | PASS |
| Std revenue QoQ | +70.19 / +21.16% | 401.95−331.76=+70.19; /331.76=21.16% | 156 | PASS (matches CFO 21%, l.80) |
| Std PAT QoQ | +16.22 / 7.42% | −202.24−(−218.46)=+16.22; /218.46 | 174 | PASS |
| Gross margin QoQ | −0.97 pp | 36.02−36.99 | derived | PASS |
| S-vs-C PAT gap Q4FY26 | +7.12 / 3.26% | −211.34−(−218.46)=+7.12; /218.46=3.26% | 380,174 | PASS |
| S-vs-C PAT gap Q1FY27 | 0.00 / 0.00% | −202.24−(−202.24)=0.00 | 380,174 | PASS |
| S-vs-C PAT gap FY26 | +7.54 / 0.82% | −908.89−(−916.43)=+7.54; /916.43 | 380,174 | PASS |
| Net debt (CFO quote) | 4,277 | 4,866−589=4,277 | 82,81 | PASS |
| Net debt QoQ | +746 | 4,277−3,531 | 81 + memory | PASS |
| Gross debt QoQ | +831 | 4,866−4,035 | 82 + memory | PASS |
| Revenue annualised | ~1,608 | 401.95×4=1,607.8 | 156 | PASS |
| Q2–Q4 avg to clear ₹2,000 | ~533/qtr | (2,000−402)/3=532.7 | derived | PASS |
| DTA build to ~434 | ~434 | 365+68.57=433.6 | 172 + memory | PASS |
| Hedge OCI swing (Q5) | 14.50 | −7.72−(+6.78)=−14.50 | 181/387 | PASS |
| PAT bridge Std (all rows) | ties to +26.57 PBT / −8.33 PAT | recomputed each expense delta l.160–167; nets to +26.57 PBT; −34.90 tax → −8.33 PAT | 156–174 | PASS |

**ARITHMETIC RESULT: 0 mismatches above rounding.** The two ₹0.01-level gross-margin roundings (Std & Cons Q1 FY26 = 42.42%) were re-verified to the third decimal (42.417% / 42.415%) and both correctly round to 42.42% — not errors. Every EBITDA, margin, ETR, YoY, QoQ, S-vs-C gap, debt identity and the PAT bridge reproduce A4 exactly. PASS.

---

## AUDIT 3 — ADVERSARIAL READ (three most-positive A4 claims; strongest bear counter from the SAME extract)

**Positive claim 1 — "Revenue nearly doubled YoY (+99%), a real and sequential recovery off the FY26 trough" (A4 l.153, 178, 202).**
Strongest bear counter from the same text: the +99% is measured off Q1 FY26, the trough print (A4 concedes base-inflation); ₹402 Cr annualises to ₹1,608 Cr, BELOW the ₹2,000 Cr thesis-break floor; the QoQ base (Q4 FY26) is a note-5 balancing figure; and the ₹402 Cr quarter's margin is flattered by the ₹109.05 Cr inventory draw-down (Change-in-inventories flip −26.84→+109.05, l.162) plus a ₹3.10 Cr obsolescence CREDIT vs an ₹18.04 Cr Q4 charge (note 3, l.218).
Survives? NO. Every element is already in A4 — base-inflation (Step 2C.1), annualised-below-floor (2C.1, 6C, flag list), balancing-figure caveat (Step 3, note 5), inventory-credit flattery (Step 3 one-off distortion). Nothing to graft.

**Positive claim 2 — "Reported PAT 'worsening' is a tax-shield optical, not operations; core PBT improved +₹27 Cr" (A4 l.181, 230, 434).**
Strongest bear counter from the same text: the entire ₹68.57 Cr tax line is a non-cash deferred-tax BENEFIT with zero current tax every period (l.171–172); the "improving core" is still operating-EBITDA-NEGATIVE at −24.98% margin (loses money before D&A and finance); finance costs are the one adverse scaler (+13.86% YoY, l.164) and will compound on the +₹746 Cr net-debt build; and the shrinking tax benefit is itself a recoverability warning since the DTA is ~52% of equity and growing.
Survives? NO. A4 carries all of it — operating-EBITDA-negative stated explicitly (Step 2C.2), DTA 52%-of-equity growing exposure (Step 4, TBC, Q4, flag list), finance-cost adverse scaler (Step 2C.5, Step 4). Symmetric already.

**Positive claim 3 — "International traction strengthening; growth triggers ON TRACK / STRENGTHENING (5G South America first win, Africa DWDM, GPON Tier-1, 46/722 patents)" (A4 l.332, 436, 6D).**
Strongest bear counter from the same text: every win is UNQUANTIFIED — no order value/customer/volume for Africa DWDM (l.76–77), the power utility is only a "vendor selection" not a booked order (l.74–75), South America is a "first commercial win" with no rupee magnitude (l.65); international mix (#6) is NOT numerically disclosable (single segment, note 2); and the order book barely moved (+₹15 Cr to ₹1,529 Cr, l.81) on a ₹402 Cr revenue quarter with undisclosed BSNL inclusion.
Survives? NO. A4 flags every point — unquantified wins → A3-F16-02 / Q6 (Step 8.5); order-book flat + BSNL scope → A3-F16-01 / Q3; international mix UNKNOWN (Step 6B #6); selection-vs-order distinction (Q6). Fully incorporated.

**ADVERSARIAL RESULT: 0 surviving bear counters.** Each of the three strongest bears is already present, symmetrically and with the same source lines, in A4. No counter needs grafting; A4's bull-bear symmetry holds. PASS.

---

## VERDICT

**COMPLETE.** All three audits pass. Coverage: both A2 count tests reproduced exactly (results 7 categories, presentation 9 categories); zero orphan ledger rows and zero rows my fresh pass found that the ledgers lack; the reg30 SMP companion is fully carried by A4. Arithmetic: every derived metric (Std + Cons EBITDA/margins/ETR, all YoY/QoQ, the standalone PAT bridge, S-vs-C PAT gaps, and the CFO-quote debt identity 4,866−589=4,277) recomputed from raw extract digits with 0 mismatches above rounding. Adversarial: the three most-positive claims each have a real bear counter, but all three are already incorporated in A4 — none survives as new. No loop-back to A2, A3, or A4 required. Proceeds to Notion save.

```yaml
stage: A5-adversary
company: "TEJASNET"
quarter: "Q1 FY27"
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
```
