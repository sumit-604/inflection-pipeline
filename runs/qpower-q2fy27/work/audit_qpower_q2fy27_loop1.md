# A5 ADVERSARY / COMPLETENESS AUDIT, LOOP 1 RE-AUDIT: QPOWER (Quality Power Electrical Equipments Limited), run cycle Q2 FY27

Agent: A5 adversary | model: claude-opus-5-5 | date: 2026-10-20
Under audit: runs/qpower-q2fy27/work/review_qpower_q2fy27.md (A4, revised, 578 lines, loop iteration 1)
Prior audit: runs/qpower-q2fy27/work/audit_qpower_q2fy27.md (INCOMPLETE; F-1 to F-6, M-1 to M-4, S-1 to S-10)
Scope (per task): (1) confirm each prior FACTUAL / MISSING finding is closed; (2) re-run Gate 0 and the coverage audit (TRK M01, M02 added); (3) check new or changed text for new FACTUAL / MISSING / CONTRADICTION errors. No full adversarial pass on unchanged text.
Inputs read (only these):
- runs/qpower-q2fy27/extracted/qpower-egm-q2fy27-fulltext.md (171 lines; all body lines re-read)
- runs/qpower-q2fy27/extracted/qpower-turkiye-q2fy27-fulltext.md (71 lines; all body lines re-read)
- runs/qpower-q2fy27/extracted/qpower-egm-q2fy27-structured.md and qpower-turkiye-q2fy27-structured.md (both unchanged since the first audit; IDs R001-R068 and R001-R028)
- runs/qpower-q2fy27/work/ledger_egm_qpower_q2fy27.md (unchanged) and ledger_turkiye_qpower_q2fy27.md (updated: M01, M02)
- the revised A4 review and the prior A5 audit
Not opened: source PDFs, anything under inputs/, A3 forensics files, notion-brief.md. A4's statements about A3 (TRK-FN-05 added, "20 of 20", "gate_a3 pass", "TRK 30 of 30 units") and the Notion "earlier Rs1,400 CMP" sit outside A5 inputs. They are not verified here; their arithmetic is checked.
Anchors: "EGM Lnnn" / "TRK Lnn" = line in the A1 fulltext. "RV Lnnn" = line in the revised A4 review. "TL Lnn" = line in the TRK ledger.

---

## A. PRIOR-FINDING CLOSURE

| Prior ID | Type | Gap | Where A4 fixed it | Re-check | Status |
|---|---|---|---|---|---|
| F-1 | FACTUAL | "about 59%" fall | RV L246, L425, L573 | 1 - 570/1,513.4 = 62.34% -> 62.3%; 1 - 456/1,513.4 = 69.87% -> 69.9%; 1 - 570/1,400 = 59.29% -> 59.3% (memory basis, labelled [INFERENCE]) | CLOSED |
| F-2 | FACTUAL | "no financial number" | RV L74, L415 | Both read "no financial statement or a results figure"; RV L74 adds that the EGM transaction figures (700 crore, 175 crore, 9%) sit in 2B. Matches EGM L106, L110 | CLOSED |
| F-3 | FACTUAL | "Both cannot be true"; "not explained" | RV L421, L393, L296 | "The two terms pull apart"; "The filing gives one reason for the loan, which is timing"; gap restated as why March 2026 net cash [Notion] cannot cover the deal; "Present cash is ND". Flag 2: "An 11-year facility can still bridge the deal". Matches EGM L109-111 | CLOSED |
| F-4 | FACTUAL | "WSIL will become a new subsidiary" | RV L116, L185, L224, L272, L303 | Stake and status ND in filed text; [Notion] up to 100%; consolidation and goodwill conditional ("IF completion delivers control"). Grep finds no "will become" / "subsidiary on completion" left | CLOSED |
| F-5 | FACTUAL | "Equity markets are open to the sector" | RV L432 | Graft carried verbatim in substance; cites EGM L106, L140-141, L110-111. Grep finds no remnant | CLOSED |
| F-6 | FACTUAL | "5 drafting defects" | RV L370-378, L402, L572 | 7 enumerated plus a possible eighth. Each item checks against the fulltext: L110-111; L59-67; L69-78; L70; L98; L100; L136-139; L98-102 | CLOSED |
| M-1 | MISSING | TRK L41-43 and L45 clause had no row | TL L3, L12, L53-55; RV L33, L144-145, L222-223, L279-280, L338, L438, L448 | M01 verbatim = TRK L41-43 exactly; M02 verbatim = TRK L45 exactly. Count test row added (TL L12). A4 cites both. (A3 review of them: outside A5 inputs; A4 records TRK-FN-05 and TRK-FN-03 citing M02, RV L38) | CLOSED |
| M-2 | MISSING | Claim 1 counter (no filed target date; manufacturing start vs commercial production) | RV L168, L220, L226, L258, L399, L417, L569 | "NOT YET A COUNTER-EXAMPLE"; "no target date of its own"; "not commercial production"; "Sangli slip is measured on commercial production". Grep finds no "first time" / "DELIVERED EARLY" left. TRK L41-43 cited in Business-Model (RV L438) | CLOSED |
| M-3 | MISSING | Acquisition-economics test | RV L256, L330, L400, L440, L468, L570 | Price/PAT NOT COMPUTABLE; 16.0x sales; 51.5% margin at 31x; Rs11.15 Cr carry = 65.3% of sales; M6 bull fork states the margin it needs. Figures recompute (Section 2) | CLOSED |
| M-4 | MISSING | "present" qualifier dropped; board size ND | RV L126-128, L306, L337, L398, L471, L559, L568 | "3 or 4 of the 8 directors present"; "Board size ND"; Reg 17(1)(b) floor labelled [INFERENCE, regulation]. Grep finds no "4 of 8" left | CLOSED |

STYLE carry-through: S-2 (A4 part), S-3, S-4, S-5, S-6, S-7, S-8, S-9, S-10 applied (RV L56-58, L63; L40-42; L129-130; L513; L387, L392, L419; L279; L112, L249, L261, L274, L326; L110, L326, L393, L459; L429). S-1 not applied (A1/A2 item, RV L499). S-2 A2 part not applied (EGM ledger L14 still says "170 lines"). Both stay STYLE and are carried below.

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate): PASS

| Part | Heading in review | Content found | Status |
|---|---|---|---|
| 1 Summary narrative | "### 1. SUMMARY NARRATIVE" (RV L413) | 6 paragraphs, 362 words by whitespace count (Document Review Protocol governs: 200-400 band) | present |
| 2 Sector intelligence | "### 2. SECTOR INTELLIGENCE" (RV L427) | 5 bullets, real content; bullet 1 tier-tagged | present |
| 3 Business-model intelligence | "### 3. BUSINESS-MODEL INTELLIGENCE" (RV L435) | 7 bullets, including the M01/M02 strand and the WSIL economics graft | present |
| 4 Competition intelligence | "### 4. COMPETITION INTELLIGENCE" (RV L445) | 4 bullets | present |
| 5 Forward map | "### 5. FORWARD MAP" (RV L452) | 14 catalyst rows (RV L458-471), each with a bull fork and a bear fork; dated where the text allows, honest "Date ND" / "Undated" fills elsewhere | present |

Gate 0 passes.

---

## 1. COVERAGE AUDIT: PASS

Method: every body line of both fulltexts re-read; digit-token sweep repeated; each unit mapped to an A1 row ID or an A2 M-row; then each ledger row mapped to an A4 citation (by ID, by line or content, or the explicit no-finding list at RV L40-42).

### 1A. Fresh enumeration vs A2 ledger

| Doc | Category | A2 count | A5 fresh count | Diff | Orphan rows | Status |
|---|---|---|---|---|---|---|
| EGM | Structured IDs R001-R068 | 68 | 68 (contiguous; 24+24+5+12+3; structured file unchanged) | 0 | none | PASS |
| EGM | NUMBER units | 24 (+ Reg 30 in M2, Plot L-61 in M4) | 27 (+ same 2) | +3 address boilerplate: Plot No. C/1 and 400 001 (L23), 400 051 (L25) | none | PASS (STYLE S-1, carried) |
| EGM | ENTITY units | 24 | 24 | 0 | none | PASS |
| EGM | FORWARD units | 5 | 5 | 0 | none | PASS |
| EGM | DATE units | 12 | 11 document dates + 1 task label (R065) | 0 | none | PASS |
| EGM | QUALIFIER units | 3 | 3 | 0 | none | PASS |
| EGM | Agenda items | 3 | 3 (L136-144) | 0 | none | PASS |
| EGM | A1 foot notes | 2 | 2 | 0 | none | PASS |
| EGM | MISSING_FROM_STRUCTURED | 5 (M1-M5) | 5 (L90, L33, L145-147, L150-152, L95-97) | 0 | none | PASS |
| TRK | Structured IDs R001-R028 | 28 | 28 (7+12+2+7+0; structured file unchanged) | 0 | none | PASS |
| TRK | NUMBER units | 7 | 7 | 0 | none | PASS |
| TRK | ENTITY units | 12 | 12 | 0 | none | PASS |
| TRK | FORWARD / claim units | 2 + M01, M02 = 4 | 4 (L41-43; L45 first clause; L46-48; L50-51) | 0 | none | PASS |
| TRK | DATE units | 7 | 7 (5 date-type + 2 non-dates R026, R028, A2 flagged) | 0 | none | PASS |
| TRK | QUALIFIER / footnotes | 0 | 0 | 0 | none | PASS |
| TRK | Slides | 1 (S1) | 1 | 0 | none | PASS |
| TRK | MISSING_FROM_STRUCTURED | 2 (M01, M02) | 2 | 0 | none | PASS (prior M-1 closed) |

TRK line map (fresh): L19 R022; L21-25 R008, R009, R002-R004, R019; L27 R001, R010; L29-30 R005, R006, R025, R012, R013; L34-36 R013, R011, R012, R023; L38-39 R014, R015; L41-43 M01; L45 M02; L46-48 R021, R016; L50-51 R020; L53-54 R027; L60 R017; L62-65 R026, R024; L67-69 R018; L71 R007. No body line is unmapped.

### 1B. Ledger rows vs A4 citations (orphan test)

| Doc | Ledger rows | Cited by ID | Cited by line or content | Explicit no-finding list (RV L41-42) | Orphans |
|---|---|---|---|---|---|
| EGM | 68 IDs | 36: R005-R009, R011-R014, R021, R022, R024, R025, R026, R028, R031, R041, R043, R045-R053, R056-R062, R065, R067 | 15: R010 (L69-78, RV L373), R019-R020 (L122-123, RV L125), R030 and R032-R037 (L57-67, RV L126-128, L171, L306), R038 (L69-78, L98, RV L373-375), R055 (L29, RV L24, L396), R063 (L55, RV L123), R064 (L154-155, RV L124), R068 (L124-126, RV L275) | 19: R001-R004, R015-R018, R023, R026, R027, R029, R039, R040, R042, R044, R054, R060, R066 (R026, R060 also cited by ID) | none |
| EGM | agenda 3, foot notes 2, M1-M5 | M1 (RV L122) | agenda (RV L118-119); foot notes (RV L32, L36); M2 (RV L5); M3 (RV L172, L304); M4 (RV L269); M5 (RV L208, L297-298) | n/a | none |
| TRK | 28 IDs | 15: R003, R011-R016, R019-R024, R026, R028 | 0 | 14: R001, R002, R004-R010, R017, R018, R022, R025, R027 (R022 also cited by ID) | none |
| TRK | M01, M02, S1 | M01 (RV L33, L144, L222, L280, L338); M02 (RV L33, L145, L223, L279); S1 (RV L33-34) | | | none |

Result: orphan_rows none; missing_from_ledger none. Coverage passes. Two residual anchor slips stay STYLE (S-2r below).

---

## 2. ARITHMETIC AUDIT: PASS

Neither fulltext carries a financial statement. Operating EBITDA, margins, effective tax rate, S-vs-C gaps, YoY, QoQ and the PAT bridge stay ND (RV L74-89, L159-163, L178-181). Confirmed. Checked below: every figure in new or changed text, plus carried figures the new text reuses.

| # | Metric | A4 value (RV line) | Recomputed | Raw inputs (source line) | Status |
|---|---|---|---|---|---|
| 1 | Fall from page CMP to Rs570 | 62.3% (RV L246, L425, L573) | 1 - 570/1,513.4 = 62.34% | RV L17 page figures (memory) | PASS |
| 2 | Fall from page CMP to MoS Rs456 | 69.9% (RV L246, L573) | 1 - 456/1,513.4 = 69.87% | RV L17 (memory) | PASS |
| 3 | Notion "59%" on the Rs1,400 basis | 59.3% (RV L246) | 1 - 570/1,400 = 59.29% | Rs1,400 is memory, unverified; arithmetic only | PASS |
| 4 | Reading B interest over 11 years at full draw | Rs173.25 Cr (RV L110, L326, L393, L459, L563) | 15.75 x 11 = 173.25 | EGM L110 | PASS |
| 5 | Bridge interest a year at full draw | 15.75 crore (RV L109, L257, L421) | 175 x 9% = 15.75 | EGM L110 | PASS |
| 6 | Start vs memory target | 46 to 76 days (RV L168) | 16-Oct to 1-Dec = 46; to 31-Dec = 76 | TRK L36; Dec 2026 is memory | PASS |
| 7 | WSIL price / FY26 sales | about 16.0x (RV L256, L400, L440, L468, L570) | 272.34 / 17.07 = 15.95 | memory inputs | PASS |
| 8 | PAT needed at 31x | Rs8.79 Cr (RV L330) | 272.34 / 31 = 8.785 | memory inputs; 31x per RV L405 | PASS |
| 9 | Net margin needed at 31x | 51.5% (RV L330, L400, L440, L468, L552) | 8.785 / 17.07 = 51.47% | memory inputs | PASS |
| 10 | Cash-leg carry at 9% | Rs11.15 Cr a year (RV L330, L400, L440, L570) | 123.84 x 9% = 11.146 | EGM L110 rate; 123.84 memory arithmetic | PASS |
| 11 | Carry as share of WSIL sales | 65.3% (RV L400, L570); 65% (RV L440) | 11.146 / 17.07 = 65.29% | as above | PASS |
| 12 | Facility over cash leg | about Rs51 Cr (RV L296, L315, L394) | 175 - 123.84 = 51.16 | EGM L110 + memory | PASS |
| 13 | Ledger units | 103 = 96 + 7; EGM 73; TRK 30 (RV L31-33) | 68 + 28 = 96; 5 + 2 = 7; 68 + 5 = 73; 28 + 2 = 30 | both ledgers | PASS |
| 14 | A3 findings incorporated | 20 of 20 (RV L38, L517) | 15 EGM + 5 TRK = 20 | count only; A3 content outside inputs | PASS |
| 15 | Drafting tally | 7 plus a possible eighth (RV L370-378, L402, L572) | 7 enumerated items, each found in EGM text; eighth = L98-99 and L100-102 | EGM L59-67, L69-78, L70, L98, L100, L110-111, L136-139 | PASS |
| 16 | Summary narrative length | 6 paragraphs (RV L415-425) | 362 words (whitespace count) | Gate 0 band 200-400 | PASS |

arithmetic_mismatches: none.

---

## 3. ADVERSARIAL READ (scope: graft check plus new text)

### Prior surviving counters: graft status
- Claim 1 (Nigde "delivered early" / "first counter-example"): grafted (RV L226, L399, L417). The positive claim is gone from every location. No residual.
- Claim 2 (WSIL "answers a real supply constraint"; bull fork "adds to earnings"). MANDATORY ACQUISITION-ECONOMICS PROBE, re-stated: ~Rs272.34 Cr consideration [Notion] / WSIL PAT NOT FOUND = price/PAT NOT COMPUTABLE; ~16.0x FY26 sales; at 31x WSIL needs PAT of Rs8.79 Cr, a 51.5% net margin; the cash-leg carry at 9% is ~Rs11.15 Cr a year, 65.3% of WSIL sales. ROCE, debt, cash and customer tenure stay ND in both extracts (EGM L103-105). Grafted (RV L440, L330, L400, L468, L449). The bear reading survives and is now in the review. No residual.
- Claim 3 ("Equity markets are open to the sector"): replaced (RV L432). No residual.

### New or changed text: the most positive claims
- RV L438, bullet 2: "It also claims new 'system integration capabilities' (MGMT, TRK L45)." This misreads the filed verb. See F-7.
- RV L439: "In-house converters may raise the value the group keeps per storage system (INFERENCE)." The same bullet carries the counter (tilt toward Turkey; 49% to minority holders), and so does RV L450 (in-group-only risk). Tagged INFERENCE. The text is carried from the first pass, so it is not re-opened.
- RV L337, M13 bull: "at least half independent" is now a floor, not a bull case (graft M-4). Balanced.

No new surviving bear counter beyond F-7.

---

## 4. NEW FINDINGS IN CHANGED TEXT

F-7 (FACTUAL, A4). RV L438 reads: "It also claims new 'system integration capabilities' (MGMT, TRK L45)." TRK L45, verbatim: "The new facility strengthens the Group's manufacturing and system integration capabilities,". The word "new" in the letter describes the facility. The capability is "strengthened", so the letter presents it as one the group already has. A4's own 2C row quotes the verb correctly (RV L145, "strengthens"). The brief bullet therefore disagrees with both the filing and A4's own table.
- Why it matters: the M01/M02 rows were added to answer the archetype question in the signed model (component maker or system integrator). "Strengthens" points to an existing integration capability going deeper. "New" points to a model change. The bullet's two readings (planned growth line vs drift from the HVDC core) rest on that premise.
- The same premise is in Q19 (RV L310, "What does 'system integration capabilities' (L45) add that the group did not have?") and in its YAML copy (RV L542).
- Fix (A4): RV L438: "It also says the plant 'strengthens' the group's 'manufacturing and system integration capabilities' (MGMT, TRK L45)." Q19 and RV L542: "How does the plant change the group's system integration capability (L45), and which BESS projects used outside integration before?" (or any wording that does not presume the capability is new). No A2 or A3 re-run is needed.

---

## VERDICT

INCOMPLETE.
- All ten prior loop findings (F-1 to F-6, M-1 to M-4) are CLOSED. Gate 0 passes. Coverage passes, with no orphan and no missing row. Arithmetic passes.
- Failing agent: A4 only.
- Finding types this loop: FACTUAL 1 (F-7), MISSING 0, CONTRADICTION 0, STYLE 5.
- Exact gap: F-7, the misread of TRK L45 at RV L438 ("claims new" vs the filed "strengthens"), and the same premise in Q19 (RV L310, L542).
- No finding moves the process verdict (PROCEED WITH FLAGS; cash conversion INDETERMINATE caps it) or Decision Status WATCHLIST.

## STYLE NOTES (logged; none re-runs an agent on its own; may ride the A4 fix)

- S-1 (A1/A2, carried): EGM address numbers Plot No. C/1 and 400 001 (L23) and 400 051 (L25) are still not itemised. The TRK file itemises the same boilerplate (TRK R002-R004 under R019).
- S-2r (A2, residual): the EGM ledger still says "170 lines" (EGM ledger L14); the A1 header says 171. The new TRK ledger M02 note says "remainder of L45-47 is R021" (TL L55); R021's verbatim runs L46-48, as A4's anchor table records (RV L63).
- S-11 (A4, carried text, logged only): RV L441 says "the group now funds growth with outside equity, a share swap and promoter debt at once". Flag 1 (RV L392) says to treat the QIP, swap and RPT as proposed until the vote result. Write "plans to fund ... (proposed; vote result ND)".
- S-12 (A4): RV L417, "These converters go into large battery storage systems", drops "and other grid-connected applications" (TRK L38-39). A4's own 6B row reads the scope as wider than BESS (RV L222).
- S-13 (A4): RV L448 ("a technology the group calls new to it") and RV L364 ("names a new strand") put the word "new" in the company's mouth. The letter says "expansion into" and "complementing its established portfolio" (TRK L41-43). RV L259 shortens the portfolio to "established high-voltage portfolio" and drops "power quality solutions" (TRK L42-43). Quote the filed words.

---

```yaml
stage: A5-adversary
company: "QPOWER"
quarter: "Q2 FY27"
model: "claude-opus-5-5"
status: complete
verdict: INCOMPLETE
plain_language_brief:
  narrative: present
  sector: present
  business_model: present
  competition: present
  forward_map: present
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches: []
surviving_bear_counters: []
findings_by_type:
  factual:
    - "F-7 RV L438: 'It also claims new system integration capabilities (MGMT, TRK L45)' misreads TRK L45 'The new facility strengthens the Group's manufacturing and system integration capabilities'; 'new' modifies the facility, the capability is 'strengthened' (existing). A4's own 2C row RV L145 quotes 'strengthens'. Same premise in Q19 RV L310 and YAML RV L542 ('add that the group did not have'). Fix A4."
  missing: []
  contradiction: []
  style:
    - "S-1 EGM address numbers L23, L25 not itemised (A1/A2, carried)"
    - "S-2r EGM ledger '170 lines' vs 171; TRK ledger M02 note 'remainder of L45-47' should be L46-48 (A2)"
    - "S-11 RV L441 'now funds growth' states proposed items as done (A4, carried text)"
    - "S-12 RV L417 drops 'and other grid-connected applications' (TRK L38-39) (A4)"
    - "S-13 RV L448, L364 'new' put in company's mouth; RV L259 drops 'power quality solutions' (A4)"
loop_back_to: "A4"
gap: "F-7 (FACTUAL): RV L438 says the company 'claims new system integration capabilities'; TRK L45 says the facility 'strengthens' them (an existing capability), and A4's own RV L145 quotes 'strengthens'. Fix RV L438 to the filed verb, and reword Q19 (RV L310) and its YAML copy (RV L542) so they do not presume the capability is new. All prior findings F-1 to F-6 and M-1 to M-4 are closed; no A2 or A3 re-run needed. STYLE S-1, S-2r, S-11 to S-13 may ride the same fix."
style_notes:
  - "S-1 (A1/A2, carried): EGM Plot No. C/1 and 400 001 (L23), 400 051 (L25) not itemised; TRK itemises the same boilerplate (R002-R004 under R019)."
  - "S-2r (A2): EGM ledger L14 '170 lines' vs A1 header 171; TRK ledger L55 M02 note 'remainder of L45-47 is R021' -> L46-48 (A4 anchor table RV L63 already has 46-48)."
  - "S-11 (A4, carried text): RV L441 'the group now funds growth with outside equity, a share swap and promoter debt at once' -> 'plans to fund ... (proposed; vote result ND)', per flag 1 RV L392."
  - "S-12 (A4): RV L417 'These converters go into large battery storage systems' -> add 'and other grid-connected applications' (TRK L38-39); A4's 6B row RV L222 reads scope as wider than BESS."
  - "S-13 (A4): RV L448 'a technology the group calls new to it' and RV L364 'names a new strand' -> quote 'expansion into' / 'complementing its established portfolio' (TRK L41-43); RV L259 'established high-voltage portfolio' drops 'power quality solutions' (TRK L42-43)."
analyst_note: "Loop 1 re-audit. All ten prior loop findings (F-1 to F-6, M-1 to M-4) are closed. The TRK ledger now carries M01 (L41-43) and M02 (the L45 clause), both verbatim-exact. The fresh coverage pass matches both ledgers with no orphan. Every grafted figure recomputes: 62.3% / 69.9%, Rs173.25 Cr, 16.0x sales, 51.5% margin at 31x, Rs11.15 Cr carry at 65.3% of sales. The brief narrative runs 362 words. One new FACTUAL error sits in new text. The Business-Model bullet says the company 'claims new system integration capabilities', but TRK L45 says the plant 'strengthens' them, and A4's own 2C row quotes 'strengthens'. The difference bears on the archetype question the M01/M02 rows were added to answer. 'Strengthens' points to an existing integrator going deeper, not a model change. Q19 carries the same premise. The fix is two lines in A4, with no A2 or A3 re-run. A4's claims about A3 (TRK-FN-05, 20 of 20, gate_a3) and the earlier Rs1,400 CMP are outside A5 inputs and unverified; the arithmetic on them holds. No finding moves PROCEED WITH FLAGS or WATCHLIST."
```
