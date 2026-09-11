# TOTEM — phase 1 verifier summary
Run: runs/totem-2026-09-09 | 2026-09-09

Scope: verifier A (numerical), verifier B (red flag coverage), verifier D
(peer utilisation), and the Gate 0 plus Emerging Moat portion of verifier C
(framework adherence). The valuation adherence half of verifier C is deferred
to phase 3 because B10 and B11 do not exist. Findings are the verifiers' own;
no commentary is added.

## Phase 1 confidence delta

| Component | Score | Source block | Verifier / model | Cycle |
|---|---|---|---|---|
| Numerical acceptance | 100 | B12a.yaml | A, claude-haiku-4-5 | 3 |
| Red flag coverage | 32 | B12b.yaml | B, claude-opus-4-8 | 3 |
| Framework adherence | 90.2 | B12c.yaml | C, claude-opus-4-8 | 2 (governing) |
| Peer utilisation | 65 | B12d.yaml | D, claude-sonnet-5 | 3 |
| **Overall** | **32** | confidence.yaml | orchestrator | governing cycle 3 |

Band: below 60, forced REWORK (prompts/00-orchestrator.md Section 5).

## Acceptance rates and counts

| Verifier | Acceptance rate | CRITICAL | MAJOR | MINOR | Coverage |
|---|---|---|---|---|---|
| A | 100 | 0 | 3 | 2 | 87 material numbers across all nine stage reports; 0 source fidelity findings |
| B | 32 | 1 | 18 | 20 | 47 red flag grade items found independently; 15 caught, 8 partially caught |
| C | 97 | 0 | 2 | 11 | 62 rules (42 Gate 0, 19 emerging moat, 1 stage 9); 60 passed on the MAJOR-or-worse convention |
| D | 65 | 0 | 5 | 3 | 3 peers audited, 2 supplied transcripts; about 28 of 30 citation spot checks clean |

B12b records major_count 18 and minor_count 20 against 18 MAJOR and 12 MINOR
rows itemised in its arrays. The itemised rows are reproduced below.

Verifier B cycle trend: cycle 1 found 19, caught 4 (21%). Cycle 2 found 33,
caught 16 (48%). Cycle 3 found 47, caught 15 (32%). The denominator grows each
cycle; the absolute catch count rose from 4 to 15.

## CRITICAL

| Verifier | Location anchor | Finding |
|---|---|---|
| B | AR2026 p.25 vs p.42; AR2025 p.19 vs p.33; AR2024 p.29 | FY26 MD&A calls exports a "stable trend" while FOB exports fell 15.9% (Rs 3,791.05L to Rs 3,189.46L); with the FY25 "improving trend" claim this is the export direction stated backwards in two consecutive reporting periods, disclosed correctly only in the s.134(3)(m) annexure |

## MAJOR

### Verifier B — missed items

| Location anchor | Finding |
|---|---|
| AR2026 p.26 vs p.63 vs p.27 | MD&A blames the 33.46% interest coverage fall on "availed borrowing facilities to meet its working capital requirements"; CARO Annexure A (ii)(b) in the same AR states "the company has not been sanctioned a working capital facility", and total borrowings FELL Rs 1,968.29L to Rs 1,487.07L |
| AR2026 p.37 vs p.110 and p.108 | Annexure II s.197(12) states KMP remuneration rose "average 7.5%"; note 30 shows KMP Rs 361.34L to Rs 566.11L (+56.7%) and MD Rs 265.52L to Rs 464.00L (+74.7%), 105.65x median, 16.1% of PAT, in a year PAT rose 0.1% |
| AR2026 p.37 and p.28; AR2025 Annexure II | Permanent headcount fell 481 to 420 (-12.7%, -61 people); the HR narrative says relations were "very cordial" and never states the number, which appears only where the Act forces it |
| AR2026 p.42 and p.41; WENDT p.10, p.21 | R&D expenditure disclosed as Nil directly beneath two paragraphs of R&D narrative; Wendt discloses R&D at 2.6% of sales with a DSIR recognised centre |
| AR2026 p.26; AR2025 p.20; AR2026 p.56 | Inventory turnover, current ratio, debt equity and net profit margin all omitted from the SEBI Schedule V ratio table; inventory turnover is the one ratio that would have forced a 25% plus explanation of the FY26 build, and the CG certificate and Secretarial Compliance Report certify clean over the gap |
| AR2026 p.69; MSMED note p.100 | MSME trade payables rose 93.1% (Rs 741.30L to Rs 1,431.62L), MSME share of trade payables 31.7% to 44.2%, in the same year inventories rose Rs 2,449L; filed evidence bearing on the inventory funding question stage 5 declares unresolved |
| AR2026 p.71-72, p.68 | CFO fell 46.3% (Rs 5,131.62L to Rs 2,755.29L); FCF about Rs 917L against Rs 2,531.03L dividend paid, that is 2.8x, bridged by Rs 4,522.62L of mutual fund sales; CFO/PAT 1.79x to 0.96x. Stage 5 said it could not reconstruct FCF from the results filing extraction; the clean statement is in the annual report it read |
| AR2026 note 30 p.108 vs p.29 | About Rs 724L of FY26 expense flowed to promoter group entities, roughly 18% of PBT, including Rs 122.95L repairs and maintenance and Rs 93.04L legal and professional to the holding company, against the Board's Report statement that there were no material related party transactions |
| AR2025 p.19 vs AR2026 p.26 and note 27 p.104 | Capex payoff walked back from "yielded substantial returns and reduced our dependencies on third parties supplies" to "benefits on the quality front... we expect the market to reward us with larger volumes in the near future"; the dependency claim is falsified by processing charges +24.8% against revenue +7.9% |
| AR2026 p.126, note 21 p.101; WENDT p.9 | No geographic revenue split and no major customer disclosure; note 38 says the principal geographical area is India while FOB exports are 12.7% of revenue. Both peers disclose revenue and margin by vertical |
| Q1 FY27 rendered p.3; Q3 FY26 filing p.4; H1 FY26 filing p.4 | The Q1 FY27 margin gain is a soft base artifact: Q1 FY26 PBT margin 9.7% was FY26's trough (Q2 17.5%, Q3 12.5%, Q4 21.6%), and Q1 FY27's 17.6% is four points BELOW Q4 FY26. On a consistent basis the gain over the FY26 full year is 1.8pp, not 6.8pp |
| Q1 FY27 rendered p.3 and p.4 | Q1 FY27 net material cost 36.1% of revenue against 32.2% in FY26 (+430bp) while other expenses FELL 5% in absolute terms on revenue +28.9%; that line is the arithmetic driver of the year on year margin gain and is covered only by a boilerplate regrouping note |
| WENDT p.6 | Wendt's exports GREW 19% year on year in Q1 FY26 (Apr-Jun 2025), the only in window peer export datapoint, opposite in direction to TOTEM's FY26 -15.9%; stage 6 cites the figure elsewhere but never deploys it in the tariff question it rules UNVERIFIABLE |

### Verifier B — claims the pipeline makes that the sources do not support

| ID | Location anchor | Finding |
|---|---|---|
| NS-1 | 05-concall.md, pledge and dividend chain | Reading A (transfer after the record date) called "the more likely reading", with SP and Co collecting Rs 1,871.86 lakh. AR2026 note 30 p.108 states SP and Co Rs 1,798.36L and Forbes Campbell Rs 106.50L. Rs 106.50L at Rs 5 is 2,130,000 shares against 665,592 held at 31-Mar-2025, so the 1,470,000 share transfer completed BEFORE the 02-May-2025 record date. Reading B is confirmed and Reading A excluded. Stage 5 quotes the resolving figure without recognising it |
| NS-2 | 05-concall.md, the correction section | The Wendt AGM line "Commodity prices stayed largely stable" used as the nearest in window peer datapoint. WENDT p.3 places it in the Chairman's calendar 2024 global economy scene setter, covering CY2024 which is TOTEM's FY25 not FY26, and it is a global macro remark, not a carbide or steel price statement. Stage 5 states it did not read the transcript. Wrong period, wrong subject, unread, and used to support a HIGH flag |
| NS-3 | 06-peers.md Part 5; 05-concall.md trigger 1 | The claim that the Q1 FY27 margin jump follows directly from the company's own capex delivery. Nothing in the corpus links them. The Q1 FY27 filing carries four boilerplate notes, no commentary, no segment or utilisation data. Three untested alternatives exist: Q1 FY26 was FY26's trough quarter, headcount fell 61 during FY26, and other expenses fell 5% absolutely on revenue up 29% under a bare regrouping note |
| NS-4 | 05-concall.md ruling on the commodity claim | The ruling that the FY26 abnormal commodity prices sentence does not survive the three year CIF series is OVERSTATED. CIF is an import value, price times quantity. Raw material inventory nearly tripled in the same year (Rs 738.71L to Rs 1,993.71L, note 8 p.92) and consumption rose 25.3%. Flat value against FY24 is consistent with higher prices on lower volumes. The series REMOVES support; it cannot refute. The correct ruling is UNEVIDENCED, not refuted |
| NS-5 | 06-peers.md Part 2D | TOTEM sized at about Rs 290 cr FY26 revenue. AR2026 p.70: revenue from operations Rs 25,101.13 lakh (Rs 251.0 cr); total income Rs 25,473.95 lakh (Rs 254.7 cr). Rs 290 cr appears in no source read. It is used to size TOTEM against peers. Verifier A is the binding authority and has not adjudicated it |

### Verifier D

| Location anchor | Finding |
|---|---|
| 06-peers.md Part 2E and the Mar-2024 coverage map row | The Kennametal market share answer at p.24 is quoted only for its refusal; the 250-300 basis point gain figure in the same answer is dropped |
| WENDT AGM p.23, unused | The market share range and the defence and aerospace revenue mix quantification are never surfaced, and the second contradicts stage 6's own claim that peers never quantify defence demand |
| 06-peers.md against B05-concall.yaml peer_questions | Stage 6 claims seven peer questions; the current B05 carries five. One, on market share, is unverdicted; two are answered only as narrative |
| 06-peers.md coverage map, Jun-2023 row, and B06-peers.yaml | The investor presentation decline quote is attributed to the Jun-2023 call at p.27-28; that transcript has only 22 pages. The same quote is correctly anchored at Mar-2023 p.27-28 elsewhere in the same report |
| 06-peers.md Part 4 and analyst note | The CONTRADICTED verdict discipline defence is incomplete: it rests on one peer with a company specific, TOTEM unrelated cause, does not address that TOTEM's own FOB data establishes the same direction more directly, and does not address that this single peer finding is repeatedly billed as the run's most consequential result |

### Verifier A

| Location anchor | Finding | source_fidelity |
|---|---|---|
| 01-gate0.md, B4 section | "WC Days FY24 = 47.03 + 61.45 - 34.65 = 73.83". Calculation arithmetically correct; the formula is stage defined, not company disclosed. Presentation clarity, not source fidelity | false |
| 03-ardeep.md, Extension 1 | "MD remuneration +74.7% FY25 to FY26 against a Board stated average KMP increase of 7.5%". Both figures verified exact from Note 30 and Board's Report Annexure II. Both numbers accurate but unreconciled inside the same annual report. A governance and disclosure gap, not a numerical error | false |
| 01-gate0.md, Block F, M5 | "M5 score 0, PEER DATA NEEDED". Scoring decision correct per the framework rule; the override of the prior run is documented. Framework application correct. Not a fidelity issue | false |

### Verifier C (Gate 0 and Emerging Moat scope)

| Location anchor | Finding |
|---|---|
| 01-gate0.md Block B, B4 | Displayed delta +5.0 contradicts the band applied (1). True delta +5.01 days. Core crosses a matrix band if scored 3; final classification unchanged |
| 01-gate0.md Block F, M5 | Segment ranking scored on a 3 peer set; Block F's missing peer data rule requires 0 and PEER DATA NEEDED. Moat class and classification unchanged |

## MINOR

### Verifier B — missed items

| Location anchor | Finding |
|---|---|
| AR2026 p.35 vs note 27 Note 1 p.105 | CSR Annexure I item 7 (unspent CSR of the preceding three years) filled "Not Applicable" when FY25 had Rs 39.78L unspent and spent in FY26 |
| AR2026 p.7 vs p.25; AR2025 p.19 | Three inconsistent counts of years of full operation: MD's Message "second full year", MD&A "third year full operations", AR2025 "first year of full operations" |
| AR2024 p.14; AR2025 p.18; AR2026 p.24 | EPS reported identically on the continuing operation and discontinued operations lines for three consecutive years; the company has no discontinued operations |
| Resignation announcement p.1-2; AR2026 p.45 | Resignation effective date filed two ways: 22-Apr-2026 in the Reg 30 announcement, 23-Apr-2026 in the AR senior management table |
| AR2026 p.50 | 17.46% of polled public non institutional votes went AGAINST the postal ballot resolution authorising non executive director commission, the only pay item minorities could vote on |
| AR2026 p.54 | Credit rating IVR BBB/Stable assigned 05-Dec-2024, unreviewed for about 17 months |
| AR2026 note 27 p.104 vs p.54 | Net foreign currency loss rose 498% (Rs 20.71L to Rs 123.87L) against a corporate governance statement that FX risk was hedged in compliance with policy |
| KENNAMET Mar-2023, Suresh Reddy | A Kennametal quote stating the exact gross versus net point behind stage 5's own withdrawal is absent from stage 6 |
| KENNAMET Mar-2024 | Kennametal's qualifier that the Indian aerospace base is "very, very, very small in the country" is not used against TOTEM's three year aerospace and defence narrative |
| WENDT p.6 | Wendt spent its full CSR obligation with no unspent amount, a ready peer benchmark for stage 5's CSR flag, absent from stage 6 |
| NS-6: 05-concall.md vs 06-peers.md | Stage 5 says three HR leadership transitions in about nine months; stage 6 says two exits inside roughly eight months. The same two exits and one appointment in the same corpus, counted two ways across the two reports |
| NS-7: 05-concall.md working capital row | FY25 debtor days used both as partial support for and as evidence against the same claim. The row cites debtor days still low and debtor days worsening 108% in the same cell, and never states that FY26 debtor days IMPROVED to 46 (AR2026 p.26) |

### Verifier C (Gate 0 and Emerging Moat scope)

| Location anchor | Finding |
|---|---|
| 01-gate0.md | "Data available" line is not the opening line; it sits behind the run-2 preamble |
| 01-gate0.md D1 | Rs 23.23 cr mutual funds excluded from cash; including them scores 5. Disclosed judgment |
| 01-gate0.md D1 vs Block F | Two FY26 EBITDA bases coexist (52.62 and 52.94); the governing basis is not declared |
| 01-gate0.md D3 | D/E 0.0987 against a 0.1 threshold; the AR's own 10% scores 4. Disclosed |
| 01-gate0.md E2 | Three year promoter holding change rule scored on a roughly 12 month window. Prompt rules 5 and 6 conflict; rule 6 chosen and flagged provisional. Accepted |
| 01-gate0.md Block F, M2 | With 3 peers the median is Wendt alone (13.72%), whose margin fell from 22.73% in one year. Year end sensitivity run; single peer fragility not tested |
| 01-gate0.md Block F, M8 | Scored 0 as not disclosed; B07 records 200+ distributors and 12 sales offices from the 2024 Information Memorandum, which scores 1 under "mentioned unquantified". Cross stage corpus scope mismatch |
| 01-gate0.md peer alignment note | Kennametal's Jun-2026 year carries a Rs 225.0 cr Change in Inventory against Rs 21.5 cr prior; the anomaly is not named beside the year end alignment disclosure |
| 07-emoat.md Section 5, H3 | Matrix label "(LM)" against a stated Medium likelihood / Low impact (ML). Both map to 1; value correct |
| B07-emoat.yaml | Two non schema fields added (em_score_scale, capex_embedded_growth_basis) |
| B07-emoat.yaml evidence_mix | Scoped to the five evidenced rows only; inference 0 is false of the document, which carries at least six labelled analyst inferences. Scoping defensible, unstated |

### Verifier D

| Location anchor | Finding |
|---|---|
| 06-peers.md Q7 evidence field | The tungsten price fall datapoint at Mar-2024 p.19 is not read back against stage 5's raw material spike question |
| B06-peers.yaml partially_verified | Wendt is listed as a supporting peer for the capex payback benchmark despite supplying no payback figure of its own |
| 06-peers.md Part 2C | The product coverage caveat is not restated when the austempering furnace capex is folded into the Kennametal based industry wide capex race read |

### Verifier A

| Location anchor | Finding | source_fidelity |
|---|---|---|
| 02-notes.md, top finding 2 | "CFO fell Rs 51.32cr to Rs 27.55cr, driven almost entirely by the inventory swing". CFO figures exact; the inventory swing is the largest single line but MSME payables are a second order lever. Compression of a two factor story into a single largest line summary. Not an error | false |
| 03-ardeep.md, Phase 3B | "Quick ratio 0.99, own computation from the balance sheet". (12,255.52 - 5,642.15) / 6,664.98 = 0.992, confirmed. Calculation correct; ratio stage computed from accurate source figures | false |

## Verifier A source fidelity gate

Zero source fidelity findings across 87 checked numbers. No figure in this pack
was flagged as absent from or contradicted by its source.

One item stands open rather than cleared. Verifier B raised NS-5, a figure of
about Rs 290 cr used to size the subject in 06-peers.md against filed revenue
of Rs 251.01 cr and total income of Rs 254.74 cr. Verifier A did not check that
cell. Under the source fidelity rule verifier A is the binding authority on
whether a number exists in a source, so the item is unadjudicated and sits on
the rework list. No downstream step contested a verifier A finding in this
phase.

## Verifier C governing cycle note

B12c records verifier C cycle 2, the governing framework adherence audit for
phase 1. Its single MAJOR on stale Gate 0 run-2 moat figures inside Sections
6C, 6D and 6E of 07-emoat.md was resolved by a mechanical figure alignment to
4 of 12 and 20/60, recorded inside 07-emoat.md under an ALIGNMENT NOTE and in
the commit that carried it. No analytical content changed and no classification
moved. Verifier C was not rerun in cycle 3 because neither B01 nor B07 changed
after its audit apart from that alignment.

Verifier C standing verdicts: Gate 0 classification AVOID CONFIRMED and robust
to both MAJOR findings applied together. No double count between the pledge cap
and the LIMITED history downgrade. Emerging moat completeness CONFIRMED, all 23
rows addressed, score 9.7, classification NONE. Peer year end alignment
DEFENSIBLE, not a basis error.
