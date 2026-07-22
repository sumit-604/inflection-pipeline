# A5 ADVERSARY / COMPLETENESS AUDIT — SOUTHWEST (South West Pinnacle Exploration Ltd) — Q1 FY27

Agent A5, re-audit of the **now-merged Role 4 + Role 5 review** (concall present this run). Fresh
context: only the A4 review, the three A1 extracts (results, presentation, concall), and the three
A2 ledgers were read. Enumeration re-run independently; every derived metric recomputed from raw
tokens (deck Rs Mn ×0.1 → Rs Cr; concall native Rs Cr ×1); every concall line-citation checked
against the extract through the ASR glossary. I re-derive; I do not defer to A4's, A3's, or the
prior-run A5's cites.

**Continuity note.** The output path held a STALE prior-run A5 audit (its header: "the two A1
extracts + the two A2 ledgers only" — i.e. the Role-4-only run before the concall existed). That
audit returned INCOMPLETE on two gaps: (i) an arithmetic error "Q1 FY26 ~66% of the non-Q1
run-rate", and (ii) an unincorporated margin-durability bear counter. I independently re-checked
BOTH against the current merged review and find **both resolved** (evidence below). This file
supersedes the stale one.

---

## AUDIT 1 — COVERAGE (fresh grep pass vs A2 ledgers; then A2 ledgers vs A4)

### 1A. Fresh enumeration vs A2 counts

| Category | A2 count | My fresh count | Method | Orphan | Status |
|---|---|---|---|---|---|
| Results: numbered notes | 0 | 0 | `^\s*\d+\.` = 0; 4-pg release, not Reg 33 | none | PASS |
| Results: financial line items (L86-90) | 5 | 5 | Income/EBITDA/EBITDA%/PAT/PAT% | none | PASS |
| Results: Q1 highlight bullets (L92-111) | 13 | 13 | bullet sweep | none | PASS |
| Results: CMD commentary claims (L115-148) | 9 | 9 | Jain-attributed paras | none | PASS |
| Results: absent Reg-33 unit classes (K1-K15) | 15 | 15 | 0-hit greps confirm structural absence | none | PASS |
| Results: total rows A–L | 70 | 70 | full sweep | none | PASS |
| Presentation: slides | 40 | 40 | formfeed + page markers | none | PASS |
| Presentation: financial line items | 80 | 80 | p33 16 + p35 16 + p36 42 + p38 6 | none | PASS |
| Presentation: chart data points | 110 | 110 | 8+8+6+11+25+6+12+32+2 | none | PASS |
| Presentation: footnotes | 7 | 7 | Table 7 | none | PASS |
| Presentation: ZERO_STANDING rows | 7 | 7 | OCI, held-for-sale, CTL, CWIP, NCI/Loans | none | PASS |
| Concall: turns | 83 | **83** | blank-line blocks, odd lines 23-187: (187−23)/2+1 = 83 | none | PASS |
| Concall: strict `?`-terminated questions | 35 | **35 (24 lines)** | independent grep confirms exactly **24 distinct lines** carry `?` (ledger's stated spread); 35 tokens reconcile | none | PASS |
| Concall: implied Qs (no terminal `?`) | 7 | 7 | IQ1–IQ7 | none | PASS |
| Concall: management numeric tokens | 155 | 155 | regex token sweep; ledger row-by-row token-sum reconciles to 155; 20+ rows spot-checked verbatim | none | PASS |
| Concall: participants | 11 announcements / 14 named | 14 named (P1–P14) | A4 uses the 14 named; 11 is the "from the line of" count | none | PASS |

Fresh pass found **no row the ledgers lack**. `missing_from_ledger = []`.

### 1B. Every ledger row cited in A4 OR reviewed-no-finding (orphan check)

Finding-bearing rows verified individually; administrative rows (letterhead, addressees, signature,
contact, project photos, macro/industry charts) fall under A4's blanket "all rows/slides read"
with no finding — acceptable.

- Results TITLE_LABEL_MISMATCH (B5/D0b, Q-on-Q vs Y-on-Y) → F14-01, Step 3. ✓
- Results F2 standalone "on similar lines" (unanchored) → First-Class Metric / Q4. ✓
- Results F3 CMD "substantial increase in input cost" (L122-123) → **now reconciled** into the
  margin-durability flag (Step 2 diag-2 L147; Watchlist #13; caveat 10; Q19). ✓
- Results G3/L1 Alara entity relationship → F14-02 / RPT. ✓
- Presentation Slide 8 Ritolia caption-vs-body → F14.1 / Q15 monitorable. ✓
- Presentation Slide 22 coal FY2027-28 → covered as the F16-01 contradiction vs concall FY28-29. ✓
- Presentation Slide 37 ROCE 16% vs Snapshot "23%" → F16.4, Step 7. ✓
- Presentation Slide 30 AHML 17.5% / ARL rights → covered. ✓
- Concall: all 9 analysts' topics (Q1–Q35, IQ1–IQ7) map to A4 Step 4A inventory + the 19-question
  answered/evaded scorecard (Step 3E); NO_RESPONSE (Sahir Duala) noted in participants; both ledger
  "most material" conflicts carried — FY27-28-vs-FY28-29 (F16-01) and 10-yr-vs-11-yr (F14-01). ✓
- Presentation Slide 9 map (~14 state labels) vs "8 States" (Slide 32): all-time footprint vs
  current ops; ledger itself deferred as a benign cross-check; within A4 blanket slide review — not
  a material orphan.

**No orphan finding-bearing row (no FAIL to A3). No missing row (no FAIL to A2).**
`orphan_rows = []`.

**COVERAGE VERDICT: PASS.**

---

## AUDIT 2 — ARITHMETIC (recomputed from raw tokens)

| Metric | A4 value | My recompute (raw source) | Source | Status |
|---|---|---|---|---|
| Op EBITDA Q1FY27 (Rev−TotExp) | 14.9 | 61.7−46.8 | L1033/35 | OK |
| Op EBITDA margin Q1FY27 / Q1FY26 | 24.15% / 14.43% | 149/617 ; 58/402 | L1037/33 | OK |
| Reported EBITDA Q1FY27 (PBT+D+Fin) | 16.6 | 11.9+3.0+1.7 | L1051/43/45 | OK |
| Core Op PBT ex-OI / ex-OI ex-JV Q1FY27 | 11.5 / 10.2 | 11.9−0.4 ; 10.6−0.4 | L1051/47/41 | OK |
| ETR Q1FY27 / pre-JV | 21.8% / 24.5% | 26/119=21.85% ; 26/106=24.53% | L1053/51/47 | OK |
| Revenue / Op EBITDA / margin-bps YoY | +53.5% / +156.9% / +972 | 215/402 ; 91/58 ; 2415−1443 | L1033/37/39 | OK |
| Core ex-OI / ex-OI ex-JV YoY | +475% / +500% | 9.5/2.0 ; 8.5/1.7 | der. | OK |
| Reported PBT / PAT / EPS YoY | +283.9% / +287.5% / +287.3% | 88/31 ; 69/24 ; 2.27/.79 | L1051/55/63 | OK |
| PAT bridge → PAT | +9.1/+7.8/+1.0/−1.9 → +6.9 | ties 9.3−2.4 both ways | L1037-55 | OK |
| JV share of consolidated PAT | 14.0% | 1.3/9.3=13.98% (deck); 1.32/9.3=14.19% (concall) | L1049/L109/L1055 | OK (within rounding) |
| JV normalise → PAT / margin | ~8.4 / ~13.6% | 9.3−(1.32−0.35)=8.33 ; 8.4/61.7=13.6% | L1092/L109 | OK |
| Receivable days FY25 / FY26 | 154.5 / 175.0 | 763/1803×365 ; 1166/2430×365=175.2 | L1132/76 | OK |
| Inventory / Payable days FY26 | 100.6 / 45.9 | 509/1847×365 ; 232/1847×365 | L1129/33/78 | OK |
| Cash conversion cycle FY26 | ~230 | 175.0+100.6−45.9=229.7 | der. | OK |
| Cash & equiv FY25→26 | 19.4→1.3 (−93%) | 194→13 (−93.3%) | L1134 | OK |
| Gross borrowings / net debt FY26 | 78.6 / 77.3 | 160+626 ; 78.6−1.3 | L1120/31/34 | OK |
| Order book net QoQ add | +180.1 (+31.0%) | (7613−5812)/10 ; /581.2 | L546 | OK |
| ROCE base (0.5×ROCE+7.5) | 15.5x / 19x | 0.5×16+7.5 ; 0.5×23+7.5 | L1170/L94 | OK |
| FY26 non-Q1 run-rate | ~67.6 | (243.0−40.2)/3 = 67.6 | L1076/33 | OK |
| **Q1 FY26 as % of non-Q1 run-rate** | **~60% (59.5%)** | **40.2/67.6 = 59.47%** | **review L146; pres L1033/L1076** | **OK — CORRECTED** |

**Prior-run FAIL re-checked and RESOLVED.** The stale audit failed A4 for stating "Q1 FY26 ~66% of
the non-Q1 run-rate" in five places. The current merged review (L146) reads "Q1 FY26 (Rs 40.2 Cr)
was **~60% (59.5%)** of that" — the correct ratio (40.2/67.6 = 59.5%). A full-text grep finds **no
remaining "66%"** anywhere in the merged review. Corrected. No arithmetic mismatch survives.

Within-rounding note (not a FAIL): JV-share-of-PAT is labelled "1.32/9.3 = 14.0%"; the literal
quotient is 14.2%, while the deck-rounded 1.3/9.3 = 14.0%. Both inputs legitimately sourced, 0.2pp
gap, material conclusion ("~14% of PAT from the JV") unchanged.

Concall line-citation spot-check (23 cites: L27,47,59,69,73,79,89,93,105,109,111,127,139,141,145,
149,155,157,171,175,179,181,183) — all carry the attributed text through the ASR glossary (HZL "7
crores"=307 at L27, resolved L71; RIL "160/166"=166; "2829"=FY28-29). No citation defect.

`arithmetic_mismatches = []`. **ARITHMETIC VERDICT: PASS.**

---

## AUDIT 3 — ADVERSARIAL READ (three most positive claims; strongest bear counter from same text)

**Positive 1 — "Headline growth is REAL, not treasury-led: core ex-OI +475%, ex-JV +500% (Rs 10.2
Cr); ~100%+ of PAT growth recurring/operating" (Step 2 verdict L147; Step 4 L196).**
Same-text counter: +500% off a Rs 1.7 Cr seasonally-weakest base (L1047); Q1FY27 revenue 61.7 <
non-Q1 run-rate 67.6 (L1076); profit uncorroborated by cash (CFO refused, L105); JV +Rs 1.0 Cr
(14% of PAT) non-cash (L111); receivables 76.3→116.6, cash 19.4→1.3 (L1132/L1134).
**Does not survive as new** — all incorporated: cash INDETERMINATE cap, seasonality-confirmed, JV
non-cash flag, receivable build. Verdict already capped at PROCEED WITH CAVEATS.

**Positive 2 — "EBITDA margin +972 bps to record 24.15%, holding the FY26 step-up; operating
leverage genuine" (Step 2 diag-2 L147).**
Same-text counter: record 24.15% (only +16 bps over FY26 full-year 23.99%, L1082) printed in the
seasonally weakest quarter, cost stack ND (materials/employee/other = K9-K13; Q19 refused, L171),
while the CMD admits a "substantial increase in input cost" (results L122-123) — could be
project-mix or cost-recognition timing as the Rs 307 Cr Rajasthan core-drilling order commences.
**Does not survive as new — NOW INCORPORATED.** The prior-run audit flagged this exact counter as
surviving because the Role-4-only draft "framed the margin only as holding and never reconciled the
input-cost admission." The merged review (L147) now states verbatim: *"The CMD's press-release
'substantial increase in input cost' (results L122-123) was NOT reconciled on the call. Could be
project-mix or cost-recognition timing."* It is further carried as Watchlist #13 (L295), Growth-
trigger row (L320), Caveat 10 (L771), Q19 (L417) and 8F management question 10 (L852). Fully grafted;
no residual gap.

**Positive 3 — "Order book all-time high Rs 761 Cr, 3-5 yr visibility; utilization >100%; CRISIL
BBB→BBB+" (Section C positives; Step 6E).**
Same-text counter: "+31% / all-time high" is a gross closing balance — net QoQ add only Rs 180.1 Cr,
smaller than the single pre-booked Rs 307 Cr HZL order that merely "kicked off 1.5 months back"
(L73); ~60% of BOTH book and revenue is two contracts (L79); HZL Q1 recognition minimal (gate 2
cannot clear); CRISIL BBB+ coexists with the unreconciled Rs 15-vs-78.6 Cr debt discrepancy
(L93 vs L1120/1131).
**Does not survive as new** — Step 6E is built on precisely this double-count; F16-02 concentration,
F11-01 debt discrepancy, and "CRISIL does not resolve the CFO question" (Step 7C) all present.

**Additional probes for a NEW surviving counter:**
- Finance cost fell (2.0→1.7) while gross borrowings ROSE 62.9→78.6 (L1088/L1120/L1131): mild
  tension, but rising borrowings + F11-01 already flagged; small line, FY26-year-end-weighted. Not
  material enough to graft.
- Concall L47 (JV1 profit "3-4 Cr, our share 35%" → ~1.05-1.4 Cr/qtr ≈ the Rs 1.32 Cr reported)
  would UNDERCUT A4's "lump/recurrence-unconfirmed" framing — but that is a BULL counter, and A4's
  conservative JV treatment is permitted by the house conservative-bias rule.
- No other extract-supported bear counter found that A4 has not surfaced.

`surviving_bear_counters = []`. **ADVERSARIAL VERDICT: PASS.**

---

## VERDICT

**COMPLETE.**

- COVERAGE: PASS. Fresh enumeration reproduces 70 results rows / 40 slides (80 line items, 110 chart
  points, 7 footnotes) / 83 concall turns, 35 strict questions (24 `?`-bearing lines independently
  confirmed), 7 implied questions, 155 management numbers. No orphan finding-bearing row; nothing the
  ledgers lack.
- ARITHMETIC: PASS. Every derived metric reconciles within rounding. The prior-run "66% vs 60%" FAIL
  is RESOLVED — the merged review now states 59.5% (~60%) and no "66%" remains.
- ADVERSARIAL: PASS. The three most positive claims each yield a strong same-text bear counter; all
  three are already incorporated — including the margin-durability / input-cost counter the prior run
  flagged as surviving, now fully grafted (L147, Watchlist #13, Caveat 10, Q19, 8F-Q10). No new
  surviving counter.

Both prior-run gaps that held this review INCOMPLETE are closed in the merged Role 4 + Role 5
review. Cash conversion remains correctly INDETERMINATE (verdict floored at PROCEED WITH CAVEATS per
house rule) — a substantive verdict, not a coverage/arithmetic defect. This review proceeds to Notion
save.

`loop_back_to = ""`. `gap = ""`.

```yaml
stage: A5-adversary
company: "SOUTHWEST"
quarter: "Q1 FY27"
model: claude-opus-4-8
status: complete
verdict: COMPLETE
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches: []
surviving_bear_counters: []
loop_back_to: ""
gap: ""
```
