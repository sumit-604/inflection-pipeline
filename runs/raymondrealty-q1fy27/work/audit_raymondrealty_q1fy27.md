# A5 ADVERSARY / COMPLETENESS AUDIT — RAYMOND REALTY — Q1 FY27

Agent: A5 ADVERSARY | Model: claude-opus-4-8
Inputs seen (only these): A4 review, A1 concall extract, A2 concall ledger. No A3 reasoning, no orchestrator commentary. All cites re-derived independently; A4/A3 cites checked, not trusted.
Line convention: `Lnn` = original transcript line (the number before the tab in the A1 extract); `Tn` = A2 Section-B turn; `Nn`/`Cn`/`Qn`/`FND-nn` = ledger/finding ids.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate, run FIRST)

The PLAIN-LANGUAGE BRIEF is present as **Section F** of the A4 review (review lines 437-455), all four labelled parts present, non-empty, real content (not placeholder), provenance-labelled ("this quarter" / Notion-sourced) with line cites.

| Brief part | Location | Present? | Content real & provenance-labelled? |
|---|---|---|---|
| (1) Summary narrative (10-20 lines) | review L439-440 | PRESENT | Yes — ~20-sentence narrative, line-anchored (₹700cr/L17, ₹824cr, 9.6%, etc.) |
| (2) SECTOR intelligence | review L442-445 | PRESENT | Yes — demand cycle, 2034 DCR policy, asset-light structural read, all labelled "this quarter" |
| (3) BUSINESS-MODEL intelligence | review L447-450 | PRESENT | Yes — two engines, unit economics, margin back-ending, ROCE step-down, all line-cited |
| (4) COMPETITION intelligence | review L452-455 | PRESENT | Yes — brand/delivery moat, Sunteck leverage/governance contrast, FII/DII exodus, PE-partner risk |

**GATE 0 = PASS.** All four parts present and provenance-labelled.

Minor observation (NOT a gate failure): five brief bullets carry mislabelled turn prefixes that duplicated the line number as the turn number — "T25/L25" (correct turn is T7), "T167/L167" and "T167/L175" (T167 does not exist; max turn is T103; correct turns are T78 and T82), "T67/L67" (T28), "T109/L109" (T49). The **`Lnn` cites all resolve to the correct content** and per the review's own convention (review L6) `Lnn` is the authoritative anchor, so provenance is intact and verifiable. Cosmetic labelling slip only; does not fail the gate and does not rise to a FAIL.

---

## AUDIT 1 — COVERAGE (fresh independent enumeration, diffed vs A2 ledger)

Fresh grep/sweep pass over the A1 extract, then diffed against the A2 count test and every ledger row checked for citation in A4.

| Category | A2 count | My fresh count | Method | Orphan rows (in ledger, absent from A4) | Status |
|---|---|---|---|---|---|
| Turns | 103 | 103 | odd lines L13-L217 = (217-13)/2+1 = 103 | none | MATCH |
| Participants | 15 | 15 | P1-P5 (4 mgmt + host) + P6-P14 (9 analysts) + P15 operator | none | MATCH |
| Questions | 28 (grep 27 / sweep 28) | 28 | Q1a-Q10b = 2+3+3+4+2+4+2+2+4+2; all 28 in A4 Step 4A | none | MATCH |
| Mgmt numbers | 71 | 71 | N1-N71 spot-verified against T3/L17 and Q&A turns | none | MATCH |
| Commitments/hedges | 19 | 19 | C1-C19; defensive re-count 4+2+2+3+1 = 12 hedges + 7 commitments cross-checks | none | MATCH |
| A3 findings | 17 (FND-01..17) | 17 | each traced below | none | MATCH |

**Fresh pass found no row the ledger lacks** (nothing to return to A2). **No orphan ledger row absent from A4** (nothing to return to A3). Every A3 finding is engaged:

- Forward-signal FND-01→QM-1, FND-02→QM-2, FND-03→QM-3, FND-04→QM-4, FND-10→QM-5 (all in Section C).
- Ambiguous FND-05→QM-6, FND-07→QM-7, FND-08→QM-8, FND-09→QM-9, FND-12→QM-10, FND-15→QM-11, FND-17→QM-12 (all in Section C).
- Confirmatory-negative FND-06/FND-14→QM-13; silence FND-11 (monitor #6 / 5B), FND-13 (monitor #9 / 5B), FND-16 (Step 2 / 5A / 8C / monitor #3).

**Forward-signal / ambiguous → management-question mandate: SATISFIED.** Every A3 forward-signal and every ambiguous finding produced ≥1 QM row (12 of 12 interpretive findings; 5 silence/confirmatory findings carried into Section D/5B). Independently re-derived from the extract, the classifications are defensible: the Mahim/Parel/6-of-8/SPV items are genuinely forward (N55/N57/N58/N61, T22/L55), the D/E "7% vs 7X" (T3/L17), 6-7-vs-7-8-yr (T3/L17), ROCE-stepdown (N68 vs N50, T28/L67) and dues-to-government (T97/L205) items are genuinely ambiguous.

Section-F data-quality flags (TURN_MERGED, NAME_INCONSISTENT, NAME_GARBLED, SPEAKER_AMBIGUOUS, MODERATOR_AS_ANALYST, MGMT_ABSENCE, ANALYST_CITED_NOT_MGMT) are each engaged: MODERATOR_AS_ANALYST at review L43; MGMT_ABSENCE at FND-15; ANALYST_CITED_NOT_MGMT (the ~50/45/20cr FY26-AR figures) correctly quarantined as analyst-cited, not management, at Exchange 2 / Step 7A / FND-17.

**AUDIT 1 = PASS.** No orphan rows; no missing-from-ledger rows.

---

## AUDIT 2 — ARITHMETIC (every derived metric recomputed from raw N-values)

| Metric | A4 / mgmt value | My recompute | Source line | Status |
|---|---|---|---|---|
| Booking YoY | +129% (N2) | (700-306)/306 = 128.8% | T3/L17 (N1/N3) | PASS (mgmt round-up, <1pp) |
| Collections YoY | +47% (N5) | base not disclosed (550/1.47 = 374 implied) | T3/L17 | PASS (mgmt-stated; no A4 derivation) |
| Total income YoY | +37% (N8) | (536-390)/390 = 37.4% | T3/L17 (N6/N7) | PASS |
| EBITDA YoY | +70% (N10) | (70-41)/41 = 70.7% | T3/L17 (N9/N11) | PASS (within rounding; mgmt-stated, not A4-derived) |
| EBITDA margin Q1 FY27 | 13% (N12) | 70/536 = 13.06% | T3/L17 | PASS |
| EBITDA margin Q1 FY26 | 11% (N13) | 41/390 = 10.5% → 11% | T3/L17 | PASS |
| Gross debt | ₹1,095cr (N70) | 824 + 271 = 1,095 | T41/L93 | PASS (A4 flags internal consistency) |
| D/E | "7%"/"7X" — untieable | net worth ≈ 824/0.07 ≈ 11,771cr if 0.07x, but "7X" contradicts; cannot tie | T3/L17 | PASS — A4 correctly FLAGS (FND-08), does not resolve or estimate |
| Q1 interest vs FY guide | ₹47cr Q1 / ₹100-120cr FY | Q2-Q4 must sum 53-73 → avg ~18-24 ea, far below Q1's 47 | T57/L125; T55/L121 | PASS — A4's "arithmetic strain" flag is correct |
| Cost of debt reconciliation | 9.6% headline understates | FY26 AR ~50+45 = ~95cr; 9.6% explains only ~20cr/Q | T97/L205 (analyst-cited) | PASS — A4 FND-17; figures correctly marked ANALYST_CITED_NOT_MGMT, not fabricated |
| FY27 EBITDA implied | "roughly ₹575-590cr" | 480-490 x 1.17-1.20 = 562-588 | T89/L189 (N; prior EBITDA) | PASS — labelled "roughly"; back-ended-ramp conclusion holds |
| Specificity ratio | 0.64 (9/14) | 9/14 = 0.643 | Step 6B | PASS |
| Defensive-phrase count | ≈12 | 4+2+2+3+1 = 12 | Step 6C | PASS |
| Opening quantified share | ~91% (21/23) | 21/23 = 91.3% | Step 1 | PASS |

**Fabrication check.** Confirmed no number was invented. Role 4 filing-number steps are marked **N.A./ND** throughout (review L18-21; Step 7A cells all "ND — no filing"; `sc_gap_pat_pct = ND` in prose and YAML). A concall was the only document; every P&L/leverage figure is labelled a **management-spoken transcript number** to be verified against the filing when it lands. Notion-sourced monitor baselines (e.g. ₹656cr net-debt green line, ₹1,000/₹1,500cr stop-loss lines, ₹641 CMP, Sunteck 0.21x) are labelled as Notion monitor definitions, not concall/filing data — not fabrications (not independently verifiable from my three inputs, but correctly provenance-separated).

**AUDIT 2 = PASS.** No mismatch above rounding.

---

## AUDIT 3 — ADVERSARIAL READ (strongest bear counter to A4's three most positive claims, from the same extract)

**Positive claim 1 — "Booking value ₹700cr, +129% YoY; growth clearly firing" (Step 1 / monitor #2 GREEN / brief).**
Strongest bear from the extract: the +129% is off a depressed ₹306cr base (T3/L17) and is a gross pre-sales/booking metric, not recognised revenue or cash — total income grew only 37% and cash collections (₹550cr) trail bookings (₹700cr); the print was juiced by four projects launched at the tail of Q4 FY26, "most of it in Q4 itself" (T3/L17), and JDA cash collection is only ~₹692cr against ~₹2,900cr cumulative JDA sales (~24%) with projects "at excavation stage."
Survives? **NO — already incorporated.** A4 caps at WATCHLIST/AVOID with cash conversion INDETERMINATE, flags collections-lag OCF withheld (review L314), and the launch-timing context appears in Step 1 / Step 6A. No new graft required.

**Positive claim 2 — "Firmly and completely on track" to FY27 EBITDA margin 17-19% (C1/N15, guidance graded HIGH-ish).**
Strongest bear from the extract: Q1 actual margin is 13% (N12), and management concedes the launched JDAs are "currently not giving 20%" and only mature "by FI28" (T74/L159), so the FY27 blend depends on H2 running well above 19% on projects management itself says are sub-target this year.
Survives? **NO — already incorporated.** This is FND-04 (Step 2 L129, monitor #1 AMBER, brief business-model #2 "single biggest model-execution risk," QM-4). Bear fully present.

**Positive claim 3 — "Flagship Parel JDA signed, GDV ₹8,500cr, SoBo entry FIRED" (Step 1 / 8A / monitor #5 GREEN).**
Strongest bear from the extract: Parel is ~18 months to market (~H2 FY28, N55) and contributes zero near-term revenue while demanding ₹350-500cr peak capital (N64) on a quarter where net debt is already ₹824cr / gross ₹1,095cr and management says debt "may not moderate for another 1-2 years" (T79/L79; T97/L95). The marquee win adds leverage before any return, on the exact axis the thesis marks weak.
Survives? **NO — already incorporated.** FND-02, 8A ("revenue DELAYED to ~H2 FY28"), capex in Step 2, FND-16. Bear present.

Additional adversarial probes tested and found already-covered: ROCE 20%+ boast flattered by cheap dues-to-government funding (FND-05/FND-17); 9.6% headline excludes the ~₹45cr govt leg (FND-17); "demand strong" set against institutional exodus 20-22%→8% (competition brief #2 / Q9c); borrowings ~₹380cr→~₹897cr YoY trajectory vs the ₹1,000cr Q2 stop-loss (monitor #3 AMBER, "watch Q2").

**AUDIT 3 = PASS.** No bear counter survives A4's existing coverage; A4's symmetric bull-bear (house STYLE) already carries every extract-supported bear. **`surviving_bear_counters = []`** — nothing to graft back to A4.

---

## VERDICT

**COMPLETE.**

- Gate 0 (plain-language brief, four parts): PASS.
- Coverage: PASS — 103 turns / 15 participants / 28 questions / 71 numbers / 19 commitments all reconciled; no orphan row; all 17 FNDs engaged; every forward-signal/ambiguous finding produced a management question.
- Arithmetic: PASS — every derived metric recomputes within rounding; no fabrication; Role 4 filing cells correctly N.A./ND.
- Adversarial: PASS — no surviving bear counter.

Only note carried forward (does not block save): cosmetic turn-label typos in five Section-F brief bullets ("T25/L25", "T167/L167", "T167/L175", "T67/L67", "T109/L109"); the `Lnn` anchors all resolve correctly, so provenance is intact. Optional A4 tidy, not a gate failure.

Proceeds to Notion save.

```yaml
stage: A5-adversary
company: "raymondrealty"
quarter: "q1fy27"
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
