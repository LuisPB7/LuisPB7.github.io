#!/usr/bin/env python3
"""Check local href/src targets and HTML fragments in a built Jekyll site.

Usage: python3 scripts/check_site.py [--site-dir _site]
External links require a separate network check. Only the Python standard
library is used, so this also runs in CI without installing dependencies.
"""

import argparse
from html.parser import HTMLParser
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urljoin, urlsplit


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.links = []
        self.ids = set()
        self.feed(path.read_text(encoding="utf-8"))

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        for attribute in (("id", "name") if tag == "a" else ("id",)):
            if attrs.get(attribute):
                self.ids.add(attrs[attribute])
        for attribute in ("href", "src", "poster"):
            if attrs.get(attribute):
                self.links.append((self.getpos()[0], attrs[attribute]))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site-dir", type=Path, default=Path("_site"))
    parser.add_argument("--base-url", default="https://luispb7.github.io")
    parser.add_argument("--forbid-path", action="append", default=[],
                        help="Also fail if a removed demo route still exists.")
    args = parser.parse_args()
    root = args.site_dir.resolve()
    html_files = sorted(root.rglob("*.html"))
    if not html_files:
        parser.error(f"No HTML files found in {root}; build the site first.")

    base = args.base_url.rstrip("/")
    host = urlsplit(base).netloc.casefold()
    pages = {path: Page(path) for path in html_files}
    errors = []
    checked = 0

    def local_target(path):
        target = (root / unquote(path).lstrip("/")).resolve()
        if not target.is_relative_to(root):
            return None
        if target.is_dir():
            target /= "index.html"
        elif not target.exists() and not target.suffix:
            target = target.with_suffix(".html")
        return target

    for source, page in pages.items():
        relative = source.relative_to(root).as_posix()
        page_url = f"{base}/{relative}"
        if page_url.endswith("/index.html"):
            page_url = page_url[:-10]
        for line, reference in page.links:
            parsed = urlsplit(urljoin(page_url, reference))
            if parsed.scheme not in ("http", "https") or parsed.netloc.casefold() != host:
                continue
            checked += 1
            target = local_target(parsed.path)
            location = f"{relative}:{line}"
            if target is None or not target.is_file():
                errors.append(f"{location}: missing target {reference}")
                continue
            if parsed.fragment and target in pages:
                fragment = unquote(parsed.fragment)
                # Text fragments are browser directives rather than element IDs.
                fragment = fragment.split(":~:text=", 1)[0]
                if fragment and fragment not in pages[target].ids:
                    errors.append(f"{location}: missing fragment {reference}")

    for path in args.forbid_path:
        target = local_target(urlsplit(path).path)
        if target is not None and target.is_file():
            errors.append(f"Removed demo route is still published: {path}")

    # CSS fonts and background images are not present in HTML src attributes.
    css_files = sorted(root.rglob("*.css"))
    for stylesheet in css_files:
        relative = stylesheet.relative_to(root).as_posix()
        css = re.sub(r"/\*.*?\*/", "", stylesheet.read_text(encoding="utf-8"), flags=re.S)
        for match in re.finditer(r"url\(\s*['\"]?([^)'\"]+)", css):
            reference = match.group(1).strip()
            parsed = urlsplit(urljoin(f"{base}/{relative}", reference))
            if parsed.scheme not in ("http", "https") or parsed.netloc.casefold() != host:
                continue
            checked += 1
            target = local_target(parsed.path)
            if target is None or not target.is_file():
                errors.append(f"{relative}: missing CSS asset {reference}")

    for error in errors:
        print(error, file=sys.stderr)
    if errors:
        print(f"FAIL: {len(errors)} error(s) across {len(pages)} HTML pages.", file=sys.stderr)
        return 1
    print(f"PASS: {len(pages)} HTML pages, {len(css_files)} stylesheets; {checked} internal links/assets; no broken targets or fragments.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
