# -*- coding: utf-8 -*-
"""Génère site-internet/sitemap.xml : pages principales (3 langues + alternates), recrutement, blog (français)."""
import os, glob, datetime, json, re
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, "..", "site-internet")
SITE = "https://www.sa-la-garonne.fr/"
TODAY = datetime.date.today().isoformat()
PAGES = [("", "1.0", "weekly"), ("assainissement.html", "0.9", "monthly"), ("eau-potable.html", "0.9", "monthly"),
         ("rehabilitation-sans-tranchee.html", "0.9", "monthly"), ("travaux-complexes.html", "0.9", "monthly"),
         ("realisations.html", "0.8", "monthly"), ("entreprise.html", "0.8", "yearly"), ("recrutement.html", "0.7", "monthly"),
         ("contact.html", "0.8", "yearly"), ("mentions-legales.html", "0.2", "yearly")]
def lastmod(path):
    try: return datetime.date.fromtimestamp(os.path.getmtime(path)).isoformat()
    except OSError: return TODAY
out = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
for prefix in ("", "en/", "zh/"):
    for page, prio, freq in PAGES:
        out += ["  <url>", f"    <loc>{SITE}{prefix}{page}</loc>"]
        for hl, pf in (("fr", ""), ("en", "en/"), ("zh-Hans", "zh/"), ("x-default", "")):
            out.append(f'    <xhtml:link rel="alternate" hreflang="{hl}" href="{SITE}{pf}{page}"/>')
        out += [f"    <lastmod>{lastmod(os.path.join(ROOT, prefix, page or 'index.html'))}</lastmod>", f"    <changefreq>{freq}</changefreq>", f"    <priority>{prio}</priority>", "  </url>"]
# blog
idx = os.path.join(HERE, "blog-index.json")
arts = json.load(open(idx, encoding="utf-8")) if os.path.exists(idx) else []
out += ["  <url>", f"    <loc>{SITE}blog/</loc>", f"    <lastmod>{arts[0]['date'] if arts else TODAY}</lastmod>", "    <changefreq>weekly</changefreq>", "    <priority>0.8</priority>", "  </url>"]
for f in sorted(glob.glob(os.path.join(ROOT, "blog", "page-*.html"))):
    out += ["  <url>", f"    <loc>{SITE}blog/{os.path.basename(f)}</loc>", "    <changefreq>weekly</changefreq>", "    <priority>0.5</priority>", "  </url>"]
for a in arts:
    out += ["  <url>", f"    <loc>{SITE}blog/{a['slug']}.html</loc>", f"    <lastmod>{a['date']}</lastmod>", "    <changefreq>yearly</changefreq>", "    <priority>0.7</priority>", "  </url>"]
out.append("</urlset>")
open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write("\n".join(out) + "\n")
print(f"sitemap : {sum(1 for l in out if l.strip().startswith('<loc>'))} URL")
