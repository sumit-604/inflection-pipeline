# QUARTERLY A5 ADVERSARY / COMPLETENESS AUDIT — QPOWER Q1 FY27

Auditor: A5 (Opus 4.8). Fresh context. Re-derived independently from the A1 extract,
A2 ledger, A3 forensics and the A4 review. A4's and A3's cites were re-checked at
line level, not deferred to.

Inputs audited:
- Review: runs/qpower-q1fy27/work/review_qpower_q1fy27.md
- Extract: runs/qpower-q1fy27/work/extract_concall_qpower_q1fy27.txt (318 lines)
- Ledger: runs/qpower-q1fy27/work/ledger_concall_qpower_q1fy27.md
- Forensics: runs/qpower-q1fy27/work/forensics_concall_qpower_q1fy27.md

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate, run first)

PLAIN-LANGUAGE BRIEF located at review lines 533-545. All four labelled parts present and non-empty:

| Part | Heading present | Content | Status |
|---|---|---|---|
| 1. Summary narrative | L535 | 10-20 line narrative; numbers-first; reaffirms WATCHLIST/deep AVOID; flag-not-instruction | PRESENT |
| 2. Sector intelligence | L538 | Transmission/renewable/BESS/data-centre tailwind; EU localization; Chinese-bidder regulation; Atlanta moat gap | PRESENT |
| 3. Business-model intelligence | L541 | Multi-entity HV platform; margin-by-entity; add-back asymmetry; NCI/Owners-vs-Total EPS nuance; cash conversion INDETERMINATE | PRESENT |
| 4. Competition intelligence | L544 | Sole >220kV HVDC coil maker; MEU ~50% share; WS insulator adjacency; Hitachi/Siemens/GE peers; Atlanta trigger open | PRESENT |

GATE 0: PASS.

---

## AUDIT 1 — COVERAGE (fresh grep re-enumeration vs A2 ledger)

Doctype = concall. Reconciliation contract = turns + questioner slots + management-number turns (notes / line items / slides / agenda / entities all N/A per A2 Section 7). Fresh grep passes over the extract:

| Category | A2 count | My fresh grep | grep used | Match | Orphan rows |
|---|---|---|---|---|---|
| Speaker turns (total) | 143 | 143 | `^\[(MODERATOR\|HOST\|MANAGEMENT\|ANALYST)` | YES | none |
| — MODERATOR+HOST | 17+1=18 | 18 (143-58-67) | derived | YES | — |
| — MANAGEMENT | 58 | 58 | `^\[MANAGEMENT` | YES | — |
| — ANALYST | 67 | 67 | `^\[ANALYST` | YES | — |
| Questioner slots | 15 | 15 | `^\[MODERATOR\].*(line of\|question is from)` | YES | none |
| Mgmt-number turns | 38 | 38 | `^\[MANAGEMENT.*[0-9]` | YES | none |
| notes / line_items / slides / agenda / entities / auditor_paras | N/A | N/A (transcript) | — | YES | — |

Every reconciliation figure matches to the unit. No row my fresh pass found that the ledger lacks (→ nothing to return to A2). 

Ledger-row-to-review carry-through: A3 reconciled the ledger at 100% (all 143 turns, 115 quantified rows, 17 flags). The A4 review carries the reconciliation preamble (L13), the full participant list (0B), the 15-slot Q&A inventory (4A), the quantified-claims cross-check (Step 7A), and — critically — every A3 forensic finding (see AUDIT 3). No ledger flag is orphaned: EV_VS_PRICE_GAP→F16-3, ARITH_DELTA→F12-1, CONFUSED_RESPONSE→F17-2, UNANSWERED_LIVE→F17-1, GUIDANCE_NARROWING→F16-2, GUIDANCE_REVISION→F16-1, ESTIMATE_CAVEAT→Step 3E/F12-1, ATTRIBUTION_AMBIGUOUS→0B caveat, SPEAKER_NO_ATTRIBUTED_TURN (Mrs. Jadu)→0B row. All surface in the review.

GATE 1: PASS. No orphan rows, no missing-from-ledger rows.

---

## AUDIT 2 — ARITHMETIC (recomputed from raw extract numbers, L38 unless noted)

| Metric | A4 value | My recompute | Source line | Status |
|---|---|---|---|---|
| Order-book split sum | 1,939 (residual ~6 / 6.5) | 801+585+553 = **1,939** | L38 | MATCH (residual vs 1,945 spoken = 6.0; vs 1,945.5 Role-4-posted = 6.5 — both used correctly) |
| YoY segment revenue sum | 259 vs 256.4 (Δ2.6) | 69+83+107 = **259** | L46 vs L38 | MATCH (mgmt self-caveated as rough) |
| Reported EBITDA margin | 25.2% | 64.7/256.4 = **25.23%** | L38 | MATCH |
| Ind AS 29 adjusted EBITDA | 72.5 | 64.7+7.82 = **72.52** | L38 | MATCH |
| Adjusted EBITDA margin | 28.3% | 72.52/256.4 = **28.28%** | L38 | MATCH |
| Adjusted PBT | 67.2 | 59.4+7.82 = **67.22** | L38 | MATCH |
| Adjusted PAT | 54.5 | 46.7+7.82 = **54.52** | L38 | MATCH (add-back untaxed — non-cash monetary loss, zero tax benefit; internally consistent) |
| Gross margin | 47.2% | 121/256.4 = **47.19%** | L38 | MATCH |
| Implied tax / reported ETR | 12.7 / 21.4% | 59.4-46.7 = **12.7**; 12.7/59.4 = **21.38%** | L38 | MATCH |
| Adjusted ETR | 18.9% | 12.7/67.22 = **18.89%** | L38 | MATCH |
| Implied share count | ~10.02 cr | 46.7/4.66 = **10.02 cr**; check 3.12 base consistent | L38 | MATCH |
| EPS | 4.66 vs 3.12 | verbatim, not derived | L38 | MATCH (transcribed correctly) |

No mismatch above rounding on any derived metric. GATE 2: PASS.

Non-blocking observation (not a FAIL): management's "order book ~1.9x last year's revenue" (L34/L38) is a verbatim spoken backward fact, not an A4-derived metric. Last-year revenue is not carried in the extract (Notion-prior ₹947 cr would imply ~2.05x), so it is not independently computable from the extract and A4 correctly relayed rather than recomputed it. No action.

---

## AUDIT 3 — A3 FINDING CARRY-THROUGH + FINDING-ANCHORED QUESTIONS

All 12 A3 findings must appear in the review, and every FORWARD-SIGNAL / AMBIGUOUS finding must yield ≥1 Questions-for-Management row. Verified against the review's finding-anchored QFM table (L480-492) and preamble (L15):

| A3 finding | Class | In review? | QFM row |
|---|---|---|---|
| F6-1 | FORWARD-SIGNAL | Yes (preamble, Step 2/3, monitorables) | Row 5 |
| F7-1 | FORWARD-SIGNAL | Yes (6C, Step 2) | Row 6 |
| F8-1 | AMBIGUOUS | Yes (7A, 5B, flags) | Row 7 |
| F10-1 | FORWARD-SIGNAL | Yes (Exchange 3, 5A, flags) | Row 3 |
| F12-1 | AMBIGUOUS | Yes (7A, Step 1) | Row 8 |
| F13-1 | FORWARD-SIGNAL | Yes (5A, flags) | Row 4 |
| F16-1 | FORWARD-SIGNAL | Yes (Step 2, 6D) | Row 9 |
| F16-2 | AMBIGUOUS | Yes (5A, Step 5A) | Row 10 |
| F16-3 | AMBIGUOUS | Yes (Exchange 3, 5A/5B, flags) | Row 11 |
| F17-1 | AMBIGUOUS | Yes (Exchange 1, 3C, flags) | Row 1 |
| F17-2 | AMBIGUOUS | Yes (4A slot 5, 6C) | Row 12 |
| F17-3 | CONFIRMATORY-NEGATIVE | Yes (5B, 8D Pillar 2, flags) | Row 2 |

All 12 present. All 5 FORWARD-SIGNAL and all 6 AMBIGUOUS findings each generate ≥1 QFM row; F17-3 generates row 2 plus a monitorable (#25/L526). GATE 3: PASS. Nothing to return to A3.

---

## AUDIT 4 — CASH CONVERSION HOUSE RULE

House rule: INDETERMINATE cash conversion must NOT silently resolve to PROCEED; it caps at PROCEED WITH CAVEATS with the missing evidence named.

- Verdict = **PROCEED WITH CAVEATS** (YAML L564; Step 8 title).
- cash_conversion = **INDETERMINATE** (YAML L565), explicitly capped: 8D Pillar 2 "cash conversion INDETERMINATE; cannot upgrade; names the missing cash bridge" (L436); Watchlist item 3 = ND (L412); thesis-broken CFO/PAT tripwire = "ND — not assessable this call" (L428).
- Missing evidence named: Q1 CFO/PAT, current net debt vs ~₹23 cr, cash-reduction quantum, receivable days, CCC (L565, QFM Row 2, brief part 3).

GATE 4: PASS. Rule honoured; not silently upgraded.

---

## AUDIT 5 — DECISION-STATUS FRAMING + BRIEF

- Decision Status verified as **WATCHLIST — deep AVOID at CMP ₹1,400; NOT held** (YAML L566; 8E L445 invokes the 8A-W non-held branch; brief L536). Not restated as BUY; no trim/exit mechanics applied. Entry zone ₹456-570 / MoS ₹456 carried unchanged from Notion prior (L441/L449).
- Plain-language brief (4 labelled parts) present — see AUDIT 0.

GATE 5: PASS.

---

## AUDIT 6 — EXIT-PE / ROUND-NUMBER / ESTIMATION / ANCHORING VIOLATIONS

- Exit multiple: destination PE **31x** sourced "set under Section 1B v3.3" (L435) / Notion prior; no new multiple minted, no round-number default introduced. Y3 FVs (Bear ₹822 / Base ₹1,114 / Bull ₹1,466) and entry zone all carried from Notion/Role 4, not invented. No CLAUDE.md "sole exit multiple authority" violation.
- Estimated numbers: none fabricated as fill. ~10.02 cr shares is a legitimate derivation (46.7/4.66). Undisclosed items (CFO/PAT, net debt, WC, ETR driver, raise size/price, Endoc blended margin, Owners-EPS split) are all explicitly carried as ND / INDETERMINATE / deferred — NOT estimated. Conforms to "NOT FOUND is the only valid fill."
- Anchoring: every this-quarter number is tagged (concall Lx / turn y), (Role 4 posted) or (Notion prior). Provenance convention stated at L7. No unanchored quantitative claim found.

GATE 6: PASS.

---

## ADVERSARIAL READ — three most-positive claims + strongest bear counter from the SAME extract

**Positive claim 1 — "Adjusted EBITDA 28.3% + every order booked above margin guidance = pricing discipline / margin quality" (Step 7A, 6D).**
Bear counter (from extract): the 28.3% rests on a one-sided ₹7.82 cr add-back whose offsetting Turkey asset-base / OCI restatement was refused live and deferred to writing (L214-220); management itself warned "please don't build your castle based on these numbers" (L190) and pre-flagged Q3 standalone-margin moderation from the aluminium lag (L38/L50).
Survives? NO as an un-incorporated counter — already grafted: F17-1 Exchange 1 (L246-252), 6B caveat (L328), brief part 3 (L542), flags (L601). No graft required.

**Positive claim 2 — "20% guidance sits at the conservative base, not the 50% bull; operations at-to-above base" (Exchange 2, 8E).**
Bear counter (from extract): the same call shows MEU delivered 18% vs a 22-23% internal target (a miss, L134), a FY28 "15%" figure appended ambiguously (L248) that could read as deceleration, two capex slips (magnet wire Q3→Q4 L62; Sangli to Q3-trickle/Q4 L206), and an imminent sub-₹500 cr raise at ~89x (L146) — i.e. "at base" is propped by a disputed add-back and threatened by dilution.
Survives? NO as un-incorporated — already grafted: Step 3A/3C, 5A L283, 8E L449, flags L603/L607. No graft required.

**Positive claim 3 — "MEU margin floor raised live to ~18%; BESS pipeline ~$100M; order book 1.9x record" (5A, 6D).**
Bear counter (from extract): raising the "floor" to 18% is an admission MEU undershot its own 22-23% target (L134); the extra $40M BESS is "next 12 months at least" pipeline, not orders, and is gated by the worldwide IGBT bottleneck management itself names (L78); the order-book split carries a ₹6 cr unreconciled residual (L38) and "wouldn't commit" on book-to-bill sustainability (L70).
Survives? NO as un-incorporated — already grafted: F16-1 (honest-miss framing, 6D L336, 5A L283), brief sector IGBT scarcity (L539), F12-1 residual (7A L363). No graft required.

Result: no bear counter survives un-incorporated. The review is symmetric bull-bear and already embeds each counter. surviving_bear_counters = [].

---

## VERDICT

All seven gates PASS. Counts re-enumerated independently and reconcile to the unit (143/15/38). All derived arithmetic recomputed from raw extract numbers — zero mismatch above rounding. All 12 A3 findings carried into the review with finding-anchored questions; every FORWARD-SIGNAL/AMBIGUOUS finding yields ≥1 QFM row. Cash conversion INDETERMINATE correctly caps the verdict at PROCEED WITH CAVEATS with missing evidence named. Decision Status framed as WATCHLIST/deep AVOID (NOT held, NOT BUY). Plain-language brief complete (4/4 parts). No exit-PE/round-number/estimation/anchoring violation. No surviving un-incorporated bear counter.

**VERDICT: COMPLETE.** Proceeds to Notion save. loop_back_to: none.

```yaml
stage: A5-adversary
company: "QPOWER"
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
surviving_bear_counters: []
loop_back_to: ""
gap: ""
```
