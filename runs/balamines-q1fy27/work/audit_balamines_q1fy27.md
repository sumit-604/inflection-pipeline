# A5 ADVERSARY / COMPLETENESS AUDIT — Balaji Amines Limited (BALAMINES), Q1 FY27

Agent: A5 ADVERSARY | Model: claude-opus-4-8 | Audit date: 2026-07-28
Fresh context: only the A4 review, the two A1 extracts, and the two A2 ledgers were read.
All numbers below re-derived from the A1 extracts (results in Lakhs, x0.01 -> Cr; press in Cr).
A4 cites and ledger cites were checked against the raw extract, not deferred to.

Doc-set limitation acknowledged per task: no concall transcript, no slide deck. A4 is NOT
faulted for absent concall coverage; that limitation is disclosed in A4's flags. Coverage
audit is scoped to the results-filing ledger rows and the press-release highlight cells.

---

## AUDIT 1 — COVERAGE

Fresh grep/sweep pass re-run over each extract, diffed against the A2 ledger counts, then
every ledger category checked for citation in A4 (or blanket "all reviewed" in A4's preamble
L11-18).

### Results filing (extract_results, 430 lines)

| Category | A2 count | My fresh count | Orphan rows | Status |
|---|---|---|---|---|
| agenda_items | 3 | 3 (L49, L51, L53-55) | none | PASS |
| line_items (logical) | 102 | 102 (34+40+32 physical rows in ranges 106-139/168-207/232-264 less 4 wrap-lines) | none | PASS |
| zero_standing | 13 | 13 (SA: L119,129,130,131,132,136 = 6; CON: L181,194,195,196,197,204 = 6; SEG: L247 = 1) | none | PASS |
| notes | 5 | 5 (L291-304) | none | PASS |
| auditor_paras | 9 | 9 (SA 4 @ L337-361; CON 5 @ L397-425) | none | PASS |
| entities | 2 | 2 (BAL parent; BSC subsidiary) | none | PASS |
| signature_blocks | 3 | 3 (CS L65-70; SA auditor L364-377; CON auditor L427-438) | none | PASS |

### Press release (extract_presentation, 232 lines)

| Category | A2 count | My fresh count | Orphan rows | Status |
|---|---|---|---|---|
| pages | 5 | 5 | none | PASS |
| highlight_cells | 48 | 48 (8 metrics x 6 period/book cols, L75-82) | none | PASS |
| segment_volumes | 3 | 3 (L98-100; sum 21,586.60 ~ 21,587 consol) | none | PASS |
| diluted_eps | 2 | 2 (L108-109: 23.13 / 19.99) | none | PASS |
| mgmt_forward_statements | 32 | 32 sentences (A4 consolidated to 16 dedup claims, Sec B Step 1) | none | PASS |
| footnotes_disclaimers | 2 | 2 (F1 Cash PAT def L84; F2 Safe Harbor L208-216) | none | PASS |
| admin_identifiers | 14 | 14 | none | PASS |
| zero_standing | 0 | 0 | none | PASS |

**Fresh counts reconcile to the A2 ledgers in every category.** No row my pass found is absent
from the ledger (nothing to return to A2). No enumerated ledger row is absent from A4's review
(nothing to return to A3): A4's preamble (L11-18) marks all rows reviewed, and every material
category is explicitly engaged — notes in Step 0D, auditor paras / opinion in Step 0D, agenda
in Step 0/0A, entities (BSC) throughout, the SIGNATURE_BEFORE_BOARD_CLOSE block as Step 8.5 Q8,
the segment table in Step 5 (assets/liabilities proxy) and Step 7 (ROCE proxy, L243), the
press highlight cells cross-checked in Steps 1C/1D, the Cash PAT footnote as F11-02, the [NS1]
DOC_ARTIFACT as F14-01, and all 32 press sentences mapped into the 16-claim inventory.

**COVERAGE VERDICT: PASS.** One interpretive gap is noted below (segment RESULTS-by-division
rows L233-253 were enumerated and touched only at the aggregate/ROCE level, not analysed per
division). Because those rows are present in the ledger and A4 did engage the segment table,
this is not a coverage orphan (no A3/A2 loopback); it surfaces instead as a surviving bear
counter in Audit 3 (routed to A4).

---

## AUDIT 2 — ARITHMETIC

Every derived metric in A4's tables recomputed from raw extract cells at full Lakh precision
(not from A4's rounded Cr), to avoid false mismatches. A4 value | my recompute | source lines.

### Standalone margins / rates (A4 Table 1C)

| Metric | A4 | Recomputed | Source (extract L) | Status |
|---|---|---|---|---|
| Op EBITDA Q1FY27 (PBT+D+FC-OI) | 103.46 | 9781.80+1154.17+26.94-616.79 = 10346.12 -> 103.46 | 118/114/115/107 | PASS |
| Op EBITDA margin Q1FY27 | 24.47% | 103.46/422.74 = 24.47% | " /106 | PASS |
| Op EBITDA margin Q1FY26 | 17.68% | 56.47/319.38 = 17.68% | 118/114/115/107/106 | PASS |
| Reported EBITDA margin Q1FY27 | 25.93% | 109.63/422.74 = 25.93% | 118/114/115/106 | PASS |
| Effective tax rate Q1FY27 | 26.25% | 2567.56/9781.80 = 26.25% | 125/118 | PASS |
| Effective tax rate Q1FY26 | 23.96% | 1254.06/5234.02 = 23.96% | 125/118 | PASS |
| PAT margin Q1FY27 | 17.07% | 72.14/422.74 = 17.07% | 126/106 | PASS |

### Consolidated margins / rates (A4 Table 1D)

| Metric | A4 | Recomputed | Source (extract L) | Status |
|---|---|---|---|---|
| Op EBITDA Q1FY27 | 115.87 | 10620.36+1378.24+141.22-552.49 = 11587.33 -> 115.87 | 180/176/177/169 | PASS |
| Op EBITDA margin Q1FY27 | 25.41% | 115.87/455.93 = 25.41% | " /168 | PASS |
| Op EBITDA margin Q1FY26 | 15.26% | 54.69/358.34 = 15.26% | 180/176/177/169/168 | PASS |
| Reported EBITDA margin Q1FY27 | 26.63% | 121.40/455.93 = 26.63% | 180/176/177/168 | PASS |
| Effective tax rate Q1FY27 | 26.45% | 2808.59/10620.36 = 26.45% | 187/180 | PASS |
| Effective tax rate Q1FY26 | 25.48% | 1248.62/4901.34 = 25.48% | 187/180 | PASS |
| PAT margin (owners) Q1FY27 | 16.44% | 74.94/455.93 = 16.44% | 190/168 | PASS |

### YoY walk (A4 Step 2A/2B) — the highest-weight step

| Metric | A4 | Recomputed | Source (extract L) | Status |
|---|---|---|---|---|
| SA revenue YoY | +32.4% | (42273.75-31937.88)/31937.88 = +32.36% | 106 | PASS |
| SA Op EBITDA YoY | +83.2% | (103.46-56.47)/56.47 = +83.2% | 118/114/115/107 | PASS |
| SA Op EBITDA margin | +679 bps | 24.47-17.68 = 6.79pp | 106/114/115/107/118 | PASS |
| SA finance cost YoY | -20.4% | (26.94-33.85)/33.85 = -20.4% | 115 | PASS |
| SA PAT YoY | +81.3% | (7214.24-3979.96)/3979.96 = +81.3% | 126 | PASS |
| CON revenue YoY | +27.2% | (45592.56-35834.12)/35834.12 = +27.2% | 168 | PASS |
| CON Op EBITDA YoY | +111.9% | (115.87-54.69)/54.69 = +111.9% | 180/176/177/169 | PASS |
| CON Op EBITDA margin | +1,015 bps | 25.41-15.26 = 10.15pp | 168/176/177/169/180 | PASS |
| CON finance cost YoY | +93.8% | (141.22-72.88)/72.88 = +93.8% | 177 | PASS |
| CON other income YoY | -38.7% | (552.49-902.00)/902.00 = -38.75% -> -38.7% | 169 | PASS |
| CON core PBT ex-OI YoY | +151.7% | (10067.87-3999.34)/3999.34 = +151.7% | 180/169 | PASS |
| CON PAT total YoY | +113.9% | (7811.77-3652.72)/3652.72 = +113.9% | 188 | PASS |
| CON PAT owners YoY | +97.2% | (7493.66-3799.98)/3799.98 = +97.2% | 190 | PASS |

### QoQ walk (A4 Step 3C)

| Metric | A4 | Recomputed | Source (extract L) | Status |
|---|---|---|---|---|
| CON revenue QoQ | +15.5% | (45592.56-39478.64)/39478.64 = +15.5% | 168 | PASS |
| CON Op EBITDA margin QoQ | +154 bps | 25.41-23.87 = 1.54pp | 168/176/177/169/180 | PASS |
| CON core PBT QoQ | +28.9% | (100.68-78.12)/78.12 = +28.9% | 180/169 | PASS |
| CON volume QoQ | -21.0% | (21587-27341)/27341 = -21.04% | press L82 | PASS |

### Standalone-vs-consolidated PAT gap (A4 Table 1E) — first-class metric

| Period | A4 gap / % | Recomputed (CON total PAT - SA PAT) | Source (extract L) | Status |
|---|---|---|---|---|
| Q1FY26 | -3.27 / -8.22% | 3652.72-3979.96 = -327.24 -> -3.27; /3979.96 = -8.22% | 188/126 | PASS |
| Q4FY26 | +2.90 / +4.69% | 6477.05-6186.60 = +290.45 -> +2.90; /6186.60 = +4.69% | 188/126 | PASS |
| Q1FY27 | +5.98 / +8.28% | 7811.77-7214.24 = +597.53 -> +5.98; /7214.24 = +8.28% | 188/126 | PASS |
| FY26 | +3.63 / +2.19% | 16915.68-16552.83 = +362.85 -> +3.63; /16552.83 = +2.19% | 188/126 | PASS |
| YoY swing | ~16.5pp | -8.22 -> +8.28 = 16.50pp | — | PASS |
| NCI swing | -1.47 -> +3.18 | (147.26) -> 318.11 (Lakh) | 191 | PASS |

### PAT bridges (A4 Step 4A/4B)

| Check | A4 | Recomputed | Status |
|---|---|---|---|
| CON PAT total change | +41.59 | 78.12-36.53 = +41.59 | PASS |
| CON gross-profit change | +56.62 | (455.93-246.09-6.89)-(358.34-166.25-45.76) = 202.95-146.33 = +56.62 | PASS |
| CON Op EBITDA change | +61.18 | 115.87-54.69 = +61.18 | PASS |
| CON tax drag | -15.60 | 12.49-28.09 = -15.60 | PASS |
| SA PAT change | +32.34 | 72.14-39.80 = +32.34 | PASS |
| SA Op EBITDA change | +46.99 | 103.46-56.47 = +46.99 | PASS |

### ~60%/MT realization inference (A4 Step 2D)

| Metric | A4 | Recomputed | Source | Status |
|---|---|---|---|---|
| CON realization Q1FY26 (Lakh/MT) | 1.30 | 35834.12/27570 = 1.300 | L168 / press L82 | PASS |
| CON realization Q1FY27 (Lakh/MT) | 2.11 | 45592.56/21587 = 2.112 | L168 / press L82 | PASS |
| CON realization YoY | ~+62% | 2.112/1.300 = +62.5% | " | PASS |
| SA realization YoY | ~+59% | (42273.75/20619)/(31937.88/24847) = 2.050/1.285 = +59.5% | L106 / press L82 | PASS |
| "~60%" inference | matches A3 ~60% | CON +62.5%, SA +59.5% -> ~60% band | — | PASS |
| CON volume YoY | -21.7% | (21587-27570)/27570 = -21.70% | press L82 | PASS |
| Other-expense ratio move (CON) | -640 bps | 71.16/358.34=19.86% -> 61.24/455.93=13.43% = -6.43pp | L178/168 | PASS |
| ROCE annualised proxy | ~19% | (10761.58x4)/(266722.79-43742.82) = 43046.32/222979.97 = 19.3% | L243/259/264 | PASS |
| Segment liabilities QoQ | -153.39 | 59081.80-43742.82 = 15338.98 L = -153.39 | L264 | PASS |

Cross-check of press-stated EBITDA/margins to filing (A4 L118/L134): SA reported EBITDA
109.63/63.74/94.49 -> press 110/64/94 (L76); CON 121.40/63.71/101.99 -> press 121/64/102;
press margins reconcile on Total Income denominators (SA 109.63/428.91=25.6%->26%; CON
121.40/461.45=26.3%->26%). **Confirmed — A4's denominator identification (press "Total Revenue"
= filing Total Income, not revenue from operations) is arithmetically correct at every cell.**

Deferred-tax OCR "&" cell (CON Q1FY26, L185): implied deferred tax = 1248.62-1088.68-159.94 =
0.00, so the total tax 12.49 A4 uses is unaffected. **No arithmetic exposure.**

**ARITHMETIC VERDICT: PASS.** Every derived metric recomputes to A4's value within rounding.
Several figures that look off at A4's 2-decimal Cr presentation (SA fin-cost -20.4%, CON
fin-cost +93.8%, CON OI -38.7%, Q4FY26 SA Op EBITDA 86.08, Q1FY27 gap 8.28%) all resolve
EXACTLY to A4's stated value when recomputed at raw-Lakh precision. No mismatch above rounding.

---

## AUDIT 3 — ADVERSARIAL READ

A4's three most positive claims, each with the strongest bear counter built FROM THE SAME
EXTRACTED TEXT, and whether the counter survives as something A4 does NOT already contain.

### Claim 1 (A4 L190, L295, L575): "Earnings quality is exceptionally clean — ~100%+ recurring, other income DECLINED (not inflating PAT), zero exceptionals; growth is real operating growth, not treasury-driven."

**Bear counter:** The "recurring" label is doing more work than the evidence supports. The
entire operating gain sits on a ~60% YoY realization step-up (L106/L168 vs press L82) against
a 21.7% volume fall; a price/spread expansion is not obviously "recurring." A material slice
of the EBITDA lift is a -640 bps other-expense-ratio drop (L178) on a SHRINKING tonnage base,
which is as consistent with transient variable-cost relief as with durable efficiency.

**Survives? NO — already fully in A4.** Step 4C states verbatim "the recurring line is real
but its base-rate durability is unproven" and Step 2D flags the -640 bps other-expense move as
"a legitimate question." The strongest counter is already incorporated. Not grafted.

### Claim 2 (A4 L188, L574): "Consolidated op EBITDA margin expanded +1,015 bps to 25.41%; PAT owners +97.2% — a genuinely strong, clean print."

**Bear counter:** The print is NOT broad-based, and part of the YoY margin optics is a
depressed comparator. (a) The Hotel Division — the company's own "diversified portfolio"
plank (MD quote L154-156) — DETERIORATED: segment revenue 1,026.54 -> 798.81 L (-22% YoY,
extract L234) and segment PBIT 390.02 -> 159.78 L (-59% YoY, L241). 100% of the profit growth
is one price-led segment (Amines & Speciality), so "strong print" masks a narrowing, not a
broadening, base. (b) The +1,015 bps is measured off a Q1FY26 consol op-EBITDA margin of
15.26% that was itself depressed by the loss-making subsidiary (NCI -1.47, L191), flattering
the YoY delta.

**Survives? PARTIALLY — the Hotel-Division deterioration is NEW to A4.** A4 never cites the
per-division segment RESULTS rows (L233-253) and nowhere notes the Hotel Division halving; its
"strong/clean" framing and its treatment of the "diversified portfolio" claim are silent on the
one diversification line that shrank. The depressed-base sub-point is partly covered (A4 does
attribute low Q1FY26 consol margin to BSC). **The Hotel-Division-not-broad-based counter is
grafted (secondary).**

### Claim 3 (A4 L145, L408, L576): "Sole subsidiary BSC turned profit-accretive — S-vs-C PAT gap -8.22% -> +8.28%, NCI -1.47 -> +3.18 Cr — a REAL NEW GROWTH VECTOR / the single live growth vector."

**Bear counter (strongest of the three):** BSC's swing CANNOT be a "growth" vector in the
volume sense, because the extract shows volume fell EVERYWHERE — consol -21.7% and standalone
-17.0% (press L82). Worse, the BSC-attributable slice fell hardest: implied external BSC volume
(consol minus standalone) collapsed from 27,570-24,847 = 2,723 MT (Q1FY26) to 21,587-20,619 =
968 MT (Q1FY27), roughly -64% (press L82, both books). So a subsidiary whose implied volume
fell ~64% swung to profit purely on realization/price/cost — it is the MOST extreme instance of
the same unproven-durability problem, not an independent growth engine. Compounding this: BSC
is not separately segmented (only "Amines & Speciality Chemicals" + "Hotel", L233-253; Note 3
L299-301), so the ONLY evidence of a "turnaround" is an accounting allocation (the S-vs-C gap
and NCI), with no BSC-level volume, price, or capacity number in the document set to support
"growth vector."

**Survives? YES — and it directly contradicts A4's own characterisation.** A4 poses a generic
driver question (Step 8.5 Q3: "volume, price, mix, or one-off") but then asserts in the Combined
Verdict (L576) and Step 1E (L145) that BSC is "a real new growth vector" and "the single live
growth vector" — a confidence the extract's across-the-board volume decline does not license.
A4 never computes or notes that group volume fell everywhere (so nothing volume-led can be
attributed to BSC) and never surfaces the ~64% implied-BSC-volume collapse. This counter is
extract-grounded, material to the most-emphasised positive claim, and absent from A4.
**MUST BE GRAFTED into Step 1E and Section C: recharacterise BSC as a realization/margin-recovery
contributor of unproven durability, not a "growth vector," and state that group volume fell in
BOTH books so BSC's swing is definitionally not volume-led (implied BSC volume proxy ~-64% YoY).**

---

## VERDICT

**INCOMPLETE.**

- Coverage audit: PASS (all fresh counts reconcile to both ledgers; no orphan rows; no rows
  missing from the ledger).
- Arithmetic audit: PASS (every derived metric recomputes to A4's value within rounding;
  standalone/consolidated margins, YoY/QoQ walks, S-vs-C PAT gap per period, effective tax
  rate, PAT bridges, and the ~60%/MT realization inference all verified).
- Adversarial read: one PRIMARY surviving bear counter (Claim 3, BSC is not a volume/"growth"
  vector — group volume fell in both books, implied BSC volume ~-64% YoY, BSC not separately
  segmented) and one SECONDARY surviving counter (Claim 2, Hotel Division revenue -22% / PBIT
  -59% YoY makes the print not broad-based) are supported by the extract and are NOT present in
  A4. Per A5 rule, a surviving counter must be added before save.

**Loop back to: A4.**

**Exact gap:** A4's Combined Verdict (L576) and Step 1E (L145) assert BSC as "a real new growth
vector / the single live growth vector" without incorporating that the extract's own volume
figures (press L82) show consol -21.7% and standalone -17.0%, i.e. no volume growth anywhere,
with the implied BSC-attributable volume (consol minus standalone) falling ~64% YoY (2,723 ->
968 MT) — so BSC's turnaround is realization/margin-driven of unproven durability, not a growth
vector; and BSC is not separately segmented (L233-253, Note 3 L299-301), so the swing rests
only on an accounting allocation. Secondary: A4 omits the Hotel Division deterioration
(revenue 1,026.54 -> 798.81 L, PBIT 390.02 -> 159.78 L; extract L234/L241), which qualifies the
"strong/clean, diversified-portfolio" framing. A4 must graft both counters (primary into Step 1E
+ Section C; secondary into Step 2/Section C) and re-emit for A5 re-check.

---

```yaml
stage: A5-adversary
company: "BALAMINES"
quarter: "Q1 FY27"
model: claude-opus-4-8
status: complete
verdict: INCOMPLETE
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches: []
surviving_bear_counters:
  - claim: "BSC turned profit-accretive; A4 calls it 'a real new growth vector / the single live growth vector' (A4 L145, L408, L576)"
    counter: "Group volume fell in both books (consol -21.7%, standalone -17.0%; press L82) so nothing volume-led can be attributed to BSC; implied BSC-attributable volume (consol minus standalone) fell ~64% YoY (2,723 -> 968 MT); BSC is not separately segmented (extract L233-253, Note 3 L299-301). BSC's swing is realization/margin-recovery of unproven durability, not a growth vector."
    source_line: "press extract L82; results extract L188/L190/L191/L233-253/L299-301"
  - claim: "Consol op EBITDA margin +1,015 bps to 25.41% and PAT owners +97.2% = a strong, clean, diversified print (A4 L188, L574-575)"
    counter: "Print is not broad-based: Hotel Division revenue fell -22% (1,026.54 -> 798.81 L) and PBIT fell -59% (390.02 -> 159.78 L) YoY; 100% of profit growth is one price-led segment, undercutting the 'diversified portfolio' framing."
    source_line: "results extract L234/L241/L251"
loop_back_to: "A4"
gap: "A4 asserts BSC as a 'real new growth vector' (L145/L576) without incorporating that consol (-21.7%) and standalone (-17.0%) volume both fell (press L82) and implied BSC volume fell ~64% YoY, so the turnaround is realization/margin-driven of unproven durability, not growth; BSC is not separately segmented (L233-253, Note 3). A4 also omits the Hotel Division deterioration (rev -22%, PBIT -59%; L234/L241). Graft both counters and re-emit."
```
