# VERIFIER B: CONCALL RED FLAGS, AVIENCE (phase 1, run 2026-09-26)

Model: claude-opus-5-5. Mode: NO-CONCALL MODE (manifest `concalls_available: false`).
Following the orchestrator's NO-CONCALL MODE section, the communication analysis is audited against the AR, the results filings, the RHP and the announcements, as well as the company's one transcript.

Sources read fresh for this audit (`[page N]` = PDF page):
- Company transcript: `inputs/concalls/Concall_Jul_2026_Transcript.txt` (H2/FY26 call, 24-Jul-2026, filed 28-Jul-2026). This was read in full.
- Results: original audited results OCR 27-Jul-2026; revised consolidated results 25-Aug-2026 (`inputs/results/`); 17-Jul-2026 cash-flow extract.
- AR FY2026: Board's Report (p.39-50), MD&A Annexure-4 (p.63-66), Notes 13/14, CARO Annexure 1.
- RHP Jun-2026: Objects of the Issue and Schedule of Implementation (p.125-131), state-wise revenue (p.160), SWOT (p.210).
- Announcements folder: all 10 files were scanned for any order or tender filing. None exists.
- Peer transcripts: QLINE Jun-2026 and TARSONS Feb/Aug-2026 were read at the passages that bear on the claims. MOLBIO Sep-2026 and TARSONS Nov-2025/Jun-2026 were checked only at the anchors B06 cites.
- Pipeline artifacts under audit: `outputs/reports/05-concall.md`, `outputs/blocks/B05-concall.yaml`, `outputs/reports/06-peers.md`.

Structural limit: there is only one company transcript. Tone shifts between quarters and repeated evasions (2+ quarters) cannot be observed, so a CRITICAL cannot come from the repeated-evasion test. Contradictions were tested across documents instead: RHP (Jun) vs call (Jul) vs revised results (Aug) vs AR (Sep).

---

## 1. INDEPENDENT RED-FLAG LIST (my read, before comparison)

| # | Item | Anchor | Severity |
|---|---|---|---|
| I1 | The CMD says twice that a ~Rs 47 Cr order is "in hand". He names no customer and no tender. No Reg 30 filing exists. The order is about 90% of FY26 revenue (Rs 52.51 Cr). | Transcript p.3, p.5 (Choudhary); announcements folder (no order filing) | MAJOR |
| I2 | The call contradicts itself on that order. It is "in hand" (p.3, p.5). Yet on working capital: "once confirmed orders are in place, banks and financial institutions can support" (p.6). The AR Board's Report sec.4, signed 07-Sep-2026, says "no material changes and commitments affecting the financial position" apart from the IPO. | Transcript p.6 (Choudhary to Manav Kothari); AR p.39-40 | MAJOR |
| I3 | The call was held for H2 FY26. That half grew revenue +5.0% YoY (Rs 2,568.65 vs Rs 2,447.04 lakh) and fell -4.2% against H1 (Rs 2,681.93 lakh). H2 PAT fell -1.3% YoY (Rs 421.50 vs Rs 426.89 lakh). Management cited full-year figures only, and the CFO called the year "consistent improvement". Full-year revenue growth (16.07%) was never stated as a percentage. No analyst asked. The >=60% FY27 guidance sits on this slowing base. | Revised consolidated results 25-Aug-2026 p.11 (Revenue line, PAT line); transcript p.4 (Saurabh Verma); AR p.39 (16.07%) | MAJOR |
| I4 | FY27 export guidance of Rs 5-7 Cr is framed without the FY26 base. That base fell from Rs 524.30 lakh to Rs 53.11 lakh (-89.9%). | Transcript p.3-4; AR Note 39(b) FOB table (line 4376-4377); AR Board's Report forex earnings (line 2169) | MAJOR |
| I5 | The RHP and the call disagree on working capital. The RHP working-capital plan (auditor-certified 28-May-2026) assumes FY27 receivable days fall to 80 from 128, a requirement of Rs 2,049.39 lakh, and IPO working capital of Rs 500 lakh. Eight weeks later the call cites 90-120 days on large government projects and does not dispute a Rs 35-40 Cr need. The CMD concedes "the entire requirement is not available today", and the bank lines are unsanctioned. [INFERENCE] The RHP receivables imply FY27 standalone revenue of ~Rs 60 Cr (1,317.50 x 365 / 80). That is below the call's trajectory. | RHP pdf p.125-126 (lines 6971-7008); transcript p.6 | MAJOR |
| I6 | Management says the equipment-heavy Rs 47-50 Cr order will carry a *higher* contribution margin than the reagent business (40-60%). Peer QLINE reports instrument-manufacturing gross margin of 15-20% and domestic traded-instrument margin of 10-15%, and says large instruments are placed at cost. Avience itself says 80-85% of its instruments earn no direct revenue. A peer statement directly contradicts the main company. | Transcript p.7 (Ashwani Agarwal Q, Choudhary A; Choudhary on reagent rental); QLINE 23-Jun-2026 p.12 (Meenal Gupta), p.17 (Ajay Mahanty), p.19 (Y.S. Prabhakara) | MAJOR |
| I7 | The FY27 guidance does not add up internally. A 50:50 mix at >Rs 100 Cr needs ~Rs 50 Cr of manufactured revenue. FY26 manufactured revenue was ~Rs 14.2 Cr (26.99% x Rs 52.51 Cr). The new plant starts only in Oct-2026 at 15-20% utilisation. The order that carries about half of FY27 is equipment-heavy, and high-end equipment is traded (Mindray). [INFERENCE] The mix lands nearer 33-40% unless the order is manufactured goods. Management was not asked to reconcile this. | Transcript p.4 (Mindray sourcing), p.6 (50:50 target; ~Rs 250 Cr capacity), p.7 (26.99%; 15-20%; equipment-heavy order) | MAJOR |
| I8 | Two headline numbers are never reconciled. >=60% growth means ~Rs 84 Cr. >Rs 100 Cr means ~+90%. Rs 52.51 Cr plus Rs 47 Cr is ~Rs 99.5 Cr, so the Rs 100 Cr figure needs a flat base plus the full order in-year. | Transcript p.3, p.5 | MINOR |
| I9 | Consolidated results were revised on 25-Aug-2026, a month after the call. Note 8 says Excel workbook links were removed, so inter-company balances of Rs 337.55 lakh were not eliminated. There is no P&L impact. The AR MD&A sec.6 then asserts that controls "ensure accuracy and reliability of financial reporting". Together with CARO ii(b) and Note 40, this makes three reporting-control errors in the first filing cycle. | Revised CFS p.1 item 3, Note 8 (lines 744-751), auditor para 3 (p.9-10); AR p.65 | MINOR |
| I10 | The Board's Report says the auditor's report has "no qualification, reservation, adverse remark". CARO Annexure 1 lists clause ii(b) against the Holding Company. The note calls the difference "not material". | AR p.50 (line 1494); CARO Annexure 1 (line 4881-4889); Note 47 | MINOR |
| I11 | The RHP set building completion for Jun-2026. The call says "balance work... by September". The Oct-2026 production date is unchanged. | RHP p.131 (line 7285-7289); transcript p.3 | MINOR |
| I12 | The AR MD&A, signed six weeks after the call, has no quantified outlook. It does not mention the order, the growth target or the YEIDA plant. The statutory document omits every number the call gave. | AR Annexure-4 p.63-66 | MINOR |
| I13 | The CMD volunteered the share price on a results call: issue Rs 208, traded ~Rs 414.95, "nearly double". | Transcript p.4 | MINOR |
| I14 | Three soft dodges. (a) The approval success rate was asked and not answered (Praneeth, p.5). (b) FY28 utilisation was asked and the FY27 figure was given (Manav Kothari, p.7). (c) The revenue breakup was deferred offline (p.5) and partly supplied later (p.7). | Transcript p.5, p.7 | MINOR |
| I15 | The CMD says the Uttarakhand order "takes us into a new territory". The RHP shows Uttarakhand standalone revenue of Rs 110.22 lakh (6.78%) in FY24 and Rs 21.74 lakh in 10M FY26. | Transcript p.5; RHP pdf p.160 | MINOR |
| I16 | The RHP strategy and SWOT describe a "WHO and US FDA approved" plant. On the call this becomes "designed with WHO prequalification requirements in mind, subject to audit". US FDA is dropped without comment. | RHP p.210 (line 11412), lines 11325-11366; transcript p.8 | MINOR |
| I17 | The filings and the call describe the plant's scope differently. The CWIP and the YEIDA lease are labelled "Biochemistry Analyser Plant". The call frames the unit as broad capacity worth Rs 250-265 Cr of revenue. | AR Note 13 (line 3711), line 3681; transcript p.6 | MINOR |
| I18 | Peer: GeM L1 bidding has eroded government lab-consumable business. TARSONS says this in two consecutive calls, while Avience's FY27 growth leans on government tenders. | TARSONS Feb-2026 p.12 (Aryan Sehgal), Aug-2026 p.18 (Aryan Sehgal) | MINOR |
| I19 | Peer: the TARSONS plant commissioning date slipped twice in nine months, which bears on Avience's Oct-2026 date. | TARSONS May-2026 p.4-5, Aug-2026 p.7-8 (per B06, spot-confirmed) | MINOR |

19 items listed: 0 CRITICAL, 7 MAJOR, 12 MINOR.

---

## 2. COMPARISON WITH THE PIPELINE (B05, B06)

| # | Status | Pipeline location / gap |
|---|---|---|
| I1 | CAUGHT | B05 4D MAJOR "Unverified flagship order"; B05 flag FLAG-UNVERIFIED-ORDER. |
| I2 | PARTIALLY CAUGHT | B05 3C quotes the working-capital answer but not the "once confirmed orders are in place" clause. B05 never cites the Board's Report "no material commitments" line. Both contradictions strengthen I1, and neither is named. |
| I3 | MISSED | B05 contains no H2 figure. It reads the call as a full-year event, repeats the CFO's framing without challenge, and never sets the ≥60% guidance against a +5.0% H2. |
| I4 | CAUGHT | B05 4D MAJOR "Silent base-year framing"; FLAG-SILENT-BASE. |
| I5 | PARTIALLY CAUGHT | B05 3C grades the working-capital answer "not fully satisfactory" but leaves it off the 4D red-flag list. B05 never compares the call with the RHP's certified 80-day, Rs 2,049.39 lakh plan. Under-weighted. |
| I6 | PARTIALLY CAUGHT | B05 3C calls the margin answer a "bare assertion". B06 Q3 holds QLINE's 15-20% instrument margin but uses it only for the reagent-margin question and never ties it to the order. |
| I7 | MISSED | B05 4A gives the mix trigger conviction L-M with no stated reason. The arithmetic tension between mix, order composition and plant timing is not raised. |
| I8 | PARTIALLY CAUGHT | B05 names the order as "the single largest quantified input" but lists ≥60% and >Rs 100 Cr as separate lines without reconciling them. |
| I9 | MISSED | B05 lists the revised results only as a source. The revision is not flagged. |
| I10 | CAUGHT | B05 4D MINOR; FLAG-DISCLOSURE. |
| I11 | CAUGHT | B05 4D WATCH; timeline_slippages. |
| I12 | PARTIALLY CAUGHT | B05 1B/2B call the MD&A "generic" but do not flag the call-vs-statute gap. |
| I13 | MISSED | Not mentioned. |
| I14 | MISSED | B05 2C says management "answered every question asked (no visible deflection)". The transcript does not support that. |
| I15 | MISSED | B05 1A repeats "new territory" without challenge. |
| I16 | MISSED | Not mentioned. |
| I17 | MISSED | Not mentioned. |
| I18 | CAUGHT | B06 2E (Aug call). The Feb-2026 repetition is not cited, but the finding is held. |
| I19 | CAUGHT | B06 Q4 and analyst_note. |

Totals: CAUGHT 6, PARTIALLY CAUGHT 5, MISSED 8.

### Pipeline red flags I did not raise independently
None. I found every B05 red flag (two MAJOR, one MINOR, one WATCH) on my own read. B06 raises no flags. Checks on the pipeline flags:
- FLAG-UNVERIFIED-ORDER: SUPPORTED. No order filing exists in the announcements folder, and the AR has no order reference.
- FLAG-SILENT-BASE: SUPPORTED. AR Note 39(b) shows Rs 53.11 vs Rs 524.30 lakh, and the transcript never mentions the base.
- FLAG-DISCLOSURE: SUPPORTED. The CARO Annexure 1 table lists ii(b) against the Holding Company. The MINOR grade is right because the differences are "not material" (Note 47).
- WATCH slippage: SUPPORTED. RHP line 7285 vs transcript p.3.

pipeline_flags_not_supported: none.

### Pipeline statements that overreach (not red flags, logged as MINOR)
- B05 2C says management "answered every question asked (no visible deflection)". NOT SUPPORTED; see I14.
- B05 2A row 2 calls FY26 CWIP additions (Rs 823.37 lakh) "directionally consistent" with the net-proceeds tranche (Rs 1,595.53 lakh, up to FY2026-27). The IPO closed in Jun-2026, which is FY27. FY26 spend was funded before the IPO and cannot evidence use of the proceeds. This is a period mismatch.
- The B06 Q2 table describes QLINE receivables as "~134 trending toward 90-120" in one cell and "120-150-day range" in another. The transcript supports both figures (134 for FY26 at p.12; "currently 120 to 150"; target "within 90 to 120" at p.13). The cells need reconciling. Cosmetic.

---

## 3. PROMISE-DELIVERY SPOT CHECKS (B05 2A)

| # | B05 row | Earlier promise present? | Later outcome as stated? | Verdict |
|---|---|---|---|---|
| 1 | RHP YEIDA schedule: building complete Jun-2026, production Oct-2026 → PARTIAL / IN PROGRESS | Yes. RHP p.131 line 7285 (Jul-2024 to Jun-2026) and line 7289 (Commencement of Operation Oct-2026). | Yes. Transcript p.3: "balance work... by September and manufacturing targeted to commence from October". | CONFIRMED |
| 2 | CWIP Rs 461.91 → Rs 1,285.28 lakh, Rs 823.37 lakh added, nothing capitalised, Note 13.2 "not overdue" | Not applicable (AR fact) | Yes. AR line 3711 (461.91 / 823.37 / 1,285.28, zero capitalised); line 3737 (13.2). | CONFIRMED |
| 3 | Board's Report: IPO proceeds used "no material deviation" → ASSERTED, NOT VERIFIABLE | Yes. AR p.39, lines 1008-1010. | No object-wise table in the AR, which I confirmed. The direction is right. The supporting "directionally consistent" comparison has a period mismatch (see above). | CONFIRMED (direction) |
| 4 | Rs 47 Cr order → UNVERIFIABLE | Yes. Transcript p.3 and p.5. | No order filing among the 10 announcement files; no AR mention. I did not independently count B00's "18 filings". | CONFIRMED |
| 5 | FY27 guidance → UNTESTED | Yes. Transcript p.3-7. | No H1 FY27 print is in the corpus. SME half-yearly results are due by Nov-2026, after the run date. | CONFIRMED |

Checked 5, confirmed 5, wrong 0.

---

## 4. CREDIBILITY GRADE

B05 grade: C. **Concur.** NO-CONCALL MODE sets C as the default, and no guidance has reached a test date. Two items I found (I2, I3) push toward the low end of C, not toward a different grade. First, the call's own wording undercuts "order in hand". Second, management framed a half with +5.0% revenue and -1.3% PAT as "consistent improvement". Neither is a delivery failure yet. Both are framing failures, and the H1 FY27 print should be read with them in mind.

---

## 5. CONSOLIDATED FINDINGS

| Severity | Location | Finding | Anchor |
|---|---|---|---|
| MAJOR | B05 2A/2D/4D | MISSED: H2 FY26 slowdown (revenue +5.0% YoY, -4.2% vs H1; PAT -1.3% YoY) is absent from the analysis. The call presented full-year numbers only. | Revised CFS p.11; transcript p.4 |
| MAJOR | B05 1B / 4A trigger 3 | MISSED: the 50:50 mix, >Rs 100 Cr revenue, an equipment-heavy order and an Oct-2026 plant start do not reconcile [INFERENCE] | Transcript p.4, p.6-7 |
| MINOR | B05 3C/4D | PARTIAL: "in hand" vs "once confirmed orders are in place"; Board's Report "no material commitments" not used | Transcript p.3/5/6; AR p.39-40 |
| MINOR | B05 3C | PARTIAL: RHP certified working-capital plan (80 days, Rs 2,049.39 lakh) vs call (90-120 days, "not available today"). Off the red-flag list. | RHP p.125-126; transcript p.6 |
| MINOR | B05 3C / B06 Q3 | PARTIAL: QLINE instrument margins (15-20% manufactured, 10-15% traded) contradict the "higher margin" claim on the order. Not linked. | QLINE p.12, p.17, p.19; transcript p.7 |
| MINOR | B05 1B | PARTIAL: ≥60% vs >Rs 100 Cr not reconciled | Transcript p.3, p.5 |
| MINOR | B05 1A/2B | PARTIAL: AR MD&A carries none of the call's numbers; gap not flagged | AR p.63-66 |
| MINOR | B05 2A row 2 | Period mismatch in the IPO-utilisation support | AR Note 13; RHP p.130 |
| MINOR | B05 2C | "Answered every question asked" not supported | Transcript p.5, p.7 |
| MINOR | B05 | MISSED: 25-Aug-2026 consolidated results revision (Rs 337.55 lakh elimination error) | Revised CFS Note 8 |
| MINOR | B05 | MISSED: CMD share-price remark | Transcript p.4 |
| MINOR | B05 1A | MISSED: "new territory" contradicted by RHP Uttarakhand revenue | RHP p.160; transcript p.5 |
| MINOR | B05 3B | MISSED: US FDA plant claim (RHP) dropped on call | RHP p.210; transcript p.8 |
| MINOR | B05 | MISSED: Biochemistry Analyser Plant label vs broad-capacity framing | AR Note 13; transcript p.6 |
| MINOR | B06 Q2 | Internal inconsistency in how QLINE receivable days are described | QLINE p.12-13 |

CRITICAL 0, MAJOR 2, MINOR 13.

Scoring: 7 items are material (all MAJOR, none CRITICAL). The pipeline had 5 of them: 2 CAUGHT (I1, I4) and 3 PARTIALLY CAUGHT (I2, I5, I6). It missed 2 (I3, I7). The rate is 5/7 = 71.4%, counting a partial catch as "found" per rule 3's definition. The strict rate, counting full catches only, is 2/7 = 28.6%, and it is disclosed for the orchestrator. The denominator is 4 or more, so rule 7 does not null the rate.

Recommended stage 5 patch (a note for the orchestrator, not a REWORK trigger on its own): add the H2 FY26 half-on-half and YoY figures to B05 2D and 4D. Add the mix-arithmetic tension to trigger 3. Add the RHP working-capital plan comparison and the "confirmed orders" clause to the order flag.

```yaml
stage: B12b
company: "AVIENCE"
run_date: "2026-09-26"
model: "claude-opus-5-5"
status: complete
no_concall_mode: true
independent_flags_found: 19
caught: 6
partially_caught: 5
missed:
  - {severity: "MAJOR", item: "H2 FY26 revenue +5.0% YoY (Rs 2,568.65 vs 2,447.04 lakh), -4.2% vs H1; H2 PAT -1.3% YoY (Rs 421.50 vs 426.89 lakh); call cited full-year only, CFO 'consistent improvement'; absent from B05", anchor: "Revised consolidated results 25-Aug-2026 p.11; transcript p.4; AR p.39"}
  - {severity: "MAJOR", item: "50:50 mix at >Rs 100 Cr needs ~Rs 50 Cr manufactured vs FY26 ~Rs 14.2 Cr; plant starts Oct-2026 at 15-20%; order is equipment-heavy and high-end equipment is traded [INFERENCE: mix nearer 33-40%]; not flagged", anchor: "Transcript p.4, p.6, p.7"}
  - {severity: "MINOR", item: "Consolidated results revised 25-Aug-2026 (Rs 337.55 lakh inter-company elimination error) vs MD&A internal-control assertion", anchor: "Revised CFS Note 8; AR p.65"}
  - {severity: "MINOR", item: "CMD volunteered share price (Rs 208 issue, ~Rs 414.95)", anchor: "Transcript p.4"}
  - {severity: "MINOR", item: "Soft dodges: approval success rate, FY28 utilisation, revenue breakup deferred; B05 says 'answered every question'", anchor: "Transcript p.5, p.7"}
  - {severity: "MINOR", item: "Uttarakhand 'new territory' vs RHP Uttarakhand revenue Rs 110.22 lakh FY24", anchor: "Transcript p.5; RHP p.160"}
  - {severity: "MINOR", item: "RHP 'WHO and US FDA approved' plant narrowed on call to WHO PQ design intent", anchor: "RHP p.210; transcript p.8"}
  - {severity: "MINOR", item: "CWIP/lease labelled Biochemistry Analyser Plant vs broad Rs 250-265 Cr capacity framing", anchor: "AR Note 13; transcript p.6"}
pipeline_flags_not_supported: []
promise_delivery_spot_checks: {checked: 5, confirmed: 5, wrong: 0}
credibility_grade_concur: "concur - C holds; the undisclosed H2 slowdown and the order/'confirmed orders' contradiction argue for low-C, but no delivery has been tested yet"
findings:
  - {severity: "MAJOR", location: "B05 2A/2D/4D", item: "MISSED H2 FY26 slowdown", anchor: "Revised CFS p.11; transcript p.4"}
  - {severity: "MAJOR", location: "B05 1B/4A", item: "MISSED mix/revenue/order/plant-timing arithmetic tension [INFERENCE]", anchor: "Transcript p.4, p.6-7"}
  - {severity: "MINOR", location: "B05 3C/4D", item: "PARTIAL: 'in hand' vs 'once confirmed orders are in place'; Board's Report 'no material commitments'", anchor: "Transcript p.3/5/6; AR p.39-40"}
  - {severity: "MINOR", location: "B05 3C", item: "PARTIAL: RHP certified WC plan (80 days, Rs 2,049.39 lakh) vs call (90-120 days, 'not available today')", anchor: "RHP p.125-126; transcript p.6"}
  - {severity: "MINOR", location: "B05 3C / B06 Q3", item: "PARTIAL: QLINE instrument margins contradict 'higher margin' on order; not linked", anchor: "QLINE p.12, p.17, p.19; transcript p.7"}
  - {severity: "MINOR", location: "B05 1B", item: "PARTIAL: >=60% vs >Rs 100 Cr not reconciled", anchor: "Transcript p.3, p.5"}
  - {severity: "MINOR", location: "B05 1A/2B", item: "PARTIAL: AR MD&A carries none of the call's numbers", anchor: "AR p.63-66"}
  - {severity: "MINOR", location: "B05 2A row 2", item: "Period mismatch in IPO-utilisation support", anchor: "AR Note 13; RHP p.130"}
  - {severity: "MINOR", location: "B05 2C", item: "'Answered every question asked' not supported", anchor: "Transcript p.5, p.7"}
  - {severity: "MINOR", location: "B05", item: "MISSED results revision 25-Aug-2026", anchor: "Revised CFS Note 8"}
  - {severity: "MINOR", location: "B05", item: "MISSED CMD share-price remark", anchor: "Transcript p.4"}
  - {severity: "MINOR", location: "B05 1A", item: "MISSED 'new territory' contradiction", anchor: "RHP p.160; transcript p.5"}
  - {severity: "MINOR", location: "B05 3B", item: "MISSED US FDA claim dropped", anchor: "RHP p.210; transcript p.8"}
  - {severity: "MINOR", location: "B05", item: "MISSED plant-scope labelling difference", anchor: "AR Note 13; transcript p.6"}
  - {severity: "MINOR", location: "B06 Q2", item: "QLINE receivable-day description inconsistent across cells", anchor: "QLINE p.12-13"}
critical_count: 0
major_count: 2
minor_count: 13
material_found: 7
material_caught: 5
acceptance_rate: 71
coverage_basis: "7 material (0 CRITICAL, 7 MAJOR) of 19 listed; 2 CAUGHT + 3 PARTIALLY CAUGHT = 5 the pipeline had, 2 MISSED. Rate 5/7 = 71.4%. Strict rate excluding partials 2/7 = 28.6%. Denominator >= 4, rule 7 does not null. No CRITICAL possible from repeated-evasion test with one transcript."
```
