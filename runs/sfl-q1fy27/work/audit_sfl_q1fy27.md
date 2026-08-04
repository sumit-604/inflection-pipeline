# A5 ADVERSARY / COMPLETENESS AUDIT — Sheela Foam Ltd (SFL) — Q1 FY27

Auditor: A5 ADVERSARY (Opus 4.8) | Date: 2026-08-04
Inputs seen: A4 review; A1 extracts (results, presentation, press release, director intimation); A2 ledgers (results, presentation). A3 reasoning NOT supplied (re-derived independently).
Verdict: **INCOMPLETE** — loop back to A4. Two nameable defects (one hard, one cite). Details below.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate)

The mandatory PLAIN-LANGUAGE BRIEF is present (review L473-499), all four parts non-empty and provenance-labelled:

| Part | Location | Present? | Provenance-labelled? |
|---|---|---|---|
| (1) Summary narrative | L475-477 | PRESENT (single ~22-line para, real content) | yes (inline R/P/PR/DI cites) |
| (2) SECTOR intelligence | L479-484 | PRESENT (4 bullets) | yes ("this quarter's filing" / "prior-Notion" tags) |
| (3) BUSINESS-MODEL intelligence | L486-492 | PRESENT (5 bullets) | yes (each bullet tagged) |
| (4) COMPETITION intelligence | L494-499 | PRESENT (4 bullets incl. peer-benchmark ND named) | yes |

Gate 0: **PASS.** All four labelled parts exist with substantive, sourced content.

---

## AUDIT 1 — COVERAGE (independent re-enumeration + diff)

### 1a. Fresh grep/sweep vs A2 counts

| Category | A2 count | My fresh count | Basis | Status |
|---|---|---|---|---|
| numbered_notes (results) | 19 | 19 | std notes @ L195,197,202,272,276,285,288,291,294 (9) + consol @ L558,561,567,635,654,659,669,672,675,679 (10) | MATCH |
| footnotes (results) | 4 | 4 | L266,268 (std), L629,631 (consol) | MATCH |
| auditor_paras (results) | 11 | 11 | std L79,85,92,101 (4) + consol L341,350,358,370,412,420,430 (7) | MATCH |
| entities (results) | 11 | 11 | L375-407, Sr.1-11 | MATCH |
| signature_blocks (results) | 5 | 5 | "Digitally signed" @ L47,110,298,454,683 | MATCH |
| agenda_items (results) | 2 | 2 | Board-outcome letter: results approval + NIL security-cover cert | MATCH |
| line_items (results) | 138 | 138 (accepted) | per-table sweep 30+16+41+16+4+31; spot-verified std P&L & Reg-52 tables cell-by-cell | MATCH |
| zero_standing (results) | 38 | 38 (accepted) | 7 statement dashes + 31 NIL security-cover rows | MATCH |
| slides (presentation) | 51 | 51 | `[page N]` @ 51 hits = pdfinfo 51 | MATCH |
| numbers (presentation) | 505 | 505 (accepted) | Table B `n`-column sums to 505; methodology (OCR-noise exclusions) sound | MATCH |
| footnotes (presentation) | 3 | 3 | L211 "*before Forex MTM", L416 "*100% monetization", L517 "*since inception" | MATCH |

No count divergence. **No row my fresh pass found is missing from the ledger** (`missing_from_ledger: []`).

### 1b. Ledger-row → A4 citation diff

Every A2 ledger row is either cited in A4 or covered by the reconciliation preamble (review L18-39) which walks all 19 notes (Step 0D), all auditor paras (opinion check + Q15), all 11 entities (Step 0D/Q5), the 5 signature blocks (Q11), and both statement tables cell-by-cell (Step 1). Presentation slides/numbers are cited throughout (P L-cites in Steps 1c, 2, 6, 8.5). **No orphan A2 ledger row** (`orphan_rows: []`).

### 1c. A3-finding → Question/Monitorable mapping (launching-agent's explicit check)

A4 asserts (L34-37) it incorporated R-A3-01..11 and P-A3-01..12, and that "Every FORWARD-SIGNAL and AMBIGUOUS finding ... is carried into the Questions-for-Management table ... and/or the monitorables list; the mapping is shown there."

Independent re-mapping of the Step 8.5 `from_finding` column and the Step 8.5b monitorables:

- R-A3-01..11: all 11 map to a question (Q4,Q2,Q15,Q3,Q7,Q8,Q9,Q12,Q11,Q1,Q5). COVERED.
- P-A3-01..11: all 11 map to a question (Q6,Q4,Q14,Q9,Q6,Q5,Q10,Q2,Q2,Q1,Q13). COVERED.
- **P-A3-12: maps to NO question row and NO monitorable.** It appears only in A4's incorporation list (review L36) and the YAML `a3_findings_incorporated` array (L515). It is absent from the Step 8.5 table, the YAML `questions_for_management` block, the Step 8.5b monitorables, and the YAML `monitorables` block.

**FAIL (loop back A4).** A4's own completeness claim (L37, "the mapping is shown there") is false for P-A3-12. I cannot resolve P-A3-12's finding-type from my inputs (the A3 findings file was not supplied), so per A5 discipline rule 4 (conservative bias: an unresolvable coverage question is a FAIL naming the missing evidence, not a pass). A4 must either (a) surface the P-A3-12 question/monitorable it claims to have carried, or (b) explicitly mark P-A3-12 "reviewed, no finding" if it is confirmatory (not FORWARD-SIGNAL/AMBIGUOUS). As written, an incorporated finding is stranded.

---

## AUDIT 2 — ARITHMETIC (recomputed from raw extract lines; nothing above rounding)

All figures re-derived from A1 results extract line cites. Core EBITDA formula = Rev − (TotExp − Finance − Depreciation), i.e. ex-other-income, ex-exceptional.

| Metric | A4 value | My recompute | Source lines | Status |
|---|---|---|---|---|
| **Std core EBITDA Q1FY27** | 68.38 | 760.92−(722.06−12.28−17.24)=68.38 | R L145/160/157/158 | PASS |
| **Std core EBITDA margin Q1FY27 vs 10% line** | 8.99% (below 10%) | 68.38/760.92=8.985% → <10% BREACHED | R L145/160 | PASS |
| Std core EBITDA Q1FY26 / margin | 60.25 / 9.49% | 634.63−574.38=60.25; 9.494% | R L145/160/157/158 | PASS |
| Std core EBITDA Q4FY26 / FY26 | 90.37 / 297.60 | 90.37; 297.60 | R L145/160… | PASS |
| **Consol core EBITDA Q1FY27** | 108.90 | 1031.94−(974.74−17.82−33.88)=108.90 | R L490/504/501/502 | PASS |
| **Consol core EBITDA margin Q1FY27 vs 10% line** | 10.55% (above 10%) | 108.90/1031.94=10.553% → >10% | R L490/504 | PASS |
| Consol core EBITDA Q1FY26 / margin | 75.23 / 9.16% | 821.41−746.18=75.23; 9.158% | R L490/504/501/502 | PASS |
| Consol core margin YoY | +139 bps | 10.553−9.158=+139.5 bps | R L490/504 | PASS |
| **Std–consol PAT gap Q1FY27** | +41.9% | (62.34−43.94)/43.94=41.87% | R L171/518 | PASS |
| Std–consol PAT gap Q4/Q1FY26/FY26 | +21.5% / −38.8% / +23.2% | 21.52% / −38.79% / 23.19% | R L171/518 | PASS |
| **YoY depreciation Δ std** | −42.4% | (17.24−29.91)/29.91=−42.36% | R L158 | PASS |
| **YoY depreciation Δ consol** | −27% (−26.5%) | (33.88−46.12)/46.12=−26.54% | R L502 | PASS |
| Std revenue YoY | +19.9% | 126.29/634.63=19.90% | R L145 | PASS |
| Consol revenue YoY | +25.6% | 210.53/821.41=25.63% | R L490 | PASS |
| Within/Outside India YoY | +20.8% / +42.1% | 20.84% / 42.13% | R L648/649 | PASS |
| Std finance cost YoY | −46.1% | −10.52/22.80=−46.14% | R L157 | PASS |
| Consol finance cost YoY | −38.9% | −11.35/29.17=−38.91% | R L501 | PASS |
| Std other income YoY | +63.2% | 5.28/8.35=63.23% | R L146 | PASS |
| Std PAT YoY | +310.7% | 33.24/10.70=310.65% | R L171 | PASS |
| Consol PAT YoY (9.5x) | +851.8% / 9.5x | 55.79/6.55=851.8%; 62.34/6.55=9.52x | R L518 | PASS |
| Std / Consol EPS YoY | +310.2% / +838% | 310.2% / 838.3% | R L188/552 | PASS |
| Std ETR (4 periods) | 32.7/16.4/25.2/20.7% | 32.66/16.42/25.21/20.71% | R L169/164 etc | PASS |
| Consol ETR (4 periods) | 50.1/17.8/25.6/23.3% | 50.10/17.82/25.58/23.31% | R L512/507 | PASS |
| Std core PBT ex-OI (all 4) | 7.54/58.48/38.86/116.42 | 15.89−8.35=7.54 … 52.49−13.63=38.86 | R L162/146 | PASS |
| Consol core PBT ex-OI Q1FY26 | (0.06) | 9.68−9.74=−0.06 | R L505/491 | PASS |
| Std PAT bridge sum | +33.24 | 8.13+12.67+10.52+5.28+6.26−9.62=33.24 | R L145-171 | PASS |
| Std bridge GP change | +5.47 | COGS-derived GP 253.34→258.81=+5.47 | R L150-155 | PASS |
| Std recurring-core % / non-rec % | 24% / 35% | 8.13/33.24=24.5%; 11.54/33.24=34.7% | derived | PASS |
| Consol PAT bridge sum | +55.79 | 33.67+12.24+11.35+6.39+6.26−15.51+1.39=55.79 | R L490-518 | PASS |
| Consol bridge GP change | +51.94 | GP 329.75→381.69=+51.94 | R L494-499 | PASS |
| Consol recurring-core % / non-rec % | 60% / 23% | 33.67/55.79=60.4%; 12.65/55.79=22.7% | derived | PASS |
| Sub+JV block swing | −4.15 → +18.40 | 6.55−10.70=−4.15; 62.34−43.94=+18.40 | R L171/518 | PASS |
| Exceptional as % std PBT (Q6) | 10.7% | 6.26/58.75=10.66% | R L282/164 | PASS |
| Unreviewed subs as % consol PAT (Q15) | 24.4% | 15.22/62.34=24.41% | R L420/518 | PASS |
| Dep Δ as % of PBT-ex-exc rise (Q1) | ~35% of 36.6 | 12.67/36.60=34.6% | R L158/162 | PASS |
| Receivable days std | 29.3 → 33.5 (+4.2) | 91/3.11=29.3; 91/2.72=33.5 | R L219 | PASS |
| Net worth Δ std / consol | +6.0% / +8.5% | 5.99% / 8.53% | R L209/573 | PASS |
| NCD Δ | −66.7% | −362.50/543.75=−66.67% | R L210 | PASS |
| Reported EBITDA (PBT+D+Fin) std/consol Q1FY27 | 88.27 / 131.29 | 58.75+17.24+12.28=88.27; 79.59+33.88+17.82=131.29 | R L164/158/157 etc | PASS |
| QoQ revenue std / consol | −7.1% / −1.7% | −7.11% / −1.73% | R L145/490 | PASS |
| QoQ core margin std / consol | −204 / −56 bps | 8.985−11.031=−204.6; 10.553−11.106=−55.3 | R L145/160/490/504 | PASS |

**Arithmetic result: ZERO mismatches above rounding.** The two first-class computations flagged by the launching agent — core-EBITDA-ex-OI on both bases vs the 10% line, and the standalone-vs-consolidated PAT gaps — both tie exactly. Deck/PR cross-checks (P L1053-1054 "109/10.6%", P L1073-1074 "68/9.0%", PR L74-75 "+139bps") corroborate. `arithmetic_mismatches: []`.

---

## AUDIT 2b — BROKEN-CITE CHECK

Spot-verified ~60 R/P/PR/DI line cites against the extracts; all resolve correctly EXCEPT one:

- **Review L219: "mattress value +15% / foam value +26% (`R L235-236`, `PR L78-79`)".** `R L235-236` (results extract) is the debt-equity-ratio FORMULA text ("Total Borrowings + Total Lease Liabilities" / "Equity Share Capital + Other Equity"), NOT mattress/foam growth. The correct anchor is **`P L235-236`** (presentation: "Mattress volume 6% / value 15%"; "Foam volume 4% / value 26%"). The claim itself remains supported by the valid co-cite `PR L78-79`, so this is a wrong-document-prefix cite (R vs P), not an unsupported claim. **Minor FAIL, loop back A4** — correct the prefix to P L235-236.

All other checked cites (R L145/160/158/502/282/407/420/533/175/522/316/41/113/648/649/171/518/167/166/223/587; P L211/224/227/243/205/296/308/316/328/335/338/1059/1064/37/139/143/406; PR L68/72-79/140; DI L31/33/99) are correct.

---

## AUDIT 3 — ADVERSARIAL READ (strongest bear counter to the three most positive claims, from the same extract)

**Positive claim 1 — "Consolidated core EBITDA margin +139bps to 10.55% is real operating expansion."**
Bear counter (same extract): the entire expansion is international — standalone (domestic SFL+KEL) core margin CONTRACTED −50bps to 8.99%, below the 10% falsification line (R L145/160); and the deck's headline EBITDA-growth figures carry a "*before Forex MTM" qualifier of ambiguous scope (P L211), so even the consolidated "expansion" may be an MTM-adjusted number, not a clean operating figure. **Counter is supported and SURVIVES — but A4 has ALREADY grafted it** (Step 2 diagnostic 2 makes the std/consol divergence its central finding; Q10 chases the MTM footnote). No new addition required.

**Positive claim 2 — "Deleveraging GREEN / on track to FY28 net cash (NCDs −67%, finance cost halved)."**
Bear counter (same extract): the same print shows depreciation down 42% std / 27% consol with NO explanatory note (R L158/502) and nil standalone current tax with an entirely deferred charge (R L166) — so a large slice of the PBT lift that accompanies the deleveraging is unexplained/non-cash and could reverse; the NCD paydown also erodes the interest shield. **Supported and SURVIVES — but A4 ALREADY grafts it** (Q1 depreciation, Q3 cash-tax, PAT-bridge "70% dep+finance, half unexplained"). The debt-path claim itself (NCD/D-E down) is factually GREEN and untouched. No new addition required.

**Positive claim 3 — "International turnaround FIRED; Australia/Spain now the group's earnings engine."**
Bear counter (same extract): that engine may be FX-aided/cyclical (translation OCI swung −₹27cr, R L533; "*before Forex MTM" footnote, P L211), and 9 of 11 subsidiaries — ₹284.14cr revenue / ₹15.22cr PAT = 24.4% of consolidated PAT — were NOT reviewed by the principal auditor (R L420), so the celebrated engine rests on unreviewed component-auditor numbers. **Supported and SURVIVES — but A4 ALREADY grafts it** (Q4 durability, Q9 FX/hedging, Q15 unreviewed subs). No new addition required.

**Adversarial result: no NEW surviving bear counter requires grafting.** `surviving_bear_counters: []`. A4's symmetry is intact; every strong bear read is already carried in its Questions/flags.

---

## VERDICT

**INCOMPLETE.** Loop back to **A4.**

Gate 0 (deliverable brief) PASS. Coverage of A2 ledger rows PASS (no orphan, none missing). Arithmetic PASS (zero mismatches; the two first-class computations tie exactly). Adversarial read PASS (no ungrafted bear counter).

Two nameable A4-owned defects block save:
1. **(Hard) P-A3-12 stranded:** listed as an incorporated A3 finding (review L36; YAML L515) but mapped to no Questions-for-Management row and no monitorable, contradicting A4's own claim (L37) that "the mapping is shown there." Unresolvable from supplied inputs (A3 findings file not provided) → conservative-bias FAIL. A4 must surface the P-A3-12 question/monitorable or explicitly mark it "reviewed, no finding."
2. **(Cite) Broken prefix at review L219:** `R L235-236` should be `P L235-236` (R L235-236 is the debt-equity formula, not mattress/foam growth); claim stays supported by co-cite PR L78-79. Correct the prefix.

Both are quick A4 fixes; re-submit for A5 re-clear before Notion save.

```yaml
stage: A5-adversary
company: "SFL"
quarter: "Q1 FY27"
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
arithmetic_mismatches: []
surviving_bear_counters: []
loop_back_to: "A4"
gap: "P-A3-12 listed as incorporated (review L36 / YAML L515) but mapped to no Questions-for-Management row and no monitorable, contradicting A4's own mapping claim at L37; A4 must surface its question/monitorable or explicitly mark it 'reviewed, no finding'. Secondary: broken cite at review L219 (`R L235-236` should be `P L235-236`; claim still supported by co-cite PR L78-79)."
```
