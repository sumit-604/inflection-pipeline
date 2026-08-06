# A5 ADVERSARY / COMPLETENESS AUDIT — Uni Abex Alloy Products (UNIABEX) — Q1 FY27

Fresh context. I re-derived every number from the A1 extract
(`extract_results_uniabex_q1fy27.txt`) and re-ran the A2 enumeration
independently. I did not defer to A4's or A3's cites; I checked them.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate, run first)

The A4 review carries a PLAIN-LANGUAGE BRIEF (review lines 391-413) with all
four labelled parts present and non-empty:

| Part | Location | Present? | Real content (not placeholder)? |
|---|---|---|---|
| 1. Summary narrative | review 393-395 | PRESENT | Yes — ~1 dense para, >10 lines of content: headline +30.5% PAT vs core −45.5%, OI 70% of PBT, ₹14.18 Cr inventory build, clean review, unlevered, WATCHLIST stance |
| 2. Sector intelligence | review 397-401 | PRESENT | Yes — single "Alloy and Steel Castings" segment, Neterwala group, cyclical capex/input-cost read, labelled provenance |
| 3. Business-model intelligence | review 403-407 | PRESENT | Yes — material-intensive conversion model, unlevered, treasury-driven profit drift, named gaps |
| 4. Competition intelligence | review 409-413 | PRESENT | Yes — group backing / debt-free as assets, small scale + input-cost exposure as risk, no fabricated peer numbers |

GATE: PASS. All four parts present with real content.

---

## AUDIT 1 — COVERAGE (independent re-enumeration vs A2 ledger)

Fresh grep/sweep over the extract, diffed against the A2 count test.

| Category | A2 count | My fresh count | Basis in extract | Orphan rows (ledger→A4) | Status |
|---|---|---|---|---|---|
| Notes | 7 | 7 | Notes 1-7, lines 260-290 | none | PASS |
| Line items | 33 | 33 | Statement rows 1-12 + sub-items + headers + totals, lines 203-250 | none | PASS |
| Agenda items | 2 | 2 | Board letter (a) results, (b) resignation, lines 50-63 | none | PASS |
| Annexure II rows | 4 | 4 | Reg 30/Sch III table, lines 317-329 | none | PASS |
| Auditor paras | 4 | 4 | Paras 1-4, lines 116-159 | none | PASS |
| Consolidation entities | 0 | 0 | Note 7 explicit nil, line 290 | none | PASS |
| Signature blocks | 3 | 3 | Shah (76-82), Daruwalla (162-178), F.D. Neterwala (300-302) | none | PASS |
| Enclosures | 3 | 3 | Annexure I, Annexure II, resignation letter, lines 92-378 | none | PASS |

Row-by-row disposition of every ledger row against A4:
- All 33 line items appear in A4 Step 1 data table (review 66-83).
- Notes 1-7 all appear in A4 0D structured table (review 42-48).
- Agenda (a) results carries the whole review; agenda (b) resignation →
  FN-05/07, monitorables #2, Q5 (review 358, 384).
- Annexure II rows 1-2 → resignation flag; rows 3-4 ("Not applicable",
  ZERO_STANDING) → A4 preamble marks "4 Annexure II rows ... reviewed"
  (review 13). Marked reviewed, no finding — permissible.
- Auditor paras 1-4 → A4 0D "Auditor opinion check" (review 50).
- Entities 0 → note 7 / Standalone-vs-Consolidated section (review 238).
- 3 signatures + 3 enclosures → A4 preamble reconciled to zero unreviewed
  (review 13). The A2-flagged detail that the resignation letter is dated
  7 Jul 2026, ~1 month before board acceptance (ledger sec.8), is a routine
  timing item; the resignation substance is incorporated (FN-05/07) and the
  enclosure is marked reviewed. No forensic dropped.
- A2-flagged note-7 indentation anomaly (ledger sec.2) resolved: 7 notes
  confirmed, formatting artifact, not mis-numbering.

Rows my fresh pass found that the ledger lacks: NONE.
Orphan rows (in ledger, absent from A4): NONE.

COVERAGE: PASS. Ledger reconciled 100%; no loop-back to A2 or A3.

---

## AUDIT 2 — ARITHMETIC (recomputed from raw extract, not from A4)

Source lines: revenue 204, OI 205, total income 206, materials 209, inv-change
210, employee 212, finance 213, dep 214, mfg&op 216, others 219, total exp 220,
PBT-pre-exc 222, exceptional 223, PBT 224, current tax 227, deferred 228, total
tax 230, PAT 232, EPS 249.

| Metric | A4 value | My recompute | Source lines | Status |
|---|---|---|---|---|
| Op EBITDA Q1FY27 | 429.37 | 973.80+120.30+16.47−681.20 = 429.37 | 222/214/213/205 | MATCH |
| Op EBITDA Q1FY26 | 681.34 | 749.02+125.49+18.59−211.76 = 681.34 | 222/214/213/205 | MATCH |
| Op EBITDA Q4FY26 | 2,423.79 | 2,576.97+131.74+19.01−303.93 = 2,423.79 | 222/214/213/205 | MATCH |
| Op EBITDA FY26 | 5,154.82 | 5,530.84+503.46+70.25−949.73 = 5,154.82 | 222/214/213/205 | MATCH |
| Op EBITDA margin Q1FY27 | 10.46% | 429.37/4,103.25 = 10.46% | 204 | MATCH |
| Op EBITDA margin Q1FY26 | 17.39% | 681.34/3,918.27 = 17.39% | 204 | MATCH |
| Op margin delta | −693 bps | 10.46−17.39 = −6.93 pp | — | MATCH |
| Reported EBITDA ex-exc Q1FY27 | 1,110.57 | 973.80+120.30+16.47 = 1,110.57 | 222/214/213 | MATCH |
| Reported EBITDA margin Q1FY27 | 27.07% | 1,110.57/4,103.25 = 27.07% | 204 | MATCH |
| Core PBT ex-OI Q1FY27 | 292.60 | 973.80−681.20 = 292.60 | 222/205 | MATCH |
| Core PBT ex-OI Q1FY26 | 537.26 | 749.02−211.76 = 537.26 | 222/205 | MATCH |
| Core PBT YoY | −45.54% | (292.60−537.26)/537.26 = −45.54% | — | MATCH |
| OI/PBT(pre-exc) Q1FY27 | 69.95% | 681.20/973.80 = 69.95% | 205/222 | MATCH |
| ETR Q1FY27 | 25.50% | 248.35/973.80 = 25.50% | 230/224 | MATCH |
| ETR Q1FY26 | 25.79% | 193.18/749.02 = 25.79% | 230/224 | MATCH |
| ETR Q4FY26 | 13.92% | 4,167.07/29,930.02 = 13.92% | 230/224 | MATCH |
| ETR FY26 | 14.89% | 4,897.68/32,883.89 = 14.89% | 230/224 | MATCH |
| PAT margin Q4FY26 | 329.1% | 25,762.95/7,829.03 = 329.1% | 232/204 | MATCH |
| PAT margin FY26 | 127.9% | 27,986.21/21,878.41 = 127.9% | 232/204 | MATCH |
| Revenue YoY | +184.98 / +4.72% | 4,103.25−3,918.27=184.98; /3,918.27=4.72% | 204 | MATCH |
| Total expense YoY | +429.64 / +12.71% | 3,810.65−3,381.01=429.64; /3,381.01=12.71% | 220 | MATCH |
| Other income YoY | +469.44 / +221.68% | 681.20−211.76=469.44; /211.76=221.68% | 205 | MATCH |
| Reported PBT YoY | +224.78 / +30.01% | 973.80−749.02=224.78; /749.02=30.01% | 224 | MATCH |
| Tax change | +55.17 / +28.56% | 248.35−193.18=55.17; /193.18=28.56% | 230 | MATCH |
| PAT YoY | +169.61 / +30.51% | 725.45−555.84=169.61; /555.84=30.51% | 232 | MATCH |
| EPS YoY | +8.59 / +30.53% | 36.73−28.14=8.59; /28.14=30.53% | 249 | MATCH |
| PAT bridge close | +169.61 | −244.66+469.44−55.17 = +169.61 | — | MATCH |
| Mfg&op expense YoY | +316.51 / +52.98% | 913.95−597.44=316.51; /597.44=52.98% | 216 | MATCH |
| Materials consumed YoY | +42.9% | (2,933.41−2,052.49)/2,052.49 = 42.92% | 209 | MATCH (within rounding) |
| Net material cost YoY | −72.19 / −4.55% | (2,933.41−1,417.69)−(2,052.49−464.58)=−72.19 | 209/210 | MATCH |
| OI-reverts run-rate PAT | ~375.8 / ~48% below | (973.80−469.44)×0.745 = 375.75; 48.2% below 725.45 | 224/205/230 | MATCH |
| Exceptional gain (note 6) | 27,353.05 | 28,019.42−653.65−12.72 = 27,353.05 | 287-288 | MATCH |
| FY26 dividend outflow | 1,975.00 L (₹19.75 Cr) | 19.75L sh × ₹100 = 1,975.00 L | 249/243 | MATCH |
| Special dividend | 1,185.00 L (₹11.85 Cr) | 19.75L sh × ₹60 = 1,185.00 L | 243/281 | MATCH |
| Deferred tax swing | +50.94 vs −18.31 | line 228 verbatim | 228 | MATCH |

ARITHMETIC: PASS. Zero mismatches above rounding. No loop-back to A4.

---

## AUDIT 3 — ADVERSARIAL READ (three most positive claims + strongest bear from same text)

For each I built the strongest bear counter from the extract, then checked
whether A4 already carries it. A counter "survives" (and must be grafted) only
if it is supported by the extract AND absent from A4.

**Positive claim 1 (headline, review 121-122, 394-395):** "Reported net profit
rose 30.5% to ₹7.25 Cr; EPS ₹36.73 vs ₹28.14 — looks like a strong quarter."
- Strongest bear (same text): Strip Other Income (681.20 vs 211.76, line 205)
  and core operating profit fell 45.5% (292.60 vs 537.26); Op EBITDA margin
  −693 bps; the entire PAT rise is non-operating treasury on the Thane proceeds.
- Already in A4? YES — Step 2 diagnostic 3, Step 4, FN-03, narrative. 
- Survives / must graft? NO (already incorporated).

**Positive claim 2 (review 50, 395, 406):** "The audit is clean and unmodified;
leverage negligible, cash-rich."
- Strongest bear (same text): It is a LIMITED REVIEW under SRE 2410, explicitly
  "substantially less in scope than an audit ... we do not express an audit
  opinion" (paras 2-3, lines 121-137); Q4 FY26 comparative is a balancing figure
  (note 4, line 270); no balance sheet or cash flow in this Q1 filing, so net
  debt/net cash is ND and the ₹412.62 Cr other equity (line 246) is a FY26
  year-end audited number inflated by the ₹273.53 Cr one-off gain. "Clean audit /
  cash-rich" overstates the assurance and the disclosed cash position.
- Already in A4? YES — note-2 row "confirms review (not audit) status",
  Step 0D, Step 5 (net debt ND), Step 7 (other equity inflated by the gain),
  business-model section.
- Survives / must graft? NO (already incorporated).

**Positive claim 3 (review 193, 359):** "Tax is clean at 25.5%, near statutory;
no land-sale tax residue leaks into FY27."
- Strongest bear (same text): Current tax actually FELL YoY (197.41 vs 211.49,
  line 227) while PBT rose; the total tax increase is entirely a deferred-tax
  swing (+50.94 vs −18.31, line 228). The stable headline ETR masks a timing
  reversal whose recurrence is unconfirmed.
- Already in A4? YES — FN-06 and management Q6 name the deferred swing and ask
  whether it recurs (review 359, 444).
- Survives / must graft? NO (already incorporated).

ADVERSARIAL READ: no surviving un-incorporated bear counter. A4's review is
already symmetric on all three headline positives; nothing to graft.

---

## VERDICT

**COMPLETE.** All four brief parts present; independent re-enumeration matches
the A2 ledger with zero orphans and zero rows missing; every derived metric
recomputed from the raw extract matches A4 within rounding; all three strongest
bear counters are already carried in A4. Proceeds to Notion save.

```yaml
stage: A5-adversary
company: "UNIABEX"
quarter: "q1fy27"
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
