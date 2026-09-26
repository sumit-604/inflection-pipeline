# RUN LOG — TLL 2026-09-26

- stage 0: run inline by the orchestrator (step1). Peer set changed at intake: LINCOLN -> CAPLIPOINT (Lincoln filed one transcript in 12 months). CAPLIPOINT BSE transcript filings were one-page cover letters; replaced with the company-hosted transcripts fetched via screener.
- tooling: poppler pdftotext exits 127 in this session; all inputs extracted with PyMuPDF (landscape pages split into halves), image-only results pages OCR'd with RapidOCR.
- stage 1: block file wrapped in markdown fences; orchestrator stripped the fences (content unchanged), now parses.
- stage 4: block file had three flag flow-mappings missing the closing brace; orchestrator added them (content unchanged), now parses.
- stage 8: status partial (no direct SEBI/MCA/NCLT/ICAI database access; general web search substituted). Auditor A Bafna & Associates vs director Ashish Anandsingh Bafna relationship: NOT FOUND either way; operator follow-up.
- stage 9: status partial (device/nutraceutical/cosmetic India market sizes and Method 5 not found within search budget). Ran parallel to stage 7, so it used AR CWIP in place of the B07 capex figure (B07 later reported capex_embedded_growth_pct NOT FOUND).
