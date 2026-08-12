# A5 ADVERSARY / COMPLETENESS AUDIT — JNK India Limited (JNKINDIA) — Q1 FY27

Agent: A5 ADVERSARY | Model: claude-opus-4-8 | Prepared: 2026-08-12
Independence: fresh context. I re-derived every figure from the A1 extracts and re-ran the A2
enumeration myself; I did not defer to A4's or A3's cites. Inputs seen: A4 review, three A1
extracts, three A2 ledgers. Nothing else.

Verdict preview: **COMPLETE**. Rationale and evidence below.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate, run first)

The mandatory PLAIN-LANGUAGE BRIEF (review L426-444) carries all four labelled parts, each
non-empty with real, quarter-specific content (not placeholders):

| Brief part | Location | Present? | Content check |
|---|---|---|---|
| (1) Summary narrative | Part 1, L430-432 | **present** | ~18-line narrative: std PAT 1.17→13.55, consol below standalone, margins below floor, order book −8.2%, 0/5 gate, HOLD decision. Real. |
| (2) SECTOR intelligence | Part 2, L434-436 | **present** | Refining/petrochem/fertiliser capex cycle, ~Rs 6,000 Cr pipeline, licensor-approval entry barrier, New Labour Codes. Real. |
| (3) BUSINESS-MODEL intelligence | Part 3, L438-440 | **present** | Fired-heater EPC economics, thin operating margins, cash-conversion weak point, Chemdist/charter drift. Real. |
| (4) COMPETITION intelligence | Part 4, L442-444 | **present** | JNK Global dependency (82% book), Thermax precedent, moat-location risk, L&T EPC exposure. Real. |

**Gate result: PASS.** All four parts present and substantive.

---

## AUDIT 1 — COVERAGE (independent re-enumeration vs A2 ledgers, then A2→A4 traceability)

### 1A. Fresh grep/sweep counts vs A2 ledgers vs A4 preamble

| Category | A2 ledger | My fresh count | A4 preamble (L16-18) | Orphan/extra | Status |
|---|---|---|---|---|---|
| Results — notes | 19 (9 std I–IX + 10 consol I–X) | 19 | 19 | none | PASS |
| Results — line items | 85 (6 tables) | 85 (27 std + 33 consol + 19 seg + 3+3 IPO) | 85 | none | PASS |
| Results — agenda items | 4 | 4 (L49,53,58,61) | 4 | none | PASS |
| Results — auditor paras | 10 (4 std + 6 consol) | 10 | 10 | none | PASS |
| Results — entities | 3 | 3 (L400-403) | 3 | none | PASS |
| Results — Annexure-B items | 9 (6 B.1 + 3 B.2) | 9 | 9 | none | PASS |
| Results — SMP profiles | 3 | 3 | 3 | none | PASS |
| Results — signature blocks | 8 | 8 | 8 | none | PASS |
| Press release — content blocks | 29 | 29 | 29 | none | PASS |
| Press release — numeric tokens | 130 | 130 (re-verified sweep) | 130 | none | PASS |
| Press release — table rows | 5 | 5 | 5 | none | PASS |
| Press release — footnotes | 3 | 3 | 3 | none | PASS |
| Press release — named items | 16 | 16 | 16 | none | PASS |
| Presentation — slides | 20 (over 21 pp) | 20 | 20 | none | PASS |
| Presentation — numeric tokens | 247 | 247 | 247 | none | PASS |
| Presentation — P&L line items | 36 (18 consol + 18 std) | 36 | 36 | none | PASS |
| Presentation — footnotes | 7 | 7 | 7 | none | PASS |

No count my fresh pass found is missing from the ledger (nothing to return to A2). No ledger count
is absent from A4's preamble.

### 1B. Ledger-flag → A4 traceability (every flagged row cited or reviewed-no-finding)

| A2 flag (source) | Reflected in A4? | Where |
|---|---|---|
| ZERO_STANDING x4 (Exceptional/reclassified items) | Yes | Step 4 L209 "Exceptional items 0.00 nil all periods (L515)" |
| RESTATEMENT x2 (FY26 EPS 11.56→11.59 / 11.57→11.61) | Yes | Step 0C L33; Notes table L45 |
| BUSINESS_COMBINATION + COMPARABILITY (Chemdist) | Yes | Notes table L47; S-vs-C section; Q2/Q3 |
| NEW_SEGMENT x4 (Process Equipment) | Yes (rev/result/assets) | Step 5 L233-235; 6D T5; Q2 |
| NCI_PRESENT x4 | Yes | Steps 1B/2B/4; S-vs-C table |
| NEW_LINE_OF_BUSINESS x4 (MOA pivot) | Yes | 6D; Monitorables; Q8 |
| NO_QUANTUM (un-numbered capex) | Yes | 8B; Monitorables; Q8 |
| SMP_DESIGNATION_ENDED / no CFO | Yes | 6B cond 4; Q7; Monitorables |
| UNAUDITED_BY_PRINCIPAL_AUDITOR (Rs 0.29 Cr inc / 0.07 Cr loss) | Yes | Auditor opinion L50 (figures re-verified below) |
| EOM/OTHER_MATTERS/GOING_CONCERN_ABSENT | Yes | Auditor opinion L50 |
| NUMBER_MISMATCH (10.30 vs 103.0) | Yes | Q13 L353 "Rs 10.30 cr decimal error" |
| STRUCTURAL_BLANK / PARTIAL_YOY_DISCLOSURE | Yes | F-09 / Q11 |
| HEADLINE_QUALIFIER (EBITDA incl OI) | Yes | central 11.8%-vs-operating thread |
| COMPARABILITY_CAVEAT (16.5 Chemdist) | Yes | diagnostic 1 organic +64.6% |
| EPS_PAT_SIGN_INCONSISTENCY (deck PAT −0.8 vs EPS 2.42) | Yes | Critical Extraction Correction L131; Q1 |
| DROPPED_SLIDE_RISK (cash flow / balance sheet / order-book split) | Yes | Step 5; F-11; Q5 |
| BSE 544220 masthead error | Yes | 6C; Q13; flags |
| Cancelled export order 8-Jun-2026 | Yes | 6B cond 5; 6D T4; Q6 |

**Two immaterial ledger flags not separately narrated by A4 (reviewed-no-finding, NOT orphans):**
1. `DISCREPANCY_VS_STANDALONE` (results ledger §8): IPO Working-Capital "proposed" prints 2,626.90
   standalone (L290) vs 2,620.00 consolidated (L658). Both reconcile to the same Total 2,797.39 and
   the same "fully utilised / nil unutilised" outcome A4 reports (L43). A2 itself labelled it "very
   likely a single OCR digit-swap … flagged … to check against the source PDF." A4 cannot re-open a
   source PDF; the analytic conclusion (fully utilised, nil unutilised) is unaffected either way.
   Immaterial — not a coverage FAIL.
2. `SIGNATURE_AFTER_HOURS` (presentation ledger C-block, 23:50:07 IST deck filing): A2 raised this
   only "for pattern tracking across quarters," not as a this-quarter defect (no board-timing
   conflict, unlike the results filing where A2 confirmed no pre-conclusion timestamps). A4 raised
   the substantive governance signals (standalone misstatement, BSE code, decimal error). The
   late-filing timestamp is immaterial to the Q1 thesis. Not a coverage FAIL.

A4's blanket "All ledger rows reviewed: TRUE. No unreviewed rows" (L21) is corroborated: every
material flag is substantively cited; the only two not narrated are immaterial and self-cancelling.
Segment-liability rows (L623-627) are enumerated data with no distinct flag beyond NEW_SEGMENT,
which A4 addresses via segment revenue/result/assets — acceptable.

**Coverage result: PASS. No orphan rows. No missing-from-ledger rows.**

---

## AUDIT 2 — ARITHMETIC (recomputed from raw extract; A4 value vs my value vs source line)

All figures INR Million x0.1 → Rs Cr. Source lines are in `extract_results` unless noted.

| Metric | A4 value | My recompute | Source line(s) | Status |
|---|---|---|---|---|
| Standalone PAT Q1FY27 | 13.55 | 135.46M→13.55 | L225 | MATCH |
| Consolidated PAT total Q1FY27 | 9.63 | 96.25M→9.63 | L521 | MATCH |
| Consol owners / NCI | 11.47 / (1.84) | 114.67M→11.47 / (18.42M)→(1.84) | L531/L532 | MATCH (11.47−1.84=9.63) |
| **Deck standalone PAT claim −0.8** | misstated; filing +13.55 | Deck opex 135.9 = consol COGS 83.46+4.89+47.56=135.91; true std COGS 76.64+0.53+45.47=122.64 | deck L234 vs L506-508 / L210-212 | **MATCH — misstatement confirmed** |
| Std Operating EBITDA Q1FY27 | 17.19 | 18.54+1.84+3.40−6.59=17.19 | L220/215/214/206 | MATCH |
| **Std Op EBITDA margin** | 10.5% | 17.19/163.55=10.51% | L205 | MATCH |
| Consol Operating EBITDA Q1FY27 | 15.91 | 14.64+2.87+4.44−6.04=15.91 | L516/511/510/502 | MATCH |
| **Consol Op EBITDA margin** | 8.8% | 15.91/179.96=8.84% | L501 | MATCH |
| Consol Reported EBITDA (incl OI) | 21.95 | 14.64+2.87+4.44=21.95 | L516/511/510 | MATCH |
| **Consol reported margin (11.8% framing)** | 11.8% | 21.95/186.00=11.80% | L503 | MATCH — confirms 11.8% is incl-OI, 8.8% operating |
| Std reported EBITDA margin | 14.0% | 23.78/170.14=13.98% | L207 | MATCH |
| Std ETR Q1FY27 | 27.0% | 5.00/18.54=26.97% | L224/L220 | MATCH |
| Consol ETR Q1FY27 | 34.2% | 5.01/14.64=34.22% | L520/L516 | MATCH |
| Consol current tax = std | 5.55 both | 55.49M=55.49M | L518=L222 | MATCH (ETR explanation sound) |
| Std revenue YoY | +65.5% | 163.55/98.83−1=65.5% | L205 | MATCH |
| Consol revenue YoY | +81.6% | 179.96/99.10−1=81.6% | L501 | MATCH |
| Organic total income YoY | +64.6% | (186.0−16.5)/103.0−1=64.6% | deck F1 / L503 | MATCH |
| Core PBT ex-OI swing (std) | (1.85)→11.95 = +13.80 | 2.03−3.88 / 18.54−6.59 | L220/L206 | MATCH |
| Core PBT ex-OI swing (consol) | (1.89)→8.60 = +10.49 | 1.98−3.87 / 14.64−6.04 | L516/L502 | MATCH |
| **S-vs-C PAT gap Q1FY27** | −3.92 / −28.9% | 9.63−13.55=−3.92; /13.55=−28.9% | L521/L225 | MATCH |
| S-vs-C gap Q4FY26 / Q1FY26 / FY26 | +4.4% / −88.9% / −0.1% | +4.36 / −88.9 / −0.08% | L521/L225 | MATCH |
| **Order book QoQ** | −8.2% | 1,801/1,961−1=−8.16% | deck L177-178 | MATCH |
| Chemdist segment loss Q1FY27 | −1.33 | (13.30M)→(1.33) | L606 | MATCH |
| Chemdist segment rev Q1→halved | 35.29→16.25 | 352.87M / 162.53M | L600 | MATCH |
| Process seg assets QoQ | 113.99→99.68 (−14.3) | 1,139.86M / 996.79M | L617 | MATCH |
| Combustion seg assets YoY | 700.93→934.93 (+234) | 7,009.30M / 9,349.27M | L616 | MATCH |
| Goodwill / consideration / DTA | 1.72 / 41.58 / 0.71 | 17.19M / 415.82M / 7.07M | L678 | MATCH |
| Other-Matters subs inc / loss | 0.29 / 0.07 (0.7% of PAT) | 2.87M→0.29 / 0.69M→0.07; 0.069/9.63=0.72% | L437 | MATCH |
| New Labour Codes (std) | 0.92 | 9.22M→0.92 | L298 | MATCH |
| IPO proceeds utilised | 281.70, fully | 2,816.99M→281.70, nil unutilised | L293-294 | MATCH |
| Share count / EPS tie | 5.595 Cr sh; 2.42 / 2.05 | 111.91M/2=55.955M; 13.55/5.595=2.42; 11.47/5.595=2.05 | L539/L237/L543 | MATCH |
| PAT bridge components | +10.48 op / +2.17 OI / (1.31) D / (0.80) FC / (4.16) tax | Rev+80.86 vs Exp+70.38; 6.04−3.87; 2.87−1.56; 4.44−3.64; 5.01−0.85 | L501/513/502/511/510/520 | MATCH |
| Q4FY26 consol revenue OCR correction | 338.44 (printed 238440) | segment total L601 3,384.40M = 3,031.53+352.87 | L601/599/600 | MATCH — correction justified |

**Arithmetic result: PASS. Zero mismatches above rounding across the entire review.**

Focus-item confirmations demanded by the task:
- (1) Standalone PAT +13.55 (L225) vs consolidated +9.63 (L521) reconcile; deck standalone P&L is
  provably misstated (consolidated opex 135.9 applied to standalone income) — **A4 correct.**
- (2) Operating EBITDA std 10.5% / consol 8.8% vs the 11.8% reported-incl-OI framing — all three
  recompute exactly; A4's separation of operating vs reported is correct — **A4 correct.**
- (3) Order-book −8.2% QoQ recomputes to −8.16% — **A4 correct.**
- (4) Cash conversion held INDETERMINATE; no CFO/balance sheet this quarter (Q1 not Reg-33-
  mandatory); deck dropped the cash-flow slide. A4 did **not** resolve it to PROCEED — it names the
  missing evidence (operating CFO, debtor days) and caps at PROCEED WITH CAVEATS at best (Step 5
  L239), issuing the more-conservative PROCEED WITH FLAGS. **House rule respected.** (Note: the
  Step-5 "caps at CAVEATS" wording and the YAML "PROCEED WITH FLAGS" are coherent — FLAGS is the
  more conservative outcome, and the position result is HOLD / no-add / no-exit. Not a violation.)
- (5) Add-back gate scored **0 of 5** — two indeterminate (CFO, debtor days), one fails on the
  anchored margin (<13% every basis; consol operating <10% kill), two clearly fail (no permanent
  CFO in Annexure C; export order cancelled, no Dangote). Independently re-verified — **A4 correct.**

---

## AUDIT 3 — ADVERSARIAL READ (three most-positive claims; strongest bear from the same text)

**Positive claim 1 (review L148/L150/L432):** "The standalone franchise turned genuinely
operational — PAT 1.17→13.55 (+1058%, ~11.6x), core PBT ex-OI swung (1.85)→+11.95."
*Strongest bear from the same extract:* the 11.6x is off a near-breakeven base where core PBT ex-OI
was itself negative, and Q1 is the seasonal trough — Q4FY26 standalone PAT was 31.66 (L225), so
13.55 is <43% of the immediately prior quarter; Other Income (6.59, L206) still supplies 35.5% of
PBT.
*Survives?* **No.** A4 already grafts every leg: "off a thin base" (L143/L150), Q1-trough seasonality
(Step 3), and OI/PBT 35.5% with the ex-OI decomposition (diagnostic 3/6). Already incorporated.

**Positive claim 2 (review L157/L170):** "Revenue +81.6% consolidated / +65.5% standalone; organic
+64.6% — strong growth."
*Strongest bear from the same extract:* forward visibility is deteriorating even as trailing revenue
looks strong — order book −8.2% QoQ to 1,801 (deck L177-178), Q1 inflow omitted (deck F-10), a
large export order cancelled 8-Jun-2026 on licensor approval (deck F4 L179-184), and ~9% of the
growth is the loss-making Chemdist slice (16.5, deck F1).
*Survives?* **No.** A4 carries all four: order book −8.2% (6D T3, flags), inflow omission (Q5),
cancellation (6B cond 5 / 6D T4 / Q6), Chemdist inorganic-and-dilutive (S-vs-C section). Already
incorporated.

**Positive claim 3 (review L143/L171/L432):** "Margins improved materially YoY (+7.1pp std, +5.5pp
consol); company reports 11.8%."
*Strongest bear from the same extract:* on the operating (ex-OI) basis the consolidated margin is
8.8% — **below the 10% kill line** — and even the reported 11.8% decelerated 340bps QoQ from 15.2%
(deck C8); every basis is below the 13% floor.
*Survives?* **No.** A4 leads with exactly this: consol operating below kill (6C T2 FLAG), QoQ
deceleration 15.2%→11.8% (Step 3, 6D T2), below floor on all bases (diagnostic 2). Already
incorporated.

**No surviving bear counter requires grafting into A4.** The review is already symmetric bull-bear
on all three positives, consistent with its conservative posture.

---

## VERDICT

**COMPLETE.**

- Deliverable gate: PASS (all four brief parts present, substantive).
- Coverage: PASS (17/17 category counts reconcile to my fresh pass; every material ledger flag cited
  in A4; two immaterial flags reviewed-no-finding; no orphan rows, nothing missing from the ledger).
- Arithmetic: PASS (every derived metric recomputed from raw lines; zero mismatches above rounding;
  all five task-focus items independently confirmed — standalone-vs-consolidated PAT reconciliation,
  the deck-misstatement diagnosis, 10.5%/8.8% vs 11.8%, order-book −8.2% QoQ, cash conversion held
  INDETERMINATE and not resolved to PROCEED, add-back gate 0 of 5).
- Adversarial read: PASS (the three strongest bear counters are already incorporated; none survives
  unaddressed).

No loop-back required. This review may proceed to the Notion save.

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
