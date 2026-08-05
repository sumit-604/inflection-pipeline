# A5 ADVERSARY / COMPLETENESS AUDIT — RSYSTEMS Q2 CY2026 — DECK-INTEGRATION OVERLAY

**Under audit:** `review_deck_addendum_rsystems_q2cy26.md` (A4 deck overlay)
**Fresh context:** A1 extracts (deck, results, press release) + A2 ledgers (deck, results, press release) only. A3 forensics NOT read; every deck number re-derived from the extracts. A4's cites and its "zero contradictions" claim were re-checked, not trusted.
**Auditor:** A5 | **Model:** claude-opus-4-8 | **Date:** 2026-08-05
**Unit convention verified:** ₹ Millions native; ₹ Cr = M x 0.1; US$ mn kept parallel, never summed across currencies.

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate, run first)

The overlay's PLAIN-LANGUAGE BRIEF (§8) carries all four labelled parts, each non-empty and with real content:

| Part | Location | Present? | Note |
|---|---|---|---|
| (1) Summary narrative (10-20 lines) | §8A DELTA NARRATIVE | **PRESENT** | 13 lines, substantive (ACV stall, FX-propped margin, reported vs adjusted, date correction). |
| (2) SECTOR intelligence | §8B | **PRESENT** | FX-as-sector-variable, geography concentration, demand narrative, named provenance gaps. |
| (3) BUSINESS-MODEL intelligence | §8C | **PRESENT** | FX-flattered margin engine, bookings soft spot, inorganic drift, capital-structure. |
| (4) COMPETITION intelligence | §8D | **PRESENT** | Where-it-wins / structurally-weaker / risks-to-watch / peer-concall-absent. |

**Deliverable gate: PASS.** No missing or placeholder part.

---

## 1. COVERAGE AUDIT (fresh enumeration vs A2 deck ledger)

Re-ran the enumeration independently from `extract_deck_rsystems_q2cy26.txt` (16 `[page ]` markers confirmed by grep = 16). Component sweep reproduced below.

| Category | A2 ledger count | My fresh count | Orphan rows (in ledger, absent from A4) | Status |
|---|---|---|---|---|
| Slides / pages | 16 | 16 (grep `^\[page ` = 16) | 0 | MATCH |
| KPI tiles (S5+S6) | 20 | 20 (10 Q2 + 10 H1) | 0 | MATCH |
| Chart datapoints | 91 (59 extractable + 32 NOT_EXTRACTABLE) | 91 — Qtr-trend 24 + bridge 4 + HY-trend 6 + bridge 4 + geo 8 + concentration 8 + ACV 5 = 59; utilization 16 + DSO 16 = 32 ND | 0 | MATCH |
| Table line items | 58 | 58 (S7 2x6=12 + S8 6 + S14 20 + S15 20) | 0 | MATCH |
| Footnotes / adj defs | 17 | 17 (S5:2 S6:2 S7:3 S8:3 S9:1 S14:3 S15:3) | 0 | MATCH |
| Key wins | 5 | 5 | 0 | MATCH |
| Agenda items | 7 | 7 | 0 | MATCH |
| Strategy / award stmts | 8 | 8 | 0 | MATCH |
| Structural / cover-letter | 12 | 12 | 0 | MATCH |
| Capability / award names | 4 | 4 | 0 | MATCH |
| **TOTAL enumerated units** | **238** | **238** (16+20+91+58+17+5+7+8+12+4) | **0** | **MATCH** |

**Orphan-row check (every ledger row cited in A4 OR reviewed-no-finding):**
- KPI tiles / P&L tables → §2 reconciliation R1-R23. Chart series → §3 N1-N6 (quarter trend, both bridges, geography, concentration, ACV). Utilization + DSO (32 ND) → N12 / item 7, explicitly reviewed-as-not-extractable, **treated as ND, NOT estimated** (CLAUDE.md "never estimate a missing number" respected). Key wins → Q13 (TCV open). Strategy/award → N9 + §8B. Cover-letter structural → §6 master-gate date. No orphan row.
- **Missing-from-ledger check (rows my fresh pass found that the ledger lacks):** none. My component sweep equals the ledger exactly.

**Coverage status: PASS.** 238/238 reconcile; zero orphan rows; zero missing rows; 32 not-extractable chart points correctly carried as ND.

---

## 2. ARITHMETIC AUDIT (recomputed from raw extract lines; A4 cites not trusted)

| # | Metric | A4 / overlay value | My recomputation | Source line(s) | Status |
|---|---|---|---|---|---|
| A | Reported Net profit → Cr | ₹555.7M = Rs 55.57 Cr | 555.7 x 0.1 = 55.57 | deck S14 L558; filing L135 | OK |
| B | Reported PAT YoY | −26.7% (R8) | 555.70/758.54 − 1 = −26.74% | deck L558 / L558 (Q2'25 758.5); filing L135 | OK |
| C | Adj Net Profit consistency | ₹628.7M (S14) ≡ ₹629M tile (S5), both ADJUSTED, not 555.7 | 628.7 → 629 (round); PR adj PAT 628.74 (L296) | deck L562 / L153; PR L296 | OK |
| D | Adj EBITDA & margin | ₹1,207.5M / 20.1% | 1,207.5/6,017.0 = 20.068% → 20.1%; PR 20.07% (L280) | deck L545-546; PR L279-280 | OK (rounding) |
| E | Interest expense | ₹94.8M; +342.7% YoY (R5) | 94.77/21.41 − 1 = +342.69% → +342.7% | deck L554; filing L120 | OK |
| F | ETR ladder | 31.0 / 27.0 / 23.5 | Q2'26 249.4/805.1 = 30.98%; Q1'26 242.2/896.3 = 27.02%; Q2'25 233.3/991.8 = 23.52% | deck L556-557 | OK — ladder 23.5→27.0→31.0 confirmed |
| G | TTM ACV level | ~$82.9m | Q2'26 = 82.9 (S11 L440) | deck L440 | OK |
| H | ACV QoQ delta | +0.6 QoQ (vs +5.8 prior) | 82.9 − 82.3 = +0.6; prior 82.3 − 76.5 = +5.8 | deck L440-444 | OK |
| I | ACV vs thresholds | below $88m, above $82m → AMBER | 82.9 < 88 (target) and 82.9 > 82 (stall floor) → between → AMBER; RED (<82) NOT breached | deck L440; Notion thresholds | OK — no RED trigger |
| J | Adj-EBITDA QoQ bridge | Q1 1,157 +98 FX −47 ops → Q2 1,207; "entire QoQ gain is FX, ops fell −47" | Precise ΔAdjEBITDA = 1,207.5 − 1,156.65 = +50.85; bridge +98−47 = +51 (chart-rounded to 1,157/1,207). FX (+98) > total gain; ops −47 | deck L156-166, L545 | OK (deck's own chart rounding; narrative reproduces) |
| K | Adj-EBITDA H1 bridge | H1'25 1,566 +552 FX +247 ops → 2,364; FX ~69% of +798 | Precise ΔAdjEBITDA = 2,364.1 − 1,565.5 = +798.6; 552/(552+247) = 69.1% | deck L193-204, L580 | OK |
| L | Interest coverage (item 8) | EBIT 908.6 / int 94.8 = ~9.6x | 908.6/94.8 = 9.58x | deck L553-554 | OK |
| M | Adj NP QoQ (N8) | (17.1)% ; Q1 adj 758.1 > Q1 rep 654.1 | 628.74/758.10 − 1 = −17.06% → −17.1%; 758.1 > 654.1 | deck L562, L225 | OK |
| N | S-vs-C PAT gaps (YAML) | Q2'26 55.2 / Q1'26 4.0 / H1 22.6 / Q2'25 11.1 / FY25 −6.6 | 197.61/358.09=55.2; 25.22/628.92=4.0; 222.83/987.01=22.6; 75.56/682.98=11.1; −132.56/1994.52=−6.6 | filing L135/L784 | OK |

**Arithmetic status: PASS.** Every material derived metric reproduces within rounding. No A4 computation error above rounding.

---

## 3. ADVERSARIAL READ — three most-positive claims, strongest bear counter each

| Positive claim (overlay) | Strongest bear counter FROM THE SAME EXTRACT | Survives? | Already in overlay? |
|---|---|---|---|
| Adj EBITDA margin 20.1% confirmed → item 4 GREEN | Deck's own QoQ bridge: the +50.85 QoQ gain is 100% FX (+98) while standard operations FELL −47 (L156-166); the 8-qtr series inflects to 20.1% exactly as Novigo consolidated (13-Nov-2025) and the rupee weakened (L136-152) → the margin is FX + inorganic-mix, not organic step | YES | YES — flag 2, N2, item-4 caveat, §8C. **Incorporated.** |
| Adj Net Profit +35.4% YoY (headline tile) | Reported PAT is −26.7% YoY; +35.4% is measured off the NOIDA-stripped base 464.4 and the current 628.7 carries hedge-accounting uplift; the reported decline sits only in appendix S14, never in a tile (L558, L562) | YES | YES — R8, R16, N8, flag 8, §8A. **Incorporated.** |
| TTM ACV disclosed $82.9m (resolves monitoring item 2) | It is decelerating (+0.6 QoQ vs +5.8 prior), below the $88m target, only ~$0.9m above the $82m stall floor; chart y-axis truncated at 68 to magnify the visual climb (L438-450) | YES | YES — N1, item 2 UNKNOWN→AMBER, flag 3. **Incorporated.** |

All three surviving bear counters are already grafted into the overlay. **No surviving, un-incorporated bear counter.**

---

## 4. FOCAL-CLAIM TESTS (the specific items the launching agent flagged)

**(a) Deck-vs-filing reconciliation.** Independently re-derived. 555.7M = 55.57 Cr (OK); 628.7/629 both adjusted, consistent, distinct from reported 555.7 (OK); adj EBITDA 1,207.5/20.1% (OK, 20.07 PR rounds to 20.1); interest 94.8 (OK); ETR ladder 23.5/27.0/31.0 (OK). The task-flagged headline pair (S14 ₹628.7M vs S5 tile ₹629M) IS consistent within rounding, both ADJUSTED — overlay's R15 handling is correct.

**(b) ACV.** ~$82.9m, +0.6 QoQ, below $88m, above $82m → AMBER, RED not breached. Correct.

**(c) FX bridges.** QoQ +98 FX / −47 ops and H1 +552 FX / +247 ops both reproduce (chart values are deck-rounded; precise deltas +50.85 and +798.6 match within rounding). Correct.

**(d) "ZERO CONTRADICTIONS" claim — tested against the three candidate contradictions.**
- Deck OI-net −8.7 vs filing gross OI +13.68 (R14): NOT a contradiction. Both figures already coexist in the **press release** (P&L gross OI 13.68 at PR L178; contribution-analysis OI-net (8.73) at PR L289). The deck's contribution table simply reproduces the PR's contribution format. Reclassification, correctly labelled. **Overlay correct.**
- Adjusted-definition drift (Ind AS 109 hedge): a real disclosure-quality issue, correctly surfaced as flag 6 / Q18 — but it is a management-definition change, not a numeric conflict. **Overlay correct.**
- TTM-vs-quarterly axis switch: none. ACV is labelled TTM throughout; quarter-trend is quarterly. No mislabel. **Overlay correct.**

On the three candidate contradictions the task named, the overlay's "not a contradiction" reads are all correct.

**(e) Master-gate date correction (05-Aug vs ~12-Aug).** SUPPORTED. Deck cover letter (S1) states verbatim: the Investors/Analysts call is "Wednesday, August 05, 2026, at 10:00 AM (IST)" (extract L30-37), per intimation dated 28-Jul-2026. Correction to 05-Aug is anchored to the deck's own Reg 30 letter. Correct.

**(f) Pre-committed thesis-broken triggers — does any deck reading fire one?** Independently checked:
- Organic negative x2: deck silent on organic → unverifiable, not fired. Correct.
- Novigo margin miss >40bps: Novigo actively carved out of ops metrics (S9 L312, "excluding the new acquisition of Novigo") → unverifiable, not confirmed-fired. Correct.
- Blackstone exit <Rs300: no share price in deck → cannot fire. Correct.
- Audit qualification: deck is "Un-audited" (S14 L536) → cannot test. Correct.
**No trigger fires from the deck.** Overlay's §7 conclusion is sound; Decision Status correctly held (analyst flags, human decides).

---

## 5. ONE DISCREPANCY FOUND — deck ₹180.47M vs filing ₹180.42M (immaterial; non-gating)

Independently caught, not one of the task's candidate items:
- Deck slide 7 footnote (extract **L238**): "other income for Q1 2026 was **higher by ₹180.47 million**."
- Results filing states the same Q1 hedge/OCI fair-value change as **₹180.42 million** in three places (extract **L146, L230, L885**); the base review uses 180.42 throughout (review L189, L501).
- The overlay propagates the deck's **180.47** (N8, Q18) and never reconciles it against the reviewed **180.42**.

This is a genuine deck-vs-filing numeric conflict of **Rs 0.05M (~Rs 50,000)** on a ₹180M footnote reference figure — an almost-certain deck transcription typo. It is therefore a narrow counter-example to the overlay's absolute phrasing ("**ZERO CONTRADICTIONS**," "**nothing in the deck disturbs a single Section-A extraction cell**").

**Materiality: nil.** It is a footnote OCI-reference amount, not a P&L line; it changes no revenue, gross margin, EBITDA, PAT, EPS, ACV, ETR, any monitoring item, any pre-committed trigger, or the verdict. It matches none of the four gate-FAIL conditions (no missing brief part; no orphan/missing ledger row; not an A4-derived-metric error — A4 quoted a source figure; not a thesis-changing bear counter).

**Disposition: REQUIRED MINOR GRAFT (non-gating), routed to A4:**
1. Add a reconciliation row: deck ₹180.47M vs filing/PR ₹180.42M — immaterial deck typo, filing figure authoritative.
2. Qualify the absolute "ZERO CONTRADICTIONS / not a single Section-A cell disturbed" wording to "one immaterial deck footnote typo (₹180.47M vs ₹180.42M) aside."
3. (Trivial) §4 item 1 states US$ YoY "+17.8%"; press release states 17.7% (63.56/53.98 − 1 = +17.75%). Align to 17.7%.

These are accuracy refinements to record before save; none alters the analysis, and none rises to a coverage, arithmetic, or surviving-bear-counter FAIL.

---

## VERDICT: **COMPLETE**

- Deliverable brief: all four parts present — PASS.
- Coverage: 238/238 units reconcile against my fresh enumeration; zero orphan rows, zero missing rows; 32 not-extractable chart points carried as ND, never estimated — PASS.
- Arithmetic: every material derived metric (555.7→55.57 Cr; 628.7/629 consistency; 1,207.5/20.1%; interest 94.8/+342.7%; ETR 23.5/27.0/31.0; ACV 82.9/+0.6/<88/>82; FX bridges +98/−47 and +552/+247; S-vs-C gaps) reproduces within rounding — PASS.
- Adversarial: all three positive claims already carry their surviving bear counter; the three task-flagged "candidate contradictions" are correctly non-contradictions; master-gate date 05-Aug is anchored to the deck cover letter; no pre-committed trigger fires — PASS.
- One immaterial deck-vs-filing footnote-typo discrepancy (₹180.47M vs ₹180.42M) recorded as a REQUIRED MINOR GRAFT to A4; it is non-gating (Rs 50k, no decision impact, matches no FAIL condition).

None of the four enumerated gate-FAIL conditions is triggered. The overlay proceeds to Notion save, with the three minor grafts in §5 applied.

```yaml
stage: A5-adversary
company: "RSYSTEMS"
quarter: "Q2CY2026"
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
arithmetic_mismatches: []      # no A4-derived-metric error above rounding
surviving_bear_counters: []    # all three positive claims already carry their counter in the overlay
required_minor_grafts:         # non-gating accuracy corrections routed to A4
  - "Add recon row: deck OCI ref ₹180.47M (deck L238) vs filing ₹180.42M (results L146/L230/L885) — immaterial deck typo; filing authoritative"
  - "Qualify absolute 'ZERO CONTRADICTIONS / not a single Section-A cell disturbed' wording to acknowledge the one immaterial deck footnote typo"
  - "Align §4 item-1 US$ YoY '+17.8%' to press-release 17.7% (63.56/53.98-1 = +17.75%)"
loop_back_to: ""
gap: ""
```
