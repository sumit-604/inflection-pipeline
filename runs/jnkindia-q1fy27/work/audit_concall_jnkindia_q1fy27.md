# A5 ADVERSARY / COMPLETENESS AUDIT — JNK India Limited (JNKINDIA), Q1 FY27 CONCALL (Role 5)

Agent: A5 ADVERSARY | Model: claude-opus-4-8 | Prepared: 2026-08-12
Review under audit: `review_concall_jnkindia_q1fy27.md` (A4, Role 5)
Independence note: I re-derived every figure from the A1 extracts and the A2 ledgers.
I did not defer to A4's or A3's cites; each number below is re-computed or re-located
at its source line. INR Million x0.1 = Cr applied to the results extract throughout.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate, run first)

The MANDATORY PLAIN-LANGUAGE BRIEF is present (review L458-472) with all four labelled
parts non-empty and carrying real content:

| Part | Heading | Present? | Content check |
|---|---|---|---|
| 1 | Summary narrative | **present** | L462-463, ~1 dense paragraph (well over the 10-line floor); states the guidance cut+denial, the 0/5 gate, cash INDETERMINATE, the Chemdist 3.6-vs-1.33 gap, the JNK-Global litigation, the HOLD decision. Real. |
| 2 | Sector intelligence | **present** | L465-466; licensor barrier cutting both ways, >Rs 6,000 Cr pipeline vs 10-12% new-segment win rate, order book −8.2% QoQ, no peer concall in window (stated, not fabricated). Real. |
| 3 | Business-model intelligence | **present** | L468-469; backended revenue, operating ex-OI margins 10.5%/8.8%, WC financed via parent BGs, rev-rec output→input + ~Rs 200 Cr unbilled, un-numbered offshore/Iraq capex. Real. |
| 4 | Competition intelligence | **present** | L471-472; back-to-back export routing through JNK Global vs direct incinerators/flares, 4 analysts pressing the parent, mid-size niche vs L&T, offshore/metals weakness, Thermax precedent, no named peer benchmarks (flagged). Real. |

GATE 0 = **PASS**. No missing or placeholder part.

---

## AUDIT 1 — COVERAGE (independent re-enumeration vs A2 ledgers)

Fresh pass over each extract (turns/participants counted directly off the embedded
1-145 numbering and the named call-in segments; commitments and hedges re-read row by
row) diffed against the three A2 ledgers.

| Category | A2 count | My fresh count | Orphan rows (ledger→A4) | Status |
|---|---|---|---|---|
| Concall turns | 145 | 145 (extract L16-160; embedded 1..145, 2 BLANK + 1 NOT_A_TURN) | none material | PASS |
| Participants | 16 | 16 (11 analysts incl. 1 no-response + moderator + 2 WTD + unnamed IR + SGA) | none | PASS |
| Questions | 44 | reconciled to 44 (13 call-in segments, 11 unique named; method-substituted per A2 Note 4 — I could not falsify the converged count) | none material | PASS |
| Mgmt numbers | 56 | 56 | #31 (70-80% capability overlap) and #45 (4 JNK-Global projects / USA / Petronas Phoenix) not individually restated in A4 — immaterial, subsumed under themes A4 covers | PASS (see note) |
| Forward commitments | 17 | 17 — every one appears in A4's Commitment Register (L395-411) | none | PASS |
| Hedge phrases | 11 | 11 — all reflected in A4 §6C deferral cluster / §3E evasion mapping | none | PASS |
| Results notes / line items / entities | 19 / 85 / 3 | 19 / 85 / 3 (Role 4 baseline; key P&L rows re-derived directly, see Audit 2) | n/a (Role 4 domain) | PASS |
| Presentation slides / footnotes / numbers | 20 / 7 / 247 | 20 / 7 / 247 (Role 4 domain; deck P&L used as arithmetic cross-check) | n/a | PASS |

Rows my fresh pass found that the ledgers lack: **none**. A2 enumeration reproduces.

Non-blocking coverage observations (do NOT fail the gate; no material forensic dropped):
- Mgmt numbers #31 and #45 are within-theme, non-thesis-material, and A4's blanket
  reconciliation preamble plus its thorough JNK-Global-dependency treatment cover the
  substance. Not orphans in the material sense; logged for transparency.
- The A2-flagged analyst garble "$60 million order prospects" (Shubham Burad, turn 41,
  excluded from the 56 as analyst-spoken, `GARBLED_FIGURE`) is not reconciled in A4.
  It is an analyst mis-statement, not a management disclosure; A2 itself only asked for
  a "sanity check." Non-blocking.

Every material A2 concall row is either cited in A4 or subsumed under a theme A4
addresses. **AUDIT 1 = PASS.**

---

## AUDIT 2 — ARITHMETIC (recomputed from raw extracts, not from A4)

All consolidated figures from results extract page 8 (L501-544); standalone from page 4
(L205-238); segment from L599-627; deck cross-checks from presentation L129/177/206-250.

| # | Metric (A4 claim) | A4 value | My recomputation | Source line | Status |
|---|---|---|---|---|---|
| 1 | Consol revenue = Rs 186 Cr | 186.00 | 1,860.00 M x0.1 = **186.00** (total income) | res L503 | MATCH |
| 2 | Consol rev +80.6% YoY | +80.6% | 186.00 / 102.97 = **+80.6%** | res L503 (Q1FY26 1,029.70) | MATCH |
| 3 | Consol reported EBITDA (incl-OI) 21.9 Cr / 11.8% | 21.95 / 11.8% | 146.35+44.35+28.67 = 219.37 M = **21.94 Cr**; /186.00 = **11.79%** | res L516/L510/L511 | MATCH (0.01 Cr rounding) |
| 4 | Consol EBITDA 3.1x | 3.06x | 219.37 / 71.72 (Q1FY26 19.81+36.35+15.56) = **3.06x** | res L514/L510/L511 | MATCH |
| 5 | Consol OPERATING EBITDA ex-OI 8.8% | 15.91 / 8.8% | 219.37 − 60.37 (OI) = 159.00 M = **15.90 Cr**; /179.963 rev = **8.83%** | res L502/L501 | MATCH (0.01 Cr rounding) |
| 6 | Standalone reported EBITDA margin 14.0% | 23.78 / 14.0% | 185.41+34.00+18.36 = 237.77 M = **23.78 Cr**; /170.144 total income = **13.97%** | res L220/L214/L215/L207 | MATCH |
| 7 | Standalone OPERATING EBITDA ex-OI 10.5% | 10.5% | 237.77 − 65.91 (OI) = 171.86 M = **17.19 Cr**; /163.553 rev = **10.51%** | res L206/L205 | MATCH |
| 8 | Consol PAT Rs 9.6 Cr / 5.2% | 9.63 / 5.18% | 96.25 M = **9.625 Cr**; /186.00 = **5.17%** (total-group PAT incl. NCI) | res L521 | MATCH |
| 9 | Consol PAT "+8.5x" spoken — UNRECONCILED | UNRECONCILED (74x consol / 11.6x std) | consol total 96.25/1.27 = **75.8x**; owners 114.67/1.27 = **90x**; std 135.46/11.69 = **11.6x**; **none = 8.5x** | res L521/L531; std L225 | UNRECONCILED — CORRECTLY FLAGGED |
| 10 | "1.1% LY consol PAT margin" is a mislabel | actually standalone 1.14% | consol Q1FY26 0.127/102.97 = **0.12%**; std Q1FY26 1.169/102.71 = **1.14%** | res L521; std L225/L207 | MISLABEL — CORRECTLY FLAGGED |
| 11 | Chemdist 3.6 Cr spoken vs −1.33 segment vs ~1.8 bridge — UNRECONCILED | UNRECONCILED | segment result 13.30 M = **−1.33 Cr**; std→consol EBITDA bridge 23.78−21.94 = **1.84 Cr**; spoken **3.6 Cr** — three bases, gap not closable from disclosure | res L606 | UNRECONCILED — CORRECTLY FLAGGED, NOT silently resolved |
| 12 | Chemdist 8.8% of group revenue | CONFIRMED (16.5/186=8.87%) | deck 16.5/186.0 = **8.87%**; segment rev 16.25/186.0 = 8.74% | deck L129; seg L600 | MATCH (approx, ~8.8%) |
| 13 | Standalone revenue "~170" = total income | 170.14 | 1,701.44 M = **170.14 Cr** (rev-from-ops is 163.55) | res L207/L205 | MATCH — conflation correctly noted |
| 14 | Order book 1,801, −8.2% QoQ | CONFIRMED | deck 1,801 vs 1,961 = **−8.16%** | deck L177/L178 | MATCH |
| 15 | S-vs-C PAT gap Q1FY27 −28.9% | −28.9% | (9.625 − 13.546)/13.546 = **−28.9%** | res L521; std L225 | MATCH |
| 16 | Consol ETR 34.2% | 34.2% | 50.10 / 146.35 = **34.24%** | res L520/L516 | MATCH |
| 17 | NCI absorption −1.84 Cr | −1.84 | 18.42 M = **1.842 Cr** | res L532 | MATCH |

**Arithmetic mismatches above rounding: NONE.** Every derived metric reproduces. The two
"UNRECONCILED" cells (rows 9, 11) and the mislabel (row 10) are correctly characterised
as unreconciled/mislabelled by A4 rather than force-fit — exactly the conservative call.
The spoken 14.0%/11.8% margins are reported-incl-OI and the clean operating figures
(10.5%/8.8%) sit below even the reset 12-14% floor; A4 states this correctly.
**AUDIT 2 = PASS.**

---

## AUDIT 3 — ADVERSARIAL READ (strongest bear counter to A4's three most positive claims)

A4 is already a bearish document; its few genuinely positive claims are stress-tested
below against the same extracted text.

**Positive claim P1 — "the core standalone franchise still looks operationally real
(std PAT 1.17→13.55, core PBT ex-OI positive); thesis intact but not advanced"
(review §8A verdict, L346).**
- Bear counter from the extract: standalone reported EBITDA 14% and PAT 13.55 Cr lean on
  Rs 6.59 Cr other income — that is ~36% of standalone PBT (6.59/18.54, res L206/L220).
  Strip it and operating EBITDA is only 10.5% (row 7 above), below the reset 12-14% floor.
  The "operational reality" is materially other-income-assisted.
- Survives? **No — already grafted.** A4 flags OI-inflation repeatedly (§2B, §7A: "the
  spoken margin embeds Rs 6.04 Cr other income," "the filing wins… materially flattering").
  No new graft required.

**Positive claim P2 — "genuine working-capital comfort (parent posts BGs; Reliance/BPCL
friendly terms; no equity/debt raise 4-6 quarters)" (review 6D/§(c)).**
- Bear counter from the extract: the BG channel runs through JNK Global (turn 61), the
  entity now in activist litigation over board legitimacy (turn 98-99), and management
  itself admitted a BG-limit / non-fund-based enhancement IS needed (turn 139) — so the
  "no raise" headline masks a balance-sheet dependency, and the comfort is exposed to the
  parent dispute.
- Survives? **No — already grafted.** A4 items (a) and (c), flags A3-F6-03 and A3-F7-01,
  state precisely this ("routed through the very parent now in litigation… non-fund
  dependency masked by the no-debt headline"). No new graft required.

**Positive claim P3 — "Chemdist break-even dated to FY27 year-end; 10-15% rev, ~20% GM —
a dated promise to hold management to" (review 6D/§(d)).**
- Bear counter from the extract: Chemdist is loss-making now (spoken 3.6 Cr / segment
  −1.33 Cr), NCI is absorbing −1.84 Cr (a large minority), the Rs 1.72 Cr goodwill is
  untested for impairment on a now-loss-making unit, and the break-even itself is hedged
  ("I'll not be able to give you exact number," turn 71). The "dated promise" is soft.
- Survives? **No — already grafted.** A4 §2C (NCI/goodwill/JV-label), monitorables
  (goodwill test), and open question O5 carry all of it. No new graft required.

**No surviving un-incorporated bear counter.** A4 has already internalised the strongest
bear reads its own positive claims invite. **AUDIT 3 = PASS.**

Non-blocking adversarial observation (recommendation, not a re-open trigger): A4's Part 1
narrative opens on "consolidated revenue rose 80.6%" without an inline reminder that
~9% of Q1FY27 total income is inorganic (Rs 16.5 Cr Chemdist not in the Q1FY26 base,
deck footnote F1 L129) and that revenue-recognition shifted output→input (a pull-forward).
The substance is carried from Role 4 (organic +64.6%, §3E Q12) and the rev-rec change is
flagged in A4 (§5A, monitorables), so it is covered by cross-reference; adding the
"~9% inorganic" clause inline would tighten the brief but is not required for completeness.

---

## TASK-SPECIFIC CONFIRMATIONS (the six items flagged in the assignment)

1. **Two guidance rails as DOWNWARD resets + "no change" verified.** CONFIRMED. A4
   characterises revenue 25-30→20-25% and EBITDA 14-15→12-14% as LOWERED (§2A, §2D, 8A).
   The "no change" denial is verified against transcript turn 119 (extract L134:
   "nothing has changed… It remains the same") and turn 4 ("remains intact" / "maintain");
   the prior 14-15% rail is independently corroborated in-transcript by the analyst at
   turn 118 (L133). The prior 25-30% revenue rail is Notion-sourced [N] and A4 labels it
   as such (MEDIUM confidence) — appropriately sourced, not an extract claim. SOUND.
2. **Spoken-vs-filed arithmetic.** CONFIRMED independently (Audit 2 rows 1-8): 186 / 14.0%
   vs 10.5% / 11.8% vs 8.8% / 9.6 Cr all reproduce from INR Million x0.1.
3. **Chemdist 3.6 vs −1.33.** CONFIRMED the review flags it UNRECONCILED (§2B, §2C, §7A,
   verdict, flags) and routes it to open question O5 — it does NOT silently resolve to
   the smaller disclosed −1.33.
4. **Cash conversion INDETERMINATE + add-back gate 0/5.** CONFIRMED. §8C re-scores the
   five binding conditions to still 0/5 after the concall; cash stays INDETERMINATE; the
   qualitative WC comfort explicitly does NOT resolve deal-breaker #4 (§(c)). Consistent
   with CLAUDE.md (INDETERMINATE cash may not silently resolve to PROCEED; missing
   evidence named = operating CFO, debtor days).
5. **F17 silences.** CONFIRMED all captured: operating CFO (A3-F17-01), debtor days
   (A3-F17-02), permanent CFO not disclosed AND not asked (A3-F17-03) — §5B RED rows,
   §4B "the obvious question not asked," §8C. Three of five gate conditions get no read.
6. **Plain-language brief (4 parts).** CONFIRMED present and non-empty (Audit 0).

Non-blocking wording note: A4's `protocol_verdict` is "PROCEED WITH FLAGS" while the
brief §(c) says the INDETERMINATE cash caps "at PROCEED WITH CAVEATS/FLAGS." CLAUDE.md
names the cap as PROCEED WITH CAVEATS. A4 does name the missing evidence and does not
resolve to a clean PROCEED, so the rule's intent is met; the CAVEATS-vs-FLAGS tier label
is an A4/human-decision matter, not an arithmetic or coverage defect. Logged, non-blocking.

---

## VERDICT

**COMPLETE.** Deliverable gate passes (all four brief parts present and substantive).
Coverage reconciles — A2 enumeration reproduces on a fresh pass, no material orphan row,
nothing my pass found that the ledgers lack. Arithmetic reproduces with zero mismatch
above rounding; the two unreconciled items and one mislabel are correctly flagged rather
than force-fit. No surviving un-incorporated bear counter. The two guidance rails are
correctly read as downward resets denied as "no change," the Chemdist 3.6-vs-1.33 gap is
held UNRECONCILED, cash conversion stays INDETERMINATE, the add-back gate is re-scored
0 of 5, and the F17 silences are all captured. Proceeds to Notion save.

```yaml
stage: A5-adversary
company: "JNKINDIA"
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
