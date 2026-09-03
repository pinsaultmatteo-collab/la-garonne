# -*- coding: utf-8 -*-
"""Assemble les pages internes du site SA LA GARONNE à partir de l'en-tête / pied de page de index.html.
Usage : python3 outils-site/build.py  (à relancer après toute modification de l'en-tête, du pied de page ou de pages.py)"""
import re, os, sys, json, importlib.util
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "site-internet")
index = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()

def between(s, a, b):
    i = s.index(a); j = s.index(b, i) + len(b)
    return s[i:j]

LOADER = between(index, "  <!-- Préchargeur -->", '<div class="page-veil" aria-hidden="true"></div>')
HEADER = between(index, "  <!-- Navigation -->", "  </nav>\n\n  <main id=\"contenu\">").replace("\n\n  <main id=\"contenu\">", "")
FOOTER = between(index, "  <!-- ============ FOOTER ============ -->", "</footer>")
FONTS = between(index, '  <link rel="preload" as="font"', '</noscript>')
ICONS = between(index, '  <link rel="icon" href="favicon.ico" sizes="any">', '<link rel="manifest" href="site.webmanifest">')

ARROW = '<svg class="btn__arrow" viewBox="0 0 18 18" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9h12M10 4l5 5-5 5"/></svg>'
LARROW = '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M2 8h11M9 4l4 4-4 4"/></svg>'
RINGS = '<svg class="hero-page__rings" viewBox="0 0 400 400" fill="none" stroke-width="1.5" aria-hidden="true"><g class="spin"><circle cx="200" cy="200" r="190" stroke="#fff" stroke-dasharray="1100 94"/></g><g class="spin-rev"><circle cx="200" cy="200" r="150" stroke="#0A94F2" stroke-dasharray="880 62"/></g><circle cx="200" cy="200" r="110" stroke="#0669BB"/><g class="spin"><circle cx="200" cy="200" r="70" stroke="#EAF4FC" stroke-dasharray="6 10" opacity=".6"/></g><path d="M200 200h190" stroke="#fff"/><circle cx="200" cy="200" r="4" fill="#0A94F2"/></svg>'
FLOW = '<svg class="cta-band__flow" viewBox="0 0 1440 400" fill="none" stroke-width="2" stroke-linecap="round" preserveAspectRatio="none" aria-hidden="true"><path d="M-20 260C300 120 700 380 1000 200S1400 120 1460 220" stroke="#fff"/><path d="M-20 274C300 134 700 394 1000 214S1400 134 1460 234" stroke="#0A94F2"/><path d="M-20 288C300 148 700 408 1000 228S1400 148 1460 248" stroke="#0669BB"/><path d="M-20 302C300 162 700 422 1000 242S1400 162 1460 262" stroke="#EAF4FC" opacity=".5"/></svg>'

# Pictogrammes (grille 32, trait 1.8, accent cyan unique)
P = {
 "assainissement": '<path class="dr" d="M6 8h20M6 24h20"/><path class="ac dr" d="M8 14c2-2 4-2 6 0s4 2 6 0 4-2 6 0M8 19c2-2 4-2 6 0s4 2 6 0 4-2 6 0"/>',
 "eau": '<path class="dr" d="M16 4c-4 6-9 11-9 16a9 9 0 0 0 18 0c0-5-5-10-9-16z"/><path class="ac dr" d="M12 21a4 4 0 0 0 3 3"/>',
 "sans-tranchee": '<path class="dr" d="M4 8h24"/><path class="dr" d="M6 12h2M11 12h2M16 12h2M21 12h2M26 12h1" opacity=".5"/><rect class="dr" x="5" y="17" width="22" height="10" rx="5"/><path class="ac dr" d="M11 22h9m-3-3 3 3-3 3"/>',
 "profondeur": '<path class="dr" d="M4 6h24"/><path class="ac dr" d="M16 10v16m-4-4 4 4 4-4"/>',
 "chantier": '<rect class="dr" x="5" y="15" width="10" height="8" rx="2"/><path class="dr" d="M4 27h24M15 17l6-8 5 3"/><path class="ac dr" d="M26 12l2 6-4 2"/>',
 "securite": '<path class="dr" d="M16 4l10 4v8c0 6-4 10-10 12C10 26 6 22 6 16V8z"/><path class="ac dr" d="M11 16l3 3 7-7"/>',
 "equipe": '<circle class="dr" cx="12" cy="11" r="4"/><path class="dr" d="M4 26c0-5 3.5-8 8-8s8 3 8 8"/><circle class="ac dr" cx="22" cy="12" r="3"/><path class="ac dr" d="M22 19c3.5 0 6 2.5 6 7"/>',
 "continuite": '<circle class="dr" cx="16" cy="16" r="11"/><path class="ac dr" d="M16 9v7l5 3"/>',
 "inspection": '<circle class="dr" cx="16" cy="19" r="6"/><circle class="ac" cx="16" cy="19" r="1.6" fill="#0A94F2" stroke="none"/><path class="ac dr" d="M10 10a9 9 0 0 1 12 0M13 13a5 5 0 0 1 6 0"/>',
 "chemisage": '<circle class="dr" cx="16" cy="16" r="11"/><circle class="ac dr" cx="16" cy="16" r="6.5"/><circle class="dr" cx="16" cy="16" r="2.5"/>',
 "reseau": '<path class="dr" d="M16 7l10 17H6z"/><circle cx="6" cy="24" r="2.2" fill="#0A94F2" stroke="none"/><circle cx="26" cy="24" r="2.2" fill="currentColor" stroke="none"/><circle cx="16" cy="7" r="2.2" fill="currentColor" stroke="none"/>',
 "regard": '<rect class="dr" x="6" y="6" width="20" height="20" rx="5"/><circle class="dr" cx="16" cy="16" r="5"/><circle cx="16" cy="16" r="1.6" fill="#0A94F2" stroke="none"/>',
 "pompage": '<circle class="dr" cx="13" cy="18" r="7"/><path class="ac dr" d="M20 18h6v-7h-5"/><path class="dr" d="M4 27h22"/>',
 "diametre": '<circle class="dr" cx="16" cy="16" r="11"/><path class="ac dr" d="M8 16h16m-3-3 3 3-3 3M11 13l-3 3 3 3"/>',
 "ville": '<path class="dr" d="M4 27V12l6-4 6 4v15M16 27V16l6-3 6 3v11"/><path class="ac dr" d="M4 27h24"/>',
 "vanne": '<circle class="dr" cx="16" cy="18" r="7"/><path class="dr" d="M16 4v7M11 6h10"/><path class="ac dr" d="M4 18h5M23 18h5"/>',
 "controle": '<path class="dr" d="M6 26V10a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v16"/><path class="dr" d="M4 26h24"/><path class="ac dr" d="M11 18l3 3 7-7"/>',
 "phasage": '<rect class="dr" x="5" y="7" width="22" height="18" rx="3"/><path class="dr" d="M5 13h22M11 4v6M21 4v6"/><path class="ac dr" d="M10 19h6"/>',
 "durabilite": '<path class="dr" d="M16 27c-6 0-10-4-10-9 0-6 5-10 10-14 5 4 10 8 10 14 0 5-4 9-10 9z"/><path class="ac dr" d="M16 27V15m0 4-4-3m4 6 4-3"/>',
}
def picto(name, cls="picto"):
    return f'<svg class="{cls}" viewBox="0 0 32 32">{P[name]}</svg>'

EXPERTISES = [
 ("assainissement.html", "Assainissement", "Réseaux d'eaux usées et pluviales", "assainissement"),
 ("eau-potable.html", "Adduction d'eau potable", "Conduites, branchements, ouvrages", "eau"),
 ("rehabilitation-sans-tranchee.html", "Réhabilitation sans tranchée", "Chemisage, gainage, robotique", "sans-tranchee"),
 ("travaux-complexes.html", "Travaux complexes", "Réseaux en service, grande profondeur", "profondeur"),
]

def related(current):
    items = [e for e in EXPERTISES if e[0] != current]
    html = '<section class="section section--tight bg-white"><div class="container"><div class="section-head"><div><p class="eyebrow" data-reveal>Autres expertises</p><h2 class="h2" data-split>Un savoir-faire complet sur les réseaux d\'eau.</h2></div></div><div class="related stagger">'
    for href, name, sub, ico in items:
        html += f'<a href="{href}">{picto(ico)}<span class="mono">{sub}</span><strong>{name}</strong></a>'
    return html + '</div></div></section>'

CTA = f'''<section class="section"><div class="container"><div class="cta-band" data-reveal="scale">{FLOW}<div class="cta-band__grid"><div><p class="eyebrow eyebrow--light">Contact</p><h2 class="h2">Un réseau à construire, entretenir ou réhabiliter ?</h2><p class="lead">Parlons de votre projet. Nos équipes vous répondent avec précision, sur la base de 70 ans de chantiers.</p></div><div class="cta-band__side"><span class="mono">Téléphone</span><span class="cta-band__contact"><a href="tel:+33562130780">+33 5 62 13 07 80</a></span><span class="mono">Email</span><span class="cta-band__contact"><a href="mailto:contact@lagaronnetp.org">contact@lagaronnetp.org</a></span><a class="btn btn--light" href="contact.html" style="margin-top:10px">Nous contacter {ARROW}</a></div></div></div></div></section>'''

def pic(name, sizes_w, alt, sizes="100vw", loading="lazy", cls=""):
    ws = sorted(sizes_w)
    from PIL import Image as _I
    _w, _h = _I.open(os.path.join(ROOT, f"assets/img/{name}-{ws[-1]}.jpg")).size
    webp = ", ".join(f"assets/img/{name}-{w}.webp {w}w" for w in ws)
    jpg = ", ".join(f"assets/img/{name}-{w}.jpg {w}w" for w in ws)
    return f'<picture><source type="image/webp" srcset="{webp}" sizes="{sizes}"><img src="assets/img/{name}-{ws[-1]}.jpg" srcset="{jpg}" sizes="{sizes}" alt="{alt}" loading="{loading}" width="{_w}" height="{_h}"{(" class=" + chr(34) + cls + chr(34)) if cls else ""}></picture>'

def hero(crumbs, eyebrow, title, lead, meta, bg=None, bgalt=""):
    SIZES = {"equipe-reunion-inspection": [768,1280,1600], "collecteur-visitable-profondeur": [536], "aep-raccordement-fonte": [768], "tranchee-blindee-monument": [529], "chantier-hydrocurage-equipe": [480,768,1024,1280,1920], "chantier-capitole-engins": [480,768,1024,1280,1920], "chantier-tranchee-centre-ville": [480,768,1024,1280,1920]}
    bgh = f'<div class="hero-page__bg">{pic(bg, SIZES.get(bg, [480,768,1024,1280,1920]), bgalt, loading="eager")}</div>' if bg else ""
    crumb_html = ' <span>/</span> '.join(crumbs)
    meta_html = "".join(f'<span class="strip-item">{k} <b>{v}</b></span>' for k, v in meta)
    return f'''<section class="hero-page">{bgh}{RINGS}<div class="container"><nav class="crumbs" aria-label="Fil d'Ariane"><a href="index.html">Accueil</a> <span>/</span> {crumb_html}</nav><p class="eyebrow eyebrow--light" style="margin-top:28px" data-reveal>{eyebrow}</p><h1 class="h1" data-split>{title}</h1><p class="lead" data-reveal>{lead}</p><div class="hero-page__meta" data-reveal>{meta_html}</div></div></section>'''

def band(name, alt, sizes_w, cap_mono, cap_title):
    from PIL import Image as _I
    _w, _h = _I.open(os.path.join(ROOT, f"assets/img/{name}-{max(sizes_w)}.jpg")).size
    ws = sorted(sizes_w)
    return f'<div class="band"><picture><source type="image/webp" srcset="{", ".join(f"assets/img/{name}-{w}.webp {w}w" for w in ws)}" sizes="100vw"><img src="assets/img/{name}-{ws[-1]}.jpg" srcset="{", ".join(f"assets/img/{name}-{w}.jpg {w}w" for w in ws)}" sizes="100vw" alt="{alt}" loading="lazy" width="{_w}" height="{_h}" data-parallax="0.12"></picture><div class="band__cap"><span class="mono">{cap_mono}</span><strong class="display" style="font-size:clamp(1.6rem,3vw,2.6rem)">{cap_title}</strong></div></div>'

def services(items):
    html = '<div class="services stagger">'
    for i, (ico, title, text) in enumerate(items, 1):
        html += f'<div class="service"><span class="mono">{i:02d}</span>{picto(ico)}<div><strong>{title}</strong><p style="margin-top:8px">{text}</p></div></div>'
    return html + '</div>'

def process(items):
    html = '<div class="process stagger">'
    for i, (ico, title, text) in enumerate(items, 1):
        html += f'<div class="process__item"><span class="mono">Étape {i:02d}</span><strong>{title}</strong><p>{text}</p>{picto(ico)}</div>'
    return html + '</div>'


def lang_links(html, filename, prefix=""):
    """Fait pointer chaque drapeau vers la même page dans l'autre langue."""
    def fix(m):
        block = m.group(0)
        block = re.sub(r'href="(?:\.\./)*index\.html"', f'href="{prefix}{filename}"', block, count=1)
        block = re.sub(r'href="(?:\.\./)*en/index\.html"', f'href="{prefix}en/{filename}"', block, count=1)
        block = re.sub(r'href="(?:\.\./)*zh/index\.html"', f'href="{prefix}zh/{filename}"', block, count=1)
        return block
    return re.sub(r'<div class="langs[^"]*"[^>]*>.*?</div>', fix, html, flags=re.S)

SITE = "https://www.sa-la-garonne.fr/"
def ld_breadcrumb(crumbs):
    items = [{"@type": "ListItem", "position": 1, "name": "Accueil", "item": SITE}]
    for i, (name, url) in enumerate(crumbs, 2):
        it = {"@type": "ListItem", "position": i, "name": name}
        if url: it["item"] = SITE + url
        items.append(it)
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items}
def ld_service(name, desc, url):
    return {"@context": "https://schema.org", "@type": "Service", "name": name, "description": desc, "url": SITE + url, "serviceType": name,
            "provider": {"@type": "GeneralContractor", "name": "SA LA GARONNE", "url": SITE, "telephone": "+33562130780",
                         "address": {"@type": "PostalAddress", "streetAddress": "63 chemin de Guilhermy", "postalCode": "31100", "addressLocality": "Toulouse", "addressCountry": "FR"}},
            "areaServed": {"@type": "City", "name": "Toulouse"}}
def page(filename, title, description, body, og_image="chantier-capitole-engins-1280.jpg", crumbs=None, service=None):
    lds = []
    if crumbs: lds.append(ld_breadcrumb(crumbs))
    if service: lds.append(ld_service(service, description, filename))
    LD = "".join(f'<script type="application/ld+json">{json.dumps(l, ensure_ascii=False)}</script>\n' for l in lds)
    ALT = (f'  <link rel="alternate" hreflang="fr" href="{SITE}{filename}">\n'
           f'  <link rel="alternate" hreflang="en" href="{SITE}en/{filename}">\n'
           f'  <link rel="alternate" hreflang="zh-Hans" href="{SITE}zh/{filename}">\n'
           f'  <link rel="alternate" hreflang="x-default" href="{SITE}{filename}">\n')
    header = lang_links(HEADER, filename)
    html = f'''<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="https://www.sa-la-garonne.fr/{filename}">
{ALT}
  <meta property="og:type" content="website">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:image" content="https://www.sa-la-garonne.fr/assets/img/{og_image}">
  <meta property="og:locale" content="fr_FR">
  <meta name="theme-color" content="#052F56">
{ICONS}
{FONTS}
{LD}</head>
<body>
  <a class="skip" href="#contenu">Aller au contenu</a>

{LOADER}

{header}

  <main id="contenu">
{body}
  </main>

{FOOTER}

  <script src="js/main.js"></script>
</body>
</html>
'''
    open(os.path.join(ROOT, filename), "w", encoding="utf-8").write(html)
    print("écrit", filename, len(html))

# Charge les contenus de pages
spec = importlib.util.spec_from_file_location("pages", os.path.join(os.path.dirname(__file__), "pages.py"))
pages = importlib.util.module_from_spec(spec)
pages.__dict__.update(dict(page=page, hero=hero, band=band, services=services, process=process, related=related, CTA=CTA, ARROW=ARROW, LARROW=LARROW, picto=picto, pic=pic, RINGS=RINGS, FLOW=FLOW))
spec.loader.exec_module(pages)
