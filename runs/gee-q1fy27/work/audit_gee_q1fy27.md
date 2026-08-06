# A5 ADVERSARY / COMPLETENESS AUDIT — GEE Limited (GEE) — Q1 FY27

Fresh context. Re-derived independently from the A1 extract (raw Rs. Lakhs) and
diffed against the A2 ledger. A4 cites were checked, not trusted. All line
numbers below are `cat -n` anchors in the named file.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate)

The MANDATORY PLAIN-LANGUAGE BRIEF appears in the A4 review at lines 349-371,
all four labelled parts present and carrying real content:

| Part | Heading | A4 line(s) | Present / Empty |
|---|---|---|---|
| 1 | SUMMARY NARRATIVE | 353-359 (3 substantive paras, ~15 lines) | PRESENT |
| 2 | SECTOR INTELLIGENCE | 361-363 | PRESENT |
| 3 | BUSINESS-MODEL INTELLIGENCE | 365-367 | PRESENT |
| 4 | COMPETITION INTELLIGENCE | 369-371 | PRESENT |

**GATE 0: PASS.** All four parts present and non-empty.

---

## AUDIT 1 — COVERAGE (fresh independent grep enumeration vs A2 ledger)

I re-ran the enumeration over the extract from scratch (not reading A2's counts
first for the sweep) and then diffed.

| Category | A2 count | My fresh count | Orphan rows | Status |
|---|---|---|---|---|
| notes (lines 111-127) | 6 | 6 | none | MATCH |
| line_items (lines 73-110) | 28 | 28 | none | MATCH |
| zero_standing (lines 89, 95, 96, 106) | 4 | 4 | none | MATCH |
| agenda_items (lines 34-46) | 5 | 5 | none | MATCH |
| auditor_paras (lines 158-188) | 5 | 5 | none | MATCH |
| signature_blocks (52-62, 129-140, 190-201) | 3 | 3 | none | MATCH |
| entities | 0 | 0 | n/a | MATCH |
| turns / questions / slides | 0 | 0 | n/a | MATCH |

Fresh-pass detail confirming the four ZERO_STANDING rows: exceptional-item dash
Q1FY26 (line 89); Previous Year Tax dash Q1FY27 & Q1FY26 (line 95); Deferred tax
dash Q1FY27 & Q1FY26 (line 96); Other Equity blank three interim cols (line 106).
No fifth zero-standing row exists. No row my fresh pass found is missing from the
ledger; no ledger row is absent from my fresh pass.

**Ledger-row → A4 citation check (every row cited OR reviewed-no-finding):**
- All 6 notes: cited in A4 Step 0D table (lines 37-43). OK.
- All 28 line items: cited in A4 Step 1 table (lines 59-81); the three tax
  sub-lines are consolidated by A4 into "Tax Expense — total (line 97)" and are
  each accounted for — Current tax appears in the ETR recompute (A4 line 97,
  "230.24/914.79"), Deferred tax is cited at A4 lines 97 and 174 (line 96, F8.1),
  and Previous Year Tax (line 95, value 1.04 L = ₹0.01 Cr) is subsumed in the
  cited tax-total reconciliation and the F8.1 tax forensic. Not an orphan.
- DATE_INCONSISTENCY (F14.1): cited A4 Step 0D note-6 row, Step 8.5 Q3, flags.
- ZERO_STANDING rows 14/25: cited A4 line 83; rows 18/19 subsumed as above.
- SCOPE_LIMITATION (Board's/Corp Gov Report absent): carried by A4 as an explicit
  UNREVIEWED flag → Role 6 (A4 flags list, line 421). Correctly not assumed
  screened.
- NO_DIGITAL_TIMESTAMP (auditor block) / OCR_ARTIFACT / FORMATTING_ANOMALY:
  quality flags, no A3 finding elevated; A4 reviews the auditor block
  substantively (opinion, FRN, UDIN, name — Step 0D line 45). Reviewed-no-finding.

**AUDIT 1: PASS.** Counts reconcile exactly; no orphan rows; no rows missing from
the ledger.

---

## AUDIT 2 — ARITHMETIC (every derived metric recomputed from raw Lakhs)

Unit rule applied as A4 states: Cr = Lakhs × 0.01. Rounding tolerance ±0.01 Cr /
±0.1 pp.

**Step 1 conversions (spot-checked all 22 value rows × 4 cols):** every Lakhs→Cr
conversion in the A4 Step 1 table (lines 59-81) is correct.

**Derived-metric block (A4 lines 89-95) — all recomputed and CORRECT:**

| Metric | A4 value (Q1FY27) | My recompute (from Lakhs) | Status |
|---|---|---|---|
| Operating EBITDA | 8.00 | 545.25+100.74+184.82−30.89 = 799.92 L = 8.00 | OK |
| Op EBITDA Margin | 7.78% | 799.92/10,285.66 = 7.78% | OK |
| Reported EBITDA (incl OI) | 8.31 | 545.25+100.74+184.82 = 830.81 L = 8.31 | OK |
| Core PBT ex-OI | 5.14 | 545.25−30.89 = 514.36 L = 5.14 | OK |
| Other Income / PBT | 3.38% | 30.89/914.79 = 3.38% | OK |
| Effective Tax Rate | 25.17% | 230.24/914.79 = 25.17% (= Q1FY26 32.82/130.41) | OK |
| PAT Margin | 6.66% | 684.55/10,285.66 = 6.66% | OK |

Op EBITDA / margin / ETR / PAT-margin also recomputed correct for Q1FY26, Q4FY26
and FY26 (all four columns). Reported-EBITDA, Core-PBT, OI/PBT: all correct.

**Step 2 YoY (A4 lines 107-117) — recomputed, all CORRECT:** Revenue +29.9%,
Op EBITDA +76.1%, margin +204 bps, Dep −0.8%, Finance −17.7%, EBIT +98.3%,
OI +1260.8%, Core PBT +301.4%, PBT-after-exc +601.5%, PAT +601.5%, EPS +594.7%.
Exceptional = 369.55/914.79 = **40.4% of PBT-after-exc**: correct.

**Step 3 QoQ / Step 6A (A4 lines 148-149, 216-218) — recomputed, all CORRECT:**
Revenue −8.3% QoQ, margin −214 bps QoQ, ex-exc PBT −43.5% QoQ; annualised
₹411 Cr / +11.5% vs FY26; normalised PBT ₹5.45 Cr = +4.2x YoY. All OK.

### FAIL — the PAT bridge total is mis-converted (Step 2 diag 4 and Step 4)

| Metric | A4 value | My recompute | Source line | Status |
|---|---|---|---|---|
| Reported PAT YoY change (Cr) | **+6.87 Cr** | **+5.87 Cr** | extract L99: 684.55 − 97.59 = 586.96 L; ×0.01 = 5.87 Cr | **FAIL** |

Raw: PAT Q1FY27 = 684.55 L, Q1FY26 = 97.59 L (extract line 99). Difference =
**586.96 L = ₹5.87 Cr**, NOT ₹6.87 Cr. A4's own Lakhs figure (+586.96 L) is
correct and its bridge components sum to it (135.83+209.91+0.81+39.67+28.62+
369.55−197.42 = 586.96 L). Only the Crore label is wrong — a 5.87→6.87
transcription slip, ₹1.00 Cr, far above rounding. A4's own walk at line 127 also
sums to 5.88 (4.15 + 3.70 − 1.97), and Step 1 gives PAT 6.85 vs 0.98 whose
difference is 5.87 — so 6.87 is internally contradicted three ways.

Occurrences to fix in A4: line 127 ("= +₹6.87 Cr PAT"), line 156 ("₹0.98 Cr →
₹6.85 Cr = +₹6.87 Cr"), line 167 (bridge-table total "+6.87"), line 170
("+₹6.87 Cr").

**Propagated FAIL — Step 4 recurring/non-recurring percentages (A4 line 170).**
Because the wrong ₹6.87 Cr was used as the denominator, the split is wrong AND it
does not sum to 100% (56.3 + 4.2 + 53.9 − 28.7 = 85.7%). Recomputed against the
correct ₹586.96 L base:

| Component | A4 % (÷6.87) | Correct % (÷5.87) | Raw (L) |
|---|---|---|---|
| Core operating (vol+margin+D+fin) | 56.3% | **65.8%** | 386.22 |
| Other Income | 4.2% | **4.9%** | 28.62 |
| Exceptional property gain | 53.9% | **63.0%** | 369.55 |
| Tax drag | −28.7% | **−33.6%** | −197.42 |

The corrected figures sum to 100.1% (rounding); A4's do not. Note A4's OWN Step 2
diag 4 (line 127) already states the exceptional is **"63.0% of the … PAT
increase"** — i.e. Step 2 used the correct ₹5.87 Cr base while Step 4 used the
wrong ₹6.87 Cr base. The review contradicts itself; the arithmetic root cause is
the 6.87 error.

**AUDIT 2: FAIL → loop back to A4.** One raw-conversion error (₹6.87 vs ₹5.87 Cr)
and its propagated Step-4 percentage block; internal contradiction with Step 2's
own 63.0%.

---

## AUDIT 3 — ADVERSARIAL READ (3 most positive A4 claims; bear counter from same text)

**Positive claim 1 (A4 lines 114, 125): "Core operating PBT ex-OI grew +301.4%
YoY (4.0x) — the single most important honest signal; core genuinely improved."**
Strongest bear counter FROM THE EXTRACT: the 4.0x is measured off an abnormally
depressed Q1FY26 base (core PBT ₹1.28 Cr, 5.74% margin); against the more recent
Q4FY26 (core PBT ₹8.54 Cr) this quarter is DOWN ~40% (extract line 88:
966.47→545.25). And purchase of stock-in-trade leapt from ₹0.06 Cr to ₹13.61 Cr
(extract line 79) while inventory build shrank (line 80: (405.18)→(76.73)) — part
of the "operating" gain is a thin-margin trading-mix shift, not core
manufacturing. **Survives, but ALREADY INCORPORATED** by A4 (Step 3 QoQ −43.5%;
brief part 3 trading drift; flag line 419). No new graft required.

**Positive claim 2 (A4 lines 107-109, 123): "Revenue +29.9% YoY strong topline;
+204 bps genuine margin expansion."** Bear counter from extract: revenue is DOWN
8.3% QoQ (112.16→102.86, line 73) and margin is DOWN 214 bps QoQ; 7.78% remains
below the FY26 9.05% and Q4 9.92%, so on any recent basis margin contracted, and
the YoY topline is partly resale of bought-in goods (line 79). **Survives, but
ALREADY INCORPORATED** (Step 3; diag 2; brief). No new graft required.

**Positive claim 3 (A4 lines 127, 170: "Headline growth is HALF real, HALF
one-off" / Step 4 exceptional = 53.9%, core = 56.3%).** Bear counter from the same
numbers: the ₹3.70 Cr property gain is **63.0% of the ₹5.87 Cr reported PAT
increase** (369.55/586.96), i.e. nearly two-thirds one-off, NOT "roughly half."
A4 understates the one-off share because Step 4 divides by the erroneous ₹6.87 Cr.
**Survives and is NOT correctly incorporated** (Step 4 contradicts Step 2's own
63.0%). **MUST be grafted into A4** — correct the split to core 65.8% / OI 4.9% /
exceptional 63.0% / tax −33.6% and align the "half real, half one-off" narrative
to "roughly one-third real, closer to two-thirds one-off" on the reported-PAT
basis. This is the same defect as the AUDIT 2 arithmetic FAIL.

---

## VERDICT

**INCOMPLETE.**

- Failing agent: **A4**.
- Exact gap: **Step-4 PAT bridge mis-converts the reported PAT YoY change as
  ₹6.87 Cr; the raw figure is 684.55 − 97.59 = 586.96 L = ₹5.87 Cr (extract line
  99). Fix the four occurrences (A4 lines 127, 156, 167, 170) and recompute the
  Step-4 recurring/non-recurring split against ₹5.87 Cr (core 65.8% / OI 4.9% /
  exceptional 63.0% / tax −33.6%), which must equal Step 2's own 63.0% one-off
  figure. Same correction resolves the surviving bear counter (the exceptional
  is ~63% of the PAT jump, not "half").** Deliverable-completeness and coverage
  both PASS; the block is arithmetic-only, so once A4 corrects and re-emits, no
  A2/A3 rework is needed.

```yaml
stage: A5-adversary
company: "GEE"
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
  - metric: "Reported PAT YoY change (Cr)"
    a4_value: "+6.87 Cr"
    recomputed: "+5.87 Cr (586.96 L)"
    source_line: "extract L99: 684.55 - 97.59 = 586.96 L x0.01 = 5.87 Cr (A4 lines 127,156,167,170)"
  - metric: "Step-4 core-operating share of PAT increase"
    a4_value: "56.3%"
    recomputed: "65.8% (386.22/586.96)"
    source_line: "A4 line 170"
  - metric: "Step-4 exceptional share of PAT increase"
    a4_value: "53.9%"
    recomputed: "63.0% (369.55/586.96)"
    source_line: "A4 line 170 (contradicts A4 line 127 own 63.0%)"
  - metric: "Step-4 Other-Income share of PAT increase"
    a4_value: "4.2%"
    recomputed: "4.9% (28.62/586.96)"
    source_line: "A4 line 170"
  - metric: "Step-4 tax-drag share of PAT increase"
    a4_value: "-28.7%"
    recomputed: "-33.6% (197.42/586.96)"
    source_line: "A4 line 170"
surviving_bear_counters:
  - claim: "Headline growth is HALF real, HALF one-off (Step 4: exceptional 53.9%)"
    counter: "The property gain is 63.0% of the reported PAT increase (369.55/586.96) - nearly two-thirds one-off, not half; A4 understates it via the wrong 6.87 Cr denominator."
    source_line: "extract L99 & L122-123; A4 lines 127 vs 170"
loop_back_to: "A4"
gap: "Step-4 PAT bridge states reported PAT YoY change as +6.87 Cr; raw is 684.55-97.59=586.96 L=+5.87 Cr (extract L99). Correct A4 lines 127,156,167,170 and recompute the Step-4 recurring/non-recurring split against 5.87 Cr (core 65.8% / OI 4.9% / exceptional 63.0% / tax -33.6%), reconciling with Step 2's own 63.0%. Arithmetic-only; no A2/A3 rework."
```
