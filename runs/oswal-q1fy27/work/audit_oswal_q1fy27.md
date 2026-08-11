# A5 ADVERSARY / COMPLETENESS AUDIT — Oswal Pumps Ltd (OSWAL) — Q1 FY27

Auditor: A5 (fresh context). Inputs re-derived independently from the A1 extract
(source lines 6-150), the A2 ledger, and the A3 forensics; A4's cites were checked,
not trusted. Doctype: ONE concall (no Reg 33 filing, no PPT).

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate)

PLAIN-LANGUAGE BRIEF present at review L497. All four labelled parts present and
carry real, non-placeholder content:

| Brief part | Location | Present? | Note |
|---|---|---|---|
| (1) Summary narrative | L499-500 | PRESENT | ~20 sentences of substantive content, this-quarter + meaning, symmetric bull (L500 "promoter on the call... backward integration advancing") and bear (L500 "entire FY27 growth rests on PM Surya Ghar... near-zero base"). Physically one dense paragraph rather than 10-20 discrete lines, but content-complete; passes. |
| (2) SECTOR intelligence | L502-503 | PRESENT | Real: B2G policy sector, PM-KUSUM 2.0 delay, single-state crowding, install-history 1.5/3.5/5 lakh, govt slow-pay; Notion RESCO/Bihar context flagged as provenance. |
| (3) BUSINESS-MODEL intelligence | L505-506 | PRESENT | Real: backward-integration margin defence, unit economics (43k vs 56k volume), multi-vertical drift, cash-conversion weak point. |
| (4) COMPETITION intelligence | L508-509 | PRESENT | Real: more players on rising volumes, backward-integration edge, commoditized single-state tender exposure, not information-leader on PM-KUSUM 2.0. |

GATE 0: PASS.

---

## AUDIT 1 — COVERAGE (independent re-enumeration vs ledger)

Fresh grep pass over the extract:
- Round-announcement phrases ("...क्वेश्चन इज़ फ्रॉम..." / "फर्स्ट/नेक्स्ट क्वेश्चन") returned
  9 hits mapping to source lines 11,25,59,65,66,83,91,108,145 — identical to the
  ledger's 9 question rounds (7 delivered, 1 audio-drop L59-65, 1 operator skip L65).
- Turn universe: source lines 6-150 = 145 content turns; matches ledger and A4 preamble.
- Management-number table spot-checked line-by-line against extract text (L9, L10, L67,
  L112, L129, L132, L103): every figure A4 cites is physically present in the extract at
  the cited line. No orphan/fabricated number.

| Category | A2 count | My fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Turns (lines 6-150) | 145 | 145 | none | PASS |
| Question rounds | 9 | 9 (L11/25/59/65/66/83/91/108/145) | none | PASS |
| Consolidated sub-questions | 28 (+1 repeat) | 28 reproduced in A4 Step 4A | none | PASS |
| Mgmt-spoken numbers | 30 (of 53 digit universe) | 30 traced to extract; 23 excluded reasons hold | none | PASS |
| ASR-ambiguity register | 14 | 14 carried unresolved in A4 (preamble + tables) | none | PASS |
| Participants | 12 | 12 (Step 0B / Table 1) | none | PASS |
| Commitment register | C1-C13 | 13 carried in A4 Step 3 baseline | none | PASS |
| A3 findings FND-01..11 | 11 | 11 all carried (see below) | none | PASS |

Finding-carry check (each FND traced into A4 and, where routed, into a Questions row):
- FND-01 FORWARD-SIGNAL → carried (L272/L252) + Q6. OK
- FND-02 FORWARD-SIGNAL → carried (L276/278) + Q8. OK
- FND-03 FORWARD-SIGNAL → carried (guidance table/Exchange 2) + Q6. OK
- FND-04 AMBIGUOUS → carried (L120) + Q7. OK
- FND-05 AMBIGUOUS → carried (L277) + Q2. OK
- FND-06 CONFIRMATORY-NEGATIVE → carried (L104/244/273), feeds scorecard. OK
- FND-07 AMBIGUOUS → carried (L106/349) + Q5. OK
- FND-08 AMBIGUOUS → carried (L49/291) + Q1. OK
- FND-09 CONFIRMATORY-NEGATIVE → carried (L274/398), feeds cash/Gate 1. OK
- FND-10 AMBIGUOUS → carried (silence table) + Q2/Q3/Q10. OK
- FND-11 AMBIGUOUS → carried (L131/440) + Q4/Q9. OK

Routing rule satisfied: all 3 FORWARD-SIGNAL and all 6 AMBIGUOUS findings each produce
at least one management-question row; the 2 CONFIRMATORY-NEGATIVE feed scorecard/cash
without a question, as specified. No orphan ledger row; no row my pass found that the
ledger lacks.

COVERAGE: PASS.

---

## AUDIT 2 — ARITHMETIC (recomputed from raw extract numbers)

| Metric | A4 value | My recompute | Source line | Status |
|---|---|---|---|---|
| Volume YoY | -23.2% | (43,000-56,000)/56,000 = -23.21% | L43/L50 | MATCH |
| Volume QoQ | -2.3% | (43,000-44,000)/44,000 = -2.27% | L43/L49 | MATCH |
| Revenue-vs-volume QoQ gap | ~4.8pp | 7.1 - 2.3 = 4.8pp | L9/L43/L49 | MATCH |
| FY27 incremental rev (20-25% on 2,064) | ~413-516 Cr | 2,064x0.20=412.8; x0.25=516 | L140 (Notion base) | MATCH |
| Analyst incremental (25% on 2,000) | ~500 Cr | 2,000x0.25=500 | L121/L125 | MATCH |
| Specificity ratio | 0.68 | 17/25 = 0.68 | L318 | MATCH |
| Q&A grade tally (28 numbered) | A8 / B14 / C6 | A8, B14, C5+ (row22 "B/C") -> C6 | Step 4A | MATCH (row22 assigned to C; sums 28) |
| Q&A share of turns | ~94% | 137/145 (L11-147) = 94.5% | L59 | MATCH |
| Hedge count | 9 | Ledger Table 5 = 9 hedges | L323 | MATCH |
| Margin bridge net | ~7.9% | management-stated at L67 (not A4-derived) | L67 | MATCH (reproduced) |

Management-stated ratios reproduced by A4 (NOT A4 computations, so not scored as A4
errors, but noted for the record): reported EBITDA margin 17.1% (82/474 = 17.30%),
operating EBITDA margin 15.7% (74/474 = 15.61%), PAT margin 11.2% (54/474 = 11.39%).
A4 correctly reproduces management's spoken figures verbatim and labels them as
source-anchored rather than recomputing/estimating them; per the NEVER-estimate rule
this is the correct handling of ASR-anchored disclosure. No A4-derived metric deviates
above rounding.

Filing-only arithmetic (CoM, employee, finance, depreciation, tax, EPS, SC-gap,
YoY/QoQ filing bridge, PAT bridge, ETR) is correctly declared ND / N.A. — no fabricated
filing number found anywhere in the review. SC-gap PAT% recorded as ND (F2 N.A.), not zero.

ARITHMETIC: PASS.

---

## AUDIT 3 — ADVERSARIAL READ (three most-positive claims, strongest bear from same text)

1. CLAIM (L47/L326): "Promoter present and answered directly — positive candour."
   BEAR (same text): the promoter fielded nearly all financial/cash/strategy questions
   while the newly-presenting CFO's audible footprint is essentially opening L10 only;
   candour clusters on backward/operational facts (A-grades) and coincides with silence
   on CFO succession, segment ROCE, and cash (L92-93, FND-08/10). SURVIVES? — Already
   grafted by A4 at L330 ("a promoter answering nearly all financial questions while a
   newly-presenting CFO stays quiet is a mild governance-depth flag, compounding FND-08").
   No new graft required.

2. CLAIM (L371/L373): capacity/backward-integration "ON TRACK" — module 1 GW operational,
   inverter advancing.
   BEAR (same text): the inverter is prototype-stage with field trials still ~2 months
   out and "production within 6 months" (L76, LOW confidence in A4's own table L127);
   the 1 GW is "operational" but commercial production has NOT started (Sep-26) and
   management itself hedged a "2-4 month monsoon slippage" (L85). SURVIVES? — Already
   grafted: A4 marks the trigger "ON TRACK but UNPROVEN" (L373), archetype treatment
   "treat all forward guidance as promotional until Q2 delivers on C2/C4" (L335), and the
   monsoon-slippage hedge is logged (L459). No new graft required.

3. CLAIM (L118/L370): FY27 "20-25% growth, clear visibility."
   BEAR (same text): the number rests entirely on PM Surya Ghar, which was ~nil in Q1
   (L129) and must ramp to Rs 800-1,000 Cr in H2 (L103/L132), a figure LARGER than the
   ~Rs 500 Cr total incremental growth — internally inconsistent unless core pumps shrink;
   the analyst named the "disconnect" (L123) and management did not reconcile it (L126-133).
   SURVIVES? — Already grafted: Exchange 2 (L247-253), guidance internal-consistency
   TENSION (L140), FND-01 carry, and flag L560. No new graft required.

All three strongest bear counters are already present in A4's review. No surviving,
un-incorporated bear counter requires grafting.

ADVERSARIAL: PASS (no additions owed).

---

## INTERNAL-CONSISTENCY / HOUSE-RULE CHECKS

- Cash conversion INDETERMINATE: A4 holds it INDETERMINATE (L24/YAML), never silently
  resolves to PROCEED, names the missing evidence (H1 CFO/PAT, committed exit-DSO,
  Rs collected in Q1 — Q4/Q9). Protocol verdict "PROCEED WITH FLAGS" is at least as
  conservative as the "caps at PROCEED WITH CAVEATS" ceiling (FLAGS sits below CAVEATS
  in cleanliness), and the numerous independent flags (governance, 3/4 hard-stop legs,
  guidance inconsistency, order-book disclosure) legitimately justify FLAGS over CAVEATS.
  Consistent with the CLAUDE.md rule set. No mechanical failure exists (GATE A2/A3 PASS),
  so no halt/REWORK is warranted; company-quality issues propagate as flags. CONSISTENT.
- Decision Status: verified WATCHLIST before framing; branch 8A-W; no HOLD/TRIM/EXIT
  language; A4 flags only, human decides; cash multiplier held 0.65x (not upgraded).
  Exit-PE / pillar revisions correctly deferred to FTTCP (sole authority). CONSISTENT.
- Exit multiple: none invented; destination PE 16-20x carried from Notion, recompute
  deferred to FTTCP with the filing. No round-number default introduced. CONSISTENT.
- Role 4 filing steps: all declared N.A., every filing-only line item ND, no fabrication.
  CONSISTENT.

---

## VERDICT

COMPLETE. All four brief parts present with real content; independent re-enumeration
matches the ledger (145 turns / 9 rounds / 28 sub-questions / 30 mgmt numbers / 14 ASR
items) with zero orphan rows; every A3 finding FND-01..11 carried with correct routing;
every derived metric recomputes within rounding; no fabricated filing number; the three
strongest bear counters are already incorporated; cash-conversion INDETERMINATE and the
PROCEED WITH FLAGS verdict are internally consistent with the house rule set. Proceeds to
Notion save.

```yaml
stage: A5-adversary
company: "OSWAL"
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
