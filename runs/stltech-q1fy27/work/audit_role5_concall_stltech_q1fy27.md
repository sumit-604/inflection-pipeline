# A5 ADVERSARY / COMPLETENESS AUDIT — STLTECH Q1FY27 (Role 5 concall review)
# RE-AUDIT (loop 2). Prior INCOMPLETE gap: attach-rate acceleration recorded by A4 as a positive only.
# Fresh context: A4 review + A1 extracts + A2 ledgers only. Every figure re-derived from the extracts.
# Auditor: A5 (Opus 4.8) | 2026-07-25

---

## 0. RE-AUDIT FOCUS ITEM — is the attach-rate bear counter now genuinely grafted?

Prior loop returned INCOMPLETE because the attach-rate guide (16% -> >20% next quarter -> 25% by
Q4FY27) is a 4x-9x acceleration off the demonstrated +1pp/yr pace, and A4 had logged it only as a
clean positive. I re-derived the pace and the graft locations independently.

**Pace re-derivation (from the extract, not A4's cite):** file line 39 (turn 11, internal src#26):
"our attach rates have increased to 16% ... compared to 15% last year ... increasing our attach rate
to above 20% from next quarter onwards and to 25% by the end of this financial year." So:
- Demonstrated: 15% -> 16% = **+1pp over one year.**
- Next quarter target: 16% -> >20% = **+4pp in one quarter** (= 4x the annual pp gain).
- Q4FY27 target: 16% -> 25% = **+9pp** (= 9x the annual pp gain).
- Restated 25%/Q4 at file line 107 (turn 44) and file line 165 (turn 73); the 23%-margin dependency
  is stated at turn 73 ("as we increase our connectivity attach rate ... going up to 25% by quarter 4
  that will further enable our EBITDA margin ... 23%"). A4's "4x-9x acceleration, no mechanism" framing
  is arithmetically sound and conservative (it compares pp-to-pp; a per-quarter framing would be harsher).

**Graft-location check (task's required four sites + spread):**

| Required site | Present? | A4 location | Cites checked |
|---|---|---|---|
| Step 6D | YES | 6D "Attach-rate dated target — RECLASSIFIED ... to a STRETCH" | L39/turn11/row35; +4pp rows 36-37; +9pp rows 37/81/89; t73 margin-leg — all verify |
| Step 8B (#5 / row 5b) | YES | 8B row **5b** "Attach-rate walk ... a named leg of the 23% margin guide" | rows 35-37; L39/L107; 6D — verify |
| Flags list | YES | flag "ATTACH-RATE STRETCH: guide needs +4pp next quarter ... +9pp by Q4 ... = 4x-9x ... NO quantified mechanism" | L39; 6D; rows 35-37 — verify |
| Question-for-Management row | YES | 8F row **N5b** "Reconcile the demonstrated attach-rate pace of +1pp/yr (15%->16%, L39) with the guide ..." | L39 — verify |

Additionally grafted (beyond the required four): Step 2 guidance table (attach row, confidence
LOW-MEDIUM, "demonstrated pace only +1pp/yr; guide needs +4pp in one quarter, +9pp by Q4"); Step 2
"internally consistent arithmetic" diagnostic (THIRD consistency question); Step 3C pattern; Step 5B
silence table (acceleration mechanism un-pushed); Step 6E archetype (OVERPROMISER-drift REINFORCED);
Section C combined verdict; monitorables; YAML `attach_rate_stretch` field; header note line 14.

**Verdict on the re-audit item: the prior gap is CLOSED.** The attach-rate acceleration is now
treated as a credibility-tested STRETCH / direct risk to the 23% margin leg, present in all four
required sites plus the verdict and YAML, with load-bearing cites (L39, ledger rows 35-37/81/89) that
all reconcile to the extract.

---

## 1. COVERAGE AUDIT (independent re-enumeration of the concall extract vs the A2 ledger)

| Category | A2 count | My fresh count | Orphan / missing rows | Status |
|---|---|---|---|---|
| Participants (speakers taking a numbered turn) | 15 | 15 (3 mgmt: Darak/Tagral/Janjari + 12 analysts; operator tracked as call-admin role) | none | PASS |
| Speaker turns | 75 | 75 (opening 1-15; Q&A 16-74 = 59; closing 75) | none | PASS |
| Operator turns | 14 | 14 (turns 1,16,23,26,31,40,45,48,55,58,61,66,69,74) | none | PASS |
| Analyst questions | 23 | 23 (Achan 3, Devarat 1, ShilJain 2, Patel 4, Krish 2, Subramanium 1, Akhil 3, Tushar 1, Aniel 1, SatiK 2, Noah 1, Naman 2) | none | PASS |
| Management answers | 23 | 23 | none | PASS |
| Mgmt disclosure-unit rows | 91 | 91 (spot-reconciled by type below) | none material | PASS |
| Refusal/hedge rows | 9 | 9 (rows 71,74,76,77,82,83,85,87,91 = t18,28,37,39,47,50,54,65,73) | none | PASS |
| EXTERNAL_STAT rows | 18 | 18 (rows 5-22 + row 72) | none | PASS |

**Ledger-row-to-review reconciliation (every material row either cited in A4 or reviewed-no-finding):**
- Backward actuals (rows 38-58): revenue/EBITDA/PAT/segment/geo/order-book/net-cash/QIP -> A4 Step 1
  rows 17-26, Step 7A, Step 8. All cited. PASS.
- Forward commitments (rows 35-37/41/45/80/81/84/86/88-90): margin 23%, mix 50%, attach walk,
  capex, US plant, net-debt-free -> A4 Step 2 guidance table + monitorables. All cited. PASS.
- Refusals (9 rows) -> A4 Step 2 diagnostics + Step 6C defensive-language count (9 phrases enumerated
  at the exact turns). All cited. PASS.
- ESG/CSR rows 59-70 -> folded into A4 Step 1 row 27 (reviewed, no material finding). PASS.
- 18 EXTERNAL_STAT rows -> A4 Step 1 rows 2-8 + Step 7C, flagged not-STL-actuals, excluded from
  arithmetic. Correctly handled. PASS.

**No orphan rows** (nothing in the ledger is absent from A4). **No rows in my fresh pass that the
ledger lacks that rise to a finding.**

Minor completeness observation (non-gating, advisory to A2): turn 42 (file line 103) carries the
spelled phrase "three or four parallel demand centers," a fourth spelled-number token not listed in
the ledger's SPELLED_NUMBER set (which enumerates only multi-core "4-7x", MMC "3x", raw-material
"3-4 elements"). It is a qualitative categorisation of demand buckets, not a testable disclosure
metric, and touches no derived figure. Recorded for transparency; does NOT constitute a missing
disclosure unit that gates the verdict.

---

## 2. ARITHMETIC AUDIT (every derived metric recomputed from the raw extracted numbers)

Raw sources: consolidated P&L (results extract lines 198-239), segment table (275-303), standalone
P&L (537-574), auditor Other-Matter paras (861-874). Concall figures cross-checked to filing.

| Metric | A4 value | My recompute | Source line(s) | Status |
|---|---|---|---|---|
| Revenue YoY | +87% | 1910/1019 - 1 = +87.44% | results L198 (1910), L198 (1019) | PASS |
| Revenue QoQ | (strong, not headlined %) | 1910/1441 - 1 = +32.5% | L198 | PASS (consistent) |
| EBITDA YoY | +184% | 397/140 - 1 = +183.6% | L211 (397), L211 (140) | PASS |
| Reported EBITDA margin | 20.8% | 397/1910 = 20.79% | L211 / L198 | PASS |
| Operating EBITDA ex-OI margin | 20.2% | (397-12)/1910 = 385/1910 = 20.16% | L211, L199 (OI 12) | PASS |
| PAT margin | 10% | 197/1910 = 10.31% | L221 / L198 | PASS |
| PAT vs FY26 full-year | 3.5x | 197/56 = 3.52x | L221 (197), L221 (56) | PASS |
| Order intake multiple | 1.7x | 13100/7687 = 1.70x | concall L31 | PASS |
| Standalone PAT | Rs125cr | 125 (direct) | standalone L562 | PASS |
| Core operating PBT ex-OI Q1 | Rs245cr | 257 - 12 = 245 | L217 (257), L199 (12) | PASS |
| Core operating PBT ex-OI growth | +4,800% | (245-5)/5; Q1FY26 = 13-8 = 5 -> 49x = +4,800% | L217/L199 both periods | PASS |
| Standalone ex-OI PBT Q1 | +Rs120cr | 169 - 49 = 120 | standalone L558 (169), L538 (49) | PASS |
| Standalone ex-OI PBT FY26 | -Rs176cr | 3 - 179 = -176 | standalone L558 (3), L538 (179) | PASS |
| Subs share of consol PAT Q1FY27 | 36.5% | (197-125)/197 = 72/197 = 36.5% | L221 / L562 | PASS |
| Gap vs standalone PAT Q1FY27 | 57.6% | 72/125 = 57.6% | L221 / L562 | PASS |
| Subs share Q4FY26 / gap | 44.1% / 78.8% | (59-33)/59 = 44.1%; 26/33 = 78.8% | L221 / L562 | PASS |
| Subs share Q1FY26 / gap | 80.0% / 400% | (10-2)/10 = 80%; 8/2 = 400% | L221 / L562 | PASS |
| Subs share FY26 / gap | 96.4% / 2700% | (56-2)/56 = 96.4%; 54/2 = 2700% | L221 / L562 | PASS |
| % PAT not PW-reviewed | ~21.8% | (42+1)/197 = 43/197 = 21.83% | auditor L862 (42), L873 (1), L221 (197) | PASS |
| Ex-QIP net position | net-DEBT ~Rs1,017cr | 483 - 1500 = -1017 | concall L45 (483), results Note 5 L364 (1500 QIP) | PASS |
| Attach demonstrated pace | +1pp/yr | 16 - 15 = +1pp over 1yr | concall L39 | PASS |
| Attach next-qtr step | +4pp (4x) | >20 - 16 = +4pp | concall L39 | PASS |
| Attach Q4 step | +9pp (9x) | 25 - 16 = +9pp | concall L39/L107/L165 | PASS |
| Credibility ratio | 66.7% (Grade B) | (0.5+1.0+0.5)/3 = 2.0/3 = 66.7% | A4 Step 3A/3B | PASS |

**No arithmetic mismatch above rounding.** Every derived metric in A4's tables, the PAT/subsidiary
bridge, the standalone-vs-consolidated decomposition, and the attach-rate acceleration reconcile to
the raw extracted numbers.

---

## 3. ADVERSARIAL READ (three most-positive claims; strongest bear counter from the same text)

**Positive claim 1 — "EBITDA margin guide RAISED 20% -> 23%, already delivered 20% in Q1."**
Bear counter (from extract turns 32-33/50): gross margin is FLAT despite the DC mix rising, input
costs are at "significant multiples" with pass-through only "up to a certain level" — the raise rests
on utilization/mix/attach, not price/cost, and one of those legs (attach) needs a 4-9x un-mechanism'd
acceleration. Counter SURVIVES. **Already incorporated** (FND-01/05; flags; Step 6D; N2; N5b). No new
graft required.

**Positive claim 2 — "Record order intake Rs13,100cr = 1.7x FY26 full year; order book Rs18,618cr
(2.4x QoQ)."**
Bear counter (turns 34-35): the 1.7x compares Q1 against a FULL prior YEAR (period mismatch);
ex-the-$1.1bn deal the like-for-like regular intake was only ~Rs3,000cr vs ~Rs7-8,000cr; 88%
(Rs16,390cr) is parked "Q3 & beyond" with no dated schedule against only ~Rs500cr/yr capex; management
concedes it must "pick and choose orders basis capacity availability." Counter SURVIVES. **Already
incorporated** (FND-03/04; Step 7A; flags; N3). No new graft required.

**Positive claim 3 — "Net debt free, net cash Rs483cr; QIP 2.5x subscribed; ICRA upgraded to AA."**
Bear counter (concall L45 + results Note 5): the net-cash position is entirely QIP-funded (Rs1,500cr
raised, 75% only earmarked for debt, undeployed at 30-Jun); ex-QIP the group is net-DEBT ~Rs1,017cr;
no Net-Debt/EBITDA ratio path is given; and the CRISIL rating on the listed NCDs remains "AA-" (results
Note 4), one notch below the ICRA "AA." Counter SURVIVES. **Already incorporated** (FND-07; Step 7A;
flags; N7). No new graft required.

**Search for any surviving counter A4 has NOT incorporated:** none found. The Fujikura-while-Prysmian-
concealed asymmetry, the marquee-QIP-subscribers-asked-nothing point, the promoter/Chairman absence,
the DC-mix-up-but-gross-margin-flat tension, and the revenue-guidance refusal are all already carried.
**No un-incorporated surviving bear counter.**

Minor citation-hygiene note (non-gating, advisory to A4): in Steps 6D and 5B the margin-dependency of
the attach leg is cited as "t152" (and the Concat support as "t94"). There are only 75 turns; 152 and
94 are the extract's INTERNAL source-line numbers for turn 73 and turn 44 respectively. The same facts
are cited correctly as t73/L165 and t44/L107 in the guidance table, Step 8B, and the monitorables, and
the quoted text is verbatim-accurate at those turns. Recommend normalising t152 -> t73 and t94 -> t44
for consistency. This is a label slip on a correctly-located, correctly-quoted, independently-verified
claim; it is not an orphan row, an arithmetic error, or a surviving bear counter, so it does not gate
the verdict.

---

## 4. VERDICT

**COMPLETE.**

- Coverage: independent re-enumeration matches the A2 ledger on every category (15/75/14/23/23/91);
  no orphan rows, no missing rows of consequence.
- Arithmetic: every derived metric, the PAT/subsidiary bridge, the standalone-vs-consolidated
  decomposition, and the attach-rate acceleration recompute within rounding.
- Adversarial: the three most-positive claims each carry a surviving bear counter, and all three
  (plus the prior-loop attach-rate counter) are already grafted into A4.
- Re-audit item: the attach-rate acceleration bear counter is genuinely grafted into Step 6D, Step 8B
  (row 5b), the flags list, and Question-for-Management row N5b, with correct load-bearing line cites
  (L39; ledger rows 35-37/81/89; L107; L165), plus the guidance table, verdict, and YAML.

Only advisory (non-gating) items remain: one immaterial spelled-number omission in the A2 ledger
("three or four demand centers") and a t152/t94 internal-line-vs-turn label slip in A4 (same fact
correctly cited as t73/t44 elsewhere). Neither blocks save.

```yaml
stage: A5-adversary
company: "STLTECH"
quarter: "Q1FY27"
model: claude-opus-4-8
status: complete
verdict: COMPLETE               # COMPLETE | INCOMPLETE
coverage:
  orphan_rows: []               # ledger rows not cited in A4
  missing_from_ledger: []       # advisory-only: spelled "three or four demand centers" (t42/L103) — immaterial, non-metric, not gating
arithmetic_mismatches: []       # all derived metrics reconcile within rounding
surviving_bear_counters: []     # all three positive-claim counters + attach-rate counter already grafted into A4; none left un-incorporated
loop_back_to: ""                # "" if COMPLETE
gap: ""                         # none
```
