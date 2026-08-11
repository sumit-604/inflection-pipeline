# A5 ADVERSARY / COMPLETENESS AUDIT — ECOSMOBILITY Q1 FY27
## Target: review_ecosmobility_q1fy27.md (A4 ANALYST) | Auditor: A5, fresh context
## Inputs seen: A4 review, A1 extract (spine), A2 ledger, VERIFIED FIGURES SUPPLEMENT (mechanical artifact resolving 14 OCR-corrupted total rows). A3 reasoning NOT seen — all cites re-derived.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate, run first)

PLAIN-LANGUAGE BRIEF present at review L446-466. Four labelled parts checked:

| Brief part | Location | Present? | Real content (not placeholder)? |
|------------|----------|----------|----------------------------------|
| (1) Summary narrative (10-20 lines) | L448-450 | PRESENT | Yes — 1 dense paragraph, ~18 lines of substance; covers revenue, flat EBITDA, margin, profitless growth, fired trigger, diversification, cash-flow gap, single metric to watch |
| (2) SECTOR intelligence | L452-456 | PRESENT | Yes — 4 bullets, each provenance-labelled (this-quarter filing vs Notion/prior-work) |
| (3) BUSINESS-MODEL intelligence | L458-461 | PRESENT | Yes — 3 bullets, provenance-labelled, unit economics quantified |
| (4) COMPETITION intelligence | L463-466 | PRESENT | Yes — 3 bullets, provenance-labelled, names "metric not disclosed" where absent |

All three intelligence blocks carry explicit provenance labels ("this quarter's filing" / "Notion/prior-work" / "metric not disclosed"). **GATE 0: PASS.** No missing or empty part.

---

## AUDIT 1 — COVERAGE (independent re-enumeration vs A2 ledger)

Fresh grep/manual sweep of the A1 extract, diffed against the A2 count test:

| Category | A2 count | My fresh count | Orphan rows | Status |
|----------|---------:|---------------:|-------------|--------|
| Notes (paras L192-210) | 6 | 6 (L193-195, 196-198, 199-201, 202-204, 205-208, 209-210) | none | MATCH |
| Agenda / board-outcome items (L34-50) | 5 | 5 | none | MATCH |
| Line items (standalone 23 + consol 31) | 54 | 54 | none | MATCH |
| Zero-standing (current-qtr dash/0.00) | 4 | 4 (L99, L137, L138, L147) | none | MATCH |
| Auditor paras (both reports) | 10 | 10 (incl. unnumbered SEBI-circular para L333-335) | none | MATCH |
| Annexure-B rows | 10 | 10 | none | MATCH |
| Annexure-C rows | 7 | 7 | none | MATCH |
| Signature blocks | 4 | 4 | none | MATCH |
| Entities (consol scope) | 0 (OCR lost) | 0 in spine; 5 in supplement (1 holding + 4 subs) | none | MATCH (resolved by supplement, not orphan) |

**No row found by my pass that the ledger lacks → no A2 loop-back.**

Every ledger row cited in A4 or reviewed-no-finding:
- ZERO_STANDING (4): all four surfaced — purchase of stock-in-trade Q1FY27 nil (review L89), changes-in-stock 0.000 (L90, F1-01), tax-relating-to-earlier-years NIL both entities (L236, L312 Step 6B row 5). COVERED.
- TOTALS_CROSS_CHECK_NEEDED (14): all superseded by supplement; A4 uses supplement values with correct provenance note (review L15, L67 etc.). COVERED.
- Board-outcome items 2-5: item 2 object clause (Step 6D, Q3/Q4 QfM, monitorables); item 3 Loomba re-appointment (monitorables, Annexure-C, F13-02); item 4 AGM 21 Sep 2026 (throughout); item 5 record date 18 Aug 2026 (monitorables, Note 6). NONE DROPPED.
- FAMILY_RELATIONSHIP, SINGLE_SEGMENT, ROUNDING_ZERO, UDIN_OCR_UNCERTAIN (resolved), OCR_ILLEGIBLE (CMD sig, administrative): all addressed or legitimately reviewed-no-finding.

A3 findings (11 claimed incorporated): each maps to a real ledger/supplement item. Every FORWARD-SIGNAL / AMBIGUOUS finding has a Questions-for-Management row: F2-02→Q1, F15-01→Q2, F13-01→Q3, F6-01→Q4, F13-03→Q5, F14-01→Q6, F15-02→Q7. Factual/PASS findings (F1-01 rounding, F2-01 gap-under-trigger, F8-01 tax-base, F13-02 governance) are handled inline and correctly do not require a QfM row. **COVERAGE: PASS — no orphan rows, no A2/A3 loop-back on coverage.**

---

## AUDIT 2 — ARITHMETIC (every derived metric re-computed from supplement raw numbers, ₹ million → ×0.1 = ₹ Cr)

Operating EBITDA = PBT + D&A + Finance − Other Income. Reported EBITDA = PBT + D&A + Finance.

| Metric | A4 value | My recompute | Source (supplement mn) | Status |
|--------|---------:|-------------:|------------------------|--------|
| Op EBITDA consol Q1FY27 | 21.848 | 191.64+61.55+2.77−37.48 = 218.48 → 21.848 | L51,48,47,41 | MATCH |
| Op EBITDA consol Q1FY26 | 21.855 | 186.68+58.30+2.32−28.75 = 218.55 → 21.855 | L51,48,47,41 | MATCH |
| Op EBITDA consol Q4FY26 | 24.153 | 196.53+79.43+1.75−36.18 = 241.53 → 24.153 | L51,48,47,41 | MATCH |
| Op EBITDA margin consol Q1FY27 | 10.34% | 218.48/2113.72 = 10.336% | L40 | MATCH |
| Op EBITDA margin consol Q1FY26 | 12.07% | 218.55/1811.19 = 12.066% | L40 | MATCH |
| Op EBITDA margin consol Q4FY26 | 11.68% | 241.53/2067.60 = 11.682% | L40 | MATCH |
| Op EBITDA margin standalone Q1FY27 | 10.07% | 207.59/2060.56 = 10.074% | L13 | MATCH |
| Op EBITDA margin standalone Q1FY26 | 12.30% | 218.49/1776.43 = 12.299% | L13 | MATCH |
| Consol margin YoY | −173 bps | 10.336−12.066 = −1.730 pp | — | MATCH |
| Standalone margin YoY | −223 bps | 10.074−12.299 = −2.225 pp | — | MATCH |
| Reported EBITDA margin consol Q1FY27 ÷rev | 12.11% | 255.96/2113.72 = 12.109% | L40,51,48,47 | MATCH |
| Reported EBITDA margin consol Q1FY27 ÷total inc | 11.90% | 255.96/2151.20 = 11.898% | L42 | MATCH |
| **Reported EBITDA margin consol Q4FY26 ÷rev** | **13.43%** | 277.71/2067.60 = **13.430%** | L40,51,48,47 | MATCH — see ADVERSARIAL |
| **Reported EBITDA margin consol Q4FY26 ÷total inc** | 13.20% | 277.71/2103.78 = **13.200%** | L42 | MATCH — see ADVERSARIAL |
| Reported EBITDA margin consol Q1FY26 ÷rev | 13.65% | 247.30/1811.19 = 13.653% | — | MATCH |
| Core PBT ex-OI consol Q1FY27 | 15.416 | 191.64−37.48 = 154.16 → 15.416 | L51,41 | MATCH |
| Core PBT ex-OI consol Q1FY26 | 15.793 | 186.68−28.75 = 157.93 → 15.793 | L51,41 | MATCH |
| Core PBT ex-OI YoY consol | −2.39% | 15.416/15.793−1 = −2.387% | — | MATCH |
| Core PBT ex-OI YoY standalone | −4.04% | 15.155/15.793−1 = −4.039% | — | MATCH |
| Effective tax rate consol Q1FY27 | 24.08% | 46.14/191.64 = 24.077% | L55,51 | MATCH |
| Effective tax rate consol Q1FY26 | 28.82% | 53.81/186.68 = 28.824% | L55,51 | MATCH |
| Effective tax rate consol Q4FY26 | 19.93% | 39.16/196.53 = 19.926% | L55,51 | MATCH |
| PAT margin consol Q1FY27 | 6.88% | 145.50/2113.72 = 6.884% | L56,40 | MATCH |
| PAT YoY consol | +9.51% | 14.550/13.287−1 = 9.506% | L56 | MATCH |
| PAT YoY standalone | +8.56% | 14.399/13.264−1 = 8.557% | L27 | MATCH |
| Revenue YoY consol | +16.7% | 211.372/181.119−1 = 16.70% | L40 | MATCH |
| Revenue YoY standalone | +16.0% | 206.056/177.643−1 = 15.99% | L13 | MATCH |
| Op EBITDA YoY consol (flat) | −0.03% | 21.848/21.855−1 = −0.032% | — | MATCH |
| S−C PAT gap Q1FY27 (labelled S−C, computes consol−standalone) | +0.151 | 14.550−14.399 = +0.151 | L56,27 | MATCH (see NOTE-b) |
| S−C gap swing Q4→Q1 | 2.58 pp | −1.53%→+1.05% = 2.58 pp | — | MATCH (under 5pp) |
| Subsidiary revenue YoY | +52.9% | 5.316/3.476−1 = 52.9% | — | MATCH |
| Consol PAT bridge sum | +1.263 | −0.007−0.325−0.045+0.873+0.767 = +1.263 | — | MATCH |
| Standalone PAT bridge sum | +1.135 | −1.090+0.481−0.029+0.954+0.819 = +1.135 | — | MATCH |
| Non-operating % of PAT growth | ~130% | 1.640/1.263 = 129.8% | — | MATCH |
| Reserve gap consol−standalone | 2.06% | 5.114/247.823 = 2.06% | supp L33,66 | MATCH |
| ₹mn→₹Cr conversion | ×0.1 | 10 mn = 1 Cr | supp L5 | MATCH |

**Arithmetic verdict: every derived metric reproduces within rounding. No arithmetic mismatch above rounding.**

Two non-fatal annotation defects (do NOT change any thesis metric; flagged for A4 cleanup):
- **NOTE-a (share-count typo, review L48 + L428):** dividend outflow "~₹14.28 Cr on **60 Cr shares**." Paid-up ₹120 mn at FV ₹2 = 60 **million** = **6 crore** shares. ₹2.38 × 6 Cr = ₹14.28 Cr (the rupee figure is correct); "60 Cr shares" is wrong by 10× and internally contradicts its own ₹14.28 Cr (2.38 × 60 Cr would be ₹142.8 Cr). Cosmetic; the load-bearing outflow is right.
- **NOTE-b (label sign, Step 4.5):** the row titled "S–C PAT gap" actually computes consolidated−standalone (Q4FY26 shown −0.244 = 15.737−15.981). Values and the "subsidiaries add/drag" reading are internally consistent; only the S–C label is sign-flipped. Cosmetic.

---

## AUDIT 3 — ADVERSARIAL READ

### The three headline POSITIVE claims already carry their bear counters (good)
1. "Revenue +16.7% YoY, growth holding." Bear counter (same text): not accelerating (identical to Q4FY26 +16.7%), ₹845 Cr annualised is short of ~₹900 Cr FY27 base and the FY28 ₹1,000-1,200 Cr target, and it is profitless (op EBITDA flat, −173 bps). **Already incorporated** (Step 2C dx1; profitless-growth thread). Not a surviving new counter.
2. "Reported PAT +9.5% YoY." Bear counter: ~130% of the growth is non-operating (Other Income +₹0.873 Cr, tax −₹0.767 Cr); core operating PBT fell 2.4-4.0%; strip Other Income and PAT growth collapses to ~+3%. **Already incorporated** (Step 4 bridge). Not surviving.
3. "Auditor CLEAN / near-zero leverage / asset-light moat." Bear counter: new WOS Ecos Fleet Management (owned-fleet/capex risk), event-management pivot into unproven economics, subsidiaries +53% revenue at breakeven, cash conversion INDETERMINATE. **Already incorporated** (flags, Step 6D, QfM Q2). Not surviving.

The profitless-growth / Other-Income-and-tax bridge claim is **SUPPORTED**: bridge sums exactly (+1.263 consol / +1.135 standalone), core PBT decline is real on both perimeters, and the ~130% non-operating share reconciles. No overstatement here.

INDETERMINATE cash-conversion cap (CLAUDE.md rule): cash conversion is flagged INDETERMINATE with the missing evidence named (review L279, Flag 2) and does **not** silently resolve to a clean PROCEED. The verdict issued is PROCEED WITH FLAGS, which sits at or below the PROCEED-WITH-CAVEATS ceiling in the CLAUDE.md severity order and names the missing evidence. **Cap correctly applied.** No zero-value lines or Board-Outcome items 2-5 dropped (confirmed in Coverage).

### SURVIVING COUNTER (must be grafted into A4 before save) — the "trigger FORMALLY FIRED" claim

The pre-committed trigger, quoted by A4 itself (review L28): **"reported EBITDA margin below 12% for 3 consecutive quarters, on the CONSOLIDATED perimeter."** The operative measure is **reported EBITDA margin**, consolidated.

Re-deriving the reported EBITDA margin (consolidated) for every quarter with hard data in this filing:

| Quarter | Reported EBITDA (₹ Cr) | ÷ rev-from-ops | ÷ total income | Below 12%? |
|---------|-----------------------:|---------------:|---------------:|------------|
| Q1 FY26 | 24.730 | 13.65% | 13.44% | NO |
| Q4 FY26 | 27.771 | **13.43%** | **13.20%** | **NO** |
| Q1 FY27 | 25.596 | 12.11% | 11.90% | Only on total-income denom |

On the trigger's **own literal measure (reported EBITDA margin)**, there is **no 3-consecutive-quarter sub-12% run**. The immediately preceding quarter, Q4 FY26, prints **13.43% (÷rev) / 13.20% (÷total income)** — clearly above 12% — which **resets any consecutive count**. Q1 FY27 is at most a **single** sub-12% quarter, and only on the total-income denominator (12.11% on rev-from-ops is above 12%). These Q4 FY26 reported figures **sit in A4's own table (review L118-119)**.

A4 reaches "FORMALLY FIRED" only by (i) silently substituting **operating** EBITDA margin for the pre-committed **reported** measure, and (ii) leaning on Notion's Q2/Q3 FY26 "<12%" baselines, which are themselves operating-basis (A4 concedes Q4FY26's "<12%" is the 11.68% operating figure, L327) and are unverifiable from this filing. A4 does flag a denominator ambiguity, but it frames that ambiguity as affecting **only Q1 FY27's borderline reading (11.90 vs 12.11)** — it never surfaces that on the literal reported measure the count is already broken one quarter earlier by Q4 FY26's 13.43%/13.20%.

Consequence: the review's most decision-relevant assertion — the prominent verdict line "**Pre-committed thesis-break trigger FORMALLY FIRED**" (L322, L330, L438) and its 8A-W mapping "WATCHLIST → AVOID" (L374) — is **NOT defensible on the trigger's own wording**. The strongest accurate statement the extract supports is: *fired on the operating-EBITDA measure; NOT fired on the pre-committed reported-EBITDA measure, where Q4 FY26 (13.43%/13.20%) breaks the consecutive-sub-12% run and Q1 FY27 is at most one borderline quarter.*

This counter is **not present** in A4 and **survives**. Under A5 rule 2 (A4 owns an unincorporated surviving counter), A4 must:
1. Soften the headline from unconditional "FORMALLY FIRED" to **measure-conditional**, and explicitly state that on the literal reported measure the trigger has **not** fired (Q4 FY26 reported = 13.43%/13.20%, above 12%).
2. Correct the "3-consecutive-quarter threshold already crossed at Q4 FY26" framing (L330), which is true only on the operating measure.
3. Carry the denominator/measure reconciliation to the human as the gating question **before** any WATCHLIST→AVOID ratification — which A4 partially does, but on the mistaken premise that only Q1 FY27's denominator is in doubt.

The margin *compression* is real and correctly evidenced (op EBITDA flat on +16.7% revenue; −173 bps YoY; deepening profitless growth) and should still travel as a prominent flag. What fails is the specific claim that the **pre-committed trigger, as written, has fired**.

---

## VERDICT

**INCOMPLETE.** Loop back to **A4**.

**Exact gap:** A4's prominent verdict "Pre-committed thesis-break trigger FORMALLY FIRED" (review L322/L330/L438) and the consequent 8A-W "WATCHLIST → AVOID" mapping are not defensible on the trigger's pre-committed measure. The trigger is written on **consolidated reported EBITDA margin < 12% for 3 consecutive quarters** (L28); on that measure the run is broken by Q4 FY26 reported EBITDA margin of **13.43% (÷rev) / 13.20% (÷total income)** — both above 12% and both already in A4's own table (L118-119) — so Q1 FY27 is at most one sub-12% quarter (and only on the total-income denominator; 12.11% on rev-from-ops). The "fired" conclusion holds only after silently switching to the **operating** EBITDA measure plus unverifiable operating-basis Notion baselines for Q2/Q3 FY26. A4 must graft the surviving counter, re-state the trigger verdict as measure-conditional (fired on operating basis; NOT fired on the literal reported basis), and correct the "already crossed at Q4 FY26" framing before save. Two cosmetic A4 cleanups also noted: the "60 Cr shares" share-count typo (should be 6 Cr; ₹14.28 Cr outflow is correct) and the sign-flipped "S–C PAT gap" label. Arithmetic is otherwise clean; coverage is complete; the mandatory PLAIN-LANGUAGE BRIEF and all three provenance-labelled intelligence blocks are present. No A2 or A3 loop-back.

```yaml
stage: A5-adversary
company: "ECOSMOBILITY"
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
  - claim: "Pre-committed thesis-break trigger FORMALLY FIRED (consolidated EBITDA margin sub-12% for 3+ consecutive quarters); maps WATCHLIST -> AVOID"
    counter: "Trigger is written on REPORTED EBITDA margin (review L28). On that measure Q4 FY26 reported EBITDA margin = 13.43% (/rev) / 13.20% (/total income), both ABOVE 12%, breaking any 3-consecutive sub-12% run; Q1 FY27 is at most one sub-12% quarter (11.90% total-income only; 12.11% on rev-from-ops). Trigger has NOT fired on its literal measure — 'fired' holds only after switching to OPERATING EBITDA plus unverifiable operating-basis Notion baselines for Q2/Q3 FY26. Q4 FY26 reported figures sit in A4's own table L118-119."
    source_line: "review L28, L118-119, L322, L330, L374, L438; supplement L40-51"
loop_back_to: "A4"
gap: "Trigger-fired headline (L322/L330/L438) and 8A-W WATCHLIST->AVOID mapping (L374) not defensible on the pre-committed REPORTED-EBITDA measure: Q4 FY26 reported EBITDA margin 13.43%/13.20% (above 12%) breaks the consecutive count; Q1 FY27 is at most one borderline sub-12% quarter on the total-income denominator only. A4 must graft the surviving counter, restate the trigger verdict as measure-conditional (fired on operating basis; NOT fired on literal reported basis), and correct the 'already crossed at Q4 FY26' framing before save. Minor: '60 Cr shares' typo (should be 6 Cr) and sign-flipped 'S-C PAT gap' label."
```
