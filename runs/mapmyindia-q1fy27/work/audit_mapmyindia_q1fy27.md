# A5 ADVERSARY / COMPLETENESS AUDIT — MapmyIndia (C.E. Info Systems Ltd) — Q1 FY27

Agent: A5 ADVERSARY | Model: claude-opus-4-8 | Fresh context (A4 review + A1 extracts + A2 ledgers only; A3 reasoning not consulted, cites re-derived).
Unit rule applied independently: results filing Lakhs x0.01 = Rs Cr; presentation and press release already Rs Cr.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate, run first)

The MANDATORY PLAIN-LANGUAGE BRIEF (review lines 460-476) carries all four labelled parts, each with real, non-placeholder content AND a "Provenance:" label:

| Brief part | Heading present | Content | Provenance-labelled | Status |
|---|---|---|---|---|
| (1) Summary narrative | Part 1 (l.462-464), ~18 lines | Yes — numbers-anchored, decision stated | Yes (l.464) | PRESENT |
| (2) Sector intelligence | Part 2 (l.466-468) | Yes — AEG demand read, govt lumpiness, AI tailwind | Yes (l.468) | PRESENT |
| (3) Business-model intelligence | Part 3 (l.470-472) | Yes — Map-led vs IoT-led economics, treasury, subsidiary drag | Yes (l.472) | PRESENT |
| (4) Competition intelligence | Part 4 (l.474-476) | Yes — moat, OEM wins, Gtropy commoditisation, Google/HERE/TomTom | Yes (l.476) | PRESENT |

Gate 0: PASS (4/4 present, non-empty, provenance-separated from prior Notion work).

---

## AUDIT 1 — COVERAGE (independent re-enumeration vs A2 ledgers)

I re-swept each A1 extract and diffed my fresh counts against each ledger, then checked every flagged/finding-bearing row resolves into A4 (cited) or is a reviewed no-finding.

### 1A. Results ledger

| Category | A2 count | My fresh count | Orphan rows (in ledger, absent from A4) | Status |
|---|---|---|---|---|
| agenda_items | 2 | 2 (l.45 results approval; l.53 Nikhil Kumar cessation) | none | MATCH |
| auditor_paras | 11 | 11 (consol 1-7 l.94/102/109/119/153/159/168 + standalone 1-4 l.365/371/377/385) | none | MATCH |
| notes | 12 | 12 (consol N1-6 + standalone N1-6) | none | MATCH |
| entities | 6 | 6 (l.123-131) | none | MATCH |
| line_items | 77 | 77 (65 main-statement + 12 note breakup rows) | none | MATCH |
| signature_blocks | 7 | 7 | none | MATCH |
| annexure_rows | 5 | 5 (a-e) | none | MATCH |
| zero_standing | 0 | 0 | none | MATCH |

Flagged rows traced into A4: OTHER_MATTER / UNAUDITED_BY_PRIMARY_AUDITOR / MGMT_FURNISHED_UNAUDITED (paras 6-7) → review Step 0D auditor-Other-Matter block + Q5. MISSING_DATE_LINE (standalone statement sign-off, ledger l.224/318) → reviewed-immaterial: results are dated Aug 4 in four parallel blocks and Board approval Aug 3-4 is captured via Note 2; no thesis impact — acceptable as no-finding. OCR_ARTIFACT flags → mechanical, non-substantive.

### 1B. Presentation ledger

| Category | A2 count | My fresh count | Orphan rows | Status |
|---|---|---|---|---|
| slides | 17 | 17 (page markers l.17-736) | none | MATCH |
| line_items | 30 | 30 (7+5+4+4+4+6 across 6 tables) | none | MATCH |
| zero_standing | 3 | 3 (EBITDA-margin YoY dash, cash YoY dash, Map-led hardware nil) | none | MATCH |
| notes | 4 | 4 (two formula notes l.296, shareholding-date l.688, disclaimer l.696) | none | MATCH |
| chart_data_labels | 60 | 60 (15+10+14+14+7) | none | MATCH |
| narrative_numbers | 32 | 32 | none | MATCH |
| toc_items | 7 | 7 | none | MATCH |
| governance_items | 4 | 4 | none | MATCH |

Flagged rows traced into A4: SEGMENT_FRAMEWORK_CHANGE (MMI-01) → Section C + Q9. PAT-margin denominator note (PAT/Total Income) → review l.134 cross-check + Q's. Government "11%" claim vs table → Step 6B item 1 + Q4. Rohan Verma Joint MD → Q6/Section C. All MMI-01…MMI-12 appear in the preamble (l.21) and map to body findings.

### 1C. Press-release ledger

| Category | A2 count | My fresh count | Orphan rows | Status |
|---|---|---|---|---|
| line_items | 7 | 7 (highlights table l.104-111) | none | MATCH |
| operational_metrics | 29 | 29 | none | MATCH |
| quote_paragraphs | 5 (1 quote / 5 sub-units) | 5 | none | MATCH |
| structural_units | 21 | 21 | none | MATCH |

Flagged rows traced into A4: FIGURE_VARIANT (quote "grew 15%" vs table 14.9%, l.117 vs l.104) → within rounding, and the material variant (govt) is carried at Step 6B/Q4; BLANK_CELL (YoY column blank for EBITDA-margin/PAT-margin/cash) → mechanical; DUPLICATE_CONTENT / PAGE_SPAN → structural. F16-1/16-2/16-3, F6-1(PR), F13-1(PR), F14-1(PR) all in preamble (l.22) and mapped to questions.

### Fresh rows the ledgers LACK (return-to-A2 test)

My independent grep surfaced NO enumeration unit absent from the ledgers. Specifically checked and found already-captured: consol Sale-of-devices +204% (760→2,311 lakhs, l.297); Map-data services QoQ −8.3% (12,719→11,661, l.298); the two distinct UDINs (l.191/399); standalone sign-off missing date (l.462-469). No missing_from_ledger rows.

Coverage verdict: PASS. No orphan rows (return-to-A3), no missing-from-ledger rows (return-to-A2).

---

## AUDIT 2 — ARITHMETIC (recomputed from raw lakhs; consol unless noted)

Raw anchors used: results l.226/227/235/236/239/241-245/248-251 (consol) and l.431/432/440/441/444/446-450 (standalone). Every figure below recomputed from the lakh values x0.01.

| Metric | A4 value | My recompute | Source lines | Status |
|---|---|---|---|---|
| Consol Op EBITDA Q1FY27 (PBT+D+FC−OI) | 56.12 | 66.44+9.15+0.18−19.65 = 56.12 | 239/236/235/227 | MATCH |
| Consol Op EBITDA Q1FY26 | 55.87 | 61.84+6.88+0.82−13.67 = 55.87 | same, Q1FY26 col | MATCH |
| Consol Op EBITDA margin Q1FY27 | 40.2% | 56.12/139.72 = 40.17% | 226 | MATCH |
| Consol Op EBITDA margin Q1FY26 | 45.9% | 55.87/121.61 = 45.94% | 226 | MATCH |
| **Consol Op EBITDA margin, YoY change** | **−574 bps** | **45.94% − 40.17% = −577.6 bps (≈−578)** | 226/227/235/236/239 | **MINOR IMPRECISION** (see note) |
| Consol core PBT ex-OI Q1FY27 | 46.79 | 66.44−19.65 = 46.79 | 239/227 | MATCH |
| Consol core PBT YoY | −2.9% | (46.79−48.17)/48.17 = −2.86% | — | MATCH |
| Consol reported PBT YoY | +7.4% | (66.44−61.84)/61.84 = +7.44% | 239 | MATCH |
| Consol PAT (incl assoc/JV) YoY | +8.6% | (49.74−45.81)/45.81 = +8.58% | 251 | MATCH |
| Consol other income YoY | +43.7% | (19.65−13.67)/13.67 = +43.74% | 227 | MATCH |
| Consol OI / PBT Q1FY27 | 29.6% | 19.65/66.44 = 29.57% | 227/239 | MATCH |
| Consol ETR Q1FY27 | 24.2% | 16.06/66.44 = 24.17% | 244/239 | MATCH |
| Consol D&A YoY | +33.0% | (9.15−6.88)/6.88 = +32.99% | 236 | MATCH |
| Consol revenue YoY | +14.9% | (139.72−121.61)/121.61 = +14.89% | 226 | MATCH |
| Standalone Op EBITDA Q1FY27 | 60.30 | 73.07+5.44+0.17−18.38 = 60.30 | 444/441/440/432 | MATCH |
| Standalone Op EBITDA margin YoY | −614 bps | 54.57%−48.44% = −613 bps | 431/432/440/441/444 | MATCH (1 bp rounding) |
| Standalone core PBT YoY | +6.2% | (54.69−51.50)/51.50 = +6.19% | 444/432 | MATCH |
| Standalone PAT YoY | +10.1% | (55.42−50.35)/50.35 = +10.07% | 450 | MATCH |
| SC gap Q1FY27 (consol−standalone PAT) | −5.68 / −10.2% | 49.74−55.42 = −5.68; /55.42 = −10.25% | 251/450 | MATCH |
| SC gap Q4FY26 | +4.33 / +9.3% | 50.93−46.60 = +4.33; /46.60 = +9.29% | 251/450 | MATCH |
| SC gap QoQ swing | 19.5 pp | +9.29 − (−10.25) = 19.5 pp | — | MATCH |
| PAT bridge: core-PBT change | −1.38 | +0.25(EBITDA) −2.27(D) +0.64(FC) = −1.38 | — | MATCH |
| PAT bridge: OI change | +5.98 | 19.65−13.67 = +5.98 | 227 | MATCH |
| PAT bridge: NPAT-before-assoc change | +3.00 | 50.38−47.38 = +3.00 | 245 | MATCH |
| PAT bridge: assoc/JV change | +0.93 | (−0.64)−(−1.57) = +0.93 | 248-250 | MATCH |
| Reported PAT change | +3.93 | 49.74−45.81 = +3.93 | 251 | MATCH |
| OI-reversion PBT (to Rs13.67) | ~60.46 | 66.44−5.98 = 60.46 | — | MATCH |
| TTM EPS | 25.17 | 24.56−8.48+9.09 = 25.17 | 274 | MATCH |
| Trailing PE @ Rs1,185 | ~47x | 1185/25.17 = 47.1x | — | MATCH |
| Deck PAT margin denominator | 31.2% = PAT/Total Income | 49.74/159.37 = 31.21% | 251/228 | MATCH (A4 correctly flags non-standard denom) |
| Govt YoY (deck claims 11%) | +9.2% actual | (16.7−15.3)/15.3 = +9.15% | deck 493/506 | MATCH (A4 correctly flags 11% as inflated) |
| IoT rev YoY / margin | +75% / +440 bps | 41.1/23.4=+75.6%; 13.1−8.7=+440 bps | deck 399/408 | MATCH |
| Map-led YoY / QoQ | +0.5% / −8.3% | 98.7/98.2=+0.5%; 116.61/127.19=−8.3% | deck 399 / results 298 | MATCH |
| Cash QoQ | +60.3 (685.0→745.3) | 745.3−685.0 = +60.3 | deck 289 | MATCH |
| Net-worth gap (standalone−consol) | ~Rs26 Cr | 920.27−894.00 = 26.27 | 272/458 | MATCH |

All primary and key derived metrics reconcile exactly. Every other cell in Step 1C, 2A, 2B, 3, 4, 5-SC that I recomputed matched to the reported precision.

**Note on the one imprecision (−574 bps).** The unrounded consol operating-EBITDA-margin fall is 45.94% − 40.17% = 577.6 bps (≈ −578); at the deck's reported 0.1% margin precision it is 45.9 − 40.2 = 570 bps. A4's −574 bps sits between the two (it pairs a rounded 45.9% with an unrounded 40.17%). Both component margins (40.2%, 45.9%) are individually correct, and every downstream conclusion (material ~575-580 bps compression, confirmed on both YoY and QoQ axes) is unchanged. This is a sub-materiality precision inconsistency in a derived-of-derived delta, within the 10 bps granularity of the source-reported margins — NOT an error in any primary or key metric. Recorded for A4 to standardise to −578 bps (full precision) or −570 bps (reported precision); does not fail the gate. The standalone −614 bps is a 1 bp rounding of the true −613 bps, immaterial.

Arithmetic verdict: PASS (no mismatch above the reported-margin rounding band on any metric that changes a conclusion).

---

## AUDIT 3 — ADVERSARIAL READ (three most positive claims, strongest bear counter from the SAME extract)

**Positive claim 1 — "Revenue +14.9% YoY is a genuine positive surprise vs the FY26 +2.3% pace" (review l.146/172).**
Strongest bear from the extract: the beat is hardware-led, not franchise-led. Consol Sale-of-devices ran 760→2,311 lakhs (+204% YoY, results l.297) while Sale-of-Map-data-and-services grew only 11,401→11,661 (+2.3%, l.298); on the deck, Map-led revenue was flat at 98.7 vs 98.2 and −8.3% QoQ, and total revenue was −3.7% QoQ (145.04→139.72). The "beat" is low-margin device volume, which is exactly what compressed the margin.
Survives? NO — already grafted: Step 0D note N1 (device +204% vs Map-data +2.3%), Step 2 diagnostics, Step 3 QoQ −3.7%, Step 6B item 5 (Map QoQ −8.3%), and Part 3 of the brief ("trading margin for growth"). Nothing to add.

**Positive claim 2 — "IoT +75% YoY with margin +440 bps to 13.1%; growth trigger ON TRACK" (review l.339).**
Strongest bear from the extract: 13.1% is still ~1/4 of Map-led's 51.4% (deck l.408); IoT's revenue share jumped 19.2%→29.4%, which is the mechanical cause of the blended −574/−578 bps fall; the "improvement" is off a tiny base (IoT EBITDA 2.0→5.4 Cr, l.406); and the IoT-heavy subsidiary block (Gtropy) is loss-making this quarter — consol NPAT-before-assoc 50.38 sits Rs5.04 Cr below standalone 55.42.
Survives? NO — already grafted: growth-trigger row tags IoT "ON TRACK (but margin-dilutive)", Step 5-SC decomposes the −5.04 Cr subsidiary drag, and Part 3/Part 4 of the brief carry the dilution and Gtropy-commoditisation reads.

**Positive claim 3 — "Map-led core returning to positive YoY (+0.5%); standalone parent healthy (core PBT +6.2%, PAT +10.1%)" (review l.165/287/316).**
Strongest bear from the extract: +0.5% is within rounding of flat and masks −8.3% QoQ (results l.298); single-segment reporting (Note 5, l.316) suppresses segment economics; and the "healthy parent" also compressed −613 bps, grew core PBT (+6.2%) far below revenue (+21.3%), and books the treasury (standalone OI 18.38 of consol 19.65) — the same treasury-financed-profit problem, concentrated at the parent.
Survives? NO — already grafted: Step 6B item 5 ("GREEN (marginal) — but QoQ −8.3%"), growth-trigger "WEAKENED → marginal", Step 2B shows standalone −614 bps, Step 5-SC/Step 2 diagnostic 6 place OI at the parent, and the brief states the parent is "barely growing."

Also stress-tested "auditor unmodified (clean)" and "net cash Rs745.3 Cr / deleveraged": the bear (consol conclusion rests on unreviewed 2 associates + 1 nil-revenue subsidiary + JV, all mgmt-furnished — results paras 6/7; cash is idle/growing with no allocation plan and OI now 29.6% of PBT) is already carried in Step 0D, Step 5, MMI-12, and Q3/Q5.

No bear counter survives un-incorporated. A4's treatment is symmetric bull-bear from the same text. No return-to-A4 on the adversarial axis.

---

## STANDING-RULE CHECKS

- INDETERMINATE cash: A4 does NOT resolve to PROCEED. Step 5 caps the verdict at PROCEED WITH CAVEATS and names 5 missing-evidence items (l.268); Section D and the YAML both carry the cap. Compliant with the NEVER rule.
- Binding falsifier: correctly left UNRESOLVABLE (P&L-only filing), not silently cleared; Rs4 Cr govt write-off carried as a partial adverse touch, escalated to the mandatory Q2 H1 balance sheet.
- Standalone AND consolidated coverage: both present (Steps 1A/1B, 2A/2B, 5-SC).
- Every A3 FORWARD-SIGNAL / AMBIGUOUS finding → management question: all forward/ambiguous IDs (BF, MMI-01/03/06/07/08/10/11/12, F2-1/2-2/3-1/8-2/12-1/13-1/15-1, F16-1/2/3, F6-1) map to Q1-Q10; neutral facts (F8-1, F14-1, MMI-02, MMI-09, F14-1(PR)) explicitly logged as monitor-not-question (l.415). No orphaned forward finding.
- Role 5 N.A. correctly declared (turns=0 across all three ledgers); no concall content fabricated.

---

## VERDICT

**COMPLETE.** Gate 0 passes (4/4 brief parts present and provenance-labelled). Coverage passes (no orphan ledger rows; no rows my fresh pass found that the ledgers lack). Arithmetic passes (every primary and key derived metric reconciles from raw lakhs; the sole deviation, −574 vs −578 bps, is a sub-materiality precision inconsistency within the source-reported 0.1% margin granularity and changes no conclusion). Adversarial read produces no surviving bear counter that is not already grafted into A4. INDETERMINATE cash is not silently resolved. This review may proceed to Notion save.

Non-blocking tidy-up handed to A4 (does not gate save): standardise the consolidated operating-margin fall to −578 bps (full precision) or −570 bps (reported precision) wherever "−574 bps" appears (review l.148, 173, 198, 405, and Section D).

```yaml
stage: A5-adversary
company: "MAPMYINDIA"
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
