# A5 ADVERSARY / COMPLETENESS AUDIT — STLTECH Q1FY27 (Role 5 concall review)

Agent A5 (Adversary). Fresh context: A4 review + A1 extracts + A2 ledgers only. Every count and
number below is re-derived independently from the extracts; A4's and A3's cites were checked, not
trusted. Verdict: **INCOMPLETE** (one surviving bear counter must be grafted into A4 before save).

Review under audit: `review_role5_concall_stltech_q1fy27.md`
Primary extract: `extract_concall_stltech_q1fy27.txt` (158 internal lines; file lines 14-171)
Secondary (for arithmetic cross-check): `extract_results_stltech_q1fy27.txt`

---

## 1. COVERAGE AUDIT (fresh grep + turn-by-turn re-enumeration of the concall extract)

| Category | A2 count | My fresh count | Orphan rows (in ledger, absent from A4) | Status |
|---|---|---|---|---|
| Participants | 15 | 15 (3 mgmt: Tagral/Janjari/Darak + 12 analysts; operator tracked as call-admin) | none | PASS |
| Speaker turns | 75 | 75 (opening 1-15; Q&A 16-74 = 59; closing 75) | none | PASS |
| Analyst questions | 23 | 23 | none — all 23 in A4 Step 4A inventory | PASS |
| Answers | 23 | 23 | none | PASS |
| Operator turns | 14 | 14 (turns 1,16,23,26,31,40,45,48,55,58,61,66,69,74) | none | PASS |
| Mgmt number-tokens | 143 | 143 (accepted A2 grep+sweep methodology; spot-verified opening + Q&A tokens) | none | PASS |
| Mgmt disclosure units | 91 | 91 | none — Step 1 inventory (27 rows) folds opening rows 1-70; Q&A rows covered in Step 4A | PASS |
| Management refusals | 9 | 9 (ledger rows 71,74,76,77,82,83,85,87,91) | none — all 9 in A4 Step 6C + Step 2 | PASS |
| Forward commitments | 6 | 6 (23% margin; 50% mix; attach >20%/25%; net-debt-free FY27; capex Rs500cr/yr x3; US plant $100M/5yr) | none — all in A4 Step 2 guidance table | PASS |
| EXTERNAL_STAT rows | 18 (A2 summary) | 19 actual (ledger rows 5-22 = 18 in opening + row 72 in Q&A) | none — row 72 (US DC 8-10GW) IS carried into A4 Step 4A Q2 | PASS (see note) |

**Refusals — line-by-line confirmation (the flagged audit focus):** every one of the 9 refusal
units is transcribed correctly AND carried into A4:
- Capacity utilization "we don't disclose actual numbers" (extract L55, turn 18) → A4 6C, Step 2. ✓
- Revenue guidance "we don't give any guidance on the revenue" (L75, turn 28, Ajay) → A4 6C, Step 2. ✓
- Germanium terms "can't comment... for competitive reasons" (L93, turn 37) → A4 6C. ✓
- Order size "can't comment on any specific size" (L97, turn 39) → A4 6C. ✓
- Realization "we do not comment on realization broadly" (L113, turn 47) → A4 6C. ✓
- Full-year "we don't guide any numbers for the full year or longer term" (L119, turn 50) → A4 6C. ✓
- Connectivity/digital split "No we don't break that out" (L127, turn 54) → A4 6C. ✓
- US-plant capacity deferred (L149, turn 65) → A4 6C. ✓
- Telecom-vs-DC margin split "we don't normally call out the margin difference" (L165, turn 73) → A4 6C. ✓

**Forward-guidance claims — all carried:** 23% margin raise (L41,L165), 50% DC+enterprise (L43,L103),
attach >20%/25% (L39,L107,L165), net-debt-free FY27 (L45,L161), capex Rs500cr/yr x3 (L123), US plant
$100M/5yr (L145). All present in A4 Step 2 table + monitorables YAML.

**Prysmian-silence finding (flagged audit focus) — VERIFIED CORRECT.** Independent grep of the
concall extract for `Prysmian|Fujikura|Celesta|Szymanski` returns exactly TWO hits: L33 (Fujikura
"definitive victory... conclusively resolved in STL's favor... UK litigation related to our Celesta
cable family to a close") and L111 (Subramanium's technical question about Celesta fiber-per-rack
counts). **"Prysmian" and "Szymanski" appear ZERO times in the concall.** They appear only in the
results extract (consol Note 6 L372-384; standalone Note 7 L648-659: $101.25M award, $41.53M bond,
live Fourth-Circuit appeal). A4's FND-09 concealment finding — Fujikura win trumpeted while Prysmian
loss omitted in the same breath (t8) — is properly and independently evidenced. PASS.

**Coverage note (not a FAIL):** A2's flag-summary line states "EXTERNAL_STAT: 18 rows" but the ledger
actually flags 19 (rows 5-22 plus row 72). This is an internal A2 summary undercount of 1; the row
itself is enumerated and IS carried into A4, so no orphan and no missing row results. Cosmetic.

**Observation (not a FAIL):** the concall extract renders the MD as "Ankit **Tagral**" (auto-transcript,
"spelling artifacts preserved," L15), whereas the filing names the MD "Ankit **Agarwal**" (results
L158, DIN 03344202). "Tagral" is almost certainly a machine-transcription garble of "Agarwal."
A4's Step 0B "promoter/Chairman ABSENT" yellow flag partly rests on treating "Tagral" as
professional management distinct from the "Agarwal group" promoter — if Tagral = Agarwal, the
promoter-family MD was in fact present and leading the call, which softens (does not void) the
promoter-absence framing (a named Chairman is still not shown present). This is a bearish A4 flag,
not a positive claim, and not an enumeration gap; logged for A3/A4 to reconcile at Q2, not failed.

**Coverage verdict: PASS.** No orphan ledger rows; no rows my fresh pass found that the ledger lacks.

---

## 2. ARITHMETIC AUDIT (recomputed from raw extracted numbers)

Raw source (results extract, consol P&L): Revenue 1,910 / Q1FY26 1,019 / Q4FY26 1,441; EBITDA 397 /
140 / 218; Other income 12; PAT 197 / 10 / 59; FY26 PAT 56; PBT-before-exceptional 257 / 13.

| Metric | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| Revenue YoY | +87% | 1910/1019−1 = +87.4% | results L198 | PASS |
| EBITDA YoY | +184% | 397/140−1 = +183.6% | results L211 | PASS |
| Reported EBITDA margin | 20.8% | 397/1910 = 20.79% | results L198/L211 | PASS |
| Operating EBITDA ex-OI margin | 20.2% | (397−12)/1910 = 20.16% | results L199/L211 | PASS |
| PAT margin | 10% | 197/1910 = 10.31% | results L221 | PASS |
| PAT vs full-year FY26 | 3.5x | 197/56 = 3.52x | results L221 (FY26 col) | PASS |
| Order intake multiple | 1.7x | 13,100/7,687 = 1.704x | concall L31 | PASS |
| Order book components sum | 18,618 | 2,228 + 16,390 = 18,618 | concall L45 | PASS |
| Ex-$1.1bn regular intake | ~Rs3,000cr | 13,100 − ~10,000 = ~3,100 (mgmt stated ~3,000) | concall L31/L87 | PASS |
| Credibility ratio | 66.7% (Grade B) | (0.5+1.0+0.5)/3 = 0.6667 | review Step 3B | PASS |
| Subs share of consol PAT Q1 | 36.5% | (197−125)/197 = 36.55% | results L221/L562 | PASS |
| Core operating PBT ex-OI | Rs245cr, +4,800% | 257−12 = 245; (245−5)/5 = +4,800% | results L215/L199 | PASS |
| Ex-OI EBITDA margin uplift | +720bps | 20.2% − (140−8)/1019=12.95% ≈ 720bps | results L211/L199 | PASS |
| Standalone ex-OI PBT swing | −176 → +120 | FY26: 3−179=−176; Q1: 169−49=+120 | results L553/L558/L538 | PASS |
| % PAT not statutory-auditor-reviewed | ~21.8% | (42 other-auditor + 1 unreviewed)/197 = 21.8% | results L861-878 | PASS |

**Promise-vs-delivery / credibility-ratio arithmetic (flagged audit focus) — VERIFIED CORRECT.**
Three scored commitments: prior 20% margin = PARTIAL (0.5); prior ~Rs1,500cr Q1-executable = DELIVERED
(1.0); deleveraging/net-debt-free = PARTIAL (0.5). Points 2.0, denominator 3 (7 forward items correctly
excluded from both numerator and denominator), 2.0/3 = 66.7% = Grade B. Scorecard internally consistent
(Delivered 1 / Partial 2 / Missed 0 / Unclear 7). Answer-tracking 0 specific + 5 partial + 6 not-addressed
= 11. Q&A distribution A1/B9/C8/D1/E4 = 23; D+E = 5/23 = 21.7% ≈ "22%"; A+B = 10/23 = 43.5% ≈ "43%".
Specificity 10/(10+4) = 0.714 ≈ 0.71; 10/23 = 0.435 ≈ 0.43. All reconcile.

**Concall-number transcription check (flagged audit focus):** every concall figure A4 quotes matches
the extract verbatim — Rs1,910cr/+87% (L41), Rs397cr/+184% (L41), Rs197cr/10%/3.5x (L41), attach
16%/15%/>20%/25% (L39), DC 21% from 1% (L43), NA 54%/39%, Europe 25%, RoW 22% (L43), order book
18,618/2,228/16,390 (L45), net cash 483 (L45), QIP 1,500/2.5x/33%/75-25 (L45), intake 13,100/1.7x/7,687
(L31), $1.1bn thru FY29 (L31), capex 500x3=1,500 (L123), US plant $100M/5yr (L145), US DC 8-10GW (L59),
BEAD 5-7yr / BharatNet 3-4yr (L103). **No mis-transcription found.**

**Arithmetic verdict: PASS.** No mismatch above rounding.

---

## 3. ADVERSARIAL READ — three most-positive claims A4 carries, strongest bear counter each

**Positive claim 1 — Guidance RAISED (EBITDA margin 20%→23%; DC+enterprise mix 30%→50%).**
Bear counter (from the same text): the raise rests on a FLAT gross margin while the CFO concedes input
costs "increased to significant multiples" under "war situations," pass-through only "up to a certain
level" (L85/turn33, L63/turn22, L119/turn50); the 23% is carried by utilization/mix/attach, not
price/cost — a live downside if volume/mix stalls.
**Survives? NO — already incorporated** by A4 (FND-01/05; Step 2 diagnostic "STRAINED"; 4C Exchange 1;
flags YAML). No action.

**Positive claim 2 — Record order book Rs18,618cr (2.4x QoQ); intake Rs13,100cr = 1.7x FY26.**
Bear counter (from the same text): the 1.7x compares one quarter's intake to a FULL prior year
(period-mismatch, flattering); ex the single unnamed $1.1bn mega-deal the regular intake was only
~Rs3,000cr vs ~Rs7-8,000cr "regular business" a year earlier (L87/turn34) — i.e., core intake fell
~60%; and 88% of the book (Rs16,390cr) is parked "Q3 & beyond" with no dated schedule against only
~Rs500cr/yr capex, with mgmt admitting it must "pick and choose the orders basis capacity availability"
(L89/turn35).
**Survives? NO — already incorporated** by A4 (FND-03; 4C Exchange 2; 7A period-mismatch; flags YAML).
No action.

**Positive claim 3 — Attach-rate trajectory 16% (from 15%) → >20% next quarter → 25% by Q4, cited by
A4 (Step 6D) as a "dated attach-rate target" CONFIDENCE indicator and (Step 8B #5) a GREEN monitorable.**
Bear counter (from the same text): management's own disclosed pace of attach-rate improvement is **+1
percentage point over a full year** (15% "last year" → 16% now, L39/turn11). The guide requires **+4pp
in a single quarter** (16% → >20% "from next quarter onwards") and **+9pp within ~3 quarters** (→25% by
Q4) — a 4x-to-9x acceleration off management's own base, with no mechanism quantified beyond "launching
new products like Concat" (L107/turn44). Dating a target does not make its slope credible; on the
disclosed run-rate this is a promotional acceleration, not a confidence tell — and attach is one of the
three legs A4 itself says carries the 23% margin.
**Survives? YES.** A4 lists the dated attach targets as a positive confidence indicator (6D) and a GREEN
item, and NOWHERE constructs the run-rate-vs-guide acceleration counter. Supported entirely by extract
L39 vs L39/L107 (ledger rows 35-37). **Must be grafted into A4** (Step 6D and Step 8B #5, and as a
Question-for-Management: "reconcile the +1pp/yr demonstrated attach-rate pace with the +4pp-in-one-
quarter / +9pp-by-Q4 guide; what specifically bridges the gap?"). Loop back to A4.

---

## VERDICT

**INCOMPLETE.**
- Coverage: PASS (no orphan rows; no missing rows; all 9 refusals, all 6 forward commitments, and the
  Prysmian-silence finding correctly carried/evidenced).
- Arithmetic: PASS (promise-vs-delivery, credibility ratio, all margins/YoY, and every quoted concall
  number reconcile within rounding; no mis-transcription).
- Adversarial: ONE surviving bear counter (attach-rate acceleration implausibility) not incorporated.

**Loop back to: A4.** Gap: A4 presents the 16%→>20%→25% attach-rate walk as a confidence positive
(Step 6D) / GREEN monitorable (Step 8B #5) without the extract-supported bear counter that management's
own demonstrated pace is only +1pp/yr (15%→16%), so the guide implies a 4x-9x acceleration with no
quantified mechanism. Graft the counter (and matching Question-for-Management) before Notion save.

```yaml
stage: A5-adversary
company: "STLTECH"
quarter: "Q1FY27"
model: claude-opus-4-8
status: complete
verdict: INCOMPLETE
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches: []
surviving_bear_counters:
  - claim: "A4 cites the attach-rate walk 16% (from 15%) -> >20% next quarter -> 25% by Q4 as a 'dated attach-rate target' confidence indicator (Step 6D) and GREEN monitorable (Step 8B #5)"
    counter: "Management's own disclosed pace is +1pp over a full year (15%->16%); the guide requires +4pp in ONE quarter and +9pp within ~3 quarters, a 4x-9x acceleration off the disclosed base with no quantified mechanism. On the demonstrated run-rate this is promotional, not a confidence tell; attach is one of the three legs A4 says carries the 23% margin."
    source_line: "extract_concall L39 (turn 11) vs L39/L107 (turn 44); ledger rows 35-37"
loop_back_to: "A4"
gap: "Graft the attach-rate acceleration bear counter into A4 Step 6D and Step 8B #5 (and add a matching Question-for-Management): reconcile the +1pp/yr demonstrated attach-rate pace with the +4pp-next-quarter / +9pp-by-Q4 guide; A4 currently records the dated target only as a positive confidence indicator."
```
