# A5 ADVERSARY / COMPLETENESS AUDIT
# Man Industries (India) Ltd (MANINDS) | Corporate Presentation 01-Sep-2026 | Quarter 2026-09
# Auditing: work/final-gate/review_maninds_2026-09.md (A4). Fresh context. Source PDF NOT opened.
# Inputs read: A1 fulltext, A1 structured (R001-R335), A2 ledger (MF01-MF10), A4 review.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate, run first)

PLAIN-LANGUAGE BRIEF present at review lines 381-452. All four labelled parts present and non-empty:

| Part | Location | Present | Content check |
|---|---|---|---|
| 1. Summary narrative (10-20 lines) | lines 383-411 | present | ~25 lines of real prose, sourced |
| 2. Sector intelligence | lines 413-424 | present | order-book/steel-spread model, Gulf capex, named gap |
| 3. Business-model intelligence | lines 426-438 | present | converter->value-added ladder, three mix shifts |
| 4. Competition intelligence | lines 440-452 | present | Aramco AVL moat, peer set, downside case |

GATE 0: PASS. No placeholder, no empty heading.

---

## AUDIT 1 — COVERAGE (independent re-enumeration vs A2 ledger)

Fresh grep pass over A1 structured + fulltext spine:

| Category | A2 count | My fresh count | Method | Status |
|---|---|---|---|---|
| Slides / pages | 37 | 37 | grep `[page N]` in fulltext = 37 | match |
| Structured row IDs | 335 | 335 | grep `^R### |` = 335 | match |
| NUMBER | 223 | 223 | grep `| NUMBER |` = 223 | match |
| ENTITY (incl SUMMARY) | 49 | 49 | grep `| ENTITY|ENTITY-SUMMARY |` = 49 | match |
| FORWARD | 20 | 20 | grep `| FORWARD |` = 20 | match |
| DATE | 43 | 43 | grep `| DATE |` = 43 | match |
| MISSING_FROM_STRUCTURED | 10 (MF01-MF10) | 10 accounted | ledger §2-§4 | match on the ten; +1 new miss found below |
| ID accountability | orphan_ids [] | R001-R335 all grouped in ledger §1 | — | match on ID grouping |

Row-ID accountability: every R001-R335 is grouped to a slide in ledger §1 and A4 Step 1 claims 335/335 + MF01-MF10 reviewed. On the pure ID/count test the ledger is clean.

TWO coverage defects survive the fresh pass:

- COV-1 (MISSING, loop A2): a fresh-pass unit is absent from BOTH the structured file and the ledger.
  Fulltext page 26 line 730 reads: "NPC carried an order position of USD 120 Million (Rs1,130-1,150 crore)
  (including executed to date)...". The qualifier "(including executed to date)" is NOT in R144's verbatim
  value ("USD 120 Million (Rs1,130-1,150 crore)"), nor in the order-book restatements R114 / R119 / R285,
  nor anywhere in the ledger (grep "executed to date" = 0 hits in structured and in ledger). This is a
  material dropped qualifier of exactly the class A2's MF mechanism exists to catch (cf. MF10). It should
  be logged MF11 (MISSING_FROM_STRUCTURED, qualifies R144/R114/R119/R285). A2 must add it.

- COV-2 (MISSING, loop A4; A3 also missed): R115 (Acquire-route "15-18% EBITDA Margin") and R116
  ("11-14% PAT margin"), slide 24, are grouped in ledger §1 but are never cited or addressed anywhere in
  the A4 review (grep "15-18%|11-14%" in review = 0 hits). These are not decorative rows: they are
  management's OWN accretion guidance for the acquisition and they contradict A4's central positive claim
  built on NPC CY2025 24.8% EBITDA / 18.1% PAT (R124/R135). Two material rows left unsurfaced = orphan
  rows carrying a finding A4 should have raised.

All other ledger rows are either cited in A4 or fall under A4's blanket "reviewed, no finding," which the
protocol permits for non-material rows.

---

## AUDIT 2 — ARITHMETIC (recomputed from raw R-rows)

Every derived metric in A4's tables recomputed from the anchored numbers. All YoY/QoQ, EBITDA, margins,
tax, PAT-bridge, balance-sheet multiples, CAGRs, and SA-vs-consol gaps tie out EXCEPT one cell.

Representative checks (all PASS unless noted):

| Metric | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| Clean EBITDA consol FY26 | 4,393 = 12.3% | 4,679-286=4,393; /35,639=12.33% | R165/R162/R161 | PASS |
| Consol below 13% floor | by 0.7pp | 13.0-12.3=0.7 | R166 | PASS |
| Clean EBITDA SA FY26 | 4,397 = 12.7% | 4,928-531=4,397; /34,552=12.72% | R153/R150/R149 | PASS |
| **SA clean vs 13% floor** | **"above floor by 0.3pp"** | **12.7% is BELOW 13% by 0.3pp** | R153/R150/R149/R154 | **FAIL** |
| Consol EBITDA YoY | +31.3% | 1,116/3,563=31.32% | R165 | PASS |
| Consol PAT YoY | +11.3% | 173/1,532=11.29% | R171 | PASS |
| SA-vs-consol swing | -415, -21.2% of SA PAT | 162-(-253)=415; 415/1,958=21.2% | R159/R171 | PASS |
| Subsidiary rev fall | ~72% | (3,872-1,087)/3,872=71.9% | R161/R149 | PASS |
| CWIP multiple | 10.68x | 3,258/305=10.68 | R191 | PASS |
| Inventories multiple | 2.38x | 15,350/6,456=2.378 | R199 | PASS |
| Paid-up capital rise | +15.7% | 51/324=15.74% | R173 | PASS |
| Other Equity premium | ~3,036 | 4,741-1,705=3,036 | R174/R171 | PASS |
| Net-cash (borrowings only) | ~1,575 | 6,572-(2,402+2,595)=1,575 | R202/R176/R181 | PASS |
| Rev CAGR FY22-26 | 13.4% | (3,592/2,178)^0.25-1=13.35% | R005/R006 | PASS |
| EBITDA CAGR | 21.0% | (468/218)^0.25-1=21.03% | R010/R011 | PASS |
| NPC EBITDA margin | 24.8% | 196.7/792.7=24.81% | R123/R120 | PASS |
| NPC rev INR | ~1,898.9 Cr | 792.7x23.955/100=1,898.9 | R120/R145 | PASS |

ARI-1 (FACTUAL, loop A4): review line 72. Standalone FY26 clean EBITDA margin is 12.7% against the 13%
Notion floor. A4's cell reads "above floor by 0.3pp (clean)". The correct direction is BELOW the floor by
0.3pp (13.0 - 12.7 = 0.3). The distance is right; the sign is inverted. The parallel consolidated cell
(line 73) is correct ("BELOW 13% floor by 0.7pp"). The error understates the adverse read: on a clean
basis standalone is ALSO below the floor, not above it. This is a wrong fact in a derived table, not
cosmetic.

Note: deck-stated YoY oddities (e.g. standalone Tax YoY 39.0% vs my 38.8%, consol D&A 74.4% vs my 74.2%)
are the deck's own rounding, faithfully copied by A4 with an R-anchor. Not A4 derivations; no FAIL.

---

## AUDIT 3 — ADVERSARIAL READ (three most positive A4 claims, same-text bear counter)

### Claim A (most positive): NPC is the entire re-rating case: 24.8% EBITDA, 29.5% ROCE, zero debt, USD 120M order book (Step 2.9, PLB line 404).
BEAR COUNTER (same deck): the deck's OWN Acquire-vs-Greenfield table, "Earnings Accretive" row, guides
"15-18% EBITDA Margin and 11-14% PAT margin" (R115/R116, slide 24, fulltext line 643). That is management's
own accretion expectation and it sits well BELOW NPC's CY2025 standalone 24.8% EBITDA / 18.1% PAT
(R124/R135). The 24.8% A4 leans on is a single trailing-year print; the deck's forward accretion figure is
15-18%. A4 never cites R115/R116.
SURVIVES: YES. Type MISSING. Must be grafted into A4 (tempers the re-rating case; internal to the deck).

### Claim B: The acquisition delivers an "immediate US$120 Mn order book" / "order book on day one" (Step 6, Step 7, PLB, R114/R119/R285).
BEAR COUNTER (same deck): the source qualifies the USD 120M as "(including executed to date)" (fulltext
line 730). Part of the USD 120M is already executed, so the true FORWARD backlog is smaller than the
"immediate / day one" framing implies. The qualifier was dropped from R144 and every restatement, so A4
inherited an overstated forward order book.
SURVIVES: YES. Type MISSING. Loop A2 to log the qualifier (MF11), then A4 to reflect "part already executed."

### Claim C: Consolidated EBITDA margin improved +290bps to 13.0%, on track to the 15% target (Step 2.2, Step 6).
BEAR COUNTER (same deck): A4 itself (Step 2.7) flags the consolidated Gross-Profit margin stepping
22.4% -> 38.0% on flat revenue as a likely materials-vs-opex reclassification, not a real pricing gain; the
13.0% headline also includes Other Income (MF04), so the clean figure is 12.3%, below the floor.
SURVIVES: NO (already incorporated). A4 flagged it (flags 1 and 6, Q9, Step 2.3/2.7). No graft needed.

Result: two of three counters survive and are NOT in A4; both must be incorporated before save.

---

## STYLE NOTES (logged, no loop)

- STY-1 (STYLE): page-4 headline "Revenue Rs3,592 Cr FY26" (R006) equals consolidated Total Income
  (35,925 Mn = 3,592.5 Cr), not Revenue-from-Operations (35,639 Mn = 3,564 Cr, which page 5 R026 states as
  "Rs3,564 Cr"). A ~0.8% deck-labeling quirk. A4 reproduced the deck figure faithfully and the gap does not
  change any conclusion or the verdict, so this is logged, not looped. If A4 re-runs for the findings above,
  a one-line note that the page-4 "Revenue" is on a Total-Income basis would tighten provenance.

---

## VERDICT

**INCOMPLETE.** Three findings loop (1 FACTUAL, 2 MISSING); one STYLE logged.

- ARI-1 (FACTUAL -> A4): review line 72, standalone clean margin "above floor by 0.3pp" must read "below
  floor by 0.3pp" (12.7% vs 13%).
- COV-1 / Counter B (MISSING -> A2): "(including executed to date)" qualifier on the NPC USD 120M order
  book (fulltext line 730) is absent from structured (R144) and from the ledger; add as MF11, then A4
  reflects the smaller forward backlog.
- COV-2 / Counter A (MISSING -> A4; A3 missed): Acquire-route 15-18% EBITDA / 11-14% PAT accretion guidance
  (R115/R116) is unsurfaced and contradicts A4's NPC 24.8%/18.1% re-rating claim; graft the surviving bear
  counter.

Loop entry point: A2 (most upstream: add MF11), cascading A2 -> A3 (surface the R115/R116 internal
contradiction) -> A4 (fix line-72 sign, graft both surviving counters). Only after these does the review
proceed to Notion save.

```yaml
stage: A5-adversary
company: "MANINDS"
quarter: "2026-09"
model: claude-opus-4-8
status: complete
verdict: INCOMPLETE
plain_language_brief:
  narrative: present
  sector: present
  business_model: present
  competition: present
coverage:
  orphan_rows: ["R115", "R116"]
  missing_from_ledger: ["NPC USD120M order book qualifier '(including executed to date)', fulltext p26 line 730 — propose MF11"]
arithmetic_mismatches:
  - {metric: "Standalone FY26 clean EBITDA margin vs 13% floor", a4_value: "above floor by 0.3pp", recomputed: "below floor by 0.3pp (12.7% vs 13%)", source_line: "review L72; R153/R150/R149/R154"}
surviving_bear_counters:
  - {claim: "NPC re-rating case at 24.8% EBITDA / 18.1% PAT (Step 2.9, PLB)", counter: "deck's own Acquire-route accretion guidance is 15-18% EBITDA and 11-14% PAT (R115/R116, slide 24), materially below the trailing print A4 uses", source_line: "R115/R116; fulltext L643", type: MISSING}
  - {claim: "immediate US$120M order book / order book on day one (R114/R119/R285)", counter: "source qualifies USD120M as '(including executed to date)'; forward backlog is smaller than the 'immediate' framing (qualifier dropped from R144 and ledger)", source_line: "fulltext L730", type: MISSING}
findings_by_type:
  factual:
    - {id: ARI-1, desc: "review L72 standalone clean margin labelled 'above floor by 0.3pp'; 12.7% is BELOW the 13% floor by 0.3pp (sign inverted)", loop_back_to: A4}
  missing:
    - {id: COV-1, desc: "'(including executed to date)' qualifier on NPC USD120M order book absent from structured (R144) and ledger; add MF11", loop_back_to: A2}
    - {id: COV-2, desc: "Acquire-route 15-18% EBITDA / 11-14% PAT (R115/R116) unsurfaced in A4; surviving bear counter undercuts NPC re-rating claim", loop_back_to: A4}
  contradiction: []
  style:
    - {id: STY-1, desc: "page-4 'Revenue Rs3,592 Cr' (R006) is Total Income basis, not Revenue-from-Ops (Rs3,564 Cr, R026); deck-labeling quirk, ~0.8%, no conclusion change"}
loop_back_to: "A2"
gap: "A2: add MF11 for dropped NPC order-book qualifier '(including executed to date)' (fulltext L730). Then A3 surface R115/R116 internal margin contradiction, and A4 (1) fix review L72 'above floor'->'below floor by 0.3pp' and (2) graft two surviving bear counters (15-18%/11-14% accretion guidance; executed-to-date on the USD120M order book)."
style_notes:
  - "STY-1: page-4 'Revenue Rs3,592 Cr' is Total-Income basis vs Revenue-from-Ops Rs3,564 Cr; logged, no loop."
analyst_note: "Counts and ID accountability are clean (37 slides, 335 rows, 223/49/20/43). The gate fails on substance, not tally. One arithmetic sign error (L72: standalone clean 12.7% is below, not above, the 13% floor). Two material MISSING items, both bearish and both surviving same-text counters: (1) the NPC USD120M order book carries '(including executed to date)' in the source (L730), dropped from R144 and the ledger, so the 'immediate order book' is partly already executed; (2) the deck's own accretion guidance is 15-18% EBITDA / 11-14% PAT (R115/R116), which A4 never cites and which undercuts its reliance on NPC's 24.8% CY2025 print. Loop A2 first (add MF11), cascade to A3 then A4. All three findings push the read MORE cautious, consistent with A4's PROCEED WITH FLAGS but requiring the flags be tightened before Notion save."
```
