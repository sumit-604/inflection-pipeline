# A5 ADVERSARY / COMPLETENESS AUDIT — Asian Energy Services Limited (ASIANENE) — Q1 FY27

**Agent:** A5 Adversary | **Model:** claude-opus-4-8 | **Date:** 13 Aug 2026
**Re-audit after one loop-back.** Prior A5 pass returned INCOMPLETE on a single surviving bear counter (GSECL Rs 187.6 Cr order framed GREEN/FIRED despite the Mineral segment RESULT falling YoY). This pass verifies the fix landed AND re-runs the full independent audit (deliverable, coverage, arithmetic, adversarial). I re-derive from the A1 extracts and A2 ledgers only; I did not defer to A4's or A3's cites.

**Role 5 scoping check:** Doc set = results (Reg 33) + presentation (34-slide deck) + pressrelease (4-page Reg 30). NO concall transcript present. A4 scoped Role 5 as N/A, turns = 0 (review L5, L15; YAML L464). **Correct — verified.**

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate, run first)

| Brief part | Location | Present? | Real content? |
|---|---|---|---|
| (1) Summary narrative | review L437-439 | present | ~20 lines, provenance-labelled, non-placeholder |
| (2) SECTOR intelligence | review L441-443 | present | policy tailwinds, segment divergence, sector cap 20x — real |
| (3) BUSINESS-MODEL intelligence | review L445-447 | present | 3 revenue engines, Kuiper margin, Oilmax model shift — real |
| (4) COMPETITION intelligence | review L449-451 | present | moat, governance disadvantage, small-cap trap — real |

**GATE: PASS.** All four labelled parts present and carrying substantive content.

---

## AUDIT 1 — COVERAGE (fresh independent enumeration vs A2 ledgers)

Fresh grep/sweep counts re-derived from the three A1 extracts and diffed against each ledger.

| Category | A2 count | My fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Results: numbered notes | 17 (9 consol L345-403 + 8 standalone L574-624) | 17 | none | MATCH — all mapped to Step 0D table C1-C9/S1-S8 |
| Results: consolidation entities | 31 (26 subs L194-219 + 5 JVs L224-228) | 31 | none | MATCH — covered in 0D auditor check + audit-coverage flag |
| Results: 4 unbucketed subs (ENTITY_COUNT_UNRECONCILED) | flagged | confirmed (26 annexure − 22 in paras 5-7) | none | MATCH — A4 Q3 (L385) + flag L504 address it |
| Results: consol P&L lines | 36 | 36 | none | MATCH — Step 1A |
| Results: standalone P&L lines | 28 | 28 | none | MATCH — Step 1B |
| Results: segment table | 14 + 4 roman notes | 14 + 4 | none | MATCH — Step 3 diagnostic + segment-result read |
| Results: auditor paras | 13 (8 consol + 5 stand) | 13 | none | MATCH — 0D auditor opinion check |
| Results: signature blocks | 5 | 5 | none | reviewed, no finding (admin) |
| Presentation: slides | 34 | 34 | none | MATCH — substantive slides cited; CSR/safety/board/TOC/glossary/map reviewed-no-finding |
| Presentation: footnotes | 5 (L255,297,437,872,898) | 5 | none | MATCH — Kuiper-integration + order-book ex-GST/ex-Kuiper/Oilmax caveats all used |
| Pressrelease: headline numbers | 19 | 19 | none | MATCH |
| Pressrelease: quotes | 2 (Garg L124, Maheshwari L139) | 2 | none | MATCH |
| Pressrelease: forward statements | 8 | 8 | none | MATCH — guidance, merger timeline, preferred bidder |
| Pressrelease: operational claims | 12 | 12 | none | MATCH — GSECL (OC4), Mid-East (OC5), OEPL 55.99% (HN19), agri subsidiary (OC12) all addressed |

**No orphan rows** (ledger rows absent from A4). **No rows my fresh pass found that the ledger lacks.** The extraction spine is unchanged and reconciles 100% on all three ledgers. Coverage **PASS**.

---

## AUDIT 2 — ARITHMETIC (every derived metric recomputed from raw Lakhs)

Conversion Lakhs x0.01 → Rs Cr. Source = results extract line numbers.

| Metric | A4 value | My recomputed | Source | Status |
|---|---|---|---|---|
| Consol Op EBITDA (ex-JV,ex-OI) Q1FY27 | 21.14 | 27,118.53−21,892.76−17.04−1,838.00−1,256.06 = 2,114.67 → 21.15 | L245/250/251/252/255 | PASS (0.01 rounding) |
| Consol Op EBITDA Q1FY26 | 11.45 | =11.46 | same, 30-Jun-25 col | PASS (0.01 rounding) |
| Op EBITDA margin Q1FY27 / Q1FY26 | 7.80% / 9.92% | 21.14/271.19=7.80%; 11.45/115.37=9.92% | derived | PASS |
| Op EBITDA margin YoY | −212 bps | 7.80−9.92 = −2.12 pp | derived | PASS |
| Deck EBITDA (incl JV) Q1FY27 | 21.93 | 21.14+0.79 = 21.93 | +L259 | PASS (deck 21.9) |
| Deck EBITDA margin Q1FY27 | 8.09% (deck 8.1%) | 21.93/271.19 = 8.09% | derived | PASS |
| Effective Tax Rate consol Q1FY27 | 25.4% | 435.20/1,710.85 = 25.4% | L268/L262 | PASS |
| PAT margin consol Q1FY27 | 4.71% | 1,275.65/27,118.53 = 4.71% | L269/L245 | PASS |
| Core PBT ex-OI Q1FY27 | 13.79 | 17.11−3.32 = 13.79 | L262−L246 | PASS |
| Revenue YoY consol | +135.1% | 27,118.53/11,536.69−1 = +135.06% | L245 | PASS |
| Standalone revenue YoY | +29.4% | 14,927.67/11,536.69−1 = +29.39% | L527 | PASS |
| PAT YoY consol | +126.5% | 1,275.65/563.23−1 = +126.49% | L269 | PASS |
| EPS basic YoY consol | +104.0% | 2.53/1.24−1 = +104.0% | L299 | PASS |
| Finance cost YoY consol | +150.3% | 376.38/150.34−1 = +150.35% | L253 | PASS |
| Standalone Op EBITDA margin Q1FY27/Q1FY26 | 10.92% / 10.30% | 16.30/149.28=10.92%; 11.88/115.37=10.30% | L527-537 | PASS |
| S-vs-C PAT gap Q1FY27 (Cr / %) | +3.21 / +33.5% | 12.76−9.55=3.21; 3.21/9.55=33.6% | L269/L550 | PASS |
| S-vs-C gap swing | ~41.3 pp | +33.5 − (−7.8) = 41.3 pp | derived | PASS |
| Revenue gap (subs) Q1FY27 | +121.91 | 271.19−149.28 = 121.91 | L245/L527 | PASS |
| PAT bridge total | +7.13 | 12.76−5.63 = 7.13; PBT +9.26 less tax +2.13 = +7.13 (closes) | L269 | PASS |
| **O&G segment result YoY (GSECL fix)** | 18.86→33.30, +76.5% | 1,886.34→3,329.93 = 18.86→33.30 Cr | **L316** | PASS |
| **Mineral segment result YoY (GSECL fix)** | 4.69→4.07, −13.2% | 469.05→406.97 = 4.69→4.07 Cr; −13.24% | **L317** | PASS |
| O&G / Mineral segment margins YoY | 20.4%→13.6% / 20.3%→15.4% | 18.86/92.24, 33.30/244.78; 4.69/23.13, 4.07/26.41 | L311/312/316/317 | PASS |
| Mineral revenue QoQ | −68% | 2,640.94/8,223.60−1 = −67.9% | L312 | PASS |
| 17.6% unaudited PAT | Rs 2.24 Cr / 17.6% | (145.19+78.85)/12,756.5 wait → (1.45+0.79)/12.76 = 17.55% | L137/L139/L269 | PASS |
| GSECL order value | Rs 187.6 Cr | deck L232 "Rs.187.6 crore ... GSECL" | deck L232 | PASS |

**No mismatch above rounding tolerance (all ≤0.01 Cr / ≤0.1 pp). Arithmetic PASS.** Independent corroboration of the fix: deck slide 11 (presentation L369/L384) shows Mineral segment profit falling 4.7→4.1, matching results L317 — the segment-result decline is disclosed in two documents, not an artifact.

---

## AUDIT 3 — ADVERSARIAL READ (three most positive claims + strongest bear counter from the same text)

**Positive claim 1 — "Revenue +135%, PAT +129% (loud growth quarter)."**
Strongest bear counter (from extract): entirely Kuiper base-effect (integrated only 01-Sep-2025, deck fn L297); standalone organic +29.4% only (L527), below the 30-40% guide; consol op-EBITDA margin fell −212 bps; incremental Rs 121.9 Cr subsidiary revenue earned ~4% margin (L245 vs L527). **Counter does NOT survive as a gap — it is already the spine of A4** (Step 2 diagnostics 1-2, Step 4S, summary narrative). No action.

**Positive claim 2 — "GSECL Ukai Rs 187.6 Cr order won, work commenced" (the re-cast item).**
Strongest bear counter: the order lands in the Mineral & other energy segment whose YoY segment RESULT fell Rs 4.69→4.07 Cr, −13.2% (L317), while ALL group segment-profit growth is Oil & Gas, Rs 18.86→33.30 Cr (L316). **Counter SURVIVES on the extract — and A4 has now grafted it in completely.** Verified present and consistent at every required cell:
- Watchlist item 4, Step 6B (review L303): GREEN/FIRED → **AMBER**, decline grafted.
- Growth-trigger, Step 6D (L328): → **AMBER**, "NOT a profit-level FIRE".
- Step 3 QoQ diagnostic (L193): segment-result read added, both margins.
- Monitorables (L420) + YAML monitorables (L490): AMBER, −13.2%, L316/L317 anchored.
- Step 7 growth-visibility pillar (L343): "into a declining-profit segment".
- Step 9 Notion note (L409) + summary narrative (L439) + sector brief (L443) + business-model brief (L447) + competition brief (L451): decline stated with L316/L317.
- YAML flags (L498): explicit "GSECL RE-CAST (A5 loop-back)" entry.
No residual cell still frames GSECL as GREEN/FIRED. **Fix landed correctly and completely.**

**Positive claim 3 — "Core operating PBT grew +135%, standalone margins improved — growth is real, not a treasury illusion."**
Strongest bear counter: standalone revenue +29.4% is BELOW the 30-40% order-backed guide floor (tripwire-4 soft miss, L316/L306); the consolidated quality is worse than headline (17.6% of PAT unreviewed by any auditor, one sub −3.26 Cr on nil revenue, L112-144); Oilmax dilution basis undisclosed. **Counter does NOT survive as a gap — already incorporated** (tripwire 4, watchlist 7-8, earnings-quality flag, Step 4S). No action.

**Fresh surviving counter elsewhere?** I searched the extract for a new thesis-relevant, line-anchored blocker: order book Rs 1,754 Cr excludes Kuiper AND Oilmax (deck fn L898) → covered (Step 6D, Q11); deck "EBITDA" non-standard incl-JV/ex-OI → covered (Step 1C); Mineral segment REVENUE actually rose +14.2% YoY even as result fell → A4 correctly anchors on the RESULT decline, no counter. **No fresh surviving counter that clears the bar.**

---

## VERDICT

**COMPLETE.**

- Deliverable gate: PASS (all four brief parts present, substantive).
- Coverage: PASS (fresh enumeration matches all three ledgers; zero orphan rows; zero missing-from-ledger rows).
- Arithmetic: PASS (every derived metric recomputes within rounding; the GSECL segment-result fix at L316/L317 is arithmetically exact and doubly corroborated by deck L369/L384).
- Adversarial: the one previously-surviving bear counter (GSECL into a shrinking-profit Mineral segment) is now grafted into A4 completely and consistently across all required cells; no fresh surviving counter.

Only COMPLETE proceeds to Notion save. This review is cleared.

```yaml
stage: A5-adversary
company: "ASIANENE"
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
surviving_bear_counters: []   # GSECL counter re-verified as fully grafted into A4 across watchlist item 4, growth-trigger 6D, Step 3, Step 7, monitorables, all four brief parts, Notion note, and YAML flags; no fresh surviving counter
loop_back_to: ""
gap: ""
```
