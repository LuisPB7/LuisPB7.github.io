---
permalink: /
title: "Information Retrieval & Machine Learning"
description: "Luís Pedro Borges: Information Retrieval and Machine Learning researcher, Ph.D. in progress. Open to research, ML and data roles in Canada; IEC Working Holiday approved, with permit activation on arrival."
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

<p class="research-lead">Building effective, efficient neural search systems through NLP and deep learning.</p>

I’m Luís Pedro Borges, a **Ph.D. student (in progress)** at Instituto Superior Técnico / INESC-ID and Carnegie Mellon University. My research connects machine learning models with practical search systems, with a focus on learned sparse retrieval.

<div class="opportunity-note" markdown="1">
**Open to jobs and internships in Canada:** Research Scientist, Data Scientist, Data Engineer, ML Engineer and Search Engineer roles.

**Canadian work authorization:** IEC Working Holiday approved for up to 2 years; work permit activation on arrival. **No employer sponsorship required during the permit period.**

<div class="portfolio-actions">
  <a class="btn btn--primary" href="mailto:{{ site.author.email }}">Get in touch</a>
  <a class="btn btn--outline" href="{{ '/cv/' | relative_url }}">View CV</a>
  <a href="{{ site.author.googlescholar | escape }}">Google Scholar</a>
</div>
</div>

## Selected Work

<div class="selected-work">
  <article class="work-item">
    <p class="work-meta">Learned sparse retrieval · ICTIR 2023</p>
    <h3><a href="{{ '/publications/kale/' | relative_url }}">KALE: sparse lexical expansion</a></h3>
    <p>Uses a K-sparse projector to control the number of active terms in learned sparse representations, connecting neural retrieval with efficient inverted-index search.</p>
    <a class="work-link" href="{{ '/publications/kale/' | relative_url }}">Read about KALE <span aria-hidden="true">→</span></a>
  </article>
  <article class="work-item">
    <p class="work-meta">LLM re-ranking · SIGIR 2024</p>
    <h3><a href="{{ '/publications/tip-of-the-tongue-llm-reranking/' | relative_url }}">Finding what users can’t quite name</a></h3>
    <p>Combines retrieval and LLM re-ranking for Tip-of-the-Tongue search: finding a known item from an incomplete or imperfect description.</p>
    <a class="work-link" href="{{ '/publications/tip-of-the-tongue-llm-reranking/' | relative_url }}">Explore the paper and code <span aria-hidden="true">→</span></a>
  </article>
  <article class="work-item">
    <p class="work-meta">Passage retrieval · ECIR 2021</p>
    <h3><a href="{{ '/publications/neural-reranking-ensembles/' | relative_url }}">Model ensembles for neural re-ranking</a></h3>
    <p>Studies how model ensembling, rank fusion and learning-to-rank improve neural passage re-ranking on MS MARCO.</p>
    <a class="work-link" href="{{ '/publications/neural-reranking-ensembles/' | relative_url }}">Read about the study <span aria-hidden="true">→</span></a>
  </article>
</div>

[View all publications]({{ '/publications/' | relative_url }})

## Current Research

My doctoral research, **in progress**, explores *Latent Vocabularies for Learned Sparse Retrieval*: neural retrievers that learn their own sparse vocabularies while retaining the efficiency of inverted-index search. It brings together sparse representations, scalable knowledge distillation, and control of retrieval cost and latency.

My broader work spans sparse and dense retrieval, passage re-ranking, model ensembles and LLM-based re-ranking, with research presented at ECIR, ICTIR, SIGIR and TREC.

## Contact

For job and internship opportunities in Canada, contact me at **[{{ site.author.email }}](mailto:{{ site.author.email }})**. I’m based in Lisbon, Portugal.

[Google Scholar]({{ site.author.googlescholar }}) · [GitHub](https://github.com/{{ site.author.github }}) · [LinkedIn](https://www.linkedin.com/in/{{ site.author.linkedin }})
