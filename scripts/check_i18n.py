#!/usr/bin/env python3
"""Checks for the bilingual site. Run from the repo root: python3 scripts/check_i18n.py"""
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://xy-cloud.org/"
PAGES = [
    "index.html", "company.html", "compass.html", "chinichi.html", "cases.html",
    "fde.html", "faq.html", "contact.html", "privacy.html", "news.html",
    "recruit.html", "column.html", "column-education-dx.html", "column-zokujinka.html",
    "investors.html", "partners.html",
]
# Japanese allowed on English pages (names that have no English form, official license numbers, and the link back to Japanese)
JA_ALLOW = ["株式会社XY", "薛 偉軒", "日本語", "派13-318864", "13-ユ-320024", "薛"]
JA_CHARS = re.compile(r"[぀-ヿ㐀-鿿！-｠　-〿]")

errors = []


def err(msg):
    errors.append(msg)


def url_path(page):
    return "" if page == "index.html" else page


def read(p):
    return p.read_text(encoding="utf-8")


def has_link(html, rel_attrs, href):
    for tag in re.findall(r"<link\b[^>]*>", html):
        if all(f'{k}="{v}"' in tag for k, v in rel_attrs.items()) and f'href="{href}"' in tag:
            return True
    return False


def check_hreflang(html, page, where):
    p = url_path(page)
    for lang, href in (("ja", SITE + p), ("en", SITE + "en/" + p), ("x-default", SITE + p)):
        if not has_link(html, {"rel": "alternate", "hreflang": lang}, href):
            err(f"{where}: missing hreflang {lang} -> {href}")


def check_pairs():
    for page in PAGES:
        ja_p, en_p = ROOT / page, ROOT / "en" / page
        if not en_p.exists():
            err(f"missing en/{page}")
            continue
        ja, en = read(ja_p), read(en_p)
        check_hreflang(ja, page, page)
        check_hreflang(en, page, f"en/{page}")
        if '<html lang="en">' not in en:
            err(f"en/{page}: <html lang=\"en\"> missing")
        if not has_link(en, {"rel": "canonical"}, SITE + "en/" + url_path(page)):
            err(f"en/{page}: canonical should be {SITE}en/{url_path(page)}")
        if 'og:locale" content="en_US"' not in en:
            err(f"en/{page}: og:locale en_US missing")
        # language switch both ways
        to_en = "en/" if page == "index.html" else f"en/{page}"
        to_ja = "../" if page == "index.html" else f"../{page}"
        if 'class="lang-switch"' not in ja or f'href="{to_en}"' not in ja:
            err(f"{page}: language switch to {to_en} missing")
        if 'class="lang-switch"' not in en or f'href="{to_ja}"' not in en:
            err(f"en/{page}: language switch to {to_ja} missing")


def visible_japanese(html):
    html = re.sub(r"<style\b.*?</style>", "", html, flags=re.S)
    for word in JA_ALLOW:
        html = html.replace(word, "")
    found = []
    for i, line in enumerate(html.splitlines(), 1):
        if JA_CHARS.search(line):
            found.append(f"L{i}: {line.strip()[:80]}")
    return found


def check_no_japanese():
    for page in PAGES:
        en_p = ROOT / "en" / page
        if en_p.exists():
            for hit in visible_japanese(read(en_p))[:5]:
                err(f"en/{page}: Japanese text {hit}")


def check_links():
    files = sorted(ROOT.glob("*.html")) + sorted((ROOT / "en").glob("*.html"))
    for f in files:
        html = read(f)
        for attr, target in re.findall(r'\b(href|src)="([^"]+)"', html):
            if re.match(r"^(https?:|mailto:|tel:|#|javascript:|data:)", target):
                continue
            path = target.split("#")[0].split("?")[0]
            if not path:
                continue
            base = ROOT if path.startswith("/") else f.parent
            resolved = (base / path.lstrip("/")).resolve()
            if resolved.is_dir() or path.endswith("/"):
                resolved = resolved / "index.html"
            if not resolved.exists():
                err(f"{f.relative_to(ROOT)}: broken {attr} {target}")


def check_sitemap():
    try:
        tree = ET.parse(ROOT / "sitemap.xml")
    except ET.ParseError as e:
        err(f"sitemap.xml: invalid XML ({e})")
        return
    ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    locs = {el.text.strip() for el in tree.getroot().findall("s:url/s:loc", ns)}
    for page in PAGES:
        for url in (SITE + url_path(page), SITE + "en/" + url_path(page)):
            if url not in locs:
                err(f"sitemap.xml: missing {url}")


def check_404():
    html = read(ROOT / "404.html")
    for href in ('href="/"', 'href="/en/"'):
        if href not in html:
            err(f"404.html: missing link {href}")


if __name__ == "__main__":
    check_pairs()
    check_no_japanese()
    check_links()
    check_sitemap()
    check_404()
    for e in errors:
        print("FAIL", e)
    print(f"{len(errors)} problem(s)")
    sys.exit(1 if errors else 0)
