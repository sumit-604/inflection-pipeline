# RUN LOG — TLL 2026-09-26

- stage 0: run inline by the orchestrator (step1). Peer set changed at intake: LINCOLN -> CAPLIPOINT (Lincoln filed one transcript in 12 months). CAPLIPOINT BSE transcript filings were one-page cover letters; replaced with the company-hosted transcripts fetched via screener.
- tooling: poppler pdftotext exits 127 in this session; all inputs extracted with PyMuPDF (landscape pages split into halves), image-only results pages OCR'd with RapidOCR.
- stage 1: block file wrapped in markdown fences; orchestrator stripped the fences (content unchanged), now parses.
