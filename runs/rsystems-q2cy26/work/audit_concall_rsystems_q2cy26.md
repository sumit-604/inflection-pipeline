# A5 ADVERSARY / COMPLETENESS AUDIT — RSYSTEMS Q2 CY2026 CONCALL OVERLAY
## Fresh-context re-derivation of A4's concall / master-gate-resolution overlay

**Company:** R Systems International (RSYSTEMS) | **Quarter:** Q2 CY2026 | **Call:** 05-Aug-2026
**Under audit:** `review_concall_addendum_rsystems_q2cy26.md` (A4)
**Re-derived from:** concall A1 extract (73 lines), concall A2 ledger, deck A1 extract, results A1 extract
**Model:** claude-opus-4-8 | **Independence:** absolute — every A4 figure and grade re-checked against the transcript AND the deck/filing; A4/A3 cites not trusted blind.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate, run first)

The mandatory PLAIN-LANGUAGE BRIEF (A4 Section 7) — all four parts present and carrying real content:

| Part | Location | Present? | Content check |
|---|---|---|---|
| (1) Summary narrative | 7A DELTA NARRATIVE (13 lines) | **PRESENT** | Real prose; settles-small/dodges-big thesis, gate-fail, HELD, PROCEED WITH FLAGS |
| (2) SECTOR intelligence | 7B (4 bullets) | **PRESENT** | FX-primary-margin-driver, AI-deflation immunity, demand narrative, disclosure gaps — each provenance-tagged |
| (3) BUSINESS-MODEL intelligence | 7C (5 bullets) | **PRESENT** | FX-flattered margin/~18% guide, project-vs-annuity, data+cloud >50%, opaque inorganic engine, cap-structure overhangs |
| (4) COMPETITION intelligence | 7D (4 bullets) | **PRESENT** | Where it wins/is weaker, competitive risks, peer cross-check explicitly NOT performed |

**Result: PASS.** All four brief parts present and non-empty.

---

## AUDIT 1 — COVERAGE (fresh independent enumeration, diffed vs A2 ledger)

Fresh grep/manual re-derivation over the A1 extract (lines 28–100):

| Category | A2 count | My fresh count | Method | Orphan/missing rows | Status |
|---|---|---|---|---|---|
| Turns | 73 | 73 | `sed -n '28,100p' | wc -l` = 73 content lines | none | MATCH |
| Analyst threads | 8 | 8 | "question from the line of" at lines 31,40,49,63,71,80,85,93 | none | MATCH |
| Questions | 21 | 21 | Thread re-tally: Anmul 4 + Ashish 3 + Sep 5 + D 1 + Sonal 2 + Manish 2 + Deepak 3 + Aush 1 = 21 | none | MATCH |
| Mgmt numbers | 73 | 73 (distinct-disclosure basis) | Table D spot-verified against deck/filing | none | MATCH |
| Non-disclosures | 7 | 7 | ND1 GCC% (L36), ND2 data+cloud exact% (L57), ND3 guidance (L36), ND4 H2 ACV (L53), ND5 deal guidance (L69), ND6 Novigo std (L44/89), ND7 organic CC% (L42/81) | none | MATCH |
| Guidance statements | 9 | 9 | G1–G9 (Table E) all located at cited lines | none | MATCH |

**Every ledger row cited or blanket-reviewed by A4:** A4's preamble (line 17) states all 73 turns, all 21 questions, all 73 M-series, Tables A–F reviewed in full; the material rows are individually cited in Steps 1–7 and Section 2. **No orphan row** (ledger row absent from A4). **No missing row** (my fresh pass found nothing the ledger lacks). The 8 MULTI_SPEAKER_TURN merges (lines 30,31,40,43,77,81,91,100) are surfaced by both A2 and A4 as flags, not silently re-counted — correct.

**The 7 non-disclosures are REAL** — I confirmed management genuinely never gave the number in any turn (including the prepared-remarks turn, line 30) for each of the seven. No analyst question was silently dropped: all 21 Table-C questions appear in A4 Section 4A.

**Coverage: PASS.**

---

## AUDIT 2 — ARITHMETIC / FACT (recomputed from raw deck/filing numbers)

Every spoken figure A4 relies on, re-derived from the audited deck (`extract_deck`) and Reg-33 filing (`extract_results`):

| Metric (A4 value) | Recomputed | Source line | Status |
|---|---|---|---|
| Adj EBITDA ₹120.7 Cr / 20.1% (NOT 1,207 Cr; "$12.8bn" garble) | Deck "INR 1,207M ($12.8M)" = 120.7 Cr; 1,207.5/6,017.0 = 20.07% | deck L145/153/539/545 | **CONFIRMED** — 10x ASR unit garble read correctly; billion→million correct |
| Adj EBITDA +51.4% YoY / +4.4% QoQ | 1,207.5/797.4−1 = 51.4%; 1,207.5/1,156.6−1 = 4.40% | deck L219 | **CONFIRMED** |
| Adj PAT ₹62.9 Cr (+35.4% YoY) | Deck 629M ($6.6M); 628.7/464.4−1 = 35.4% | deck L153/225/562 | **CONFIRMED** |
| Adj PAT −17.1% QoQ | 628.7/758.1−1 = −17.06% | deck L225/562 | **CONFIRMED** |
| Reported PAT ₹55.6 Cr | Consol profit 555.70M = 55.57 Cr | results L135/160/288 | **CONFIRMED** |
| Reported PAT −26.7% YoY / −15.0% QoQ | 555.70 vs 758.54 (Q2CY25) = −26.7%; vs 654.14 (Q1) = −15.0% | results L135 | **CONFIRMED** |
| Q1 reported ₹65.4 Cr vs adjusted ₹75.8 Cr | Reported Q1 654.14M = 65.4 Cr; adjusted Q1 758.1M = 75.8 Cr | results L135; deck L562 | **CONFIRMED** — A4 correctly treats M70's "65.4" as reported-vs-adjusted, NOT a garble to be laundered |
| Q1 one-time hedge benefit ~₹18 Cr | Management-stated (line 30); drives the 75.8→62.9 adj-PAT QoQ step | concall L30 | **CONFIRMED** (spoken; not independently re-derivable, correctly left as mgmt-stated) |
| ETR ~31% / normalized 28–29% ("28 to 19 29%" garble) | Base ETR 30.98%; statutory 25.17%; stray "19" digit | concall L30; base | **CONFIRMED** — garble read correctly |
| Forward cover $43.32m @ 93.27 | Management-stated new disclosure | concall L30 (M66) | **CONFIRMED** (spoken; not in deck — correctly tagged NEW) |
| ACV $82.9m vs $82.3m | Deck bridge 82.3 → 82.9 | deck L440 | **CONFIRMED** — decelerating |
| Data + cloud ">50%" | Not in filing/deck; management-stated only | concall L57 | **CONFIRMED as UNVERIFIABLE** — A4 tags it so; exact % declined |
| Sustainable adj-EBITDA "~18%" guide | Spoken "18 18 x%" (trailing digit garbled) | concall L47 (G2/M73) | **CONFIRMED** — kept garbled, not invented (no-estimate rule honoured) |
| FX bridge +98 / standard ops −47 QoQ | Deck: 1,157 +98 −47 = 1,207 | deck L158/159 | **CONFIRMED** |
| H1 adj PAT 11.8%; +54.4% YoY | 1,386.84/11,764.69 = 11.79%; /898.10−1 = 54.4% | deck L580/597 | **CONFIRMED** |
| S-vs-C PAT gap +55.2% (Q2) | (55.57−35.81)/35.81 = 55.2% (SA PAT 358.09M) | results L135/784 | **CONFIRMED** |

**No mismatch above rounding. Every A4 figure reproduces. Arithmetic: PASS.**

**Garble-handling integrity check (task-specific):** A4 did NOT launder any real inconsistency as a garble. The five garbles (1,207-unit; 904.5-digit-drop; "appreciation"→depreciation; "28 to 19 29"; "18-x%") each reconcile to an audited source. The one figure that looked like a garble (M70 Q1 "65.4" vs "75.8") A4 correctly diagnosed as a genuine reported-vs-adjusted definitional pair — both figures are real and independently confirmed in the filing/deck. The "18% QoQ" (line 43) vs "18% YoY" (line 47) tension is correctly read as a verbal slip reconciled to the YoY basis (17.7% USD YoY ≈ 18%; QoQ was only 1.2–4.7%, so 18% cannot be QoQ) — a defensible garble call, not a laundered management contradiction.

---

## AUDIT 3 — ADVERSARIAL READ (five crux calls + three strongest bear counters)

### The five crux calls A4 had to get right

**(1) Did the master gate REALLY not clear, or did A4 overstate the miss?** — **A4 CORRECT, not overstated.**
Re-checked all four legs against verbatim: Organic — no % ever (L43/L81), DODGED. Novigo — no standalone number (L44/L89), DODGED. Margin — answered but candidly negative FX-prop + ~18% sustainable (L47), ANSWERED-negative. ACV — backward high-base explained (L51), forward dodged "million dollar question" (L53), PARTIAL. Scorecard 1 ANSWERED / 1 PARTIAL / 2 DODGED is faithful. Calling it "cleared none of the four legs favourably" is accurate (the one answered leg is a bear tell), not an overstatement.

**(2) Is the "Novigo 3rd-evasion formally tripped" claim correct?** — **A4 CORRECT.**
I swept the entire transcript including the prepared-remarks turn (line 30, where Nand cites "nogo acquisition" only as a qualitative revenue-growth support). No Novigo standalone revenue or margin number appears anywhere — despite two direct probes (Ashish L43, Deepak L88). Third consecutive silence (results filing → deck/press-release → concall) is real; monitoring-item-3 evasion flag genuinely tripped. A4 correctly FLAGS it to Role 1 and does not itself re-grade the promoter.

**(3) Is "margin guided DOWN to ~18%" faithful, or did A4 over-read a hedge?** — **A4 FAITHFUL, not over-read.**
Verbatim L47: "quite a large portion of it also comes from the forex … which we cannot take for granted, beyond our control … we continue to stay focused to stay in that 18-x% adjusted EBITDA on a sustainable basis." The FX-prop concession is explicit; the sustainable number (~18%) is explicitly below the reported 20.1%. A4 kept the trailing digit garbled ("~18%"), did NOT invent a precise figure, and graded it "WEAKENED not broken (18% > 17%)." Corroborated independently by the deck bridge (FX +98 vs standard ops −47). This is the conservative, text-supported reading.

**(4) MOST IMPORTANT — is the Decision-Status call correct?** — **A4 CORRECT on both horns.**
A4 tested all four pre-committed thesis-broken triggers: (a) 2 consecutive quarters organic NEGATIVE — organic claimed positive (L43), un-confirmable but not confirmed-negative → NOT fired; (b) Novigo margin-uplift missed >40 bps — never broken out, UNVERIFIABLE → NOT confirmed-fired (correctly also NOT confirmed-cleared); (c) Blackstone exit signal <₹300 — N.A. on a concall → NOT fired; (d) KMP fraud / audit qualification — audit unmodified → NOT fired. NONE formally fired → status HELD (WATCHLIST/BUY) is correct per CLAUDE.md "Decision Status changes only on a formally-fired pre-committed trigger." Critically, A4 did NOT (i) let the failed gate silently DECIDE a downgrade — it flags, per the flag-don't-decide rule; nor (ii) bury the weakening under a clean PROCEED — the verdict is PROCEED WITH FLAGS with three prominent operator-decision flags (gate failed to confirm; forward evidence weakened; 3rd Novigo evasion). Both failure modes the audit had to catch are absent.

**(5) Is the FTTCP re-engagement-rule evaluation correct?** — **A4 CORRECT.**
Rule = conjunction: 3+ triggers firing favourably AND organic >5%. Organic: no number, implied sub-3-4% (unrebutted analyst "return to 3-4%" framing, L81) → below 5% → NOT met. Favourable triggers: margin (guided down), Novigo (3rd evasion + new geopolitical drag), ACV (decelerating, forward dodged), organic (un-quantified) = 0 of 4 favourable → NOT met. Both conjuncts fail → NO upgrade SMALL-MEDIUM → MEDIUM. Faithful.

### Three most-positive A4 claims — strongest bear counters (completeness device)

| A4 positive claim | Strongest bear counter from the SAME text | Survives / already incorporated? |
|---|---|---|
| "MEASURED & CREDIBLE (provisional), NOT Overpromiser" | Credibility is UNDEFINED (first call, no trailing record); "backward numbers reconcile cleanly" is a low bar since they are already audited; 7 refusals / 0.11 forward specificity reads equally as opacity on the thesis-critical items, not virtue | **Already incorporated** — A4 states credibility is UNDEFINED and names the risk as "information-starvation on the forward axis." No graft needed. |
| "Positive tell on CEO operational depth — CEO fielded all 21 questions" | CEO answering everything while CFO stayed silent and promoter/chairman absent can be a control/opacity signal; "answered all 21" but 10 of the thesis-critical asks were PARTIAL/DODGED — answering ≠ informing | **Already incorporated** — A4 logs MGMT_ABSENCE and explicitly flags that the answered questions are backward/qualitative while the thesis-critical ones are partial/dodged. No graft needed. |
| "Data + cloud crossed 50% supports the strategic-spend/moat narrative" | Management-stated only, exact % declined (ND2), unverifiable; could be inflated by Novigo consolidation/reclassification | **Already incorporated** — A4 tags it UNVERIFIABLE and files NQ22 for the exact %/margin. No graft needed. |

**No bear counter SURVIVES un-incorporated.** A4's review is already symmetric and bear-complete on its own positive claims; nothing must be grafted before save.

---

## VERDICT

**COMPLETE.**

- Deliverable-completeness: PASS (all four brief parts present).
- Coverage: PASS (73 turns / 8 threads / 21 questions / 73 numbers / 7 non-disclosures / 9 guidance — all reconcile; no orphan, no missing row; 7 non-disclosures genuine).
- Arithmetic/fact: PASS (every A4 figure reproduces from the deck/filing to within rounding; garbles correctly reconciled; no laundered inconsistency).
- Adversarial: PASS (all five crux calls faithful; Decision-Status HELD correct with flag-don't-decide honoured on both horns; three strongest bear counters already incorporated).

No loop-back to A2, A3, or A4 required. This overlay may proceed to Notion save.

---

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
arithmetic_mismatches: []
surviving_bear_counters: []
loop_back_to: ""
gap: ""
```
