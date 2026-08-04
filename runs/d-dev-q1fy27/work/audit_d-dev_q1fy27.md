# A5 ADVERSARY / COMPLETENESS AUDIT — DEE Development Engineers Ltd
**Ticker:** D-DEV | NSE DEEDEV | BSE 544198 | **Quarter:** Q1 FY27 (quarter ended 30 June 2026)
**Agent:** A5 ADVERSARY (fresh context: A4 review + A1 extracts + A2 ledgers only) | **Model:** claude-opus-4-8
**Review under attack:** review_d-dev_q1fy27.md
**Verdict:** INCOMPLETE (loop_back_to A4) — one hard coverage gap; all arithmetic and all other coverage pass.

Independence note: every figure below was recomputed from the A1 line-cited raw numbers (results Rs. Lakhs, lines 289-627; press release Rs. Crores, lines 74-79). I did not defer to A4's or A3's cites; I re-derived and then diffed.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate: PLAIN-LANGUAGE BRIEF, four parts)

| Part | Location | Present? | Content check |
|---|---|---|---|
| (1) Summary narrative | Section E, lines 438-448 | **present** | ~11 lines, real content (revenue/PAT/margin, Heavy-Fab clock, audit, cash, governance, decision) |
| (2) SECTOR intelligence | Section E, lines 450-454 | **present** | capex cycle, seamless-pipe/Anjar, Punjab tariff overhang; provenance caveat included |
| (3) BUSINESS-MODEL intelligence | Section E, lines 456-460 | **present** | piping engine vs subsidiary leg, ₹5.56 Cr uplift, finance-cost drag, cash unproven |
| (4) COMPETITION intelligence | Section E, lines 462-466 | **present** | super-duplex/Inconel capability, Heavy-Fab weakness, HRSG/BHEL unverifiable |

**Gate 0 result: PASS.** All four labelled parts present and non-empty.

---

## AUDIT 1 — COVERAGE (fresh grep/sweep vs A2 ledgers vs A4)

### 1A. Fresh enumeration vs A2 ledger (diff)

| Category | A2 count | My fresh count | Match | A1 lines |
|---|---|---|---|---|
| Board agenda items | 11 | 11 | yes | 34,41,52,61,80,88,103,110,115,122,130 |
| Annexures B–I | 8 | 8 | yes | 697,727,741,783,816,849,884,911 (Annexure A = results, not double-counted) |
| Standalone notes | 7 | 7 | yes | 361,365,368,369,370,381,395 |
| Consolidated notes | 7 | 7 | yes | 631,636,637,638,652,666,676 (line-671 date-header correctly excluded) |
| Consolidation entities | 6 | 6 | yes | 454-459 |
| Consol reportable segments | 4 | 4 | yes | Piping 598 / Power 599 / Heavy Fab 600 / Unallocated 601 |
| Standalone auditor paras | 5 | 5 | yes | 204,210,218,229,244 (para 5 = EoM) |
| Consolidated auditor paras | 9 | 9 | yes | 426,432,439,450,462,477,486,495,500 (para 5-6 qual, 7 EoM, 8-9 reliance) |
| Digital signatures (results doc) | 4 | 4 | yes | SA auditor 265, consol auditor 517, CMD 405, CMD 687 |
| Press headline metrics | 6 | 6 | yes | 74-79 |
| Press forward-looking claims | 9 | 9 | yes | Table 5 (65,89,91,106,115,119,128,138,145) |

No row my fresh pass found is missing from the A2 ledgers. **missing_from_ledger = [] (A2 clean).**

### 1B. Ledger-row / disclosure-unit coverage in A4

- **Standalone + consolidated notes (7+7):** all covered in Step 0D table (SA-1…SA-7 / C-1…C-7), lines 38-45. C-5 Malwa is the qualification note, extensively covered. **Covered.**
- **All 11 board agenda items:** Items 1(results),2(auth cap→Q7),3(Shikha remun→Q12),4(RPT landlord→Q14),5(Ashvika CSR→Q13),6(Sec 62(3)→Q5),10(AGM→Q16) individually cited. Items 7,8,9,11 (Bhisham-continuation, Shikha re-appt, Shruti re-appt, committee reconstitution) are routine, carry no A3 finding, and fall under the blanket "All rows reviewed" (line 16) + monitorable "AGM special resolutions." **Covered (no-finding routine items acceptable).**
- **All 8 annexures B–I:** B/C/D/E cited via Q5/Q7/Q13/Q14; F/G/H/I routine, covered under blanket review. **Covered.**
- **4 consolidated segments incl. Heavy Fabrication:** Piping (Step 2), Power (Q11, watch 2, trigger check), Heavy Fabrication (Step 2, Q2, watch 2, trigger 4, Step 8C — extensively), Unallocated (bridge). **Covered.**
- **6 headline press metrics + 9 forward-looking claims:** all six reconciled in Section B (lines 392-402); all nine forward-looking claims land in Monitorables / growth-trigger / Section B. **Covered.**

### 1C. A3-FINDING COVERAGE — **FAIL (2 orphaned findings) [RESOLVED in loop 1 — see RE-AUDIT below]**

A4 asserts (lines 18-20, and YAML line 488) it incorporated **all** findings: results A3-01…A3-17 and press A3-F01…A3-F09, and states (line 353) "Every A3 FORWARD-SIGNAL and AMBIGUOUS finding from BOTH forensics files generates at least one question."

Fresh grep of the entire review for each id:

- A3-01→Q9/Step2; A3-02→Q1; A3-03→Q9; A3-04→Q8; A3-05→Q8; A3-06→Q7; A3-07→Q5; A3-08→Q10; A3-09→Q6; A3-10→Q2; A3-11→Q11/Q19; A3-12→Q12; A3-13→Q13; A3-14→Q14; A3-15→Q16; A3-16→Q15. **(16 of 17 traced)**
- **A3-17 — ORPHAN.** Appears ONLY at line 19. Not in any question, watch, trigger (Step 6C references A3-16/12/13/14/04/05/10 — not 17), monitorable, or analysis. Its subject is never identified anywhere in the review.
- A3-F01→Q17; A3-F02→Q3; A3-F03→Q3/Q5/Q19; A3-F04→Q6; A3-F05→Q5; A3-F07→Q18; A3-F08→Q4; A3-F09→Q1/Q2. **(8 of 9 traced)**
- **A3-F06 — ORPHAN.** Appears ONLY at lines 20 and 488 (the two incorporation lists). Not in any question, watch, monitorable, Section B row, or brief.

**This was a coverage FAIL (loop 0).** A4 claimed 26 findings incorporated but substantively traced only 24. Two findings (A3-17 results; A3-F06 press) were listed as "incorporated" yet left zero trace in the deliverable. From loop-0 inputs (A4 + A1 + A2 only; the A3 forensics files were out of scope) I could not determine whether A3-17 / A3-F06 were FORWARD-SIGNAL/AMBIGUOUS (which per A4's own contract mandate a question) or informational; per conservative bias that was a FAIL naming the missing evidence.

---

## AUDIT 2 — ARITHMETIC RE-RUN (independent, from A1 raw lines)

All figures recomputed from source. Rounding tolerance = last printed digit.

| Metric | A4 value | My recompute | Source lines | Status |
|---|---|---|---|---|
| Consol Revenue YoY | +31.6% | (29,446.22−22,375.83)/22,375.83 = +31.60% | 541 | tie |
| Standalone Revenue YoY | +40.4% | (23,849.46−16,983.16)/16,983.16 = +40.43% | 289 | tie (confirms press = consol, not SA) |
| Consol Op EBITDA Q1FY27 | 4,974.61 | 2,005.43+1,500.77+1,716.30−247.89 = 4,974.61 | 554/549/550/542 | tie |
| Consol Op EBITDA Q1FY26 | 3,587.37 | 1,577.59+1,273.29+1,145.46−408.97 = 3,587.37 | 554/549/550/542 | tie |
| Consol Op EBITDA YoY | +38.7% | 1,387.24/3,587.37 = +38.67% | — | tie (press YoY col prints 38.7%) |
| Press "38.4%" artifact | rounding, true 38.7% | (49.7−35.9)/35.9 = 38.4% from *rounded* prints; unrounded 38.67% | 75 | **A4 correct — artifact, not mismatch** |
| Consol EBITDA margin Q1FY27 | 16.89% | 4,974.61/29,446.22 = 16.893% | 541/554/549/550/542 | tie |
| Consol EBITDA margin Q1FY26 | 16.03% | 3,587.37/22,375.83 = 16.033% | — | tie |
| Margin bps YoY | +86 bps | 16.893−16.033 = 0.86 pp | — | tie (press 86 bps) |
| Margin gap vs >19% guidance | ~210 bps | 19.00−16.89 = 2.11 pp = 211 bps | — | tie ("210+") |
| Consol PAT YoY | +22.4% | (1,608.30−1,313.94)/1,313.94 = +22.40% | 562 | tie (press 22.4%) |
| Press "22.9%" artifact | rounding, true 22.4% | (16.1−13.1)/13.1 = 22.9% from *rounded* prints; unrounded 22.40% | 77 | **A4 correct — artifact, not mismatch** |
| Consol PAT margin bps | (41) bps | 5.462%−5.872% = −0.41 pp | 562/541 | tie |
| Diluted EPS YoY | +22.1% | (2.32−1.90)/1.90 = +22.1% | 588 | tie (press "22.1" missing % glyph — cosmetic) |
| Standalone PAT YoY | +47.4% | (1,052.31−713.70)/713.70 = +47.44% | 310 | tie |
| SA↔Consol PAT gap Q1FY27 | 555.99 / 52.8% | 1,608.30−1,052.31 = 555.99; /1,052.31 = 52.83% | 562/310 | tie |
| Gap Q1FY26 / Q4FY26 | 84.1% / 36.5% | 600.24/713.70 = 84.10%; 739.63/2,027.87 = 36.47% | 562/310 | tie |
| Subsidiary PAT (para 8) | 555.96 (~100% of uplift) | line 497 = 555.96 vs gap 555.99 | 497 | tie |
| Component-auditor % of consol PAT | 34.6% | 555.96/1,608.30 = 34.57% | 497/562 | tie |
| PAT bridge PBT change | +427.84 | +1,387.24−227.48−570.84−161.08 = +427.84 = 2,005.43−1,577.59 | 554-562 | tie (fully articulates) |
| PAT bridge PAT change | +294.36 | 427.84−133.48 = 294.36 = 1,608.30−1,313.94 | 562 | tie |
| Consol ETR Q1FY27 / Q1FY26 | 19.8% / 16.7% | 397.13/2,005.43 = 19.80%; 263.65/1,577.59 = 16.71% | 561/557 | tie |
| Consol core PBT ex-OI YoY | +50.4% | (1,757.54−1,168.62)/1,168.62 = +50.40% | 557/542 | tie |
| Consol finance cost YoY | +49.8% | 570.84/1,145.46 = +49.84% | 550 | tie |
| Standalone finance cost YoY | +56.0% | 584.43/1,043.96 = +55.98% | 297 | tie |
| Consol depreciation YoY | +17.9% | 227.48/1,273.29 = +17.87% | 549 | tie |
| Consol Other Income YoY | −39.4% | −161.08/408.97 = −39.39% | 542 | tie |
| QoQ revenue off Q4 | −18.6% | (294.46−361.57)/361.57 = −18.56% | 541 | tie |
| Q4FY26 consol Op EBITDA | ₹63.6 Cr | 3,560.41+1,388.21+1,590.46−174.99 = 6,364.09 = ₹63.64 Cr | 554/549/550/542 | tie (confirms "record" holds only same-quarter YoY) |
| Heavy Fab revenue YoY | +3.7% | (1,534.93−1,480.06)/1,480.06 = +3.71% | 600 | tie |
| Heavy Fab result YoY | −7.2% | (367.66−396.03)/396.03 = −7.16% | 608 | tie |
| Heavy Fab assets YoY | +28.8% | (4,781.58−3,713.21)/3,713.21 = +28.77% | 619 | tie |
| Heavy Fab liab QoQ | +44.9% | (2,139.98−1,476.48)/1,476.48 = +44.94% | 625 | tie |
| Power segment liab YoY | +57% | (3,018.87−1,926.07)/1,926.07 = +56.74% | 624 | tie |
| Heavy Fab quarterly rev | ₹15.35 Cr | 1,534.93 × 0.01 | 600 | tie (vs ₹150 Cr bar) |
| Order book base implied | ~₹1,261 Cr | 2,428/1.925 = 1,261.3 Cr; not in filing | 87 | tie — **UNVERIFIABLE upheld** |
| Pending dilution | ~8.6% | 59,76,096/6,92,63,342 = 8.63% | 584 (+Notion count) | tie |

**Arithmetic result: PASS. Zero mismatches above rounding across ~40 recomputations. The PAT bridge fully articulates and ties both to PBT and to reported PAT.**

### 2A. Press-release YoY: artifacts vs genuine mismatches (as tasked)
The press-release **YoY columns themselves print 31.6% / 38.7% / 22.4%** (lines 74/75/77) and every one ties to the *unrounded* consolidated filing to two decimals. The "38.4%" and "22.9%" that A3-F07 flags arise only if you divide the *rounded display values* (49.7/35.9, 16.1/13.1). A4's conclusion — rounding artifacts, not data errors — is **correct and independently reproduced.** The only genuine defect is the missing "%" glyph on Diluted EPS "22.1" (line 79) — cosmetic, correctly carried as Q18.

### 2B. Annexure E "Rs. 2,000" unit resolution (as tasked) — **A4 upheld**
- Body line 91-92 states in words: "the Company has availed a **loan facility of Rs. 2,000 Crores** from Bank of India (Lead Bank) and a Consortium of Lenders." Annexure E line 789 prints a **bare "Rs. 2,000"** with no unit. The two are consistent on the figure "2,000"; the body supplies the unit "Crores." A4's resolution to **₹2,000 Crores** is textually correct.
- Plausibility vs "~₹687 Cr drawn": **no drawn-borrowings figure exists in this Q1 filing** — Reg 33 gives no balance sheet at Q1 (A4 Step 5 correct), so the ~₹687 Cr is a Notion/prior anchor, not a document figure. A ₹2,000 Cr **consortium working-capital SANCTION** (fund-based + large non-fund BG/LC limits, standard for an EPC/heavy-fabrication contractor) against ~₹600-687 Cr fund-based drawn and Notion net debt ₹602.57 Cr is **plausible, not a self-evident unit error.** Press line 96 corroborates: the Sec 62(3) relates to "existing working capital facilities approved in May 2025… does not relate to any new borrowing." A4 correctly (i) does not assert ₹2,000 Cr as drawn debt, (ii) routes the fund-based-vs-non-fund split and covenant headroom to Q5, and (iii) does not manufacture distress. **Faithful; no overstatement; no FAIL.** The residual is a genuine Annexure-E disclosure ambiguity that A4 resolved conservatively.

---

## AUDIT 3 — ADVERSARIAL READ (three most positive claims, strongest bear counter from the same extract)

**Positive claim 1 — "Growth is clean and recurring: consol core PBT ex-OI +50.4%; ~100% of PAT growth recurring; no favourable one-off; underlying stronger than PAT reads" (Step 2 diag 3, Step 4).**
Bear counter (same extract): the +50.4% is *consolidated*, but consol PAT grew only +22.4% while the parent standalone grew +47.4% — the entire subsidiary block (which houses Heavy Fabrication and the two biomass plants, the growth thesis) **decelerated**: Heavy Fab revenue +3.7% / result −7.2% (600/608), Power segment −120.86 loss with liabilities +57% YoY (607/624). Finance costs +49.8% and a rising ETR (16.7%→19.8%) are *recurring drags* that persist. **Counter survives** — but it is **already grafted** into A4 (Step 2 diag 3-4, SA↔consol gap para line 193, Heavy-Fab RED watch 2, Q11). No new graft required.

**Positive claim 2 — "Revenue +31.6% consol / +40.4% SA, comfortably ahead of 25% CAGR pace; had the ₹25 Cr deferral landed, ~+42%" (Step 2 diag 1).**
Bear counter (same extract): sequential revenue is **−18.6% QoQ off Q4** (541); the "+42% if deferral landed" rests on an **unverified management assertion** (press line 91, no line-item proof in the audited filing); the order-book "+92.5%" is **UNVERIFIABLE** (base absent, line 87). So "ahead of pace" leans on forward, unaudited claims. **Counter survives** — **already grafted** (Step 3 QoQ −18.6%, deferral flagged press-only Q3, order book UNVERIFIABLE Section B/Q4). No new graft required.

**Positive claim 3 — "Record Operating EBITDA ₹50 Cr, margin expanded +86 bps to 16.89%; margin path progressing" (Section B, Step 6D).**
Bear counter (same extract): "record" holds **only same-quarter YoY** — Q4 FY26 op EBITDA was **₹63.64 Cr, higher** (recomputed above); margin 16.89% is still **211 bps below the >19% guidance with no inflection**, and the +86 bps is off a soft comparator. **Counter survives** — **already grafted** (Section B "PARTIALLY CONFIRMED" line 398, Step 2 diag 2, margin AMBER/RED watch 1, Step 6D "DELAYED"). No new graft required.

**Adversarial-read result: all three bear counters survive but are ALREADY present in A4. No unincorporated surviving counter. This audit adds no FAIL.**

### 3A. Other adversarial checks (as tasked)
- **Audit-qualification characterisation (retained + Note 5 widened):** faithful. Para 5 (462) "unable to determine whether any impairment is required and the consequential impact"; para 6 (477) "except for the possible effects of our observation in para 5 above" = a genuine **qualified** conclusion. A4 labels it QUALIFIED — correct, and if anything conservative (not overstated). "Note 5 widened" language ("operational viability" line 662; "evaluation of strategic alternatives" line 665) is **verbatim present.** Caveat: the comparative "widened" rests on A3-04/A3-05 (no prior-quarter text in my inputs); the *current* text is faithfully represented and materially concerning, so no overstatement.
- **Decision Status held (flag not decide):** correct. Step 8 "8A decision: HOLD… No Decision Status change; findings FLAGGED"; closing "I flag; the human decides." Compliant with CLAUDE.md (flags propagate; no STOP).
- **INDETERMINATE cash conversion capped and named:** correct. Step 5 classifies INDETERMINATE, names missing evidence (no Q1 CFO/balance sheet under Reg 33), and states it "caps the verdict at PROCEED WITH CAVEATS… subsumed into FLAGS." Consistent with CLAUDE.md NEVER rule. **Faithful.**
- **19 management questions:** all 19 present and non-empty; each carries source-finding ids and line cites — **except** the two orphaned findings A3-17 and A3-F06 which generate no question (Audit 1C).

---

## VERDICT (loop 0)

**INCOMPLETE.**

Everything material passes: deliverable-completeness gate (four brief parts), all A2 ledger enumeration, ~40 recomputed metrics (zero arithmetic mismatch, PAT bridge ties), the press-release rounding-artifact adjudication, the Annexure-E ₹2,000 Cr resolution, the qualified-audit characterisation, the held Decision Status, and the capped INDETERMINATE cash reading. All three strongest bear counters are already grafted.

The single blocking gap is coverage of A3 findings: **A4 lists A3-17 (results) and A3-F06 (press) as "incorporated" (lines 18-20, YAML line 488) but neither appears anywhere else in the review.** loop_back_to: A4 to disposition each.

```yaml
stage: A5-adversary
company: "D-DEV"
quarter: "Q1FY27"
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
    - "A3-17 (results forensic): listed incorporated at review l.19 & YAML l.488, but absent from every question/watch/trigger/monitorable/analysis; no question generated"
    - "A3-F06 (press forensic): listed incorporated at review l.20 & YAML l.488, but absent from every question/watch/monitorable/Section-B row; no question generated"
  missing_from_ledger: []
arithmetic_mismatches: []
surviving_bear_counters: []   # all three survive but are already present in A4; none requires new graft
loop_back_to: "A4"
gap: "A4 claims 26 A3 findings incorporated (lines 18-20, YAML l.488) but only 24 are traceable in the review. A3-17 (results) and A3-F06 (press) appear ONLY in the incorporation lists and generate no management question, watch, trigger, or monitorable, contradicting A4's own rule (l.353) that every FORWARD-SIGNAL/AMBIGUOUS finding yields >=1 question and the blanket 'All rows reviewed' claim (l.16). A4 must, for each: cite where it is addressed, or add the mandatory question if FORWARD-SIGNAL/AMBIGUOUS, or explicitly mark 'reviewed - no question required' with reason. Not resolvable from A5 inputs (A3 files not in scope), so failed per conservative-bias rule."
```

---
---

# RE-AUDIT (loop 1) — closing the single blocking gap

**Scope:** per coordinator instruction, I verified ONLY the delta that closed loop-0's single gap (A3-17, A3-F06 disposition). The loop-0 body above stands unchanged in full — coverage of all A2 ledger rows, ~40 arithmetic recomputations, the Annexure-E ₹2,000 Cr resolution, the audit-qualification characterisation, Decision-Status-held/flagged, the INDETERMINATE cash cap, and the four-part plain-language brief were all upheld and were NOT re-litigated. This run also confirmed nothing in the touched region regressed.

For loop 1 I was granted access to the two A3 source forensics files (out of scope in loop 0), so I can now verify the NEUTRAL-FACT classifications at source rather than inferring.

### Check 1 — Are A3-17 and A3-F06 genuinely NEUTRAL-FACT at source (not misclassified to dodge a question)?

- **A3-17 (forensics_results, line 28; YAML line 133):** classification column reads **NEUTRAL-FACT**. Content = drafting inconsistencies (header typos "Uudited"/"udited"; entity "Relationship" column populated only for rows 1 and 4 of the 6-entity table; finance/depreciation line-item reordering SA vs consol), described verbatim as "Individually immaterial; cumulatively a controls data point alongside A3-16." Corroborated by the checklist scorecard (F14, line 49) and — decisively — by the machine arrays: `forward_signals` (line 134) = [A3-01,02,05,06,07,08,15] and `ambiguous` (line 135) = [A3-03,09,11,12,13,14,16]. **A3-17 is in neither array.** Classification is genuine, not a dodge.
- **A3-F06 (forensics_presentation, line 21; YAML line 129):** classification column reads **NEUTRAL-FACT**. Content = entity name rendered four ways incl. undefined "DDEL" (lines 23/59/68/157), "logged as a cumulative drafting/governance data point." Corroborated by scorecard (F14, line 45) and the arrays: `forward_signals` (line 133) = [A3-F02,F04,F05] and `ambiguous` (line 134) = [A3-F01,F03,F07,F08,F09]. **A3-F06 is in neither array.** Classification is genuine, not a dodge.

Both are legitimately NEUTRAL-FACT (immaterial drafting/branding artifacts, no numeric or thesis bearing). Neither is FORWARD-SIGNAL nor AMBIGUOUS, so A4's own mandatory-question rule (review line 359) does not attach. **PASS.**

### Check 2 — Are the Section 0 dispositions present, and do their cross-references (Q15, Q17, Q18) exist in the review?

- New **"Coverage of non-actionable findings"** note present at review lines 24-28, applying disposition (c) to each with a one-line reason:
  - A3-17 (line 25): reason = immaterial drafting/controls artifacts; the underlying controls concern "already carried actively as management question Q15 (SIG_BEFORE_CONCLUSION signature-sequencing) and in the governance-cluster flag."
  - A3-F06 (line 26): reason = cosmetic branding inconsistency; substantive press-release disclosure-quality concerns "already carried as questions Q17 and Q18."
- Cross-reference existence verified in the live question table:
  - **Q15** present (line 377): CMD signatures 10:49:58/10:50:53 predate stated 10:52 conclusion — source A3-16. ✓
  - **Q17** present (line 379): press Financial Summary carries no standalone/consolidated label — source A3-F01. ✓
  - **Q18** present (line 380): headline YoY tie only on unrounded numbers; missing EPS "%" glyph — source A3-F07. ✓
  All three cross-references resolve to real, on-point questions. The dispositions are accurate (A3-17's controls angle genuinely overlaps Q15; A3-F06's disclosure-quality angle genuinely overlaps Q17/Q18). **PASS.**

### Check 3 — Are all 26 findings now accounted for?

24 findings drive a question/watch/trigger/Section-B row/monitorable (loop-0 Audit 1C trace, unchanged); the remaining 2 (A3-17, A3-F06) are now explicitly dispositioned as NEUTRAL-FACT "reviewed, no question required" in Section 0 and mirrored in YAML `findings_disposition.non_actionable_neutral_fact: ["A3-17","A3-F06"]` (lines 495-496). 24 + 2 = **26/26 accounted for.** The blanket "All rows reviewed" claim (line 16) is no longer contradicted. **PASS.**

### Check 4 — Did anything else regress?

- Management-questions count = **19, unchanged** (table still ends at Q19, line 381); Step 8.5 header (line 359) now correctly excludes the two NEUTRAL-FACT items.
- Protocol verdict = **PROCEED WITH FLAGS** (YAML line 497); Decision Status = **HELD**; cash = **INDETERMINATE** cap intact (line 498). Unchanged.
- The fix is additive (a new Section 0 note + a YAML `findings_disposition` block + two parenthetical pointers at lines 359 and 28). No arithmetic table, reconciliation, trigger, or brief content was altered. No regression detected. **PASS.**

### RE-AUDIT VERDICT

**COMPLETE.** The sole loop-0 blocking gap is closed and independently verified against the A3 source forensics: A3-17 and A3-F06 are genuinely NEUTRAL-FACT (present in neither forensics file's `forward_signals` nor `ambiguous` array), so no mandatory question attaches; disposition (c) is applied with accurate, existing cross-references (Q15/Q17/Q18); all 26 findings are accounted for; nothing regressed. No new gap surfaced. This review proceeds to Notion save.

```yaml
stage: A5-adversary
loop: 1
company: "D-DEV"
quarter: "Q1FY27"
model: claude-opus-4-8
status: complete
verdict: COMPLETE
delta_verified:
  a3_17_neutral_fact_at_source: true      # forensics_results l.28/133; absent from forward_signals & ambiguous arrays
  a3_f06_neutral_fact_at_source: true     # forensics_presentation l.21/129; absent from forward_signals & ambiguous arrays
  section0_disposition_present: true      # review l.24-28, disposition (c) with reasons
  crossrefs_exist: ["Q15","Q17","Q18"]    # review l.377/379/380 — all present and on-point
  findings_accounted: "26/26"             # 24 actionable + 2 NEUTRAL-FACT dispositioned
  questions_count_unchanged: 19
  protocol_verdict_unchanged: "PROCEED WITH FLAGS"
  decision_status_unchanged: "HELD"
  regression_detected: false
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
