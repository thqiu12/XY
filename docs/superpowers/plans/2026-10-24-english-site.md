# English Site (/en/) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publish an English version of xy-cloud.org under `/en/`, one page per Japanese page, linked by a language switch and hreflang.

**Architecture:** Static HTML only (GitHub Pages, no build). `/en/*.html` mirror the Japanese filenames and reuse `../css/style.css` and `../assets/`. A Python checker (`scripts/check_i18n.py`) is the test suite: it enforces page pairs, hreflang, canonical, language switch links, internal link targets, no stray Japanese on English pages, and sitemap coverage.

**Tech Stack:** HTML, CSS, Python 3 (stdlib only) for checks, `python3 -m http.server` for preview.

**Spec:** `docs/superpowers/specs/2026-10-24-english-site-design.md`

---

## File map

| File | Action | Responsibility |
|---|---|---|
| `scripts/check_i18n.py` | Create | Test suite for the bilingual site |
| `css/style.css` | Modify (append) | `.lang-switch` styles |
| 14 Japanese pages (`index.html` … `column-zokujinka.html`) | Modify | hreflang trio, language switch in nav + footer, CSS version bump |
| `en/<page>.html` ×14 | Create | English pages |
| `404.html` | Modify | Bilingual 404 (JA top, EN bottom) |
| `sitemap.xml` | Modify | Add 14 English URLs |
| `README.md` | Modify | Bilingual maintenance rule |

Pages (`PAGES`): `index.html company.html compass.html chinichi.html cases.html fde.html faq.html contact.html privacy.html news.html recruit.html column.html column-education-dx.html column-zokujinka.html`

---

## Shared reference (every task that writes English uses this)

### Glossary

| Japanese | English |
|---|---|
| 株式会社XY | XY, K.K. (first mention may add "(株式会社XY)") |
| 代表取締役 薛 偉軒 | Iken Setsu, Representative Director & CEO |
| 学校法人 羽場学園 | Haba Gakuen Educational Corporation |
| 学校法人 平井学園 | Hirai Gakuen Educational Corporation |
| SGG外語学院 | SGG Gaigo Gakuin (a Japanese language school) |
| 学校法人 | educational corporation |
| 日本語学校 / 専門学校 / 学習塾 | Japanese language school / vocational college / cram school |
| 留学生 | international students |
| 募集 / 出願 / 入学手続き | student recruitment / applications / enrollment |
| 属人化 | dependence on specific individuals |
| Compass | Compass, a student application & management system |
| chinichi-OS | chinichi-OS, an operating platform for school corporations |
| FDE | Forward Deployed Engineering (FDE) |
| サービス / 導入事例 / コラム / 採用 / 会社概要 | Services / Case Studies / Insights / Careers / Company |
| お知らせ / よくある質問 / プライバシーポリシー / お問い合わせ | News / FAQ / Privacy Policy / Contact |

Group disclosure (use wherever the three schools appear as customers): *"Compass runs in daily operations at schools operated within our education group — Haba Gakuen, Hirai Gakuen and SGG Gaigo Gakuin."*

Tone: plain, specific, professional American English. No hype words ("revolutionary", "cutting-edge"). Rewrite for overseas readers; do not translate word for word. Do not invent facts, prices, SLAs or service terms that are not on the Japanese site.

Contact facts: phone `+81-80-4876-7999` (`tel:+818048767999`), email `setsuiken@xy-cloud.org`, address `3F Sankei Bldg., 1-28-10 Takadanobaba, Shinjuku-ku, Tokyo 169-0075, Japan`.

### English `<head>` template (replace `{PAGE}`, `{TITLE}`, `{DESC}`; for index, `{URL_PATH}` is empty, otherwise it equals `{PAGE}`)

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#0f2747">
<meta property="og:image" content="https://xy-cloud.org/assets/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<title>{TITLE}</title>
<meta name="description" content="{DESC}">
<link rel="canonical" href="https://xy-cloud.org/en/{URL_PATH}">
<link rel="alternate" hreflang="ja" href="https://xy-cloud.org/{URL_PATH}">
<link rel="alternate" hreflang="en" href="https://xy-cloud.org/en/{URL_PATH}">
<link rel="alternate" hreflang="x-default" href="https://xy-cloud.org/{URL_PATH}">
<meta property="og:type" content="website">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="{DESC}">
<meta property="og:url" content="https://xy-cloud.org/en/{URL_PATH}">
<meta property="og:site_name" content="XY, K.K.">
<meta property="og:locale" content="en_US">
<link rel="icon" type="image/svg+xml" href="../assets/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preconnect" href="https://unpkg.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://unpkg.com/@phosphor-icons/web@2.1.1/src/regular/style.css">
<link rel="stylesheet" href="https://unpkg.com/@phosphor-icons/web@2.1.1/src/fill/style.css">
<link rel="stylesheet" href="../css/style.css?v=16">
</head>
```

Keep any page-specific `<style>` or JSON-LD from the Japanese page, translated (JSON-LD: `"name": "XY, K.K."`, `"alternateName": "株式会社XY"`, `"inLanguage": "en"`, founder `"Iken Setsu"`).

### English header template (`{PAGE}` = filename; for index use `../` instead of `../index.html`)

```html
<header class="site-header">
  <div class="wrap">
    <nav class="nav" id="nav">
      <a class="nav__brand" href="index.html" aria-label="XY, K.K. home">
        <img class="logo" src="../assets/logo.svg" alt="" width="80" height="32">
        <span class="brand-jp">XY, K.K.</span>
      </a>
      <div class="nav__links">
        <a href="index.html#services">Services</a>
        <a href="fde.html">FDE</a>
        <a href="cases.html">Case Studies</a>
        <a href="column.html">Insights</a>
        <a href="recruit.html">Careers</a>
        <a href="company.html">Company</a>
      </div>
      <div class="nav__cta">
        <div class="lang-switch" role="group" aria-label="Language"><a href="../{PAGE}" hreflang="ja" lang="ja">JA</a><span aria-current="true">EN</span></div>
        <a class="nav__phone" href="tel:+818048767999"><i class="ph-fill ph-phone-call"></i>+81-80-4876-7999</a>
        <a class="btn btn--primary" href="contact.html">Contact us</a>
        <button class="nav__toggle" id="navToggle" aria-label="Open menu" aria-expanded="false"><i class="ph ph-list"></i></button>
      </div>
    </nav>
  </div>
</header>
```

On `en/index.html` the Services link is `#services`.

### English footer template

```html
<footer class="site-footer">
  <div class="wrap">
    <div class="footer__top">
      <div class="footer__brand">
        <img class="logo" src="../assets/logo-white.svg" alt="XY, K.K." width="80" height="32">
        <div class="brand-jp">XY, K.K.</div>
        <p>Software and AI for educational institutions,<br>built by people who run schools.</p>
      </div>
      <div class="footer__col">
        <h4>Company</h4>
        <ul>
          <li><a href="index.html#services">Services</a></li>
          <li><a href="fde.html">FDE</a></li>
          <li><a href="index.html#strengths">Why XY</a></li>
          <li><a href="cases.html">Case Studies</a></li>
          <li><a href="index.html#representative">Message from the CEO</a></li>
          <li><a href="company.html">Corporate Profile</a></li>
          <li><a href="column.html">Insights</a></li>
          <li><a href="news.html">News</a></li>
          <li><a href="recruit.html">Careers</a></li>
          <li><a href="faq.html">FAQ</a></li>
          <li><a href="privacy.html">Privacy Policy</a></li>
        </ul>
      </div>
      <div class="footer__col footer__contact">
        <h4>Contact</h4>
        <div><i class="ph-fill ph-map-pin"></i><span>3F Sankei Bldg., 1-28-10 Takadanobaba,<br>Shinjuku-ku, Tokyo 169-0075, Japan</span></div>
        <div><i class="ph-fill ph-phone-call"></i><span><a href="tel:+818048767999" style="color:inherit">+81-80-4876-7999</a></span></div>
        <div><i class="ph-fill ph-envelope-simple"></i><span><a href="mailto:setsuiken@xy-cloud.org" style="color:inherit">setsuiken@xy-cloud.org</a></span></div>
      </div>
    </div>
    <div class="footer__bottom">
      <p>© 2024 XY, K.K. (株式会社XY) All rights reserved.</p>
      <div class="legal">
        <a href="company.html">Corporate Profile</a>
        <a href="privacy.html">Privacy Policy</a>
        <a href="../{PAGE}" hreflang="ja" lang="ja">日本語</a>
      </div>
    </div>
  </div>
</footer>

<a class="float-cta" href="contact.html" aria-label="Contact us"><i class="ph-fill ph-chat-circle-dots"></i>Contact us</a>
```

Then copy the page's `<script>` block from the Japanese page unchanged except user-facing strings (translate them).

---

### Task 1: Checker script (the test suite)

**Files:**
- Create: `scripts/check_i18n.py`

- [ ] **Step 1: Write the checker**

```python
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
]
# Japanese allowed on English pages (names that have no English form, and the link back to Japanese)
JA_ALLOW = ["株式会社XY", "薛 偉軒", "日本語", "薛"]
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
```

- [ ] **Step 2: Run it — expect failures**

Run: `python3 scripts/check_i18n.py`
Expected: exit 1, `missing en/index.html` … for all 14 pages, sitemap and 404 failures. No Python traceback.

- [ ] **Step 3: Commit**

```bash
git add scripts/check_i18n.py
git commit -m "test: 英語版サイト用のチェックスクリプトを追加"
```

### Task 2: Language switch CSS + Japanese pages

**Files:**
- Modify: `css/style.css` (append at end)
- Modify: the 14 Japanese pages

- [ ] **Step 1: Append CSS**

```css
/* ---------- language switch ---------- */
.lang-switch { display: inline-flex; align-items: center; gap: 2px; padding: 3px; border: 1px solid var(--line); border-radius: 999px; font-size: 12.5px; font-weight: 700; letter-spacing: .04em; }
.lang-switch a, .lang-switch span { padding: 4px 10px; border-radius: 999px; line-height: 1.2; }
.lang-switch a { color: var(--ink-2); }
.lang-switch a:hover { color: var(--accent-ink); text-decoration: none; background: var(--accent-soft); }
.lang-switch [aria-current] { background: var(--navy); color: #fff; }
```

- [ ] **Step 2: Patch the Japanese pages with a one-off script**

Run from the repo root:

```bash
python3 - <<'EOF'
import re
from pathlib import Path
PAGES = ["index.html","company.html","compass.html","chinichi.html","cases.html","fde.html","faq.html","contact.html","privacy.html","news.html","recruit.html","column.html","column-education-dx.html","column-zokujinka.html"]
for page in PAGES:
    p = Path(page); html = p.read_text(encoding="utf-8")
    up = "" if page == "index.html" else page
    to_en = "en/" if page == "index.html" else f"en/{page}"
    hreflang = (f'<link rel="alternate" hreflang="ja" href="https://xy-cloud.org/{up}">\n'
                f'<link rel="alternate" hreflang="en" href="https://xy-cloud.org/en/{up}">\n'
                f'<link rel="alternate" hreflang="x-default" href="https://xy-cloud.org/{up}">\n')
    assert 'hreflang=' not in html, page
    html, n = re.subn(r'(<link rel="canonical"[^>]*>\n)', r'\1' + hreflang, html, count=1); assert n == 1, page
    switch = f'<div class="lang-switch" role="group" aria-label="言語"><span aria-current="true">JA</span><a href="{to_en}" hreflang="en" lang="en">EN</a></div>\n        '
    html, n = re.subn(r'(<div class="nav__cta">\n\s*)', r'\1' + switch, html, count=1); assert n == 1, page
    html, n = re.subn(r'(<a href="privacy.html">プライバシーポリシー</a>\n)(\s*</div>\n\s*</div>\n\s*</footer>)',
                      r'\1' + f'        <a href="{to_en}" hreflang="en" lang="en">English</a>\n' + r'\2', html, count=1); assert n == 1, page
    html = html.replace("css/style.css?v=15", "css/style.css?v=16")
    p.write_text(html, encoding="utf-8")
    print("patched", page)
EOF
```

Expected: `patched <page>` ×14, no AssertionError. If an assertion fires, open that page, adjust its header/footer to match the pattern by hand, and rerun only for remaining pages.

- [ ] **Step 3: Verify**

Run: `git diff --stat && python3 scripts/check_i18n.py | grep -E 'hreflang|language switch to en' | grep -v '^FAIL en/' | head`
Expected: no lines about Japanese pages' hreflang or switch (only `en/...` and missing-file failures remain).

- [ ] **Step 4: Commit**

```bash
git add css/style.css *.html
git commit -m "feat(i18n): 日本語ページに言語切替と hreflang を追加"
```

### Task 3: `en/index.html` (reference page — establishes voice)

**Files:**
- Create: `en/index.html`
- Source: `index.html`

- [ ] **Step 1: Write the page** from `index.html` using the head/header/footer templates, `{PAGE}` = `index.html` (switch links `../`). Content rules:
  - Title: `XY, K.K. | School operations software and AI, built by educators in Tokyo`
  - Hero h1: "AI-native school operations, built by educators." Eyebrow "Education × Technology". Lead covers: we build and deploy operations software and AI agents for language schools, vocational colleges and other educational institutions; we run schools ourselves.
  - Keep sections: traction metrics, problem, services (6), AI capability, strengths, products, why, representative, cases teaser, mission, CTA.
  - **Delete** the `#subsidy` section entirely.
  - Strength 04: retitle "Direct access to the people who decide and build"; drop "OPC (One Person Company)"; say clients work directly with the CEO, who leads product and engineering with an AI-assisted development process, so decisions and changes are fast.
  - Cases teaser uses the group disclosure sentence. Screenshot caption: "The Compass application portal in production (school names hidden)".
  - Representative: name "Iken Setsu", role "Representative Director & CEO", tags: "Keio University (B.A.)", "The University of Tokyo (Master's)", "Chair of an educational corporation", "Leads AI & product development", "Former Recruit Co., Ltd.". Avatar `<span aria-hidden="true">薛</span>`, image `../assets/daihyou.jpg` alt "Iken Setsu, Representative Director & CEO".
  - JSON-LD per the head template rules; `"areaServed": "Worldwide"`; `knowsAbout` and offers in English.
- [ ] **Step 2: Run checker**: `python3 scripts/check_i18n.py | grep 'en/index.html'` → expected: no output.
- [ ] **Step 3: Commit** `git add en/index.html && git commit -m "feat(en): 英語版トップページ"`

### Task 4: Company, Contact, Privacy

**Files:** Create `en/company.html`, `en/contact.html`, `en/privacy.html` (sources: same names at root)

- [ ] **Step 1: `en/company.html`** — title "Corporate Profile | XY, K.K.". Profile table rows exactly:
  Company name `XY, K.K. (株式会社XY)` · Address (EN address) · Representative `Iken Setsu, Representative Director & CEO` · Established `February 7, 2024` · Capital `JPY 1,000,000` · Fiscal year `October 1 – September 30` · Corporate Number `9011101106148` · D-U-N-S Number `964338668` · Phone `+81-80-4876-7999` · Email · Business (summary sentence: development and deployment of operations software — CRM, student management, recruitment, HR — and AI agents for educational institutions; then the articles-of-incorporation purposes translated as a list, labeled "Business purposes stated in the Articles of Incorporation"). Omit 公告方法. Translate any other sections on the page (history, map, etc.).
- [ ] **Step 2: `en/contact.html`** — translate labels, placeholders, notes and the JS status messages. Keep the same Web3Forms `access_key`. Add two fields after the organization field: `Country` (text input, `name="country"`, required) and `Organization type` (select, `name="organization_type"`: Educational institution / Investor / Partner / Other, required). Set the hidden subject (or add `<input type="hidden" name="subject" value="[EN] New inquiry from xy-cloud.org">`). Phone shown in international format.
- [ ] **Step 3: `en/privacy.html`** — full translation; first paragraph: "This English translation is provided for convenience. The Japanese version is the official text and prevails in case of any discrepancy." linking to `../privacy.html`.
- [ ] **Step 4: Run** `python3 scripts/check_i18n.py | grep -E 'en/(company|contact|privacy)'` → no output.
- [ ] **Step 5: Commit** `git add en/company.html en/contact.html en/privacy.html && git commit -m "feat(en): 会社概要・お問い合わせ・プライバシーポリシーの英語版"`

### Task 5: Products and cases

**Files:** Create `en/compass.html`, `en/chinichi.html`, `en/cases.html`

- [ ] **Step 1:** Translate each page. Wherever the three schools appear as customers, use the group disclosure. Keep all metrics as on the Japanese pages. Image paths `../assets/...`, alt texts in English.
- [ ] **Step 2:** `python3 scripts/check_i18n.py | grep -E 'en/(compass|chinichi|cases)'` → no output.
- [ ] **Step 3:** `git add en/compass.html en/chinichi.html en/cases.html && git commit -m "feat(en): Compass・chinichi-OS・導入事例の英語版"`

### Task 6: FDE, FAQ, News, Careers

**Files:** Create `en/fde.html`, `en/faq.html`, `en/news.html`, `en/recruit.html`

- [ ] **Step 1: `en/fde.html`** — translate.
- [ ] **Step 2: `en/faq.html`** — rewrite for overseas readers. Keep only questions whose answers are supported by the Japanese site (FAQ, product pages, company page). Remove subsidy questions. Where the Japanese FAQ covers remote support, data handling, on-premise AI, languages or contracts, adapt them. Do not add pricing, currency or SLA claims that are not on the site.
- [ ] **Step 3: `en/news.html`** — translate each item, keep dates (format `Oct 24, 2026` style).
- [ ] **Step 4: `en/recruit.html`** — translate; state the work location is Tokyo; keep the Japanese-language requirements exactly as the Japanese page states them.
- [ ] **Step 5:** `python3 scripts/check_i18n.py | grep -E 'en/(fde|faq|news|recruit)'` → no output.
- [ ] **Step 6:** `git add en/fde.html en/faq.html en/news.html en/recruit.html && git commit -m "feat(en): FDE・FAQ・お知らせ・採用の英語版"`

### Task 7: Insights (columns)

**Files:** Create `en/column.html`, `en/column-education-dx.html`, `en/column-zokujinka.html`

- [ ] **Step 1:** Translate. At the top of each article add: "This article draws on the experience of educational institutions in Japan."
- [ ] **Step 2:** `python3 scripts/check_i18n.py | grep -E 'en/column'` → no output.
- [ ] **Step 3:** `git add en/column*.html && git commit -m "feat(en): コラムの英語版"`

### Task 8: 404, sitemap, README

**Files:** Modify `404.html`, `sitemap.xml`, `README.md`

- [ ] **Step 1: 404** — keep the Japanese block; below it add an English block: heading "Page not found", text "The page may have been moved or deleted. Please check the URL or go back to the home page.", button `<a class="btn btn--ghost" href="/en/">English home</a>`. Make the Japanese "トップへ戻る" link `href="/"`. Use absolute `/css/style.css?v=16` and `/assets/...` paths if the page currently uses relative ones (404 is served at any path).
- [ ] **Step 2: sitemap** — for each of the 14 pages add a `<url>` with `<loc>https://xy-cloud.org/en/{URL_PATH}</loc>`, `<lastmod>2026-10-24</lastmod>`, same changefreq/priority as its Japanese entry. Add Japanese entries that are missing so every page pair is listed.
- [ ] **Step 3: README** — add section:

```markdown
## 英語版（/en/）

- `/en/` 以下に日本語版と同名の英語ページがある。日本語ページを変更したら、同名の英語ページも更新する。
- ページを追加するときは英語版も作り、hreflang・言語切替・sitemap.xml を両方に入れる。
- `python3 scripts/check_i18n.py` が 0 problem(s) になることを確認してから push する。
```

- [ ] **Step 4:** `python3 scripts/check_i18n.py` → expected `0 problem(s)`, exit 0.
- [ ] **Step 5:** `git add 404.html sitemap.xml README.md && git commit -m "feat(i18n): 404 の日英併記・sitemap・README"`

### Task 9: Visual check, then publish

- [ ] **Step 1:** `python3 -m http.server 8765 --bind 127.0.0.1` (background) and open `http://127.0.0.1:8765/en/`.
- [ ] **Step 2:** Screenshot desktop (1440×900) and mobile (375×812) for `en/index.html`, `en/company.html`, `en/contact.html`; also `index.html` (JA) to confirm the switch fits the nav. Check: no horizontal scroll (`document.documentElement.scrollWidth === innerWidth`), long English words don't overflow cards, language switch visible on mobile next to the menu button.
- [ ] **Step 3:** Click JA⇄EN on three pages and confirm it lands on the counterpart page.
- [ ] **Step 4:** Ask the user before sending a real test inquiry from `en/contact.html`.
- [ ] **Step 5:** `python3 scripts/check_i18n.py` → `0 problem(s)`; `git push origin main`; after ~1 minute `curl -s https://xy-cloud.org/en/ | grep -c 'XY, K.K.'` ≥ 1 and `curl -s -o /dev/null -w '%{http_code}' https://xy-cloud.org/en/company.html` = 200.
