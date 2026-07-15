# Verifier D: Peer Coverage Audit — FEDFINA (2026-07-15)

Model: claude-sonnet-5 | Fresh context | Inputs: 15 peer transcripts (Manappuram x4, MAS
Financial x4, SBFC x3, Five-Star x4) + B06 (06-peers.md) + B05.peer_questions[] (9 items)

Scope note: the stage-12 master prompt's INPUTS line names "{{12_PEER_TRANSCRIPTS}}" but the
actual injected set is 15 files, matching B06's own stated coverage (4+4+3+4). All 15 were read
in full or targeted-searched against every B06 citation. This is a MINOR documentation mismatch
in the pipeline prompt, not a B06 defect — noted for completeness, not scored against B06.

---

## PART 1: COVERAGE AUDIT TABLE (peer x quarter, all marked SUBSTANTIVE in B06 Part 3)

| Peer | Quarter/File | B06 claimed contribution | Verified in transcript? | Result |
|---|---|---|---|---|
| Manappuram | Aug 2025 (Q1 FY26) | Yield 22.2%→20.7%, LTV 57%, tonnage "hardly there, just 1%" vs AUM +12% | Bindu A.L.: "Last quarter, the yield was 22.2% this quarter, 20.7%"; "Average LTV at 57%"; Gaurav Q&A: "tonnage, growth is hardly there, just 1%" vs AUM +12% QoQ | CONFIRMED, exact |
| Manappuram | Nov 2025 (Q2 FY26) | 20-25% CAGR guidance, LTV 56%, static branch count (analyst) | V.P. Nandakumar: "we are targeting a CAGR of 20%-25%... 25% CAGR can be maintained"; Bindu: "average LTV remains at 56%"; Shweta Daptardar: "Our branch count has remained static" | CONFIRMED, exact |
| Manappuram | Feb 2026 (Q3 FY26) | AUM 22-23% Y-o-Y, mix-driven yield explanation, tonnage +2.8% Y-o-Y | Zhixuan: "AUM growth is very good at 23%"; Bindu: "AUM growth is almost 22%... shifting to higher ticket borrowers"; Nandakumar opening: "tonnage was 58.9 up by 3.2% Q-o-Q and up by 2.8% Y-o-Y"; yield "19.7% last quarter to 18.3% this quarter" (Abhijit Tibrewal) | CONFIRMED, exact |
| Manappuram | May 2026 (Q4 FY26) | Tonnage +3.82 tons, yield guided 17.5-18%, LTV regime detail | "Tonnage grew by 3.82 tons in Q4"; Piran Engineer: "tonnage growth is 6%-7% Q-o-Q"; Nandakumar: "We expect the yield to remain between the 17.5%-18%"; LTV 57%, new April-2026 LTV-regulation detail | CONFIRMED, exact |
| MAS Financial | Nov 2025 (Q2 FY26) | Opex-to-assets 2.84%, distribution-point staffing cost driver | Kamlesh Gandhi: "our opex cost is 2.84%"; "15,000 distribution points, it has to be staffed properly" | CONFIRMED, exact |
| MAS Financial | Feb 2026 (Investor/Analyst Meet, Q3 FY26) | Co-lending guideline "come to live very recently," fresh-guard repricing; branch expansion "20 to 25 new branches" | Ankit Jain (line 2013): "there has been a change in co-lending guidelines which has come to live very recently... take a fresh guard"; Darshana Pandya (p.12): "every year we are planning to open 20 to 25 new branches" | CONFIRMED, exact (see note below on sub-file labeling) |
| MAS Financial | Feb 2026_2 (Q3 FY26 earnings call) | Cost-to-income 36.6% (Q5 anchor); CV stress "Rajasthan 1 and 2... MP 1 and 2" (Q4 anchor) | Hardik Doshi Q: "cost-to-income ratios also continue to remain high at 36.6%"; Kamlesh Gandhi: "distinct stress in Rajasthan 1 and 2... and MP 1 and 2" | CONFIRMED, exact |
| MAS Financial | May 2026 (Q4 FY26) | Confirms prior-guided MFI-linked NPA resolution | Analyst: "in the next 2 quarters, you will see all your credit quality issues and the NPA supplied in the microfinance book, that seems to be taking place. So, congratulations" | CONFIRMED, exact |
| SBFC | Jul 2025 (Q1 FY26) | Gold branch co-location economics (AUM/branch >Rs7.5-8cr); "hand loan" blind spot | Mahesh Dayani: "the moment your AUM per branch is more than INR 7.5 crores to INR 8-odd crores, it is a highly profitable product"; "a grey area for the entire industry" re: hand loans | CONFIRMED, exact |
| SBFC | Nov 2025 (Q2 FY26) | Sub-7L LAP pullback; Karnataka-specific stress (11-12%), TN "not very large"; no DA/co-lending upfronting | Mahesh Dayani: "sub 7 lakhs"; "Karnataka where we hold close to around 11%-12% odd"; "We are present in Tamil Nadu, but the portfolio is not very large"; Aseem Dhru: "we do not upfront any income through DA or any co-origination"; also "political risk and climate risk" and MSME TAM "24%... neither accelerated nor decelerated" | CONFIRMED, exact |
| SBFC | Jan 2026 (Q3 FY26) | Cost-to-income 35% (Q5 anchor); yield -23bps on risk-driven LAP cuts | Aseem Dhru: "we now have moved to a cost-to-income ratio of 35%... reduced it by 150 basis points"; Narayan Barasia: yield "17.78%... reduction of 23 basis point"; "we have cut down small ticket LAP... this is more like a hygiene" | CONFIRMED, exact |
| Five-Star | Aug 2025 (Q1 FY26) | MFI-overlap spillover mechanism; cost-to-income 33%/41%; TN NPA sub-1.5%, TN/Telangana strong | Srikanth: "the overlap has actually gone up... what used to be about 30-odd percent of microfinance"; "broadly 33% cost to income and about 8% of credit cost to income"; "Tamil Nadu's NPA is sub-1.5%... the two big states of Tamil Nadu and Telangana are performing very well" | CONFIRMED, exact |
| Five-Star | Nov 2025 (Q2 FY26) | Maharashtra "turnaround state," cost-to-income ex-credit ~31% | Srikanth: "that is a turnaround state for us. We will definitely grow the state in the coming quarters"; "cost-to-income ex-credit cost is largely stable at around 31%" | CONFIRMED, exact |
| Five-Star | Feb 2026 (Q3 FY26) | Continued MFI-overlap discussion at small-ticket end | Renish Bhuva / Srikanth exchange on 25-30% MFI overlap persisting under new regime | CONFIRMED |
| Five-Star | May 2026 (Q4 FY26) | Opex-to-AUM guided 7-7.25%; Maharashtra branch push 40→70-80 | Srikanth: "opex to AUM level, we should be at about 7% to 7.25% for this year"; Lakshmipathy D: "moving our branch network from close to 40 to 70, 80 branches in Maharashtra" | CONFIRMED, exact |

**Result: 15/15 SUBSTANTIVE claims confirmed with a real, findable, accurately-quoted citation.
Zero fabricated or misattributed citations found.**

Note on sub-file labeling (MINOR): the Q8 co-lending quote and the "20-25 branches/year" quote
both live in the MASFIN "Feb 2026" investor/analyst-meet transcript (48-page event, not the
quarterly earnings call proper), while a separate file "Feb_2026_Transcript_2.txt" holds the
Q3 FY26 earnings-call transcript with the 36.6% cost-to-income and Rajasthan/MP quotes. B06's own
transcript inventory (report header) explicitly discloses both files as "two separate transcripts
of the same quarter, labelled Feb 2026 and Feb 2026_2," so this is disclosed methodology, not a
concealed error. No rework needed; flagged as MINOR presentational note only.

---

## PART 2: UNUSED-BUT-RELEVANT CHECK

B06 marks all 15 transcripts SUBSTANTIVE (Part 3: "All 15 provided transcripts yielded material,
cited evidence; none classified CITED-ONLY or UNUSED"). Spot-reading each transcript beyond the
cited passages for claim-relevant material B06 did not use:

- Five-Star Aug 2025: LGD data (15-20% seasoned, 18-20% IRR recovery on settled NPAs) — informative
  on Five-Star's own credit quality but not tied to any of the 9 peer_questions; correctly left
  unused. Industry-context, not claim-relevant.
- SBFC Jul/Nov 2025: political risk (Karnataka ordinance) and "hand loan" blind spot — both WERE
  captured in B06 Part 2E ("Risks peers discuss that Fedfina does not"), so not missed.
- MAS Financial Feb 2026 investor meet: extensive SME product/yield-matrix detail (12%-19% by
  sub-product), Vision 2036 targets — general company detail, not tied to any Fedfina claim in
  B05's peer_questions list; correctly left unused.
- Manappuram: Bain Capital transaction detail, leadership transition (Deepak Reddy medical leave,
  May 2026) — company-specific governance news with no bearing on the 9 claims; correctly unused.

No directly claim-relevant peer statement was found unused in any transcript. No industry-context
items were found that should have been folded into Part 2 but were missed either.

**Result: 0 unused_but_relevant items.**

---

## PART 3: VERDICT-DISCIPLINE AUDIT (per claim)

| Claim | B06 Verdict | Peer anchors cited | Independent peers | Rule 4 check |
|---|---|---|---|---|
| Q1 (gold AUM growth) | PARTIALLY VERIFIED | Manappuram only (3 transcripts) | 1 | Correctly capped below VERIFIED — Muthoot absent from evidence set, single-peer coverage. PASS |
| Q2 (LTV/yield mix) | PARTIALLY VERIFIED | Manappuram only | 1 | Correctly capped — Fedfina's own LTV figure absent, magnitude untestable. PASS |
| Q3 (sub-5-7L LAP/MFI spillover) | VERIFIED | Five-Star, SBFC, MAS Financial (anchor_count 4) | 3 | ≥2 independent peers with real anchors — VERIFIED justified. PASS |
| Q4 (MH/TN stress) | CONTRADICTED | Five-Star, SBFC, MAS Financial | 3 | Contradiction well-evidenced by 3 independent peers each naming a different stress state. PASS |
| Q5 (cost-to-income gap) | VERIFIED | SBFC 35%, Five-Star 31-41%, MAS Financial 36.6% (anchor_count 3) | 3 | ≥2 independent peers — VERIFIED justified. PASS |
| Q6 (MT LAP yield compression) | PARTIALLY VERIFIED | SBFC (MASFIN silent, disclosed) | 1 effective | Correctly capped — B06 itself flags MASFIN as silent on this specific point. PASS |
| Q7 (branch capex cycle) | PARTIALLY VERIFIED | SBFC, Five-Star, MAS Financial | 3 | Correctly held at PARTIALLY VERIFIED despite 3 peers because scale/funding-logic mismatch is explicitly the basis for non-full-verification, not anchor count. PASS |
| Q8 (DA-to-co-lending shift) | PARTIALLY VERIFIED | MAS Financial, SBFC | 2 | Correctly capped — SBFC structurally avoids the mechanic, so only 1 peer actually confirms magnitude/timing; reasoning transparent in "net read." PASS |
| Q9 (tonnage growth) | CONTRADICTED | Manappuram (only named peer) | 1 | Contradiction stands on a single peer, but this is the only peer named in the B05 question itself (check_peers: ["Manappuram"]), and the figure (2.8% Y-o-Y) is a direct, explicit disclosure, not an inference. Rule 4 targets VERIFIED-on-one-peer as MAJOR; CONTRADICTED is not covered by that rule and the single citation is unambiguous management-disclosed data. No fail. |

**No claim was upgraded from silence. No VERIFIED claim rests on a single peer. Both VERIFIED
verdicts (Q3, Q5) have 3 independent, real citations each.**

Cross-check against B05.peer_questions[] (9 entries, verbatim): all 9 questions (Muthoot/Manappuram
growth; LTV/yield mix; sub-5-7L LAP stress; MH/TN stress; cost-to-income; MT LAP yield; branch
capex; DA-to-co-lending; tonnage growth) map 1:1 to B06 Part 1 Q1-Q9. **No skipped claim.**

---

## PART 4: FINDINGS

| Severity | Location | Note |
|---|---|---|
| MINOR | B06 Part 3, MASFIN Feb 2026 rows | Two MASFIN "Feb 2026" source files (investor/analyst meet vs. earnings-call transcript) are both cited under a single "Feb 2026/Q3 FY26" label in places; B06 discloses this explicitly in its report header ("two separate transcripts of the same quarter"), so the ambiguity is transparent, not concealed. Presentational only. |
| MINOR | B06 Part 3, MASFIN May 2026 row | Contribution line ("Confirms resolution of prior MFI-linked NPA flow-through") rests on a single analyst-framed confirmation rather than a management-disclosed number; still a real, correctly-quoted, claim-relevant citation, so SUBSTANTIVE classification holds. Flagged only for thinness relative to other rows. |

No CRITICAL or MAJOR findings. Every SUBSTANTIVE citation checked against source text was
verbatim or near-verbatim accurate. No fabricated peer evidence. No claim-relevant peer material
was found unused. No verdict was upgraded from silence. Both VERIFIED verdicts carry ≥2
independent peer anchors as required.

---

## PART 5: OVERALL ASSESSMENT

B06 is a high-fidelity peer-verification report. Across 15 transcripts and 9 injected claims,
every citation traced to source cleanly, quarter/speaker attribution was accurate in all but one
presentational ambiguity (self-disclosed by B06), and verdict discipline (2-peer rule for VERIFIED,
no silent upgrades, full claim coverage) was honored throughout. The report's most consequential
finding — the tonnage-growth contradiction (Q9) — is anchored to an explicit, unambiguous
management disclosure ("tonnage was 58.9 up by... 2.8% Y-o-Y") and is not overstated relative to
what the single available peer disclosed.

```yaml
stage: B12d
company: "FEDFINA"
run_date: "2026-07-15"
model: claude-sonnet-5
status: complete
peers_audited: 15
substantive_confirmed: 15
substantive_unsupported: []
unused_but_relevant: []
claims_all_addressed: true
verdict_discipline_fails: []
findings:
  - {severity: "MINOR", location: "B06 Part 3, MASFIN 'Feb 2026' rows", claimed: "single 'Feb 2026/Q3 FY26' label spans two distinct source files (investor/analyst meet + earnings call)", source_truth: "B06's own header discloses both files as 'Feb 2026' and 'Feb 2026_2' for the same quarter", note: "presentational ambiguity, self-disclosed by B06, not concealed"}
  - {severity: "MINOR", location: "B06 Part 3, MASFIN May 2026 row", claimed: "contribution described as confirming prior MFI-linked NPA resolution", source_truth: "rests on one analyst-framed confirmation rather than a fresh management-disclosed figure", note: "citation is real and accurate; flagged only for relative thinness vs other SUBSTANTIVE rows"}
critical_count: 0
major_count: 0
minor_count: 2
acceptance_rate: 100
```
