---
name: feedback-hold-the-documents
description: Operator expects company documents to be actually downloaded and held on disk before being "read"; cloud MCP snippet search must be labelled as such, never presented as having the document
metadata:
  type: feedback
---

On 2026-09-06, after shallow cards were written from Trendlyne MCP search
snippets, the operator asked: "did you download all these documents? Because
till the time you don't download the documents, how do you read them?" The
cards had said NOT FOUND for credit reports and concalls that the operator
could see on screener.in.

**Why:** the operator's mental model is that reading means holding the file.
A NOT FOUND that really means "not in this service's index" reads to them as a
false claim that the document does not exist. Credit reports in particular are
never in the cloud indexes.

**How to apply:** when using Trendlyne or Bull AI, say plainly that no file
was downloaded and that results are snippets or pages served from the
service's copy. Write "not retrievable from <service>" instead of NOT FOUND
when the document may exist elsewhere. For anything the operator wants held,
use the local screener.in collector (tools/collector), which downloads the
PDFs; it does not yet fetch credit ratings and needs that added. See
[[project-chartink-breadth-pipeline]] for the wider system.
