---
title: "Team CMU-LTI at TREC 2023 Tip-of-the-Tongue Track"
collection: publications
permalink: /publications/trec-2023-tip-of-the-tongue/
date: 2023-11-20
venue: "Text Retrieval Conference (TREC), participant paper"
authors: "Luís Borges, Jamie Callan, and Bruno Martins"
excerpt: "A two-stage movie retrieval system combining dense passage retrieval with zero-shot LLM re-ranking for uncertain, verbose queries."
paperurl: "https://trec.nist.gov/pubs/trec32/papers/CMU-LTI.T.pdf"
paper_label: "Paper (PDF)"
codeurl: "https://github.com/LuisPB7/TipTongue/tree/main/TREC_Participation"
redirect_from:
  - /publications/2009-10-01-paper-title-number-3/
---

**{{ page.authors }}**

This TREC participant paper describes a movie search pipeline for tip-of-the-tongue queries: descriptions that can be long, uncertain, or partially inaccurate. The system combines dense passage retrieval with GPT-4 re-ranking over candidate movie titles, comparing re-ranking strategies and ways to match query sentences to Wikipedia content.

[Paper (PDF)]({{ page.paperurl }}) · [Code and data]({{ page.codeurl }})

[All publications]({{ '/publications/' | relative_url }})
