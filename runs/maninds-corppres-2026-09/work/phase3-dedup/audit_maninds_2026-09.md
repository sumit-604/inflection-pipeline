# MANINDS Corporate Presentation (01 Sep 2026) — A5 ADVERSARY / COMPLETENESS AUDIT

Agent: A5 ADVERSARY | Model: claude-opus-4-8 | Quarter: 2026-09
Inputs read: A1 fulltext, A1 structured (R001-R335), A2 ledger, A4 review. No source PDF, no inputs/.
Coverage re-run greps the A1 FULLTEXT spine. All numbers re-derived independently.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate, run first)

PLAIN-LANGUAGE BRIEF present at review line 409. All four labelled parts present and non-empty:

| Part | Review line | Content check | Status |
|---|---|---|---|
| 1. SUMMARY NARRATIVE | 411 | ~26 lines; standalone vs consol, ex-OI margin, WC, NPC price, decision status | PRESENT |
| 2. SECTOR INTELLIGENCE | 440 | project-driven demand, GCC/Aramco tailwind, tax backdrop, India cycle ND | PRESENT |
| 3. BUSINESS-MODEL INTELLIGENCE | 460 | converter model, unit economics, mix-upgrade thesis, quality drift | PRESENT |
| 4. COMPETITION INTELLIGENCE | 481 | peer set, approval moat, scale/pricing gaps, concentration | PRESENT |

Gate 0: PASS.

---

## AUDIT 1 — COVERAGE (fresh grep pass over the fulltext spine, diffed vs A2 ledger)

Fresh enumeration from fulltext (page markers [page 1]-[page 37]):

| Category | A2 count | My fresh count | Basis | Orphan rows | Status |
|---|---|---|---|---|---|
| Slides (physical pages) | 37 | 37 | formfeed/page markers 1-37 in fulltext | none | MATCH |
| Data-bearing pages | 34 | 34 | dividers confirmed pages 3/27/33 (lines 56/740/943) | none | MATCH |
| Section dividers (no data) | 3 | 3 | "Business Overview"/"Financial Overview"/"Next 5 years Goal" | none | MATCH |
| NUMBER | 223 | 223 | structured R001-R223 contiguous; ID range verified | none | MATCH |
| ENTITY (incl. 9 summary) | 49 | 49 | R224-R272 contiguous | none | MATCH |
| FORWARD | 20 | 20 | R273-R292 contiguous | none | MATCH |
| DATE | 43 | 43 | R293-R335 contiguous | none | MATCH |
| Footnotes | 5 rows / 4 units | 5 / 4 | R004,R021,R153,R165,R269 | none | MATCH |
| Zero-standing | 2 | 2 | R194 (intangibles FY24 nil), R206 (current tax assets nil) | none | MATCH |

ID accountability: R001-R335 contiguous, no gaps. Structured COUNTS header (223+49+20+43=335) ties to A2 ledger and to A4 STEP 1 (all 335 reviewed). No orphan IDs in the ledger; no fresh-pass unit missing from the structured file.

Every ledger row is cited in A4 or reviewed. A4 STEP 1 confirms all 335 reviewed; A3 findings A3-01..A3-06 and checklist F2/F6/F10/F14/F15/F16 incorporated; no orphan.

Footnote-resolution note (not a failure): A2 flagged R153/R165 EBITDA* as FOOTNOTE_UNRESOLVED because the asterisk definition was absent from A1's STRUCTURED file. The definition IS present in the fulltext spine (lines 775 and 812: "EBITDA is inclusive of Other Income, since it's operational in nature"). A4 correctly resolved it from the fulltext and made it the load-bearing ex-OI flag. Chain closed. No coverage FAIL.

Coverage verdict: PASS. No orphan rows, none missing from ledger.

---

## AUDIT 2 — ARITHMETIC (every derived metric recomputed from raw fulltext numbers)

Standalone P&L (fulltext lines 749-771), consolidated (786-808), balance sheet (823-852), NPC (711-736):

| Metric | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| Std EBITDA FY26 (TotInc-Opex) | 4,928 | 35,083-30,155=4,928 | 753/755 | OK |
| Std EBITDA YoY | 48.9% | 1,619/3,309=48.9% | 757 | OK |
| Std PBT FY26 | 2,630 | 4,928-756-1,542=2,630 | 761/763/765 | OK |
| Std PAT YoY | 42.8% | 588/1,370=42.9% | 769 | OK |
| Consol EBITDA FY26 | 4,679 | 35,925-31,246=4,679 | 790/792 | OK |
| Consol PBT FY26 | 2,370 | 4,679-789-1,520=2,370 | 794/798/800 | OK |
| Consol PAT YoY | 11.3% | 173/1,532=11.3% | 806 | OK |
| Std ex-OI EBITDA margin FY26 | 12.7% | (4,928-531)/34,552=12.72% | 749/751/757 | OK |
| Std ex-OI margin FY25 | 8.9% | (3,309-542)/31,182=8.87% | 749/751/757 | OK |
| **Consol ex-OI margin FY26** | **12.3%** | (4,679-286)/35,639=12.33% | 786/788/794 | OK (below 13% floor confirmed) |
| Consol ex-OI margin FY25 | 9.6% | (3,563-200)/35,054=9.59% | 786/788/794 | OK |
| GP margin jump FY25->FY26 | 22.4%->38.0% | 7,905/35,253=22.4%; 13,639/35,925=38.0% | 866-870 | OK |
| GP delta vs EBITDA delta | +5,734 vs +1,116 | 13,639-7,905=5,734; 4,679-3,563=1,116 | 866/879 | OK |
| Std PAT bridge (EBITDA+1,619; D&A-323; Fin-520; Tax-188) | +588 | 1,619-323-520-188=588 | 757/761/763/767 | OK |
| Consol PAT bridge (EBITDA+1,116; D&A-336; Fin-493; Tax-113) | +173 | 1,116-336-493-113=174 (rounding, deck PAT delta=173) | 794/798/800/804 | OK (rounding) |
| EBITDA growth consumed by D&A+Fin (consol) | 74% | (336+493)/1,116=74.3% | 794/798/800 | OK |
| S-vs-C gap FY25 | +162 (+11.8%) | 1,532-1,370=162; 162/1,370=11.8% | 769/806 | OK |
| S-vs-C gap FY26 | -253 (-12.9%) | 1,705-1,958=-253; 253/1,958=12.9% | 769/806 | OK |
| S-vs-C swing | -415 (-21.2% std PAT) | 162-(-253)=415; 415/1,958=21.2% | derived | OK |
| Implied non-std revenue FY25/FY26 | 3,872 / 1,087 | 35,054-31,182=3,872; 35,639-34,552=1,087 | 749/786 | OK |
| Non-std revenue drop | -2,785 (-72%) | 3,872-1,087=2,785; 2,785/3,872=71.9% | derived | OK |
| Net cash ex-lease (consol FY26) | +2,283 | (6,572+708)-(2,402+2,595)=2,283 | 831/841/843 | OK |
| Net cash incl leases | +999 | 2,283-(610+674)=999 | 832/842 | OK |
| Inventory 2yr / FY26 | +138% / +21% | 15,350/6,456=2.38; 15,350/12,685=1.21 | 840 | OK |
| Trade recv (cur) 2yr / FY26 | +184% / +13% | 10,098/3,551=2.84; 10,098/8,959=1.13 | 842 | OK |
| Trade payables 2yr / FY26 | +193% / +23% | 14,712/5,028=2.93; 14,712/12,002=1.23 | 843 | OK |
| Paid-up capital rise | +15.7% | 375/324=1.157 | 823 | OK |
| Other equity rise FY26 | +4,741 | 20,490-15,749=4,741 | 825 | OK |
| NPC EBITDA margin CY2025 | 24.8% | 196.7/792.7=24.8% | 711/714 | OK |
| NPC PAT margin | 18.1% | 143.5/792.7=18.1% | 711/730 | OK |
| NPC tax+zakat rate | 11.4% | 18.5/162.0=11.4% | 723/727 | OK |
| NPC purchase multiple | ~2.7x | 102/38.3=2.66x | 730 (USD PAT), 19-tx | OK |
| NPC enterprise outlay net of cash | ~19 vs EBITDA 52.5 | 102-83=19; EBITDA 52.5 | 714/715 | OK |

Growth-trajectory CAGRs (slide 4) are deck-stated, not A4-derived: Revenue 13.4% (I get 13.3%), EBITDA 21.0%, PAT 13.8% — all within rounding of the deck labels. Margins on P&L are computed on total-income basis (deck convention), reproduced faithfully.

Arithmetic verdict: PASS. No mismatch above rounding.

---

## AUDIT 3 — ADVERSARIAL READ (three most positive A4 claims, strongest same-text bear counter each)

### Claim A (positive): "NPC looks bought cheap — ~2.7x CY2025 PAT with USD 83M cash on its books; EBITDA 24.8%, ROCE 29.5%." (review 2.7 / summary / Q8)
Bear counter (same text): the 2.7x rests on a SINGLE CY2025 snapshot the deck cannot confirm is representative; only one year is shown (fulltext 706-732). Peak-year earnings make any multiple look cheap. Durability rests on an Aramco relationship the deck dates inconsistently (see Claim B).
Survives: YES. Already incorporated by A4 (2.7 "whether CY2025 is a peak/representative year is not answerable"; Q8; flag list). No graft needed.

### Claim B (positive): "USD 120M order book on day one + Aramco AVL status skips 1-2 years of greenfield audits." (review SECTOR line 448; tripwire table line 314 "CONSTRUCTIVE"; table 2.7 "Order book at acquisition USD 120M")
Bear counter (same text): the fulltext at line 729 states the USD 120M order position is "(including executed to date)" — part is ALREADY delivered, so the true forward book is smaller than USD 120M. Against NPC's own CY2025 revenue of USD 211.4M (R120/line 711), USD 120M is ~57% of one year, under 7 months of backlog for a lumpy order-book converter. "L1 status" (line 641/696) is not firm orders. A4 dropped the "including executed to date" qualifier from table 2.7 (R144) and presents USD 120M as unqualified day-one strength; A4's only order-book caveat (competition section, line 498) is about price competition, not book SIZE or the executed-to-date deflator.
Survives: YES, and NOT incorporated. This is a load-bearing, same-text deflator on the deck's headline acquisition positive. GRAFT REQUIRED -> A4.

### Claim C (positive): "NPC lifts the group's average — NPC EBITDA 24.8% and ROCE 29.5%, far above the India base; the mix upgrade drives re-rating." (review BUSINESS-MODEL lines 471-473)
Bear counter (same text): NPC's 430,000 MT capacity (line 105) is ~26% of the ~1.63M MT combined base; a 24.8% slice blended against a sub-13% India base lifts the group average only modestly, and NPC consolidates just from Q2FY27 while the PRE-NPC subsidiaries already turned dilutive (S-vs-C swing -415M, Step 4). The 24.8% is one CY2025 year.
Survives: YES. Substance incorporated by A4 (Step 4 dilutive subs; 2.7/Q8 one-year; business-model "converter-level margin, not franchise"). Capacity-weighting point is an enhancement, not a missing counter. No graft required.

Adversarial verdict: one surviving bear counter (Claim B, the order-book deflator) is NOT incorporated in A4 and must be grafted before save.

---

## VERDICT

INCOMPLETE. loop_back_to = A4.

Gap: A4's NPC framing omits a same-text bear deflator on its headline positive. Graft into the SECTOR/COMPETITION brief and table 2.7: the USD 120M order book is stated "including executed to date" (fulltext line 729), so the forward book is below USD 120M, and even at face it is ~57% of NPC's own CY2025 revenue (USD 211.4M) — under 7 months of backlog for a lumpy order-book converter; "L1 status" is not firm orders. Restore the "(including executed to date)" qualifier dropped from R144 in table 2.7.

Coverage PASS, Arithmetic PASS, Deliverable gate PASS. The only blocker is the un-incorporated surviving bear counter, per the A5 rule that a surviving same-text counter must be added before save.

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
  - claim: "USD 120M NPC order book on day one + Aramco AVL skips 1-2yr greenfield audits (SECTOR line 448; tripwire CONSTRUCTIVE line 314; table 2.7)"
    counter: "Order position is stated 'including executed to date' (line 729), so forward book is below USD 120M; even at face it is ~57% of NPC CY2025 revenue USD 211.4M (~7 months backlog) for a lumpy order-book converter; 'L1 status' (line 641/696) is not firm orders. A4 dropped the executed-to-date qualifier from R144 and frames USD 120M as unqualified strength."
    source_line: "729 (fulltext); R144/R114/R119"
loop_back_to: "A4"
gap: "A4 must graft the order-book deflator bear counter (Claim B): USD 120M is 'including executed to date' (fulltext line 729) so the forward book is smaller, and equals ~57% of NPC CY2025 revenue USD 211.4M (under 7 months backlog); restore the dropped 'including executed to date' qualifier to table 2.7 (R144). Coverage and arithmetic pass; this is the only blocker."
analyst_note: "A4 is thorough and already skeptical: coverage ties out (335 rows contiguous, no orphans), arithmetic is clean to rounding, and the load-bearing ex-OI flag (consol FY26 12.3% below 13% floor) recomputes exactly. Two of three adversarial counters (NPC cheap on one CY2025 year; NPC margin lift diluted by pre-NPC dilutive subs) are already carried by A4. The single un-incorporated survivor is the order-book deflator: the deck itself says USD 120M is 'including executed to date' (line 729), a qualifier A1's R144 and A4's table 2.7 dropped, and USD 120M is under 7 months of NPC's own revenue. A4 presents the order book as unqualified day-one strength and its only caveat is price competition, not book size. Per the A5 rule that a surviving same-text counter must be added before save, this blocks save. Fix is a one-paragraph graft plus restoring the dropped qualifier; then COMPLETE."
```
