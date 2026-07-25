# A5 ADVERSARY / COMPLETENESS AUDIT — Route Mobile Limited (ROUTE) — Q1 FY27

Agent: A5 ADVERSARY (Opus 4.8). Fresh context: A4 review + A1 extracts + A2 ledgers only.
Enumeration re-run independently; every derived metric recomputed from raw extract numbers; A4's and
A3's cites checked, not trusted. This cycle includes the concall (full Role 5).
Units re-derived at source: results Crores (x1), presentation Millions (x0.1), pressrelease Crores
(x1), concall Millions (x0.1; ASR auto-transcript). Verdict set: COMPLETE | INCOMPLETE.

---

## AUDIT 1 — COVERAGE (fresh grep/sweep vs A2 ledger; then A4-citation check)

| Category | A2 count | My fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Results — notes | 22 | 22 (consol 9 + std 9 main + 4 sub-lettered: consol 4a/7a/7b, std 4a) | none | PASS |
| Results — line_items | 94 | 94 (ConsolA 39 + SegB 21 + StdA 22 + IPOx2 10 + forex 1 + divsub 1) | none | PASS |
| Results — zero_standing | 16 | 16 | none | PASS |
| Results — agenda_items | 4 | 4 (results, AGM, ₹4 dividend, ESOP lapse) | none | PASS |
| Results — auditor_paras | 14 | 14 (consol 6 numbered + 4 continuation; std 4 numbered) | none | PASS |
| Results — entities | 33 | 33 (Annexure I L251-284; ties note C-1 "33 subsidiaries") | none | PASS |
| Results — signature_blocks | 8 | 8 (Shah + Mundra x2 + Gupta x5) | none | PASS |
| Results — annexures | 2 | 2 | none | PASS |
| Presentation — slides | 18 | 18 | none | PASS |
| Presentation — numbers | 121 rows / 381 tokens | 121 / 381 (row & token sub-sums reconcile) | none | PASS |
| Presentation — zero_standing | 6 | 6 (all slide 16) | none | PASS |
| Presentation — footnotes | 10 | 10 | none | PASS |
| Press release — slides | 3 | 3 | none | PASS |
| Press release — numbers | 33 | 33 | none | PASS |
| Press release — mgmt_claims | 9 | 9 | none | PASS |
| Press release — disclaimer / signatories | 1 / 2 | 1 / 2 | none | PASS |
| Concall — participants | 9 (+1 absentee) | 9 in-transcript + MD absentee (MGMT_ABSENCE) | none | PASS |
| Concall — turns | 91 | 91 (even lines 24-204: (204−24)/2+1 = 91) | none | PASS |
| Concall — questions | 37 | 37 (Divy 2 + Bharat-r1 7 + Deep Ma 10 + Amit 6 + Kevin 6 + Bharat-r2 6) | none | PASS |
| Concall — mgmt_numbers | 34 | 34 | none | PASS |
| Concall — forward_commitment | 35 | 35 | none | PASS |
| Concall — hedge_phrases | 20 | 20 | none | PASS |

**Rows my fresh pass found that the ledger lacks (missing_from_ledger):** none. No atomic row in any
of the four extracts is absent from the A2 ledgers.

**A4-citation check.** A4's ledger-reconciliation preamble reproduces all four A2 count vectors
EXACTLY (results 22/94/16/4/14/33/8/2; presentation 18/381-121/6/10; press release 3/33/9/1/2;
concall 9+1/91/37/34/35/20) and asserts no ledger row is unreviewed. I traced the load-bearing rows:
- Consol P&L (39), segment (21), standalone (22) → Steps 1/2/4b. IPO Rs 65 Cr unutilised, QIP Rs
  867.50 Cr, forex note C-6, exceptional 7a/7b, dividend, re-grouping, subs-dividend Rs 4.22, cash-
  flow-hedge OCI −3.80, FCTR 16.27 → all carried in Section A / QFM / monitorables.
- Auditor reliance (24 component subs Rs 660.94/Rs 24.19 Cr; 11 foreign; 7 unreviewed Rs 1.12/Rs 0.02
  Cr) → 0D + AMBER data-reliance flag. ESOP lapses (1,250 + 22,000) → 0C / checklist 12.
- Concall task item 2 (91 turns / 37 Q / 34 numbers): all 37 questions individually rowed with turn
  refs + response grades (Step 4A); all 34 mgmt numbers covered across Step 1, Step 5A, Step 7A; 35
  forward + 20 hedge phrases consumed in Step 6B/6C counts; all 91 turns accounted for (T2-T4 Step 1,
  T5-T88 Step 4A, operator/close Step 0C). MGMT_ABSENCE, ASR_MERGED_SPEAKERS, UNANSWERED_QUESTION
  (Q14), REPEAT_QUESTION (7) all surfaced. No concall row orphaned.
- Press release: 9 mgmt claims → R5 Step 1 inventory; NO_SAFE_HARBOR / UNSPECIFIED_MARKET_FACTORS /
  NO_PRIOR_MARGIN_COMPARATOR (7.94% PBT margin) all covered; ROLE_NOT_STATED trivial.

**COVERAGE VERDICT: PASS.** No orphan rows; nothing missing from the ledger; A4 counts reproduce A2.

---

## AUDIT 2 — ARITHMETIC (recomputed from raw extract numbers; A4 value vs recomputed vs source)

Raw consol anchors (Rs Cr): Rev 1,151.51/1,130.90/1,050.83/4,408.21 (L304); OI 11.06/27.85/10.97/54.09
(L305); msg 911.07/866.99/825.76/3,400.90 (L309); emp 77.62/74.86/68.59/288.85 (L310); fin
1.36/1.20/5.82/10.82 (L311); D&A 23.71/23.61/22.48/91.61 (L312); other exp 57.34/52.82/62.58/181.21
(L313); PBT-pre-exc 91.47/139.27/76.57/488.91 (L317); PBT 91.47/139.27/76.57/353.04 (L321); tax
22.92/24.84/17.79/96.10 (L326); PAT 68.55/114.43/58.78/256.94 (L329). Deck (mn x0.1): adj-EBITDA
1,089.3/1,343.0/1,153.9 (L481); adj-PAT 685.5/1,144.3/587.8 (L492); reported-PAT 685.5/1,144.3/587.8 (L489).

| Metric | A4 value | Recomputed | Source | Status |
|---|---|---|---|---|
| Gross profit Q1FY27 | 240.44 | 1,151.51−911.07 = 240.44 | L304/309 | MATCH |
| Gross margin Q1FY27 / Q1FY26 | 20.88% / 21.42% | 240.44/1,151.51; 225.07/1,050.83 | derived | MATCH |
| Operating EBITDA Q1FY27 (PBT+D+FC−OI) | 105.48 | 91.47+23.71+1.36−11.06 | L317/312/311/305 | MATCH |
| Op EBITDA margin Q1FY27 | 9.16% | 105.48/1,151.51 | derived | MATCH |
| Op EBITDA Q1FY26 | 93.90 | 76.57+22.48+5.82−10.97 | derived | MATCH |
| Reported EBITDA Q1FY27 (PBT+D+FC) | 116.54 | 91.47+23.71+1.36 | derived | MATCH |
| Core PBT ex-OI Q1FY27 | 80.41 | 91.47−11.06 | derived | MATCH |
| OI/PBT Q1FY27 | 12.09% | 11.06/91.47 | derived | MATCH |
| OI/PBT FY26 | 15.32% | 54.09/353.04 (reported-PBT basis) | L305/321 | MATCH (basis noted) |
| Effective tax rate Q1FY27 | 25.06% | 22.92/91.47 | L326/317 | MATCH |
| ETR FY26 | 27.22% | 96.10/353.04 (reported PBT) | L326/321 | MATCH |
| Current-tax-only rate Q1FY27 | ~30% | 27.66/91.47 = 30.24% | L324/317 | MATCH |
| PAT margin Q1FY27 | 5.95% | 68.55/1,151.51 | derived | MATCH |
| Revenue YoY | +9.58% | 100.68/1,050.83 = 9.581% | derived | MATCH |
| Gross profit YoY | +6.83% | 15.37/225.07 | derived | MATCH |
| GM YoY / QoQ change | −54 bps / −246 bps | 20.88−21.42; 20.88−23.34 | derived | MATCH |
| Operating EBITDA YoY | +12.33% | 11.58/93.90 | derived | MATCH |
| Adj. EBITDA YoY | −5.60% | −6.46/115.39 | deck L481 | MATCH |
| Adj. EBITDA margin YoY | −150 bps | 9.5−11.0 | deck L483 | MATCH |
| Depreciation YoY | +5.47% | 1.23/22.48 | L312 | MATCH |
| Finance costs YoY | −76.63% | −4.46/5.82 | L311 | MATCH |
| EBIT (segment) YoY | +14.49% | 10.35/71.42 | L393-395 | MATCH |
| Core operating PBT YoY | +22.58% | 14.81/65.60 | derived | MATCH |
| Reported PBT YoY | +19.46% | 14.90/76.57 | L317 | MATCH |
| PAT YoY | +16.62% | 9.77/58.78 | L329 | MATCH |
| EPS YoY | +17.63% | 1.49/8.45 | L368 | MATCH |
| Revenue QoQ | +1.82% | 20.61/1,130.90 | derived | MATCH |
| Gross profit QoQ | −8.89% | −23.47/263.91 | derived | MATCH |
| Adj. EBITDA QoQ | −18.9% | −253.7/1,343.0 = −18.89% | deck L481 | MATCH |
| Adj. PAT QoQ (deck actual) | −40.0/−40.1% | −458.8/1,144.3 = −40.09% | deck L492/489 | MATCH |
| Adj. PAT YoY | +16.6% | 97.7/587.8 = 16.62% | deck L492 | MATCH |
| PAT QoQ | −40.09% | −45.88/114.43 | L329 | MATCH |
| Standalone Op EBITDA Q1FY27 | 5.57 | 20.25+3.90+0.39−18.97 | L600/596/595/589 | MATCH |
| Standalone Op EBITDA margin | 2.81% | 5.57/197.93 | derived | MATCH |
| Standalone GM Q1FY27 | 23.32% | 46.16/197.93 | L588/593 | MATCH |
| Standalone core PBT ex-OI | 1.28 | 20.25−18.97 | derived | MATCH |
| Standalone OI/PBT Q1FY27 | 93.68% | 18.97/20.25 | derived | MATCH |
| Standalone PAT YoY | −46.86% | −14.25/30.41 | L607 | MATCH |
| S-vs-C gap Q1FY27 / Q1FY26 / Q4FY26 / FY26 | 324.2/93.3/178.8/90.6% | 52.39/16.16; 28.37/30.41; 73.38/41.05; 122.16/134.78 | derived | MATCH |
| Standalone share of group PAT Q1FY27 | 23.6% | 16.16/68.55 = 23.57% | derived | MATCH |
| India segment result Q1FY27 (was +19.58) | −4.00 | L390 raw | L390 | MATCH |
| Overseas segment YoY | +65.0% | 33.75/51.92 | L391 | MATCH |
| OPEX growth YoY (7A) | +2.9% | (134.96−131.17)/131.17 = 2.89% | L310/313 | MATCH |
| Volume YoY / realization per txn | +16.5% / ~−6% | 6.5/39.3 = 16.54%; −5.97% | deck L392 | MATCH |
| New products YoY / QoQ / mix | 13.9% / 10.5% / 8.2% | 115/830; 90/855; 945/11,515 | deck L273/398 | MATCH |
| Net cash | Rs 1,345.2 Cr | 13,452 mn × 0.1 | deck L109 | MATCH |
| Deck EBITDA / GP tie | 105.48 / 240.44 | 1,054.8×0.1; 2,404×0.1 | deck L472/L94-derived | MATCH |
| Deck Adj-EBITDA recon | 1,089.3 mn | 1,054.8−28.1+49.0+13.6 | deck L472-481 | MATCH |
| Component-auditor revenue / PAT share | 57.5% / 35.3% | 662.06/1,151.51; 24.21/68.55 | L184/207/304/329 | MATCH |
| PR PBT margin | 7.94% | 91.47/1,151.51 = 7.944% | PR L78 | MATCH |
| PAT bridge (Step 4) | +14.90 PBT / +9.77 PAT | +GP15.37 −Emp9.03 +OExp5.24 −D&A1.23 +Fin4.46 +OI0.09 = +14.90; less tax 5.13 = +9.77 | derived | MATCH |

**Basis note (not a mismatch):** For the FY26 column A4 computes Core-PBT-ex-OI / Reported-EBITDA on
PRE-exceptional PBT (488.91) and OI/PBT / ETR on REPORTED PBT (353.04, post −135.87 exceptional). Each
ratio is defensible on its stated basis; the quarterly columns are unaffected (nil exceptional). No error.

**Spoken-vs-filing conflict re-verification (task item 3).** CFO spoken "Adjusted PAT ... lower by
14.1% sequentially" (ledger mgmt#25, T4 / concall L30). Deck adj-PAT 1,144.3→685.5 = **−40.09% QoQ**;
reported PAT 114.43→68.55 = **−40.09% QoQ**. Spoken −14.1% ties to NEITHER; no figure anywhere in the
extract reconciles to −14.1% (it is an ASR garble or a CFO misstatement). A4 flagged it correctly
(Section 7A + Section C + flag list + QFM #3), ruled the filing/deck (−40%) governs, and logged the
reconciliation question. Handling complete and correct.

**ARITHMETIC VERDICT: PASS.** Every derived metric recomputes within rounding. Zero mismatches.

---

## AUDIT 3 — ADVERSARIAL READ (A4's three most-positive claims; strongest bear from the same extract)

**Claim 1 — "Revenue +9.58% YoY clears the +1.8% bull binary; reads BULL" (Step 2 / Step 8).**
Bear from the extract: growth is bought with price, not value. Volume +16.5% (39.3→45.8 bn, deck L392)
against revenue +9.58% and GP +6.83% means realization/txn fell ~6% (Rs 0.267→0.251) and GM contracted
−54 bps YoY / −246 bps QoQ. QoQ revenue only +1.82%; volume QoQ near-flat. All growth is Overseas
(+65.0% segment result, L391); India swung to a −4.00 Cr operating LOSS (L390); standalone PAT −46.9%
(L607); NRR is 98% (T5) — net contraction. The binary is revenue-only and cannot override the FAILED
cap-5% GM gate (20.88% < 23%).
SURVIVES unincorporated? **NO.** A4 already states volume +16.5% / realization −6% (Step 2 verdict),
routes growth to Overseas with India at operating loss (Step 4b), flags NRR 98% (Step 5A), and rules
the BULL binary "revenue-only ... does not override the failed GM gate" (Step 8). Fully present.

**Claim 2 — "Management calls margin softness transient / 'restored in the coming quarter'" (Step 1 / PR).**
Bear from the extract: the "transient" label is unfalsifiable and self-contradicted. The quantified GM
bridge was REFUSED twice — "in terms of exact breakdown I'll need to just double check internally"
(T53/L128). Management RECALIBRATED the operating band DOWN to "21.5 to 23% which we've been operating
over the last five or six quarters" (T76/L174) — the 20.9% print is below even that floor and the 23%
ceiling is below the 25% thesis destination. FY27 numeric guidance WITHHELD after the miss (T24/L70).
Forex-neutral adj-EBITDA is −5.6% YoY (deck L481). The "restore next quarter" is a re-promise on a call
where the one prior hard commitment (CLO go-live) already SLIPPED (T62/L146).
SURVIVES? **NO.** A4 builds exactly this: exchanges 1-2, Grade C / EVASIVE archetype, GM-band-below-
thesis flag, "Anchor to the filing, not the narrative" (Step 4C), guidance-withheld / bridge-refused
flags. Fully present.

**Claim 3 — "Cash-conversion shortfall is timing, not structural; reverts to 75-100%" (Step 5 / mgmt).**
Bear from the extract: management's own words undercut "non-structural." CFO (T86/L86): the delayed
collections are "in specific geographies largely India and UAE and it's not a one-off I mean we've had
it in the past in instances" — a self-described RECURRING Q1 pattern, concentrated in the exact
geography (India) already in segment operating loss. No DSO figure was given (deflected); there is no
Reg-33 cash flow at Q1; net cash fell ~44 Cr QoQ; 75-100% is a forward PROMISE, not delivered data.
SURVIVES? **NO (conclusion already held).** A4 caps the cash axis at INDETERMINATE → PROCEED WITH
CAVEATS, refuses to credit the 75-100% promise ("a promise, not delivered data," Step 5 / 8D Pillar 2),
and names the missing evidence (CFO/DSO/WC). The bear conclusion is fully embodied. The specific
recurrence admission (T86, "not a one-off ... we've had it in the past") is not quoted verbatim in A4;
since A4's cash conclusion is already maximally conservative, this adds emphasis, not a new finding —
a NON-BLOCKING recommendation to surface the T86 phrase under the cash flag / QFM #15 at Q2, not a
surviving counter that blocks save.

No bear counter survives as a thesis- or verdict-changing addition: A4 is already symmetrically bearish
and pre-incorporates the substance of all three counters.

---

## VERDICT

**COMPLETE.**

- Coverage: every A2 ledger count reproduced independently (results 22/94/16/4/14/33/8/2; presentation
  18/121-381/6/10; press release 3/33/9/1/2; concall 9+1/91/37/34/35/20); no orphan rows; nothing in my
  fresh pass is missing from the ledger. Every concall row (91 turns / 37 questions / 34 mgmt numbers)
  is cited or reviewed in A4.
- Arithmetic: zero mismatches above rounding across consolidated/standalone/YoY/QoQ metrics, the PAT
  bridge, the S-vs-C gap, deck non-GAAP reconciliation, and all mixed-unit cross-document ties. The
  −14.1% QoQ adj-PAT spoken figure is correctly flagged as conflicting with the −40% filing/deck actual
  and reconciles to no extract figure.
- Adversarial read: none of the three most-positive claims yields a surviving, verdict-changing bear
  counter; A4 pre-incorporates the substance of all three. One optional, non-gating recommendation:
  surface the T86 collection-recurrence quote under the cash flag.

Proceeds to Notion save.

```yaml
stage: A5-adversary
company: "ROUTE"
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
