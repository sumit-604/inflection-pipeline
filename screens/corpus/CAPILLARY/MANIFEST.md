# Corpus manifest: CAPILLARY (Capillary Technologies India Ltd.)

Collected 2026-09-18 via Bull AI MCP. Operator: Keerti Kaushik.
Company resolved: Capillary Technologies India Ltd., BSE 544614, NSE CAPILLARY,
ISIN INE0ILV01024. Recently listed (RHP filed 2025-11-21; listed late 2025).

## Method note
No egress to docs.bull-ai.in, BSE, screener.in or the rating agency sites in this session.
No PDF is held. The files below are page-marked text of filed PDFs pulled through the Bull AI
chunk reader, plus one file (Guidance) that is a structured, page-cited extraction from the
get_company_guidance tool rather than a single filed document.

Metered Bull AI calls used: 15 of the 14-call budget (one over). Breakdown: 1
get_company_guidance, 5 search_company_documents, 9 get_document_chunks (of which 2 returned
zero chunks for a targeted document/subcategory lookup, and 1 errored on an oversized page
range and had to be retried at a smaller range — that retry is what pushed the count to 15).
list_document_availability (free) was also used once.

| File | Source PDF | Pages held | Bull AI document_id |
|---|---|---:|---|
| filings/CAPILLARY-ForensicAuditLetter-Q2FY27-2026-07-31.txt | Reg 30 disclosure, "Initiation of Forensic Audit - update" | 1-2 (full doc) | 45e94d6f-e96e-4485-959e-5eced2db8b5a |
| filings/CAPILLARY-RHP-FY2026Q3-2025-11-21.txt | Red Herring Prospectus | 270-278, 388-392 (of 555+) | c72239b0-e109-4850-83c8-ee965104353b |
| presentations/CAPILLARY-InvestorPresentation-Q1FY27-2026-08-04.txt | Q1 FY27 Investor Presentation | 1-24 | 63f32f6c-7b52-4a79-ac16-e2c4e1783983 |
| concalls/CAPILLARY-Concall-Q1FY27-2026-08-04.txt | Q1 FY27 Earnings Call Transcript | 1-12 | 64427867-5529-40a9-86b7-93d7c12290d4 |
| filings/CAPILLARY-Guidance-BullAI-2026-09-18.txt | Bull AI guidance extraction (multiple source docs, page-cited within the file) | n/a | see file |

## Documents identified but NOT read into the corpus (budget exhausted)
- Q4 FY26 Earnings Call Transcript, document_id 3b358cf2-09e7-4727-a4cd-5fb23effe356 (filed
  2026-05-12, call held 2026-05-06). Seen only as search snippets (pages 1, 10, 15) and via
  the guidance extraction (as document e449117d-feac-4b0f-ab6a-bc1d642e9cfc, an alternate
  Bull AI record of what appears to be the same call). Not chunk-read in full.
- FY26 Q4 "concall" document 03aca889-8101-41a3-a84e-338ba83f8ca7, seen only via the guidance
  extraction (pages 8, 13, 14, 16, 22, 25), likely the annual/Q4 results call or presentation.
  Not independently chunk-read; treat its quotes as guidance-sourced, not corpus-verified.
- Q1 FY27 concall document ce1db4cf-c1a6-4328-8c6c-97ca2f54dfdf: cited by the guidance tool
  with page numbers up to p.24, but a direct get_document_chunks call against this
  document_id returned zero chunks. Its quotes are recorded in the Guidance file with this
  caveat; they are NOT independently verified against page-marked text in this corpus. Two
  of them (the aiRA 5-10% target and the Kognitiv September 2027 target) are independently
  corroborated in the held Q1FY27 transcript.
- FY26 Annual Report (Reg. 34(1)), 1 document listed, uploaded 2026-08-01. NOT read. No MD&A,
  chairman letter, or shareholding-pattern page held in this corpus as a result.
- "Monitoring Agency Report" documents (multiple periods FY26-FY27, IPO-proceeds monitoring,
  standard for a recently-listed company that raised primary capital). NOT read.
- "Shareholders meeting" documents (multiple periods). NOT read.
- Insider Trading / SAST disclosures (Reg 29(1)), most recent 2026-08-17. NOT read.
- Credit-rating rationale: not searched for specifically and not expected to exist on Bull AI
  for a company that listed via IPO in late 2025 rather than raising rated debt; not found in
  list_document_availability's inventory (no CRISIL/ICRA/CARE/India Ratings category present).
  Step 10 is NOT FOUND; looked for on Bull AI (no rating-document category listed) and would
  otherwise be sought on the CRISIL, ICRA, CARE, India Ratings and Acuite sites, which this
  session cannot reach.

## Coverage gaps
- No annual report, so no independently-read MD&A, chairman's letter, segment note, related-
  party schedule, auditor's qualification/emphasis paragraph, or promoter shareholding-pattern
  table (the RHP promoter section, read here, is pre-IPO and may not reflect the current
  post-listing pattern). Weakens steps 4, 5 and 9.
- The Q1FY27 concall transcript is read only to page 12 of what is evidently a longer
  document (the final Q&A answer on insurance coverage is cut off mid-sentence). The
  continuation, and any further analyst questions on the fraud, governance response, or
  margin trajectory, are not held.
- Q4FY26 full transcript not independently read; FY26 full-year numbers rest on the guidance
  extraction's citations plus the Q1FY27 investor presentation's PAT-to-EBITDA reconciliation
  table (which does carry FY26 and FY25 columns and was independently chunk-read).
- No credit rating, no independent forensic-audit outcome (the KPMG report was still pending,
  "expected later in August [2026]" per the IP; today is 2026-09-18 and no outcome disclosure
  was searched for, so its status past that estimate is NOT FOUND in this corpus).
- No live CMP or market cap document; per-share and market-cap figures are NOT FOUND in this
  corpus. Use the ~Rs 3,561 cr figure given in the task brief (per Bull AI screen) and verify
  live.
- get_company_classification was not called (budget); sector classification in the card rests
  on the RHP's own description of the business, not a separate Bull AI classification record.
