---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
excerpt: "Research by Luís Pedro Borges on neural information retrieval, learned sparse retrieval, passage re-ranking, and NLP."
---

My research spans neural information retrieval, learned sparse representations, passage re-ranking, and natural language processing. Each publication below includes a short summary and links to the paper; code and data are included where available.

{% if site.author.googlescholar %}
See also my [Google Scholar profile]({{ site.author.googlescholar }}).
{% endif %}

{% assign publications = site.publications | sort: 'date' | reverse %}
{% assign current_year = '' %}
{% for post in publications %}
  {% assign publication_year = post.date | date: '%Y' %}
  {% if publication_year != current_year %}
<h2>{{ publication_year }}</h2>
    {% assign current_year = publication_year %}
  {% endif %}
<article class="publication-entry">
  <h3><a href="{{ post.url | relative_url }}">{{ post.title | escape }}</a></h3>
  <p>{{ post.authors | escape }}<br><em>{{ post.venue | escape }}</em></p>
  <p>{{ post.excerpt | escape }}</p>
  <p class="publication-links">{% if post.publication_url %}<a href="{{ post.publication_url }}">Publisher record</a> · {% endif %}<a href="{{ post.paperurl }}">{{ post.paper_label }}</a>{% if post.codeurl %} · <a href="{{ post.codeurl }}">Code and data</a>{% endif %}</p>
</article>
{% endfor %}
