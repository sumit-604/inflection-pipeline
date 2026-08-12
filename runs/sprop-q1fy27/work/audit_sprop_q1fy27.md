# A5 ADVERSARY / COMPLETENESS AUDIT — Shriram Properties Limited (SPROP), Q1 FY27
# Auditor: A5 | model claude-opus-4-8 | fresh context (A4 review + A1 extracts + A2 ledgers only)
# Re-derived independently from the extracts; A4/A3 cites checked, not trusted.

Anchor key: `R-Lxxx` results extract line; `P-Lxxx` presentation extract line;
`PR-Lxxx` press-release extract line. Results filing in Rs Lakhs, converted x0.01
to Rs Cr; presentation and press release native Rs Cr. Every recompute below is
built from the raw extracted cells, not from A4's derived tables.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate, run FIRST)

The A4 review carries a `SECTION D — PLAIN-LANGUAGE BRIEF` (review L693) with all
four labelled parts present and carrying real content:

| Brief part | Location | Present? | Content check |
|------------|----------|----------|---------------|
| (1) Summary narrative | review L695-723 | **present** | ~22 lines of plain prose; states the -7.4% recognised-revenue fall, Other Income 328% of PBT, PAT -46%, AVOID stands. Non-placeholder. |
| (2) SECTOR intelligence | review L725-742 | **present** | Mid-market residential; e-Khata/Bangalore approval as live sector variable; JDA/JV revenue-share headwind. Non-placeholder. |
| (3) BUSINESS-MODEL intelligence | review L744-766 | **present** | Asset-light Own/JDA/JV/DM; earnings from Other Income not homebuilding; SC-gap reversal (cons PAT 11.0 < SA 12.8). Non-placeholder. |
| (4) COMPETITION intelligence | review L768-791 | **present** | Positioning, where SPL wins/weaker vs peers, moat 5/60, Uttarpara land as unrealised NAV. Non-placeholder. |

**GATE 0 RESULT: PASS.** All four brief parts present and non-empty.

---

## AUDIT 1 — COVERAGE (independent re-enumeration, diffed against A2 ledgers)

Fresh grep/manual sweep re-run over each extract; my counts vs the A2 ledger:

| Category | A2 count | My fresh count | Orphan rows (in ledger, absent from A4) | Missing from ledger (my pass found, ledger lacks) | Status |
|----------|----------|----------------|------------------------------------------|---------------------------------------------------|--------|
| Results — notes | 17 | 17 (6 SA numbered + S-FN1 + 7 cons numbered + C-FN1/C-FN2/A1-FN1) | none | none | PASS |
| Results — line items | 59 | 59 (24 SA + 35 cons) | none | none | PASS |
| Results — zero_standing | 7 | 7 (SA rows 14/21/22 + cons 27/30/32/33) | none | none | PASS |
| Results — agenda items | 2 | 2 (results approval + AGM convening) | none | none | PASS |
| Results — auditor paras | 11 | 11 (5 SA + 6 cons incl. EoM + Other Matter) | none | none | PASS |
| Results — entities | 31 | 31 (26 subs + 5 JVs; C-N6 reconciles) | none | none | PASS |
| Results — signatures | 5 | 5 (Ramaswamy + Vishal x2 + Murali x2) | none | none | PASS |
| Presentation — slides | 26 | 26 (`^\[page N\]` 1-26) | none | none | PASS |
| Presentation — numeric rows | 256 | 256 (digit-bearing body lines L15-666) | none | none | PASS |
| Presentation — footnotes | 5 (+F0) | 5 marked + F0 full-page disclaimer = 6 | none | none | PASS |
| Press release — pages | 4 | 4 | none | none | PASS |
| Press release — narrative claims | 21 | 21 | none | none | PASS |
| Press release — numbers/metrics | 28 | 28 | none | none | PASS |
| Press release — table line items | 4 | 4 (Rev/EBITDA/PBT/NetProfit) | none | none | PASS |
| Press release — forward statements | 8 | 8 | none | none | PASS |

**Ledger-row-to-A4 traceability (every flag row cited or reviewed):** ED search
S-N5/C-N5 (Q18, EoM flag); balancing-figure Q4 S-N6/C-N7 (Step 3); Other Matter
18 subs/4 JVs (Q5, 70% PAT, A3-F4); entity-change Shrivision Upscale A1-FN1 (Q17);
signature-timing (Q16); current-tax dash ZERO_STANDING (Step 1.1/F8); deck
unwinding-impact ZERO_STANDING GoWB (Q7); fair-value-gains footnote F3 (Q1);
NO_SAFE_HARBOR (Q20); Manjari slip (Q10/B3); LAYOUT_AMBIGUOUS slide-20 handover
tiles (Section C monitorables). No orphan rows; no row my fresh pass surfaced is
absent from the ledger.

**AUDIT 1 RESULT: PASS.** Enumeration reconciles exactly; no A2 gap, no A3 orphan.

---

## AUDIT 2 — ARITHMETIC (every derived metric recomputed from raw cells)

Verified and CONFIRMED (sample of the load-bearing recomputes, all tie):
- Consol Core Operating EBITDA Q1FY27 = 224.28 − (73.77+96.09−1.56+26.87+33.95=229.12) = **−4.84** ✓; Q1FY26 = 242.32−219.90 = **22.42** ✓; margin −2.2% / 9.3% = **−1150 bps** ✓.
- Consol YoY: rev −7.4% ✓; OI +143.3% ✓; PBT-after-JV 14.24 vs 21.85 = **−34.8%** ✓; PAT 11.04 vs 20.59 = **−46.4%** ✓; EPS −46.3% ✓.
- ETR Q1FY27 3.20/14.24 = **22.5%** ✓; FY26 −22.78/78.03 = **−29.2%** ✓. PAT margin 4.9% ✓. OI/PBT 328.4% ✓.
- PAT bridge sums: −27.26 (core EBITDA) +0.03 −0.27 +1.06 +27.54 −8.71 = −7.61 (PBT), −1.94 tax = **−9.55** ✓ (= 11.04−20.59).
- Deck-basis EBITDA (PBT-before-JV+D+Fin) Q1FY27 41.90 / Q1FY26 41.59 / Q4FY26 108.87 / FY26 176.88 — all ✓.
- Reported EBITDA Q1FY26 46.45 ✓, Q4FY26 91.36 ✓, Q1FY27 38.05 ✓.
- Standalone core EBITDA ex-OI: Q1FY27 −20.71 ✓, Q1FY26 −22.40 ✓, Q4FY26 −4.87 ✓, FY26 −84.47 ✓. Standalone OI/PBT, core PBT ex-OI all ✓.
- Unit conversions x0.01 spot-checked across ~40 consol/standalone cells: all correct.
- 70% PAT from unreviewed JVs = 7.71/11.04 = 69.8% ✓. Net debt +32.5% vs Mar'25 ✓. Other Equity gap 1427.67−1289.27 = 138.4 ✓. True FCF 54−88 = −34 ✓. QoQ rev −65% ✓. Guidance run-rate 14-18% ✓.

**MISMATCHES FOUND (above rounding):**

| # | Metric (A4 location) | A4 value | Recomputed | Source line | Status |
|---|----------------------|----------|------------|-------------|--------|
| 1 | Gross external debt change vs Mar'26 (Step 5 table, review L344) | **"+5 vs Mar'26"** | **+41 vs Mar'26** (651 − 610); the +5 is vs Mar'25 (651 − 646) | P-L420: 651 Jun'26 / 610 Mar'26 / 646 Mar'25 | **FAIL → A4** |
| 2 | Reported EBITDA FY26, consolidated (Table 1.3, review L169) | **174.65** | **174.29** (78.03 PBT + 10.05 D&A + 86.21 Finance) | R-L432 / R-L425 / R-L424; cross-check 176.88 deck-basis − 2.59 JV loss = 174.29 | **FAIL → A4** |

Mismatch #1 is material: gross external debt rose Rs 41 Cr QoQ (610→651), a
leverage-build fact that A4's "+5" label buries; the correct QoQ delta is 8x the
stated figure. Mismatch #2 is immaterial to any conclusion (a non-load-bearing
summary cell) but is a genuine arithmetic slip above rounding and must be
corrected. Per the A5 rule ("any mismatch above rounding = FAIL"), both loop to A4.

**AUDIT 2 RESULT: FAIL (2 mismatches), loop_back_to A4.**

---

## AUDIT 3 — ADVERSARIAL READ (three most positive A4 claims + strongest bear counter from the same extract)

A4's stance is already AVOID/bearish, so its "positive" assertions are the few
relief/quality points it concedes. Each is stress-tested against the extract.

**Positive claim 1 — "Finance costs −4.8%; modest, permanent ~Rs 5-6 Cr/yr finance
relief from the GoWB royalty cessation" (review L211, L297, Q7).**
Bear counter from the same deck: the reported finance-cost fall is *entirely* the
non-cash "Unwinding Impact (GoWB Royalty)" line dropping 1.5→0 (P-L320). The cash
"Interest expense & other finance cost" line actually **ROSE** 20.8→21.2 (P-L319),
because gross external debt rose 610→651 (P-L420). So there is no cash
deleveraging; the "relief" is a non-cash optical item while cash interest and
gross debt both increased. **COUNTER SURVIVES — must be grafted into A4** (A4 flags
the item as non-cash but nowhere states cash interest rose on higher gross debt).

**Positive claim 2 — "Net debt Rs 432 Cr, roughly flat QoQ (438→432)" (review L346,
L368).**
Bear counter from the deck: net debt is flat only because cash rose 172→219
(+47), and that cash was raised by **Rs 106 Cr of fresh loan drawals** in the
quarter (P-L382, net borrowings +50). Gross external debt itself rose **+41 QoQ**
(610→651, P-L420 — the figure A4 mis-stated as +5). "Net debt flat" is
debt-funded liquidity, not balance-sheet improvement. **COUNTER SURVIVES — must be
grafted into A4** (and is the same fact behind arithmetic mismatch #1).

**Positive claim 3 — "Total Equity rolls cleanly +Rs 11 Cr = Q1 PAT (F11 deck
PASS)" (review L348).**
Bear counter: the +Rs 11 Cr book-equity accretion equals a PAT that is itself
entirely Other Income / fair-value gains (OI 46.76 = 328% of PBT; core operating
EBITDA −4.84). The equity roll is "clean" only in a mechanical roll-forward sense;
economically it is non-cash fair-value accretion, not retained operating earnings.
**COUNTER DOES NOT NEED GRAFTING** — A4 already makes this earnings-quality point
extensively (Step 1.3 reading, Step 4, Flags, brief), so it is already incorporated.

**AUDIT 3 RESULT: two surviving bear counters (finance-relief optics; net-debt-flat
is debt-funded) not incorporated → loop_back_to A4 to graft.**

---

## VERDICT

**INCOMPLETE.** The deliverable gate (Audit 0) and coverage (Audit 1) both PASS,
but Audit 2 found two arithmetic mismatches above rounding and Audit 3 found two
surviving bear counters that A4 has not incorporated.

- **loop_back_to: A4**
- **gap:**
  1. Step 5 gross-external-debt change is stated as "+5 vs Mar'26" but the true
     QoQ delta is **+41 vs Mar'26** (651−610, P-L420); +5 is the vs-Mar'25 figure.
     Correct the number/label — gross leverage rose Rs 41 Cr this quarter.
  2. Table 1.3 consolidated Reported EBITDA FY26 is 174.65; recomputes to **174.29**
     (78.03+10.05+86.21; cross-checks to deck-basis 176.88 − JV 2.59). Correct the cell.
  3. Graft the surviving bear counter that the finance-cost "relief" is a non-cash
     unwinding item only — cash interest ROSE 20.8→21.2 (P-L319) on gross debt up
     +41 (P-L420); no cash deleveraging.
  4. Graft the surviving bear counter that "net debt flat QoQ" is debt-funded:
     cash rose only via Rs 106 Cr fresh loan drawals (P-L382); gross debt +41.

No A2 (enumeration) or A3 (orphan/forensic) failure — those gates pass. All four
corrections are A4-level (table arithmetic + bear-counter incorporation). After
A4 fixes these, the review may return for re-audit before Notion save.

```yaml
stage: A5-adversary
company: "SPROP"
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
arithmetic_mismatches:
  - {metric: "Gross external debt change vs Mar'26 (Step 5)", a4_value: "+5 vs Mar'26", recomputed: "+41 vs Mar'26 (651-610); +5 is vs Mar'25 (646)", source_line: "P-L420"}
  - {metric: "Reported EBITDA FY26 consolidated (Table 1.3)", a4_value: "174.65", recomputed: "174.29 (78.03+10.05+86.21)", source_line: "R-L432/R-L425/R-L424"}
surviving_bear_counters:
  - {claim: "Finance costs -4.8% = modest/permanent finance relief (GoWB royalty cessation)", counter: "Fall is entirely the non-cash unwinding line 1.5->0 (P-L320); cash interest expense ROSE 20.8->21.2 (P-L319) on gross debt up 610->651 (P-L420). No cash deleveraging.", source_line: "P-L319/P-L320/P-L420"}
  - {claim: "Net debt Rs 432 Cr roughly flat QoQ (438->432)", counter: "Net debt flat only because cash rose 172->219 via Rs 106 Cr fresh loan drawals (P-L382); gross external debt rose +41 QoQ (610->651, P-L420). Debt-funded liquidity, not deleveraging.", source_line: "P-L382/P-L420"}
loop_back_to: "A4"
gap: "A4-level fixes: (1) Step 5 gross debt change +5->+41 vs Mar'26 (P-L420); (2) Table 1.3 FY26 Reported EBITDA 174.65->174.29; (3) graft finance-relief-is-non-cash counter (cash interest rose, gross debt +41); (4) graft net-debt-flat-is-debt-funded counter (Rs 106 Cr drawals, P-L382). Coverage/enumeration (A2/A3) pass."
```
