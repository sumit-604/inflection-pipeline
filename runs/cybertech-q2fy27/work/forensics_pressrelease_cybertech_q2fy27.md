# A3 FORENSIC NOTES: CYBERTECH Q2FY27, doctype presentation (press release, file tag "pressrelease")

Revision 2 (2026-10-24). The orchestrator and A1 rendered page 3. The text layer had shifted the YoY % column down one row. A1 corrected fulltext L96-L111 and rows R025, R030, R034, R039, R043, R048, R058, R061, R064, R067, and added qualifier R141. A2 updated its ledger (141 IDs). This revision re-reads the corrected lines. It reclassifies FN-01 from AMBIGUOUS to NEUTRAL-FACT and retires FN-02 as an extraction artifact. All other findings are unchanged.

Inputs read: A1 structured `extracted/cybertech-pressrelease-q2fy27-structured.md` (R001-R141), A1 fulltext `extracted/cybertech-pressrelease-q2fy27-fulltext.md` (lines 1-150, corrected page 3), A2 ledger `work/ledger_pressrelease_cybertech_q2fy27.md` (141 IDs). Cross-document reconciliation file (task-authorised): `extracted/cybertech-results-q2fy27-fulltext.md` (Rs lakh). Prior-quarter fulltext: NONE. Notion checklist: NONE. Nothing under inputs/ was opened.

Units: press release (PR) INR million (x0.1 to Rs Cr); results filing Rs lakh (x0.01 to Rs Cr). 1 mn = 10 lakh. "PR Lnn" = press-release fulltext line; "RF Lnn" = results-filing fulltext line.

## 0. LEDGER RECONCILIATION

All 141 structured IDs (R001-R141) referenced in the A2 ledger were read at their cited fulltext line. 141 of 141 read; reconciled 100%.

Corrected rows, re-read at their lines:
- Profit-row YoY cells now carry values: R025 "2.0%" (L96), R034 "1.2%" (L98), R043 "0.3%" (L100), R058 "8.9%" (L108), R064 "7.9%" (L110).
- Margin-row YoY cells are now blank: R030 (L97), R039 (L99), R048 (L101), R061 (L109), R067 (L111).
- R141 (QUALIFIER, cited L93, the YoY % column header) records the offset and A1's correction. It is a pipeline qualifier with no source text of its own. Reconciled.

Two rows cite the start line of a multi-line span (R139 cites L143, list continues L144-145; R140 cites L145, close runs to L148). Neither is an error.

Pipeline metadata note (not a document finding): fulltext header L11-L12 still reads "render_candidates: none" and "rendered_pages: none", but page 3 was render-checked (R141). A1 should update the header.

A2 flags handled here: ZERO_STANDING x5, now the margin-row cells (F1); COLUMN_ANOMALY retracted by A2 (FN-02 retired, F16); PARTNER_TIER_CONFLICT (F14); DATE_MISMATCH (F14); UNQUANTIFIED_CLAIM R117 (F16); NO_QUANT_GUIDANCE (F6); UNAUDITED_SOURCE R134 (F4 basis).

### Cross-document tie-out (PR vs consolidated results, RF L100-L128)

| Line item | PR Q2FY27 / Q1FY27 / Q2FY26 (mn) | RF consolidated (lakh) | Tie |
|---|---|---|---|
| Operating revenue (PR L94) | 733.0 / 684.5 / 587.9 | 7,329.57 / 6,844.73 / 5,878.50 (RF L100) | yes |
| Total revenue (PR L95) | 780.3 / 766.3 / 667.3 | 7,802.80 / 7,663.28 / 6,673.18 (RF L102) | yes |
| EBITDA (PR L96) | 128.2 / 139.0 / 125.7 | PBT + finance cost + D&A = 1,282.10 / 1,390.44 / 1,256.60 (RF L106, L107, L110) | yes, INCLUDES other income |
| PBT (PR L98) | 115.4 / 126.2 / 114.0 | 1,154.43 / 1,261.53 / 1,140.34 (RF L110) | yes |
| PAT (PR L100) | 86.8 / 94.8 / 86.6 | 867.73 / 947.72 / 865.54 (RF L115) | yes |
| H1 op rev / total / EBITDA / PAT (PR L106-L110) | 1417.4 / 1546.6 / 267.3 / 181.5 | 14,174.30 / 15,466.08 / 2,672.54 / 1,815.45 (RF L100-L115) | yes |
| H1FY26 same (PR L106-L110) | 1169.8 / 1319.7 / 245.5 / 168.3 | 11,697.91 / 13,197.18 / 2,454.52 / 1,682.88 | yes |

Margins in the PR are computed on total revenue (for example 128.2 / 780.3 = 16.4%). Every percentage cell, including the corrected profit-row YoY cells, recomputes within rounding on the lakh figures: EBITDA YoY 1,282.10 / 1,256.60 = +2.0%; PBT YoY 1,154.43 / 1,140.34 = +1.2%; PAT YoY 867.73 / 865.54 = +0.3%; H1 EBITDA 2,672.54 / 2,454.52 = +8.9%; H1 PAT 1,815.45 / 1,682.88 = +7.9%; PBT QoQ 1,154.43 / 1,261.53 = -8.5%. No number in the PR mismatches the filing. The PR figures are CONSOLIDATED; they do not tie to standalone (standalone PAT Q2FY27 540.44 lakh, RF L301).

Derived (from RF, not stated in PR):
- Other income: 47.3 mn Q2FY27, 81.9 mn Q1FY27, 79.5 mn Q2FY26 (RF L101). -40.5% YoY, -42.2% QoQ.
- Other income / PBT: 41.0% Q2FY27, 64.9% Q1FY27, 69.7% Q2FY26.
- Core EBITDA (EBITDA less other income) on operating revenue: 11.0% Q2FY27, 8.4% Q1FY27, 7.9% Q2FY26; H1 9.7% vs 8.2%.
- Core PBT (PBT less other income): 68.1 mn Q2FY27 vs 44.3 mn Q1FY27 vs 34.6 mn Q2FY26 (+97% YoY, +54% QoQ).
- ETR (PR figures): 24.8% Q2FY27, 24.9% Q1FY27, 24.0% Q2FY26, vs 25.17% statutory.

## 1. FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| FN-01 | F1 | R030, R039, R048, R061, R067 (ZERO_STANDING, corrected); R025, R034, R043, R058, R064 | PR L97, L99, L101, L109, L111; PR L96, L98, L100 | "EBITDA Margin %              16.4%     18.8%            18.1%" | NEUTRAL-FACT (revised from AMBIGUOUS) | After the correction the release shows flat profit growth openly: EBITDA +2.0%, PBT +1.2%, PAT +0.3% YoY (L96, L98, L100). The margin rows have no YoY cell, so the release states no margin change. The reader must compute it: EBITDA margin -240 bps (18.8% to 16.4%), PBT -230 bps, PAT -190 bps; H1 -130 / -110 bps. The CEO quote (L64-L87) does not mention margins. The blank cells anticipate no transaction class; this is ordinary layout. No management question needed; the margin story is carried by FN-03. |
| FN-02 | F16 | R030, R039, R048, R061, R067 | PR L97, L99, L101, L109, L111 | RETIRED | RETIRED | Text-layer artifact, confirmed by the page-3 render (R141). The YoY values sit on the profit rows in the image, so the "margins rose" misread does not exist in the source. No A4 question. |
| FN-03 | F16 | R023-R031, R132 | PR L96-L97; RF L101, L106, L107, L110 | PR "EBITDA 128.2"; RF "2 Other income \| 473.23" | FORWARD-SIGNAL | PR EBITDA = PBT 1,154.43 + finance 46.48 + D&A 81.19 = 1,282.10 lakh, so it includes other income. The reported margin decline is entirely other income. Core EBITDA margin on operating revenue rose to 11.0% from 7.9% YoY and 8.4% QoQ; core PBT nearly doubled YoY. Two readings: real operating leverage from the delivery-mix shift (R116), or one-quarter cost timing. Separator: core margin in Q3FY27 holding above 10%. |
| FN-04 | F16 | R133 | PR L69; RF L101, L212, L235, L405 | "reflecting lower other income compared with the same period last year" | FORWARD-SIGNAL | PR names other income as the PAT driver but never shows the amount. Other income fell to 47.3 mn from 79.5 mn YoY and 81.9 mn QoQ; the QoQ PAT fall of 8.4% has no explanation in the PR. Other income was 41% of PBT this quarter (65% Q1, 70% a year ago). Treasury yield is under pressure from an H1 buyback of 149.8 mn (RF L235) and a 411.3 mn investment in a wholly owned subsidiary (RF L405). Fair-value gains fell to 1.9 mn H1 from 26.5 mn (RF L212). Question: composition and run-rate of other income (interest, FX, MTM). |
| FN-05 | F16 | R117 (UNQUANTIFIED_CLAIM) | PR L68; RF L104-L105, L108 | "our operating revenue grew at a faster pace than our delivery costs" | NEUTRAL-FACT | PR gives no figure; the filing supports the claim. Outsourced + employee cost +20.3% YoY (5,718.20 vs 4,751.94 lakh) and +4.7% QoQ, vs operating revenue +24.7% / +7.1%. Adding other expenses: still +20.4% YoY, +4.0% QoQ. A2 flag resolved; no question needed beyond the FN-03 durability test. |
| FN-06 | F14 | R101 vs R109 (PARTNER_TIER_CONFLICT) | PR L75 vs PR L132-L133 | "Our standing as an Esri Platinum Partner" vs "CyberTech is an Esri Gold Partner" | AMBIGUOUS | Same document states two Esri tiers. If Platinum is new, it is an unannounced upgrade that bears on the geospatial franchise. If the About text is current, the CEO quote overstates. Question: current tier and effective date. |
| FN-07 | F14 | R107, R126 vs R111; R108, R127; R139 | PR L116-L118 vs L131-L132; PR L119-L121; PR L143-L145 | "revenue from the Technology sector ... contributed 68% towards our operating revenue" vs "Serving utilities, government, public safety, manufacturing, and healthcare industries" | AMBIGUOUS | The About section's industry list omits the sector that produces 68% of operating revenue. Candidate reading: clients are technology vendors, possibly platform partners subcontracting work. That would make revenue depend on the partners. US is 99% of revenue (L121), yet the safe-harbour risk list (L143-L145) names no currency or client-concentration risk. Question: who the Technology-sector clients are, top-client and top-5 share, partner-as-customer share. |
| FN-08 | F14 | R080, R083 vs R084 (DATE_MISMATCH) | PR L22, L46-L47 vs PR L59; RF L46 | "Date: October 23, 2026" vs "Mumbai, India - 22nd October, 2026" | NEUTRAL-FACT | PR says "announced today" on 22 Oct. The exchange filing is signed 23 Oct 16:09, about 19.6 hours after the board meeting ended at 20:30 on 22 Oct (RF L46). This is inside 24 hours. Low materiality; it matters only if the release reached media before the exchange upload. |
| FN-09 | F14 | R001-R067, R001 headline | PR L57, L91-L111; RF L100-L115, L301 | "CyberTech Reports Q2FY27 Revenue  780.3 million" | NEUTRAL-FACT | The PR never says whether its figures are consolidated or standalone. All of them tie to consolidated. Subsidiaries carry 37.7% of consolidated PAT (867.73 less standalone 540.44 = 327.29 lakh). The headline "Revenue" is total income including 47.3 mn other income. Downstream stages must not mix PR figures with standalone figures. |
| FN-10 | F6 | R119, R125 (NO_QUANT_GUIDANCE) | PR L74, L85-L86; RF L235, L405 | "we will continue to build on them selectively"; "both in our operations and in how we deploy capital" | FORWARD-SIGNAL | Zero F6 lexicon hits. The PR has no dated or dateable commitment and no quantified guidance; the register below holds only open-ended "continue" statements. The capital-discipline pledge sits beside two H1 deployments the PR does not mention: a 149.8 mn buyback (RF L235) and a 411.3 mn investment in a wholly owned subsidiary (RF L405). Question: purpose of the subsidiary funding, further buybacks, and the capital-allocation rule. |

## 2. CHECKLIST SCORECARD

| check | status | basis |
|---|---|---|
| F1 | FINDING | FN-01 (NEUTRAL-FACT): five blank YoY cells, all on margin rows after the correction (PR L97, L99, L101, L109, L111); margin compression is unstated. |
| F2 | N.A. | PR shows one basis only (consolidated, per tie-out); S-vs-C decomposition belongs to the results-filing A3. The basis-label gap is FN-09. |
| F3 | N.A. | PR carries no cost lines. |
| F4 | N.A. | No auditor report in PR; R134 (PR L36) states "Unaudited". The limited review sits in the results filing. |
| F5 | N.A. | No Going Concern or EoM paragraph; no prior quarter to diff. |
| F6 | FINDING | FN-10: zero lexicon hits, no dateable commitment, five open-ended statements registered. |
| F7 | PASS | No lexicon hit ("may constitute" L141, "could cause" L142 are boilerplate safe harbour, not lexicon terms). No prior release to diff for newly added hedges. Missing FX and concentration risks noted in FN-07. |
| F8 | PASS | ETR from PR PBT and PAT: 24.8% Q2FY27, 24.9% Q1FY27, 24.0% Q2FY26 vs 25.17% statutory. PR carries no deferred tax or earlier-year tax line; those sit with the results-filing A3. |
| F9 | N.A. | No OCI in PR. |
| F10 | N.A. | PR carries no share count, paid-up capital or EPS. |
| F11 | N.A. | PR carries no net worth or reserves figure. |
| F12 | N.A. | No segment assets or liabilities in PR (results note RF L433: single segment). Sector mix 68% Technology and geography 99% US are covered in FN-07. |
| F13 | N.A. | No board outcome in PR (cover letter is a Reg 30 enclosure note only). |
| F14 | FINDING | FN-06 (Esri tier conflict), FN-07 (sector list conflict), FN-08 (dateline vs filing date), FN-09 (basis not labelled, headline revenue is total income). |
| F15 | N.A. | No consolidation entity list in PR; no prior list. |
| F16 | FINDING | FN-03 (EBITDA includes other income), FN-04 (other income undisclosed), FN-05 (R117 claim verified). FN-02 retired as an extraction artifact (R141). Dropped-disclosure test not possible: no prior release. |
| F17 | N.A. | Not a concall; no Notion monitoring checklist, no company memory, no spear. |

## 3. COMMITMENT REGISTER (F6)

No F6 lexicon hit. Each entry is an open-ended management statement with no date.

| commitment | implied date | ref | status word |
|---|---|---|---|
| Build "selectively" on specialized engineering, AI-enabled delivery and cloud | none stated | R119, PR L72-L74 | underway |
| Manage the business "with discipline, both in our operations and in how we deploy capital" | none stated | R125, PR L85-L86 | underway |
| Apply GeoAI "in engagements where location data informs operational decisions" | none stated | R121, PR L76-L77 | underway |
| SAP Migration Factory collaboration to help clients move to SAP cloud | none stated | R123, PR L79-L80 | underway |
| Delivery expanded through own engineers, specialist partners and AI-assisted delivery | Q2FY27 (past tense) | R116, PR L67-L68 | completed |

## 4. FLAGS FOR A4

- Management questions: FN-03, FN-04, FN-10 (FORWARD-SIGNAL); FN-06, FN-07 (AMBIGUOUS).
- FN-01 is now NEUTRAL-FACT and FN-02 is retired. Neither generates a question.
- Results-filing items seen during the tie-out, left to the results-filing A3 (not judged here): tax adjustments for earlier years non-zero (RF L114); paid-up capital movement and the note 3 ESOP wording (RF L124, L432); H1 other income 1,291.78 lakh against about 729.90 lakh of identifiable treasury items in cash-flow adjustments (RF L204, L206, L211, L212).

```yaml
stage: A3-forensics
company: "CYBERTECH"
quarter: "q2fy27"
doctype: "presentation"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/cybertech-q2fy27/work/forensics_pressrelease_cybertech_q2fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: PASS
  F8: PASS
  F9: N.A.
  F10: N.A.
  F11: N.A.
  F12: N.A.
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: N.A.
findings:
  - {id: "FN-01", check: "F1", line: "PR L97, L99, L101, L109, L111; PR L96, L98, L100", classification: "NEUTRAL-FACT", implication: "Corrected table shows flat YoY profit (EBITDA +2.0%, PBT +1.2%, PAT +0.3%); margin rows carry no YoY cell, so the 240/230/190 bps Q2 and 130/110 bps H1 margin falls are unstated; no question, margin story carried by FN-03"}
  - {id: "FN-03", check: "F16", line: "PR L96-L97; RF L101, L106, L107, L110", classification: "FORWARD-SIGNAL", implication: "PR EBITDA includes other income; core EBITDA margin on op revenue 11.0% vs 7.9% YoY and 8.4% QoQ; core PBT +97% YoY; durability test is Q3 core margin above 10%"}
  - {id: "FN-04", check: "F16", line: "PR L69; RF L101, L212, L235, L405", classification: "FORWARD-SIGNAL", implication: "Other income 47.3 mn vs 79.5 mn YoY, 81.9 mn QoQ, undisclosed in PR; 41% of PBT; treasury base cut by 149.8 mn buyback and 411.3 mn subsidiary investment; ask composition and run-rate"}
  - {id: "FN-05", check: "F16", line: "PR L68; RF L104-L105, L108", classification: "NEUTRAL-FACT", implication: "R117 delivery-cost claim verified: outsourced+employee cost +20.3% YoY, +4.7% QoQ vs op revenue +24.7%, +7.1%"}
  - {id: "FN-06", check: "F14", line: "PR L75 vs PR L132-L133", classification: "AMBIGUOUS", implication: "Esri Platinum (CEO quote) vs Esri Gold (About); unannounced upgrade or overstated quote; ask current tier and date"}
  - {id: "FN-07", check: "F14", line: "PR L116-L118 vs L131-L132; PR L121; PR L143-L145", classification: "AMBIGUOUS", implication: "Technology sector is 68% of op revenue but absent from About industry list; possible partner-as-customer dependency; 99% US with no FX or concentration risk in safe harbour; ask client identity and top-client share"}
  - {id: "FN-08", check: "F14", line: "PR L22, L46-L47 vs PR L59; RF L46", classification: "NEUTRAL-FACT", implication: "PR dated 22 Oct, filed 23 Oct 16:09, about 19.6h after board ended; inside 24h; low materiality"}
  - {id: "FN-09", check: "F14", line: "PR L57, L91-L111; RF L100-L115, L301", classification: "NEUTRAL-FACT", implication: "PR basis unlabelled but ties to consolidated; subsidiaries 37.7% of consolidated PAT; headline Revenue is total income incl other income"}
  - {id: "FN-10", check: "F6", line: "PR L74, L85-L86; RF L235, L405", classification: "FORWARD-SIGNAL", implication: "No dated commitment or quantified guidance; capital-discipline pledge silent on H1 149.8 mn buyback and 411.3 mn subsidiary investment; ask capital-allocation rule"}
forward_signals: ["FN-03", "FN-04", "FN-10"]
ambiguous: ["FN-06", "FN-07"]
commitments:
  - {commitment: "Build selectively on specialized engineering, AI-enabled delivery, cloud", implied_date: "none stated", ref: "R119 PR L72-L74", status_word: "underway"}
  - {commitment: "Manage with discipline in operations and capital deployment", implied_date: "none stated", ref: "R125 PR L85-L86", status_word: "underway"}
  - {commitment: "Apply GeoAI in location-data engagements", implied_date: "none stated", ref: "R121 PR L76-L77", status_word: "underway"}
  - {commitment: "SAP Migration Factory collaboration for SAP cloud transitions", implied_date: "none stated", ref: "R123 PR L79-L80", status_word: "underway"}
  - {commitment: "Delivery expanded via own engineers, specialist partners, AI-assisted delivery", implied_date: "Q2FY27 (past tense)", ref: "R116 PR L67-L68", status_word: "completed"}
gate_a3: pass
blank_checks: []
analyst_note: "Revision 2 after the page-3 render (R141). FN-02 is retired as a text-layer artifact. FN-01 is now NEUTRAL-FACT: the release shows flat YoY profit openly, but its margin rows carry no YoY cell. Every PR number ties to the consolidated filing, so the integrity risk is low. The risk is in framing. The PR's EBITDA and all its margins sit on total income, which includes other income. The headline margin fall (18.8% to 16.4%) is therefore an other-income effect. Core EBITDA margin on operating revenue rose to 11.0% from 7.9%, and core PBT nearly doubled YoY. That supports the CEO's delivery-cost claim (FN-05). The bear side is earnings quality: other income was 41-70% of PBT over the three quarters shown. The treasury base shrank after the buyback and the subsidiary funding, and the PR discloses neither. One quarter cannot show whether the core-margin step-up is structural. A4 should ask for the other-income run-rate and the cost mix. The 68% Technology-sector share (FN-07) may point to partner-as-customer dependency."
```
