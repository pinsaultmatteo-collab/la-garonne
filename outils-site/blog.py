# -*- coding: utf-8 -*-
"""Blog SA LA GARONNE — rendu des articles Markdown (contenu-blog/*.md) en pages HTML.

Produit : site-internet/blog/<slug>.html, blog/index.html (+ pagination), blog/<slug>.md (copie
Markdown pour les LLM), blog/feed.xml (RSS). Le français est la seule langue du blog.
Usage : python3 outils-site/blog.py
"""
import os, re, json, glob, datetime, html as H, importlib.util
import markdown

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..", "site-internet")
SRC = os.path.join(HERE, "..", "contenu-blog")
spec = importlib.util.spec_from_file_location("build", os.path.join(HERE, "build.py"))
B = importlib.util.module_from_spec(spec); spec.loader.exec_module(B)
SITE = B.SITE
PAR_PAGE = 9
AUTEUR = "L'équipe SA LA GARONNE"

# Photos utilisables en couverture : nom → largeurs disponibles (JPEG + WebP)
COVERS = {
 "chantier-capitole-engins": [480,768,1024,1280,1440,1920], "chantier-tranchee-centre-ville": [480,768,1024,1280,1440,1920],
 "chantier-hydrocurage-equipe": [480,768,1024,1280,1440,1920], "equipe-reunion-inspection": [768,1280,1600],
 "ric-robot-inspection": [768,1024], "collecteur-visitable-profondeur": [536], "tranchee-blindee-monument": [529],
 "aep-raccordement-fonte": [768], "camion-rehabilitation-sans-tranchee": [800], "pelle-mecanique-chantier": [300,605],
 "parc-engins": [768,1280,1920],
}
for _f in glob.glob(os.path.join(ROOT, "assets/img/realisations/*-01-1200.jpg")):
    COVERS["realisations/" + os.path.basename(_f)[:-9]] = [800, 1200]

CATEGORIES = {
 "Assainissement": ("assainissement.html", "assainissement"),
 "Eau potable": ("eau-potable.html", "eau-potable"),
 "Réhabilitation sans tranchée": ("rehabilitation-sans-tranchee.html", "sans-tranchee"),
 "Travaux complexes": ("travaux-complexes.html", "complexes"),
 "Entreprise": ("entreprise.html", "entreprise"),
}
MOIS = ["janvier","février","mars","avril","mai","juin","juillet","août","septembre","octobre","novembre","décembre"]
def date_fr(d): return f"{d.day} {MOIS[d.month-1]} {d.year}"
def rfc822(d): return datetime.datetime(d.year, d.month, d.day, 8, 0, 0, tzinfo=datetime.timezone.utc).strftime("%a, %d %b %Y %H:%M:%S +0000")

def parse(path):
    raw = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", raw, re.S)
    if not m: raise SystemExit(f"{path} : frontmatter absent")
    meta = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1); meta[k.strip()] = v.strip()
    for k in ("title", "slug", "date", "description", "category", "cover"):
        if not meta.get(k): raise SystemExit(f"{path} : champ « {k} » manquant")
    if meta["category"] not in CATEGORIES: raise SystemExit(f"{path} : catégorie inconnue « {meta['category']} »")
    if meta["cover"] not in COVERS: raise SystemExit(f"{path} : couverture inconnue « {meta['cover']} »")
    meta["date"] = datetime.date.fromisoformat(meta["date"])
    meta["tags"] = [t.strip() for t in meta.get("tags", "").split(",") if t.strip()]
    meta["body_md"] = m.group(2).strip()
    meta["words"] = len(re.findall(r"\w+", meta["body_md"]))
    meta["minutes"] = max(1, round(meta["words"] / 200))
    meta["file"] = path
    return meta

def render_md(text):
    md = markdown.Markdown(extensions=["extra", "toc", "sane_lists"], extension_configs={"toc": {"toc_depth": "2-2", "anchorlink": False}})
    html = md.convert(text)
    toc = [(t["id"], t["name"]) for t in md.toc_tokens]
    return html, toc

def faq_from_md(text):
    """Paires question / réponse sous la section « Questions fréquentes »."""
    m = re.search(r"^## (?:Questions fréquentes|FAQ)[^\n]*\n(.*?)(?=^## |\Z)", text, re.S | re.M)
    if not m: return []
    out = []
    for q, a in re.findall(r"^### (.+?)\n(.*?)(?=^### |\Z)", m.group(1), re.S | re.M):
        out.append((q.strip(), re.sub(r"\s+", " ", re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", a)).strip()))
    return out

def cover_pic(name, alt, sizes="100vw", loading="lazy", dims=True):
    ws = COVERS[name]; base = f"assets/img/{name}"
    from PIL import Image
    w, h = Image.open(os.path.join(ROOT, f"{base}-{ws[-1]}.jpg")).size
    webp = ", ".join(f"{base}-{x}.webp {x}w" for x in ws); jpg = ", ".join(f"{base}-{x}.jpg {x}w" for x in ws)
    return (f'<picture><source type="image/webp" srcset="{webp}" sizes="{sizes}"><img src="{base}-{ws[-1]}.jpg" srcset="{jpg}" sizes="{sizes}" alt="{H.escape(alt, quote=True)}" loading="{loading}" width="{w}" height="{h}"></picture>', f"{SITE}{base}-{ws[-1]}.jpg")

def card(a, tag="h3"):
    pic, _ = cover_pic(a["cover"], a["title"], "(max-width: 960px) 100vw, 33vw")
    _, catslug = CATEGORIES[a["category"]]
    return (f'<article class="post" data-cat="{catslug}" data-reveal><a class="post__media" href="blog/{a["slug"]}.html" data-cursor="Lire">{pic}<span class="post__kicker mono">{H.escape(a["category"])}</span></a>'
            f'<div class="post__body"><p class="post__meta"><span class="mono"><time datetime="{a["date"].isoformat()}">{date_fr(a["date"])}</time></span><span class="mono">{a["minutes"]} min de lecture</span></p>'
            f'<{tag} class="post__title"><a href="blog/{a["slug"]}.html">{H.escape(a["title"])}</a></{tag}><p class="post__excerpt">{H.escape(a["description"])}</p>'
            f'<a class="link-arrow" href="blog/{a["slug"]}.html"><span>Lire l\'article</span>{B.LARROW}</a></div></article>')

def featured(a):
    pic, _ = cover_pic(a["cover"], a["title"], "100vw", loading="eager")
    return (f'<a class="feature-post" href="blog/{a["slug"]}.html" data-reveal="scale" data-cursor="Lire">{pic}<div class="feature-post__body">'
            f'<span class="mono feature-post__label">À la une · {H.escape(a["category"])}</span><h2 class="feature-post__title">{H.escape(a["title"])}</h2>'
            f'<p>{H.escape(a["description"])}</p><span class="mono feature-post__meta">{date_fr(a["date"])} · {a["minutes"]} min de lecture</span>'
            f'<span class="btn btn--light">Lire l\'article {B.ARROW}</span></div></a>')

def enrich_body(html):
    """FAQ en accordéon, encadré final « En résumé »."""
    def faq_block(m):
        head, inner = m.group(1), m.group(2)
        inner = re.sub(r'<h3[^>]*>(.*?)</h3>\s*((?:(?!<h3)[\s\S])*?)(?=<h3|\Z)',
                       lambda q: f'<details class="faq"><summary>{q.group(1)}</summary><div class="faq__a">{q.group(2).strip()}</div></details>', inner)
        return head + inner
    html = re.sub(r'(<h2 id="questions-frequentes">.*?</h2>)([\s\S]*?)(?=<h2 |\Z)', faq_block, html, count=1)
    html = re.sub(r'(<h2 id="en-resume">[\s\S]*)$', r'<div class="article__summary">\1</div>', html, count=1)
    return html

def article_page(a, all_articles):
    body_html, toc = render_md(a["body_md"])
    faq = faq_from_md(a["body_md"])
    cat_href, _ = CATEGORIES[a["category"]]
    pic, img_url = cover_pic(a["cover"], a["title"], "100vw", loading="eager")
    body_html = enrich_body(body_html)
    related = [x for x in all_articles if x["slug"] != a["slug"] and x["category"] == a["category"]]
    related += [x for x in all_articles if x["slug"] != a["slug"] and x not in related]
    related = related[:3]
    toc_html = "".join(f'<li><a href="#{i}">{H.escape(n)}</a></li>' for i, n in toc)
    tags_html = "".join(f'<span class="chip"><i></i>{H.escape(t)}</span>' for t in a["tags"])
    body = f'''<div class="readbar" aria-hidden="true"><i></i></div>
<section class="hero-page hero-page--article"><div class="hero-page__bg">{pic}</div>{B.RINGS}<div class="container"><nav class="crumbs" aria-label="Fil d'Ariane"><a href="index.html">Accueil</a> <span>/</span> <a href="blog/index.html">Blog</a> <span>/</span> {H.escape(a["category"])}</nav>
<p class="eyebrow eyebrow--light" style="margin-top:28px" data-reveal>{H.escape(a["category"])}</p><h1 class="h1 article__title" data-split>{H.escape(a["title"])}</h1><p class="lead" data-reveal>{H.escape(a["description"])}</p>
<div class="hero-page__meta" data-reveal><span class="strip-item">Publié le <b><time datetime="{a["date"].isoformat()}">{date_fr(a["date"])}</time></b></span><span class="strip-item">Lecture <b>{a["minutes"]} min</b></span><span class="strip-item">Par <b>{AUTEUR}</b></span></div></div></section>
<section class="section"><div class="container article-grid">
<article class="article prose" itemscope itemtype="https://schema.org/BlogPosting">{body_html}
<footer class="article__foot"><p class="mono" style="color:var(--steel-text)">Mots-clés</p><div class="chips">{tags_html}</div><div class="article__share"><span class="mono" style="color:var(--steel-text)">Partager</span><a class="btn btn--ghost btn--sm" href="https://www.linkedin.com/sharing/share-offsite/?url={SITE}blog/{a["slug"]}.html" target="_blank" rel="noopener">LinkedIn</a><a class="btn btn--ghost btn--sm" href="mailto:?subject={H.escape(a["title"], quote=True)}&amp;body={SITE}blog/{a["slug"]}.html">Email</a></div></footer></article>
<aside class="article__aside"><div class="aside-sticky">
<details class="aside-card aside-card--toc" open><summary class="mono aside-card__title">Sommaire</summary><ol class="toc">{toc_html}</ol></details>
<div class="aside-card aside-card--navy"><p class="eyebrow eyebrow--light">Votre projet</p><strong>Un réseau à construire, entretenir ou réhabiliter ?</strong><p>Nos équipes vous répondent avec précision, sur la base de 70 ans de chantiers à Toulouse.</p><a class="btn btn--light btn--sm" href="contact.html">Nous contacter {B.ARROW}</a></div>
<div class="aside-card"><p class="mono aside-card__title">Expertise liée</p><a class="link-arrow" href="{cat_href}"><span>{H.escape(a["category"])}</span>{B.LARROW}</a></div>
</div></aside></div></section>
<section class="section section--tight bg-white"><div class="container"><div class="section-head"><div><p class="eyebrow" data-reveal>À lire ensuite</p><h2 class="h2" data-split>D'autres articles.</h2></div><a class="link-arrow" href="blog/index.html" data-reveal><span>Tout le blog</span>{B.LARROW}</a></div><div class="posts posts--3">{"".join(card(x) for x in related)}</div></div></section>
{B.CTA}'''
    ld = [{
        "@context": "https://schema.org", "@type": "BlogPosting", "headline": a["title"], "description": a["description"],
        "datePublished": a["date"].isoformat(), "dateModified": a["date"].isoformat(), "inLanguage": "fr-FR",
        "author": {"@type": "Organization", "name": "SA LA GARONNE", "url": SITE},
        "publisher": {"@type": "Organization", "name": "SA LA GARONNE", "logo": {"@type": "ImageObject", "url": SITE + "assets/logo/logo-principal-couleur.png"}},
        "image": img_url, "mainEntityOfPage": f"{SITE}blog/{a['slug']}.html", "keywords": ", ".join(a["tags"]),
        "articleSection": a["category"], "wordCount": a["words"],
    }]
    if faq:
        ld.append({"@context": "https://schema.org", "@type": "FAQPage",
                   "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": r}} for q, r in faq]})
    title = a["title"] if len(a["title"]) > 52 else a["title"] + " — SA LA GARONNE"
    extra_head = '  <link rel="alternate" type="application/rss+xml" title="Blog SA LA GARONNE" href="blog/feed.xml">\n'
    B.page(f"{a['slug']}.html", title, a["description"], body, og_image=f"{a['cover']}-{COVERS[a['cover']][-1]}.jpg", crumbs=None, translated=False, subdir="blog/",
           md=f"blog/{a['slug']}.md", extra_head=extra_head + f'  <meta property="article:published_time" content="{a["date"].isoformat()}">\n  <meta property="article:section" content="{H.escape(a["category"], quote=True)}">\n  <meta property="og:type" content="article">\n',
           extra_ld=ld + [B.ld_breadcrumb([("Blog", "blog/index.html"), (a["title"], None)])])
    # copie Markdown pour les LLM
    md_txt = (f"# {a['title']}\n\n> {a['description']}\n\n"
              f"Publié le {date_fr(a['date'])} par {AUTEUR} · Catégorie : {a['category']} · Source : {SITE}blog/{a['slug']}.html\n\n"
              + re.sub(r"\]\((?!https?:)([^)]+)\)", lambda m: f"]({SITE}{m.group(1)})", a["body_md"]) + "\n")
    open(os.path.join(ROOT, "blog", f"{a['slug']}.md"), "w", encoding="utf-8").write(md_txt)

def index_pages(articles):
    n = len(articles); pages = max(1, (n + PAR_PAGE - 1) // PAR_PAGE)
    for p in range(1, pages + 1):
        chunk = articles[(p-1)*PAR_PAGE:p*PAR_PAGE]
        fname = "index.html" if p == 1 else f"page-{p}.html"
        cats = []
        for a in articles:
            if a["category"] not in cats: cats.append(a["category"])
        filters = '<div class="filters"><button class="is-active" data-filter="all">Tous</button>' + "".join(f'<button data-filter="{CATEGORIES[cat][1]}">{H.escape(cat)}</button>' for cat in cats) + '</div>'
        toolbar = f'<div class="blog-toolbar" data-reveal>{filters}<a class="blog-toolbar__rss" href="blog/feed.xml"><svg viewBox="0 0 24 24" fill="currentColor"><circle cx="5" cy="19" r="2"/><path d="M3 10a11 11 0 0 1 11 11h3A14 14 0 0 0 3 7zm0-6a17 17 0 0 1 17 17h3A20 20 0 0 0 3 1z"/></svg>Flux RSS</a></div>'
        top = featured(chunk[0]) if (p == 1 and chunk) else ""
        rest = chunk[1:] if p == 1 else chunk
        cards = "".join(card(a, tag="h2") for a in rest)
        pager = ""
        if pages > 1:
            links = "".join(f'<a class="pager__link{" is-active" if q == p else ""}" href="blog/{"index.html" if q == 1 else f"page-{q}.html"}">{q}</a>' for q in range(1, pages + 1))
            pager = f'<nav class="pager" aria-label="Pagination">{links}</nav>'
        body = f'''{B.hero(["Blog"], "Blog", "Le blog des réseaux d'eau.", "Conseils, méthodes et retours de terrain sur l'assainissement, l'eau potable, la réhabilitation sans tranchée et les chantiers complexes, par les équipes de SA LA GARONNE. Un nouvel article chaque mardi.", [("Articles", str(n)), ("Rythme", "Un article par semaine"), ("Flux", '<a href="blog/feed.xml">RSS</a>')], bg="chantier-hydrocurage-equipe", bgalt="Équipe SA LA GARONNE en intervention")}
<section class="section"><div class="container">{top}{toolbar}<div class="posts posts--index">{cards}</div>{pager}</div></section>
{B.CTA}'''
        title = "Blog — conseils et méthodes réseaux d'eau | SA LA GARONNE" if p == 1 else f"Blog — page {p} | SA LA GARONNE"
        B.page(fname, title, "Le blog de SA LA GARONNE : assainissement, eau potable, réhabilitation sans tranchée, chantiers complexes. Un article par semaine, par nos équipes de Toulouse.",
               body, translated=False, subdir="blog/", md=None,
               extra_head='  <link rel="alternate" type="application/rss+xml" title="Blog SA LA GARONNE" href="blog/feed.xml">\n',
               extra_ld=[B.ld_breadcrumb([("Blog", None)]), {"@context": "https://schema.org", "@type": "Blog", "name": "Blog SA LA GARONNE", "url": SITE + "blog/", "inLanguage": "fr-FR",
                         "publisher": {"@type": "Organization", "name": "SA LA GARONNE", "url": SITE}}])

def feed(articles):
    items = ""
    for a in articles[:20]:
        items += (f"    <item>\n      <title>{H.escape(a['title'])}</title>\n      <link>{SITE}blog/{a['slug']}.html</link>\n      <guid isPermaLink=\"true\">{SITE}blog/{a['slug']}.html</guid>\n"
                  f"      <pubDate>{rfc822(a['date'])}</pubDate>\n      <category>{H.escape(a['category'])}</category>\n      <description>{H.escape(a['description'])}</description>\n    </item>\n")
    xml = (f'<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">\n  <channel>\n    <title>Blog SA LA GARONNE</title>\n    <link>{SITE}blog/</link>\n'
           f'    <atom:link href="{SITE}blog/feed.xml" rel="self" type="application/rss+xml"/>\n    <description>Conseils et méthodes sur les réseaux d\'eau et d\'assainissement, par SA LA GARONNE, Toulouse.</description>\n    <language>fr-FR</language>\n'
           f'    <lastBuildDate>{rfc822(articles[0]["date"]) if articles else rfc822(datetime.date.today())}</lastBuildDate>\n{items}  </channel>\n</rss>\n')
    open(os.path.join(ROOT, "blog", "feed.xml"), "w", encoding="utf-8").write(xml)

def load_all():
    arts = [parse(f) for f in sorted(glob.glob(os.path.join(SRC, "[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]-*.md")))]
    slugs = [a["slug"] for a in arts]
    if len(slugs) != len(set(slugs)): raise SystemExit("slugs en double : " + str([s for s in slugs if slugs.count(s) > 1]))
    arts.sort(key=lambda a: (a["date"], a["file"]), reverse=True)
    return arts

if __name__ == "__main__":
    os.makedirs(os.path.join(ROOT, "blog"), exist_ok=True)
    arts = load_all()
    for a in arts: article_page(a, arts)
    index_pages(arts); feed(arts)
    json.dump([{"slug": a["slug"], "title": a["title"], "date": a["date"].isoformat(), "category": a["category"], "description": a["description"]} for a in arts],
              open(os.path.join(HERE, "blog-index.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"blog : {len(arts)} articles, {max(1,(len(arts)+PAR_PAGE-1)//PAR_PAGE)} page(s) d'index, flux RSS")
