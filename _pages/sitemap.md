---
layout: single
title: "Sitemap"
excerpt: "Pages and publications on Luís Borges's professional portfolio."
permalink: /sitemap/
author_profile: false
---

## Pages

- [Home]({{ '/' | relative_url }})
- [Publications]({{ '/publications/' | relative_url }})
- [CV]({{ '/cv/' | relative_url }})

## Publication pages

{% assign publications = site.publications | sort: 'date' | reverse %}
{% for publication in publications %}
- [{{ publication.title }}]({{ publication.url | relative_url }})
{% endfor %}

[XML sitemap]({{ '/sitemap.xml' | relative_url }})
