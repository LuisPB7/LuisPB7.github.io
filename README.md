# Luís Borges — professional portfolio

Source for [luispb7.github.io](https://luispb7.github.io/), a Jekyll portfolio covering Information Retrieval, Machine Learning, NLP, and neural search.

## Local development

With Ruby 3.3 and Bundler installed:

```sh
bundle install
JEKYLL_ENV=production bundle exec jekyll build --safe --strict_front_matter
python3 scripts/check_site.py
bundle exec jekyll serve --config _config.yml,_config.dev.yml
```

The local preview is available at `http://localhost:4000`. Generated output is written to `_site/` and should not be committed.

## Editing content

- `_pages/about.md`: homepage, research focus, and selected work.
- `_pages/publications.md` and `_publications/`: publication list and individual research pages.
- `_pages/cv.md`: current web CV.
- `_config.yml`: identity, contact details, and site metadata.
- `_data/navigation.yml`: primary navigation.
- `files/cv.pdf`: original downloadable CV, November 2025.
- `images/profile.png`: profile photograph.

Keep the Ph.D. status explicitly **in progress** until graduation is confirmed. Check publication status and biographical details against the existing research records before changing them. The primary contact address is `lpborges.careers@gmail.com`.

The validation workflow builds with the locked GitHub Pages dependencies and checks internal links, assets and HTML fragments on pull requests. External publisher and profile links require a separate network check.

Changes are reviewed through pull requests against `master`; merging to the publishing branch updates GitHub Pages.

## Theme attribution

The site is based on [AcademicPages](https://github.com/academicpages/academicpages.github.io), derived from [Minimal Mistakes](https://github.com/mmistakes/minimal-mistakes). The original MIT license and Michael Rose copyright notice are retained in [LICENSE](LICENSE).
