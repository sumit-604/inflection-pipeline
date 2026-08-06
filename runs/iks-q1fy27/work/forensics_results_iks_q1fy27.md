# A3 FORENSIC NOTES — IKS (Inventurus Knowledge Solutions Ltd) — Q1FY27 — DOCTYPE: results

Source filing package (all dated August 5, 2026, same board meeting):
- Primary: `extract_results_iks_q1fy27.txt` (results_board_outcome.pdf, 12 pages, INR Million)
- Supplementary: `extract_results_pressrelease_iks_q1fy27.txt` (results_press_release.pdf)
- Supplementary: `extract_results_directors_iks_q1fy27.txt` (results_change_directors.pdf)
- A2 ledger: `ledger_results_iks_q1fy27.md`

Ledger reconciliation: 100%. All 37 line items (L318-393), 11 auditor paras
(L132-286), 11 entities (L228-239), 10 notes (L406-457), 3 agenda items,
4 annexures, 10 annexure-disclosure rows, 5 signature blocks, and all 4
ZERO_STANDING line items read verbatim at their cited lines before judging.
Unit convention: INR Million (x0.1 to Cr). Both review reports UNMODIFIED;
no Going Concern, no Emphasis of Matter, no qualification anywhere.

A2 flags given special attention: ZERO_STANDING (F1), standalone-vs-consolidated
PAT gap (F2), UNAUDITED_ENTITIES (F3/F4), ENTITY_CHANGE / WWMG reclassification
(F4/F15), OCR_GARBLED headings (F14), board-outcome items 2-3 chairman
retirement + succession (F13), auditor Other Matters paras 6-7 read verbatim (F4).

---

## FINDINGS TABLE

| id | check | ledger row ref | line/turn/slide | verbatim quote | classification | forward implication |
|----|-------|----------------|-----------------|----------------|----------------|---------------------|
| F-01 | F2 | S6 PAT (Sr.No 7) | L345 | "Profit for the period... 1,937.41 [C] ... 1,625.46 [S]" | AMBIGUOUS | Consolidated PAT premium over standalone has collapsed 34.3% (Q1FY26) -> 21.9% (Q4FY26) -> 19.2% (Q1FY27), a 15.1pp narrowing; parent is out-earning the incremental subsidiary/associate contribution. Direction uncertain (parent outgrowth vs subsidiary margin erosion vs associate drag) -> A4 question. |
| F-02 | F2 | S6 Revenue (L319); Note 9 | L319, L442-444 | "Revenue related to this agreement was recognised during the quarter" (L442) | FORWARD-SIGNAL | Standalone revenue +48.8% YoY (3,194.69 -> 4,752.68) vs consolidated +20.7%; parent quarter carries a TruBridge pre-acquisition software-license sale recognised under Ind AS 115. TruBridge became a subsidiary July 9, 2026, so this revenue turns INTERCOMPANY and eliminates from Q2FY27 -> standalone growth likely reverses. Quantum undisclosed -> A4 question. |
| F-03 | F2 | S6 Other expenses (L328); PAT (L345) | L328, L345 | "Other expenses ... 573.57 [S Q1FY27] ... 264.30 [S Q4FY26]" | AMBIGUOUS | Standalone other expenses +117% QoQ (264.30 -> 573.57) and +113% YoY; consolidated PAT fell QoQ (2,059.68 -> 1,937.41, -5.9%) and standalone PAT fell QoQ (1,690.05 -> 1,625.46, -3.8%) even as press release headlines "+28% YoY PAT". QoQ margin compression is masked by the YoY frame -> A4 question on the standalone other-expense spike (TruBridge license COGS? acquisition costs?). |
| F-04 | F3 | Auditor para 7 | L275-278 | "five subsidiaries which have not been reviewed ... total revenue from operations of INR 0.28 million, total net loss after tax of INR 5.67 million" | NEUTRAL-FACT | Five consolidated subsidiaries are effectively dormant (INR 0.28mn revenue across all five). No Going Concern EoM exists to reconcile against. Watch for cleanup/liquidation or a Going Concern flag at the Annual Report on these near-shell entities. |
| F-05 | F4 | Auditor para 7; S6 assoc (L335) | L279-282, L335 | "the Group's share of net loss after tax of INR 53.07 million ... in respect of one associate (upto June 29, 2026) ... which have not been reviewed by their auditors" | FORWARD-SIGNAL | The single largest non-principal-auditor number is the fully-UNREVIEWED associate loss share of INR 53.07mn (2.7% of consolidated PAT), NEW vs Q1FY26 (nil). Per Note 8 the associate (IKS WWMG MSO) flipped to step-down subsidiary effective June 30, 2026, so from Q2FY27 the one-line equity loss is replaced by full-line consolidation of WWMG revenue AND losses -> reset of the consolidation base -> A4 question on WWMG standalone economics. Aggregate unreviewed impact (para 6 + para 7) ~5.8% of PAT, below the 10% threshold. |
| F-06 | F6 | Notes 8, 9, 10 | L434-436, L438-440, L455-457 | "The Group will complete the purchase price allocation ... within the measurement period (not exceeding twelve months from the acquisition date)" (L434) | FORWARD-SIGNAL | Three dateable management commitments (see Commitment Register): WWMG PPA + remeasurement of the previously held 48.02% interest by ~June 30, 2027; ARAI PPA by ~May 14, 2027; TruBridge completion (delivered July 9, 2026). Retrospective adjustments will restate prior periods. |
| F-07 | F7 | Note 8 | L432-436 | "the initial accounting for the business combination ... is incomplete as at the reporting date, pending finalisation ... accounted for ... on a provisional basis" | FORWARD-SIGNAL | Pre-emptive hedge language on WWMG: "no remeasurement gain/loss on the previously held equity interest has been recognised in the current quarter" and "will be recognised retrospectively." A material remeasurement gain/loss on the 48.02% legacy stake is deferred and could hit restated results within 12 months -> A4 question on expected direction/magnitude. |
| F-08 | F8 | S6 Tax (L341-343) | L341-343 | "Deferred tax (110.95) [C Q1FY27] ... 173.99 [C Q4FY26]" | AMBIGUOUS | Consolidated ETR runs below the 25.17% statutory rate every period (Q1FY27 22.8%, Q4FY26 18.6%, Q1FY26 22.2%, FY26 20.3%); standalone lower still (Q1FY27 21.2%, Q4FY26 14.8%). Q1FY27 consolidated shield ~240bps; Q4FY26 shield ~660bps. Persistent deferred-tax credits at group level plus foreign (US) rate mix; sustainability uncertain -> A4 question. No "tax adjustments relating to earlier years" line present (that sub-check clean). |
| F-09 | F10 | Note 5 | L418-420 | "granted 143,814 stock options to eligible employees" | NEUTRAL-FACT | ESOP grants (143,814 this quarter) exceed exercises/allotments (140,085); paid-up capital unchanged at 170.71 (face value Rs1). Basic-vs-diluted spread stable at ~2% (11.56 vs 11.32 consolidated) — no new dilutive instrument signal, but the option pool keeps growing = slow structural dilution overhang. |
| F-10 | F13 | Agenda items 2-3; Annexure B/D; Note 9 | L45-54, L77-84, L488-489, L438-440 | "he shall cease to be a Director and Non-Executive Chairman ... upon the conclusion of the ensuing 20th AGM" (L53-54) | FORWARD-SIGNAL | Board approved a chairman succession effective conclusion of 20th AGM (cessation date September 21, 2026 per Annexure B, L488-489): Non-Executive, Non-INDEPENDENT chairman Berjis Desai exits (reason: appointed to National Commission for Minorities, GoI — non-adverse, L483-487) and is replaced by INDEPENDENT director Clarence Carleton King II designated Non-Executive Chairman while retaining independence — a governance UPGRADE (independent chairman). The "ensuing 20th AGM" (~Sept 21, 2026) signals the Annual Report and AGM notice drop within weeks -> schedule Role 6 AR Deep Dive. Subsequent event: TruBridge completed July 9, 2026 at EV up to US$557mn -> funding structure (debt/equity) undisclosed -> A4 capital-structure question. |
| F-11 | F14 | Notes 7, 8, 9; entity table | L228, L427, L438 | "IKS Inc., a US-incorporated step-down subsidiary" (L427) vs "IKS Inc., a wholly owned US subsidiary" (L438) | NEUTRAL-FACT | The same entity (Inventurus Knowledge Solutions Inc, classified "Wholly owned Subsidiary" in the auditor entity table L228 and Note 7 L424) is described as a "step-down subsidiary" in Note 8 (L427) but a "wholly owned ... subsidiary" in Note 9 (L438). Individually immaterial relationship-descriptor drafting inconsistency; a governance-hygiene data point given the reclassification activity this quarter. |
| F-12 | F15 | Entities (S5); Notes 8, 10 | L230, L238-239, L427-428, L446-448 | "ARAI Solutions Private Limited ... has become a subsidiary ... with effect from the acquisition date" (L447-448) | FORWARD-SIGNAL | Consolidation scope changed on three fronts: ARAI Solutions Pvt Ltd NEW subsidiary (acquired May 14, 2026, cash Rs110mn, L446-448); IKS WWMG MSO LLC RECLASSIFIED Associate -> Step-down Subsidiary w.e.f. June 30, 2026 (48.02% -> 51.88%, L238-239 / L427-428); TruBridge not yet consolidated (completed July 9, post quarter) but lands in Q2FY27. Q2FY27 consolidation base is materially reset -> prior-quarter comparability breaks. |

Supplementary observation (press release, results-class evidence, F16 formally N.A. on
this doctype): Adjusted PAT of INR 2,153 Mn is disclosed (L100 press release) against
statutory PAT of INR 1,937 Mn — an undefined +216mn add-back with no reconciliation
bridge. EBITDA of INR 2,949 Mn (L98) ties cleanly to the statement (PBT-before-associate
2,562.51 + D&A 342.89 + finance 101.10 − other income 57.10 = 2,949.4). The Adjusted-PAT
bridge does not tie to any disclosed line -> flag for A4 to request the reconciliation.

---

## CHECKLIST SCORECARD

| Check | Status | One-line basis |
|-------|--------|----------------|
| F1 ZERO-VALUE STANDING LINE ITEMS | PASS | All 4 ZERO_STANDING standalone-nil lines (Changes in inventories L324, Share of associates L335, FX translation of foreign ops L371, FVOCI equity investments L377) are group-level-only transaction classes structurally absent from the parent-only entity; template signal, no anomaly. |
| F2 STANDALONE vs CONSOLIDATED DECOMP | FINDING | PAT gap narrowed 34.3% -> 19.2% (>5pp) [F-01]; standalone revenue +48.8% YoY on TruBridge license that becomes intercompany [F-02]; QoQ PAT decline + standalone other-expense spike [F-03]. |
| F3 SHELL-ENTITY DETECTION | FINDING | Five unreviewed subsidiaries effectively dormant (Rs0.28mn revenue, L275-278); no Going Concern EoM to reconcile [F-04]. Group cost lines (consol employee 4,550 vs standalone 1,985) confirm the Aquity/operating subs are NOT shells. |
| F4 UNAUDITED CONTRIBUTION RATIO | FINDING | Aggregate unreviewed impact ~5.8% of PAT (below 10% threshold), BUT the unreviewed associate loss share (Rs53.07mn) is a YoY jump from nil in Q1FY26 = separate FINDING [F-05]. |
| F5 GOING CONCERN / EoM SCOPE | PASS | No Going Concern paragraph and no Emphasis of Matter in either report (standalone L155-160, consolidated L255-261); both conclusions UNMODIFIED. Fresh coverage — no prior-quarter paragraph to verbatim-diff. |
| F6 FORWARD-COMMITMENT MINING | FINDING | Three dateable "will complete"/"completed" commitments across Notes 8/9/10 [F-06]; see Commitment Register. |
| F7 HEDGE PHRASE MINING | FINDING | "incomplete as at the reporting date, pending finalisation ... provisional basis" (L432-433) defers a WWMG remeasurement gain/loss to a retrospective restatement [F-07]. Press-release Safe Harbour (L121-124) is boilerplate. |
| F8 TAX FORENSICS | FINDING | ETR below statutory 25.17% every period (consol 22.8%/18.6%/22.2%/20.3%); persistent deferred-tax credits; ~240bps shield Q1FY27, ~660bps Q4FY26 [F-08]. No earlier-year tax-adjustment line. |
| F9 OCI FORENSICS | PASS | Actuarial remeasurement (consol Q1FY27 8.91) within the full prior-year magnitude (FY26 (31.55)); no single-quarter OCI item exceeds its full prior year (cash-flow-hedge 359.93 < FY26 856.30; FVOCI 226.42 < FY26 931.52). Reclassifiable hedge swings drive TCI volatility but no assumption-change trigger. |
| F10 SHARE COUNT AND DILUTION | FINDING | Paid-up capital unchanged 170.71; basic/diluted spread stable ~2%; ongoing ESOP grants (143,814) exceed allotments (140,085) = slow dilution overhang [F-09]. |
| F11 RESERVES / NET WORTH TIE-OUT | PASS | Other Equity + Paid-up ties internally (consol 27,831.66 + 170.71 = 28,002.37mn; standalone 17,713.67 + 170.71 = 17,884.38mn, at FY26 balance-sheet date L385/L387). Fresh coverage — no rating rationale or presentation number for external cross-check. |
| F12 SEGMENT FORENSICS | N.A. | Single reportable operating segment per Note 4 (L415-416); no segment asset/liability disaggregation to trend. |
| F13 BOARD OUTCOME BEYOND RESULTS | FINDING | Chairman succession (Non-Independent -> Independent chairman) effective ~Sept 21, 2026; AGM/AR imminent -> Role 6 event; TruBridge US$557mn completion, funding undisclosed [F-10]. |
| F14 NOTE DRAFTING INCONSISTENCIES | FINDING | IKS Inc described "step-down subsidiary" (L427) vs "wholly owned subsidiary" (L438) vs entity-table "Wholly owned Subsidiary" (L228) [F-11]; minor entity-name comma variance (WWMG "LLC" vs ", LLC"). Note/letter both say "review" (no audit-vs-review mismatch). |
| F15 ENTITY LIST DIFFS | FINDING | ARAI new subsidiary; WWMG Associate->Step-down Subsidiary; TruBridge inbound Q2 [F-12]. |
| F16 PRESENTATION: DROPPED/REFRAMED | N.A. | Doctype = results, not a presentation deck (per applicability rule). Adjusted-PAT observation surfaced in narrative above for A4. |
| F17 CONCALL: SILENCE AUDIT | N.A. | Doctype = results, not a concall transcript; no Notion monitoring checklist (fresh coverage). |

Blank checks: none. GATE A3: pass.

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/ref | status word |
|------------|--------------|----------|-------------|
| Complete WWMG PPA incl. remeasurement of previously held 48.02% interest; recognise any resulting gain/loss retrospectively | by ~June 30, 2027 (12-mo measurement period) | Note 8, L434-436 | underway (provisional) |
| Complete ARAI Solutions PPA; retrospective adjustment to goodwill/capital reserve | by ~May 14, 2027 (12-mo measurement period) | Note 10, L455-457 | underway (provisional) |
| Complete TruBridge Inc acquisition (EV up to US$557mn) | July 9, 2026 (achieved) | Note 9, L438-440 | completed |
| Chairman succession: Berjis Desai cessation; Clarence Carleton King II designated Non-Executive Chairman | conclusion of 20th AGM — September 21, 2026 | Agenda items 2-3 (L45-84); Annexure B L488-489; Annexure D L575-578 | board approved / pending AGM |

---

## A4 HANDOFF — QUESTIONS TO GENERATE

FORWARD-SIGNAL (convert to management questions): F-02, F-05, F-06, F-07, F-10, F-12.
AMBIGUOUS (lean-bear, resolve via question): F-01, F-03, F-08.
Plus the undefined Adjusted-PAT (Rs2,153mn) vs statutory PAT (Rs1,937mn) +216mn bridge
(press release L99-100).

```yaml
stage: A3-forensics
company: "IKS"
quarter: "q1fy27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/iks-q1fy27/work/forensics_results_iks_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: PASS
  F2: FINDING
  F3: FINDING
  F4: FINDING
  F5: PASS
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: PASS
  F10: FINDING
  F11: PASS
  F12: N.A.
  F13: FINDING
  F14: FINDING
  F15: FINDING
  F16: N.A.
  F17: N.A.
findings:
  - {id: "F-01", check: "F2", line: "L345", classification: "AMBIGUOUS", implication: "Consol-vs-standalone PAT premium narrowed 34.3%->19.2% (15.1pp); parent out-earning incremental sub/associate contribution"}
  - {id: "F-02", check: "F2", line: "L319,L442-444", classification: "FORWARD-SIGNAL", implication: "Standalone revenue +48.8% YoY on TruBridge pre-acquisition license sale; becomes intercompany and eliminates from Q2FY27"}
  - {id: "F-03", check: "F2", line: "L328,L345", classification: "AMBIGUOUS", implication: "Standalone other expenses +117% QoQ and QoQ PAT decline (both S and C) masked by YoY +28% headline"}
  - {id: "F-04", check: "F3", line: "L275-278", classification: "NEUTRAL-FACT", implication: "Five unreviewed subsidiaries near-dormant (Rs0.28mn revenue); watch for cleanup/Going Concern at AR"}
  - {id: "F-05", check: "F4", line: "L279-282,L335", classification: "FORWARD-SIGNAL", implication: "Unreviewed associate loss share Rs53.07mn new vs Q1FY26 nil; WWMG flips to full consolidation from Q2FY27"}
  - {id: "F-06", check: "F6", line: "L434-436,L438-440,L455-457", classification: "FORWARD-SIGNAL", implication: "WWMG and ARAI PPAs to complete within 12 months; retrospective restatements pending; TruBridge completed"}
  - {id: "F-07", check: "F7", line: "L432-436", classification: "FORWARD-SIGNAL", implication: "Provisional/pending WWMG PPA defers remeasurement gain/loss on 48.02% legacy stake to retrospective restatement"}
  - {id: "F-08", check: "F8", line: "L341-343", classification: "AMBIGUOUS", implication: "ETR below 25.17% statutory every period (Q1FY27 consol 22.8%, ~240bps shield); deferred-tax credit reliance, sustainability unclear"}
  - {id: "F-09", check: "F10", line: "L418-420", classification: "NEUTRAL-FACT", implication: "ESOP grants (143,814) exceed allotments (140,085); stable ~2% diluted spread; slow dilution overhang"}
  - {id: "F-10", check: "F13", line: "L45-54,L77-84,L438-440", classification: "FORWARD-SIGNAL", implication: "Non-independent chairman replaced by independent chairman eff ~Sept 21 2026; AGM/AR imminent (Role 6); TruBridge US$557mn funding undisclosed"}
  - {id: "F-11", check: "F14", line: "L228,L427,L438", classification: "NEUTRAL-FACT", implication: "IKS Inc described inconsistently (step-down vs wholly-owned subsidiary); governance-hygiene data point"}
  - {id: "F-12", check: "F15", line: "L230,L238-239,L427-428,L446-448", classification: "FORWARD-SIGNAL", implication: "ARAI new sub, WWMG reclassified to subsidiary, TruBridge inbound Q2; consolidation base reset, comparability breaks"}
forward_signals: ["F-02", "F-05", "F-06", "F-07", "F-10", "F-12"]
ambiguous: ["F-01", "F-03", "F-08"]
commitments:
  - {commitment: "Complete WWMG PPA and remeasure previously held 48.02% interest; recognise gain/loss retrospectively", implied_date: "2027-06-30", ref: "Note 8 L434-436", status_word: "underway"}
  - {commitment: "Complete ARAI Solutions PPA; retrospective goodwill/capital-reserve adjustment", implied_date: "2027-05-14", ref: "Note 10 L455-457", status_word: "underway"}
  - {commitment: "Complete TruBridge Inc acquisition (EV up to US$557mn)", implied_date: "2026-07-09", ref: "Note 9 L438-440", status_word: "completed"}
  - {commitment: "Chairman succession: Desai cessation, King designated Non-Executive Chairman", implied_date: "2026-09-21", ref: "Agenda 2-3 L45-84; Annexure B L488-489", status_word: "initiated"}
gate_a3: pass
blank_checks: []
```

---

## TARGETED SUPPLEMENT — A5 GAP CLOSURE (added 2026-08-06)

Scope: ONE additional forensic cluster to close the A5-adversary gap on the
YoY ROE decline and its disclosed driver. Cross-document evidence (results
filing + investor presentation). Not a re-run of the 17-check pass; the
scorecard and YAML above are unchanged. This supplement adds F-13 and maps it
to F16 (presentation reframing) primary, corroborated by F11 (net-worth /
equity-base composition) and F9 (OCI / FVOCI). Because the primary evidence is
the deck (a presentation doctype), F16 — marked N.A. on the results doctype
above — is the correct home for the framing contradiction; the filing FVOCI
line supplies the corroborating results-side anchor.

### Evidence read verbatim (anchored to the extracts, not to approximate cites)

Presentation `extract_presentation_iks_q1fy27.txt` (slide footer 12 / p13):
- L415 (slide TITLE): "Q1 FY 27 - Improving EPS and maintaining high ROE"
- L420 / L421 / L423 (ROE % series, left-to-right): "32.3%" (Q1 FY26) -> "31.3%"
  (Q4 FY26) -> "26.4%" (Q1 FY27); x-axis period labels at L435.
  A2 ledger flags this series `AMBIGUOUS_CHART_MAPPING` (ledger units 6-8,
  L323-325): the period-to-value binding is inferred sequentially, not directly
  labelled, but is corroborated by the footnote "*ROE declined..." and the
  x-axis order — mapping treated as robust for this finding.
- L438-439 (ROE definition): "Return on Equity is calculated as profit for the
  period divided by average equity balance during the period." (annualised basis:
  quarterly PAT 1,937.41 x4 / average equity ~= 26.4% reconciles.)
- L443 (footnote, the disclosed DRIVER): "*ROE declined due to increased equity
  base from revaluation of Abridge, alongside lower earnings from reduced
  currency gains and one-time acquisition costs."

Filing `extract_results_iks_q1fy27.txt` (Statement of OCI, Sr.No 8):
- L377 (FVOCI corroboration): "Changes in the fair value of equity investments
  at FVOCI  226.42" — consolidated Q1FY27 = 226.42 (FY26 = 931.52; standalone =
  dash all periods; A2 ledger L179, ZERO_STANDING). Income tax on the item
  L378 (56.86); net-of-tax addition to the FVOCI reserve L379 = 178.47
  (consolidated). This is the non-cash Abridge (equity investment) mark flowing
  through OCI into net worth — the exact equity-base inflator the deck footnote
  names.

### FINDINGS TABLE (supplement)

| id | check | ledger row ref | line/turn/slide | verbatim quote | classification | forward implication |
|----|-------|----------------|-----------------|----------------|----------------|---------------------|
| F-13 | F16 (primary); corrob. F11, F9 | Deck slide 12 title + ROE series + footnote (ledger units 6-8, footnote #10); filing S8 FVOCI L377 (ledger L179) | Deck L415, L420-423, L438-439, L443; filing L377-379 | Title: "Improving EPS and maintaining high ROE" (L415) vs footnote: "*ROE declined due to increased equity base from revaluation of Abridge, alongside lower earnings from reduced currency gains and one-time acquisition costs" (L443) | AMBIGUOUS | Title-vs-data contradiction: the deck headlines "maintaining high ROE" while its own chart shows ROE 32.3% -> 26.4%, a ~590bps YoY fall (~490bps QoQ from 31.3%). The footnote leads with a benign non-cash denominator artefact (the Abridge FVOCI mark, filing L377 Rs226.42mn gross / Rs178.47mn net) but concedes, "alongside," an EARNINGS-side driver (reduced currency gains + acquisition costs). Illustrative normalisation ex the Abridge revaluation reserve (annualised PAT 7,749.6 / average equity ~29,354 less the cumulative net FVOCI reserve ~872mn = ~28,482) lifts ROE only ~26.4% -> ~27.2%, i.e. the named Abridge artefact explains at most ~80bps of the ~590bps decline; the residual ~500bps is earnings/denominator effects the footnote sub-orders (FX-gain normalisation, acquisition drag, and IPO/acquisition equity growth that dwarfs the Abridge mark). So the reported ROE decline does NOT understate operating deterioration by hiding a non-cash mark — ex-artefact ROE is marginally HIGHER — but the deck's FRAMING (headline "maintaining" + footnote leading on the benign equity-base line) understates that the fall is mostly earnings-driven, and IKS as a serial acquirer makes "one-time acquisition costs" a likely recurring item. Direction of true forward operating ROE unresolved -> lean bear -> A4 management question. |

### Normalised-ROE working (illustrative; balance-sheet detail not in the quarterly)
- Reported ROE Q1FY27 (consolidated, annualised) = 26.4% (deck L423).
- Annualised consolidated PAT = 1,937.41 x4 = 7,749.64 (filing L345).
- Implied average equity = 7,749.64 / 0.264 ~= 29,354mn.
- Cumulative net FVOCI (Abridge) reserve = FY26 net 693.44 + Q1FY27 net 178.47
  ~= 871.9mn (gross 931.52 + 226.42 = 1,157.9mn) (filing L377-379).
- Average equity ex Abridge reserve ~= 29,354 - 872 = 28,482mn.
- Normalised ROE ~= 7,749.64 / 28,482 ~= 27.2% -> Abridge mark explains ~80bps
  of the ~590bps YoY decline; ~500bps is earnings/other-equity growth.

### A4 HANDOFF — SUPPLEMENT
AMBIGUOUS (lean-bear, resolve via question): F-13. Questions to generate:
(1) Provide ROE decomposition — how much of the 590bps YoY fall is denominator
(equity-base growth from IPO proceeds, acquisition equity, and the Rs226.42mn
Abridge FVOCI mark) vs numerator (earnings, incl. the reduced currency gains
and the "one-time" acquisition costs quantified)? (2) Are the "one-time
acquisition costs" genuinely non-recurring given the ongoing acquisition
cadence (ARAI, WWMG, TruBridge)? (3) Normalised/underlying ROE excluding the
non-cash Abridge revaluation and one-off costs, and the reconciliation to the
"maintaining high ROE" headline claim.

```yaml
# SUPPLEMENT YAML — A5 gap closure (F-13 only; does not supersede the primary block above)
stage: A3-forensics-supplement
company: "IKS"
quarter: "q1fy27"
doctype: "presentation+results (cross-doc)"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/iks-q1fy27/work/forensics_results_iks_q1fy27.md"
new_findings:
  - {id: "F-13", check: "F16", corroborating_checks: ["F11", "F9"], line: "deck L415,L420-423,L438-439,L443; filing L377-379", ledger_ref: "pres ledger units 6-8 + footnote #10 (L134-135); results ledger L179", verbatim_title: "Improving EPS and maintaining high ROE", verbatim_footnote: "*ROE declined due to increased equity base from revaluation of Abridge, alongside lower earnings from reduced currency gains and one-time acquisition costs", classification: "AMBIGUOUS", implication: "Title-vs-data contradiction: deck says 'maintaining high ROE' while chart shows 32.3%->26.4% (~590bps YoY). Abridge FVOCI mark (Rs226.42mn gross/178.47mn net, filing L377-379) explains only ~80bps; residual ~500bps is earnings/denominator. Framing understates that the decline is mostly earnings-driven; 'one-time' acquisition costs likely recur -> A4 question."}
ambiguous: ["F-13"]
forward_signals: []
gate_a3: pass          # F-13 carries a status (FINDING) and a cite; no blank check introduced
new_finding_status:
  F-13: FINDING
new_finding_line: "deck L415, L420-423, L443; filing L377-379"
```
