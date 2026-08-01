# A5 ADVERSARY / COMPLETENESS AUDIT — SASKEN Q1 FY27 (Results, Reg 33, audited)

Target: `review_sasken_q1fy27.md` (A4). Re-derived independently from the A1 extract
(2092-line spine) and the A2 ledger. Every finding carries an A1 line cite. Units converted
by me per the A1 header (pages 1-15 Lakhs x0.01; 16-25 Crores x1; 26-57 Millions x0.1).

---

## AUDIT 1 — COVERAGE (fresh enumeration vs A2 ledger vs A4 review)

Fresh grep/sweep pass over the spine, diffed against the A2 count block (l.6-22 of ledger):

| Category | A2 count | My fresh count | Basis (A1 lines) | Orphan in A4? | Status |
|---|---|---|---|---|---|
| Notes (consol 3 / standalone 3) | 6 | 6 | l.454-474 / l.689-700 | no | MATCH |
| Board agenda items | 1 | 1 | l.75/78-79 (results approval only) | no | MATCH |
| Auditor Other-Matter paras | 3 | 3 | l.285-293, l.305-310, l.611-617 | no | MATCH |
| Segments | 2 | 2 | l.408-409 (SW Svcs / Product Solns) | no | MATCH |
| Group entities | 13 | 13 | l.139-151 | no | MATCH |
| Presentation slides | 32 | 32 | [page 26]-[page 57] | no (quant slides carried) | MATCH |
| Concall turns / questions | 0 / 0 | 0 / 0 | no transcript in filing | n/a | MATCH |
| Statement line-items | 99 | 99 | 36+27+17+19 | no | MATCH |
| Footnotes | 10 | 10 | l.384/389/435/678/755/756/758/1479/1546/1984 | n/a | MATCH |
| Digital signatures | 10 | 10 | Section 10 ledger | n/a | MATCH |
| ZERO_STANDING rows | 6 | 6 | l.351,380,411,654,674,747 | see note | MATCH |

**No row my fresh pass found is absent from the A2 ledger. No A2 count differs from mine.**
-> No loop-back to A2.

**Ledger-row -> A4 traceability (orphan test).** Every material ledger item is carried into A4:
- Other-Matters para 1 (unnamed component-audited step-down sub, l.285-293) -> A4 FN3 + Q5.
- Other-Matters para 2 / standalone Other-Matter (Ind AS 34 balancing figure, l.305-310/611-617)
  -> A4 Section 0, Section 1 table note, Section 3 QoQ.
- Standalone-vs-consolidated structural gap -> A4 Section 1C + FN2 (first-class metric).
- 13-entity list, Sasken Mexico "under liquidation" (l.152) -> A4 FN10; SSTPL (l.141) -> Q11.
- Segment note both segments, segment assets balloon (l.430) -> A4 Section 5 + FN7.
- Labour-code exceptional ZERO_STANDING (l.351/654) -> A4 FN1 + Section 4; nil inter-segment
  revenue (l.411) -> A4 FN1.
- All 16 quantitative slides (income stmt l.1695-1741, balance sheet l.1748-1767, segment
  gross margin l.1500-1513, 60x4x3/concentration l.1663-1679, KPI tiles) -> A4 Sections 5, 8, 6.

**Two immaterial reviewed-no-finding items (not FAILs).** (i) The three "Other equity / Reserves"
ZERO_STANDING blanks (l.380, l.674, l.747) are FY26 annual balance-sheet-date figures with no
quarter column; A4 does not cite them line-by-line but reaches net worth via the presentation
balance sheet (l.1763). Not gate-relevant. (ii) SEGMENT_CAPITAL_EMPLOYED_NOT_DISCLOSED
(l.440-442) is subsumed in A4's segment-asset / WC-balloon discussion (Section 5, FN7). Neither
bears on the five master-gate criteria. No loop-back warranted.

**Gate-criteria completeness test (explicitly requested).** Every disclosed number bearing on the
five criteria is in A4: EBITDA 9.5% (l.1705), Product Solutions Rs119.68 Cr (l.409), CFO absent
(no statement anywhere in 57 pages — confirmed by my own sweep; l.1748-1767 is a balance sheet,
not a cash-flow statement), WC-strategy language (only supply-chain, l.857-860), Top-5 both
readings (50.8% l.841/1009 vs 56% l.1669/1679/1396). No forward-commitment phrase missed
(l.1073/1183-1185/1241/1348 all logged to FN4/Q10-11). **COVERAGE COMPLETE.**

---

## AUDIT 2 — ARITHMETIC (independent recompute from A1 line cites, units converted by me)

| Metric | A4 value | My recompute | Source lines | Status |
|---|---|---|---|---|
| Blended (operating) EBITDA margin Q1FY27 | 9.5% | 32.12/339.24 = 9.47% -> 9.5%; PBT29.57+D&A10.78+Fin1.44-OI9.67=32.12 | l.349/346/345/339; xchk l.1705 (321.20 ₹M) | OK |
| Operating EBITDA Q1FY26 / Q4FY26 | 14.65 / 33.17 | 12.01+9.17+1.07-7.60=14.65; 37.43+10.32+0.75-15.33=33.17 | l.349/346/345/339 | OK |
| Consol PAT Q1FY27 | 23.52 | 2,352.15 lakhs x0.01 = 23.52 | l.356 | OK |
| Standalone PAT Q1FY27 | 28.86 | 2,885.58 x0.01 = 28.86 | l.659 | OK |
| Subsidiary net contribution swing Q4->Q1 | +9.26 -> -5.33 | 29.00-19.74=+9.26; 23.52-28.86=-5.33 (precise -5.334); swing -14.59 | l.356/659 | OK |
| NCI Q1FY27 | -1.34 | (133.84) x0.01 = -1.34 | l.373 | OK |
| Product Solutions revenue Q1FY27 vs Rs100 Cr gate | 119.68 (PASS) | 11,967.97 x0.01 = 119.68 > 100 | l.409 | OK |
| Product Solutions segment assets | 54.90 -> 128.32 (+133.7%) | 5,489.90->12,831.64 x0.01; 73.42/54.90=133.7% | l.430 | OK |
| Product Solutions segment result / margin | 16.00->7.08 (-55.8%); 12.8%->5.9% | 1,599.76->708.12 x0.01; 7.08/119.68=5.9%, 16.00/124.55=12.8% | l.418/409; l.1513 | OK |
| ETR consol Q1FY27 vs 25.17% statutory | 20.5% (467 bps below) | 604.94/2,957.09 = 20.46%; 25.17-20.5=4.67pp | l.353/352 | OK |
| Current-tax-only ETR | 32.6% | 965.18/2,957.09 = 32.64% | l.354/352 | OK |
| Deferred-tax credit | 3.60 | (360.24) x0.01 = -3.60 | l.355 | OK |
| Top-5 concentration | 50.8% vs 56% | both figures present verbatim | l.841/1009 vs l.1669/1679/1396 | OK (genuine inconsistency) |
| Net worth (shareholders' equity) | 854.75 (Mar) / 878.70 (Jun) | 8,547.50 / 8,786.97 ₹M x0.1 | l.1763 | OK |
| EPS basic Q1FY27 consol / standalone | 16.37 / 19.00 | as printed | l.382 / l.676 | OK |
| PAT bridge YoY (10.01->23.52 = +13.51) | +13.51 | PBT chg +17.56, tax drag -4.04, precise +13.516 | l.352/353 | OK |
| Core operating PBT ex-OI change | +15.49 (~115% of PAT chg) | 19.90-4.41=15.49; 15.49/13.51=114.7% | l.352/339 | OK |
| Receivables / inventory balloon | +57.69 / +30.08 | 2,324.16-1,747.27=576.89 ₹M x0.1; 653.84-353.07=300.77 x0.1 | l.1757 / l.1756 | OK |
| Component-audited sub (FN3) | 65.44 rev / 0.65 PAT / 19.3% / 0.99% | 6,543.83/64.71 lakhs; 65.44/339.24=19.3%; 0.65/65.44=0.99% | l.285-293 | OK |
| EBIT (presentation) Q1FY27 / YoY | 21.34 / +289.8% | 213.43 ₹M x0.1; vs 54.76 = +289.8% | l.1707 | OK |

**No mismatch above rounding. Every figure A4 relies on reproduces from its cited line, and every
cite I spot-checked (l.1705, l.1512-1513, l.1669, l.1748-1767, l.1348, l.963, l.285-293) supports
the number quoted.** The lone rounding artefact (component-wise PAT bridge sums to 13.52 vs the
precise 13.51) resolves in A4's favour — its stated 13.51 equals the direct calc (1,351.58 lakhs).
No arithmetic loop-back to A4.

---

## AUDIT 3 — ADVERSARIAL READ (strongest bear counter to A4's three most positive claims)

**Positive claim 1 (Section 2): "The YoY read is clean and strong — revenue +24.0%, operating
EBITDA margin +411 bps, core operating PBT ex-OI +351%."**
Strongest bear from the same text: consolidated PAT 23.52 is BELOW standalone 28.86 (l.356/659);
subsidiaries swung +9.26 -> -5.33 Cr and NCI turned -1.34 (l.373); the group print is a
subtraction from the services entity, and revenue is a +1.6% QoQ plateau (l.829) with Product
Solutions -3.9% QoQ and margin -690 bps (l.409/1513). **Survives on the evidence — but already
fully grafted into A4** (Section 1C, FN2, Section 3, flags). Not un-incorporated.

**Positive claim 2 (Section 5 / criterion 2): "Product Solutions Rs119.68 Cr clears the Rs100 Cr
gate (PASS)."**
Strongest bear: the topline was "supported" by "the contractual pass-through of increased memory
costs" (l.853-855), segment result HALVED (16.00->7.08, l.418) and segment assets +133.7% on
FALLING revenue (l.430) — capital absorbed by a shrinking, 5.9%-margin business. If the undisclosed
pass-through quantum is large, organic PS revenue could sit below Rs100 Cr, so a "genuine" pass is
unverifiable. **Survives — but already carried:** A4 marks criterion 2 "PASS (caveated)", logs FN5,
and asks Q3 (quantum of pass-through). Independent view: the criterion tests *reported audited*
revenue, which is a hard Rs119.68 Cr, so a literal PASS is correct; the caveat is the right
treatment, and materially the point is moot because the gate is ALREADY NOT CLEARED (criteria 1
and 4 FAIL, 3 INDETERMINATE) regardless of how criterion 2 resolves.

**Positive claim 3 (Section 4): "~115% of the YoY PAT change is recurring/core; high-quality P&L
improvement; the thesis does not depend on treasury."**
Strongest bear: the "quality" is P&L-only and standalone-only. The 20.5% ETR is flattered by a
Rs3.60 Cr deferred-tax credit; on a current-tax basis ETR is 32.6% and persistent DTA drawdown
steps future ETR up (FN6, l.353-355). At the consolidated/cash layer the picture inverts —
receivables +57.69 and inventory +30.08 (l.1756-1757) against no cash-flow statement, so
"high-quality earnings" coexists with unverifiable, likely-deteriorating cash conversion.
**Survives — but already carried** (Section 4 tax note, FN6, Section 8, watchlist RED-risk).

**Result: all three strongest bear counters are already incorporated in A4. No surviving
un-incorporated counter -> no A4 loop-back on adversarial grounds.**

### Verdict-logic attack (task items a-e)

(a) **Is PROCEED WITH CAVEATS defensible?** Yes, and it is the *only* correct verdict. The house
NEVER rule (CLAUDE.md) caps INDETERMINATE cash conversion at PROCEED WITH CAVEATS with the missing
evidence named — A4 names all four (CFO absent, WC strategy undisclosed, Top-5 inconsistent,
disputed tax/goodwill). It is NOT REWORK/INSUFFICIENT EVIDENCE because the results are analytically
usable (unmodified opinion l.462/696, tables reconcile) and the CFO absence is *structural* (Reg 33
carries no Q1 cash-flow statement), not a pipeline evidence failure. Nor is A4 too harsh: the verdict
proceeds and flags; the AVOID Decision Status is held by pre-committed discipline, not tightened.

(b) **Is the CFO-absence really INDETERMINATE, or did A4 soften a defensible negative inference?**
A4 did NOT soften it. Section 8 states the balance-sheet balloon (receivables +57.7, inventory +30.1)
makes the absence "material, not neutral," rates cash-conversion watchlist RED-risk, and notes the
WC build is NOT growth-induced because segment revenue fell (l.409). Drawing a *quantified* negative
CFO is correctly refused — no cash-flow statement exists, and the NEVER rule forbids resolving
INDETERMINATE either way. Handling is conservative and correct; and the verdict is invariant to it.

(c) **Decision Status / thesis-broken triggers.** A4 tests all five pre-committed triggers plus the
NEW Top-3 (Section 6C): (a) EBITDA<8% x2 NOT FIRED (9.5%/9.9%, l.1705); (b) Top-5>60% NOT FIRED
(max 56%, l.1669); (c) FY27 CFO<0 UNRESOLVED (not yet observable); (d) SSTPL<Rs50 Cr NOT ASSESSABLE;
(e) Borqs goodwill impairment NOT FIRED (l.1754); NEW Top-3>45% NOT ASSESSABLE. None formally fired,
so refraining from a Decision-Status change is correct.

(d) **Do the 10 required forward-signal/ambiguous findings each get a Questions-for-Management row?**
Verified. Required = FN2,3,4,5,6,7,8,9,11,12 (FN1 and FN10 are NEUTRAL-FACT, not required). Mapping:
FN12->Q1, FN7->Q2+Q12, FN5->Q3, FN8->Q4, FN3->Q5, FN2->Q6+Q11, FN9->Q7, FN6->Q8, FN11->Q9, FN4->Q10.
All 10 covered; A4's claim of 12 rows is accurate.

(e) **Should the Product Solutions PASS be caveated to INDETERMINATE?** A4 already caveats it and,
as shown above, the gate result does not turn on it. No change required.

---

## VERDICT

**COMPLETE.**

Coverage is complete (my fresh enumeration reproduces every A2 count with zero orphan and zero
missing rows; all material ledger rows are carried into A4). Arithmetic is sound (every load-bearing
figure reproduces from its A1 cite within rounding, units converted independently; no unsupported
quote found). The PROTOCOL VERDICT of **PROCEED WITH CAVEATS** is the correct and only defensible
call under the house NEVER rule — INDETERMINATE cash conversion caps there with the missing evidence
named, the master gate is correctly NOT CLEARED (criterion 1 FAIL 9.5%<10%, criterion 4 FAIL,
criterion 3 INDETERMINATE), and Decision Status correctly stays AVOID because no thesis-broken
trigger formally fired. All three strongest adversarial bear counters were already incorporated by
A4. No loop-back to A2, A3, or A4. This review may proceed to Notion save.

**Independent view on the verdict:** I concur with PROCEED WITH CAVEATS and with AVOID-held. If
anything the filing is a hair weaker than a clean caveat implies — the WC balloon sits in the
shrinking, margin-collapsing Product Solutions segment, the group headline is entirely standalone,
and the single most important signal (consolidated CFO) is simply absent — but every one of those
points is already surfaced as a flag, and the verdict ceiling is fixed by the INDETERMINATE rule
regardless, so no downgrade is available or warranted.

```yaml
stage: A5-adversary
company: "SASKEN"
quarter: "q1fy27"
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
