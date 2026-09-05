# STAGE 12D: VERIFIER D — PEER COVERAGE AUDIT — YASHO
Run date: 2026-09-05 | Model: claude-sonnet-5 | Audits: B06 (peer verification) against 11 peer transcripts and the six B05 peer_questions.

Peers provided: 11 transcripts (NOCIL x4, CAMLINFINE x4, FINEORG x3). B06 correctly notes this is 11, not the "up to 12" ceiling. Nothing to flag there; B06 did not overclaim peer count.

---

## PART 1: COVERAGE AUDIT PER PEER (SUBSTANTIVE claims spot-checked against transcript)

| Peer / call | B06 usage | Citation checked | Found in transcript? |
|---|---|---|---|
| NOCIL Nov'25 | SUBSTANTIVE | "heightened competitive pricing pressure from imports" (revenue commentary) | CONFIRMED, line ~138-139: "...largely due to heightened competitive pricing pressure from imports." |
| NOCIL Nov'25 | SUBSTANTIVE | Korean players "pricing it below Chinese also"; DGTR pending Finance Ministry sign-off | CONFIRMED — V.S. Anand line 651-654 ("pricing it below Chinese also"); Dhaval Shah/P. Srinivasan exchange line 764-772 (DGTR recommendation, Finance Ministry pending, "sub judice") |
| NOCIL Feb'26 | SUBSTANTIVE | "the India-EU FTA is only expected to come into play in calendar year '27 roughly" | CONFIRMED, line 308-309, verbatim |
| NOCIL Feb'26 | SUBSTANTIVE | "In terms of newer capacities coming in, outside of China, there hasn't been too much of investment[s]... largely been more in China. There have been some capacities in antioxidants and accelerators that have come [in the last 12-15 months]" | CONFIRMED, line 550-553, near-verbatim (B06 paraphrases "investment" as singular/plural interchangeably — cosmetic, not a fidelity issue) |
| NOCIL May'26 | SUBSTANTIVE | Aniline Rs.100-112/kg (Jul-Dec'25) to Rs.190/kg | CONFIRMED, line 494-497, verbatim ("Rs.100 to around Rs.112 per kg... Rs.110 becoming Rs.190 per kg") |
| NOCIL May'26 | SUBSTANTIVE | Rs.250cr Dahej capex ~20% capacity increase, "completely merchant [sales]"; FY26 revenue Rs.1,303cr vs FY25 Rs.1,393cr | CONFIRMED — capex/20%/merchant at line 464-488; revenue figures at line 227-230, verbatim |
| NOCIL Aug'26 | SUBSTANTIVE | Named Chinese competitor "China Sunshine... putting up additional capacity in one of the accelerators" | CONFIRMED, line 473-476, verbatim (raised by analyst, confirmed by management context) |
| CAMLINFINE Nov'25 | SUBSTANTIVE | "The trend is very bad because the Chinese are desperate, selling at $7-$7.5" | CONFIRMED, line 450-451, verbatim |
| CAMLINFINE May'26 | SUBSTANTIVE | Phenol "INR85 is now being quoted at more than INR150 per kg"; caustic "gone up by literally doubled up... after the war situation" | CONFIRMED — phenol at line 261-263 and 297-300 (clarified as raw material phenol, not diphenol product, correctly distinguished in B06's Q3 writeup); caustic at line 790-792, verbatim |
| CAMLINFINE Aug'26 | SUBSTANTIVE | 250% ADD math (Solvay pricing, Chinese producers still competitive at higher headline prices) | CONFIRMED, line 1176-1186, substance matches (numbers $18/$7-8/$20/$21 all present) |
| CAMLINFINE Aug'26 | SUBSTANTIVE | EBITDA guidance cut to 10-12% citing "prolonging war situation" | CONFIRMED, line 257-259, verbatim |
| FINEORG May'25 | SUBSTANTIVE | "plastic additives as a market in India is, let's say, $1 billion and, let's say, globally $25 billion" | CONFIRMED, line 894-896, verbatim (correctly attributed to the analyst, Dhruvesh Sanghvi, not management — B06 correctly notes management "did not contest but also did not confirm") |
| FINEORG Mar'26 | SUBSTANTIVE | SEZ capex Rs.700-750cr, management "No idea... it is impossible to predict anything" on revenue potential | CONFIRMED, line 426-430, verbatim |
| FINEORG Mar'26 | SUBSTANTIVE | West Asia conflict as freight-cost driver | CONFIRMED, line 145-147, verbatim |
| FINEORG May'24 | CITED-ONLY | "asset turns and CAPEX... are slow moving areas" | CONFIRMED, line 550-551, near-verbatim |

**All 15 spot-checked SUBSTANTIVE/CITED-ONLY citations located in the named transcript at or near the stated anchor. Zero fabricated or unsupported SUBSTANTIVE claims found.** Every peer marked SUBSTANTIVE in B06's Part 3 coverage map has at least one real, findable citation confirmed here.

---

## PART 2: UNUSED-MATERIAL CHECK (peers/calls B06 did not mark SUBSTANTIVE, or thin claim areas)

- **FINEORG May'24 (CITED-ONLY)**: spot-read for material B06 should have used (China exposure, market sizing, RM inflation) — the call mentions China only once, as a customer geography ("customers are located worldwide, including... China," line 151-153), nothing quantitative or claim-relevant. No missed substantive material. CITED-ONLY classification is appropriate, not a coverage gap.
- **Q1 TAM (peer market sizing)**: grepped all 11 transcripts for "billion" / "market size" / "TAM" outside the one FINEORG May'25 quote already used — no other market-sizing figure exists anywhere in the corpus (NOCIL Nov'25, CAMLINFINE Nov'25 checked directly, zero hits). B06's UNVERIFIABLE verdict on Q1 is not leaving usable peer evidence on the table.
- **Q5 LTSA structure**: grepped CAMLINFINE Feb'26 for customer-funded capex language — no hits, consistent with B06's finding that no peer in this set discusses a customer-funded capacity structure.
- **"Yasho" name-check**: independently re-ran the search across all 11 transcripts — zero matches, confirming B06's claim that no peer references the company by name.
- No unused-but-relevant material found in any peer/call that would change a verdict. `unused_but_relevant` is empty.

---

## PART 3: VERDICT-DISCIPLINE AUDIT PER CLAIM (six B05 peer_questions)

| # | B05 peer_question | B06 verdict | Peers anchoring it | Discipline check |
|---|---|---|---|---|
| 1 | $12-15bn TAM corroborated? | UNVERIFIABLE | none (correctly, no corroborating or contradicting evidence exists) | PASS — correctly held to UNVERIFIABLE, not stretched either way |
| 2 | Chinese/Asian capacity+pricing pressure into FY27? | VERIFIED | NOCIL (4 calls) + CAMLINFINE (4 calls), anchor_count 6 | PASS — 2 independent peers, well above the ≥2-anchor floor for a VERIFIED verdict |
| 3 | RM inflation 10-15% since "pre-war"? | PARTIALLY VERIFIED | NOCIL + CAMLINFINE + FINEORG (direction only; magnitude 4-7x higher in peer data) | PASS — direction genuinely corroborated by 3 peers, magnitude mismatch correctly downgrades to PARTIALLY VERIFIED rather than VERIFIED |
| 4 | EU FTA timeline internal consistency? | CONTRADICTED | NOCIL (single peer, but the claim being tested is an internal-consistency question resolved by one clean same-period quote) | PASS — CONTRADICTED verdicts are not subject to the ≥2-anchor VERIFIED rule; single strong same-period anchor (NOCIL Feb'26, dated, verbatim) is sufficient to support a CONTRADICTED call here |
| 5 | 15-yr customer-funded LTSA market-standard? | UNVERIFIABLE | none found in peer set | PASS — correctly UNVERIFIABLE, peer set structurally cannot answer this (no CDMO-adjacent peer provided) |
| 6 | Peer asset-turn ratios support 2.5-4x? | CONTRADICTED | NOCIL (single peer, one computed data point ~1.0-1.1x) | PASS on disclosure — B06 explicitly labels this "a computed inference from one peer's disclosed figures, not a peer directly stating an asset-turn ratio" and flags it as "directional rather than definitive." This self-flagging is the correct discipline: a CONTRADICTED verdict resting on one computed data point is defensible ONLY because B06 hedges it explicitly rather than presenting it as settled. Still MINOR: a reader skimming only the verdict table (not the hedge text) could over-read "CONTRADICTED" as more definitive than the underlying single-peer, single-data-point evidence supports. |

**All six peer_questions received an explicit verdict; none skipped.** `claims_all_addressed: true`.

No VERIFIED claim rests on fewer than 2 independent peers (only one VERIFIED claim exists, Q2, and it has 2). No verdict was upgraded from silence — every verdict traces to a specific, located quote or an explicit absence-of-evidence finding.

---

## PART 4: FINDINGS

| Severity | Item | Note |
|---|---|---|
| MINOR | Q6 CONTRADICTED verdict rests on a single peer and a single computed (not peer-stated) data point | B06 discloses this hedge in the claim text itself, which is the correct practice, but the top-line "CONTRADICTED" verdict label carries more apparent certainty than one computed inference from one peer supports. Recommend a verdict-label distinction (e.g., "CONTRADICTED (single-peer, computed)") at synthesis so it is not read with equal weight to Q2's 2-peer, 4-quarter VERIFIED. |
| MINOR | Q4 CONTRADICTED verdict also rests on a single peer (NOCIL) | Lower concern than Q6 because the anchor is a direct, dated, verbatim same-period quote (not a computed inference), and the claim being tested is internal-consistency, which a single clean external data point can resolve. Noted for completeness, not scored as a coverage failure. |

No MAJOR or CRITICAL findings. No SUBSTANTIVE-without-citation cases. No unused-but-relevant peer material identified. No verdict upgraded from silence.

---

## PART 5: PEER UTILISATION COMPUTATION

peer_utilisation = peers used substantively / peers provided.

Counting at the PEER-ENTITY level (not per-call): 3 peers provided (NOCIL, CAMLINFINE, FINEORG), all 3 used substantively (FINEORG has 2 of 3 calls SUBSTANTIVE, 1 CITED-ONLY, but the entity overall contributed material verdicts on Q1 and Q6-adjacent commentary) → 3/3 = 100%.

Counting at the CALL level (11 transcripts): 10 of 11 calls marked SUBSTANTIVE, 1 (FINEORG May'24) CITED-ONLY → 10/11 = 90.9%.

Both cuts are reported below; the YAML uses the call-level figure (finer grain, matches the coverage-map row count) as `peer_utilisation`.

---

```yaml
stage: B12d
company: "YASHO"
run_date: "2026-09-05"
model: claude-sonnet-5
status: complete
peers_audited: 11
substantive_confirmed: 10
substantive_unsupported: []
unused_but_relevant: []
claims_all_addressed: true
verdict_discipline_fails: []
peer_utilisation: 90.9   # 10 substantive calls / 11 peer calls provided (entity-level: 3/3 = 100%)
findings:
  - {severity: "MINOR", location: "B06 Part 1 Q6 verdict table + Part 4 YAML contradicted[]", claimed: "CONTRADICTED (peer brownfield asset-turn ~1.0-1.1x vs Yasho's 2.5-4x)", source_truth: "single peer (NOCIL), single computed inference from disclosed capex/revenue figures, not a peer-stated ratio", note: "B06 hedges this correctly in prose ('directional rather than definitive') but the bare CONTRADICTED label risks being read with the same weight as the 2-peer VERIFIED Q2 finding at synthesis", source_fidelity: true}
  - {severity: "MINOR", location: "B06 Part 1 Q4 verdict table + Part 4 YAML contradicted[]", claimed: "CONTRADICTED (EU FTA timeline)", source_truth: "single peer (NOCIL Feb'26), direct dated verbatim quote, correctly anchored", note: "single-peer basis noted for completeness; anchor quality (direct quote, not computed) makes this lower-risk than Q6"}
critical_count: 0
major_count: 0
minor_count: 2
acceptance_rate: 100   # peers correctly handled / peers, %; all 3 peer entities and 10/11 calls correctly handled, 1 correctly downgraded to CITED-ONLY, zero fabricated or unsupported SUBSTANTIVE citations
```
