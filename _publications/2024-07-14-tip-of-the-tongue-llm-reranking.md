---
title: "Generalizable Tip-of-the-Tongue Retrieval with LLM Re-ranking"
collection: publications
permalink: /publications/tip-of-the-tongue-llm-reranking/
date: 2024-07-14
venue: "ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR)"
authors: "Luís Borges, Rohan Jha, Jamie Callan, and Bruno Martins"
excerpt: "Combining retrieval and LLM re-ranking to find remembered items from uncertain descriptions across multiple domains."
publication_url: "https://doi.org/10.1145/3626772.3657917"
paperurl: "https://www.cs.cmu.edu/~callan/Papers/sigir24-luis_borges.pdf"
paper_label: "Paper (PDF)"
codeurl: "https://github.com/LuisPB7/TipTongue"
redirect_from:
  - /publications/2009-10-01-paper-title-number-5/
---

**{{ page.authors }}**

This work studies how retrieval systems generalize across domains when users describe items they cannot name. It introduces a multi-domain dataset and evaluates first-stage retrieval followed by zero-shot GPT-4 re-ranking using item titles. The experiments show benefits from training across domains and from applying an LLM to retrieved candidates.

[Publisher record]({{ page.publication_url }}) · [Paper (PDF)]({{ page.paperurl }}) · [Code and data]({{ page.codeurl }})

[All publications]({{ '/publications/' | relative_url }})
