# QUARTERLY PIPELINE A5 — ADVERSARY / COMPLETENESS AUDIT
# ZEEL (Zee Entertainment Enterprises Ltd) — Q1 FY27 (quarter ended 30 June 2026)

Fresh-context audit. I re-derived every count and every metric from the A1 extract's
own embedded line numbers (`L<n>`), diffed against the A2 ledger, and checked A4's
tables and claims. I did not defer to A4's or A3's cites; I recomputed. Filing units
Rs Millions; conversion x0.1 to Rs Crores (verified against both statement headers,
L266 / L954).

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate, run first)

The PLAIN-LANGUAGE BRIEF (review L644-724) carries all four labelled parts, each
non-empty and with real content:

| Brief part | Location | Present? | Real content? |
|---|---|---|---|
| 1. Summary narrative (10-20 lines) | L646-668 | present | Yes — 20-line narrative, revenue/PAT/margin/tax/LCIA/SEBI/dilution all covered |
| 2. Sector intelligence | L670-685 | present | Yes — linear-ad decline vs subscription, regulatory headwind, single-segment gap |
| 3. Business-model intelligence | L687-705 | present | Yes — two revenue engines, unit economics, model drift, tax/geography, BS dependency |
| 4. Competition intelligence | L707-724 | present | Yes — JioStar structural disadvantage, subscription resilience, ad-share risk |

GATE 0 = PASS. All four present.

---

## AUDIT 1 — COVERAGE (fresh enumeration vs A2 ledger)

I re-enumerated each category directly from the extract (board letter L20-61; standalone
notes L315-654; consolidated notes L1024-1435; standalone table L272-306; consolidated
table L960-1009; review reports L104-249 and L685-889; Annexure 1 entities L907-937;
Annexure A profiles L1457-1607) and diffed against the A2 count test.

| Category | A2 count | My fresh count | Orphan / delta | Status |
|---|---|---|---|---|
| Agenda items (board outcome) | 8 | 8 (items 1-8, L20-61) | none | MATCH — all 8 in review Sec J (items 2-8) + Step 0D/Sec J (item 1) |
| Notes — standalone | 15 | 15 (L316-654) | none | MATCH |
| Notes — consolidated | 17 | 17 (L1026-1435) | none | MATCH |
| Notes — total | 32 | 32 | none | MATCH — all in review Step 0D note table |
| Line items — standalone | 33 | 33 (L272-306) | none | MATCH |
| Line items — consolidated | 46 | 46 (L960-1009) | none | MATCH |
| Line items — total | 79 | 79 | none | MATCH |
| Review reports | 2 | 2 (standalone L104-249; consol L685-889) | none | MATCH — both in Sec I |
| Auditor paras — standalone | 6 | 6 | none | MATCH |
| Auditor paras — consolidated | 9 | 9 | none | MATCH |
| Consolidation entities | 25 | 25 (7 subs + 15 step-down + 2 JV + 1 associate, L907-937) | none | MATCH — Sec H |
| Annexure A profiles | 6 | 6 (L1457-1607) | none | MATCH — Sec J |

No row my fresh pass found that the ledger lacks (nothing to return to A2).
No ledger row absent from A4 (nothing to return to A3). Every P&L line, every note,
every agenda item, both reports, all entities and profiles are either cited in A4 or
carried under A4's blanket "all reviewed" reconciliation (review L20-29).

Coverage note (non-blocking): A4's 1A/1B data tables reproduce the P&L only to PAT +
EPS and do not individually reprint the Other-Comprehensive-Income rows (standalone
L293-301; consolidated L988-998, L1002-1004). These are covered by A4's explicit
"all 79 result-table line items reviewed" statement (L25) and carry no thesis-relevant
finding (OCI is not a derived-metric input here). Accepted as "reviewed, no finding";
not an orphan.

COVERAGE = PASS.

---

## AUDIT 2 — ARITHMETIC (independent recompute from raw Millions)

Recomputed from the extract's raw Rs Million anchors. All headline numbers, margins,
YoY, the standalone-vs-consolidated PAT gap, and the consolidated PAT bridge reconcile
to A4 within rounding.

### Unit conversion and the two A4-self-reported OCR items — verified independently

| Check | Source (raw Millions) | My derivation | A4 value | Status |
|---|---|---|---|---|
| STD-OCR-1: Other income Q1FY27 | Total income 18,030 (L274) − Revenue 17,809 (L272) = 221; printed "21" (L273) | 221 Mn = Rs 22.1 Cr | 22.1 (printed "21", OCR) | CONFIRMED — printed "21" is truncation of 221 |
| STD-OCR-2: Operational cost Q1FY27 | Total expenses 17,353 (L283) − (emp 1,774 + fin 129 + D&A 362 + FV (207) + ad&pub 2,257 + other 1,178 = 5,493) = 11,860; printed "9,860" (L276) | 11,860 Mn = Rs 1,186.0 Cr; under-foots by exactly 2,000 | 1,186.0 (printed "986.0", OCR) | CONFIRMED — printed 9,860 is truncation of 11,860 |

Both A4 self-reported items are correct. The reconciled standalone PBT/PAT walk is
undisturbed (Total income, Total expenses, PBT 677, tax 204, PAT 473 all foot).

### Standalone headline / derived (Rs Cr)

| Metric | A4 value | My recompute | Source lines | Status |
|---|---|---|---|---|
| Revenue YoY | +5.88% | (1,780.9−1,682.0)/1,682.0 = +5.88% | L272 | OK |
| Operating EBITDA Q1FY27 (PBT+D&A+Fin−OI) | 94.7 | 67.7+36.2+12.9−22.1 = 94.7 | L286/279/278/274 | OK |
| Op EBITDA margin Q1FY27 | 5.32% | 94.7/1,780.9 = 5.32% | — | OK |
| Op EBITDA margin delta | −612 bps | 5.32−11.44 = −6.12 pp | — | OK |
| Core PBT ex-OI YoY | −66.5% | (45.6−136.0)/136.0 = −66.47% | — | OK |
| Effective tax rate Q1FY27 | 30.1% | 20.4/67.7 = 30.13% | L291/286 | OK |
| ETR Q1FY26 (tax printed "a3") | 27.9% (43.2 = 400+32 component sum) | 432 Mn = 43.2; 43.2/154.7 = 27.93% | L288-291 | OK — OCR reconciled |
| PAT YoY | −57.6% | (47.3−111.5)/111.5 = −57.58% | L292 | OK |
| PAT margin Q1FY27 | 2.66% | 47.3/1,780.9 = 2.66% | — | OK |

### Consolidated headline / derived (Rs Cr)

| Metric | A4 value | My recompute | Source lines | Status |
|---|---|---|---|---|
| Revenue from ops Q1FY27 | 1,907.3 | 6,714+11,369+990 = 19,073 Mn | L961-963 | OK |
| Revenue YoY | +4.52% | 82.5/1,824.8 = +4.52% | — | OK |
| Advertisement revenue YoY | −11.48% | (671.4−758.5)/758.5 = −11.48% | L961 | OK |
| Subscription revenue YoY | +15.81% | (1,136.9−981.7)/981.7 = +15.81% | L962 | OK |
| Total expenses Q1FY27 (foots) | 1,864.4 | 10,317+2,126+132+435−207+4,468+1,373 = 18,644 | L967-975 | OK — clean footing |
| Operating EBITDA Q1FY27 | 99.6 | 74.1+43.5+13.2−31.2 = 99.6 | L981/970/969/964 | OK |
| Op EBITDA margin Q1FY27 | 5.22% | 99.6/1,907.3 = 5.22% | — | OK |
| Op EBITDA margin delta | −788 bps | 5.22−13.10 = −7.88 pp | — | OK |
| Ad&publicity expense YoY | +62.4% | (446.8−275.2)/275.2 = +62.35% | L973 | OK |
| Reported PBT YoY | −62.4% | (74.1−197.2)/197.2 = −62.42% | L981 | OK |
| Total tax Q1FY27 | (0.2) | 255−289+32 = −2 Mn = (0.2) | L983-986 | OK |
| Effective tax rate Q1FY27 | −0.3% | (0.2)/74.1 = −0.27% | — | OK |
| PAT (total) Q1FY27 | 74.3 | 741−(−2) = 743 Mn | L987 | OK |
| PAT (total) YoY | −48.3% | (74.3−143.7)/143.7 = −48.30% | — | OK |
| PAT attributable YoY | −46.9% | (76.3−143.7)/143.7 = −46.90% | L1000 | OK |
| Other Income / PBT Q1FY27 | 42.1% | 31.2/74.1 = 42.11% | — | OK |

### Consolidated PAT bridge (Q1FY26 -> Q1FY27)

Recomputed each component from L961-987; sum of PBT deltas = +82.5+6.2−60.7+7.5−5.5
+15.6+9.8−171.6−6.8−0.1 = **−123.1** (matches A4 reported PBT change). Tax swing 53.5 ->
(0.2) = **+53.7** benefit; −123.1+53.7 = **−69.4** PAT change (matches A4). Rs 28.9 Cr
earlier-years credit (L984) correctly identified as the non-recurring cushion. BRIDGE OK.

### Standalone-vs-consolidated PAT gap (Section G)

| Period | S PAT (L292) | C PAT (L987) | Gap C−S | Gap % of S | My check |
|---|---|---|---|---|---|
| Q1 FY27 | 47.3 | 74.3 | +27.0 | +57.1% | 27.0/47.3 = 57.08% OK |
| Q1 FY26 | 111.5 | 143.7 | +32.2 | +28.9% | 32.2/111.5 = 28.88% OK |
| FY26 | 120.5 | 271.3 | +150.8 | +125.1% | 150.8/120.5 = 125.1% OK |

Gap widened +28.2 pp YoY (28.9 -> 57.1). OK. The "~83% of group PAT outside principal
auditor" claim also checks: (602+14)/743 = 82.9% (L818-855). OK.

**Arithmetic verdict: all headline numbers, margins, YoY/QoQ, the PAT gap, and the PAT
bridge reconcile within rounding. No derived-metric mismatch.**

### One non-propagating transcription note for A4 (annotate at save; not a derived-metric fail)

Consolidated line L977 ("Profit before share of JV & associate, exceptional & tax
[1+2−3]") prints **781** for the current quarter, and A4's 1B table transcribes it as
**78.1**. But 1+2−3 = Total income 19,385 (L965) − Total expenses 18,644 (L975) = **741 =
Rs 74.1 Cr**, and L979 (after JV share 0.0) prints **741 -> 74.1**. So the source "781"
is OCR-inconsistent with the filing's own arithmetic; the reconciling value is 74.1.
A4 flagged the FY26 and Q1FY26 columns of this same line as OCR garble but left the
current-quarter cell as a clean "78.1", creating an internal inconsistency in its own
table (78.1 + 0.0 JV != 74.1). Impact: **none downstream** — every headline, margin, YoY,
ETR, PAT bridge and the PAT gap correctly use PBT 74.1 (L981). Recommended fix: A4
annotates the L977 current-quarter cell as OCR-suspect (=741 = Rs 74.1 Cr), consistent
with its treatment of the other columns. Non-blocking (this is a source-line
transcription artifact, not one of the enumerated derived metrics, and it does not
propagate).

---

## AUDIT 3 — ADVERSARIAL READ (three most positive claims + strongest bear counter)

For each, I built the strongest bear case from the SAME extracted text and asked whether
it survives AND whether A4 already incorporated it.

**Positive claim 1 — "Subscription revenue +15.81% YoY, the lone bright spot carrying the
top line" (review L229, L448).**
Bear counter (same extract): subscription grew +15.81% (L962) yet consolidated revenue
rose only +4.52% because advertisement revenue fell −11.48% (L961); and despite the
subscription growth, op EBITDA margin still collapsed −788 bps and PAT fell −48.3%,
because ad&publicity spend rose +62.4% (L973) consuming the gain. Subscription growth is
not converting to profit. Counter SURVIVES — but A4 already incorporates it fully (Step 2
diagnostics 1-4, Step 8C, Sec K). Not un-grafted.

**Positive claim 2 — "Margin recovered from a Q4 loss to +5.22% (recovery off a distorted
Q4)" (review L296, L301).**
Bear counter (same extract): the Q4 loss was inflated by a Rs 302.2 Cr one-off movie-
inventory catch-up (Note 10, L595), so the QoQ "recovery" is just the one-off not
repeating; against the clean Q1 FY26 base both mix and margin deteriorated. Counter
SURVIVES — A4 already states exactly this ("not recovery but the one-off is gone and the
underlying is still weak", L300-304). Not un-grafted.

**Positive claim 3 — "Reported PAT fell only −48.3%, cushioned" (review L239, L266).**
Bear counter (same extract): the cushion is a non-repeatable near-zero tax charge —
consolidated ETR −0.3% carried by a Rs 28.9 Cr earlier-years credit (L984); normalised at
~27% PAT would be ~Rs 54 Cr, a ~−62% fall in line with PBT. Counter SURVIVES — A4 already
incorporates it (Step 4A/4B, L266-268, L336-342). Not un-grafted.

**Additional adversarial probe — "warrants at Rs 126, a premium to CMP Rs 108.31, hence
not distress-priced dilution" (review L436).** Bear counter: the raise is to a Promoter
Group entity (related party, control-entrenching, L606), is ~30% dilution, and the SEBI
31-Jul-2026 order restrains market access with the Company itself seeking clarification
whether the ban blocks the allotment (L481-483). A4 already marks watchlist item 6 RED and
raises management question 2. Covered; not un-grafted.

No surviving bear counter is absent from A4. Nothing to graft.

### Other adversarial completeness checks (task-mandated)

- AMBIGUOUS / FORWARD-SIGNAL findings -> management questions: all 14 A3 IDs incorporated;
  12 management questions (review L513-526) include all five task-mandated items (SEBI-ban-
  vs-warrant Q2; missing consol EPS Q6; FCCB coupon Q8; Note-7 cross-ref Q9; Phantom name
  Q10). Board item 2 (AGM, FORWARD-SIGNAL) routed to a monitorable/Role 6 rather than a
  Q&A row — acceptable (a date, not a Q&A matter). PASS.
- Dropped zero-value lines: exceptional items (blank 3/4 periods, L285/980), other equity
  (year-end only, L303/1006), JV share (0.0), NCI, all addressed. PASS.
- Auditor Emphasis-of-Matter paragraphs: standalone 2 EoM (Note 7 SEBI L168-196; Note 9
  JioStar L197-211) + 1 Other Matter (Note 15 balancing, L229). Consolidated 3 EoM (Note 7
  L742-768; Note 9 L783-797; Note 13 RIICO reproduced from ZSL auditor L801-815) + 3 Other
  Matters (7 subs component-audited L817-824; 9 subs + 1 JV unreviewed L853-866; Note 17
  L868-871). All in review Sec I / Step 0D. No going-concern EoM despite IDBI IBC petition
  (Note 3) — A4 flags the tension. PASS.
- Board Outcome items beyond item 1: items 2-8 enumerated in Sec J (all four IDs re-
  appointed to 2031; cost/internal auditors re-appointed; AGM convening). PASS.
- FCCB coupon inconsistency independently verified: standalone L506 "5%" vs consolidated
  L1255 "6%" for the same USD 239M instrument — real, flagged, Q8. PASS.

---

## VERDICT

**COMPLETE.**

- GATE 0 (plain-language brief, four parts): PASS.
- COVERAGE: PASS — my fresh enumeration (8 / 15 / 17 / 33 / 46 / 2 / 25 / 6) matches the
  A2 ledger exactly; no orphan rows, nothing missing from the ledger.
- ARITHMETIC: PASS — every headline number, margin, YoY/QoQ, the standalone-vs-
  consolidated PAT gap, the ETR, and the consolidated PAT bridge reconcile within
  rounding from the raw Rs Million anchors. Unit conversion (Millions x0.1) verified.
  Both A4-self-reported OCR items (Other income 21->221; Operational cost 9,860->11,860)
  independently confirmed.
- ADVERSARIAL: PASS — the three strongest bear counters all survive but are already
  incorporated by A4; no un-grafted surviving counter.

One non-blocking annotation is handed to A4 for the save copy: the consolidated L977
current-quarter cell (printed "781", shown as 78.1) should be annotated OCR-suspect and
reconciled to Rs 74.1 Cr (Total income 19,385 − Total expenses 18,644 = 741; L979 = 741),
matching A4's own treatment of the other columns of that line. This does not change any
headline, margin, YoY, the PAT gap, or the PAT bridge — all of which correctly use 74.1 —
so it does not block the save; it is a table-consistency tidy-up.

```yaml
stage: A5-adversary
company: "ZEEL"
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
notes:
  - "Non-blocking: A4 to annotate consolidated L977 current-quarter cell (printed 781, shown 78.1) as OCR-suspect; reconciled value 741 = Rs 74.1 Cr (Total income 19,385 - Total expenses 18,644 = 741; L979 confirms 741 with JV share 0). Does not propagate to any headline/derived metric."
  - "Verified STD-OCR-1 (Other income 21->221, Rs 22.1 Cr) and STD-OCR-2 (Operational cost 9,860->11,860, Rs 1,186.0 Cr) independently; both correct."
```
