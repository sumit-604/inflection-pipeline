# A5 ADVERSARY / COMPLETENESS AUDIT — MAN INDUSTRIES (MANINDS), 2026-09

Doctype: Corporate Presentation (Reg 30, 01 Sep 2026). Inputs read: A1 fulltext,
A1 structured extraction, A2 ledger, A4 review. Source PDF and inputs/ NOT opened.
All recomputation from A1 raw extracted numbers. INR Mn unless stated.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate)

The PLAIN-LANGUAGE BRIEF is present at review L500-554. All four labelled parts
present and carry real content:

| Part | Location | Present? | Content check |
|---|---|---|---|
| 1. Summary narrative | L502-518 (17 lines) | present | Two-picture standalone-vs-consolidated story, tripwires, dilution, net-debt, price. Non-placeholder. |
| 2. SECTOR intelligence | L520-529 | present | Line-pipe demand cycle, Gulf/Aramco capex, steel-coil input, tender lumpiness. |
| 3. BUSINESS-MODEL intelligence | L531-542 | present | Converter + value-add spread, WC days, ladder-climb thesis, undisclosed metrics. |
| 4. COMPETITION intelligence | L544-554 | present | Welspun/Jindal/Ratnamani peers, inherited Aramco moat, NPC margin-durability risk. |

GATE: PASS. All four present and non-empty.

---

## AUDIT 1 — COVERAGE (independent re-enumeration)

Fresh pass over A1 fulltext page-marker spine ([page 1]..[page 37]) and the four
structured category tables, diffed against the A2 ledger and A1 `## COUNTS`.

| Category | A2 count | My fresh count | Orphan rows | Missing from ledger | Status |
|---|---|---|---|---|---|
| Slides (physical pages) | 37 | 37 ([page 1]..[page 37] all present) | 0 | 0 | PASS |
| NUMBER rows | 223 | 223 (ledger rows #1-223 = structured #COUNTS = 223) | 0 | 0 | PASS |
| ENTITY rows | 49 (40+9 summary) | 49 | 0 | 0 | PASS |
| FORWARD rows | 20 | 20 | 0 | 0 | PASS |
| DATE rows | 43 | 43 | 0 | 0 | PASS |
| ZERO_STANDING | 2 (#194 Intangibles FY24; #206 Current Tax Assets) | 2 | 0 | 0 | PASS |
| Footnotes | 4 (1 resolved, 2 EBITDA* unresolved, 1 disclaimer) | 4 | 0 | 0 | PASS |
| **Total disclosure units** | **335** | **335** | **0** | **0** | **PASS** |

Ledger-row-to-review reconciliation: A4's LEDGER-RECONCILIATION PREAMBLE (L11-22)
states all 37 slides / 335 rows reviewed, A2 GATE pass, A3 GATE pass, and lists A3
findings A1-A9 incorporated. Spot-audit of material rows:
- P&L rows #149-172 (standalone + consolidated FY26/FY25) → all in review Steps 1.1/1.2.
- Balance-sheet rows #173-208 (page 30) → all in Step 5 table.
- Historical rows #209-215 (page 31) → Step 2 F-GP flag + Step 4 bridge.
- Quarterly rows #216-220 (page 32) → Step 3 table; per-quarter GP #217 correctly
  treated ND (mapping unresolvable), matching A1's own note.
- Forward rows F1-F20 → Section B claims inventory C1-C11 + monitorables + guidance table.
- Footnotes FN2/FN3 EBITDA* (A2 FOOTNOTE_UNRESOLVED) → review resolves them via the
  page-28/29/31 in-table asterisk text "EBITDA is inclusive of Other Income" (fulltext
  L775, L812, L890); the A2 "unresolved" flag is over-cautious, A4 correctly closed it.
- Non-material spec/roster/glossary/timeline rows (pipe dimensions, EPC roster, awards)
  → covered by the blanket "reviewed, no finding" provision; correctly not individually
  cited (immaterial for a results review). No material orphan.

COVERAGE: PASS. No orphan rows; no rows my fresh pass found that the ledger lacks.

---

## AUDIT 2 — ARITHMETIC (every derived metric recomputed from A1 raw numbers)

### Derived metrics (review 1.3), Operating EBITDA ex-OI = PBT+D+Fin−OI
| Metric | A4 value | Recomputed | Source line (fulltext) | Status |
|---|---|---|---|---|
| Op EBITDA ex-OI Std FY25 | 2,767 | 1,854+433+1,022−542 = 2,767 | L765/761/763/751 | OK |
| Op EBITDA ex-OI Std FY26 | 4,397 | 2,630+756+1,542−531 = 4,397 | L765/761/763/751 | OK |
| Op EBITDA ex-OI Cons FY25 | 3,364 | 2,084+453+1,027−200 = 3,364 | L802/798/800/788 | OK |
| Op EBITDA ex-OI Cons FY26 | 4,393 | 2,370+789+1,520−286 = 4,393 | L802/798/800/788 | OK |
| Op EBITDA margin Std FY25 | 8.9% | 2,767/31,182 = 8.87% | L749 | OK |
| Op EBITDA margin Std FY26 | 12.7% | 4,397/34,552 = 12.72% | L749 | OK |
| Op EBITDA margin Cons FY25 | 9.6% | 3,364/35,054 = 9.60% | L786 | OK |
| Op EBITDA margin Cons FY26 | 12.3% | 4,393/35,639 = 12.32% | L786 | OK |
| Core PBT ex-OI Std FY26 | 2,099 | 2,630−531 = 2,099 | L765/751 | OK |
| Core PBT ex-OI Cons FY26 | 2,084 | 2,370−286 = 2,084 | L802/788 | OK |
| OI/PBT Cons FY26 | 12.1% | 286/2,370 = 12.07% | L788/802 | OK |
| ETR Std FY26 | 25.6% | 672/2,630 = 25.55% | L767/765 | OK |
| ETR Cons FY26 | 28.1% | 665/2,370 = 28.06% | L804/802 | OK |
| ETR Cons FY25 | 26.5% | 552/2,084 = 26.49% | L804/802 | OK |
| PAT margin Cons FY26 | 4.7% | 1,705/35,639 = 4.78% | L806/786 | OK |

### YoY (review Step 2)
| Metric | A4 value | Recomputed | Status |
|---|---|---|---|
| Op EBITDA ex-OI Std YoY | +58.9% | 4,397/2,767−1 = +58.9% | OK |
| Op EBITDA ex-OI Cons YoY | +30.6% | 4,393/3,364−1 = +30.6% | OK |
| Core PBT ex-OI Std YoY | +60.0% | 2,099/1,312−1 = +59.98% | OK |
| Core PBT ex-OI Cons YoY | +10.6% | 2,084/1,884−1 = +10.62% | OK |
| Cons revenue YoY | +1.7% | 35,639/35,054−1 = +1.67% | OK |
| Cons D&A YoY | +74.4% | 789/453−1 = +74.2% | OK (rounding) |
| Cons finance YoY | +48.1% | 1,520/1,027−1 = +48.0% | OK (rounding) |
| Sub revenue net add | +1,087 | 35,639−34,552 = 1,087 | OK |
| S-vs-C PAT gap FY25 | +11.8% | (1,532−1,370)/1,370 = +11.8% | OK |
| S-vs-C PAT gap FY26 | −12.9% | (1,705−1,958)/1,958 = −12.9% | OK |
| Std PAT YoY | +42.8% | 588/1,370 = +42.9% | OK — A4 carried deck-filed 42.8% (L769); my +42.9% is 0.1pp = within rounding |

### F-GP flag (review L153-157)
| Item | A4 value | Recomputed | Status |
|---|---|---|---|
| Cons GP FY25→FY26 | 7,905→13,639, +72.5% | 13,639/7,905−1 = +72.54% | OK |
| GP margin move | 22.4%→38.0%, +1,560bp | 7,905/35,253=22.4%; 13,639/35,925=38.0% | OK |
| EBITDA margin move | 10.1%→13.0%, +290bp | as filed L796 | OK |
| Below-gross cost added | ~1,270bp | 1,560−290 = 1,270 | OK |

### QoQ (review Step 3) — all five quarters' margins tie to values
Q1FY26 806/7,736=10.4%, 276/7,736=3.6%; Q2 1,018/8,148=12.5%, 370/8,148=4.5%;
Q3 1,376/8,386=16.4%, 550/8,386=6.6%; Q4 1,480/11,655=12.7%, 509/11,655=4.4%;
Q1FY27 1,553/10,650=14.6%, 614/10,650=5.8%. All OK — mapping confirmed by margin tie-out.
Q1FY27 annualised PAT 614×4 = 2,456 > FY26 1,705. OK.

### PAT bridge (review Step 4)
+173 (1,705−1,532); EBITDA +1,116; D&A −336; finance −493; OI +86; PBT +286;
tax −113; all recompute exactly. OK.

### Balance sheet / net-debt (review Step 5)
| Item | A4 value | Recomputed | Status |
|---|---|---|---|
| Capital WIP multiple | 10.7x | 3,258/305 = 10.68x | OK |
| RoU multiple | 8.5x | 1,389/163 = 8.52x | OK |
| Inventory days (opex) | ~179 | 15,350/31,246×365 = 179.3 | OK |
| Recv days (rev) | ~103 | 10,098/35,639×365 = 103.4 | OK |
| Payable days (opex) | ~172 | 14,712/31,246×365 = 171.9 | OK |
| Non-current recv | +145% / 2.5x | 2,385/973 = 2.45x | OK |
| Other fin liab jump | +1,826% | 5,797/301−1 = +1,826% | OK |
| Lease liab cur+ncur | +532% | (674+610)/(47+156)−1 = +532% | OK |
| Net-debt narrow | −999 (≈net cash) | (2,402+2,595+1,284)−(6,572+708) = −999 | OK |
| Net-debt conservative | +4,798 ≈ Rs 480 Cr | 12,078−7,280 = 4,798; /10 = 480 Cr | OK |
| CCC FY26 / FY25 | 110 / 101 days | 179+103−172=110; 146+93−138=101 | OK |

### Dilution / raise (review 0C) and Rs-Cr conversions (review 0B/6A)
Equity capital 375/324 = +15.7% OK. Other-equity add 4,741; less PAT 1,705 = 3,036
securities premium ≈ Rs 304 Cr OK. Cons rev Rs 3,564 Cr (35,639/10) OK; EBITDA Rs 468 Cr
(4,679/10) OK; PAT Rs 171 Cr (1,705/10) OK; slide-4 ₹3,592 Cr = Total Income 35,925/10 —
A4 correctly separated headline Total Income from Revenue-from-Ops 35,639. OK.

ARITHMETIC: PASS. Zero mismatches above rounding. The single 0.1pp item (Std PAT YoY
42.8% vs recomputed 42.9%) is the deck's own filed figure carried verbatim; within tolerance.

---

## AUDIT 3 — ADVERSARIAL READ (strongest same-text bear counter to A4's 3 most positive claims)

### Positive claim 1 (MOST positive operational): standalone turnaround is real
A4 L128, L142-143, L433: standalone core PBT ex-OI +60.0% is "genuine operating
improvement," "the single cleanest signal in the deck."
**Bear counter (same text):** A4 raised flag F-GP because consolidated gross margin
leapt 22.4%→38.0% (+1,560bp) while EBITDA margin rose only +290bp, i.e. ~1,270bp of
cost was reclassified or the GP definition shifted — "unexplained" (L157). The standalone
+60% rides the identical unexplained margin behaviour: standalone opex grew only +6.1%
against revenue +10.8% (L749/755), yet the deck discloses NO volume, realisation, or
steel-price split, and the archetype is a commodity/spread converter for which a falling
HR-coil price (A4's own sector brief, L526) lifts spread cyclically. The extract gives
no evidence the +60% is structural rather than a cyclical steel-spread / reclassification
gain. **SURVIVES.** A4 applied the F-GP/"unexplained" doubt to the consolidated line but
NOT to its "genuine operating improvement / real turnaround" verdict on standalone. This
caveat must be grafted onto claim 1 before save.

### Positive claim 2 (MOST positive strategic): NPC economics strong, re-rating ON TRACK
A4 L280, L293, 6D: NPC CY25 24.8% EBITDA / 29.5% ROCE / zero debt; growth trigger "ON TRACK."
**Bear counter (same text):** management's OWN build-vs-buy slide models the acquired
route at 15-18% EBITDA and 11-14% PAT (p24, ledger #115-116) — a ~700bp haircut to the
24.8% CY25 print; "zero debt at closing" (p25) is contradicted by USD 70 Mn debt raised
to fund the deal (p19/p30 #92/#185) that the group now carries; CY25 is one un-audited
pre-acquisition year; only 40 days in the group P&L. **Counter is substantially INCORPORATED**
(A4 tripwire #5 AMBER "unproven in group P&L" L280; A6 inconsistency L414/469; A8 soft
order book; net-debt Step 5; Q5/Q8). Residual defect: A4's 6D status word "ON TRACK"
(L293) contradicts its own AMBER tripwire — a labelling inconsistency, not a missing
counter. Note for A4 to align the 6D label to AMBER/UNPROVEN; does not independently fail.

### Positive claim 3 (MOST positive forward): the climb is funded and underway
A4 L540-541: "the climb is funded and underway (Jammu 58% spent, NPC closed)."
**Bear counter (same text):** 20-25% revenue CAGR is set against FY26 consolidated +1.7%,
and the 15% margin target sits above even the OI-lifted 13.0%; value-add plants produce
nothing until Mar 2027; Jammu still needs ~Rs 250 Cr of its ~Rs 600 Cr (p16 #79/#80);
"funded" enlarged the capital base faster than earnings (ROE fell to 9.2%, net-debt leans
~Rs 480 Cr, ~15.7% dilution). **Counter is INCORPORATED** (ambitious-guidance flag L377-379,
WEAKENED margin trigger L295, net-debt/dilution/ROE flags). Does not independently fail;
minor phrase-softening suggested only.

**Surviving, non-incorporated counter requiring graft:** claim 1 (standalone +60% turnaround
lacks the F-GP / cyclical-steel-spread caveat). Loop to A4.

---

## VERDICT

INCOMPLETE. loop_back_to = A4.

Gate 0 (deliverable brief) PASS, Audit 1 (coverage) PASS, Audit 2 (arithmetic) PASS.
Audit 3 found one surviving bear counter not incorporated: A4 calls the standalone core
PBT ex-OI +60% a "genuine operating improvement / real turnaround" (L128, L142-143, L433)
without carrying its own F-GP "unexplained gross-margin/reclassification" doubt (L157) or
the cyclical steel-spread possibility (its sector brief L526) onto that claim. The deck
discloses no volume/realisation/steel-price split, so the structural-vs-cyclical nature is
unresolvable from the extract; conservative bias requires the caveat. GAP: graft a
one-line caveat onto the Step 2 diagnostic-3 / Section C / business-brief "genuine
turnaround" characterisation — the standalone +60% may be a cyclical spread or
gross-margin-definition artifact, not a proven structural climb; then re-emit. Secondary
alignment (not a separate fail): reconcile the 6D NPC status word "ON TRACK" (L293) to the
AMBER/UNPROVEN reading A4's own tripwire #5 (L280) already carries.

---

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
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches: []
surviving_bear_counters:
  - claim: "Standalone core PBT ex-OI +60% is a 'genuine operating improvement / real turnaround' (review L128, L142-143, L433)"
    counter: "Rides the same unexplained gross-margin move A4 flagged as F-GP (cons GP margin 22.4->38.0%, +1,560bp, only +290bp to EBITDA, ~1,270bp cost reclassified/unexplained, review L157); standalone opex +6.1% vs revenue +10.8% with NO volume/realisation/steel-price split disclosed; commodity-converter archetype means a falling HR-coil price lifts spread cyclically (A4 sector brief L526). Extract cannot prove the +60% is structural vs cyclical/reclassification. Caveat absent from A4's positive characterisation."
    source_line: "review L128/L142-143/L157/L433/L526; fulltext L749/L755/L866-870"
loop_back_to: "A4"
gap: "Graft onto the standalone +60% core-PBT 'genuine turnaround' claim (Step 2 diagnostic 3 / Section C / business-model brief) a caveat that the gain may be a cyclical steel-spread or gross-margin-definition/reclassification artifact (per A4's own F-GP flag), not a proven structural climb, since the deck discloses no volume/realisation/steel-price split; then re-emit. Secondary: align the 6D NPC growth-trigger status word 'ON TRACK' (L293) to the AMBER/UNPROVEN reading A4's tripwire #5 (L280) already carries."
analyst_note: "Coverage and arithmetic are clean: 335/335 rows enumerate independently to A2, all P&L/BS/QoQ/bridge/net-debt derived metrics recompute within rounding, and the four-part plain-language brief is present and substantive. The only defect is one surviving bear counter. A4 is unusually and correctly bearish (two RED tripwires, F-GP, dilution, net-debt, INDETERMINATE cash) and its NPC and funded-and-underway positives already embed their bear side. But A4 asserts the standalone +60% core-PBT turnaround as 'genuine/real' while its own F-GP flag calls the parallel gross-margin leap unexplained; with no volume/realisation/steel-price split in a commodity-converter deck, that structural claim is unresolvable and needs the cyclicality/reclassification caveat before Notion save. Small graft, single loop to A4."
```
