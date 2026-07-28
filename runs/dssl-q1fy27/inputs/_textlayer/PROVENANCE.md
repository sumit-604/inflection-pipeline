# Extraction toolchain note (DSSL Q1 FY27 quarterly run)
poppler (pdftotext/pdfinfo/pdftoppm) and tesseract are NOT installable in this
environment (apt main archive unreachable, PPAs 403 via agent proxy). Per the
recurring LESSONS.md pattern (KARNIKA/OBSCP/SFL/VOEPL/KCPSUGIND etc.), the
reliable substitute toolchain is python3 + PyMuPDF (fitz), which is installed.

- `_textlayer/*.pagetext.txt` : faithful page-marked text dump of each source
  PDF, built with PyMuPDF get_text(), one `[[PAGE n]]` marker per page.
  This is the deterministic text-extraction spine (equivalent role to
  `pdftotext -layout`), NOT the Read tool's PDF rendering.
- `_pageimages/*.png` : PyMuPDF-rendered raster of the presentation's
  image-only slides (text layer < 100 chars) for OCR-equivalent transcription
  via the Read tool's vision, since tesseract is unavailable.
Source PDFs are born-digital; text extracts cleanly except the noted
image-only presentation slides.
