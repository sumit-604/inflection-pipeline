# VERIFIER D: PEER COVERAGE AUDIT — SHHARICH (Shree Hari Chemicals Export Ltd)

Run date: 2026-09-05. Model: claude-sonnet-5. Inputs: 9 peer transcript files (BODALCHEM x4,
SHREEPUSHK x4, AKSHARCHEM x1, all under runs/shharich-2026-09-05/work/), B06_REPORT
(outputs/reports/06-peers.md), B05_PEER_QUESTIONS (outputs/blocks/B05-peer-questions.yaml).
Every transcript was read in full against every citation B06 attributes to it. Note per task: the
main company holds no earnings calls; this has no bearing on the audit, which tests only whether
B06 actually used the 9 peer files it says it used.

---

## PART 1: COVERAGE AUDIT TABLE (per peer_coverage_map row)

| # | Peer / Quarter | B06 usage tag | Citations checked | Result |
|---|---|---|---|---|
| 1 | BODALCHEM Q2 FY25 (Nov-2024) | SUBSTANTIVE | H-Acid Rs444/Vinyl Sulphone Rs228 (p.5); "growth...led by improvement in volumes...majorly by intermediates" (p.4) | CONFIRMED. Both citations exact-match the transcript at the cited page. |
| 2 | BODALCHEM Q3 FY25 (Feb-2025) | SUBSTANTIVE | H-Acid Rs490/VS Rs242 (p.5); raw-material basket "Sulfur, Aniline oil, Naphthalene, Soda ash, Caustic soda, Coal" (p.13); "we are not presently considering any raising of equity" (p.8); cancelled warrant/preferential deal (p.14); competitors named incl. AksharChem/Shree Pushkar/Kiri (p.15); demand-normalization "more than 6 months back" (p.18-19); "almost 90% utilization" + "considering near to peak utilization" (cited p.4-5 and p.11-12); ZLD "no risk or any issues...any manufacturing activity" (p.12) | MOSTLY CONFIRMED, one MAJOR anchor defect. "Considering near to peak utilization" is correctly on p.5. But "almost 90% utilization" (Ankit Patel) is actually on **p.8**, not p.11-12 as cited; p.11-12 in this transcript discusses power-cost optimization and the ZLD/environmental question, unrelated content. All other citations in this row check out exactly (p.8, p.12, p.13, p.14, p.15, p.18-19 all confirmed verbatim). See Finding F1. |
| 3 | BODALCHEM Q4 FY25 (May-2025) | SUBSTANTIVE | H-Acid Rs508/VS Rs255 (p.5); sulphur Rs18-20k->25-27k/ton, "prices like this don't happen for few years" (p.10); sulphuric acid Rs8k->13k/ton (p.10-11); "we don't plan to do any major CAPEX at the moment" (p.14); anti-dumping duty on TCCA "implemented since 7th March 2025...from China" (cited p.1 and p.3) | MOSTLY CONFIRMED, one MAJOR anchor defect. The ADD/TCCA quote — the evidentiary basis for the single most consequential finding in the whole stage (Q2 CONTRADICTED) — is actually on **p.4** (Ankit Patel's opening remarks), not p.1 (BSE cover letter, unrelated) or p.3 (management-names page, unrelated). All other citations in this row (p.5, p.10, p.10-11, p.14) check out exactly. See Finding F2. |
| 4 | BODALCHEM Q1 FY26 (Aug-2025) | SUBSTANTIVE | H-Acid Rs503/VS Rs247, "turnover and margin remained similar QoQ" (p.4-5); Dye Intermediates degrowth on lower aniline oil/ethylene (p.4); sulphur ~27k, sulphuric ~12k "same range" (p.8-9); export 22% of revenue, US "hardly 1%" (p.9) | CONFIRMED. All four citations exact-match. |
| 5 | SHREEPUSHK Q2 FY26 (Nov-2025) | SUBSTANTIVE | Rs30cr promoter preferential for Unit-8 (cited p.7); chemicals 65%/fertiliser 70% utilization (p.10); "majority of our sales is for the export business not for the domestic business" (cited p.10); ten-year promoter-only-dilution pattern, "creeping or preferential," never selling (cited p.11) | MOSTLY CONFIRMED, three MINOR anchor defects (systematic, same document). The Rs30cr-preferential quote is actually on **p.8** (cited p.7); the export-mix quote is actually on **p.11** (cited p.10); the ten-year-promoter quote is actually on **p.12** (cited p.11). Each is off by exactly one page in the same direction. Cross-checking the printed in-document page numbers (e.g., PDF marker p.8 carries the printed footer "Page 7 of 16") shows the cited numbers match the document's own printed footer, not the "=== PAGE n ===" PDF-marker convention the task specifies as authoritative. The 65%/70% utilization citation (p.10) is correctly anchored to the PDF marker, so the convention is applied inconsistently even within this one file. See Finding F3. |
| 6 | SHREEPUSHK Q3 FY26 (Feb-2026) | SUBSTANTIVE | Gross margin 35.7%->31.9% YoY (p.5); sulphur $283-284->$560/tonne, sulphuric acid Rs9-10k->18k/ton (p.5-6); China VAT-refund withdrawal, India net-exporting H-Acid, "non-competitive" (p.7-8); Bangladesh ~7-8% of revenue (p.8); third preferential allotment, "underscoring the promoter[']s continu[ed] confidence" (opening remarks, p.3-4) | CONFIRMED. All five citations exact-match, including the bracketed grammatical repair of the quote, which is a fair rendering of the transcript's rougher original wording ("underscoring the promoter continuation confidence"). |
| 7 | SHREEPUSHK Q4 FY26 (May-2026) | SUBSTANTIVE | H-Acid Rs525-530 recalled Feb/early-Mar (p.9); H-Acid "easily" Rs750/kg, VS Rs240->Rs350/kg (p.9); ammonia Rs40-42->Rs100+/kg, sulphur Rs30->Rs100/kg, "almost 3x" (p.5-6); "practically stopped our sales" mid-March, Kharif season foregone (p.6-7) | CONFIRMED. All four citations exact-match. |
| 8 | SHREEPUSHK Q1 FY27 (Aug-2026) | SUBSTANTIVE | K-Acid Rs550->Rs700+ (p.13); chemical volume -38.6% YoY (9,113 vs 14,837 MT) vs revenue +17.1% YoY (opening remarks, p.3-4); "when you get value, volume and value won't go together. First, you need value, then volume" (p.13); advance-payment-input/credit-sale-output WC mechanism (p.12); "we have plenty of inquiries...China is giving orders back to India" (cited as one Punit Makharia quote, p.13) | MOSTLY CONFIRMED, two MINOR quotation-mechanics defects. The K-Acid price figure, the volume/revenue split, the "value, then volume" quote, and the WC mechanism are all exact-match at the cited pages, correctly attributed. But (a) the phrase "in the last 15-20 days" (used elsewhere in the report to date the K-Acid move) was actually spoken by analyst Prit Nagersheth, not Punit Makharia; and (b) the spliced quote "we have plenty of inquiries...China is giving orders back to India" merges a genuine Makharia sentence ("We have plenty of inquiries for K-acid, H-acid, and Vinyl Sulphone to China") with a phrase spoken by analyst Prit Nagersheth ("China is giving orders back to India"), presented via ellipsis as one continuous management quote. Both fragments are on the correct page (p.13) and the underlying claim (active Chinese buying interest returning) is independently supported by both speakers, but the splice misattributes analyst commentary as management's own words. See Finding F4/F5. |
| 9 | AKSHARCHEM (Aug-2019 investor presentation) | UNUSED | N/A — B06 states no fact from this file was used in any verdict | CORRECTLY CLASSIFIED. Confirmed by direct read: this is a 31-slide investor-presentation deck (not a transcript) covering Q1 FY20 results, dated August 2019, seven years stale relative to the 2026-09-05 run date. B06's classification (UNUSED, with the staleness reason stated in the coverage map and Part 3) is exactly the treatment Verifier D's brief requires ("marked UNUSED or CITED-ONLY... never SUBSTANTIVE"). One MINOR spot-read finding: the deck does carry a quantified, on-point metric — "Annual Pollution treatment expenses as a % of Revenue," 4.4%-5.7% across FY15-FY19 (slide/PDF p.19) — that is at least topically responsive to Q8 (ZLD/environmental compliance cost trend). Given the metric is six-to-ten years stale and pre-dates the current transition thesis by a wide margin, treating it as UNUSED rather than CITED-ONLY is a defensible call, not a material miss; noted for completeness as an industry-context item left on the table. See Finding F6. |

**Coverage summary:** 9 of 9 coverage-map rows classified correctly at the usage-tag level (8 SUBSTANTIVE, 1 UNUSED, no SUBSTANTIVE-without-real-content found anywhere). 2 of the 9 rows carry a MAJOR anchor-location defect (Finding F1, F2); 2 rows carry MINOR anchor/attribution defects (Finding F3 covers 3 instances in one row; F4/F5 cover 2 instances in one row); 1 row carries a MINOR spot-read miss (F6). No fabricated citation was found anywhere: every quote B06 attributes to a transcript is genuinely present in that transcript, in every case I checked, sometimes at a different page than stated.

---

## PART 2: VERDICT-DISCIPLINE AUDIT (per claim, B05 Q1-Q10)

| Claim | B06 verdict | Peers backing it | Independent-anchor check | Discipline result |
|---|---|---|---|---|
| Q1 H-Acid price/spread trend | VERIFIED | BODALCHEM (4 transcripts) + SHREEPUSHK (4 transcripts), anchor_count 8 | Confirmed: 4 independent BODALCHEM price points (Rs444/490/508/503) + 3 independent SHREEPUSHK price points (Rs525-530/750; K-Acid 550/700+) all directly verified in transcript | PASS. Two genuinely independent peers, well over the 2-anchor floor. Not upgraded from silence. |
| Q2 Chinese competition/ADD | CONTRADICTED | SHREEPUSHK (VAT-refund/export-reversal evidence) + BODALCHEM (TCCA-only ADD, no H-Acid ADD found) | Confirmed: SHREEPUSHK p.7-8 (verified exact), BODALCHEM p.4 (content verified, though cited at wrong pages, see F2) | PASS on substance. The CONTRADICTED verdict itself is well-supported by transcript content; the citation-location defect in F2 does not change the underlying finding but should be corrected. |
| Q3 export-mix step-change | UNVERIFIABLE | Both peers checked, neither gives comparable figure | Confirmed: BODALCHEM 22% export/US~1% (p.9, exact); SHREEPUSHK qualitative-only export statement (actual p.11, cited p.10 — F3) | PASS. Correctly labelled UNVERIFIABLE rather than stretched into a verdict the evidence doesn't support. |
| Q4 raw-material cost trend | VERIFIED (sulphur/sulphuric chain); naphthalene partial | BODALCHEM (4 transcripts) + SHREEPUSHK (3 transcripts), anchor_count 7 | Confirmed: sulphur/sulphuric numbers verified across Q3 FY25, Q4 FY25, Q1 FY26 (BODALCHEM) and Q3 FY26, Q4 FY26, Q1 FY27 (SHREEPUSHK) | PASS. Two independent peers, hedged appropriately on the naphthalene leg (correctly not oversold to VERIFIED). |
| Q5 capacity/utilization | PARTIALLY VERIFIED | Both peers | Confirmed directionally; BODALCHEM near-peak (90%, p.8) vs SHREEPUSHK headroom (65%, p.10) — genuinely mixed signal, verdict matches evidence | PASS on substance; carries Finding F1 (anchor location for the 90% figure). |
| Q6 margin range/driver | PARTIALLY VERIFIED | Both peers | Confirmed: BODALCHEM margin band 8.6%-11.6% and SHREEPUSHK band 8.9%-11.4%, both above SHHARICH's 5.31-8.13%; driver split (volume-led then price-led) matches transcript language in both calls | PASS. |
| Q7 working-capital norms | UNVERIFIABLE | Both peers checked; no quantified WC-days found | Confirmed no peer discloses receivable/payable/inventory days; the one qualitative WC-mechanism quote (SHREEPUSHK p.12) verified exact | PASS. Correctly UNVERIFIABLE, not stretched. |
| Q8 ZLD/compliance cost | UNVERIFIABLE | Both peers checked | Confirmed BODALCHEM's ZLD framing (p.12, exact) and SHREEPUSHK's "zero waste" framing, neither gives a cost trend | PASS. Also correctly excludes the stale AKSHARCHEM figure (F6) rather than smuggling seven-year-old data into a current-period verdict — a defensible discipline call. |
| Q9 volume-vs-price regime (load-bearing) | VERIFIED, regime split | BODALCHEM (volume-led phase) + SHREEPUSHK (price-led phase), anchor_count 6 | Confirmed: BODALCHEM "growth...led by improvement in volumes" (p.4, Q2 FY25, exact) and near-90% utilization; SHREEPUSHK -38.6% volume/+17.1% revenue (p.3-4, exact) and "first you need value, then volume" (p.13, exact) | PASS. Two independent peers each carrying genuine, load-bearing numeric anchors. The verdict is explicitly and appropriately hedged in the Net Read ("does not prove... but removes benefit of the doubt") — this is correct calibration, not an upgrade from silence. |
| Q10 promoter preferential warrants | PARTIALLY VERIFIED | SHREEPUSHK (pattern, 3 rounds) + BODALCHEM (contrary case: cancelled/avoided) | Confirmed: SHREEPUSHK's three rounds verified (p.8 [cited p.7, F3], p.3-4 exact, and the ten-year-pattern quote at p.12 [cited p.11, F3]); BODALCHEM's cancelled-deal quote verified exact at p.14 | PASS on substance; carries Finding F3 (three page-citation defects in the same transcript). |

**Discipline summary:** All 10 B05 claims received a verdict (claims_all_addressed = true; no skipped claim). Every VERIFIED claim (Q1, Q4, Q9) rests on two genuinely independent peers with multiple corroborating anchors each — none rests on a single peer, none is an upgrade from silence. No verdict is more confident than its evidence; UNVERIFIABLE and PARTIALLY VERIFIED calls are used correctly where evidence is thin or mixed rather than being stretched into VERIFIED. This is the core finding of the audit: B06's verdict discipline is sound. The defects found are anchor-location and quotation-mechanics problems (Findings F1-F6), not verdict-inflation problems.

---

## FINDINGS

| ID | Severity | Location | Issue | Detail |
|---|---|---|---|---|
| F1 | MAJOR | B06 Part 1 Q5 / Part 3 coverage map (BODALCHEM Q3 FY25 row) | Anchor-location error | "Almost 90% utilization" (Ankit Patel) cited at "p.4-5 and p.11-12"; actual location is PDF marker p.8. Pages 11-12 of this transcript discuss power-cost optimization and the ZLD/environmental question — unrelated content. The "considering near to peak utilization" phrase in the same sentence is correctly on p.5. Quote is genuine and exists in the transcript; the specific page cited for the numeric claim does not contain it. |
| F2 | MAJOR | B06 Part 1 Q2 / Part 4 (BODALCHEM Q4 FY25 row) | Anchor-location error on the flagship finding | The ADD/TCCA quote ("anti-dumping duty has been implemented since 7th March 2025...from China") is the evidentiary basis for Q2's CONTRADICTED verdict, flagged in B06 as "the single most consequential contradiction" in the stage. It is cited at "p.1 and p.3"; actual location is PDF marker p.4 (Ankit Patel's opening remarks). p.1 is the BSE/NSE cover letter and p.3 is the management-names page — neither contains any ADD content. Quote is genuine and accurately reproduced at p.4; the cited pages are wrong. |
| F3 | MINOR (x3, same row) | B06 Part 1 Q3/Q10 / Part 3 coverage map (SHREEPUSHK Q2 FY26 row) | Systematic off-by-one anchor pattern | Three citations in this row are each off by exactly one page: Rs30cr promoter preferential cited p.7 (actual p.8); export-mix quote cited p.10 (actual p.11); ten-year-promoter-pattern quote cited p.11 (actual p.12). In each case the cited page number matches this transcript's own printed footer ("Page N of 16"), not the "=== PAGE n ===" PDF-marker convention specified as authoritative for this run. The same row's chemicals/fertiliser utilization citation (p.10) is correctly anchored to the PDF marker, showing the convention was applied inconsistently within one document. |
| F4 | MINOR | B06 Part 3 coverage map (SHREEPUSHK Q1 FY27 row) | Speaker misattribution | The phrase "in the last 15-20 days" (used to date the K-Acid price move) was spoken by analyst Prit Nagersheth, not by Punit Makharia (management), though it is on the correctly-cited page (p.13). |
| F5 | MINOR | B06 Part 1 Q2 (SHREEPUSHK Q1 FY27 row) | Spliced quote across two speakers | "we have plenty of inquiries...China is giving orders back to India" (cited as a single Punit Makharia quote, p.13) merges Makharia's actual sentence ("We have plenty of inquiries for K-acid, H-acid, and Vinyl Sulphone to China") with a phrase spoken by analyst Prit Nagersheth ("China is giving orders back to India") via an ellipsis that reads as one continuous management statement. Both fragments are genuine and on the cited page; the underlying claim (active Chinese buying interest) is independently supported by both speakers, so the substance is not wrong, but the quotation mechanics misattribute analyst language to management. |
| F6 | MINOR | B06 Part 3 coverage map (AKSHARCHEM row) | Industry-context item left unused | The Aug-2019 AksharChem deck (correctly classified UNUSED) contains a quantified, topically-relevant metric for Q8 — pollution-treatment expense at 4.4%-5.7% of revenue, FY15-FY19 (PDF p.19) — that was not mentioned even as a caveated aside. Given the 6-10 year staleness of the figure relative to the FY26/FY27 window, omitting it is defensible rather than a material miss. |
| F7 | MINOR | B06 Part 2, item 2E (BODALCHEM Turkey AS29 cross-read) | Minor range overstatement | B06 states BODALCHEM's Turkey-subsidiary AS29 hyperinflation losses ran "Rs 1.45-2.44cr per quarter across all four calls." The four in-scope quarters (Q2 FY25 through Q1 FY26) actually show Rs1.85cr, Rs1.65cr, Rs2.34cr, Rs1.45cr (range Rs1.45-2.34cr); the Rs2.44cr figure belongs to Q1 FY25, a fifth, out-of-scope quarter mentioned only in passing during the Q2 FY25 call as the prior quarter's figure. Not one of the 10 B05 claims; a background cross-read item. |

No CRITICAL finding. No fabricated citation. No claim skipped. No VERIFIED verdict resting on fewer than two independent peers. No verdict upgraded from silence.

---

## OVERALL ASSESSMENT

B06's peer-verification substance is sound: all 10 injected claims received an appropriately
calibrated verdict, the three VERIFIED claims each rest on two genuinely independent,
multiply-anchored peers, and the UNVERIFIABLE/PARTIALLY VERIFIED calls are used correctly
rather than stretched. AKSHARCHEM's stale file is correctly excluded from any substantive
role. The defect pattern that does exist is entirely in citation mechanics — a recurring habit
of citing a transcript's own printed page footer instead of the PDF-marker page specified as
authoritative for this run (F3), two isolated but more consequential anchor misses that land on
pages containing unrelated content (F1, F2), and two quotation-mechanics slips that attribute
analyst language to management via splicing/misattribution (F4, F5). None of these change any
verdict; all affected quotes are genuine and exist in the named transcript. They should be
corrected before this report is treated as a citation-grade source, particularly F2, which anchors
the stage's single most consequential finding.

---

```yaml
stage: B12d
company: "SHHARICH"
run_date: "2026-09-05"
model: claude-sonnet-5
status: complete
peers_audited: 9
substantive_confirmed: 8
substantive_unsupported: []
unused_but_relevant:
  - {peer: "AKSHARCHEM", missed_item: "Quantified pollution-treatment expense as % of revenue (4.4%-5.7%, FY15-FY19), topically responsive to Q8 but 6-10 years stale; correctly left unused rather than material miss", anchor: "AKSHARCHEM Aug-2019 investor presentation, PDF p.19"}
claims_all_addressed: true
verdict_discipline_fails: []
findings:
  - {severity: "MAJOR", location: "B06 Part 1 Q5 / Part 3 (BODALCHEM Q3 FY25 row)", claimed: "'almost 90% utilization' anchored at p.4-5 and p.11-12", source_truth: "quote is genuine but located at PDF marker p.8; p.11-12 covers unrelated power-cost/ZLD content", note: "F1: anchor-location error, quote real but mislocated"}
  - {severity: "MAJOR", location: "B06 Part 1 Q2 / Part 4 (BODALCHEM Q4 FY25 row)", claimed: "ADD/TCCA quote anchored at p.1 and p.3", source_truth: "quote is genuine but located at PDF marker p.4; p.1 is BSE cover letter, p.3 is management-names page", note: "F2: anchor-location error on the flagship CONTRADICTED-verdict citation"}
  - {severity: "MINOR", location: "B06 Part 1 Q10 / Part 3 (SHREEPUSHK Q2 FY26 row)", claimed: "Rs30cr preferential quote anchored p.7", source_truth: "actual PDF marker p.8 (matches transcript's own printed footer, not PDF-marker convention)", note: "F3 instance 1 of 3, systematic off-by-one in this transcript"}
  - {severity: "MINOR", location: "B06 Part 1 Q3 (SHREEPUSHK Q2 FY26 row)", claimed: "export-mix quote anchored p.10", source_truth: "actual PDF marker p.11", note: "F3 instance 2 of 3"}
  - {severity: "MINOR", location: "B06 Part 1 Q10 (SHREEPUSHK Q2 FY26 row)", claimed: "ten-year-promoter-pattern quote anchored p.11", source_truth: "actual PDF marker p.12", note: "F3 instance 3 of 3"}
  - {severity: "MINOR", location: "B06 Part 3 (SHREEPUSHK Q1 FY27 row)", claimed: "'in the last 15-20 days' attributed to Punit Makharia, p.13", source_truth: "phrase spoken by analyst Prit Nagersheth, same page (p.13)", note: "F4: speaker misattribution, page correct"}
  - {severity: "MINOR", location: "B06 Part 1 Q2 (SHREEPUSHK Q1 FY27 row)", claimed: "'we have plenty of inquiries...China is giving orders back to India' as one Punit Makharia quote, p.13", source_truth: "spliced from Makharia's sentence plus a separate analyst (Prit Nagersheth) phrase, same page", note: "F5: two speakers merged into one quote via ellipsis; substance independently supported by both"}
  - {severity: "MINOR", location: "B06 Part 3 (AKSHARCHEM row)", claimed: "UNUSED, no fact used in any verdict", source_truth: "deck does contain a stale (FY15-19) pollution-cost-%-of-revenue figure topically relevant to Q8", note: "F6: defensible omission given 6-10 year staleness, noted for completeness"}
  - {severity: "MINOR", location: "B06 Part 2, item 2E", claimed: "BODALCHEM Turkey AS29 losses 'Rs1.45-2.44cr per quarter across all four calls'", source_truth: "the four in-scope quarters run Rs1.45-2.34cr; Rs2.44cr belongs to a fifth, out-of-scope quarter (Q1 FY25) mentioned only in passing", note: "F7: minor range overstatement, background cross-read item, not one of the 10 B05 claims"}
critical_count: 0
major_count: 2
minor_count: 7
acceptance_rate: 78
```
