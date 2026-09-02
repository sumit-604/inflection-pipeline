# A5 ADVERSARY / COMPLETENESS AUDIT — Man Industries (India) Ltd (MANINDS)
## Quarter 2026-09 | Corporate Presentation, 01 Sep 2026

Inputs read: A1 fulltext, A1 structured extraction, A2 ledger, A4 review.
Source PDF and `inputs/` NOT opened (A1 is sole source reader). Coverage
re-run greps the A1 fulltext spine. All cites re-derived; A4/A3 cites checked,
not deferred to.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate, run first)

A4 Step 10 PLAIN-LANGUAGE BRIEF, four labelled parts:

| Part | A4 location | Present | Content check |
|---|---|---|---|
| 1. Summary narrative (10-20 lines) | review L403-443 | PRESENT | ~28 real lines, numbers-anchored, non-placeholder |
| 2. SECTOR intelligence | review L445-467 | PRESENT | line-pipe demand, GCC/Aramco, converter spread, ND items named |
| 3. BUSINESS-MODEL intelligence | review L469-491 | PRESENT | buy-form-coat model, margin drift, cash/consolidation weak point |
| 4. COMPETITION intelligence | review L493-516 | PRESENT | Welspun/Jindal peer set, moat vs scale, backlog-quality risk |

GATE 0: PASS. All four present and non-empty.

---

## AUDIT 1 — COVERAGE (fresh grep pass over A1 fulltext, diff vs A2 ledger)

Fresh enumeration of the fulltext spine:
- Page markers `[page N]`: 1 through 37 all present (fulltext L18-1060). Fresh
  slide count = 37.
- A1 structured `## COUNTS` (structured L10-14): NUMBER 223, ENTITY 49,
  FORWARD 20, DATE 43, TOTAL 335.
- A2 count test (ledger L11-17): 37 / 223 / 49 / 20 / 43 / 2 zero_standing.

| Category | A2 count | My fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Slides (pages) | 37 | 37 (fulltext L18-1060, markers 1-37 contiguous) | none | MATCH |
| NUMBER | 223 | 223 (structured L19-241; financial spine pp.26/28-32 all present) | none material | MATCH |
| ENTITY | 49 (40+9) | 49 (structured L246-294) | none | MATCH |
| FORWARD | 20 | 20 (structured L299-318) | none | MATCH |
| DATE | 43 | 43 (structured L323-365) | none | MATCH |
| ZERO_STANDING | 2 | 2 (Intangibles FY24 L153; Current Tax Assets L165, both p30) | none | MATCH |

Material-row cite check (every load-bearing ledger row cited in A4 OR
reviewable as no-finding):
- Standalone P&L p28 L749-771 -> A4 table 2.1. Cited.
- Consolidated P&L p29 L786-808 -> A4 table 2.2. Cited.
- Slide-4 headline p4 L65-86 -> A4 table 2.3. Cited.
- Historical p31 L866-886 -> A4 table 2.4. Cited.
- Quarterly p32 L899-938 -> A4 table 2.5. Cited (GP series carried as unmapped,
  matching A1 note).
- Balance sheet p30 L823-852 -> A4 table 2.6. Cited (all lines incl. both
  ZERO_STANDING rows).
- NPC CY2025 p26 L711-736 -> A4 table 2.7. Cited.
- NPC acquisition terms p19/20/25/26 -> A4 table 2.8. Cited.
- FORWARD rows p5/16/17/24/25/32/34 -> A4 Step 7 register + Step 9
  monitorables. Cited.

Minor coverage observation (NOT an orphan FAIL): slide-4 headline CAGRs
(EBITDA CAGR 21.0% L30, PAT CAGR 13.8% structured L35) are not individually
cited in A4's tables; only Revenue CAGR 13.4% is used (A4 M7). These are
marketing-headline growth metrics and fall under "reviewed, no finding"
(A4 Step 1 asserts no unreviewed row). See Adversarial counter B for the one
substantive point they carry.

COVERAGE VERDICT: PASS. No orphan row (ledger->A4). No missing row
(fresh pass->ledger). Counts reconcile 37/223/49/20/43/2.

---

## AUDIT 2 — ARITHMETIC (recompute every derived metric from raw extract)

Raw numbers taken from A1 fulltext pp.26/28-32.

### Standalone P&L (A4 table 2.1), fulltext L749-771
| Metric | A4 value | Recomputed | Status |
|---|---|---|---|
| EBITDA check 4928-756-1542 = PBT | 2,630 | 2,630 | OK |
| PBT-Tax = PAT 2630-672 | 1,958 | 1,958 | OK |
| Revenue YoY (34552/31182-1) | +10.8% | +10.81% | OK |
| EBITDA YoY (4928/3309-1) | +48.9% | +48.93% | OK |
| EBITDA margin (4928/35083) | 14.0% | 14.05% | OK |
| PAT YoY (1958/1370-1) | +42.8% | +42.92% | OK (deck rounds to 42.8) |
| ETR (672/2630) | 25.6% | 25.55% | OK |

### Consolidated P&L (A4 table 2.2), fulltext L786-808
| Metric | A4 value | Recomputed | Status |
|---|---|---|---|
| EBITDA check 4679-789-1520 = PBT | 2,370 | 2,370 | OK |
| PBT-Tax = PAT 2370-665 | 1,705 | 1,705 | OK |
| Revenue YoY (35639/35054-1) | +1.7% | +1.67% | OK |
| EBITDA YoY (4679/3563-1) | +31.3% | +31.32% | OK |
| EBITDA margin (4679/35925) | 13.0% | 13.02% | OK |
| PAT YoY (1705/1532-1) | +11.3% | +11.29% | OK |
| ETR (665/2370) | 28.1% | 28.06% | OK |

### EBITDA ex-Other-Income (A4 Step 6, the margin-floor claim)
| Metric | A4 value | Recomputed | Status |
|---|---|---|---|
| Cons ex-OI (4679-286)/35639 | 12.3% | 12.33% | OK (below 13% floor confirmed) |
| SA ex-OI (4928-531)/34552 | 12.7% | 12.72% | OK |

### Standalone-vs-Consolidated gap (A4 Step 4), L769/L806
| Metric | A4 value | Recomputed | Status |
|---|---|---|---|
| FY25 gap (1532-1370)/1370 | +11.8% | +11.82% | OK |
| FY26 gap (1705-1958)/1958 | -12.9% | -12.92% | OK |
| Swing in gap ratio (11.8 + 12.9) | ~25 pts | 24.74 pts | OK |
| Absolute swing 162 -> -253 | ~415 Mn | 415 Mn | OK |

Wording note (not an arithmetic FAIL): A4 writes "~415 Mn, ~24-25 pts of
standalone PAT" (review L252). The 24-25 pts is the swing in the (Cons-SA)/SA
RATIO (24.7 pts), not 415 as a share of SA PAT (that would be 21.2% of FY26
or 30.3% of FY25). The numbers are individually correct; the phrase conflates
two bases. Cosmetic, below the FAIL bar.

### Quarterly QoQ / YoY (A4 table 2.5), L900-903/L917-927
| Metric | A4 value | Recomputed | Status |
|---|---|---|---|
| TI QoQ (10650/11655-1) | -8.6% | -8.62% | OK |
| EBITDA QoQ (1553/1480-1) | +4.9% | +4.93% | OK |
| PAT QoQ (614/509-1) | +20.6% | +20.63% | OK |
| TI YoY (10650/7736-1) | +37.7% | +37.67% | OK |
| EBITDA YoY (1553/806-1) | +92.7% | +92.68% | OK |
| PAT YoY (614/276-1) | +122.5% | +122.46% | OK |

### Net-cash vs net-debt (A4 Step 5), p30 balance sheet
| Metric | A4 value | Recomputed | Status |
|---|---|---|---|
| Named borrowings 2402+2595 | 4,997 | 4,997 | OK |
| Cash 6572 + Investments 708 | 7,280 | 7,280 | OK |
| Net cash on named debt | +2,283 | +2,283 | OK |
| Total debt if +USD70Mn acq | ~10,847 | 4,997+5,850 = 10,847 | OK |
| Net debt in that case | ~-3,567 | 7,280-10,847 = -3,567 | OK |

Reconciliation note: A4's total-debt add uses the USD 70 Mn acquisition-debt
estimate (~5,850 Mn at ~83.6 INR, review L302), NOT the book line "Other
financial liabilities" 5,797 (L847). Using the book 5,797 instead gives total
debt 10,794 and net debt -3,514. Both bases yield NET DEBT of the same order;
A4's own tilde figures are internally consistent on the 5,850 basis. The axis
is flagged INDETERMINATE regardless (the sign flips on classification, not on
this 53 Mn spread). No FAIL.

### NPC CY2025 margins (A4 table 2.7), p26 L711-732
| Metric | A4 value | Recomputed | Status |
|---|---|---|---|
| Gross margin 214.1/792.7 | 27.0% | 27.01% | OK |
| EBITDA margin 196.7/792.7 | 24.8% | 24.81% | OK |
| PAT margin 143.5/792.7 | 18.1% | 18.10% | OK |
| Tax rate 18.5/162.0 | 11.4% | 11.42% | OK |
| INR Revenue 792.7 x 23.955 | ~1,898.9 Cr | 1,898.8 Cr | OK |

### Slide-4 headline ties (A4 table 2.3)
| Metric | A4 value | Recomputed | Status |
|---|---|---|---|
| FY26 Rev 3,592 Cr = Total Income | 35,925 Mn | 35,925 x 0.1 = 3,592.5 | OK (ties TI, not Rev-from-Ops 35,639=3,564) |
| FY26 EBITDA 468 Cr | 4,679 Mn | 467.9 | OK |
| FY26 PAT 171 Cr | 1,705 Mn | 170.5 | OK |
| FY26 Networth 2,087 Cr | 20,865 Mn | 2,086.5 | OK |

### Historical gross-margin step (A4 table 2.4), p31
| Metric | A4 value | Recomputed | Status |
|---|---|---|---|
| FY26 GP margin 13639/35925 | 38.0% | 37.97% | OK |
| FY25 GP margin 7905/35253 | 22.4% | 22.42% | OK |

ARITHMETIC VERDICT: PASS. Every derived metric recomputes within rounding.
Two cosmetic wording items (gap-swing basis; 5,797 vs 5,850 debt add) noted,
neither above the FAIL bar. No mismatch to loop back to A4.

---

## AUDIT 3 — ADVERSARIAL READ (three most positive A4 claims, strongest
## same-text bear counter each)

### Claim A (most positive): NPC is a high-quality business, the constructive
offset to the thesis. "NPC CY2025: 24.8% EBITDA, 18.1% PAT, 29.5% ROCE, zero
debt at closing" (review L331, L436-438).

Same-text bear counter: The deck's OWN build-vs-buy slide underwrites NPC at
15-18% EBITDA and 11-14% PAT (fulltext L643, p24), well below the 24.8%/18.1%
CY2025 actuals (L714/L732, p26). Management's own model implies material
post-integration margin compression, or the CY2025 print is a peak. The USD
120 Mn order book "includes executed to date" (L729-730), so forward backlog
is smaller than the headline. NPC's USD 83 Mn cash / 158.6 Mn net worth is as
of Apr'2026 (L715-716); the buyer then loaded USD 70 Mn debt to fund the
purchase (L489), so "zero debt" is NPC-entity, not group.
SURVIVES: yes, fully supported by same text.
Incorporated in A4: yes — Q4 (15-18 vs 24.8, review L371), Q7 (order book
incl executed, L374), Step 6 tripwire "order-book definition soft" (L331).
No new graft required.

### Claim B (most positive): "Robust Growth Trajectory" — standalone PAT
+42.8%, EBITDA margin +360bps to 14.0%; headline EBITDA CAGR 21.0%
(review L410, fulltext L70).

Same-text bear counter: (i) 14.0% and the EBITDA growth include Other Income
by definition (L775); ex-OI standalone margin is 12.7%. (ii) Standalone is the
flattering lens — consolidated PAT grew only 11.3% and sits BELOW standalone
for the first time (1,705 < 1,958). (iii) Over FY22-26 the headline EBITDA CAGR
is 21.0% (L30) but PAT CAGR is only 13.8% (structured L35), barely above
Revenue CAGR 13.4% — the EBITDA-level margin expansion is NOT reaching the
bottom line; rising depreciation (+74.6% YoY) and finance cost (+50.9% YoY)
absorb it (L761/L763).
SURVIVES: yes.
Incorporated in A4: (i) and (ii) yes — central thesis, Step 4/Step 6, flags.
(iii) the EBITDA-CAGR-vs-PAT-CAGR divergence over 5 years is only PARTIALLY
present (A4 shows the one-year dep/interest drag in the PAT bridge, review
L219-221, but not the multi-year CAGR gap). This is a soft, derivative add
that the PAT-bridge narrative already implies. Not a required graft; logged so
A4 may optionally note the 5-year EBITDA-CAGR (21%) vs PAT-CAGR (13.8%) gap.

### Claim C (most positive): Acquisition value creation — "Immediate EBITDA
Accretion," Vision 2030 play, Aramco moat, immediate order book (fulltext
L455-457, p18; review sector/competition sections).

Same-text bear counter: FY26 consolidated results PREDATE NPC (completed
21 May 2026, in Q1FY27, L938), so ZERO of the claimed accretion is in reported
FY26 numbers; the only visible group effect to date is the subsidiary DRAG
(-253 Mn, Step 4). "Immediate EBITDA accretion" (p18) is an unproven forward
claim. The deal is funded by USD 70 Mn debt (possibly in current liabilities,
L847) plus an undisclosed ~Rs 300 Cr equity raise (capital +15.7%, EPS omitted,
review Q2). Aramco tenure is stated three inconsistent ways: "40+ Years"
(L579), "since 2005 / ~20 yrs" (L639), "2+ Decades" (L531).
SURVIVES: yes.
Incorporated in A4: yes — Q2 (dilution, L369), Q3 (Aramco tenure, L370),
Q9 (NPC guidance, L376), Step 4 (drag, NPC not the FY26 cause). No new graft.

ADVERSARIAL VERDICT: All three strongest bear counters survive and are already
incorporated in A4's flags/questions/tripwire table. No UNINCORPORATED
surviving counter forces a loop-back. One optional refinement (Counter B(iii),
5-yr EBITDA-CAGR vs PAT-CAGR gap) logged for A4's discretion, not a gate
failure.

---

## VERDICT

COMPLETE.

- Gate 0 deliverable: PASS (all four brief parts present).
- Coverage: PASS (37/223/49/20/43/2 reconcile; no orphan, no missing row).
- Arithmetic: PASS (all derived metrics within rounding; two cosmetic wording
  items below the FAIL bar).
- Adversarial: PASS (three strongest same-text bear counters survive, all
  already incorporated in A4).

No loop-back. Proceeds to Notion save.

```yaml
stage: A5-adversary
company: "MANINDS"
quarter: "2026-09"
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
analyst_note: >-
  All four audits pass; verdict COMPLETE. Counts reconcile 37/223/49/20/43/2
  against a fresh fulltext-spine pass. Every A4 derived metric recomputes
  within rounding. Two cosmetic items, below the FAIL bar, not looped back:
  (1) A4's "~24-25 pts of standalone PAT" is the swing in the (Cons-SA)/SA
  ratio (24.7 pts), not 415 Mn as a share of SA PAT; numbers correct, phrase
  mixes bases. (2) A4's net-debt add uses the USD70Mn estimate 5,850 not the
  book line 5,797 (Other financial liabilities); both give net debt of the
  same order and the axis is INDETERMINATE regardless. Three strongest
  same-text bear counters (NPC 15-18% own-model vs 24.8% actual; standalone
  lens masking consolidated drag; NPC accretion predates FY26) all survive
  and are already grafted into A4 flags/Q2-Q9/Step4-6, so no loop-back.
  One optional refinement logged: the 5-yr EBITDA CAGR 21.0% vs PAT CAGR
  13.8% gap (headline slide 4) is only partially surfaced; A4 may add it.
```
