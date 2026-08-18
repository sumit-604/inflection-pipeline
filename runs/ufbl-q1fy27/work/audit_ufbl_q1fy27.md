# A5 ADVERSARY / COMPLETENESS AUDIT — UFBL Q1 FY27 (full three-document run)

Auditor: A5 (fresh context). Inputs seen: A4 review, A1 extracts (results/concall/presentation), A2 ledgers (results/concall/presentation). A3 reasoning NOT seen — every count and metric below is re-derived from the extracts and ledgers directly.

Verdict: **COMPLETE**. Detail follows.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate, run first)

Section D of the review carries the PLAIN-LANGUAGE BRIEF with all four labelled parts present and non-empty:

| Part | Review location | Present? | Real content check |
|---|---|---|---|
| 1. Summary narrative | L699-700 | YES | ~20-line narrative, numbers-first, names the five cautions and the cap |
| 2. Sector intelligence | L702-703 | YES | industry size, organised mix, AMC tailwind, GCC inflation, Labour Codes — provenance-tagged |
| 3. Business-model intelligence | L705-706 | YES | segment split, unit economics, operating-leverage engine, captive channel, delivery drift, CFO gap |
| 4. Competition intelligence | L708-709 | YES | #1 CDR, captive-channel moat, Jubilant 9.3% stake, structural weaknesses, margin risk |

GATE 0: **PASS.** No placeholder, no empty heading.

---

## AUDIT 1 — COVERAGE (independent re-enumeration vs A2 ledger)

Fresh grep/sweep counts over each extract, diffed against the A2 ledger:

| Category | A2 count | My fresh count | Orphan / missing | Status |
|---|---|---|---|---|
| RESULTS notes (std+cons) | 14 + 13 = 27 | 27 (std L191..289 = 14; cons L532..699 = 13) | none | MATCH |
| RESULTS line items (value-bearing) | 23 + 30 = 53 | 23 std (L152-186) + 30 cons (L478-527) | none | MATCH |
| RESULTS consolidation entities | 14 (1 holding + 13 subs) | 14 (subs a–m L361-383) | none | MATCH |
| RESULTS auditor paras | 4 + 8 = 12 | std 1-4; cons 1-8 | none | MATCH |
| RESULTS signature blocks | 5 | 5 (Nagamani; Rahul×2; Sunil×2) | none | MATCH |
| RESULTS agenda items | 1 | 1 (L34-36) | none | MATCH |
| CONCALL participants | 17 | 17 (P1-P17) | none | MATCH |
| CONCALL turns | 63 | 63 (61 grep + 2 missing-colon Disha turns L933/948) | none | MATCH |
| CONCALL questions | 22 | 22 (11 hand-offs + 11 follow-ups) | none | MATCH |
| CONCALL mgmt numbers / hedges | 88 / 14 | MN1-88 / FH1-14 | none | MATCH |
| PRESENTATION slides | 39 | 39 (`[page N]` N=1..39 contiguous) | none | MATCH |
| PRESENTATION P&L / BS rows | 17 / 37 | slide 31 = 17; slide 32 = 37 (ties 14,373/13,141) | none | MATCH |

**No missing-from-ledger rows** (nothing in my fresh pass that the ledger lacks). **No orphan review claims** (every review number traces to an extract line).

Ledger cross-cutting flags all reflected in the review:
- STANDALONE_CONSOLIDATED_PAT_GAP → Step 4, Step 6B#9, C-1#6, FLAG 2, QFM Q3.
- OTHER_AUDITOR / UNAUDITED_SUBSIDIARY_RELIANCE → Step 0D-bis, C-1#6, FLAG 1, QFM Q2.
- SIGNATURE_TIMING → Step 8 FLAG 3, C-1#8, QFM Q12.
- ENTITY_CHANGE (retro amalgamation, Thai/Qatar) → Step 0D notes, 1B restatement note, C-1#8, QFM.
- ZERO_STANDING nil tax → Step 4, F8-a, C-1#7, FLAG 4, QFM Q5.
- Deck ZERO_STANDING investments-vanished → Step 5, Watchlist 3 (RED), C-1#9, QFM Q8.
- Deck GSI ZERO_STANDING → Watchlist 4, QFM Q10.
- Deck SSSG chart 4.7% vs 28.7% → Watchlist 1, C-1#5, QFM Q4.
- Deck footnote "temporary GCC" (International basis) → C-1#2, QFM Q7.

A3 AMBIGUOUS / FORWARD-SIGNAL findings (all three forensics files, as enumerated in the review header L21-23) are each either a QFM row or RESOLVED-BY-CALL with a transcript cite:
- RESOLVED-BY-CALL (C-5a): Deck A5, Deck A3 (FY27 portion), Concall F7-3, F17-9, F6-3, F6-1/F6-2 — each with an L-cite.
- OPEN QFM (C-5b, 14 rows): F11-a, F4-a/b/c, F2-a/b, F3-a, A8/F17-1/F17-2, F8-a/A6, A3/F17-10, A5/A10/F7-4/F7-5, A1/F11-a/F17-5, F6-a/F7-a, A2/F17-8, F6-b, F14-a, A9/F17-7, F7-6.
- Backward/descriptive findings (e.g. deck A4 three-engine growth, F1-a approval, F9/F10/F12 mechanical notes) carried in the body as reviewed-no-open-question.

No forward-signal or ambiguous item that I can derive from the extracts is left unrouted. COVERAGE: **PASS.**

---

## AUDIT 2 — ARITHMETIC (recomputed from cited extract lines; Mn ×0.1 = Cr)

| Metric | A4 value | My recompute | Source line | Status |
|---|---|---|---|---|
| Std revenue YoY | +43.4% | 3,283.85/2,289.36−1 = +43.44% | res L152 | OK |
| Cons revenue YoY | +43.4% | 4,258.99/2,969.81−1 = +43.41% | res L478 | OK |
| Std Op EBITDA | 53.24 | 54.98−1.74 = 53.24 | res L160/153 | OK |
| Std Op EBITDA YoY | +66.4% | 53.24/31.99−1 = +66.4% | derived | OK |
| Std Op EBITDA margin | 16.2% / +224bps | 53.24/328.39 = 16.21%; 16.21−13.97 = 224bps | res L152/160 | OK |
| Cons Op EBITDA | 69.86 | 71.095−1.238−0 = 69.857 | res L490/479/489 | OK |
| Cons Op EBITDA margin | 16.4% / +90bps | 69.86/425.90 = 16.40%; −15.49 = 91bps | res L478/490 | OK |
| Cons Op EBITDA YoY | +51.8% | 69.86/46.01−1 = +51.8% | derived | OK |
| Std reported EBITDA | 54.98 | 6.13+31.30+17.55 = 54.98 | res L164/163/162 | OK |
| Cons reported EBITDA | 71.09 | 2.43+45.71+22.95 = 71.09 | res L494/493/492 | OK |
| Std core PBT ex-OI | 4.39 | 6.13−1.74 = 4.39 | res L164/153 | OK |
| Cons core PBT ex-OI | 1.19 | 2.43−1.24 = 1.19 | res L494/479 | OK |
| Std OI/PBT | 28.4% | 1.74/6.13 = 28.4% | res L153/164 | OK |
| Cons OI/PBT | 51.0% | 1.24/2.43 = 51.0% | res L479/494 | OK |
| Std ETR | 0.0% | 0/6.13 = 0% | res L170 | OK |
| Cons ETR | 5.3% | 0.126/2.434 = 5.35% | res L500/494 | OK |
| Std PAT margin | 1.87% | 6.13/328.39 = 1.87% | res L171/152 | OK |
| Cons PAT margin | 0.54% | 2.31/425.90 = 0.54% | res L501/478 | OK |
| **S-vs-C PAT gap** | −3.82 Cr | 6.13−2.31 = −3.82 | res L171/501 | OK |
| **Gap % of std PAT** | 62% / −62.3% | 3.82/6.13 = 62.3% | derived | OK |
| Q4FY26 subs drag | −3.72 | −11.35−(−15.07) = +3.72 (subs drag) | res L171/501 | OK |
| Q1FY26 subs | +0.28 | −16.96−(−16.68) = −0.28 (subs positive) | res L171/501 | OK |
| **Other-auditor rev share** | 22.7% | 968.86/4,258.99 = 22.75% | res L397/478 | OK |
| **Unaudited loss vs cons PAT** | ~50% / 49.5% | 11.43/23.08 = 49.5% | res L419/501 | OK |
| Para6+7 loss | 3.69 Cr | (25.50+11.43)/10 = 3.693 | res L398/419 | OK |
| Std EPS basic/diluted | 1.57 / 1.55 | as filed | res L185/186 | OK |
| Cons EPS basic/diluted | 0.79 / 0.78 | as filed | res L526/527 | OK |
| PAT bridge (cons YoY) | +18.99 | 23.85−0.79−2.91−0.69−0.03−0.44 = 18.99 | res L490/493/492/479/489/500 | OK |
| Std PAT swing | +23.09 | 6.13−(−16.96) | res L171 | OK |
| Cons revenue QoQ | +18.2% | 425.90/360.40−1 = +18.17% | res L478 | OK |
| Std revenue QoQ | +18.0% | 328.39/278.24−1 = +18.02% | res L152 | OK |
| Normalised std PAT @25.17% | ~4.6 | 6.13×0.7483 = 4.59 | derived | OK |
| Deck adj Op EBITDA % | 8.1% | 343/4,259 = 8.05% | pres L999/983 | OK |
| Deck PAT delta "190 mn" | +190 | 23−(−167) = 190 | pres L994 | OK |
| Deck adj PAT delta "215 mn" | +215 | 87−(−128) = 215 | pres L1001 | OK |
| Int'l GM moderation | ~3pp / 320bps | 72.8−69.6 = 320bps | pres L933 (slide 29) | OK |
| Annualised revenue | 17,036 Mn = Q1×4 | 4,259×4 = 17,036 | pres L983/L144 | OK |
| Net debt ex-lease Mar-26 | ~106.7 | (772+572−256−21)/10 = 106.7 | pres slide 32 | OK |
| Net debt ex-lease Mar-25 | ~53 | (462+233−169−2)/10 = 52.4 | pres slide 32 | OK |
| Labour-Code std / cons one-off | 6.09 / 7.47 | (46.68+14.20)/10; (55.13+19.58)/10 | res L256/L687 | OK |

**Arithmetic mismatches above rounding: NONE.** Every derived figure ties to its raw line within rounding. The gap is stated as both "62%" (body) and "-62.3%" (YAML) — consistent rounding, not a discrepancy.

---

## AUDIT 3 — ADVERSARIAL READ (three most positive claims, strongest bear counter from the SAME extract)

**Positive claim 1 — "Clean operational turn to PAT-positive; ~100% of the PAT swing from recurring core ops; Other Income fell YoY" (review Step 4, L216).**
Strongest bear from same text: the reported PAT is tax-shield-flattered and group-marginal. Standalone 6.13 Cr carries 0% ETR (res L170); a 25.17% charge cuts it to ~4.6 Cr. Consolidated PAT is only 0.54% margin, and ~49.5% of it (an 11.43 Mn unaudited loss, res L419) rests on management-certified numbers; the −3.82 Cr subsidiary drag means the GROUP barely broke even. FY26 was additionally flattered by a non-recurring 6.14 Cr earlier-year tax credit (res L167).
Survives? Counter is fully supported — but it is ALREADY grafted (Step 4 mandatory Qs, FLAG 1/2/4, C-1#6/#7, QFM Q1/Q2/Q3/Q5). No new graft required.

**Positive claim 2 — "Revenue +43.4% YoY, SSSG 28.7%" headline (Step 1/2).**
Strongest bear from same text: the 28.7% sits on a depressed base (Q1FY26 BBQ-India SSSG −5.2%, pres slide 27), the deck's own 12-year chart shows Q1FY27 SSSG of 4.7% with 28.7% tagged to FY26 (pres L746-748), management refuses to defend durability (FH12, concall L1138), and the 28% quoted in an International context conflates segment (Int'l 8.5%, MN10) with consolidated (F17-2).
Survives? Supported — but ALREADY grafted (Watchlist 1 AMBER, C-1#5, QFM Q4, growth-trigger caveat). No new graft required.

**Positive claim 3 — "Operating-margin expansion +224bps std / +90bps cons on operating leverage" (Step 2).**
Strongest bear from same text: the expansion is entirely leverage-driven while GROSS margin COMPRESSED — consolidated gross margin 67.7%→65.8% YoY (pres slide 25) and BBQ-India 66.1%→64.1%, with MN76 showing gross margin −2pp YoY vs restaurant-operating-EBITDA +3pp. Add the not-yet-booked recurring Labour-Code charge (res Note 9, F6-a) and the partly-permanent International GM step-down (concall L1133-1135), and the margin engine is opex leverage over a compressing gross line.
Survives? The review already attributes the margin engine explicitly to operating leverage NOT gross margin ("D&A fell, back-end cost 7.1%→6.5%," Steps 2/4, business-model brief), flags International step-down (C-1#2) and the un-booked Labour-Code charge (Step 3, QFM Q9), and carries MN58/MN76 gross-margin drag in the ledger. The gross-margin-compression nuance is substantially represented; it does not survive as an UNADDRESSED claim requiring a new graft. (Noted for completeness only.)

**No bull claim survives unaddressed either** — deck's FY30 400-425 target, 30-40% store ROCE, and annualised 17,036 Mn optics are each flagged as dropped/unpriced/matured-basis (C-1#3/#9, QFM Q6/Q13, Pillar seeding).

**Surviving bear counters requiring graft into A4: NONE.**

---

## SPECIFIC GATE CHECKS (per task)

- Cash-conversion INDETERMINATE cap: the Q1 filing contains NO cash-flow statement (confirmed — extract has standalone + consolidated P&L only, no CF, no balance sheet). Review RETAINS the cap and states verdict "cannot exceed PROCEED WITH CAVEATS … cap is NOT lifted" (Step 5 L242, C-1#1, C-3 CAVEAT 1). Correctly retained, not wrongly lifted. PASS.
- Cross-document contradictions represented faithfully: (a) deck "temporary" vs call "part permanent" International GM — C-1#2, faithful; (b) deck FY30 400-425 vs call FY27 300 — C-1#3, faithful (path reconcilable but FY30 silently dropped); (c) deck net-debt "doubled" YoY vs CFO "marginally up" QoQ — C-1#4, correctly framed as a comparison-window/framing tell, not a numeric contradiction (both ~106 Cr; my recompute 52.4→106.7 confirms the ~doubling); (d) 28.7% consolidated vs 4.7% chart / vs 8.5% International SSSG — C-1#5, faithful. PASS.
- The "doubled" wording is A3/A4 characterisation, not a verbatim deck quote; substance (net debt roughly doubled YoY on the deck balance sheet) is arithmetically correct and the review itself clarifies it is a framing difference — not a defect.

---

## VERDICT

**COMPLETE.** Deliverable brief present (4/4), fresh enumeration matches the ledger on every category (no orphan rows, none missing-from-ledger), every derived metric recomputes within rounding, the INDETERMINATE cash-conversion cap is correctly retained, all four cross-document contradictions are represented faithfully, and no bear or bull counter survives unaddressed. Proceeds to Notion save.

loop_back_to: none. gap: none.

```yaml
stage: A5-adversary
company: "UFBL"
quarter: "Q1FY27"
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
