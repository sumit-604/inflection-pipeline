# A5 ADVERSARY AUDIT: Cyient DLM (CYIENTDLM) Q2 FY27, ROLE 5 ADDENDUM

Agent: A5 adversary | Model: claude-opus-5-5 | Audit date: 2026-10-18
Scope: the "## ROLE 5: CONCALL ANALYSIS" section (review L647-L1230) and every "(Role 5 addendum)" passage in the merged review. The Role 4 body was audited and closed earlier (audit_cyientdlm_q2fy27.md, loop 2, open item OI-1).
Inputs read: review_cyientdlm_q2fy27.md (1,468 lines); concall A1 fulltext (488 lines) and structured (R001-R303, T001-T097); concall A2 ledger; results fulltext (P&L authority L533-L565, balance sheet L135-L190, cash flow L206-L262, notes L280-L291); presentation fulltext (L140-L454).
Not read: the source PDF, the audio, anything under inputs/, A3 reasoning. A3 CF IDs were checked only for presence in the review.
Anchors: "cc L###" = concall fulltext; "res L###" = results fulltext; "pres L###" = presentation fulltext; "rev L###" = review line.
Source caveat applied: the concall is a machine transcript with inferred speakers. No finding below treats a misheard number as management error.

---

## DELIVERABLE-COMPLETENESS AUDIT (gate)

| Part | Heading (rev line) | Status |
|---|---|---|
| 1. Summary narrative | "### 1. Summary narrative" (rev L1240-L1277) | PRESENT (25 bullet lines plus a call-vs-filing table; above the 10-20 line spec, see STYLE S2) |
| 2. Sector intelligence | rev L1279-L1288 | PRESENT |
| 3. Business-model intelligence | rev L1290-L1300 | PRESENT |
| 4. Competition intelligence | rev L1302-L1308 | PRESENT |
| 5. Forward map | rev L1310-L1326; 16 dated rows, each with a bull and a bear fork | PRESENT |

Gate: PASS. All five parts exist and carry real content.

---

## COVERAGE AUDIT (concall)

Fresh grep pass over the concall fulltext: moderator cue lines ("question comes", "last question", "Please go ahead", "hand the conference", "dropped from the queue", "not receiving a response").

| Category | A2 count | Fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Question slots (moderator cue lines cc L191, L219, L241, L268, L271, L322, L364, L370, L421, L448) | 10 | 10 | none | MATCH |
| Analysts who asked (Meeth Jain no response cc L268-L270; Suman Kumar dropped cc L364-L369) | 8 | 8 | none | MATCH |
| Moderator turns | 17 | 17 | none | MATCH |
| Total turns T001-T097 | 97 | 97 (moderator turns verified; non-moderator boundaries are A1 speaker-change inferences, not independently countable) | none | MATCH |
| Question turns (A1 QUESTION tag; T043, T045, T080 are clarifications) | 26 | 26 | none | MATCH |
| Participants | 14 | 14 | none | MATCH |
| Numbers | 160 | 161 (cc L238 "In the last two quarters, we have the revenues on that", T017, semicap revenue period: no structured row) | none | FAIL: 1 unit missing from structured and ledger (R5-M4, A2) |
| Forward | 53 | 53 (plus a routine next-call commitment at cc L485-L486, minor) | none | MATCH (minor note in R5-M4) |
| Entities / dates / qualifiers | 37 / 22 / 31 | 37 / 22 / 31 | none | MATCH |
| Ledger rows R001-R303 cited or marked reviewed in Role 5 | 303 | 303 (blanket "all 303 ledger rows" statement, rev L656; spot-checked 60 structured rows against the fulltext: only the two anchor defects A4 already logs, R294 and R177) | none | PASS |
| A3 concall findings CF01-CF25 cited | 25 | 25 (grep: every CF ID appears; CF19, CF22, CF23 marked NEUTRAL-FACT at rev L578) | none | PASS |
| 4A inventory covers the 26 question turns | 26 | 26 (24 graded exchanges; T024+T026 and T074+T076 combined) | none | PASS |

Coverage verdict: no orphan row. One fresh-pass unit is missing from the structured file and the ledger (cc L238). A4 already cites cc L238 nine times from the fulltext, so the review lost nothing. The fix is a ledger annotation only (R5-M4).

---

## ROLE 4 INTEGRITY (no HEAD diff available; tie-out to the filing instead)

| Table | Cells recomputed from res L538-L565 (Rs Mn x 0.1) | Result |
|---|---|---|
| 1A consolidated, all 19 line rows x 6 periods, plus the 10 derived rows | about 125 | All tie (e.g. op EBITDA Q2 FY27 393.13 + 113.71 + 61.01 - 226.15 = 341.70 Mn = 34.17 Cr; gross margin 1,470.59 / 3,930.90 = 37.41%) |
| 1B standalone (revenue, PAT, op EBITDA, gross margin) | 12 | All tie |
| 1C / 1D (subsidiary op EBITDA 11.51 Mn; gap % all six periods) | 14 | All tie |
| 2A / 2B headline rows | 8 | All tie |
| Step 4 PAT bridge main rows (8.28, (5.30), (0.81), +0.71, (0.05), (0.97), +1.87) | 7 | All tie |
| Step 8.5 Q1-Q30 embedded figures (Q3, Q7, Q10, Q12, Q13, Q20, Q22, Q23, Q24) | 12 | All tie |
| Acquisition probe (5.4x, 25.6x, (18.17) Mn, 32.0%, 4.4x) | 6 | All tie |

Result: PASS. No Role 4 table number deviates from the filing. The only Role 4 table edits are marked "(Role 5 addendum)": the new ANSWER STATUS column, Q31-Q42, and the Q10 bull answer (OI-1).

OI-1 check: CORRECTED. The Q10 bull answer (rev L542) now reads "Internal cash plus the standalone short-term line drawn in H1 (Rs 287.91 Mn), repaid from H2 collections; finance cost holds near Rs 61 Mn a quarter". It ties to res L177 and L565 (standalone current borrowings 287.91 Mn) and res L544 (61.01, 61.23 Mn). The consolidated borrowing rise of 258.35 Mn is all standalone (subsidiary borrowings fell 29.56 Mn: 1,031.69 vs 1,061.25), so the corrected text no longer conflicts with the filing.

---

## ARITHMETIC AUDIT (Role 5 section and addendum passages)

| Metric | A4 value (rev line) | Recomputed | Source line | Status |
|---|---|---|---|---|
| Prepared remarks share | 1,580 s = 43.0% (L707) | 1,580 / 3,674 = 43.0% | cc L186, L488 | OK |
| Q&A share | 1,987 s = 54.1%; 33:07 (L708, L1205) | 3,567 - 1,580 = 1,987 s; 54.1% | cc L186, L470 | OK |
| Close share | 107 s = 2.9% (L709) | 3,674 - 3,567 = 107 s; 2.9% | cc L470, L488 | OK |
| Claim type count | 27/9/7/6/5/5/2 = 61 (L789) | recounted 61 rows: same | rev L727-L787 | OK |
| Quantified share | 43/61 = 70.5%; forward 6/11 = 54.5% (L792) | 43/61 = 70.49%; 6/11 = 54.5% | rev L727-L787 | OK |
| FY27 revenue at +30-35% | 1,639.94-1,703.01 Cr (L827) | 12,614.85 Mn x 1.30 / 1.35 = 1,639.93-1,703.00 Cr | res L538 | OK (0.01 rounding) |
| H2 FY27 revenue and growth | 873.05-936.12 Cr; +29.8% to +39.2% (L827) | 873.05/672.42 = 1.298; 936.12/672.42 = 1.392 | res L538 | OK |
| H2 margin at 9% FY27 | 8.51-8.54% (L827, L1221) | (147.59 - 73.33)/873.05 = 8.51%; (153.27 - 73.33)/936.12 = 8.54% | res L538-L548 | OK |
| H2 margin at 10% FY27 | 10.36-10.38% (L827) | 90.66/873.05 = 10.38%; 96.97/936.12 = 10.36% | res L538-L548 | OK |
| H2 per quarter vs Q2 | 436.5-468.1 Cr; +11-19% (L828) | 436.53/393.09 = 1.111; 468.06/393.09 = 1.191 | res L538 | OK |
| S&M freeze threshold | about Rs 7,862 Mn a quarter (L820) | 2 x 3,931 = 7,862 | cc L126, L288 | OK |
| P09 H2 floor / Q3 bar | 874.15 Cr / 394.29 Cr (L856) | 672.42 x 1.3 = 874.15; 303.3 x 1.3 = 394.29 | res L538; pres L249 | OK (test design: see R5-M2) |
| P10 intake fit | "600 crores plus" fits the walk (L547) | 28,137 - 25,989 + 3,930.90 = 6,078.90 Mn = 607.9 Cr | pres L289-L294; res L538 | OK |
| Specificity ratio | 29/53 = 0.547; de-dup 22/46 = 0.478 (L1036-L1037) | ID lists recounted: 29 + 24 = 53, no gaps or duplicates; 7 quantified restatements collapsed | ledger R198-R250 | OK |
| Defensive phrases / "probably" | 11 / 12; analyst "we expect" 6 excluded (L1048-L1051) | grep: refusal 3, deferral 2, "we believe" 3, "we expect" 3; "probably" 12 in management turns | cc L46-L461 | OK |
| 4A grade tally | A3 B11 C5 D4 E1 = 24; C/D/E 41.7% (L928) | recounted 24 rows: same; 10/24 = 41.7% | rev L901-L926 | OK |
| Earnout share of Q2 other income | 80.4% (L571, L953, L1080, L1182, L1220, L1273, L1448) | 181.95 / 226.15 = 80.46%, rounds to 80.5% | res L288, L539 | STYLE S1 (A4 divided by the rounded 226.2) |
| Other-income residual | 25.2 Mn (L954, L1080) | 226.15 - 181.95 - 19.01 = 25.19 | res L286, L288, L539 | OK |
| Combined opex ratio YoY | 31.18% to 28.72%, -245 bps (L1075) | 31.176% to 28.718% = -245.75 bps | res L538, L543, L546 (529.42 corrected base) | OK (rounding; STYLE S10) |
| H1 gross margin fall | -307 bps (L946) | 40.739% to 37.671% = -306.8 bps | res L538, L541, L542 | OK |
| Finance cost YoY, H1 | -10.4%; H1 -20.8% (L1081) | 61.01/68.11 = -10.42%; 122.24/154.27 = -20.76% | res L544 | OK |
| Gross borrowings H1 | +24.3% (L1082) | 1,319.60 / 1,061.25 = +24.34% | res L170, L177 | OK |
| Order book QoQ / YoY | +2.1 bn / +5.2 bn CONFIRMED (L1083) | 28,137 - 25,989 = 2,148; 28,137 - 22,911 = 5,226 | pres L289-L294 | OK |
| Book walk | 1.55x (L1084) | 6,078.90 / 3,930.90 = 1.546x | pres L289-L294; res L538 | OK |
| H1 CFO minus capex | 4.11 Mn (L1087) | 147.51 - 143.40 = 4.11 | res L229, L234 | OK |
| H1 revenue / EBITDA growth | +30.19% / +30.4% (L1088) | 7,668.90/5,890.61 = +30.19%; 733.33/562.51 = +30.37% | res L538-L548 | OK |
| H1 normalized / reported PAT growth | +60.3% / +27.0% (L1089) | 321.04/200.33 = +60.26%; 502.99/396.08 = +26.99% | res L552, L213, L288 | OK |
| Subsidiary Q2 op EBITDA margin; PAT ex-earnout | 1.17%; (3.56) Cr (L1091) | 11.51/982.98 = 1.17%; 146.35 - 181.95 = (35.60) Mn | res L538-L552, L288 | OK |
| Normalized PAT margin | 4.02% vs 4.05% (L1094) | 158.19/3,930.90 = 4.02%; 125.70/3,106.34 = 4.05% | res L538, L552; pres L392 | OK |
| Subsidiary DT credit | 14.48 Mn (L1078) | (16.12) - (1.64) = (14.48) | res L550 | OK |
| QoQ margin split | -178 = GM -53, employee +3, other +122 (L946) | -178.4 = -53.3 + 3.3 + 121.8 (sign as margin effect) | res L538-L546 | OK |
| B2S run-rate | $111-143 Mn a year (L979) | 1,000/9 = 111.1; 1,000/7 = 142.9 | cc L309, L431 | OK |
| Win ratio check | 40% x $1.5 bn = $600 Mn (L982) | 0.40 x 1,500 = 600 | cc L262, L338 | OK |
| Material ratio rise, "filed" | +379 bps (L1104) | filed basis: 62.589% vs 58.782% = +380.7 bps; 379 is the deck-rounded basis | res L538, L541, L542; pres L376 | STYLE S3 |
| Industry mix under the call's mapping | not computed; Role 4 range 881.7-981.0 Mn and "6-15%" carried (L1090, L1242, L1283, L1303) | call shares cc L151-L152: Aerospace + Industrial 981.0 Mn = 119.0% of 824.56 Mn; Aerospace alone 707.1 Mn = 85.8%; other 22% fell 15.3% (1,021.3 to 864.8 Mn); with +/-0.5 pp share rounding 969-993 Mn (118-120%) and -14% to -17% | cc L151-L152; res L538 | MISSING (R5-M3) |
| Q3 pass at the 30% bar | not computed | Q3 at 394.29 Cr = +0.3% QoQ on 393.09; then Q4 needs 874.15 - 394.29 = 479.86 Cr (+21.7% QoQ; +30.0% YoY on 369.1) | res L538; pres L247-L249 | MISSING (R5-M2) |

No arithmetic mismatch above rounding. Two numbers the review needed but did not compute are under R5-M2 and R5-M3.

---

## ANSWER-STATUS GRADE TEST (ANSWERED and PARTIALLY rows)

| Q | A4 grade | Test against the extract | A5 grade |
|---|---|---|---|
| Q19 numeric FY27 revenue guide | ANSWERED | Analyst offered 30-35% (cc L353); reply "I think now probably yes" (cc L354) with a material caveat (cc L356-L357). But "for the H2, we will definitely be going above 30% growth" (cc L361) is management's own numeric floor. H1 is +30.19%, so the FY floor follows. The review already records the hedge and the analyst origin (rev L805). | ANSWERED stands |
| Q4 gross-margin split | PARTIALLY | The split was asked (cc L222-L223, including PCBA vs Box Build) and deflected: "a mix of various factors" (cc L225-L228), graded D in 4A (rev L903). T039 then gave a direction (not mix, S&M; cc L282-L290). Directional answer, no split, no component cost. | PARTIALLY defensible; cell should cite the deflection (STYLE S6) |
| Q5 EXPAND metric and entry year | PARTIALLY | Metric left as "margin framework" (cc L78, L86, L96). New information on timing: FY27 9-10% (cc L244), FY28 "double digits" (cc L266). | PARTIALLY stands; the "entry not before FY29" text is wrong (R5-F1) |
| Q10 30-Sep-2025 borrowings; WC funding source | PARTIALLY | The cited lines (cc L160, L179) are CFO prepared remarks. They restate the deck's cause, which is the claim Q10 tests. No balance, no funding source, no new fact. Q6, Q8 and Q12 carry the same pattern (figure or claim restated, requested detail absent) and are graded NOT ADDRESSED. | NOT ADDRESSED (R5-C1) |
| Q15 cancellations, FX, re-scoping | PARTIALLY | "600 crores plus" intake (cc L256) is new and fits the 6,078.90 Mn walk. Cancellations and the YoY tie remain open. | PARTIALLY stands |
| Q17 new-vertical order book | PARTIALLY | AI DC and robotics "just started exploring" (cc L215, L460); semicap revenue in the last two quarters, run rate asked (cc L235) and not given (cc L238-L239). | PARTIALLY stands |
| Q28 Altek rename date; earnout terms | PARTIALLY | The rename was already in the deck and press release (pres L192; pr L103-L104). The call restates it (cc L114, L437). The review's own cell says "no date, no earnout terms". Same pattern as Q12. | NOT ADDRESSED (R5-C1) |

EVADED rows Q3, Q14, Q16, Q18: each was asked and got no figure (cc L433-L439; L451-L455; L375-L394; L194-L208). The grades stand.
Corrected tally: ANSWERED 1, PARTIALLY 4, EVADED 4, NOT ADDRESSED 21, of 30.

---

## PRE-SET FORK CHECK (forks and open readings the call resolved)

| Pre-set fork or open reading | What the call says | Recorded? |
|---|---|---|
| Forward map "Now" row: component split and earnout residual vs evasion (rev L1315) | No component cost; earnout omitted when asked (cc L464-L465) | YES, outcome bear fork |
| Q19 bull "a reaffirmed figure" | H2 above 30% (cc L361); FY 30-35% accepted (cc L354) | YES (ANSWERED) |
| Q5 bear leg "undefined metric" | "margin framework", metric unnamed (cc L78, L86, L96) | YES (fact recorded) |
| Q17 bear "nil or immaterial" for AI DC and robotics | "just started exploring" (cc L215, L460) | YES |
| Role 4 Step 2C: p12 slice-to-label mapping unassigned, both mappings tested (rev L257) | CFO assigns the slices: aerospace 47%, industrial 31%, defence 7%, Med Tech 14% (cc L151-L152). This resolves to the upper end. | NO (R5-M3a) |
| Q4 and Q18 bull "one-off purchases"; Role 4 Step 8C bull text "one-off, as management says (pres L374)" (rev L520) | Chairman: product development "has been going on for a while, it's not ... only started this quarter" (cc L286); "it's not a one-off thing" (cc L291) | PARTLY: only as a within-call contradiction (rev L1027); not linked to the deck label or the bull forks (R5-M3b) |
| Q37 (new): pipeline rose to $1.5 bn vs fell | CEO "we are also seeing some of the things going up" (cc L330); chairman: both 1.4 and 1.5 unweighted, "1.5 which has increased" (cc L338-L339) | Recorded as "unresolved" with an unsupported "fall" reading (R5-F2) |

---

## ADVERSARIAL READ (three most management-favourable readings in the Role 5 section)

### P1. The S&M freeze is "the one hard, testable pledge on the call" (rev L946), confidence MEDIUM-HIGH (rev L820), "Hard operating-leverage pledge" (rev L977), one of "the testable positives" (rev L1465)
Strongest bear counter, from the same extract:
- The speaker cut his own pledge mid-sentence: "till we at least hit about, or at least net new, we won't add any more sales and marketing costs" (cc L288). The pledge covers net new additions. Wage and bonus growth on the "fully loaded" team (cc L289) falls outside it.
- No S&M base exists. The filing has no S&M line. Management refused the product development figure (cc L205, L208) and never sized S&M in rupees. The pledge is testable only if management discloses the base (Q33).
- The only filing proxy (P07, combined employee plus other-expense ratio) also carries product development. Management says that spend continues: "we will keep investing on a healthy basis" (cc L207); "we continue to invest in product development" (cc L286); "we will continually invest for the long term" (cc L386).
- The speaker is inferred (T039). Q2 other expenses rose 17.7% QoQ (382.41 to 450.02 Mn, res L546) beside the "fully loaded" claim.
- Horizon: quarterly revenue doubling from 3,931 Mn takes about 2.6 years at 30% a year [INFERENCE: ln 2 / ln 1.3].
Survives: YES. The review's quote at rev L943 drops "net new" behind an ellipsis. The brief (rev L1261) says "no new". "Hard, testable" and MEDIUM-HIGH overstate a pledge with no base. Graft required (R5-M1).

### P2. The H2 >30% pledge is tested by "Q3 revenue up 30% or more YoY" (forward map rev L1316, make-or-break rev L1311, monitorable 18 rev L620, tripwire (g) rev L1149, YAML rev L1416)
Strongest bear counter:
- Q3 FY26 is the weakest base of the six quarters: 303.3 Cr, a 2.36% QoQ dip (rev L272; pres L249).
- The 30% bar is 394.29 Cr, which is +0.3% QoQ on Q2's 393.09 Cr (res L538). A flat quarter passes the bull fork.
- A pass at the bar leaves Q4 needing 479.86 Cr to reach the 874.15 Cr H2 floor: +21.7% QoQ and +30.0% YoY on Q4 FY26's 369.1 Cr (pres L247).
- The CEO ties conversion to material availability (cc L248-L251, L356). So a lenient Q3 read can show "on track" while H2 fails.
Survives: YES. Tripwire (g) is lenient the same way: it fires only if Q3 revenue falls QoQ. Graft required (R5-M2).

### P3. Four B2S programmes "close to $1 billion" (rev L979: "New customer / contract win (unnamed)", material YES, Pillar 3 candidate; rev L1171 "undisclosed material positive"; brief rev L1298)
Strongest bear counter:
- The value is management's estimate from expected volumes: "we know what are the volumes are going to be ... that is why I said it is a billion dollar" (cc L313).
- Only some contracts are signed: "few ... are contract signed and few will be contract signed" (cc L427).
- The programmes sit outside the order book (cc L309), and only "a part" sits in the pipeline (cc L327-L328).
- No customer is named (cc L426-L429). Revenue starts FY29-FY30, and the call dates it four ways (cc L308, L317, L411, L428-L429).
- An analyst reported a press interview that called it an "order book" (cc L301-L302). The call says "not there currently in our order book" (cc L309).
Survives: NO, as a loop item. The review already carries partly signed, outside the book, partly outside the pipeline, the FY29-FY30 start, the unstable timing (rev L1028), the signed-status conflict (Q36) and "hold pending verification" (rev L1171). The residual qualifiers are logged as STYLE S9.

### Mandatory acquisition-economics probe (the call references the Altec integration and rename, cc L114, L437)
- The call adds no consideration figure. It says only "currently doing as per our plans" (cc L438), with no number when asked about US revenue and margin (cc L433-L436).
- The probe, recomputed from the filing: carrying value 730.94 + 447.97 = 1,178.91 Mn (res L137-L138 consolidated minus standalone) / subsidiary TTM op EBITDA 217.37 Mn (H2 FY26 148.43 + H1 FY27 68.94) = about 5.4x. On Q2 annualised (11.51 x 4 = 46.04 Mn) it is about 25.6x.
- Subsidiary TTM PAT ex-earnout is (18.17) Mn, so no positive earnings multiple exists.
- Earnout write-backs total 377.70 Mn = 32.0% of the carrying value. Net debt is 961.79 Mn = 4.4x TTM op EBITDA.
- Reading: the bear reading survives and is already grafted (Role 4 Step 5A, rev L380-L387; Role 5 Step 7A row 19, rev L1091). The call does not change it. No new graft.

---

## FINDINGS (tagged; all loop items name the agent)

### FACTUAL
- R5-F1 (A4). The review says the EXPAND ~11-13% band "cannot be entered before FY29". The extract does not support that. FY28 is guided at a floor: "double digits" (cc L266) and "10 plus percent ... without even doing any further additional effort" (cc L476-L477). "Around 200 basis points" (cc L294, base lost) on a 9-10% base would reach 11-12% [INFERENCE].
  - Correct reading: FY27 (9-10%) sits below the band. Band entry is unguided, with FY28 the earliest year. The DELAYED status holds, because FY27, the phase's first year, misses.
  - Lines: rev L537 (Q5 status), L829, L1127, L1222 (flag 4), L1450.
- R5-F2 (A4). The pipeline direction is mis-stated. "just over $1 bn" (rev L569, L1227) is not in the extract: the CEO said "more than a billion dollars" (cc L331), which restates the opening floor (cc L33). The "fall" reading omits "we are also seeing some of the things going up" (cc L330). The chairman then gives both figures on one unweighted basis, "1.5 which has increased" (cc L338-L339).
  - Correct reading: rose $1.4 bn to about $1.5 bn unweighted (CALL; T053 attribution low confidence). Q37 narrows to the date of the 1.4 figure and the weighted value.
  - Lines: rev L569, L812, L981, L1125, L1227 (flag 9), L1392, L1455.
- R5-F3 (A4). The CFO-vs-chairman "contradiction" on the margin cause is over-read. The CEO scopes the mix comment to the quarter: "whatever earlier I said is for this quarter ... revenue mix" (cc L279-L280). The chairman concedes "this quarter there was a bit of a revenue mix" and says "that was just mentioned as it was this quarter thing" (cc L283-L284). So the CFO's Q2 cause (cc L158) and the chairman's FY cause (S&M, cc L285) differ in weight, not in fact.
  - What stands: the chairman's claim that gross and contribution margin are higher YoY and YTD (cc L282-L283) against the filed -381 bps (Q2) and -307 bps (H1). That call-vs-filing finding is correct and stays.
  - Lines: rev L536, L698 (note a), L795 (d), L882, L937, L1022 ("speakers disagree"), L1138, L1224 (flag 6), L1452.
- R5-F4 (A4). Step 7A row 23 (rev L1095) marks "over all the challenges that we had last year" (cc L481) as CONTRADICTED by "the filing", citing inventory 177.8 days. That filing figure improved from 187.3 days at Mar-26 (rev L346). It does not contradict the claim.
  - The within-call contradiction stands: "continued supply chain shortages" (cc L39); "challenges in getting the materials" (cc L248); delays (cc L356).
  - Fix: re-tag row 23 as within the call. State the tally as 7 claims contradicting the filing or the deck, plus 1 contradicting the call itself. Or reword the headline to "the filing, the deck or the call itself".
  - Lines: rev L1095, L1097, L1208, L1264.

### CONTRADICTION
- R5-C1 (A4). Q10 (rev L542) and Q28 (rev L560) are graded PARTIALLY, but their own evidence cells show no new information: a restated deck claim, and a restated known rename with "no date, no earnout terms". The same pattern is graded NOT ADDRESSED at Q6 (rev L538), Q8 (rev L540) and Q12 (rev L544).
  - Regrade both to NOT ADDRESSED. Corrected tally: ANSWERED 1, PARTIALLY 4, EVADED 4, NOT ADDRESSED 21.
  - Lines: rev L542, L560, L578, L585 ("Send the 21 NOT ADDRESSED ..."), L888, L1189, L1263, L1461.
- R5-C2 (A4). The brief's "Management said vs filing shows" row (rev L1275) answers "Finance cost fell on 'lower working capital borrowings'" with "Gross borrowings up 24.3% in H1". That presents the H1 FY27 build as refuting a YoY cause.
  - Step 7A row 10 (rev L1082) and Role 4 loop 2 rule the opposite. The YoY cause is untestable, because the 30-Sep-2025 balance is NOT FOUND, and H1 FY26 repayments (992.96, 746.72 Mn) fit it (rev L326, L394, L1439; res L244-L245).
  - Fix: restate the row as "YoY cause untestable (30-Sep-2025 balance NOT FOUND); H1 FY26 repayments fit it; the H1 FY27 build (+24.3%) is a Q3 finance-cost risk (FILED)".
- R5-C3 (A4). The YAML `docs_merged: [results, presentation, concall]` (rev L1337) omits the press release. The press release is merged per rev L5, L21 and the 21-slide count.
  - Fix: [results, presentation, pressrelease, concall].

### MISSING
- R5-M1 (A4). The S&M freeze qualifier and its testability are missing (P1 graft).
  - Carry "net new" (cc L288) in the quotes at rev L820 and L943, and in the brief at rev L1261 ("no net new").
  - Replace "hard, testable" (rev L946, L977, L1055) with "testable only once the S&M base is disclosed (Q33); the filing proxy P07 also carries product development, which management says continues (cc L207, L286, L386)".
  - Set the Step 2 confidence (rev L820) to MEDIUM. Align tripwire (f) (rev L1149) with the pledge as given: no net new S&M.
  - Update the role5_analyst_note "testable positives" (rev L1465).
- R5-M2 (A4). The Q3 test of the H2 >30% pledge lacks the base-effect qualifier (P2 graft).
  - State at rev L1311, L1316, L620, L1149 (g) and L1416: "Q3 FY26 is the weakest base (303.3 Cr); the 394.29 Cr bar is +0.3% QoQ; a pass at the bar leaves Q4 needing 479.86 Cr (+21.7% QoQ)".
  - Test H2 as Q3 + Q4 >= 874.15 Cr (about 437 Cr a quarter), with the Q4 requirement restated after Q3.
- R5-M3 (A4). Two things the call resolved are not recorded.
  - (a) The CFO's mix (cc L151-L152) assigns the deck slices and collapses the Role 4 two-mapping range to the upper end. At point shares: Aerospace plus Industrial gave 981.0 Mn = 119.0% of the 824.56 Mn rise; Aerospace alone gave 707.1 Mn = 85.8%; the other 22% fell 15.3% (1,021.3 to 864.8 Mn). With +/-0.5 pp share rounding: 969-993 Mn (118-120%) and -14% to -17%.
  - Add this as a Role 5 addendum note, keeping the Role 4 numbers, at rev L775 (claim 49), L1090 (row 18), L1242, L1283 and L1303.
  - (b) The chairman says product development "has been going on for a while" (cc L286) and the hit is "not a one-off thing" (cc L291). That undercuts the deck's "one-off ... purchases towards product development" (pres L374-L375). The Role 4 Step 8C bull text ("as management says", rev L520) and the Q4 and Q18 bull answers rest on that label.
  - Add a Role 5 addendum cross-reference at rev L536 and L550, and a call-vs-deck line in Step 7A.
- R5-M4 (A2; ledger only). A fresh-pass unit is missing from the structured file and the ledger: cc L238 "In the last two quarters, we have the revenues on that" (T017, management, semicap revenue period). Minor: cc L485-L486 is a next-call disclosure commitment.
  - Fix: A2 adds a MISSING_FROM_STRUCTURED entry. A4 adds one line to the Role 5 preamble (rev L656, L660).
  - No A3 re-run is needed: A4 already cites cc L238 directly (CF18, Q17, Q40, P16).

---

## VERDICT

INCOMPLETE.
- Failing agent: A4, for the review text (R5-F1 to F4, R5-C1 to C3, R5-M1 to M3). Also A2, for a ledger annotation only (R5-M4).
- Finding types: FACTUAL 4, CONTRADICTION 3, MISSING 4.
- Exact gaps and line targets: listed under FINDINGS above.
- Verdict effect: none of the findings changes the protocol verdict (PROCEED WITH FLAGS), the cash classification (INDETERMINATE-WITH-DIRECTION) or the Role 5 net impact (WEAKENED). The fixes correct readings, grades, the tally, and two missing qualifiers.
- Role 4 tables: tie to the filing (sample above). OI-1: corrected.

---

## STYLE NOTES (logged; no loop)

- S1. 80.4% should read 80.5% (181.95 / 226.15 = 80.46%). A4 divided by the rounded 226.2. Lines: rev L571, L953, L1080, L1182, L1220, L1273, L1448.
- S2. The summary narrative now runs 25 bullet lines (rev L1241-L1265) plus a table. The spec is 10-20 lines. Merge the seven addendum bullets into three.
- S3. Rev L1104 calls +379 bps the "filed material ratio rise". The filed basis is +380.7 bps, equal to the gross margin fall. 379 bps is the deck-rounded basis (pres L376).
- S4. Rev L981 reads "additions ~$100 Mn". The source says "another x 100 million dollars" (cc L341), an illustration. Keep it verbatim, as rev L914 does.
- S5. Rev L1260 says costs "ease from Q3". The source says "from Q3 or Q4 onwards" (cc L295).
- S6. The Q4 status (rev L536) should cite the deflected quantification at cc L222-L228 (graded D, rev L903) beside L158 and L284. The PARTIALLY grade holds only because T039 gave a direction.
- S7. Rev L931 reads "The $1 bn pipeline / B2S, asked by 6 of 8". With B2S in the label, Q8 (T061, T063) also asked, which makes 7 of 8. Relabel the topic "order book / pipeline" to keep 6 of 8.
- S8. The forward map carries two Q1 FY28 rows (rev L1318, L1326) and two FY27-margin rows (rev L1317, L1322) with different thresholds. Add one line saying each row tests a different claim: the pledge vs the company band, and the guide vs the H1 run rate.
- S9. B2S: optionally add that the $1 bn rests on expected volumes (cc L313), and that a press "order book" label (cc L301-L302, analyst-reported) was walked back to "not there currently in our order book" (cc L309).
- S10. The YoY combined opex ratio fall is 245.75 bps. 245 is the sum of rounded parts. This is within rounding; no change is needed.

```yaml
stage: A5-adversary
company: "CYIENTDLM"
quarter: "q2fy27"
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
  missing_from_ledger:
    - "cc L238 'In the last two quarters, we have the revenues on that' (T017, management, semicap revenue period): no structured row, no ledger entry"
    - "cc L485-L486 next-call disclosure commitment (minor)"
arithmetic_mismatches: []
surviving_bear_counters:
  - {claim: "S&M freeze is the one hard, testable pledge; confidence MEDIUM-HIGH (rev L820, L946, L977)", counter: "Pledge self-qualified to 'at least net new' (cc L288); no S&M base disclosed or filed (Q33); filing proxy P07 carries product development, which continues (cc L207, L286, L386); speaker inferred (T039); Q2 other expenses +17.7% QoQ (res L546)", source_line: "cc L288, L207, L286, L386; res L546", type: MISSING}
  - {claim: "H2 >30% pledge tested by Q3 YoY >= 30% (rev L1311, L1316, L620, L1149 g, L1416)", counter: "Q3 FY26 is the weakest base (303.3 Cr, pres L249); the 394.29 Cr bar is +0.3% QoQ on 393.09; a pass at the bar leaves Q4 needing 479.86 Cr (+21.7% QoQ) for the 874.15 Cr H2 floor; conversion is material-limited (cc L248-L251, L356)", source_line: "res L538; pres L247-L249; cc L361", type: MISSING}
findings_by_type:
  factual:
    - "R5-F1 (A4): EXPAND band 'cannot be entered before FY29' unsupported; FY28 guided at a floor ('double digits' cc L266; '10 plus ... without even doing any further additional effort' cc L476-L477; '200 bps' cc L294); fix rev L537, L829, L1127, L1222, L1450"
    - "R5-F2 (A4): pipeline 'fall to just over $1 bn' not in extract; cc L330 'going up' omitted; chairman gives 1.4 to 1.5 on one unweighted basis (cc L338-L339); fix rev L569, L812, L981, L1125, L1227, L1392, L1455"
    - "R5-F3 (A4): CFO-vs-chairman margin-cause 'contradiction' over-read; CEO and chairman scope mix to Q2 (cc L279-L280, L283-L284); keep the call-vs-filing gross margin finding; fix rev L536, L698, L795, L882, L937, L1022, L1138, L1224, L1452"
    - "R5-F4 (A4): Step 7A row 23 filing leg unsupported (inventory days improved 187.3 to 177.8, rev L346); within-call leg stands (cc L39, L248, L356); fix rev L1095, L1097, L1208, L1264"
  missing:
    - "R5-M1 (A4): S&M freeze 'net new' qualifier dropped (rev L820, L943, L1261); 'hard, testable' and MEDIUM-HIGH overstate an unbased pledge (rev L946, L977, L1055, L1465); align tripwire f (rev L1149)"
    - "R5-M2 (A4): Q3 30% bull fork passes on a flat quarter; add Q4 requirement 479.86 Cr and an H2 Q3+Q4 >= 874.15 Cr test (rev L1311, L1316, L620, L1149 g, L1416)"
    - "R5-M3 (A4): (a) call mix cc L151-L152 resolves the Role 4 slice mapping: A+I 981.0 Mn = 119.0% of 824.56 Mn, Aerospace 85.8%, other 22% -15.3% (rounding band 118-120%, -14% to -17%); add Role 5 note at rev L775, L1090, L1242, L1283, L1303; (b) chairman 'not a one-off thing' (cc L291) and PD 'going on for a while' (cc L286) vs deck 'one-off' (pres L374-L375); cross-reference at rev L520, L536, L550 and Step 7A"
    - "R5-M4 (A2, ledger only): cc L238 unit missing from structured and ledger; add MISSING_FROM_STRUCTURED; A4 preamble note rev L656, L660; no A3 re-run"
  contradiction:
    - "R5-C1 (A4): Q10 (rev L542) and Q28 (rev L560) PARTIALLY on restated facts with no new information, while Q6, Q8, Q12 grade the same pattern NOT ADDRESSED; regrade; tally 1/4/4/21; fix rev L578, L585, L888, L1189, L1263, L1461"
    - "R5-C2 (A4): brief row rev L1275 presents the H1 FY27 debt build as refuting the YoY finance-cost cause; Step 7A row 10 (rev L1082) and Role 4 (rev L326, L394, L1439) rule it untestable with H1 FY26 repayments fitting it (res L244-L245)"
    - "R5-C3 (A4): YAML docs_merged (rev L1337) omits pressrelease vs rev L5, L21"
  style:
    - "S1: 80.4% should read 80.5% (181.95/226.15 = 80.46%); rev L571, L953, L1080, L1182, L1220, L1273, L1448"
    - "S2: summary narrative 25 lines vs 10-20 spec (rev L1241-L1265)"
    - "S3: rev L1104 '+379 bps filed' is the deck-rounded basis; filed is +380.7 bps"
    - "S4: rev L981 '~$100 Mn' additions; keep verbatim 'x 100 million' (cc L341)"
    - "S5: rev L1260 'from Q3' drops 'or Q4' (cc L295)"
    - "S6: Q4 status rev L536 should cite the deflected split at cc L222-L228"
    - "S7: rev L931 '6 of 8' with B2S in the label is 7 of 8 (Q8 T061, T063); relabel"
    - "S8: forward map duplicate-catalyst rows with different thresholds (rev L1317/L1322, L1318/L1326); add a cross-reference"
    - "S9: B2S $1 bn rests on expected volumes (cc L313); press 'order book' label (cc L301-L302) vs 'not in our order book' (cc L309)"
    - "S10: combined opex ratio fall 245.75 bps vs 245 (rounding; no change)"
loop_back_to: "A4"
gap: "A4: fix R5-F1 (EXPAND entry not before FY29: rev L537, L829, L1127, L1222, L1450), R5-F2 (pipeline direction: rev L569, L812, L981, L1125, L1227, L1392, L1455), R5-F3 (CFO vs chairman scope: rev L536, L698, L795, L882, L937, L1022, L1138, L1224, L1452), R5-F4 (row 23 and tally wording: rev L1095, L1097, L1208, L1264), R5-C1 (Q10 and Q28 to NOT ADDRESSED; tally 1/4/4/21 at rev L578, L585, L888, L1189, L1263, L1461), R5-C2 (rev L1275), R5-C3 (rev L1337), R5-M1 (net new and testability: rev L820, L943, L946, L977, L1055, L1149, L1261, L1465), R5-M2 (Q4 requirement 479.86 Cr: rev L1311, L1316, L620, L1149, L1416), R5-M3 (call mapping 981.0 Mn = 119%; one-off label: rev L520, L536, L550, L775, L1090, L1242, L1283, L1303). Also A2, ledger annotation only: R5-M4 (cc L238). Role 4 numbers stay unchanged; graft as (Role 5 addendum)."
style_notes:
  - "S1-S10 as listed under findings_by_type.style; logged, no re-run"
analyst_note: "Filing arithmetic in the Role 5 section ties, Role 4 tables tie on a 150-cell sample, and OI-1 is corrected. The faults are reading and grading, and they run both ways. Management-favourable: the S&M freeze is called hard and testable at MEDIUM-HIGH confidence, but the pledge was qualified to 'net new' (cc L288) and no S&M base exists; the Q3 30% bull fork passes on a flat quarter, because Q3 FY26 is the weakest base; Q10 and Q28 are PARTIALLY on restated facts that Q6, Q8 and Q12 grade NOT ADDRESSED. Bear-side over-reads: EXPAND entry 'not before FY29' against a 10% FY28 floor; a pipeline 'fall to just over $1 bn' against 'going up' (cc L330) and the chairman's 1.4 to 1.5 on one basis; a CFO-chairman conflict that cc L279 and L283 scope to Q2; a brief row that revives the finance-cost conflict Role 4 loop 2 dropped. The call also fixes the Role 4 slice mapping at the upper end (Aerospace plus Industrial 119% of the rise), which the review omits. None of this moves the verdict. The cc L238 ledger gap is hygiene; A4 already cites the line."
```

---
---

# LOOP 1 RE-AUDIT (Role 5 addendum, correction loop 1)

Agent: A5 adversary, fresh instance | Model: claude-opus-5-5 | Re-audit date: 2026-10-18
Run-1 record above is kept unchanged. This section supersedes the run-1 verdict and YAML.
Scope (task message, strict): (1) deliverable gate on the revised review; (2) closure of run-1 findings F1-F4, C1-C3, M1, M2, M3a, M3b, with every changed figure recomputed from the concall fulltext and the filing fulltexts (results Rs Mn; page 2 P&L authority res L533-L565); (3) new FACTUAL / MISSING / CONTRADICTION introduced by the edited passages, and no Role 4 number changed; (4) one fresh adversarial pass on three management-favourable Role 5 readings that run 1 did not test. No full arithmetic sweep. No coverage re-run. The A2 ledger note for cc L238 (R5-M4) is handled separately and is not re-flagged.
Inputs read: review_cyientdlm_q2fy27.md (now 1,469 lines); A4 edit file role5_parts/loop1_edits.md (E01-E76) and block a4-role5-loop1.yaml (finding map); concall fulltext (488 lines) and structured file (targeted greps); concall A2 ledger (targeted grep); results fulltext (res L128-L145, L280-L291, L530-L565); presentation fulltext (pres L240-L400); press release fulltext (targeted grep, pr L93-L95).
Not read: the source PDF, the audio, anything under inputs/, A3 reasoning.
Line shift: E38 added one row (Step 7A row 24, rev L1096). Run-1 line references from rev L1096 onward now sit one line lower. All "rev L###" below are current lines.

---

## 1. DELIVERABLE-COMPLETENESS AUDIT (gate)

| Part | Heading (rev line) | Status |
|---|---|---|
| 1. Summary narrative | "### 1. Summary narrative" (rev L1241-L1266), plus the call-vs-filing table (rev L1268-L1278) | PRESENT (25 bullet lines; spec 10-20; run-1 S2 still open, STYLE) |
| 2. Sector intelligence | rev L1280-L1289 | PRESENT |
| 3. Business-model intelligence | rev L1291-L1301 | PRESENT |
| 4. Competition intelligence | rev L1303-L1309 | PRESENT |
| 5. Forward map | rev L1311-L1327; 12 dated rows, each with a bull and a bear fork | PRESENT |

Gate: PASS.

---

## 2. RUN-1 FINDING CLOSURE

| Run-1 finding | Edits (A4 map) | Re-check against the extract (rev line; source line) | Status |
|---|---|---|---|
| R5-F1 EXPAND entry "not before FY29" | E03, E19, E42, E52, E72, E76 | Q5 (rev L537), Step 2 (rev L829), 8A (rev L1128), flag 4 (rev L1223), YAML (rev L1451), note (rev L1466) now read: FY27 9-10% misses the band; FY28 guided at a floor; entry unguided, FY28 earliest. Ties to cc L244, L266, L476-L477, L294. Only remaining "not before FY29" is the correction note itself (rev L537) | CLOSED |
| R5-F2 pipeline direction | E07, E15, E16, E33, E41, E54, E69, E74, E76 | Q37 (rev L569), Step 2 (rev L812), 5A (rev L981), 8A (rev L1126), flag 9 (rev L1228), YAML (rev L1393, L1456): "rose $1.4 bn to ~$1.5 bn unweighted (low confidence)". Ties to cc L330, L331, L338-L339. Residue: 8F row 7 (rev L1186) still asks for the pipeline "at 30-Jun and 30-Sep on one basis ... One basis, two dates", against the revised Q37 | CLOSED except one residue (L1-C2) |
| R5-F3 CFO vs chairman scope | E02, E12, E14, E22, E26, E28, E34, E44, E50, E53, E61, E73, E76 | rev L536, L698, L795 (d withdrawn), L882, L937, L944, L1022, L1139, L1220, L1225, L1271, L1453 now scope the mix to Q2. Ties to cc L279-L280, L283-L284. The call-vs-filing gross margin finding stays (rev L1076, L1271: 37.41% vs 41.22% Q2; 37.67% vs 40.74% H1) | CLOSED |
| R5-F4 Step 7A row 23 | E38, E39, E49, E60 | Row 23 (rev L1095) is within the call only; inventory days 187.3 to 177.8 (rev L346). Tally (rev L1098) recounted row by row: CONFIRMED 10 (rows 1, 2, 9, 11, 14, 16, 17, 20, 21, 22), PARTIALLY 3 (5, 6, 13), CONTRADICTED by filing or deck 8 (3, 4, 7, 8, 12, 18, 19, 24), within the call 1 (23), UNVERIFIABLE 2 (10, 15) = 24 | CLOSED (row 24 reading: see L1-C1) |
| R5-C1 Q10 and Q28 regrade | E04, E06, E09, E10, E23, E47, E59, E75 | Q10 (rev L542) and Q28 (rev L560) NOT ADDRESSED. Status column recounted Q1-Q30: ANSWERED 1 (Q19), PARTIALLY 4 (Q4, Q5, Q15, Q17), EVADED 4 (Q3, Q14, Q16, Q18), NOT ADDRESSED 21 = 30. Matches rev L578, L585, L888, L1190, L1264, L1462 | CLOSED |
| R5-C2 brief finance-cost row | E63 | rev L1276 now matches Step 7A row 10 (rev L1082) and Role 4 (rev L1440) | CLOSED |
| R5-C3 docs_merged | E68 | rev L1338: [results, presentation, pressrelease, concall] | CLOSED |
| R5-M1 S&M "net new" and testability | E17, E18, E20, E24, E27, E28, E29, E31, E35, E43, E45, E48, E58, E67, E76 | Quotes at rev L820 and L943 match cc L288 verbatim; confidence MEDIUM (rev L820); "hard, testable" gone (grep); rev L946, L977, L1055, L1133, L1150 (f), L1200, L1262, L1466 carry net new and the missing base (Q33). Product development continues: cc L207, L286, L386 verified | CLOSED |
| R5-M2 Q3 base-effect qualifier | E11, E21, E45, E66, E67, E70, E76 | Qualifier and the 479.86 Cr Q4 need are at rev L620, L856, L1150 (g), L1312, L1317, L1417. The new forward-map forks (E67, rev L1317) over-correct: they class a Q3 at the 30% bar as bear | CLOSED; fork edit over-corrects (L1-M1) |
| R5-M3a call mix mapping | E13, E37, E55, E64, E65 | Notes at rev L775, L1090, L1243, L1284, L1304; figures recomputed in section 3 | CLOSED (STYLE LS3 on rev L1243) |
| R5-M3b one-off label | E01, E02, E05, E38, E39, E56 | PD-purchase leg: grafted at rev L536, L550, L1096. But rev L520, L1096 and L1247 also apply the chairman's "not a one-off thing" to the mix effect, which the review itself records he called a "this quarter thing" (rev L698, L795, L1271; cc L283-L284). Part of this traces to run-1's own M3b wording, which named the Step 8C mix bull | CLOSED on the PD leg; mix-leg over-read (L1-C1) |

Run-1 STYLE notes: S1 CLOSED (80.5% at rev L571, L953, L1080, L1183, L1221, L1274, L1449; no "80.4%" left). S2 OPEN (not applied; A4 cites CRLF anchoring). S3, S4, S5, S6, S8, S9 CLOSED. S7 applied, label still mixed (LS4). S10 no change needed.

---

## 3. CHANGED-FIGURE RECOMPUTATION (only figures loop 1 introduced or changed)

| Metric | A4 value (rev line) | Recomputed | Source line | Status |
|---|---|---|---|---|
| Aerospace Q2 FY27 increment, share of rise | 707.1 Mn, 85.8% (L775); "about 86%" (L1304) | 0.47 x 3,930.90 = 1,847.52; prior 1,847.52 / 1.62 = 1,140.45; +707.08; / 824.56 = 85.75% | cc L151; res L538 | OK |
| Aerospace plus Industrial increment | 981.0 Mn, 119.0% (L775, L1243, L1284) | Industrial 0.31 x 3,930.90 = 1,218.58; prior / 1.29 = 944.64; +273.94; A+I +981.02; / 824.56 = 118.97% | cc L151; res L538 | OK |
| Other 22% | 1,021.3 to 864.8 Mn, -15.3% (L775, L1090) | 3,106.34 - 1,140.45 - 944.64 = 1,021.26; 0.22 x 3,930.90 = 864.80; -15.32% | cc L151-L152; res L538 | OK |
| Share-rounding band | 969-993 Mn (118-120%); -14% to -17% (L775, L1090) | shares 46.5/30.5 to 47.5/31.5: 969.08-992.96 Mn = 117.5%-120.4%; other 22%: -13.8% to -16.9% | cc L151-L152; res L538 | OK (rounding) |
| H2 FY27 floor | 874.15 Cr; about 437 Cr a quarter (L620, L856, L1312, L1317) | H2 FY26 = 12,614.85 - 5,890.61 = 6,724.24 Mn; x 1.3 = 8,741.51 Mn = 874.15 Cr; / 2 = 437.08 | res L538 | OK |
| Q3 bar and QoQ | 394.29 Cr; +0.3% QoQ (L620, L856, L1150, L1312) | 3,033 x 1.3 = 3,942.9 Mn; / 3,930.90 = +0.31% | pres L249; res L538 | OK |
| Q4 need at the bar | 479.86 Cr; +21.7% QoQ; +30.0% YoY (L620) | 874.15 - 394.29 = 479.86; / 394.29 = +21.70%; / 369.1 = +30.01% | pres L247-L249 | OK (the fork reading: L1-M1) |
| Earnout share of Q2 other income | 80.5% (seven lines) | 181.95 / 226.15 = 80.46% | res L288, L539 | OK |
| Filed material ratio rise | +380.7 bps; deck 379 bps (L1105) | (2,558.66 - 98.35) / 3,930.90 = 62.589%; (1,961.22 - 135.24) / 3,106.34 = 58.782%; +380.7; deck 2,460/3,931 vs 1,826/3,106 = +379 | res L538, L541, L542; pres L375-L376 | OK |
| H1 gross margin, brief table | 37.67% vs 40.74% (L1271) | 1 - (4,727.40 + 52.56)/7,668.90 = 37.67%; 1 - (3,578.11 - 87.31)/5,890.61 = 40.74% | res L538, L541, L542 | OK |
| EXPAND reach on "200 bps" | 11-12% (L829) | 9% + 2 = 11%; 10% + 2 = 12% [INFERENCE] | cc L294, L244 | OK |
| Inventory days, row 23 | 187.3 to 177.8 (L1095) | as Step 5A (rev L346) | rev L346 | OK |
| Answer-status tally | 1 / 4 / 4 / 21 (L578 and five more) | row-by-row recount, Q1-Q30 | rev L533-L562 | OK |
| Step 7A tally | 10 / 3 / 8 / 1 / 2 = 24 (L1098) | row-by-row recount, rows 1-24 | rev L1073-L1096 | OK (row 24 tag: L1-C1) |
| Analysts on the topic | 7 of 8 (L931) | seven slots listed: Q2, Q3, Q5, Q6, Q8, Q9, Q10 | rev L902-L925 | OK (label: LS4) |

No arithmetic mismatch above rounding.

---

## 4. ROLE 4 INTEGRITY

- Edit list: all 76 FIND strings are single lines. Inside Role 4 they touch only the Role 5 ANSWER STATUS column (Q4, Q5, Q10, Q18, Q28), Role 5 rows (Q37, Q39, monitorable 18), Role 5 coverage text (rev L578, L585) and an appended note on the Step 8C bull line (rev L520). No Role 4 table cell number is in a FIND string.
- Spot tie-out after the edits: Table 1A revenue, other income, materials, PBT, total tax, current tax, deferred tax and PAT, six periods each (48 cells, rev L106-L120), against res L538-L552: all tie. Step 2C (rev L257) still reads 881.7-981.0 Mn, 107-119%, 6-15%, 57-86%. Step 8C thresholds (rev L520-L522) recomputed: H2 FY26 gross margin 1 - 4,031.31/6,724.24 = 40.05%; Q1 FY27 combined ratio 1,026.72/3,738.00 = 27.47%; Q2 FY27 1,128.89/3,930.90 = 28.72%.
- One brief edit (E55, rev L1243) replaced the Role 4 range "6-15%" in the summary bullet with the call figure "about 15%". The bullet is marked "(Role 5 addendum, loop 1)", and the Role 4 range survives at rev L257, L1284 and L1437. No fact is wrong. Logged as STYLE LS3.
Result: PASS. No Role 4 table number changed.

---

## 5. NEW-ISSUE CHECK ON THE EDITED PASSAGES

### L1-C1 (CONTRADICTION; A4). The chairman's "not a one-off thing" is applied to the mix effect, which he called a "this quarter thing"
- What the call says, in order (T039, speaker inferred): "this quarter there was a bit of a revenue mix" (cc L283); "it's not the revenue mix, revenue mix is always going to be there, I think that was just mentioned as it was this quarter thing" (cc L284); the margin is lower from sales and marketing and product development, "not capitalized", and product development "has been going on for a while, it's not that it is something that we only started this quarter" (cc L285-L286); the drop is the S&M cost base, "fully loaded" with "zero absorption" (cc L287-L290); then "So I just want to clarify that it's not a one-off thing, it's not a con, yes there is, there was a..." (cc L291), which breaks into the audio gap (cc L292-L294) and resumes "It is just the fact that we are investing in sales and marketing and we are investing in product development" (cc L293).
- What follows: "it's not a one-off thing" refers to the S&M and product-development investment drag on EBITDA margin. In the same answer the chairman denies any gross-margin fall (cc L282-L284), so he does not address the deck's one-off, which is the Q2 direct-material-cost variance: "DMC % is variance in Q2FY27 due to one-off Revenue mix impact and purchases towards product development" (pres L374-L375). On the mix leg he supports the deck: mix was this quarter's effect. On the product-development-purchase leg, "going on for a while" (cc L286) makes repeat purchases likely [INFERENCE]. That undercuts the deck. It does not contradict it on the DMC measure. The quoted sentence also drops its trailing fragment ("yes there is, there was a..."), which may be a concession lost in the gap. Run 1 held the "net new" ellipsis to this bar; the same bar applies here.
- Where the review contradicts itself:
  - rev L520 (Step 8C, E01): "'As management says' now rests on the deck and the CEO's 'some of these one-offs' (cc L231), against the chairman." The 8C bull is "the Q2 mix effect was one-off". On mix, the chairman agrees with the deck. This conflicts with rev L698, L795, L944, L1220 and L1271, which record that he scoped the mix to Q2.
  - rev L1096 (Step 7A row 24, E38): "CONTRADICTED (call vs deck ... it removes management support from the Role 4 Step 8C, Q4 and Q18 'one-off' bull readings)". The CEO's "some of these one-offs" (cc L231) and the chairman's "this quarter thing" (cc L284) both still support a one-off reading. "Removes" is not supported.
  - rev L1247 (brief, E56): "Management calls the material jump a one-off ... On the call the chairman said it is 'not a one-off thing'." Here "it" is the material jump. The chairman never said that; he said gross margin was higher (cc L282-L283).
  - rev L1466 (role5_analyst_note, E76): "calls the cost 'not a one-off', against the deck's one-off label". The cost he calls not one-off is the investment drag, not the deck's DMC item.
  - Lighter: rev L536 (Q4, E02) and rev L550 (Q18, E05) read the PD undercut correctly in direction, but carry no [INFERENCE] tag and also cite cc L291 for it.
- Fix (minimum; keeps the Step 7A count at 8, consistent with rows 18 and 19, which already count as CONTRADICTED [INFERENCE]): retag row 24 "CONTRADICTED [INFERENCE] (call vs deck; product-development-purchase leg only)". State that the mix leg has the chairman's support (cc L283-L284). State that cc L291 refers to the investment drag and breaks into the audio gap. Correct rev L520, L1247 and L1466 the same way. Add [INFERENCE] at rev L536 and L550.

### L1-M1 (MISSING; A4). The new Q3 forks class a Q3 at the 30% bar as bear. The Q4 step it leaves is the one Q4 FY26 made
- rev L1317 (E67): bull "Q3 revenue at or above about 437 Cr, on pace for the 874.15 Cr H2 floor"; bear "Q3 near the 394.29 Cr bar or below, leaving Q4 above 479.86 Cr (+21.7% QoQ)".
- From the extract: at the bar, both H2 quarters grow 30.0% YoY (394.29 on 303.3; 479.86 on 369.1; pres L247-L249). That is the pledged rate (cc L361). The +21.7% QoQ Q4 step equals the step Q4 FY26 made (3,691 on 3,033 = +21.69%; rev L273). Q3 FY26 was 45.1% of H2 FY26 (3,033 / 6,724.24). On that shape, the 874.15 Cr floor splits 394.3 / 479.9 Cr [INFERENCE, one year of data].
- So "about 437 a quarter" is one reading (even split). The FY26 shape is the other. The separating observation is whether Q3 FY26's -2.36% QoQ dip was seasonal (Q3 FY25 not in the run). A Q3 between 394.29 and 437 Cr does not decide H2; Q4 does. The bull fork now needs Q3 +44.1% YoY (437.08 / 303.3). The bear fork includes a quarter that meets the pledge. That holds the bull claim to a harder bar than the bear claim.
- rev L1312, L856 (P09) and L1150 (g) give the Q4 need as "+21.7% QoQ" with no "+30.0% YoY" and no FY26 comparator. rev L620 gives "+30.0% YoY" but not the FY26 step. The YAML at rev L1417 gives neither.
- Fix: at rev L1317, keep bull at Q3 >= about 437 Cr (Q4 then needs no QoQ growth). Add a neutral band, Q3 394.29-437 Cr: H2 rests on Q4 at up to +21.7% QoQ, the step Q4 FY26 made; at the bar both quarters grow at the pledged 30% YoY. Set bear at Q3 below 394.29 Cr, where Q4 must beat the FY26 Q4 step. Name the two readings and the separating observation. At rev L1312, L856, L1150, L620 and L1417, add "(+30.0% YoY; the same QoQ step Q4 FY26 made, rev L273)" after the 479.86 Cr figure.

### L1-C2 (CONTRADICTION; A4). The 8F table still asks for the pipeline basis that the chairman gave
- rev L1186 (8F row 7): "Q37: pipeline at 30-Jun and 30-Sep on one basis | Feeder metric | One basis, two dates". The revised Q37 (rev L569, L1393) records that both figures are unweighted (cc L338-L339) and asks for the date of the 1.4 figure and the weighted value. This row was not in run-1's F2 line list.
- Fix: "Q37: date of the $1.4 bn unweighted figure; weighted value of the ~$1.5 bn | Feeder metric | A dated 1.4 and a weighted value".

No other edited passage adds a FACTUAL, MISSING or CONTRADICTION finding. E01-E76 were each checked against their cited lines.

---

## 6. ADVERSARIAL READ (fresh; three management-favourable Role 5 readings run 1 did not test)

Run 1 tested the S&M freeze, the Q3 30% test of the H2 pledge, the $1 bn B2S programmes and the acquisition probe. The review's own "Positives to test" (rev L1466) names H2 revenue, 600 Cr intake and full product-development expensing. The three untested readings are the intake guide, the P07 intensity test, and full expensing as a positive.

### A1. Order intake "600 crores plus" in Q3 and Q4 is carried as a dated pledge and a positive (rev L812, L857 P10, L983 "Forward catalyst pre-announced", L1054 "Specific dated pledges", L1126 and L1140 "pledged", L1161, L1466 "Positives to test")
Strongest bear counter, from the same extract:
- The statement is hedged: "and this quarter is close to 600 crores plus, that's where probably you will be expecting it for the next two quarters too" (cc L256). The review's Step 2 quote (rev L812) drops "probably" behind an ellipsis. Step 6C (rev L1049) counts cc L256 among the hedges, while Step 6D (rev L1054) lists it as a specific dated pledge.
- It came as the first reply to a win-ratio question, and the analyst rejected it: "No, sir. I asked about something else" (cc L257). The review grades this first reply C (rev L908).
- Base rate from the book walk (closing book - opening book + revenue; pres L247-L249, L289-L294; res L538): Q2 FY26 469.9, Q3 FY26 361.6, Q4 FY26 436.3, Q1 FY27 556.1, Q2 FY27 607.9 Cr. Intake reached 600 Cr in one quarter out of five. H2 FY26 intake was 797.9 Cr, so the guide needs H2 FY27 intake about 50% higher [INFERENCE: 1,200 / 797.9].
- The "last quarter" leg ties only loosely: the Q1 FY27 walk is 556.1 Cr (1.49x), below "600 crores plus".
Survives: YES. The hedge and the base rate are absent wherever the review calls this a pledge or a positive. Graft required (L1-M2). The order-book GREEN (rev L1140) rests on the book level and stays.

### A2. P07 "investment intensity lower from Q3 or Q4" is tested by the combined employee plus other-expense ratio below Q2's 28.72% (rev L854, L622, L1419)
Strongest bear counter:
- The call states an absolute claim next to the intensity claim: "Whatever has been done, sales and the marketing cost, that is already done now. There will not be any future investment in that area" (cc L296-L297). The ratio cannot test that. P06 (absolute S&M) cannot be tested until the base is disclosed (Q33). So P07 is the only live filing test.
- At the H2 pace of about 437 Cr a quarter, the ratio stays below 28.72% with combined expenses up to about 1,255 Mn, +11.2% on Q2's 1,128.89 Mn [INFERENCE: 0.28718 x 4,370.8; res L543, L546]. A ratio pass can therefore score DELIVERED in a quarter where the expense lines grow 11%.
- That pass comes from the same revenue growth P09 scores. Two promise-log rows would then credit one improvement.
- Q1 FY27 already printed 27.47% (rev L522), so a return to the Q1 level passes with no change in spend.
Survives: YES. Graft required (L1-M3): add the absolute co-reading.

### A3. Full expensing of product development as a positive, confidence HIGH (rev L821, L987, L1466)
Strongest bear counter:
- The policy is stated as "today": "as a policy, today we are not capitalizing any of the costs" (cc L199). The option to capitalise is kept (cc L389-L391). Management refused to size product development (cc L205, L208), so the positive cannot be sized.
- The filing supports the claim. Neither balance sheet has an intangible-assets-under-development line (res L133-L145). Standalone other intangible assets fell from 22.17 to 18.57 Mn (res L138). Nothing filed shows capitalised development.
Survives: NO, as a loop item. The option is already tripwire (h) (rev L1150) and Q41 (rev L573), and the refused amount is Q18 (EVADED). The missing "today" is logged as STYLE LS5.

Acquisition-economics probe: the run-1 result stands. Loop 1 did not touch rev L380-L387, L1091 or L1434. It was not re-run (outside this loop's scope).

---

## 7. FINDINGS (loop 1, tagged)

### CONTRADICTION
- L1-C1 (A4): rev L520, L1096 (row 24), L1247 and L1466 apply the chairman's "not a one-off thing" (cc L291) to the mix effect and the deck's DMC item. The review's own rev L698, L795, L944, L1220 and L1271 record that he called mix a "this quarter thing" (cc L283-L284). His words undercut only the product-development-purchase leg, by inference (cc L286). The quote also drops "yes there is, there was a..." (cc L291), which runs into the audio gap. Lighter alignment at rev L536 and L550 ([INFERENCE] tag).
- L1-C2 (A4): rev L1186 (8F row 7) asks for the pipeline "on one basis". This conflicts with the revised Q37 (rev L569, L1393; cc L338-L339).

### MISSING
- L1-M1 (A4): the forward-map forks at rev L1317 class a Q3 at the 30% bar as bear. Missing: at the bar both H2 quarters grow 30.0% YoY, and the +21.7% Q4 step equals Q4 FY26's step (rev L273). Also missing: the even-split versus FY26-shape readings. Align at rev L1312, L856, L1150, L620 and L1417.
- L1-M2 (A4): the 600 Cr intake guide is carried as a pledge without its "probably" (cc L256) and without the walk base rate (one quarter in five reached 600 Cr). Lines: rev L812, L857, L983, L1054, L1126, L1140, L1466.
- L1-M3 (A4): the P07 ratio test passes with expenses up to about 11% QoQ at the H2 revenue pace. It re-credits P09 and cannot test "no future investment" (cc L297). Lines: rev L854, L622, L1419.

### FACTUAL
- None new.

### STYLE (logged; no loop)
- LS1: "Q3 FY26 is the weakest base" (rev L620, L856, L1150, L1312, L1317, L1417). In level, Q1 FY26 (278.43 Cr, rev L270) is lower. Say "the only QoQ decline of the six quarters (-2.36%) and the weaker of the two H2 bases". The run-1 audit text "weakest base of the six quarters" has the same slip.
- LS2: rev L820 "wage and bonus growth ... sits outside it" and rev L853 "wage growth on the existing team sits outside the pledge as given" are readings of "net new". Tag them [INFERENCE] and drop "bonus", which is not in the extract.
- LS3: rev L1243 (E55) replaced the Role 4 brief range "6-15%" in place. Keep "(deck alone: 6-15%)" beside the call figure, as rev L1284 does.
- LS4: rev L931 label "The $1 bn pipeline / B2S" includes Q2 T016 and Q10 T087, which asked about the order book. Relabel it "order book, pipeline and B2S" to keep 7 of 8. On the narrow label the count is 5 of 8.
- LS5: rev L821 should carry "as a policy, today" (cc L199).
- LS6: the review YAML (rev L1337) records loop_iteration: 2 (the Role 4 loop) and has no Role 5 loop marker. The Role 5 header (rev L649) has no loop-1 line like rev L8-L9. Add both for traceability.
- S2 (run 1): still open. The summary narrative runs 25 lines against the 10-20 spec.

---

## 8. VERDICT (loop 1)

INCOMPLETE.
- Failing agent: A4.
- Finding types: CONTRADICTION 2 (L1-C1, L1-C2), MISSING 3 (L1-M1, L1-M2, L1-M3), FACTUAL 0. STYLE 6 new plus S2.
- Run-1 closure: 8 of 11 closed clean. F2 is closed except one residue (L1-C2). M2 is closed, but the fork edit over-corrects (L1-M1). M3b is closed on the PD leg, with a mix-leg over-read (L1-C1).
- Direction of the open findings: L1-C1 and L1-M1 are bear-side over-reads. L1-M2 and L1-M3 are bull-side leniencies. L1-C2 is a stale cell.
- Verdict effect: none. The protocol verdict PROCEED WITH FLAGS, cash INDETERMINATE-WITH-DIRECTION and the Role 5 impact WEAKENED do not move. The Step 7A count stays 8 of 24 under the minimum L1-C1 fix. All fixes are single-line text edits. No Role 4 number changes.
- Exact gap: see the YAML gap field below.

```yaml
stage: A5-adversary
company: "CYIENTDLM"
quarter: "q2fy27"
model: "claude-opus-5-5"
status: complete
loop_iteration: 1
verdict: INCOMPLETE
plain_language_brief:
  narrative: present
  sector: present
  business_model: present
  competition: present
  forward_map: present
coverage:
  orphan_rows: []          # coverage not re-run in loop 1 (scope); no ledger row removed by the edits
  missing_from_ledger: []  # cc L238 (R5-M4) handled separately per task; not re-flagged
arithmetic_mismatches: []  # every loop-1 figure recomputes within rounding (audit section 3)
run1_closure:
  R5-F1: CLOSED
  R5-F2: "CLOSED except residue rev L1186 (L1-C2)"
  R5-F3: CLOSED
  R5-F4: CLOSED
  R5-C1: CLOSED
  R5-C2: CLOSED
  R5-C3: CLOSED
  R5-M1: CLOSED
  R5-M2: "CLOSED; fork edit over-corrects (L1-M1)"
  R5-M3a: CLOSED
  R5-M3b: "CLOSED on the PD-purchase leg; mix-leg over-read (L1-C1)"
role4_numbers_changed: false
surviving_bear_counters:
  - {claim: "Order intake '600 crores plus' in Q3 and Q4 is a dated pledge and a positive to test (rev L812, L857, L983, L1054, L1126, L1140, L1466)", counter: "Hedged 'that's where probably you will be expecting it' (cc L256), dropped behind an ellipsis at rev L812 while 6C counts it as a hedge; first reply to a win-ratio question the analyst rejected (cc L257); book-walk intake Q2 FY26 469.9, Q3 FY26 361.6, Q4 FY26 436.3, Q1 FY27 556.1, Q2 FY27 607.9 Cr: 600 Cr reached once in five quarters; guide needs H2 intake about 50% above H2 FY26 797.9 Cr [INFERENCE]; Q1 walk 556.1 Cr ties loosely to 'last quarter ... close to 600 crores plus'", source_line: "cc L256-L257; pres L247-L249, L289-L294; res L538", type: MISSING}
  - {claim: "P07 'investment intensity lower' is tested by the combined employee plus other-expense ratio below Q2's 28.72% (rev L854, L622, L1419)", counter: "Call adds an absolute claim, 'There will not be any future investment in that area' (cc L296-L297), that a ratio cannot test; P06 is untestable until Q33; at about 437 Cr a quarter the ratio stays under 28.72% with combined expenses up to about 1,255 Mn, +11.2% on Q2's 1,128.89 Mn [INFERENCE], so a ratio pass re-credits the P09 revenue growth; Q1 FY27 already printed 27.47%", source_line: "cc L295-L297; res L538, L543, L546", type: MISSING}
findings_by_type:
  factual: []
  missing:
    - "L1-M1 (A4): forward-map forks rev L1317 class a Q3 at the 30% bar (394.29 Cr) as bear, but at the bar both H2 quarters grow 30.0% YoY and the +21.7% QoQ Q4 step equals Q4 FY26's step (3,691 on 3,033, rev L273; pres L247-L249); even split (437 Cr) vs FY26 shape (Q3 45.1% of H2 = 394.3 Cr) not named; align rev L1312, L856, L1150, L620, L1417"
    - "L1-M2 (A4): 600 Cr intake guide lacks its hedge 'probably' (cc L256) and the walk base rate (one of five quarters at 600 Cr; H2 FY26 797.9 Cr); rev L812, L857, L983, L1054, L1126, L1140, L1466"
    - "L1-M3 (A4): P07 ratio test lacks an absolute co-reading (combined employee plus other expenses vs Q2 FY27 1,128.89 Mn, res L543, L546); ratio passes with expenses up about 11% QoQ at the H2 pace, re-crediting P09, and cannot test cc L297; rev L854, L622, L1419"
  contradiction:
    - "L1-C1 (A4): rev L520, L1096 (row 24), L1247, L1466 apply the chairman's 'not a one-off thing' (cc L291) to the mix effect and the deck's DMC one-off (pres L374-L375), while rev L698, L795, L944, L1220, L1271 record that he called mix a 'this quarter thing' (cc L283-L284); his words undercut only the PD-purchase leg [INFERENCE] (cc L286); the cc L291 quote drops 'yes there is, there was a...' into the audio gap (cc L292-L294); align rev L536, L550 with an [INFERENCE] tag"
    - "L1-C2 (A4): rev L1186 (8F row 7) asks for the pipeline 'at 30-Jun and 30-Sep on one basis', against the revised Q37 (rev L569, L1393) and cc L338-L339 (both unweighted)"
  style:
    - "LS1: 'weakest base' (rev L620, L856, L1150, L1312, L1317, L1417): Q1 FY26 278.43 Cr is lower in level (rev L270); say 'only QoQ decline of the six quarters (-2.36%), weaker of the two H2 bases'"
    - "LS2: rev L820 'wage and bonus growth', rev L853 'wage growth' outside the pledge are readings of 'net new'; tag [INFERENCE]; 'bonus' not in the extract"
    - "LS3: rev L1243 (E55) replaced the Role 4 brief range 6-15% in place; keep '(deck alone: 6-15%)' beside the call figure"
    - "LS4: rev L931 label '$1 bn pipeline / B2S' includes order-book questions Q2 T016 and Q10 T087; relabel 'order book, pipeline and B2S' for 7 of 8"
    - "LS5: rev L821 should carry 'as a policy, today' (cc L199)"
    - "LS6: review YAML rev L1337 has no Role 5 loop marker and the Role 5 header rev L649 has no loop-1 line; add for traceability"
    - "S2 (run 1, open): summary narrative 25 lines vs 10-20 spec (rev L1242-L1266)"
loop_back_to: "A4"
gap: "A4 loop 2, single-line edits marked '(Role 5 addendum, loop 2)', Role 4 numbers unchanged. (1) L1-C1: rev L1096 row 24: say 'it's not a one-off thing' (cc L291) refers to the S&M and PD investment drag (cc L285-L293) and breaks into the audio gap ('yes there is, there was a...', cc L291-L294); retag 'CONTRADICTED [INFERENCE] (call vs deck; PD-purchase leg only: PD going on for a while, cc L286)'; replace 'removes management support from the Role 4 Step 8C, Q4 and Q18 one-off bull readings' with 'the mix leg has the chairman's support (this quarter thing, cc L283-L284); the PD-purchase leg of the Q4 and Q18 bull answers is weakened'. Count stays 8 of 24. rev L520: replace 'against the chairman' with 'on mix the chairman agrees (cc L283-L284); on PD purchases he undercuts the deck (cc L286) [INFERENCE]'. rev L1247: replace 'the chairman said it is not a one-off thing' with 'the chairman called the mix a this quarter thing and said product development has been going on for a while (CALL), so repeat PD purchases are likely (INFERENCE)'. rev L1466: same correction to 'calls the cost not a one-off, against the deck's one-off label'. rev L536, L550: add [INFERENCE] to the PD undercut and cite cc L286, not cc L291. (2) L1-M1: rev L1317 forks: bull Q3 >= about 437 Cr (Q4 then needs no QoQ growth); neutral Q3 394.29-437 Cr (H2 rests on Q4 at up to +21.7% QoQ, the step Q4 FY26 made, rev L273; at the bar both quarters grow the pledged 30% YoY); bear Q3 below 394.29 Cr (Q4 must beat the FY26 Q4 step); name the two readings (even split 437 vs FY26 shape 394.3, Q3 45.1% of H2) [INFERENCE, one year]. At rev L1312, L856, L1150, L620, L1417 add '(+30.0% YoY; the same QoQ step Q4 FY26 made, rev L273)' after 479.86 Cr. (3) L1-C2: rev L1186: 'Q37: date of the $1.4 bn unweighted figure; weighted value of the ~$1.5 bn | Feeder metric | A dated 1.4 and a weighted value'. (4) L1-M2: rev L812 restore 'that's where probably you will be expecting it for the next two quarters too' (cc L256); rev L983, L1054, L1126, L1140: tag the intake guide 'hedged: probably (cc L256)', not 'pledged', and move it out of 6D 'specific dated pledges'; rev L857 and L1466: add 'walk intake Q2 FY26 469.9, Q3 FY26 361.6, Q4 FY26 436.3, Q1 FY27 556.1, Q2 FY27 607.9 Cr (pres L247-L249, L289-L294; res L538): 600 Cr reached once in five quarters; the guide needs H2 intake about 50% above H2 FY26 797.9 Cr [INFERENCE]'. (5) L1-M3: rev L854, L622, L1419: add 'absolute co-reading: combined employee plus other expenses vs Q2 FY27 1,128.89 Mn (res L543, L546); at about 437 Cr a quarter the ratio stays below 28.72% with expenses up to about 1,255 Mn (+11.2% QoQ), so a ratio pass alone re-credits P09 and does not test There will not be any future investment in that area (cc L297)'."
style_notes:
  - "LS1-LS6 and run-1 S2 as listed under findings_by_type.style; logged, no re-run"
analyst_note: "Loop 1 addressed all eleven run-1 findings, and eight close clean. Every changed figure recomputes within rounding, and no Role 4 table number moved. The open faults run both ways. Bear-side: the new Step 7A row 24, the Step 8C note and the brief treat the chairman's 'not a one-off thing' as denying the one-off mix effect. The review itself records that he called mix a 'this quarter thing'; his words undercut only the product-development purchase leg, by inference. The new Q3 forks class a Q3 at the 30% bar as bear, yet at the bar both H2 quarters grow 30% YoY and Q4 needs the same +21.7% step Q4 FY26 made. Bull-side: the 600 Cr intake guide is carried as a pledge without its 'probably' and against a walk base rate of one quarter in five. The P07 intensity test passes with expenses up 11% in a quarter at the H2 revenue pace. One stale 8F cell still asks for the pipeline basis the chairman gave. All fixes are single-line edits. The verdict, cash class and WEAKENED impact do not move."
```

---
---

# LOOP 2 RE-AUDIT (Role 5 addendum, correction loop 2; final)

Agent: A5 adversary, fresh instance | Model: claude-opus-5-5 | Re-audit date: 2026-10-18
The run-1 record and the loop-1 re-audit above are kept unchanged. This section supersedes the loop-1 verdict and YAML. No further loop exists. Any open item goes to the flag list, not to a loop.
Scope (task message, strict): (1) deliverable gate; (2) closure of L1-C1, L1-C2, L1-M1, L1-M2 and L1-M3, with every changed figure recomputed (results Rs Mn); (3) no new FACTUAL / MISSING / CONTRADICTION in the loop-2 edits, and no Role 4 number touched. No adversarial pass beyond the edited passages. No full arithmetic sweep. No coverage re-run. The A2 ledger note for cc L238 is handled separately and is not re-flagged.
Inputs read: review_cyientdlm_q2fy27.md (1,469 lines; line numbers unchanged from loop 1, because each loop-2 edit replaces exactly one line); A4 edit file role5_parts/loop2_edits.md (E01-E32) and block a4-role5-loop2.yaml (finding map); concall fulltext (cc L196-L200, L228-L232, L252-L299); results fulltext (res L533-L552); presentation fulltext (pres L240-L299).
Not read: the source PDF, the audio, anything under inputs/, A3 reasoning. The concall ledger was not opened: coverage is out of scope, and no edit removes a row reference.
Tool limit: no git diff was available in this context. Role 4 integrity rests on the 32 FIND strings and a filing tie-out (section 4).

---

## 1. DELIVERABLE-COMPLETENESS AUDIT (gate)

| Part | Heading (rev line) | Status |
|---|---|---|
| 1. Summary narrative | "### 1. Summary narrative" (rev L1241-L1266), plus the call-vs-filing table (rev L1268-L1278) | PRESENT (25 bullet lines; spec 10-20; run-1 S2 still open, STYLE) |
| 2. Sector intelligence | rev L1280-L1289 | PRESENT |
| 3. Business-model intelligence | rev L1291-L1301 | PRESENT |
| 4. Competition intelligence | rev L1303-L1309 | PRESENT |
| 5. Forward map | rev L1311-L1327; 12 dated rows, each with a bull and a bear fork; the Q3 FY27 call row (rev L1317) also carries a labelled neutral band | PRESENT |

Gate: PASS.

---

## 2. LOOP-1 FINDING CLOSURE

| Loop-1 finding | Edits (A4 map) | Re-check against the extract (rev line; source line) | Status |
|---|---|---|---|
| L1-C1 chairman's "not a one-off thing" applied to the mix | E01, E02, E03, E18, E25, E32 | rev L520: "On mix the chairman agrees (cc L283-L284) ... product development 'has been going on for a while' (cc L286), so repeat purchases are likely [INFERENCE]. His 'it's not a one-off thing' (cc L291) refers to the S&M and PD investment drag". rev L536 and L550: the PD undercut cites cc L286 and carries [INFERENCE]; cc L291 is cited only for the drag. rev L1096: retagged "CONTRADICTED [INFERENCE] (call vs deck; PD-purchase leg only)"; mix leg has the chairman's support; the trailing fragment and the break are recorded. rev L1247 and L1466 corrected. Quotes match cc L283-L286, L291 and L293 verbatim. Tally rev L1098 stays 8 of 24; brief rev L1265 "Eight of 24" unchanged. Grep "against the chairman" and "removes management support": no hit | CLOSED (wording residue: L2-S1, L2-S3) |
| L1-C2 8F row 7 pipeline basis | E23 | rev L1186: "Q37: date of the $1.4 bn unweighted figure; weighted value of the ~$1.5 bn ... A dated 1.4 and a weighted value". Matches Q37 (rev L569) and cc L338-L339. Grep "one basis": no hit | CLOSED |
| L1-M1 Q3 forks | E04, E13, E21, E26, E27, E29, E32 | rev L1317: bull Q3 >= about 437 Cr (Q4 then needs no QoQ growth); labelled neutral band 394.29-437 Cr; bear below 394.29 Cr (Q4 must beat the FY26 Q4 step); two readings and the separating observation (Q3 FY25 not in the run) named with [INFERENCE, one year of data]. "+30.0% YoY; the same QoQ step Q4 FY26 made" is at rev L620, L856, L1150 (g), L1312 and L1417. Figures in section 3 | CLOSED (placement note: L2-S4) |
| L1-M2 600 Cr intake hedge and base rate | E05, E08, E14, E16, E17, E19, E20, E22, E30, E32 | rev L812 restores the full cc L256 sentence verbatim, with "probably", and the rejected first reply (cc L257). rev L983 "hedged, not pledged". rev L1054 moves it out of 6D "specific dated pledges"; 6C already counts cc L256 (rev L1049). rev L1126, L1140 and L1161 read "expected, hedged" with the base rate. rev L857 (P10), L621 and L1418 carry the five walk quarters and the +50% need. rev L1466 carries the hedge and "met once in five" but not the +50% leg, which sits in P10 (note at 196 of 200 words). Grep "pledged": only rev L983 ("not pledged"), L1262 (S&M) and L1317 (30% YoY) | CLOSED |
| L1-M3 P07 absolute co-reading | E06, E12, E31 | rev L854 (P07), L622 (monitorable 20) and L1419 (YAML) add the absolute co-reading against 1,128.89 Mn, the +11.2% headroom at about 437 Cr a quarter, the P09 double-credit and the cc L297 test gap. Quote matches cc L297 | CLOSED |

Loop-1 STYLE notes: LS1 CLOSED (grep "weakest base": no hit; "only QoQ decline in Step 3 (-2.36%)" or "weaker H2 base" at rev L620, L856, L1150, L1312 and L1417; L1317 wording removed). LS2 CLOSED (rev L820 and L853 tagged [INFERENCE]; "bonus" gone). LS3 CLOSED (rev L1243 "(deck alone: 6-15%)"). LS4 CLOSED (rev L931 relabelled; narrow count 5 of 8, recounted in section 3). LS5 CLOSED (rev L821 "as a policy, today", cc L199). LS6 CLOSED (rev L649 loop-1 and loop-2 lines; rev L1337 comment). Run-1 S2 OPEN (25 lines; A4 cites single-line anchoring).

---

## 3. CHANGED-FIGURE RECOMPUTATION (loop-2 figures only; results Rs Mn)

| Metric | A4 value (rev line) | Recomputed | Source line | Status |
|---|---|---|---|---|
| Walk intake Q2 FY26 | 469.9 Cr (L857) | 22,911 - 21,318 + 3,106.34 = 4,699.3 Mn | pres L289-L294; res L538 | OK |
| Walk intake Q3 FY26 | 361.6 Cr (L857) | 23,494 - 22,911 + 3,033 = 3,616 Mn | pres L249, L289-L293 | OK |
| Walk intake Q4 FY26 | 436.3 Cr (L857) | 24,166 - 23,494 + 3,691 = 4,363 Mn | pres L247, L289-L293 | OK |
| Walk intake Q1 FY27 | 556.1 Cr (L857) | 25,989 - 24,166 + 3,738.00 = 5,561 Mn | pres L290, L293; res L538 | OK |
| Walk intake Q2 FY27 | 607.9 Cr (L857) | 28,137 - 25,989 + 3,930.90 = 6,078.9 Mn | pres L289-L290; res L538 | OK |
| 600 Cr hit rate | once in five (L621, L857, L983, L1126, L1140, L1161, L1418, L1466) | only Q2 FY27 reaches 6,000 Mn | as above | OK |
| H2 FY26 intake; the +50% need | 797.9 Cr; about 50% (L621, L857, L1418) | 3,616 + 4,363 = 7,979 Mn; 12,000 / 7,979 = 1.504, +50.4% | as above | OK |
| P07 Q2 FY27 combined base | 1,128.89 Mn; 28.72% (L622, L854, L1419) | 678.87 + 450.02 = 1,128.89; / 3,930.90 = 28.718% | res L538, L543, L546 | OK |
| P07 headroom at the H2 pace | about 1,255 Mn, +11.2% QoQ (L622, L854, L1419) | 8,741.51 / 2 = 4,370.76 Mn; x 0.287184 = 1,255.2; / 1,128.89 = +11.19% | res L538, L543, L546 | OK |
| Q1 FY27 combined ratio | 27.47% (L854) | (644.31 + 382.41) / 3,738.00 = 27.467% | res L538, L543, L546 | OK |
| Q3 FY26 QoQ dip | -2.36% (L620, L856, L1312, L1317) | 3,033 / 3,106.34 = 0.97639 | pres L249; res L538 | OK |
| Only QoQ decline in Step 3 | (L620, L856, L1150, L1312) | QoQ +11.57%, -2.36%, +21.69%, +1.27%, +5.16% | rev L271-L275 | OK |
| Q4 FY26 step vs Q4 need at the bar | +21.7% both (L620, L856, L1150, L1312, L1317, L1417) | 3,691 / 3,033 = +21.69%; 479.86 / 394.29 = +21.70% | pres L247-L249 | OK (same within rounding) |
| YoY at the bar | +30.0% for both H2 quarters (L1317 and five more) | 3,942.9 / 3,033 = +30.00%; 4,798.6 / 3,691 = +30.01% | pres L247-L249; res L538 | OK |
| FY26 H2 shape | Q3 45.1% of H2; 394.3 / 479.9 Cr (L1317) | 12,614.85 - 5,890.61 = 6,724.24; 3,033 / 6,724.24 = 45.11%; 8,741.51 x 0.45106 = 3,942.9; remainder 4,798.6 | res L538; pres L249 | OK |
| Even split; Q4 then flat | about 437 Cr (L1317) | 4,370.76 Mn a quarter; Q4 = Q3, 0% QoQ | res L538 | OK |
| Neutral band YoY | (implied, L1317) | 394.29 / 303.3 = +30.0%; 437.08 / 303.3 = +44.1% | pres L249 | OK |
| Narrow-label analyst count | 5 of 8 (L931) | 7 slots less Q2 T016 and Q10 T087 (order book): Q3, Q5, Q6, Q8, Q9 | rev L905, L908, L912-L914, L917, L920-L921, L924 | OK |

No arithmetic mismatch above rounding.
Aside [INFERENCE]: the FY26-shape split of the H2 floor (394.3 / 479.9 Cr) equals the 30%-per-quarter bar. A 30% rise on each FY26 quarter keeps the FY26 weights. So on that reading, Q3 prints on the neutral/bear boundary itself. Near 394 Cr the fork label cannot separate the two readings; the Q4 need can.

---

## 4. ROLE 4 INTEGRITY

- Edit list: 32 FIND strings, one per line, 32 distinct lines. Inside Role 4 sections they touch only: the loop-1 note appended to the Step 8C bull line (E01, rev L520; the 40.05% threshold text before the note is unchanged), the Role 5 ANSWER STATUS cells of Q4 and Q18 (E02, E03), Role 5 addendum monitorables 18-20 (E04-E06), and a comment on the Role 4 YAML loop_iteration line (E28; value 2 unchanged). No Role 4 table number appears in any FIND string. No FIND string touches the acquisition passages (rev L380-L387, L1091, L1434).
- Tie-out after the edits: Table 1A, 15 line rows (revenue to PAT) x 6 periods = 90 cells (rev L106-L120), against res L538-L552: all tie. Step 3 (rev L270-L275) intact: 278.43, 310.63, 303.3, 369.1, 373.80, 393.09 Cr. Step 8C thresholds recomputed: H2 FY26 gross margin 1 - (4,269.79 - 238.48) / 6,724.24 = 40.05%; Q2 FY27 gross margin 1 - 2,460.31 / 3,930.90 = 37.41%; H2 FY26 combined ratio (1,160.54 + 826.71) / 6,724.24 = 29.55%.
- E24 restores the Role 4 brief range (6-15%) beside the call figure at rev L1243. The Role 4 range also stands at rev L1284.
Result: PASS. No Role 4 number changed.

---

## 5. NEW-ISSUE CHECK ON THE LOOP-2 EDITS

Each of E01-E32 was read in place and checked against its cited lines. No edit adds a FACTUAL, MISSING or CONTRADICTION finding. Four STYLE items remain. Each is wording or placement. None changes a grade, a count, a threshold or the verdict.

- L2-S1 (STYLE). Same-line qualifier on the mix leg. rev L520, L536, L1096 and L1247 say the chairman agrees with the deck on mix ("this quarter thing", cc L284). The same sentence says "it's not the revenue mix, revenue mix is always going to be there" (cc L284). The review quotes that clause nowhere (grep). "This quarter thing" scopes the CFO's mention to Q2. It does not say the mix effect will not recur. His premise, gross and contribution margin higher (cc L282), is contradicted by the filing (rev L1271). So his support is partial. Why STYLE, not MISSING: row 24 is graded on the PD leg only, Q4 stays PARTIALLY, and no count or threshold moves. The review already carries the structural-mix bear (Step 8C reading b, rev L521; the deck calls the mix shift the strategy, rev L1247). Fix at rev L1096: "On mix he scopes the CFO's mention to this quarter ('this quarter thing') and adds 'revenue mix is always going to be there' (cc L284): partial support".
- L2-S2 (STYLE). rev L1027 (Step 6A, not edited; A4 not_in_scope) still pairs the CEO's "some of these one-offs" (cc L231) with the chairman's "it's not a one-off thing" (cc L291) under the topic "product development cost", graded "Contradicted within the call" with no tag. After loop 2 the review reads cc L291 as the S&M and PD drag (rev L1096) and uses cc L231 as support for the deck's one-off label (rev L520, L536, L1096). The tension still holds, as a CEO-vs-chairman disagreement on whether the margin drag is one-off (cc L231: one-offs ease from Q1; cc L291: not a one-off). Fix: retopic "margin drag: one-off or investment" and tag [INFERENCE], to match row 24. A4's block rationale for leaving the row ("both statements concern the investment drag") would make cc L231 unusable as deck support. The review text does not carry that rationale, so no contradiction lands in the review.
- L2-S3 (STYLE). Gap location at rev L1096. The cc L291 fragment ends at the page break (cc L292). The transcript resumes at cc L293 (00:40:00, 7 s after cc L291). The 30-second gap falls between cc L293 and cc L294 (00:40:00 to 00:40:30), as rev L811 records. "At a page break and an audio gap (cc L292-L294)" is loose. "At a page break (cc L292), before the 30-second gap (cc L293-L294)" is exact. The reading (the sentence is unfinished) stands.
- L2-S4 (STYLE). Placement at rev L1317. The neutral band sits inside the bull-fork cell. It is labelled, but a reader who scans the bull column can take it as bull. On the Notion render, start it with "Neutral (not bull):" or move it to a line under the table.

---

## 6. ADVERSARIAL CHECK (edited passages only)

Two edited passages carry a management-favourable reading. Each was tested against the same extract.

### E1. The neutral band: "a Q3 of 394.29-437 Cr does not decide H2" (rev L1317)
Strongest bear counter:
- Q2 FY27 grew 26.54% YoY (rev L1242). Thirty percent in both H2 quarters needs re-acceleration.
- The Q4 FY26 step (+21.69%) came off the Q3 FY26 dip. A Q3 FY27 at the bar has no dip to recover from.
- Material availability limits conversion (cc L248-L251, L356; rev L828).
Survives: NO. A Q3 inside the band is already +30.0% to +44.1% YoY, so the band itself requires the re-acceleration. The bear fork keeps the case where Q3 fails it. The H2 floor still governs (tripwire g, rev L1150).

### E2. "The mix leg has the chairman's support" (rev L520, L536, L1096, L1247)
Strongest bear counter:
- Same sentence: "it's not the revenue mix, revenue mix is always going to be there" (cc L284).
- "This quarter thing" scopes the CFO's mention, not non-recurrence.
- His premise, gross margin higher (cc L282), is contradicted by the filed -381 bps (res L538, L541, L542; rev L1271).
Survives: PARTLY, not as a loop item. The structural-mix bear is already in the review (rev L521, L1247). The missing clause is logged as L2-S1. Precedent: loop-1 A3 ("as a policy, today"), logged as STYLE LS5.

Acquisition-economics probe: not re-run. Loop 2 touched no acquisition passage (section 4).

---

## 7. FINDINGS (loop 2, tagged)

### FACTUAL
- None.

### MISSING
- None.

### CONTRADICTION
- None.

### STYLE (logged; no loop)
- L2-S1: mix-leg support omits the same-line clause "revenue mix is always going to be there" (cc L284); rev L520, L536, L1096, L1247.
- L2-S2: rev L1027 within-call row: retopic "margin drag: one-off or investment" and tag [INFERENCE].
- L2-S3: rev L1096 gap location: page break at cc L292; 30-second gap at cc L293-L294.
- L2-S4: rev L1317 neutral band sits in the bull-fork cell; set it apart on the Notion render.
- S2 (run 1): still open. The summary narrative runs 25 lines against the 10-20 spec (rev L1242-L1266).

---

## 8. VERDICT (loop 2, final)

COMPLETE.
- All five loop-1 findings are CLOSED: L1-C1, L1-C2, L1-M1, L1-M2, L1-M3. All six loop-1 STYLE notes are closed.
- Every loop-2 figure recomputes within rounding. No Role 4 number changed.
- No FACTUAL, MISSING or CONTRADICTION finding is open. Open items for the flag list: none. STYLE carried for the record: L2-S1 to L2-S4 and run-1 S2.
- Verdict effect: none. PROCEED WITH FLAGS, cash INDETERMINATE-WITH-DIRECTION and the Role 5 impact WEAKENED stand. Step 7A stays 8 of 24. Answer status stays 1 / 4 / 4 / 21.
- Out of scope, handled separately: the A2 ledger note for cc L238 (R5-M4).

```yaml
stage: A5-adversary
company: "CYIENTDLM"
quarter: "q2fy27"
model: "claude-opus-5-5"
status: complete
loop_iteration: 2
verdict: COMPLETE
plain_language_brief:
  narrative: present
  sector: present
  business_model: present
  competition: present
  forward_map: present
coverage:
  orphan_rows: []          # coverage not re-run in loop 2 (scope); each edit replaces one line, no row reference removed
  missing_from_ledger: []  # cc L238 (R5-M4) handled separately per task; not re-flagged
arithmetic_mismatches: []  # every loop-2 figure recomputes within rounding (loop-2 section 3)
loop1_closure:
  L1-C1: CLOSED
  L1-C2: CLOSED
  L1-M1: CLOSED
  L1-M2: CLOSED
  L1-M3: CLOSED
  LS1-LS6: CLOSED
  S2: "OPEN (STYLE; summary narrative 25 lines vs 10-20)"
role4_numbers_changed: false
open_items: []             # no FACTUAL / MISSING / CONTRADICTION open
surviving_bear_counters:
  - {claim: "On mix the chairman agrees with the deck; the mix leg has the chairman's support (rev L520, L536, L1096, L1247)", counter: "Same sentence: 'it's not the revenue mix, revenue mix is always going to be there' (cc L284); 'this quarter thing' scopes the CFO's mention, not non-recurrence; his premise, gross and contribution margin higher (cc L282), is contradicted by the filed -381 bps (rev L1271). Partly lands; structural-mix bear already at rev L521 and L1247, so logged, not looped", source_line: "cc L282-L284; res L538, L541, L542", type: STYLE}
findings_by_type:
  factual: []
  missing: []
  contradiction: []
  style:
    - "L2-S1: rev L520, L536, L1096, L1247 say the chairman agrees with the deck on mix ('this quarter thing', cc L284) but omit the same-line clause 'revenue mix is always going to be there' (cc L284); support is partial (Q2 scoping, not non-recurrence) on a premise the filing contradicts (cc L282 vs rev L1271); no grade, count or threshold moves; fix at rev L1096: 'On mix he scopes the CFO's mention to this quarter and adds revenue mix is always going to be there (cc L284): partial support'"
    - "L2-S2: rev L1027 (not edited) pairs cc L231 'some of these one-offs' with cc L291 'not a one-off thing' under 'product development cost', untagged; the tension holds as CEO vs chairman on whether the margin drag is one-off; retopic 'margin drag: one-off or investment' and tag [INFERENCE] to match row 24"
    - "L2-S3: rev L1096 places the audio gap at cc L292-L294; the cc L291 fragment ends at the page break (cc L292), the transcript resumes at cc L293 (00:40:00), and the 30-second gap is cc L293-L294 (00:40:00 to 00:40:30), as rev L811 records; reading unchanged"
    - "L2-S4: rev L1317 neutral band sits in the bull-fork cell; labelled, but set it apart on the Notion render ('Neutral (not bull):')"
    - "S2 (run 1, open): summary narrative 25 lines vs 10-20 spec (rev L1242-L1266)"
loop_back_to: ""
gap: ""
style_notes:
  - "L2-S1 to L2-S4 and run-1 S2 as listed under findings_by_type.style; logged, no re-run"
analyst_note: "Loop 2 closes all five loop-1 findings and the six loop-1 style notes. Every changed figure recomputes from res L538-L546 and pres L247-L294: five walk quarters, the 797.9 Cr H2 FY26 intake and the +50% need, the 1,128.89 Mn P07 base and its +11.2% headroom, and the H2 split. No Role 4 number moved; Table 1A ties on 90 cells. Four style notes remain; none moves a grade, count or threshold. The one with substance runs bull-side: the review now says the chairman agrees with the deck on mix, but the same sentence says revenue mix 'is always going to be there' (cc L284), on a premise the filing contradicts. His support is partial. The structural-mix bear is already in the review (Step 8C reading b; the deck calls the mix shift the strategy), so it is logged, not looped. An aside for the Q3 read: the FY26-shape split of the H2 floor equals the 30%-per-quarter bar, so on that reading Q3 lands on the neutral/bear boundary. Near 394 Cr, read the Q4 need, not the fork label. Verdict, cash class and WEAKENED impact are unchanged."
```
