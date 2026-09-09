# -*- coding: utf-8 -*-
"""Fichiers destinés aux LLM et aux moteurs de réponse :
- site-internet/md/<page>.md : version Markdown de chaque page française (contenu de <main>)
- site-internet/llms.txt : index au format llmstxt.org
- site-internet/llms-full.txt : tout le contenu du site en un seul fichier
- site-internet/robots.txt : robots classiques et robots IA explicitement autorisés
Usage : python3 outils-site/llms.py (après build.py, translate.py et blog.py)
"""
import os, re, glob, json, html as H, datetime
from html.parser import HTMLParser
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, "..", "site-internet")
SITE = "https://www.sa-la-garonne.fr/"
PAGES = [("index.html", "Accueil", "Présentation de SA LA GARONNE : expertises, savoir-faire signature, bureau d'études, engagements"),
         ("assainissement.html", "Assainissement", "Construction, renouvellement et réhabilitation des réseaux d'eaux usées et pluviales"),
         ("eau-potable.html", "Adduction d'eau potable", "Pose et renouvellement de conduites, branchements, ouvrages hydrauliques"),
         ("rehabilitation-sans-tranchee.html", "Réhabilitation sans tranchée", "Chemisage, gainage, fraisage robotisé, inspection par robot RIC"),
         ("travaux-complexes.html", "Travaux complexes", "Réseaux en service, grande profondeur, grand diamètre, secteurs très fréquentés"),
         ("realisations.html", "Réalisations", "Chantiers documentés à Toulouse et dans son agglomération"),
         ("entreprise.html", "L'entreprise", "Histoire familiale depuis 1956, valeurs, équipe, bureau d'études, qualifications"),
         ("recrutement.html", "Recrutement", "Métiers recrutés, raisons de nous rejoindre, candidature"),
         ("contact.html", "Contact", "Coordonnées, formulaire et plan d'accès"),
         ("mentions-legales.html", "Mentions légales", "Éditeur, hébergement, données personnelles")]
SKIP = {"script", "style", "svg", "template", "noscript", "form", "button", "select", "textarea", "input", "iframe", "picture", "source", "img"}

class ToMD(HTMLParser):
    """Convertit le contenu de <main> en Markdown lisible."""
    def __init__(self):
        super().__init__(); self.out = []; self.stack = []; self.skip = 0; self.in_main = False; self.cur = []; self.href = None; self.list_depth = 0; self.skip_cls = 0
    def _flush(self, prefix=""):
        t = re.sub(r"\s+", " ", "".join(self.cur)).strip()
        if t: self.out.append(prefix + t)
        self.cur = []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "main": self.in_main = True; return
        if not self.in_main: return
        cls = a.get("class", "")
        if tag in SKIP or self.skip or any(c in cls for c in ("lightbox", "hscroll__progress", "scrub__progress", "loader", "menu", "coupe", "filters", "crumbs", "hero-page__rings", "work__count", "aside-card--navy", "article__share", "pager")):
            self.skip += 1; return
        self.stack.append(tag)
        if tag in ("h1", "h2", "h3", "h4", "p", "li", "blockquote", "figcaption", "dt", "dd", "tr", "article", "section", "div", "footer", "header", "aside", "address"):
            self._flush()
            if tag == "li": self.cur.append("- ")
        if tag in ("ul", "ol"): self._flush(); self.list_depth += 1
        if tag == "a" and a.get("href") and not a["href"].startswith(("#", "mailto:", "tel:", "javascript:")):
            href = a["href"]
            if not href.startswith("http"): href = SITE + re.sub(r"^(\.\./)+", "", href)
            self.href = href; self.cur.append("[")
        if tag == "strong" or tag == "b": self.cur.append("**")
        if tag == "br": self.cur.append(" ")
        if tag == "time": pass
    def handle_endtag(self, tag):
        if tag == "main": self.in_main = False; self._flush(); return
        if not self.in_main: return
        if self.skip:
            if tag in SKIP or True:
                self.skip -= 1 if self.skip else 0
            return
        if tag == "a" and self.href: self.cur.append(f"]({self.href})"); self.href = None
        if tag in ("strong", "b"): self.cur.append("**")
        if tag in ("h1", "h2", "h3", "h4"): self._flush({"h1": "# ", "h2": "## ", "h3": "### ", "h4": "#### "}[tag])
        elif tag in ("p", "li", "blockquote", "figcaption", "dt", "dd", "tr", "address"): self._flush("> " if tag == "blockquote" else "")
        if tag in ("ul", "ol"): self._flush(); self.list_depth -= 1
        if self.stack and self.stack[-1] == tag: self.stack.pop()
    def handle_data(self, d):
        if self.in_main and not self.skip: self.cur.append(d)

def page_to_md(path):
    s = open(path, encoding="utf-8").read()
    title = re.search(r"<title>(.*?)</title>", s, re.S).group(1).strip()
    desc = re.search(r'<meta name="description" content="([^"]*)"', s)
    p = ToMD(); p.feed(s)
    lines, seen = [], set()
    for l in p.out:
        if l in seen and not l.startswith("#"): continue
        seen.add(l); lines.append(l)
    body = "\n\n".join(lines)
    body = re.sub(r"\n{3,}", "\n\n", body)
    return H.unescape(title), H.unescape(desc.group(1)) if desc else "", body

def main():
    os.makedirs(os.path.join(ROOT, "md"), exist_ok=True)
    sections, full = [], []
    for fname, name, hint in PAGES:
        title, desc, body = page_to_md(os.path.join(ROOT, fname))
        md = f"# {title}\n\n> {desc}\n\nSource : {SITE}{fname}\n\n{body}\n"
        open(os.path.join(ROOT, "md", fname[:-5] + ".md"), "w", encoding="utf-8").write(md)
        sections.append(f"- [{name}]({SITE}md/{fname[:-5]}.md): {hint}")
        full.append(md)
    # blog
    idx = os.path.join(HERE, "blog-index.json")
    arts = json.load(open(idx, encoding="utf-8")) if os.path.exists(idx) else []
    blog_lines = [f"- [{a['title']}]({SITE}blog/{a['slug']}.md): {a['description']}" for a in arts]
    for a in arts:
        full.append(open(os.path.join(ROOT, "blog", a["slug"] + ".md"), encoding="utf-8").read())
    today = datetime.date.today().isoformat()
    llms = f"""# SA LA GARONNE

> SA LA GARONNE est une PME familiale de travaux publics fondée à Toulouse en 1956, spécialisée dans les réseaux d'eau et d'assainissement : construction, renouvellement et réhabilitation de réseaux d'assainissement, adduction d'eau potable, réhabilitation sans tranchée (chemisage, gainage, fraisage robotisé) et travaux complexes (réseaux en service, tranchées jusqu'à 7 m, canalisations jusqu'à Ø 2000 mm). 35 collaborateurs, quatre équipes de chantier, un atelier et un bureau d'études intégré (géomètre-dessinateur et chargé d'études). Dirigée par Nicolas Pascual, troisième génération. Robot d'inspection RIC (4K, 360°) breveté en 2018. Zone d'intervention : Toulouse Métropole et son agglomération. Clients : collectivités, exploitants de réseaux, acteurs publics, professionnels du cycle de l'eau.

Site principal en français ; versions anglaise ({SITE}en/) et chinoise ({SITE}zh/) des pages principales. Coordonnées : 63 chemin de Guilhermy, 31100 Toulouse, France · +33 5 62 13 07 80 · contact@lagaronnetp.org. Dernière génération : {today}.

## Pages

{chr(10).join(sections)}

## Blog (un article par semaine)

{chr(10).join(blog_lines) if blog_lines else "- (aucun article)"}
- [Flux RSS]({SITE}blog/feed.xml): derniers articles

## Optional

- [Version anglaise]({SITE}en/): pages principales en anglais
- [中文版]({SITE}zh/): pages principales en chinois simplifié
- [Plan du site]({SITE}sitemap.xml): toutes les URL
- [Contenu complet]({SITE}llms-full.txt): l'ensemble des pages et articles en un seul fichier Markdown
"""
    open(os.path.join(ROOT, "llms.txt"), "w", encoding="utf-8").write(llms)
    open(os.path.join(ROOT, "llms-full.txt"), "w", encoding="utf-8").write(llms + "\n\n---\n\n" + "\n\n---\n\n".join(full))
    robots = f"""# SA LA GARONNE — robots classiques et robots IA bienvenus
User-agent: *
Allow: /

# Robots des assistants et moteurs de réponse IA : accès explicitement autorisé
User-agent: GPTBot
User-agent: OAI-SearchBot
User-agent: ChatGPT-User
User-agent: ClaudeBot
User-agent: Claude-SearchBot
User-agent: anthropic-ai
User-agent: PerplexityBot
User-agent: Google-Extended
User-agent: Applebot-Extended
User-agent: CCBot
User-agent: Bytespider
User-agent: meta-externalagent
Allow: /

Sitemap: {SITE}sitemap.xml
# Index destiné aux LLM : {SITE}llms.txt
"""
    open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8").write(robots)
    print(f"llms : {len(PAGES)} pages Markdown, {len(arts)} articles, llms.txt {len(llms)//1024} Ko, llms-full.txt {os.path.getsize(os.path.join(ROOT,'llms-full.txt'))//1024} Ko")

if __name__ == "__main__":
    main()
