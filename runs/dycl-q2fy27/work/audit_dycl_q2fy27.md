# A5 ADVERSARY / COMPLETENESS AUDIT: Dynamic Cables Limited (DYCL), Q2 FY27 (CORRECTION LOOP 1 RE-AUDIT)

| Field | Value |
|---|---|
| Review under audit | runs/dycl-q2fy27/work/review_dycl_q2fy27.md (1,071 lines, corrected in loop 1) |
| Drift baseline | runs/dycl-q2fy27/work/review_dycl_q2fy27_loop0.md (1,032 lines) |
| Prior audit | runs/dycl-q2fy27/work/audit_dycl_q2fy27_loop0.md; runs/dycl-q2fy27/work/blocks/a5-loop0.yaml |
| Inputs read | 4 A1 fulltexts (spans named below), PR structured file (grep), 2 A2 ledgers (new rows and count blocks), both A4 reviews. No source PDF. Nothing under inputs/. No A3 file opened (the loop-1 A3 addendum is cited by A4; A5 did not read it). |
| Anchor convention | REV Lnnn = corrected review file line. REV0 Lnnn = loop-0 review file line. RES / PR / GOV Lnnn = fulltext file line. CC Lnnn = concall line prefix (file line = Lnnn + 20). LC / LP Lnnn = ledger_concall / ledger_pressrelease file line. |
| Units | Results Rs Lakhs x0.01 = Rs Cr, recomputed at full precision, then rounded. |
| Scope (task message) | (1) closure of F-01 to F-07 with recomputation; (2) deliverable gate; (3) drift check of every changed line, plus a verdict-card check; (4) coverage for new ledger rows only. Unchanged sections are not re-audited in full. |
| Model | claude-opus-5-5 |

---

## R. LOOP-0 FINDING CLOSURE (F-01 to F-07)

| ID | Type | Closing lines in corrected review | A5 recomputation (raw source) | Status |
|---|---|---|---|---|
| F-01 | FACTUAL | REV L370 (Step 8C guide arithmetic), L196, L173, L368, L390 (Q12), L490, L507, L736 (7A now NOT YET TESTABLE), L853, L862 (M4), L970, L981, L1037, L1040, L1063 | FY26 rev 1,19,781.73 L = 1,197.8173 Cr (RES L329). x1.20 = 1,437.3808. Less H1 FY27 712.2934 = 725.0874 H2 need. H2 FY26 = 1,197.8173 - 543.5921 = 654.2252; 725.0874 / 654.2252 = +10.83%. Per quarter 362.5437. Bull 327.1126 x 1.20 = 392.535; two quarters + H1 = 1,497.3636 = FY27 +25.01%. All match. REV L507 fixes the old REV0 L496 point (FY27 needs +10.8% H2 value, not volume above 20%). | CLOSED |
| F-02 | FACTUAL | REV L231-L234 (day-count rows), L244-L248 (basis), L254, L306, L731, L1057, L1068 | Balances RES L209, L211, L231-L232. Flows RES L329, L332, L334. TTM: rec 87.72 to 73.30 (-14.4); inv 65.42 to 79.79 (+14.4); pay 60.34 to 55.13 (-5.2); CCC 92.80 to 97.96 (+5.2). Trailing 6M: rec 80.31 to 70.31 (-10.0); inv 59.53 to 76.09 (+16.6); pay 54.91 to 52.57 (-2.3); CCC 84.93 to 93.83 (+8.9). TTM COGS 529.6725 + 583.8891 = 1,113.5616. All match REV L231-L234, L245-L246. | CLOSED |
| F-03 | CONTRADICTION | REV L913 (brief), L238 (Step 5 MF row), L1059 | Redemption 2,834.58 L = 28.35 (RES L503). Balance fall 3,062.04 - 92.85 = 2,969.19 L = 29.69 (RES L210). FV item 134.80 L = 1.35 (RES L464). 28.35 + 1.35 = 29.69. Brief and sources table now agree. | CLOSED |
| F-04 | FACTUAL | REV L737 | 1,529.01 / 28,155.68 = 5.4306%; 1,120.51 / 36,319.23 = 3.0852% (RES L329, L338). -234.5 bps, shown as -235. | CLOSED |
| F-05 | MISSING (A2) | LC L405-L409 (M06-M10), LC L18 count; LP L72 (M3), LP L15 count. A4 cites: M06 REV L466; M07 L467; M08 L471, L554; M09 L457, L473; M10 L474, L482, L497, L555, L658, L729, L782; M3 L27, L402, L480, L556, L730 | Ledger text matches the fulltext verbatim: CC L030-L034, L044-L047, L050-L054 (file L50-L74); PR L108-L110. | CLOSED |
| F-06 | MISSING | REV L102 (clause reads on this filing), L103 (prior-year record ND row), L106 ("Not a pattern" is not shown), L309, L403 (Q25), L418, L532, L848, L876 (M18 widened), L901, L920, L983, L1035, L1054, L1062 | All four fix elements are present: the qualifier, the widened monitor, the FY26 question and the Section C row. | CLOSED as specified. The trigger wording added with the widening is a new error: see N-01. |
| F-07 | MISSING | REV L849 (Section C Net impact), L921-L922 (summary) | 363.1923 / 281.5568 = 1.28994 (RES L329); / 1.06 = 1.2169, so +21.7% per unit. The 6% sits in the Q2 context (CC L113 "this quarter"; CC L123; CC L198). The pass-through reversal is carried at REV L933 and L626. | CLOSED (see S-10 on "four-fifths") |

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate)

| Part | Heading | Content check | Status |
|---|---|---|---|
| 1 Summary narrative | REV L903 | 19 lines (REV L905-L923), inside the 10-20 band. Each line carries a provenance tag. | present |
| 2 Sector intelligence | REV L925 | 12 lines (REV L927-L938) | present |
| 3 Business-model intelligence | REV L940 | 11 lines (REV L942-L952) | present |
| 4 Competition intelligence | REV L954 | 11 lines (REV L956-L966) | present |
| 5 Forward map | REV L968 | make-or-break line plus 10 catalyst rows, each with a bull and a bear column (REV L970-L983) | present (S-07 carried) |

Gate result: PASS.

---

## 1. COVERAGE AUDIT (new ledger rows only)

Method. I partitioned every sentence of the T03 opening (CC L025-L058) and of the press-release MD quote (PR L105-L111) against the structured rows and ledger sweep rows. Then I checked each new row against A4 citations.

| Document / category | A2 count | Fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Concall sweep rows (M01-M10) | 10 (LC L18, L400-L409) | 10. T03 partitions fully: L025-L029 greeting; L030-L032 M06; L033-L034 M07; L035-L037 R066; L038-L041 R113, R145; L042-L043 R067, R068; L044-L047 M08; L048-L049 R114; L050-L051 M09; L052-L054 M10; L055-L057 M01; L058 R115 | none | PASS |
| Press-release sweep rows (M1-M3) | 3 (LP L15, L72) | 3. MD quote partitions fully: PR L105 R125; L106 R126; L107 R127; L108 M2; L108-L110 M3; L110-L111 R128 | none | PASS |
| PR rows reviewed (A4 preamble) | 151 + 3 = 154 (REV L27) | 154 | none | PASS |
| Concall extra rows reviewed | M01-M10 (REV L28) | 10 | none | PASS |

Orphan test. Each of M06-M10 and M3 is cited in A4 (closure table, F-05 row). No orphan rows. No unit missing from the ledger.

---

## 2. ARITHMETIC AUDIT (every number on a changed line)

| Metric | A4 value (line) | Recomputed | Source line | Status |
|---|---|---|---|---|
| FY27 at +20% | 1,437.38 (REV L370) | 1,437.381 | RES L329 | PASS |
| H2 FY27 need; growth on H2 FY26 | 725.09; +10.8% (REV L370) | 725.087; +10.83% | RES L329 | PASS |
| Guide pace per quarter | 362.54 (REV L370) | 362.544 | RES L329 | PASS |
| Bull line; FY27 pace if held | 392.5; 1,497.36, +25.0% (REV L196) | 392.535; 1,497.364, +25.01% | RES L329 | PASS |
| Day counts, TTM and 6M, both dates | REV L231-L234 | identical (closure table, F-02) | RES L209, L211, L231-L232, L329, L332, L334 | PASS |
| TTM COGS; H2 FY26 COGS; H1 FY27 COGS | 1,113.56; 529.67; 583.89 (REV L245-L246) | 1,113.562; 529.673; 583.889 | RES L332, L334 | PASS |
| MF redemption; balance fall; FV item | 28.35; 29.69; 1.35 (REV L913, L238) | 28.346; 29.692; 1.348 | RES L503, L210, L464 | PASS |
| Other expenses / revenue YoY | -235 bps (REV L737) | -234.5 bps | RES L329, L338 | PASS |
| Price and mix per unit at 6% volume | +21.7% (REV L849, L922) | +21.69% | RES L329; CC L123 | PASS |
| Receivables change; inventory change | -4.7%; +40.9% (REV L482, L729, L402) | -4.67%; +40.89% | RES L209, L211 | PASS |
| Inventory build H1 FY27 | 70.65 (REV L402) | 70.647 (BS) / 70.647 (CF) | RES L209, L480 | PASS |
| Counts: PR rows; commitments; questions | 154; 16; 25 (REV L27, L524, L410) | 151 + 3; C01-C16; Q1-Q25 | LP L4, L15; REV L539-L556, L377-L403 | PASS |

No arithmetic mismatch.

---

## DRIFT CHECK (corrected review vs loop-0 review)

I compared the two files section by section. Every changed line is listed in the A4 change log (REV L881-L895), with three omissions (S-12).

| Area | Changed lines (REV) | Result |
|---|---|---|
| Header, preamble | L11, L22, L27-L28, L31 | Correct. ID ranges match the ledgers. |
| Step 0F governance | L102-L103, L106, L108 | F-06 closed. New trigger claim at L106 fails: N-01. |
| Steps 2-3, 8C | L173, L196, L368-L370 | Correct (F-01). |
| Step 5 | L231-L234, L238, L244-L248, L254 | Numbers correct. L248 seasonality sentence: S-11. L231, L247 loop history in body: S-13. |
| Step 6B, 7, 8.5, 9 | L306, L309, L345, L375, L390, L402-L403, L407, L410, L412, L418 | Correct. L345 and L407 changed without a change-log entry (S-12). |
| Role 5 Steps 0D, 1, 2 | L457, L466-L476, L480, L482-L484, L490, L497, L507 | Correct. PR L108 says "has improved despite" (CC-A3-19 reading holds). L480: S-14. |
| Role 5 Steps 3, 5B, 7A, 8B, 8F | L524, L532, L535, L537, L554-L556, L658, L729-L731, L736-L737, L782, L826 | Correct. PR has no inventory or cash-flow line (grep), so L730 "leaves out" holds. C16: S-14. |
| Section C verdict card | L847-L849, L853 | Every change is logged (item 7, F-06, F-07, F-01). Thresholds 392.5 / 363.19 unchanged. Verdict PROCEED WITH FLAGS, cash class and branch 8A-W unchanged. L853 "equals": S-09. |
| Monitorables | L859, L861-L862, L871, L876 | M1, M4 correct. M18 trigger claim: N-01. |
| Brief | L901, L913-L923, L970, L975, L981, L983 | Numbers correct. L849 and L922 "four-fifths": S-10. L983 bear fork: N-01. |
| A4 YAML | L999, L1022, L1034-L1035, L1037, L1039-L1040, L1049, L1054, L1057-L1063, L1068 | Correct, except L1054 and L1062: N-01. |

Verdict-card check: no verdict-card number moved except as the change log states. The new numbers on the card (L849: 6%, +21.7%; L853: 1,437.38, 725.09, 362.54) are logged under F-07 and F-01.

### N-01 (FACTUAL, loop A4). The Z-group trigger is overstated. A5 owns the origin.

- Extract: "Further in the event of this being the second consecutive year of non-compliance for the Regulation 31 would result in the company being transferred to Z group" (GOV L173-L174). The extract does not define "year".
- A4, corrected review:
  - REV L106: "any further Reg 31 delay on a filing up to the Jun-2027 quarter (due 21-Jul-2027) would put a second consecutive year on the record and trigger the Z-group rule".
  - REV L876 (M18): "Any delay puts a second consecutive year on the record and triggers the Z-group rule."
  - REV L983 bear fork: "Any delay: a second consecutive year of Reg 31 non-compliance".
  - REV L1054: "any delay makes a second consecutive year and triggers the Z-group rule".
  - REV L1062: "any Reg 31 delay to Jul-2027 triggers it".
- Why it fails:
  - The lapsed filing was for the Jun-2026 quarter, due 21-Jul-2026 (GOV L38; REV L95). The Sep-2026 quarter filing is due 21-Oct-2026. Both fall in FY27 and in calendar 2026. On a financial-year, calendar-year or rolling 12-month reading, a Sep-2026 delay is a second lapse in the same year, not a second consecutive year.
  - For the Dec-2026, Mar-2027 and Jun-2027 quarters, the answer depends on how "year" is read. The extract does not say. So "any delay triggers" is a claim the extract does not support, and for one of the four filings it is wrong on every natural reading.
- Origin: my loop-0 F-06(b) text said "Any Reg 31 lapse in the following year can count. The first test is the Sep-2026 pattern due 21-Oct-2026" (audit_dycl_q2fy27_loop0.md L178). That sentence was wrong. A4 followed it faithfully.
- Fix (wording only, five places): keep the widened monitor on every filing to Jul-2027. Replace the trigger sentence with: "GOV L173-L174 does not define 'year'. A delay on the Sep-2026 quarter filing would be a second lapse in the same financial and calendar year as the Jun-2026 lapse. Whether a delay on the Dec-2026, Mar-2027 or Jun-2027 quarter filing makes a second consecutive year is ND. Any further delay is a second Reg 31 lapse and a possible Z-group trigger." Optionally extend Q25 with: "How does BSE count a 'year' under this clause?"
- Moves a number or the verdict: no. Governance weight stays LOW. Classification stays GOVERNANCE-MINOR.

---

## 3. ADVERSARIAL READ (positive claims on changed lines)

### ADV-R1. Claim: receivable days "GREEN on both matched windows" (REV L231); the "prudent working capital" claim "holds on collection" (REV L482, L729)
- Bear counter from the extract:
  - Other current assets rose Rs 10.32 Cr (2,356.25 L to 3,388.20 L, RES L216; CF RES L483). That offsets most of the Rs 13.45 Cr receivable fall (RES L211).
  - The filing does not split other current assets. So a move of contract assets or retention money out of trade receivables cannot be ruled out [INFERENCE].
- Survives: NO.
  - The receivable fall is filed. No discounting, factoring or bill line appears in any fulltext (grep).
  - The company KPI on gross sales (~59 days, PR L129) reconciles independently (70.3 / 1.18 = 59.6).
  - A4 already asks about the other-current-asset rise in Q17 (REV L395). Nothing to graft.

### ADV-R2. Claim: "a bear-line Q3 still keeps the 20% guide on pace" (REV L370, L923)
- Bear counter from the extract:
  - The H2 need of +10.8% is a value figure. With 80-90% pass-through (CC L255) and metal "dipping" (CC L317), H2 realisations fall unless volume grows.
  - Q3 FY26 and Q4 FY26 are not filed, so the H2 seasonal split is ND.
  - Management refused an FY27 number (CC L372). The analyst framed the 20% as "long-term guidance" (CC L368).
- Survives: NO. A4 carries each piece: the FY27 refusal (REV L370, L736), the metal bear fork (REV L981) and the long-run reading (REV L507). The claim is labelled as arithmetic, not a commitment.

### ADV-R3. Claim: "Growth is real at the top line in value terms" (REV L849, L921)
- Bear counter: this is the loop-0 ADV-1 counter. It is now grafted (F-07 closed). Survives: already incorporated.

### Mandatory acquisition-economics probe
- Not triggered. No changed line describes an acquisition, purchase or stake buy. The loop-0 finding stands (audit_dycl_q2fy27_loop0.md L169).

---

## FINDINGS REGISTER

| ID | Type | Loop to | Gap | Moves a verdict-card number? |
|---|---|---|---|---|
| N-01 | FACTUAL | A4 | Z-group trigger stated as certain for any Reg 31 delay to Jul-2027. GOV L173-L174 does not define "year". A Sep-2026 quarter delay is in the same year as the Jun-2026 lapse. REV L106, L876, L983, L1054, L1062. Origin: A5 loop-0 F-06(b). | No. The governance row (REV L848) is unaffected. |

---

## VERDICT

INCOMPLETE.

- Loop-0 findings: F-01 to F-07 all CLOSED. Recomputation matches on every number.
- New finding: N-01 (FACTUAL, A4). Wording only, five lines. No number, verdict, cash class or branch moves. A2 and A3 need no re-run.
- Exact gap: restate the Z-group trigger at REV L106, L876 (M18), L983, L1054 and L1062 with the N-01 fix text. Optionally extend Q25.

---

## STYLE NOTES (logged, no loop)

Carried from loop 0 (unchanged in the corrected review; none required):
- S-01. Peer-work quotes (REV L936, L957) come from a Notion page outside A5's inputs. A5 did not verify them. Their provenance tag is present.
- S-02. REV L958 tags CC L186 (analyst turn T35) as MGMT-ASR.
- S-03. REV L237 labels RES L207 "Capital advances" with no [INFERENCE] tag.
- S-04. REV L178 attributes the OI fall to MF redemption with no [INFERENCE] tag. Interest income fell 2.08 to 0.96 Cr (RES L461).
- S-05. Note 5 (RES L363) conforms the comparatives. The REV L70 caveat and the Q13 premise could say so.
- S-06. REV L609 counts the CC L202 analyst misreading as pushback.
- S-07. The forward-map trading-window row (REV L974) has identical forks. Two catalysts are undated.
- S-08. A1 anchor drift: concall R037-R038 cite line 267; the text is on CC L268.

New in loop 1:
- S-09. REV L853 says Rs 362.54 Cr "equals the bear line". The bear line is Rs 363.19 Cr. Use "about", as REV L859 and L970 do.
- S-10. REV L849 and L922 say "four-fifths". The stated working (+21.7% per unit) gives 21.7 of 29.0 points, 75%. Four-fifths needs the cross term: 1.06 x 21.7% = 23.0 of 29.0 points, 79%. Show "23.0 of 29.0 points" or say "about three-quarters".
- S-11. REV L248 says the 6M basis divides by "a strong H2" and "a weaker H1", with no [INFERENCE] tag. The filed H1 FY27 flows exceed H2 FY26 (revenue 712.29 vs 654.23; COGS 583.89 vs 529.67). Seasonality is one component, not the net effect.
- S-12. The change log omits three changed loop-0 lines: REV0 L339 (now REV L345, "refused as an FY27 number"), REV0 L398 (now REV L407, Q24 cross-reference) and REV0 L867 (now REV L901, prior-year Reg 31 record added to the ND list). No number is involved.
- S-13. Loop history sits in body text that goes to Notion: REV L231 ("smaller than loop 0 stated") and REV L247 ("Loop 0 set..."). Move it to the change log.
- S-14. C16 (REV L556) registers a historical claim ("We have always followed...") as a commitment with status "underway". REV L480 "It is a scripted line" has no [INFERENCE] tag.

---

```yaml
stage: A5-adversary
company: "DYCL"
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
  missing_from_ledger: []
arithmetic_mismatches: []
surviving_bear_counters: []
findings_by_type:
  factual:
    - "N-01 A4: Z-group trigger stated as certain for any Reg 31 delay to Jul-2027 (REV L106, L876 M18, L983, L1054, L1062); GOV L173-L174 does not define 'year'; Sep-2026 quarter filing (due 21-Oct-2026) is in the same financial and calendar year as the Jun-2026 lapse (due 21-Jul-2026); origin A5 loop-0 F-06(b) wording"
  missing: []
  contradiction: []
  style:
    - "S-01 (carried) peer-work quotes REV L936, L957 outside A5 inputs, unverified, provenance tag present"
    - "S-02 (carried) REV L958 tags analyst turn CC L186 as MGMT-ASR"
    - "S-03 (carried) REV L237 'Capital advances' label for RES L207 without [INFERENCE]"
    - "S-04 (carried) REV L178 OI fall attributed to MF redemption without [INFERENCE]; interest income RES L461"
    - "S-05 (carried) Note 5 RES L363 conforms comparatives; REV L70 caveat and Q13 could say so"
    - "S-06 (carried) REV L609 counts CC L202 analyst misreading as pushback"
    - "S-07 (carried) forward map REV L974 trading-window row identical forks; two catalysts undated"
    - "S-08 (carried) A1 concall R037-R038 anchor line 267; text on CC L268"
    - "S-09 REV L853 'equals the bear line': 362.54 vs 363.19; use 'about'"
    - "S-10 REV L849, L922 'four-fifths': +21.7% gives 21.7 of 29.0 points (75%); four-fifths needs the cross term, 23.0 of 29.0 (79%)"
    - "S-11 REV L248 'strong H2 / weaker H1' untagged; filed H1 FY27 flows exceed H2 FY26 (712.29 vs 654.23 revenue; 583.89 vs 529.67 COGS)"
    - "S-12 change log omits REV0 L339, L398, L867 (now REV L345, L407, L901); no number involved"
    - "S-13 loop history in body text REV L231, L247; move to change log"
    - "S-14 C16 REV L556 registers a historical claim as a commitment 'underway'; REV L480 'scripted line' untagged"
loop_back_to: "A4"
gap: "A4 only (N-01, FACTUAL, wording): at REV L106, L876 (M18), L983, L1054, L1062 keep the widened monitor on every Reg 31 filing to Jul-2027 but replace the trigger claim with: 'GOV L173-L174 does not define year. A delay on the Sep-2026 quarter filing would be a second lapse in the same financial and calendar year as the Jun-2026 lapse. Whether a delay on the Dec-2026, Mar-2027 or Jun-2027 quarter filing makes a second consecutive year is ND. Any further delay is a second Reg 31 lapse and a possible Z-group trigger.' Optional: extend Q25 to ask how BSE counts a year under this clause. No number, verdict, cash class or branch moves; A2 and A3 not re-run."
style_notes:
  - "S-01 (carried) peer-work quotes REV L936, L957 unverified by A5"
  - "S-02 (carried) REV L958 retag CC L186 analyst tier"
  - "S-03 (carried) REV L237 tag [INFERENCE] on capital advances"
  - "S-04 (carried) REV L178 tag [INFERENCE] on OI fall cause"
  - "S-05 (carried) REV L70 / Q13 Note 5 conforming wording"
  - "S-06 (carried) REV L609 CC L202 not pushback"
  - "S-07 (carried) REV L974 trading-window row identical forks"
  - "S-08 (carried) A1 R037-R038 anchor L267 vs CC L268"
  - "S-09 REV L853 'equals' to 'about'"
  - "S-10 REV L849, L922 show 23.0 of 29.0 points or say about three-quarters"
  - "S-11 REV L248 tag seasonality sentence [INFERENCE]; growth outweighs seasonality in filed denominators"
  - "S-12 change log omits REV0 L339, L398, L867"
  - "S-13 move loop history out of REV L231, L247"
  - "S-14 C16 is a historical claim, not a commitment; tag REV L480 inference"
analyst_note: "Re-audit, correction loop 1. All seven loop-0 findings close. Every changed number recomputes from RES L201-L514: FY27 +20% = Rs 1,437.38 Cr; H2 needs Rs 725.09 Cr (+10.8%), Rs 362.54 Cr a quarter; matched-window cash cycle +5.2 (TTM) / +8.9 (6M) days; MF redemption Rs 28.35 Cr; -235 bps; +21.7% per unit. No verdict-card number moved outside the change log. The verdict, cash class and branch are unchanged. One new FACTUAL finding, N-01, and A5 owns its origin. My loop-0 F-06(b) said 'the first test is the Sep-2026 pattern'. That was wrong. GOV L173-L174 does not define 'year', and the Sep-2026 quarter filing falls in the same financial and calendar year as the Jun-2026 lapse. A4 applied my wording and now states that any Reg 31 delay to Jul-2027 'triggers' the Z-group rule (REV L106, L876, L983, L1054, L1062). The fix is wording only, in five places: keep the widened monitor and state the year definition as ND. No number or verdict moves. If the quarterly loop cap is spent, N-01 is self-contained enough to carry as an open item."
```
