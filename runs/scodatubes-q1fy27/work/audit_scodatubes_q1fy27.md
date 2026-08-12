# A5 ADVERSARY / COMPLETENESS AUDIT — Scoda Tubes Limited (SCODATUBES), Q1 FY27

Fresh context. Re-derived independently from the A1 extract (lines 1-204 body, plus the
appended A1 CORRECTIONS/footing-proof at 205-289 for provenance only). A4 cites checked,
not deferred to. Units: source filed in Rs Millions; A4 works in Rs Crore (Millions x 0.1).

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate)

PLAIN-LANGUAGE BRIEF present at review L411. All four labelled parts present, non-empty, real:

| Part | Location | Present? | Real content? |
|---|---|---|---|
| 1. SUMMARY NARRATIVE | L413-414 | PRESENT | Yes — dense multi-line narrative, revenue/PAT/margin/cash-INDETERMINATE, each number line-anchored. Well over 10 lines. |
| 2. SECTOR INTELLIGENCE | L416-417 | PRESENT | Yes — specialty SS pipes, import-substitution/anti-dumping tailwind, BHEL/marine catalysts flagged unconfirmed. |
| 3. BUSINESS-MODEL INTELLIGENCE | L419-420 | PRESENT | Yes — capex-heavy model, backward integration, deferred-tax shield, cash-conversion Achilles heel. |
| 4. COMPETITION INTELLIGENCE | L422-423 | PRESENT | Yes — peer scale/margin/CCC vs Venus/Ratnamani/Welspun, promoter-quality edge. |

**Gate 0: PASS.** All four parts present and substantive.

---

## AUDIT 1 — COVERAGE (independent re-enumeration vs A2 ledger)

Fresh grep/sweep of extract body (L1-204). Diff against A2 COUNT TEST (ledger L11-20).

| Category | A2 count | My fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Notes (numbered) | 7 | 7 (L115,118,120,122,123,125,127) | none | PASS |
| Line items (value-bearing) | 25 | 25 (L81,82,83,85-94,96-99,102,103,104,106,107,110,111,112) | none | PASS |
| Zero-standing | 3 | 3 (L93 Exceptional, L97 Earlier-yr tax, L111 EPS-Discontinued) | none | PASS |
| Agenda items | 1 | 1 (L38-39, results + LRR approval) | none | PASS |
| Auditor paras | 4 | 4 (L158-161, 162-167, 169-178, 179-185) | none | PASS |
| Entities | 1 | 1 (Scoda standalone, Note 5 L123-124) | none | PASS |
| Signatories | 3 | 3 (MD DIN 06785595 L53; Chairman/WTD DIN 08036100 L143; auditor M.No.134475/UDIN L197) | none | PASS |
| Concall turns / slides | 0 / 0 | 0 / 0 (bare Reg 33 filing, no transcript/PPT) | n/a | PASS |

My fresh pass reproduces every A2 count exactly. No row my pass found is missing from the ledger
(nothing to loop to A2). Every ledger row is cited in A4: the 7 notes in Step 0D (L50-58), the 25
line-items in Step 1 (L73-95), zero-standing at L85/87/95 of the review, agenda/auditor/entity/
signatory rows in the reconciliation preamble (L14-27). **No orphan row** (nothing to loop to A3).

**Audit 1: PASS.** Coverage complete, zero orphans, zero missing-from-ledger.

---

## AUDIT 2 — ARITHMETIC (recomputed from raw extracted numbers)

### 2a. Footing re-proof (independent, Rs Millions, corrected body values L81-112)
Five identities x four columns, re-derived by hand:

| Column | Total income | Total expenses | PBT | PAT | TCI | Foots? |
|---|---|---|---|---|---|---|
| Q1FY27 | 1,243.45+16.30=1,259.75 | 1,001.65-156.14+24.62+64.81+41.31+213.53=1,189.78 | 1,259.75-1,189.78=69.97 | 69.97-6.25-11.22=52.50 | 52.50+1.71-0.43=53.78 | YES |
| Q4FY26 | 1,235.69+44.03=1,279.72 | 1,007.73-183.41+26.34+81.39+36.12+217.98=1,186.15 | 93.57 | 93.57-25.72-4.66=63.19 | 63.19-1.47+0.37=62.09 | YES |
| Q1FY26 | 974.17+17.61=991.78 | 742.49-52.47+24.20+51.04+15.72+118.05=899.03 | 92.75 | 92.75-18.90-3.02=70.83 | 70.83+1.47-0.37=71.93 | YES |
| FY26 | 5,186.50+105.71=5,292.21 | 4,143.75-611.44+104.54+248.66+92.17+787.21=4,764.89 | 527.32 | 527.32-116.33-22.56=388.43 | 388.43+1.18-0.30=389.31 | YES |

**20/20 checks foot on the corrected grid.** Confirms A1's restoration (including Q1FY26 PAT
70.83 not the corrupt 10.83). No column fails. A4's "footing 20/20" claim is verified independently.

### 2b. Derived-metric recompute (Rs Crore = Millions x 0.1)

| Metric | A4 value | My recompute | Source lines | Status |
|---|---|---|---|---|
| Op EBITDA Q1FY27 (PBT+D+Fin-OI) | 15.979 | 6.997+4.131+6.481-1.630=15.979 | L94/89/88/82 | PASS |
| Op EBITDA Q1FY26 | 14.190 | 9.275+1.572+5.104-1.761=14.190 | L94/89/88/82 | PASS |
| Op EBITDA FY26 | 76.244 | 52.732+9.217+24.866-10.571=76.244 | L94/89/88/82 | PASS |
| Op EBITDA margin Q1FY27 | 12.85% | 15.979/124.345=12.851% | L81 | PASS |
| Op EBITDA margin Q1FY26 | 14.57% | 14.190/97.417=14.566% | L81 | PASS |
| Reported EBITDA margin Q1FY27 | 14.16% | 17.609/124.345=14.161% | L81 | PASS |
| Effective tax rate Q1FY27 | 24.97% | 1.747/6.997=24.97% | L96+98/94 | PASS |
| Effective tax rate Q4FY26 | 32.47% | 3.038/9.357=32.47% | L96+98/94 | PASS |
| Current-tax share PBT Q1FY27 | 8.93% | 0.625/6.997=8.93% | L96/94 | PASS |
| Other income/PBT Q4FY26 | 47.1% | 4.403/9.357=47.06% | L82/94 | PASS |
| PAT margin Q1FY27 | 4.22% | 5.250/124.345=4.22% | L99/81 | PASS |
| Revenue YoY | +27.64% | (124.345-97.417)/97.417=+27.64% | L81 | PASS |
| Op EBITDA YoY | +12.61% | 1.789/14.190=+12.61% | derived | PASS |
| Op EBITDA margin YoY | -172 bps | 12.851-14.566=-171.5 bps | derived | PASS |
| Depreciation YoY | +162.8% | (4.131-1.572)/1.572=+162.8% | L89 | PASS |
| Finance cost YoY | +26.98% | (6.481-5.104)/5.104=+26.98% | L88 | PASS |
| Core op PBT (ex-OI) YoY | -28.57% | (5.367-7.514)/7.514=-28.57% | L94/82 | PASS |
| PAT YoY | -25.88% | (5.250-7.083)/7.083=-25.88% | L99 | PASS |
| EPS YoY | -38.89% | (0.88-1.44)/1.44=-38.89% | L110 | PASS |
| Revenue QoQ | +0.63% | (124.345-123.569)/123.569=+0.63% | L81 | PASS |
| PAT QoQ | -16.92% | (5.250-6.319)/6.319=-16.92% | L99 | PASS |
| S-vs-C PAT gap (all periods) | 0.00% | No consolidated exists (Note 5, L123-124) — structurally zero | L123 | PASS |
| PAT bridge total | -1.833 | +11.379-0.042-9.548-2.559-1.377-0.131+0.445=-1.833 | Step 4B legs | PASS |
| — gross profit leg | +11.379 | (124.345-100.165+15.614)-(97.417-74.249+5.247)=39.794-28.415 | L81/85/86 | PASS |
| — other-exp leg | -9.548 | 21.353-11.805 | L90 | PASS |
| Net material cost Q1FY27 | 68.0% | (100.165-15.614)/124.345=68.00% | L85/86/81 | PASS |
| Net material cost Q1FY26 | 70.8% | (74.249-5.247)/97.417=70.83% | L85/86/81 | PASS |
| Inventory build YoY | +198% | (15.614-5.247)/5.247=+197.6% | L86 | PASS |
| Implied wtd shares Q1FY26 (F10-1) | ~49.2M | 70.83M PAT / 1.44 EPS = 49.2M | L99/110 | PASS |

**Audit 2: PASS.** Every A4 derived metric ties to the raw extracted numbers within rounding.
Zero arithmetic mismatches. Footing 20/20 confirmed independently.

---

## AUDIT 3 — ADVERSARIAL READ (strongest bear counter to A4's three most positive claims, same text)

**Claim 1 (most positive): "Revenue +27.64% YoY — the one genuinely good number" (L139, at/above base, L260).**
Bear counter (same text): Sequential revenue is essentially flat, +0.63% QoQ (124.345 vs 123.569,
L81), and the Q4FY26 base is a Note-6 balancing/derived figure (L125), not independently reported.
The entire YoY gain was already on the books by Q4FY26; Q1FY27 added nothing sequentially, and the
plateau lands exactly on the quarter depreciation stepped +162.8% (plant switched on).
**Survives? NO.** A4 already carries this in full — Step 3 plateau diagnostic (L165-167), the
"commissioned plant that does not lift the run-rate" red flag, and the summary narrative. Incorporated.

**Claim 2: "Gross material economics improved (68.0% vs 70.8%); the entire earnings decline sits below EBITDA in depreciation and finance costs" (L146; repeated in summary narrative L414).**
Bear counter (same text): The operating EBITDA margin contraction A4 itself flags RED (-172 bps,
trigger 9) is by definition an ABOVE-EBITDA event — depreciation and finance sit BELOW EBITDA and
cannot move it. Decomposing the -172 bps from the extract: gross material margin +283 bps
(70.83% -> 68.00%, L85/86/81), employee leverage +50 bps (2.48% -> 1.98%, L87/81), and
**Other Expenses -505 bps (12.12% -> 17.17%, L90/81)** — sum -172 bps, ties exactly. Other expenses
rose **+80.9% YoY** (11.805 -> 21.353 Cr, L90), ~2.9x the revenue growth rate and a larger absolute
drag (-9.548 Cr) than depreciation (-2.559) and finance (-1.377) combined. The operating-margin
miss is an OTHER-EXPENSES story, not a depreciation story. A4 lists other expenses only as an
absolute bridge leg (L196, L209), never diagnoses it as the cause of the margin contraction it
flags, raises no management question on its composition, and its narrative ("the entire earnings
decline sits in depreciation and interest") mis-attributes the cause.
**Survives? YES.** Supported by the extract, absent from A4's diagnosis. Must be grafted to A4.

**Claim 3: "No thesis-broken condition has FIRED; verdict PROCEED WITH CAVEATS, AVOID held — nothing mechanically worse this quarter" (Step 6C L294, Step 8 L339).**
Bear counter (same text): Two of the four thesis-broken legs (cumulative CFO/PAT <0.30x; inventory
days >180) are fed by the one hard datum this filing DOES supply — the Rs15.614 Cr inventory build,
+198% YoY, outpacing revenue +27.6% (L86). "Not fired" reflects the balance sheet being absent, not
the risk abating; the sole visible directional proxy pushes both open legs toward breach.
**Survives? NO.** A4 explicitly carries this ("bear-leaning," "worsens the prior," L241; "trending
adversely and remain open," L294). Substance incorporated.

**One surviving bear counter (Claim 2).** Must be grafted into A4 before save.

---

## VERDICT

**INCOMPLETE.** Loop back to **A4**.

- Gate 0 (deliverable): PASS. Audit 1 (coverage): PASS, zero orphans. Audit 2 (arithmetic):
  PASS, 20/20 footing re-proved, every derived metric ties.
- **The single failure is an unincorporated surviving bear counter (Audit 3, Claim 2):** the
  operating-EBITDA-margin contraction of -172 bps that A4 flags RED is driven by **Other Expenses
  +80.9% YoY (L90: 11.805 -> 21.353 Cr, a -505 bps ratio drag that ties out the full -172 bps),
  not by depreciation/finance** (which sit below the EBITDA line and cannot move the margin). A4
  gives other expenses only as an absolute bridge leg, never diagnoses it as the margin-miss driver,
  and its narrative claim that "the entire earnings decline sits in depreciation and interest"
  (L414/L146) mis-attributes the cause of the operating-margin weakness A4 itself scores RED.
- **Exact graft required in A4:** (i) name Other Expenses +80.9% YoY (+505 bps of revenue) as the
  proximate driver of the operating-EBITDA-margin contraction, with the +283/+50/-505 bps
  decomposition; (ii) reconcile the summary-narrative statement so the margin miss is not
  attributed solely to depreciation/finance; (iii) add a management question on the composition of
  the other-expenses surge (job-work/power/conversion vs one-off). Re-emit A4, then re-run A5.

---

```yaml
stage: A5-adversary
company: "SCODATUBES"
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
surviving_bear_counters:
  - claim: "Gross economics improved; the entire earnings decline sits below EBITDA in depreciation and finance costs (L146/L414)."
    counter: "The -172 bps operating EBITDA margin contraction (A4's own trigger-9 RED) is an above-EBITDA event driven by Other Expenses +80.9% YoY (11.805->21.353 Cr), a -505 bps ratio drag that alone exceeds the full -172 bps; gross (+283 bps) and employee (+50 bps) cushioned it. Depreciation/finance sit below EBITDA and cannot move the margin. A4 never diagnoses other expenses as the margin-miss driver and mis-attributes it to depreciation."
    source_line: "L90 (other expenses), L85/L86/L81 (gross), L87 (employee), L94 (PBT)"
loop_back_to: "A4"
gap: "Surviving bear counter not incorporated: Other Expenses +80.9% YoY (L90) is the driver of the -172 bps operating EBITDA margin contraction A4 flags RED, not depreciation/finance. Graft the +283/+50/-505 bps decomposition, correct the summary-narrative 'entire decline sits in depreciation and interest' attribution, and add a management question on the other-expenses composition. Then re-emit A4 and re-run A5."
```
