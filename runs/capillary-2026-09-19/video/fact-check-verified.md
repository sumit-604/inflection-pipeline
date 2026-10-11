# Capillary video: fact check against the run corpus

Run folder: runs/capillary-2026-09-19. Checked 11-Oct-2026. Page numbers are the `[page N]` markers
in the extracted `.txt` files (PDF page, not the printed page).
Tolerance: a figure that differs by more than 5% is corrected in the script. None did.

## Section 5, item 1: scene 11 placeholders and cross-check

Source: `outputs/final/scenario-rebuild-page64.md` (commit 60d653a8), BASE case table.
Script: `fill_scene11.py` (exit code 2 stops the build; it passed).

| Item | Value | Source |
|---|---|---|
| REV27 | 1,065 | base total revenue 1,065.0 |
| REV28 | 1,120 | base total revenue 1,119.9, rounded to nearest crore |
| REV29 | 1,190 | base total revenue 1,190.0 |
| REV30 | 1,324 | base total revenue 1,323.5, rounded (matches the job's 1,324) |
| M27 / M28 / M29 | 16.2% / 21.8% / 27.0% | EBITDA 172 / 244 / 321 divided by the rounded revenue |
| PM27 / PM28 / PM29 | 4.8% / 9.0% / 12.9% | operating PAT 51 / 101 / 154 divided by the rounded revenue |
| FY30 margins in the job | 30.6% / 16.0% | 405/1,324 = 30.59%; 212/1,324 = 16.01% |

All 24 EBITDA and PAT figures (3 cases x 4 years x 2 lines) are within 1% of the file. The largest gap is bear FY27 PAT:
job 43, file 42.6 (0.94%).

| Case | EBITDA, job vs file | PAT, job vs file |
|---|---|---|
| Bear | 161/195/230/268 vs 160.8/194.8/230.4/267.7 | 43/64/86/109 vs 42.6/63.6/85.8/109.3 |
| Base | 172/244/321/405 vs 172.0/244.0/321.3/404.7 | 51/101/154/212 vs 51.0/100.5/154.0/212.0 |
| Bull | 186/303/431/512 vs 186.0/302.6/430.6/512.2 | 62/144/236/293 vs 61.5/144.5/236.0/292.6 |

## Section 5, item 2: LINE 7.4

Question: did reported PAT for the June 2026 quarter show a loss?
Answer: YES. Used the loss wording:
"The headline result for that quarter showed a loss, because of a one-off fraud charge. The operating line kept rising."

Evidence:
- Q1 FY27 results (`inputs/results/Results-Q1FY27-20260804.txt`), page 9, consolidated statement, line X
  "(Loss)/ profit after tax": quarter ended 30-Jun-26 = (95.52) million rupees. Profit before tax (VIII) = (85.88).
- Exceptional item 333.86 million rupees (page 11 note: cyber-enabled banking fraud at the Czech step-down subsidiary).
- Q1 FY27 investor presentation (`inputs/presentation/20260804-Investor-Presentation-30pp.txt`), page 13:
  "Profit After Tax (PAT) ₹ (95.5)* Mn, -4% margin" with the footnote naming the 333.9 Mn exceptional loss.
- The standalone statement (page 4) shows a profit of 77.65 million rupees. The group result is the headline, so it governs.

## Section 5, item 3: script claims against the corpus

| # | Claim in script | Verdict | Passage and page |
|---|---|---|---|
| 1 | Contract length 3 to 7 years | CONFIRMED | Annual Report FY26, page 76: "Capillary sales long-term subscription contracts, typically running 3–7 years with many renewing them subsequently" (sic, "sales") |
| 2 | About 9 integrations per customer | CONFIRMED | Annual Report FY26, page 79: "an average of approximately nine integrations per enterprise customer". Also Feb-2026 call transcript, page 5: "on an average there's about 9 integrations in a customer" |
| 3 | Churn about 5% a year | CONFIRMED (spoken) with a note | Aug-2026 call transcript, page 12. Asked the churn rate inside NRR, the CFO says: "About 5%-ish." The UDRHP-I (Jun-2025, page 170 and 260) gives 5.98%, 5.61% and 9.68% for FY25, FY24 and FY23. 5.98% differs from 5% by more than 5% in relative terms, so the script uses the latest figure, management's FY27 call statement. Operator may prefer "about six in a hundred" for FY25; the script keeps "five" |
| 4 | Optum contract ends in early 2029 | NOT CONFIRMED FROM A FILED PAGE | The corpus has no filed page that states the Optum contract end date. The red herring prospectus (Nov-2025) is not in the corpus: `inputs/prospectus/` holds only the UDRHP-I of Jun-2025. The only support is secondary: `inputs/research/web-handover-dossier.md` line 49 and `outputs/expectation-ledger.md` row D3 use "not renewed by Mar-2029" as the confirm-by date. The dossier sources the Optum figures to "RHP pp.71-73" and the sibling reports mark them "not in corpus". Script wording kept as written. Needs the RHP to close |
| 5 | FY26 cash from operations / adjusted EBITDA about 1.4 | CONFIRMED | Q4 FY26 investor presentation (`inputs/other/20260506-Investor-Presentation-Q4FY26.txt`), page 16: "OCF / Adj. EBITDA 140%". Arithmetic: OCF 1,499.1 million / adjusted EBITDA 1,069 million = 1.402. Annual Report page 82 gives the OCF; May-2026 deck page 58 gives "FCF ₹1,106 Mn vs EBITDA ₹1,069 Mn" |
| 6 | Q1 FY27 revenue growth above 40% | CONFIRMED | Q1 FY27 results page 9: revenue from operations 2,566.44 vs 1,798.93 million = +42.7%. Q1 FY27 deck page 13: "Revenue from Operations ₹2,566.4 Mn, 43% YoY" |

## Other checks done on the way

- Scene 3 source line "contract liabilities, p.233": Annual Report FY26 page 233 carries "Contract liabilities - Deferred revenue (refer Note 20) 770.99 / 680.74" (million rupees). Confirmed.
- Scene 10 fraud loss about 33 crore: 333.86 million rupees = ₹33.4 crore. Confirmed (Q1 FY27 results, page 11).
- Scene 10 KPMG forensic review: BSE filing `inputs/announcements/20260731-17c4e00c-...txt` names "KPMG Assurance and Consulting Services LLP" as forensic auditor. Confirmed.
- Scene 4 warrant discount (₹21 crore this year, ₹31 crore after): in the dossier (Section 2) as "Warrant charge FY27 Rs 20.6 Cr, FY28-29 about Rs 31 Cr a year [FILED, RHP pp.71-73]". Secondary only, RHP not in corpus. Same gap as row 4 above. Optum revenue 11.9 and 98.9 crore (FY24, FY25) is also dossier-only.
- Scenes 7 and 8 numbers (0.6, 0.7, 7.4, 12.5, 20.3; 1.5%, 3.9%, 13.6%; core 11-13%) are Keerti Sharma's calculations named in the job. Not re-derived here.
- The scene 6 Q1 FY27 deck (page 15) reports organic revenue growth of 17%. The video's 11-13% is the job's estimate with Optum and currency removed, so the two do not clash.
