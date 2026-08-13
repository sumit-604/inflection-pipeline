# A5 ADVERSARY / COMPLETENESS AUDIT — KERNEX Microsystems (India) Ltd | Q1 FY27

Scope this run: RESULTS filing only (no concall, no presentation). Role 5 N.A.
Inputs audited (only these): A4 review, A1 extract (641 lines), A2 ledger.
Method: fresh independent re-derivation. Every A4 cite re-checked against raw
extract line numbers; every derived metric recomputed from raw Lakhs x0.01;
A2 enumeration re-run by independent grep + manual row walk.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate, run first)

The A4 review carries a PLAIN-LANGUAGE BRIEF at L460-472 with all four labelled
parts present and non-empty:

| Part | Heading location | Present? | Real content? |
|---|---|---|---|
| 1. Summary narrative | L462-463 | PRESENT | Yes — ~15-line narrative, numbers anchored (Rev 503.58, PAT 109.85, OI 0.33% of PBT, warranty 30.05, DTC 8.59, order book 3,641, cash ND, AVOID) |
| 2. Sector intelligence | L465-466 | PRESENT | Yes — Kavach single-payer rollout tailwind vs lumpy tender + long-collection structure |
| 3. Business-model intelligence | L468-469 | PRESENT | Yes — asset-light, debt-funded WC, shell JVs, warranty recurrence |
| 4. Competition intelligence | L471-472 | PRESENT | Yes — HBL Power peer, 17-mo Kavach lag, 268 vs 71 debtor days, cash-gap question |

**GATE 0 RESULT: PASS.** All four parts present with substantive, non-placeholder content.

---

## AUDIT 1 — COVERAGE (fresh enumeration diff vs A2 ledger)

Independent re-count (grep + manual row walk over the raw extract), diffed
against the A2 count-test block:

| Category | A2 count | My fresh count | Method | Orphan/extra | Status |
|---|---|---|---|---|---|
| agenda_items | 5 | 5 | L54-64 items (i)-(v); board-timing L70 is separate | none | MATCH |
| annexure_fields | 14 | 14 | 7 fields x 2 directors, L88-166 | none | MATCH |
| line_items | 63 | 63 (35 consol + 28 standalone) | manual DATA-row walk L184-243 (35) + L462-508 (28) | none | MATCH |
| zero_standing | 3 | 3 | consol Excep L203, consol OCI-NCI L231, SA Excep L481 | none | MATCH |
| notes | 19 | 19 | grep on note-open pattern -> 19; 10 consol (L248-278) + 9 SA (L513-539) | none | MATCH |
| auditor_paras | 18 | 18 | grep confirms; 12 consol (L304-427) + 6 SA (L565-619) | none | MATCH |
| entities | 6 | 6 | parent + Avant-Garde + TCAS JV + KERNEX-VRRC JV + VRRC KERNEX CE RVR JV + KERNEX-BHEPL JV (L268-271/L331-341) | none | MATCH |
| signature_blocks | 4 | 4 | 2 MD (L286/L547) + 2 auditor (L437/L635) | none | MATCH |

**No row my fresh pass found is missing from the ledger. No count divergence. (A2 gate holds.)**

### Ledger-row-to-A4 citation check (orphan test)
Every ledger flag category is cited or dispositioned in A4:
- ZERO_STANDING x3 -> Exceptional line A3-01 (Step 4/Q4); OCI-NCI dispositioned neutral. Covered.
- ENTITY_CHANGE (KERNEX-BHEPL) -> A3-08/A3-17, Step 4X + Q8 + monitorables. Covered.
- UNREVIEWED_UNAUDITED (Avant-Garde) -> A3-05, Step 4X + Q3, flag L526. Covered.
- OTHER_AUDITOR_REVIEWED x3 -> Step 0D L50, Step 4X shell read. Covered.
- BLANK_QUARTERLY x2 (Other equity) -> reconciled in preamble L11; non-material annual-only line. Covered as reviewed/no-finding.
- Cross-report EOM PY-ECL inconsistency (211.67 vs 309.59) -> A3-15, Step 0D L50 + Q11. Covered.
- Warranty / order book / DTC / ECL / BG arbitration -> A3-09/A3-07/A3-12/A3-06/A3-11, all surfaced.

**One non-blocking observation (not an orphan row):** the A2 DIN_MISMATCH flag
(board letter L59 DIN **07992925** vs Annexure A L88/L91 DIN **07993925** for
Badari Narayana Raju Manthena — a real digit transposition, confirmed against
raw extract) is not explicitly surfaced anywhere in A4. The *rows* carrying it
(agenda item iii; Annexure field 1) ARE cited by A4 (L325, L435, via A3-10), so
this is not an orphan row and not a gate failure. It is a mechanical documentation
typo, immaterial to the AVOID thesis, which the ledger itself left "not resolved."
Recommendation (non-blocking): A4 may add a one-line note flagging the DIN typo
for completeness of the governance record. Does not fail coverage.

**COVERAGE RESULT: PASS.** Fresh counts match A2 on all eight categories; no
orphan rows; no rows missing from the ledger.

---

## AUDIT 2 — ARITHMETIC (every derived metric recomputed from raw Lakhs x0.01)

Recomputed independently from raw extract lines. Consolidated unless noted (SA = standalone).

| Metric | Period | A4 value | My recompute (raw source) | Status |
|---|---|---|---|---|
| Op EBITDA (PBT+D+Fin-OI) | Q1FY27 C | 162.82 | 148.14+1.94+13.23-0.49 = 162.82 (L205/196/195/186) | OK |
| Op EBITDA margin | Q1FY27 C | 32.33% | 162.82/503.58 = 32.33% | OK |
| Op EBITDA | Q1FY26 C | 12.58 | 9.55+0.84+2.55-0.36 = 12.58 | OK |
| Op EBITDA | Q4FY26 C | 105.12 | 92.12+2.13+11.79-0.92 = 105.12 | OK |
| Op EBITDA | FY26 C | 148.76 | 117.04+5.82+28.15-2.25 = 148.76 | OK |
| Reported EBITDA | Q1FY27 C | 163.31 | 148.14+1.94+13.23 = 163.31 | OK |
| Core PBT (PBT-OI) | Q1FY27 C | 147.65 | 148.14-0.49 = 147.65 | OK |
| Other Income / PBT | Q1FY27 C | 0.33% | 0.49/148.14 = 0.33% | OK |
| Effective Tax Rate | Q1FY27 C | 25.85% | 38.29/148.14 = 25.85% (L211/205) | OK |
| Current-tax ETR (ex-DTC) | Q1FY27 C | 31.65% | 46.88/148.14 = 31.65% (L208) | OK |
| PAT margin | Q1FY27 C | 21.81% | 109.85/503.58 = 21.81% | OK |
| PAT ex-DTC (clean) | Q1FY27 C | 101.26 | 109.85-8.59 = 101.26 (L210 credit) | OK |
| PAT ex-DTC | Q1FY26 C | 5.27 | 7.41-2.14 = 5.27 (DTC credit 213.97L) | OK |
| PAT ex-DTC | Q4FY26 C | 68.92 | 68.25+0.67 = 68.92 (DTC charge 66.99L, added back) | OK |
| PAT ex-DTC | FY26 C | 93.84 | 88.24+5.60 = 93.84 (DTC charge 560.16L) | OK |
| Op EBITDA | Q1FY27 SA | 162.54 | 147.86+1.94+13.22-0.48 = 162.54 (L483/474/473/464) | OK |
| Op EBITDA margin | Q1FY27 SA | 32.38% | 162.54/502.03 = 32.38% | OK |
| Op EBITDA | FY26 SA | 140.61 | 109.42+5.82+28.14-2.77 = 140.61 | OK |
| PAT ex-DTC | Q1FY27 SA | 100.98 | 109.57-8.59 = 100.98 | OK |
| ETR | Q1FY27 SA | 25.90% | 38.29/147.86 = 25.90% | OK |
| Revenue YoY | Q1FY27 C | +800.4% (9.00x) | (503.58-55.93)/55.93 = 800.4% | OK |
| Op EBITDA YoY | Q1FY27 C | +1194% | 150.24/12.58 = 1194% | OK |
| Margin YoY | Q1FY27 C | +984 bps | 32.33-22.49 = 9.84pp | OK |
| Finance cost YoY | Q1FY27 C | +418.8% (5.19x) | 10.68/2.55 = 418.8% | OK |
| Core PBT YoY | Q1FY27 C | +1506% | 138.46/9.19 = 1506% | OK |
| Reported PBT YoY | Q1FY27 C | +1451% | 138.59/9.55 = 1451% | OK |
| PAT YoY | Q1FY27 C | +1382% | 102.44/7.41 = 1382% | OK |
| EPS YoY | Q1FY27 C | +1369% | 60.92/4.45 = 1369% | OK |
| Revenue YoY | Q1FY27 SA | +840.1% (9.40x) | 448.63/53.40 = 840.1% | OK |
| Core PBT YoY | Q1FY27 SA | +1558% | 138.49/8.89 = 1558% | OK |
| PAT YoY | Q1FY27 SA | +1387% | 102.20/7.37 = 1387% | OK |
| S-vs-C PAT premium | Q1FY26 | +0.05 / 0.64% | 741.21-736.53 = 4.68L; 0.05/7.37 = 0.64% | OK |
| S-vs-C PAT premium | Q4FY26 | +3.69 / 5.72% | 68.25-64.56 = 3.69; 5.72% | OK |
| S-vs-C PAT premium | FY26 | +7.61 / 9.44% | 88.24-80.63 = 7.61; 9.44% | OK |
| S-vs-C PAT premium | Q1FY27 | +0.27 / 0.25% | 10,984.57-10,957.16 = 27.41L; 0.27/109.57 = 0.25% | OK |
| Avant-Garde vs premium | Q1FY27 | ~100% | AG NP 27.56L (L415) vs premium 27.41L | OK |
| PAT bridge total | Q1FY27 C | +102.44 | 109.85-7.41 = 102.44 | OK |
| Bridge: rev@prior margin | | +100.68 | 447.65 x 22.49% = 100.68 | OK |
| Bridge: margin contrib | | +49.55 | 9.84% x 503.58 = 49.55 | OK |
| Bridge: PBT change | | +138.59 | 150.24-1.10-10.68+0.13 = 138.59 | OK |
| Bridge: tax change | | -36.15 | 38.29-2.14 = 36.15 | OK |
| Ex-warranty Op EBITDA | Q1FY27 C | 192.87 / 38.30% | 162.82+30.05 = 192.87; /503.58 = 38.30% | OK |
| Warranty margin drag | Q1FY27 C | ~597 bps | 30.05/503.58 = 5.97% | OK |
| DTC PAT inflation | Q1FY27 C | ~7.8% | 8.59/109.85 = 7.82% | OK |
| Q2+Q3 FY26 combined | derived | 119.71 | 430.22-55.93-254.58 = 119.71 | OK |
| Revenue QoQ (Q4->Q1) | | +97.8% | 249.00/254.58 = 97.8% | OK |
| QoQ margin | | -896 bps | 41.29-32.33 = 8.96pp | OK |
| Q1 rev / gross book | | ~13.8% | 503.58/3641 = 13.8% | OK |
| Q1 rev / Notion base | | 42% | 503.58/1200 = 42% | OK |

**ARITHMETIC RESULT: PASS. Zero mismatches above rounding across all consolidated
and standalone derived metrics, all YoY/QoQ percentages, the S-vs-C gap, and the
PAT bridge.** Tax-sign handling (DTC credit vs charge across periods) is internally
consistent and correctly re-derived.

---

## AUDIT 3 — ADVERSARIAL READ (three most positive claims, strongest bear counter each)

**Positive claim 1 — "The profit is genuinely operational, not treasury-driven"
(Step 2 diag 3, L194): core operating PBT +1506%, other income only 0.33% of PBT.**
Strongest bear counter FROM THE EXTRACT: the revenue is a single lumpy
percentage-completion burst — 13.8% of the gross Rs3,641 Cr book billed in ONE
quarter off one CLW order at 45% completion (L272-273) — and recognised profit is
unvalidated as cash because a Q1 filing carries no cash-flow statement (Step 5),
while a frozen >3yr receivable with rising ECL (L263-264) and a new Rs30.05 Cr
warranty (L274) sit against it. Verdict: SUPPORTED by the extract, but ALREADY
INCORPORATED in A4 (Step 2 diag 1 lumpiness; Step 3 QoQ; Step 5 INDETERMINATE cash;
Q1 management question). Does NOT survive as a new graft.

**Positive claim 2 — "Operating margin 32.3%, top of the healthy band, even after
the Rs30.05 Cr warranty; ex-warranty 38.30%" (Step 2 diag 2).**
Strongest bear counter FROM THE EXTRACT: the ex-warranty 38.30% is misleading as a
"true" margin because A4 itself classes the warranty as a NEW RECURRING drag that
scales with the installed base (Note 8, L274; A3-09); and QoQ operating margin FELL
896 bps (41.29% -> 32.33%), with even the ex-warranty 38.30% BELOW Q4's 41.29% —
i.e. margin is compressing, not expanding. Verdict: SUPPORTED, but ALREADY
INCORPORATED (Step 3 explicitly states ex-warranty 38.30% is still below Q4 41.29%
= cost normalisation; warranty flagged recurring). Does NOT survive as a new graft.

**Positive claim 3 — "Q1 FY27 is tracking at or above the Notion base case on
revenue, margin and PAT pace" (Step 6A).**
Strongest bear counter FROM THE EXTRACT: annualising one lumpy quarter is invalid;
the order book has slipped to Rs3,641 Cr incl GST, below the Rs4,500 Cr red line
and far under the ~Rs6,500 Cr thesis (L272), so revenue is FIRING off a DEPLETING
backlog (execution outrunning replenishment = forward cliff risk); and the P&L
"beat" mechanically worsens the receivable/WC absorption the thesis fears, with
finance cost 5.2x YoY (L195) confirming the funding cost. Verdict: SUPPORTED, but
ALREADY INCORPORATED (A4 explicitly states this "does NOT change the AVOID," Step
6A/6D order-book WEAKENED, Step 8 flag). Does NOT survive as a new graft.

**No surviving bear counter requires grafting into A4.** All three strongest
counters are already present and prominently surfaced in the review. This is a
completeness pass, not an endorsement of the underlying thesis (Role 3 Devil's
Advocate runs separately).

---

## VERDICT

**COMPLETE.**

- Gate 0 (plain-language brief, all four parts): PASS.
- Coverage: PASS — fresh enumeration matches A2 on all eight categories; no orphan
  rows; no rows missing from the ledger.
- Arithmetic: PASS — zero mismatches above rounding on every recomputed metric
  (consol + standalone derived, YoY, QoQ, S-vs-C gap, PAT bridge).
- Adversarial: PASS — the three strongest bear counters are all already
  incorporated in A4; none survives as an unaddressed addition.

Non-blocking observation (no loop-back required): the A2 DIN_MISMATCH flag
(07992925 vs 07993925) is not explicitly surfaced in A4; the rows are cited, the
item is an immaterial mechanical typo. Recommend A4 add a one-line note at next
touch; does not fail the gate. Only COMPLETE proceeds to Notion save.

```yaml
stage: A5-adversary
company: "KERNEX"
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
